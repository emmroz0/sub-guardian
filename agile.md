
---

## Definicja Ukończenia

1. Kod napisany, działa na środowisku deweloperskim.
2. Migracje (jeśli dotyczy modeli) napisane i zatwierdzone.
3. Testy jednostkowe/integracyjne napisane i przechodzą.
4. Kod nie psuje istniejących testów.
5. Manualna weryfikacja przez `runserver`.
6. Dokumentacja (README/AGENTS.md) zaktualizowana, jeśli zmienia się interfejs.

---

## Sprint 1 — Fundacja projektu

**Cel sprintu:** Przygotowanie szkieletu Django, modeli danych i panelu admina.

**Czas:** 2 tygodnie (18.03.2026 – 31.03.2026)

### Zadania

| ID | Zadanie | Godziny | Zależności |
|----|---------|---------|------------|
| S1-T1 | Inicjalizacja projektu Django (`django-admin startproject core`) w katalogu `src/` | 1 | — |
| S1-T2 | Konfiguracja `pyproject.toml` z zależnościami (Django 6.0, crispy-bootstrap5, django-stubs) | 1 | — |
| S1-T3 | Konfiguracja `settings.py` (baza SQLite, aplikacje, middleware, crispy, auth redirects, CSRF\_TRUSTED\_ORIGINS z placeholderem) | 2 | S1-T1 |
| S1-T4 | Konfiguracja `core/urls.py` (mount admin, api, dashboard, auth) | 1 | S1-T1 |
| S1-T5 | Utworzenie aplikacji `api` | 0.5 | S1-T1 |
| S1-T6 | Implementacja modelu `Subscription` (user, name, url, cost, billing\_cycle, next\_billing\_date, is\_active, created\_at, updated\_at) | 2 | S1-T5 |
| S1-T7 | Migracja 0001 — `Subscription` z polem `URLField` dla url | 0.5 | S1-T6 |
| S1-T8 | Migracja 0002 — zmiana `URLField` → `CharField` | 0.5 | S1-T7 |
| S1-T9 | Rejestracja `SubscriptionAdmin` w `api/admin.py` | 0.5 | S1-T6 |
| S1-T10 | Utworzenie aplikacji `dashboard` + konfiguracja szablonów + `base.html` | 2 | S1-T1 |
| S1-T11 | Konfiguracja `AGENTS.md` i inicializacja repo git | 1 | S1-T1 |

**Suma godzin:** 12

### Zaakceptowane historie: US-001, US-002, US-003

### Kryteria akceptacji

- `uv run src/manage.py migrate` tworzy tabele `api_subscription`.
- `uv run src/manage.py runserver` uruchamia serwer.
- Panel admin dostępny pod `/admin/` i pozwala zarządzać subskrypcjami.
- Szablon `base.html` renderuje się z Bootstrap 5.

### Testy (Sprint 1)

Brak testów automatycznych w tym sprincie — weryfikacja manualna.

---

## Sprint 2 — Autoryzacja i dashboard

**Cel sprintu:** Implementacja rejestracji, logowania i strony głównej dashboardu.

**Czas:** 2 tygodnie (01.04.2026 – 14.04.2026)

### Zadania

| ID    | Zadanie                                                                                                                                                  | Godziny | Zależności   |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------ |
| S2-T1 | Implementacja widoku `sign_up` (GET: formularz, POST: walidacja + create user + login + redirect) w `dashboard/views.py`                                 | 3       | S1-T10       |
| S2-T2 | Szablon `registration/sign_up.html` z crispy forms                                                                                                       | 2       | S2-T1        |
| S2-T3 | Szablon `registration/login.html` z crispy forms                                                                                                         | 1.5     | S2-T1        |
| S2-T4 | Konfiguracja `dashboard/urls.py` (home, sign\_up)                                                                                                        | 0.5     | S2-T1        |
| S2-T5 | Integracja `django.contrib.auth.urls` w `core/urls.py`                                                                                                   | 0.5     | S1-T4        |
| S2-T6 | Implementacja widoku `home` w `dashboard/views.py` — wersja niezalogowana: hero + przyciski logowania/rejestracji                                        | 2       | S2-T4        |
| S2-T7 | Implementacja widoku `home` — wersja zalogowana: statystyki (liczba subskrypcji, koszt miesięczny, godziny, wizyty) + lista subskrypcji + ostatnie sesje | 6       | S2-T6, S1-T6 |
| S2-T8 | Szablon `dashboard/home.html` — karty statystyk, lista subskrypcji, wykresy Chart.js (czas na subskrypcję, aktywność dzienna), tabela sesji              | 5       | S2-T7        |
| S2-T9 | Konfiguracja crispy forms (`CRISPY_TEMPLATE_PACK`, `CRISPY_ALLOWED_TEMPLATE_PACKS`)                                                                      | 0.5     | S1-T3        |

**Suma godzin:** 21

### Zaakceptowane historie: US-004, US-005

### Kryteria akceptacji

- Rejestracja działa: nowy użytkownik może się zarejestrować i zostaje automatycznie zalogowany.
- Logowanie/wylogowanie działa poprzez wbudowane widoki Django.
- Dashboard po zalogowaniu pokazuje: liczbę subskrypcji, koszt miesięczny, śledzone godziny, liczbę wizyt.
- Wykresy Chart.js renderują się poprawnie (słupkowy — czas na subskrypcję, liniowy — aktywność dzienna).
- Dashboard dla niezalogowanego użytkownika pokazuje stronę powitalną z przyciskami.

### Testy (Sprint 2)

Brak automatycznych testów dashboardu w tym sprincie — weryfikacja manualna.
`dashboard/tests.py` pozostaje stubbed.

---

## Sprint 3 — Silnik sesji i API

**Cel sprintu:** Implementacja modeli SiteEvent i Session, logiki budowania sesji oraz endpointów API dla rozszerzenia.

**Czas:** 2 tygodnie (15.04.2026 – 28.04.2026)

### Zadania

| ID | Zadanie | Godziny | Zależności |
|----|---------|---------|------------|
| S3-T1 | Implementacja modelu `SiteEvent` (user, url, tab\_id, event\_type, timestamp, created\_at) + Meta z indeksem `(user, timestamp)` | 2 | S1-T5 |
| S3-T2 | Migracja 0003 — `SiteEvent` | 0.5 | S3-T1 |
| S3-T3 | Implementacja modelu `Session` (user, subscription, url, started\_at, ended\_at, duration\_seconds, created\_at) + Meta z indeksem `(user, subscription, ended\_at)` | 2 | S1-T6 |
| S3-T4 | Migracja 0004 — `Session` | 0.5 | S3-T3 |
| S3-T5 | Rejestracja `SiteEventAdmin` i `SessionAdmin` w `api/admin.py` | 0.5 | S3-T1, S3-T3 |
| S3-T6 | Implementacja `session_manager.py` — `get_site_name(url)` | 1 | — |
| S3-T7 | Implementacja `session_manager.py` — `match_subscription(user, url)` | 1 | S3-T6, S1-T6 |
| S3-T8 | Implementacja `session_manager.py` — `_tab_states(user)` rekonstrukcja stanu kart z eventów | 2 | S3-T1 |
| S3-T9 | Implementacja `session_manager.py` — `count_open_tabs_for_subscription(user, subscription)` | 1 | S3-T8 |
| S3-T10 | Implementacja `session_manager.py` — `_close_previous_site_for_tab(user, tab_id, current_url, timestamp)` wykrywanie przełączania kart | 3 | S3-T7, S3-T8, S3-T9 |
| S3-T11 | Implementacja `session_manager.py` — `process_open_event(user, url, tab_id, timestamp)` | 2 | S3-T7, S3-T9, S3-T10 |
| S3-T12 | Implementacja `session_manager.py` — `process_close_event(user, url, tab_id, timestamp)` | 2 | S3-T7, S3-T9 |
| S3-T13 | Implementacja widoku `health_check` (GET → `{"status": "ok"}`) | 0.5 | — |
| S3-T14 | Implementacja widoku `auth_status` (GET → status autoryzacji) | 0.5 | — |
| S3-T15 | Implementacja widoku `subscription_list` (GET, @login\_required, zwraca aktywne subskrypcje) | 1.5 | S1-T6 |
| S3-T16 | Implementacja widoku `create_site_event` (POST, @login\_required, walidacja + delegacja do session\_managera) | 2 | S3-T11, S3-T12 |
| S3-T17 | Implementacja widoku `create_site_events_batch` (POST, batch, pętla + walidacja + delegacja) | 2 | S3-T16 |
| S3-T18 | Konfiguracja `api/urls.py` (5 endpointów) | 0.5 | S3-T13..S3-T17 |
| S3-T19 | Testy jednostkowe `session_manager` (12 testów: open, close, tab switching, get\_site\_name, count\_open\_tabs) | 5 | S3-T6..S3-T12 |
| S3-T20 | Testy integracyjne API (4 testy: pojedyncze open/close, batch, batch close) | 3 | S3-T16, S3-T17 |

**Suma godzin:** 30

### Zaakceptowane historie: US-006, US-007, US-008, US-009

### Kryteria akceptacji

- Wysłanie zdarzenia `open` dla dopasowanej subskrypcji tworzy rekord `SiteEvent` i `Session`.
- Wysłanie zdarzenia `close` dla ostatniej otwartej karty kończy `Session` z wypełnionym `duration_seconds`.
- Przełączenie karty z jednej subskrypcji na inną zamyka poprzednią sesję.
- Wysłanie zdarzenia dla niezmapowanego URL nie tworzy sesji.
- Endpoint `/api/health/` zwraca `{"status": "ok"}`.
- Endpoint `/api/auth_status/` zwraca stan autoryzacji.
- Endpoint `/api/events/` akceptuje batch eventów.
- Endpoint `/api/subscriptions/` zwraca listę aktywnych subskrypcji.
- Wszystkie testy przechodzą: `uv run src/manage.py test api` — 16 testów, all green.

### Testy (Sprint 3)

- **`SessionManagerTests`** (12 testów) — w `api/tests.py`:
  - `test_open_creates_session` — otwarcie na dopasowanej subskrypcji tworzy sesję
  - `test_open_no_session_for_unmatched_url` — brak sesji dla nieznanego URL
  - `test_open_does_not_duplicate_session` — drugie otwarcie (inna karta) nie duplikuje sesji
  - `test_close_ends_session_when_last_tab` — zamknięcie ostatniej karty kończy sesję
  - `test_close_does_not_end_session_when_other_tab_open` — inna karta wciąż otwarta → sesja trwa
  - `test_close_noop_when_no_active_session` — close bez open → noop
  - `test_close_noop_for_unmatched_url` — close na nieznanym URL → noop
  - `test_switching_to_new_sub_closes_previous_session` — przełączenie na inną subskrypcję zamyka poprzednią
  - `test_switching_to_same_site_keeps_session` — nawigacja w ramach tej samej strony nie przerywa sesji
  - `test_multiple_tabs_different_subs_close_correctly` — wiele kart różnych subskrypcji
  - `test_get_site_name` — ekstrakcja nazwy z URL (www.netflix.com → netflix.com)
  - `test_count_open_tabs` — zliczanie otwartych kart
- **`SessionViaApiTests`** (4 testy) — w `api/tests.py`:
  - `test_post_open_event_creates_session` — POST `/api/events/single/` tworzy sesję
  - `test_post_close_event_ends_session` — open → close kończy sesję
  - `test_batch_events_create_and_close_session` — batch tworzy sesję
  - `test_batch_close_last_tab_ends_session` — batch close kończy sesję

---

## Sprint 4 — Rozszerzenie Chrome

**Cel sprintu:** Implementacja rozszerzenia Chrome w wersji Manifest V3 wraz z integracją z backendem.

**Czas:** 2 tygodnie (29.04.2026 – 12.05.2026)

### Zadania

| ID | Zadanie | Godziny | Zależności |
|----|---------|---------|------------|
| S4-T1 | Konfiguracja `manifest.json` (Manifest V3, permissions: tabs, scripting, storage, cookies; host\_permissions: <all\_urls>; service worker, popup) | 1.5 | — |
| S4-T2 | Implementacja `js/helpers.js` — `getSiteName(url)` ekstrakcja hostname | 1 | — |
| S4-T3 | Implementacja `js/api.js` — `checkHealth()`, `getAuthStatus()`, `getCsrfToken()`, `postSiteEvent()`, `getSubscriptions()` | 4 | — |
| S4-T4 | Implementacja `background.js` — service worker: cache subskrypcji, nasłuchiwanie `chrome.tabs.onCreated`, `onRemoved`, `onUpdated`, `matchesSubscription()` | 6 | S4-T2, S4-T3 |
| S4-T5 | Implementacja `popup/popup.html` — Bootstrap 5, dark theme, status API, link do dashboardu | 2 | — |
| S4-T6 | Implementacja `popup/popup.js` — sprawdzanie health + auth, wyświetlanie stanu | 1.5 | S4-T3 |
| S4-T7 | Konfiguracja `CSRF_TRUSTED_ORIGINS` w `settings.py` z dwoma ID rozszerzenia | 0.5 | S1-T3 |
| S4-T8 | Testowanie manualne: załadowanie unpacked extension, logowanie, weryfikacja wysyłania eventów | 3 | S4-T1..S4-T7 |

**Suma godzin:** 19.5

### Zaakceptowane historie: US-010, US-011

### Kryteria akceptacji

- Rozszerzenie ładuje się jako unpacked extension w Chrome.
- Service worker uruchamia się i nasłuchuje zdarzeń kart.
- Po otwarciu karty z subskrybowaną stroną (dopasowanie po nazwie subskrypcji) wysyłane jest zdarzenie `open`.
- Po zamknięciu karty wysyłane jest zdarzenie `close`.
- Przeładowanie/zmiana URL na karcie wysyła nowe zdarzenie `open`.
- Popup pokazuje:
  - "Online" (zielony) / "Offline" (czerwony)
  - "Logged as {username}" (zielony) / "Not logged in" (żółty)
- Link w popupie prowadzi do `http://127.0.0.1:8000/home/`.
- Wszystkie żądania wysyłane z `credentials: "include"` i nagłówkiem `X-CSRFToken`.

### Testy (Sprint 4)

Brak automatycznych testów dla rozszerzenia — testowanie manualne w przeglądarce.

---

## Sprint 5 — CRUD, Analityka, Jakość (planowany)

**Cel sprintu:** Implementacja brakujących funkcji: pełne CRUD subskrypcji przez API i dashboard, strona analityczna, log sesji, poprawki bezpieczeństwa i konfiguracja narzędzi jakości.

**Czas:** 2 tygodnie (13.05.2026 – 26.05.2026) — *planowany*

### Zadania

| ID | Zadanie | Godziny | Zależności | Priorytet |
|----|---------|---------|------------|-----------|
| S5-T1 | Implementacja widoku `create_subscription` (POST, @login\_required, walidacja JSON, tworzenie) | 2 | S1-T6 | Must |
| S5-T2 | Implementacja widoku `update_subscription` (PUT, @login\_required, walidacja, aktualizacja) | 2 | S1-T6 | Must |
| S5-T3 | Implementacja widoku `delete_subscription` (DELETE, @login\_required, dezaktywacja/usunięcie) | 1.5 | S1-T6 | Must |
| S5-T4 | Dodanie tras POST/PUT/DELETE do `api/urls.py` | 0.5 | S5-T1..S5-T3 | Must |
| S5-T5 | Implementacja widoku `session_list` (GET, @login\_required, filtrowanie po dacie/subskrypcji, paginacja) | 4 | S3-T3 | Should |
| S5-T6 | Dodanie trasy GET `/api/sessions/` do `api/urls.py` | 0.5 | S5-T5 | Should |
| S5-T7 | Implementacja widoku `stats` (GET, @login\_required, agregacja czasu/kosztu na subskrypcję w zakresie dat) | 5 | S1-T6, S3-T3 | Should |
| S5-T8 | Dodanie trasy GET `/api/stats/` do `api/urls.py` | 0.5 | S5-T7 | Should |
| S5-T9 | Implementacja widoku dashboardowego `subscription_list_view` — lista subskrypcji z przyciskami akcji | 3 | S2-T4 | Should |
| S5-T10 | Implementacja widoku dashboardowego `subscription_create_view` — formularz dodawania subskrypcji (crispy forms) | 3 | S2-T4 | Should |
| S5-T11 | Implementacja widoków dashboardowych `subscription_update_view` / `subscription_delete_view` — formularz edycji i potwierdzenie usunięcia | 3 | S2-T4 | Should |
| S5-T12 | Szablony dashboardowe dla subskrypcji: `subscription_list.html`, `subscription_form.html`, `subscription_confirm_delete.html` | 4 | S5-T9..S5-T11 | Should |
| S5-T13 | Implementacja widoku dashboardowego `analytics_view` — agregacja danych, przekazanie do szablonu | 4 | S5-T7 | Should |
| S5-T14 | Szablon `dashboard/analytics.html` — Chart.js: czas vs pieniądze, koszt na subskrypcję, filtr zakresu dat (tydzień/miesiąc) | 5 | S5-T13 | Should |
| S5-T15 | Implementacja widoku dashboardowego `session_list_view` — lista sesji z paginacją i filtrami | 3 | S5-T5 | Should |
| S5-T16 | Szablon `dashboard/session_list.html` — tabela sesji, filtry (data, subskrypcja, czas trwania) | 3 | S5-T15 | Should |
| S5-T17 | Aktualizacja `dashboard/urls.py` o nowe trasy | 0.5 | S5-T9..S5-T16 | Should |
| S5-T18 | Testy dashboardu: testy widoków dashboardowych (home, sign\_up, subscription CRUD, analytics, sessions) — min. 10 testów | 6 | S5-T9..S5-T17 | Could |
| S5-T19 | Testy API dla CRUD subskrypcji: testy POST/PUT/DELETE `/api/subscriptions/` — 6 testów | 3 | S5-T1..S5-T4 | Could |
| S5-T20 | Testy API dla sesji: testy GET `/api/sessions/` z filtrami — 3 testy | 2 | S5-T5 | Could |
| S5-T21 | Testy API dla statystyk: testy GET `/api/stats/` — 3 testy | 2 | S5-T7 | Could |
| S5-T22 | Limitowanie żądań na endpointach eventowych (np. `django-ratelimit` lub własny decorator) — max 60 req/min na użytkownika | 3 | S3-T16, S3-T17 | Could |
| S5-T23 | Paginacja w `GET /api/subscriptions/` i `GET /api/sessions/` | 2 | S3-T15, S5-T5 | Could |
| S5-T24 | Konfiguracja narzędzi: ruff (linter), black (formatter), myqsl/pyright (type checker), pre-commit hooks | 2 | — | Could |
| S5-T25 | Dodanie `.gitignore` w katalogu głównym i `sg-webapp/` (wykluczenie `.venv`, `db.sqlite3`, `__pycache__`, `.ruff_cache`) | 0.5 | — | Could |
| S5-T26 | Dodanie statycznych plików (logo, favicon, własny CSS) — katalog `dashboard/static/` | 2 | — | Could |
| S5-T27 | Poprawki bezpieczeństwa: `SECRET_KEY` → zmienna środowiskowa, `DEBUG=False` dla produkcji, ograniczenie `ALLOWED_HOSTS` | 2 | S1-T3 | Could |
| S5-T28 | Dokumentacja techniczna: aktualizacja README, komentarze w kodzie, opis architektury w AGENTS.md | 2 | wszystkie powyższe | Could |


### Zaakceptowane historie: US-012, US-013, US-014, US-015, US-016, US-017, US-018, US-019, US-020

### Kryteria akceptacji

- **CRUD API:** POST `/api/subscriptions/` tworzy subskrypcję, PUT `/api/subscriptions/<id>/` aktualizuje, DELETE `/api/subscriptions/<id>/` dezaktywuje.
- **Sessions API:** GET `/api/sessions/` zwraca paginowaną listę sesji z filtrami `?from=`, `?to=`, `?subscription_id=`.
- **Stats API:** GET `/api/stats/` zwraca zagregowane dane: czas na subskrypcję, koszt na subskrypcję, porównanie czas vs koszt.
- **Dashboard subskrypcji:** strona `/subscriptions/` z listą, dodawaniem, edycją i usuwaniem.
- **Dashboard analityki:** strona `/analytics/` z wykresami Chart.js i filtrem zakresu dat.
- **Dashboard sesji:** strona `/sessions/` z paginowaną tabelą i filtrami.
- **Limitowanie:** endpoint `/api/events/` odrzuca żądania powyżej 60/min z kodem 429.
- **Narzędzia:** `ruff check .`, `black --check .`, i type checker przechodzą na całym kodzie.
- **Bezpieczeństwo:** `SECRET_KEY` w zmiennej środowiskowej, `DEBUG=False` w produkcji.
- Wszystkie testy przechodzą: `uv run src/manage.py test` — co najmniej 38 testów.

### Testy (Sprint 5)

#### Nowe testy w `api/tests.py`

**`SubscriptionCrudApiTests(TestCase)`** — 6 testów:
1. `test_create_subscription` — POST tworzy subskrypcję
2. `test_create_subscription_unauthenticated` — bez autoryzacji → 403
3. `test_update_subscription` — PUT aktualizuje
4. `test_update_subscription_other_user` — nie można edytować cudzej
5. `test_delete_subscription` — DELETE dezaktywuje
6. `test_delete_subscription_other_user` — nie można usunąć cudzej

**`SessionApiTests(TestCase)`** — 3 testy:
1. `test_list_sessions` — GET zwraca sesje użytkownika
2. `test_list_sessions_filter_by_date` — filtr `from`/`to` działa
3. `test_list_sessions_filter_by_subscription` — filtr `subscription_id` działa

**`StatsApiTests(TestCase)`** — 3 testy:
1. `test_stats_returns_data` — GET zwraca zagregowane dane
2. `test_stats_with_date_filter` — filtr zakresu dat działa
3. `test_stats_empty_for_new_user` — nowy użytkownik dostaje puste statystyki

#### Nowe testy w `dashboard/tests.py`

**`DashboardViewTests(TestCase)`** — 10 testów:
1. `test_home_unauthenticated` — strona główna dla niezalogowanego
2. `test_home_authenticated` — strona główna dla zalogowanego
3. `test_sign_up_get` — formularz rejestracji
4. `test_sign_up_post` — rejestracja tworzy użytkownika
5. `test_subscription_list_view` — lista subskrypcji
6. `test_subscription_create_view` — formularz dodawania
7. `test_subscription_update_view` — formularz edycji
8. `test_subscription_delete_view` — potwierdzenie usunięcia
9. `test_analytics_view` — strona analityki
10. `test_session_list_view` — lista sesji
