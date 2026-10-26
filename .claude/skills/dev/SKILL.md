---
name: dev
description: Ein spezifiziertes Epic vollständig implementieren und nachweisen.
---
# Dev
1. Lies das gewählte specs/*-Epic und CLAUDE.md.
2. Implementiere das komplette Epic, einschließlich Tests.
3. Schreibe den Fortschritt in specs/progress/{nr}-{name}-progress.md fort.
4. Committe relevante Einzelschritte auf dem Feature-Branch.
5. Erstelle specs/tests/{nr}-{name}-testplan.md.
6. Führe anschließend die Browserprüfung mit Playwright MCP in Chrome durch; wenn die Umgebung fehlt, offenlegen und Setup mit Nutzer abstimmen.
7. Fixe gefundene Bugs und öffne PR gegen staging, nie selbst mergen.
