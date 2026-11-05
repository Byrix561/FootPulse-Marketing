"""Schneidet Vorlagen aus Gruppenaufnahmen (vorlagen.html?nur=id1,id2,...; Vorlagen ohne Abstand nebeneinander).
Aufruf: python -I vorlagen_export.py <Option> <Ordner mit gruppe_<Option>_<n>.png> <Zielordner>
"""
import os
import sys

from PIL import Image

GRUPPEN = [
    [("reel-cover", 1080, 1920), ("reel-safe", 1080, 1920)],
    [("story", 1080, 1920), ("untertitel", 1080, 1920)],
    [("karussell-1", 1080, 1350), ("karussell-2", 1080, 1350), ("karussell-3", 1080, 1350)],
    [("x-bild", 1600, 900)],
    [("intro-1", 540, 960), ("intro-2", 540, 960), ("intro-3", 540, 960), ("outro-1", 540, 960), ("outro-2", 540, 960)],
]
NAMEN = {"reel-cover": "Reel-TikTok-Cover_1080x1920", "reel-safe": "Reel-Cover_mit_Safe-Zone_1080x1920", "story": "Story_SL_1080x1920",
         "untertitel": "Video-Untertitel_1080x1920", "karussell-1": "Karussell_BL_1_Titel_1080x1350", "karussell-2": "Karussell_BL_2_Inhalt_1080x1350",
         "karussell-3": "Karussell_BL_3_Ende_1080x1350", "x-bild": "X-Bild_PL_1600x900", "intro-1": "Intro_1", "intro-2": "Intro_2", "intro-3": "Intro_3",
         "outro-1": "Outro_1", "outro-2": "Outro_2"}


def main(opt, src, ziel):
    os.makedirs(ziel, exist_ok=True)
    for n, g in enumerate(GRUPPEN):
        img = Image.open(os.path.join(src, f"gruppe_{opt}_{n}.png"))
        x = 0
        for tid, w, h in g:
            img.crop((x, 0, x + w, h)).save(os.path.join(ziel, f"{opt}_{NAMEN[tid]}.png"))
            x += w
    print(opt, "ok")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
