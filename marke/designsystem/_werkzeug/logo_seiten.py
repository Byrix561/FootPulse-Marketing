"""Logo-Regelseite (logo-regeln.html) und Export-Seite (logo-export.html) je Option."""
import optionen as O

# Schutzzone und Mindestgrößen je Option. Einheit x = Maß, das im Logo selbst steckt.
REGELN = {
    "A": {"x": "Breite des Kartenanschnitts (¼ der Bildmarken-Breite)", "zone": 0.25, "min_quer": 96, "min_marke": 16, "min_druck": "20 mm Breite (quer)",
          "marke": "bildmarke-rot.svg", "quer": "kombi-quer-auf-dunkel.svg", "quer_h": "kombi-quer-auf-hell.svg"},
    "B": {"x": "Ringstärke × 4 (≈ ⅕ der Bildmarke)", "zone": 0.2, "min_quer": 88, "min_marke": 16, "min_druck": "18 mm Breite (quer)",
          "marke": "bildmarke-dunkel.svg", "quer": "kombi-quer-auf-dunkel.svg", "quer_h": "kombi-quer-auf-hell.svg"},
    "C": {"x": "Höhe des Puls-Schnitts (⅙ der Bildmarke)", "zone": 0.17, "min_quer": 110, "min_marke": 20, "min_druck": "24 mm Breite (quer)",
          "marke": "bildmarke-rot.svg", "quer": "kombi-quer-auf-dunkel.svg", "quer_h": "kombi-quer-auf-hell.svg"},
}

DONTS = [
    ("verzerrt", "transform:scaleX(1.5)", "Nicht verzerren"),
    ("gedreht", "transform:rotate(-8deg)", "Nicht drehen oder kursiv stellen"),
    ("schatten", "filter:drop-shadow(0 0 14px #ff0) drop-shadow(6px 6px 0 #00f)", "Keine Schatten, kein Glühen"),
    ("farbe", "filter:hue-rotate(140deg)", "Keine fremden Farben"),
    ("rot", "", "Farbiges Logo nie auf Rot: dort nur einfarbig weiß"),
    ("foto", "", "Nicht auf unruhigen Fotos ohne Fläche dahinter"),
]

EXPORT = {  # Datei -> Liste von Zielbreiten in px (Höhe ergibt sich)
    "app-icon.svg": [1024, 512, 256, 180, 120],
    "favicon.svg": [16, 32, 48, 192],
    "profilbild.svg": [1080, 400],
    "profilbild-bl.svg": [1080], "profilbild-pl.svg": [1080], "profilbild-sl.svg": [1080],
    "kombi-quer-auf-dunkel.svg": [2000, 1000, 500], "kombi-quer-auf-hell.svg": [2000, 1000, 500],
    "kombi-quer-mono-weiss.svg": [2000, 1000], "kombi-quer-mono-schwarz.svg": [2000, 1000],
    "wortmarke-auf-dunkel.svg": [2000, 1000], "wortmarke-auf-hell.svg": [2000, 1000],
    "wortmarke-mono-weiss.svg": [2000], "wortmarke-mono-schwarz.svg": [2000],
    "bildmarke-mono-weiss.svg": [1024, 256], "bildmarke-mono-schwarz.svg": [1024, 256],
}
EXTRA = {"A": {"bildmarke-rot.svg": [1024, 512, 256], "bildmarke-hell.svg": [1024], "kombi-hoch-auf-dunkel.svg": [1200], "kombi-hoch-auf-hell.svg": [1200]},
         "B": {"bildmarke-dunkel.svg": [1024, 512, 256], "bildmarke-hell.svg": [1024], "kombi-hoch-auf-dunkel.svg": [1200], "kombi-hoch-auf-hell.svg": [1200]},
         "C": {"bildmarke-rot.svg": [1024, 512, 256], "bildmarke-dunkel.svg": [1024], "wortmarke-einzeilig-auf-dunkel.svg": [2000], "wortmarke-einzeilig-auf-hell.svg": [2000]}}


def regeln(r, p):
    g = REGELN[r]
    ink, paper, red = p["mkInk"], p["mkPaper"], p["accent"]
    donts = "".join(
        f'<figure><div class="dt" style="background:{red if k == "rot" else (("repeating-linear-gradient(45deg,#7a8b6e 0 18px,#c9b38a 18px 36px,#3d5a73 36px 54px)") if k == "foto" else ink)}">'
        f'<img src="logo/{"kombi-quer-auf-dunkel.svg"}" style="height:44px;{css}"></div><figcaption>✕ {txt}</figcaption></figure>'
        for k, css, txt in DONTS)
    zone = g["zone"]
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Logo-Regeln {r}</title>
<link rel="stylesheet" href="tokens.css"><style>
*{{box-sizing:border-box}} body{{margin:0;background:#ececec;color:#16171a;font:15px/1.5 system-ui,sans-serif}}
.w{{padding:32px;max-width:1400px}} h1{{margin:0 0 4px;font-size:28px}} h2{{font-size:18px;margin:32px 0 12px}}
.row{{display:flex;flex-wrap:wrap;gap:20px;align-items:flex-start}}
figure{{margin:0}} figcaption{{font-size:13px;margin-top:6px;color:#444}}
.tile{{padding:28px;display:flex;align-items:center;justify-content:center;min-width:260px;min-height:140px}}
.zone{{position:relative;display:inline-block;outline:2px dashed #e0313c;outline-offset:var(--z)}}
.zone img{{display:block}}
.dt{{width:300px;height:150px;display:flex;align-items:center;justify-content:center}}
.ok{{color:#0a7d32}} table{{border-collapse:collapse}} td,th{{border-bottom:1px solid #ccc;padding:6px 10px;text-align:left}}
</style></head><body><div class="w" id="regeln">
<h1>Option {r} · {O.NAME[r]} · Logo-Regeln</h1><p>Alle Dateien liegen als SVG in <code>logo/</code>, PNG-Exporte in OneDrive <code>00 Marke/Designsystem 2026/Logos/</code>.</p>
<h2>1. Varianten</h2><div class="row">
<figure><div class="tile" style="background:{ink}"><img src="logo/{g['quer']}" style="height:56px"></div><figcaption>Quer auf Dunkel (Standard)</figcaption></figure>
<figure><div class="tile" style="background:#fff"><img src="logo/{g['quer_h']}" style="height:56px"></div><figcaption>Quer auf Hell</figcaption></figure>
<figure><div class="tile" style="background:{red}"><img src="logo/kombi-quer-mono-weiss.svg" style="height:56px"></div><figcaption>Auf Rot: einfarbig weiß</figcaption></figure>
<figure><div class="tile" style="background:#fff"><img src="logo/kombi-quer-mono-schwarz.svg" style="height:56px"></div><figcaption>Einfarbig schwarz (Stempel, Fax, Gravur)</figcaption></figure>
<figure><div class="tile" style="background:{ink}"><img src="logo/{g['marke']}" style="height:90px"></div><figcaption>Bildmarke allein</figcaption></figure>
<figure><div class="tile" style="background:#ddd"><img src="logo/app-icon.svg" style="height:120px;border-radius:26px"></div><figcaption>App-Icon (Ecken rundet das Betriebssystem)</figcaption></figure>
<figure><div class="tile" style="background:#ddd"><img src="logo/profilbild.svg" style="height:120px;border-radius:50%"></div><figcaption>Profilbild, rund beschnitten</figcaption></figure>
<figure><div class="tile" style="background:#ddd;gap:10px"><img src="logo/favicon.svg" style="height:16px"><img src="logo/favicon.svg" style="height:32px"><img src="logo/favicon.svg" style="height:48px"></div><figcaption>Favicon 16 · 32 · 48 px</figcaption></figure>
</div>
<h2>2. Liga-Konten</h2><div class="row">
<figure><div class="tile"><img src="logo/profilbild-bl.svg" style="height:140px;border-radius:50%"></div><figcaption>Bundesliga (DE)</figcaption></figure>
<figure><div class="tile"><img src="logo/profilbild-pl.svg" style="height:140px;border-radius:50%"></div><figcaption>Premier League (EN)</figcaption></figure>
<figure><div class="tile"><img src="logo/profilbild-sl.svg" style="height:140px;border-radius:50%"></div><figcaption>Süper Lig (TR)</figcaption></figure>
<p style="max-width:420px">Gleiches Zeichen, gleiche Farben. Nur das Kürzel und der Liga-Akzent unterscheiden die Konten. Keine Flaggen, keine echten Liga-Logos, keine Liga-Farben.</p>
</div>
<h2>3. Schutzzone und Mindestgröße</h2><div class="row">
<figure><div class="tile" style="background:#fff;padding:60px"><span class="zone" style="--z:{round(56 * zone * 2.2)}px"><img src="logo/{g['quer_h']}" style="height:56px"></span></div>
<figcaption>Schutzzone rundherum = x · x = {g['x']}</figcaption></figure>
<table><tr><th>Element</th><th>digital mindestens</th><th>Druck</th></tr>
<tr><td>Logo quer</td><td>{g['min_quer']} px breit</td><td>{g['min_druck']}</td></tr>
<tr><td>Bildmarke</td><td>{g['min_marke']} px</td><td>6 mm</td></tr>
<tr><td>Profilbild</td><td>Zeichen ≤ 60 % des Kreises</td><td>–</td></tr></table>
<figure><div class="tile" style="background:{ink};gap:16px"><img src="logo/{g['quer']}" style="width:{g['min_quer']}px"><img src="logo/{g['marke']}" style="height:{g['min_marke']}px"></div><figcaption>Mindestgrößen in Originalgröße</figcaption></figure>
</div>
<h2>4. So nicht</h2><div class="row">{donts}</div>
</div></body></html>"""


def export_seite(r):
    files = dict(EXPORT)
    files.update(EXTRA[r])
    import json
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Export {r}</title></head><body>
<script>
const LISTE = {json.dumps(files)};
async function render(name, w) {{
  const txt = await (await fetch('logo/' + name)).text();
  const img = new Image();
  const url = URL.createObjectURL(new Blob([txt], {{type: 'image/svg+xml'}}));
  await new Promise((ok, no) => {{ img.onload = ok; img.onerror = no; img.src = url; }});
  const h = Math.round(w * img.naturalHeight / img.naturalWidth);
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  c.getContext('2d').drawImage(img, 0, 0, w, h);
  return c.toDataURL('image/png');
}}
window.exportAlle = async () => {{
  const out = {{}};
  for (const [n, ws] of Object.entries(LISTE)) for (const w of ws) out[n.replace('.svg', '') + '_' + w + 'px.png'] = await render(n, w);
  return out;
}};
</script></body></html>"""
