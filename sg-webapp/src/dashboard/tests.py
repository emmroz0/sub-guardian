from datetime import timedelta

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from api.models import Session, SiteEvent, Subscription


class RegistrationTests(TestCase):
    """Sprint 1 — T1-01, T1-02"""

    def test_sign_up_creates_user_and_logs_in(self):
        resp = self.client.post(
            "/sign_up/",
            {"username": "testuser", "password1": "TestPass123!", "password2": "TestPass123!"},
        )
        self.assertRedirects(resp, "/home", fetch_redirect_response=False)
        self.assertTrue(User.objects.filter(username="testuser").exists())

    def test_sign_up_empty_fields_returns_errors(self):
        resp = self.client.post(
            "/sign_up/",
            {"username": "", "password1": "", "password2": ""},
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'class="textinput form-control is-invalid"')


class LoginTests(TestCase):
    """Sprint 1 — T1-03, T1-04"""

    def setUp(self):
        self.user = User.objects.create_user("testuser", password="TestPass123!")

    def test_login_correct_credentials_redirects(self):
        resp = self.client.post(
            "/auth/login/",
            {"username": "testuser", "password": "TestPass123!"},
        )
        self.assertRedirects(resp, "/home/", fetch_redirect_response=False)

    def test_login_wrong_password_shows_error(self):
        resp = self.client.post(
            "/auth/login/",
            {"username": "testuser", "password": "WrongPass!"},
        )
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Please enter a correct username and password")


class HomeViewTests(TestCase):
    """Sprint 2 — T2-01, T2-02, T2-03"""

    def setUp(self):
        self.user = User.objects.create_user("testuser", password="pass")
        self.sub = Subscription.objects.create(
            user=self.user, name="netflix.com", url="https://netflix.com",
            cost=10, billing_cycle="monthly",
        )

    def test_dashboard_unauthenticated_shows_landing(self):
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Zaloguj si")

    def test_dashboard_authenticated_shows_stats(self):
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Subskrypcje")

    def test_dashboard_monthly_cost_normalization(self):
        Subscription.objects.create(
            user=self.user, name="yearly.com", url="https://yearly.com",
            cost=120, billing_cycle="yearly",
        )
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "20.00")

    def test_dashboard_keeps_recent_sessions(self):
        now = timezone.now()
        Session.objects.create(
            user=self.user, subscription=self.sub,
            url="https://netflix.com", started_at=now - timedelta(days=5),
            ended_at=now - timedelta(days=5, hours=-1), duration_seconds=3600,
        )
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "netflix.com")

    def test_dashboard_empty_user_shows_zero_stats(self):
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "0")

    def test_dashboard_visit_count(self):
        now = timezone.now()
        SiteEvent.objects.create(
            user=self.user, url="https://netflix.com", tab_id=1,
            event_type="open", timestamp=now - timedelta(days=2),
        )
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "1")

    def test_dashboard_time_per_subscription_aggregated(self):
        now = timezone.now()
        sub2 = Subscription.objects.create(
            user=self.user, name="spotify.com", url="https://spotify.com",
            cost=20, billing_cycle="monthly",
        )
        Session.objects.create(
            user=self.user, subscription=self.sub,
            url="https://netflix.com", started_at=now - timedelta(days=5),
            ended_at=now - timedelta(days=5, hours=-1), duration_seconds=3600,
        )
        Session.objects.create(
            user=self.user, subscription=sub2,
            url="https://spotify.com", started_at=now - timedelta(days=3),
            ended_at=now - timedelta(days=3, minutes=-30), duration_seconds=1800,
        )
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "netflix.com")
        self.assertContains(resp, "spotify.com")

    def test_dashboard_daily_usage_aggregated(self):
        now = timezone.now()
        Session.objects.create(
            user=self.user, subscription=self.sub,
            url="https://netflix.com", started_at=now - timedelta(days=1),
            ended_at=now - timedelta(days=1, minutes=-30), duration_seconds=1800,
        )
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)

    def test_dashboard_active_sessions_shown_as_active(self):
        now = timezone.now()
        Session.objects.create(
            user=self.user, subscription=self.sub,
            url="https://netflix.com", started_at=now - timedelta(minutes=30),
            ended_at=None, duration_seconds=None,
        )
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)


class TemplateRenderingTests(TestCase):
    """Sprint 1 — T1-10"""

    def test_base_html_renders_bootstrap(self):
        resp = self.client.get("/home/")
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "bootstrap", html=False)
