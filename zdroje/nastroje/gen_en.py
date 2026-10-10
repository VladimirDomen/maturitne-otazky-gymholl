"""Anglická verzia: en/ModelN_questions.html + en/ModelN_solutions.html.
Text je v nastroje/en/mN_q.html a mN_s.html (časti oddelené <!--PART-->,
obrázky ako {{SVGi}} = i-ty obrázok zo slovenskej stránky, popisy sa preložia
podľa SVG_EN). Do slovenských stránok doplní prepínač EN.
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen_en.py"""
import re, sys, pathlib

ROOT = pathlib.Path('FYZIKA'); EN = ROOT / 'en'; TXT = pathlib.Path(__file__).parent / 'en'
EN.mkdir(exist_ok=True)

TOPICS = {
    1: ['Mechanics of Fluids', 'Alternating Current – Transformer', 'Dispersion of Light'],
    2: ['Gravitational Field', 'Mechanical Waves', 'Electric Current'],
    3: ['Motion in a Gravitational Field', 'Interference of Waves', 'Origin of Electric Current'],
    4: ['Kinematics of a Particle', 'Magnetic Field', 'The Microworld'],
    5: ['Dynamics', 'Electromagnetic Induction', 'Nuclear Power Plant'],
    6: ['Energy of a Particle', 'Oscillator', 'Electric Circuit'],
    7: ['Mechanics of a Rigid Body', 'Alternating Current', 'Refractive Index of Light'],
    26: ['Electron Shell of the Atom', 'Electric Current', 'Properties of Gases'],
}

SVG_EN = {
    'Schéma: modré rovnobežné lúče sa sústreďujú bližšie za šošovkou než červené':
        'Diagram: parallel blue rays are focused closer behind the lens than red rays',
    'F modré': 'F blue', 'F červené': 'F red', 'spojná šošovka': 'converging lens',
    'Energetické hladiny a prechody – absorpcia nahor a emisia nadol':
        'Energy levels and transitions – absorption upwards, emission downwards',
    'Vyššia energetická hladina': 'Higher energy level', 'Nižšia energetická hladina': 'Lower energy level',
    'absorpcia': 'absorption', 'energia atómu rastie': 'energy of the atom increases',
    'emisia': 'emission', 'energia atómu klesá': 'energy of the atom decreases',
    'Schéma vzduchu v striekačke pri stláčaní a rozpínaní': 'Air in a syringe during compression and expansion',
    'Rýchle stláčanie': 'Rapid compression', 'Rýchle rozpínanie': 'Rapid expansion',
    'tlačíme': 'push', 'ťaháme': 'pull',
    'V ↓, T ↑ (rýchlo)': 'V ↓, T ↑ (rapid)', 'V ↑, T ↓ (rýchlo)': 'V ↑, T ↓ (rapid)',
    'Sínusový graf od 0 po 12 s amplitúdou 0,2, vyznačené body A a B':
        'Sine graph from 0 to 12 with amplitude 0.2, points A and B marked',
    '+0,2': '+0.2', '−0,2': '−0.2',
    'Elektrický obvod: ampérmeter a rezistor v sérii, voltmeter paralelne k rezistoru':
        'Electric circuit: ammeter and resistor in series, voltmeter in parallel with the resistor',
    'Zdroj napätia – A v sérii – V paralelne k R': 'Voltage source – A in series – V in parallel with R',
    'Stojaté vlnenie, uzly vzdialené 0,7 metra': 'Standing wave, nodes 0.7 metres apart',
    '0,0 m': '0.0 m', '0,7 m': '0.7 m', '1,4 m': '1.4 m', '2,1 m': '2.1 m', '2,8 m': '2.8 m',
    'kmitňa': 'antinode', 'uzol': 'node', 'Susedné uzly: λ/2 = 0,7 m': 'Adjacent nodes: λ/2 = 0.7 m',
    'Dva rovnobežné vodiče, prúdy smerujú doprava, stred P medzi vodičmi':
        'Two parallel wires, currents flowing to the right, midpoint P between the wires',
    'Klesajúca exponenciálna závislosť počtu nerozpadnutých jadier od času':
        'Decreasing exponential dependence of the number of undecayed nuclei on time',
    'Zdvíhanie závažia o výšku 1,5 metra': 'Lifting a load by a height of 1.5 metres',
    'Graf harmonického kmitania s amplitúdou 0,1 m a prechodmi nulou v časoch 0,25 a 0,55 s':
        'Graph of harmonic oscillation with amplitude 0.1 m and zero crossings at 0.25 s and 0.55 s',
    'Jednosmerný obvod: batéria, vypínač a ampérmeter v sérii s rezistorom; voltmeter paralelne k rezistoru':
        'DC circuit: battery, switch and ammeter in series with a resistor; voltmeter in parallel with the resistor',
    'Graf lineárnej závislosti elektrického prúdu od napätia pre 100 ohmový odpor':
        'Linear graph of current against voltage for a 100-ohm resistor',
    'Graf magnetického toku: od 0 do 0,01 s konštantný 0,002 Wb; od 0,01 do 0,02 s rastie lineárne na 0,008 Wb; od 0,02 do 0,03 s konštantný 0,008 Wb.':
        'Graph of magnetic flux: from 0 to 0.01 s constant at 0.002 Wb; from 0.01 to 0.02 s increasing linearly to 0.008 Wb; from 0.02 to 0.03 s constant at 0.008 Wb.',
    'Riešenie: indukované napätie je nula do 0,01 s, mínus 0,6 voltu do 0,02 s a opäť nula do 0,03 s.':
        'Solution: the induced voltage is zero up to 0.01 s, minus 0.6 volts up to 0.02 s and zero again up to 0.03 s.',
    'Zjednodušená schéma jadrovej elektrárne s tlakovodným reaktorom': 'Simplified diagram of a nuclear power plant with a pressurised water reactor',
    'Dve rovnobežné sily pôsobiace na nosník v rôznych bodoch': 'Two parallel forces acting on a beam at different points',
    'Dvojica síl – opačne orientované rovnobežné sily': 'A couple – opposite parallel forces',
    'Graf sínusu uhla dopadu v závislosti od sínusu uhla lomu': 'Graph of the sine of the angle of incidence against the sine of the angle of refraction',
    'Schéma lomu svetla na rovinnom rozhraní vzduchu a priehľadného materiálu': 'Refraction of light at a plane boundary between air and a transparent material',
    'Schematické znázornenie skladania rovnobežných síl': 'Schematic composition of parallel forces',
    'dopadajúci lúč': 'incident ray', 'lomený lúč': 'refracted ray', 'kolmica': 'normal',
    'priehľadný materiál n₂': 'transparent material n₂', 'vzduch n₁ ≈ 1': 'air n₁ ≈ 1', 'smernica ≈ n': 'gradient ≈ n',
    'sin α': 'sin α', 'sin β': 'sin β',
    'spínač': 'switch', 'zdroj': 'source', 'ampérmeter': 'ammeter', 'voltmeter': 'voltmeter', 'rezistor': 'resistor',
}

def tr_svg(svg):
    def t(m):
        txt = m.group(2)
        if txt in SVG_EN:
            txt = SVG_EN[txt]
        elif re.fullmatch(r'[\w\s=+−().-]*\d,\d[\w\s=+−().,-]*', txt) and not re.search(r'[a-záäčďéíĺľňóôŕšťúýž]{3,}', txt):
            txt = re.sub(r'(\d),(\d)', r'\1.\2', txt)   # čísla a jednotky: desatinná bodka
        elif re.search(r'[a-záäčďéíĺľňóôŕšťúýž]{3,}|\d,\d', txt):
            raise SystemExit(f'Nepreložený text v obrázku: {txt}')
        return m.group(1) + txt + m.group(3)
    svg = re.sub(r'(<text[^>]*>)([^<]+)(</text>)', t, svg)
    return re.sub(r'(aria-label=")([^"]+)(")', t, svg)

def page(n, kind, parts):
    sol = kind == 'solutions'
    label = 'Worked solutions' if sol else 'Questions'
    sub = 'Detailed worked solutions with explanations' if sol else 'Physics · 3 topic parts'
    sk = f'../Vzor{n}_{"vypracovanie" if sol else "zadanie"}.html'
    body = ''.join(f'\n<section class="sheet" id="cast-{i}"><div class="topline">Part {i} of {len(parts)}</div>\n{p.strip()}\n</section>\n'
                   for i, p in enumerate(parts, 1))
    q_on, s_on = ('', ' class="on"') if sol else (' class="on"', '')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Model {n} – {label}</title>
<link rel="stylesheet" href="../mo.css">
</head>
<body class="{'vyp' if sol else 'zad'}">

<header class="mo-head"><div class="mo-head-in">
<div class="mo-kicker"><span class="mo-num">MODEL {n}</span><span class="mo-kind">{label}</span></div>
<h1>{' · '.join(TOPICS[n])}</h1>
<p>{sub}</p>
</div></header>

<nav class="mo-bar"><div class="mo-bar-in">
<a class="mo-back" href="index.html">← All models</a>
<div class="mo-switch"><a href="Model{n}_questions.html"{q_on}>Questions</a><a href="Model{n}_solutions.html"{s_on}>Solutions</a></div>
<button type="button" onclick="window.print()">Print / PDF</button>
<a class="mo-lang" href="{sk}" hreflang="sk" title="Slovenská verzia">SK</a>
</div></nav>

<main class="wrap">
{body}
</main>

<footer class="mo-foot"><a href="index.html">← All models</a><span>Model {n} · {label}</span></footer>
<script src="../mo.js"></script>
</body>
</html>
'''

for n in TOPICS:
    for sk_kind, en_kind, f in (('zadanie', 'questions', 'q'), ('vypracovanie', 'solutions', 's')):
        sk_path = ROOT / f'Vzor{n}_{sk_kind}.html'
        sk = sk_path.read_text(encoding='utf-8')
        main = re.search(r'<main class="wrap">(.*)</main>', sk, re.S).group(1)
        svgs = [tr_svg(x) for x in re.findall(r'<svg.*?</svg>', main, re.S)]
        txt = (TXT / f'm{n}_{f}.html').read_text(encoding='utf-8')
        used = sorted(set(int(i) for i in re.findall(r'\{\{SVG(\d+)\}\}', txt)))
        assert used == list(range(len(svgs))), (n, f, used, len(svgs))
        txt = re.sub(r'\{\{SVG(\d+)\}\}', lambda m: svgs[int(m.group(1))], txt)
        parts = txt.split('<!--PART-->')
        assert len(parts) == 3 == main.count('<section'), (n, f)
        html = page(n, en_kind, parts)
        assert not re.search(r'\d,\d', re.sub(r'<svg.*?</svg>', '', html, flags=re.S).replace('points="', '')), (n, f, 'desatinná čiarka')
        (EN / f'Model{n}_{en_kind}.html').write_text(html, encoding='utf-8', newline='\n')
        # prepínač EN v slovenskej stránke
        if 'class="mo-lang"' not in sk:
            link = f'<a class="mo-lang" href="en/Model{n}_{en_kind}.html" hreflang="en" title="English version">EN</a>\n</div></nav>'
            sk = sk.replace('</div></nav>', link, 1)
            sk_path.write_text(sk, encoding='utf-8', newline='\n')
        print('ok', n, en_kind)
