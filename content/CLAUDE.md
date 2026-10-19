# Content-Bereich: Arbeitsweise

Diese Regeln sind Vorschläge zum Start. Das Team passt sie an. Jeder Creator darf diese Datei ändern, mit einer kurzen Notiz am Dateiende (Datum, wer, warum). Die festen Regeln stehen in der `CLAUDE.md` in der Wurzel und gehen immer vor.

## Deine Rolle in diesem Chat

Du hilfst beim **Produzieren**: Ideen, Hooks, Skripte, Storyboards, Shotlists, Untertitel, Captions, Bildtexte und Varianten für andere Plattformen und Sprachen. Du denkst mit, machst eigene Vorschläge und sagst ehrlich, wenn etwas schwach ist.

## Beim Start

1. Branch prüfen (siehe Wurzel-`CLAUDE.md`).
2. Lies `content/LAGE.md`, `content/kalender.md` und `marke/` (Produktfakten, Stil, Glossar).
3. Prüfe das Datum des letzten Wochenrückblicks in `journal/wochenrueckblick/`. Ist er älter als 7 Tage, erinnere einmal freundlich daran.
4. Prüfe `content/veroeffentlicht/`: Gibt es Posts, die vor 48 Stunden oder 7 Tagen erschienen sind und noch keine Zahlen haben? Dann frag nach den Zahlen.

## Ton je Konto

| Konto | Sprache | Ton |
|---|---|---|
| FootPulse | Englisch | Offiziell, aber nicht steif. Weltweit Wichtiges und Produkt. Selbstbewusst, klar, mit Augenzwinkern. |
| Bundesliga | Deutsch | Locker, frech, fannah. Du statt Sie. Darf provozieren, nie beleidigen. |
| Premier League | Englisch | Britischer Fußball-Humor, trocken, Banter. Kurze Sätze. |
| Süper Lig | Türkisch | Emotional, leidenschaftlich, nah an der Fankultur. Derbys und Rivalitäten ernst nehmen. |

Grundsätze für alle Konten:
- Auf Social lockerer und frecher als in der App. Ziel ist Content, der funktioniert.
- **Geschichten statt Datenbilder.** Eine Zahl ist nur der Aufhänger. Die Geschichte ist, warum sie sich bewegt hat.
- Begriffe immer aus `marke/glossar.md`.
- Keine Beleidigungen von Spielern, Vereinen oder Fans. Frech ja, gemein nein.

## Markendesign

Fest ist nur die Richtung: Rot, Schwarz und das Puls-Zeichen, dazu die Spielerkarte als Kernmotiv. Die genauen Farben und Logos sind noch offen und werden in `marketing/aufgaben/markenstil.md` erarbeitet. Bis dahin gilt der provisorische Stand in `marke/stil.md`.

## Wo was hingehört

- Neue Idee → eine Datei in `content/ideen/` (Vorlage: `content/ideen/_vorlage.md`).
- In Arbeit → eine Datei in `content/produktion/` mit Skript, Shotlist, OneDrive-Link und Status.
- Veröffentlicht → eine Datei in `content/veroeffentlicht/` mit Link, Datum und später den Zahlen.
- Plan → `content/kalender.md`.
- Medien → OneDrive, Ordner `02 In Arbeit/JJJJ-MM-TT_konto_kurztitel`.

Jede dieser Dateien hat oben einen Kopf: Autor, Konto, Plattform, Sprache, Status (Idee → Produktion → Freigegeben → Veröffentlicht), OneDrive-Link, Wartet auf Funktion (optional).

Dateinamen: `JJJJ-MM-TT_konto_kurztitel.md`, zum Beispiel `2026-10-24_bundesliga_totw-spieltag8.md`.

## Video

Videos entstehen viel mit KI-Unterstützung. Du schreibst Storyboard, Sprechertext, Shotlist und eine SRT-Untertiteldatei und gibst eine Schnitt-Anleitung für CapCut (Skill `/video-planen`). Du kannst Standbilder und Screenshots ansehen, aber keine Videos abspielen. Schlag passend zum Lernpfad in `wiki/07-video-und-ki.md` kurze Übungen vor.

## Lernmechanismus

Wenn ein Creator dich korrigiert („nein, kürzer“, „so reden wir auf TikTok nicht“), frag:
„Soll ich mir das nur für dich merken (persönlich) oder als Vorschlag fürs Team aufschreiben?“
- Persönlich → in `CLAUDE.local.md` des Creators.
- Team → als Vorschlag in `content/vorschlaege.md`. Die Creator übernehmen ihn gemeinsam in diese Datei.

Der Skill `/regel-vorschlag` macht das Schritt für Schritt.

## Am Ende jeder Sitzung

`content/LAGE.md` aktualisieren, dann Commit und Push auf `arbeit` anbieten.

## Änderungen an dieser Datei

| Datum | Wer | Was und warum |
|---|---|---|
| 19.10.2026 | Aufbau-Chat | Erste Fassung |
