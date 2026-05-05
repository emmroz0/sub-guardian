from django.contrib.auth.models import User
from django.db import models


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
