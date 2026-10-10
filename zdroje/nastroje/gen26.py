"""MO26.html (zdroje) -> Vzor26_zadanie.html + Vzor26_vypracovanie.html (FYZIKA).
Spustenie: python -I gen26.py <priečinok zdroje> <priečinok FYZIKA>"""
import re, sys, pathlib

SRC = pathlib.Path(sys.argv[1]); DST = pathlib.Path(sys.argv[2])
N = 26
TOPICS = ['Elektrónový obal atómu', 'Elektrický prúd', 'Vlastnosti plynov']

def rep1(old, new, s):
    if s.count(old) != 1:
        raise SystemExit(f'Text sa našiel {s.count(old)}x: {old[:70]}')
    return s.replace(old, new)

def page(n, kind, parts):
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
<title>Vzor {n} – {label}</title>
<link rel="stylesheet" href="mo.css">
</head>
<body class="{'vyp' if vyp else 'zad'}">

<header class="mo-head"><div class="mo-head-in">
<div class="mo-kicker"><span class="mo-num">VZOR {n}</span><span class="mo-kind">{label}</span></div>
<h1>{' · '.join(TOPICS)}</h1>
<p>{sub}</p>
</div></header>

<nav class="mo-bar"><div class="mo-bar-in">
<a class="mo-back" href="index.html">← Všetky vzory</a>
<div class="mo-switch"><a href="Vzor{n}_zadanie.html"{z_on}>Zadanie</a><a href="Vzor{n}_vypracovanie.html"{v_on}>Vypracovanie</a></div>
<button type="button" onclick="window.print()">Tlačiť / PDF</button>
<a class="mo-lang" href="en/Model{n}_{'solutions' if vyp else 'questions'}.html" hreflang="en" title="English version">EN</a>
</div></nav>

<main class="wrap">
{body}
</main>

<footer class="mo-foot"><a href="index.html">← Všetky vzory</a><span>Vzor {n} · {label}</span></footer>
<script src="mo.js"></script>
</body>
</html>
'''

s = (SRC / 'MO26.html').read_text(encoding='utf-8')
s = s.replace('class="eq"', 'class="formula"').replace('class="given"', 'class="task"')
s = s.replace('class="questions"', '').replace('<ol >', '<ol>')
s = re.sub(r'<p class="solution-step">(.*?)</p>', r'<h4>\1</h4>', s)
# texty v SVG: štýl bol v CSS pôvodnej stránky, tu ho dáme priamo do atribútov
s = re.sub(r'<text ([^>]*?)class="minor"', r'<text \1font-size="12" fill="#637889"', s)
s = re.sub(r'<text (?![^>]*font-size)', '<text font-size="14" fill="#253d51" ', s)

# ---- zadanie ----
zad = re.search(r'<div class="question-page">(.*?)<p class="small">Rekonštrukcia', s, re.S).group(1)
z = []
for a in re.findall(r'<article class="task">(.*?)</article>', zad, re.S):
    a = re.sub(r'<div class="task-head"><span class="number">\d</span>(<h2>)(.*?)</h2>\s*</div>',
               lambda m: f'<h2>{len(z) + 1}. {m.group(2)}</h2>', a, flags=re.S)
    z.append(a)
assert len(z) == 3

# ---- vypracovanie ----
v = re.findall(r'<section>(.*?)</section>', s, re.S)
assert len(v) == 3
# odborná oprava obrázka striekačky: pri stláčaní ide piest dnu (menší objem, šípka k ústiu),
# pri rozpínaní von (väčší objem, šípka von); šípky sú nad striekačkou pri tiahle
old_svg = re.search(r'<svg class="diagram" viewBox="0 0 720 195".*?</svg>', v[2], re.S).group(0)
new_svg = '''<svg class="diagram" viewBox="0 0 720 195" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schéma vzduchu v striekačke pri stláčaní a rozpínaní"><text font-size="14" fill="#253d51" x="105" y="28">Rýchle stláčanie</text><text font-size="14" fill="#253d51" x="470" y="28">Rýchle rozpínanie</text><rect x="50" y="68" width="250" height="60" fill="#fff" stroke="#375873" stroke-width="3" rx="6"/><rect x="52" y="70" width="70" height="56" fill="#fde3cf"/><rect x="122" y="70" width="13" height="56" fill="#7e9cb2"/><path d="M135 98 H340" stroke="#375873" stroke-width="6"/><path d="M340 80 V116" stroke="#375873" stroke-width="7"/><path d="M50 92 H30 V104 H50" stroke="#375873" fill="none" stroke-width="4"/><path d="M300 52 H225" stroke="#bb7728" stroke-width="4"/><path d="M237 44 L225 52 L237 60" fill="none" stroke="#bb7728" stroke-width="3"/><text font-size="12" fill="#637889" x="235" y="40">tlačíme</text><text font-size="14" fill="#253d51" x="83" y="158">V ↓, T ↑ (rýchlo)</text><rect x="416" y="68" width="250" height="60" fill="#fff" stroke="#375873" stroke-width="3" rx="6"/><rect x="418" y="70" width="142" height="56" fill="#dcebf7"/><rect x="560" y="70" width="13" height="56" fill="#7e9cb2"/><path d="M573 98 H697" stroke="#375873" stroke-width="6"/><path d="M697 80 V116" stroke="#375873" stroke-width="7"/><path d="M416 92 H396 V104 H416" stroke="#375873" fill="none" stroke-width="4"/><path d="M590 52 H665" stroke="#26724c" stroke-width="4"/><path d="M653 44 L665 52 L653 60" fill="none" stroke="#26724c" stroke-width="3"/><text font-size="12" fill="#637889" x="600" y="40">ťaháme</text><text font-size="14" fill="#253d51" x="472" y="158">V ↑, T ↓ (rýchlo)</text></svg>'''
v[2] = rep1(old_svg, new_svg, v[2])

for name, html in (('zadanie', page(N, 'zad', z)), ('vypracovanie', page(N, 'vyp', v))):
    for bad in ('ekonštru', 'rukopis', 'MO26', 'Otázka', 'maturit'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
