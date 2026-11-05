# Testmatrix Farbe

Stand 04.11.2026. Alle Werte selbst gerechnet mit `_werkzeug/farbe.py` (WCAG 2.x, APCA 0.0.98G-4g, Farbschwäche-Simulation nach Machado 2009 mit Stärke 1,0, Farbabstand in OKLab ×100). Keine Zahl ist geschätzt.

## Wie man die Tabelle liest

- **WCAG**: Kontrastverhältnis. Text braucht mindestens 4,5 : 1, große Schrift und Nicht-Text (Ränder, Icons, Fokus) 3 : 1.
- **APCA Lc**: neueres Kontrastmaß, das helle Schrift auf dunkel realistischer bewertet. Minus heißt helle Schrift auf dunklem Grund. Ziele: Fließtext Lc 75, Inhaltstext Lc 60, große Schrift Lc 45, Nicht-Text Lc 30.
- **ΔL**: Helligkeitsabstand zweier Flächen (OKLab ×100). Unter 3 wirkt es flach, ab 4 deutlich.
- **ΔE**: Farbabstand. Ab 10 sind zwei Farben klar trennbar, auch in der Simulation von Rot-Grün-Schwäche (protan, deutan) und Blau-Gelb-Schwäche (tritan).

## Ausgangslage: die heutige App

| Stufe | ΔL | Kontrast |
|---|---|---|
| background → surfaceSunken | 2,5 | 1,02 : 1 |
| surfaceSunken → surfaceDeep | 1,5 | 1,02 : 1 |
| surfaceDeep → surface | 2,3 | 1,04 : 1 |
| surface → surfaceElevated | 3,7 | 1,08 : 1 |
| surfaceElevated → surfaceOverlay | 4,8 | 1,14 : 1 |

Drei von fünf Stufen liegen unter ΔL 3. Das bestätigt die Kritik: Tabs und Flächen wirken flach. Der Hintergrund `#050507` hat Kanalwerte von 5 bis 7 und liegt damit fast bei „Pixel aus“. Auf OLED-Bildschirmen schalten solche Pixel beim Scrollen verzögert an. Dadurch zieht dunkler Inhalt Schlieren (Black Smear). Hier ist das nicht messbar, es braucht einen Gerätetest. Die Faustregel „kein Kanal unter 12“ steht deshalb als eigene Prüfung in der Matrix.

## Übersicht

| Option | Modus | v1 bestanden | v2 bestanden | offen in v2 |
|---|---|---|---|---|
| A Anzeigetafel | dark | 45 / 75 | **74 / 75** | accent auf surface |
| A Anzeigetafel | light | 46 / 69 | **69 / 69** | – |
| B Messgerät | dark | 44 / 75 | **72 / 75** | mkRed auf mkInk, accent auf background, accent auf surface |
| B Messgerät | light | 49 / 69 | **69 / 69** | – |
| C Flutlicht | dark | 44 / 75 | **73 / 75** | mkRed auf mkInk, accent auf surface |
| C Flutlicht | light | 46 / 69 | **69 / 69** | – |

## Was sich von v1 zu v2 geändert hat

- **Flächenstufen:** Alle Dunkel-Stufen auf mindestens 3,5 Punkte Abstand gezogen (v1: 2,2–2,7). Der Hintergrund bleibt über Kanalwert 12 (OLED). Im Hell-Modus ist die Seite jetzt grau (L 0,905) und Karten sind weiß. So gibt es genug Abstand nach oben.
- **Rote Schrift:** accentText heller (L 0,805 bei leicht weniger Buntheit), weil APCA Lc 60 bei v1 nicht erreicht wurde. accentMuted dunkler, damit rote Schrift auch auf dem Chip-Grund trägt.
- **Roter Button:** Button-Rot in allen drei Richtungen so dunkel (L 0,58–0,60), dass weiße Schrift 4,5 : 1 erreicht. C nutzt für Plakate dasselbe tiefe Rot mit Kreide-Schrift (Lc 72). Ein helleres Signalrot mit schwarzer Schrift (v2-Entwurf, L 0,685) wirkte korallig und erreichte nur Lc 47, deshalb verworfen.
- **Noten-Skala:** Per Rechnung über 60 000 Kombinationen gesucht: Jedes Paar der fünf Stufen hat jetzt in allen vier Sehweisen ΔE ≥ 9,8 (v1: 2,1). Dafür ist die Helligkeit nicht mehr stufenweise ansteigend. Die Zahl steht deshalb immer im Chip.
- **Auf und Ab:** Aufwertung ist jetzt Türkis statt Grün und deutlich heller (Dunkel) bzw. dunkler (Hell) als Abwertung. So bleibt sie auch bei Rot-Grün-Schwäche unterscheidbar (ΔE ≥ 10). Pfeil und Vorzeichen sind trotzdem Pflicht.
- **Liga-Akzente:** Gesucht per Rechnung über alle Farbtöne: BL Blauviolett, PL Mint, SL Flieder. Mehr als ΔE 10,8 ist mit Gold und Rot im Vergleich nicht erreichbar, deshalb Schwelle 10. Liga-Farben sind Flächen mit dunkler Schrift, keine Schriftfarben, und stehen immer neben dem Kürzel.
- **Rot für Schlecht (nur A, Runde 4):** Burhans Wunsch: zwei echte Rottöne, kein Rosa. Note Poor ist das Rot von Sofascore (#DC0C00) mit weißer Zahl: 5,0 : 1, Lc 76. Abwertung ist das Rot der Website (#FF5260, wie heute in der App) auf dunklem Rot-Chip: 5,1 : 1, aber nur Lc 41. Das ist eine bewusste Ausnahme: WCAG hält, APCA verlangt für kleine Schrift Lc 60. Der Chip trägt deshalb immer Pfeil und Minus, fett. Im Hell-Modus bleibt Abwertung #BB081A (6,0 : 1, Lc 74).
- **Marketing:** Rote Wörter auf Schwarz nutzen accentText, nicht mkRed. mkRed ist nur Fläche.

## Bewusst offene Punkte in v2 (mit Regel)

- **Rote Flächen (accent) als Nicht-Text:** WCAG 3 : 1 ist erfüllt, APCA erreicht Lc 27–29 statt 30. Noch helleres Rot würde weiße Button-Schrift unter 4,5 : 1 drücken. Regel: Rote Flächen und Linien mindestens 8 px bzw. 2 px. Kleinere rote Punkte kommen in `accentText`.
- **Option C, verworfenes Signalrot:** Ein helleres Plakatrot (L 0,685) mit schwarzer Schrift erreichte nur Lc 47 und wirkte korallig. C nutzt deshalb dasselbe tiefe Rot wie A und B, mit Kreide-Schrift.
- **Auf und Ab:** Rechnerisch auch bei Farbschwäche trennbar, aber nur knapp über ΔE 10. Pfeil (▲/▼) und Vorzeichen (+/−) bleiben Pflicht.

## Option A · Anzeigetafel · v2 im Detail

### Dark

| Art | Paar | Vordergrund | Hintergrund | WCAG | APCA Lc | ΔL / ΔE | Ziel | Ergebnis |
|---|---|---|---|---|---|---|---|---|
| Text | textPrimary auf background | `#F2F3F6` | `#0D0F14` | 17,28 | -99,6 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surface | `#F2F3F6` | `#1D1F24` | 14,86 | -98,0 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceElevated | `#F2F3F6` | `#272A30` | 12,96 | -96,2 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceHover | `#F2F3F6` | `#26282D` | 13,29 | -96,5 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceOverlay | `#F2F3F6` | `#34373D` | 10,75 | -93,0 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textSecondary auf background | `#CDCFD5` | `#0D0F14` | 12,31 | -77,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surface | `#CDCFD5` | `#1D1F24` | 10,58 | -75,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceElevated | `#CDCFD5` | `#272A30` | 9,23 | -73,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceHover | `#CDCFD5` | `#26282D` | 9,47 | -74,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceOverlay | `#CDCFD5` | `#34373D` | 7,66 | -70,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf background | `#C0C2C8` | `#0D0F14` | 10,76 | -69,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surface | `#C0C2C8` | `#1D1F24` | 9,26 | -67,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceElevated | `#C0C2C8` | `#272A30` | 8,08 | -66,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceHover | `#C0C2C8` | `#26282D` | 8,28 | -66,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceOverlay | `#C0C2C8` | `#34373D` | 6,70 | -62,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textMuted auf background | `#A7A9AE` | `#0D0F14` | 8,15 | -55,3 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surface | `#A7A9AE` | `#1D1F24` | 7,01 | -53,7 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceElevated | `#A7A9AE` | `#272A30` | 6,12 | -51,9 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceHover | `#A7A9AE` | `#26282D` | 6,27 | -52,2 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceOverlay | `#A7A9AE` | `#34373D` | 5,07 | -48,7 | – | ≥4,5 · Lc 45 | ✅ |
| Text | accentText auf background | `#FFA29F` | `#0D0F14` | 9,97 | -65,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surface | `#FFA29F` | `#1D1F24` | 8,57 | -63,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surfaceElevated | `#FFA29F` | `#272A30` | 7,48 | -62,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf accentMuted | `#FFA29F` | `#401011` | 8,40 | -63,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf background | `#5EF9F1` | `#0D0F14` | 14,88 | -89,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf surface | `#5EF9F1` | `#1D1F24` | 12,79 | -87,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf positiveMuted | `#5EF9F1` | `#002F2D` | 11,28 | -86,0 | – | ≥4,5 · Lc 60 | ✅ |
| Abwertung (Ausnahme) | ratingDown auf accentMuted | `#FF5260` | `#401011` | 5,10 | -41,5 | – | ≥4,5 · Lc 40 | ✅ |
| Text | goldText auf background | `#F2BF47` | `#0D0F14` | 11,24 | -72,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf surface | `#F2BF47` | `#1D1F24` | 9,67 | -70,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf goldMuted | `#F2BF47` | `#392C0C` | 8,00 | -67,8 | – | ≥4,5 · Lc 60 | ✅ |
| Button-Text | onAccent auf accent | `#FCFCFC` | `#E31D29` | 4,58 | -73,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingElite | `#0D0F14` | `#85BAFF` | 9,55 | 64,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingExcellent | `#0D0F14` | `#9EFFFE` | 16,60 | 95,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingGood | `#0D0F14` | `#D6FC91` | 16,61 | 95,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingAverage | `#0D0F14` | `#F8A052` | 9,26 | 63,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onRatingPoor auf ratingPoor | `#FCFCFC` | `#DC0C00` | 5,00 | -76,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueBL | `#0D0F14` | `#9CACFF` | 8,91 | 61,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leaguePL | `#0D0F14` | `#9DFFB2` | 15,86 | 93,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueSL | `#0D0F14` | `#DECEFF` | 13,12 | 81,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onMkRed auf mkRed | `#FCFCFC` | `#E31D29` | 4,58 | -73,9 | – | ≥4,5 · Lc 60 | ✅ |
| Schlagzeile | onMkRedLarge auf mkRed | `#FCFCFC` | `#E31D29` | 4,58 | -73,9 | – | ≥3,0 · Lc 45 | ✅ |
| Text | mkPaper auf mkInk | `#F4F5F8` | `#0D0F14` | 17,58 | -100,9 | – | ≥4,5 · Lc 75 | ✅ |
| Nicht-Text | mkRed auf mkInk | `#E31D29` | `#0D0F14` | 4,08 | -30,9 | – | ≥3,0 · Lc 30 | ✅ |
| Text | accentText auf mkInk | `#FFA29F` | `#0D0F14` | 9,97 | -65,5 | – | ≥4,5 · Lc 60 | ✅ |
| Nicht-Text | borderStrong auf surface | `#808389` | `#1D1F24` | 4,34 | -34,1 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf background | `#E4E8EF` | `#0D0F14` | 15,60 | -92,3 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf surface | `#E4E8EF` | `#1D1F24` | 13,42 | -90,7 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | textFaint auf background | `#7B7D82` | `#0D0F14` | 4,65 | -32,9 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf background | `#E31D29` | `#0D0F14` | 4,08 | -30,9 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf surface | `#E31D29` | `#1D1F24` | 3,51 | -29,3 | – | ≥3,0 · Lc 30 | ❌ |
| Stufe | background → surfaceDeep | `#15171C` | `#0D0F14` | 1,07 | – | 3,6 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceDeep → surface | `#1D1F24` | `#15171C` | 1,09 | – | 3,5 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceElevated | `#272A30` | `#1D1F24` | 1,15 | – | 4,5 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceElevated → surfaceOverlay | `#34373D` | `#272A30` | 1,21 | – | 5,2 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceSunken → background | `#0D0F14` | `#06080C` | 1,05 | – | 3,5 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceWarm | `#352222` | `#1D1F24` | 1,10 | – | 3,6 | ΔL ≥3 | ✅ sichtbar |
| Stufe | tabTrack → tabActive | `#34373D` | `#15171C` | 1,50 | – | 13,2 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceHover | `#26282D` | `#1D1F24` | 1,12 | – | 3,8 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceHover → surfacePressed | `#2F3237` | `#26282D` | 1,15 | – | 3,9 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceSelected | `#44211F` | `#1D1F24` | 1,16 | – | 5,6 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceDisabled | `#14161A` | `#1D1F24` | 1,10 | – | 4,0 | ΔL ≥3 | ✅ sichtbar |
| Farbschwäche | Auf ↔ Ab (normal) | `#5EF9F1` | `#FF5260` | – | – | 40,1 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (normal): Good–Excellent | – | – | – | – | 13,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (normal): BL–SL | – | – | – | – | 13,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (protan) | `#EBEDF1` | `#80795F` | – | – | 37,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (protan): Good–Excellent | – | – | – | – | 13,9 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (protan): BL–SL | – | – | – | – | 11,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (deutan) | `#D4DBF2` | `#AC9E5B` | – | – | 23,1 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (deutan): Good–Excellent | – | – | – | – | 14,0 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–Gold | – | – | – | – | 11,6 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (tritan) | `#00FFF6` | `#FF2458` | – | – | 47,4 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (tritan): Good–Excellent | – | – | – | – | 10,0 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (tritan): SL–Gold | – | – | – | – | 10,8 | ΔE ≥10 | ✅ |
| OLED | background #0D0F14 (R13 G15 B20) | – | `#0D0F14` | – | – | – | kein Kanal unter 12 | ✅ |

### Light

| Art | Paar | Vordergrund | Hintergrund | WCAG | APCA Lc | ΔL / ΔE | Ziel | Ergebnis |
|---|---|---|---|---|---|---|---|---|
| Text | textPrimary auf background | `#111419` | `#DBDEE3` | 13,68 | 85,5 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surface | `#111419` | `#F2F4F7` | 16,75 | 98,4 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceElevated | `#111419` | `#FFFFFF` | 18,45 | 105,1 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceHover | `#111419` | `#E6E8EE` | 15,06 | 91,5 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceOverlay | `#111419` | `#E7E9EF` | 15,20 | 92,1 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textSecondary auf background | `#3E4148` | `#DBDEE3` | 7,58 | 74,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surface | `#3E4148` | `#F2F4F7` | 9,28 | 87,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceElevated | `#3E4148` | `#FFFFFF` | 10,22 | 93,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceHover | `#3E4148` | `#E6E8EE` | 8,34 | 80,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceOverlay | `#3E4148` | `#E7E9EF` | 8,42 | 80,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf background | `#4B4E55` | `#DBDEE3` | 6,18 | 69,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surface | `#4B4E55` | `#F2F4F7` | 7,56 | 82,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceElevated | `#4B4E55` | `#FFFFFF` | 8,33 | 88,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceHover | `#4B4E55` | `#E6E8EE` | 6,80 | 75,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceOverlay | `#4B4E55` | `#E7E9EF` | 6,86 | 75,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textMuted auf background | `#565960` | `#DBDEE3` | 5,20 | 64,8 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surface | `#565960` | `#F2F4F7` | 6,37 | 77,6 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceElevated | `#565960` | `#FFFFFF` | 7,02 | 84,3 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceHover | `#565960` | `#E6E8EE` | 5,73 | 70,7 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceOverlay | `#565960` | `#E7E9EF` | 5,78 | 71,3 | – | ≥4,5 · Lc 45 | ✅ |
| Text | accentText auf background | `#BB081A` | `#DBDEE3` | 4,92 | 60,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surface | `#BB081A` | `#F2F4F7` | 6,03 | 73,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surfaceElevated | `#BB081A` | `#FFFFFF` | 6,64 | 80,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf accentMuted | `#BB081A` | `#FFDDDA` | 5,25 | 64,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf background | `#005763` | `#DBDEE3` | 6,12 | 68,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf surface | `#005763` | `#F2F4F7` | 7,49 | 81,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf positiveMuted | `#005763` | `#CBECF2` | 6,61 | 73,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingDown auf accentMuted | `#BB081A` | `#FFDDDA` | 5,25 | 64,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf background | `#845500` | `#DBDEE3` | 4,75 | 62,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf surface | `#845500` | `#F2F4F7` | 5,81 | 74,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf goldMuted | `#845500` | `#F7E5B9` | 5,14 | 66,9 | – | ≥4,5 · Lc 60 | ✅ |
| Button-Text | onAccent auf accent | `#FCFCFC` | `#DB1B26` | 4,88 | -75,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingElite | `#0C0E13` | `#85BAFF` | 9,62 | 64,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingExcellent | `#0C0E13` | `#9EFFFE` | 16,72 | 96,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingGood | `#0C0E13` | `#D6FC91` | 16,72 | 95,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingAverage | `#0C0E13` | `#F8A052` | 9,32 | 63,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onRatingPoor auf ratingPoor | `#FCFCFC` | `#DC0C00` | 5,00 | -76,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueBL | `#0C0E13` | `#9CACFF` | 8,97 | 61,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leaguePL | `#0C0E13` | `#9DFFB2` | 15,98 | 93,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueSL | `#0C0E13` | `#DECEFF` | 13,22 | 81,4 | – | ≥4,5 · Lc 60 | ✅ |
| Nicht-Text | borderStrong auf surface | `#72747A` | `#F2F4F7` | 4,24 | 65,8 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf background | `#111419` | `#DBDEE3` | 13,68 | 85,5 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf surface | `#111419` | `#F2F4F7` | 16,75 | 98,4 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | textFaint auf background | `#777A80` | `#DBDEE3` | 3,19 | 50,3 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf background | `#DB1B26` | `#DBDEE3` | 3,71 | 52,9 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf surface | `#DB1B26` | `#F2F4F7` | 4,54 | 65,7 | – | ≥3,0 · Lc 30 | ✅ |
| Stufe | background → surfaceDeep | `#E7E9EE` | `#DBDEE3` | 1,11 | – | 3,4 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceDeep → surface | `#F2F4F7` | `#E7E9EE` | 1,10 | – | 3,3 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceElevated | `#FFFFFF` | `#F2F4F7` | 1,10 | – | 3,4 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceElevated → surfaceOverlay | `#E7E9EF` | `#FFFFFF` | 1,21 | – | 6,6 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceSunken → background | `#DBDEE3` | `#D0D3D8` | 1,11 | – | 3,4 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceWarm | `#F9E1E1` | `#F2F4F7` | 1,13 | – | 3,7 | ΔL ≥3 | ✅ sichtbar |
| Stufe | tabTrack → tabActive | `#FFFFFF` | `#E3E6EC` | 1,25 | – | 7,6 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceHover | `#E6E8EE` | `#F2F4F7` | 1,11 | – | 3,5 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceHover → surfacePressed | `#D9DCE1` | `#E6E8EE` | 1,12 | – | 3,8 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceSelected | `#FFDDDA` | `#F2F4F7` | 1,15 | – | 4,2 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceDisabled | `#E6E8EB` | `#F2F4F7` | 1,11 | – | 3,6 | ΔL ≥3 | ✅ sichtbar |
| Farbschwäche | Auf ↔ Ab (normal) | `#005763` | `#BB081A` | – | – | 28,5 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (normal): Good–Excellent | – | – | – | – | 13,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (normal): BL–SL | – | – | – | – | 13,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (protan) | `#4D5364` | `#4E4517` | – | – | 10,8 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (protan): Good–Excellent | – | – | – | – | 13,9 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (protan): BL–SL | – | – | – | – | 11,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (deutan) | `#414B63` | `#76690E` | – | – | 17,8 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (deutan): Good–Excellent | – | – | – | – | 14,0 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–SL | – | – | – | – | 13,0 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (tritan) | `#005C5B` | `#CF0014` | – | – | 31,0 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (tritan): Good–Excellent | – | – | – | – | 10,0 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (tritan): PL–SL | – | – | – | – | 12,1 | ΔE ≥10 | ✅ |

### v1 (zum Vergleich): durchgefallen

- **dark** (30): textTertiary auf background (8,39 : 1 / Lc -56,4); textTertiary auf surface (7,63 : 1 / Lc -55,4); textTertiary auf surfaceElevated (6,76 : 1 / Lc -54,0); textTertiary auf surfaceHover (6,92 : 1 / Lc -54,3); textTertiary auf surfaceOverlay (5,74 : 1 / Lc -51,6); textMuted auf surfaceOverlay (4,92 : 1 / Lc -44,6); accentText auf background (6,93 : 1 / Lc -48,6); accentText auf surface (6,31 : 1 / Lc -47,7); accentText auf surfaceElevated (5,58 : 1 / Lc -46,2); accentText auf accentMuted (5,22 : 1 / Lc -44,9); ratingDown auf accentMuted (5,22 : 1 / Lc -44,9); onAccent auf accent (3,95 : 1 / Lc -69,4); ratingInk auf ratingElite (6,68 : 1 / Lc 48,7); onRatingPoor auf ratingPoor (5,66 : 1 / Lc 43,0); ratingInk auf leagueBL (6,12 : 1 / Lc 45,2); onMkRed auf mkRed (4,35 : 1 / Lc 35,2); accentText auf mkInk (6,93 : 1 / Lc -48,6); borderStrong auf surface (2,92 : 1 / Lc -20,5); textFaint auf background (3,51 : 1 / Lc -23,9); background → surfaceDeep (1,05 : 1 / Lc –); surfaceDeep → surface (1,05 : 1 / Lc –); surfaceSunken → background (1,03 : 1 / Lc –); surface → surfaceWarm (1,00 : 1 / Lc –); surface → surfaceDisabled (1,05 : 1 / Lc –); Noten-Skala, engstes Paar (protan): Average–Good (3,5); Liga-Akzente + Rot + Gold, engstes Paar (protan): PL–Gold (6,7); Auf ↔ Ab (deutan) (8,1); Noten-Skala, engstes Paar (deutan): Average–Good (2,1); Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–Gold (2,4); Noten-Skala, engstes Paar (tritan): Excellent–Elite (7,9)
- **light** (23): textMuted auf surfaceOverlay (4,07 : 1 / Lc 56,5); ratingUp auf background (4,12 : 1 / Lc 61,5); ratingUp auf positiveMuted (4,06 : 1 / Lc 60,5); goldText auf background (3,97 : 1 / Lc 60,6); goldText auf surface (4,34 : 1 / Lc 66,6); goldText auf goldMuted (3,96 : 1 / Lc 60,6); ratingInk auf ratingElite (6,68 : 1 / Lc 48,7); onRatingPoor auf ratingPoor (5,66 : 1 / Lc 43,0); ratingInk auf leagueBL (3,41 : 1 / Lc 25,8); ratingInk auf leaguePL (4,39 : 1 / Lc 33,4); ratingInk auf leagueSL (3,99 : 1 / Lc 30,7); textFaint auf background (2,61 : 1 / Lc 46,3); background → surfaceDeep (1,05 : 1 / Lc –); surface → surfaceElevated (1,07 : 1 / Lc –); surface → surfaceWarm (1,02 : 1 / Lc –); surface → surfaceHover (1,08 : 1 / Lc –); surfaceHover → surfacePressed (1,08 : 1 / Lc –); Noten-Skala, engstes Paar (protan): Average–Good (3,5); Auf ↔ Ab (deutan) (4,7); Noten-Skala, engstes Paar (deutan): Average–Good (2,1); Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–Rot (4,3); Noten-Skala, engstes Paar (tritan): Excellent–Elite (7,9); Liga-Akzente + Rot + Gold, engstes Paar (tritan): BL–SL (3,7)

## Option B · Messgerät · v2 im Detail

### Dark

| Art | Paar | Vordergrund | Hintergrund | WCAG | APCA Lc | ΔL / ΔE | Ziel | Ergebnis |
|---|---|---|---|---|---|---|---|---|
| Text | textPrimary auf background | `#F2F3F5` | `#131517` | 16,49 | -99,1 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surface | `#F2F3F5` | `#232528` | 13,84 | -97,1 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceElevated | `#F2F3F5` | `#2E3133` | 11,80 | -94,7 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceHover | `#F2F3F5` | `#2D2F31` | 12,10 | -95,1 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceOverlay | `#F2F3F5` | `#3B3D40` | 9,81 | -91,2 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textSecondary auf background | `#CDD0D2` | `#131517` | 11,81 | -77,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surface | `#CDD0D2` | `#232528` | 9,91 | -74,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceElevated | `#CDD0D2` | `#2E3133` | 8,45 | -72,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceHover | `#CDD0D2` | `#2D2F31` | 8,67 | -72,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceOverlay | `#CDD0D2` | `#3B3D40` | 7,03 | -69,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf background | `#C0C3C6` | `#131517` | 10,34 | -69,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surface | `#C0C3C6` | `#232528` | 8,68 | -67,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceElevated | `#C0C3C6` | `#2E3133` | 7,40 | -64,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceHover | `#C0C3C6` | `#2D2F31` | 7,59 | -65,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceOverlay | `#C0C3C6` | `#3B3D40` | 6,15 | -61,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textMuted auf background | `#A7A9AC` | `#131517` | 7,77 | -54,8 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surface | `#A7A9AC` | `#232528` | 6,52 | -52,7 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceElevated | `#A7A9AC` | `#2E3133` | 5,56 | -50,3 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceHover | `#A7A9AC` | `#2D2F31` | 5,70 | -50,8 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceOverlay | `#A7A9AC` | `#3B3D40` | 4,62 | -46,8 | – | ≥4,5 · Lc 45 | ✅ |
| Text | accentText auf background | `#FFA29E` | `#131517` | 9,51 | -65,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surface | `#FFA29E` | `#232528` | 7,99 | -63,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surfaceElevated | `#FFA29E` | `#2E3133` | 6,81 | -60,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf accentMuted | `#FFA29E` | `#401010` | 8,40 | -63,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf background | `#A8E1FF` | `#131517` | 12,97 | -82,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf surface | `#A8E1FF` | `#232528` | 10,89 | -80,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf positiveMuted | `#A8E1FF` | `#142E3F` | 9,97 | -79,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingDown auf accentMuted | `#FFA29E` | `#401010` | 8,40 | -63,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf background | `#E9B452` | `#131517` | 9,69 | -66,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf surface | `#E9B452` | `#232528` | 8,13 | -63,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf goldMuted | `#E9B452` | `#3C2E14` | 6,98 | -61,6 | – | ≥4,5 · Lc 60 | ✅ |
| Button-Text | onAccent auf accent | `#FCFCFC` | `#DC2628` | 4,70 | -75,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingElite | `#131517` | `#85BAFF` | 9,12 | 64,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingExcellent | `#131517` | `#9EFFFE` | 15,85 | 95,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingGood | `#131517` | `#D6FC91` | 15,86 | 95,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingAverage | `#131517` | `#F8A052` | 8,84 | 62,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onRatingPoor auf ratingPoor | `#131517` | `#FFBFB6` | 11,66 | 76,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueBL | `#131517` | `#9CACFF` | 8,51 | 60,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leaguePL | `#131517` | `#9DFFB2` | 15,15 | 92,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueSL | `#131517` | `#DECEFF` | 12,53 | 80,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onMkRed auf mkRed | `#FCFCFC` | `#DC2628` | 4,70 | -75,0 | – | ≥4,5 · Lc 60 | ✅ |
| Schlagzeile | onMkRedLarge auf mkRed | `#FCFCFC` | `#DC2628` | 4,70 | -75,0 | – | ≥3,0 · Lc 45 | ✅ |
| Text | mkPaper auf mkInk | `#F6F5F1` | `#131517` | 16,78 | -100,4 | – | ≥4,5 · Lc 75 | ✅ |
| Nicht-Text | mkRed auf mkInk | `#DC2628` | `#131517` | 3,79 | -29,3 | – | ≥3,0 · Lc 30 | ❌ |
| Text | accentText auf mkInk | `#FFA29E` | `#131517` | 9,51 | -65,1 | – | ≥4,5 · Lc 60 | ✅ |
| Nicht-Text | borderStrong auf surface | `#888B8E` | `#232528` | 4,49 | -37,0 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf background | `#6DC4FF` | `#131517` | 9,58 | -65,4 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf surface | `#6DC4FF` | `#232528` | 8,04 | -63,3 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | textFaint auf background | `#7B7D80` | `#131517` | 4,43 | -32,4 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf background | `#DC2628` | `#131517` | 3,79 | -29,3 | – | ≥3,0 · Lc 30 | ❌ |
| Nicht-Text | accent auf surface | `#DC2628` | `#232528` | 3,18 | -27,2 | – | ≥3,0 · Lc 30 | ❌ |
| Stufe | background → surfaceDeep | `#1B1D1F` | `#131517` | 1,08 | – | 3,5 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceDeep → surface | `#232528` | `#1B1D1F` | 1,10 | – | 3,4 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceElevated | `#2E3133` | `#232528` | 1,17 | – | 4,7 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceElevated → surfaceOverlay | `#3B3D40` | `#2E3133` | 1,20 | – | 4,8 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceSunken → background | `#131517` | `#0C0D0F` | 1,06 | – | 3,6 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceWarm | `#3B2926` | `#232528` | 1,12 | – | 3,8 | ΔL ≥3 | ✅ sichtbar |
| Stufe | tabTrack → tabActive | `#3B3D40` | `#1B1D1F` | 1,55 | – | 13,0 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceHover | `#2D2F31` | `#232528` | 1,14 | – | 4,0 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceHover → surfacePressed | `#36383A` | `#2D2F31` | 1,14 | – | 3,6 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceSelected | `#1C3648` | `#232528` | 1,22 | – | 5,7 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceDisabled | `#1A1C1E` | `#232528` | 1,11 | – | 3,8 | ΔL ≥3 | ✅ sichtbar |
| Farbschwäche | Auf ↔ Ab (normal) | `#A8E1FF` | `#FFA29E` | – | – | 19,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (normal): Poor–Average | – | – | – | – | 11,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (normal): BL–SL | – | – | – | – | 13,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (protan) | `#D2DFFF` | `#B5B09D` | – | – | 16,5 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (protan): Poor–Elite | – | – | – | – | 12,6 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (protan): BL–SL | – | – | – | – | 11,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (deutan) | `#C6D5FF` | `#CBC29D` | – | – | 12,8 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (deutan): Poor–Excellent | – | – | – | – | 10,0 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–SL | – | – | – | – | 13,0 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (tritan) | `#8AE9EA` | `#FF97A1` | – | – | 23,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (tritan): Poor–Average | – | – | – | – | 9,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (tritan): PL–SL | – | – | – | – | 12,1 | ΔE ≥10 | ✅ |
| OLED | background #131517 (R19 G21 B23) | – | `#131517` | – | – | – | kein Kanal unter 12 | ✅ |

### Light

| Art | Paar | Vordergrund | Hintergrund | WCAG | APCA Lc | ΔL / ΔE | Ziel | Ergebnis |
|---|---|---|---|---|---|---|---|---|
| Text | textPrimary auf background | `#101419` | `#DFDEDA` | 13,73 | 85,7 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surface | `#101419` | `#F5F4F1` | 16,81 | 98,5 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceElevated | `#101419` | `#FFFFFF` | 18,48 | 105,1 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceHover | `#101419` | `#EAE8E4` | 15,11 | 91,6 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceOverlay | `#101419` | `#EBE9E5` | 15,24 | 92,2 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textSecondary auf background | `#3C4247` | `#DFDEDA` | 7,56 | 74,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surface | `#3C4247` | `#F5F4F1` | 9,26 | 87,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceElevated | `#3C4247` | `#FFFFFF` | 10,18 | 93,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceHover | `#3C4247` | `#EAE8E4` | 8,32 | 80,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceOverlay | `#3C4247` | `#EBE9E5` | 8,40 | 80,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf background | `#4A4F55` | `#DFDEDA` | 6,14 | 69,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surface | `#4A4F55` | `#F5F4F1` | 7,51 | 82,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceElevated | `#4A4F55` | `#FFFFFF` | 8,27 | 88,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceHover | `#4A4F55` | `#EAE8E4` | 6,75 | 75,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceOverlay | `#4A4F55` | `#EBE9E5` | 6,82 | 75,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textMuted auf background | `#545A60` | `#DFDEDA` | 5,19 | 64,8 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surface | `#545A60` | `#F5F4F1` | 6,35 | 77,6 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceElevated | `#545A60` | `#FFFFFF` | 6,98 | 84,2 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceHover | `#545A60` | `#EAE8E4` | 5,70 | 70,7 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceOverlay | `#545A60` | `#EBE9E5` | 5,76 | 71,3 | – | ≥4,5 · Lc 45 | ✅ |
| Text | accentText auf background | `#BB0916` | `#DFDEDA` | 4,93 | 60,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surface | `#BB0916` | `#F5F4F1` | 6,04 | 73,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surfaceElevated | `#BB0916` | `#FFFFFF` | 6,64 | 80,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf accentMuted | `#BB0916` | `#FFDDDA` | 5,25 | 64,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf background | `#005182` | `#DFDEDA` | 6,24 | 69,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf surface | `#005182` | `#F5F4F1` | 7,64 | 81,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf positiveMuted | `#005182` | `#D2EAFC` | 6,77 | 74,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingDown auf accentMuted | `#BB0916` | `#FFDDDA` | 5,25 | 64,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf background | `#845500` | `#DFDEDA` | 4,75 | 62,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf surface | `#845500` | `#F5F4F1` | 5,82 | 74,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf goldMuted | `#845500` | `#F7E5B9` | 5,14 | 66,9 | – | ≥4,5 · Lc 60 | ✅ |
| Button-Text | onAccent auf accent | `#FCFCFC` | `#DB2527` | 4,75 | -75,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingElite | `#121416` | `#85BAFF` | 9,20 | 64,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingExcellent | `#121416` | `#9EFFFE` | 15,99 | 95,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingGood | `#121416` | `#D6FC91` | 16,00 | 95,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingAverage | `#121416` | `#F8A052` | 8,92 | 62,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onRatingPoor auf ratingPoor | `#121416` | `#FFBFB6` | 11,76 | 76,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueBL | `#121416` | `#9CACFF` | 8,58 | 60,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leaguePL | `#121416` | `#9DFFB2` | 15,28 | 92,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueSL | `#121416` | `#DECEFF` | 12,64 | 80,9 | – | ≥4,5 · Lc 60 | ✅ |
| Nicht-Text | borderStrong auf surface | `#767470` | `#F5F4F1` | 4,24 | 65,9 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf background | `#0061BE` | `#DFDEDA` | 4,52 | 60,2 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf surface | `#0061BE` | `#F5F4F1` | 5,53 | 73,0 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | textFaint auf background | `#767B80` | `#DFDEDA` | 3,17 | 50,1 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf background | `#DB2527` | `#DFDEDA` | 3,62 | 52,4 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf surface | `#DB2527` | `#F5F4F1` | 4,43 | 65,3 | – | ≥3,0 · Lc 30 | ✅ |
| Stufe | background → surfaceDeep | `#EAE9E6` | `#DFDEDA` | 1,11 | – | 3,4 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceDeep → surface | `#F5F4F1` | `#EAE9E6` | 1,10 | – | 3,3 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceElevated | `#FFFFFF` | `#F5F4F1` | 1,10 | – | 3,3 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceElevated → surfaceOverlay | `#EBE9E5` | `#FFFFFF` | 1,21 | – | 6,6 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceSunken → background | `#DFDEDA` | `#D4D3CE` | 1,11 | – | 3,4 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceWarm | `#F8E3DB` | `#F5F4F1` | 1,12 | – | 3,6 | ΔL ≥3 | ✅ sichtbar |
| Stufe | tabTrack → tabActive | `#FFFFFF` | `#E7E6E2` | 1,25 | – | 7,5 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceHover | `#EAE8E4` | `#F5F4F1` | 1,11 | – | 3,6 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceHover → surfacePressed | `#DDDCD7` | `#EAE8E4` | 1,12 | – | 3,8 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceSelected | `#D2EAFC` | `#F5F4F1` | 1,13 | – | 4,2 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceDisabled | `#E8E8E6` | `#F5F4F1` | 1,12 | – | 3,7 | ΔL ≥3 | ✅ sichtbar |
| Farbschwäche | Auf ↔ Ab (normal) | `#005182` | `#BB0916` | – | – | 30,2 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (normal): Poor–Average | – | – | – | – | 11,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (normal): BL–SL | – | – | – | – | 13,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (protan) | `#395384` | `#4E4513` | – | – | 16,4 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (protan): Poor–Elite | – | – | – | – | 12,6 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (protan): BL–SL | – | – | – | – | 11,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (deutan) | `#274981` | `#776907` | – | – | 23,1 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (deutan): Poor–Excellent | – | – | – | – | 10,0 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–SL | – | – | – | – | 13,0 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (tritan) | `#005D63` | `#CF0013` | – | – | 31,0 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (tritan): Poor–Average | – | – | – | – | 9,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (tritan): PL–SL | – | – | – | – | 12,1 | ΔE ≥10 | ✅ |

### v1 (zum Vergleich): durchgefallen

- **dark** (31): textTertiary auf background (8,00 : 1 / Lc -55,8); textTertiary auf surface (7,24 : 1 / Lc -54,7); textTertiary auf surfaceElevated (6,42 : 1 / Lc -53,2); textTertiary auf surfaceHover (6,66 : 1 / Lc -53,7); textTertiary auf surfaceOverlay (5,51 : 1 / Lc -50,8); textMuted auf surfaceOverlay (4,84 : 1 / Lc -44,9); accentText auf background (6,91 : 1 / Lc -49,9); accentText auf surface (6,25 : 1 / Lc -48,8); accentText auf surfaceElevated (5,55 : 1 / Lc -47,2); accentText auf accentMuted (5,25 : 1 / Lc -46,2); ratingDown auf accentMuted (5,25 : 1 / Lc -46,2); onAccent auf accent (3,71 : 1 / Lc -67,6); ratingInk auf ratingElite (5,30 : 1 / Lc 40,9); ratingInk auf ratingExcellent (8,35 : 1 / Lc 60,0); onRatingPoor auf ratingPoor (5,67 : 1 / Lc 44,1); ratingInk auf leagueBL (5,85 : 1 / Lc 44,7); onMkRed auf mkRed (4,56 : 1 / Lc 37,2); accentText auf mkInk (6,91 : 1 / Lc -49,9); borderStrong auf surface (3,03 : 1 / Lc -22,4); textFaint auf background (3,65 : 1 / Lc -26,1); background → surfaceDeep (1,05 : 1 / Lc –); surfaceDeep → surface (1,06 : 1 / Lc –); surfaceSunken → background (1,04 : 1 / Lc –); surface → surfaceWarm (1,00 : 1 / Lc –); surface → surfaceHover (1,09 : 1 / Lc –); surface → surfaceDisabled (1,06 : 1 / Lc –); Noten-Skala, engstes Paar (protan): Average–Good (6,3); Liga-Akzente + Rot + Gold, engstes Paar (protan): PL–Gold (9,9); Noten-Skala, engstes Paar (deutan): Average–Good (6,5); Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–Gold (4,5); Noten-Skala, engstes Paar (tritan): Good–Excellent (7,6)
- **light** (20): textMuted auf surfaceOverlay (4,17 : 1 / Lc 59,3); goldText auf background (4,26 : 1 / Lc 65,5); goldText auf goldMuted (4,09 : 1 / Lc 62,7); onAccent auf accent (4,45 : 1 / Lc -73,4); ratingInk auf ratingElite (5,30 : 1 / Lc 40,9); ratingInk auf ratingExcellent (8,35 : 1 / Lc 60,0); onRatingPoor auf ratingPoor (5,67 : 1 / Lc 44,1); ratingInk auf leagueBL (3,26 : 1 / Lc 25,3); ratingInk auf leaguePL (4,20 : 1 / Lc 32,9); ratingInk auf leagueSL (3,82 : 1 / Lc 30,1); textFaint auf background (2,59 : 1 / Lc 47,9); background → surfaceDeep (1,05 : 1 / Lc –); surface → surfaceElevated (1,03 : 1 / Lc –); surface → surfaceWarm (1,05 : 1 / Lc –); surface → surfaceHover (1,09 : 1 / Lc –); Noten-Skala, engstes Paar (protan): Average–Good (6,3); Noten-Skala, engstes Paar (deutan): Average–Good (6,5); Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–Rot (4,8); Noten-Skala, engstes Paar (tritan): Good–Excellent (7,6); Liga-Akzente + Rot + Gold, engstes Paar (tritan): BL–SL (3,7)

## Option C · Flutlicht · v2 im Detail

### Dark

| Art | Paar | Vordergrund | Hintergrund | WCAG | APCA Lc | ΔL / ΔE | Ziel | Ergebnis |
|---|---|---|---|---|---|---|---|---|
| Text | textPrimary auf background | `#F4F0E6` | `#140F0E` | 16,71 | -97,7 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surface | `#F4F0E6` | `#241F1D` | 14,32 | -96,0 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceElevated | `#F4F0E6` | `#2F2A28` | 12,45 | -94,1 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceHover | `#F4F0E6` | `#2D2826` | 12,79 | -94,5 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceOverlay | `#F4F0E6` | `#3C3734` | 10,32 | -90,9 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textSecondary auf background | `#D5CEC4` | `#140F0E` | 12,18 | -76,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surface | `#D5CEC4` | `#241F1D` | 10,44 | -75,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceElevated | `#D5CEC4` | `#2F2A28` | 9,07 | -73,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceHover | `#D5CEC4` | `#2D2826` | 9,32 | -73,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceOverlay | `#D5CEC4` | `#3C3734` | 7,52 | -70,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf background | `#C8C2B7` | `#140F0E` | 10,74 | -69,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surface | `#C8C2B7` | `#241F1D` | 9,20 | -68,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceElevated | `#C8C2B7` | `#2F2A28` | 8,00 | -66,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceHover | `#C8C2B7` | `#2D2826` | 8,22 | -66,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceOverlay | `#C8C2B7` | `#3C3734` | 6,63 | -62,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textMuted auf background | `#AFA89E` | `#140F0E` | 8,07 | -55,2 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surface | `#AFA89E` | `#241F1D` | 6,92 | -53,5 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceElevated | `#AFA89E` | `#2F2A28` | 6,01 | -51,6 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceHover | `#AFA89E` | `#2D2826` | 6,18 | -52,0 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceOverlay | `#AFA89E` | `#3C3734` | 4,99 | -48,3 | – | ≥4,5 · Lc 45 | ✅ |
| Text | accentText auf background | `#FFA697` | `#140F0E` | 10,10 | -66,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surface | `#FFA697` | `#241F1D` | 8,65 | -64,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surfaceElevated | `#FFA697` | `#2F2A28` | 7,52 | -63,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf accentMuted | `#FFA697` | `#40100E` | 8,59 | -64,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf background | `#53FEEC` | `#140F0E` | 15,17 | -91,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf surface | `#53FEEC` | `#241F1D` | 13,00 | -89,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf positiveMuted | `#53FEEC` | `#0F3118` | 11,38 | -87,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingDown auf accentMuted | `#FFA697` | `#40100E` | 8,59 | -64,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf background | `#F1BE3D` | `#140F0E` | 11,02 | -71,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf surface | `#F1BE3D` | `#241F1D` | 9,45 | -69,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf goldMuted | `#F1BE3D` | `#3D2E0A` | 7,64 | -66,5 | – | ≥4,5 · Lc 60 | ✅ |
| Button-Text | onAccent auf accent | `#FCFCFC` | `#E32018` | 4,56 | -73,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingElite | `#140F0E` | `#85BAFF` | 9,48 | 64,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingExcellent | `#140F0E` | `#9EFFFE` | 16,47 | 95,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingGood | `#140F0E` | `#D6FC91` | 16,47 | 95,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingAverage | `#140F0E` | `#F8A052` | 9,18 | 63,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onRatingPoor auf ratingPoor | `#140F0E` | `#FFBFB6` | 12,11 | 77,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueBL | `#140F0E` | `#9CACFF` | 8,84 | 61,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leaguePL | `#140F0E` | `#9DFFB2` | 15,74 | 92,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueSL | `#140F0E` | `#DECEFF` | 13,02 | 81,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onMkRed auf mkRed | `#F5F1E9` | `#D71712` | 4,64 | -70,0 | – | ≥4,5 · Lc 60 | ✅ |
| Schlagzeile | onMkRedLarge auf mkRed | `#F4F0E6` | `#D71712` | 4,59 | -69,3 | – | ≥3,0 · Lc 45 | ✅ |
| Text | mkPaper auf mkInk | `#F3EEE3` | `#140F0E` | 16,43 | -96,5 | – | ≥4,5 · Lc 75 | ✅ |
| Nicht-Text | mkRed auf mkInk | `#D71712` | `#140F0E` | 3,64 | -27,7 | – | ≥3,0 · Lc 30 | ❌ |
| Text | accentText auf mkInk | `#FFA697` | `#140F0E` | 10,10 | -66,5 | – | ≥4,5 · Lc 60 | ✅ |
| Nicht-Text | borderStrong auf surface | `#898381` | `#241F1D` | 4,37 | -34,6 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf background | `#F4F0E6` | `#140F0E` | 16,71 | -97,7 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf surface | `#F4F0E6` | `#241F1D` | 14,32 | -96,0 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | textFaint auf background | `#827C73` | `#140F0E` | 4,60 | -32,8 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf background | `#E32018` | `#140F0E` | 4,06 | -30,9 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf surface | `#E32018` | `#241F1D` | 3,48 | -29,2 | – | ≥3,0 · Lc 30 | ❌ |
| Stufe | background → surfaceDeep | `#1C1715` | `#140F0E` | 1,07 | – | 3,5 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceDeep → surface | `#241F1D` | `#1C1715` | 1,09 | – | 3,4 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceElevated | `#2F2A28` | `#241F1D` | 1,15 | – | 4,5 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceElevated → surfaceOverlay | `#3C3734` | `#2F2A28` | 1,21 | – | 5,1 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceSunken → background | `#140F0E` | `#0C0807` | 1,05 | – | 3,5 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceWarm | `#362422` | `#241F1D` | 1,11 | – | 3,7 | ΔL ≥3 | ✅ sichtbar |
| Stufe | tabTrack → tabActive | `#3C3734` | `#1C1715` | 1,51 | – | 13,1 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceHover | `#2D2826` | `#241F1D` | 1,12 | – | 3,7 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceHover → surfacePressed | `#37322F` | `#2D2826` | 1,15 | – | 4,0 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceSelected | `#46221F` | `#241F1D` | 1,17 | – | 5,6 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceDisabled | `#1A1615` | `#241F1D` | 1,10 | – | 4,0 | ΔL ≥3 | ✅ sichtbar |
| Farbschwäche | Auf ↔ Ab (normal) | `#53FEEC` | `#FFA697` | – | – | 26,1 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (normal): Poor–Average | – | – | – | – | 11,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (normal): BL–SL | – | – | – | – | 13,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (protan) | `#F2F0EB` | `#BAB296` | – | – | 19,5 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (protan): Poor–Elite | – | – | – | – | 12,6 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (protan): BL–SL | – | – | – | – | 11,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (deutan) | `#D9DEEE` | `#CFC496` | – | – | 11,9 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (deutan): Poor–Excellent | – | – | – | – | 10,0 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–Gold | – | – | – | – | 12,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (tritan) | `#00FFF8` | `#FF9AA2` | – | – | 29,8 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (tritan): Poor–Average | – | – | – | – | 9,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (tritan): SL–Gold | – | – | – | – | 11,0 | ΔE ≥10 | ✅ |
| OLED | background #140F0E (R20 G15 B14) | – | `#140F0E` | – | – | – | kein Kanal unter 12 | ✅ |

### Light

| Art | Paar | Vordergrund | Hintergrund | WCAG | APCA Lc | ΔL / ΔE | Ziel | Ergebnis |
|---|---|---|---|---|---|---|---|---|
| Text | textPrimary auf background | `#19120F` | `#E3DDD2` | 13,69 | 85,5 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surface | `#19120F` | `#F7F4ED` | 16,85 | 98,6 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceElevated | `#19120F` | `#FFFFFF` | 18,51 | 105,1 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceHover | `#19120F` | `#EDE8DD` | 15,15 | 91,7 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textPrimary auf surfaceOverlay | `#19120F` | `#EEE9DE` | 15,29 | 92,3 | – | ≥4,5 · Lc 75 | ✅ |
| Text | textSecondary auf background | `#473F3C` | `#E3DDD2` | 7,60 | 74,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surface | `#473F3C` | `#F7F4ED` | 9,35 | 87,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceElevated | `#473F3C` | `#FFFFFF` | 10,27 | 93,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceHover | `#473F3C` | `#EDE8DD` | 8,41 | 80,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textSecondary auf surfaceOverlay | `#473F3C` | `#EEE9DE` | 8,49 | 81,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf background | `#544C49` | `#E3DDD2` | 6,20 | 69,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surface | `#544C49` | `#F7F4ED` | 7,63 | 82,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceElevated | `#544C49` | `#FFFFFF` | 8,38 | 88,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceHover | `#544C49` | `#EDE8DD` | 6,86 | 75,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textTertiary auf surfaceOverlay | `#544C49` | `#EEE9DE` | 6,92 | 76,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | textMuted auf background | `#605754` | `#E3DDD2` | 5,20 | 64,7 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surface | `#605754` | `#F7F4ED` | 6,40 | 77,9 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceElevated | `#605754` | `#FFFFFF` | 7,03 | 84,4 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceHover | `#605754` | `#EDE8DD` | 5,75 | 70,9 | – | ≥4,5 · Lc 45 | ✅ |
| Text | textMuted auf surfaceOverlay | `#605754` | `#EEE9DE` | 5,80 | 71,5 | – | ≥4,5 · Lc 45 | ✅ |
| Text | accentText auf background | `#BC0002` | `#E3DDD2` | 4,95 | 60,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surface | `#BC0002` | `#F7F4ED` | 6,09 | 73,7 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf surfaceElevated | `#BC0002` | `#FFFFFF` | 6,69 | 80,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | accentText auf accentMuted | `#BC0002` | `#FFDDD9` | 5,29 | 64,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf background | `#005860` | `#E3DDD2` | 6,06 | 68,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf surface | `#005860` | `#F7F4ED` | 7,45 | 81,3 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingUp auf positiveMuted | `#005860` | `#CBECF2` | 6,56 | 73,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingDown auf accentMuted | `#BC0002` | `#FFDDD9` | 5,29 | 64,6 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf background | `#845500` | `#E3DDD2` | 4,74 | 61,9 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf surface | `#845500` | `#F7F4ED` | 5,83 | 75,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | goldText auf goldMuted | `#845500` | `#F7E5B9` | 5,14 | 66,9 | – | ≥4,5 · Lc 60 | ✅ |
| Button-Text | onAccent auf accent | `#FCFCFC` | `#E11D16` | 4,66 | -74,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingElite | `#100B09` | `#85BAFF` | 9,75 | 64,8 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingExcellent | `#100B09` | `#9EFFFE` | 16,94 | 96,1 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingGood | `#100B09` | `#D6FC91` | 16,94 | 96,0 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf ratingAverage | `#100B09` | `#F8A052` | 9,44 | 63,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | onRatingPoor auf ratingPoor | `#100B09` | `#FFBFB6` | 12,46 | 77,5 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueBL | `#100B09` | `#9CACFF` | 9,09 | 61,4 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leaguePL | `#100B09` | `#9DFFB2` | 16,19 | 93,2 | – | ≥4,5 · Lc 60 | ✅ |
| Text | ratingInk auf leagueSL | `#100B09` | `#DECEFF` | 13,39 | 81,5 | – | ≥4,5 · Lc 60 | ✅ |
| Nicht-Text | borderStrong auf surface | `#7A7468` | `#F7F4ED` | 4,22 | 65,8 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf background | `#19120F` | `#E3DDD2` | 13,69 | 85,5 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | focusRing auf surface | `#19120F` | `#F7F4ED` | 16,85 | 98,6 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | textFaint auf background | `#807975` | `#E3DDD2` | 3,17 | 50,0 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf background | `#E11D16` | `#E3DDD2` | 3,54 | 51,3 | – | ≥3,0 · Lc 30 | ✅ |
| Nicht-Text | accent auf surface | `#E11D16` | `#F7F4ED` | 4,36 | 64,5 | – | ≥3,0 · Lc 30 | ✅ |
| Stufe | background → surfaceDeep | `#EDE9E0` | `#E3DDD2` | 1,12 | – | 3,5 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceDeep → surface | `#F7F4ED` | `#EDE9E0` | 1,10 | – | 3,3 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceElevated | `#FFFFFF` | `#F7F4ED` | 1,10 | – | 3,2 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceElevated → surfaceOverlay | `#EEE9DE` | `#FFFFFF` | 1,21 | – | 6,5 | ΔL ≥3 | ✅ deutlich |
| Stufe | surfaceSunken → background | `#E3DDD2` | `#D7D2C7` | 1,12 | – | 3,5 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceWarm | `#F8E3DB` | `#F7F4ED` | 1,12 | – | 3,7 | ΔL ≥3 | ✅ sichtbar |
| Stufe | tabTrack → tabActive | `#FFFFFF` | `#EBE6DB` | 1,24 | – | 7,4 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceHover | `#EDE8DD` | `#F7F4ED` | 1,11 | – | 3,6 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surfaceHover → surfacePressed | `#E1DBD0` | `#EDE8DD` | 1,13 | – | 3,9 | ΔL ≥3 | ✅ sichtbar |
| Stufe | surface → surfaceSelected | `#FFDDD9` | `#F7F4ED` | 1,15 | – | 4,3 | ΔL ≥3 | ✅ deutlich |
| Stufe | surface → surfaceDisabled | `#EAE7E2` | `#F7F4ED` | 1,12 | – | 3,9 | ΔL ≥3 | ✅ sichtbar |
| Farbschwäche | Auf ↔ Ab (normal) | `#005860` | `#BC0002` | – | – | 28,8 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (normal): Poor–Average | – | – | – | – | 11,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (normal): BL–SL | – | – | – | – | 13,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (protan) | `#4F5461` | `#4E4400` | – | – | 11,9 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (protan): Poor–Elite | – | – | – | – | 12,6 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (protan): BL–SL | – | – | – | – | 11,3 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (deutan) | `#444B60` | `#776900` | – | – | 17,7 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (deutan): Poor–Excellent | – | – | – | – | 10,0 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–SL | – | – | – | – | 13,0 | ΔE ≥10 | ✅ |
| Farbschwäche | Auf ↔ Ab (tritan) | `#005C5A` | `#D00008` | – | – | 31,2 | ΔE ≥10 | ✅ |
| Farbschwäche | Noten-Skala, engstes Paar (tritan): Poor–Average | – | – | – | – | 9,8 | ΔE ≥8 | ✅ |
| Farbschwäche | Liga-Akzente + Rot + Gold, engstes Paar (tritan): PL–SL | – | – | – | – | 12,1 | ΔE ≥10 | ✅ |

### v1 (zum Vergleich): durchgefallen

- **dark** (31): textTertiary auf background (8,63 : 1 / Lc -57,2); textTertiary auf surface (7,89 : 1 / Lc -56,4); textTertiary auf surfaceElevated (7,07 : 1 / Lc -55,1); textTertiary auf surfaceHover (7,30 : 1 / Lc -55,5); textTertiary auf surfaceOverlay (6,03 : 1 / Lc -52,8); accentText auf background (7,30 : 1 / Lc -50,3); accentText auf surface (6,68 : 1 / Lc -49,5); accentText auf surfaceElevated (5,98 : 1 / Lc -48,2); accentText auf accentMuted (5,29 : 1 / Lc -46,0); ratingDown auf accentMuted (5,29 : 1 / Lc -46,0); onAccent auf accent (5,54 : 1 / Lc 42,6); ratingInk auf ratingElite (6,77 : 1 / Lc 48,9); onRatingPoor auf ratingPoor (5,74 : 1 / Lc 43,2); ratingInk auf leagueBL (6,20 : 1 / Lc 45,4); onMkRed auf mkRed (5,54 : 1 / Lc 42,6); onMkRedLarge auf mkRed (5,54 : 1 / Lc 42,6); accentText auf mkInk (7,30 : 1 / Lc -50,3); borderStrong auf surface (2,98 : 1 / Lc -20,7); textFaint auf background (3,54 : 1 / Lc -23,9); background → surfaceDeep (1,04 : 1 / Lc –); surfaceDeep → surface (1,05 : 1 / Lc –); surfaceSunken → background (1,03 : 1 / Lc –); surface → surfaceWarm (1,02 : 1 / Lc –); surface → surfaceDisabled (1,05 : 1 / Lc –); Noten-Skala, engstes Paar (protan): Average–Good (3,5); Liga-Akzente + Rot + Gold, engstes Paar (protan): PL–Gold (5,0); Auf ↔ Ab (deutan) (9,1); Noten-Skala, engstes Paar (deutan): Average–Good (2,1); Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–Gold (3,4); Noten-Skala, engstes Paar (tritan): Excellent–Elite (7,9); background #100B09 (R16 G11 B9) (–)
- **light** (23): textMuted auf surfaceOverlay (4,31 : 1 / Lc 58,6); ratingUp auf background (4,39 : 1 / Lc 64,1); ratingUp auf positiveMuted (4,15 : 1 / Lc 60,5); goldText auf background (4,02 : 1 / Lc 61,6); goldText auf surface (4,36 : 1 / Lc 66,8); goldText auf goldMuted (3,86 : 1 / Lc 58,9); onAccent auf accent (4,42 : 1 / Lc 35,4); ratingInk auf ratingElite (6,77 : 1 / Lc 48,9); onRatingPoor auf ratingPoor (5,74 : 1 / Lc 43,2); ratingInk auf leagueBL (3,45 : 1 / Lc 25,9); ratingInk auf leaguePL (4,44 : 1 / Lc 33,5); ratingInk auf leagueSL (4,04 : 1 / Lc 30,8); textFaint auf background (2,75 : 1 / Lc 48,6); background → surfaceDeep (1,05 : 1 / Lc –); surface → surfaceElevated (1,07 : 1 / Lc –); surface → surfaceWarm (1,06 : 1 / Lc –); surface → surfaceHover (1,08 : 1 / Lc –); Noten-Skala, engstes Paar (protan): Average–Good (3,5); Auf ↔ Ab (deutan) (4,5); Noten-Skala, engstes Paar (deutan): Average–Good (2,1); Liga-Akzente + Rot + Gold, engstes Paar (deutan): PL–Rot (6,3); Noten-Skala, engstes Paar (tritan): Excellent–Elite (7,9); Liga-Akzente + Rot + Gold, engstes Paar (tritan): BL–SL (3,7)

