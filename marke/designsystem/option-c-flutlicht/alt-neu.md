# Option C · Flutlicht: alter Wert → neuer Wert

Stand 04.11.2026. Vorlage für den App-Umbau: Jede Zeile ist ein Austausch in der Token-Datei. Spalte „alt“ ist der heutige Dark-Wert. Light gibt es heute nicht, die Spalte ist neu.

| Rolle | Zweck | alt (Dark) | neu Dark | neu Light | Änderung |
|---|---|---|---|---|---|
| `background` | Seitenhintergrund | `#050507` | `#140F0E` | `#E3DDD2` | heller (ΔL 5.8) |
| `surfaceSunken` | Vertiefte Flächen (Eingabefeld, Mulde) | `#09090D` | `#0C0807` | `#D7D2C7` | dunkler (ΔL 0.2) |
| `surface` | Karten, Listen | `#111116` | `#241F1D` | `#F7F4ED` | heller (ΔL 6.4) |
| `surfaceElevated` | Gehobene Karten, Kopfzeilen | `#191920` | `#2F2A28` | `#FFFFFF` | heller (ΔL 7.3) |
| `surfaceOverlay` | Menüs, Popover, Tooltips | `#24242D` | `#3C3734` | `#EEE9DE` | heller (ΔL 7.7) |
| `surfaceWarm` | Hervorgehobene Karte mit Rot-Stich | `#151014` | `#362422` | `#F8E3DB` | heller (ΔL 10.1) |
| `surfaceDeep` | Zwischenebene (Leisten, Tab-Spur) | `#0C0C11` | `#1C1715` | `#EDE9E0` | heller (ΔL 5.3) |
| `borderSubtle` | Trenner in Listen | `#1D1D24` | `#35302E` | `#D6D0C5` | heller (ΔL 8.0) |
| `border` | Karten-Rand | `#2A2A34` | `#484240` | `#C2BDB2` | heller (ΔL 9.5) |
| `borderStrong` | Rand von Bedienelementen (3 : 1) | `#3D3D49` | `#898381` | `#7A7468` | heller (ΔL 25.0) |
| `textPrimary` | Haupttext, Zahlen | `#F2F2F5` | `#F4F0E6` | `#19120F` | dunkler (ΔL 0.7) |
| `textSecondary` | Nebentext | `#ABABB6` | `#D5CEC4` | `#473F3C` | heller (ΔL 11.0) |
| `textTertiary` | Beschriftungen | `#93939F` | `#C8C2B7` | `#544C49` | heller (ΔL 14.9) |
| `textMuted` | Hinweise, ab 14 px halbfett | `#82828E` | `#AFA89E` | `#605754` | heller (ΔL 12.4) |
| `textFaint` | Nur Nicht-Text: Pfeile, Trenner, Icons | `#666672` | `#827C73` | `#807975` | heller (ΔL 7.4) |
| `accent` | Rote Flächen, Buttons, Linien ≥ 2 px | `#F02D3A` | `#E32018` | `#E11D16` | dunkler (ΔL 3.4) |
| `accentText` | Rote Schrift, kleine rote Punkte | `#FF5260` | `#FFA697` | `#BC0002` | heller (ΔL 12.9) |
| `accentDim` | Gedrücktes Rot, rote Linie auf Rot | `#9F1D28` | `#A3241B` | `#ED8C83` | heller (ΔL 1.2) |
| `accentMuted` | Hintergrund roter Chips | `#381015` | `#40100E` | `#FFDDD9` | heller (ΔL 1.4) |
| `gold` | Nur verdiente Auszeichnung (MVP, Rang 1) | `#F1C15B` | `#F1BE3D` | `#F3BA25` | dunkler (ΔL 0.8) |
| `goldMuted` | Hintergrund Gold-Chip | `#302613` | `#3D2E0A` | `#F7E5B9` | heller (ΔL 3.6) |
| `pitchGreen` | Spielfeld-Fläche (TOTW) | `#0B251B` | `#122D19` | `#B9E0C0` | heller (ΔL 2.9) |
| `pitchLine` | Spielfeld-Linien | `#285442` | `#325B3B` | `#80B38A` | heller (ΔL 2.3) |
| `ratingUp` | Aufwertung (immer mit ▲ und +) | `#2ECC71` | `#53FEEC` | `#005860` | heller (ΔL 16.0) |
| `positiveMuted` | Hintergrund Aufwertungs-Chip | `#0D2618` | `#0F3118` | `#CBECF2` | heller (ΔL 3.7) |
| `ratingDown` | Abwertung (immer mit ▼ und −) | `#FF5260` | `#FFA697` | `#BC0002` | heller (ΔL 12.9) |
| `ratingElite` | Note Elite (Fläche, Zahl in ratingInk) | `#3B82F6` | `#85BAFF` | `#85BAFF` | heller (ΔL 15.6) |
| `ratingExcellent` | Note Excellent | `#18B981` | `#9EFFFE` | `#9EFFFE` | heller (ΔL 24.3) |
| `ratingGood` | Note Good | `#8BC34A` | `#D6FC91` | `#D6FC91` | heller (ΔL 18.7) |
| `ratingAverage` | Note Average | `#F2B84B` | `#F8A052` | `#F8A052` | dunkler (ΔL 3.7) |
| `ratingPoor` | Note Poor | `#EF5B5B` | `#FFBFB6` | `#FFBFB6` | heller (ΔL 19.6) |

## Neue Rollen

| Rolle | Zweck | neu Dark | neu Light |
|---|---|---|---|
| `tabTrack` | NEU: Spur der Tab-Leiste | `#1C1715` | `#EBE6DB` |
| `tabActive` | NEU: Fläche des aktiven Tabs | `#3C3734` | `#FFFFFF` |
| `surfaceHover` | NEU: Hover auf Fläche | `#2D2826` | `#EDE8DD` |
| `surfacePressed` | NEU: Gedrückt / aktiv | `#37322F` | `#E1DBD0` |
| `surfaceSelected` | NEU: Ausgewählte Zeile oder Karte | `#46221F` | `#FFDDD9` |
| `surfaceDisabled` | NEU: Deaktivierte Fläche | `#1A1615` | `#EAE7E2` |
| `textDisabled` | NEU: Deaktivierter Text (keine Kontrastpflicht) | `#726E69` | `#837F7D` |
| `focusRing` | NEU: Fokusrahmen 2 px, 2 px Abstand | `#F4F0E6` | `#19120F` |
| `onAccent` | NEU: Schrift auf Rot | `#FCFCFC` | `#FCFCFC` |
| `goldText` | NEU: Gold als Schrift (im Hell-Modus dunkler) | `#F1BE3D` | `#845500` |
| `ratingInk` | NEU: Zahl auf Noten- und Liga-Flächen | `#140F0E` | `#100B09` |

## Marketing und Liga (beide Modi)

| Rolle | Zweck | Wert |
|---|---|---|
| `mkRed` | Marketing: rote Vollfläche | `#D71712` |
| `mkRedDeep` | Marketing: zweites Rot für Tiefe, Streifen | `#8A0605` |
| `mkInk` | Marketing: Schwarz | `#140F0E` |
| `mkPaper` | Marketing: Weiß / Kreide | `#F3EEE3` |
| `onMkRed` | Marketing: kleine Schrift auf Rot | `#F5F1E9` |
| `onMkRedLarge` | Marketing: Schlagzeile auf Rot | `#F4F0E6` |
| `leagueBL` | Akzent Bundesliga-Konto (Fläche) | `#9CACFF` |
| `leaguePL` | Akzent Premier-League-Konto (Fläche) | `#9DFFB2` |
| `leagueSL` | Akzent Süper-Lig-Konto (Fläche) | `#DECEFF` |

## Schrift, Größen, Radien

- Überschrift: **Big Shoulders Display**, Text: **Sofia Sans Condensed**, Zahlen: **Sofia Sans Condensed** mit `tabular-nums`, Beschriftung: **Sofia Sans Condensed**.
- Größen (px): display 76/68, h1 50/46, h2 36/34, h3 26/26, title 20/24, body 17/24, small 15/20, label 13/16, caption 13/16, micro 11/12, ovr 58/52, stat 18/20.
- Radien: `radius-xs` 0 px (Fast alles: harte Kanten), `radius-sm` 2 px (Eingabefelder (Fokus sichtbar)), `radius-md` 0 px (Karten), `radius-lg` 4 px (Dialoge).
- Raster 4 pt, Gutter 20, mobile Spalte 560 px, Breakpoints 720 und 960 bleiben.
