"""MO12_zadanie.html + MO12_vypracovanie.html (zdroje) -> Vzor12_*.html (FYZIKA).
Text a obrázky sa preberajú zo zdroja, menia sa len triedy a obal.
Oprava obrázka pružiny: Δl bolo vyznačené cez výšku závažia, nie ako predĺženie
pružiny; nevysvetlená zvislá úsečka pri stopkách odstránená.
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen12.py"""
import pathlib, re

SRC = pathlib.Path('zdroje'); DST = pathlib.Path('FYZIKA')
N = 12
TOPICS = ['Pevné látky', 'Fotoelektrický jav', 'Zotrvačná hmotnosť']

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
    s = re.sub(r'<figure class="figure">\s*(<svg.*?</svg>)\s*<figcaption>(.*?)</figcaption>\s*</figure>',
               r'\1\n<p class="caption">\2</p>', s, flags=re.S)
    s = s.replace(' xmlns="http://www.w3.org/2000/svg"', '')
    s = s.replace('class="question"', 'class="task"').replace('class="answer"', 'class="result"')
    s = s.replace('class="muted"', 'class="subtle"')
    return s

def casti(html):
    p = re.findall(r'<section[^>]*>(.*?)</section>', html, re.S)
    assert len(p) == 3, len(p)
    return [uprav(x) for x in p]

Z = casti((SRC / 'MO12_zadanie.html').read_text(encoding='utf-8'))
V = casti((SRC / 'MO12_vypracovanie.html').read_text(encoding='utf-8'))

# Δl = predĺženie pružiny: medzi koncom nezaťaženej (prerušovane) a zaťaženej pružiny
V[2] = rep1('<path d="M307 190 V245 M297 190 H317 M297 245 H317" stroke="#cd7340" stroke-width="2.5"/><text x="328" y="223" font-family="Arial" font-size="19" fill="#a65d32">Δl</text>',
            '<path d="M236 140 H322 M260 190 H322" stroke="#8aa0b0" stroke-width="1.5" stroke-dasharray="5 4"/>'
            '<path d="M307 140 V190 M299 140 H315 M299 190 H315" stroke="#cd7340" stroke-width="2.5"/>'
            '<text x="328" y="171" font-family="Arial" font-size="19" fill="#a65d32">Δl</text>'
            '<text x="328" y="137" font-family="Arial" font-size="14" fill="#6b7f8e">bez závažia</text>', V[2])
V[2] = rep1('<path d="M422 75 L422 241 M411 75 H433 M411 241 H433" stroke="#57778a" stroke-width="2"/>', '', V[2])

for name, html in (('zadanie', page('zad', Z)), ('vypracovanie', page('vyp', V))):
    for bad in ('ekonštru', 'rukopis', 'MO12', 'maturit', 'Maturit'):
        assert bad not in html, (name, bad)
    assert html.count('<section') == 3
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
