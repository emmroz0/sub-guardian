from django.contrib import admin

from .models import Subscription


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
