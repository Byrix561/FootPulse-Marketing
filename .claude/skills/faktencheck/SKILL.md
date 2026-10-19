---
name: faktencheck
description: Prüft einen Entwurf (Skript, Caption, Karussell, Werbetext) gegen marke/produktfakten.md und das Glossar und gibt Hinweise, keine Sperre. Nutzen vor der Freigabe eines Posts oder wenn ein Creator fragt, ob etwas so stimmt.
argument-hint: "[Datei oder Text]"
---

# Faktencheck

Du prüfst einen Entwurf. Du gibst Hinweise, du blockierst nichts.

## 1. Entwurf holen

Nimm den Entwurf aus `$ARGUMENTS` (Dateipfad oder Text). Fehlt er, frag danach.

## 2. Lesen

Lies `marke/produktfakten.md` und `marke/glossar.md`. Ist `produktfakten.md` älter als 30 Tage, sag das einmal.

## 3. Prüfen

Geh diese Punkte durch:
1. **Funktionen**: Zeigt oder verspricht der Entwurf etwas, das nicht live ist (z. B. Bundesliga oder Premier League in der App, Live-Bewertung, App-Store-App, mehrsprachige App)?
2. **Formulierungen**: „live“, „Echtzeit“, „das genaueste“, „die Ersten“, „die Einzigen“, „herunterladen“?
3. **Rating-Logik**: Stimmt, was über das Rating gesagt wird (Karriere zählt, nur Leistung, kein Marktwert, gedeckelter Verlust bei Nichtspielen ist noch nicht umgesetzt, „eine 78 bedeutet überall dasselbe“ ist nur ein Ziel)?
4. **Begriffe**: Passen sie zum Glossar in der jeweiligen Sprache?
5. **Spielerzahlen**: Gibt es Zahlen ohne Stand-Datum? Zahlen, die du nicht prüfen kannst, als „bitte in der App prüfen“ markieren.
6. **Fußball-Fakten**: Ergebnisse, Transfers, Verletzungen, Rekorde. Wenn du unsicher bist, sag es. Biete eine Webrecherche an.
7. **Bildrechte**: Werden Medien erwähnt, die vermutlich nicht frei sind?

## Ergebnis

Eine kurze Liste, sortiert nach Wichtigkeit:
- ✅ Was passt.
- ⚠️ Hinweise mit Stelle im Text, Grund und einem konkreten Verbesserungsvorschlag.
- ❓ Was der Creator selbst prüfen muss.

Am Ende ein Satz: „Aus meiner Sicht bereit zur Freigabe“ oder „Ich würde vorher X ändern“. Die Entscheidung liegt beim Creator. Biete an, die Änderungen direkt in die Datei einzuarbeiten.
