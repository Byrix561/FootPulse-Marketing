"""Weitere Beispiele je Option (beispiele.html), alle mit demselben Inhalt, damit A, B und C direkt vergleichbar sind.
Alle Spieler und Vereine sind erfunden. Fotos sind Platzhalter.
"""
import re
import optionen as O
import seiten
import totw as XI

LOGO_D = "logo/kombi-quer-auf-dunkel.svg"
LOGO_H = "logo/kombi-quer-auf-hell.svg"
LOGO_W = "logo/kombi-quer-mono-weiss.svg"

# Größe je Beispiel (Breite, Höhe) – auch für das Zuschneiden
GROESSE = {
    "ex-profil-dark": (390, 844), "ex-profil-light": (390, 844), "ex-rangliste": (390, 844),
    "ex-web": (1280, 720), "ex-homescreen": (390, 300), "ex-konten": (720, 230),
    "ex-abwertung": (540, 675), "ex-vergleich": (540, 675), "ex-totw": (540, 675), "ex-banter": (540, 540),
    "ex-youtube": (640, 360), "ex-umfrage": (405, 720),
}

FORM = [86, 84, 84, 85, 83, 84, 86, 85, 88]  # Overall über 9 Spieltage


def spark(w, h, farbe, punkte=FORM):
    lo, hi = min(punkte) - 1, max(punkte) + 1
    xs = [i * (w - 8) / (len(punkte) - 1) + 4 for i in range(len(punkte))]
    ys = [h - 4 - (p - lo) / (hi - lo) * (h - 8) for p in punkte]
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in zip(xs, ys))
    dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{farbe}"/>' for x, y in zip(xs[-1:], ys[-1:]))
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><polyline points="{pts}" fill="none" stroke="{farbe}" stroke-width="2.5" stroke-linejoin="round"/>{dots}</svg>'


def nav(aktiv=0):
    items = ["Karten", "Bewegung", "TOTW", "Profil"]
    return '<nav class="bn">' + "".join(f'<span class="{"on" if i == aktiv else ""}"><i></i>{t}</span>' for i, t in enumerate(items)) + "</nav>"


def profil(theme):
    return f"""<section class="ex phone" id="ex-profil-{theme}" data-theme="{theme}">
<header class="top"><span class="back">←</span><img src="{LOGO_D if theme == 'dark' else LOGO_H}" alt="" style="height:20px"><span class="back">⋯</span></header>
<div class="pad">
<div class="card" style="width:100%"><span class="cardline"></span>
<div class="top2"><div class="ovrbox"><span class="ovr num">88</span><span class="pos label" lang="tr">ST · Süper Lig</span></div>{seiten._bew(4)}</div>
<div class="nm h" lang="tr">Kaan Demir</div><div class="club">Kartal SK · 24 Jahre</div>
<div class="stats"><div class="stat">Pace <b>91</b></div><div class="stat">Dribbling <b>86</b></div><div class="stat">Shooting <b>87</b></div>
<div class="stat">Defending <b>42</b></div><div class="stat">Passing <b>78</b></div><div class="stat">Physical <b>80</b></div></div></div>
<div class="tabs" style="margin-top:14px;width:100%"><button class="tab is-active" style="flex:1">Begründung</button><button class="tab" style="flex:1">Form</button><button class="tab" style="flex:1">Werte</button></div>
<div class="panel"><div class="ph"><span class="label">Warum +4</span><span class="label" style="color:var(--textTertiary)">Spieltag 11</span></div>
<ul class="why2"><li><b>2 Tore</b> aus 3 Schüssen</li><li><b>Pressing</b> 18 % über Ligaschnitt</li><li><b>Sprints</b> 61, Saisonbestwert</li></ul></div>
<div class="panel"><div class="ph"><span class="label">Formverlauf</span><span class="num" style="color:var(--ratingUp);font-weight:700">▲ +4</span></div>{spark(330, 70, 'var(--ratingUp)')}</div>
</div>{nav(0)}</section>"""


def rangliste():
    rows = [("K. Demir", "ST", 88, 4, 8.9), ("E. Yıldız", "ZM", 83, 4, 8.1), ("T. Brennan", "RV", 80, 3, 7.6), ("C. Öztürk", "RA", 84, 3, 7.9),
            ("R. Novak", "IV", 84, 2, 7.2), ("P. Lindqvist", "ZM", 82, -2, 5.8), ("D. Moreau", "IV", 81, -1, 6.1), ("A. Şahin", "LV", 64, -5, 4.6)]
    li = "".join(f'<div class="rr{" sel" if i == 0 else ""}"><span class="num rk">{i + 1}</span><span class="rn"><b lang="tr">{n}</b><small>{p} · Kartal SK</small></span>'
                 f'<span class="num ro">{o}</span>{seiten._bew(d)}{seiten._note(nt)}</div>' for i, (n, p, o, d, nt) in enumerate(rows))
    return f"""<section class="ex phone" id="ex-rangliste" data-theme="dark">
<header class="top"><span class="h" style="font-size:22px">Bewegungen</span><span class="label" style="color:var(--textTertiary)">Spieltag 11</span></header>
<div class="pad"><div class="tabs" style="width:100%"><button class="tab is-active" style="flex:1">Alle</button><button class="tab" style="flex:1">Auf</button><button class="tab" style="flex:1">Ab</button><button class="tab is-focus" style="flex:1">Süper Lig</button></div>
<div class="list">{li}</div></div>{nav(1)}</section>"""


def web():
    return f"""<section class="ex" id="ex-web" data-theme="dark" style="background:var(--background)">
<header class="wh"><img src="{LOGO_D}" style="height:30px" alt=""><nav><span>So funktioniert's</span><span>Team der Woche</span><span>Ligen</span></nav><button class="btn" style="width:auto;height:40px;padding:0 18px">Warteliste</button></header>
<div class="wb"><div class="wl"><div class="status"><span class="chip up"><b>●</b> Süper Lig verfügbar</span><span class="chip flat">Premier League bald</span><span class="chip flat">Bundesliga bald</span></div>
<h1 class="h">Jede Zahl hat einen Grund.</h1><p>FootPulse bewertet Spieler nach dem, was auf dem Platz passiert, und erklärt nach jedem Spieltag, warum sich ein Wert bewegt.</p>
<div class="wf"><input class="input" placeholder="deine@mail.de"><button class="btn" style="width:auto;padding:0 22px">Auf die Warteliste</button></div></div>
<div class="wr"><div class="card" style="width:300px;transform:rotate(-2deg);margin-right:150px"><span class="cardline"></span><div class="top2"><div class="ovrbox"><span class="ovr num">88</span><span class="pos label">ST</span></div>{seiten._bew(4)}</div>
<div class="nm h" lang="tr">Kaan Demir</div><div class="stats"><div class="stat">Pace <b>91</b></div><div class="stat">Dribbling <b>86</b></div><div class="stat">Shooting <b>87</b></div><div class="stat">Defending <b>42</b></div></div>
<div class="why"><b>Warum +4?</b> 2 Tore, Pressing 18 % über Schnitt.</div></div>
<div class="card mini2" style="width:190px;position:absolute;right:0;top:250px;transform:rotate(3deg)"><div class="top2"><div class="ovrbox"><span class="ovr num" style="font-size:40px">81</span><span class="pos label">IV</span></div>{seiten._bew(-1)}</div><div class="nm h" style="font-size:18px">D. Moreau</div></div></div></div></section>"""


def homescreen(r):
    fake = "".join(f'<span class="ap"><i style="background:{c}"></i>{n}</span>' for c, n in (("#3b82f6", "Wetter"), ("#22c55e", "Karten"), ("#f59e0b", "Notizen")))
    return f"""<section class="ex" id="ex-homescreen" style="background:linear-gradient(160deg,#4b5b7a,#1f2533)">
<div class="hs">{fake}<span class="ap"><img src="logo/app-icon.svg" alt="">FootPulse</span>{fake}</div></section>"""


def konten():
    k = [("profilbild.svg", "footpulse", "EN"), ("profilbild-bl.svg", "footpulse.bl", "DE"), ("profilbild-pl.svg", "footpulse.pl", "EN"), ("profilbild-sl.svg", "footpulse.sl", "TR")]
    return '<section class="ex" id="ex-konten" style="background:#000">' + "".join(
        f'<div class="ko"><img src="logo/{f}" alt=""><b>{h}</b><small>{s}</small></div>' for f, h, s in k) + "</section>"


def abwertung(r):
    big = "−5" if r != "C" else "Absturz"
    return f"""<section class="ex post dark" id="ex-abwertung" style="width:540px;height:675px">
<div class="grid-bg"></div><div class="in"><div><span class="lgt" style="background:var(--leagueBL)">BL</span><div class="t" style="color:var(--ratingDown);margin-top:14px">Abwertung der Woche</div></div>
<div><div class="big" style="font-size:{170 if r != 'C' else 112}px;color:var(--ratingDown)">{big}</div>
<div class="sub" style="font-size:24px;margin-top:8px">P. Lindqvist · jetzt 77</div>
<div class="s" style="font-size:16px;margin-top:6px">Warum? Drei Spiele ohne Torschuss, Zweikampfquote 38 %.</div></div>
<img src="{LOGO_D}" style="height:24px" alt=""></div></section>"""


def vergleich(r):
    def mk(o, n, pace, akz):
        return (f'<div class="vc" style="border-color:{akz}"><span class="num vo">{o}</span><span class="vn">{n}</span>'
                f'<span class="vs">Pace <b class="num">{pace}</b></span></div>')
    return f"""<section class="ex post" id="ex-vergleich" style="width:540px;height:675px">
<div class="in"><div class="t">Overall ≠ speed</div>
<div style="display:flex;gap:16px;justify-content:center">{mk(64, "A. Şahin", 89, "var(--mkPaper)")}{mk(90, "J. Okafor", 71, "var(--mkInk)")}</div>
<div><div class="hl2">A 64 can be faster than a 90.</div><div class="s" style="font-size:16px;margin-top:8px">Overall compares players. Stats tell what they do.</div>
<img src="{LOGO_W}" style="height:24px;margin-top:16px" alt=""></div></div></section>"""


def totw(r="B"):
    if r == "A":  # Runde 4: nah am heutigen App-TOTW (Burhans Screenshot)
        return f"""<section class="ex post dark" id="ex-totw" style="width:540px;height:675px">
<div class="in" style="padding:22px 22px 18px"><div style="display:flex;justify-content:space-between;align-items:center"><span class="lgt" style="background:var(--leagueSL)">SL</span><span class="t" style="font-size:16px;margin-right:64px" lang="tr">11. Hafta · 4-3-3</span></div>
<div class="hl2" lang="tr" style="margin-top:2px;font-size:36px">Haftanın Takımı</div>
<div style="font-size:7.4px;margin:8px 0 6px">{XI.spielfeld(68)}</div>
<div style="display:flex;justify-content:space-between;align-items:center"><span class="s" style="font-size:14px" lang="tr">MVP: Demir · ★ 9,3 · Neden? Profilde.</span><img src="{LOGO_D}" style="height:20px" alt=""></div></div></section>"""
    pos = [(50, 87, 82, "Iversen"), (16, 66, 79, "Şahin"), (38, 69, 84, "Novak"), (62, 69, 81, "Moreau"), (84, 66, 80, "Brennan"), (26, 45, 86, "Okafor"),
           (50, 48, 83, "Yıldız"), (74, 45, 82, "Lindqvist"), (18, 22, 85, "Silva"), (50, 17, 88, "Demir"), (82, 22, 84, "Öztürk")]
    pm = "".join(f'<div class="pm2{" mvp" if n == "Demir" else ""}" style="left:{x}%;top:{y}%"><b class="num">{o}</b><span lang="tr">{n}</span></div>' for x, y, o, n in pos)
    return f"""<section class="ex post dark" id="ex-totw" style="width:540px;height:675px">
<div class="in" style="padding:24px"><div style="display:flex;justify-content:space-between;align-items:center"><span class="lgt" style="background:var(--leagueSL)">SL</span><span class="t" style="font-size:16px" lang="tr">11. Hafta</span></div>
<div class="hl2" lang="tr" style="margin-top:6px">Haftanın Takımı</div>
<div class="pitch2">{pm}</div>
<div style="display:flex;justify-content:space-between;align-items:center"><span class="s" style="font-size:14px" lang="tr">MVP: Demir · Neden? Profilde.</span><img src="{LOGO_D}" style="height:20px" alt=""></div></div></section>"""


def banter():
    return f"""<section class="ex post dark" id="ex-banter" style="width:540px;height:540px">
<div class="in"><div style="display:flex;justify-content:space-between"><span class="lgt" style="background:var(--leaguePL)">PL</span><span class="t" style="font-size:16px;color:var(--accentText)">Gameweek 11</span></div>
<div class="hl2" style="font-size:44px">Everyone's talking about the goal.<br><span style="color:var(--accentText)">We're talking about the 14 tackles.</span></div>
<div style="display:flex;justify-content:space-between;align-items:center"><span class="s" style="font-size:15px">R. Novak · +2 · now 84</span><img src="{LOGO_D}" style="height:22px" alt=""></div></div></section>"""


def youtube(r):
    return f"""<section class="ex post" id="ex-youtube" style="width:640px;height:360px">
<div class="foto2" style="position:absolute;right:0;top:0;width:330px;height:360px"><span>Platzhalter Foto</span></div>
<div class="in" style="padding:28px;width:340px"><div class="t" style="font-size:20px">Spieltag 11</div>
<div class="hl2" style="font-size:{58 if r != 'C' else 72}px">Warum<br>+4?</div><img src="{LOGO_W}" style="height:22px" alt=""></div>
<div class="yt">12:48</div></section>"""


def umfrage(r):
    return f"""<section class="ex post dark" id="ex-umfrage" style="width:405px;height:720px">
<div class="foto2" style="position:absolute;inset:0;opacity:.5"><span>Platzhalter Videobild</span></div>
<div class="in" style="justify-content:center;gap:22px;padding:30px">
<div class="card" style="width:100%"><span class="cardline"></span><div class="top2"><div class="ovrbox"><span class="ovr num">88</span><span class="pos label">ST</span></div>{seiten._bew(4)}</div><div class="nm h" lang="tr">Kaan Demir</div></div>
<div class="poll"><div class="pq h">Verdient?</div><div class="po"><span class="pa">Ja, klar</span><span class="pb">Zu viel</span></div></div></div></section>"""


EXTRA = {
"A": ".post::after{content:\"\";position:absolute;top:0;right:0;width:0;height:0;border-style:solid;border-width:0 64px 64px 0;border-color:transparent var(--accent) transparent transparent} .post:not(.dark)::after{border-right-color:var(--mkInk)} .post .in{z-index:1} .poll .pa,.poll .pb{clip-path:polygon(0 0,calc(100% - 10px) 0,100% 10px,100% 100%,0 100%)} .vc{clip-path:polygon(0 0,calc(100% - 16px) 0,100% 16px,100% 100%,0 100%)} .hl2{text-transform:uppercase}",
"B": ".poll .pa,.poll .pb{border-radius:999px} .vc{border-radius:14px} .hl2{font-stretch:80%;letter-spacing:-.01em}",
"C": ".post.dark::after{content:\"\";position:absolute;left:0;right:0;bottom:0;height:14px;background:repeating-linear-gradient(-60deg,var(--accent) 0 14px,var(--mkRedDeep) 14px 28px)} .post:not(.dark)::after{content:\"\";position:absolute;inset:0;background:repeating-linear-gradient(-60deg,transparent 0 60px,rgba(0,0,0,.12) 60px 84px)} .post .in{z-index:1} .ex img[src*=kombi-quer]{height:44px!important} .phone .top img,.wh img{height:34px!important} .poll .pa,.poll .pb{border-radius:0} .vc{border-radius:0;border-top-width:10px!important} .hl2{text-transform:uppercase}",
}


def seite(r):
    html = seiten.seite(r)
    css = re.search(r"<style>(.*?)\[data-safe", html, re.S).group(1)
    disp = "var(--font-display)"
    eigen = f"""
body{{background:#5a5a5a}} .wrapx{{display:flex;flex-wrap:wrap;gap:40px;padding:40px;align-items:flex-start}}
.ex{{position:relative;overflow:hidden;flex:none;color:var(--textPrimary);font-family:var(--font-text)}}
.phone{{width:390px;height:844px;background:var(--background);display:flex;flex-direction:column}}
.phone .top{{display:flex;justify-content:space-between;align-items:center;padding:16px 18px 10px}}
.back{{font-size:20px;color:var(--textSecondary)}} .pad{{padding:0 16px;flex:1;overflow:hidden}}
.top2{{display:flex;justify-content:space-between;align-items:flex-start}}
.panel{{background:var(--surface);border:1px solid var(--borderSubtle);padding:12px 14px;margin-top:12px}}
.ph{{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}}
.why2{{margin:0;padding-left:18px;color:var(--textSecondary);font-size:14px;line-height:1.7}} .why2 b{{color:var(--textPrimary)}}
.bn{{display:flex;justify-content:space-around;border-top:1px solid var(--border);background:var(--surfaceDeep);padding:10px 0 24px}}
.bn span{{display:flex;flex-direction:column;align-items:center;gap:4px;font-size:11px;color:var(--textTertiary);font-weight:600}}
.bn i{{width:22px;height:22px;border:2px solid currentColor;border-radius:6px}} .bn .on{{color:var(--textPrimary)}} .bn .on i{{background:var(--accent);border-color:var(--accent)}}
.list{{margin-top:12px;background:var(--surface);border:1px solid var(--borderSubtle)}}
.rr{{display:flex;align-items:center;gap:10px;padding:10px 12px;border-bottom:1px solid var(--borderSubtle)}} .rr.sel{{background:var(--surfaceSelected)}}
.rk{{width:18px;color:var(--textTertiary);font-weight:700}} .rn{{flex:1;display:flex;flex-direction:column;line-height:1.2}} .rn b{{font-size:15px}} .rn small{{color:var(--textTertiary);font-size:12px}}
.ro{{font-family:var(--font-zahl);font-weight:800;font-size:20px;width:30px;text-align:right}}
.wh{{display:flex;align-items:center;gap:40px;padding:22px 48px;border-bottom:1px solid var(--borderSubtle)}} .wh nav{{flex:1;display:flex;gap:28px;color:var(--textSecondary);font-size:15px}}
.wb{{display:flex;padding:70px 48px 0;gap:40px}} .wl{{width:640px}} .wl h1{{font-size:76px;line-height:.95;margin:0 0 20px}} .wl p{{font-size:19px;color:var(--textSecondary);max-width:520px;margin:0 0 28px}}
.wf{{display:flex;gap:10px;max-width:560px}} .wf .input{{flex:1}} .wr{{position:relative;flex:1;display:flex;justify-content:center;padding-top:10px}}
.hs{{display:grid;grid-template-columns:repeat(4,1fr);gap:22px 10px;padding:40px 24px}} .ap{{display:flex;flex-direction:column;align-items:center;gap:6px;color:#fff;font:500 12px system-ui}}
.ap i,.ap img{{width:62px;height:62px;border-radius:15px;display:block}}
#ex-konten{{display:flex;justify-content:space-around;align-items:center;padding:24px}} .ko{{display:flex;flex-direction:column;align-items:center;gap:8px;color:#fff;font:600 14px system-ui}}
.ko img{{width:120px;height:120px;border-radius:50%}} .ko small{{color:#999;font-weight:500}}
.post .in{{position:absolute;inset:0;padding:32px;display:flex;flex-direction:column;justify-content:space-between}}
.lgt{{display:inline-block;padding:4px 10px;font:800 14px var(--font-label);letter-spacing:.08em;color:var(--ratingInk)}}
.hl2{{font-family:{disp};font-weight:800;font-size:48px;line-height:.98}}
.vc{{width:200px;padding:16px;background:var(--mkInk);color:var(--mkPaper);border:3px solid;display:flex;flex-direction:column;gap:6px}}
.vo{{font-family:var(--font-zahl);font-weight:800;font-size:72px;line-height:.9}} .vn{{font-weight:700;font-size:18px}} .vs{{font-size:16px;color:var(--mkPaper)}} .vs b{{font-size:24px;color:var(--ratingUp)}}
.pitch2{{position:relative;flex:1;margin:14px 0;border:2px solid var(--pitchLine);background:var(--pitchGreen)}} .pitch2::before{{content:"";position:absolute;left:0;right:0;top:50%;border-top:2px solid var(--pitchLine)}}
.pm2{{position:absolute;transform:translate(-50%,-50%);width:74px;text-align:center;padding:4px 2px;background:var(--surfaceElevated);border:1px solid var(--border)}}
.pm2 b{{display:block;font-family:var(--font-zahl);font-size:24px;font-weight:800;line-height:1}} .pm2 span{{font-size:11px;font-weight:600}} .pm2.mvp{{border:2px solid var(--gold)}}
.foto2{{background:repeating-linear-gradient(135deg,#2c2f35 0 16px,#363a42 16px 32px);display:flex;align-items:flex-end}} .foto2 span{{color:#cfd2d8;font:600 13px system-ui;padding:12px}}
.yt{{position:absolute;right:10px;bottom:10px;background:rgba(0,0,0,.85);color:#fff;font:600 13px system-ui;padding:2px 6px;border-radius:3px}}
.poll{{background:var(--surfaceElevated);padding:18px;border:1px solid var(--border)}} .pq{{font-size:32px;margin-bottom:12px;text-align:center}}
.po{{display:flex;gap:10px}} .po span{{flex:1;text-align:center;padding:14px 6px;font-weight:700;font-size:17px}}
.pa{{background:var(--accent);color:var(--onAccent)}} .pb{{background:var(--surfaceOverlay);color:var(--textPrimary)}}
"""
    body = "".join([profil("dark"), profil("light"), rangliste(), web(), homescreen(r), konten(), abwertung(r), vergleich(r), totw(r), banter(), youtube(r), umfrage(r)])
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>Beispiele {r} {O.NAME[r]}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{O.SCHRIFT[r]['google']}&display=block" rel="stylesheet">
<link rel="stylesheet" href="tokens.css"><style>{css}{seiten.STIL[r]}{XI.CSS if r == 'A' else ''}{eigen}{EXTRA[r]}</style></head>
<body data-theme="dark"><div class="wrapx">{body}</div></body></html>"""
