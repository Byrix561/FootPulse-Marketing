"""Erzeugt je Option die Testseite testseiten.html (Dark/Light über ?theme=, v1/v2 über ?v=).

Alle Spieler und Vereine sind erfunden. Keine echten Wappen, keine echten Liga-Logos.
"""
import optionen as O
import totw as XI

SPIELER = [  # Position, Name, Overall, Bewegung, Verein
    ("TW", "G. Iversen", 82, +1, "NHF"), ("LV", "A. Şahin", 79, 0, "ATL"), ("IV", "R. Novak", 84, +2, "RVS"), ("IV", "D. Moreau", 81, -1, "NHF"),
    ("RV", "T. Brennan", 80, +3, "KRT"), ("ZM", "J. Okafor", 86, +2, "ATL"), ("ZM", "E. Yıldız", 83, +4, "KRT"), ("ZM", "P. Lindqvist", 82, -2, "RVS"),
    ("LA", "M. Silva", 85, +1, "NHF"), ("ST", "K. Demir", 88, +4, "KRT"), ("RA", "C. Öztürk", 84, +3, "ATL"),
]

# Option-spezifische Gestaltung (Formen, Schriftrollen). Farben kommen nur aus den Token-Variablen.
STIL = {
"A": """
.h, .ovr, .num, .stat b, .tab, .btn, .chip, .post .big, .post .t { font-family: var(--font-display); }
.label { font-family: var(--font-label); text-transform: uppercase; letter-spacing: .06em; font-weight: 600; font-size: 12px; }
.card { clip-path: polygon(0 0, calc(100% - var(--cut-md)) 0, 100% var(--cut-md), 100% 100%, 0 100%); border-radius: 0; }
.cardline { position:absolute; top:0; right:0; width: calc(var(--cut-md) * 1.4142); height: 2px; background: var(--accent); transform-origin: 100% 0; transform: translateX(0) rotate(45deg) translateY(-1px); }
.ovr { font-size: 56px; font-weight: 800; line-height: .85; }
.tabs { border-radius: var(--radius-sm); padding: 4px; gap: 4px; }
.tab { border-radius: var(--radius-xs); font-weight: 700; text-transform: uppercase; letter-spacing: .04em; font-size: 15px; }
.tab.is-active { box-shadow: inset 0 -3px 0 var(--accent); }
.chip { border-radius: var(--radius-xs); font-weight: 700; font-size: 15px; }
.btn { clip-path: polygon(0 0, calc(100% - var(--cut-sm)) 0, 100% var(--cut-sm), 100% 100%, 0 100%); border-radius: 0; font-weight: 800; text-transform: uppercase; letter-spacing: .04em; font-size: 17px; }
.mini { clip-path: polygon(0 0, calc(100% - 8px) 0, 100% 8px, 100% 100%, 0 100%); }
.post { clip-path: none; }
.post .frame { position:absolute; inset: 0; border: 0; }
.post .big { font-weight: 800; letter-spacing: -.01em; }
.post .t { font-weight: 800; text-transform: uppercase; }
""",
"B": """
.h { font-family: var(--font-display); font-stretch: 75%; letter-spacing: -.01em; }
.ovr, .num, .stat b { font-family: var(--font-zahl); font-stretch: 80%; }
.label, .tab, .chip { font-family: var(--font-label); text-transform: uppercase; letter-spacing: .08em; font-weight: 500; font-size: 11px; }
.card { border-radius: var(--radius-md); background-image: linear-gradient(var(--borderSubtle) 1px, transparent 1px), linear-gradient(90deg, var(--borderSubtle) 1px, transparent 1px); background-size: 100% 25%, 25% 100%; }
.cardline { position:absolute; top:14px; right:14px; width:8px; height:8px; border-radius:50%; background: var(--accentText); }
.ovr { font-size: 48px; font-weight: 700; line-height: .9; }
.tabs { border-radius: var(--radius-pill); padding: 4px; gap: 2px; }
.tab { border-radius: var(--radius-pill); font-size: 12px; }
.tab.is-active::before { content: ""; display:inline-block; width:6px; height:6px; border-radius:50%; background: var(--accentText); margin-right:6px; vertical-align: middle; }
.chip { border-radius: var(--radius-pill); }
.btn { border-radius: var(--radius-sm); font-family: var(--font-text); font-weight: 600; font-size: 16px; }
.mini { border-radius: 8px; }
.post { border-radius: 0; }
.post .big { font-family: var(--font-zahl); font-stretch: 70%; font-weight: 700; }
.post .t { font-family: var(--font-text); font-weight: 600; }
.post .grid-bg { position:absolute; inset:0; background-image: linear-gradient(rgba(255,255,255,.06) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.06) 1px, transparent 1px); background-size: 20% 12.5%; }
""",
"C": """
.h, .post .big { font-family: var(--font-display); text-transform: uppercase; font-weight: 900; }
.ovr, .num, .stat b, .chip, .btn { font-family: var(--font-zahl); }
.label, .tab { font-family: var(--font-label); text-transform: uppercase; letter-spacing: .08em; font-weight: 800; font-size: 13px; }
.card { border-radius: 0; border-width: 2px; border-top: 8px solid var(--accent); }
.cardline { display:none; }
.ovr { font-size: 58px; font-weight: 800; line-height: .85; }
.tabs { border-radius: 0; padding: 0; gap: 0; border: 2px solid var(--border); }
.tab { border-radius: 0; }
.tab.is-active { box-shadow: inset 0 -6px 0 var(--accent); }
.chip { border-radius: 0; font-weight: 800; }
.btn { border-radius: 0; font-weight: 800; text-transform: uppercase; letter-spacing: .06em; font-size: 17px; }
.mini { border-radius: 0; border-top: 4px solid var(--accent) !important; }
.post { border-radius: 0; }
.post .t { font-family: var(--font-label); text-transform: uppercase; letter-spacing: .06em; font-weight: 800; }
""",
}

LOGO = {  # Dateien für dunklen bzw. hellen Grund
    "A": ("logo/kombi-quer-auf-dunkel.svg", "logo/kombi-quer-auf-hell.svg", "logo/bildmarke-rot.svg", "logo/profilbild.svg"),
    "B": ("logo/kombi-quer-auf-dunkel.svg", "logo/kombi-quer-auf-hell.svg", "logo/bildmarke-dunkel.svg", "logo/profilbild.svg"),
    "C": ("logo/kombi-quer-auf-dunkel.svg", "logo/kombi-quer-auf-hell.svg", "logo/bildmarke-rot.svg", "logo/profilbild.svg"),
}

POST_TXT = {
    "A": {"kicker": "Aufwertung der Woche", "big": "+4", "sub": "K. Demir · jetzt 88", "why": "Warum? 3 Spiele, 2 Tore, Pressing über Ligaschnitt."},
    "B": {"kicker": "SPIELTAG 11 · AUFWERTUNG", "big": "84→88", "sub": "Warum Demir jetzt vier Punkte mehr hat.", "why": "3 Spiele · 2 Tore · Pressing +18 % über Ligaschnitt"},
    "C": {"kicker": "Spieltag 11 · Aufwertung", "big": "Wer stoppt ihn?", "sub": "Demir +4 · jetzt 88", "why": "3 Spiele. 2 Tore. Und niemand kommt hinterher."},
}


def _bew(d):
    if d > 0:
        return f'<span class="chip up" aria-label="Aufwertung um {d}"><b>▲</b> +{d}</span>'
    if d < 0:
        return f'<span class="chip down" aria-label="Abwertung um {-d}"><b>▼</b> −{-d}</span>'
    return '<span class="chip flat" aria-label="unverändert"><b>■</b> 0</span>'


def _note(v):
    st = "Elite" if v >= 9 else "Excellent" if v >= 8 else "Good" if v >= 7 else "Average" if v >= 6 else "Poor"
    return f'<span class="note n-{st.lower()}" title="{st}">{v:.1f}</span>'.replace(".", ",", 1)


def seite(r):
    p = POST_TXT[r]
    ld, lh, mark, prof = LOGO[r]
    rows = "".join(
        f'<tr{" class=sel" if i == 1 else ""}><td class="num rk">{i + 1}</td><td><span class="pos">{pos}</span> {n}</td><td class="club">{c}</td>'
        f'<td class="num">{o}</td><td>{_bew(d)}</td><td>{_note([8.9, 7.4, 9.2, 6.3, 5.4, 8.1][i % 6])}</td></tr>'
        for i, (pos, n, o, d, c) in enumerate(sorted(SPIELER, key=lambda x: -x[2])[:6]))
    lineup = [(50, 88, 0), (18, 70, 1), (39, 72, 2), (61, 72, 3), (82, 70, 4), (28, 47, 5), (50, 50, 6), (72, 47, 7), (20, 22, 8), (50, 16, 9), (80, 22, 10)]
    totw = "".join(
        f'<div class="mini{" mvp" if SPIELER[k][1] == "K. Demir" else ""}" style="left:{x}%;top:{y}%"><span class="mo num">{SPIELER[k][2]}</span>'
        f'<span class="mp">{SPIELER[k][0]}</span><span class="mn" lang="tr">{SPIELER[k][1].split(" ")[-1]}</span>'
        f'{"<span class=mvptag>MVP</span>" if SPIELER[k][1] == "K. Demir" else ""}</div>'
        for x, y, k in lineup)
    css = """
*{box-sizing:border-box} html{background:var(--background)}
body{margin:0;background:var(--background);color:var(--textPrimary);font-family:var(--font-text);font-size:16px;line-height:1.5;-webkit-font-smoothing:antialiased}
.num,.ovr,.stat b,.mo{font-variant-numeric:tabular-nums}
.wrap{padding:24px;display:flex;flex-wrap:wrap;gap:24px;align-items:flex-start;max-width:1500px}
.blk{background:var(--background);padding:16px;border:1px dashed var(--borderSubtle);position:relative}
.blk>.label.cap{display:block;color:var(--textTertiary);margin-bottom:12px}
.head{width:100%;display:flex;justify-content:space-between;align-items:center;gap:16px;padding:8px 0 0}
.head h1{margin:0;font-size:28px}
.head p{margin:0;color:var(--textSecondary);font-size:14px}
/* Flächenleiter */
.ladder{display:grid;grid-template-columns:repeat(4,110px);gap:0}
.ladder div{height:84px;padding:8px;font-size:12px;line-height:1.3;color:var(--textSecondary);border-right:1px solid transparent}
.ladder div b{display:block;color:var(--textPrimary);font-size:13px}
/* Karte */
.card{position:relative;width:300px;padding:20px;background:var(--surface);border:1px solid var(--border);overflow:hidden}
.card .top{display:flex;justify-content:space-between;align-items:flex-start}
.ovrbox{display:flex;flex-direction:column;gap:6px}
.card .pos{color:var(--textSecondary);font-size:14px}
.card .nm{font-size:24px;line-height:1.1;margin:14px 0 2px;font-weight:700}
.card .club{color:var(--textTertiary);font-size:14px}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:6px 20px;margin-top:16px}
.stat{display:flex;justify-content:space-between;align-items:baseline;color:var(--textSecondary);font-size:15px;border-bottom:1px solid var(--borderSubtle);padding-bottom:4px}
.stat b{color:var(--textPrimary);font-size:19px}
.why{margin-top:14px;padding:10px 12px;background:var(--surfaceElevated);color:var(--textSecondary);font-size:14px;line-height:1.4}
.why b{color:var(--textPrimary)}
/* Tabs */
.tabs{display:flex;background:var(--tabTrack);width:max-content}
.tab{padding:10px 16px;color:var(--textSecondary);border:0;background:transparent;position:relative;white-space:nowrap}
.tab.is-hover{background:var(--surfaceHover);color:var(--textPrimary)}
.tab.is-pressed{background:var(--surfacePressed);color:var(--textPrimary)}
.tab.is-active{background:var(--tabActive);color:var(--textPrimary)}
.tab.is-selected{background:var(--surfaceSelected);color:var(--textPrimary)}
.tab.is-focus{outline:2px solid var(--focusRing);outline-offset:2px;color:var(--textPrimary);z-index:1}
.tab.is-disabled{background:var(--surfaceDisabled);color:var(--textDisabled)}
.legend{display:flex;gap:4px;margin-top:6px;font-size:11px;color:var(--textTertiary)}
.legend span{white-space:nowrap}
/* Tabelle */
.tbl{border-collapse:collapse;width:520px;background:var(--surface);font-size:15px}
.tbl th{font-family:var(--font-label);text-align:left;color:var(--textTertiary);font-weight:600;font-size:12px;text-transform:uppercase;letter-spacing:.06em;padding:10px 12px;border-bottom:1px solid var(--border);background:var(--surfaceElevated)}
.tbl td{padding:9px 12px;border-bottom:1px solid var(--borderSubtle)}
.tbl td.num{font-size:17px;text-align:right;font-weight:700}
.tbl td.rk{color:var(--textTertiary);font-weight:600;width:32px}
.tbl tr.sel td{background:var(--surfaceSelected)}
.tbl tr.hov td{background:var(--surfaceHover)}
.tbl .pos{display:inline-block;min-width:28px;color:var(--textTertiary);font-size:13px}
.tbl .club{color:var(--textSecondary);font-size:13px}
/* Chips */
.chip{display:inline-flex;align-items:center;gap:4px;padding:3px 8px;font-size:14px;line-height:1.2;white-space:nowrap}
.chip b{font-size:.75em}
.chip.up{background:var(--positiveMuted);color:var(--ratingUp)}
.chip.down{background:var(--downChipBg);color:var(--downChipFg)}
.chip.flat{background:var(--surfaceElevated);color:var(--textSecondary)}
.chip.gold{background:var(--goldMuted);color:var(--goldText)}
.note{display:inline-block;min-width:40px;text-align:center;padding:3px 6px;font-weight:700;font-size:14px;color:var(--ratingInk);font-variant-numeric:tabular-nums}
.n-elite{background:var(--ratingElite)}.n-excellent{background:var(--ratingExcellent)}.n-good{background:var(--ratingGood)}.n-average{background:var(--ratingAverage)}.n-poor{background:var(--ratingPoor);color:var(--onRatingPoor)}
.chiprow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;max-width:520px}
.lg{display:inline-block;padding:3px 8px;font-weight:700;font-size:13px;color:var(--ratingInk)}
/* TOTW */
.pitch{position:relative;width:420px;height:560px;background:var(--pitchGreen);border:2px solid var(--pitchLine);overflow:hidden}
.pitch::before{content:"";position:absolute;left:0;right:0;top:50%;border-top:2px solid var(--pitchLine)}
.pitch::after{content:"";position:absolute;left:50%;top:50%;width:110px;height:110px;margin:-55px 0 0 -55px;border:2px solid var(--pitchLine);border-radius:50%}
.box1,.box2{position:absolute;left:28%;width:44%;height:13%;border:2px solid var(--pitchLine)}.box1{top:-2px}.box2{bottom:-2px}
.mini{position:absolute;transform:translate(-50%,-50%);width:76px;padding:6px 6px 5px;background:var(--surfaceElevated);border:1px solid var(--border);text-align:center;z-index:1}
.mini .mo{display:block;font-family:var(--font-zahl);font-size:24px;font-weight:800;line-height:1}
.mini .mp{display:block;font-size:10px;color:var(--textTertiary);font-weight:700;letter-spacing:.06em}
.mini .mn{display:block;font-size:12px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.mini.mvp{border:2px solid var(--gold)}
.mvptag{position:absolute;top:-10px;left:50%;transform:translateX(-50%);background:var(--gold);color:var(--ratingInk);font-size:10px;font-weight:800;padding:1px 6px;letter-spacing:.08em}
/* Warteliste */
.wait{width:390px;background:var(--background);border:1px solid var(--border);padding:28px 24px}
.wait img{height:30px;display:block;margin-bottom:36px}
.wait h2{font-size:38px;line-height:1;margin:0 0 12px}
.wait p{color:var(--textSecondary);margin:0 0 20px;font-size:16px}
.field{display:block;margin-bottom:12px}
.field span{display:block;font-size:13px;color:var(--textSecondary);margin-bottom:6px;font-weight:600}
.input{width:100%;height:48px;padding:0 14px;background:var(--surfaceSunken);border:1px solid var(--borderStrong);color:var(--textPrimary);font:inherit;border-radius:var(--radius-sm)}
.input.focus{outline:2px solid var(--focusRing);outline-offset:2px}
.input.err{border-color:var(--accentText)}
.errtxt{color:var(--accentText);font-size:13px;margin-top:4px;display:block}
.btn{display:block;width:100%;height:52px;border:0;background:var(--accent);color:var(--onAccent);cursor:pointer}
.btn.dis{background:var(--surfaceDisabled);color:var(--textDisabled)}
.fine{font-size:13px;color:var(--textTertiary);margin-top:14px}
.status{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:22px}
/* Kleinschrift */
.small{width:520px;background:var(--surface);padding:12px}
.small div{display:flex;gap:10px;align-items:baseline;border-bottom:1px solid var(--borderSubtle);padding:4px 0}
.small code{width:110px;color:var(--textTertiary);font-size:11px;flex:none}
/* Posts */
.post{position:relative;overflow:hidden;background:var(--mkRed);color:var(--onMkRedLarge)}
.p916{width:360px;height:640px}
.p45{width:432px;height:540px}
.post .in{position:absolute;inset:0;padding:28px;display:flex;flex-direction:column;justify-content:space-between}
.post .t{font-size:30px;line-height:.95}
.post .big{font-size:150px;line-height:.82}
.post .sub{font-size:20px;font-weight:700;font-family:var(--font-display)}
.post .s{font-size:15px;line-height:1.35;color:var(--onMkRed)}
.post .lo{height:22px}
.post.dark{background:var(--mkInk);color:var(--mkPaper)}
.post.dark .s{color:var(--mkPaper)}
.post.dark .big em{color:var(--accentText);font-style:normal}
.safe{position:absolute;inset:0;pointer-events:none}
.safe i{position:absolute;background:rgba(0,180,255,.18);border:1px dashed rgba(0,180,255,.9)}
.grid9{display:grid;grid-template-columns:repeat(3,130px);gap:3px;background:var(--background)}
.grid9 .th{width:130px;height:162px;overflow:hidden;position:relative}
.grid9 .th .post{transform:scale(.3);transform-origin:0 0}
.prof{display:flex;gap:14px;align-items:center;margin-bottom:12px}
.prof img{width:72px;height:72px;border-radius:50%}
.prof b{display:block;font-size:16px}
.prof span{font-size:13px;color:var(--textSecondary)}
.feed{width:390px;background:#000;padding:0 0 12px}
.fp{width:390px;margin-bottom:14px}
.fp .bar{display:flex;align-items:center;gap:8px;padding:8px 10px;color:#fff;font:600 13px system-ui}
.fp .bar i{width:28px;height:28px;border-radius:50%;background:#555;display:inline-block}
.fake{width:390px;height:488px}
.f1{background:linear-gradient(160deg,#3a5f7d,#c9a27a 60%,#5b4636)}
.f2{background:linear-gradient(200deg,#e8e2d6,#9cb8a1 50%,#2f4f3a)}
.f3{background:linear-gradient(170deg,#f4c542,#e86a3a 55%,#3a1f4f)}
"""
    html = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Testseiten {r} {O.NAME[r]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{O.SCHRIFT[r]['google']}&display=block" rel="stylesheet">
<link id="tok" rel="stylesheet" href="tokens.css">
<script>
  const q = new URLSearchParams(location.search);
  document.documentElement.dataset.theme = q.get("theme") || "dark";
  if (q.get("v") === "1") document.getElementById("tok").href = "tokens-v1.css";
  document.documentElement.dataset.safe = q.get("safe") === "0" ? "0" : "1";
</script>
<style>{css}{STIL[r]}{XI.CSS if r == "A" else ""}
[data-safe="0"] .safe{{display:none}}
</style>
</head>
<body>
<div class="wrap">
<div class="head"><div><h1 class="h">Option {r} · {O.NAME[r]}</h1><p>Testseiten. Modus und Version stehen in der Adresse (?theme=dark|light&amp;v=1|2). Alle Spieler sind erfunden.</p></div>
<img src="{ld}" class="logo-d" style="height:34px" alt="FootPulse"></div>

<section class="blk" id="t-flaechen"><span class="label cap">Flächenstufen</span>
<div class="ladder">
<div style="background:var(--surfaceSunken)"><b>surfaceSunken</b>Mulde, Eingabefeld</div>
<div style="background:var(--background)"><b>background</b>Seite</div>
<div style="background:var(--surfaceDeep)"><b>surfaceDeep</b>Leisten</div>
<div style="background:var(--surface)"><b>surface</b>Karte</div>
<div style="background:var(--surfaceHover)"><b>surfaceHover</b>Hover</div>
<div style="background:var(--surfaceElevated)"><b>surfaceElevated</b>gehoben</div>
<div style="background:var(--surfacePressed)"><b>surfacePressed</b>aktiv</div>
<div style="background:var(--surfaceOverlay)"><b>surfaceOverlay</b>Menü</div>
<div style="background:var(--surfaceSelected)"><b>surfaceSelected</b>ausgewählt</div>
<div style="background:var(--surfaceWarm)"><b>surfaceWarm</b>hervorgehoben</div>
<div style="background:var(--surfaceDisabled);color:var(--textDisabled)"><b style="color:var(--textDisabled)">surfaceDisabled</b>deaktiviert</div>
<div style="background:var(--surface);outline:2px solid var(--focusRing);outline-offset:-4px"><b>focusRing</b>Fokus</div>
</div></section>

<section class="blk" id="t-karte"><span class="label cap">Spielerkarte</span>
<div class="card"><span class="cardline"></span>
<div class="top"><div class="ovrbox"><span class="ovr num">88</span><span class="pos label" lang="tr">ST · Süper Lig</span></div>{_bew(4)}</div>
<div class="nm h" lang="tr">Kaan Demir</div><div class="club">Kartal SK · 24 Jahre</div>
<div class="stats">
<div class="stat">Pace <b>91</b></div><div class="stat">Dribbling <b>86</b></div>
<div class="stat">Shooting <b>87</b></div><div class="stat">Defending <b>42</b></div>
<div class="stat">Passing <b>78</b></div><div class="stat">Physical <b>80</b></div></div>
<div class="why"><b>Warum +4?</b> 3 Spiele, 2 Tore, Pressing-Werte 18 % über Ligaschnitt.</div>
</div></section>

<section class="blk" id="t-tabs"><span class="label cap">Tab-Leiste · alle Zustände</span>
<div class="tabs" role="tablist">
<button class="tab">Normal</button><button class="tab is-hover">Hover</button><button class="tab is-pressed">Gedrückt</button>
<button class="tab is-active" aria-selected="true">Aktiv</button><button class="tab is-selected">Ausgewählt</button>
<button class="tab is-focus">Fokus</button><button class="tab is-disabled" disabled>Aus</button></div>
<div style="height:14px"></div>
<div class="tabs" role="tablist"><button class="tab is-active">Übersicht</button><button class="tab">Werte</button><button class="tab">Form</button><button class="tab">Begründung</button></div>
</section>

<section class="blk" id="t-tabelle"><span class="label cap">Tabelle mit Zahlen · Zeile 2 ausgewählt</span>
<table class="tbl"><thead><tr><th>#</th><th>Spieler</th><th>Verein</th><th style="text-align:right">OVR</th><th>Woche</th><th>Note</th></tr></thead><tbody>{rows}</tbody></table>
</section>

<section class="blk" id="t-chips"><span class="label cap">Auf- und Ab-Chips · Noten · Liga</span>
<div class="chiprow">{_bew(4)}{_bew(1)}{_bew(0)}{_bew(-2)}{_bew(-7)}<span class="chip gold"><b>★</b> MVP</span>
{_note(9.4)}{_note(8.3)}{_note(7.2)}{_note(6.1)}{_note(4.8)}
<span class="lg" style="background:var(--leagueBL)">BL</span><span class="lg" style="background:var(--leaguePL)">PL</span><span class="lg" style="background:var(--leagueSL)">SL</span></div>
</section>

<section class="blk" id="t-totw"><span class="label cap">Team der Woche · 4-3-3</span>
{XI.app_block(10) if r == "A" else '<div class="pitch"><span class="box1"></span><span class="box2"></span>' + totw + '</div>'}
</section>

<section class="blk" id="t-warteliste"><span class="label cap">Wartelisten-Seite (Handy)</span>
<div class="wait">
<img src="{ld}" class="logo-d" alt="FootPulse"><img src="{lh}" class="logo-l" alt="FootPulse">
<div class="status"><span class="chip up"><b>●</b> Süper Lig live</span><span class="chip flat">Premier League bald</span><span class="chip flat">Bundesliga bald</span></div>
<h2 class="h">Jede Zahl hat einen Grund.</h2>
<p>FootPulse bewertet Spieler nach dem, was auf dem Platz passiert, und erklärt nach jedem Spieltag, warum sich ein Wert bewegt.</p>
<label class="field"><span>E-Mail</span><input class="input focus" value="kaan@" aria-label="E-Mail"></label>
<label class="field"><span>E-Mail (Fehler)</span><input class="input err" value="kaan@beispiel" aria-label="E-Mail"><small class="errtxt">Bitte prüfe die Adresse.</small></label>
<button class="btn">Auf die Warteliste</button>
<div style="height:8px"></div><button class="btn dis" disabled>Wird gesendet …</button>
<p class="fine">Kein Spam. Abmelden jederzeit. footpulse.org</p>
</div></section>

<section class="blk" id="t-klein"><span class="label cap">Kleine Schrift 10–14 px</span>
<div class="small">
<div><code>textPrimary 12</code><span style="font-size:12px">Pace 91 · Ğ İ ş ı ç · 0123456789</span></div>
<div><code>textSecondary 12</code><span style="font-size:12px;color:var(--textSecondary)">Pace 91 · Ğ İ ş ı ç · 0123456789</span></div>
<div><code>textTertiary 12</code><span style="font-size:12px;color:var(--textTertiary)">Pace 91 · Ğ İ ş ı ç · 0123456789</span></div>
<div><code>textMuted 14/600</code><span style="font-size:14px;font-weight:600;color:var(--textMuted)">Hinweis · 14 px halbfett</span></div>
<div><code>textSecondary 11</code><span style="font-size:11px;color:var(--textSecondary)">Spieltag 11 · 04.11.2026 · Pace 91</span></div>
<div><code>textPrimary 10</code><span style="font-size:10px">10 px nur für Zahlen und Kürzel: ST 88 · TW 82</span></div>
<div><code>accentText 13/600</code><span style="font-size:13px;font-weight:600;color:var(--accentText)">Alle ansehen → · Abwertung −2</span></div>
<div><code>ratingUp 13/600</code><span style="font-size:13px;font-weight:600;color:var(--ratingUp)">▲ +3 diese Woche</span></div>
</div></section>

<section class="blk" id="t-916"><span class="label cap">Post 9:16 · Reel-Cover (blau = Safe Zone)</span>
<div class="post p916"><div class="in" style="padding:56px 28px 150px">
<div class="t">{p['kicker']}</div><div class="big">{p['big'] if r != 'C' else 'Wer<br>stoppt<br>ihn?'}</div>
<div><div class="sub" lang="tr">{p['sub']}</div><div class="s">{p['why']}</div><img class="lo" src="{ld}" style="margin-top:14px" alt=""></div></div>
<div class="safe"><i style="left:0;right:0;top:0;height:64px"></i><i style="left:0;right:0;bottom:0;height:130px"></i><i style="right:0;top:220px;width:56px;height:290px"></i></div>
</div></section>

<section class="blk" id="t-45"><span class="label cap">Post 4:5 · Karussell-Titel</span>
<div class="post p45 dark"><div class="grid-bg"></div><div class="in">
<div class="t" style="color:var(--accentText)">{p['kicker']}</div>
<div class="big" style="font-size:{'130' if r=='B' else '150' if r=='A' else '96'}px">{p['big'] if r != 'C' else 'Wer stoppt<br>ihn?'}</div>
<div><div class="sub" lang="tr">{p['sub']}</div><div class="s">{p['why']}</div><img class="lo" src="{ld}" style="margin-top:14px" alt=""></div></div></div>
</section>

<section class="blk" id="t-raster"><span class="label cap">Profilraster (Instagram)</span>
<div class="prof"><img src="{prof}" alt=""><div><b>footpulse</b><span>Jede Zahl hat einen Grund. Warteliste ↓</span></div></div>
<div class="grid9">
<div class="th"><div class="post p45"><div class="in"><div class="t">Aufwertung</div><div class="big">+4</div><div class="sub">Demir</div></div></div></div>
<div class="th"><div class="post p45 dark"><div class="in"><div class="t" style="color:var(--accentText)">Team der Woche</div><div class="big" style="font-size:110px">11</div><div class="sub">Spieltag 11</div></div></div></div>
<div class="th"><div class="post p45" style="background:var(--mkRedDeep)"><div class="in"><div class="t">Abwertung</div><div class="big">−3</div><div class="sub">Lindqvist</div></div></div></div>
<div class="th"><div class="post p45 dark"><div class="in"><div class="t" style="color:var(--accentText)">Warum?</div><div class="big" style="font-size:110px">78</div><div class="sub">Ein 78er ist schneller als ein 90er.</div></div></div></div>
<div class="th"><div class="post p45"><div class="in"><div class="t">Aufwertung</div><div class="big">+3</div><div class="sub">Brennan</div></div></div></div>
<div class="th"><div class="post p45 dark"><div class="in"><div class="t" style="color:var(--accentText)">Formkurve</div><div class="big" style="font-size:110px">5×</div><div class="sub">Yıldız in Serie</div></div></div></div>
<div class="th"><div class="post p45 dark"><div class="in"><div class="t" style="color:var(--accentText)">MVP</div><div class="big" style="font-size:110px;color:var(--gold)">88</div><div class="sub">Demir</div></div></div></div>
<div class="th"><div class="post p45"><div class="in"><div class="t">Neu bewertet</div><div class="big">64</div><div class="sub">Şahin</div></div></div></div>
<div class="th"><div class="post p45 dark"><div class="in"><div class="t" style="color:var(--accentText)">Warteliste</div><div class="big" style="font-size:80px">footpulse.org</div></div></div></div>
</div></section>

<section class="blk" id="t-feed"><span class="label cap">Wirkung im Feed (fremde Posts als Farbflächen)</span>
<div class="feed">
<div class="fp"><div class="bar"><i></i>anderes_konto</div><div class="fake f1"></div></div>
<div class="fp"><div class="bar"><img src="{prof}" style="width:28px;height:28px;border-radius:50%">footpulse</div>
<div class="post" style="width:390px;height:488px"><div class="in"><div class="t">{p['kicker']}</div><div class="big" style="font-size:{'140' if r!='C' else '92'}px">{p['big'] if r!='C' else 'Wer stoppt<br>ihn?'}</div><div><div class="sub">{p['sub']}</div></div></div></div></div>
<div class="fp"><div class="bar"><i></i>noch_ein_konto</div><div class="fake f2"></div></div>
</div></section>
</div>
<style>img.logo-l{{display:none!important}} [data-theme="light"] img.logo-l{{display:block!important}} [data-theme="light"] img.logo-d{{display:none!important}}</style>
</body></html>
"""
    return html
