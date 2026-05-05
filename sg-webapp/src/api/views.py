import logging

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Subscription

logger = logging.getLogger(__name__)


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
