# TeamPulse – Projektregeln

## Projekt und Stack
Team-Stimmungs-Barometer: anonyme tägliche Smileys und ein datensparsamer Wochenverlauf.
Python 3.12 · Django 5.2 · SQLite · Django Templates · CSS · Vanilla JS/SVG · Docker Compose · GitHub Actions.
Keine externen APIs und keine CDN-Abhängigkeiten.

## Schnellstart
- docker compose up --build: App und Migrationen
- python manage.py migrate && python manage.py runserver: lokal ohne Docker (nach pip install)
- python manage.py test: Tests
- ruff check --select E4,E7,E9,F .: Lint

## Struktur
- mood/models.py: Stimmen ohne direkte Identitätsdaten
- mood/views.py: Cookie und Abstimmung
- mood/trends.py: aggregierte Wochenwerte
- templates/mood/home.html: Benutzeroberfläche
- static: CSS und SVG-Zeichner
- docs/project-map.md: Modul- und Datenflusskarte
- specs: Roadmap, Epics, Testpläne und Fortschritt

## Arbeitsweise
- Mit dem Nutzer Deutsch sprechen, Code und Bezeichner auf Englisch.
- Keine Features oder Dependency-Upgrades ohne Auftrag.
- Keine destruktiven/irreversiblen Aktionen ohne ausdrückliche Zustimmung.
- Kleine Commits, keine unangefragten Refactorings.
- Für Features und Fixes Tests verfassen, echte Testdatenbank nutzen.
- Sprache der Oberfläche: Deutsch. WCAG 2.1 AA anstreben, Tastaturfokus und aussagekräftige Formulare.
- Keine Namen, E-Mail-Adressen, IP-Adressen oder Konten in MoodEntry speichern.
- Stimmungsdurchschnitt und exakte Tageszahl nur bei mindestens fünf Abgaben freigeben.
- Änderungen an Architektur oder APIs in docs/project-map.md dokumentieren.

## Git
- Immer feature/* oder fix/*, keine direkten Feature-Commits auf main.
- Präfixe feat:, fix:, chore:, test:.
- PR-Ziel: staging, niemals main. Mergen ist Nutzersache.
- Kein --force und kein --no-verify.
- Nach Modelländerungen Migrationsdateien mitcommitten.
- Vor Push / PR: Checks, Tests, Lint prüfen. Bei fehlender Laufzeitumgebung offenlegen, CI zur Kontrolle verwenden.

## Security
- .env und .env.prod niemals lesen, schreiben oder ändern; nur .env.example.
- Keine Geheimnisse in Git oder Logs. Inputvalidierung, CSRF, Escape und sichere Cookies beibehalten.
- Bei Infrastrukturänderungen Dev und Prod gemeinsam bedenken.

## Skills
plan → specs/roadmap.md mit für den Workshop genau ZWEI Epics.
spec → Brainstorming pro Epic, dann vollständige Spezifikation.
dev → Implementierung, Fortschrittsprotokoll, Commits, Browserplan und Verifikation.

Sonderfreigabe 26.10.2026: Nutzer möchte die Umsetzung beider Epics in einem zusammenhängenden Durchlauf. Browserprüfung am Ende.
