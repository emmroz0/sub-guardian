from django.urls import path

from . import views

urlpatterns = [
    path("health/", views.health_check, name="health_check"),
    path("auth_status/", views.auth_status, name="auth_status"),
    path("subscriptions/", views.subscription_list, name="subscription_list"),
]
