import logging
from urllib.parse import urlparse

from django.utils.dateparse import parse_datetime

logger = logging.getLogger(__name__)


def _ensure_dt(value):
    if isinstance(value, str):
        return parse_datetime(value)
    return value


def get_site_name(url):
    try:
        hostname = urlparse(url).hostname
        parts = hostname.split(".")
        return ".".join(parts[-2:]).lower()
    except Exception:
        return url or ""


def match_subscription(user, url):
    from .models import Subscription

    site_name = get_site_name(url)
    try:
        return Subscription.objects.get(
            user=user,
            name__iexact=site_name,
            is_active=True,
        )
    except Subscription.DoesNotExist:
        return None


def _tab_states(user):
    from .models import SiteEvent

    states = {}
    for ev in SiteEvent.objects.filter(user=user).order_by("timestamp").iterator():
        states[ev.tab_id] = (get_site_name(ev.url), ev.event_type)
    return states


def count_open_tabs_for_subscription(user, subscription):
    site_name = subscription.name.lower()
    return sum(
        1 for s, t in _tab_states(user).values() if s == site_name and t == "open"
    )


def _close_previous_site_for_tab(user, tab_id, current_url, timestamp):
    from .models import Session, SiteEvent, Subscription

    current_site = get_site_name(current_url)

    events = list(
        SiteEvent.objects.filter(user=user, tab_id=tab_id)
        .order_by("-timestamp")
        .values_list("url", "event_type")[:2]
    )

    if len(events) < 2:
        return

    prev_url, prev_type = events[1]
    prev_site = get_site_name(prev_url)

    if prev_site == current_site or prev_type != "open":
        return

    try:
        prev_sub = Subscription.objects.get(
            user=user, name__iexact=prev_site, is_active=True
        )
    except Subscription.DoesNotExist:
        return

    if count_open_tabs_for_subscription(user, prev_sub) > 0:
        return

    try:
        session = Session.objects.get(
            user=user, subscription=prev_sub, ended_at__isnull=True
        )
    except Session.DoesNotExist:
        return

    session.ended_at = timestamp
    if session.started_at:
        session.duration_seconds = int((timestamp - session.started_at).total_seconds())
    session.save()
    logger.info("Closed session %s for %s (tab switched)", session.id, prev_sub.name)


def process_open_event(user, url, tab_id, timestamp):
    from .models import SiteEvent, Session

    timestamp = _ensure_dt(timestamp)

    SiteEvent.objects.create(
        user=user,
        url=url,
        tab_id=tab_id,
        event_type="open",
        timestamp=timestamp,
    )

    subscription = match_subscription(user, url)
    if not subscription:
        return None

    _close_previous_site_for_tab(user, tab_id, url, timestamp)

    active = Session.objects.filter(
        user=user, subscription=subscription, ended_at__isnull=True
    ).first()

    if active:
        return None

    session = Session.objects.create(
        user=user,
        subscription=subscription,
        url=url,
        started_at=timestamp,
    )
    logger.info("Created session %s for %s", session.id, subscription.name)
    return session


def process_close_event(user, url, tab_id, timestamp):
    from .models import SiteEvent, Session

    timestamp = _ensure_dt(timestamp)

    SiteEvent.objects.create(
        user=user,
        url=url,
        tab_id=tab_id,
        event_type="close",
        timestamp=timestamp,
    )

    subscription = match_subscription(user, url)
    if not subscription:
        return None

    open_tabs = count_open_tabs_for_subscription(user, subscription)
    if open_tabs > 0:
        return None

    try:
        session = Session.objects.get(
            user=user, subscription=subscription, ended_at__isnull=True
        )
    except Session.DoesNotExist:
        return None

    session.ended_at = timestamp
    if session.started_at:
        session.duration_seconds = int((timestamp - session.started_at).total_seconds())
    session.save()
    logger.info("Closed session %s for %s", session.id, subscription.name)
    return session
