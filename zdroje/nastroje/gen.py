import re, sys, pathlib

SRC = pathlib.Path(sys.argv[1])   # záloha originálov
DST = pathlib.Path(sys.argv[2])   # cieľový priečinok

def load(name):
    return (SRC / name).read_text(encoding='utf-8')

def sub1(pattern, repl, s, flags=re.S):
    """Nahradí presne jeden výskyt, inak chyba (aby sa nič nestratilo potichu)."""
    new, n = re.subn(pattern, repl, s, flags=flags)
    if n != 1:
        raise SystemExit(f'Vzor sa našiel {n}x: {pattern[:70]}')
    return new

def rep1(old, new, s):
    if s.count(old) != 1:
        raise SystemExit(f'Text sa našiel {s.count(old)}x: {old[:70]}')
    return s.replace(old, new)

def sections(html):
    return re.findall(r'<section\b[^>]*>(.*?)</section>', html, re.S)

def strip_topline(inner):
    return re.sub(r'^\s*<div class="topline">.*?</div>', '', inner, count=1, flags=re.S)

def common(s):
    s = s.replace('viewbox=', 'viewBox=')
    s = s.replace('class="figcaption"', 'class="caption"')
    s = s.replace('class="meta"', 'class="fill"')
    return s

TOPICS = {
    1: ['Mechanika kvapalín a plynov', 'Striedavý prúd – transformátor', 'Disperzia svetla'],
    2: ['Gravitačné pole', 'Mechanické vlnenie', 'Elektrický prúd'],
    3: ['Pohyb v gravitačnom poli', 'Interferencia vlnenia', 'Vznik elektrického prúdu'],
    4: ['Kinematika hmotného bodu', 'Magnetické pole', 'Mikrosvet'],
}

def page(n, kind, parts):
    vyp = kind == 'vyp'
    label = 'Vypracovanie' if vyp else 'Zadanie'
    sub = ('Podrobné vypracovanie s vysvetlením' if vyp
           else 'Fyzika · 3 tematické časti')
    body = ''
    for i, inner in enumerate(parts, 1):
        body += (f'\n<section class="sheet" id="cast-{i}">'
                 f'<div class="topline">Časť {i} z {len(parts)}</div>\n'
                 f'{inner.strip()}\n</section>\n')
    z_on = '' if vyp else ' class="on"'
    v_on = ' class="on"' if vyp else ''
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
<h1>{' · '.join(TOPICS[n])}</h1>
<p>{sub}</p>
</div></header>

<nav class="mo-bar"><div class="mo-bar-in">
<a class="mo-back" href="index.html">← Všetky vzory</a>
<div class="mo-switch"><a href="Vzor{n}_zadanie.html"{z_on}>Zadanie</a><a href="Vzor{n}_vypracovanie.html"{v_on}>Vypracovanie</a></div>
<button type="button" onclick="window.print()">Tlačiť / PDF</button>
</div></nav>

<main class="wrap">
{body}
</main>

<footer class="mo-foot"><a href="index.html">← Všetky vzory</a><span>Vzor {n} · {label}</span></footer>
</body>
</html>
'''

out = {}

# ================= MO1 =================
src = common(load('MO1.html'))
src = src.replace('class="eq answer"', 'class="formula hl"').replace('class="eq"', 'class="formula"')
src = src.replace('class="box"', 'class="task"').replace('class="answer"', 'class="hl"')

assign = re.search(r'<section id="assignment"><h2>Zadanie</h2>(.*?)</section>', src, re.S).group(1)
a_parts = re.split(r'<h3>(?=\d\. )', assign)[1:]
z = []
for p in a_parts:
    title, rest = p.split('</h3>', 1)
    z.append(f'<h2>{title}</h2>{rest}')
# časť 1: poznámka o variantoch g bez zmienky o neistých údajoch
z[0] = rep1('Hmotnosť je zatiaľ neistá a pôvodná hodnota g nie je známa. Vypočítajte varianty g = 9,81 m/s² a g = 10 m/s².',
            'Úlohu riešte pre g = 9,81 m/s² aj pre g = 10 m/s² a výsledky porovnajte.', z[0])
z[0] = rep1('<ol>', '<h3>Teoretická časť</h3>\n<ol>', z[0])
z[0] = rep1('<div class="task"><strong>Výpočtová úloha – určenie materiálu gule</strong>',
            '<h3>Výpočtová úloha – určenie materiálu gule</h3>\n<div class="task">', z[0])
z[1] = rep1('<p>Vysvetlite princíp', '<h3>Teoretická časť</h3>\n<p>Vysvetlite princíp', z[1])
z[1] = rep1('<div class="task">', '<h3>Výpočtová úloha</h3>\n<div class="task">', z[1])
out['Vzor1_zadanie.html'] = page(1, 'zad', z)

sol = re.search(r'<section id="solution">.*?VYPRACOVANIE</div>(.*?)</section>', src, re.S).group(1)
v = ['<h2>' + p for p in sol.split('<h2>')[1:]]
v[0] = sub1(r'<div class="note"><strong>Záver:</strong> Materiál sa z rekonštruovaných údajov nedá jednoznačne určiť\.',
            '<div class="note"><strong>Záver:</strong> Materiál nemožno jednoznačne určiť, výsledok citlivo závisí od použitej hodnoty g.', v[0])
v[0] = rep1(' Treba overiť hmotnosť, silu, použitú hodnotu g a prípadnú toleranciu.', '', v[0])
out['Vzor1_vypracovanie.html'] = page(1, 'vyp', v)

# ================= MO2 =================
s = common(load('MO2_zadanie.html'))
z = [strip_topline(x) for x in sections(s)]
z[0] = sub1(r'\s*<div class="note warning"><strong>Poznámka k rekonštrukcii:</strong>.*?</div>', '', z[0])
z[1] = sub1(r'\s*<div class="note warning"><strong>Predpoklady rekonštrukcie:</strong>.*?</div>', '', z[1])
out['Vzor2_zadanie.html'] = page(2, 'zad', z)

s = common(load('MO2_vypracovanie.html'))
v = [strip_topline(x) for x in sections(s)]
# odborná oprava: zhoda zrýchlenia a intenzity platí v každom mieste poľa, nielen na povrchu
v[0] = rep1('Na povrchu je gravitačné zrýchlenie spôsobené gravitačným poľom číselne zhodné s intenzitou',
            'V každom mieste poľa je gravitačné zrýchlenie číselne zhodné s intenzitou', v[0])
v[1] = rep1('Na zvolených vzorových grafoch sa v rozsahu', 'Na grafoch sa v rozsahu', v[1])
v[1] = sub1(r'\s*<div class="note warning"><strong>Dôležité:</strong>.*?</div>', '', v[1])
v[2] = rep1('Tieto číselné hodnoty slúžia len ako ukážka postupu; v pôvodnej poznámke nie sú zadané.',
            'Číselné hodnoty sú ilustračné, slúžia ako ukážka postupu.', v[2])
# odborná oprava schémy: záporný pól batérie má byť kratšia (hrubšia) čiara
v[2] = rep1('<path d="M76 140 H124 M76 157 H124" fill="none" stroke="#203d60" stroke-width="3"></path>',
            '<path d="M76 140 H124" fill="none" stroke="#203d60" stroke-width="3"></path>', v[2])
v[2] = rep1('<path d="M88 140 H112" stroke="#203d60" stroke-width="5"></path><path d="M94 157 H106" stroke="#203d60" stroke-width="2"></path>',
            '<path d="M88 157 H112" stroke="#203d60" stroke-width="6"></path>', v[2])
out['Vzor2_vypracovanie.html'] = page(2, 'vyp', v)

# ================= MO3 =================
s = common(load('MO3_zadanie.html'))
z = sections(s)
z[1] = sub1(r'\s*<div class="note"><strong>Poznámka k rekonštrukcii:</strong>.*?</div>', '', z[1])
out['Vzor3_zadanie.html'] = page(3, 'zad', z)

s = common(load('MO3_vypracovanie.html'))
v = sections(s)
v[1] = sub1(r'\s*<div class="note">Frekvencia 245 Hz je pracovná rekonštrukcia\..*?</div>', '', v[1])
out['Vzor3_vypracovanie.html'] = page(3, 'vyp', v)

# ================= MO4 =================
s = common(load('MO4_zadanie.html'))
z = sections(s)
z[2] = sub1(r'<div style="height:165px;border-bottom:1px dashed #ccd6e1" aria-label="Priestor na náčrt grafu"></div>',
            '<div class="sketch" aria-label="Priestor na náčrt grafu"></div>', z[2])
out['Vzor4_zadanie.html'] = page(4, 'zad', z)

s = common(load('MO4_vypracovanie.html')).replace('class="answer"', 'class="result"')
v = sections(s)
v[0] = sub1(r'\s*<div class="note"><b>Poznámka k rekonštrukcii:</b>.*?</div>', '', v[0])
out['Vzor4_vypracovanie.html'] = page(4, 'vyp', v)

for name, html in out.items():
    assert html.count('<section') == 3, name
    for bad in ('rekonštru', 'Rekonštru', 'fotograf', 'rukopis', 'pôvodn', 'originál'):
        if bad in html:
            print('POZOR', name, bad)
    (DST / name).write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
