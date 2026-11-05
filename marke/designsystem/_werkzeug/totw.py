"""Team der Woche (FootPulse XI) für Option A, nah am heutigen App-Aufbau (Burhans Screenshot vom 05.11.2026).

Aufbau wie heute: Spielerkarte mit Position, NOW-Wert, rundem Foto, Name, Beitrags-Chip (Tore/Vorlagen) und Noten-Chip.
MVP mit Krone. Neu ist nur die Gestaltung aus A: Farben aus den Tokens, eckige Karten mit Schräge, A-Schriften.
Alle Spieler sind erfunden. Fotos sind Platzhalter (Initialen), bis frei lizenzierte Bilder da sind.
"""

# Position, Name, NOW, Note, Tore, Vorlagen, x %, y %
XI = [
    ("Winger", "Silva", 76, 8.4, 2, 0, 17, 11), ("ST", "Demir", 88, 9.3, 3, 0, 50, 11), ("Winger", "Öztürk", 73, 7.9, 1, 0, 83, 11),
    ("DM", "Okafor", 72, 7.4, 0, 1, 17, 36), ("CM", "Yıldız", 71, 8.1, 1, 0, 50, 36), ("AM", "Brennan", 71, 7.5, 1, 0, 83, 36),
    ("FB/WB", "Şahin", 73, 8.4, 0, 2, 11, 62), ("CB", "Novak", 82, 8.6, 1, 0, 37, 64), ("CB", "Moreau", 84, 8.2, 1, 0, 63, 64),
    ("FB/WB", "Lindqvist", 84, 7.3, 0, 0, 89, 62), ("GK", "Iversen", 72, 7.7, 0, 1, 50, 88),
]
MVP = "Demir"

BALL = ('<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.6" fill="none" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M8 4.6l3 2.2-1.1 3.6H6.1L5 6.8z" fill="currentColor"/></svg>')
SCHUH = ('<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M1.5 6.5h4l1.2 1.6 3.3.6c2.6.5 4.5 1.4 4.5 3v.8H1.5z" fill="currentColor"/>'
         '<path d="M2 13.6h12.5" stroke="currentColor" stroke-width="1.2"/></svg>')


def _komma(v):
    return f"{v:.1f}".replace(".", ",")


def _stufe(v):
    return "elite" if v >= 9 else "excellent" if v >= 8 else "good" if v >= 7 else "average" if v >= 6 else "poor"


def _karte(pos, name, now, note, tore, vorl, x, y):
    mvp = name == MVP
    beitrag = ""
    if tore:
        beitrag = f'<span class="xb" title="{tore} Tore">{BALL}{tore}</span>'
    elif vorl:
        beitrag = f'<span class="xb xa" title="{vorl} Vorlagen">{SCHUH}{vorl}</span>'
    ini = "".join(w[0] for w in name.split())[:2].upper()
    return (f'<div class="xk{" mvp" if mvp else ""}" style="left:{x}%;top:{y}%">'
            f'{"<span class=xm>♛ MVP</span>" if mvp else ""}'
            f'<div class="xh"><span class="xp">{pos}</span><span class="xo"><small>NOW</small>{now}</span></div>'
            f'<div class="xf" aria-hidden="true">{ini}</div><div class="xn" lang="tr">{name}</div>'
            f'<div class="xc">{beitrag}<span class="xr n-{_stufe(note)}">★ {_komma(note)}</span></div></div>')


def spielfeld(hoehe_em=68):
    karten = "".join(_karte(*s) for s in XI)
    return (f'<div class="xpitch" style="height:{hoehe_em}em"><span class="xl1"></span><span class="xl2"></span>'
            f'<span class="xbox1"></span><span class="xbox2"></span>{karten}</div>')


def app_block(groesse=10):
    """Wie der heutige TOTW-Tab: Kopf mit Logo-Kachel, Woche, Formation, Spielfeld, Summenzeile."""
    tore = sum(s[4] for s in XI)
    vorl = sum(s[5] for s in XI)
    schnitt = sum(s[3] for s in XI) / len(XI)
    return f"""<div class="xwrap" style="font-size:{groesse}px">
<div class="xtop"><span class="xtile">{PULS}</span><div><div class="xt">FootPulse XI</div><div class="xs">Spieltag 11 · Woche vom 03.11.2026</div></div><span class="xform">4-3-3</span></div>
{spielfeld()}
<div class="xsum"><div><span>★</span><b class="num">{_komma(schnitt)}</b><small>Ø Note</small></div><div><span>{BALL}</span><b class="num">{tore}</b><small>Tore</small></div><div><span>{SCHUH}</span><b class="num">{vorl}</b><small>Vorlagen</small></div></div>
</div>"""


PULS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2 13h5l2-5 3 10 3-8 2 3h5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/></svg>'

CSS = """
.xwrap{width:42em;background:var(--surface);border:1px solid var(--borderSubtle);position:relative;padding:1.6em 1.6em 1.2em;
  clip-path:polygon(0 0,calc(100% - 1.6em) 0,100% 1.6em,100% 100%,0 100%)}
.xwrap::before{content:"";position:absolute;left:18%;right:18%;top:0;height:2px;background:var(--gold)}
.xtop{display:flex;align-items:center;gap:1.1em;margin-bottom:1.4em}
.xtile{width:4.4em;height:4.4em;display:grid;place-items:center;background:var(--accentMuted);color:var(--accentText);flex:none}
.xtile svg{width:2.4em;height:2.4em}
.xt{font-family:var(--font-display);font-weight:800;font-size:2.4em;line-height:1;color:var(--textPrimary)}
.xs{font-family:var(--font-label);font-size:1.4em;color:var(--textTertiary);margin-top:.2em}
.xform{margin-left:auto;font-family:var(--font-display);font-weight:800;font-size:2.2em;color:var(--textSecondary)}
.xpitch{position:relative;background:var(--pitchGreen);border:2px solid var(--pitchLine);overflow:visible}
.xl1{position:absolute;left:0;right:0;top:50%;border-top:2px solid var(--pitchLine)}
.xl2{position:absolute;left:50%;top:50%;width:11em;height:11em;margin:-5.5em 0 0 -5.5em;border:2px solid var(--pitchLine);border-radius:50%}
.xbox1,.xbox2{position:absolute;left:28%;width:44%;height:11%;border:2px solid var(--pitchLine)}.xbox1{top:-2px;border-top:0}.xbox2{bottom:-2px;border-bottom:0}
.xk{position:absolute;transform:translate(-50%,-50%);width:9.4em;padding:.6em .6em .7em;background:var(--surfaceElevated);border:1px solid var(--border);
  display:flex;flex-direction:column;align-items:center;gap:.35em;clip-path:polygon(0 0,calc(100% - .9em) 0,100% .9em,100% 100%,0 100%)}
.xk.mvp{border:2px solid var(--gold);clip-path:none;overflow:visible}
.xm{position:absolute;top:-1.1em;left:50%;transform:translateX(-50%);background:var(--gold);color:var(--ratingInk);font:800 1em var(--font-label);letter-spacing:.06em;padding:.1em .6em;white-space:nowrap}
.xh{display:flex;justify-content:space-between;align-items:baseline;width:100%}
.xp{font-family:var(--font-label);font-weight:600;font-size:1.05em;color:var(--textTertiary);letter-spacing:.03em}
.xo{font-family:var(--font-display);font-weight:800;font-size:1.9em;line-height:1;color:var(--goldText);font-variant-numeric:tabular-nums}
.xo small{font-family:var(--font-label);font-size:.42em;font-weight:600;color:var(--textMuted);margin-right:.25em;letter-spacing:.06em}
.xf{width:3.1em;height:3.1em;border-radius:50%;display:grid;place-items:center;background:linear-gradient(160deg,var(--surfaceOverlay),var(--surfaceDeep));
  border:2px solid var(--goldMuted);color:var(--textSecondary);font:700 1.5em/1 var(--font-display)}
.xn{font-family:var(--font-display);font-weight:700;font-size:1.3em;line-height:1.1;color:var(--textPrimary);white-space:nowrap}
.xc{display:flex;gap:.4em;align-items:center;justify-content:center}
.xb{display:inline-flex;align-items:center;gap:.2em;height:2em;padding:0 .45em;border:1px solid var(--goldMuted);color:var(--goldText);font:700 1.1em var(--font-display)}
.xb svg{width:1.1em;height:1.1em}.xb.xa{border-color:var(--positiveMuted);color:var(--ratingUp)}
.xr{display:inline-flex;align-items:center;height:2em;padding:0 .5em;font:800 1.2em var(--font-display);color:var(--ratingInk);font-variant-numeric:tabular-nums}
.xr.n-elite{background:var(--ratingElite)}.xr.n-excellent{background:var(--ratingExcellent)}.xr.n-good{background:var(--ratingGood)}
.xr.n-average{background:var(--ratingAverage)}.xr.n-poor{background:var(--ratingPoor);color:var(--onRatingPoor)}
.xsum{display:grid;grid-template-columns:repeat(3,1fr);margin-top:1.2em;background:var(--surfaceDeep);border:1px solid var(--borderSubtle)}
.xsum div{display:flex;flex-direction:column;align-items:center;padding:.8em 0;gap:.1em;color:var(--textSecondary)}
.xsum div+div{border-left:1px solid var(--borderSubtle)}
.xsum span{font-size:1.6em;line-height:1;display:inline-flex}.xsum span svg{width:1em;height:1em}
.xsum b{font-family:var(--font-display);font-size:2.2em;line-height:1;color:var(--textPrimary)}
.xsum small{font-family:var(--font-label);font-size:1.1em;color:var(--textMuted);text-transform:uppercase;letter-spacing:.06em}
"""
