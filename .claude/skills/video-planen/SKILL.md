---
name: video-planen
description: Plant ein Kurzvideo komplett - Storyboard, Shotlist, Sprechertext, Untertiteldatei (SRT) zum Import in CapCut, Vorschlag für freie Musik und eine Schnitt-Anleitung Schritt für Schritt für CapCut. Nutzen, wenn ein Creator ein Reel, TikTok oder Video produzieren will.
argument-hint: "[Thema, Länge, Konto]"
---

# Video planen

Du planst ein Kurzvideo so, dass der Creator es in CapCut direkt umsetzen kann. Du kannst keine Videos abspielen, aber Standbilder und Screenshots ansehen.

## 1. Angaben klären

Frag in einer Nachricht nach allem, was fehlt (Angaben aus `$ARGUMENTS` nicht nochmal fragen):
- Konto, Plattform, Sprache
- Thema und Ziel
- Länge (Empfehlung: 15–35 Sekunden)
- Mit gesprochenem Text (Voiceover) oder nur Text und Musik?
- Welches Material gibt es schon (App-Aufnahmen, Screenshots, eigene Clips)?
- Erfahrungsstand in CapCut (aus `CLAUDE.local.md`, falls vorhanden)

Lies `marke/stil.md`, `marke/produktfakten.md`, `marke/glossar.md` und `wiki/06-content-der-funktioniert.md`.

## 2. Geschichte

Schlag zwei bis drei Hooks vor und einen Ablauf: Hook → Spannung → (Wendung) → Auflösung → CTA. Empfiehl eine Variante und begründe sie. Warte auf das Okay, bevor du ins Detail gehst, außer der Creator will alles auf einmal.

## 3. Liefern

1. **Storyboard** als Tabelle: Zeit | Bild | Text auf dem Bild | Ton/Sprache.
2. **Shotlist**: alle Aufnahmen und Grafiken, die gebraucht werden, mit Quelle (z. B. „Bildschirmaufnahme FootPulse-App: Karte von Spieler X, langsam scrollen“, „Canva-Grafik: Overall 78 → 82“). Markiere, was nicht frei ist.
3. **Sprechertext** (falls Voiceover), auf Sekunden getimt, gut sprechbar.
4. **SRT-Datei**: Lege sie unter `content/produktion/JJJJ-MM-TT_konto_kurztitel.srt` an. Format: Nummer, Zeit `HH:MM:SS,mmm --> HH:MM:SS,mmm`, Text, Leerzeile. Zwei bis sechs Wörter pro Block, Zeiten passend zum Storyboard.
5. **Musikvorschlag**: Stimmung und Tempo, dazu Quellen aus `rechte/freie-quellen.md`. Bei TikTok: kommerzielle Musikbibliothek.
6. **Schnitt-Anleitung für CapCut**, nummeriert, mit Menüpfaden: Projekt in 9:16 anlegen, Material importieren, Reihenfolge, Schnitte, Text, SRT importieren (Text → Untertitel bzw. lokale Untertitel), Zooms/Keyframes, Musik und Lautstärke, Cover, Export (1080×1920, 30 fps). Passe die Tiefe an den Erfahrungsstand an und baue eine kleine Übung aus dem Lernpfad in `wiki/07-video-und-ki.md` ein.
7. **OneDrive**: Ordnername in `02 In Arbeit/` nach Schema `JJJJ-MM-TT_konto_kurztitel`.

## 4. Speichern

Alles (außer der SRT, die als eigene Datei liegt) in `content/produktion/JJJJ-MM-TT_konto_kurztitel.md` nach `content/produktion/_vorlage.md`. Kopf ausfüllen.

## 5. Feedback-Runde anbieten

Sag: „Schick mir Standbilder aus deinem Schnitt (z. B. das erste Bild, eine Textstelle, das Ende), dann gebe ich dir Feedback zu Hook, Lesbarkeit und Stil.“

## Ergebnis

Pfad der Produktionsdatei und der SRT-Datei, der Hook, die Länge und der nächste Schritt für den Creator.
