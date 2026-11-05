"""Paletten der drei Richtungen, Version 1 und 2.

Jede Farbe ist in OKLCH notiert: (Helligkeit L 0–1, Buntheit C, Farbton H in Grad).
Gleiche Schritte in L wirken gleich groß. So lassen sich die Flächenstufen gezielt sichtbar setzen.
Version 2 überschreibt nur die Rollen, die in der Testmatrix v1 schwach waren (Begründung steht daneben).
"""
from farbe import oklch_to_hex

# Rollennamen wie in der App (Stand 04.11.2026) – unverändert übernommen
ROLLEN_APP = [
    "background", "surfaceSunken", "surface", "surfaceElevated", "surfaceOverlay", "surfaceWarm", "surfaceDeep",
    "borderSubtle", "border", "borderStrong",
    "textPrimary", "textSecondary", "textTertiary", "textMuted", "textFaint",
    "accent", "accentText", "accentDim", "accentMuted",
    "gold", "goldMuted", "pitchGreen", "pitchLine",
    "ratingUp", "positiveMuted", "ratingDown",
    "ratingElite", "ratingExcellent", "ratingGood", "ratingAverage", "ratingPoor",
]
# Neue Rollen (Vorschlag, für Burhans Kritik an Tabs und Zuständen)
ROLLEN_NEU = [
    "tabTrack", "tabActive", "surfaceHover", "surfacePressed", "surfaceSelected", "surfaceDisabled",
    "textDisabled", "focusRing", "onAccent", "goldText", "ratingInk",
]
ROLLEN_MARKETING = ["mkRed", "mkRedDeep", "mkInk", "mkPaper", "onMkRed", "onMkRedLarge"]
ROLLEN_LIGA = ["leagueBL", "leaguePL", "leagueSL"]
ALLE = ROLLEN_APP + ROLLEN_NEU + ROLLEN_MARKETING + ROLLEN_LIGA

BESTAND_DARK = {
    "background": "#050507", "surfaceSunken": "#09090D", "surface": "#111116", "surfaceElevated": "#191920",
    "surfaceOverlay": "#24242D", "surfaceWarm": "#151014", "surfaceDeep": "#0C0C11",
    "borderSubtle": "#1D1D24", "border": "#2A2A34", "borderStrong": "#3D3D49",
    "textPrimary": "#F2F2F5", "textSecondary": "#ABABB6", "textTertiary": "#93939F", "textMuted": "#82828E", "textFaint": "#666672",
    "accent": "#F02D3A", "accentText": "#FF5260", "accentDim": "#9F1D28", "accentMuted": "#381015",
    "gold": "#F1C15B", "goldMuted": "#302613", "pitchGreen": "#0B251B", "pitchLine": "#285442",
    "ratingUp": "#2ECC71", "positiveMuted": "#0D2618", "ratingDown": "#FF5260",
    "ratingElite": "#3B82F6", "ratingExcellent": "#18B981", "ratingGood": "#8BC34A", "ratingAverage": "#F2B84B", "ratingPoor": "#EF5B5B",
}


def K(L, C=0.0, H=0.0):
    return ("oklch", L, C, H)


# ------------------------------------------------------------------ A · Anzeigetafel
A_DARK = dict(
    background=K(.165, .010, 265), surfaceSunken=K(.140, .010, 265), surfaceDeep=K(.190, .010, 265),
    surface=K(.215, .011, 265), surfaceWarm=K(.215, .020, 20), surfaceElevated=K(.260, .012, 265), surfaceOverlay=K(.310, .013, 265),
    borderSubtle=K(.280, .011, 265), border=K(.350, .012, 265), borderStrong=K(.500, .012, 265),
    textPrimary=K(.965, .004, 265), textSecondary=K(.820, .008, 265), textTertiary=K(.740, .010, 265), textMuted=K(.700, .010, 265), textFaint=K(.520, .010, 265),
    accent=K(.620, .225, 25.5), accentText=K(.710, .180, 22), accentDim=K(.470, .170, 25), accentMuted=K(.290, .075, 22),
    gold=K(.830, .145, 85), goldMuted=K(.300, .050, 85), pitchGreen=K(.270, .045, 160), pitchLine=K(.420, .060, 160),
    ratingUp=K(.800, .160, 152), positiveMuted=K(.290, .055, 152), ratingDown="=accentText",
    ratingElite=K(.680, .150, 255), ratingExcellent=K(.750, .140, 165), ratingGood=K(.820, .150, 128), ratingAverage=K(.830, .130, 80), ratingPoor=K(.660, .190, 25),
    tabTrack=K(.190, .010, 265), tabActive=K(.310, .013, 265), surfaceHover=K(.250, .012, 265), surfacePressed=K(.290, .013, 265),
    surfaceSelected=K(.270, .050, 22), surfaceDisabled=K(.190, .008, 265), textDisabled=K(.500, .008, 265), focusRing=K(.920, .010, 265),
    onAccent=K(.990, 0, 0), goldText="=gold", ratingInk=K(.165, .010, 265),
    mkRed=K(.600, .235, 26), mkRedDeep=K(.420, .170, 25), mkInk=K(.165, .010, 265), mkPaper=K(.970, .004, 265), onMkRed=K(.165, .010, 265), onMkRedLarge=K(.990, 0, 0),
    leagueBL=K(.660, .160, 262), leaguePL=K(.850, .170, 128), leagueSL=K(.760, .120, 200),
)
A_LIGHT = dict(
    background=K(.940, .006, 265), surfaceSunken=K(.910, .007, 265), surfaceDeep=K(.925, .006, 265),
    surface=K(.970, .004, 265), surfaceWarm=K(.965, .014, 20), surfaceElevated=K(.995, .002, 265), surfaceOverlay=K(.885, .008, 265),
    borderSubtle=K(.870, .007, 265), border=K(.820, .008, 265), borderStrong=K(.620, .010, 265),
    textPrimary=K(.190, .012, 265), textSecondary=K(.400, .012, 265), textTertiary=K(.470, .012, 265), textMuted=K(.510, .012, 265), textFaint=K(.660, .010, 265),
    accent=K(.585, .220, 26), accentText=K(.530, .200, 26), accentDim=K(.740, .120, 22), accentMuted=K(.935, .030, 22),
    gold=K(.800, .150, 85), goldMuted=K(.940, .050, 90), pitchGreen=K(.880, .050, 158), pitchLine=K(.740, .070, 158),
    ratingUp=K(.530, .140, 152), positiveMuted=K(.930, .040, 152), ratingDown="=accentText",
    ratingElite="=A_DARK", ratingExcellent="=A_DARK", ratingGood="=A_DARK", ratingAverage="=A_DARK", ratingPoor="=A_DARK",
    tabTrack=K(.910, .007, 265), tabActive=K(.995, .002, 265), surfaceHover=K(.945, .006, 265), surfacePressed=K(.920, .007, 265),
    surfaceSelected=K(.930, .035, 22), surfaceDisabled=K(.935, .004, 265), textDisabled=K(.620, .008, 265), focusRing=K(.190, .012, 265),
    onAccent=K(.990, 0, 0), goldText=K(.560, .120, 75), ratingInk=K(.165, .010, 265),
    mkRed="=A_DARK", mkRedDeep="=A_DARK", mkInk="=A_DARK", mkPaper="=A_DARK", onMkRed="=A_DARK", onMkRedLarge="=A_DARK",
    leagueBL=K(.520, .170, 262), leaguePL=K(.560, .150, 135), leagueSL=K(.540, .100, 205),
)

# ------------------------------------------------------------------ B · Messgerät
B_DARK = dict(
    background=K(.190, .005, 250), surfaceSunken=K(.165, .005, 250), surfaceDeep=K(.212, .005, 250),
    surface=K(.235, .006, 250), surfaceWarm=K(.235, .014, 30), surfaceElevated=K(.275, .006, 250), surfaceOverlay=K(.320, .007, 250),
    borderSubtle=K(.300, .006, 250), border=K(.360, .007, 250), borderStrong=K(.520, .008, 250),
    textPrimary=K(.955, .003, 250), textSecondary=K(.810, .005, 250), textTertiary=K(.740, .006, 250), textMuted=K(.705, .006, 250), textFaint=K(.540, .006, 250),
    accent=K(.635, .215, 27), accentText=K(.720, .170, 24), accentDim=K(.480, .160, 27), accentMuted=K(.300, .065, 24),
    gold=K(.800, .130, 80), goldMuted=K(.310, .045, 80), pitchGreen=K(.280, .030, 170), pitchLine=K(.430, .040, 170),
    ratingUp=K(.800, .120, 232), positiveMuted=K(.300, .045, 240), ratingDown="=accentText",
    ratingElite=K(.640, .160, 272), ratingExcellent=K(.740, .120, 210), ratingGood=K(.820, .130, 150), ratingAverage=K(.830, .120, 80), ratingPoor=K(.670, .180, 30),
    tabTrack=K(.165, .005, 250), tabActive=K(.320, .007, 250), surfaceHover=K(.265, .006, 250), surfacePressed=K(.300, .007, 250),
    surfaceSelected=K(.290, .040, 240), surfaceDisabled=K(.210, .004, 250), textDisabled=K(.510, .005, 250), focusRing=K(.760, .130, 240),
    onAccent=K(.990, 0, 0), goldText="=gold", ratingInk=K(.190, .005, 250),
    mkRed=K(.620, .225, 27), mkRedDeep=K(.300, .065, 24), mkInk=K(.190, .005, 250), mkPaper=K(.970, .006, 95), onMkRed=K(.190, .005, 250), onMkRedLarge=K(.990, 0, 0),
    leagueBL=K(.660, .160, 262), leaguePL=K(.850, .170, 128), leagueSL=K(.760, .120, 200),
)
B_LIGHT = dict(
    background=K(.965, .006, 95), surfaceSunken=K(.935, .007, 95), surfaceDeep=K(.950, .006, 95),
    surface=K(.990, .003, 95), surfaceWarm=K(.975, .012, 40), surfaceElevated=K(1.0, 0, 0), surfaceOverlay=K(.905, .006, 95),
    borderSubtle=K(.895, .006, 95), border=K(.840, .006, 95), borderStrong=K(.640, .008, 250),
    textPrimary=K(.200, .006, 250), textSecondary=K(.410, .008, 250), textTertiary=K(.480, .008, 250), textMuted=K(.520, .008, 250), textFaint=K(.680, .006, 250),
    accent=K(.590, .215, 27), accentText=K(.530, .200, 27), accentDim=K(.760, .110, 24), accentMuted=K(.945, .025, 24),
    gold=K(.790, .140, 80), goldMuted=K(.950, .045, 90), pitchGreen=K(.900, .040, 165), pitchLine=K(.760, .060, 165),
    ratingUp=K(.500, .130, 245), positiveMuted=K(.940, .030, 240), ratingDown="=accentText",
    ratingElite="=B_DARK", ratingExcellent="=B_DARK", ratingGood="=B_DARK", ratingAverage="=B_DARK", ratingPoor="=B_DARK",
    tabTrack=K(.935, .007, 95), tabActive=K(1.0, 0, 0), surfaceHover=K(.960, .006, 95), surfacePressed=K(.930, .007, 95),
    surfaceSelected=K(.945, .030, 240), surfaceDisabled=K(.950, .004, 95), textDisabled=K(.640, .006, 250), focusRing=K(.520, .170, 255),
    onAccent=K(.990, 0, 0), goldText=K(.560, .110, 75), ratingInk=K(.190, .005, 250),
    mkRed="=B_DARK", mkRedDeep="=B_DARK", mkInk="=B_DARK", mkPaper="=B_DARK", onMkRed="=B_DARK", onMkRedLarge="=B_DARK",
    leagueBL=K(.520, .170, 262), leaguePL=K(.560, .150, 135), leagueSL=K(.540, .100, 205),
)

# ------------------------------------------------------------------ C · Flutlicht
C_DARK = dict(
    background=K(.155, .010, 45), surfaceSunken=K(.130, .009, 45), surfaceDeep=K(.180, .011, 45),
    surface=K(.205, .012, 45), surfaceWarm=K(.215, .030, 25), surfaceElevated=K(.250, .013, 45), surfaceOverlay=K(.300, .014, 45),
    borderSubtle=K(.270, .012, 45), border=K(.340, .013, 45), borderStrong=K(.500, .014, 45),
    textPrimary=K(.950, .013, 85), textSecondary=K(.820, .016, 75), textTertiary=K(.745, .016, 70), textMuted=K(.705, .016, 65), textFaint=K(.520, .014, 55),
    accent=K(.655, .245, 28.5), accentText=K(.720, .190, 28), accentDim=K(.480, .180, 28), accentMuted=K(.300, .085, 27),
    gold=K(.850, .160, 88), goldMuted=K(.310, .055, 85), pitchGreen=K(.270, .050, 150), pitchLine=K(.430, .070, 150),
    ratingUp=K(.820, .180, 145), positiveMuted=K(.300, .060, 145), ratingDown="=accentText",
    ratingElite=K(.680, .150, 255), ratingExcellent=K(.750, .140, 165), ratingGood=K(.820, .150, 128), ratingAverage=K(.830, .130, 80), ratingPoor=K(.660, .190, 25),
    tabTrack=K(.180, .011, 45), tabActive=K(.300, .014, 45), surfaceHover=K(.240, .013, 45), surfacePressed=K(.280, .014, 45),
    surfaceSelected=K(.270, .060, 27), surfaceDisabled=K(.180, .008, 45), textDisabled=K(.500, .010, 50), focusRing=K(.950, .013, 85),
    onAccent=K(.155, .010, 45), goldText="=gold", ratingInk=K(.155, .010, 45),
    mkRed=K(.655, .245, 28.5), mkRedDeep=K(.400, .160, 27), mkInk=K(.155, .010, 45), mkPaper=K(.950, .013, 85), onMkRed=K(.155, .010, 45), onMkRedLarge=K(.155, .010, 45),
    leagueBL=K(.660, .160, 262), leaguePL=K(.850, .170, 128), leagueSL=K(.760, .120, 200),
)
C_LIGHT = dict(
    background=K(.945, .014, 85), surfaceSunken=K(.915, .016, 82), surfaceDeep=K(.930, .015, 84),
    surface=K(.972, .010, 85), surfaceWarm=K(.955, .025, 40), surfaceElevated=K(.993, .005, 85), surfaceOverlay=K(.890, .016, 80),
    borderSubtle=K(.880, .016, 80), border=K(.820, .018, 75), borderStrong=K(.600, .020, 50),
    textPrimary=K(.190, .012, 45), textSecondary=K(.390, .016, 45), textTertiary=K(.460, .016, 45), textMuted=K(.500, .016, 45), textFaint=K(.650, .016, 50),
    accent=K(.600, .235, 28), accentText=K(.530, .210, 28), accentDim=K(.740, .130, 27), accentMuted=K(.925, .040, 30),
    gold=K(.820, .160, 85), goldMuted=K(.930, .060, 90), pitchGreen=K(.870, .060, 150), pitchLine=K(.720, .080, 150),
    ratingUp=K(.520, .150, 145), positiveMuted=K(.920, .050, 145), ratingDown="=accentText",
    ratingElite="=C_DARK", ratingExcellent="=C_DARK", ratingGood="=C_DARK", ratingAverage="=C_DARK", ratingPoor="=C_DARK",
    tabTrack=K(.915, .016, 82), tabActive=K(.993, .005, 85), surfaceHover=K(.945, .014, 85), surfacePressed=K(.915, .016, 82),
    surfaceSelected=K(.925, .040, 30), surfaceDisabled=K(.935, .010, 85), textDisabled=K(.620, .014, 50), focusRing=K(.190, .012, 45),
    onAccent=K(.155, .010, 45), goldText=K(.560, .120, 75), ratingInk=K(.155, .010, 45),
    mkRed="=C_DARK", mkRedDeep="=C_DARK", mkInk="=C_DARK", mkPaper="=C_DARK", onMkRed="=C_DARK", onMkRedLarge="=C_DARK",
    leagueBL=K(.520, .170, 262), leaguePL=K(.560, .150, 135), leagueSL=K(.540, .100, 205),
)

V1 = {"A": {"dark": A_DARK, "light": A_LIGHT}, "B": {"dark": B_DARK, "light": B_LIGHT}, "C": {"dark": C_DARK, "light": C_LIGHT}}

# Version 2: nur Änderungen gegenüber v1. Wird nach der Testmatrix v1 befüllt.
V2_AENDERUNGEN = {"A": {"dark": {}, "light": {}}, "B": {"dark": {}, "light": {}}, "C": {"dark": {}, "light": {}}}
V2_GRUENDE = {}


def aufloesen(spec_by_theme, richtung):
    """Wandelt OKLCH-Angaben in Hex um und löst Verweise auf (='=andereRolle' oder '=X_DARK')."""
    out = {}
    for theme in ("dark", "light"):
        spec = spec_by_theme[theme]
        res = {}
        def val(rolle, seen=()):
            v = spec[rolle]
            if isinstance(v, tuple):
                return oklch_to_hex(v[1], v[2], v[3])
            if isinstance(v, str) and v.startswith("=") and v.endswith("_DARK"):
                return out["dark"][rolle]
            if isinstance(v, str) and v.startswith("="):
                return val(v[1:], seen + (rolle,))
            return v
        for r in ALLE:
            res[r] = val(r)
        out[theme] = res
    return out


def palette(richtung, version=2):
    spec = {t: dict(V1[richtung][t]) for t in ("dark", "light")}
    if version >= 2:
        for t in ("dark", "light"):
            spec[t].update(V2_AENDERUNGEN[richtung][t])
    return aufloesen(spec, richtung)
