# AGENTS.md — Sub Guardian Project Instructions

## Project Overview

**Sub Guardian** to dwukomponentowy system do monitorowania subskrypcji:
- **`sg-webapp/`** — backend Django 6.0 + dashboard webowy (Bootstrap 5, Chart.js)
- **`sg-extension/`** — rozszerzenie Chrome (Manifest V3) monitorujące aktywność kart

Autor: Michał Mroziński, Uniwersytet Kazimierza Wilekiego w Bydgoszczy

## Struktura repozytorium

```
sub-guardian/
├── AGENTS.md              ← niniejszy plik
├── docs/                   ← materiały kursu (PDF)
├── sg-extension/           ← rozszerzenie Chrome
│   ├── manifest.json       ← manifest V3
│   ├── background.js       ← service worker (nasłuchuje zdarzeń kart)
│   ├── js/
│   │   ├── api.js          ← klient API (fetch do backendu)
│   │   └── helpers.js      ← funkcje pomocnicze (np. getSiteName)
│   └── popup/
│       ├── popup.html      ← UI wyskakującego okna (Bootstrap 5)
│       └── popup.js        ← logika popupu
└── sg-webapp/
    └── src/
        ├── manage.py
        ├── db.sqlite3      ← baza SQLite (z danymi testowymi)
        ├── core/
        │   ├── settings.py ← konfiguracja Django
        │   └── urls.py     ← główne routy
        ├── api/            ← aplikacja API
        │   ├── models.py   ← Subscription, SiteEvent, Session
        │   ├── views.py    ← widoki REST API
        │   ├── urls.py     ← routy /api/*
        │   ├── session_manager.py ← logika budowania sesji
        │   ├── tests.py    ← 14 testów (unit + integracyjne)
        │   ├── admin.py    ← rejestracja modeli w adminie
        │   └── fixtures/   ← dane testowe
        └── dashboard/      ← aplikacja web UI
            ├── views.py    ← home (dashboard) + sign_up
            ├── urls.py     ← routy strony
            └── templates/  ← szablony HTML (base, home, login, sign_up)
```

## Komendy

```bash
# Uruchomienie serwera
uv run src/manage.py runserver          # z katalogu sg-webapp/

# Testy
uv run src/manage.py test               # wszystkie testy
uv run src/manage.py test api           # tylko api
uv run src/manage.py test api.tests.SessionManagerTests  # konkretna klasa

# Migracje
uv run src/manage.py makemigrations
uv run src/manage.py migrate

# Admin
uv run src/manage.py createsuperuser
```

## Zasady pracy

1. **Język**: UI i komunikaty w języku polskim (zgodnie z istniejącym kodem)
2. **Framework**: Django 6.0, Python 3.13, Bootstrap 5 (via CDN), Chart.js (via CDN)
3. **UI**: wszystkie strony rozszerzają `base.html`, używają `crispy_forms` z `crispy-bootstrap5`
4. **Testy**: Django `TestCase`, bez pytest. Wzorzec: mockowanie API i testowanie logiki sesji
5. **Git**: jedna gałąź (`master`), jeden commit. Przy większych zmianach: branch + PR
6. **Baza**: SQLite (`src/db.sqlite3`), migracje w `api/migrations/`
7. **API**: wszystkie endpointy JSON, auth przez session cookies, CSRF przez `X-CSRFToken` z ciasteczka

## Model danych

| Model | Pola | Opis |
|-------|------|------|
| `Subscription` | user, name, url, cost, billing_cycle, next_billing_date, is_active | Subskrypcja użytkownika |
| `SiteEvent` | user, url, tab_id, event_type, timestamp, created_at | Surowe zdarzenie otwarcia/zamknięcia karty |
| `Session` | user, subscription, url, started_at, ended_at, duration_seconds, created_at | Wyliczona sesja użytkowania |

## API endpoints

| Metoda | Ścieżka | Auth | Opis |
|--------|---------|------|------|
| GET | `/api/health/` | nie | Health check |
| GET | `/api/auth_status/` | nie | Status autoryzacji |
| GET | `/api/subscriptions/` | tak | Lista aktywnych subskrypcji |
| POST | `/api/subscriptions/add/` | tak | Dodanie subskrypcji |
| DELETE | `/api/subscriptions/<id>/` | tak | Miękkie usunięcie subskrypcji |
| POST | `/api/events/` | tak | Zdarzenia tab (batch) |
| POST | `/api/events/single/` | tak | Pojedyńcze zdarzenie tab |

## Logika biznesowa (session_manager.py)

- `process_open_event` → tworzy SiteEvent + Session jeśli URL pasuje do subskrypcji
- `process_close_event` → tworzy SiteEvent + zamyka Session jeśli to ostatnia karta
- Obsługa przełączania kart między subskrypcjami
- Obsługa wielu kart tej samej subskrypcji
- Obsługa zdarzeń dla URL spoza subskrypcji (SiteEvent tak, Session nie)

## Wymagania przedmiotu "Zarządzanie projektami"

1. **Aplikacja z min. 3 funkcjonalnościami na 3 stronach** — zrealizowane
2. **Szacowanie prac z dokładnością do godzin** — udokumentowane w sprawozdaniu
3. **Aplikacja w min. 2 iteracjach** — udokumentowane w sprawozdaniu
4. **Plan testów** — testy jednostkowe + integracyjne + scenariusze
5. **Harmonogram + lista błędów** — udokumentowane w sprawozdaniu
6. **PR, branch, tagi w repozytorium** — do uzupełnienia w przyszłości

## Kolejne kroki rozwoju

Priorytetowo:
1. Endpoint `GET /api/stats/` — agregacje dla dashboardu
2. Endpoint `GET /api/sessions/` — lista sesji z filtrami
3. Dashboard: strony subskrypcji (CRUD z UI)
4. Dashboard: strona analityk (Chart.js z danych API)
5. Dashboard: lista sesji z paginacją
6. Rate limiting na endpointach zdarzeń
7. Indeksy na `(user, timestamp)` w Event i Session
