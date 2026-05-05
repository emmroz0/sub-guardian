# AGENTS.md

## Project

Django 6.0 webapp for Sub Guardian. Python 3.13.

## Package manager

- **`uv`** — use `uv sync` to install deps, `uv run <cmd>` to run commands within the venv.
- Do not use `pip` or `python -m venv`.

## Entry point

- `src/manage.py` — all Django commands run from the `src/` directory.
- Settings module: `core.settings`
- Database: SQLite at `src/db.sqlite3`

## Apps

| App | Mount | Purpose |
|-----|-------|---------|
| `core` | — | Project config (settings, urls, wsgi, asgi) |
| `api` | `/api/` | API views |
| `dashboard` | `/` | Web UI (Bootstrap 5 via django-crispy-forms) |

## Commands

```
uv run src/manage.py runserver      # Dev server
uv run src/manage.py migrate        # Apply migrations
uv run src/manage.py makemigrations # Create migrations
uv run src/manage.py test           # Run tests
uv run src/manage.py createsuperuser
```

## Testing

- Django built-in `TestCase` only (no pytest).
- Run: `uv run src/manage.py test` (all) or `uv run src/manage.py test api` (per-app).
- Test files are stubs (`src/api/tests.py`, `src/dashboard/tests.py`).

## Notes

- `CSRF_TRUSTED_ORIGINS` includes a Chrome extension origin — keep this when modifying CSRF settings.
- No lint, formatter, typecheck, or CI tools configured yet.
- `DEBUG = True` and `ALLOWED_HOSTS = ["*"]` — dev-only defaults.
