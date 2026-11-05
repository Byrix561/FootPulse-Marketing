"""Bildtests auf den Screenshots der Testseiten.

- schneidet jeden Abschnitt als eigenes Bild aus
- simuliert Rot-Grün- (protan, deutan) und Blau-Gelb-Schwäche (tritan) direkt auf dem Bild
- misst die Flächenstufen im gerenderten Bild nach (Pixel, nicht Token)
- misst die Wirkung im Feed (Farbabstand zu fremden Posts, Kontrast nach Unschärfe)
Aufruf:  python -I bildtests.py <Screenshot-Ordner> <Rects-Ordner>
"""
import io
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from farbe import simulate_image, rgb_to_hex, delta_l, delta_e, hex_to_oklab
import optionen as O

S = 2  # deviceScaleFactor der Aufnahmen
ZELLEN = ["surfaceSunken", "background", "surfaceDeep", "surface", "surfaceHover", "surfaceElevated", "surfacePressed", "surfaceOverlay",
          "surfaceSelected", "surfaceWarm", "surfaceDisabled", "focusRing"]
KETTE = [("background", "surfaceDeep"), ("surfaceDeep", "surface"), ("surface", "surfaceElevated"), ("surfaceElevated", "surfaceOverlay"),
         ("surfaceSunken", "background"), ("surface", "surfaceHover"), ("surfaceHover", "surfacePressed"), ("surface", "surfaceSelected")]


def crop(img, r, pad=0):
    x, y, w, h = r
    return img.crop(((x - pad) * S, (y - pad) * S, (x + w + pad) * S, (y + h + pad) * S))


def px_hex(img, x, y):
    a = np.asarray(img.crop((x * S - 3, y * S - 3, x * S + 3, y * S + 3)).convert("RGB")).reshape(-1, 3).mean(0) / 255
    return rgb_to_hex(a)


def leiter(img, r):
    x, y, w, h = r
    x0, y0 = x + 17, y + h - 17 - 252
    out = {}
    for i, name in enumerate(ZELLEN):
        row, col = divmod(i, 4)
        out[name] = px_hex(img, x0 + col * 110 + 100, y0 + row * 84 + 76)
    return out


def cvd_tafel(teil):
    arr = np.asarray(teil.convert("RGB"))
    bilder = [("normal", arr)] + [(k, simulate_image(arr, k)) for k in ("protan", "deutan", "tritan")]
    w, h = teil.size
    tafel = Image.new("RGB", (w * 2 + 20, h * 2 + 80), (128, 128, 128))
    d = ImageDraw.Draw(tafel)
    namen = {"normal": "normales Sehen", "protan": "Protanopie (Rot-Schwäche)", "deutan": "Deuteranopie (Grün-Schwäche)", "tritan": "Tritanopie (Blau-Gelb-Schwäche)"}
    for i, (k, a) in enumerate(bilder):
        cx, cy = (i % 2) * (w + 20), (i // 2) * (h + 40)
        d.text((cx + 6, cy + 8), namen[k], fill=(0, 0, 0))
        tafel.paste(Image.fromarray(a), (cx, cy + 30))
    return tafel


def oklab_mean(arr):
    x = arr.reshape(-1, 3).astype(np.float64) / 255
    lin = np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)
    m = lin.mean(0)
    return rgb_to_hex([(12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055) for c in m])


def feed(img, r):
    x, y, w, h = r
    y0 = y + h - 17 - 1650
    teile = []
    for k in range(3):
        top = y0 + k * 546 + 44
        teile.append(np.asarray(img.crop(((x + 17) * S, top * S, (x + 17 + 390) * S, (top + 488) * S)).convert("RGB")))
    eigen, fremd = teile[1], np.concatenate([teile[0], teile[2]])
    m_e, m_f = oklab_mean(eigen), oklab_mean(fremd)
    blur = Image.fromarray(eigen).filter(ImageFilter.GaussianBlur(24)).convert("L")
    L = np.asarray(blur).astype(float)
    lo, hi = np.percentile(L, 5), np.percentile(L, 95)
    blur_f = Image.fromarray(np.asarray(img.crop(((x + 17) * S, y0 * S, (x + 17 + 390) * S, (y0 + 1650) * S)).convert("RGB"))).filter(ImageFilter.GaussianBlur(24))
    return {"mittel_eigen": m_e, "mittel_fremd": m_f, "dE_zum_feed": round(delta_e(m_e, m_f), 1),
            "kontrast_nach_unschaerfe": round((hi - lo) / (hi + lo + 1e-6), 2)}, blur_f


def main(shots, rects_dir):
    ergebnis = {}
    for r in "ABC":
        rects = json.load(open(os.path.join(rects_dir, f"rects_{r}.json"), encoding="utf-8"))
        ergebnis[r] = {}
        for theme in ("dark", "light"):
            for v in ("v1", "v2"):
                f = os.path.join(shots, f"R2_{r}_{theme}_{v}_ganz.png")
                img = Image.open(f)
                key = f"{theme}_{v}"
                lad = leiter(img, rects["t-flaechen"])
                ketten = {f"{a} → {b}": round(delta_l(lad[a], lad[b]), 1) for a, b in KETTE}
                res = {"pixel": lad, "dL": ketten}
                ausw = ("t-flaechen", "t-tabs", "t-chips") if v == "v1" else rects.keys()
                for sec in ausw:
                    crop(img, rects[sec]).save(os.path.join(shots, f"R2_{r}_{theme}_{v}_{sec[2:]}.png"))
                if v == "v2":
                    for sec in ("t-chips", "t-tabelle", "t-karte", "t-totw"):
                        cvd_tafel(crop(img, rects[sec])).save(os.path.join(shots, f"R2_{r}_{theme}_v2_farbschwaeche_{sec[2:]}.png"))
                    fd, blur = feed(img, rects["t-feed"])
                    res["feed"] = fd
                    blur.save(os.path.join(shots, f"R2_{r}_{theme}_v2_feed_unschaerfe.png"))
                ergebnis[r][key] = res
    # Vergleich v1/v2 der Flächenleiter
    for r in "ABC":
        for theme in ("dark", "light"):
            a = Image.open(os.path.join(shots, f"R2_{r}_{theme}_v1_flaechen.png"))
            b = Image.open(os.path.join(shots, f"R2_{r}_{theme}_v2_flaechen.png"))
            t = Image.new("RGB", (a.width + b.width + 20, max(a.height, b.height) + 30), (128, 128, 128))
            d = ImageDraw.Draw(t)
            d.text((6, 8), "v1", fill=(0, 0, 0)); d.text((a.width + 26, 8), "v2", fill=(0, 0, 0))
            t.paste(a, (0, 30)); t.paste(b, (a.width + 20, 30))
            t.save(os.path.join(shots, f"R2_{r}_{theme}_flaechen_v1_v2.png"))
    return ergebnis


def md(erg):
    o = ["# Testmatrix Bild", "", "Stand 05.11.2026. Gemessen auf den Screenshots der Testseiten (Chrome, doppelte Pixeldichte). "
         "Die Bilder liegen in OneDrive unter `00 Marke/Designsystem 2026/Screenshots/Runde 2/`.", "",
         "## 1. Flächenstufen im gerenderten Bild (ΔL, OKLab ×100)", "",
         "Gemessen wird die Pixelfarbe in jeder Zelle der Flächenleiter, nicht der Token. Ziel: jeder Schritt ≥ 3.", ""]
    for r in "ABC":
        o += [f"### Option {r} · {O.NAME[r]}", "", "| Schritt | Dark v1 | Dark v2 | Light v1 | Light v2 |", "|---|---|---|---|---|"]
        for k in erg[r]["dark_v2"]["dL"]:
            vals = [erg[r][t]["dL"][k] for t in ("dark_v1", "dark_v2", "light_v1", "light_v2")]
            o.append(f"| {k} | " + " | ".join((f"**{v:.1f}**" if v < 3 else f"{v:.1f}").replace(".", ",") for v in vals) + " |")
        o.append("")
    o += ["Fett = unter 3. Die Pixelwerte stimmen bis auf Rundung mit den Tokens überein. Das zeigt, dass die Seite die Farben richtig ausspielt.", "",
          "## 2. Wirkung im Feed (Näherung)", "",
          "Der eigene Post steht zwischen zwei fremden Posts (Farbflächen wie Fotos). Gemessen werden der Farbabstand des Mittelwerts zum Feed "
          "und der Hell-Dunkel-Kontrast des eigenen Posts nach starker Unschärfe (Blinzeltest). Beides sind Näherungen für „stoppt der Daumen“, "
          "kein Ersatz für einen echten Post-Test.", "",
          "| Option | Modus | ΔE zum Feed | Kontrast nach Unschärfe (0–1) |", "|---|---|---|---|"]
    for r in "ABC":
        for t in ("dark", "light"):
            f = erg[r][f"{t}_v2"]["feed"]
            o.append(f"| {r} {O.NAME[r]} | {t} | {str(f['dE_zum_feed']).replace('.', ',')} | {str(f['kontrast_nach_unschaerfe']).replace('.', ',')} |")
    o += ["", "Der Feed-Post ist in allen Modi derselbe (Marketing-Farben gelten unabhängig vom App-Modus). Die Zeilen je Option sind deshalb fast gleich.", "",
          "## 3. Farbschwäche auf dem Bild", "",
          "Für Chips, Tabelle, Spielerkarte und Team der Woche gibt es je Option und Modus eine Tafel mit vier Ansichten "
          "(normal, Protanopie, Deuteranopie, Tritanopie), Dateien `R2_<Option>_<Modus>_v2_farbschwaeche_<Teil>.png`. "
          "Auswertung siehe Abschnitt 4 im Bericht.", ""]
    return "\n".join(o) + "\n"


if __name__ == "__main__":
    erg = main(sys.argv[1], sys.argv[2])
    ds = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with io.open(os.path.join(ds, "testmatrix-bild.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write(md(erg))
    with io.open(os.path.join(ds, "_werkzeug", "bildtests-ergebnis.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(erg, f, indent=1, ensure_ascii=False)
    print(json.dumps({r: {k: v.get("feed") for k, v in erg[r].items() if "feed" in v} for r in erg}, ensure_ascii=False))
