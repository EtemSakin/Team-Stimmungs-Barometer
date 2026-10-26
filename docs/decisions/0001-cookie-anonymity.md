# ADR-0001: Tagesbezogene Browser-Pseudonyme
Status: Accepted · 2026-10-26

Problem: Anonyme Abgaben ohne Konten, Duplikate möglichst verhindern.
Entscheidung: 180-Tage-Cookie mit zufälligem Token; je Datum HMAC unter SECRET_KEY; nur Tageshash in der DB. DB-UniqueConstraint verhindert Duplikate desselben Tageshashes. Veröffentlichung nur bei mindestens fünf Stimmen pro Tag.
Alternativen: Logins, personenspezifische Codes oder IP-Sperren. Logins/Codes erfordern zusätzliche Identitäts- und Verwaltungsprozesse; IP ist unzuverlässig und datenschutzkritisch.
Folgen: Cookie-Löschen oder Zweitbrowser umgeht Sperre; Secret-Rotation verändert Hashes; Proxy-Logs sind getrennt zu prüfen. Keine manipulationssichere Wahl.
