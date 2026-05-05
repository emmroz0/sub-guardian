# AGENTS.md

## Project Overview

**Sub Guardian** — Track your subscriptions and see how much time and money you actually spend on them.

**Two-part system:**
- **sg-webapp** — Django backend + dashboard
- **sg-extension** — Chrome extension that detects tab activity on subscribed sites

### How it works

1. User adds subscriptions in the dashboard (name, URL, monthly cost).
2. The browser extension fetches the user's subscription list and monitors tab open/close events on those URLs.
3. Extension sends raw events to the server. The server transforms them into **sessions** (start, end, tab ID, URL, duration).
4. Dashboard displays: active subscriptions, time spent per site, money spent vs. time spent, cost breakdowns.

### Architecture

```
┌─────────────────┐     tab events      ┌──────────────────┐
│  sg-extension   │ ──────────────────► │                  │
│  (Chrome)       │ ◄─── subscriptions  │   sg-webapp      │
└─────────────────┘                     │   (Django 6.0)   │
                                        │                  │
  Dashboard ◄──────────────────────────►│   SQLite DB       │
  (Bootstrap 5)                         │                  │
└──────────────────────────────────────┴──────────────────┘
```

---

## sg-webapp (Django Backend)

### Tech stack

- **Python 3.13**, **Django 6.0**
- **SQLite** (`src/db.sqlite3`)
- **Bootstrap 5** via `django-crispy-forms` + `crispy-bootstrap5`
- **Package manager:** `uv`
- **Testing:** Django `TestCase` (no pytest)
- **Charts:** Chart.js (client-side, rendered in dashboard templates)

### Package manager

- **`uv`** — use `uv sync` to install deps, `uv run <cmd>` to run commands within the venv.
- Do not use `pip` or `python -m venv`.

### Entry point

- `src/manage.py` — all Django commands run from the `src/` directory.
- Settings module: `core.settings`
- Database: SQLite at `src/db.sqlite3`

### Apps

| App | Mount | Purpose |
|-----|-------|---------|
| `core` | — | Project config (settings, urls, wsgi, asgi) |
| `api` | `/api/` | API views |
| `dashboard` | `/` | Web UI (Bootstrap 5 via django-crispy-forms) |

### Data models

| Model | Purpose |
|-------|---------|
| `User` | Django built-in auth user |
| `Subscription` | A paid service: name, URL pattern, cost, billing cycle, active flag |
| `SiteEvent` | Raw event from extension: open/close, tab ID, URL, timestamp |
| `Session` | Computed from paired events: start, end, tab ID, URL, duration, linked to a `Subscription` |

### API endpoints (`/api/`)

| Method | Path | Auth | Purpose |
|--------|------|------|---------|
| `POST` | `/api/subscriptions/` | required | Add a subscription |
| `GET` | `/api/subscriptions/` | required | List user's subscriptions (extension fetches this) |
| `PUT` | `/api/subscriptions/<id>/` | required | Update subscription |
| `DELETE` | `/api/subscriptions/<id>/` | required | Deactivate/delete |
| `POST` | `/api/events/` | required | Batch-submit tab open/close events |
| `GET` | `/api/sessions/` | required | List sessions (with date/user filters) |
| `GET` | `/api/stats/` | required | Aggregate stats for dashboard charts |

### Dashboard pages (`/`)

| Page | Description |
|------|-------------|
| `/home/` | Overview: active subscriptions, total monthly cost, recent sessions |
| `/subscriptions/` | Full subscription list with add/edit/delete |
| `/analytics/` | Charts: time per site, money per site, time vs. money comparison |
| `/sessions/` | Raw session log with filters |

### Commands

```bash
# Dependencies
uv sync

# Database
uv run src/manage.py makemigrations
uv run src/manage.py migrate

# Dev server
uv run src/manage.py runserver

# Tests
uv run src/manage.py test                          # All
uv run src/manage.py test api                      # Single app
uv run src/manage.py test api.tests.SessionTest    # Single test class

# Admin
uv run src/manage.py createsuperuser
```

Dev server runs at `http://localhost:8000/`. `DEBUG = True`, `ALLOWED_HOSTS = ["*"]`.

### Testing

- Django built-in `TestCase` only (no pytest).
- Run: `uv run src/manage.py test` (all) or `uv run src/manage.py test api` (per-app).
- Test files are stubs (`src/api/tests.py`, `src/dashboard/tests.py`).

### Project structure

```
src/
  manage.py
  core/             # Project config (settings, urls, wsgi, asgi)
  api/              # API endpoints (extension-facing + stats)
    models.py       # Subscription, SiteEvent, Session
    views.py        # JSON API views
    urls.py         # /api/* routes
  dashboard/        # Web UI (Bootstrap 5, crispy-forms)
    models.py       # (uses api models)
    views.py        # Template views
    templates/      # HTML templates
    urls.py         # / routes
```

### Notes

- `CSRF_TRUSTED_ORIGINS` includes a Chrome extension origin — preserve it.
- No lint, formatter, typecheck, or CI tools configured yet.
- Extension communicates via session cookies (not token auth).
- Events should be batched by the extension (not sent one-by-one).

---

## sg-extension (Chrome Extension)

### Tech stack

- **Manifest V3**
- **Vanilla JavaScript** (ES modules)
- **Bootstrap 5** (CDN, for popup UI)

### Permissions

- `tabs` — monitor tab activity
- `scripting` — inject scripts
- `storage` — persist local data
- `cookies` — access session cookies for auth
- `host_permissions`: `<all_urls>`

### Files

| File | Purpose |
|------|---------|
| `manifest.json` | Extension manifest (v3), declares permissions, background service worker, popup |
| `background.js` | Service worker — listens to `chrome.tabs.onUpdated` for tab events |
| `popup/popup.html` | Extension popup UI |
| `popup/popup.js` | Popup logic |
| `js/` | Shared modules (e.g., API client — currently empty) |

### Extension setup

1. Load unpacked extension from `sg-extension/` in Chrome.
2. Log in to the webapp once (the extension uses session cookies for auth).
3. Ensure `CSRF_TRUSTED_ORIGINS` in `settings.py` includes the extension origin.

### Notes

- Background script is declared as ES module (`"type": "module"`).
- API client module (`js/api.js`) is planned but not yet implemented.
- Popup links to the webapp dashboard at `http://127.0.0.1:8000/home/`.

---

## Development plan

### Phase 1 — Data models + migrations

- [ ] Create `Subscription` model (user, name, url, cost, billing_cycle, next_billing_date, is_active)
- [ ] Create `SiteEvent` model (user, url, tab_id, event_type, timestamp)
- [ ] Create `Session` model (user, subscription, url, tab_id, started_at, ended_at, duration_seconds)
- [ ] Run `makemigrations` + `migrate`
- [ ] Register models in admin

### Phase 2 — Extension API

- [ ] `POST /api/subscriptions/` — authenticated CRUD (use Django serializers or manual JSON)
- [ ] `GET /api/subscriptions/` — return active subscriptions for the authenticated user
- [ ] `POST /api/events/` — accept batch of `{url, tab_id, event_type, timestamp}` events
- [ ] Validate events, store as `SiteEvent` records
- [ ] Wire up extension CSRF handling (session auth + CSRF token from cookie)

### Phase 3 — Session builder

- [ ] Implement session matching logic: pair open/close events by `(user, tab_id, url)`
- [ ] Handle edge cases: orphan opens (no close), orphan closes, overlapping sessions
- [ ] Link sessions to `Subscription` by matching URL domain
- [ ] Trigger session building on event receipt (or via periodic task)

### Phase 4 — Dashboard: Subscriptions

- [ ] Subscription list view with crispy forms
- [ ] Add/edit/delete forms
- [ ] Show total monthly cost, active count

### Phase 5 — Dashboard: Analytics

- [ ] Stats aggregation queries (time per subscription, cost per subscription, time vs. money)
- [ ] `GET /api/stats/` endpoint for chart data
- [ ] Chart.js integration in analytics template
- [ ] Date range filtering (week, month, custom)

### Phase 6 — Dashboard: Sessions

- [ ] Session list view with pagination
- [ ] Filters by date, subscription, duration
- [ ] Link back to subscription detail

### Phase 7 — Polish

- [ ] Error handling and validation in API
- [ ] Unit tests for session builder logic
- [ ] Rate limiting on event endpoint
- [ ] Performance: index on `(user, timestamp)` for events and sessions
