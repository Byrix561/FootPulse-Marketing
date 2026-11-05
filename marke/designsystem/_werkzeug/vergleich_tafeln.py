"""Setzt die Beispiele der drei Optionen zu Vergleichstafeln A | B | C zusammen.
Aufruf: python -I vergleich_tafeln.py <Ordner mit bsp_X.png und bsp_rects_X.json> <Zielordner>
"""
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

S = 2
NAMEN = {"A": "A · Anzeigetafel", "B": "B · Messgerät", "C": "C · Flutlicht"}
TITEL = {
    "ex-profil-dark": "App · Spielerprofil (Dark)", "ex-profil-light": "App · Spielerprofil (Light)", "ex-rangliste": "App · Bewegungen der Woche",
    "ex-web": "Website · Startseite mit Warteliste", "ex-homescreen": "Handy · App-Icon auf dem Homescreen", "ex-konten": "Social · Profilbilder der vier Konten",
    "ex-abwertung": "Post 4:5 · Bundesliga (DE) · Abwertung", "ex-vergleich": "Post 4:5 · FootPulse (EN) · Erklär-Post",
    "ex-totw": "Post 4:5 · Süper Lig (TR) · Team der Woche", "ex-banter": "Post 1:1 · Premier League (EN) · Banter",
    "ex-youtube": "YouTube-Thumbnail 16:9", "ex-umfrage": "Story 9:16 · Umfrage",
}
TAFELN = [
    ("1_App-Screens", ["ex-profil-dark", "ex-profil-light", "ex-rangliste"], "quer"),
    ("2_Website", ["ex-web"], "hoch"),
    ("3_Icon-und-Konten", ["ex-homescreen", "ex-konten"], "quer"),
    ("4_Posts", ["ex-abwertung", "ex-vergleich", "ex-totw", "ex-banter"], "quer"),
    ("5_Video-und-Story", ["ex-youtube", "ex-umfrage"], "quer"),
]
F = "C:/Windows/Fonts/arialbd.ttf"


def font(n):
    try:
        return ImageFont.truetype(F, n)
    except OSError:
        return ImageFont.load_default()


def main(src, ziel):
    os.makedirs(ziel, exist_ok=True)
    teile = {}
    for r in "ABC":
        rects = json.load(open(os.path.join(src, f"bsp_rects_{r}.json"), encoding="utf-8"))
        img = Image.open(os.path.join(src, f"bsp_{r}.png")).convert("RGB")
        d = os.path.join(ziel, "Einzeln", f"Option {r}")
        os.makedirs(d, exist_ok=True)
        for k, (x, y, w, h) in rects.items():
            t = img.crop((x * S, y * S, (x + w) * S, (y + h) * S))
            t.save(os.path.join(d, f"{r}_{k[3:]}.png"))
            teile[(r, k)] = t
    gap, pad, kopf = 40, 60, 90
    for name, ids, art in TAFELN:
        zeilen = []
        for k in ids:
            ims = [teile[(r, k)] for r in "ABC"]
            if art == "quer":
                w = sum(i.width for i in ims) + gap * 2
                h = max(i.height for i in ims)
                z = Image.new("RGB", (w, h + 70), (52, 52, 56))
                dr = ImageDraw.Draw(z)
                x = 0
                for r, i in zip("ABC", ims):
                    dr.text((x, 8), NAMEN[r], font=font(36), fill=(235, 235, 235))
                    z.paste(i, (x, 70))
                    x += i.width + gap
            else:
                w = max(i.width for i in ims)
                h = sum(i.height + 70 for i in ims) + gap * 2
                z = Image.new("RGB", (w, h), (52, 52, 56))
                dr = ImageDraw.Draw(z)
                y = 0
                for r, i in zip("ABC", ims):
                    dr.text((0, y + 8), NAMEN[r], font=font(36), fill=(235, 235, 235))
                    z.paste(i, (0, y + 70))
                    y += i.height + 70 + gap
            zeilen.append((TITEL[k], z))
        W = max(z.width for _, z in zeilen) + pad * 2
        H = sum(z.height + kopf + gap for _, z in zeilen) + pad * 2
        t = Image.new("RGB", (W, H), (36, 36, 40))
        dr = ImageDraw.Draw(t)
        y = pad
        for titel, z in zeilen:
            dr.text((pad, y + 20), titel, font=font(48), fill=(255, 255, 255))
            t.paste(z, (pad, y + kopf))
            y += z.height + kopf + gap
        if max(t.size) > 6000:
            f = 6000 / max(t.size)
            t = t.resize((int(t.width * f), int(t.height * f)), Image.LANCZOS)
        t.save(os.path.join(ziel, f"Vergleich_{name}.jpg"), quality=88)
        print(name, t.size)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
