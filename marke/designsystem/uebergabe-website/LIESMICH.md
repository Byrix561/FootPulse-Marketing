# Übergabe Website · Designsystem FootPulse 2026

Für: den Builder der Website footpulse.org · Stand: 05.11.2026 · Freigegeben von: Burhan (Option A „Anzeigetafel“)

Dieser Ordner enthält alles, was du für den neuen Look der Website brauchst: Farben, Schrift, Größen, Abstände, Formen, Bausteine und Logos.

## Das Wichtigste zuerst

1. **Bestehende Funktionen bleiben, wie sie sind.** Das gilt besonders für das **Team der Woche (TOTW)**: Aufbau, Karten, Reihenfolge und Inhalte bleiben genau wie heute. Übernommen werden dort nur die **Farben** (Noten-Chips, Rot, Gold).
2. **Der Aufbau der Seiten ist nicht Teil dieser Übergabe.** Burhan ändert ihn später. Die Beispielseiten in diesem Ordner zeigen den **Stil** (Farbe, Schrift, Karten, Symbole), nicht den fertigen Seitenaufbau.
3. **Logo:** Vorerst bleibt das **heutige Logo** auf der Website (`logo-heute/`). Das neue A-Logo liegt als Vorschlag bei (`logo/`). Es wird erst nach einem eigenen Logo-Termin eingesetzt.
4. **Farben nur über Tokens.** Keine Hex-Werte direkt im Code. Alle Werte stehen in `tokens.css` (CSS-Variablen) und `tokens.json`. Die Namen sind dieselben wie in der App-Token-Datei.

## Dateien

| Datei | Was |
|---|---|
| `tokens.css` | Alle Farben für Dark (`:root`, `[data-theme="dark"]`) und Light (`[data-theme="light"]`), dazu Schriften, Abstände, Radien |
| `tokens.json` | Dieselben Werte als JSON, auch Schriftgrößen und Social-Größen |
| `alt-neu.md` | Tabelle: heutiger App-Wert → neuer Wert je Token |
| `testseiten.html` | Alle Bausteine: Spielerkarte, Tabs mit allen Zuständen, Tabelle, Chips, Warteliste, Profilraster. Light mit `?theme=light` |
| `beispiele.html` | Beispiele im Stil: App-Screens, Website-Startseite, Posts. **Nur Stil, kein fertiger Aufbau** |
| `logo-regeln.html` | Logo-Varianten, Schutzzone, Mindestgrößen, Do's und Don'ts (für das A-Logo) |
| `logo/` | A-Logo als SVG (Vorschlag, noch nicht live) |
| `logo-heute/` | Das heutige Logo (bleibt vorerst auf der Website), als PNG und SVG. Nur im OneDrive-Ordner und im Zip |
| `vorschau/` | Screenshots der Seiten, falls du die HTML-Dateien nicht öffnen willst. Nur im OneDrive-Ordner und im Zip |

Die HTML-Dateien funktionieren nur, wenn sie neben `tokens.css` und `logo/` liegen. Lass die Ordnerstruktur also, wie sie ist.

## Schrift

| Rolle | Schrift | Gewichte |
|---|---|---|
| Überschriften, Zahlen, Buttons | Barlow Condensed | 700, 800 |
| Fließtext | Barlow | 400, 500, 600 |
| Labels (Großbuchstaben, Abstand 0,06 em) | Barlow Condensed | 600 |

- Beide Schriften sind frei (SIL Open Font License), über Google Fonts:
  `https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800&family=Barlow:wght@400;500;600&display=swap`
- Zahlen immer mit `font-variant-numeric: tabular-nums`, damit sie in Tabellen nicht springen.
- Türkische Texte brauchen `lang="tr"`, sonst wird aus „i“ in Großbuchstaben ein „I“ statt „İ“.

### Größen (Web)

| Name | Größe | Zeilenhöhe | Gewicht | Schrift |
|---|---|---|---|---|
| `display` | 68 px | 64 px | 800 | display |
| `h1` | 44 px | 44 px | 800 | display |
| `h2` | 32 px | 34 px | 700 | display |
| `h3` | 24 px | 28 px | 700 | display |
| `title` | 20 px | 24 px | 600 | text |
| `body` | 16 px | 24 px | 400 | text |
| `small` | 14 px | 20 px | 500 | text |
| `label` | 13 px | 16 px | 600 | label |
| `caption` | 12 px | 16 px | 500 | text |
| `micro` | 10 px | 12 px | 600 | label |
| `ovr` | 56 px | 52 px | 800 | zahl |
| `stat` | 18 px | 20 px | 700 | zahl |

## Farben

### Flächen

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--background` | `#0D0F14` | `#DBDEE3` | Seitenhintergrund |
| `--surfaceSunken` | `#06080C` | `#D0D3D8` | Vertiefte Flächen (Eingabefeld, Mulde) |
| `--surfaceDeep` | `#15171C` | `#E7E9EE` | Zwischenebene (Leisten, Tab-Spur) |
| `--surface` | `#1D1F24` | `#F2F4F7` | Karten, Listen |
| `--surfaceElevated` | `#272A30` | `#FFFFFF` | Gehobene Karten, Kopfzeilen |
| `--surfaceOverlay` | `#34373D` | `#E7E9EF` | Menüs, Popover, Tooltips |
| `--surfaceWarm` | `#352222` | `#F9E1E1` | Hervorgehobene Karte mit Rot-Stich |
| `--surfaceHover` | `#26282D` | `#E6E8EE` | Hover auf Fläche |
| `--surfacePressed` | `#2F3237` | `#D9DCE1` | Gedrückt / aktiv |
| `--surfaceSelected` | `#44211F` | `#FFDDDA` | Ausgewählte Zeile oder Karte |
| `--surfaceDisabled` | `#14161A` | `#E6E8EB` | Deaktivierte Fläche |
| `--tabTrack` | `#15171C` | `#E3E6EC` | Spur der Tab-Leiste |
| `--tabActive` | `#34373D` | `#FFFFFF` | Fläche des aktiven Tabs |

### Linien

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--borderSubtle` | `#2E3036` | `#CED1D6` | Trenner in Listen |
| `--border` | `#404248` | `#BBBEC3` | Karten-Rand |
| `--borderStrong` | `#808389` | `#72747A` | Rand von Bedienelementen (3 : 1) |
| `--focusRing` | `#E4E8EF` | `#111419` | Fokusrahmen 2 px, 2 px Abstand |

### Text

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--textPrimary` | `#F2F3F6` | `#111419` | Haupttext, Zahlen |
| `--textSecondary` | `#CDCFD5` | `#3E4148` | Nebentext |
| `--textTertiary` | `#C0C2C8` | `#4B4E55` | Beschriftungen |
| `--textMuted` | `#A7A9AE` | `#565960` | Hinweise, ab 14 px halbfett |
| `--textFaint` | `#7B7D82` | `#777A80` | Nur Nicht-Text: Pfeile, Trenner, Icons |
| `--textDisabled` | `#6D6F71` | `#7E8084` | Deaktivierter Text (keine Kontrastpflicht) |

### Rot und Gold

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--accent` | `#E31D29` | `#DB1B26` | Rote Flächen, Buttons, Linien ≥ 2 px |
| `--accentText` | `#FF5260` | `#BB081A` | Rote Schrift, kleine rote Punkte |
| `--accentDim` | `#A32224` | `#ED8B87` | Gedrücktes Rot, rote Linie auf Rot |
| `--accentMuted` | `#401011` | `#FFDDDA` | Hintergrund roter Chips |
| `--onAccent` | `#FCFCFC` | `#FCFCFC` | Schrift auf Rot |
| `--gold` | `#F2BF47` | `#EAB532` | Nur verdiente Auszeichnung (MVP, Rang 1) |
| `--goldText` | `#F2BF47` | `#845500` | Gold als Schrift (im Hell-Modus dunkler) |
| `--goldMuted` | `#392C0C` | `#F7E5B9` | Hintergrund Gold-Chip |

### Auf und Ab

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--ratingUp` | `#5EF9F1` | `#005763` | Aufwertung (immer mit ▲ und +) |
| `--positiveMuted` | `#002F2D` | `#CBECF2` | Hintergrund Aufwertungs-Chip |
| `--ratingDown` | `#FF5260` | `#BB081A` | Abwertung (immer mit ▼ und −) |

### Noten (wie heute in der App, Poor = Sofascore-Rot)

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--ratingElite` | `#3B82F6` | `#3B82F6` | Note Elite (Fläche, Zahl in ratingInk) |
| `--ratingExcellent` | `#18B981` | `#18B981` | Note Excellent |
| `--ratingGood` | `#8BC34A` | `#8BC34A` | Note Good |
| `--ratingAverage` | `#F2B84B` | `#F2B84B` | Note Average |
| `--ratingPoor` | `#DC0C00` | `#DC0C00` | Note Poor |
| `--ratingInk` | `#0D0F14` | `#0C0E13` | Zahl auf Noten- und Liga-Flächen |
| `--onRatingPoor` | `#FCFCFC` | `#FCFCFC` | Zahl auf der Note Poor (A: weiß auf Rot) |

### Spielfeld

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--pitchGreen` | `#0F2D1F` | `#BDE2CB` | Spielfeld-Fläche (TOTW) |
| `--pitchLine` | `#2D5742` | `#85B99A` | Spielfeld-Linien |

### Marketing (nur Social, nicht für die Website-Oberfläche)

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--mkRed` | `#E31D29` | `#E31D29` | Marketing: rote Vollfläche |
| `--mkRedDeep` | `#8A0410` | `#8A0410` | Marketing: zweites Rot für Tiefe, Streifen |
| `--mkInk` | `#0D0F14` | `#0D0F14` | Marketing: Schwarz |
| `--mkPaper` | `#F4F5F8` | `#F4F5F8` | Marketing: Weiß / Kreide |
| `--onMkRed` | `#FCFCFC` | `#FCFCFC` | Marketing: kleine Schrift auf Rot |
| `--onMkRedLarge` | `#FCFCFC` | `#FCFCFC` | Marketing: Schlagzeile auf Rot |

### Liga-Akzente (nur Flächen mit Kürzel BL/PL/SL)

| Token | Dark | Light | Wofür |
|---|---|---|---|
| `--leagueBL` | `#9CACFF` | `#9CACFF` | Akzent Bundesliga-Konto (Fläche) |
| `--leaguePL` | `#9DFFB2` | `#9DFFB2` | Akzent Premier-League-Konto (Fläche) |
| `--leagueSL` | `#DECEFF` | `#DECEFF` | Akzent Süper-Lig-Konto (Fläche) |

### Regeln für Farbe

- **Dark ist Standard.** Light gibt es als zweiten Modus mit denselben Token-Namen.
- **Rot heißt Zustand oder Aktion:** Buttons, aktiver Tab, Fehler, Abwertung. Rote Flächen mindestens 8 px, Linien mindestens 2 px.
- **Rote Schrift** (`--accentText`, im Dark-Modus das heutige Website-Rot #FF5260) nur halbfett ab 14 px und für kurze Wörter, nie für Fließtext.
- **Zwei Rottöne mit Absicht:** Abwertung = Website-Rot `--ratingDown`. Schlechte Note = Sofascore-Rot `--ratingPoor` mit weißer Zahl (`--onRatingPoor`). Diese zwei nicht vertauschen.
- **Noten-Chips** nutzen die Farben wie heute in der App. Die Zahl steht immer im Chip, dunkel (`--ratingInk`), nur bei Poor weiß.
- **Auf und Ab nie nur über Farbe:** immer ▲ mit +, ▼ mit −, ■ für unverändert.
- **Gold nur für Verdientes:** MVP im Team der Woche, Rang 1.
- **Keine Verläufe, kein Blur, kein Neon.** Flächen heben sich nur über die Flächenstufen ab.
- Liga-Farben (BL, PL, SL) sind nur für Social-Konten, nicht für die Website-Oberfläche.

### Gemessen (Dark)

Jeder Text erfüllt WCAG AA (mindestens 4,5 : 1). Haupttext auf Hintergrund 17,3 : 1, Nebentext 10,6 : 1, weiße Schrift auf rotem Button 4,6 : 1, weiße Zahl auf Poor 5,0 : 1.
Bewusste Ausnahmen nach dem strengeren APCA-Test, von Burhan so gewählt: Website-Rot als Schrift (Lc 44) und die heutige Noten-Skala (dunkle Zahl auf Elite Lc 40; bei Rot-Grün-Schwäche liegen Good und Average dicht beieinander). Deshalb: rote Schrift nur kurz und halbfett, Noten nie ohne Zahl. Alle Messwerte: `marke/designsystem/testmatrix.md` im Marketing-Repo.

## Abstände, Radien, Formen

- Abstände: `--space-1` 4 px · `--space-2` 8 px · `--space-3` 12 px · `--space-4` 16 px · `--space-5` 20 px · `--space-6` 24 px · `--space-8` 32 px · `--space-10` 40 px · `--space-12` 48 px · `--space-16` 64 px
- Linien: 1 px Linien, 2 px für aktiv. Akzentbalken 4 px.

| Token | Wert | Wofür |
|---|---|---|
| `--radius-xs` | 2 px | Chips, Tags |
| `--radius-sm` | 4 px | Buttons, Eingabefelder |
| `--radius-md` | 6 px | Karten, Tabellen |
| `--radius-lg` | 8 px | Dialoge |
| `--cut-sm` | 8 px | Angeschnittene Ecke klein (Buttons, Chips mit Aktion) |
| `--cut-md` | 14 px | Angeschnittene Ecke Spielerkarte |
| `--cut-lg` | 28 px | Angeschnittene Ecke Post-Rahmen |

**Die Form von A:** Karten haben oben rechts eine angeschnittene Ecke (`clip-path`, Größe `--cut-md`), darauf eine 2 px rote Linie. Buttons und Chips sind fast eckig (2–4 px). Keine Pillen, keine weichen Schatten.

```css
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  clip-path: polygon(0 0, calc(100% - var(--cut-md)) 0, 100% var(--cut-md), 100% 100%, 0 100%);
}
```

## Bausteine (siehe `testseiten.html`)

| Baustein | Fläche | Schrift | Zustände |
|---|---|---|---|
| Button primär | `--accent`, Ecke oben rechts angeschnitten (`--cut-sm`) | `--onAccent`, Barlow Condensed 800, Großbuchstaben, 17 px | Fokus 2 px `--focusRing` mit 2 px Abstand, deaktiviert `--surfaceDisabled` + `--textDisabled`. Hover-Vorschlag: `--accentDim` |
| Tabs | Spur `--tabTrack`, aktiv `--tabActive` + 3 px rote Unterkante (`--accent`) | Barlow Condensed 700, Großbuchstaben; aktiv `--textPrimary`, sonst `--textSecondary` | Hover `--surfaceHover`, gedrückt `--surfacePressed`, ausgewählt `--surfaceSelected`, Fokus `--focusRing`, deaktiviert `--surfaceDisabled` |
| Aufwertungs-Chip | `--positiveMuted` | `--ratingUp`, „▲ +4“ | – |
| Abwertungs-Chip | `--accentMuted` | `--ratingDown`, „▼ −2“ | – |
| Noten-Chip | `--rating…` je Stufe (≥ 9 Elite, ≥ 8 Excellent, ≥ 7 Good, ≥ 6 Average, darunter Poor) | `--ratingInk`, bei Poor `--onRatingPoor` | – |
| MVP | `--goldMuted` oder Rand `--gold` | `--goldText` | – |
| Tabelle | Zeilen `--surface`, Trenner `--borderSubtle`, Auswahl `--surfaceSelected` | Zahlen rechtsbündig, tabular | Hover `--surfaceHover` |
| Eingabefeld | `--surfaceSunken`, Rand `--borderStrong`, 48 px hoch | `--textPrimary`, Platzhalter `--textMuted` | Fokus `--focusRing`, Fehler: Rand und Fehlertext `--accentText` |

## Bewegung

Schnell und hart wie eine Einblendung: 160 ms ein (ease-out), 120 ms aus. Zahlen zählen hoch (400 ms). Wischen von links nach rechts. Bei `prefers-reduced-motion: reduce` keine Bewegung, nur Einblenden.

## Was nicht geht

- Keine Kartenpacks, kein Metallic, keine Seltenheitsstufen (kein Videospiel-Look).
- Kein „Live“-Wording, kein Neongrün (kein Wettanbieter-Look).
- Keine Vereinswappen, keine echten Liga-Logos und keine Spielerfotos ohne Rechte.
- Das Logo auf Rot nur einfarbig weiß.

## Fragen

Alles, was hier nicht steht, entscheidet Burhan. Der Marketing-Chat (Repo FootPulse-Marketing, `marke/designsystem/`) kann Werte nachrechnen oder Bausteine ergänzen.
