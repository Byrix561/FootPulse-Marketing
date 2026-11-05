# Für den Supervisor (Vorschlag, Burhan überträgt)

Stand 05.11.2026. Das ist ein Vorschlag aus dem Marketing-Repo. Den App-Umbau macht der Marketing-Chat nicht. Welche Option gilt, entscheidet Burhan. Der Absatz gilt für jede Option, die Werte stehen je Option in `option-*/alt-neu.md` und `option-*/tokens.json`.

---

**Designsystem 2026: was sich für die App ändert.** Die Token-Datei bekommt neue Werte auf denselben Rollennamen. Es ist ein Austausch, kein Neubau. Die Tabelle „alter Wert → neuer Wert“ liegt je Option bei.

Wichtig sind diese Punkte:

1. **Flächenstufen:** background, surfaceDeep, surface, surfaceElevated und surfaceOverlay liegen jetzt mindestens ΔL 3 auseinander (heute 1,5–2,5). Der Hintergrund ist kein Fast-Schwarz mehr, das hilft gegen Schlieren auf OLED. Bitte auf einem OLED-Handy prüfen.
2. **Elf neue Rollen:** `tabTrack`, `tabActive`, `surfaceHover`, `surfacePressed`, `surfaceSelected`, `surfaceDisabled`, `textDisabled`, `focusRing`, `onAccent`, `goldText`, `ratingInk`. Tabs, Listen und Buttons sollten diese Rollen statt fester Werte nutzen.
3. **Light-Modus:** Für jede Rolle gibt es jetzt einen Light-Wert. Ob die App Light anbietet, ist eine Produktentscheidung.
4. **Auf und Ab:** `ratingUp` ist Türkis statt Grün und deutlich heller als `ratingDown`. Jede Bewegung zeigt zusätzlich ▲/▼ und +/−, auch in Tabellen und Chips. Das ist für Menschen mit Rot-Grün-Schwäche nötig.
5. **Noten-Skala 0–10:** Es gibt neue Werte für Elite, Excellent, Good, Average und Poor. Die Helligkeit steigt nicht mehr stufenweise an, deshalb steht die Note immer als Zahl im Chip, in `ratingInk`.
6. **Rot:** `accent` ist so gewählt, dass weiße Schrift darauf 4,5 : 1 erreicht (`onAccent`). `accentText` ist heller als heute, damit rote Schrift auch nach APCA lesbar ist. Rote Punkte unter 8 px nutzen `accentText`.
7. **Fokus:** 2 px `focusRing` mit 2 px Abstand an allen Bedienelementen.
8. **Schrift:** Option A behält Barlow Condensed und Barlow. Option B wechselt auf Archivo und IBM Plex Mono, Option C auf Big Shoulders Display (nur Überschriften) und Sofia Sans Condensed. Alle sind frei lizenziert (OFL), haben Türkisch und gleich breite Ziffern, wo Zahlen stehen. Türkischer Text in Großbuchstaben braucht `lang="tr"`.
9. **Radien und Raster:** Das 4-pt-Raster, Gutter 20, mobile Spalte 560 und die Breakpoints 720/960 bleiben. Die Radien ändern sich je Option (A: kleine Radien plus angeschnittene Kartenecke, B: 8–16, C: 0).
10. **Logo und Favicon:** neue SVGs in `option-*/logo/` (App-Icon, Favicon, Wortmarke).

Messwerte und Testseiten: `marke/designsystem/testmatrix.md`, `testmatrix-bild.md` und `option-*/testseiten.html`.
