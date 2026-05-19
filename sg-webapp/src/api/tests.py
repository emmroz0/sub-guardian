from datetime import datetime, timedelta, timezone as tz

from django.contrib.auth.models import User
from django.test import TestCase

from . import session_manager
from .models import Session, SiteEvent, Subscription


class SessionManagerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("testuser", password="pass")
        self.sub = Subscription.objects.create(
            user=self.user,
            name="netflix.com",
            url="https://netflix.com",
            cost=10,
            billing_cycle="monthly",
        )

    def _ts(self, minutes_ago=0):
        return datetime.now(tz.utc) - timedelta(minutes=minutes_ago)

    def _open_event(self, url, tab_id, ts=None):
        return SiteEvent.objects.create(
            user=self.user,
            url=url,
            tab_id=tab_id,
            event_type="open",
            timestamp=ts or self._ts(),
        )

    def _close_event(self, url, tab_id, ts=None):
        return SiteEvent.objects.create(
            user=self.user,
            url=url,
            tab_id=tab_id,
            event_type="close",
            timestamp=ts or self._ts(),
        )

    # --- process_open_event ---

    def test_open_creates_session(self):
        ts = self._ts()
        s = session_manager.process_open_event(self.user, "https://netflix.com", 1, ts)
        self.assertIsNotNone(s)
        self.assertEqual(s.subscription, self.sub)
        self.assertEqual(s.started_at, ts)
        self.assertIsNone(s.ended_at)

    def test_open_no_session_for_unmatched_url(self):
        s = session_manager.process_open_event(self.user, "https://unknown.com", 1, self._ts())
        self.assertIsNone(s)

    def test_open_does_not_duplicate_session(self):
        ts = self._ts()
        session_manager.process_open_event(self.user, "https://netflix.com", 1, ts)
        s2 = session_manager.process_open_event(self.user, "https://netflix.com", 2, ts)
        self.assertIsNone(s2)
        self.assertEqual(Session.objects.count(), 1)

    # --- process_close_event ---

    def test_close_ends_session_when_last_tab(self):
        ts = self._ts(10)
        session_manager.process_open_event(self.user, "https://netflix.com", 1, ts)
        close_ts = self._ts()
        s = session_manager.process_close_event(self.user, "https://netflix.com", 1, close_ts)
        self.assertIsNotNone(s)
        self.assertEqual(s.ended_at, close_ts)
        self.assertIsNotNone(s.duration_seconds)

    def test_close_does_not_end_session_when_other_tab_open(self):
        session_manager.process_open_event(self.user, "https://netflix.com", 1, self._ts(10))
        session_manager.process_open_event(self.user, "https://netflix.com", 2, self._ts(9))
        s = session_manager.process_close_event(self.user, "https://netflix.com", 1, self._ts())
        self.assertIsNone(s)
        active = Session.objects.get(subscription=self.sub, ended_at__isnull=True)
        self.assertIsNotNone(active)

    def test_close_noop_when_no_active_session(self):
        s = session_manager.process_close_event(self.user, "https://netflix.com", 1, self._ts())
        self.assertIsNone(s)

    def test_close_noop_for_unmatched_url(self):
        s = session_manager.process_close_event(self.user, "https://unknown.com", 1, self._ts())
        self.assertIsNone(s)

    # --- tab switching ---

    def test_switching_to_new_sub_closes_previous_session(self):
        sub2 = Subscription.objects.create(
            user=self.user,
            name="youtube.com",
            url="https://youtube.com",
            cost=0,
            billing_cycle="monthly",
        )
        session_manager.process_open_event(
            self.user, "https://netflix.com", 1, self._ts(10)
        )
        session_manager.process_open_event(
            self.user, "https://youtube.com", 1, self._ts()
        )
        netflix_session = Session.objects.get(subscription=self.sub)
        self.assertIsNotNone(netflix_session.ended_at)
        youtube_session = Session.objects.get(subscription=sub2)
        self.assertIsNone(youtube_session.ended_at)

    def test_switching_to_same_site_keeps_session(self):
        session_manager.process_open_event(
            self.user, "https://netflix.com/browse", 1, self._ts(10)
        )
        s2 = session_manager.process_open_event(
            self.user, "https://netflix.com/movie/123", 1, self._ts()
        )
        self.assertIsNone(s2)
        self.assertEqual(Session.objects.count(), 1)
        self.assertIsNone(Session.objects.first().ended_at)

    def test_multiple_tabs_different_subs_close_correctly(self):
        sub2 = Subscription.objects.create(
            user=self.user,
            name="youtube.com",
            url="https://youtube.com",
            cost=0,
            billing_cycle="monthly",
        )
        session_manager.process_open_event(
            self.user, "https://netflix.com", 1, self._ts(10)
        )
        session_manager.process_open_event(
            self.user, "https://youtube.com", 2, self._ts(9)
        )
        s = session_manager.process_close_event(
            self.user, "https://youtube.com", 2, self._ts()
        )
        self.assertIsNotNone(s)
        self.assertIsNotNone(s.ended_at)
        netflix_session = Session.objects.get(subscription=self.sub)
        self.assertIsNone(netflix_session.ended_at)

    # --- get_site_name ---

    def test_get_site_name(self):
        self.assertEqual(
            session_manager.get_site_name("https://www.netflix.com/movie"),
            "netflix.com",
        )
        self.assertEqual(
            session_manager.get_site_name("https://youtube.com"),
            "youtube.com",
        )
        self.assertEqual(
            session_manager.get_site_name("http://localhost:8000/home/"),
            "localhost",
        )

    # --- count_open_tabs_for_subscription ---

    def test_count_open_tabs(self):
        self.assertEqual(
            session_manager.count_open_tabs_for_subscription(self.user, self.sub), 0
        )
        self._open_event("https://netflix.com", 1, self._ts(10))
        self.assertEqual(
            session_manager.count_open_tabs_for_subscription(self.user, self.sub), 1
        )
        self._open_event("https://netflix.com", 2, self._ts(9))
        self.assertEqual(
            session_manager.count_open_tabs_for_subscription(self.user, self.sub), 2
        )
        self._close_event("https://netflix.com", 1, self._ts())
        self.assertEqual(
            session_manager.count_open_tabs_for_subscription(self.user, self.sub), 1
        )


class SessionViaApiTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("testuser", password="pass")
        Subscription.objects.create(
            user=self.user,
            name="netflix.com",
            url="https://netflix.com",
            cost=10,
            billing_cycle="monthly",
        )
        self.client.login(username="testuser", password="pass")

    def test_post_open_event_creates_session(self):
        resp = self.client.post(
            "/api/events/single/",
            {
                "url": "https://netflix.com",
                "tab_id": 1,
                "event_type": "open",
                "timestamp": datetime.now(tz.utc).isoformat(),
            },
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Session.objects.count(), 1)

    def test_post_close_event_ends_session(self):
        self.client.post(
            "/api/events/single/",
            {
                "url": "https://netflix.com",
                "tab_id": 1,
                "event_type": "open",
                "timestamp": datetime.now(tz.utc).isoformat(),
            },
            content_type="application/json",
        )
        close_ts = datetime.now(tz.utc).isoformat()
        resp = self.client.post(
            "/api/events/single/",
            {
                "url": "https://netflix.com",
                "tab_id": 1,
                "event_type": "close",
                "timestamp": close_ts,
            },
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 201)
        session = Session.objects.first()
        self.assertIsNotNone(session.ended_at)

    def test_batch_events_create_and_close_session(self):
        self.client.post(
            "/api/events/",
            {
                "events": [
                    {
                        "url": "https://netflix.com",
                        "tab_id": 1,
                        "event_type": "open",
                        "timestamp": datetime.now(tz.utc).isoformat(),
                    },
                ]
            },
            content_type="application/json",
        )
        self.assertEqual(Session.objects.count(), 1)

    def test_batch_close_last_tab_ends_session(self):
        self.client.post(
            "/api/events/",
            {
                "events": [
                    {
                        "url": "https://netflix.com",
                        "tab_id": 1,
                        "event_type": "open",
                        "timestamp": datetime.now(tz.utc).isoformat(),
                    },
                ]
            },
            content_type="application/json",
        )
        self.client.post(
            "/api/events/",
            {
                "events": [
                    {
                        "url": "https://netflix.com",
                        "tab_id": 1,
                        "event_type": "close",
                        "timestamp": datetime.now(tz.utc).isoformat(),
                    },
                ]
            },
            content_type="application/json",
        )
        session = Session.objects.first()
        self.assertIsNotNone(session.ended_at)


class SubscriptionApiTests(TestCase):
    """Sprint 1 — T1-05, T1-06, T1-07, T1-08 + Sprint 4 — T4-01, T4-02"""

    def setUp(self):
        self.user = User.objects.create_user("testuser", password="pass")
        self.other_user = User.objects.create_user("other", password="pass")
        self.client.login(username="testuser", password="pass")

    def test_create_subscription_via_api(self):
        resp = self.client.post(
            "/api/subscriptions/add/",
            {"name": "netflix.com", "url": "https://netflix.com", "cost": 59.00, "billing_cycle": "monthly"},
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Subscription.objects.count(), 1)
        self.assertEqual(Subscription.objects.first().name, "netflix.com")

    def test_create_subscription_empty_name_rejected(self):
        resp = self.client.post(
            "/api/subscriptions/add/",
            {"name": "", "url": "https://netflix.com", "cost": 10},
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(Subscription.objects.count(), 0)

    def test_subscription_list_empty_for_new_user(self):
        resp = self.client.get("/api/subscriptions/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["subscriptions"], [])

    def test_subscription_list_isolated_per_user(self):
        Subscription.objects.create(
            user=self.user, name="netflix.com", url="https://netflix.com",
            cost=10, billing_cycle="monthly",
        )
        Subscription.objects.create(
            user=self.other_user, name="spotify.com", url="https://spotify.com",
            cost=5, billing_cycle="monthly",
        )
        resp = self.client.get("/api/subscriptions/")
        subs = resp.json()["subscriptions"]
        self.assertEqual(len(subs), 1)
        self.assertEqual(subs[0]["name"], "netflix.com")

    def test_delete_subscription_soft(self):
        sub = Subscription.objects.create(
            user=self.user, name="netflix.com", url="https://netflix.com",
            cost=10, billing_cycle="monthly",
        )
        resp = self.client.delete(f"/api/subscriptions/{sub.id}/")
        self.assertEqual(resp.status_code, 200)
        sub.refresh_from_db()
        self.assertFalse(sub.is_active)

    def test_delete_other_users_subscription_forbidden(self):
        sub = Subscription.objects.create(
            user=self.other_user, name="spotify.com", url="https://spotify.com",
            cost=5, billing_cycle="monthly",
        )
        resp = self.client.delete(f"/api/subscriptions/{sub.id}/")
        self.assertEqual(resp.status_code, 404)
        sub.refresh_from_db()
        self.assertTrue(sub.is_active)


class AuthAndHealthTests(TestCase):
    """Sprint 1—2 — health, auth_status"""

    def setUp(self):
        self.user = User.objects.create_user("testuser", password="pass")

    def test_health_endpoint_returns_ok(self):
        resp = self.client.get("/api/health/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {"status": "ok"})

    def test_auth_status_authenticated(self):
        self.client.login(username="testuser", password="pass")
        resp = self.client.get("/api/auth_status/")
        data = resp.json()
        self.assertTrue(data["authenticated"])
        self.assertEqual(data["username"], "testuser")

    def test_auth_status_unauthenticated(self):
        resp = self.client.get("/api/auth_status/")
        data = resp.json()
        self.assertFalse(data["authenticated"])


class EventApiAdditionalTests(TestCase):
    """Sprint 3 — T3-17, T3-18"""

    def setUp(self):
        self.user = User.objects.create_user("testuser", password="pass")
        Subscription.objects.create(
            user=self.user, name="netflix.com", url="https://netflix.com",
            cost=10, billing_cycle="monthly",
        )

    def test_post_event_unauthenticated_returns_403(self):
        resp = self.client.post(
            "/api/events/single/",
            {"url": "https://netflix.com", "tab_id": 1, "event_type": "open", "timestamp": "2026-05-01T12:00:00Z"},
            content_type="application/json",
        )
        self.assertIn(resp.status_code, (302, 403))

    def test_post_event_missing_event_type_field_rejected(self):
        self.client.login(username="testuser", password="pass")
        resp = self.client.post(
            "/api/events/single/",
            {"url": "https://netflix.com", "tab_id": 1, "timestamp": "2026-05-01T12:00:00Z"},
            content_type="application/json",
        )
        self.assertIn(resp.status_code, (400, 500))

    def test_post_event_invalid_event_type_rejected(self):
        self.client.login(username="testuser", password="pass")
        resp = self.client.post(
            "/api/events/single/",
            {"url": "https://netflix.com", "tab_id": 1, "event_type": "refresh", "timestamp": "2026-05-01T12:00:00Z"},
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 400)


class EventApiBatchTests(TestCase):
    """Sprint 3 — T3-19, T3-20"""

    def setUp(self):
        self.user = User.objects.create_user("testuser", password="pass")
        Subscription.objects.create(
            user=self.user, name="netflix.com", url="https://netflix.com",
            cost=10, billing_cycle="monthly",
        )
        self.client.login(username="testuser", password="pass")

    def test_batch_100_events_all_processed(self):
        events = []
        for i in range(100):
            ts = (datetime.now(tz.utc) - timedelta(minutes=100 - i)).isoformat()
            events.append({
                "url": "https://netflix.com",
                "tab_id": (i % 5) + 1,
                "event_type": "open" if i % 2 == 0 else "close",
                "timestamp": ts,
            })
        resp = self.client.post("/api/events/", {"events": events}, content_type="application/json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()["processed"], 100)

    def test_batch_events_old_timestamps_accepted(self):
        old_ts = (datetime.now(tz.utc) - timedelta(days=30)).isoformat()
        resp = self.client.post(
            "/api/events/",
            {"events": [{"url": "https://netflix.com", "tab_id": 1, "event_type": "open", "timestamp": old_ts}]},
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(SiteEvent.objects.count(), 1)

    def test_batch_malformed_events_reports_errors(self):
        resp = self.client.post(
            "/api/events/",
            {"events": [
                {"url": "https://netflix.com", "tab_id": 1, "event_type": "open", "timestamp": "2026-05-01T12:00:00Z"},
                {"url": "", "tab_id": 2},
            ]},
            content_type="application/json",
        )
        data = resp.json()
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data["processed"], 1)
        self.assertEqual(len(data["errors"]), 1)
