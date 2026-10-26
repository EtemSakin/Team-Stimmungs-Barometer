# Team-Stimmungs-Barometer · TeamPulse

Ein **anonymes Team-Stimmungs-Barometer** zur täglichen Smiley-Auswahl (😫 🙁 😐 🙂 😄) und zum Blick auf den **7-Tage-Trend**.

## Funktionsumfang

- Smiley-Check-in (fünf Stufen), serverseitige Eingabeprüfung, CSRF-Schutz.
- Je Browser und lokalem Kalendertag eine Abgabe (Cookie-basierte, umgehbare Sperre).
- Keine Konten, Namen, E-Mail-Adressen oder IP-Felder im Abstimmungsmodell.
- Trenddiagramm (SVG ohne Drittanbieter/CDN), zugängliche HTML-Tabelle und responsive Oberfläche.
- Tagesmittel und exakte Tageszahlen werden nur ab **fünf Abgaben am jeweiligen Tag** angezeigt; Tage darunter fließen nicht in den Wochenmittelwert ein.
- SQLite-Datenbank, Docker Compose, Django-Tests und GitHub Actions.

## Lokal starten: Docker

Docker Desktop installieren und im Projektverzeichnis ausführen:

    docker compose up --build

Im Browser: http://localhost:8000. Migrationen werden beim Containerstart ausgeführt.

## Lokal starten: Python 3.12

    python -m venv .venv
    # Windows: .venv\Scripts\activate
    # Linux/macOS: source .venv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver

Browser: http://127.0.0.1:8000.

## Tests

    pip install -r requirements-dev.txt
    python manage.py check
    python manage.py makemigrations --check --dry-run
    python manage.py test
    ruff check --select E4,E7,E9,F .
    python manage.py collectstatic --noinput

Die Browser-Testpläne stehen unter specs/tests. CI läuft bei Pushes auf Feature-Branches und PRs nach staging.

## Für eine Produktionsumgebung

Setze DJANGO_DEBUG=0, DJANGO_SECRET_KEY und DJANGO_ALLOWED_HOSTS als echte Laufzeitvariablen. Nutze einen vertrauenswürdigen HTTPS-Reverse-Proxy, überprüfe SSL, Cookie- und Log-Konfiguration und starte:

    docker compose -f compose.prod.yaml up --build -d

SQLite liegt im persistenten Docker-Volume. Sichere es regelmäßig. Die Anwendung bringt bewusst keine automatische Löschroutine und keine Authentifizierung mit; für einen realen Personalbetrieb sind Datenschutz, Betriebsmodell und Retention gesondert zu prüfen.

## Anonymität und Manipulationsgrenzen

Ein zufälliger HttpOnly-Cookie wird pro Tag mit HMAC-SHA256 in ein tagesbezogenes Pseudonym umgewandelt. Der Hash ist in der Datenbank nur mit dem jeweiligen Datum relevant. Browserwechsel oder Cookie-Löschen ermöglichen zusätzliche Abgaben. Die App garantiert daher **weder absolute Anonymität gegenüber Infrastrukturbetreibern noch eine manipulationssichere Einmalabgabe**.

## Code-Struktur

- mood: Datenmodell, Abstimmung und Trendservice mit Tests.
- barometer: Django-Konfiguration.
- templates und static: deutschsprachige Oberfläche und SVG.
- docs: Projektkarte, ADR und Runbook.
- specs: zwei abgeschlossene Epics samt Fortschritten und Browserabnahme.
- .claude/skills: plan, spec und dev; maßgebend ist CLAUDE.md.

Git-Flow: feature/* → staging → main. Änderungen werden über Pull Requests geprüft. Der Nutzer führt die Merges aus.
