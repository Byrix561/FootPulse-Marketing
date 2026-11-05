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

Flächen: Option A bestätigt (Burhan 05.11.).

### AB-20261105-03 · Website-Builder · Rollen für Tabellenzonen

Die Website führt nach FS-20261105-08 vier eigene Zonenrollen in `frontend/src/lib/theme.ts` ein. Die Übergabe enthält hierfür keine Werte. Die Rollen färben die Randmarke und die dazugehörige Legende ausschließlich bei veröffentlichter Zonen-Policy.

| Rolle | Bisherige Zuordnung | Neuer Website-Wert | Kontrast auf `surface` |
| --- | --- | --- | --- |
| `zoneChampions` | `matchRatingElite` | `#91B9FF` | 8,31:1 |
| `zoneEurope` | `gold` | `#C7A9F0` | 8,14:1 |
| `zoneConference` | `positive` | `#89CFD9` | 9,41:1 |
| `zoneRelegation` | `accent` | `#F392A7` | 7,44:1 |

Die kleinste Kontrastrate gegen `surfaceOverlay` beträgt 5,39:1. Für Marketing zur Info.

Status: offen (Website-Abnahme Schritt 4 folgt)

### AB-20261105-02 · Website-Builder · Option A, Schritt 0

| Rolle | Vorher | Jetzt |
| --- | --- | --- |
| `background` | `#050507` | `#0D0F14` |
| `surfaceSunken` | `#09090D` | `#06080C` |
| `surface` | `#111116` | `#1D1F24` |
| `surfaceElevated` | `#191920` | `#272A30` |
| `surfaceOverlay` | `#24242D` | `#34373D` |
| `surfaceWarm` | `#151014` | `#352222` |
| `surfaceDeep` | `#0C0C11` | `#15171C` |
| `borderSubtle` | `#1D1D24` | `#2E3036` |
| `border` | `#2A2A34` | `#404248` |
| `borderStrong` | `#3D3D49` | `#808389` |
| `textPrimary` | `#F2F2F5` | `#F2F3F6` |
| `textSecondary` | `#ABABB6` | `#CDCFD5` |
| `textTertiary` | `#93939F` | `#C0C2C8` |
| `textMuted` | `#82828E` | `#A7A9AE` |
| `textFaint` | `#666672` | `#7B7D82` |
| `accent` | `#F02D3A` | `#E31D29` |
| `accentDim` | `#9F1D28` | `#A32224` |
| `accentMuted` | `#381015` | `#401011` |
| `gold` | `#F1C15B` | `#F2BF47` |
| `goldMuted` | `#302613` | `#392C0C` |
| `pitchGreen` | `#0B251B` | `#0F2D1F` |
| `pitchLine` | `#285442` | `#2D5742` |
| `ratingUp` | `#2ECC71` | `#5EF9F1` |
| `positiveMuted` | `#0D2618` | `#002F2D` |
| `ratingInk` | `#07100B` | `#0D0F14` |

Neue Rollen aus der Übergabe: `tabTrack #15171C`, `tabActive #34373D`, `surfaceHover #26282D`, `surfacePressed #2F3237`, `surfaceSelected #44211F`, `surfaceDisabled #14161A`, `textDisabled #6D6F71`, `focusRing #E4E8EF`, `onAccent #FCFCFC`, `goldText #F2BF47`, `leagueBL #9CACFF`, `leaguePL #9DFFB2`, `leagueSL #DECEFF`. Poor erhält abweichend die dunkle Ziffer `onRatingPoor #0D0F14`. Die Kartenrollen verwenden separat die bisherigen Werte. Die Vereins- und Ausweichfarben sind zentralisiert. Bisher lokal gesetzte Töne beziehen sich auf die zentralen Flächen-, Rot-, Gold- und Spielfeldrollen.

Barlow 400/500/600 kommt als Textschrift hinzu, Barlow Condensed bleibt für Überschriften, Zahlen und das Logo. Barlow Condensed 800, die Typostufen der Übergabe und Schnitte 8/14/28 px liegen als Rollen vor. Radius xs ist neu mit 2 px, sm bleibt 4 px, md wechselt 8 → 6 px und lg 14 → 8 px. Die bisherigen xl/xxl-Aliasse gehen im allgemeinen Rahmen auf 8 px. Die TOTW-spezifischen Radien und Schriftzuschnitte behalten ihre Werte.

Für Marketing gilt die dunkle Poor-Ziffer. O-20261105-10 setzt die Aufwertung vorläufig auf Grün (`ratingUp #2ECC71`, `positiveMuted #0D2618`). Bei einer späteren Änderung des Hintergrundtons wird Türkis erneut verglichen.

Status: geschlossen (Entscheidung über die Aufwertungsfarbe)


### AB-20261105-01 · Website-Supervisor · Start des Website-Umbaus mit Option A

Die Website wird jetzt Tab für Tab auf Option A „Anzeigetafel“ umgebaut. Codex baut, Claude prüft, und jeder fertige Tab geht einzeln live. Grundlage ist `uebergabe-website/` mit Stand 05.11.2026. Burhan hat dazu gesagt: Die Töne sind ein Vorschlag, kein Muss. Wo die heutigen Website-Werte besser sind, bleiben sie, zum Beispiel bei den Notenfarben (Tabelle oben). Weitere Abweichungen trägt die Website hier ein, sobald Burhan sie entschieden hat.

Für Marketing: Für Noten-Chips in Posts bitte die Werte aus der Tabelle oben nehmen, nicht `#DC0C00`. Ob die Zahl auf „Poor“ dann dunkel oder weiß steht, rechnet die Website beim Bau nach und schreibt es hier dazu.

→ Antwort (Website-Builder, 05.11.2026): #0D0F14 auf #EF5B5B erreicht 5,77:1. Die Zahl wird dunkel gesetzt.

Status: erledigt (05.11.2026, Website-Builder)
