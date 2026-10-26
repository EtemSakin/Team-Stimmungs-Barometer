# Betriebsanleitung
1. HTTP lokal über docker compose up --build starten.
2. Produktion: DJANGO_DEBUG=0, starkes DJANGO_SECRET_KEY und DJANGO_ALLOWED_HOSTS setzen.
3. Docker compose -f compose.prod.yaml up --build -d mit HTTPS-Reverse-Proxy auf 127.0.0.1:8000.
4. Prüfen: docker compose logs web; python manage.py check.
5. SQLite-Volume regelmäßig konsistent sichern, Restore testen.
6. HTTPS, Hostvalidierung, Cookie-Flags und Reverse-Proxy-Logs prüfen.
7. Vor Realbetrieb Rechtsgrundlage, Informationstexte, Zugriffskontrolle und Löschfristen klären. Die Workshopversion hat noch keine automatische Aufbewahrungs-/Löschfunktion.
