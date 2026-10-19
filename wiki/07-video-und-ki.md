# 7. Video und KI

## Das Wichtigste in fünf Sätzen

1. Du schneidest in **CapCut** (kostenlos, für TikTok und Reels gebaut), wechselst bei Grenzen zu **DaVinci Resolve** und machst Grafiken, Karten-Visuals und Vorlagen in **Canva**.
2. Claude übernimmt die Planung: Idee, Storyboard, Sprechertext, Shotlist, eine Untertiteldatei (SRT) für CapCut und eine Schnitt-Anleitung Schritt für Schritt (Skill `/video-planen`).
3. Claude kann Standbilder und Screenshots ansehen und Feedback geben, aber keine Videos abspielen.
4. Für Canva gibt es einen offiziellen Claude-Connector, für CapCut (Stand 19.10.2026) nicht.
5. Du lernst Schritt für Schritt: zwei Wochen CapCut-Grundlagen, dann Übergänge, Sounddesign und Keyframes, und jede Woche ein Video, das „mehr kann als letzte Woche“.

## Werkzeuge

| Werkzeug | Wofür | Kosten | Wann |
|---|---|---|---|
| **CapCut** | Schnitt von Kurzvideos, automatische Untertitel, Effekte, Vorlagen | Kostenlos (Pro-Version optional) | Ab sofort, unser Standard |
| **DaVinci Resolve** | Professioneller Schnitt, Farbkorrektur, Ton | Kostenlos | Wenn CapCut an Grenzen stößt |
| **Canva** | Grafiken, Karten-Visuals, Karussells, Cover, Vorlagen, einfache Animationen | Kostenlos oder Pro | Ab sofort |
| **Bildschirmaufnahme** | App-Aufnahmen der FootPulse-Karten | In Handy oder Rechner eingebaut | Ab sofort |

Schriften und Farben aus `marke/stil.md` (heute: Barlow Condensed, Rot und Schwarz).

## Verbindungen (Connectors)

Ein **Connector** verbindet Claude mit einem anderen Werkzeug, sodass Claude dort direkt arbeiten kann.

- **Canva**: Es gibt einen offiziellen Connector. Damit kann Claude Designs suchen, neue erstellen, Vorlagen befüllen und exportieren.
  So verbindest du ihn: In der Claude-App die Einstellungen öffnen, den Bereich **Connectors** (Verbindungen) wählen, **Canva** suchen, auf **Verbinden** klicken und dich mit deinem Canva-Konto anmelden. Danach kannst du im Chat sagen: „Erstelle in Canva ein Karussell aus diesem Text.“ Wenn die Menüpunkte anders heißen, frag den Wiki-Chat.
  Hinweis: Du meldest dich selbst bei Canva an. Claude bekommt kein Passwort.
- **CapCut**: Kein Connector (Stand 19.10.2026). Claude liefert dir Dateien und Anleitungen, du schneidest selbst.

## Arbeitsweise mit KI

Der Ablauf für ein Video (Skill `/video-planen`):

1. **Idee**: Du sagst Claude, worum es gehen soll. Claude schlägt Hooks und eine Geschichte vor und sagt ehrlich, was er für stark oder schwach hält.
2. **Storyboard**: Szene für Szene: was man sieht, was man hört, welcher Text eingeblendet wird.
3. **Sprechertext**: Wenn gesprochen wird, auf Sekunden getimt.
4. **Shotlist**: Liste aller Aufnahmen und Grafiken, die du brauchst (z. B. „Bildschirmaufnahme der Karte, Zoom auf Pace“).
5. **Untertiteldatei (SRT)**: Eine Textdatei mit Zeitangaben, die du in CapCut importierst. So musst du Untertitel nicht abtippen.
6. **Musikvorschlag**: Nur aus freien Quellen (`rechte/freie-quellen.md`).
7. **Schnitt-Anleitung für CapCut**: Schritt für Schritt, mit Menüpfaden.
8. **Feedback**: Du schickst Standbilder oder Screenshots aus deinem Schnitt. Claude gibt konkretes Feedback (Lesbarkeit, Tempo-Gefühl, Hook-Bild).

**Was eine SRT-Datei ist:** Eine einfache Textdatei für Untertitel. Jeder Block hat eine Nummer, eine Zeitangabe und den Text:

```
1
00:00:00,000 --> 00:00:01,800
+4 in einer Woche.

2
00:00:01,800 --> 00:00:03,500
Kein Tor. Wie?
```

In CapCut: Text → Untertitel → Datei importieren (bzw. „Lokale Untertitel“). Die Menüpunkte ändern sich manchmal; Claude hilft dir, wenn du einen Screenshot schickst.

**KI-Werkzeuge für Bilder und Videos** (z. B. Bild- oder Videogeneratoren): Nur nach den Regeln in `rechte/freie-quellen.md`. Keine fotorealistischen Fakes echter Spieler, keine echten Vereinslogos. KI-Rohclips gehören in OneDrive `01 Rohmaterial/`.

## Code-basierte Videos (später)

Claude Code kann einfache Videos auch selbst erzeugen, zum Beispiel animierte Karten oder hochzählende Zahlen mit HTML oder Remotion (ein Werkzeug, das Videos aus Code baut) und Schnitt mit ffmpeg (ein Programm zum Verarbeiten von Videodateien). Das lohnt sich für wiederkehrende Formate wie das Team der Woche: Einmal gebaut, entsteht jede Woche ein neues Video mit neuen Daten.

Wichtig:
- Erst einrichten, wenn sich ein Format bewährt hat (Testjournal).
- Installationen nur mit Burhans Ja.
- Bis dahin: CapCut und Canva.

## Lernpfad

| Zeitraum | Fokus | Übung |
|---|---|---|
| Woche 1 | CapCut-Grundlagen: Projekt anlegen, schneiden, trimmen, Reihenfolge, Export in 9:16 | Ein 15-Sekunden-Video aus Screenshots der App mit Text |
| Woche 2 | Text, automatische Untertitel, SRT-Import, Tempo (Pausen raus) | Ein Video mit Hook und Untertiteln aus einer SRT-Datei von Claude |
| Woche 3 | Übergänge (sparsam), Zoom-Effekte, Musik unterlegen | Team der Woche als Video mit Zoom auf jede Karte |
| Woche 4 | Sounddesign: Soundeffekte auf Schnitte, Lautstärke anpassen, Ducking (Musik leiser, wenn gesprochen wird) | Ein Video mit gesprochenem Text und Musik darunter |
| Woche 5–6 | Keyframes: eigene Bewegungen (Zoom, Verschieben, Einblenden) | Overall, der animiert hochzählt; Karte, die ins Bild fliegt |
| Ab Woche 7 | Vorlagen bauen, eigener Stil, DaVinci Resolve anschauen | Eine wiederverwendbare CapCut-Vorlage für eine Serie |

Parallel: **Jede Woche ein Video, das „mehr kann als letzte Woche“.** Der Content-Chat schlägt passende kurze Übungen vor. Fortschritte kannst du in deiner `CLAUDE.local.md` notieren.

Gute Lernquellen: das offizielle CapCut-Hilfecenter und kurze Tutorials auf YouTube („CapCut keyframe tutorial“, „CapCut auto captions“). Tipp: Schau dir ein Tutorial an, dann mach sofort dasselbe mit FootPulse-Material.

## Wo die Dateien hinkommen

| Was | OneDrive-Ordner |
|---|---|
| Eigene Aufnahmen, App-Bildschirmaufnahmen, KI-Rohclips | `01 Rohmaterial/` (Bundesliga, Premier League, Süper Lig, FootPulse) |
| Projekt in Arbeit (CapCut-Projekt, Zwischenstände) | `02 In Arbeit/JJJJ-MM-TT_konto_kurztitel/` |
| Fertiger Export | `03 Fertig/` |
| Nach dem Veröffentlichen | `04 Veröffentlicht/JJJJ-MM/` |
| Musik und Sounds mit Lizenz-Textdatei | `05 Musik und Sounds/` |
| CapCut- und Canva-Vorlagen, Untertitel-Stile | `06 Vorlagen/` |

Dateinamen: `2026-10-24_bundesliga_totw-spieltag8_v2.mp4`.
