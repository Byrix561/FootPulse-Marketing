# Option B · Messgerät: alter Wert → neuer Wert

Stand 04.11.2026. Vorlage für den App-Umbau: Jede Zeile ist ein Austausch in der Token-Datei. Spalte „alt“ ist der heutige Dark-Wert. Light gibt es heute nicht, die Spalte ist neu.

| Rolle | Zweck | alt (Dark) | neu Dark | neu Light | Änderung |
|---|---|---|---|---|---|
| `background` | Seitenhintergrund | `#050507` | `#131517` | `#DFDEDA` | heller (ΔL 7.8) |
| `surfaceSunken` | Vertiefte Flächen (Eingabefeld, Mulde) | `#09090D` | `#0C0D0F` | `#D4D3CE` | heller (ΔL 1.7) |
| `surface` | Karten, Listen | `#111116` | `#232528` | `#F5F4F1` | heller (ΔL 8.4) |
| `surfaceElevated` | Gehobene Karten, Kopfzeilen | `#191920` | `#2E3133` | `#FFFFFF` | heller (ΔL 9.4) |
| `surfaceOverlay` | Menüs, Popover, Tooltips | `#24242D` | `#3B3D40` | `#EBE9E5` | heller (ΔL 9.5) |
| `surfaceWarm` | Hervorgehobene Karte mit Rot-Stich | `#151014` | `#3B2926` | `#F8E3DB` | heller (ΔL 12.0) |
| `surfaceDeep` | Zwischenebene (Leisten, Tab-Spur) | `#0C0C11` | `#1B1D1F` | `#EAE9E6` | heller (ΔL 7.3) |
| `borderSubtle` | Trenner in Listen | `#1D1D24` | `#353739` | `#D2D1CD` | heller (ΔL 10.2) |
| `border` | Karten-Rand | `#2A2A34` | `#47494C` | `#BFBEB9` | heller (ΔL 11.5) |
| `borderStrong` | Rand von Bedienelementen (3 : 1) | `#3D3D49` | `#888B8E` | `#767470` | heller (ΔL 27.0) |
| `textPrimary` | Haupttext, Zahlen | `#F2F2F5` | `#F2F3F5` | `#101419` | heller (ΔL 0.2) |
| `textSecondary` | Nebentext | `#ABABB6` | `#CDD0D2` | `#3C4247` | heller (ΔL 11.1) |
| `textTertiary` | Beschriftungen | `#93939F` | `#C0C3C6` | `#4A4F55` | heller (ΔL 14.9) |
| `textMuted` | Hinweise, ab 14 px halbfett | `#82828E` | `#A7A9AC` | `#545A60` | heller (ΔL 12.3) |
| `textFaint` | Nur Nicht-Text: Pfeile, Trenner, Icons | `#666672` | `#7B7D80` | `#767B80` | heller (ΔL 7.4) |
| `accent` | Rote Flächen, Buttons, Linien ≥ 2 px | `#F02D3A` | `#DC2628` | `#DB2527` | dunkler (ΔL 4.2) |
| `accentText` | Rote Schrift, kleine rote Punkte | `#FF5260` | `#FFA29E` | `#BB0916` | heller (ΔL 12.3) |
| `accentDim` | Gedrücktes Rot, rote Linie auf Rot | `#9F1D28` | `#A32321` | `#ED8B86` | heller (ΔL 1.1) |
| `accentMuted` | Hintergrund roter Chips | `#381015` | `#401010` | `#FFDDDA` | heller (ΔL 1.5) |
| `gold` | Nur verdiente Auszeichnung (MVP, Rang 1) | `#F1C15B` | `#E9B452` | `#E9AF41` | dunkler (ΔL 3.4) |
| `goldMuted` | Hintergrund Gold-Chip | `#302613` | `#3C2E14` | `#F7E5B9` | heller (ΔL 3.6) |
| `pitchGreen` | Spielfeld-Fläche (TOTW) | `#0B251B` | `#192E27` | `#C7E7D7` | heller (ΔL 4.0) |
| `pitchLine` | Spielfeld-Linien | `#285442` | `#39574C` | `#8EBEA8` | heller (ΔL 2.1) |
| `ratingUp` | Aufwertung (immer mit ▲ und +) | `#2ECC71` | `#A8E1FF` | `#005182` | heller (ΔL 13.5) |
| `positiveMuted` | Hintergrund Aufwertungs-Chip | `#0D2618` | `#142E3F` | `#D2EAFC` | heller (ΔL 4.5) |
| `ratingDown` | Abwertung (immer mit ▼ und −) | `#FF5260` | `#FFA29E` | `#BB0916` | heller (ΔL 12.3) |
| `ratingElite` | Note Elite (Fläche, Zahl in ratingInk) | `#3B82F6` | `#85BAFF` | `#85BAFF` | heller (ΔL 15.6) |
| `ratingExcellent` | Note Excellent | `#18B981` | `#9EFFFE` | `#9EFFFE` | heller (ΔL 24.3) |
| `ratingGood` | Note Good | `#8BC34A` | `#D6FC91` | `#D6FC91` | heller (ΔL 18.7) |
| `ratingAverage` | Note Average | `#F2B84B` | `#F8A052` | `#F8A052` | dunkler (ΔL 3.7) |
| `ratingPoor` | Note Poor | `#EF5B5B` | `#FFBFB6` | `#FFBFB6` | heller (ΔL 19.6) |

## Neue Rollen

| Rolle | Zweck | neu Dark | neu Light |
|---|---|---|---|
| `tabTrack` | NEU: Spur der Tab-Leiste | `#1B1D1F` | `#E7E6E2` |
| `tabActive` | NEU: Fläche des aktiven Tabs | `#3B3D40` | `#FFFFFF` |
| `surfaceHover` | NEU: Hover auf Fläche | `#2D2F31` | `#EAE8E4` |
| `surfacePressed` | NEU: Gedrückt / aktiv | `#36383A` | `#DDDCD7` |
| `surfaceSelected` | NEU: Ausgewählte Zeile oder Karte | `#1C3648` | `#D2EAFC` |
| `surfaceDisabled` | NEU: Deaktivierte Fläche | `#1A1C1E` | `#E8E8E6` |
| `textDisabled` | NEU: Deaktivierter Text (keine Kontrastpflicht) | `#6D6F70` | `#7E8084` |
| `focusRing` | NEU: Fokusrahmen 2 px, 2 px Abstand | `#6DC4FF` | `#0061BE` |
| `onAccent` | NEU: Schrift auf Rot | `#FCFCFC` | `#FCFCFC` |
| `goldText` | NEU: Gold als Schrift (im Hell-Modus dunkler) | `#E9B452` | `#845500` |
| `ratingInk` | NEU: Zahl auf Noten- und Liga-Flächen | `#131517` | `#121416` |

## Marketing und Liga (beide Modi)

| Rolle | Zweck | Wert |
|---|---|---|
| `mkRed` | Marketing: rote Vollfläche | `#DC2628` |
| `mkRedDeep` | Marketing: zweites Rot für Tiefe, Streifen | `#491F1D` |
| `mkInk` | Marketing: Schwarz | `#131517` |
| `mkPaper` | Marketing: Weiß / Kreide | `#F6F5F1` |
| `onMkRed` | Marketing: kleine Schrift auf Rot | `#FCFCFC` |
| `onMkRedLarge` | Marketing: Schlagzeile auf Rot | `#FCFCFC` |
| `leagueBL` | Akzent Bundesliga-Konto (Fläche) | `#9CACFF` |
| `leaguePL` | Akzent Premier-League-Konto (Fläche) | `#9DFFB2` |
| `leagueSL` | Akzent Süper-Lig-Konto (Fläche) | `#DECEFF` |

## Schrift, Größen, Radien

- Überschrift: **Archivo**, Text: **Archivo**, Zahlen: **Archivo** mit `tabular-nums`, Beschriftung: **IBM Plex Mono**.
- Größen (px): display 64/62, h1 40/42, h2 30/34, h3 22/28, title 18/24, body 16/24, small 14/20, label 12/16, caption 12/16, micro 10/12, ovr 48/48, stat 16/20.
- Radien: `radius-xs` 4 px (Tags), `radius-sm` 8 px (Buttons, Eingabefelder), `radius-md` 12 px (Karten), `radius-lg` 16 px (Dialoge, Sheets), `radius-pill` 999 px (Chips).
- Raster 4 pt, Gutter 20, mobile Spalte 560 px, Breakpoints 720 und 960 bleiben.
