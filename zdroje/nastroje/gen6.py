"""MO6.html (zdroje) -> Vzor6_zadanie.html + Vzor6_vypracovanie.html (FYZIKA).
Pôvodný súbor má zadanie aj vypracovanie spolu a graf kmitania kreslí skriptom;
tu je graf vygenerovaný ako hotové SVG. Opravené obrázky: schéma obvodu
(rezistor nebol premostený drôtom, správna značka zdroja), mriežka grafu I(U).
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen6.py"""
import math, pathlib, re

DST = pathlib.Path('FYZIKA')
N = 6
TOPICS = ['Energia hmotného bodu', 'Oscilátor', 'Elektrický obvod']

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

c = lambda x: f'{x:.2f}'.replace('.', ',')

# ---------- obrázky ----------
SVG_ZDVIH = '''<svg class="diagram" viewBox="0 0 380 285" role="img" aria-label="Zdvíhanie závažia o výšku 1,5 metra" style="max-width:380px"><defs><marker id="sipka6" markerWidth="7" markerHeight="7" refX="4" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="none" stroke="#206390" stroke-width="1.4"/></marker></defs><line x1="38" y1="249" x2="340" y2="249" stroke="#6d8490" stroke-width="3"/><rect x="103" y="178" width="93" height="70" rx="5" fill="#b7c9d7" stroke="#46677e" stroke-width="2"/><text x="149" y="218" font-size="21" text-anchor="middle" fill="#233b50">50 kg</text><rect x="103" y="55" width="93" height="70" rx="5" fill="#d9e7f0" stroke="#46677e" stroke-width="2" stroke-dasharray="6 5"/><text x="149" y="95" font-size="20" text-anchor="middle" fill="#233b50">50 kg</text><path d="M232 207 V92" stroke="#206390" stroke-width="3" marker-end="url(#sipka6)"/><text x="246" y="151" font-size="19" fill="#206390">h = 1,5 m</text><text x="205" y="268" font-size="16" fill="#506273">t = 7,5 s</text></svg>'''

def svg_kmitanie():
    l, r, mid, scale, tmax = 80, 825, 192, 1200, .95
    px = lambda t: l + (r - l) * t / tmax
    py = lambda y: mid - scale * y
    o = ['<svg class="graph" viewBox="0 0 860 390" role="img" aria-label="Graf harmonického kmitania s amplitúdou 0,1 m a prechodmi nulou v časoch 0,25 a 0,55 s">']
    for v in (-.1, -.05, 0, .05, .1):
        y = py(v)
        o.append(f'<line x1="{l}" x2="{r}" y1="{y:.1f}" y2="{y:.1f}" stroke="{"#496377" if v == 0 else "#d9e3e9"}" stroke-width="{2 if v == 0 else 1}"/>')
        o.append(f'<text x="{l - 12}" y="{y + 6:.1f}" text-anchor="end" fill="#38546b" font-size="18">{"0" if v == 0 else c(v).replace("-", "−")}</text>')
    for k in range(10):
        t = k / 10; x = px(t)
        o.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="58" y2="326" stroke="#edf1f4"/>')
        o.append(f'<text x="{x:.1f}" y="355" text-anchor="middle" fill="#38546b" font-size="16">{f"{t:.1f}".replace(".", ",")}</text>')
    d = ' '.join(f'{"L" if i else "M"}{px(i * tmax / 600):.2f} {py(.1 * math.sin(2 * math.pi * (i * tmax / 600) / .6 + math.pi / 6)):.2f}' for i in range(601))
    o.append(f'<path d="{d}" fill="none" stroke="#126d9b" stroke-width="4"/>')
    for t in (.25, .55):
        x = px(t)
        o.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="65" y2="326" stroke="#b15c43" stroke-dasharray="5 6" stroke-width="2"/>')
        o.append(f'<circle cx="{x:.1f}" cy="{mid}" r="6" fill="#b15c43"/>')
        o.append(f'<text x="{x:.1f}" y="42" text-anchor="middle" fill="#9b4d39" font-size="19" font-weight="bold">{c(t)} s</text>')
    o.append('<text x="20" y="30" fill="#38546b" font-size="20">y (m)</text>')
    o.append('<text x="765" y="380" fill="#38546b" font-size="20">t (s)</text>')
    o.append('<text x="388" y="80" fill="#126d9b" font-size="20">A = 0,10 m</text></svg>')
    return ''.join(o)

# schéma: vodič už nevedie cez rezistor; zdroj = dlhá tenká a krátka hrubá platňa naprieč vodičom
SVG_OBVOD = '''<svg class="diagram" viewBox="0 0 850 310" role="img" aria-label="Jednosmerný obvod: batéria, vypínač a ampérmeter v sérii s rezistorom; voltmeter paralelne k rezistoru" style="max-width:760px"><g fill="none" stroke="#284b67" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M110 88 H235 M285 88 H382 M442 88 H565 M670 88 H736 V254 H110 V168 M110 150 V88"/><circle cx="412" cy="88" r="30"/><rect x="565" y="62" width="105" height="52" rx="3" fill="#e9f1f8"/><path d="M565 88 V165 H590 M670 88 V165 H642"/><circle cx="616" cy="165" r="26"/><circle cx="237" cy="88" r="4" fill="#284b67"/><circle cx="285" cy="88" r="4" fill="#284b67"/><path d="M239 86 L279 62"/><circle cx="565" cy="88" r="4" fill="#284b67"/><circle cx="670" cy="88" r="4" fill="#284b67"/></g><path d="M86 150 H134" stroke="#284b67" stroke-width="3"/><path d="M98 168 H122" stroke="#284b67" stroke-width="7"/><g font-size="22" text-anchor="middle" fill="#173f5e"><text x="412" y="96">A</text><text x="616" y="173">V</text><text x="617" y="96">R</text><text x="148" y="147" font-size="18">+</text><text x="148" y="178" font-size="18">−</text><text x="258" y="40" font-size="19">spínač</text><text x="58" y="166" font-size="19">zdroj</text><text x="412" y="37" font-size="19">ampérmeter</text><text x="615" y="226" font-size="19">voltmeter</text><text x="615" y="42" font-size="19">rezistor</text></g></svg>'''

def svg_iu():
    y0, y5 = 294, 48
    ys = [y0 - (y0 - y5) * k / 5 for k in range(6)]
    xs = [96 + (785 - 96) * k / 5 for k in range(6)]
    grid = ' '.join(f'M96 {y:.1f}H785' for y in ys) + ' ' + ' '.join(f'M{x:.0f} 48V294' for x in xs)
    o = ['<svg class="diagram" viewBox="0 0 850 320" role="img" aria-label="Graf lineárnej závislosti elektrického prúdu od napätia pre 100 ohmový odpor" style="max-width:760px">',
         f'<g stroke="#d4e0e8" stroke-width="1"><path d="{grid}"/></g>',
         '<g stroke="#263f56" stroke-width="2.5" fill="none"><path d="M96 38 V294 H795"/></g>',
         '<path d="M96 294 L785 48" stroke="#176d9a" stroke-width="4"/><g fill="#176d9a">',
         ''.join(f'<circle cx="{x:.0f}" cy="{y:.1f}" r="5"/>' for x, y in zip(xs, ys)), '</g><g fill="#2b475b" font-size="20">',
         ''.join(f'<text x="{86}" y="{y + 6:.1f}" text-anchor="end">{"0" if k == 0 else c(k / 100)}</text>' for k, y in enumerate(ys)),
         ''.join(f'<text x="{x:.0f}" y="315" text-anchor="middle">{k}</text>' for k, x in enumerate(xs) if k),
         '<text x="17" y="28">I (A)</text><text x="793" y="277">U (V)</text></g></svg>']
    return ''.join(o)

SVG_KMIT = svg_kmitanie()
SVG_IU = svg_iu()

# ---------- zadanie ----------
Z = [
f'''<h2>1. Energia hmotného bodu</h2>
<h3>Teoretická časť</h3>
<p>Vysvetlite mechanickú prácu, pohybovú (kinetickú) a polohovú (potenciálnu) energiu, zákon zachovania mechanickej energie, výkon a účinnosť.</p>
<h3>Výpočtová úloha</h3>
<div class="task">Závažie s hmotnosťou <b>50 kg</b> zdvihneme o <b>1,5 m</b> za <b>7,5 s</b>. Určte priemerný výkon pri zdvíhaní. Straty zanedbajte.</div>''',
f'''<h2>2. Oscilátor</h2>
<div class="task">Na grafe je časová závislosť výchylky harmonického oscilátora. Určte amplitúdu, periódu, frekvenciu a uhlovú frekvenciu. Napíšte rovnicu kmitania, opíšte fázu a určte maximálnu rýchlosť a maximálne zrýchlenie. Na osi výchylky sú vyznačené hodnoty <b>0,05 m</b> a <b>0,10 m</b>; na časovej osi prechody rovnovážnou polohou pri <b>0,25 s</b> a <b>0,55 s</b>.</div>
{SVG_KMIT}
<p class="caption">Prechody cez rovnovážnu polohu pri 0,25 s (nadol) a 0,55 s (nahor).</p>''',
'''<h2>3. Meranie napätia a prúdu v elektrickom obvode</h2>
<div class="task">Navrhnite jednoduchý elektrický obvod a predveďte správne meranie elektrického napätia a prúdu. Ako doplňujúcu úlohu overte meraním Ohmov zákon pre rezistor pri približne stálej teplote.</div>''',
]

# ---------- vypracovanie ----------
V = [
f'''<h2>1. Energia hmotného bodu</h2>
<div class="task"><b>Zadanie.</b> Vysvetlite mechanickú prácu, pohybovú (kinetickú) a polohovú (potenciálnu) energiu, zákon zachovania mechanickej energie, výkon a účinnosť. <b>Úloha:</b> Závažie s hmotnosťou <b>50 kg</b> zdvihneme o <b>1,5 m</b> za <b>7,5 s</b>. Určte priemerný výkon pri zdvíhaní. Straty zanedbajte.</div>
<h3>Teória</h3>
<p><b>Mechanická práca</b> konštantnej sily je <i>W = Fs cos α</i>, kde α je uhol medzi silou a premiestnením. Jednotka je joule (J).</p>
<div class="grid2"><div><p><b>Kinetická energia:</b></p>
<div class="formula">E<sub>k</sub> = ½mv²</div>
<p><b>Gravitačná potenciálna energia</b> blízko povrchu Zeme:</p>
<div class="formula">E<sub>p</sub> = mgh</div>
</div>
<div><p><b>Zákon zachovania mechanickej energie:</b> ak konajú prácu iba konzervatívne sily,</p>
<div class="formula">E<sub>k</sub> + E<sub>p</sub> = konšt.</div>
<p>Pri pôsobení nekonzervatívnych síl sa mechanická energia môže meniť na iné formy energie.</p>
</div>
</div>
<p><b>Priemerný výkon</b> je podiel práce a času: <i>P = W/t</i> (jednotka watt, W). <b>Účinnosť</b> je podiel užitočnej energie alebo výkonu k dodanej energii alebo príkonu: <i>η = P<sub>už</sub>/P<sub>dod</sub></i>; v percentách násobíme 100 %.</p>
<div class="grid2"><div>
{SVG_ZDVIH}
<p class="caption">Schéma zdvíhania závažia</p>
</div>
<div><h3>Riešenie</h3>
<p>Pri rovnomernom zdvíhaní sa vykonaná práca rovná prírastku potenciálnej energie:</p>
<div class="formula">W = mgh</div>
<div class="formula">W = 50 · 9,81 · 1,5 = 735,75 J</div>
<div class="formula">P = W/t = 735,75/7,5</div>
<div class="result">Výsledok: P = 98,1 W (približne 100 W pri použití g ≈ 10 m/s²).</div>
<p class="subtle">Platí pre priemerný mechanický výkon bez strát, pričom závažie na začiatku a konci neprechádza zmenou kinetickej energie.</p>
</div>
</div>''',
f'''<h2>2. Oscilátor</h2>
<div class="task"><b>Zadanie.</b> Na grafe je časová závislosť výchylky harmonického oscilátora. Určte amplitúdu, periódu, frekvenciu a uhlovú frekvenciu. Napíšte rovnicu kmitania, opíšte fázu a určte maximálnu rýchlosť a maximálne zrýchlenie. Na osi výchylky sú vyznačené hodnoty <b>0,05 m</b> a <b>0,10 m</b>; na časovej osi prechody rovnovážnou polohou pri <b>0,25 s</b> a <b>0,55 s</b>.</div>
{SVG_KMIT}
<p class="caption">Prechody cez rovnovážnu polohu pri 0,25 s (nadol) a 0,55 s (nahor).</p>
<h3>Riešenie</h3>
<p><b>Amplitúda:</b> A = 0,10 m. Uvedené dva prechody rovnovážnou polohou sú po sebe nasledujúce; preto sa čas medzi nimi rovná polovici periódy.</p>
<div class="formula">T/2 = 0,55 − 0,25 = 0,30 s ⇒ <b>T = 0,60 s</b></div>
<div class="formula">f = 1/T = 1/0,60 ≈ <b>1,67 Hz</b></div>
<div class="formula">ω = 2π/T = 10π/3 ≈ <b>10,47 rad/s</b></div>
<p>Všeobecná rovnica kmitania je <i>y(t) = A sin(ωt + φ<sub>0</sub>)</i>. Na grafe je pri t = 0,25 s klesajúci prechod nulou, čiže fáza je π. Odtiaľ:</p>
<div class="formula">φ<sub>0</sub> = π − ω · 0,25 = π/6</div>
<div class="result">Rovnica grafu:<div class="formula">y(t) = 0,10 sin((10π/3)t + π/6) &nbsp; [m]</div></div>
<p><b>Fáza</b> φ(t) = ωt + φ<sub>0</sub> určuje stav kmitania v príslušnom čase. Rýchlosť a zrýchlenie získame derivovaním výchylky:</p>
<div class="formula">v(t) = Aω cos(ωt + φ<sub>0</sub>), &nbsp; a(t) = −Aω² sin(ωt + φ<sub>0</sub>)</div>
<div class="grid2"><div class="result">Maximálna rýchlosť:<div class="formula">v<sub>max</sub> = Aω ≈ <b>1,05 m/s</b></div></div>
<div class="result">Maximálne zrýchlenie:<div class="formula">a<sub>max</sub> = Aω² ≈ <b>10,97 m/s²</b></div></div>
</div>
<p class="subtle">Výchylka a zrýchlenie majú vždy opačné znamienka: a = −ω²y. Najväčšia veľkosť rýchlosti je v rovnovážnej polohe; najväčšia veľkosť zrýchlenia v krajných polohách.</p>''',
f'''<h2>3. Meranie napätia a prúdu v elektrickom obvode</h2>
<div class="task"><b>Zadanie.</b> Navrhnite jednoduchý elektrický obvod a predveďte správne meranie elektrického napätia a prúdu. Ako doplňujúcu úlohu overte meraním Ohmov zákon pre rezistor pri približne stálej teplote.</div>
<h3>Schéma zapojenia</h3>
{SVG_OBVOD}
<p class="caption">Ampérmeter A je v sérii so spotrebičom; voltmeter V je pripojený paralelne na rezistor R.</p>
<h3>Postup merania</h3>
<ol><li>Pri odpojenom zdroji zostavte obvod podľa schémy; skontrolujte polaritu a vhodné rozsahy meracích prístrojov.</li>
<li>Ampérmeter zapojte <b>sériovo</b>, voltmeter <b>paralelne</b> k rezistoru. Ampérmeter nikdy nepripájajte priamo paralelne na zdroj.</li>
<li>Zapnite zdroj s nízkym bezpečným napätím a odčítajte napätie U a prúd I.</li>
<li>Meňte napätie zdroja a zapisujte ďalšie dvojice (U, I). Rezistor neprehrievajte.</li>
<li>Vypočítajte R = U/I a zostrojte graf I = f(U). Overte, či sú body približne na priamke prechádzajúcej počiatkom.</li>
</ol>
<h3>Ohmov zákon</h3>
<p>Pri konštantnej teplote je prúd cez ohmický vodič priamo úmerný napätiu na jeho koncoch:</p>
<div class="formula"><b>U = RI, &nbsp; I = U/R, &nbsp; R = U/I</b></div>
<p>Jednotky: napätie volt (V), prúd ampér (A), odpor ohm (Ω).</p>
<p><b>Ukážka výsledkov</b> pre rezistor s odporom 100 Ω (ide o modelové hodnoty, nie skutočne namerané údaje):</p>
<div class="scroll"><table><thead><tr><th>U (V)</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th></tr>
</thead><tbody><tr><th>I (A)</th><td>0</td><td>0,010</td><td>0,020</td><td>0,030</td><td>0,040</td><td>0,050</td></tr>
<tr><th>R (Ω)</th><td>–</td><td>100</td><td>100</td><td>100</td><td>100</td><td>100</td></tr>
</tbody></table></div>
{SVG_IU}
<p class="caption">Ukážkový graf I = f(U) pre R = 100 Ω; smernica priamky sa rovná 1/R.</p>
<div class="result">Záver experimentu: Ak sú pri približne stálej teplote hodnoty U/I konštantné a graf I = f(U) tvorí priamku prechádzajúcu počiatkom, meranie podporuje platnosť Ohmovho zákona pre použitý rezistor.</div>''',
]

for name, html in (('zadanie', page('zad', Z)), ('vypracovanie', page('vyp', V))):
    for bad in ('ekonštru', 'rukopis', 'MO6', 'maturit', 'prekreslen'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
