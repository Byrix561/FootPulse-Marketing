# Designsystem 2026

Stand 05.11.2026 · Status: **drei Optionen fertig, Entscheidung durch Burhan offen**

Hier liegt das komplette Designsystem von FootPulse in drei Optionen. Jede Option ist vollständig, und die Optionen lassen sich mischen.

| Datei | Was |
|---|---|
| [kurzbericht.md](kurzbericht.md) | Das Wichtigste auf einer Seite |
| [entscheidung.md](entscheidung.md) | Vergleich, Mischregeln, Empfehlung, offene Fragen |
| [testmatrix.md](testmatrix.md) | Farbtests mit Zahlen: WCAG, APCA, Farbschwäche, Flächenstufen, v1 und v2 |
| [testmatrix-bild.md](testmatrix-bild.md) | Tests auf den Screenshots: Flächenstufen im Bild, Wirkung im Feed |
| [fuer-supervisor.md](fuer-supervisor.md) | Absatz für den Supervisor (App-Umbau als Vorschlag) |
| [canva-anleitung.md](canva-anleitung.md) | Schritt für Schritt für Kerem |
| [runde-1/](runde-1/) | Markenkern, Bestandsanalyse, Vorbilder, Moodboards |
| [tests/schrift-check.html](tests/schrift-check.html) | Messung der Schriften (Türkisch, Ziffern) |

## Je Option

Ordner `option-a-anzeigetafel/`, `option-b-messgeraet/`, `option-c-flutlicht/`:

| Datei | Was |
|---|---|
| `tokens.json` | Alle Farben für Dark und Light auf den App-Rollennamen, dazu Marketing, Liga, Schrift, Größen, Abstände, Radien |
| `alt-neu.md` | Tabelle alter Wert → neuer Wert je Rolle, die Vorlage für den App-Umbau |
| `tokens.css` / `tokens-v1.css` | Dieselben Werte als CSS (v2 und die erste Runde v1) |
| `testseiten.html` | Spielerkarte, Tabs, Tabelle, Chips, Team der Woche, Warteliste, Posts, Profilraster, Feed. Mit `?theme=light` und `?v=1` umschaltbar |
| `vorlagen.html` | Alle Marketing-Vorlagen in Originalgröße |
| `beispiele.html` | 12 weitere Beispiele zum Vergleichen: App-Screens Dark/Light, Bewegungen, Website, Homescreen, Profilbilder, Posts je Konto, YouTube, Story-Umfrage |
| `logo-regeln.html` | Varianten, Liga-Konten, Schutzzone, Mindestgröße, Do's und Don'ts |
| `logo/` | Alle Logos als SVG |

Design-System-Artefakte (privat, Freigabe über „Teilen“): [A](https://claude.ai/artifact/87k4nXC24dJHUAwpWWbc6y) · [B](https://claude.ai/artifact/QttJMNLHMkkQuE3brQ1jre) · [C](https://claude.ai/artifact/HfHw9KDWWJpAGQ5PcWvYUx)

OneDrive `00 Marke/Designsystem 2026/`: Logos als PNG und SVG in allen Größen, Screenshots der Tests, Vorlagen-Exporte, Links zu den Schriften. Vergleichstafeln A | B | C in `Screenshots/Beispiele/`.

## Neu bauen (für spätere Änderungen)

Alles wird aus `_werkzeug/` erzeugt. Farben ändern heißt `paletten_v2.py` ändern und dann im Ordner `_werkzeug` Folgendes aufrufen:

```bash
python -I bauen.py
```

Danach sind Tokens, Tabellen, Testmatrix, Logos und HTML-Seiten neu. Screenshots und PNG-Exporte macht der Chat im Browser (Ablauf siehe Skripte `bildtests.py`, `vorlagen_export.py`, `logo_png.py`).
