"""Baut den Übergabe-Ordner für den Website-Builder: marke/designsystem/uebergabe-website/.
Quelle ist Option A (Burhans Wahl vom 05.11.2026). Aufruf im Ordner _werkzeug: python -I uebergabe.py
"""
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.stdout.reconfigure(encoding="utf-8")
import optionen as O
from bauen import palette, ZWECK
from farbe import wcag

DS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUELLE = os.path.join(DS, O.ORDNER["A"])
ZIEL = os.path.join(DS, "uebergabe-website")

GRUPPEN = [
    ("Flächen", ["background", "surfaceSunken", "surfaceDeep", "surface", "surfaceElevated", "surfaceOverlay", "surfaceWarm",
                 "surfaceHover", "surfacePressed", "surfaceSelected", "surfaceDisabled", "tabTrack", "tabActive"]),
    ("Linien", ["borderSubtle", "border", "borderStrong", "focusRing"]),
    ("Text", ["textPrimary", "textSecondary", "textTertiary", "textMuted", "textFaint", "textDisabled"]),
    ("Rot und Gold", ["accent", "accentText", "accentDim", "accentMuted", "onAccent", "gold", "goldText", "goldMuted"]),
    ("Auf und Ab", ["ratingUp", "positiveMuted", "ratingDown"]),
    ("Noten (wie heute in der App, Poor = Sofascore-Rot)", ["ratingElite", "ratingExcellent", "ratingGood", "ratingAverage", "ratingPoor", "ratingInk", "onRatingPoor"]),
    ("Spielfeld", ["pitchGreen", "pitchLine"]),
    ("Marketing (nur Social, nicht für die Website-Oberfläche)", ["mkRed", "mkRedDeep", "mkInk", "mkPaper", "onMkRed", "onMkRedLarge"]),
    ("Liga-Akzente (nur Flächen mit Kürzel BL/PL/SL)", ["leagueBL", "leaguePL", "leagueSL"]),
]


def tabelle(p):
    z = []
    for titel, rollen in GRUPPEN:
        z.append(f"\n### {titel}\n\n| Token | Dark | Light | Wofür |\n|---|---|---|---|")
        for k in rollen:
            z.append(f"| `--{k}` | `{p['dark'][k]}` | `{p['light'][k]}` | {ZWECK.get(k, '').replace('NEU: ', '')} |")
    return "\n".join(z)


def text(p):
    d = p["dark"]
    s = O.SCHRIFT["A"]
    groessen = "\n".join(f"| `{n}` | {sz} px | {lh} px | {w} | {rolle} |" for n, sz, lh, w, rolle in O.GROESSEN["A"])
    abst = " · ".join(f"`--{n}` {v} px" for n, v in O.ABSTAND)
    rad = "\n".join(f"| `--{n}` | {v} px | {zw} |" for n, v, zw in O.RADIUS["A"])
    kw = lambda a, b: f"{wcag(d[a], d[b]):.1f} : 1".replace(".", ",")
    return f"""# Übergabe Website · Designsystem FootPulse 2026

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
| Überschriften, Zahlen, Buttons | {s['display']['family']} | {', '.join(map(str, s['display']['weights']))} |
| Fließtext | {s['text']['family']} | {', '.join(map(str, s['text']['weights']))} |
| Labels (Großbuchstaben, Abstand 0,06 em) | {s['label']['family']} | {', '.join(map(str, s['label']['weights']))} |

- Beide Schriften sind frei (SIL Open Font License), über Google Fonts:
  `https://fonts.googleapis.com/css2?{s['google']}&display=swap`
- Zahlen immer mit `font-variant-numeric: tabular-nums`, damit sie in Tabellen nicht springen.
- Türkische Texte brauchen `lang="tr"`, sonst wird aus „i“ in Großbuchstaben ein „I“ statt „İ“.

### Größen (Web)

| Name | Größe | Zeilenhöhe | Gewicht | Schrift |
|---|---|---|---|---|
{groessen}

## Farben
{tabelle(p)}

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

Jeder Text erfüllt WCAG AA (mindestens 4,5 : 1). Haupttext auf Hintergrund {kw('textPrimary', 'background')}, Nebentext {kw('textSecondary', 'surface')}, weiße Schrift auf rotem Button {kw('onAccent', 'accent')}, weiße Zahl auf Poor {kw('onRatingPoor', 'ratingPoor')}.
Bewusste Ausnahmen nach dem strengeren APCA-Test, von Burhan so gewählt: Website-Rot als Schrift (Lc 44) und die heutige Noten-Skala (dunkle Zahl auf Elite Lc 40; bei Rot-Grün-Schwäche liegen Good und Average dicht beieinander). Deshalb: rote Schrift nur kurz und halbfett, Noten nie ohne Zahl. Alle Messwerte: `marke/designsystem/testmatrix.md` im Marketing-Repo.

## Abstände, Radien, Formen

- Abstände: {abst}
- Linien: {O.LINIE['A']}

| Token | Wert | Wofür |
|---|---|---|
{rad}

**Die Form von A:** Karten haben oben rechts eine angeschnittene Ecke (`clip-path`, Größe `--cut-md`), darauf eine 2 px rote Linie. Buttons und Chips sind fast eckig (2–4 px). Keine Pillen, keine weichen Schatten.

```css
.card {{
  background: var(--surface);
  border: 1px solid var(--border);
  clip-path: polygon(0 0, calc(100% - var(--cut-md)) 0, 100% var(--cut-md), 100% 100%, 0 100%);
}}
```

## Bausteine (siehe `testseiten.html`)

| Baustein | Fläche | Schrift | Zustände |
|---|---|---|---|
| Button primär | `--accent`, Ecke oben rechts angeschnitten (`--cut-sm`) | `--onAccent`, {s['display']['family']} 800, Großbuchstaben, 17 px | Fokus 2 px `--focusRing` mit 2 px Abstand, deaktiviert `--surfaceDisabled` + `--textDisabled`. Hover-Vorschlag: `--accentDim` |
| Tabs | Spur `--tabTrack`, aktiv `--tabActive` + 3 px rote Unterkante (`--accent`) | {s['display']['family']} 700, Großbuchstaben; aktiv `--textPrimary`, sonst `--textSecondary` | Hover `--surfaceHover`, gedrückt `--surfacePressed`, ausgewählt `--surfaceSelected`, Fokus `--focusRing`, deaktiviert `--surfaceDisabled` |
| Aufwertungs-Chip | `--positiveMuted` | `--ratingUp`, „▲ +4“ | – |
| Abwertungs-Chip | `--accentMuted` | `--ratingDown`, „▼ −2“ | – |
| Noten-Chip | `--rating…` je Stufe (≥ 9 Elite, ≥ 8 Excellent, ≥ 7 Good, ≥ 6 Average, darunter Poor) | `--ratingInk`, bei Poor `--onRatingPoor` | – |
| MVP | `--goldMuted` oder Rand `--gold` | `--goldText` | – |
| Tabelle | Zeilen `--surface`, Trenner `--borderSubtle`, Auswahl `--surfaceSelected` | Zahlen rechtsbündig, tabular | Hover `--surfaceHover` |
| Eingabefeld | `--surfaceSunken`, Rand `--borderStrong`, 48 px hoch | `--textPrimary`, Platzhalter `--textMuted` | Fokus `--focusRing`, Fehler: Rand und Fehlertext `--accentText` |

## Bewegung

{O.BEWEGUNG['A']} Bei `prefers-reduced-motion: reduce` keine Bewegung, nur Einblenden.

## Was nicht geht

- Keine Kartenpacks, kein Metallic, keine Seltenheitsstufen (kein Videospiel-Look).
- Kein „Live“-Wording, kein Neongrün (kein Wettanbieter-Look).
- Keine Vereinswappen, keine echten Liga-Logos und keine Spielerfotos ohne Rechte.
- Das Logo auf Rot nur einfarbig weiß.

## Fragen

Alles, was hier nicht steht, entscheidet Burhan. Der Marketing-Chat (Repo FootPulse-Marketing, `marke/designsystem/`) kann Werte nachrechnen oder Bausteine ergänzen.
"""


def main():
    if os.path.isdir(ZIEL):
        shutil.rmtree(ZIEL)
    os.makedirs(ZIEL)
    for f in ("tokens.css", "tokens.json", "alt-neu.md", "testseiten.html", "beispiele.html", "logo-regeln.html"):
        shutil.copy(os.path.join(QUELLE, f), os.path.join(ZIEL, f))
    shutil.copytree(os.path.join(QUELLE, "logo"), os.path.join(ZIEL, "logo"))
    with open(os.path.join(ZIEL, "LIESMICH.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text(palette("A")))
    print("ok", ZIEL)


if __name__ == "__main__":
    main()
