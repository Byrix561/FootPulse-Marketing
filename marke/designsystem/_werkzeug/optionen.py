"""Alles, was eine Option außer Farbe ausmacht: Name, Schriften, Größen, Abstände, Radien, Formen."""

ORDNER = {"A": "option-a-anzeigetafel", "B": "option-b-messgeraet", "C": "option-c-flutlicht"}
NAME = {"A": "Anzeigetafel", "B": "Messgerät", "C": "Flutlicht"}
KURZ = {
    "A": "Wie eine TV-Einblendung: kantig, aufrecht, Zahlen groß. Rot ist der Balken, der sagt: hier passiert etwas.",
    "B": "Wie ein Messinstrument: ruhig, genau, Raster und Haarlinien. Rot ist nur der Messpunkt.",
    "C": "Wie die Kurve: Plakat, Doppelhalter, Choreo. Rot flutet ganze Flächen, dazu Kreide statt kühlem Weiß.",
}

SCHRIFT = {
    "A": {
        "display": {"family": "Barlow Condensed", "weights": [700, 800], "css": "'Barlow Condensed', 'Arial Narrow', sans-serif"},
        "text": {"family": "Barlow", "weights": [400, 500, 600], "css": "'Barlow', system-ui, sans-serif"},
        "zahl": {"family": "Barlow Condensed", "weights": [600, 700, 800], "css": "'Barlow Condensed', 'Arial Narrow', sans-serif", "feature": "tabular-nums"},
        "label": {"family": "Barlow Condensed", "weights": [600], "css": "'Barlow Condensed', sans-serif", "case": "upper", "tracking": "0.06em"},
        "google": "family=Barlow+Condensed:wght@500;600;700;800&family=Barlow:wght@400;500;600",
    },
    "B": {
        "display": {"family": "Archivo", "weights": [700, 800], "css": "'Archivo', system-ui, sans-serif", "stretch": "75%"},
        "text": {"family": "Archivo", "weights": [400, 500, 600], "css": "'Archivo', system-ui, sans-serif", "stretch": "100%"},
        "zahl": {"family": "Archivo", "weights": [600, 700], "css": "'Archivo', system-ui, sans-serif", "feature": "tabular-nums", "stretch": "80%"},
        "label": {"family": "IBM Plex Mono", "weights": [500], "css": "'IBM Plex Mono', ui-monospace, monospace", "case": "upper", "tracking": "0.08em"},
        "google": "family=Archivo:wdth,wght@62..125,400..800&family=IBM+Plex+Mono:wght@400;500;600",
    },
    "C": {
        "display": {"family": "Big Shoulders Display", "weights": [800, 900], "css": "'Big Shoulders Display', Impact, sans-serif", "hinweis": "nur Schlagzeilen, keine gleich breiten Ziffern"},
        "text": {"family": "Sofia Sans Condensed", "weights": [400, 600], "css": "'Sofia Sans Condensed', 'Arial Narrow', sans-serif"},
        "zahl": {"family": "Sofia Sans Condensed", "weights": [700, 800], "css": "'Sofia Sans Condensed', 'Arial Narrow', sans-serif", "feature": "tabular-nums"},
        "label": {"family": "Sofia Sans Condensed", "weights": [800], "css": "'Sofia Sans Condensed', sans-serif", "case": "upper", "tracking": "0.08em"},
        "google": "family=Big+Shoulders+Display:wght@700;800;900&family=Sofia+Sans+Condensed:wght@400;600;700;800",
    },
}

# Größenskala Web/App in px (Schriftgröße / Zeilenhöhe / Gewicht / Rolle)
GROESSEN = {
    "A": [("display", 68, 64, 800, "display"), ("h1", 44, 44, 800, "display"), ("h2", 32, 34, 700, "display"), ("h3", 24, 28, 700, "display"),
          ("title", 20, 24, 600, "text"), ("body", 16, 24, 400, "text"), ("small", 14, 20, 500, "text"), ("label", 13, 16, 600, "label"),
          ("caption", 12, 16, 500, "text"), ("micro", 10, 12, 600, "label"), ("ovr", 56, 52, 800, "zahl"), ("stat", 18, 20, 700, "zahl")],
    "B": [("display", 64, 62, 800, "display"), ("h1", 40, 42, 700, "display"), ("h2", 30, 34, 700, "display"), ("h3", 22, 28, 600, "text"),
          ("title", 18, 24, 600, "text"), ("body", 16, 24, 400, "text"), ("small", 14, 20, 400, "text"), ("label", 12, 16, 500, "label"),
          ("caption", 12, 16, 400, "text"), ("micro", 10, 12, 500, "label"), ("ovr", 48, 48, 700, "zahl"), ("stat", 16, 20, 600, "zahl")],
    "C": [("display", 76, 68, 900, "display"), ("h1", 50, 46, 900, "display"), ("h2", 36, 34, 800, "display"), ("h3", 26, 26, 800, "display"),
          ("title", 20, 24, 600, "text"), ("body", 17, 24, 400, "text"), ("small", 15, 20, 400, "text"), ("label", 13, 16, 800, "label"),
          ("caption", 13, 16, 600, "text"), ("micro", 11, 12, 800, "label"), ("ovr", 58, 52, 800, "zahl"), ("stat", 18, 20, 700, "zahl")],
}
# Social-Skala in px bei 1080 px Breite
SOCIAL = {
    "A": [("hero-zahl", 360, 300), ("schlagzeile", 120, 108), ("unterzeile", 56, 60), ("text", 40, 50), ("fuss", 28, 34), ("untertitel", 52, 60)],
    "B": [("hero-zahl", 300, 270), ("schlagzeile", 96, 100), ("unterzeile", 48, 56), ("text", 38, 50), ("fuss", 28, 34), ("untertitel", 50, 60)],
    "C": [("hero-zahl", 380, 310), ("schlagzeile", 160, 136), ("unterzeile", 56, 60), ("text", 42, 52), ("fuss", 30, 34), ("untertitel", 56, 62)],
}

ABSTAND = [("space-1", 4), ("space-2", 8), ("space-3", 12), ("space-4", 16), ("space-5", 20), ("space-6", 24), ("space-8", 32), ("space-10", 40), ("space-12", 48), ("space-16", 64)]

RADIUS = {
    "A": [("radius-xs", 2, "Chips, Tags"), ("radius-sm", 4, "Buttons, Eingabefelder"), ("radius-md", 6, "Karten, Tabellen"), ("radius-lg", 8, "Dialoge"),
          ("cut-sm", 8, "Angeschnittene Ecke klein (Buttons, Chips mit Aktion)"), ("cut-md", 14, "Angeschnittene Ecke Spielerkarte"), ("cut-lg", 28, "Angeschnittene Ecke Post-Rahmen")],
    "B": [("radius-xs", 4, "Tags"), ("radius-sm", 8, "Buttons, Eingabefelder"), ("radius-md", 12, "Karten"), ("radius-lg", 16, "Dialoge, Sheets"), ("radius-pill", 999, "Chips")],
    "C": [("radius-xs", 0, "Fast alles: harte Kanten"), ("radius-sm", 2, "Eingabefelder (Fokus sichtbar)"), ("radius-md", 0, "Karten"), ("radius-lg", 4, "Dialoge")],
}

LINIE = {"A": "1 px Linien, 2 px für aktiv. Akzentbalken 4 px.", "B": "1 px Haarlinien, Raster sichtbar. Akzent als Punkt 6–8 px.", "C": "2 px Linien, 6–10 px Balken. Keine Haarlinien."}
BEWEGUNG = {
    "A": "Schnell und hart wie eine Einblendung: 160 ms ein (ease-out), 120 ms aus. Zahlen zählen hoch (400 ms). Wischen von links nach rechts.",
    "B": "Ruhig: 200 ms Überblendung, Zahlen tippen Ziffer für Ziffer um (Messgerät). Keine Federn.",
    "C": "Laut: Schnitte statt Überblendung, 2–3 Frames Rot-Blitz beim Wechsel, Text schlägt mit 6 % Überschwung ein. In der App gedämpft: 180 ms.",
}

# Alte Radien 4–26 → neue Werte (für die Umbau-Tabelle)
RADIUS_ALT = [4, 8, 12, 16, 20, 26]
