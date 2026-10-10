"""MO8_zadanie.html + MO8_vypracovanie.html (zdroje) -> Vzor8_*.html (FYZIKA).
Text a obrázky sa preberajú zo zdroja, menia sa len triedy a obal.
Úpravy: nadpis časti 1 „Teoretická a výpočtová časť“ -> názov témy;
v grafe T²(l) bola vodorovná os o 10 px pod nulou stupnice (body sú voči nule správne).
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen8.py"""
import pathlib, re

SRC = pathlib.Path('zdroje'); DST = pathlib.Path('FYZIKA')
N = 8
TOPICS = ['Molekulová fyzika a termodynamika', 'Elektromagnetické vlnenie', 'Matematické kyvadlo']

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
    s = s.replace('class="question"', 'class="task"').replace('class="equation"', 'class="formula"')
    s = s.replace('class="note"', 'class="subtle"')
    s = re.sub(r' width="\d+"(?= viewBox| role)', '', s)   # pevná šírka SVG (riadi ju mo.css)
    s = s.replace('<svg class="diagram" viewBox', '<svg class="diagram" viewBox')
    return s.replace('<h2>1. Teoretická a výpočtová časť</h2>', '<h2>1. Molekulová fyzika a termodynamika</h2>')

def casti(html):
    telo = html[html.index('<h2>'):html.index('<footer>')]
    p = ['<h2' + x for x in telo.split('<h2')[1:]]
    assert len(p) == 3, len(p)
    return [uprav(x) for x in p]

Z = casti((SRC / 'MO8_zadanie.html').read_text(encoding='utf-8'))
V = casti((SRC / 'MO8_vypracovanie.html').read_text(encoding='utf-8'))

# graf T²(l): os x na úrovni nuly stupnice (y = 255), popisy osi x pod ňou
V[2] = rep1('M170 45V265M265 45V265M360 45V265M455 45V265M550 45V265', 'M170 45V255M265 45V255M360 45V255M455 45V255M550 45V255', V[2])
V[2] = rep1('<path d="M75 35V265H565"', '<path d="M75 35V255H565"', V[2])
V[2] = V[2].replace('y="288">', 'y="276">')
V[2] = rep1('<text x="552" y="292">l (m)</text>', '<text x="552" y="298">l (m)</text>', V[2])

for name, html in (('zadanie', page('zad', Z)), ('vypracovanie', page('vyp', V))):
    for bad in ('ekonštru', 'rukopis', 'MO8', 'maturit', 'Maturit', 'Teoretická a výpočtová časť'):
        assert bad not in html, (name, bad)
    assert html.count('<section') == 3
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
