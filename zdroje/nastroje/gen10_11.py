"""MO10_* a MO11_* (zdroje) -> Vzor10_*.html a Vzor11_*.html (FYZIKA).
Text a obrázky sa preberajú zo zdroja; odborné chyby sa nenašli.
Zadania: obsah časti sa vkladá do rámčeka úlohy (ako pri ostatných vzoroch).
MO11: päta s odkazom NIST rozdelená k ortuti (časť 1) a k optike (časť 2).
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen10_11.py"""
import pathlib, re

SRC = pathlib.Path('zdroje'); DST = pathlib.Path('FYZIKA')
TOPICS = {
    10: ['Vlastnosti plynov', 'Duté guľové zrkadlo', 'Hustota pevnej látky'],
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

# Vzor 10: zdroj MO10 mal tlak v pneumatike ako samostatnú časť a chýbal mu experiment. Podľa fotky:
# časť 1 = plyny + úloha s pneumatikou, časť 2 = zrkadlo, časť 3 = experiment – hustota pevnej látky (písané tu).
VAHY = ('<svg class="diagram" viewBox="0 0 520 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hydrostatické váženie: teleso zavesené na silomere na vzduchu a ponorené do vody">'
        '<g stroke="#193b59" stroke-width="2"><rect x="95" y="20" width="30" height="95" rx="6" fill="#f4f9fc"/><rect x="335" y="20" width="30" height="95" rx="6" fill="#f4f9fc"/></g>'
        '<g stroke="#637889" stroke-width="1.5"><path d="M101 40H119M101 55H119M101 70H119M101 85H119M101 100H119M341 40H359M341 55H359M341 70H359M341 85H359M341 100H359"/></g>'
        '<path d="M98 98H122M338 74H362" stroke="#c0392b" stroke-width="3"/>'
        '<g stroke="#193b59" stroke-width="2"><path d="M110 115V150M350 115V165"/></g>'
        '<rect x="285" y="125" width="130" height="125" fill="none" stroke="#375873" stroke-width="2.5"/>'
        '<rect x="287" y="140" width="126" height="108" fill="#cfe7f6"/><path d="M287 140H413" stroke="#2f6db3" stroke-width="2"/>'
        '<rect x="90" y="150" width="40" height="55" fill="#b9c4cf" stroke="#475569" stroke-width="2"/>'
        '<rect x="330" y="165" width="40" height="55" fill="#b9c4cf" stroke="#475569" stroke-width="2"/>'
        '<g font-size="15" fill="#193b59"><text x="140" y="70">G = 0,416 N</text><text x="380" y="80">G′ = 0,262 N</text>'
        '<text x="70" y="235">na vzduchu</text><text x="320" y="268">vo vode</text><text x="140" y="40">silomer</text></g></svg>')

Z10_3 = ('<h2>3. Experiment – hustota pevnej látky</h2><div class="task"><p>Experimentálne určte hustotu pevnej látky (napríklad kovového valčeka). '
         'Navrhnite aspoň dva spôsoby merania – pre teleso pravidelného tvaru a pre teleso nepravidelného tvaru – a výsledky porovnajte s tabuľkovou hodnotou.</p></div>')

V10_3 = ('<h2>3. Experiment – hustota pevnej látky</h2><h3>3.1 Teória</h3><p><strong>Hustota</strong> látky je podiel hmotnosti telesa a jeho objemu:</p>'
         '<div class="formula">ρ = m/V &nbsp;&nbsp; [ρ] = kg/m³ (1 g/cm³ = 1 000 kg/m³)</div><p>Hmotnosť určíme váhami. Objem pravidelného telesa vypočítame z rozmerov, objem nepravidelného telesa určíme ponorením do vody. '
         'Hustota je charakteristická veličina látky, preto podľa nej môžeme látku identifikovať (hliník 2 700 kg/m³, oceľ 7 850 kg/m³, mosadz asi 8 500 kg/m³).</p>'
         '<h3>3.2 Pomôcky</h3><p>Kovový valček (napr. hliníkový), digitálne váhy, posuvné meradlo, odmerný valec s vodou, silomer, kadička s vodou, nitka.</p>'
         '<h3>3.3 Spôsob A – teleso pravidelného tvaru</h3><ol><li>Váhami zmeriame hmotnosť m valčeka.</li><li>Posuvným meradlom zmeriame priemer d a výšku h, každý rozmer viackrát na rôznych miestach.</li>'
         '<li>Vypočítame objem V = πd²h/4 a hustotu ρ = m/V.</li></ol>'
         '<h3>3.4 Spôsob B – ponorenie do odmerného valca</h3><ol><li>Do odmerného valca nalejeme vodu a odčítame objem V₁ (na spodnom okraji menisku).</li>'
         '<li>Teleso na nitke opatrne ponoríme celé pod vodu a odčítame V₂.</li><li>Objem telesa je V = V₂ − V₁. Spôsob funguje aj pre telesá nepravidelného tvaru.</li></ol>'
         '<h3>3.5 Spôsob C – hydrostatické váženie</h3>' + VAHY +
         '<p>Teleso zavesíme na silomer a odčítame jeho tiaž G na vzduchu. Potom ho ponoríme do vody a odčítame G′. Rozdiel je vztlaková sila podľa Archimedovho zákona:</p>'
         '<div class="formula">F<sub>vz</sub> = G − G′ = ρ<sub>v</sub>Vg &nbsp; → &nbsp; ρ = ρ<sub>v</sub> · G/(G − G′)</div><p>Objem ani hmotnosť nemusíme poznať – stačia dva údaje silomera.</p>'
         '<h3>3.6 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje pre hliníkový valček; nejde o skutočné meranie.</p>'
         '<table><tr><th>Spôsob</th><th>Namerané hodnoty</th><th>ρ</th></tr>'
         '<tr><td>A – rozmery</td><td>m = 42,4 g; d = 2,00 cm; h = 5,00 cm; V = 15,7 cm³</td><td>2,70 g/cm³</td></tr>'
         '<tr><td>B – odmerný valec</td><td>V₁ = 50,0 ml; V₂ = 65,5 ml; V = 15,5 cm³</td><td>2,74 g/cm³</td></tr>'
         '<tr><td>C – hydrostatické váženie</td><td>G = 0,416 N; G′ = 0,262 N</td><td>2,70 g/cm³</td></tr></table>'
         '<div class="formula">A: ρ = m/V = 42,4 g / (π · 2,00² · 5,00/4) cm³ = 42,4 g / 15,7 cm³ ≈ 2,70 g/cm³<br>'
         'C: ρ = 1 000 kg/m³ · 0,416 N / (0,416 N − 0,262 N) ≈ 2 700 kg/m³</div>'
         '<div class="result"><strong>Záver:</strong> Hustota valčeka je asi 2 700 kg/m³, čo zodpovedá hliníku. Najpresnejšie sú spôsoby A a C; odmerný valec má hrubú stupnicu.</div>'
         '<h3>3.7 Nepresnosti</h3><p>Pri spôsobe B je najväčšia chyba v odčítaní objemu – dielik 0,5 ml pri objeme 15 ml znamená relatívnu chybu asi 3 %. '
         'Na telese nesmú ostať vzduchové bubliny a nitka by mala byť tenká. Pri spôsobe A ovplyvní výsledok najmä priemer, lebo vystupuje v druhej mocnine: '
         'relatívna chyba objemu je δV ≈ 2δd + δh. Pri spôsobe C sú rozhodujúce dielik silomera a to, že teleso nesmie byť opreté o dno ani steny kadičky.</p>')

vystup = {}
for N in (10, 11):
    Z = [ramcek(x) for x in casti((SRC / f'MO{N}_zadanie.html').read_text(encoding='utf-8'))]
    v_src = (SRC / f'MO{N}_vypracovanie.html').read_text(encoding='utf-8')
    V = casti(v_src)
    if N == 10:   # popis a = 1 cm prekrýval odrazený lúč
        V[2] = rep1('<text x="365" y="315">a = 1 cm</text>', '<text x="398" y="345">a = 1 cm</text>', V[2])
        V[2] = rep1('<text x="563" y="315">|a′| = 2 cm</text>', '<text x="563" y="345">|a′| = 2 cm</text>', V[2])
        # pneumatika ako úloha k časti 1, zrkadlo ako časť 2, nový experiment ako časť 3
        uloha_z = rep1('<h2>2. Tlak vzduchu v pneumatike</h2>\n<div class="task"><p>', '<div class="task"><p><strong>Úloha – tlak v pneumatike:</strong> ', Z[1])
        Z = [Z[0].rstrip() + '\n' + uloha_z, rep1('<h2>3. Duté', '<h2>2. Duté', Z[2]), Z10_3]
        uloha_v = rep1('<h2>2. Tlak vzduchu v pneumatike</h2>', '<h3>Úloha – tlak v pneumatike</h3>', V[1])
        V = [V[0].rstrip() + '\n' + uloha_v, rep1('<h2>3. Duté', '<h2>2. Duté', V[2]), V10_3]
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
