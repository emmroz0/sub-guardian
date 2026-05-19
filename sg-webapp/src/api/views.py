import json
import logging

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

from .models import Subscription
from . import session_manager

logger = logging.getLogger(__name__)

_EVENT_FIELDS = ["url", "tab_id", "event_type", "timestamp"]


def _validate_event_data(data):
    for field in _EVENT_FIELDS:
        if field not in data:
            return {"error": f"Missing field: {field}"}
    if data["event_type"] not in ("open", "close"):
        return {"error": "event_type must be 'open' or 'close'"}
    return None


def health_check(request):
    return JsonResponse({"status": "ok"})


def auth_status(request):
    if request.user.is_authenticated:
        return JsonResponse({"authenticated": True, "username": request.user.username})
    else:
        return JsonResponse({"authenticated": False})


@login_required
def subscription_list(request):
    subscriptions = Subscription.objects.filter(
        user=request.user, is_active=True
    ).values("id", "name", "url", "cost", "billing_cycle", "next_billing_date")
    return JsonResponse({"subscriptions": list(subscriptions)})


@require_POST
@login_required
def create_subscription(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    name = data.get("name", "").strip()
    if not name:
        return JsonResponse({"error": "name is required"}, status=400)

    sub = Subscription.objects.create(
        user=request.user,
        name=name,
        url=data.get("url", ""),
        cost=data.get("cost", 0),
        billing_cycle=data.get("billing_cycle", "monthly"),
        next_billing_date=data.get("next_billing_date"),
    )
    return JsonResponse(
        {
            "id": sub.id,
            "name": sub.name,
            "url": sub.url,
            "cost": str(sub.cost),
            "billing_cycle": sub.billing_cycle,
            "next_billing_date": sub.next_billing_date,
        },
        status=201,
    )


@require_http_methods(["DELETE"])
@login_required
def delete_subscription(request, id):
    try:
        sub = Subscription.objects.get(id=id, user=request.user)
    except Subscription.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
    sub.is_active = False
    sub.save()
    return JsonResponse({"status": "deleted"})


@require_POST
@login_required
def create_site_event(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    error = _validate_event_data(data)
    if error:
        return JsonResponse(error, status=400)

    try:
        if data["event_type"] == "open":
            session_manager.process_open_event(
                request.user, data["url"], int(data["tab_id"]), data["timestamp"]
            )
        else:
            session_manager.process_close_event(
                request.user, data["url"], int(data["tab_id"]), data["timestamp"]
            )
        return JsonResponse({"status": "created"}, status=201)
    except Exception as e:
        logger.error("Failed to process site event: %s", e)
        return JsonResponse({"error": "Failed to process event"}, status=500)


@require_POST
@login_required
def create_site_events_batch(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    events_data = data.get("events", [])
    if not isinstance(events_data, list):
        return JsonResponse({"error": "'events' must be a list"}, status=400)

    errors = []
    for i, event_data in enumerate(events_data):
        error = _validate_event_data(event_data)
        if error:
            errors.append({"index": i, "error": error["error"]})
            continue

        try:
            if event_data["event_type"] == "open":
                session_manager.process_open_event(
                    request.user,
                    event_data["url"],
                    int(event_data["tab_id"]),
                    event_data["timestamp"],
                )
            else:
                session_manager.process_close_event(
                    request.user,
                    event_data["url"],
                    int(event_data["tab_id"]),
                    event_data["timestamp"],
                )
        except Exception as e:
            logger.error("Failed to process site event at index %d: %s", i, e)
            errors.append({"index": i, "error": str(e)})

    return JsonResponse(
        {"processed": len(events_data) - len(errors), "errors": errors},
        status=201 if len(errors) == 0 else 400,
    )
