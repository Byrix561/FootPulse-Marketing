"""Paletten Version 2: Korrekturen nach Testmatrix v1. Jede Änderung hat einen Grund (V2_GRUENDE)."""
from paletten import K, A_DARK, A_LIGHT, B_DARK, B_LIGHT, C_DARK, C_LIGHT


def _v2_dark(base, hue, chroma, warm_h, txt_c, txt_h, lv, red, extra):
    d = dict(base)
    sk, bg, dp, sf, el, ov = lv
    d.update(surfaceSunken=K(sk, chroma, hue), background=K(bg, chroma, hue), surfaceDeep=K(dp, chroma, hue),
             surface=K(sf, chroma * 1.05, hue), surfaceWarm=K(sf + .036, .028, warm_h), surfaceElevated=K(el, chroma * 1.1, hue),
             surfaceOverlay=K(ov, chroma * 1.15, hue),
             borderSubtle=K(sf + .070, chroma, hue), border=K(sf + .140, chroma, hue), borderStrong=K(sf + .370, chroma, hue),
             textPrimary=K(.965, txt_c * .5, txt_h), textSecondary=K(.855, txt_c, txt_h), textTertiary=K(.815, txt_c, txt_h),
             textMuted=K(.735, txt_c, txt_h), textFaint=K(.590, txt_c, txt_h),
             tabTrack=K(dp, chroma, hue), tabActive=K(ov, chroma * 1.15, hue), surfaceHover=K(sf + .038, chroma, hue),
             surfacePressed=K(sf + .075, chroma, hue), surfaceDisabled=K(sf - .040, chroma * .8, hue), textDisabled=K(.540, txt_c * .6, txt_h))
    rL, rC, rH = red
    d.update(accent=K(rL, rC, rH), accentText=K(.805, .130, rH - 4), accentDim=K(.470, .165, rH), accentMuted=K(.255, .075, rH - 3),
             surfaceSelected=K(sf + .055, .055, rH - 3), mkRed=K(rL, rC, rH), mkRedDeep=K(.400, .160, rH),
             ratingUp=K(.900, .130, 190), positiveMuted=K(.275, .050, 190),
             ratingPoor=K(.860, .140, 28), ratingAverage=K(.780, .140, 60), ratingGood=K(.940, .140, 125),
             ratingExcellent=K(.940, .140, 195), ratingElite=K(.780, .140, 255),
             leagueBL=K(.765, .130, 275), leaguePL=K(.920, .170, 150), leagueSL=K(.880, .120, 300))
    d.update(extra)
    return d


def _v2_light(base, hue, chroma, warm_h, txt_h, red, extra):
    d = dict(base)
    d.update(surfaceSunken=K(.865, chroma, hue), background=K(.900, chroma, hue), surfaceDeep=K(.934, chroma * .8, hue),
             surface=K(.967, chroma * .6, hue), surfaceWarm=K(.930, .026, warm_h), surfaceElevated=K(1.0, 0, 0),
             surfaceOverlay=K(.935, chroma, hue),
             borderSubtle=K(.860, chroma, hue), border=K(.800, chroma, hue), borderStrong=K(.560, chroma * 1.2, hue),
             textPrimary=K(.190, .012, txt_h), textSecondary=K(.375, .012, txt_h), textTertiary=K(.425, .012, txt_h),
             textMuted=K(.465, .012, txt_h), textFaint=K(.580, .010, txt_h),
             tabTrack=K(.925, chroma, hue), tabActive=K(1.0, 0, 0), surfaceHover=K(.932, chroma, hue), surfacePressed=K(.893, chroma, hue),
             surfaceDisabled=K(.930, chroma * .5, hue), textDisabled=K(.600, .006, txt_h))
    rL, rC, rH = red
    d.update(accent=K(rL, rC, rH), accentText=K(.500, .200, rH), accentDim=K(.740, .120, rH - 3), accentMuted=K(.925, .040, rH - 3),
             surfaceSelected=K(.925, .045, rH - 3), ratingUp=K(.420, .110, 210), positiveMuted=K(.920, .035, 210),
             goldText=K(.490, .105, 72), goldMuted=K(.925, .060, 88),
             leagueBL="=X_DARK", leaguePL="=X_DARK", leagueSL="=X_DARK")
    d.update(extra)
    return d


A2_DARK = _v2_dark(A_DARK, 265, .010, 20, .008, 265, (.135, .170, .205, .240, .285, .335), (.585, .225, 26), dict(
    onAccent=K(.990, 0, 0), onMkRed=K(.990, 0, 0), onMkRedLarge=K(.990, 0, 0), focusRing=K(.930, .010, 265),
    ratingInk=K(.170, .010, 265), mkInk=K(.170, .010, 265),
    # Runde 4 (Burhans Wahl A): Note Poor = Sofascore-Rot, Abwertung = Website-Rot. Zwei verschiedene Rottöne.
    # Noten-Skala: wie heute in der App (Burhan, 05.11.), nur Poor ist das Sofascore-Rot
    ratingDown="#FF5260", accentText="#FF5260", ratingElite="#3B82F6", ratingExcellent="#18B981", ratingGood="#8BC34A", ratingAverage="#F2B84B", ratingPoor="#DC0C00", onRatingPoor="=onAccent"))
A2_LIGHT = _v2_light(A_LIGHT, 265, .008, 20, 265, (.570, .220, 26), dict(
    onAccent=K(.990, 0, 0), ratingElite="#3B82F6", ratingExcellent="#18B981", ratingGood="#8BC34A", ratingAverage="#F2B84B", ratingPoor="#DC0C00", onRatingPoor="=onAccent"))

B2_DARK = _v2_dark(B_DARK, 250, .005, 30, .005, 250, (.160, .195, .230, .265, .310, .360), (.578, .215, 27), dict(
    ratingUp=K(.880, .090, 232), positiveMuted=K(.290, .045, 240), surfaceSelected=K(.320, .045, 240),
    onAccent=K(.990, 0, 0), onMkRed=K(.990, 0, 0), onMkRedLarge=K(.990, 0, 0), focusRing=K(.790, .120, 240),
    ratingInk=K(.195, .005, 250), mkInk=K(.195, .005, 250), mkRedDeep=K(.300, .065, 24)))
B2_LIGHT = _v2_light(B_LIGHT, 95, .006, 40, 250, (.575, .215, 27), dict(
    ratingUp=K(.420, .120, 245), positiveMuted=K(.925, .035, 240), surfaceSelected=K(.925, .035, 240),
    surface=K(.967, .004, 95), onAccent=K(.990, 0, 0), focusRing=K(.500, .170, 255)))

C2_DARK = _v2_dark(C_DARK, 45, .008, 25, .016, 80, (.140, .175, .210, .245, .290, .340), (.585, .225, 29), dict(
    textPrimary=K(.955, .014, 85), accentText=K(.810, .130, 30), onAccent=K(.990, 0, 0), mkRed=K(.560, .220, 29), onMkRed=K(.960, .012, 85),
    onMkRedLarge=K(.955, .014, 85), focusRing=K(.955, .014, 85), ratingInk=K(.175, .008, 45), mkInk=K(.175, .008, 45),
    mkPaper=K(.950, .016, 85), gold=K(.825, .150, 86), ratingUp=K(.905, .140, 185), positiveMuted=K(.280, .060, 150)))
C2_LIGHT = _v2_light(C_LIGHT, 85, .016, 40, 45, (.580, .225, 29), dict(
    surfaceElevated=K(1.0, 0, 0), tabActive=K(1.0, 0, 0), onAccent=K(.990, 0, 0), surface=K(.967, .010, 85), focusRing=K(.190, .012, 45),
    ratingUp=K(.420, .110, 205), accentText=K(.500, .205, 29), gold=K(.820, .160, 85)))

V2 = {"A": {"dark": A2_DARK, "light": A2_LIGHT}, "B": {"dark": B2_DARK, "light": B2_LIGHT}, "C": {"dark": C2_DARK, "light": C2_LIGHT}}

V2_GRUENDE = [
    ("Flächenstufen", "Alle Dunkel-Stufen auf mindestens 3,5 Punkte Abstand gezogen (v1: 2,2–2,7). Der Hintergrund bleibt über Kanalwert 12 (OLED). Im Hell-Modus ist die Seite jetzt grau (L 0,905) und Karten sind weiß. So gibt es genug Abstand nach oben."),
    ("Rote Schrift", "accentText heller (L 0,805 bei leicht weniger Buntheit), weil APCA Lc 60 bei v1 nicht erreicht wurde. accentMuted dunkler, damit rote Schrift auch auf dem Chip-Grund trägt."),
    ("Roter Button", "Button-Rot in allen drei Richtungen so dunkel (L 0,58–0,60), dass weiße Schrift 4,5 : 1 erreicht. C nutzt für Plakate dasselbe tiefe Rot mit Kreide-Schrift (Lc 72). Ein helleres Signalrot mit schwarzer Schrift (v2-Entwurf, L 0,685) wirkte korallig und erreichte nur Lc 47, deshalb verworfen."),
    ("Noten-Skala", "Per Rechnung über 60 000 Kombinationen gesucht: Jedes Paar der fünf Stufen hat jetzt in allen vier Sehweisen ΔE ≥ 9,8 (v1: 2,1). Dafür ist die Helligkeit nicht mehr stufenweise ansteigend. Die Zahl steht deshalb immer im Chip."),
    ("Auf und Ab", "Aufwertung ist jetzt Türkis statt Grün und deutlich heller (Dunkel) bzw. dunkler (Hell) als Abwertung. So bleibt sie auch bei Rot-Grün-Schwäche unterscheidbar (ΔE ≥ 10). Pfeil und Vorzeichen sind trotzdem Pflicht."),
    ("Liga-Akzente", "Gesucht per Rechnung über alle Farbtöne: BL Blauviolett, PL Mint, SL Flieder. Mehr als ΔE 10,8 ist mit Gold und Rot im Vergleich nicht erreichbar, deshalb Schwelle 10. Liga-Farben sind Flächen mit dunkler Schrift, keine Schriftfarben, und stehen immer neben dem Kürzel."),
    ("Rot für Schlecht (nur A, Runde 4)", "Burhans Wunsch: zwei echte Rottöne, kein Rosa. Note Poor ist das Rot von Sofascore (#DC0C00) mit weißer Zahl: 5,0 : 1, Lc 76. Abwertung ist das Rot der Website (#FF5260, wie heute in der App) auf dunklem Rot-Chip: 5,1 : 1, aber nur Lc 41. Das ist eine bewusste Ausnahme: WCAG hält, APCA verlangt für kleine Schrift Lc 60. Der Chip trägt deshalb immer Pfeil und Minus, fett. Im Hell-Modus bleibt Abwertung #BB081A (6,0 : 1, Lc 74)."),
    ("Rote Schrift (nur A, Runde 4)", "accentText ist im Dark-Modus wieder das Website-Rot #FF5260 statt Rosa #FFA29F (Burhan: das Website-Rot passt). 6,1 : 1 auf dem Hintergrund, aber nur Lc 44. Rote Schrift deshalb nur halbfett ab 14 px und für kurze Wörter, nie für Fließtext."),
    ("Noten-Skala (nur A, Runde 4)", "Burhans Wahl: die Noten-Farben wie heute in der App (Elite #3B82F6, Excellent #18B981, Good #8BC34A, Average #F2B84B), nur Poor ist das Sofascore-Rot #DC0C00 mit weißer Zahl. Bewusste Ausnahme: Bei Rot-Grün-Schwäche liegen Good und Average dicht beieinander (Protan ΔE 1,0), und die dunkle Zahl auf Elite erreicht nur Lc 40. Die Zahl steht deshalb immer im Chip."),
    ("Marketing", "Rote Wörter auf Schwarz nutzen accentText, nicht mkRed. mkRed ist nur Fläche."),
]
