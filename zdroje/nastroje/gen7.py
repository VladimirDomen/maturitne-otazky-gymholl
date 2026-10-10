"""MO7_zadanie.html + MO7_vypracovanie.html (zdroje) -> Vzor7_*.html (FYZIKA).
Text a obrázky sa preberajú zo zdroja, menia sa len triedy a obal.
Opravy: šípka dopadajúceho lúča smerovala od rozhrania; graf sin α – sin β
mal nepresné body a priamku so sklonom ≈ 1,65 namiesto n ≈ 1,49.
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen7.py"""
import math, pathlib, re

SRC = pathlib.Path('zdroje'); DST = pathlib.Path('FYZIKA')
N = 7
TOPICS = ['Mechanika tuhého telesa', 'Striedavý prúd', 'Index lomu svetla']

def page(kind, parts):
    vyp = kind == 'vyp'
    label = 'Vypracovanie' if vyp else 'Zadanie'
    sub = 'Podrobné vypracovanie s vysvetlením' if vyp else 'Fyzika · 3 tematické časti'
    body = ''.join(f'\n<section class="sheet" id="cast-{i}"><div class="topline">Časť {i} z {len(parts)}</div>\n{p.strip()}\n</section>\n'
                   for i, p in enumerate(parts, 1))
    z_on, v_on = ('', ' class="on"') if vyp else (' class="on"', '')
    return f'''<!DOCTYPE html>
<html lang="sk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Vzor {N} – {label}</title>
<link rel="stylesheet" href="mo.css">
</head>
<body class="{'vyp' if vyp else 'zad'}">

<header class="mo-head"><div class="mo-head-in">
<div class="mo-kicker"><span class="mo-num">VZOR {N}</span><span class="mo-kind">{label}</span></div>
<h1>{' · '.join(TOPICS)}</h1>
<p>{sub}</p>
</div></header>

<nav class="mo-bar"><div class="mo-bar-in">
<a class="mo-back" href="index.html">← Všetky vzory</a>
<div class="mo-switch"><a href="Vzor{N}_zadanie.html"{z_on}>Zadanie</a><a href="Vzor{N}_vypracovanie.html"{v_on}>Vypracovanie</a></div>
<button type="button" onclick="window.print()">Tlačiť / PDF</button>
<a class="mo-lang" href="en/Model{N}_{'solutions' if vyp else 'questions'}.html" hreflang="en" title="English version">EN</a>
</div></nav>

<main class="wrap">
{body}
</main>

<footer class="mo-foot"><a href="index.html">← Všetky vzory</a><span>Vzor {N} · {label}</span></footer>
<script src="mo.js"></script>
</body>
</html>
'''

def rep1(old, new, s):
    if s.count(old) != 1:
        raise SystemExit(f'Text sa našiel {s.count(old)}x: {old[:70]}')
    return s.replace(old, new)

def uprav(s):
    """triedy zdroja -> triedy mo.css"""
    s = re.sub(r'<div class="diagram">\s*(<svg.*?</svg>)\s*<div class="caption">(.*?)</div>\s*</div>',
               r'\1\n<p class="caption">\2</p>', s, flags=re.S)
    s = s.replace('<svg viewBox', '<svg class="diagram" role="img" viewBox')
    s = s.replace('class="eq"', 'class="formula"').replace('class="answer"', 'class="result"')
    s = s.replace('class="small"', 'class="subtle"').replace(' class="pagebreak"', '')
    return s

def casti(html, zaciatok, koniec):
    telo = html[html.index(zaciatok) + len(zaciatok):html.index(koniec)]
    p = ['<h2' + x for x in telo.split('<h2')[1:]]
    assert len(p) == 3, len(p)
    return [uprav(x) for x in p]

# ---------- graf sin α – sin β v mierke ----------
def svg_graf():
    X0, Y0, SX, SY = 85, 265, (569 - 85) / 0.6, (265 - 28) / 1.0
    X = lambda v: X0 + SX * v
    Y = lambda v: Y0 - SY * v
    data = [(20, 13.3), (30, 19.6), (40, 25.6), (50, 30.9), (60, 35.5)]
    n = 1.490
    body = ''.join(f'<circle cx="{X(math.sin(math.radians(b))):.1f}" cy="{Y(math.sin(math.radians(a))):.1f}" r="6"/>' for a, b in data)
    return ('<svg class="diagram" role="img" viewBox="0 0 690 330" aria-label="Graf sínusu uhla dopadu v závislosti od sínusu uhla lomu">'
            '<path d="M85 28V265H630" stroke="#334f67" stroke-width="2.5" fill="none"/>'
            '<g stroke="#e2e9ed" stroke-width="1"><path d="M85 206H630M85 147H630M85 88H630M206 28V265M327 28V265M448 28V265M569 28V265"/></g>'
            f'<path d="M85 265L{X(1 / n):.1f} 28" stroke="#267baf" stroke-width="3"/>'
            f'<g fill="#bd6b34">{body}</g>'
            '<g font-family="Arial" font-size="18" fill="#425b6a"><text x="285" y="313">sin β</text><text x="96" y="20">sin α</text>'
            '<text x="75" y="282">0</text><text x="327" y="282" text-anchor="middle">0,3</text><text x="569" y="282" text-anchor="middle">0,6</text>'
            '<text x="44" y="151">0,5</text><text x="44" y="32">1,0</text><text x="400" y="45" fill="#267baf">smernica ≈ n</text></g></svg>')

# ---------- zadanie ----------
z_src = (SRC / 'MO7_zadanie.html').read_text(encoding='utf-8')
Z = casti(z_src, '</p>', '<p class="small">Poznámka')   # od úvodného odseku po poznámku o rekonštrukcii

# ---------- vypracovanie ----------
v_src = (SRC / 'MO7_vypracovanie.html').read_text(encoding='utf-8')
V = casti(v_src, '</p>', '<div class="foot">')
V[2] = rep1('V zadaní sa odkazuje na žiakove laboratórne poznámky. Nasleduje',
            'Zadanie odkazuje na postup z laboratórnych cvičení. Nasleduje', V[2])
# šípka dopadajúceho lúča: hrot v strede lúča smerom k rozhraniu (pôvodne na začiatku, opačne)
V[2] = rep1('M184 46L167 43L172 61 M481 349L482 372L461 363', 'M251.4 124.4L271 129L262.8 110.6 M481 349L482 372L461 363', V[2])
# popisy, ktoré prekrývali lúč, presunuté do voľného miesta
V[2] = rep1('<text x="40" y="65" font-size="24" fill="#244960">vzduch n₁ ≈ 1</text>',
            '<text x="520" y="65" font-size="24" fill="#244960">vzduch n₁ ≈ 1</text>', V[2])
V[2] = rep1('<text x="186" y="99" font-size="21" fill="#a33d29">dopadajúci lúč</text>',
            '<text x="60" y="150" font-size="21" fill="#a33d29">dopadajúci lúč</text>', V[2])
stary = re.search(r'<svg class="diagram" role="img" viewBox="0 0 690 330".*?</svg>', V[2], re.S).group(0)
V[2] = rep1(stary, svg_graf(), V[2])

for name, html in (('zadanie', page('zad', Z)), ('vypracovanie', page('vyp', V))):
    for bad in ('ekonštru', 'rukopis', 'MO7', 'maturit', 'Maturit', 'žiakove'):
        assert bad not in html, (name, bad)
    assert html.count('<section') == 3
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
