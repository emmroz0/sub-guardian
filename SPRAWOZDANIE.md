
# 1. Wprowadzenie

## 1.1 Misja oraz cel projektu

Naszą misją było dostarczenie prostego, automatycznego rozwiązania, które pokazuje użytkownikowi ile czasu spędza, a ile pieniędzy wydaje na każdą subskrypcję, robiąc to bez jego udziału; powstanie narzędzia pomagającego konsumentom w podejmowaniu racjonalnych decyzji zakupowych na podstawie twardych danych o własnym zachowaniu. Wynikła ona z założenia, że przeciętny użytkownik nie pamięta wszystkich aktywnych subskrypcji, nie śledzi na bieżąco czasu spędzonego na każdej platformie i nie potrafi jednoznacznie ocenić, czy dany serwis mu się opłaca.

Projekt miał za cel utworzenie dwuelementowego systemu do monitorowania subskrypcji, który rejestruje czas użytkowania przez rozszerzenie do przeglądarki, przechowuje dane na serwerze i prezentuje statystyki na dashboardzie dostępnym w formie aplikacji internetowej. W przeciwieństwie do zwykłych kalendarzy czy notatników, nasza aplikacja dostarcza konkretnych danych (koszt za minutę użytkowania) i przypomina o płatnościach, pomagając zarządzać finansami.

### Persony użytkowników

| Persona                                         | Sylwetka                                                                            | Potrzeba                                                                                                                                                                                                                                  |
| ----------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Oszczędny Student** (Kacper, 22 lata)         | Posiada kilka subskrypcji (Netflix, Spotify, Discord Nitro) oraz ograniczony budżet | Chce wiedzieć, z czego faktycznie korzysta, a co może odpuścić na czas sesji. Korzysta z laptopa na uczelni i telefonu w domu — potrzebuje synchronizacji między urządzeniami, aby dane były spójne niezależnie od tego, gdzie się loguje |
| **Zapominalski Profesjonalista** (Anna, 38 lat) | Pracuje zdalnie, ma wiele subskrypcji (m. in. Canva, Adobe, HBO)                    | Zapomina anulować triale; potrzebuje twardych danych i przypomnień                                                                                                                                                                        |
| **Analityczny Rodzic** (Tomek, 45 lat)          | Opłaca pakiety rodzinne na kilku platformach, jest słabiej obeznany z technologią   | Chce sprawdzić, czy rodzina używa wszystkich kanałów i czy droższy pakiet się opłaca. Liczy na maksymalną prostotę — najlepiej żeby dodanie nowej subskrypcji wymagało jednego kliknięcia, a dashboard sam mówił mu, co jest ważne        |

## 1.2 Zakres projektu

Zakres projektu obejmuje realizację następujących funkcjonalności:

1. **Rejestracja i logowanie użytkownika** — formularz rejestracji z automatycznym logowaniem oraz login/logout oparty o bazę danych użytkowników.
2. **Zarządzanie subskrypcjami** — dodawanie, przeglądanie i usuwanie subskrypcji przez prosty interfejs połączony z API.
3. **Monitorowanie aktywności przeglądarki** — rozszerzenie przeglądarki śledzi zdarzenia otwarcia i zamknięcia kart na stronach subskrypcji i wysyła je do backendu.
4. **Budowanie sesji użytkowania** — backend agreguje surowe zdarzenia w sesje, obsługując otwieranie, przełączanie oraz zamykanie kart.
5. **Dashboard** — wyświetla aktywne subskrypcje, miesięczny koszt, czas spędzony na każdej usłudze, wykresy oraz listę ostatnich sesji.
6. **Panel administracyjny** — zarządzanie modelami przez wbudowany panel admina.

## 1.3 Metodyka pracy

W projekcie zastosowano metodykę Scrum. Wybór ten podyktowany był następującymi przesłankami:

- **Iteracyjność** — możliwość dostarczania działającego przyrostu co sprint
- **Priorytetyzacja** — Backlog Produktu pozwala skupić się na najważniejszych funkcjonalnościach
- **Ciągłe doskonalenie** — retrospektywy po każdym sprincie umożliwiają refleksję nad procesem
- **Transparentność** — sprinty i backlog są jasno zdefiniowane

Każdy sprint trwał 2 tygodnie, jednocześnie odbywały się regularne standupy, planowanie przed oraz retrospektywa po każdym sprincie.

---

# 2. Organizacja zespołu projektowego

## 2.1 Podział ról i odpowiedzialności

| Osoba                   | Rola                                 | Odpowiedzialność                                                                                                             |
| ----------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Maja Jarka**          | Project Manager                      | Definiowanie wymagań, akceptacja dostarczonych funkcji, koordynacja pracy zespołu oraz organizacja standupów                 |
| **Zuzanna Olejarz**     | Product Manager, UI/UX Designer      | Definiowanie wizji produktu, analiza potrzeb rynku oraz projekty graficzne z przestrzeganiem norm dostępności cyfrowej       |
| **Przemysław Paliwoda** | Business Analyst, Tester             | Przełożenie wymagań biznesowych na szczegółowe specyfikacje techniczne, testy manualne i przygotowanie scenariuszy testowych |
| **Michał Mroziński**    | Software Developer, System Architect | Projekt architektury systemu, implementacja logiki aplikacji oraz komunikacji z wtyczką przeglądarkową                       |
| **Kacper Domek**        | Tester, Spec. ds. bezpieczeństwa     | Implementacja i automatyzacja testów jednostkowych, funkcjonalnych oraz bezpieczeństwa, przygotowanie danych testowych       |

## 2.2 Plan komunikacji

### 2.2.1 Typy komunikacji

| Kanał                     | Częstotliwość            | Cel                                                                                                                                                                                                             |
| ------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Standup**               | Dwa razy w tygodniu      | Synchronizacja postępów: co zostało zrobione, co pozostało w obecnym sprincie, czy powstały trudności lub blokery.                                                                                              |
| **Sprint Planning**       | Co sprint                | Wybór User Stories z backlogu do realizacji w sprincie, estymacja zadań (Planning Poker), ustalenie kryteriów akceptacji (Definition of Done) dla każdej historii, przypisywanie zadań do osób odpowiedzialnych |
| **Sprint Review**         | Po sprincie              | Demonstracja działającego przyrostu oprogramowania, zebranie feedbacku, weryfikacja czy dostarczona funkcja spełnia kryteria akceptacji, aktualizacja backlogu                                                  |
| **Retrospektywa**         | Po sprincie              | Refleksja nad procesem pracy: co działało dobrze (Continue), co wymaga zmiany (Stop/Start). Identyfikacja konkretnych akcji usprawniających na kolejny sprint. Feedback 360° między członkami zespołu           |
| **Pozostała komunikacja** | Podczas trwania sprintów | Zgłaszanie błędów, weryfikacja zmian w kodzie źródłowym, regularna aktualizacja dokumentacji oraz plików instrukcji dla asystentów AI (`AGENTS.md`), komunikacja poprzez wiadomości oraz komunikatory głosowe   |

### 2.2.2 Reguły komunikacji w zespole

1. **Zasada Jednej Prawdy** — wszystkie decyzje i ustalenia są dokumentowane, by uniknąć nieporozumień
2. **Dobór języka do odbiorcy** — komunikacja techniczna (code review, architektura) prowadzona jest precyzyjnym językiem specjalistycznym; komunikacja z osobami nietechnicznymi językiem ogólnym, zorientowanym na wartość biznesową
3. **Transparentność** — backlog, postęp zadań i problemy są widoczne dla wszystkich; blokery są zgłaszane natychmiast
4. **Aktywne słuchanie** — przed odpowiedzią parafraza i potwierdzenie zrozumienia
5. **Follow-up** — każde ustalenie ze spotkania ma osobę odpowiedzialną i termin

---

# 3. Planowanie i szacowanie pracy

## 3.1 Wstępny Backlog Produktu

### 3.1.1 Epiki

| ID   | Epik                                  | Opis                                                                                                                                                                    |
| ---- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E-01 | **Rejestracja i pierwsze kroki**      | Umożliwia nowemu użytkownikowi założenie konta, zalogowanie się i szybkie zrozumienie działania systemu                                                                 |
| E-02 | **Zarządzanie listą subskrypcji**     | Pozwala użytkownikowi na dodawanie, przeglądanie, edycję i usuwanie subskrypcji — zarówno ręcznie, jak i automatycznie z poziomu przeglądarki                           |
| E-03 | **Automatyczne śledzenie czasu**      | Rozszerzenie Chrome automatycznie wykrywa wizyty na subskrybowanych stronach i rejestruje spędzony na nich czas bez potrzeby ręcznego dodawania sesji przez użytkownika |
| E-04 | **Podgląd i analiza na dashboardzie** | Dashboard prezentuje podsumowanie wydatków, czasu użytkowania, wykresy i historię sesji w czytelnej formie graficznej                                                   |
| E-05 | **Powiadomienia i alerty**            | System aktywnie informuje użytkownika o zbliżających się płatnościach, nieużywanych subskrypcjach i przekroczeniu budżetu                                               |
| E-06 | **Raportowanie i eksport danych**     | Użytkownik może wygenerować raport i wyeksportować dane w formacie PDF lub CSV                                                                                          |
| E-07 | **Personalizacja i budżetowanie**     | Użytkownik może ustawić miesięczny budżet, kategoryzować subskrypcje i zarządzać preferencjami                                                                          |

### 3.1.2 Historie Użytkowników

| ID    | Epik | User Story                                                                                                                                                                                                    | Priorytet |
| ----- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| US-01 | E-01 | Jako nowy użytkownik, chcę założyć konto i zalogować się, aby mieć dostęp do moich danych                                                                                                                     | Wysoki    |
| US-02 | E-02 | Jako użytkownik, chcę dodać subskrypcję (nazwa, koszt, cykl rozliczeniowy), aby śledzić moje wydatki                                                                                                          | Wysoki    |
| US-03 | E-02 | Jako użytkownik, chcę zobaczyć listę wszystkich moich subskrypcji, aby wiedzieć za co płacę                                                                                                                   | Wysoki    |
| US-04 | E-02 | Jako użytkownik, chcę usunąć subskrypcję, gdy już z niej nie korzystam                                                                                                                                        | Średni    |
| US-05 | E-02 | Jako użytkownik, chcę jednym kliknięciem dodać stronę, którą właśnie przeglądam, jako nową subskrypcję — bez ręcznego wypełniania formularza                                                                  | Średni    |
| US-06 | E-03 | Jako użytkownik, chcę aby rozszerzenie samo wykrywało, gdy odwiedzam stronę mojej subskrypcji i zaczynało liczyć czas                                                                                         | Wysoki    |
| US-07 | E-03 | Jako użytkownik, chcę aby rozszerzenie przestawało liczyć czas gdy zamykam kartę z subskrypcją                                                                                                                | Wysoki    |
| US-08 | E-03 | Jako użytkownik, chcę aby czas był liczony poprawnie nawet gdy mam otwartych kilka kart tej samej subskrypcji                                                                                                 | Średni    |
| US-09 | E-03 | Jako użytkownik, chcę aby system poprawnie rozpoznawał gdy przełączam się między różnymi subskrypcjami i odpowiednio aktualizował czas                                                                        | Średni    |
| US-10 | E-04 | Jako użytkownik, chcę widzieć na dashboardzie podsumowanie: liczbę subskrypcji, łączny koszt miesięczny i czas użytkowania                                                                                    | Wysoki    |
| US-11 | E-04 | Jako użytkownik, chcę widzieć na wykresie ile czasu spędzam na każdej usłudze, aby porównać którą używam najczęściej                                                                                          | Średni    |
| US-12 | E-04 | Jako użytkownik, chcę widzieć wykres mojej dziennej aktywności, aby sprawdzić w które dni najwięcej korzystam z subskrypcji                                                                                   | Średni    |
| US-13 | E-04 | Jako użytkownik, chcę widzieć na wyskakującym okienku rozszerzenia stan połączenia i zalogowania, aby wiedzieć czy wszystko działa                                                                            | Średni    |
| US-14 | E-04 | Jako użytkownik, chcę szybko sprawdzić na pasku rozszerzenia czy system jest online i czy jestem zalogowany                                                                                                   | Niski     |
| US-15 | E-02 | Jako użytkownik, chcę edytować dane subskrypcji (koszt, cykl, nazwę), aby aktualizować zmieniające się warunki umowy                                                                                          | Wysoki    |
| US-16 | E-04 | Jako użytkownik, chcę zarządzać subskrypcjami bezpośrednio z poziomu dashboardu (dodawanie, edycja, usuwanie), aby mieć wygodny interfejs graficzny                                                           | Wysoki    |
| US-17 | E-04 | Jako użytkownik, chcę przeglądać pełną historię sesji z możliwością filtrowania po dacie i nazwie subskrypcji, aby szczegółowo analizować swoją aktywność                                                     | Średni    |
| US-18 | E-04 | Jako użytkownik, chcę widzieć stronę analityczną z rozbudowanymi wykresami (koszt w czasie, porównanie usług), aby dogłębnie analizować wydatki                                                               | Średni    |
| US-19 | E-01 | Jako nowy użytkownik, chcę zobaczyć krótki przewodnik po aplikacji przy pierwszym logowaniu, aby szybko zrozumieć jak działa system i co mogę w nim zrobić                                                    | Niski     |
| US-20 | E-05 | Jako użytkownik, chcę otrzymać przypomnienie przed zbliżającą się płatnością subskrypcji, aby nie przegapić odnowienia i nie stracić dostępu                                                                  | Wysoki    |
| US-21 | E-05 | Jako użytkownik, chcę dostać powiadomienie gdy nie korzystam z aktywnej subskrypcji dłużej niż miesiąc, aby rozważyć jej anulowanie i zaoszczędzić pieniądze                                                  | Średni    |
| US-22 | E-05 | Jako użytkownik, chcę ustawić miesięczny budżet na subskrypcje, aby dostać ostrzeżenie gdy go przekraczam                                                                                                     | Średni    |
| US-23 | E-06 | Jako użytkownik, chcę wyeksportować raport moich subskrypcji i czasu użytkowania do pliku PDF lub CSV, aby móc przedstawić go księgowemu lub przeanalizować w arkuszu kalkulacyjnym                           | Niski     |
| US-24 | E-06 | Jako użytkownik, chcę zobaczyć obliczony koszt za minutę użytkowania każdej subskrypcji, aby ocenić która usługa jest najbardziej opłacalna                                                                   | Średni    |
| US-25 | E-06 | Jako użytkownik, chcę porównać moje wydatki na subskrypcje z poprzednim miesiącem, aby zobaczyć trend i zmiany w moich nawykach                                                                               | Średni    |
| US-26 | E-07 | Jako użytkownik, chcę kategoryzować subskrypcje (rozrywka, praca, edukacja, zdrowie), aby lepiej rozumieć na co wydaję pieniądze i gdzie mogę ciąć koszty                                                     | Niski     |
| US-27 | E-07 | Jako użytkownik, chcę dostać cotygodniowe podsumowanie (np. w formie maila lub powiadomienia push) z informacją ile czasu spędziłem na subskrypcjach i ile to kosztowało, abym na bieżąco kontrolował wydatki | Niski     |

## 3.2 Techniki szacowania pracy

W projekcie zastosowano technikę Planning Poker opartą na ciągu Fibonacciego, jako jednostkę szacowania — Story Pointy (SP) zamiast szacowania godzinowego. Referencją jest US-14 ("Sprawdzenie statusu online", 1 SP) jako najprostsza — pozostałe historie szacowano względem niej.
## 3.3 Sprinty
### 3.3.1 Sprint 1 — Fundacja projektu

**Cel:** Przygotowanie szkieletu Django, modeli danych, panelu administracyjnego oraz rejestracji użytkownika.

**Czas:** 2 tygodnie (18.03.2026 – 31.03.2026) | **Velocity:** 10 SP

#### Zaakceptowane User Stories

| ID | User Story | SP | Status |
|----|------------|-----|--------|
| US-01 | Jako nowy użytkownik, chcę założyć konto i zalogować się, aby mieć dostęp do moich danych | 5 | Zrealizowane |
| US-02 | Jako użytkownik, chcę dodać subskrypcję (nazwa, koszt, cykl rozliczeniowy), aby śledzić moje wydatki | 3 | Zrealizowane |
| US-03 | Jako użytkownik, chcę zobaczyć listę wszystkich moich subskrypcji, aby wiedzieć za co płacę | 2 | Zrealizowane |

#### Kryteria akceptacji

**US-01:**
- Nowy użytkownik może wypełnić formularz rejestracji (nazwa, hasło) i utworzyć konto
- Po poprawnej rejestracji użytkownik jest automatycznie zalogowany i przekierowany na dashboard
- Użytkownik może zalogować się istniejącym kontem na stronie `/accounts/login/`
- Niepoprawne dane logowania wyświetlają komunikat błędu
- Przycisk wylogowania jest dostępny dla zalogowanego użytkownika

**US-02:**
- Zalogowany użytkownik może dodać subskrypcję przez wysłanie nazwy, URL-a, kosztu i cyklu rozliczeniowego
- Koszt jest przechowywany jako kwota z dwoma miejscami po przecinku (PLN)
- Cykl rozliczeniowy przyjmuje jedną z wartości: miesięczny, kwartalny, roczny
- Pole nazwy subskrypcji nie może być puste

**US-03:**
- Zalogowany użytkownik otrzymuje listę wszystkich swoich aktywnych subskrypcji
- Każdy element listy zawiera: nazwę, URL, koszt, cykl, datę następnej płatności
- Usunięte subskrypcje (nieaktywne) nie są zwracane

#### Testy (Sprint 1)

| ID testu | Funkcja                                        | Opis                                                                                     | Rodzaj       |
| -------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------- | ------------ |
| T1-01    | `test_sign_up_creates_user_and_logs_in`        | Rejestracja nowego użytkownika przez formularz — konto utworzone, automatyczne logowanie | Automatyczny |
| T1-02    | `test_sign_up_empty_fields_returns_errors`     | Próba rejestracji z pustymi polami — formularz zwraca błędy walidacji                    | Automatyczny |
| T1-03    | `test_login_correct_credentials_redirects`     | Logowanie poprawnymi danymi — przekierowanie na dashboard                                | Automatyczny |
| T1-04    | `test_login_wrong_password_shows_error`        | Logowanie błędnym hasłem — komunikat błędu, brak dostępu                                 | Automatyczny |
| T1-05    | `test_create_subscription_via_api`             | Dodanie subskrypcji przez API — status 201, dane zapisane w bazie                        | Automatyczny |
| T1-06    | `test_create_subscription_empty_name_rejected` | Dodanie subskrypcji z pustą nazwą — błąd walidacji                                       | Automatyczny |
| T1-07    | `test_subscription_list_empty_for_new_user`    | Lista subskrypcji dla użytkownika bez subskrypcji — pusta lista                          | Automatyczny |
| T1-08    | `test_subscription_list_isolated_per_user`     | Lista subskrypcji nie zwraca subskrypcji innego użytkownika                              | Automatyczny |
| T1-09    | —                                              | Panel admina dostępny dla superusera — modele widoczne i edytowalne                      | Ręczny       |
| T1-10    | `test_base_html_renders_bootstrap`             | Szablon `base.html` renderuje się z Bootstrap 5                                          | Automatyczny |

**SUMA: 10 testów** (9 automatycznych + 1 ręczny)

---

### 3.3.2 Sprint 2 — Autoryzacja i dashboard

**Cel:** Implementacja strony głównej dashboardu z podsumowaniem, wykresami Chart.js, przewodnikiem dla nowego użytkownika oraz statusem systemu w rozszerzeniu.

**Czas:** 2 tygodnie (01.04.2026 – 14.04.2026) | **Velocity:** 14 SP | **Status:** Ukończone

#### Zaakceptowane User Stories

| ID | User Story | SP | Status |
|----|------------|-----|--------|
| US-10 | Jako użytkownik, chcę widzieć na dashboardzie podsumowanie: liczbę subskrypcji, łączny koszt miesięczny i czas użytkowania | 5 | Zrealizowane |
| US-11 | Jako użytkownik, chcę widzieć na wykresie ile czasu spędzam na każdej usłudze, aby porównać którą używam najczęściej | 3 | Zrealizowane |
| US-12 | Jako użytkownik, chcę widzieć wykres mojej dziennej aktywności, aby sprawdzić w które dni najwięcej korzystam z subskrypcji | 3 | Zrealizowane |
| US-14 | Jako użytkownik, chcę szybko sprawdzić na pasku rozszerzenia czy system jest online i czy jestem zalogowany | 1 | Zrealizowane |
| US-19 | Jako nowy użytkownik, chcę zobaczyć krótki przewodnik po aplikacji przy pierwszym logowaniu, aby szybko zrozumieć jak działa system i co mogę w nim zrobić | 3 | Przesunięte |

#### Kryteria akceptacji

**US-10:**
- Dashboard wyświetla 4 karty statystyk: liczba aktywnych subskrypcji, łączny koszt miesięczny (PLN), czas śledzony (h), liczba wizyt
- Koszt miesięczny normalizuje subskrypcje roczne (/12) i kwartalne (/3)
- Statystyki bazują na ostatnich 30 dniach
- Niezalogowany użytkownik widzi stronę powitalną z przyciskami logowania i rejestracji

**US-11:**
- Wykres słupkowy Chart.js prezentuje czas spędzony na każdej subskrypcji w minutach
- Subskrypcje są posortowane malejąco według czasu
- Wykres renderuje się poprawnie przy braku danych (pusty komunikat)

**US-12:**
- Wykres liniowy Chart.js prezentuje dzienną aktywność (suma minut) z ostatnich 14 dni
- Oś X pokazuje daty, oś Y — minuty
- Dni bez aktywności są pokazane jako wartość 0

**US-14:**
- Rozszerzenie Chrome sprawdza czy backend jest osiągalny (`/api/health/`)
- Status wyświetlany jako zielony (online) lub czerwony (offline) na popupie

**US-19:**
- Przy pierwszym zalogowaniu strona powitalna pokazuje 3-4 kroki (dodaj subskrypcję, zainstaluj rozszerzenie, sprawdź dashboard)
- Przewodnik można zamknąć/pominąć
- Przewodnik nie pokazuje się przy kolejnych logowaniach

#### Testy (Sprint 2)

| ID testu | Funkcja                                        | Opis                                                           | Rodzaj       |
| -------- | ---------------------------------------------- | -------------------------------------------------------------- | ------------ |
| T2-01    | `test_dashboard_authenticated_shows_stats`     | Dashboard zalogowanego użytkownika pokazuje 4 karty statystyk  | Automatyczny |
| T2-02    | `test_dashboard_unauthenticated_shows_landing` | Dashboard niezalogowanego — strona powitalna z przyciskami     | Automatyczny |
| T2-03    | `test_dashboard_monthly_cost_normalization`    | Normalizacja kosztu: subskrypcja 120 PLN/rok → 10 PLN/miesiąc  | Automatyczny |
| T2-04    | —                                              | Wykres słupkowy — poprawne dane dla użytkownika z sesjami      | Ręczny       |
| T2-05    | —                                              | Wykres słupkowy — brak danych (pusty wykres, brak błędu JS)    | Ręczny       |
| T2-06    | —                                              | Wykres liniowy — 14 dni na osi X, wartości w minutach          | Ręczny       |
| T2-07    | —                                              | Wykres liniowy — dni bez sesji mają wartość 0                  | Ręczny       |
| T2-08    | —                                              | Status online/offline w rozszerzeniu po `checkHealth()`        | Ręczny       |
| T2-09    | `test_onboarding_guide_first_login`            | Przewodnik pokazuje się tylko przy pierwszym logowaniu (flaga) | Automatyczny |
| T2-10    | `test_onboarding_guide_dismissed`              | Przewodnik można zamknąć — nie wyświetla się ponownie          | Automatyczny |
| T2-11    | `test_csrf_token_in_requests`                  | CSRF token poprawnie dołączany do żądań z rozszerzenia         | Automatyczny |
| T2-12    | —                                              | Dashboard działa poprawnie w Chrome, Firefox, Edge             | Ręczny       |

**SUMA: 12 testów** (7 automatycznych + 5 ręcznych)

---

### 3.3.3 Sprint 3 — Silnik sesji i API

**Cel:** Implementacja logiki budowania sesji — łączenie zdarzeń otwarcia/zamknięcia kart w kompletne sesje użytkowania, obsługa przypadków brzegowych (wielokartowość, przełączanie między subskrypcjami).

**Czas:** 2 tygodnie (15.04.2026 – 28.04.2026) | **Velocity:** 26 SP | **Status:** Ukończone

#### Zaakceptowane User Stories

| ID | User Story | SP | Status |
|----|------------|-----|--------|
| US-06 | Jako użytkownik, chcę aby rozszerzenie samo wykrywało, gdy odwiedzam stronę mojej subskrypcji i zaczynało liczyć czas | 8 | Zrealizowane |
| US-07 | Jako użytkownik, chcę aby rozszerzenie przestawało liczyć czas gdy zamykam kartę z subskrypcją | 5 | Zrealizowane |
| US-08 | Jako użytkownik, chcę aby czas był liczony poprawnie nawet gdy mam otwartych kilka kart tej samej subskrypcji | 5 | Zrealizowane |
| US-09 | Jako użytkownik, chcę aby system poprawnie rozpoznawał gdy przełączam się między różnymi subskrypcjami i odpowiednio aktualizował czas | 8 | Zrealizowane |

#### Kryteria akceptacji

**US-06:**
- Wysłanie zdarzenia `open` dla URL-a dopasowanego do subskrypcji tworzy rekord `SiteEvent` (typ: "open")
- Jeśli nie istnieje aktywna sesja dla tej subskrypcji, tworzona jest nowa `Session` z `started_at`
- Dopasowanie URL-a działa na podstawie nazwy domeny (np. `netflix.com`), ignorując `www.` i ścieżkę

**US-07:**
- Zdarzenie `close` tworzy rekord `SiteEvent` (typ: "close")
- Jeśli zamknięta karta była jedyną otwartą kartą dla danej subskrypcji, sesja zostaje zamknięta (`ended_at`, `duration_seconds`)
- Czas trwania sesji jest obliczany jako różnica `ended_at - started_at` w sekundach

**US-08:**
- Przy otwarciu drugiej karty tej samej subskrypcji nie tworzy się nowa sesja
- Zamknięcie jednej z kart nie kończy sesji, jeśli pozostałe karty są wciąż otwarte
- Sesja kończy się dopiero po zamknięciu ostatniej karty

**US-09:**
- Przełączenie karty z subskrypcji A na subskrypcję B zamyka sesję A i otwiera sesję B
- Nawigacja w ramach tej samej subskrypcji (inna ścieżka URL) nie przerywa sesji
- Przełączenie na stronę spoza subskrypcji nie zamyka sesji

#### Testy (Sprint 3)

**Testy jednostkowe — `SessionManagerTests` (12 testów, w kodzie źródłowym):**

| ID    | Funkcja                                               | Test                                                           | Rodzaj       |
| ----- | ----------------------------------------------------- | -------------------------------------------------------------- | ------------ |
| T3-01 | `test_open_creates_session`                           | Otwarcie na dopasowanej subskrypcji tworzy SiteEvent i Session | Automatyczny |
| T3-02 | `test_open_no_session_for_unmatched_url`              | Nieznany URL tworzy SiteEvent, ale nie Session                 | Automatyczny |
| T3-03 | `test_open_does_not_duplicate_session`                | Druga karta tej samej subskrypcji nie duplikuje sesji          | Automatyczny |
| T3-04 | `test_close_ends_session_when_last_tab`               | Zamknięcie ostatniej karty kończy sesję z duration > 0         | Automatyczny |
| T3-05 | `test_close_does_not_end_session_when_other_tab_open` | Inna karta wciąż otwarta → sesja trwa                          | Automatyczny |
| T3-06 | `test_close_noop_when_no_active_session`              | Close bez żadnej sesji → brak zmian                            | Automatyczny |
| T3-07 | `test_close_noop_for_unmatched_url`                   | Close na nieznanym URL → tylko SiteEvent                       | Automatyczny |
| T3-08 | `test_switching_to_new_sub_closes_previous_session`   | Przełączenie z Netflix na Spotify zamyka Netflix               | Automatyczny |
| T3-09 | `test_switching_to_same_site_keeps_session`           | Zmiana ścieżki nie przerywa sesji                              | Automatyczny |
| T3-10 | `test_multiple_tabs_different_subs_close_correctly`   | Zamknięcie karty Netflix nie wpływa na sesję Spotify           | Automatyczny |
| T3-11 | `test_get_site_name`                                  | Poprawna ekstrakcja nazwy domeny                               | Automatyczny |
| T3-12 | `test_count_open_tabs`                                | Poprawne zliczanie otwartych kart dla subskrypcji              | Automatyczny |
| T3-13 | `test_post_open_event_creates_session`                | POST single open tworzy sesję                                  | Automatyczny |
| T3-14 | `test_post_close_event_ends_session`                  | Sekwencja open → close kończy sesję z duration                 | Automatyczny |
| T3-15 | `test_batch_events_create_and_close_session`          | POST batch open+close → sesja utworzona                        | Automatyczny |
| T3-16 | `test_batch_close_last_tab_ends_session`              | Batch close kończy sesję                                       | Automatyczny |


**SUMA: 16 testów** (16 automatycznych + 0 ręcznych)

---

### 3.3.4 Sprint 4 — Rozszerzenie i zarządzanie subskrypcjami

**Cel:** Implementacja rozszerzenia Chrome Manifest V3 zintegrowanego z backendem, zarządzanie subskrypcjami (CRUD) z poziomu dashboardu, dodawanie subskrypcji jednym kliknięciem oraz kategoryzacja subskrypcji.

**Czas:** 2 tygodnie (29.04.2026 – 12.05.2026) | **Velocity:** 9 SP | **Status:** Ukończone

#### Zaakceptowane User Stories

| ID    | User Story | SP | Status |
|----|------------|-----|--------|
| US-04 | Jako użytkownik, chcę usunąć subskrypcję, gdy już z niej nie korzystam | 2 | Zrealizowane |
| US-05 | Jako użytkownik, chcę jednym kliknięciem dodać stronę, którą właśnie przeglądam, jako nową subskrypcję — bez ręcznego wypełniania formularza | 5 | Zrealizowane |
| US-13 | Jako użytkownik, chcę widzieć na wyskakującym okienku rozszerzenia stan połączenia i zalogowania, aby wiedzieć czy wszystko działa | 2 | Zrealizowane |
| US-15 | Jako użytkownik, chcę edytować dane subskrypcji (koszt, cykl, nazwę), aby aktualizować zmieniające się warunki umowy | 3 | Przesunięte |
| US-16 | Jako użytkownik, chcę zarządzać subskrypcjami bezpośrednio z poziomu dashboardu (dodawanie, edycja, usuwanie), aby mieć wygodny interfejs graficzny | 8 | Przesunięte |
| US-26 | Jako użytkownik, chcę kategoryzować subskrypcje (rozrywka, praca, edukacja, zdrowie), aby lepiej rozumieć na co wydaję pieniądze i gdzie mogę ciąć koszty | 2 | Przesunięte |

#### Kryteria akceptacji

**US-04:**
- Usunięcie subskrypcji ustawia flagę `is_active=False` (miękkie usunięcie)
- Usunięte subskrypcje nie są zwracane na liście aktywnych, ale dane historyczne (sesje) pozostają
- Użytkownik może usunąć tylko własną subskrypcję

**US-05:**
- Kliknięcie przycisku w popupie rozszerzenia dodaje aktualnie otwartą stronę jako subskrypcję
- Przycisk jest dostępny tylko gdy użytkownik jest zalogowany
- Po dodaniu przycisk zmienia się w "Remove from subscriptions"
- Nazwa subskrypcji jest automatycznie pobierana z domeny strony

**US-13:**
- Popup rozszerzenia pokazuje: status API (online/offline), nazwę zalogowanego użytkownika (lub "Not logged in")

**US-15:**
- Użytkownik może zmienić koszt, cykl rozliczeniowy i nazwę istniejącej subskrypcji
- Zmiana kosztu aktualizuje wyświetlane statystyki miesięczne

**US-16:**
- Dashboard zawiera stronę `/subscriptions/` z listą subskrypcji
- Formularz dodawania subskrypcji (nazwa, URL, koszt, cykl, data następnej płatności)
- Formularz edycji subskrypcji z wstępnie wypełnionymi polami
- Przycisk usuwania z potwierdzeniem ("Czy na pewno?")
- Strona dostępna z nawigacji dashboardu

**US-26:**
- Każda subskrypcja ma pole kategorii (rozrywka, praca, edukacja, zdrowie)
- Dashboard wyświetla podział kosztów według kategorii (wykres kołowy)

#### Testy (Sprint 4)

| ID testu | Funkcja                                          | Opis                                                                    | Rodzaj       |
| -------- | ------------------------------------------------ | ----------------------------------------------------------------------- | ------------ |
| T4-01    | `test_delete_subscription_soft`                  | Soft-delete subskrypcji — `is_active=False`, sesje pozostają            | Automatyczny |
| T4-02    | `test_delete_other_users_subscription_forbidden` | Próba usunięcia cudzej subskrypcji — 404                                | Automatyczny |
| T4-03    | —                                                | Dodanie subskrypcji przez popup rozszerzenia — nowa subskrypcja w bazie | Ręczny       |
| T4-04    | —                                                | Przycisk w popupie zmienia się "Add"/"Remove" w zależności od stanu     | Ręczny       |
| T4-05    | —                                                | Popup pokazuje "Logged as {username}" i zielony status po zalogowaniu   | Ręczny       |
| T4-06    | —                                                | Popup pokazuje "Not logged in" i żółty status dla niezalogowanego       | Ręczny       |
| T4-07    | —                                                | Próba dodania subskrypcji bez logowania — przycisk ukryty               | Ręczny       |
| T4-08    | `test_update_subscription_via_api`               | Edycja subskrypcji — zmiana kosztu, odświeżenie statystyk               | Automatyczny |
| T4-09    | `test_subscription_list_view`                    | Strona `/subscriptions/` — lista z przyciskami Edytuj/Usuń              | Automatyczny |
| T4-10    | `test_subscription_create_view`                  | Formularz dodawania — walidacja pól, zapis do bazy                      | Automatyczny |
| T4-11    | `test_subscription_update_view`                  | Formularz edycji — wstępnie wypełnione pola, zapis zmian                | Automatyczny |
| T4-12    | `test_subscription_delete_view`                  | Usuwanie przez dashboard — potwierdzenie, soft-delete                   | Automatyczny |
| T4-13    | `test_subscription_category_field`               | Przypisanie kategorii do subskrypcji — wykres kołowy                    | Automatyczny |
| T4-14    | —                                                | Service worker nasłuchuje `tabs.onCreated`/`onRemoved`/`onUpdated`      | Ręczny       |
| T4-15    | —                                                | Rozszerzenie poprawnie obsługuje CSRF (token z ciasteczek)              | Ręczny       |
| T4-16    | —                                                | Rozszerzenie działa po przeładowaniu (service worker restart)           | Ręczny       |

**SUMA: 16 testów** (8 automatycznych + 8 ręcznych)

---

### 3.3.5 Sprint 5 — Analityka i powiadomienia

**Cel:** Implementacja zaawansowanych funkcji analitycznych, systemu powiadomień, eksportu danych, integracji zewnętrznych, personalizacji oraz narzędzi jakościowych.

**Czas:** 2 tygodnie (13.05.2026 – 26.05.2026) | **Velocity:** 47 SP | **Status:** Planowany

#### Zaakceptowane User Stories

| ID    | User Story                                                                                                                                                                          | SP  | Status    |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | --------- |
| US-17 | Jako użytkownik, chcę przeglądać pełną historię sesji z możliwością filtrowania po dacie i nazwie subskrypcji, aby szczegółowo analizować swoją aktywność                           | 5   | Planowane |
| US-18 | Jako użytkownik, chcę widzieć stronę analityczną z rozbudowanymi wykresami (koszt w czasie, porównanie usług), aby dogłębnie analizować wydatki                                     | 8   | Planowane |
| US-20 | Jako użytkownik, chcę otrzymać przypomnienie przed zbliżającą się płatnością subskrypcji, aby nie przegapić odnowienia i nie stracić dostępu                                        | 8   | Planowane |
| US-21 | Jako użytkownik, chcę dostać powiadomienie gdy nie korzystam z aktywnej subskrypcji dłużej niż miesiąc, aby rozważyć jej anulowanie i zaoszczędzić pieniądze                        | 5   | Planowane |
| US-22 | Jako użytkownik, chcę ustawić miesięczny budżet na subskrypcje, aby dostać ostrzeżenie gdy go przekraczam                                                                           | 5   | Planowane |
| US-23 | Jako użytkownik, chcę wyeksportować raport moich subskrypcji i czasu użytkowania do pliku PDF lub CSV, aby móc przedstawić go księgowemu lub przeanalizować w arkuszu kalkulacyjnym | 5   | Planowane |
| US-24 | Jako użytkownik, chcę zobaczyć obliczony koszt za minutę użytkowania każdej subskrypcji, aby ocenić która usługa jest najbardziej opłacalna                                         | 3   | Planowane |
| US-25 | Jako użytkownik, chcę porównać moje wydatki na subskrypcje z poprzednim miesiącem, aby zobaczyć trend i zmiany w moich nawykach                                                     | 3   | Planowane |
| US-27 | Jako użytkownik, chcę dostać cotygodniowe podsumowanie z informacją ile czasu spędziłem na subskrypcjach i ile to kosztowało, abym na bieżąco kontrolował wydatki                   | 5   | Planowane |
| US-15 | *(Przesunięte z S4)* Edycja subskrypcji (koszt, cykl, nazwa)                                                                                                                        | 3   | Planowane |
| US-16 | *(Przesunięte z S4)* Zarządzanie subskrypcjami z poziomu dashboardu                                                                                                                 | 8   | Planowane |
| US-19 | *(Przesunięte z S2)* Przewodnik pierwszego logowania                                                                                                                                | 3   | Planowane |
| US-28 | *(Przesunięte z S4)* Kategoryzacja subskrypcji                                                                                                                                      | 2   | Planowane |
#### Kryteria akceptacji

**US-19:**
- Tak jak w sprincie 2

**US-15, US-16, US-28:**
- Tak jak w sprincie 4

**US-17:**
- Strona `/sessions/` wyświetla tabelę sesji z podziałem na strony (20 na stronę)
- Filtry: zakres dat (od/do), wybór subskrypcji z listy rozwijanej, minimalny czas trwania
- Każdy wiersz pokazuje: nazwę subskrypcji, datę rozpoczęcia, czas trwania w minutach

**US-18:**
- Strona `/analytics/` z wykresami Chart.js: koszt całkowity w czasie (miesiące), porównanie koszt vs. czas (wykres punktowy), udział procentowy każdej subskrypcji w całości kosztów (wykres kołowy)
- Filtr zakresu dat: ostatni tydzień, miesiąc, 3 miesiące, niestandardowy

**US-20:**
- System wysyła e-mail 3 dni przed datą następnej płatności
- E-mail zawiera: nazwę subskrypcji, kwotę, datę odnowienia, link do anulowania (dashboard)
- Użytkownik może wyłączyć powiadomienia dla konkretnej subskrypcji

**US-21:**
- System wykrywa subskrypcje, z których użytkownik nie korzystał przez 30+ dni
- Raz w tygodniu wysyłane jest zbiorcze powiadomienie w dashboardzie z listą nieużywanych subskrypcji
- Każda pozycja zawiera przycisk szybkiego usunięcia

**US-22:**
- Użytkownik ustawia miesięczny limit wydatków w ustawieniach
- Gdy suma kosztów przekroczy budżet, na dashboardzie pojawia się ostrzeżenie (żółty/czerwony pasek)
- Ostrzeżenie znika gdy suma spadnie poniżej progu

**US-23:**
- Przycisk "Eksportuj raport" na stronie analityki generuje PDF
- Raport zawiera: listę subskrypcji z kosztami, podsumowanie czasu, wykresy
- Plik PDF można pobrać bezpośrednio z przeglądarki

**US-24:**
- Dashboard wyświetla obok czasu spędzonego koszt za minutę (koszt / czas w minutach)
- Sortowanie subskrypcji od najbardziej do najmniej opłacalnej

**US-25:**
- Sekcja porównawcza na dashboardzie: koszt w tym miesiącu vs. poprzedni miesiąc
- Różnica wyświetlana jako wartość +/- ze strzałką trendu (↑↓)

**US-27:**
- W każdy poniedziałek o 8:00 wysyłane jest e-mailowe podsumowanie tygodnia
- Zawartość: łączny czas, najczęściej używane subskrypcje, łączny koszt w tym tygodniu, porównanie z poprzednim tygodniem

#### Testy (Sprint 5)

| ID testu | Funkcja                                      | Opis                                                                              | Rodzaj       |
| -------- | -------------------------------------------- | --------------------------------------------------------------------------------- | ------------ |
| T5-01    | `test_session_list_pagination`               | Lista sesji z paginacją — strona 2 zwraca kolejne 20 rekordów                     | Automatyczny |
| T5-02    | `test_session_list_filter_by_date`           | Filtr sesji po dacie `?from=2026-05-01&to=2026-05-15` — poprawne zawężenie        | Automatyczny |
| T5-03    | `test_session_list_filter_by_subscription`   | Filtr sesji po subskrypcji `?subscription_id=1` — tylko sesje dla Netflix         | Automatyczny |
| T5-04    | —                                            | Strona analityczna z wykresami — wszystkie 3 wykresy renderują się                | Ręczny       |
| T5-05    | —                                            | Filtr zakresu dat na analityce — zmiana z "miesiąc" na "tydzień"                  | Ręczny       |
| T5-06    | —                                            | Przypomnienie o płatności — e-mail wysłany 3 dni przed datą                       | Ręczny       |
| T5-07    | `test_notification_toggle_per_subscription`  | Wyłączenie powiadomień dla konkretnej subskrypcji                                 | Automatyczny |
| T5-08    | `test_unused_subscription_detection_30_days` | Powiadomienie o nieużywanej subskrypcji (>30 dni bez aktywności)                  | Automatyczny |
| T5-09    | `test_budget_exceeded_warning`               | Ustawienie budżetu 50 PLN, subskrypcje 60 PLN → ostrzeżenie                       | Automatyczny |
| T5-10    | `test_budget_warning_disappears`             | Ostrzeżenie znika gdy koszt spada poniżej budżetu                                 | Automatyczny |
| T5-11    | —                                            | Eksport PDF — plik zawiera wszystkie wymagane sekcje                              | Ręczny       |
| T5-12    | `test_cost_per_minute_calculation`           | Koszt za minutę — poprawna kalkulacja (koszt / czas)                              | Automatyczny |
| T5-13    | `test_monthly_comparison_displayed`          | Porównanie miesięczne — różnica wyświetlona ze strzałką                           | Automatyczny |
| T5-16    | —                                            | Cotygodniowe podsumowanie — e-mail z poprawnymi danymi                            | Ręczny       |
| T5-17    | `test_rate_limiting_on_event_endpoint`       | Rate limiting — ponad 60 req/min na `/api/events/` → 429 Too Many Requests        | Automatyczny |
| T5-18    | `test_user_data_isolation`                   | Brak wycieku danych — użytkownik A nie widzi sesji użytkownika B                  | Automatyczny |
| T5-19    | —                                            | Strona analityki bez danych — komunikaty zamiast pustych wykresów                 | Ręczny       |
| T5-20    | —                                            | Eksport PDF dla użytkownika bez subskrypcji — pusty raport z informacją           | Ręczny       |

**SUMA: 18 testów** (12 automatycznych + 6 ręcznych)

---

## 3.4 Wykres Gantta — realizacja epików

```
Epik   | Nazwa                                  | Mar 18-31 | Kwi 1-14 | Kwi 15-28 | Kwi 29-Maj 12 | Maj 13-26 |
       |                                        |  (S1)     |  (S2)    |  (S3)     |    (S4)       |  (S5)     |
-------|----------------------------------------|-----------|----------|-----------|---------------|-----------|
E-01   | Rejestracja i pierwsze kroki           |██████████████████████|           |               |           |
-------|----------------------------------------|-----------|----------|-----------|---------------|-----------|
E-02   | Zarządzanie listą subskrypcji          |██████████████████████████████████████████████████|           |
-------|----------------------------------------|-----------|----------|-----------|---------------|-----------|
E-03   | Automatyczne śledzenie czasu           |           |          |███████████|               |           |
-------|----------------------------------------|-----------|----------|-----------|---------------|-----------|
E-04   | Podgląd i analiza na dashboardzie      |           |██████████████████████████████████████████████████|
-------|----------------------------------------|-----------|----------|-----------|---------------|-----------|
E-05   | Powiadomienia i alerty                 |           |          |           |               |███████████|
-------|----------------------------------------|-----------|----------|-----------|---------------|-----------|
E-06   | Raportowanie i eksport danych          |           |          |           |               |███████████|
-------|----------------------------------------|-----------|----------|-----------|---------------|-----------|
E-07   | Personalizacja i budżetowanie          |           |          |           |███████████████████████████|
-------|----------------------------------------|-----------|----------|-----------|---------------|-----------|
```

## 3.5 Podsumowanie — Velocity i postęp

| Sprint                 | Cel                            | SP         | Status                                     |
| ---------------------- | ------------------------------ | ---------- | ------------------------------------------ |
| Sprint 1               | Fundacja projektu              | 10         | Ukończone                                  |
| Sprint 2               | Dashboard i autoryzacja        | 14/17      | Częściowo ukończone                        |
| Sprint 3               | Silnik sesji i API             | 26         | Ukończone                                  |
| Sprint 4               | Rozszerzenie i zarządzanie     | 9/22       | Częściowo ukończone                        |
| Sprint 5               | Analityka, jakość, przesunięte | 47         | Planowane (+16 SP przesuniętych z S2 i S4) |
| **Razem zrealizowane** | **Sprinty 1–4**                | **59 SP**  |                                            |
| **Razem planowane**    | **5 sprintów**                 | **106 SP** |                                            |

---

# 4. Dokumentacja techniczna

## 4.1 Schematy logiczne aplikacji

### Architektura systemu

```
┌─────────────────────────────────────────────────────────────────────┐
│                        SUB GUARDIAN SYSTEM                          │
│                                                                     │
│  ┌──────────────────┐      HTTP/JSON      ┌──────────────────────┐  │
│  │  sg-extension    │ ──────────────────► │   sg-webapp          │  │
│  │  (Chrome Ext.)   │ ◄────────────────── │   (Django 6.0)       │  │
│  │                  │   GET subscriptions │                      │  │
│  │  background.js   │                     │  API Views           │  │
│  │  popup UI        │                     │  Session Manager     │  │
│  │  api.js client   │                     │  Dashboard Views     │  │
│  └──────────────────┘                     └──────────┬───────────┘  │
│                                                      │              │
│  ┌──────────────────┐                     ┌──────────▼───────────┐  │
│  │  Użytkownik      │ ◄─────────────────► │   SQLite Database    │  │
│  │  (przeglądarka)  │   Dashboard HTML    │                      │  │
│  │                  │                     │  Subscription        │  │
│  │  Bootstrap 5     │                     │  SiteEvent           │  │
│  │  Chart.js        │                     │  Session             │  │
│  └──────────────────┘                     │  User (Django Auth)  │  │
│                                           └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### Schemat bazy danych (ERD)

```
┌──────────────────────────────────────────────────┐
│                   User                           │
│──────────────────────────────────────────────────│
│ id (PK)                                          │
│ username, email, password, ...                   │
└────────┬────────────────────────────────────────┬┘
         │                                        │
         │ 1:N                                    │ 1:N
         ▼                                        ▼
┌───────────────────────┐     ┌───────────────────────────┐
│    Subscription       │     │      SiteEvent            │
│───────────────────────│     │───────────────────────────│
│ id (PK)               │     │ id (PK)                   │
│ user_id (FK)          │     │ user_id (FK)              │
│ name                  │     │ url                       │
│ url                   │     │ tab_id                    │
│ cost                  │     │ event_type (open/close)   │
│ billing_cycle         │     │ timestamp                 │
│ next_billing_date     │     │ created_at                │
│ is_active             │     │                           │
│ created_at            │     │ INDEX: (user, timestamp)  │
│ updated_at            │     └───────────────────────────┘
└──────────┬────────────┘
           │ 1:N
           ▼
┌───────────────────────┐
│      Session          │
│───────────────────────│
│ id (PK)               │
│ user_id (FK)          │
│ subscription_id (FK)  │
│ url                   │
│ started_at            │
│ ended_at              │
│ duration_seconds      │
│ created_at            │
│ INDEX: (user, sub,    │
│         ended_at)     │
└───────────────────────┘
```

## 4.2 Opis funkcji i komponentów

### Komponent: Backend API (`api/`)

**Modele danych:**

- **`Subscription`** — reprezentuje subskrypcję użytkownika. Pola: `user` (FK do User), `name` (np. "Netflix"), `url` (np. "https://netflix.com"), `cost` (Decimal, max 8 cyfr), `billing_cycle` (CharField: "monthly", "yearly", "quarterly"), `next_billing_date` (Date, nullable), `is_active` (Boolean, default True — soft delete). Kolejność: `-created_at`.

- **`SiteEvent`** — surowe zdarzenie z rozszerzenia. Pola: `user` (FK), `url`, `tab_id` (Integer), `event_type` (CharField: "open" lub "close"), `timestamp` (DateTime), `created_at` (auto_now_add). Indeks na `(user, timestamp)`. Kolejność: `-timestamp`.

- **`Session`** — wyliczona sesja użytkowania. Pola: `user` (FK), `subscription` (FK, nullable, SET_NULL), `url`, `started_at` (DateTime), `ended_at` (DateTime, nullable), `duration_seconds` (Integer, nullable), `created_at` (auto_now_add). Indeks na `(user, subscription, ended_at)`.

**Endpointy REST:** 7 endpointów (szczegóły w sekcji 3.1 Backlog Produktu). Wszystkie zwracają JSON. Mutacje wymagają CSRF.

**Session Manager (`session_manager.py`):** Główna logika biznesowa. Zdarzenia `open` i `close` są przetwarzane przez funkcje `process_open_event` i `process_close_event`. Logika:
1. Ekstrakcja nazwy domeny z URL (`get_site_name`)
2. Dopasowanie do subskrypcji przez porównanie nazwy domeny z `subscription.name` (case-insensitive)
3. Dla zdarzenia `open`: tworzenie SiteEvent + Session jeśli URL pasuje do subskrypcji; obsługa przełączania kart
4. Dla zdarzenia `close`: tworzenie SiteEvent + zamknięcie Session jeśli to ostatnia otwarta karta dla tej subskrypcji

### Komponent: Rozszerzenie Chrome (`sg-extension/`)

- **background.js** — Service worker nasłuchujący `chrome.tabs.onCreated`, `onUpdated`, `onRemoved`. Przy każdym zdarzeniu sprawdza, czy URL pasuje do subskrypcji i wysyła zdarzenie `open`/`close` do backendu.
- **js/api.js** — Klient API z obsługą CSRF (pobiera `csrftoken` z ciasteczek przez `chrome.cookies`).
- **js/helpers.js** — Funkcja `getSiteName(url)` wyodrębnia domenę z URL.
- **popup/popup.html + popup.js** — UI popupu z Bootstrap 5, wyświetla status API, status karty, przycisk dodawania/usuwania subskrypcji.

### Komponent: Dashboard (`dashboard/`)

- **views.py** — `home(request)`: dla zalogowanego użytkownika oblicza statystyki (liczba subskrypcji, koszt miesięczny, czas śledzenia, wizyty) i przekazuje do szablonu. `sign_up(request)`: rejestracja z auto-login.
- **Templates** — `base.html` (szkielet Bootstrap 5), `home.html` (dashboard z kartami statystyk, subskrypcjami, wykresami Chart.js, tabelą sesji), `login.html` i `sign_up.html` (crispy forms).

---

# 5. Implementacja

## 5.1 Lista zrealizowanych User Stories

| ID | User Story | Epik | Sprint | SP | Status |
|----|-----------|------|--------|-----|--------|
| US-01 | Rejestracja i logowanie | E-01 | Sprint 1 | 5 | Zrealizowane |
| US-02 | Dodawanie subskrypcji | E-02 | Sprint 1 | 3 | Zrealizowane |
| US-03 | Lista subskrypcji | E-02 | Sprint 1 | 2 | Zrealizowane |
| US-10 | Dashboard z podsumowaniem | E-04 | Sprint 2 | 5 | Zrealizowane |
| US-11 | Wykres czasu na usługę | E-04 | Sprint 2 | 3 | Zrealizowane |
| US-12 | Wykres aktywności dziennej | E-04 | Sprint 2 | 3 | Zrealizowane |
| US-14 | Status online w rozszerzeniu | E-04 | Sprint 2 | 1 | Zrealizowane |
| US-06 | Automatyczne wykrywanie odwiedzin | E-03 | Sprint 3 | 8 | Zrealizowane |
| US-07 | Kończenie liczenia czasu | E-03 | Sprint 3 | 5 | Zrealizowane |
| US-08 | Obsługa wielu kart | E-03 | Sprint 3 | 5 | Zrealizowane |
| US-09 | Przełączanie między subskrypcjami | E-03 | Sprint 3 | 8 | Zrealizowane |
| US-04 | Usuwanie subskrypcji | E-02 | Sprint 4 | 2 | Zrealizowane |
| US-05 | Jedno-kliknięcie dodawania z otwartej strony | E-02 | Sprint 4 | 5 | Zrealizowane |
| US-13 | Stan połączenia w popupie rozszerzenia | E-04 | Sprint 4 | 2 | Zrealizowane |
| US-15 | Edycja subskrypcji | E-02 | Sprint 4 | 3 | Przesunięte (Sprint 5) |
| US-16 | Zarządzanie subskrypcjami z dashboardu | E-04 | Sprint 4 | 8 | Przesunięte (Sprint 5) |
| US-19 | Przewodnik dla nowego użytkownika | E-01 | Sprint 2 | 3 | Przesunięte (Sprint 5) |
| US-28 | Kategoryzacja subskrypcji | E-08 | Sprint 4 | 2 | Przesunięte (Sprint 5) |

**Podsumowanie:** 14 User Stories zrealizowanych (59 SP), 4 przesunięte do Sprintu 5 (16 SP).

## 5.2 Technologie użyte w projekcie

| Technologia               | Wersja      | Zastosowanie                             |
| ------------------------- | ----------- | ---------------------------------------- |
| **Python**                | 3.13        | Język programowania backendu             |
| **Django**                | 6.0         | Framework webowy (MVC, ORM, auth, admin) |
| **SQLite**                | 3.x         | Baza danych                              |
| **uv**                    | najnowsza   | Zarządzanie zależnościami i środowiskiem |
| **django-crispy-forms**   | 2.x         | Renderowanie formularzy Bootstrap 5      |
| **crispy-bootstrap5**     | 2026.x      | Template pack dla crispy-forms           |
| **Bootstrap 5**           | 5.3.8       | CSS framework (CDN)                      |
| **Chart.js**              | 4.4.7       | Wykresy JavaScript (CDN)                 |
| **Chrome Extensions API** | Manifest V3 | API przeglądarki Chrome                  |
| **Git**                   | —           | Kontrola wersji                          |

## 5.3 Problemy napotkane podczas implementacji i ich rozwiązania

| Problem                                | Przyczyna                                                                        | Rozwiązanie                                                                                                                        |
| -------------------------------------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Brak URL-a w `tabs.onRemoved`          | Chrome nie przekazuje URL przy zamknięciu karty                                  | Utrzymywanie cache `tabUrls` (Map<tabId, url>) aktualizowanej w `onCreated` i `onUpdated`                                          |
| Błąd CSRF                              | Django domyślnie wymaga tokenów CSRF dla zapytań POST                            | Dodanie chrome-extension:// origin do `CSRF_TRUSTED_ORIGINS`; pobieranie CSRF tokena z ciasteczek przez `chrome.cookies`           |
| Sesja zamykana za wcześnie             | Przy wielu kartach jedna subskrypcja była zamykana po zamknięciu pierwszej karty | Implementacja `count_open_tabs_for_subscription` — sesja kończy się dopiero gdy wszystkie karty dla danej subskrypcji są zamknięte |
| Podwójne otwarcie sesji                | Przeładowanie strony generowało nowe `open` zdarzenie                            | Session tworzona tylko gdy nie ma aktywnej (bez `ended_at`) sesji dla tej subskrypcji                                              |
| Przełączanie kart między subskrypcjami | Ta sama karta mogła najpierw pokazywać Netflix, potem Spotify                    | Implementacja `_close_previous_site_for_tab` — przed otwarciem nowej sesji zamykana jest poprzednia dla tego tab_id                |
| Nazwa domeny a subskrypcja             | Różne URL-e (www.netflix.com, netflix.com/movie)                                 | Funkcja `getSiteName` wyodrębnia ostatnie 2 części hostname                                                                        |
| Koszt miesięczny dla różnych cykli     | Subskrypcje roczne/kwartalne mają inny koszt niż miesięczne                      | Normalizacja: roczny/12, kwartalny/3, miesięczny/1                                                                                 |

---

# 6. Testowanie i jakość

## 6.1 Rodzaje testów automatycznych

| Rodzaj testu     | Ilość | Co sprawdza                                                                                                   |
| ---------------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| **Jednostkowe**  | 29    | Logika sesji (12), API CRUD subskrypcji (6), autoryzacja i health (3), zdarzenia API dodatkowe (3), batch (3) |
| **Integracyjne** | 16    | Widok dashboardu (7), rejestracja (2), logowanie (2), renderowanie (1), API przez HTTP (4)                    |

Wszystkie testy automatyczne znajdują się w plikach `sg-webapp/src/api/tests.py` (33 testy) oraz `sg-webapp/src/dashboard/tests.py` (12 testów).

## 6.2 Dokumentacja testowa — testy manualne

Scenariusze testów automatycznych (wraz z nazwami funkcji w kodzie źródłowym) zostały szczegółowo opisane w punkcie 3.3 (Sprinty). Poniżej znajduje się dokumentacja wyłącznie testów ręcznych — z warunkami wstępnymi, danymi testowymi i szczegółowymi krokami.

### T1-09: Panel administracyjny Django

| Pole | Wartość |
|------|---------|
| **ID** | T1-09 |
| **Sprint** | Sprint 1 — Fundacja projektu |
| **Nazwa** | Panel admina dostępny dla superusera — modele widoczne i edytowalne |
| **Warunki wstępne** | Serwer uruchomiony (`runserver`); utworzony superuser (`createsuperuser`); modele `Subscription`, `SiteEvent`, `Session` istnieją w bazie |
| **Dane testowe** | Superuser: `admin` / hasło testowe |
| **Kroki** | 1. Otwórz `http://127.0.0.1:8000/admin/` w przeglądarce<br>2. Zaloguj się jako superuser<br>3. Sprawdź, czy w panelu widoczne są modele: Subscriptions, Site Events, Sessions<br>4. Kliknij "Subscriptions" → zweryfikuj, że lista subskrypcji jest widoczna<br>5. Kliknij "Dodaj subscription" → zweryfikuj, że formularz dodawania działa<br>6. Powtórz krok 4–5 dla Site Events i Sessions |
| **Oczekiwany rezultat** | Wszystkie 3 modele widoczne w panelu admina; formularze dodawania/edycji działają; zapis do bazy poprawny |

### T2-04: Wykres słupkowy — dane dla użytkownika z sesjami

| Pole | Wartość |
|------|---------|
| **ID** | T2-04 |
| **Sprint** | Sprint 2 — Dashboard i autoryzacja |
| **Nazwa** | Wykres słupkowy Chart.js — poprawne dane dla użytkownika z sesjami |
| **Warunki wstępne** | Zalogowany użytkownik z co najmniej 2 subskrypcjami; w bazie istnieją sesje dla tych subskrypcji (różne czasy trwania) |
| **Dane testowe** | Netflix: 3 sesje (łącznie 120 min); Spotify: 2 sesje (łącznie 45 min); HBO: 1 sesja (15 min) |
| **Kroki** | 1. Zaloguj się i przejdź na `/home/`<br>2. Znajdź wykres słupkowy `#timeChart`<br>3. Sprawdź etykiety osi X — powinny zawierać nazwy subskrypcji (Netflix, Spotify, HBO)<br>4. Sprawdź wysokości słupków — Netflix najwyższy (120), HBO najniższy (15)<br>5. Zweryfikuj, że kolejność słupków jest malejąca według czasu |
| **Oczekiwany rezultat** | Wykres słupkowy renderuje się poprawnie; słupki odpowiadają rzeczywistym danym; etykiety czytelne |

### T2-05: Wykres słupkowy — brak danych

| Pole | Wartość |
|------|---------|
| **ID** | T2-05 |
| **Sprint** | Sprint 2 — Dashboard i autoryzacja |
| **Nazwa** | Wykres słupkowy — brak danych (pusty wykres, brak błędu JS) |
| **Warunki wstępne** | Zalogowany użytkownik bez żadnych zakończonych sesji (lub bez subskrypcji) |
| **Dane testowe** | Brak sesji z `ended_at != null` |
| **Kroki** | 1. Zaloguj się na konto bez sesji<br>2. Przejdź na `/home/`<br>3. Otwórz konsolę deweloperską przeglądarki (F12)<br>4. Sprawdź, czy w konsoli nie ma błędów JS<br>5. Zweryfikuj, że obszar wykresu nie jest pusty — wyświetla się informacja o braku danych |
| **Oczekiwany rezultat** | Brak błędów JavaScript; wykres renderuje się z komunikatem "brak danych" lub pustą osią |

### T2-06: Wykres liniowy — 14 dni na osi X

| Pole | Wartość |
|------|---------|
| **ID** | T2-06 |
| **Sprint** | Sprint 2 — Dashboard i autoryzacja |
| **Nazwa** | Wykres liniowy aktywności dziennej — 14 dni na osi X, wartości w minutach |
| **Warunki wstępne** | Zalogowany użytkownik z sesjami rozłożonymi na ostatnie 14 dni |
| **Dane testowe** | Sesje w dniach: dzisiaj (30 min), 2 dni temu (60 min), 5 dni temu (15 min), 10 dni temu (90 min) |
| **Kroki** | 1. Zaloguj się i przejdź na `/home/`<br>2. Znajdź wykres liniowy `#dailyChart`<br>3. Policz liczbę punktów na osi X — powinno być 14 etykiet (daty)<br>4. Najedź kursorem na punkty z danymi — sprawdź, czy tooltip pokazuje datę i minuty<br>5. Sprawdź dni bez sesji — powinny mieć wartość 0 na osi Y |
| **Oczekiwany rezultat** | Oś X zawiera 14 dat; punkty danych odpowiadają sesjom; tooltip działa; dni bez sesji = 0 |

### T2-07: Wykres liniowy — dni zerowe

| Pole | Wartość |
|------|---------|
| **ID** | T2-07 |
| **Sprint** | Sprint 2 — Dashboard i autoryzacja |
| **Nazwa** | Wykres liniowy — dni bez sesji mają wartość 0 |
| **Warunki wstępne** | Zalogowany użytkownik z sesjami tylko w 2 z ostatnich 14 dni |
| **Dane testowe** | Sesje tylko w dniu dzisiejszym i 7 dni temu; pozostałe 12 dni bez sesji |
| **Kroki** | 1. Zaloguj się na konto z rzadkimi sesjami<br>2. Przejdź na `/home/`<br>3. Znajdź wykres liniowy `#dailyChart`<br>4. Sprawdź, czy linia opada do 0 w dniach bez sesji<br>5. Zweryfikuj, że w dniach z sesjami linia wznosi się do odpowiedniej wartości |
| **Oczekiwany rezultat** | Linia łączy punkty danych; dni bez sesji = 0 na osi Y; brak skoków/artefaktów |

### T2-08: Status online/offline w rozszerzeniu

| Pole | Wartość |
|------|---------|
| **ID** | T2-08 |
| **Sprint** | Sprint 2 — Dashboard i autoryzacja |
| **Nazwa** | Status online/offline w popupie rozszerzenia |
| **Warunki wstępne** | Rozszerzenie Chrome załadowane (unpacked); serwer Django uruchomiony na `127.0.0.1:8000` |
| **Dane testowe** | — |
| **Kroki** | 1. Uruchom serwer Django<br>2. Kliknij ikonę rozszerzenia Sub Guardian → popup powinien pokazać zielony status "Online"<br>3. Zatrzymaj serwer Django (Ctrl+C)<br>4. Ponownie kliknij ikonę rozszerzenia → popup powinien pokazać czerwony status "Offline"<br>5. Uruchom ponownie serwer, odśwież popup → status powinien wrócić do "Online" |
| **Oczekiwany rezultat** | Status zmienia się dynamicznie: zielony "Online" gdy serwer działa, czerwony "Offline" gdy nie |

### T2-12: Kompatybilność między przeglądarkami

| Pole | Wartość |
|------|---------|
| **ID** | T2-12 |
| **Sprint** | Sprint 2 — Dashboard i autoryzacja |
| **Nazwa** | Dashboard działa poprawnie w Chrome, Firefox, Edge |
| **Warunki wstępne** | Serwer dostępny na `127.0.0.1:8000`; konto testowe utworzone |
| **Dane testowe** | Konto: `testuser` / `pass123` z subskrypcjami i sesjami |
| **Kroki** | 1. W Chrome: otwórz `/home/`, zaloguj się, sprawdź renderowanie kart i wykresów<br>2. W Firefox: powtórz krok 1<br>3. W Edge: powtórz krok 1<br>4. W każdej przeglądarce sprawdź: formularz logowania, dashboard, wykresy Chart.js, responsywność na mobile (DevTools) |
| **Oczekiwany rezultat** | Wszystkie elementy UI renderują się identycznie w 3 przeglądarkach; wykresy Chart.js działają; responsywność zachowana |

### T4-03: Dodanie subskrypcji jednym kliknięciem przez popup

| Pole | Wartość |
|------|---------|
| **ID** | T4-03 |
| **Sprint** | Sprint 4 — Rozszerzenie i zarządzanie |
| **Nazwa** | Popup — dodanie subskrypcji jednym kliknięciem z otwartej strony |
| **Warunki wstępne** | Zalogowany użytkownik w rozszerzeniu; otwarta karta z nową stroną (np. `hbogo.pl`) niebędącą jeszcze subskrypcją |
| **Dane testowe** | Karta: `https://hbogo.pl`; nazwa domeny: `hbogo.pl` |
| **Kroki** | 1. Otwórz `https://hbogo.pl` w nowej karcie<br>2. Kliknij ikonę rozszerzenia Sub Guardian<br>3. Sprawdź, czy popup pokazuje "Active tab is not in any subscription" (żółty)<br>4. Kliknij przycisk "Add to subscriptions"<br>5. Odśwież stronę dashboardu `/home/` → sprawdź, czy `hbogo.pl` pojawiło się na liście |
| **Oczekiwany rezultat** | Po kliknięciu "Add" subskrypcja `hbogo.pl` zostaje dodana; widoczna na dashboardzie i w API |

### T4-04: Przycisk Add/Remove — dynamiczna zmiana stanu

| Pole | Wartość |
|------|---------|
| **ID** | T4-04 |
| **Sprint** | Sprint 4 — Rozszerzenie i zarządzanie |
| **Nazwa** | Przycisk w popupie zmienia tekst "Add"/"Remove" w zależności od stanu subskrypcji |
| **Warunki wstępne** | Zalogowany użytkownik; subskrypcja `netflix.com` istnieje w bazie |
| **Dane testowe** | Karta: `https://netflix.com` (subskrybowana); karta: `https://spotify.com` (nie-subskrybowana) |
| **Kroki** | 1. Otwórz kartę `netflix.com`, kliknij ikonę rozszerzenia → przycisk powinien mówić "Remove from subscriptions"<br>2. Otwórz kartę `spotify.com`, kliknij ikonę → przycisk powinien mówić "Add to subscriptions"<br>3. Na karcie `spotify.com` kliknij "Add" → przycisk powinien zmienić się na "Remove"<br>4. Kliknij "Remove" → przycisk powinien wrócić do "Add" |
| **Oczekiwany rezultat** | Przycisk dynamicznie zmienia tekst i akcję; stan subskrypcji aktualizuje się natychmiast |

### T4-05: Popup — status zalogowanego użytkownika

| Pole                    | Wartość                                                                                                                                                                                                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ID**                  | T4-05                                                                                                                                                                                                                                                                                                                              |
| **Sprint**              | Sprint 4 — Rozszerzenie i zarządzanie                                                                                                                                                                                                                                                                                              |
| **Nazwa**               | Popup pokazuje "Logged as {username}" z zielonym statusem                                                                                                                                                                                                                                                                          |
| **Warunki wstępne**     | Użytkownik zalogowany w przeglądarce na `127.0.0.1:8000` (session cookie aktywny)                                                                                                                                                                                                                                                  |
| **Dane testowe**        | Konto: `testuser`                                                                                                                                                                                                                                                                                                                  |
| **Kroki**               | 1. Zaloguj się w przeglądarce na `127.0.0.1:8000/auth/login/` jako `testuser` hasłem `testpassword`<br>2. Kliknij ikonę rozszerzenia<br>3. Sprawdź pierwszy wiersz statusu — powinien być zielony "Online"<br>4. Sprawdź drugi wiersz — powinien być zielony "Logged as testuser"<br>5. Sprawdź, czy przycisk toggle jest widoczny |
| **Oczekiwany rezultat** | Status API: zielony "Online"; status auth: zielony "Logged as testuser"; przycisk toggle widoczny                                                                                                                                                                                                                                  |

### T4-06: Popup — status niezalogowanego użytkownika

| Pole                    | Wartość                                                                                                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ID**                  | T4-06                                                                                                                                                                                                                    |
| **Sprint**              | Sprint 4 — Rozszerzenie i zarządzanie                                                                                                                                                                                    |
| **Nazwa**               | Popup pokazuje "Not logged in" z żółtym statusem                                                                                                                                                                         |
| **Warunki wstępne**     | Użytkownik nie zalogowany (brak session cookie lub cookie wygasł)                                                                                                                                                        |
| **Dane testowe**        | —                                                                                                                                                                                                                        |
| **Kroki**               | 1. Wyczyść ciasteczka dla `127.0.0.1:8000` lub otwórz okno incognito<br>2. Kliknij ikonę rozszerzenia<br>3. Sprawdź wiersz statusu — powinien być żółty "Not logged in"<br>4. Sprawdź, czy przycisk `toggle` jest ukryty |
| **Oczekiwany rezultat** | Status API: zielony "Online"; status auth: żółty "Not logged in"; przycisk `toggle` niewidoczny                                                                                                                          |

### T4-07: Przycisk ukryty przy braku logowania

| Pole | Wartość |
|------|---------|
| **ID** | T4-07 |
| **Sprint** | Sprint 4 — Rozszerzenie i zarządzanie |
| **Nazwa** | Próba dodania subskrypcji bez logowania — przycisk ukryty |
| **Warunki wstępne** | Użytkownik niezalogowany; otwarta dowolna karta |
| **Dane testowe** | Karta: `https://netflix.com` |
| **Kroki** | 1. Upewnij się, że nie jesteś zalogowany (popup pokazuje "Not logged in")<br>2. Otwórz kartę `netflix.com`<br>3. Kliknij ikonę rozszerzenia<br>4. Sprawdź, czy przycisk toggle NIE jest widoczny<br>5. Sprawdź, czy nie ma innej ścieżki pozwalającej dodać subskrypcję bez logowania |
| **Oczekiwany rezultat** | Przycisk toggle ukryty; brak możliwości modyfikacji subskrypcji bez logowania |

### T4-14: Service worker — nasłuchiwanie zdarzeń kart

| Pole | Wartość |
|------|---------|
| **ID** | T4-14 |
| **Sprint** | Sprint 4 — Rozszerzenie i zarządzanie |
| **Nazwa** | Service worker nasłuchuje `onCreated`, `onRemoved`, `onUpdated` |
| **Warunki wstępne** | Rozszerzenie załadowane i aktywne; serwer uruchomiony; użytkownik zalogowany; subskrypcja `netflix.com` istnieje |
| **Dane testowe** | URL: `https://netflix.com` |
| **Kroki** | 1. Otwórz `chrome://extensions/`, kliknij "Service Worker" dla Sub Guardian — otwórz konsolę SW<br>2. W nowej karcie otwórz `https://netflix.com` → w konsoli SW powinien pojawić się log "Tab created" z `isSubscription: true`<br>3. Przejdź na `https://netflix.com/browse` → powinien pojawić się log "Tab updated (loaded)"<br>4. Zamknij kartę → powinien pojawić się log "Tab removed" z `isSubscription: true`<br>5. Sprawdź w panelu admina Django, czy powstały zdarzenia `SiteEvent` z odpowiednimi typami |
| **Oczekiwany rezultat** | Zdarzenia `open` przy tworzeniu/aktualizacji karty, `close` przy zamknięciu; logi w konsoli SW; SiteEvent w bazie |

### T4-15: Rozszerzenie — obsługa CSRF

| Pole | Wartość |
|------|---------|
| **ID** | T4-15 |
| **Sprint** | Sprint 4 — Rozszerzenie i zarządzanie |
| **Nazwa** | Rozszerzenie poprawnie obsługuje CSRF (token z ciasteczek) |
| **Warunki wstępne** | Użytkownik zalogowany; rozszerzenie aktywne; serwer z `CSRF_TRUSTED_ORIGINS` zawierającym origin rozszerzenia |
| **Dane testowe** | Subskrypcja: `netflix.com` |
| **Kroki** | 1. Zaloguj się w przeglądarce (session cookie + csrftoken cookie ustawione)<br>2. Otwórz kartę `netflix.com` — zdarzenie `open` powinno zostać wysłane<br>3. Sprawdź w konsoli SW, czy żądanie POST `/api/events/` nie zwróciło 403<br>4. W DevTools (Network) sprawdź nagłówki żądania — powinien zawierać `X-CSRFToken`<br>5. Usuń ciasteczko `csrftoken`, odśwież kartę — żądanie powinno zawieść z 403 |
| **Oczekiwany rezultat** | Żądania z poprawnym tokenem CSRF przechodzą (201); bez tokena — 403 Forbidden |

### T4-16: Service worker — restart

| Pole | Wartość |
|------|---------|
| **ID** | T4-16 |
| **Sprint** | Sprint 4 — Rozszerzenie i zarządzanie |
| **Nazwa** | Rozszerzenie działa po przeładowaniu (service worker restart) |
| **Warunki wstępne** | Rozszerzenie aktywne; użytkownik zalogowany; subskrypcje załadowane |
| **Dane testowe** | — |
| **Kroki** | 1. Zweryfikuj, że rozszerzenie działa (otwórz/zamknij kartę z subskrypcją — event wysłany)<br>2. W `chrome://extensions/` kliknij przycisk odświeżenia rozszerzenia<br>3. Poczekaj aż service worker się zrestartuje<br>4. Ponownie otwórz/zamknij kartę z subskrypcją<br>5. Sprawdź, czy zdarzenie zostało poprawnie wysłane (SiteEvent w bazie) |
| **Oczekiwany rezultat** | Po restarcie SW rozszerzenie nadal nasłuchuje zdarzeń kart i wysyła je poprawnie |

### T5-04: Strona analityczna — wykresy

| Pole | Wartość |
|------|---------|
| **ID** | T5-04 |
| **Sprint** | Sprint 5 — Analityka i jakość (planowane) |
| **Nazwa** | Strona analityczna — wszystkie 3 wykresy renderują się poprawnie |
| **Warunki wstępne** | Zalogowany użytkownik z subskrypcjami i sesjami z ostatnich 3 miesięcy; strona `/analytics/` zaimplementowana |
| **Dane testowe** | 3 subskrypcje; sesje rozłożone na 3 miesiące; różne koszty |
| **Kroki** | 1. Przejdź na `/analytics/`<br>2. Sprawdź, czy renderuje się wykres kosztu całkowitego w czasie (liniowy)<br>3. Sprawdź, czy renderuje się wykres porównania koszt vs. czas (punktowy)<br>4. Sprawdź, czy renderuje się wykres kołowy udziału % każdej subskrypcji<br>5. Zweryfikuj brak błędów w konsoli JS |
| **Oczekiwany rezultat** | 3 wykresy Chart.js widoczne; dane zgodne z bazą; brak błędów JS |

### T5-05: Analityka — filtr zakresu dat

| Pole | Wartość |
|------|---------|
| **ID** | T5-05 |
| **Sprint** | Sprint 5 — Analityka i jakość (planowane) |
| **Nazwa** | Filtr zakresu dat na analityce — zmiana z "miesiąc" na "tydzień" |
| **Warunki wstępne** | Strona `/analytics/` z kontrolką wyboru zakresu dat (dropdown: tydzień/miesiąc/3 miesiące) |
| **Dane testowe** | Sesje z ostatnich 90 dni |
| **Kroki** | 1. Otwórz `/analytics/` z domyślnym zakresem "miesiąc"<br>2. Zanotuj wartości na wykresach<br>3. Zmień zakres na "tydzień"<br>4. Sprawdź, czy dane na wykresach zawęziły się do ostatnich 7 dni<br>5. Zmień na "3 miesiące" → sprawdź, czy dane rozszerzyły się |
| **Oczekiwany rezultat** | Wykresy aktualizują się dynamicznie; dane odpowiadają wybranemu zakresowi dat |

### T5-06: Przypomnienie o płatności — e-mail

| Pole | Wartość |
|------|---------|
| **ID** | T5-06 |
| **Sprint** | Sprint 5 — Analityka i jakość (planowane) |
| **Nazwa** | Przypomnienie o płatności — e-mail wysłany 3 dni przed datą odnowienia |
| **Warunki wstępne** | Subskrypcja z `next_billing_date` ustawioną na datę za 3 dni; system powiadomień e-mail skonfigurowany |
| **Dane testowe** | Subskrypcja Netflix: `next_billing_date = dzisiaj + 3 dni`; e-mail użytkownika: `test@example.com` |
| **Kroki** | 1. Ustaw `next_billing_date` subskrypcji na datę za 3 dni<br>2. Uruchom zadanie cron / komendę wysyłającą przypomnienia<br>3. Sprawdź skrzynkę e-mail `test@example.com`<br>4. Zweryfikuj treść e-maila: nazwa subskrypcji, kwota, data odnowienia, link do dashboardu |
| **Oczekiwany rezultat** | E-mail dotarł; zawiera nazwę subskrypcji (Netflix), kwotę, datę i link do anulowania |

### T5-11: Eksport raportu do PDF

| Pole | Wartość |
|------|---------|
| **ID** | T5-11 |
| **Sprint** | Sprint 5 — Analityka i jakość (planowane) |
| **Nazwa** | Eksport raportu do PDF — plik zawiera wszystkie wymagane sekcje |
| **Warunki wstępne** | Zalogowany użytkownik z subskrypcjami i sesjami; przycisk "Eksportuj raport" na stronie analityki |
| **Dane testowe** | 2 subskrypcje, 5 sesji, łączny koszt miesięczny 39.99 PLN |
| **Kroki** | 1. Przejdź na `/analytics/`<br>2. Kliknij "Eksportuj raport"<br>3. Zapisz pobrany plik PDF<br>4. Otwórz PDF i sprawdź: listę subskrypcji z kosztami, podsumowanie czasu, wykresy, datę wygenerowania<br>5. Zweryfikuj, czy dane w PDF są zgodne z danymi na ekranie |
| **Oczekiwany rezultat** | PDF zawiera: listę subskrypcji, podsumowanie czasu, wykresy, datę; dane zgodne z dashboardem |

### T5-16: Cotygodniowe podsumowanie — e-mail

| Pole | Wartość |
|------|---------|
| **ID** | T5-16 |
| **Sprint** | Sprint 5 — Analityka i jakość (planowane) |
| **Nazwa** | Cotygodniowe podsumowanie — e-mail z poprawnymi danymi |
| **Warunki wstępne** | Użytkownik z subskrypcjami i sesjami w ostatnim tygodniu; system e-mail skonfigurowany |
| **Dane testowe** | Tydzień: 3 sesje Netflix (90 min), 2 sesje Spotify (45 min); łączny koszt: 30 PLN |
| **Kroki** | 1. Wygeneruj sesje dla ostatniego tygodnia<br>2. Uruchom zadanie wysyłające podsumowania tygodniowe (poniedziałek 8:00)<br>3. Sprawdź skrzynkę e-mail<br>4. Zweryfikuj: łączny czas (135 min), najczęściej używana subskrypcja (Netflix), łączny koszt (30 PLN), porównanie z poprzednim tygodniem |
| **Oczekiwany rezultat** | E-mail zawiera poprawne dane tygodniowe; porównanie z poprzednim tygodniem obecne |

### T5-19: Analityka — brak danych

| Pole | Wartość |
|------|---------|
| **ID** | T5-19 |
| **Sprint** | Sprint 5 — Analityka i jakość (planowane) |
| **Nazwa** | Strona analityki bez danych — komunikaty zamiast pustych wykresów |
| **Warunki wstępne** | Zalogowany użytkownik bez subskrypcji lub bez sesji |
| **Dane testowe** | Konto bez subskrypcji |
| **Kroki** | 1. Zaloguj się na puste konto<br>2. Przejdź na `/analytics/`<br>3. Sprawdź, czy zamiast pustych wykresów wyświetlane są komunikaty (np. "Brak danych do wyświetlenia")<br>4. Sprawdź konsolę JS — brak błędów |
| **Oczekiwany rezultat** | Komunikaty "brak danych" zamiast pustych wykresów; brak błędów JS |

### T5-20: Eksport PDF — pusty użytkownik

| Pole | Wartość |
|------|---------|
| **ID** | T5-20 |
| **Sprint** | Sprint 5 — Analityka i jakość (planowane) |
| **Nazwa** | Eksport PDF dla użytkownika bez subskrypcji — pusty raport z informacją |
| **Warunki wstępne** | Zalogowany użytkownik bez subskrypcji i sesji |
| **Dane testowe** | Puste konto |
| **Kroki** | 1. Zaloguj się na puste konto<br>2. Przejdź na `/analytics/`, kliknij "Eksportuj raport"<br>3. Otwórz pobrany PDF<br>4. Sprawdź, czy PDF zawiera informację "Brak danych" zamiast pustych sekcji<br>5. Sprawdź, czy data wygenerowania jest obecna |
| **Oczekiwany rezultat** | PDF wygenerowany poprawnie; zawiera komunikat o braku danych; nie jest całkowicie pusty |

## 6.3 Bug Tracking
### Naprawione błędy

| ID      | Tytuł                                                 | Wpływ  | Priorytet | Rozwiązanie                                                                            |
| ------- | ----------------------------------------------------- | ------ | --------- | -------------------------------------------------------------------------------------- |
| BUG-001 | Sesja zamykana przy zamknięciu pierwszej z wielu kart | Wysoki | Wysoki    | Dodano `count_open_tabs_for_subscription` — sesja zamykana dopiero po ostatniej karcie |
| BUG-002 | Podwójna sesja przy przeładowaniu karty               | Średni | Średni    | Sprawdzanie czy istnieje aktywna sesja przed utworzeniem nowej                         |
| BUG-003 | CSRF 403 Forbidden z rozszerzenia                     | Wysoki | Średni    | Dodanie rozszerzenia do `CSRF_TRUSTED_ORIGINS` + pobieranie CSRF tokena z ciasteczek   |
| BUG-004 | Brak URL w `tabs.onRemoved`                           | Wysoki | Wysoki    | Utrzymywanie cache tabUrls (Map)                                                       |
| BUG-005 | Przełączanie kart nie zamyka poprzedniej sesji        | Średni | Średni    | Dodano `_close_previous_site_for_tab`                                                  |
| BUG-006 | Błędna nazwa domeny dla www.example.com               | Niski  | Średni    | Funkcja `getSiteName` bierze ostatnie 2 części hostname zamiast całego                 |
| BUG-007 | Koszt miesięczny nie uwzględnia cyklu rocznego        | Niski  | Średni    | Dodano normalizację kosztu: yearly/12, quarterly/3                                     |
### Błędy do naprawy

#### BUG-008: Sesja nie tworzy się po dodaniu subskrypcji przez wtyczkę, gdy karta jest już otwarta

| Pole                        | Wartość                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ID**                      | BUG-008                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Tytuł**                   | Brak automatycznego wysłania zdarzenia `open` po dodaniu subskrypcji przez wtyczkę na aktywnej karcie                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Wpływ**                   | Średni                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Priorytet**               | Wysoki                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Środowisko**              | Rozszerzenie Chrome (Manifest V3) v1.0.2; backend Django 6.0 na `127.0.0.1:8000`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Opis**                    | Gdy użytkownik dodaje nową subskrypcję za pomocą wtyczki (przycisk "Add to subscriptions" w popupie) będąc już na stronie danej subskrypcji (np. `youtube.com`), system zapisuje subskrypcję w bazie, ale nie wysyła zdarzenia `open` dla aktualnie otwartej karty. Sesja dla tej subskrypcji nie zostaje utworzona, a czas spędzony przed dodaniem subskrypcji jest bezpowrotnie tracony.                                                                                                                                                                                                                   |
| **Kroki reprodukcji**       | 1. Otwórz przeglądarkę i zaloguj się do aplikacji Sub Guardian<br>2. Otwórz nową kartę i przejdź na `https://youtube.com` (strona nie jest jeszcze subskrypcją)<br>3. Kliknij ikonę rozszerzenia Sub Guardian — popup pokazuje "Active tab is not in any subscription"<br>4. Kliknij "Add to subscriptions" — subskrypcja `youtube.com` zostaje zapisana<br>5. Odśwież dashboard `/home/` — `youtube.com` widnieje na liście subskrypcji, ale nie ma dla niej żadnej sesji ani zdarzenia `open`<br>6. Sprawdź `SiteEvent` w panelu admina — brak wpisu `open` dla `youtube.com` z chwili dodania subskrypcji |
| **Oczekiwany rezultat**     | Po dodaniu subskrypcji przez wtyczkę, gdy karta z daną stroną jest już otwarta, system powinien wywołać `postSiteEvent(url, tabId, "open", timestamp)`, tworząc `SiteEvent` i `Session` dla właśnie dodanej subskrypcji                                                                                                                                                                                                                                                                                                                                                                                      |
| **Rzeczywisty rezultat**    | Subskrypcja zapisana — SiteEvent nie wysłany, sesja nie utworzona. Śledzenie rozpocznie się dopiero przy następnym zdarzeniu karty (przeładowanie, ponowne otwarcie)                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Przyczyna**               | Funkcja `addSubscription()` w `js/api.js` wykonuje POST `/api/subscriptions/add/`, ale nie wywołuje `postSiteEvent()` dla aktualnie aktywnej karty. Logika `background.js` nasłuchuje tylko zdarzeń `onCreated`/`onUpdated`/`onRemoved` — żadne z nich nie jest wyzwalane przez samo dodanie subskrypcji                                                                                                                                                                                                                                                                                                     |
| **Proponowane rozwiązanie** | W `popup/popup.js`, po pomyślnym wywołaniu `addSubscription()`, należy dodatkowo wywołać `postSiteEvent(tabUrl, tabId, "open", new Date().toISOString())` — lub przenieść tę logikę do `background.js` po wykryciu nowej subskrypcji przez `chrome.storage.onChanged`                                                                                                                                                                                                                                                                                                                                        |

#### BUG-009: Sesje nie są zamykane po gwałtownym zamknięciu przeglądarki

| Pole                        | Wartość                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **ID**                      | BUG-009                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Tytuł**                   | Zdarzenia `close` nie są wysyłane przy wymuszonym zamknięciu przeglądarki (Alt+F4, kill procesu, awaria systemu)                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Wpływ**                   | Wysoki                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Priorytet**               | Wysoki                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Środowisko**              | Rozszerzenie Chrome (Manifest V3) v1.0.2; przeglądarka Chrome na Windows/Linux                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Opis**                    | Gdy użytkownik zamyka przeglądarkę w sposób wymuszony (Alt+F4, zabicie procesu, awaria zasilania, crash przeglądarki), `chrome.tabs.onRemoved` może nie zostać wywołane dla wszystkich otwartych kart. W konsekwencji zdarzenia `close` nie są wysyłane do backendu, a sesje użytkowania pozostają w stanie otwartym (`ended_at = NULL`). Przy ponownym uruchomieniu przeglądarki sesje te nie są automatycznie zamykane — pozostają jako wiecznie aktywne.                                                                                                                    |
| **Kroki reprodukcji**       | 1. Otwórz przeglądarkę, zaloguj się do Sub Guardian<br>2. Otwórz kartę z subskrybowaną stroną (np. `netflix.com`) — zdarzenie `open` wysłane, sesja utworzona<br>3. Otwórz drugą kartę z inną subskrybowaną stroną (np. `spotify.com`) — druga sesja utworzona<br>4. Naciśnij Alt+F4 (Windows) lub zamknij proces Chrome przez menedżer zadań<br>5. Uruchom ponownie przeglądarkę, przejdź do dashboardu `/home/`<br>6. Sprawdź listę ostatnich sesji — sesje dla `netflix.com` i `spotify.com` mają status "Aktywna" i `ended_at = NULL`, mimo że przeglądarka była zamknięta |
| **Oczekiwany rezultat**     | Po wymuszonym zamknięciu przeglądarki wszystkie aktywne sesje powinny zostać oznaczone jako zakończone z poprawnym `duration_seconds`                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Rzeczywisty rezultat**    | Sesje pozostają w stanie otwartym. `ended_at = NULL`, `duration_seconds = NULL`. Statystyki czasu na dashboardzie są zaniżone, ponieważ niezamknięte sesje nie są wliczane do sumy `duration_seconds`                                                                                                                                                                                                                                                                                                                                                                          |
| **Przyczyna**               | `chrome.tabs.onRemoved` nie jest gwarantowane przy wymuszonym zamknięciu procesu przeglądarki. Ponadto backend nie ma żadnego mechanizmu wykrywania osieroconych (orphaned) sesji i ich automatycznego zamykania                                                                                                                                                                                                                                                                                                                                                               |
| **Proponowane rozwiązanie** | 1. W `background.js` nasłuchiwać `chrome.runtime.onSuspend` i przed zamknięciem service workera wysłać zdarzenia `close` dla wszystkich śledzonych kart (z `tabUrls`).<br>2. W backendzie dodać cykliczne zadanie (np. `manage.py close_orphaned_sessions`) zamykające sesje bez `ended_at`, które mają `started_at` starsze niż 24 godziny — jako fallback dla przypadków, gdy SW nie zdąży wysłać zdarzeń.                                                                                                                                                                   |

## 6.4 Checklista jakościowa

Dla każdej funkcji spełnione muszą być następujące kryteria:

- Funkcja działa zgodnie z User Story
- Spełnione są kryteria akceptacji
- Wykonano testy jednostkowe (jeśli dotyczy)
- Wykonano testy integracyjne (jeśli dotyczy)
- Brak błędów blokujących (Critical/High)
- Zmiana nie zepsuła wcześniejszych funkcji (testy regresyjne: `uv run python manage.py test dashboard api`)

---

# 7. Zarządzanie ryzykiem

## 7.1 Analiza SWOT projektu

### Mocne strony (Strengths)
- S1: Obszerna wizualizacja danych
- S2: Zachowanie danych historycznych nawet po usunięciu subskrypcji
- S3: Wygoda użytkowania — wtyczka jest zawsze pod ręką podczas przeglądania stron, co pozwala na natychmiastowe dodanie nowej subskrypcji bez otwierania osobnej aplikacji
- S4: Niskie bariery wejścia — wystarczy jedno kliknięcie w sklepie Chrome Web Store lub Firefox Add-ons
- S5: Powiadomienia w czasie rzeczywistym — bezpośrednie alerty w przeglądarce o zbliżających się terminach płatności

### Słabe strony (Weaknesses)
- W1: Brak CI/CD (ciągła integracja)
- W2: SQLite — nie nadaje się do produkcji
- W3: Brak dokumentacji API (OpenAPI/Swagger)
- W4: Ograniczenia mobilne — wtyczka do przeglądarki działa tylko na desktopie; brak natywnego wsparcia dla urządzeń mobilnych
- W5: Kwestie prywatności — użytkownicy mogą być nieufni wobec narzędzia, które monitoruje strony odwiedzane w ramach subskrypcji
- W6: Brak pełnej automatyzacji bankowej — bez integracji z bankowością użytkownik musi ręcznie dodawać subskrypcje

### Szanse (Opportunities)
- O1: Dodanie powiadomień e-mail o zbliżającej się płatności
- O2: Integracja z zewnętrznymi API (np. sprawdzanie ceny subskrypcji)
- O3: Rosnąca frustracja konsumentów nadmiarem subskrypcji stwarza ogromny popyt na narzędzia do ich optymalizacji i redukcji kosztów
- O4: Współpraca z bankami w celu oferowania wspólnych systemów kontroli wydatków
- O5: Wersja dla małych firm — stworzenie wersji dla firm, które mają problem z kontrolowaniem licencji na oprogramowanie dla swoich pracowników (SaaS Management)

### Zagrożenia (Threats)
- T1: Zmiany w Chrome Manifest V3 mogą wpłynąć na działanie rozszerzenia
- T2: Utrata danych przy braku backupu SQLite
- T3: Uzależnienie od CDN (Bootstrap, Chart.js) — brak offline
- T4: Konkurencja ze strony banków — banki mogą wprowadzić funkcje zarządzania subskrypcjami bezpośrednio do swoich aplikacji mobilnych
- T5: Zmiany w prawie ochrony danych — zaostrzenie przepisów dotyczących śledzenia aktywności użytkowników w sieci może ograniczyć funkcjonalność detekcji
- T6: Cyberbezpieczeństwo — wyciek danych o subskrypcjach użytkowników byłby bardzo cenny dla hakerów

## 7.2 Plan zarządzania ryzykiem

### Macierz ryzyk (Risk Matrix)

| Ryzyko                              | Prawdop. (1–5) | Wpływ (1–5) | Wynik (P×W) | Priorytet     |
| ----------------------------------- | :------------: | :---------: | :---------: | ------------- |
| Konkurencja ze strony banków        |       4        |      3      |   **12**    | Bardzo wysoki |
| Zmiany w prawie ochrony danych      |       3        |      4      |   **12**    | Bardzo wysoki |
| Cyberbezpieczeństwo — wyciek danych |       2        |      5      |   **10**    | Wysoki        |
| Zmiany w Chrome API (Manifest V3)   |       2        |      4      |    **8**    | Średni        |
| Utrata danych SQLite                |       2        |      4      |    **8**    | Średni        |
| Awaria CDN                          |       2        |      3      |    **6**    | Niski         |


### Działania minimalizujące

**Konkurencja ze strony banków:**
- Agregacja międzybankowa — wtyczka może agregować subskrypcje z różnych kart i banków w jednym miejscu (bank widzi tylko swoje transakcje). Przewaga nad rozwiązaniami bankowymi.
- Funkcja "One-click Cancel" — uproszczenie procesu rezygnacji poprzez bezpośrednie linki do stron deaktywacji subskrypcji (banki zazwyczaj tylko blokują płatność, nie umożliwiają anulowania).
- Niezależność od sektora bankowego — pozycjonowanie wtyczki jako narzędzia niezależnego, które nie faworyzuje żadnego banku ("Privacy Privacy").

**Zmiany w prawie ochrony danych:**
- Privacy by Design — projektowanie narzędzia tak, aby analiza danych odbywała się lokalnie w przeglądarce użytkownika, bez wysyłania historii przeglądania na serwer zewnętrzny. Przetwarzane są wyłącznie nazwy domen subskrypcji, nie pełna historia przeglądania.
- Audyty prawne — regularne konsultacje z prawnikami specjalizującymi się w IT/Privacy w celu szybkiej adaptacji do nowych dyrektyw (np. ePrivacy Regulation).
- Transparentność — jasny "Privacy Center" wewnątrz wtyczki, pokazujący dokładnie jakie dane są przetwarzane i dlaczego.

**Cyberbezpieczeństwo:**
- Zero-Knowledge Architecture — szyfrowanie danych kluczem należącym tylko do użytkownika. Nawet jeśli baza danych wycieknie, dane są nieczytelne dla hakerów.
- Dwuetapowa weryfikacja (2FA — obowiązkowe lub zalecane 2FA przy dostępie do panelu zarządzania subskrypcjami.
- Regularne testy penetracyjne — zlecanie zewnętrznym firmom prób włamania do systemu co najmniej raz w roku.

**Zmiany w Chrome API (Manifest V3):**
- Monitorowanie zmian Chrome Extensions
- Modularyzacja kodu dla łatwej migracji

**Utrata danych SQLite:**
- Regularny backup pliku db.sqlite3
- Migracja do PostgreSQL w przyszłości

**Awaria CDN:**
- Hostowanie Bootstrap/Chart.js lokalnie jako fallback

---

# 8. Dokumentacja użytkowa

## 8.1 Instrukcja obsługi

### Wymagania

- Python 3.13+
- Google Chrome (najnowsza wersja)
- `uv` (menedżer pakietów Python)

### Krok 1: Uruchomienie backendu

```bash
cd sg-webapp/
uv sync                          # Instalacja zależności
uv run src/manage.py migrate     # Inicjalizacja bazy danych
uv run src/manage.py runserver   # Uruchomienie serwera na http://127.0.0.1:8000
```

### Krok 2: Rejestracja konta

1. Otwórz `http://127.0.0.1:8000/home/`
2. Kliknij "Zarejestruj się"
3. Wypełnij formularz (nazwa użytkownika, hasło)
4. Po rejestracji nastąpi automatyczne zalogowanie

### Krok 3: Instalacja rozszerzenia Chrome

1. Otwórz Chrome i wejdź na `chrome://extensions/`
2. Włącz "Tryb dewelopera" (prawy górny róg)
3. Kliknij "Załaduj rozszerzenie bez pakowania"
4. Wybierz folder `sg-extension/`

### Krok 4: Dodawanie subskrypcji

**Przez rozszerzenie:**
1. Otwórz stronę subskrypcji (np. netflix.com)
2. Kliknij ikonę Sub Guardian w pasku rozszerzeń
3. Kliknij "Add to subscriptions"

**Przez API:**
```bash
curl -X POST http://127.0.0.1:8000/api/subscriptions/add/ \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: <token>" \
  --cookie "csrftoken=<token>; sessionid=<session>" \
  -d '{"name": "netflix.com", "url": "https://netflix.com", "cost": 59.00, "billing_cycle": "monthly"}'
```

### Krok 5: Korzystanie z dashboardu

1. Otwórz `http://127.0.0.1:8000/home/`
2. Zaloguj się
3. Dashboard wyświetla:
   - Liczbę aktywnych subskrypcji
   - Łączny koszt miesięczny (PLN)
   - Czas śledzony w ostatnich 30 dniach
   - Liczbę wizyt w ostatnich 30 dniach
   - Karty subskrypcji z kosztem i cyklem rozliczeniowym
   - Wykres słupkowy: czas na poszczególne usługi
   - Wykres liniowy: aktywność dzienna
   - Tabelę ostatnich sesji

### Krok 6: Testowanie

```bash
cd sg-webapp/
uv run src/manage.py test api dashboard   # Wszystkie testy
```

## 8.2 FAQ

**P: Czy mogę używać Sub Guardian bez rejestracji?**
Nie. System wymaga konta użytkownika do przechowywania subskrypcji i zdarzeń.

**P: Czy rozszerzenie działa na wszystkich stronach?**
Rozszerzenie monitoruje tylko te strony, które zostały dodane jako subskrypcje. Strony chrome:// i chrome-extension:// są ignorowane.

**P: Jak często rozszerzenie wysyła zdarzenia?**
Przy każdym otwarciu i zamknięciu karty. Zdarzenia grupowane dla wydajności.

**P: Czy mogę edytować subskrypcję po dodaniu?**
Obecnie edycja jest dostępna tylko przez panel admina Django (`/admin/`) lub bezpośrednio przez API. Planowana jest edycja z poziomu dashboardu.

**P: Co się stanie gdy zamknę przeglądarkę?**
Wszystkie otwarte sesje zostaną automatycznie zakończone, gdy karty zostaną zamknięte. Jeśli jednak sesja pozostanie otwarta, zostanie automatycznie zamknięta przy następnym uruchomieniu.

**P: Czy mogę używać PostgreSQL zamiast SQLite?**
Obecnie system korzysta z SQLite. Migracja do PostgreSQL wymaga zmiany konfiguracji w `settings.py` i jest planowana na przyszłość.

**P: Jak wygląda format danych w API?**
Wszystkie endpointy zwracają JSON. Przykład odpowiedzi `/api/subscriptions/`:
```json
{
  "subscriptions": [
    {
      "id": 1,
      "name": "netflix.com",
      "url": "https://netflix.com",
      "cost": "59.00",
      "billing_cycle": "monthly",
      "next_billing_date": "2025-06-15"
    }
  ]
}
```

---


---

*Sprawozdanie przygotowane na potrzeby zaliczenia przedmiotu "Zarządzanie projektami" — Uniwersytet Kazimierza Wielkiego w Bydgoszczy, rok akademicki 2024/2025.*
*Autorstwo: Maja Jarka, Zuzanna Olejarz, Przemysław Paliwoda, Kacper Domek, Michał Mroziński*
