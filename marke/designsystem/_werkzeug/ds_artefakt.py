"""Erzeugt je Option das Paket für das Design-System-Artefakt (project/...): tokens.json, README.md, Bausteine, Deckblatt.
Aufruf: python -I ds_artefakt.py <Zielordner>   → <Ziel>/<Option>/project/...
"""
import io
import json
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import optionen as O
import seiten
from bauen import palette, ZWECK
from paletten import ALLE, ROLLEN_MARKETING, ROLLEN_LIGA

DS = os.path.dirname(HIER)


def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def tokens(r, p):
    s = O.SCHRIFT[r]
    col = []
    for k in ALLE:
        if k in ROLLEN_MARKETING + ROLLEN_LIGA:
            col.append({"name": k, "value": {"dark": p["dark"][k], "light": p["dark"][k]}, "usage": ZWECK[k] + " Gilt in beiden Modi."})
        else:
            col.append({"name": k, "value": {"dark": p["dark"][k], "light": p["light"][k]}, "usage": ZWECK[k]})
    fam = {k: s[k]["css"].replace("'", '"') for k in ("display", "text", "zahl", "label")}
    groups = {}
    for n, sz, lh, wt, ro in O.GROESSEN[r]:
        groups.setdefault(ro, []).append({"name": n, "fontSize": f"{sz}px", "lineHeight": f"{lh}px", "fontWeight": wt,
                                          "sample": {"zahl": "88 · 0123456789"}.get(ro, "Jede Zahl hat einen Grund · Haftanın Takımı")})
    gname = {"display": "Überschrift", "text": "Text", "zahl": "Zahlen", "label": "Beschriftung"}
    t = {"name": f"FootPulse {r} · {O.NAME[r]}", "version": 2,
         "color": {"themes": [{"id": "dark", "name": "Dark"}, {"id": "light", "name": "Light"}], "tokens": col},
         "type": {"fonts": [], "families": fam, "groups": [{"name": gname[g], "family": g, "styles": st} for g, st in groups.items()]},
         "spacing": {"tokens": [{"name": n, "value": f"{v}px", "usage": "Raster 4 pt"} for n, v in O.ABSTAND]},
         "radius": {"tokens": [{"name": n, "value": f"{v}px", "usage": z} for n, v, z in O.RADIUS[r]]}}
    return json.dumps(t, indent=1, ensure_ascii=False)


def readme(r, p):
    s = O.SCHRIFT[r]
    erg = json.load(open(os.path.join(HIER, "bildtests-ergebnis.json"), encoding="utf-8"))
    from matrix import pruefen, zusammenfassung
    zahlen = {t: zusammenfassung(pruefen(p[t], t)) for t in ("dark", "light")}
    feed = erg[r]["dark_v2"]["feed"]
    gr = "\n".join(f"| {n} | {sz}/{lh} px | {wt} | {ro} |" for n, sz, lh, wt, ro in O.GROESSEN[r])
    so = "\n".join(f"| {n} | {sz}/{lh} px |" for n, sz, lh in O.SOCIAL[r])
    return f"""# FootPulse {r} · {O.NAME[r]}

> Eine von drei Optionen für das FootPulse-Designsystem 2026 (A Anzeigetafel, B Messgerät, C Flutlicht). Stand 05.11.2026. **Noch nicht entschieden:** Burhan wählt oder mischt. Bis dahin ist das hier ein Vorschlag, keine gültige Fassung.

{O.KURZ[r]}

## Markenkern

FootPulse bewertet Fußballspieler nach dem, was auf dem Platz passiert, und sagt, warum sich eine Zahl bewegt. **Jede Zahl hat einen Grund.** (EN: Every number has a reason. TR: Her sayının bir sebebi var.)

Persönlichkeit: der ehrliche Experte aus der Kurve. Er ist ehrlich, genau, nah dran und jede Woche lebendig. FootPulse ist kein Videospiel, kein Liveticker, kein Wettanbieter und keine Gesundheits-App.

**Eine Marke, zwei Einsatzarten.** App und Website sind leise: wenig Rot, viel Struktur, die Zahlen sind die Hauptsache. Marketing ist laut: viel Rot, großer Kontrast, große Zahlen. Beide nutzen dieselben Grundfarben, dieselbe Schrift und dasselbe Zeichen.

## Farbe

Die Rollennamen sind dieselben wie in der App-Token-Datei. Neue Rollen für Zustände: `tabTrack`, `tabActive`, `surfaceHover`, `surfacePressed`, `surfaceSelected`, `surfaceDisabled`, `textDisabled`, `focusRing`, `onAccent`, `goldText`, `ratingInk`.

Regeln:
- **Rot heißt Zustand oder Aktion**, nie Deko. Rote Flächen mindestens 8 px, Linien mindestens 2 px. Rote Schrift und kleine rote Punkte kommen immer in `accentText`.
- **Gold nur für Verdientes** (MVP, Rang 1). Als Schrift im Hell-Modus `goldText`.
- **Auf und Ab nie nur über Farbe.** Immer ▲ mit +, ▼ mit −, ■ für unverändert.
- **Noten-Chips** zeigen immer die Zahl, in `ratingInk` auf der Stufenfarbe.
- **Ebenen trennen sich durch Helligkeit** (jede Stufe mindestens ΔL 3) und Linien. Keine Verläufe, kein Blur in der App.
- **Liga-Akzente** (`leagueBL`, `leaguePL`, `leagueSL`) sind nur Flächen für die Konten, immer mit Kürzel daneben. Keine echten Liga-Farben oder Liga-Logos.
- **Auf Rot steht das Logo nur einfarbig weiß.**

Gemessen (Testmatrix im Repo `marke/designsystem/testmatrix.md`): Dark {zahlen['dark'][0] - len(zahlen['dark'][1])} von {zahlen['dark'][0]}, Light {zahlen['light'][0] - len(zahlen['light'][1])} von {zahlen['light'][0]} Prüfungen bestanden (WCAG 2.x, APCA, Farbschwäche, Flächenstufen). Offen mit Regel: {', '.join(x['paar'] for x in zahlen['dark'][1]) or 'nichts'}.

## Schrift

Alle Schriften sind frei (SIL Open Font License, Google Fonts), haben ä ö ü ß und ğ ş ı İ ç und wurden im Browser gemessen.

| Rolle | Schrift |
|---|---|
| Überschrift | {s['display']['family']} {s['display'].get('hinweis', '')} |
| Text | {s['text']['family']} |
| Zahlen | {s['zahl']['family']}, immer `font-variant-numeric: tabular-nums` |
| Beschriftung | {s['label']['family']}, Großbuchstaben, Sperrung {s['label'].get('tracking', '')} |

Türkischer Text in Großbuchstaben braucht die Sprachangabe Türkisch (`lang="tr"`, in Canva die Spracheinstellung). Sonst wird aus „Demir“ „DEMIR“ statt „DEMİR“.

### Größen Web und App

| Stil | Größe/Zeile | Gewicht | Rolle |
|---|---|---|---|
{gr}

### Größen Social (bei 1080 px Breite)

| Stil | Größe/Zeile |
|---|---|
{so}

## Formensprache

- **Raster** 4 pt, Gutter 20, mobile Spalte 560 px, Breakpoints 720 und 960.
- **Ecken:** {', '.join(f'{n} {v} px ({z})' for n, v, z in O.RADIUS[r])}.
- **Linien:** {O.LINIE[r]}
- **Ebenen:** background → surfaceDeep → surface → surfaceElevated → surfaceOverlay, jede Stufe ΔL ≥ 3. Hover ist eine Stufe heller, gedrückt zwei.
- **Bewegung:** {O.BEWEGUNG[r]} Wer „Bewegung reduzieren“ eingestellt hat, bekommt nur Überblendungen.
- **Icons:** Strich 2 px bei 24 px, Ecken wie das Radius-Token, keine gefüllten Mehrfarb-Icons.

## Logo

Die Wortmarke ist eine eigene Zeichnung, keine Schrift. Dateien im Asset-Bereich „Logos“, alle Größen als PNG in OneDrive `00 Marke/Designsystem 2026/Logos/`. Die Regeln (Schutzzone, Mindestgröße, Do's und Don'ts) stehen in `logo-regeln.html` im Repo. Profilbilder der Liga-Konten nutzen dasselbe Zeichen mit Kürzel und Liga-Akzent.

## Social und Video

- **Reel- und TikTok-Cover 9:16 (1080 × 1920):** Safe Zone oben 250, unten 480, rechts 150, links 60 px. Das Profilraster schneidet mittig auf 3:4 (1080 × 1440). Das Wichtigste gehört in diesen Ausschnitt.
- **Karussell 4:5 (1080 × 1350):** Folie 1 Behauptung, Folien 2–3 der Grund mit Zahlen, letzte Folie Warteliste.
- **Story 9:16, X-Bild 16:9 (1600 × 900).**
- **Untertitel:** höchstens 2 Zeilen und 42 Zeichen je Zeile, Schlüsselwort in `accentText`, im unteren Drittel über der Safe Zone.
- **Intro** höchstens 1,6 s (Zeichen → Zahl → „Warum?“), **Outro** 2 s (Kernsatz → Logo und footpulse.org).
- **Bildsprache:** echte Spielszenen, frei lizenziert oder eigene Rechte. Im Marketing Schwarz-Weiß mit Rot, sonst neutral. Keine Vereinswappen ohne Rechte, keine KI-Gesichter echter Spieler.
- Wirkung im Feed (Näherung, gemessen): Farbabstand zum Feed ΔE {feed['dE_zum_feed']}, Kontrast nach Unschärfe {feed['kontrast_nach_unschaerfe']}.

## Text und Ton

Kurze Sätze. Zahlen zuerst, dann der Grund. Glossar: `marke/glossar.md`. Nicht „live“, sondern „nach jedem Spieltag“.
"""


PREV_HEAD = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
             '<link href="https://fonts.googleapis.com/css2?{g}&display=swap" rel="stylesheet">')


def bausteine(r):
    html = seiten.seite(r)
    css = re.search(r"<style>(.*?)\[data-safe", html, re.S).group(1)
    css = css.replace("html{background:var(--background)}", "")
    sec = lambda i: re.search(rf'<section class="blk" id="{i}">(.*?)</section>', html, re.S).group(1)
    strip = lambda t: re.sub(r'<span class="label cap">.*?</span>', "", t, count=1).replace('src="logo/', 'src="../../assets/Logos/')
    head = PREV_HEAD.format(g=O.SCHRIFT[r]["google"])
    def prev(group, h, body, sub):
        return f'<!-- @dsCard group="{group}" height={h} subtitle="{sub}" -->\n<!doctype html><html><head>{head}</head><body style="margin:0;padding:16px;background:var(--background);color:var(--textPrimary);font-family:var(--font-text)">{body}</body></html>\n'
    btn = ('<div style="display:flex;flex-direction:column;gap:10px;width:320px"><button class="btn">Auf die Warteliste</button>'
           '<button class="btn" style="background:var(--surfaceElevated);color:var(--textPrimary);box-shadow:inset 0 0 0 1px var(--borderStrong)">Zweitaktion</button>'
           '<button class="btn" style="background:transparent;color:var(--accentText)">Textknopf →</button>'
           '<button class="btn" style="outline:2px solid var(--focusRing);outline-offset:2px">Fokus</button><button class="btn dis" disabled>Deaktiviert</button></div>')
    form = ('<div style="width:340px"><label class="field"><span>E-Mail</span><input class="input" placeholder="name@beispiel.de"></label>'
            '<label class="field"><span>E-Mail (Fokus)</span><input class="input focus" value="kaan@"></label>'
            '<label class="field"><span>E-Mail (Fehler)</span><input class="input err" value="kaan@beispiel"><small class="errtxt">Bitte prüfe die Adresse.</small></label></div>')
    comps = {
        "PlayerCard": ("Daten", 520, strip(sec("t-karte")), "Overall, Position, sechs Werte, Bewegung und Grund",
                       "Die Spielerkarte ist das Kernmotiv. Overall groß oben links, Position darunter, sechs Werte in zwei Spalten, die Bewegung als Chip und der Grund in einem Kasten. Kein Wappenschild, kein Metallic."),
        "Tabs": ("Navigation", 200, strip(sec("t-tabs")), "Normal, Hover, gedrückt, aktiv, ausgewählt, Fokus, aus",
                 "Tab-Leiste mit allen Zuständen. Aktiv = tabActive plus Markierung (siehe Formensprache). Fokus = 2 px focusRing mit 2 px Abstand. Deaktiviert nutzt textDisabled und hat keine Kontrastpflicht."),
        "StatsTable": ("Daten", 420, strip(sec("t-tabelle")), "Zahlen mit gleich breiten Ziffern, ausgewählte Zeile",
                       "Tabellen trennen Zeilen mit borderSubtle. Zahlen stehen rechtsbündig in tabular-nums. Ausgewählte Zeile = surfaceSelected."),
        "RatingChips": ("Daten", 150, strip(sec("t-chips")), "Auf, Ab, gleich, MVP, Noten, Liga",
                        "Auf und Ab nie nur über Farbe: ▲ +, ▼ −, ■ 0. Noten-Chips immer mit Zahl in ratingInk. Liga-Akzente nur mit Kürzel."),
        "TeamOfTheWeek": ("Daten", 620, strip(sec("t-totw")), "Aufstellung auf dem Spielfeld, MVP in Gold",
                          "Team der Woche auf pitchGreen mit pitchLine. Mini-Karten mit Overall, Position und Name. Nur der MVP bekommt Gold."),
        "Button": ("Aktion", 330, btn, "Haupt-, Zweit- und Textaktion, Fokus, deaktiviert",
                   "Hauptaktion = accent mit onAccent. Eine Hauptaktion pro Ansicht. Zweitaktion mit borderStrong. Textknopf in accentText."),
        "Input": ("Formular", 300, form, "Normal, Fokus, Fehler",
                  "Eingabefeld auf surfaceSunken mit borderStrong (3 : 1). Fokus = focusRing. Fehler = accentText für Rand und Hinweis, immer mit Text, nie nur Farbe."),
    }
    return css + O_STIL(r), {k: (prev(g, h, b, sub), f"# {k}\n\n{txt}\n") for k, (g, h, b, sub, txt) in comps.items()}


def O_STIL(r):
    return seiten.STIL[r] + "\nimg.logo-l{display:none!important}"


def cover(r, p):
    name = "FootPulse"
    tag = {"A": "Anzeigetafel · Jede Zahl hat einen Grund.", "B": "Messgerät · Jede Zahl hat einen Grund.", "C": "Flutlicht · Jede Zahl hat einen Grund."}[r]
    if r == "A":
        der = ("blocks: accent 240×288 (cut-lg Anschnitt), surfaceElevated 120×144, surfaceOverlay 120×144, gold 48×48 · "
               "arrangement: hohe Platte mit Satelliten, rechts angeschnitten · pattern: Kacheln mit angeschnittener Ecke (cut-sm), weil die Kartenecke das Formmotiv ist · steps: space-6 Abstand, cut-sm/cut-lg")
        svg = ('<polygon class="a" points="600,0 812,0 840,28 840,288 600,288"/>'
               '<rect class="e" x="864" y="0" width="96" height="144"/><rect class="o" x="864" y="168" width="96" height="120"/>'
               '<rect class="g" x="528" y="216" width="48" height="48"/>'
               + "".join(f'<polygon class="t" points="{x},{y} {x + 32},{y} {x + 40},{y + 8} {x + 40},{y + 40} {x},{y + 40}"/>' for x in (504, 552) for y in (24, 88, 152)))
        sty = ".a{fill:var(--accent)}.e{fill:var(--surfaceElevated)}.o{fill:var(--surfaceOverlay)}.g{fill:var(--gold)}.t{fill:var(--surfaceHover)}"
    elif r == "B":
        der = ("blocks: surfaceElevated 216×288, accent 96×96 (radius-md), positiveMuted 120×120, gold 24 Kreis · arrangement: Raster aus Modulen · "
               "pattern: Punktraster im Abstand space-6, weil das System Raster und Haarlinien sagt · steps: space-6, radius-md, radius-pill")
        svg = ('<rect class="e" x="624" y="0" width="216" height="288"/><rect class="a" x="864" y="24" width="96" height="96" rx="12"/>'
               '<rect class="u" x="840" y="168" width="120" height="120" rx="12"/><circle class="g" cx="552" cy="240" r="12"/>'
               + "".join(f'<circle class="d" cx="{x}" cy="{y}" r="2.5"/>' for x in range(504, 601, 24) for y in range(24, 193, 24)))
        sty = ".e{fill:var(--surfaceElevated)}.a{fill:var(--accent)}.u{fill:var(--positiveMuted)}.g{fill:var(--gold)}.d{fill:var(--textFaint)}"
    else:
        der = ("blocks: mkRed 336×288, mkPaper 96×288, gold 48×96 · arrangement: Streifen ungleicher Breite, oben angeschnitten · "
               "pattern: schräge Streifen im Rot (Doppelhalter), weil das System Plakat und Kurve sagt · steps: space-6, radius-xs 0")
        svg = ('<rect class="r" x="576" y="0" width="336" height="288"/><rect class="p" x="912" y="0" width="48" height="288"/>'
               '<rect class="g" x="504" y="192" width="48" height="96"/>'
               + "".join(f'<polygon class="s" points="{x},288 {x + 24},288 {x + 120},0 {x + 96},0"/>' for x in range(576, 820, 72)))
        sty = ".r{fill:var(--mkRed)}.p{fill:var(--mkPaper)}.g{fill:var(--gold)}.s{fill:var(--mkRedDeep)}"
    head = PREV_HEAD.format(g=O.SCHRIFT[r]["google"])
    nf = "var(--font-display)"
    return f"""<!-- @dsCard height=288 -->
<!doctype html><html><head>{head}<style>
body{{margin:0;background:var(--background)}} .c{{position:relative;width:960px;height:288px;overflow:hidden;background:var(--background)}}
svg{{position:absolute;inset:0}} {sty}
.n{{position:absolute;left:40px;bottom:64px;font-family:{nf};font-weight:800;font-size:96px;line-height:.92;color:var(--textPrimary);{'text-transform:uppercase;' if r != 'B' else 'font-stretch:75%;'}}}
.tg{{position:absolute;left:42px;bottom:36px;font-family:var(--font-text);font-size:14px;color:var(--textSecondary);max-width:440px}}
</style></head><body><div class="c"><svg viewBox="0 0 960 288" width="960" height="288"><!-- {der} -->{svg}</svg>
<div class="n">{name}</div><div class="tg">{tag}</div></div></body></html>
"""


def index(r, assets):
    return json.dumps({"v": 3, "layout": "files", "createdOnFiles": {"v": 1, "at": "2026-11-05T01:30:00Z"},
                       "title": f"FootPulse {r} · {O.NAME[r]}", "namespace": f"FootPulse{r}", "libraries": [], "sections": {},
                       "groups": ["Logos"], "assetGroups": {"Logos": {"name": "Logos", "tile": "m", "order": [a["name"] for a in assets],
                                                                       "files": {a["name"]: a for a in assets}}},
                       "blobs": {}, "docs": {"sections": []},
                       "lastChange": {"by": "Burhan", "at": "2026-11-05T01:30:00Z", "via": "Claude Code", "note": "Erste Fassung aus marke/designsystem"}},
                      indent=1, ensure_ascii=False)


if __name__ == "__main__":
    ziel = sys.argv[1]
    for r in "ABC":
        p = palette(r, 2)
        base = os.path.join(ziel, r, "project")
        w(os.path.join(base, "tokens.json"), tokens(r, p))
        w(os.path.join(base, "README.md"), readme(r, p))
        css, comps = bausteine(r)
        w(os.path.join(base, "components", "bundle.css"), css)
        for k, (prev, rd) in comps.items():
            w(os.path.join(base, "components", k, "preview.html"), prev)
            w(os.path.join(base, "components", k, "README.md"), rd)
        w(os.path.join(base, "components", "Cover", "preview.html"), cover(r, p))
        w(os.path.join(base, "assets", "Logos", "README.md"),
          "# Logos\n\nAlle Logos als SVG. Auf Rot nur `kombi-quer-mono-weiss.svg`. Schutzzone und Mindestgrößen: `logo-regeln.html` im Repo. PNG in allen Größen: OneDrive `00 Marke/Designsystem 2026/Logos/`.\n")
    print("ok")
