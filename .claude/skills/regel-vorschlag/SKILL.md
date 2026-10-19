---
name: regel-vorschlag
description: Der Lernmechanismus - hält eine Korrektur oder Vorliebe eines Creators fest, entweder persönlich in CLAUDE.local.md oder als Team-Vorschlag in content/vorschlaege.md bzw. marketing/vorschlaege.md. Nutzen, wenn ein Creator Claude korrigiert, etwas dauerhaft ändern will oder einen neuen Skill vorschlägt.
argument-hint: "[die Regel oder Korrektur]"
---

# Regel-Vorschlag

Du sorgst dafür, dass Claude aus Korrekturen lernt, ohne dass jemand allein die Team-Regeln ändert.

## 1. Regel klären

Nimm die Regel aus `$ARGUMENTS` oder aus der letzten Korrektur im Chat. Formuliere sie als klaren, kurzen Satz und frag, ob das so gemeint ist. Beispiel: „Auf TikTok keine Hashtags im Bildtext, nur in der Caption.“

## 2. Fragen: persönlich oder Team?

Frag genau so: **„Soll ich mir das nur für dich merken (persönlich) oder als Vorschlag fürs Team aufschreiben?“**

## 3a. Persönlich

- Gibt es `CLAUDE.local.md`? Wenn nicht, biete an, sie aus `CLAUDE.local.beispiel.md` anzulegen.
- Trag die Regel unter „Was Claude sich für mich merken soll“ ein.
- Die Datei bleibt auf diesem Rechner und wird nicht geteilt.

## 3b. Team

- Passender Bereich: Content → `content/vorschlaege.md`, Marketing → `marketing/vorschlaege.md`. Wenn unklar, frag.
- Neue Zeile unter „Offen“: Datum, von wem, Vorschlag, warum.
- Sag: „Ihr könnt ihn beim Wochenrückblick gemeinsam besprechen und dann in die `CLAUDE.md` des Bereichs übernehmen.“
- Wollen alle Creator den Vorschlag schon jetzt übernehmen, trag ihn in die `CLAUDE.md` des Bereichs ein, mit Notiz am Dateiende (Datum, wer, warum), und hake ihn in `vorschlaege.md` als übernommen ab.

**Wichtig:** Die `CLAUDE.md` in der Wurzel ändert nur Burhan. Betrifft der Vorschlag eine feste Regel, schreib ihn in `marketing/vorschlaege.md` mit dem Vermerk „für Burhan“.

## 3c. Neuer Skill

Schlägt der Creator einen neuen Skill vor, schreib ihn als Team-Vorschlag auf: Name, was er tut, welche Fragen er stellt, was am Ende rauskommt.

## Ergebnis

Ein Satz, wo die Regel jetzt steht, und ab wann sie gilt (persönlich: ab dem nächsten Chat; Team: nach der Übernahme in die `CLAUDE.md`).
