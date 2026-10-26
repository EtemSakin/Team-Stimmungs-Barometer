# Projektkarte
GET / → mood.views.home → Form, Cookie, Trend.
POST /vote/ → mood.views.vote → MoodForm, CSRF, MoodEntry, Redirect.
DB: MoodEntry(day, score, daily_voter_hash) mit täglicher Eindeutigkeitsbedingung.
Service: mood.trends.build_week_trend; DB-Aggregation, k=5-Unterdrückung, gewichtetes Mittel.
UI: templates/mood/home.html, static/css/style.css und dashboard.css, static/js/trend.js.
Betrieb: Docker Compose in Dev/Prod, GitHub Actions, WhiteNoise für Staticfiles.
