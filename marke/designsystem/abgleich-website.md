# Abgleich Marketing ↔ Website

Stand: 05.11.2026 · angelegt vom Frontend-Supervisor (Claude, FootPulse-Code-Repo) auf Wunsch von Burhan

## Wozu diese Datei da ist

Marketing und Website nutzen dieselben Farben, Schriften und Formen. Ändert eine Seite etwas, soll die andere es hier finden, ohne Code oder Ordner durchsuchen zu müssen. Diese Datei ist der einzige Ort dafür. Sie funktioniert wie die `LAGE.md`, nur zwischen Marketing und Website.

**Wer liest und schreibt:**

- der Marketing-Chat (und die Creator) in diesem Repo
- der Website-Builder (Codex) und der Frontend-Supervisor (Claude) aus dem Code-Repo `FootPulse`

**Die Regel dahinter:** Die Übergabe in `uebergabe-website/` ist ein Vorschlag. Was am Ende auf die Website kommt, entscheidet Burhan. Weicht die Website bewusst ab, steht das unten in der Tabelle „Entschiedene Abweichungen“. Marketing soll für Bilder und Posts dann den Website-Wert nehmen, damit beide gleich aussehen.

## So schreibst du einen Eintrag

- Neueste Einträge **oben** im Abschnitt „Einträge“.
- Kopf: `### AB-JJJJMMTT-NN · Absender · kurzer Titel`. Absender ist `Marketing`, `Website-Builder` oder `Website-Supervisor`.
- Darunter wenige ganze Sätze: **was** geändert wurde, **welche Tokens oder Dateien** betroffen sind, **was die andere Seite tun soll** (oder „nur zur Info“).
- Status am Ende: `offen`, `erledigt (Datum, von wem)` oder `abgelehnt (Grund)`.
- Die andere Seite antwortet unter dem Eintrag mit `→ Antwort (Absender, Datum): …` und setzt den Status.
- Keine Zugangsdaten, keine Namen von Fans oder Wartelisten-Nutzern.

**Wer welche Datei ändert:**

- `uebergabe-website/tokens.css` und `tokens.json` ändert nur Marketing. Möchte die Website einen anderen Wert, schreibt sie einen Eintrag hier. Marketing trägt den Wert danach in die Tokens ein.
- Die Farbdatei der Website (`frontend/src/lib/theme.ts` im Code-Repo) ändert nur der Website-Builder. Jede Wertänderung dort bekommt einen Eintrag hier.

## Entschiedene Abweichungen (Website-Wert gilt)

| Token | Übergabe (Option A) | Website nimmt | Entschieden | Grund |
| --- | --- | --- | --- | --- |
| `ratingElite` … `ratingAverage` | wie heute | wie heute | Burhan, 05.11.2026 | Die heutigen Notenfarben gefallen ihm |
| `ratingPoor` | `#DC0C00` | `#EF5B5B` (heutiger Wert) | Burhan, 05.11.2026 | wie oben; siehe AB-20261105-01 zur Zahlfarbe |

## Einträge

### AB-20261105-01 · Website-Supervisor · Start des Website-Umbaus mit Option A

Die Website wird jetzt Tab für Tab auf Option A „Anzeigetafel“ umgebaut. Codex baut, Claude prüft, und jeder fertige Tab geht einzeln live. Grundlage ist `uebergabe-website/` mit Stand 05.11.2026. Burhan hat dazu gesagt: Die Töne sind ein Vorschlag, kein Muss. Wo die heutigen Website-Werte besser sind, bleiben sie, zum Beispiel bei den Notenfarben (Tabelle oben). Weitere Abweichungen trägt die Website hier ein, sobald Burhan sie entschieden hat.

Für Marketing: Für Noten-Chips in Posts bitte die Werte aus der Tabelle oben nehmen, nicht `#DC0C00`. Ob die Zahl auf „Poor“ dann dunkel oder weiß steht, rechnet die Website beim Bau nach und schreibt es hier dazu.

Status: offen (Zahlfarbe auf Poor)
