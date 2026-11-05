"""Logo-System der drei Optionen als SVG. Die Buchstaben sind eigene Konstruktionen (Polygone bzw. Linien), keine Schrift.

A · Anzeigetafel: kantige Großbuchstaben, jede obere rechte Außenecke angeschnitten wie die Spielerkarte.
   Bildmarke: Karte mit angeschnittener Ecke, darin ein Puls, der höher endet, als er beginnt (Aufwertung).
B · Messgerät: kleingeschriebene Strichschrift mit runden Enden. Bildmarke: Rundinstrument mit Ausschlag nach oben.
C · Flutlicht: sehr schmale, schwere Plakat-Großbuchstaben, zweizeilig. Bildmarke: FP-Schablone, ein Puls schneidet hindurch.
"""
import os

# ------------------------------------------------------------------ Polygon-Alphabet (A und C)


def glyph(ch, W, H, s, c):
    """Gibt eine Liste von Polygonen (Liste von Punkten) zurück. Das erste ist außen, weitere sind Löcher (evenodd)."""
    cs = min(c, s * 0.45) if c else 0  # Anschnitt auf schmalen Stämmen
    m = round(H * 0.42)                 # Höhe der Mittellinie
    if ch == "F":
        return [[(0, 0), (W - c, 0), (W, c), (W, s), (s, s), (s, m), (W - 3, m), (W - 3, m + s), (s, m + s), (s, H), (0, H)]]
    if ch == "O":
        ci = c * 0.5
        return [[(0, 0), (W - c, 0), (W, c), (W, H), (c, H), (0, H - c)],
                [(s, s), (W - s - ci, s), (W - s, s + ci), (W - s, H - s), (s + ci, H - s), (s, H - s - ci)]]
    if ch == "T":
        a, b = (W - s) / 2, (W + s) / 2
        return [[(0, 0), (W - c, 0), (W, c), (W, s), (b, s), (b, H), (a, H), (a, s), (0, s)]]
    if ch == "P":
        pb = round(H * 0.6)
        return [[(0, 0), (W - c, 0), (W, c), (W, pb), (s, pb), (s, H), (0, H)], [(s, s), (W - s, s), (W - s, pb - s), (s, pb - s)]]
    if ch == "B":
        return [[(0, 0), (W - c, 0), (W, c), (W, m), (W - 2, m), (W - 2, m + s), (W, m + s), (W, H), (0, H)],
                [(s, s), (W - s, s), (W - s, m), (s, m)], [(s, m + s), (W - s, m + s), (W - s, H - s), (s, H - s)]]
    if ch == "U":
        return [[(0, 0), (s - cs, 0), (s, cs), (s, H - s), (W - s, H - s), (W - s, 0), (W - cs, 0), (W, cs), (W, H), (c, H), (0, H - c)]]
    if ch == "L":
        return [[(0, 0), (s - cs, 0), (s, cs), (s, H - s), (W, H - s), (W, H), (0, H)]]
    if ch == "S":
        return [[(0, 0), (W - c, 0), (W, c), (W, s), (s, s), (s, m), (W, m), (W, H), (c, H), (0, H - c), (0, H - s), (W - s, H - s), (W - s, m + s), (0, m + s)]]
    if ch == "E":
        return [[(0, 0), (W - c, 0), (W, c), (W, s), (s, s), (s, m), (W - 3, m), (W - 3, m + s), (s, m + s), (s, H - s), (W, H - s), (W, H), (0, H)]]
    raise ValueError(ch)


def poly_d(polys, dx=0, dy=0):
    out = []
    for p in polys:
        out.append("M" + " L".join(f"{x + dx:g} {y + dy:g}" for x, y in p) + "Z")
    return "".join(out)


def word_d(text, W, H, s, c, gap, dx=0, dy=0, breiten=None):
    d, x = "", dx
    for ch in text:
        w = (breiten or {}).get(ch, W)
        d += poly_d(glyph(ch, w, H, s, c), x, dy)
        x += w + gap
    return d, x - gap - dx


# ------------------------------------------------------------------ SVG-Hülle


def svg(w, h, body, title, bg=None, defs=""):
    bgr = f'<rect width="{w:g}" height="{h:g}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" width="{w:g}" height="{h:g}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{('<defs>' + defs + '</defs>') if defs else ''}{bgr}{body}</svg>\n")


# ------------------------------------------------------------------ A · Anzeigetafel
A_PULS = "M6 32H13L17 24L23 38L29 13L33 21H36"   # endet bei y 21, beginnt bei y 32: höher = Aufwertung


def a_marke(x, y, scale, fill, puls, mono=False, mid="a"):
    """Karte 40×48 mit Anschnitt. puls: Farbe oder None (dann ausgeschnitten)."""
    card = f"M0 0H30L40 10V48H0Z"
    t = f'transform="translate({x:g} {y:g}) scale({scale:g})"'
    if puls is None:
        m = (f'<mask id="m{mid}" maskUnits="userSpaceOnUse" x="-2" y="-2" width="44" height="52"><rect x="-2" y="-2" width="44" height="52" fill="#fff"/>'
             f'<path d="{A_PULS}" fill="none" stroke="#000" stroke-width="3.8" stroke-linejoin="miter" stroke-linecap="square"/></mask>')
        return m, f'<g {t}><path d="{card}" fill="{fill}" mask="url(#m{mid})"/></g>'
    return "", (f'<g {t}><path d="{card}" fill="{fill}"/>'
                f'<path d="{A_PULS}" fill="none" stroke="{puls}" stroke-width="3.8" stroke-linejoin="miter" stroke-linecap="square"/></g>')


def a_wort(x, y, fill, h=40):
    k = h / 40
    d, w = word_d("FOOTPULSE", 25, 40, 7.5, 6, 4.5)
    return f'<path transform="translate({x:g} {y:g}) scale({k:g})" fill="{fill}" fill-rule="evenodd" d="{d}"/>', w * k


# ------------------------------------------------------------------ B · Messgerät
B_GLYPHEN = {  # Strichschrift, Grundlinie y 30, x-Höhe y 10, Oberlänge y 0, Unterlänge y 40
    "f": ("M9 30V9A7.5 7.5 0 0 1 16.5 1.5H18M2 11H16", 18),
    "o": ("M10 10A10 10 0 1 1 9.99 10Z", 20),
    "t": ("M6 2V23A7 7 0 0 0 13 30H15M0.5 11H14", 15),
    "p": ("M0 10V40M0 20A10 10 0 1 1 0 20.01Z", 20),
    "u": ("M0 10V20A10 10 0 0 0 20 20V10M20 10V30", 20),
    "l": ("M3 0V30", 6),
    "s": ("M16.5 13C15 11 12.5 10 9.5 10C5 10 2 12 2 15C2 19 6 19.6 9.5 20C13.5 20.5 17.5 21.5 17.5 25.5C17.5 28.6 14.5 30 10 30C6 30 3 29 1 26.5", 18.5),
    "e": ("M0.5 20H20A10 10 0 1 0 17.07 27.07", 20),
    "b": ("M0 0V30M0 20A10 10 0 1 0 0 19.99Z", 20),
}


def b_wort(x, y, color, text="footpulse", h=40, sw=5.2, gap=7):
    k = h / 40
    parts, cx = [], 0
    for ch in text:
        d, w = B_GLYPHEN[ch]
        off = 3 if ch in "fpb" else 2
        parts.append(f'<path transform="translate({cx + off:g} 0)" d="{d}"/>')
        cx += w + gap
    w = cx - gap + 4
    return (f'<g transform="translate({x:g} {y:g}) scale({k:g})" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
            + "".join(parts) + "</g>"), w * k


B_PULS = "M-15 4H-6L-2 -3L3 12L8 -12L11.5 -3H15"


def b_marke(x, y, d, ring, puls, sw_ring=3.2):
    """Rundinstrument, Durchmesser d. Ausschlag endet höher als Start."""
    k = d / 44
    return (f'<g transform="translate({x + d / 2:g} {y + d / 2:g}) scale({k:g})">'
            f'<circle r="20.4" fill="none" stroke="{ring}" stroke-width="{sw_ring}"/>'
            f'<path d="{B_PULS}" fill="none" stroke="{puls}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></g>')


# ------------------------------------------------------------------ C · Flutlicht
C_PULS = "M0 33H12L17 26L23 41L31 16L36 28H60"


def c_marke(x, y, size, quadrat, buchst, puls_schnitt, mid="c"):
    """FP-Schablone im Quadrat 60×60. Der Puls schneidet die Buchstaben (Farbe des Quadrats)."""
    k = size / 60
    f, _ = word_d("FP", 20, 44, 8, 0, 4, 8, 8)
    body = (f'<g transform="translate({x:g} {y:g}) scale({k:g})">'
            f'<rect width="60" height="60" fill="{quadrat}"/>'
            f'<path d="{f}" fill="{buchst}" fill-rule="evenodd"/>'
            f'<path d="{C_PULS}" fill="none" stroke="{puls_schnitt}" stroke-width="3.2" stroke-linejoin="miter"/></g>')
    return body


def c_marke_mono(x, y, size, farbe, mid="c"):
    """Einfarbig: Quadrat in Farbe, Buchstaben und Puls ausgeschnitten."""
    k = size / 60
    f, _ = word_d("FP", 20, 44, 8, 0, 4, 8, 8)
    defs = (f'<mask id="m{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="60" height="60"><rect width="60" height="60" fill="#fff"/>'
            f'<path d="{f}" fill="#000" fill-rule="evenodd"/><path d="{C_PULS}" fill="none" stroke="#fff" stroke-width="3.2"/></mask>')
    return defs, f'<g transform="translate({x:g} {y:g}) scale({k:g})"><rect width="60" height="60" fill="{farbe}" mask="url(#m{mid})"/></g>'


def c_wort(x, y, farbe1, farbe2, h=104, zweizeilig=True):
    """FOOT / PULSE in schmalen Plakat-Großbuchstaben. h = Gesamthöhe bei zwei Zeilen."""
    zh = 52
    k = h / (2 * zh + 6) if zweizeilig else h / zh
    d1, w1 = word_d("FOOT", 19, zh, 7.5, 0, 3.5)
    d2, w2 = word_d("PULSE", 19, zh, 7.5, 0, 3.5)
    if zweizeilig:
        return (f'<g transform="translate({x:g} {y:g}) scale({k:g})"><path fill="{farbe1}" fill-rule="evenodd" d="{d1}"/>'
                f'<path transform="translate(0 {zh + 6})" fill="{farbe2}" fill-rule="evenodd" d="{d2}"/></g>'), max(w1, w2) * k
    d, w = word_d("FOOTPULSE", 19, zh, 7.5, 0, 3.5)
    dF, wF = word_d("FOOT", 19, zh, 7.5, 0, 3.5)
    dP, _ = word_d("PULSE", 19, zh, 7.5, 0, 3.5, dx=wF + 3.5)
    return (f'<g transform="translate({x:g} {y:g}) scale({k:g})"><path fill="{farbe1}" fill-rule="evenodd" d="{dF}"/>'
            f'<path fill="{farbe2}" fill-rule="evenodd" d="{dP}"/></g>'), w * k


# ------------------------------------------------------------------ Liga-Kürzel
def kuerzel(r, text, x, y, h, farbe):
    if r == "B":
        return b_wort(x, y - h * 0.25, farbe, text.lower(), h=h * 1.0, sw=6)[0]
    W = 22 if r == "A" else 19
    s = 8.5 if r == "A" else 7.5
    c = 6 if r == "A" else 0
    H = 40 if r == "A" else 52
    k = h / H
    d, _ = word_d(text, W, H, s, c, 4)
    return f'<path transform="translate({x:g} {y:g}) scale({k:g})" fill="{farbe}" fill-rule="evenodd" d="{d}"/>'


# ------------------------------------------------------------------ Satz aller Dateien je Option


def satz(r, p):
    """p: Palette (dark). Gibt {dateiname: svg} zurück."""
    rot, ink, paper = p["accent"], p["mkInk"], p["mkPaper"]
    lightbg = "#FFFFFF"
    out = {}
    L = {"BL": p["leagueBL"], "PL": p["leaguePL"], "SL": p["leagueSL"]}
    if r == "A":
        for name, fill, puls, bg in (("rot", rot, ink, None), ("dunkel", rot, ink, ink), ("hell", rot, lightbg, lightbg)):
            out[f"bildmarke-{name}.svg"] = svg(40, 48, a_marke(0, 0, 1, fill, puls)[1], "FootPulse Bildmarke", None)
        for name, col in (("mono-schwarz", "#000000"), ("mono-weiss", "#FFFFFF")):
            d, b = a_marke(0, 0, 1, col, None, mid=name)
            out[f"bildmarke-{name}.svg"] = svg(40, 48, b, "FootPulse Bildmarke einfarbig", None, d)
        for name, col in (("auf-dunkel", paper), ("auf-hell", ink), ("mono-schwarz", "#000000"), ("mono-weiss", "#FFFFFF")):
            b, w = a_wort(0, 0, col)
            out[f"wortmarke-{name}.svg"] = svg(round(w + 0.5), 40, b, "FootPulse Wortmarke")
        for name, wcol, pc, bg in (("auf-dunkel", paper, ink, None), ("auf-hell", ink, lightbg, None)):
            m = a_marke(0, 0, 1, rot, pc)[1]
            b, w = a_wort(54, 4, wcol)
            out[f"kombi-quer-{name}.svg"] = svg(round(54 + w + 0.5), 48, m + b, "FootPulse Logo quer")
            m2 = a_marke((w - 80) / 2, 0, 2, rot, pc)[1]
            b2, _ = a_wort(0, 112, wcol)
            out[f"kombi-hoch-{name}.svg"] = svg(round(w + 0.5), 152, m2 + b2, "FootPulse Logo hoch")
        for name, fill, puls in (("mono-schwarz", "#000000", None), ("mono-weiss", "#FFFFFF", None)):
            d, m = a_marke(0, 0, 1, fill, None, mid="k" + name)
            b, w = a_wort(54, 4, fill)
            out[f"kombi-quer-{name}.svg"] = svg(round(54 + w + 0.5), 48, m + b, "FootPulse Logo quer einfarbig", None, d)
        out["app-icon.svg"] = svg(1024, 1024, a_marke(512 - 200, 512 - 240, 10, ink, rot)[1], "FootPulse App-Icon", rot)
        out["favicon.svg"] = svg(32, 32, '<path d="M0 0H24L32 8V32H0Z" fill="%s"/><path d="M3 21H8L11 15L15 26L19 9L22 15H25" fill="none" stroke="%s" stroke-width="3" stroke-linejoin="miter" stroke-linecap="square"/>' % (rot, ink), "FootPulse Favicon")
        out["profilbild.svg"] = svg(1080, 1080, a_marke(540 - 180, 540 - 216, 9, rot, ink)[1], "FootPulse Profilbild", ink)
        for lg, col in L.items():
            body = a_marke(540 - 180, 540 - 270, 9, rot, ink)[1] + f'<rect x="300" y="770" width="480" height="96" fill="{col}"/>' + kuerzel("A", lg, 540 - 46, 784, 68, ink)
            out[f"profilbild-{lg.lower()}.svg"] = svg(1080, 1080, body, f"FootPulse {lg} Profilbild", ink)
    if r == "B":
        graph = p["background"]
        for name, ring, puls in (("dunkel", paper, rot), ("hell", ink, rot)):
            out[f"bildmarke-{name}.svg"] = svg(44, 44, b_marke(0, 0, 44, ring, puls), "FootPulse Bildmarke")
        for name, col in (("mono-schwarz", "#000000"), ("mono-weiss", "#FFFFFF")):
            out[f"bildmarke-{name}.svg"] = svg(44, 44, b_marke(0, 0, 44, col, col), "FootPulse Bildmarke einfarbig")
        for name, col in (("auf-dunkel", paper), ("auf-hell", ink), ("mono-schwarz", "#000000"), ("mono-weiss", "#FFFFFF")):
            b, w = b_wort(3, 3, col)
            out[f"wortmarke-{name}.svg"] = svg(round(w + 6), 46, b, "FootPulse Wortmarke")
        for name, wcol, ring in (("auf-dunkel", paper, paper), ("auf-hell", ink, ink), ("mono-schwarz", "#000000", "#000000"), ("mono-weiss", "#FFFFFF", "#FFFFFF")):
            puls = rot if "mono" not in name else wcol
            b, w = b_wort(58, 5, wcol)
            out[f"kombi-quer-{name}.svg"] = svg(round(58 + w + 4), 48, b_marke(2, 2, 44, ring, puls) + b, "FootPulse Logo quer")
            b2, w2 = b_wort(0, 104, wcol)
            out[f"kombi-hoch-{name}.svg"] = svg(round(w2 + 2), 150, b_marke((w2 - 88) / 2, 0, 88, ring, puls) + b2, "FootPulse Logo hoch")
        out["app-icon.svg"] = svg(1024, 1024, b_marke(232, 232, 560, paper, rot, 3.0), "FootPulse App-Icon", graph)
        out["favicon.svg"] = svg(32, 32, f'<circle cx="16" cy="16" r="13.5" fill="{graph}" stroke="{paper}" stroke-width="3"/><path d="M5 18H10L12.5 14L15.5 23L19 8L21 14H27" fill="none" stroke="{rot}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>', "FootPulse Favicon")
        out["profilbild.svg"] = svg(1080, 1080, b_marke(260, 260, 560, paper, rot, 3.0), "FootPulse Profilbild", graph)
        for lg, col in L.items():
            body = (b_marke(290, 200, 500, paper, rot, 3.0) + f'<rect x="390" y="760" width="300" height="112" rx="56" fill="{col}"/>'
                    + kuerzel("B", lg, 462, 790, 64, ink))
            out[f"profilbild-{lg.lower()}.svg"] = svg(1080, 1080, body, f"FootPulse {lg} Profilbild", graph)
    if r == "C":
        mk = p["mkRed"]
        out["bildmarke-rot.svg"] = svg(60, 60, c_marke(0, 0, 60, mk, paper, mk), "FootPulse Bildmarke")
        out["bildmarke-dunkel.svg"] = svg(60, 60, c_marke(0, 0, 60, ink, paper, ink), "FootPulse Bildmarke")
        out["bildmarke-hell.svg"] = svg(60, 60, c_marke(0, 0, 60, paper, ink, paper), "FootPulse Bildmarke")
        for name, col in (("mono-schwarz", "#000000"), ("mono-weiss", "#FFFFFF")):
            d, b = c_marke_mono(0, 0, 60, col, mid=name)
            out[f"bildmarke-{name}.svg"] = svg(60, 60, b, "FootPulse Bildmarke einfarbig", None, d)
        for name, c1, c2 in (("auf-dunkel", paper, p["accentText"]), ("auf-hell", ink, mk), ("mono-schwarz", "#000000", "#000000"), ("mono-weiss", "#FFFFFF", "#FFFFFF")):
            b, w = c_wort(0, 0, c1, c2, h=110)
            out[f"wortmarke-{name}.svg"] = svg(round(w + 1), 110, b, "FootPulse Wortmarke zweizeilig")
            b1, w1 = c_wort(0, 0, c1, c2, h=52, zweizeilig=False)
            out[f"wortmarke-einzeilig-{name}.svg"] = svg(round(w1 + 1), 52, b1, "FootPulse Wortmarke einzeilig")
        for name, c1, c2, q, bu in (("auf-dunkel", paper, p["accentText"], mk, paper), ("auf-hell", ink, mk, mk, paper)):
            b, w = c_wort(124, 4, c1, c2, h=110)
            out[f"kombi-quer-{name}.svg"] = svg(round(124 + w + 1), 118, c_marke(0, 0, 118, q, bu, q) + b, "FootPulse Logo quer")
        for name, col in (("mono-weiss", "#FFFFFF"), ("mono-schwarz", "#000000")):
            d, m = c_marke_mono(0, 0, 118, col, mid="k" + name)
            bw, w = c_wort(124, 4, col, col, h=110)
            out[f"kombi-quer-{name}.svg"] = svg(round(124 + w + 1), 118, m + bw, "FootPulse Logo quer einfarbig", None, d)
        out["app-icon.svg"] = svg(1024, 1024, c_marke(152, 152, 720, mk, paper, mk), "FootPulse App-Icon", mk)
        out["favicon.svg"] = svg(32, 32, c_marke(0, 0, 32, mk, paper, mk), "FootPulse Favicon")
        out["profilbild.svg"] = svg(1080, 1080, c_marke(240, 240, 600, mk, paper, mk), "FootPulse Profilbild", mk)
        for lg, col in L.items():
            body = c_marke(290, 170, 500, mk, paper, mk) + f'<rect x="0" y="740" width="1080" height="150" fill="{col}"/>' + kuerzel("C", lg, 540 - 54, 760, 110, ink)
            out[f"profilbild-{lg.lower()}.svg"] = svg(1080, 1080, body, f"FootPulse {lg} Profilbild", mk)
    return out


def schreiben_alle(ds_dir, paletten, ordner):
    for r in "ABC":
        d = os.path.join(ds_dir, ordner[r], "logo")
        os.makedirs(d, exist_ok=True)
        for n, s in satz(r, paletten[r]["dark"]).items():
            with open(os.path.join(d, n), "w", encoding="utf-8", newline="\n") as f:
                f.write(s)
