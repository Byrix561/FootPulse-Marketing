---
name: spieltag-paket
description: Erstellt nach einem Spieltag für eine Liga das Content-Paket - Team der Woche, größte Auf- und Abwertungen mit Begründung, drei Story-Ideen und je einen Hook. Nutzen nach jedem Spieltag oder wenn ein Creator Screenshots der FootPulse-App zu einem Spieltag schickt.
argument-hint: "[Liga, z. B. Süper Lig]"
---

# Spieltag-Paket

Du machst aus einem Spieltag ein fertiges Content-Paket für eine Liga.

## 1. Liga und Quelle klären

- **Liga** aus `$ARGUMENTS` oder fragen: Süper Lig, Premier League, Bundesliga.
- Lies `marke/produktfakten.md`. Ist die Liga noch nicht live in der App, sag das kurz: Dann gibt es keine FootPulse-Daten, und das Paket wird als Vorproduktion mit „Wartet auf Funktion: <Liga> live“ markiert, oder es arbeitet nur mit öffentlichen Spieldaten.
- **Quelle der Daten**: Bitte um Screenshots aus der FootPulse-App (Team der Woche, Auf- und Abwertungen mit Begründung) oder, wenn möglich, lies die öffentliche Seite. Erfinde keine Werte.
- **Spieltag und Datum** festhalten.

## 2. Daten zusammenstellen

Mit **Stand-Datum** und **Quelle** (Screenshot vom … / Seite vom …):
- **Team der Woche**: Aufstellung mit Overall.
- **Größte Aufwertungen** (Top 3): Spieler, Verein, alt → neu, Begründung aus der App in einem Satz.
- **Größte Abwertungen** (Top 3): genauso.
- **Auffälligkeiten**: Überraschungen, Widersprüche (z. B. ein Spieler mit Tor, der trotzdem fällt), Derbys.

Kannst du einen Wert nicht sicher ablesen, markiere ihn mit „bitte prüfen“.

## 3. Drei Story-Ideen

Jede Idee als Geschichte, nicht als Datenbild:
- **Titel**
- **Konto und Plattform**, für die sie am besten passt
- **Die Geschichte in zwei Sätzen** (Spannung → Auflösung)
- **Hook-Vorschlag** (in der Sprache des Kontos)
- **Format** (Reel, Karussell, X-Post)

Sag, welche der drei du für die stärkste hältst und warum.

## 4. Speichern

Lege `content/ideen/JJJJ-MM-TT_<liga>_spieltag<N>-paket.md` an (Kopf nach `content/ideen/_vorlage.md`, Konto = Liga-Konto, Status = Idee) mit Daten, Story-Ideen und Hooks.

## Ergebnis

Pfad der Datei, die drei Story-Ideen in Kurzform mit Empfehlung und das Angebot, die stärkste direkt mit `/post-entwerfen` oder `/video-planen` weiterzumachen.
