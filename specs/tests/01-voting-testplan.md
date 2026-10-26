# Browser-Testplan – Epic 01
In Chrome mit Desktop- und mobiler Viewport-Breite testen:
1. Startseite zeigt fünf beschriftete Smileys.
2. Leeres Formular zeigt Browservalidierung.
3. Gültiges Formular erzeugt Danke-Meldung und eine Stimme.
4. Browser mit bereits abgegebener Stimme zeigt gesperrte Eingabe.
5. Neues Privatfenster darf abstimmen.
6. Löschen des Cookies erlaubt neue Stimme (bekannte Grenze).
7. Tastaturfokus, Pfeiltasten für Radiobuttons, Submit und Fehlermeldungen prüfen.
8. Smartphone-Breite 375px: kein Überlauf.
9. CSRF-Fehler und invaliden POST über gesonderten Testclient prüfen.
10. Dieselben Abläufe non-scripted in Chrome per Playwright MCP nachvollziehen und Ergebnisse dokumentieren.
