"""Entpackt die PNG-Exporte aus export_<Option>.json und kopiert die SVGs dazu.
Aufruf: python -I logo_png.py <Ordner mit export_X.json> <Zielordner Logos>
"""
import base64
import json
import os
import shutil
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import optionen as O

DS = os.path.dirname(HIER)


def main(src, ziel):
    for r in "ABC":
        d = os.path.join(ziel, O.ORDNER[r])
        os.makedirs(os.path.join(d, "PNG"), exist_ok=True)
        os.makedirs(os.path.join(d, "SVG"), exist_ok=True)
        raw = open(os.path.join(src, f"export_{r}.json"), encoding="utf-8").read()
        data = json.loads(raw[raw.index("{"):raw.rindex("}") + 1])
        for name, url in data.items():
            with open(os.path.join(d, "PNG", name), "wb") as f:
                f.write(base64.b64decode(url.split(",", 1)[1]))
        for f in os.listdir(os.path.join(DS, O.ORDNER[r], "logo")):
            shutil.copy(os.path.join(DS, O.ORDNER[r], "logo", f), os.path.join(d, "SVG", f))
        print(r, len(data), "PNG")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
