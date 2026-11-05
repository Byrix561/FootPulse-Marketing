# Testmatrix Bild

Stand 05.11.2026. Gemessen auf den Screenshots der Testseiten (Chrome, doppelte Pixeldichte). Die Bilder liegen in OneDrive unter `00 Marke/Designsystem 2026/Screenshots/Runde 2/`.

## 1. Flächenstufen im gerenderten Bild (ΔL, OKLab ×100)

Gemessen wird die Pixelfarbe in jeder Zelle der Flächenleiter, nicht der Token. Ziel: jeder Schritt ≥ 3.

### Option A · Anzeigetafel

| Schritt | Dark v1 | Dark v2 | Light v1 | Light v2 |
|---|---|---|---|---|
| background → surfaceDeep | **2,7** | 3,6 | **1,5** | 3,4 |
| surfaceDeep → surface | **2,3** | 3,5 | 4,6 | 3,3 |
| surface → surfaceElevated | 4,6 | 4,5 | **2,4** | 3,4 |
| surfaceElevated → surfaceOverlay | 4,9 | 5,2 | 11,0 | 6,6 |
| surfaceSunken → background | **2,5** | 3,5 | 3,0 | 3,4 |
| surface → surfaceHover | 3,7 | 3,8 | **2,5** | 3,5 |
| surfaceHover → surfacePressed | 3,8 | 3,9 | **2,5** | 3,8 |
| surface → surfaceSelected | 5,6 | 5,6 | 4,1 | 4,2 |

### Option B · Messgerät

| Schritt | Dark v1 | Dark v2 | Light v1 | Light v2 |
|---|---|---|---|---|
| background → surfaceDeep | **2,2** | 3,5 | **1,5** | 3,4 |
| surfaceDeep → surface | **2,2** | 3,4 | 4,1 | 3,3 |
| surface → surfaceElevated | 4,1 | 4,7 | **1,0** | 3,3 |
| surfaceElevated → surfaceOverlay | 4,4 | 4,8 | 9,4 | 6,6 |
| surfaceSunken → background | **2,3** | 3,6 | 3,0 | 3,4 |
| surface → surfaceHover | **2,9** | 4,0 | 3,0 | 3,6 |
| surfaceHover → surfacePressed | 3,6 | 3,6 | 3,0 | 3,8 |
| surface → surfaceSelected | 5,6 | 5,7 | 4,5 | 4,2 |

### Option C · Flutlicht

| Schritt | Dark v1 | Dark v2 | Light v1 | Light v2 |
|---|---|---|---|---|
| background → surfaceDeep | **2,5** | 3,5 | **1,5** | 3,5 |
| surfaceDeep → surface | **2,6** | 3,4 | 4,1 | 3,3 |
| surface → surfaceElevated | 4,4 | 4,5 | **2,2** | 3,2 |
| surfaceElevated → surfaceOverlay | 5,0 | 5,1 | 10,4 | 6,5 |
| surfaceSunken → background | **2,7** | 3,5 | 3,0 | 3,5 |
| surface → surfaceHover | 3,3 | 3,7 | **2,7** | 3,6 |
| surfaceHover → surfacePressed | 4,1 | 4,0 | 3,0 | 3,9 |
| surface → surfaceSelected | 6,3 | 5,6 | 4,7 | 4,3 |

Fett = unter 3. Die Pixelwerte stimmen bis auf Rundung mit den Tokens überein. Das zeigt, dass die Seite die Farben richtig ausspielt.

## 2. Wirkung im Feed (Näherung)

Der eigene Post steht zwischen zwei fremden Posts (Farbflächen wie Fotos). Gemessen werden der Farbabstand des Mittelwerts zum Feed und der Hell-Dunkel-Kontrast des eigenen Posts nach starker Unschärfe (Blinzeltest). Beides sind Näherungen für „stoppt der Daumen“, kein Ersatz für einen echten Post-Test.

| Option | Modus | ΔE zum Feed | Kontrast nach Unschärfe (0–1) |
|---|---|---|---|
| A Anzeigetafel | dark | 20,4 | 0,25 |
| A Anzeigetafel | light | 20,4 | 0,25 |
| B Messgerät | dark | 16,3 | 0,33 |
| B Messgerät | light | 16,3 | 0,33 |
| C Flutlicht | dark | 14,8 | 0,4 |
| C Flutlicht | light | 14,8 | 0,4 |

Der Feed-Post ist in allen Modi derselbe (Marketing-Farben gelten unabhängig vom App-Modus). Die Zeilen je Option sind deshalb fast gleich.

## 3. Farbschwäche auf dem Bild

Für Chips, Tabelle, Spielerkarte und Team der Woche gibt es je Option und Modus eine Tafel mit vier Ansichten (normal, Protanopie, Deuteranopie, Tritanopie), Dateien `R2_<Option>_<Modus>_v2_farbschwaeche_<Teil>.png`. Auswertung siehe Abschnitt 4 im Bericht.

