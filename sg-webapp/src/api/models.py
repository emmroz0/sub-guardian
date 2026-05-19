from django.contrib.auth.models import User
from django.db import models


class SiteEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="site_events")
    url = models.CharField()
    tab_id = models.IntegerField()
    event_type = models.CharField(
        max_length=10,
        choices=[
            ("open", "Open"),
            ("close", "Close"),
        ],
    )
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
            models.Index(fields=["user", "timestamp"]),
        ]

    def __str__(self):
        return f"{self.event_type} {self.url} (tab={self.tab_id}, {self.user.username})"


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    name = models.CharField(max_length=255)
    url = models.CharField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    billing_cycle = models.CharField(
        max_length=20,
        choices=[
            ("monthly", "Monthly"),
            ("yearly", "Yearly"),
            ("quarterly", "Quarterly"),
        ],
        default="monthly",
    )
    next_billing_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class Session(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sessions"
    )
    subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="sessions",
    )
    url = models.CharField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)
    duration_seconds = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-started_at"]
        indexes = [
            models.Index(fields=["user", "subscription", "ended_at"]),
        ]

    def __str__(self):
        return f"{self.subscription} session ({self.user.username})"
