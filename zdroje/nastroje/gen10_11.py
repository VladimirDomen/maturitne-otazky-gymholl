"""MO10_* a MO11_* (zdroje) -> Vzor10_*.html a Vzor11_*.html (FYZIKA).
Text a obrázky sa preberajú zo zdroja; odborné chyby sa nenašli.
Zadania: obsah časti sa vkladá do rámčeka úlohy (ako pri ostatných vzoroch).
MO11: päta s odkazom NIST rozdelená k ortuti (časť 1) a k optike (časť 2).
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen10_11.py"""
import pathlib, re

SRC = pathlib.Path('zdroje'); DST = pathlib.Path('FYZIKA')
TOPICS = {
    10: ['Vlastnosti plynov', 'Tlak v pneumatike', 'Duté guľové zrkadlo'],
    11: ['Vlastnosti kvapalín', 'Interferencia na tenkej vrstve', 'Voltampérová charakteristika diódy'],
}

def page(N, kind, parts):
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
<h1>{' · '.join(TOPICS[N])}</h1>
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
    s = s.replace('class="note"', 'class="subtle"')
    s = s.replace('<svg viewBox', '<svg class="diagram" viewBox')
    return s

def casti(html):
    koniec = html.index('<footer>') if '<footer>' in html else html.index('</main>')
    telo = html[html.index('<h2>'):koniec]
    p = ['<h2' + x for x in telo.split('<h2')[1:]]
    assert len(p) == 3, len(p)
    return [uprav(x) for x in p]

def ramcek(p):
    """obsah zadania za posledným nadpisom do rámčeka úlohy"""
    i = max(p.rfind('</h2>'), p.rfind('</h3>'))
    i = p.index('>', i) + 1
    return p[:i] + '\n<div class="task">' + p[i:].strip() + '</div>'

vystup = {}
for N in (10, 11):
    Z = [ramcek(x) for x in casti((SRC / f'MO{N}_zadanie.html').read_text(encoding='utf-8'))]
    v_src = (SRC / f'MO{N}_vypracovanie.html').read_text(encoding='utf-8')
    V = casti(v_src)
    if N == 10:   # popis a = 1 cm prekrýval odrazený lúč
        V[2] = rep1('<text x="365" y="315">a = 1 cm</text>', '<text x="398" y="345">a = 1 cm</text>', V[2])
        V[2] = rep1('<text x="563" y="315">|a′| = 2 cm</text>', '<text x="563" y="345">|a′| = 2 cm</text>', V[2])
    if N == 11:
        V[0] = V[0].rstrip() + ('\n<p class="subtle">Tabuľková hodnota rozťažnosti ortuti je zaokrúhlená na 1,82 × 10⁻⁴ K⁻¹. '
                                'Referencia k teplotnej závislosti: <a href="https://www.nist.gov/system/files/documents/srd/jpcrd483.pdf">'
                                'údaje o hustote a rozťažnosti ortuti (NIST)</a>.</p>')
        V[1] = V[1].rstrip() + '\n<p class="subtle">Všetky optické výsledky platia pre podmienky uvedené v zadaní.</p>'
    vystup[N] = (Z, V)

for N, (Z, V) in vystup.items():
    for name, html in (('zadanie', page(N, 'zad', Z)), ('vypracovanie', page(N, 'vyp', V))):
        for bad in ('ekonštru', 'rukopis', f'MO{N}', 'maturit', 'Maturit', 'Otázka č.'):
            assert bad not in html, (N, name, bad)
        assert html.count('<section') == 3
        (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
        print('ok', N, name, len(html))
