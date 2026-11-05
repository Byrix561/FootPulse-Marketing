"""Testmatrix: rechnet alle Prüfungen für eine Palette und gibt Zeilen mit Messwert und Urteil zurück."""
import itertools
from farbe import wcag, apca, delta_e, delta_l, simulate, hex_to_rgb

# Schwellen. Quelle: WCAG 2.2 (1.4.3, 1.4.11) und APCA-Leitwerte (Bronze-Stufe, Stand 2024)
APCA_ZIEL = {"fliess": 75, "inhalt": 60, "gross": 45, "nichttext": 30}
STUFE_MIN = 3.0      # ΔL (OKLab × 100) zwischen benachbarten Flächenstufen, darunter wirkt es flach
STUFE_GUT = 4.0
CVD_MIN = 10.0       # ΔE (OKLab × 100), ab dem zwei Farben in der Simulation klar trennbar sind
SKALA_MIN = 8.0

TEXT_ROLLEN = [("textPrimary", "fliess"), ("textSecondary", "inhalt"), ("textTertiary", "inhalt"), ("textMuted", "gross")]
TEXT_GRUENDE = ["background", "surface", "surfaceElevated", "surfaceHover", "surfaceOverlay"]

STUFEN_KETTE = [
    ("background", "surfaceDeep"), ("surfaceDeep", "surface"), ("surface", "surfaceElevated"), ("surfaceElevated", "surfaceOverlay"),
    ("surfaceSunken", "background"), ("surface", "surfaceWarm"),
    ("tabTrack", "tabActive"), ("surface", "surfaceHover"), ("surfaceHover", "surfacePressed"), ("surface", "surfaceSelected"),
    ("surface", "surfaceDisabled"),
]


def _text(p, fg, bg, ziel):
    w, a = wcag(p[fg], p[bg]), apca(p[fg], p[bg])
    ok_w, ok_a = w >= 4.5, abs(a) >= APCA_ZIEL[ziel]
    return dict(art="Text", paar=f"{fg} auf {bg}", fg=p[fg], bg=p[bg], wcag=round(w, 2), apca=round(a, 1),
                ziel=f"≥4,5 · Lc {APCA_ZIEL[ziel]}", ok=ok_w and ok_a, ok_wcag=ok_w, ok_apca=ok_a)


def _gross(p, fg, bg, ziel_wcag=3.0, ziel_apca=45, art="Großtext"):
    w, a = wcag(p[fg], p[bg]), apca(p[fg], p[bg])
    ok_w, ok_a = w >= ziel_wcag, abs(a) >= ziel_apca
    return dict(art=art, paar=f"{fg} auf {bg}", fg=p[fg], bg=p[bg], wcag=round(w, 2), apca=round(a, 1),
                ziel=f"≥{str(ziel_wcag).replace('.', ',')} · Lc {ziel_apca}", ok=ok_w and ok_a, ok_wcag=ok_w, ok_apca=ok_a)


def pruefen(p, theme):
    rows = []
    # 1. Lesbarer Text
    for fg, ziel in TEXT_ROLLEN:
        for bg in TEXT_GRUENDE:
            rows.append(_text(p, fg, bg, ziel))
    for bg in ("background", "surface", "surfaceElevated", "accentMuted"):
        rows.append(_text(p, "accentText", bg, "inhalt"))
    for bg in ("background", "surface", "positiveMuted"):
        rows.append(_text(p, "ratingUp", bg, "inhalt"))
    if p["onRatingPoor"] != p["ratingInk"] and theme == "dark":  # A ab Runde 4: Website-Rot, bewusste Ausnahme (siehe V2_GRUENDE)
        rows.append(_gross(p, "ratingDown", "accentMuted", 4.5, 40, "Abwertung (Ausnahme)"))
    else:
        rows.append(_text(p, "ratingDown", "accentMuted", "inhalt"))
    for bg in ("background", "surface"):
        rows.append(_text(p, "goldText", bg, "inhalt"))
    rows.append(_text(p, "goldText", "goldMuted", "inhalt"))
    rows.append(_gross(p, "onAccent", "accent", 4.5, 60, "Button-Text"))
    for s in ("ratingElite", "ratingExcellent", "ratingGood", "ratingAverage"):
        rows.append(_text(p, "ratingInk", s, "inhalt"))
    rows.append(_text(p, "onRatingPoor", "ratingPoor", "inhalt"))
    for l in ("leagueBL", "leaguePL", "leagueSL"):
        rows.append(_text(p, "ratingInk", l, "inhalt"))
    # Marketing: kleiner Text auf Rot und große Schlagzeilen
    if theme == "dark":  # Marketing-Farben gelten unabhängig vom App-Modus, sie werden einmal geprüft
        rows.append(_text(p, "onMkRed", "mkRed", "inhalt"))
        rows.append(_gross(p, "onMkRedLarge", "mkRed", 3.0, 45, "Schlagzeile"))
        rows.append(_text(p, "mkPaper", "mkInk", "fliess"))
        rows.append(_gross(p, "mkRed", "mkInk", 3.0, 30, "Nicht-Text"))
        rows.append(_text(p, "accentText", "mkInk", "inhalt"))
    # 2. Nicht-Text (WCAG 1.4.11: 3 : 1)
    for fg, bg in (("borderStrong", "surface"), ("focusRing", "background"), ("focusRing", "surface"),
                   ("textFaint", "background"), ("accent", "background"), ("accent", "surface")):
        rows.append(_gross(p, fg, bg, 3.0, APCA_ZIEL["nichttext"], "Nicht-Text"))
    # 3. Flächenstufen
    for a, b in STUFEN_KETTE:
        dl, w = delta_l(p[a], p[b]), wcag(p[a], p[b])
        rows.append(dict(art="Stufe", paar=f"{a} → {b}", fg=p[b], bg=p[a], wcag=round(w, 2), apca=None, dl=round(dl, 1),
                         ziel=f"ΔL ≥{STUFE_MIN:.0f}", ok=dl >= STUFE_MIN,
                         urteil="deutlich" if dl >= STUFE_GUT else ("sichtbar" if dl >= STUFE_MIN else "flach")))
    # 4. Farbschwäche: Auf/Ab, Skala, Liga
    for kind in ("normal", "protan", "deutan", "tritan"):
        sim = (lambda h: h) if kind == "normal" else (lambda h, k=kind: simulate(h, k))
        up, dn = sim(p["ratingUp"]), sim(p["ratingDown"])
        de = delta_e(up, dn)
        rows.append(dict(art="Farbschwäche", paar=f"Auf ↔ Ab ({kind})", fg=up, bg=dn, wcag=None, apca=None, de=round(de, 1),
                         ziel=f"ΔE ≥{CVD_MIN:.0f}", ok=de >= CVD_MIN))
        skala = [sim(p[s]) for s in ("ratingPoor", "ratingAverage", "ratingGood", "ratingExcellent", "ratingElite")]
        namen = ["Poor", "Average", "Good", "Excellent", "Elite"]
        paare = [(namen[i], namen[j], delta_e(skala[i], skala[j])) for i, j in itertools.combinations(range(5), 2)]
        schw = min(paare, key=lambda x: x[2])
        rows.append(dict(art="Farbschwäche", paar=f"Noten-Skala, engstes Paar ({kind}): {schw[0]}–{schw[1]}", fg=None, bg=None,
                         wcag=None, apca=None, de=round(schw[2], 1), ziel=f"ΔE ≥{SKALA_MIN:.0f}", ok=schw[2] >= SKALA_MIN))
        liga = [sim(p[l]) for l in ("leagueBL", "leaguePL", "leagueSL", "accent", "gold")]
        ln = ["BL", "PL", "SL", "Rot", "Gold"]
        lp = [(ln[i], ln[j], delta_e(liga[i], liga[j])) for i, j in itertools.combinations(range(5), 2)]
        ls = min(lp, key=lambda x: x[2])
        rows.append(dict(art="Farbschwäche", paar=f"Liga-Akzente + Rot + Gold, engstes Paar ({kind}): {ls[0]}–{ls[1]}", fg=None, bg=None,
                         wcag=None, apca=None, de=round(ls[2], 1), ziel="ΔE ≥10", ok=ls[2] >= 10))
    # 5. OLED: dunkelster Kanal des Hintergrunds
    if theme == "dark":
        r, g, b = (round(c * 255) for c in hex_to_rgb(p["background"]))
        rows.append(dict(art="OLED", paar=f"background {p['background']} (R{r} G{g} B{b})", fg=None, bg=p["background"], wcag=None, apca=None,
                         ziel="kein Kanal unter 12", ok=min(r, g, b) >= 12))
    return rows


def zusammenfassung(rows):
    gesamt = len(rows)
    fail = [r for r in rows if not r["ok"]]
    return gesamt, fail
