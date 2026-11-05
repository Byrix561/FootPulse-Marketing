"""Erzeugt aus den Paletten: tokens.json, tokens.css, alt-neu.md je Option und die Testmatrix (Farbteil).

Aufruf aus diesem Ordner:  python -I bauen.py
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from farbe import hex_to_oklch, wcag, apca, delta_l
from paletten import BESTAND_DARK, ROLLEN_APP, ROLLEN_NEU, ROLLEN_MARKETING, ROLLEN_LIGA, ALLE, aufloesen, V1
from paletten_v2 import V2, V2_GRUENDE
from matrix import pruefen, zusammenfassung, STUFE_MIN
import optionen as O

HIER = os.path.dirname(os.path.abspath(__file__))
DS = os.path.dirname(HIER)
STAND = "04.11.2026"

ZWECK = {
    "background": "Seitenhintergrund", "surfaceSunken": "Vertiefte Flächen (Eingabefeld, Mulde)", "surface": "Karten, Listen",
    "surfaceElevated": "Gehobene Karten, Kopfzeilen", "surfaceOverlay": "Menüs, Popover, Tooltips", "surfaceWarm": "Hervorgehobene Karte mit Rot-Stich",
    "surfaceDeep": "Zwischenebene (Leisten, Tab-Spur)", "borderSubtle": "Trenner in Listen", "border": "Karten-Rand", "borderStrong": "Rand von Bedienelementen (3 : 1)",
    "textPrimary": "Haupttext, Zahlen", "textSecondary": "Nebentext", "textTertiary": "Beschriftungen", "textMuted": "Hinweise, ab 14 px halbfett",
    "textFaint": "Nur Nicht-Text: Pfeile, Trenner, Icons", "accent": "Rote Flächen, Buttons, Linien ≥ 2 px", "accentText": "Rote Schrift, kleine rote Punkte",
    "accentDim": "Gedrücktes Rot, rote Linie auf Rot", "accentMuted": "Hintergrund roter Chips", "gold": "Nur verdiente Auszeichnung (MVP, Rang 1)",
    "goldMuted": "Hintergrund Gold-Chip", "pitchGreen": "Spielfeld-Fläche (TOTW)", "pitchLine": "Spielfeld-Linien", "ratingUp": "Aufwertung (immer mit ▲ und +)",
    "positiveMuted": "Hintergrund Aufwertungs-Chip", "ratingDown": "Abwertung (immer mit ▼ und −)", "ratingElite": "Note Elite (Fläche, Zahl in ratingInk)",
    "ratingExcellent": "Note Excellent", "ratingGood": "Note Good", "ratingAverage": "Note Average", "ratingPoor": "Note Poor",
    "tabTrack": "NEU: Spur der Tab-Leiste", "tabActive": "NEU: Fläche des aktiven Tabs", "surfaceHover": "NEU: Hover auf Fläche",
    "surfacePressed": "NEU: Gedrückt / aktiv", "surfaceSelected": "NEU: Ausgewählte Zeile oder Karte", "surfaceDisabled": "NEU: Deaktivierte Fläche",
    "textDisabled": "NEU: Deaktivierter Text (keine Kontrastpflicht)", "focusRing": "NEU: Fokusrahmen 2 px, 2 px Abstand", "onAccent": "NEU: Schrift auf Rot",
    "goldText": "NEU: Gold als Schrift (im Hell-Modus dunkler)", "ratingInk": "NEU: Zahl auf Noten- und Liga-Flächen", "onRatingPoor": "NEU: Zahl auf der Note Poor (A: weiß auf Rot)",
    "mkRed": "Marketing: rote Vollfläche", "mkRedDeep": "Marketing: zweites Rot für Tiefe, Streifen", "mkInk": "Marketing: Schwarz",
    "mkPaper": "Marketing: Weiß / Kreide", "onMkRed": "Marketing: kleine Schrift auf Rot", "onMkRedLarge": "Marketing: Schlagzeile auf Rot",
    "leagueBL": "Akzent Bundesliga-Konto (Fläche)", "leaguePL": "Akzent Premier-League-Konto (Fläche)", "leagueSL": "Akzent Süper-Lig-Konto (Fläche)",
}


def palette(r, v=2):
    q = V1 if v == 1 else V2
    return aufloesen({t: dict(q[r][t]) for t in ("dark", "light")}, r)


def schreiben(pfad, text):
    os.makedirs(os.path.dirname(pfad), exist_ok=True)
    with io.open(pfad, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def tokens_json(r, p):
    s = O.SCHRIFT[r]
    data = {
        "meta": {"name": f"FootPulse · Option {r} · {O.NAME[r]}", "stand": STAND, "version": "2",
                 "hinweis": "Rollennamen wie in der App-Token-Datei. Neue Rollen sind in 'neu' gelistet. Marketing- und Liga-Farben gelten in beiden Modi."},
        "color": {
            "dark": {k: p["dark"][k] for k in ROLLEN_APP + ROLLEN_NEU},
            "light": {k: p["light"][k] for k in ROLLEN_APP + ROLLEN_NEU},
        },
        "neu": ROLLEN_NEU,
        "marketing": {k: p["dark"][k] for k in ROLLEN_MARKETING},
        "league": {k: p["dark"][k] for k in ROLLEN_LIGA},
        "font": {k: v for k, v in s.items() if k != "google"},
        "fontSource": f"https://fonts.google.com (OFL) · {s['google']}",
        "fontSize": {n: {"size": sz, "lineHeight": lh, "weight": w, "role": ro} for n, sz, lh, w, ro in O.GROESSEN[r]},
        "socialSize1080": {n: {"size": sz, "lineHeight": lh} for n, sz, lh in O.SOCIAL[r]},
        "space": {n: v for n, v in O.ABSTAND},
        "radius": {n: v for n, v, _ in O.RADIUS[r]},
        "layout": {"grid": 4, "gutter": 20, "mobileColumn": 560, "breakpoints": [720, 960]},
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def tokens_css(r, p):
    lines = [f"/* FootPulse Option {r} · {O.NAME[r]} · erzeugt aus tokens.json ({STAND}) */"]
    for theme in ("dark", "light"):
        sel = ':root, [data-theme="dark"]' if theme == "dark" else '[data-theme="light"]'
        lines.append(sel + " {")
        for k in ALLE:
            lines.append(f"  --{k}: {p[theme][k]};")
        lines.append("  --downChipBg: var(--accentMuted);")
        lines.append("  --downChipFg: var(--ratingDown);")
        lines.append("}")
    s = O.SCHRIFT[r]
    lines.append(":root {")
    for k in ("display", "text", "zahl", "label"):
        lines.append(f"  --font-{k}: {s[k]['css']};")
    for n, v in O.ABSTAND:
        lines.append(f"  --{n}: {v}px;")
    for n, v, _ in O.RADIUS[r]:
        lines.append(f"  --{n}: {v}px;")
    lines.append("}")
    return "\n".join(lines) + "\n"


def alt_neu(r, p):
    out = [f"# Option {r} · {O.NAME[r]}: alter Wert → neuer Wert", "",
           f"Stand {STAND}. Vorlage für den App-Umbau: Jede Zeile ist ein Austausch in der Token-Datei. "
           "Spalte „alt“ ist der heutige Dark-Wert. Light gibt es heute nicht, die Spalte ist neu.", "",
           "| Rolle | Zweck | alt (Dark) | neu Dark | neu Light | Änderung |", "|---|---|---|---|---|---|"]
    for k in ROLLEN_APP:
        alt = BESTAND_DARK[k]
        neu = p["dark"][k]
        dl = delta_l(alt, neu)
        art = "gleich" if alt.upper() == neu.upper() else (f"heller (ΔL {dl:.1f})" if hex_to_oklch(neu)[0] > hex_to_oklch(alt)[0] else f"dunkler (ΔL {dl:.1f})")
        out.append(f"| `{k}` | {ZWECK[k]} | `{alt}` | `{neu}` | `{p['light'][k]}` | {art} |")
    out += ["", "## Neue Rollen", "", "| Rolle | Zweck | neu Dark | neu Light |", "|---|---|---|---|"]
    for k in ROLLEN_NEU:
        out.append(f"| `{k}` | {ZWECK[k]} | `{p['dark'][k]}` | `{p['light'][k]}` |")
    out += ["", "## Marketing und Liga (beide Modi)", "", "| Rolle | Zweck | Wert |", "|---|---|---|"]
    for k in ROLLEN_MARKETING + ROLLEN_LIGA:
        out.append(f"| `{k}` | {ZWECK[k]} | `{p['dark'][k]}` |")
    out += ["", "## Schrift, Größen, Radien", ""]
    s = O.SCHRIFT[r]
    out.append(f"- Überschrift: **{s['display']['family']}**, Text: **{s['text']['family']}**, Zahlen: **{s['zahl']['family']}** mit `tabular-nums`, Beschriftung: **{s['label']['family']}**.")
    out.append("- Größen (px): " + ", ".join(f"{n} {sz}/{lh}" for n, sz, lh, _, _ in O.GROESSEN[r]) + ".")
    out.append("- Radien: " + ", ".join(f"`{n}` {v} px ({z})" for n, v, z in O.RADIUS[r]) + ".")
    out.append("- Raster 4 pt, Gutter 20, mobile Spalte 560 px, Breakpoints 720 und 960 bleiben.")
    return "\n".join(out) + "\n"


def fmt(x, nd=2):
    return "–" if x is None else (f"{x:.{nd}f}".replace(".", ","))


def matrix_md(alle):
    o = ["# Testmatrix Farbe", "", f"Stand {STAND}. Alle Werte selbst gerechnet mit `_werkzeug/farbe.py` (WCAG 2.x, APCA 0.0.98G-4g, "
         "Farbschwäche-Simulation nach Machado 2009 mit Stärke 1,0, Farbabstand in OKLab ×100). Keine Zahl ist geschätzt.", "",
         "## Wie man die Tabelle liest", "",
         "- **WCAG**: Kontrastverhältnis. Text braucht mindestens 4,5 : 1, große Schrift und Nicht-Text (Ränder, Icons, Fokus) 3 : 1.",
         "- **APCA Lc**: neueres Kontrastmaß, das helle Schrift auf dunkel realistischer bewertet. Minus heißt helle Schrift auf dunklem Grund. "
         "Ziele: Fließtext Lc 75, Inhaltstext Lc 60, große Schrift Lc 45, Nicht-Text Lc 30.",
         f"- **ΔL**: Helligkeitsabstand zweier Flächen (OKLab ×100). Unter {STUFE_MIN:.0f} wirkt es flach, ab 4 deutlich.",
         "- **ΔE**: Farbabstand. Ab 10 sind zwei Farben klar trennbar, auch in der Simulation von Rot-Grün-Schwäche (protan, deutan) und Blau-Gelb-Schwäche (tritan).",
         "", "## Ausgangslage: die heutige App", ""]
    b = BESTAND_DARK
    o += ["| Stufe | ΔL | Kontrast |", "|---|---|---|"]
    for a, c in [("background", "surfaceSunken"), ("surfaceSunken", "surfaceDeep"), ("surfaceDeep", "surface"), ("surface", "surfaceElevated"), ("surfaceElevated", "surfaceOverlay")]:
        o.append(f"| {a} → {c} | {fmt(delta_l(b[a], b[c]), 1)} | {fmt(wcag(b[a], b[c]))} : 1 |")
    o += ["", "Drei von fünf Stufen liegen unter ΔL 3. Das bestätigt die Kritik: Tabs und Flächen wirken flach. "
          f"Der Hintergrund `#050507` hat Kanalwerte von 5 bis 7 und liegt damit fast bei „Pixel aus“. "
          "Auf OLED-Bildschirmen schalten solche Pixel beim Scrollen verzögert an. Dadurch zieht dunkler Inhalt Schlieren (Black Smear). "
          "Hier ist das nicht messbar, es braucht einen Gerätetest. Die Faustregel „kein Kanal unter 12“ steht deshalb als eigene Prüfung in der Matrix.", ""]
    o += ["## Übersicht", "", "| Option | Modus | v1 bestanden | v2 bestanden | offen in v2 |", "|---|---|---|---|---|"]
    for r in "ABC":
        for t in ("dark", "light"):
            r1 = pruefen(alle[r][1][t], t)
            r2 = pruefen(alle[r][2][t], t)
            g1, f1 = zusammenfassung(r1)
            g2, f2 = zusammenfassung(r2)
            o.append(f"| {r} {O.NAME[r]} | {t} | {g1 - len(f1)} / {g1} | **{g2 - len(f2)} / {g2}** | {', '.join(x['paar'] for x in f2) or '–'} |")
    o += ["", "## Was sich von v1 zu v2 geändert hat", ""]
    for k, v in V2_GRUENDE:
        o.append(f"- **{k}:** {v}")
    o += ["", "## Bewusst offene Punkte in v2 (mit Regel)", "",
          "- **Rote Flächen (accent) als Nicht-Text:** WCAG 3 : 1 ist erfüllt, APCA erreicht Lc 27–29 statt 30. Noch helleres Rot würde weiße Button-Schrift unter 4,5 : 1 drücken. "
          "Regel: Rote Flächen und Linien mindestens 8 px bzw. 2 px. Kleinere rote Punkte kommen in `accentText`.",
          "- **Option C, verworfenes Signalrot:** Ein helleres Plakatrot (L 0,685) mit schwarzer Schrift erreichte nur Lc 47 und wirkte korallig. C nutzt deshalb dasselbe tiefe Rot wie A und B, mit Kreide-Schrift.",
          "- **Auf und Ab:** Rechnerisch auch bei Farbschwäche trennbar, aber nur knapp über ΔE 10. Pfeil (▲/▼) und Vorzeichen (+/−) bleiben Pflicht.", ""]
    for r in "ABC":
        o += [f"## Option {r} · {O.NAME[r]} · v2 im Detail", ""]
        for t in ("dark", "light"):
            o += [f"### {t.capitalize()}", "", "| Art | Paar | Vordergrund | Hintergrund | WCAG | APCA Lc | ΔL / ΔE | Ziel | Ergebnis |", "|---|---|---|---|---|---|---|---|---|"]
            for x in pruefen(alle[r][2][t], t):
                d = x.get("dl", x.get("de"))
                o.append(f"| {x['art']} | {x['paar']} | {('`' + x['fg'] + '`') if x['fg'] else '–'} | {('`' + x['bg'] + '`') if x['bg'] else '–'} | "
                         f"{fmt(x['wcag'])} | {fmt(x['apca'], 1)} | {fmt(d, 1) if d is not None else '–'} | {x['ziel']} | {'✅' if x['ok'] else '❌'}"
                         f"{(' ' + x['urteil']) if 'urteil' in x else ''} |")
            o.append("")
        o += [f"### v1 (zum Vergleich): durchgefallen", ""]
        for t in ("dark", "light"):
            f1 = [x for x in pruefen(alle[r][1][t], t) if not x["ok"]]
            o.append(f"- **{t}** ({len(f1)}): " + "; ".join(f"{x['paar']} ({fmt(x['wcag'])} : 1 / Lc {fmt(x['apca'], 1)})" if x['wcag'] else f"{x['paar']} ({fmt(x.get('dl', x.get('de')), 1)})" for x in f1))
        o.append("")
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    alle = {r: {1: palette(r, 1), 2: palette(r, 2)} for r in "ABC"}
    for r in "ABC":
        d = os.path.join(DS, O.ORDNER[r])
        schreiben(os.path.join(d, "tokens.json"), tokens_json(r, alle[r][2]))
        schreiben(os.path.join(d, "tokens.css"), tokens_css(r, alle[r][2]))
        schreiben(os.path.join(d, "tokens-v1.css"), tokens_css(r, alle[r][1]))
        schreiben(os.path.join(d, "alt-neu.md"), alt_neu(r, alle[r][2]))
    schreiben(os.path.join(DS, "testmatrix.md"), matrix_md(alle))
    import logos, seiten, vorlagen, logo_seiten
    for r in "ABC":
        schreiben(os.path.join(DS, O.ORDNER[r], "logo-regeln.html"), logo_seiten.regeln(r, alle[r][2]["dark"]))
        schreiben(os.path.join(DS, "_werkzeug", f"logo-export-{r}.html").replace("_werkzeug", O.ORDNER[r]), logo_seiten.export_seite(r))
    for r in "ABC":
        schreiben(os.path.join(DS, O.ORDNER[r], "vorlagen.html"), vorlagen.board(r))
    for r in "ABC":
        schreiben(os.path.join(DS, O.ORDNER[r], "testseiten.html"), seiten.seite(r))
    logos.schreiben_alle(DS, {r: alle[r][2] for r in "ABC"}, O.ORDNER)
    # schnelle Übersicht aller Logo-Dateien (Arbeitsansicht)
    html = ['<!doctype html><meta charset="utf-8"><title>Logo-Übersicht</title><style>body{font:13px system-ui;margin:16px;background:#888}'
            'section{margin-bottom:24px}div{display:inline-flex;flex-direction:column;gap:4px;margin:6px;vertical-align:top}'
            'img{max-height:140px;max-width:320px;background:repeating-conic-gradient(#ccc 0 25%,#eee 0 50%) 0 0/16px 16px}</style>']
    for r in "ABC":
        d = os.path.join(DS, O.ORDNER[r], "logo")
        html.append(f"<section><h2>{r} · {O.NAME[r]}</h2>")
        for n in sorted(os.listdir(d)):
            html.append(f'<div><img src="../{O.ORDNER[r]}/logo/{n}"><span>{n}</span></div>')
        html.append("</section>")
    schreiben(os.path.join(DS, "_werkzeug", "logo-uebersicht.html"), "".join(html))
    print("fertig")
