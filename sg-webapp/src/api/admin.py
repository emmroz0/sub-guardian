from django.contrib import admin

from .models import Session, SiteEvent, Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "user",
        "cost",
        "billing_cycle",
        "is_active",
        "next_billing_date",
    ]
    list_filter = ["is_active", "billing_cycle", "user"]
    search_fields = ["name", "url", "user__username"]


@admin.register(SiteEvent)
class SiteEventAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "url",
        "tab_id",
        "event_type",
        "timestamp",
        "created_at",
    ]
    list_filter = ["event_type", "user", "timestamp"]
    search_fields = ["url", "user__username"]
    ordering = ["-timestamp"]


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = [
        "user",
        "subscription",
        "url",
        "started_at",
        "ended_at",
        "duration_seconds",
    ]
    list_filter = ["subscription", "user", "started_at"]
    search_fields = ["url", "user__username"]
    ordering = ["-started_at"]
