# Option A · Anzeigetafel: alter Wert → neuer Wert

Stand 04.11.2026. Vorlage für den App-Umbau: Jede Zeile ist ein Austausch in der Token-Datei. Spalte „alt“ ist der heutige Dark-Wert. Light gibt es heute nicht, die Spalte ist neu.

| Rolle | Zweck | alt (Dark) | neu Dark | neu Light | Änderung |
|---|---|---|---|---|---|
| `background` | Seitenhintergrund | `#050507` | `#0D0F14` | `#DBDEE3` | heller (ΔL 5.2) |
| `surfaceSunken` | Vertiefte Flächen (Eingabefeld, Mulde) | `#09090D` | `#06080C` | `#D0D3D8` | dunkler (ΔL 0.8) |
| `surface` | Karten, Listen | `#111116` | `#1D1F24` | `#F2F4F7` | heller (ΔL 5.9) |
| `surfaceElevated` | Gehobene Karten, Kopfzeilen | `#191920` | `#272A30` | `#FFFFFF` | heller (ΔL 6.8) |
| `surfaceOverlay` | Menüs, Popover, Tooltips | `#24242D` | `#34373D` | `#E7E9EF` | heller (ΔL 7.2) |
| `surfaceWarm` | Hervorgehobene Karte mit Rot-Stich | `#151014` | `#352222` | `#F9E1E1` | heller (ΔL 9.5) |
| `surfaceDeep` | Zwischenebene (Leisten, Tab-Spur) | `#0C0C11` | `#15171C` | `#E7E9EE` | heller (ΔL 4.8) |
| `borderSubtle` | Trenner in Listen | `#1D1D24` | `#2E3036` | `#CED1D6` | heller (ΔL 7.6) |
| `border` | Karten-Rand | `#2A2A34` | `#404248` | `#BBBEC3` | heller (ΔL 9.0) |
| `borderStrong` | Rand von Bedienelementen (3 : 1) | `#3D3D49` | `#808389` | `#72747A` | heller (ΔL 24.5) |
| `textPrimary` | Haupttext, Zahlen | `#F2F2F5` | `#F2F3F6` | `#111419` | heller (ΔL 0.2) |
| `textSecondary` | Nebentext | `#ABABB6` | `#CDCFD5` | `#3E4148` | heller (ΔL 11.0) |
| `textTertiary` | Beschriftungen | `#93939F` | `#C0C2C8` | `#4B4E55` | heller (ΔL 14.7) |
| `textMuted` | Hinweise, ab 14 px halbfett | `#82828E` | `#A7A9AE` | `#565960` | heller (ΔL 12.4) |
| `textFaint` | Nur Nicht-Text: Pfeile, Trenner, Icons | `#666672` | `#7B7D82` | `#777A80` | heller (ΔL 7.5) |
| `accent` | Rote Flächen, Buttons, Linien ≥ 2 px | `#F02D3A` | `#E31D29` | `#DB1B26` | dunkler (ΔL 3.4) |
| `accentText` | Rote Schrift, kleine rote Punkte | `#FF5260` | `#FFA29F` | `#BB081A` | heller (ΔL 12.4) |
| `accentDim` | Gedrücktes Rot, rote Linie auf Rot | `#9F1D28` | `#A32224` | `#ED8B87` | heller (ΔL 1.1) |
| `accentMuted` | Hintergrund roter Chips | `#381015` | `#401011` | `#FFDDDA` | heller (ΔL 1.5) |
| `gold` | Nur verdiente Auszeichnung (MVP, Rang 1) | `#F1C15B` | `#F2BF47` | `#EAB532` | dunkler (ΔL 0.5) |
| `goldMuted` | Hintergrund Gold-Chip | `#302613` | `#392C0C` | `#F7E5B9` | heller (ΔL 2.6) |
| `pitchGreen` | Spielfeld-Fläche (TOTW) | `#0B251B` | `#0F2D1F` | `#BDE2CB` | heller (ΔL 2.9) |
| `pitchLine` | Spielfeld-Linien | `#285442` | `#2D5742` | `#85B99A` | heller (ΔL 1.1) |
| `ratingUp` | Aufwertung (immer mit ▲ und +) | `#2ECC71` | `#5EF9F1` | `#005763` | heller (ΔL 15.3) |
| `positiveMuted` | Hintergrund Aufwertungs-Chip | `#0D2618` | `#002F2D` | `#CBECF2` | heller (ΔL 3.2) |
| `ratingDown` | Abwertung (immer mit ▼ und −) | `#FF5260` | `#FFA29F` | `#BB081A` | heller (ΔL 12.4) |
| `ratingElite` | Note Elite (Fläche, Zahl in ratingInk) | `#3B82F6` | `#85BAFF` | `#85BAFF` | heller (ΔL 15.6) |
| `ratingExcellent` | Note Excellent | `#18B981` | `#9EFFFE` | `#9EFFFE` | heller (ΔL 24.3) |
| `ratingGood` | Note Good | `#8BC34A` | `#D6FC91` | `#D6FC91` | heller (ΔL 18.7) |
| `ratingAverage` | Note Average | `#F2B84B` | `#F8A052` | `#F8A052` | dunkler (ΔL 3.7) |
| `ratingPoor` | Note Poor | `#EF5B5B` | `#FFBFB6` | `#FFBFB6` | heller (ΔL 19.6) |

## Neue Rollen

| Rolle | Zweck | neu Dark | neu Light |
|---|---|---|---|
| `tabTrack` | NEU: Spur der Tab-Leiste | `#15171C` | `#E3E6EC` |
| `tabActive` | NEU: Fläche des aktiven Tabs | `#34373D` | `#FFFFFF` |
| `surfaceHover` | NEU: Hover auf Fläche | `#26282D` | `#E6E8EE` |
| `surfacePressed` | NEU: Gedrückt / aktiv | `#2F3237` | `#D9DCE1` |
| `surfaceSelected` | NEU: Ausgewählte Zeile oder Karte | `#44211F` | `#FFDDDA` |
| `surfaceDisabled` | NEU: Deaktivierte Fläche | `#14161A` | `#E6E8EB` |
| `textDisabled` | NEU: Deaktivierter Text (keine Kontrastpflicht) | `#6D6F71` | `#7E8084` |
| `focusRing` | NEU: Fokusrahmen 2 px, 2 px Abstand | `#E4E8EF` | `#111419` |
| `onAccent` | NEU: Schrift auf Rot | `#FCFCFC` | `#FCFCFC` |
| `goldText` | NEU: Gold als Schrift (im Hell-Modus dunkler) | `#F2BF47` | `#845500` |
| `ratingInk` | NEU: Zahl auf Noten- und Liga-Flächen | `#0D0F14` | `#0C0E13` |

## Marketing und Liga (beide Modi)

| Rolle | Zweck | Wert |
|---|---|---|
| `mkRed` | Marketing: rote Vollfläche | `#E31D29` |
| `mkRedDeep` | Marketing: zweites Rot für Tiefe, Streifen | `#8A0410` |
| `mkInk` | Marketing: Schwarz | `#0D0F14` |
| `mkPaper` | Marketing: Weiß / Kreide | `#F4F5F8` |
| `onMkRed` | Marketing: kleine Schrift auf Rot | `#FCFCFC` |
| `onMkRedLarge` | Marketing: Schlagzeile auf Rot | `#FCFCFC` |
| `leagueBL` | Akzent Bundesliga-Konto (Fläche) | `#9CACFF` |
| `leaguePL` | Akzent Premier-League-Konto (Fläche) | `#9DFFB2` |
| `leagueSL` | Akzent Süper-Lig-Konto (Fläche) | `#DECEFF` |

## Schrift, Größen, Radien

- Überschrift: **Barlow Condensed**, Text: **Barlow**, Zahlen: **Barlow Condensed** mit `tabular-nums`, Beschriftung: **Barlow Condensed**.
- Größen (px): display 68/64, h1 44/44, h2 32/34, h3 24/28, title 20/24, body 16/24, small 14/20, label 13/16, caption 12/16, micro 10/12, ovr 56/52, stat 18/20.
- Radien: `radius-xs` 2 px (Chips, Tags), `radius-sm` 4 px (Buttons, Eingabefelder), `radius-md` 6 px (Karten, Tabellen), `radius-lg` 8 px (Dialoge), `cut-sm` 8 px (Angeschnittene Ecke klein (Buttons, Chips mit Aktion)), `cut-md` 14 px (Angeschnittene Ecke Spielerkarte), `cut-lg` 28 px (Angeschnittene Ecke Post-Rahmen).
- Raster 4 pt, Gutter 20, mobile Spalte 560 px, Breakpoints 720 und 960 bleiben.
