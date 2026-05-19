# 9. Retrospektywa projektu

## 9.1 Podsumowanie retrospektyw

### Retrospektywa Sprintu 1

**Co działało dobrze:**
- Szybka konfiguracja Django z `uv`
- Modele danych zostały dobrze zaprojektowane od początku (brak późniejszych migracji)
- Endpointy REST działają zgodnie z oczekiwaniami
- Udane użycie `crispy-forms` dla formularzy

**Co można poprawić:**
- Brak testów w Sprint 1 — testy powinny być pisane równolegle z kodem
- Konfiguracja CSRF dla rozszerzenia zajęła więcej czasu niż planowano
- Większy nacisk na dokumentację API od początku

### Retrospektywa Sprintu 2

**Co działało dobrze:**
- Wszystkie testy (16) przechodzą
- Logika sesji obsługuje wszystkie brzegowe przypadki
- Dashboard z Chart.js wygląda profesjonalnie
- Rozszerzenie Chrome stabilnie rejestruje zdarzenia
- Story Pointy zrealizowane zgodnie z planem (14 z 17 SP; 3 SP przesunięte — US-19)

**Co można poprawić:**
- Brak endpointu `/api/stats/` — agregacje są liczone w widoku dashboardu
- Brak rate limitingu na endpointach zdarzeń
- Za mało testów integracyjnych (tylko 4)
- Dokumentacja projektu wymaga uzupełnienia (sprawozdanie)

**Action items:**
- [ ] Dodać endpoint `/api/stats/` w kolejnej iteracji
- [ ] Dodać rate limiting
- [x] Przygotować sprawozdanie końcowe

## 9.2 Feedback 360°

Feedback 360° został przeprowadzony między członkami zespołu w trzech obszarach:

**Mocne strony:**
- Efektywna współpraca przy projektowaniu i implementacji pełnego systemu (backend + frontend + rozszerzenie przeglądarki)
- Zespół wykazał się dobrą znajomością Django i Pythona
- Dbałość o obsługę przypadków brzegowych w logice biznesowej
- Kompleksowe testy (45 testów z pokryciem kluczowych scenariuszy)

**Obszary do poprawy:**
- Dokumentacja API (brak OpenAPI/Swagger)
- CI/CD i automatyzacja (brak pipeline'ów)
- Wcześniejsze rozpoczęcie pisania testów (Sprint 1 nie miał testów)

**Konkretne sugestie:**
- W przyszłych projektach rozpocząć pisanie testów od pierwszego dnia
- Używać GitHub Actions dla automatycznego uruchamiania testów przy każdym pushu
- Rozważyć użycie Django REST Framework zamiast ręcznych widoków JSON

---

# 10. Wnioski i rekomendacje

## 10.1 Ocena realizacji projektu

Projekt **Sub Guardian** został zrealizowany w 4 z 5 zaplanowanych sprintów (59% całkowitego zakresu — 59 z 106 SP). Ostatni sprint (Sprint 5) obejmuje 47 SP (41%) i pozostaje planowany.

| Wymóg | Status | Komentarz |
|-------|--------|-----------|
| Aplikacja z min. 3 funkcjonalnościami na 3 stronach | **Zrealizowane** | (1) Dashboard z Chart.js, (2) Logowanie/rejestracja, (3) Popup rozszerzenia + API |
| Szacowanie prac z dokładnością do godzin / SP | **Zrealizowane** | Szacowanie w Story Pointach ciągiem Fibonacciego; szczegóły w sekcji 3 |
| Aplikacja w min. 2 iteracjach | **Zrealizowane** | 5 sprintów: Sprint 1 (fundamenty), Sprint 2 (dashboard), Sprint 3 (silnik sesji), Sprint 4 (rozszerzenie), Sprint 5 (planowany) |
| Plan testów | **Zrealizowane** | 45 testów: 29 jednostkowych + 16 integracyjnych w `api/tests.py` i `dashboard/tests.py` |
| Harmonogram + lista błędów | **Zrealizowane** | Wykres Gantta epików + 7 zgłoszonych błędów |
| PR, branch, tagi w repozytorium | **Do uzupełnienia** | Obecnie 1 commit na master; wymagane w przyszłości |

4 User Stories (US-15, US-16, US-19, US-28 — łącznie 16 SP) zostały przesunięte do Sprintu 5 z powodu niepełnej implementacji. Najwięcej wysiłku (26 SP) pochłonął Sprint 3 — logika sesji i obsługa przypadków brzegowych (przełączanie kart, wielokartowość).

## 10.2 Propozycje dalszego rozwoju aplikacji

Priorytetowo — dokończenie 4 przesuniętych User Stories (Sprint 5):

1. **Edycja subskrypcji** (US-15, 3 SP) — dodanie endpointu PUT `/api/subscriptions/<id>/` umożliwiającego zmianę kosztu, cyklu i nazwy subskrypcji.
2. **Dashboardowe CRUD subskrypcji** (US-16, 8 SP) — strony `/subscriptions/` z formularzami dodawania, edycji i usuwania subskrypcji w dashboardzie (obecnie tylko API).
3. **Przewodnik pierwszego logowania** (US-19, 3 SP) — wykrywanie pierwszej wizyty użytkownika i wyświetlenie 3-4 kroków wprowadzających.
4. **Kategoryzacja subskrypcji** (US-28, 2 SP) — dodanie pola `category` do modelu `Subscription` (rozrywka, praca, edukacja, zdrowie).

Pozostałe kierunki rozwoju:

5. **Endpoint agregacji statystyk** (`GET /api/stats/`) — przeniesienie logiki agregacji z widoku dashboardu do osobnego endpointu API.
6. **Rate limiting** — ograniczenie liczby żądań na endpointach zdarzeń dla ochrony przed przeciążeniem.
7. **Django REST Framework** — migracja z ręcznych widoków JSON na DRF (serializery, widoki generyczne, dokumentacja OpenAPI).
8. **Docker + PostgreSQL** — konteneryzacja aplikacji dla łatwiejszego wdrożenia produkcyjnego.

## 10.3 Rekomendacje dotyczące pracy zespołowej i zarządzania projektami

1. **Testy od pierwszego dnia** — w Sprint 1 nie było testów, co jest błędem. Testy jednostkowe powinny być pisane równolegle z implementacją, zgodnie z zasadami TDD.

2. **Continuous Integration** — skonfigurowanie GitHub Actions do automatycznego uruchamiania testów, lintingu i type checków przy każdym pushu.

3. **Branching strategy** — używanie branchy (`feature/*`, `bugfix/*`) i Pull Requestów dla zachowania historii wszystkich zmian i możliwości rollbacku.

4. **Dokumentacja API** — użycie OpenAPI/Swagger dla automatycznie generowanej dokumentacji endpointów, niezależnie od frameworka.

5. **Regularne retrospektywy** — cotygodniowe retrospektywy (nawet 15-minutowe) pomagają wyłapać problemy wcześnie i ciągle ulepszać proces.

6. **Szacowanie z buforem** — mimo że szacunki były trafne, warto dodać 10-15% bufora na nieprzewidziane problemy.
