"""Vzor 21 zo zdrojov MO21_zadanie.html + MO21_riesenie.html a fotky 21 (stavy A → B → C → D, text doplnený, obrázky prekreslené)
-> Vzor21_zadanie.html + Vzor21_vypracovanie.html.
Spustenie: python -I gen21.py <priečinok FYZIKA>"""
import sys, math, pathlib

DST = pathlib.Path(sys.argv[1])
N = 21
TOPICS = ['Striedavý prúd – výroba a transformácia', 'Štruktúra a vlastnosti plynov', 'Premeny mechanickej energie']

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

# ---------- obrázky ----------
T = 'font-size="16" fill="#193b59"'

GENERATOR = ('<svg class="diagram" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Princíp generátora striedavého napätia: závit sa otáča v magnetickom poli medzi pólmi N a S, cez zberacie krúžky je pripojený k spotrebiču">'
             '<path d="M40 60H120V190H40Z" fill="#c0392b"/><path d="M360 60H440V190H360Z" fill="#2f6db3"/>'
             '<g font-size="22" font-weight="bold" fill="#fff"><text x="70" y="133">N</text><text x="392" y="133">S</text></g>'
             '<g stroke="#637889" stroke-width="1.3" stroke-dasharray="5 4" fill="none"><path d="M120 90H360M120 125H360M120 160H360"/></g>'
             '<path d="M200 70L280 90V180L200 160Z" fill="none" stroke="#b87333" stroke-width="5" stroke-linejoin="round"/>'
             '<path d="M240 40V212" stroke="#193b59" stroke-width="2" stroke-dasharray="8 5"/>'
             '<path d="M214 30A30 10 0 1 0 266 30" fill="none" stroke="#c0392b" stroke-width="2.2"/><path d="M262 22L268 31L258 34" fill="none" stroke="#c0392b" stroke-width="2.2"/>'
             '<g stroke="#193b59" stroke-width="2.5" fill="none"><ellipse cx="240" cy="222" rx="18" ry="5"/><ellipse cx="240" cy="236" rx="18" ry="5"/>'
             '<path d="M200 160V222H222M280 180V236H258M258 222H520V150M258 236H540V150"/><circle cx="530" cy="130" r="22" fill="#fff"/></g>'
             '<text x="520" y="138" font-size="22" fill="#193b59">~</text>'
             '<g font-size="15"><text x="272" y="34" fill="#c0392b">ω</text><text x="146" y="82" fill="#637889">B</text><text x="290" y="200" fill="#b87333">závit</text>'
             '<text x="60" y="240" fill="#193b59">zberacie krúžky</text><text x="560" y="135" fill="#193b59">u</text></g></svg>')

def sinus3():
    X = lambda t: 60 + 380 * t
    farby = ('#c0392b', '#2f6db3', '#26724c')
    cesty = ''.join(f'<polyline points="' + ' '.join(f'{X(i / 200):.1f},{110 - 70 * math.sin(2 * math.pi * (i / 200) - k * 2 * math.pi / 3):.1f}' for i in range(201)) + f'" fill="none" stroke="{farby[k]}" stroke-width="2.5"/>' for k in range(3))
    return ('<svg class="diagram" viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Trojfázová sústava: tri sínusové napätia rovnakej amplitúdy posunuté o tretinu periódy">'
            '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M60 196V24M50 110H470M54 36L60 24L66 36M458 104L470 110L458 116"/></g>'
            f'{cesty}<g font-size="14" fill="#253d51"><text x="68" y="24">u</text><text x="462" y="130">t</text></g>'
            '<g font-size="14"><text x="120" y="210" fill="#c0392b">L1</text><text x="200" y="210" fill="#2f6db3">L2</text><text x="280" y="210" fill="#26724c">L3</text>'
            '<text x="330" y="210" fill="#637889">posun o T/3 (120°)</text></g></svg>')

SINUS3 = sinus3()

def transformator(vyp):
    u2 = 'U₂ = 115 V' if vyp else 'U₂ = ?'
    civ = lambda x1, x2, ys: ''.join(f'M{x1} {y}H{x2}' for y in ys)
    return ('<svg class="diagram" viewBox="0 0 560 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Transformátor: primárna cievka s 5000 závitmi na napätí 230 V, sekundárna cievka s 2500 závitmi">'
            '<path d="M200 40H360V200H200ZM228 68V172H332V68Z" fill="#b9c4cf" fill-rule="evenodd" stroke="#637889" stroke-width="1.5"/>'
            f'<g stroke="#b87333" stroke-width="4" fill="none"><path d="{civ(192, 236, range(76, 168, 8))}{civ(324, 368, range(80, 165, 14))}"/></g>'
            '<g stroke="#193b59" stroke-width="3" fill="none"><path d="M192 76H90M192 164H90M368 80H470M368 164H470"/></g>'
            '<g fill="#fff" stroke="#193b59" stroke-width="2"><circle cx="86" cy="76" r="5"/><circle cx="86" cy="164" r="5"/><circle cx="474" cy="76" r="5"/><circle cx="474" cy="164" r="5"/></g>'
            f'<g {T}><text x="40" y="125">U₁ = 230 V</text><text x="480" y="125">{u2}</text><text x="140" y="222">N₁ = 5 000</text><text x="318" y="222">N₂ = 2 500</text><text x="258" y="30">jadro</text></g></svg>')

TRAFO_Z = transformator(False)
TRAFO_V = transformator(True)

# p–V: V 0–14 m³ -> 30 px/m³ od x=70; p 0–0,5 MPa -> 500 px/MPa od y=290
def pv(vyp):
    X = lambda v: 70 + 30 * v
    Y = lambda p: 290 - 500 * p
    a, b, c, d = (X(3), Y(0.4)), (X(12), Y(0.4)), (X(12), Y(0.1)), (X(3), Y(0.1))
    plocha = f'<rect x="{a[0]}" y="{a[1]}" width="{b[0] - a[0]}" height="{d[1] - a[1]}" fill="#f6dccd"/><text x="{(a[0] + b[0]) / 2 - 46:.0f}" y="{(a[1] + d[1]) / 2 + 5:.0f}" font-size="15" fill="#c0392b">W = 2,7 MJ</text>' if vyp else ''
    sip = lambda x, y, sm: {'r': f'M{x - 8} {y - 7}L{x + 4} {y}L{x - 8} {y + 7}', 'l': f'M{x + 8} {y - 7}L{x - 4} {y}L{x + 8} {y + 7}',
                            'd': f'M{x - 7} {y - 8}L{x} {y + 4}L{x + 7} {y - 8}', 'u': f'M{x - 7} {y + 8}L{x} {y - 4}L{x + 7} {y + 8}'}[sm]
    sipky = sip((a[0] + b[0]) / 2, a[1], 'r') + sip(b[0], (b[1] + c[1]) / 2, 'd') + sip((c[0] + d[0]) / 2, c[1], 'l') + sip(a[0], (a[1] + d[1]) / 2, 'u')
    return ('<svg class="diagram" viewBox="0 0 560 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="p–V diagram kruhového deja: A (3 m³; 0,4 MPa), B (12 m³; 0,4 MPa), C (12 m³; 0,1 MPa), D (3 m³; 0,1 MPa), smer A, B, C, D, A">'
            f'{plocha}<g stroke="#dbe5ee" stroke-width="1" stroke-dasharray="5 4" fill="none"><path d="M70 {a[1]}H{a[0]}M70 {d[1]}H{d[0]}M{a[0]} 290V{d[1]}M{b[0]} 290V{c[1]}"/></g>'
            '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M70 302V25M60 290H520M64 37L70 25L76 37M508 284L520 290L508 296"/></g>'
            f'<path d="M{a[0]} {a[1]}H{b[0]}V{c[1]}H{d[0]}Z" fill="none" stroke="#2f6db3" stroke-width="3"/>'
            f'<path d="{sipky}" fill="none" stroke="#2f6db3" stroke-width="2.5"/>'
            f'<g fill="#2f6db3">' + ''.join(f'<circle cx="{x}" cy="{y}" r="5"/>' for x, y in (a, b, c, d)) + '</g>'
            f'<g font-size="17" fill="#193b59"><text x="{a[0] - 22}" y="{a[1] - 8}">A</text><text x="{b[0] + 8}" y="{b[1] - 8}">B</text><text x="{c[0] + 8}" y="{c[1] + 20}">C</text><text x="{d[0] - 22}" y="{d[1] + 20}">D</text></g>'
            f'<g font-size="14" fill="#253d51"><text x="34" y="{a[1] + 5}">0,4</text><text x="34" y="{d[1] + 5}">0,1</text><text x="{a[0] - 4}" y="310">3</text><text x="{b[0] - 8}" y="310">12</text>'
            '<text x="80" y="24">p (MPa)</text><text x="490" y="314">V (m³)</text></g></svg>')

PV_Z = pv(False)
PV_V = pv(True)

def kyvadlo():
    L = 190
    ox, oy = 280, 30
    al = math.radians(38)
    bx, by = ox - L * math.sin(al), oy + L * math.cos(al)
    h = L - L * math.cos(al)
    return ('<svg class="diagram" viewBox="0 0 560 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kyvadlo vychýlené do výšky h nad najnižšiu polohu, v ktorej je svetelná závora meriaca rýchlosť guľôčky">'
            '<path d="M200 30H360" stroke="#193b59" stroke-width="5"/>'
            f'<path d="M{ox} {oy}L{bx:.1f} {by:.1f}" stroke="#637889" stroke-width="2"/><path d="M{ox} {oy}V{oy + L}" stroke="#637889" stroke-width="1.5" stroke-dasharray="5 4"/>'
            f'<path d="M{bx:.1f} {by:.1f}A{L} {L} 0 0 0 {ox + L * math.sin(al):.1f} {by:.1f}" fill="none" stroke="#9fb3c8" stroke-width="1.5" stroke-dasharray="4 4"/>'
            f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="12" fill="#c0392b"/><circle cx="{ox}" cy="{oy + L}" r="12" fill="#e8a093" stroke="#c0392b" stroke-width="2"/>'
            f'<g stroke="#193b59" stroke-width="2.5" fill="none"><path d="M{ox - 30} {oy + L + 22}V{oy + L - 30}M{ox + 30} {oy + L + 22}V{oy + L - 30}M{ox - 30} {oy + L + 22}H{ox + 30}"/></g>'
            f'<path d="M{ox - 30} {oy + L}H{ox + 30}" stroke="#e53935" stroke-width="1.5" stroke-dasharray="3 3"/>'
            f'<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M{bx - 50:.1f} {by:.1f}H{bx - 14:.1f}M{bx - 50:.1f} {oy + L}H{ox - 34}M{bx - 40:.1f} {by:.1f}V{oy + L}"/></g>'
            f'<g {T}><text x="{bx - 66:.0f}" y="{(by + oy + L) / 2 + 5:.0f}">h</text><text x="{ox + 40}" y="{oy + L + 18}">svetelná závora</text>'
            f'<text x="{bx - 150:.0f}" y="{by - 22:.0f}">Eₚ max, v = 0</text><text x="{ox + 40}" y="{oy + L - 30}">Eₖ max</text><text x="{ox + 8}" y="{oy + 110}">l</text></g></svg>')

KYVADLO = kyvadlo()

# ---------- zadanie ----------
Z1 = f'''<h2>1. Striedavý prúd – výroba a transformácia</h2><div class="task"><ol><li>Vysvetlite výrobu striedavého napätia a prúdu v alternátore. Čo je trojfázová sústava?</li><li>Vysvetlite princíp činnosti transformátora. Prečo sa elektrická energia prenáša pri vysokom napätí?</li><li>Opíšte rôzne typy elektrární a premeny energie v nich.</li></ol><p><strong>Úloha:</strong> Ideálny transformátor má na primárnej cievke <strong>N₁ = 5 000 závitov</strong> a na sekundárnej <strong>N₂ = 2 500 závitov</strong>. Primárne napätie je <strong>U₁ = 230 V</strong>.</p>{TRAFO_Z}<ol type="a"><li>Vypočítajte sekundárne napätie U₂.</li><li>Určte transformačný pomer a uveďte, ako ho definujete.</li><li>Rozhodnite, či ide o zvyšovací alebo znižovací transformátor.</li></ol></div>'''

Z2 = f'''<h2>2. Štruktúra a vlastnosti plynov</h2><div class="task"><ol><li>Opíšte štruktúru plynov z hľadiska molekulovej fyziky. Čo je ideálny plyn?</li><li>Napíšte stavovú rovnicu ideálneho plynu a charakterizujte základné deje v plyne.</li><li>Ako sa určí práca plynu z p–V diagramu?</li></ol><p><strong>Úloha:</strong> Ideálny plyn s nemennou hmotnosťou prechádza kruhovým dejom A → B → C → D → A podľa p–V diagramu.</p>{PV_Z}<ol type="a"><li>Opíšte jednotlivé deje medzi stavmi. Pri každom uveďte, či plyn koná kladnú, zápornú alebo nulovú prácu, a ako sa mení jeho teplota.</li><li>Vypočítajte prácu plynu na jednotlivých úsekoch a celkovú prácu W za celý kruhový dej.</li></ol></div>'''

Z3 = '''<h2>3. Experiment – premeny mechanickej energie</h2><div class="task"><p>Navrhnite a vykonajte experiment, v ktorom pozorujete a porovnáte premeny potenciálnej energie na kinetickú a naopak. Na základe meraní overte zákon zachovania mechanickej energie a vysvetlite vplyv odporových síl.</p></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Striedavý prúd – výroba a transformácia</h2><h3>1.1 Výroba striedavého napätia</h3><p>Striedavé napätie vzniká <strong>elektromagnetickou indukciou</strong>. Ak sa závit (cievka s N závitmi) otáča stálou uhlovou rýchlosťou ω v homogénnom magnetickom poli, magnetický indukčný tok sa mení harmonicky, Φ = BS cos ωt. Podľa Faradayovho zákona sa indukuje napätie:</p>{GENERATOR}<div class="formula">u = U<sub>m</sub> sin ωt &nbsp;&nbsp;&nbsp; U<sub>m</sub> = N B S ω</div><p>V elektrárňach sa používa <strong>alternátor</strong>: otáča sa elektromagnet (rotor) a napätie sa indukuje v nepohyblivých cievkach statora – nie sú potrebné zberacie krúžky pre veľké prúdy. Frekvencia siete je f = 50 Hz. Napätie siete udávame <strong>efektívnou hodnotou</strong> U = U<sub>m</sub>/√2 = 230 V (amplitúda ≈ 325 V).</p><p><strong>Trojfázová sústava:</strong> alternátor má tri cievky statora pootočené o 120°. Vznikajú tri napätia rovnakej amplitúdy a frekvencie, fázovo posunuté o tretinu periódy. Medzi fázovým a stredným vodičom je 230 V, medzi dvoma fázami 400 V. Trojfázový prúd umožňuje hospodárny prenos a vytvára točivé magnetické pole pre elektromotory.</p>{SINUS3}<p>Činný výkon v obvode striedavého prúdu je P = U I cos φ, kde cos φ je účinník. Pri odporovej záťaži P = UI. Elektrická energia je E = P t (v praxi v kWh).</p><h3>1.2 Transformátor a prenos energie</h3><p>Transformátor má primárnu a sekundárnu cievku na spoločnom uzavretom jadre z izolovaných plechov. Striedavý prúd v primárnej cievke vytvára v jadre premenlivý magnetický tok. Ten prechádza aj sekundárnou cievkou a indukuje v nej napätie. Pre ideálny transformátor (bez strát):</p><div class="formula">U₂ / U₁ = N₂ / N₁ = k &nbsp;&nbsp;&nbsp; I₂ / I₁ = N₁ / N₂ &nbsp;&nbsp;&nbsp; P₁ = P₂</div><p>Transformátor pracuje len so striedavým prúdom – stály prúd nevytvára premenlivý tok.</p><p><strong>Prenos energie:</strong> straty vo vedení sú ΔP = R I². Pri rovnakom prenášanom výkone P = UI je pri vyššom napätí prúd menší – pri desaťnásobnom napätí sú straty stokrát menšie. Preto sa napätie z alternátora (asi 10–25 kV) zvyšuje na 110–400 kV, prenáša sa a pri spotrebiteľoch sa postupne znižuje na 230/400 V.</p><h3>1.3 Typy elektrární</h3><table><tr><th>Elektráreň</th><th>Premena energie</th></tr><tr><td>tepelná (uhlie, plyn, biomasa)</td><td>chemická → vnútorná (para) → mechanická (turbína) → elektrická</td></tr><tr><td>jadrová</td><td>jadrová (štiepenie uránu) → vnútorná → mechanická → elektrická</td></tr><tr><td>vodná (prietočná, akumulačná, prečerpávacia)</td><td>potenciálna a kinetická energia vody → mechanická → elektrická</td></tr><tr><td>veterná</td><td>kinetická energia vetra → mechanická → elektrická</td></tr><tr><td>fotovoltická</td><td>energia slnečného žiarenia → elektrická priamo (jednosmerný prúd, menič ho mení na striedavý)</td></tr><tr><td>geotermálna, slapová</td><td>vnútorná energia Zeme, energia prílivu → mechanická → elektrická</td></tr></table><p>Okrem fotovoltiky vyrábajú všetky elektrárne elektrickú energiu alternátorom poháňaným turbínou. Prečerpávacia vodná elektráreň uchováva energiu: pri nadbytku čerpá vodu hore, pri špičke vyrába.</p><h3>1.4 Riešenie úlohy</h3>{TRAFO_V}<p><strong>a)</strong> Pre ideálny transformátor:</p><div class="formula">U₂ = U₁ · N₂ / N₁ = 230 V · 2 500 / 5 000 = 115 V</div><p><strong>b)</strong> Transformačný pomer definujeme ako podiel sekundárneho a primárneho napätia:</p><div class="formula">k = U₂ / U₁ = N₂ / N₁ = 2 500 / 5 000 = 0,5</div><p>Niektoré učebnice používajú opačnú definíciu k′ = N₁/N₂ = 2. Preto treba vždy uviesť, ktorý podiel myslíme.</p><p><strong>c)</strong> k &lt; 1 (N₂ &lt; N₁), napätie sa zmenšilo na polovicu – ide o <strong>znižovací transformátor</strong>. Prúd v sekundárnom obvode bude dvojnásobný oproti primárnemu.</p><div class="result"><strong>U₂ = 115 V; k = N₂/N₁ = 0,5; znižovací transformátor.</strong></div>'''

V2 = f'''<h2>2. Štruktúra a vlastnosti plynov</h2><h3>2.1 Štruktúra plynov a ideálny plyn</h3><p>Molekuly plynu sú od seba v priemere oveľa ďalej, ako sú ich rozmery. Vzájomné príťažlivé sily sú preto veľmi slabé a plyn nemá stály tvar ani objem – vyplní celú nádobu. Molekuly sa pohybujú neusporiadane (tepelný pohyb) veľkými rýchlosťami, rádovo stovky m/s, a navzájom sa zrážajú. Dôkazom je difúzia a Brownov pohyb. <strong>Tlak plynu</strong> je dôsledkom nárazov molekúl na steny nádoby.</p><p><strong>Ideálny plyn</strong> je model: rozmery molekúl zanedbávame, molekuly na seba pôsobia len pri zrážkach a zrážky sú dokonale pružné. Skutočné plyny sa mu podobajú pri nízkych tlakoch a vysokých teplotách. Termodynamická teplota je úmerná strednej kinetickej energii molekúl: E<sub>k</sub> = 3/2 kT.</p><h3>2.2 Stavová rovnica a deje v plyne</h3><div class="formula">p V = n R T = N k T &nbsp;&nbsp;&nbsp; pre stálu hmotnosť: p V / T = konšt.</div><ul><li><strong>izotermický</strong> dej (T = konšt.): pV = konšt. (Boylov-Mariottov zákon), v p–V diagrame hyperbola,</li><li><strong>izobarický</strong> dej (p = konšt.): V/T = konšt. (Gay-Lussacov zákon), vodorovná úsečka,</li><li><strong>izochorický</strong> dej (V = konšt.): p/T = konšt. (Charlesov zákon), zvislá úsečka,</li><li><strong>adiabatický</strong> dej: bez tepelnej výmeny s okolím.</li></ul><h3>2.3 Práca plynu</h3><p>Pri izobarickom deji vykoná plyn prácu W′ = p ΔV. Všeobecne sa práca rovná <strong>obsahu plochy pod grafom</strong> v p–V diagrame. Pri zväčšovaní objemu plyn prácu koná (W′ &gt; 0), pri zmenšovaní ju konajú vonkajšie sily (W′ &lt; 0). Pri izochorickom deji je W′ = 0.</p><p>Pri <strong>kruhovom deji</strong> sa plyn vráti do počiatočného stavu. Celková práca sa rovná obsahu plochy ohraničenej uzavretou krivkou. Ak cyklus prebieha v smere hodinových ručičiek, je celková práca kladná – na tom pracujú tepelné motory. Podľa 1. termodynamického zákona Q = ΔU + W′ a za cyklus ΔU = 0, takže W′ = Q<sub>prijaté</sub> − Q<sub>odovzdané</sub>.</p><h3>2.4 Riešenie úlohy</h3>{PV_V}<p><strong>a)</strong> Deje. Teplotu porovnáme zo stavovej rovnice pV/T = konšt. Súčin pV je úmerný teplote: p<sub>A</sub>V<sub>A</sub> = 1,2 MJ, p<sub>B</sub>V<sub>B</sub> = 4,8 MJ, p<sub>C</sub>V<sub>C</sub> = 1,2 MJ, p<sub>D</sub>V<sub>D</sub> = 0,3 MJ. Teda T<sub>B</sub> = 4T<sub>A</sub>, T<sub>C</sub> = T<sub>A</sub>, T<sub>D</sub> = T<sub>A</sub>/4.</p><table><tr><th>Dej</th><th>Charakter</th><th>Teplota</th><th>Práca plynu</th></tr><tr><td>A → B</td><td>izobarické rozpínanie pri 0,4 MPa</td><td>rastie 4-krát</td><td>kladná</td></tr><tr><td>B → C</td><td>izochorický pokles tlaku pri 12 m³</td><td>klesá 4-krát</td><td>nulová</td></tr><tr><td>C → D</td><td>izobarické stláčanie pri 0,1 MPa</td><td>klesá 4-krát</td><td>záporná</td></tr><tr><td>D → A</td><td>izochorický rast tlaku pri 3 m³</td><td>rastie 4-krát</td><td>nulová</td></tr></table><p>Pri A → B a D → A plyn teplo prijíma, pri B → C a C → D ho odovzdáva.</p><p><strong>b)</strong> Práca na úsekoch:</p><div class="formula">W′<sub>AB</sub> = p<sub>A</sub> (V<sub>B</sub> − V<sub>A</sub>) = 0,4 · 10⁶ Pa · (12 − 3) m³ = 3,6 · 10⁶ J = 3,6 MJ<br>W′<sub>BC</sub> = 0 &nbsp;&nbsp;&nbsp; W′<sub>DA</sub> = 0<br>W′<sub>CD</sub> = p<sub>C</sub> (V<sub>D</sub> − V<sub>C</sub>) = 0,1 · 10⁶ Pa · (3 − 12) m³ = −0,9 MJ</div><div class="formula">W = 3,6 MJ + 0 − 0,9 MJ + 0 = 2,7 MJ</div><p>Kontrola obsahom obdĺžnika: (0,4 − 0,1) MPa · (12 − 3) m³ = 0,3 · 10⁶ Pa · 9 m³ = 2,7 MJ. Cyklus prebieha v smere hodinových ručičiek, preto je celková práca kladná.</p><div class="result"><strong>W′<sub>AB</sub> = 3,6 MJ, W′<sub>BC</sub> = 0, W′<sub>CD</sub> = −0,9 MJ, W′<sub>DA</sub> = 0; za cyklus W = 2,7 MJ.</strong></div>'''

# modelové údaje: m = 0,100 kg, d = 2,0 cm
DATA = [(5.0, 20.4), (10.0, 14.5), (20.0, 10.3)]
def riadky(desat):
    r = ''
    for h, dt in DATA:
        v = 0.02 / (dt / 1000)
        ep = 0.1 * 9.81 * h / 100
        ek = 0.5 * 0.1 * v * v
        cis = lambda x, n: f'{x:.{n}f}'.replace('.', desat)
        r += f'<tr><td>{cis(h, 1)}</td><td>{cis(dt, 1)}</td><td>{cis(v, 2)}</td><td>{cis(ep * 1000, 1)}</td><td>{cis(ek * 1000, 1)}</td><td>{round(100 * ek / ep)} %</td></tr>'
    return r

V3 = f'''<h2>3. Experiment – premeny mechanickej energie</h2><h3>3.1 Teória</h3><p>Kinetická energia E<sub>k</sub> = ½ m v² je energia pohybu, potenciálna tiažová energia E<sub>p</sub> = m g h je energia polohy. Ich súčet je mechanická energia. <strong>Zákon zachovania mechanickej energie:</strong> ak pôsobia len konzervatívne sily (tiažová, pružná), mechanická energia je stála a mení sa len jej forma:</p><div class="formula">E<sub>k</sub> + E<sub>p</sub> = konšt. &nbsp; → &nbsp; m g h = ½ m v² &nbsp; → &nbsp; v = √(2 g h)</div><p>Odporové sily (odpor vzduchu, trenie) konajú zápornú prácu a časť mechanickej energie sa mení na vnútornú energiu telies a prostredia.</p><h3>3.2 Pomôcky</h3><p>Kyvadlo: guľôčka s hmotnosťou m = 100 g a priemerom d = 2,0 cm na tenkom neprestupnom vlákne, stojan, svetelná závora s časomerom (meria čas Δt zatienenia), meradlo výšky, váha.</p><h3>3.3 Usporiadanie a pozorovanie</h3>{KYVADLO}<p>Svetelná závora je v najnižšej polohe guľôčky. Guľôčku vychýlime tak, aby bola o výšku h vyššie, a pustíme ju bez počiatočnej rýchlosti.</p><ul><li><strong>Krajná poloha:</strong> v = 0, E<sub>k</sub> = 0, E<sub>p</sub> je najväčšia.</li><li><strong>Pri pohybe dole:</strong> E<sub>p</sub> klesá a E<sub>k</sub> rastie o rovnakú hodnotu.</li><li><strong>Najnižšia poloha:</strong> E<sub>p</sub> = 0 (nulová hladina), rýchlosť a E<sub>k</sub> sú najväčšie.</li><li><strong>Na druhej strane</strong> sa E<sub>k</sub> opäť mení na E<sub>p</sub> a guľôčka vystúpi takmer do rovnakej výšky. Po mnohých kmitoch sa výchylka zmenšuje – prejav odporových síl.</li></ul><h3>3.4 Postup merania</h3><ol><li>Zvážime guľôčku a zmeriame jej priemer d.</li><li>Guľôčku zdvihneme do výšky h nad najnižšiu polohu (meriame výšku jej stredu) a pustíme.</li><li>Časomer zaznamená čas Δt, počas ktorého guľôčka zatieni lúč. Rýchlosť v najnižšej polohe je v = d/Δt.</li><li>Meranie zopakujeme pre rôzne výšky h.</li><li>Pre každú výšku porovnáme E<sub>p</sub> = mgh a E<sub>k</sub> = ½mv².</li></ol><h3>3.5 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje pre m = 0,100 kg, d = 2,0 cm, g = 9,81 m/s²; nejde o skutočné meranie.</p><table><tr><th>h (cm)</th><th>Δt (ms)</th><th>v = d/Δt (m/s)</th><th>E<sub>p</sub> (mJ)</th><th>E<sub>k</sub> (mJ)</th><th>E<sub>k</sub>/E<sub>p</sub></th></tr>{riadky(',')}</table><p>Napríklad pre h = 10,0 cm:</p><div class="formula">E<sub>p</sub> = m g h = 0,100 · 9,81 · 0,100 J ≈ 98,1 mJ<br>v = d/Δt = 0,020 m / 0,0145 s ≈ 1,38 m/s &nbsp;&nbsp; E<sub>k</sub> = ½ · 0,100 · 1,38² J ≈ 95,1 mJ</div><p>Kinetická energia v najnižšom bode je 96–98 % potenciálnej energie v krajnej polohe. Zákon zachovania mechanickej energie je v rámci presnosti merania splnený. Teoretická rýchlosť pre h = 10 cm je v = √(2gh) ≈ 1,40 m/s.</p><h3>3.6 Nepresnosti a vplyv odporových síl</h3><ul><li>Odpor vzduchu a trenie v závese – časť energie sa mení na vnútornú energiu, E<sub>k</sub> vyjde o niečo menšia. Pri väčšej výške (rýchlosti) je strata väčšia, lebo odpor vzduchu rastie s rýchlosťou.</li><li>Závora meria strednú rýchlosť na dráhe d, nie okamžitú. Lúč musí prechádzať stredom guľôčky.</li><li>Nepresné určenie výšky h (meriame výšku stredu guľôčky).</li><li>Guľôčka sa môže pri pohybe pootáčať a kmitať do strán – časť energie pripadne na tieto pohyby.</li></ul><div class="result"><strong>Záver:</strong> Pri pohybe kyvadla sa potenciálna energia mení na kinetickú a naopak. Meranie ukázalo E<sub>k</sub> ≈ E<sub>p</sub> (96–98 %); malý rozdiel spôsobujú odporové sily, ktoré časť mechanickej energie menia na vnútornú energiu.</div>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO21', 'Otázka', 'maturit', 'riginál'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
