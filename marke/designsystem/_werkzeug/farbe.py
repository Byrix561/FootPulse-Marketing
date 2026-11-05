"""Farb-Werkzeuge für das FootPulse-Designsystem.

Alles hier ist selbst gerechnet, ohne fremde Bibliotheken außer numpy:
- OKLCH <-> sRGB (Björn Ottosson, OKLab 2020)
- WCAG 2.x Kontrastverhältnis
- APCA Lc (APCA-W3 0.0.98G-4g, die Konstanten der öffentlichen Referenz)
- Simulation von Farbschwäche nach Machado, Oliveira & Fernandes 2009 (Stärke 1.0)
- Farbabstand ΔE in OKLab (×100, damit die Zahlen gut lesbar sind)
"""
import math
import numpy as np


# ---------- sRGB ----------
def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(c * 255))):02X}" for c in rgb)


def to_lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def from_lin(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


# ---------- OKLab / OKLCH ----------
def lin_to_oklab(r, g, b):
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (np.cbrt(x) for x in (l, m, s))
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def oklab_to_lin(L, a, b):
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
            -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
            -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s)


def oklch_to_hex(L, C, H):
    """OKLCH nach Hex. Liegt die Farbe außerhalb von sRGB, wird die Buntheit gesenkt (Ton und Helligkeit bleiben)."""
    lo, hi = 0.0, C
    def conv(c):
        a, b = c * math.cos(math.radians(H)), c * math.sin(math.radians(H))
        return oklab_to_lin(L, a, b)
    rgb = conv(C)
    if all(-1e-6 <= x <= 1 + 1e-6 for x in rgb):
        return rgb_to_hex([from_lin(max(0, min(1, x))) for x in rgb])
    for _ in range(30):
        mid = (lo + hi) / 2
        if all(-1e-6 <= x <= 1 + 1e-6 for x in conv(mid)):
            lo = mid
        else:
            hi = mid
    return rgb_to_hex([from_lin(max(0, min(1, x))) for x in conv(lo)])


def hex_to_oklab(h):
    r, g, b = (to_lin(c) for c in hex_to_rgb(h))
    return lin_to_oklab(r, g, b)


def hex_to_oklch(h):
    L, a, b = hex_to_oklab(h)
    return L, math.hypot(a, b), (math.degrees(math.atan2(b, a)) + 360) % 360


def delta_e(h1, h2):
    a, b = hex_to_oklab(h1), hex_to_oklab(h2)
    return 100 * math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def delta_l(h1, h2):
    return 100 * abs(hex_to_oklab(h1)[0] - hex_to_oklab(h2)[0])


# ---------- WCAG 2.x ----------
def rel_lum(h):
    r, g, b = (to_lin(c) for c in hex_to_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def wcag(fg, bg):
    a, b = rel_lum(fg), rel_lum(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


# ---------- APCA 0.0.98G-4g ----------
def _apca_y(h):
    r, g, b = hex_to_rgb(h)
    y = 0.2126729 * r ** 2.4 + 0.7151522 * g ** 2.4 + 0.0721750 * b ** 2.4
    return y + (0.022 - y) ** 1.414 if y < 0.022 else y


def apca(fg, bg):
    """APCA Lc. Positiv = dunkle Schrift auf hell, negativ = helle Schrift auf dunkel."""
    yt, yb = _apca_y(fg), _apca_y(bg)
    if abs(yb - yt) < 0.0005:
        return 0.0
    if yb > yt:
        s = (yb ** 0.56 - yt ** 0.57) * 1.14
        return 0.0 if s < 0.1 else (s - 0.027) * 100
    s = (yb ** 0.65 - yt ** 0.62) * 1.14
    return 0.0 if s > -0.1 else (s + 0.027) * 100


# ---------- Farbschwäche (Machado 2009, Stärke 1.0, in linearem RGB) ----------
CVD = {
    "protan": np.array([[0.152286, 1.052583, -0.204868], [0.114503, 0.786281, 0.099216], [-0.003882, -0.048116, 1.051998]]),
    "deutan": np.array([[0.367322, 0.860646, -0.227968], [0.280085, 0.672501, 0.047413], [-0.011820, 0.042940, 0.968881]]),
    "tritan": np.array([[1.255528, -0.076749, -0.178779], [-0.078411, 0.930809, 0.147602], [0.004733, 0.691367, 0.303900]]),
}


def simulate(h, kind):
    lin = np.array([to_lin(c) for c in hex_to_rgb(h)])
    out = np.clip(CVD[kind] @ lin, 0, 1)
    return rgb_to_hex([from_lin(c) for c in out])


def simulate_image(arr, kind):
    """arr: numpy uint8 HxWx3. Gibt simuliertes Bild zurück."""
    x = arr.astype(np.float64) / 255
    lin = np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)
    out = np.clip(lin @ CVD[kind].T, 0, 1)
    srgb = np.where(out <= 0.0031308, 12.92 * out, 1.055 * out ** (1 / 2.4) - 0.055)
    return (srgb * 255 + 0.5).astype(np.uint8)
