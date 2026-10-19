---
name: uebersetzen
description: Übersetzt Hooks, Skripte, Captions oder Bildtexte zwischen Deutsch, Englisch und Türkisch mit dem FootPulse-Glossar und passt sie an den Ton des Zielkontos an, statt wörtlich zu übersetzen. Nutzen, wenn ein Post für ein anderes Konto oder eine andere Sprache gebraucht wird.
argument-hint: "[Text oder Datei] [Zielkonto]"
---

# Übersetzen

Du überträgst einen Text in eine andere Sprache und in den Ton eines anderen Kontos. Nicht wörtlich, sondern so, wie ein Muttersprachler und Fan dieser Liga es sagen würde.

## 1. Angaben klären

- **Text** aus `$ARGUMENTS` (Text oder Dateipfad). Fehlt er, frag danach.
- **Zielkonto**: FootPulse (Englisch), Bundesliga (Deutsch), Premier League (Englisch), Süper Lig (Türkisch). Daraus folgt die Sprache.
- **Was ist es**: Hook, Skript, Caption, Bildtext, Untertitel (SRT)?

## 2. Lesen

`marke/glossar.md` (Pflichtbegriffe je Sprache) und den Ton je Konto aus `content/CLAUDE.md`.

## 3. Übertragen

- Begriffe exakt nach Glossar. Die Werte-Namen (Pace, Shooting …) bleiben englisch.
- Ton des Zielkontos treffen: Bundesliga locker und frech, Premier League trockener Banter, Süper Lig emotional, FootPulse selbstbewusst-offiziell.
- Wortspiele und Redewendungen **ersetzen**, nicht übersetzen. Sag, wo du etwas ersetzt hast.
- Fußball-Bezüge an die Liga anpassen, wenn sinnvoll (z. B. „Spieltag“ → „Gameweek“ in der Premier League, „Hafta“ in der Süper Lig).
- Längen im Blick behalten: Bildtexte und Hooks dürfen nicht viel länger werden.
- Bei SRT-Dateien: Zeitangaben unverändert lassen.

## Ergebnis

- Die Übersetzung, fertig zum Kopieren.
- Eine kurze Liste der Stellen, an denen du bewusst abgewichen bist, mit Grund.
- Bei Türkisch und Deutsch: der Hinweis, dass ein Muttersprachler kurz gegenlesen sollte, wenn es veröffentlicht wird.
- Angebot, die Fassung in die passende Datei in `content/` zu schreiben.
