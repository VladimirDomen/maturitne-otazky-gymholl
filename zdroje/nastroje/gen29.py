"""Vzor 29 podľa fotky 29 a MO29 (text písaný priamo). Časť 3 podľa fotky: pilinové obrazce magnetu, priameho vodiča,
závitu a súhlasných/nesúhlasných pólov (MO29 tu mal rovnobežné vodiče, ktoré na fotke nie sú). Obrázky prekreslené.
-> Vzor29_zadanie.html + Vzor29_vypracovanie.html.  Spustenie: python -I gen29.py <priečinok FYZIKA>"""
import sys, pathlib, math

DST = pathlib.Path(sys.argv[1])
N = 29
TOPICS = ['Vlnová optika', 'Elektrický prúd', 'Stacionárne magnetické pole']

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

def hrot(x, y, ux, uy, farba, l=10, w=5):
    """Šípka s hrotom v (x, y) v smere (ux, uy)."""
    d = math.hypot(ux, uy); ux, uy = ux / d, uy / d
    a = (x - l * ux + w * uy, y - l * uy - w * ux); b = (x - l * ux - w * uy, y - l * uy + w * ux)
    return f'<path d="M{x:.1f} {y:.1f}L{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}Z" fill="{farba}"/>'

MOD = '#2f6db3'

# ---------- obrázky ----------
VRSTVA = ('<svg class="diagram" viewBox="0 0 560 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Interferencia svetla na tenkej vrstve: lúč sa odráža od hornej aj dolnej plochy vrstvy">'
          '<rect x="20" y="80" width="520" height="70" fill="#dcebf7"/><rect x="20" y="150" width="520" height="45" fill="#eef2f6"/>'
          '<path d="M20 80H540M20 150H540" stroke="#375873" stroke-width="2"/>'
          '<g stroke="#c4661b" stroke-width="3" fill="none"><path d="M90 20L190 80L290 20"/><path d="M190 80L240 150L290 80L390 20"/></g>'
          + hrot(150, 56, 100, 60, '#c4661b') + hrot(250, 44, 100, -60, '#c4661b') + hrot(220, 122, 50, 70, '#c4661b') + hrot(350, 44, 100, -60, '#c4661b') +
          '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M470 80V150M463 80H477M463 150H477"/></g>'
          '<g font-size="15" fill="#193b59"><text x="28" y="70">vzduch</text><text x="28" y="122">vrstva n</text><text x="28" y="180">podložka</text>'
          '<text x="480" y="120">d</text><text x="296" y="16">1</text><text x="396" y="16">2</text></g></svg>')

def magnet(x, y, w, h, lavy):
    """Tyčový magnet; lavy = pól na ľavej strane ('N' alebo 'S')."""
    farby = {'N': '#f2b8b0', 'S': '#b9d3ee'}
    pravy = 'S' if lavy == 'N' else 'N'
    return (f'<rect x="{x}" y="{y}" width="{w / 2}" height="{h}" fill="{farby[lavy]}" stroke="#193b59" stroke-width="1.5"/>'
            f'<rect x="{x + w / 2}" y="{y}" width="{w / 2}" height="{h}" fill="{farby[pravy]}" stroke="#193b59" stroke-width="1.5"/>'
            f'<text x="{x + w / 4 - 6}" y="{y + h / 2 + 6}" font-size="17" fill="#193b59">{lavy}</text>'
            f'<text x="{x + 3 * w / 4 - 6}" y="{y + h / 2 + 6}" font-size="17" fill="#193b59">{pravy}</text>')

def pole_1():
    """Tyčový magnet (N vľavo), priamy vodič (prúd k pozorovateľovi), závit v reze."""
    g = []
    # magnet: čiary mimo magnetu idú od N (vľavo) k S (vpravo)
    for cy, mid in ((40, 58), (5, 31.75)):
        g.append(f'<path d="M60 112C0 {cy} 260 {cy} 200 112" fill="none" stroke="{MOD}" stroke-width="2"/>' + hrot(136, mid, 1, 0, MOD))
    for cy, mid in ((200, 182), (235, 208.25)):
        g.append(f'<path d="M60 128C0 {cy} 260 {cy} 200 128" fill="none" stroke="{MOD}" stroke-width="2"/>' + hrot(136, mid, 1, 0, MOD))
    g.append(f'<path d="M60 120H14M246 120H200" stroke="{MOD}" stroke-width="2"/>' + hrot(14, 120, -1, 0, MOD) + hrot(204, 120, -1, 0, MOD))
    g.append(magnet(60, 104, 140, 32, 'N'))
    # priamy vodič: prúd k nám -> čiary proti smeru hodinových ručičiek (hore idú doľava)
    for r in (24, 44, 66):
        g.append(f'<circle cx="400" cy="120" r="{r}" fill="none" stroke="{MOD}" stroke-width="2"/>' + hrot(396, 120 - r, -1, 0, MOD))
    g.append('<circle cx="400" cy="120" r="9" fill="#fff" stroke="#193b59" stroke-width="2"/><circle cx="400" cy="120" r="3" fill="#193b59"/>')
    # závit v reze: hore prúd k nám (⊙), dole od nás (⊗); medzi nimi pole doprava
    for r in (16, 28):
        g.append(f'<circle cx="585" cy="80" r="{r}" fill="none" stroke="{MOD}" stroke-width="1.8"/>' + hrot(581, 80 - r, -1, 0, MOD, 8, 4))
        g.append(f'<circle cx="585" cy="160" r="{r}" fill="none" stroke="{MOD}" stroke-width="1.8"/>' + hrot(581, 160 + r, -1, 0, MOD, 8, 4))
    g.append(f'<path d="M535 120H640" stroke="{MOD}" stroke-width="2"/>' + hrot(645, 120, 1, 0, MOD))
    g.append('<circle cx="585" cy="80" r="8" fill="#fff" stroke="#193b59" stroke-width="2"/><circle cx="585" cy="80" r="2.5" fill="#193b59"/>'
             '<circle cx="585" cy="160" r="8" fill="#fff" stroke="#193b59" stroke-width="2"/><path d="M580 155L590 165M590 155L580 165" stroke="#193b59" stroke-width="2"/>')
    return ('<svg class="diagram" viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Indukčné čiary tyčového magnetu, priameho vodiča s prúdom a závitu s prúdom">'
            + ''.join(g) +
            '<g font-size="14" fill="#193b59"><text x="80" y="254">tyčový magnet</text><text x="350" y="254">priamy vodič</text><text x="568" y="254">závit</text></g></svg>')

def pole_2():
    """Nesúhlasné póly (N–S) a súhlasné póly (N–N)."""
    g = [magnet(20, 84, 110, 32, 'S'), magnet(200, 84, 110, 32, 'S')]
    for y in (90, 100, 110):
        g.append(f'<path d="M130 {y}H200" stroke="{MOD}" stroke-width="2"/>' + hrot(170, y, 1, 0, MOD, 8, 4))
    g.append(f'<path d="M130 86C150 60 180 60 200 86M130 114C150 140 180 140 200 114" fill="none" stroke="{MOD}" stroke-width="2"/>')
    g += [magnet(370, 84, 110, 32, 'S'), magnet(560, 84, 110, 32, 'N')]
    for sx in (1, -1):
        x0 = 480 if sx == 1 else 560
        for dy, tip in ((-1, (500 if sx == 1 else 540, 40)), (1, (500 if sx == 1 else 540, 160))):
            y0 = 100 + dy * 10
            g.append(f'<path d="M{x0} {y0}C{x0 + sx * 25} {y0} {x0 + sx * 22} {100 + dy * 40} {tip[0]} {tip[1]}" fill="none" stroke="{MOD}" stroke-width="2"/>'
                     + hrot(tip[0], tip[1], sx * -0.1, dy, MOD, 8, 4))
        g.append(f'<path d="M{x0} 100H{x0 + sx * 28}" stroke="{MOD}" stroke-width="2"/>' + hrot(x0 + sx * 30, 100, sx, 0, MOD, 8, 4))
    g.append('<circle cx="520" cy="100" r="4" fill="#c0392b"/>')
    return ('<svg class="diagram" viewBox="0 0 690 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Indukčné čiary medzi nesúhlasnými pólmi a medzi súhlasnými pólmi dvoch magnetov">'
            + ''.join(g) +
            '<g font-size="14" fill="#193b59"><text x="60" y="190">nesúhlasné póly – priťahujú sa</text><text x="420" y="190">súhlasné póly – odpudzujú sa</text></g></svg>')

POLE1 = pole_1()
POLE2 = pole_2()

# ---------- zadanie ----------
Z1 = '''<h2>1. Vlnová optika</h2><div class="task"><ol><li>Vysvetlite, prečo svetlo považujeme za elektromagnetické vlnenie.</li><li>Vysvetlite interferenciu svetla na tenkých vrstvách. Objasnite koherentnosť, optickú dráhu a podmienky interferenčného maxima a minima (rád maxima a minima).</li><li>Vysvetlite podstatu rozkladu svetla pri lome na rovinnom rozhraní.</li></ol></div>'''

Z2 = '''<h2>2. Elektrický prúd</h2><div class="task"><p>Rezistorom s odporom <strong>R = 15&nbsp;Ω</strong> prešiel za čas <strong>t = 2&nbsp;min</strong> náboj <strong>Q = 30&nbsp;C</strong>. Elementárny náboj e = 1,602 · 10⁻¹⁹&nbsp;C.</p><ol type="a"><li>Koľko elektrónov prešlo prierezom vodiča?</li><li>Definujte elektrický prúd a vypočítajte ho.</li><li>Definujte elektrické napätie. Aké napätie bolo na koncoch rezistora?</li><li>Aké napätie by bolo na koncoch rezistora s odporom R = 50&nbsp;Ω pri rovnakom prúde?</li></ol></div>'''

Z3 = '''<h2>3. Experiment – stacionárne magnetické pole</h2><div class="task"><p>Pomocou železných pilín znázornite magnetické pole (pilinové obrazce):</p><ol><li>permanentného tyčového magnetu,</li><li>priameho vodiča s prúdom,</li><li>závitu (cievky) s prúdom,</li><li>dvoch magnetov priložených k sebe súhlasnými a nesúhlasnými pólmi.</li></ol><p>Obrazce zakreslite, vyznačte smer indukčných čiar a vysvetlite pozorované rozdiely.</p></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Vlnová optika</h2><h3>1.1 Svetlo ako elektromagnetické vlnenie</h3><p>Svetlo sa správa ako vlnenie: interferuje, ohýba sa a polarizuje. Polarizácia ukazuje, že ide o <strong>priečne</strong> vlnenie. Maxwellova teória predpovedala, že elektromagnetické vlnenie sa vo vákuu šíri rýchlosťou c = 1/√(ε₀μ₀) ≈ 3 · 10⁸ m/s – rovnakou, akú má svetlo. Svetlo je preto elektromagnetické vlnenie s vlnovými dĺžkami asi 380 – 760 nm; vektor 𝐄 a vektor 𝐁 kmitajú kolmo na seba aj na smer šírenia. Farbu svetla určuje jeho frekvencia.</p><h3>1.2 Koherentnosť a optická dráha</h3><p>Stály interferenčný obrazec vznikne len pri skladaní <strong>koherentných</strong> vlnení – majú rovnakú frekvenciu a stály fázový rozdiel. Dva nezávislé zdroje (dve žiarovky) koherentné nie sú. Koherentné vlnenia získame rozdelením svetla z jedného zdroja – napríklad odrazom na dvoch plochách tenkej vrstvy.</p><p><strong>Optická dráha</strong> je súčin indexu lomu a geometrickej dráhy, l = n·s. V látke s indexom n sa svetlo šíri n-krát pomalšie, preto dráha s v látke zodpovedá dráhe n·s vo vákuu.</p><p>Podmienky interferencie pre dráhový rozdiel Δl (bez fázových skokov pri odraze):</p><div class="formula">maximum: Δl = kλ &nbsp;&nbsp;&nbsp; minimum: Δl = (2k + 1)λ/2 &nbsp;&nbsp;&nbsp; k = 0, 1, 2, …</div><p>Číslo k je <strong>rád</strong> interferenčného maxima alebo minima.</p><h3>1.3 Interferencia na tenkej vrstve</h3>{VRSTVA}<p>Lúč 1 sa odráža od hornej plochy vrstvy, lúč 2 prejde vrstvou, odrazí sa od dolnej plochy a vystúpi späť. Pri kolmom dopade je ich dráhový rozdiel 2nd. Pri odraze od opticky hustejšieho prostredia sa fáza zmení o π, čo zodpovedá dráhe λ/2. Ak je vrstva vo vzduchu (mydlová blana), skok nastáva len pri lúči 1:</p><div class="formula">maximum: 2nd = (2k + 1)λ/2 &nbsp;&nbsp;&nbsp; minimum: 2nd = kλ</div><p>Pri bielom svetle sa pre rôzne hrúbky zosilňujú rôzne farby – preto sú mydlové bubliny a olejové škvrny na vode farebné. Využíva sa to pri antireflexných vrstvách na okuliaroch a objektívoch.</p><h3>1.4 Rozklad svetla pri lome</h3><p>Index lomu látky závisí od frekvencie (vlnovej dĺžky) svetla – <strong>disperzia</strong>. V skle je index lomu pre fialové svetlo väčší ako pre červené, takže fialové svetlo sa láme viac. Biele svetlo, zložené z rôznych farieb, sa preto pri lome na rozhraní rozloží na spektrum. Pri rovinnom rozhraní sú lomené lúče rôznych farieb rozbiehavé len málo; výrazne sa spektrum prejaví v hranole, kde sa svetlo láme dvakrát v rovnakom zmysle. V prírode tak vzniká dúha – lom a odraz v kvapkách vody.</p><div class="formula">sin α / sin β = n(λ) &nbsp;&nbsp;&nbsp; n<sub>fialová</sub> &gt; n<sub>červená</sub></div>'''

V2 = '''<h2>2. Elektrický prúd</h2><p>R = 15 Ω, t = 2 min = 120 s, Q = 30 C, e = 1,602 · 10⁻¹⁹ C.</p><p><strong>a)</strong> Náboj je kvantovaný – je celistvým násobkom elementárneho náboja, Q = Ne:</p><div class="formula">N = Q/e = 30 C / (1,602 · 10⁻¹⁹ C) ≈ 1,87 · 10²⁰</div><p><strong>b)</strong> <strong>Elektrický prúd</strong> je usporiadaný pohyb voľných nosičov náboja. Ako veličina udáva náboj, ktorý prejde prierezom vodiča za jednotku času. Jednotkou je ampér (A):</p><div class="formula">I = Q/t = 30 C / 120 s = 0,25 A</div><p><strong>c)</strong> <strong>Elektrické napätie</strong> medzi dvoma bodmi je podiel práce, ktorú vykonajú elektrické sily pri prenesení náboja medzi týmito bodmi, a veľkosti tohto náboja: U = W/Q. Jednotkou je volt (V = J/C). Pre rezistor platí Ohmov zákon U = RI:</p><div class="formula">U = RI = 15 Ω · 0,25 A = 3,75 V</div><p>Elektrické sily pri tom vykonali prácu W = QU = 30 C · 3,75 V = 112,5 J, ktorá sa v rezistore premenila na teplo.</p><p><strong>d)</strong> Pri rovnakom prúde I = 0,25 A:</p><div class="formula">U = RI = 50 Ω · 0,25 A = 12,5 V</div><div class="result"><strong>a) 1,87 · 10²⁰ elektrónov; b) I = 0,25 A; c) U = 3,75 V; d) U = 12,5 V.</strong></div><p class="subtle">Pri rovnakom prúde je napätie priamo úmerné odporu. Aby rezistorom s väčším odporom prechádzal rovnaký prúd, musí zdroj dodať väčšie napätie.</p>'''

V3 = f'''<h2>3. Experiment – stacionárne magnetické pole</h2><h3>3.1 Princíp</h3><p>Stacionárne magnetické pole sa s časom nemení. Vytvárajú ho permanentné magnety a vodiče, ktorými prechádza stály prúd. Železné piliny sa v magnetickom poli zmagnetizujú a správajú sa ako malé magnetky – usporiadajú sa pozdĺž <strong>indukčných čiar</strong>. Indukčné čiary sú uzavreté krivky; mimo magnetu smerujú od severného pólu N k južnému S. Ich smer určíme magnetkou – jej severný pól ukazuje smer čiar.</p><h3>3.2 Pomôcky</h3><p>Tyčové magnety, železné piliny v sypátku, priehľadná doska alebo tvrdý papier, magnetka, vodič prestrčený zvislo cez dosku, závit (cievka) prestrčený cez dosku, nízkonapäťový zdroj s väčším prúdom (niekoľko ampérov), spínač.</p><h3>3.3 Postup a pozorovanie</h3><ol><li><strong>Tyčový magnet:</strong> magnet položíme pod dosku, nasypeme piliny a jemne poklepeme. Čiary vychádzajú z pólov a obopínajú magnet; najhustejšie sú pri póloch, kde je pole najsilnejšie.</li><li><strong>Priamy vodič:</strong> vodič prechádza kolmo cez dosku. Po zapnutí prúdu sa piliny usporiadajú do sústredných kružníc okolo vodiča. Smer čiar určuje <strong>Ampérovo pravidlo pravej ruky</strong>: palec ukazuje smer prúdu, prsty smer čiar. Pole slabne so vzdialenosťou od vodiča.</li><li><strong>Závit (cievka):</strong> okolo každej strany závitu sú kružnice, vnútri závitu sú čiary takmer rovnobežné. Cievka má pole podobné tyčovému magnetu; vnútri dlhej cievky je pole homogénne.</li><li><strong>Nesúhlasné póly (N k S):</strong> čiary prechádzajú z jedného magnetu do druhého – magnety sa priťahujú.</li><li><strong>Súhlasné póly (N k N):</strong> čiary sa od seba odkláňajú a medzi pólmi vznikne miesto, kde je pole takmer nulové (bez pilín) – magnety sa odpudzujú.</li></ol>{POLE1}{POLE2}<p>V obrázkoch ⊙ znamená prúd smerujúci k pozorovateľovi, ⊗ od pozorovateľa. Červený bod medzi súhlasnými pólmi označuje miesto s nulovým poľom.</p><div class="result"><strong>Záver:</strong> Magnetické pole magnetu aj vodiča s prúdom má uzavreté indukčné čiary. Pole priameho vodiča tvoria sústredné kružnice, pole závitu a cievky sa podobá poľu tyčového magnetu. Nesúhlasné póly sa priťahujú, súhlasné odpudzujú.</div><h3>3.4 Bezpečnosť a chyby</h3><p>Používame len nízke napätie a prúd zapíname krátko – vodič sa zahrieva. Piliny nesypeme priamo na magnet (ťažko sa odstraňujú) a chránime oči. Pri slabom prúde je obrazec pri vodiči nevýrazný; pomôže väčší prúd alebo viac závitov.</p>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO29', 'Otázka', 'maturit'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
