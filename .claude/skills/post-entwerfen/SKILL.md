---
name: post-entwerfen
description: Entwirft einen Social-Media-Post für FootPulse (Hook, Skript oder Bildtext, Caption, Hashtags, Call-to-Action) und legt ihn als Datei in content/ideen/ oder content/produktion/ an. Nutzen, wenn ein Creator einen Post, ein Reel, ein Karussell, ein TikTok oder einen X-Post machen will.
argument-hint: "[Thema, Konto oder Plattform]"
---

# Post entwerfen

Du hilfst einem Creator, einen Post zu entwerfen. Schreib auf Deutsch mit dem Creator; der Post selbst ist in der Sprache des Kontos.

## 1. Vorbereitung

Lies `marke/produktfakten.md`, `marke/glossar.md`, `marke/stil.md` und die passende Bereichs-`CLAUDE.md` (Ton je Konto). Schau in `inspiration/hooks.md` nach passenden Hook-Mustern.

## 2. Fehlende Angaben abfragen

Frag in einer einzigen Nachricht nach allem, was noch fehlt (Angaben aus `$ARGUMENTS` nicht nochmal fragen):
- **Konto**: FootPulse (Englisch), Bundesliga (Deutsch), Premier League (Englisch), Süper Lig (Türkisch)
- **Plattform**: Instagram, TikTok, X
- **Format**: Reel / Kurzvideo, Karussell, Bild, Story, Thread
- **Ziel**: Reichweite, Debatte, Follower, Warteliste
- **Thema / Aufhänger**: Spieler, Spieltag, Debatte, Produkt
- **Status**: nur Idee oder schon in Produktion?

## 3. Entwurf liefern

- **Drei Hook-Varianten** mit unterschiedlichen Mustern. Sag, welche du empfiehlst und warum.
- **Skript** (Video: Szenen mit Zeit, Bild, Text, Sprache) oder **Bildtext** (Karussell: Folie für Folie).
- **Caption** mit starker erster Zeile.
- **3–5 Hashtags**.
- **Ein Call-to-Action**.
- Deine **ehrliche Einschätzung**: Was ist stark, was ist schwach, was würdest du ändern?

## 4. Hinweise geben (keine Sperre)

- Zeigt der Post etwas, das laut `produktfakten.md` noch nicht live ist? Kurz darauf hinweisen und „Wartet auf Funktion: …“ in den Kopf schreiben.
- Formulierungen wie „live“, „das genaueste“, „die Einzigen“? Bessere Variante vorschlagen.
- Bilder, Musik oder Schriften, die nicht frei sind? Deutlich sagen, freie Alternative aus `rechte/freie-quellen.md` vorschlagen. Wird trotzdem Unfreies genutzt, Eintrag in `rechte/nicht-freie-medien.md` anbieten.
- Zahlen zu Spielern: Stand-Datum nennen und den Creator bitten, sie in der App zu prüfen.

Entscheidet der Creator anders, setz es um.

## 5. Datei anlegen

- Status „Idee“ → `content/ideen/JJJJ-MM-TT_konto_kurztitel.md` nach `content/ideen/_vorlage.md`.
- Status „Produktion“ → `content/produktion/JJJJ-MM-TT_konto_kurztitel.md` nach `content/produktion/_vorlage.md`.
- Kopf ausfüllen: Autor, Konto, Plattform, Sprache, Status, OneDrive-Link (falls bekannt), Wartet auf Funktion (optional).
- Biete an, den Post in `content/kalender.md` einzutragen.

## Ergebnis

Am Ende steht: der Pfad der angelegten Datei, die empfohlene Hook-Variante und der nächste Schritt (z. B. `/video-planen`, `/faktencheck` oder Freigabe).
