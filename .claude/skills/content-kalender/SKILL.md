---
name: content-kalender
description: Pflegt den Content-Plan in content/kalender.md (was, wann, wo, Status) und zeigt Lücken je Konto und Plattform. Nutzen, wenn ein Creator planen will, fragt was als Nächstes kommt oder einen Post in den Plan eintragen will.
argument-hint: "[z. B. nächste Woche, Lücken, Post eintragen]"
---

# Content-Kalender

Du pflegst `content/kalender.md`.

## 1. Stand lesen

Lies `content/kalender.md`, die Dateien in `content/ideen/`, `content/produktion/` und `content/veroeffentlicht/` (nur den Kopf) und `content/LAGE.md`.

## 2. Abgleichen

- Stimmen die Status im Kalender mit dem Kopf der Dateien überein? Wenn nicht, korrigieren und sagen, was du geändert hast.
- Veröffentlichte Posts in „Erledigt“ verschieben; Einträge älter als vier Wochen dort entfernen.
- Posts mit „Wartet auf Funktion“ markieren und prüfen, ob die Funktion laut `marke/produktfakten.md` inzwischen live ist.

## 3. Auftrag aus `$ARGUMENTS` ausführen

- **Eintragen**: Datum, Konto, Plattform, Sprache, Kurztitel mit Link zur Datei, Status. Fehlende Angaben abfragen.
- **Übersicht**: Die nächsten 7 oder 14 Tage als Tabelle.
- **Lücken**: Für jedes der vier Konten und jede der drei Plattformen: Wie viele Posts sind in den nächsten 7 Tagen geplant? Zeig Lücken deutlich. Kein Konto muss täglich posten, aber jedes sollte mindestens zwei- bis dreimal pro Woche etwas haben (Empfehlung, kein Muss).
- **Anlässe**: Bekannte Spieltage, Derbys, Transferfristen und Länderspielpausen in „Feste Termine und Anlässe“ ergänzen, wenn der Creator das möchte (bei Unsicherheit Webrecherche anbieten).

## 4. Vorschläge

Schlag für die zwei größten Lücken konkrete Ideen vor (aus `content/ideen/` oder neu). Achte auf den Spieltagsrhythmus aus `wiki/06-content-der-funktioniert.md`.

## Ergebnis

Die aktualisierte Wochenübersicht als Tabelle, die Lücken je Konto in einem Satz und deine zwei Vorschläge. Die Datei `content/kalender.md` ist gespeichert.
