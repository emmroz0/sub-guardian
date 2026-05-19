from datetime import timedelta

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from django.db.models.functions import TruncDate
from django.shortcuts import redirect, render
from django.utils import timezone

from api.models import Session, SiteEvent, Subscription


def home(request):
    context = {}

    if request.user.is_authenticated:
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)

        subscriptions = Subscription.objects.filter(
            user=request.user, is_active=True
        )
        context["subscriptions"] = subscriptions
        context["active_subscriptions_count"] = subscriptions.count()

        total_monthly = 0
        for sub in subscriptions:
            if sub.billing_cycle == "monthly":
                total_monthly += sub.cost
            elif sub.billing_cycle == "quarterly":
                total_monthly += sub.cost / 3
            elif sub.billing_cycle == "yearly":
                total_monthly += sub.cost / 12
        context["total_monthly_cost"] = round(total_monthly, 2)

        recent_sessions = Session.objects.filter(
            user=request.user,
            started_at__gte=thirty_days_ago,
        ).select_related("subscription").order_by("-started_at")[:20]
        context["recent_sessions"] = recent_sessions

        total_seconds = Session.objects.filter(
            user=request.user,
            started_at__gte=thirty_days_ago,
            ended_at__isnull=False,
        ).aggregate(total=Sum("duration_seconds"))["total"] or 0
        context["total_tracked_hours"] = round(total_seconds / 3600, 1)

        time_per_sub = (
            Session.objects.filter(
                user=request.user,
                started_at__gte=thirty_days_ago,
                ended_at__isnull=False,
            )
            .values("subscription__name")
            .annotate(total_seconds=Sum("duration_seconds"))
            .order_by("-total_seconds")
        )
        context["time_per_subscription"] = time_per_sub

        fourteen_days_ago = now - timedelta(days=14)
        daily_usage = (
            Session.objects.filter(
                user=request.user,
                started_at__gte=fourteen_days_ago,
                ended_at__isnull=False,
            )
            .annotate(date=TruncDate("started_at"))
            .values("date")
            .annotate(total_seconds=Sum("duration_seconds"))
            .order_by("date")
        )
        context["daily_usage"] = daily_usage

        context["visit_count"] = SiteEvent.objects.filter(
            user=request.user,
            event_type="open",
            timestamp__gte=thirty_days_ago,
        ).count()

    return render(request, "dashboard/home.html", context)


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = UserCreationForm()

    return render(request, "registration/sign_up.html", {"form": form})
