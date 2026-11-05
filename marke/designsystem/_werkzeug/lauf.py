"""Schnelllauf: druckt Bestanden/Gesamt je Palette und die Fehler von v2."""
import sys
sys.path.insert(0, ".")
sys.stdout.reconfigure(encoding="utf-8")
from paletten import aufloesen, V1
from paletten_v2 import V2
from matrix import pruefen, zusammenfassung


def palette(r, v):
    q = V1 if v == 1 else V2
    return aufloesen({t: dict(q[r][t]) for t in ("dark", "light")}, r)


if __name__ == "__main__":
    for v in (1, 2):
        for R in "ABC":
            p = palette(R, v)
            for t in ("dark", "light"):
                rows = pruefen(p[t], t)
                g, f = zusammenfassung(rows)
                print(f"== v{v} {R} {t}: {g - len(f)}/{g} ok")
                if v == 2:
                    for r in f:
                        print("   FAIL", r["art"], r["paar"], r.get("wcag"), r.get("apca"), r.get("dl", ""), r.get("de", ""), r["ziel"])
