# Entscheidungsvorlage: Designsystem 2026

Für: Burhan · Stand: 05.11.2026 · Vorbereitet vom Marketing-Chat

## Entscheidung (05.11.2026)

Burhan wählt **Option A „Anzeigetafel“**, mit diesen Änderungen:

- **Noten-Farben (Rating):** Es gelten die **heutigen App-Farben**: Elite #3B82F6, Excellent #18B981, Good #8BC34A, Average #F2B84B, jeweils mit dunkler Zahl. Nur **Poor** ist das Rot von Sofascore (#DC0C00) mit weißer Zahl (5,0 : 1, Lc 76). Die A-Skala (Blau, Türkis, Hellgrün, Orange) ist damit verworfen. Bewusste Ausnahme: Bei Rot-Grün-Schwäche liegen Good und Average dicht beieinander (Protan ΔE 1,0), und die dunkle Zahl auf Elite erreicht nur Lc 40. Deshalb steht die Zahl immer im Chip.
- **Rot:** Abwertung und rote Schrift sind im Dark-Modus das **Website-Rot #FF5260** (wie heute). Es hat 6,1 : 1 auf dem Hintergrund, aber nur Lc 44. Rote Schrift steht deshalb nur halbfett ab 14 px und in kurzen Wörtern. Das Rosa aus A (#FFA29F) ist verworfen. Abwertung und Note Poor sind bewusst zwei verschiedene Rottöne. Im Hell-Modus bleibt rote Schrift #BB081A.
- **Messung A:** Dark 65/75, Light 65/69. Jeder Text besteht WCAG AA. Alle Ausnahmen betreffen nur den strengeren APCA-Test oder die Farbschwäche-Simulation und folgen aus den zwei Punkten oben.
- **Team der Woche:** Das TOTW in App und Website **bleibt im Aufbau, wie es ist**. Übernommen werden dort nur die Farben. Das TOTW in den Testseiten und Beispielen ist nur eine Farbprobe und soll nicht nachgebaut werden.
- **Beispiele:** Die Beispielseiten zeigen Farbe und Stil, nicht den Aufbau.
- **Aufbau der Seiten:** Den will Burhan später ändern. Karten und Symbole bleiben, wie sie in A sind.
- **Logo:** Vorerst bleibt das heutige Logo, das A-Logo liegt als Vorschlag bereit. Ein eigener Termin nur für das Logo folgt.
- **Übergabe an den Website-Builder:** `marke/designsystem/uebergabe-website/` (neu bauen mit `_werkzeug/uebergabe.py`). Fertig gepackt mit Vorschaubildern und heutigem Logo liegt sie in OneDrive: `00 Marke/Designsystem 2026/FootPulse_Designsystem_Website_Uebergabe.zip`.

Es gibt drei vollständige Optionen. Jede hat Farben für Dark und Light, eine Marketing-Erweiterung, Liga-Akzente, Schrift, Logo-System, Formensprache, Bausteine und Vorlagen. Alle drei nutzen dieselben Rollennamen wie die App. Deshalb lassen sie sich auch **mischen**.

## Die drei Optionen auf einen Blick

| | A · Anzeigetafel | B · Messgerät | C · Flutlicht |
|---|---|---|---|
| Idee | TV-Einblendung: kantig, aufrecht, Zahlen groß | Messinstrument: ruhig, Raster, Haarlinien | Fankurve: Plakat, Rot flutet, Kreide |
| Rot (Fläche / Schrift) | `#E31D29` / `#FFA29F` | `#DC2628` / `#FFA29E` | `#E32018` / `#FFA697` |
| Hintergrund Dark | `#0D0F14` kühles Anthrazit | `#131517` neutrales Graphit | `#140F0E` warmes Schwarz |
| Schrift | Barlow Condensed + Barlow (**wie heute**) | Archivo + IBM Plex Mono | Big Shoulders Display + Sofia Sans Condensed |
| Logo | Karte mit Anschnitt + Aufwertungs-Puls, Wortmarke in eckigen Großbuchstaben | Rundinstrument mit Ausschlag, Wortmarke klein in Strichschrift | FP-Schablone mit Puls-Schnitt, Wortmarke zweizeilig |
| Formmotiv | angeschnittene Ecke | Raster und Messpunkt | harte Kanten, dicke Balken, Streifen |
| Prüfungen v2 (Dark / Light) | 74 / 75 · 69 / 69 | 72 / 75 · 69 / 69 | 73 / 75 · 69 / 69 |
| Engste Flächenstufe (ΔL) | 3,5 / 3,3 | 3,4 / 3,3 | 3,4 / 3,2 |
| Feed: Farbabstand zum Umfeld | **20,4** | 16,3 | 14,8 |
| Feed: Kontrast nach Unschärfe | 0,25 | 0,33 | **0,40** |
| App-Umbau | klein (Schrift bleibt) | mittel (neue Schrift) | groß (zwei neue Schriften) |
| Design-System-Artefakt | [öffnen](https://claude.ai/artifact/87k4nXC24dJHUAwpWWbc6y) | [öffnen](https://claude.ai/artifact/QttJMNLHMkkQuE3brQ1jre) | [öffnen](https://claude.ai/artifact/HfHw9KDWWJpAGQ5PcWvYUx) |

Heute (zum Vergleich): Flächenstufen nur ΔL 1,5–2,5. Auf und Ab nur über die Farbe. Kein Light-Modus.

## Was du mischen kannst

Die Optionen bestehen aus vier Bausteinen. Jeder Baustein lässt sich einzeln tauschen.

| Baustein | frei tauschbar? | Was du beachten musst |
|---|---|---|
| **Palette** | ja | Alle drei sind auf denselben Rollen gemessen. Wer mischt, nimmt eine Palette ganz und keine einzelnen Farben aus zwei Paletten. Sonst gelten die Messungen nicht mehr. |
| **Schrift** | ja | Bei C sind es immer zwei Schriften, weil Big Shoulders keine gleich breiten Ziffern hat. Mit A bleibt der App-Umbau am kleinsten. |
| **Logo** | ja | Die Logos sind eigene Zeichnungen und hängen nicht an der Schrift. Das Logo A passt zu jeder Palette. Logo C wirkt mit Palette B kühl und fremd. |
| **Formensprache** | bedingt | Die Ecken und Linien gehören zum Logo. Wer Logo A nimmt, sollte auch die angeschnittene Ecke nehmen, sonst fehlt der rote Faden. |

Sinnvolle Mischungen:

1. **A komplett.** Meine Empfehlung, siehe unten.
2. **A, aber Social-Schlagzeilen aus C.** Die App bleibt A. Auf Social kommt Big Shoulders nur für große Schlagzeilen dazu, dazu die C-Streifen als Muster. Das ist lauter im Feed (Kontrast 0,40 statt 0,25), kostet aber eine dritte Schrift.
3. **B-Palette mit A-Logo und A-Schrift.** Das ist ruhiger und neutraler (Graphit statt Anthrazit), mit blauer statt türkiser Aufwertung. Das passt, wenn die App sehr nüchtern wirken soll.

Nicht empfehlenswert: Logo B mit Formensprache C (rund gegen hart), oder Schrift B mit Logo C (zwei Stile, die gegeneinander arbeiten).

## Meine Empfehlung

**Option A, komplett.** Begründung:

- Sie ist die einzige Option, die **beide Einsatzarten** mit denselben Mitteln schafft: ruhig in der App, laut im Feed. Im Feed hat sie den größten Farbabstand zum Umfeld (ΔE 20,4).
- **Die Schrift bleibt.** Barlow Condensed und Barlow sind schon in der App. Der Umbau ist ein Austausch von Werten.
- **Das Logo erzählt das Produkt.** Die Karte mit der angeschnittenen Ecke ist das Kernmotiv. Der Puls endet höher, als er beginnt, also eine Aufwertung und kein EKG. Das gibt es so bei keinem Vorbild.
- **Kein Bruch mit dem Bestand.** Rot, Schwarz, Puls und kantige Sportgrafik bleiben erkennbar, nur sauber und eigen.

Ehrliche Schwächen von A:
- Kantige Sportgrafik ist verbreitet. A wird nur eigen, wenn die Kartenecke konsequent eingesetzt wird.
- Im Blinzeltest ist A weniger kontrastreich als C (0,25 gegen 0,40). Für den Feed heißt das: große Zahlen und viel Rot-Fläche nutzen, nicht kleine Texte.
- Rote Schrift auf Dunkel (`accentText`) ist sehr hell und wirkt lachsfarben (`#FFA29F`). Das ist der Preis für APCA Lc 60, betrifft alle drei Optionen und ist deshalb ein Grund mehr, Rot fast nur als Fläche einzusetzen. Wer ein kräftigeres Rot als Schrift will, muss auf APCA verzichten. Gemessen: Das heutige `#FF5260` erreicht WCAG noch knapp (4,54 : 1 auf surfaceElevated), aber nur Lc 40–44.
- Die Aufwertung ist jetzt Türkis (`#5EF9F1`) statt Grün. Das ist für Menschen mit Rot-Grün-Schwäche besser, aber ungewohnt. Wer klassisches Grün will, verliert diese Trennbarkeit. Pfeil und Vorzeichen bleiben in jedem Fall Pflicht.

## Was du entscheiden musst

1. Option A, B oder C, oder eine Mischung (Nummer oben oder eigene Angabe).
2. Ob das alte FP-Monogramm wirklich wegfällt. In A und B fällt es weg, in C lebt es als Schablone weiter.
3. Ob die Aufwertung Türkis bleiben darf.

Danach mache ich: `marke/stil.md` auf die gewählte Option festlegen, die Tokens als eine `tokens.json` zusammenführen, das gewählte Artefakt als gültig markieren, die Vorlagen nach `06 Vorlagen` (ohne „Entwurf“) übernehmen und Kerem die Canva-Anleitung mit den finalen Werten geben.
