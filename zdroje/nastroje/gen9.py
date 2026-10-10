"""MO9_zadanie.html + MO9_vypracovanie.html (zdroje) -> Vzor9_*.html (FYZIKA).
Text a obrázky sa preberajú zo zdroja, menia sa len triedy a obal.
Odborné chyby sa nenašli; menia sa len triedy a obal (bez „Otázka č. 9“ a päty MO9).
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen9.py"""
import pathlib, re

SRC = pathlib.Path('zdroje'); DST = pathlib.Path('FYZIKA')
N = 9
TOPICS = ['Zmeny skupenstva', 'Elektrón v elektrickom poli', 'Postupné priečne vlnenie']

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
    return s

def casti(html):
    telo = html[html.index('<h2>'):html.index('<footer>')]
    p = ['<h2' + x for x in telo.split('<h2')[1:]]
    assert len(p) == 3, len(p)
    return [uprav(x) for x in p]

Z = casti((SRC / 'MO9_zadanie.html').read_text(encoding='utf-8'))
V = casti((SRC / 'MO9_vypracovanie.html').read_text(encoding='utf-8'))

# fázový diagram: popisy ležali na krivkách / na trojnom bode -> posunuté vedľa
for stare, nove in (
    ('<text x="115" y="278">sublimácia</text>', '<text x="100" y="262">sublimácia</text>'),
    ('<text x="275" y="185" transform="rotate(-68 275 185)">topenie</text>', '<text x="292" y="192" transform="rotate(-68 292 192)">topenie</text>'),
    ('<text x="335" y="214">vyparovanie</text>', '<text x="365" y="238">vyparovanie</text>'),
    ('<text x="175" y="232">trojný bod</text>', '<text x="230" y="234" text-anchor="end">trojný bod</text>'),
):
    V[0] = rep1(stare, nove, V[0])

for name, html in (('zadanie', page('zad', Z)), ('vypracovanie', page('vyp', V))):
    for bad in ('ekonštru', 'rukopis', 'MO9', 'maturit', 'Maturit', 'Otázka č.'):
        assert bad not in html, (name, bad)
    assert html.count('<section') == 3
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
