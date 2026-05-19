from django.urls import path

from . import views

urlpatterns = [
    path("health/", views.health_check, name="health_check"),
    path("auth_status/", views.auth_status, name="auth_status"),
    path("subscriptions/", views.subscription_list, name="subscription_list"),
    path("subscriptions/add/", views.create_subscription, name="create_subscription"),
    path("subscriptions/<int:id>/", views.delete_subscription, name="delete_subscription"),
    path("events/", views.create_site_events_batch, name="create_site_events_batch"),
    path("events/single/", views.create_site_event, name="create_site_event"),
]
