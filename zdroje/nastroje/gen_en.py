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
    8: ['Molecular Physics and Thermodynamics', 'Electromagnetic Waves', 'Simple Pendulum'],
    9: ['Changes of State', 'Electron in an Electric Field', 'Progressive Transverse Waves'],
    10: ['Properties of Gases', 'Pressure in a Tyre', 'Concave Spherical Mirror'],
    11: ['Properties of Liquids', 'Thin-Film Interference', 'Current–Voltage Characteristic of a Diode'],
    12: ['Solids', 'Photoelectric Effect', 'Inertial Mass'],
    13: ['Electric Current in Semiconductors', 'Mechanics of a Rigid Body', 'Inductance and Capacitance'],
    14: ['Electric Current in Electrolytes', 'Energy of a Particle', 'Efficiency of a Transformer'],
    15: ['Electric Field', 'Atomic Nucleus', 'Inclined Plane'],
    16: ['Electric Current', 'Kinematics – v–t Graph', 'Wavelength of Light'],
    17: ['Electric Current in Metals', 'Dynamics – Bullet in a Barrel', 'Surface Layer of a Liquid'],
    18: ['Free Oscillations', 'Motion in a Gravitational Field – Horizontal Projection', 'Diameter of an Oleic Acid Molecule'],
    19: ['Magnetic Field', 'Fluid Mechanics – Flow in a Pipe', 'Specific Latent Heat of Fusion of Ice'],
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
    'Závesná pružina so závažím a meranie predĺženia a periódy': 'Hanging spring with a mass; measuring the extension and the period',
    'Stopky: čas N kmitov': 'Time of N oscillations', 'bez závažia': 'without load',
    'Graf závislosti druhej mocniny periódy od dĺžky kyvadla': 'Graph of the square of the period against the length of the pendulum',
    'Schéma matematického kyvadla': 'Diagram of a simple pendulum',
    'Dĺžka l sa meria od závesu po ťažisko závažia.': 'Length l is measured from the pivot to the centre of the bob.',
    'Ilustračné výsledky – približne lineárna závislosť': 'Illustrative results – approximately linear dependence',
    'Schematický fázový diagram bežnej látky s kladným sklonom krivky topenia':
        'Schematic phase diagram of a typical substance with a positive slope of the melting curve',
    'Priečne vlnenie: lano sa vlní, body kmitajú zvislo a vlna sa šíri vodorovne':
        'Transverse wave: the rope undulates, points oscillate vertically and the wave travels horizontally',
    'PEVNÁ FÁZA': 'SOLID', 'KVAPALINA': 'LIQUID', 'PLYN': 'GAS', 'sublimácia': 'sublimation', 'topenie': 'melting',
    'vyparovanie': 'vaporisation', 'trojný bod': 'triple point', 'kritický bod': 'critical point',
    'nadkritická': 'supercritical', 'oblasť': 'region', 'šírenie vlnenia': 'direction of propagation',
    'Častice lana kmitajú kolmo na smer šírenia.': 'Rope particles oscillate perpendicular to the propagation.',
    'Dve paralelné vetvy po dvoch sériových kondenzátoroch, potom dva sériové kondenzátory':
        'Two parallel branches of two capacitors in series, followed by two capacitors in series',
    'Konštrukcia zdanlivého obrazu dutým zrkadlom': 'Construction of a virtual image in a concave mirror',
    'predmet': 'object', 'obraz': 'image',
    'Plné čiary: lúče. Prerušované čiary: ich predĺženia za zrkadlo.': 'Solid lines: rays. Dashed lines: their extensions behind the mirror.',
    'Odrazy svetla na olejovej vrstve': 'Reflections of light on an oil film',
    'Vzduch: n ≈ 1': 'Air: n ≈ 1', 'Olej: n = 1,50': 'Oil: n = 1.50', 'Voda: n ≈ 1,33': 'Water: n ≈ 1.33',
    'odraz: posun π': 'reflection: shift π', 'odraz: bez posunu π': 'reflection: no shift π', 'dopad': 'incident',
    'Schéma merania voltampérovej charakteristiky': 'Circuit for measuring the current–voltage characteristic',
    'Zdroj': 'Source', 'Dióda': 'Diode',
    'Ampérmeter sériovo, voltmeter paralelne k dióde.': 'Ammeter in series, voltmeter in parallel with the diode.',
    'Kvalitatívny graf charakteristiky diódy': 'Qualitative graph of the diode characteristic',
    'záverný smer': 'reverse bias', 'priepustný smer': 'forward bias',
    'Schematicky, bez mierky; nejde o namerané údaje.': 'Schematic, not to scale; not measured data.',
    'Obvod: zdroj, ampérmeter, rezistor a dióda v priepustnom smere v sérii; voltmeter V₁ na rezistore, V₂ na dióde':
        'Circuit: source, ammeter, resistor and forward-biased diode in series; voltmeter V₁ across the resistor, V₂ across the diode',
    'Voltampérová charakteristika diódy v priepustnom smere, pri prúde 4 A je napätie 1 V':
        'Current–voltage characteristic of the diode in forward bias; at a current of 4 A the voltage is 1 V',
    'Nosník dĺžky 6 m na dvoch stenách A a B s bremenom vo vzdialenosti x od steny A':
        'Beam of length 6 m on two walls A and B with a load at distance x from wall A',
    'Nosník na dvoch stenách s bremenom, sily pôsobiace na nosník': 'Beam on two walls with a load; forces acting on the beam',
    'Zapojenie: zdroj striedavého napätia, ampérmeter v sérii s kondenzátorom alebo cievkou, voltmeter paralelne':
        'Circuit: AC voltage source, ammeter in series with a capacitor or a coil, voltmeter in parallel',
    'C alebo L': 'C or L',
    'spínač': 'switch', 'zdroj': 'source', 'ampérmeter': 'ammeter', 'voltmeter': 'voltmeter', 'rezistor': 'resistor',
    'Elektrolýza roztoku síranu meďnatého medzi dvoma medenými elektródami; katióny medi idú ku katóde, síranové anióny k anóde':
        'Electrolysis of copper(II) sulfate solution between two copper electrodes; copper cations move to the cathode, sulfate anions to the anode',
    'anóda (+)': 'anode (+)', 'katóda (−)': 'cathode (−)', 'roztok CuSO₄': 'CuSO₄ solution',
    'Voltampérová charakteristika elektrolytického vodiča: s medenými elektródami priamka z počiatku, s inertnými elektródami prúd tečie až nad rozkladným napätím':
        'Current–voltage characteristic of an electrolytic conductor: a straight line through the origin with copper electrodes; with inert electrodes current flows only above the decomposition voltage',
    'Cu elektródy v CuSO₄': 'Cu electrodes in CuSO₄', 'inertné elektródy': 'inert electrodes',
    'Teleso s hmotnosťou 1 kg vo výške 45 m nad zemou, poloha v čase 1 s nie je známa':
        'Body of mass 1 kg at a height of 45 m above the ground; its position at 1 s is unknown',
    'zem (Eₚ = 0)': 'ground (Eₚ = 0)',
    'Poloha telesa pri voľnom páde z výšky 45 m v časoch 0, 1, 2 a 3 sekundy':
        'Position of a body falling freely from 45 m at times 0, 1, 2 and 3 seconds',
    'Graf kinetickej a potenciálnej energie od času pri voľnom páde; ich súčet je stále 450 J':
        'Graph of kinetic and potential energy against time in free fall; their sum is always 450 J',
    'Zapojenie na meranie účinnosti transformátora: zdroj, ampérmeter A1 a voltmeter V1 na primárnej cievke; ampérmeter A2, voltmeter V2 a záťaž R na sekundárnej cievke':
        'Circuit for measuring the efficiency of a transformer: source, ammeter A1 and voltmeter V1 on the primary coil; ammeter A2, voltmeter V2 and load R on the secondary coil',
    'jadro': 'core', 'záťaž R': 'load R',
    'Uzavretý obvod: zdroj s elektromotorickým napätím a vnútorným odporom, ampérmeter, vonkajší rezistor R a voltmeter na svorkách zdroja':
        'Complete circuit: source with emf and internal resistance, ammeter, external resistor R and voltmeter across the source terminals',
    'Zaťažovacia charakteristika zdroja: svorkové napätie lineárne klesá od elektromotorického napätia pri nulovom prúde po nulu pri skratovom prúde':
        'Load characteristic of a source: terminal voltage decreases linearly from the emf at zero current to zero at the short-circuit current',
    'naprázdno': 'open circuit', 'skrat': 'short circuit',
    'Graf rýchlosti od času s vyznačenými dráhami ako plochami pod grafom: 12 m, 24 m a 32 m':
        'Velocity–time graph with distances marked as areas under the graph: 12 m, 24 m and 32 m',
    'Graf rýchlosti od času: od 0 do 3 s rýchlosť 4 m/s, od 3 do 7 s rastie na 8 m/s, od 7 do 15 s klesá na nulu':
        'Velocity–time graph: from 0 to 3 s velocity 4 m/s, from 3 to 7 s it rises to 8 m/s, from 7 to 15 s it falls to zero',
    'Graf dráhy od času: priamka do 3 s, potom parabola so stúpajúcou strmosťou do 7 s a parabola s klesajúcou strmosťou do 15 s, kde dráha dosiahne 68 m':
        'Distance–time graph: a straight line up to 3 s, then a parabola of increasing steepness up to 7 s and a parabola of decreasing steepness up to 15 s, where the distance reaches 68 m',
    'Graf zrýchlenia od času: 0 do 3 s nulové, od 3 do 7 s 1 m/s², od 7 do 15 s mínus 1 m/s², potom nulové':
        'Acceleration–time graph: zero from 0 to 3 s, 1 m/s² from 3 to 7 s, minus 1 m/s² from 7 to 15 s, then zero',
    'Laser, optická mriežka a tienidlo vo vzdialenosti L; na tienidle stredové maximum a maximá 1. a 2. rádu vo vzdialenostiach x1 a x2':
        'Laser, diffraction grating and screen at distance L; on the screen the central maximum and 1st- and 2nd-order maxima at distances x1 and x2',
    'laser': 'laser', 'mriežka': 'grating', 'tienidlo': 'screen',
    'Pružinový oscilátor: závažie na pružine kmitá okolo rovnovážnej polohy medzi výchylkami plus A a mínus A':
        'Mass–spring oscillator: the mass oscillates about the equilibrium position between displacements plus A and minus A',
    'rovnovážna poloha: y = 0':
        'equilibrium position: y = 0',
    'Graf výchylky od času s vyznačenou amplitúdou 90 mm a periódou 0,2 s':
        'Displacement–time graph with the amplitude 90 mm and the period 0.2 s marked',
    'Graf výchylky od času: sínusoida s maximom 90 mm, začína v nule a stúpa, prechody nulou v časoch 0,1 s, 0,2 s a 0,3 s':
        'Displacement–time graph: a sine curve with a maximum of 90 mm, starting at zero and rising, crossing zero at 0.1 s, 0.2 s and 0.3 s',
    'Teleso vrhnuté vodorovne rýchlosťou 60 m/s z výšky 60 m; poloha v čase 2 s a miesto dopadu sú neznáme':
        'Body projected horizontally at 60 m/s from a height of 60 m; its position at 2 s and the point of impact are unknown',
    'Trajektória vodorovného vrhu v mierke: v čase 2 s je teleso 120 m od okraja a 40 m nad zemou, dopadne 208 m od okraja pod uhlom 30 stupňov':
        'Trajectory of the horizontal projection to scale: at 2 s the body is 120 m from the edge and 40 m above the ground; it lands 208 m from the edge at an angle of 30 degrees',
    'dopad po 3,46 s':
        'impact after 3.46 s',
    'Vľavo pohľad zhora na vaničku s vodou posypanou práškom a kruhovou olejovou škvrnou s priemerom D; vpravo rez jednomolekulovou vrstvou hrúbky d na hladine vody':
        'Left: top view of a tray of water sprinkled with powder and a circular oil film of diameter D; right: cross-section of the monomolecular layer of thickness d on the water surface',
    'pohľad zhora':
        'top view',
    'rez vrstvou (zväčšené)':
        'cross-section (enlarged)',
    'voda':
        'water',
    'molekuly kyseliny olejovej':
        'oleic acid molecules',
    '– polárna skupina vo vode':
        '– polar group in the water',
    'Indukčné čiary tyčového magnetu vychádzajú zo severného pólu a vstupujú do južného pólu':
        'Field lines of a bar magnet leave the north pole and enter the south pole',
    'Indukčné čiary cievky s prúdom: vo vnútri rovnobežné, zvonka sa uzatvárajú ako pri tyčovom magnete':
        'Field lines of a current-carrying coil: parallel inside, closing outside as for a bar magnet',
    'Dva rovnobežné vodiče: pri prúdoch rovnakého smeru sa priťahujú, pri prúdoch opačného smeru sa odpudzujú':
        'Two parallel wires: they attract when the currents are in the same direction and repel when the currents are opposite',
    'rovnaký smer: priťahujú sa':
        'same direction: attract',
    'opačný smer: odpudzujú sa':
        'opposite directions: repel',
    'Kladne nabitá častica v homogénnom magnetickom poli kolmom na nákresňu sa pohybuje po kružnici; Lorentzova sila smeruje do stredu':
        'A positively charged particle in a uniform magnetic field perpendicular to the page moves in a circle; the Lorentz force points to the centre',
    'B (do nákresne)':
        'B (into the page)',
    'Vodorovná trubica: užšia časť s prierezom 20 cm² a rýchlosťou vody 8 m/s prechádza do širšej časti s prierezom 40 cm²':
        'Horizontal pipe: the narrower part with a cross-section of 20 cm² and water speed 8 m/s widens to a part with a cross-section of 40 cm²',
    'Kalorimeter: vonkajšia a vnútorná nádoba, voda, kúsok ľadu, teplomer a miešačka':
        'Calorimeter: outer and inner vessel, water, a piece of ice, thermometer and stirrer',
    'teplomer':
        'thermometer',
    'ľad':
        'ice',
    'kalorimeter':
        'calorimeter',
    'miešačka':
        'stirrer',
    'Rozvetvený obvod s dvoma zdrojmi a tromi rezistormi; prúdy I1 a I2 vtekajú do horného uzla, prúd I3 z neho vyteká cez stredný rezistor R3':
        'Branched circuit with two sources and three resistors; currents I1 and I2 flow into the upper junction, current I3 flows out of it through the middle resistor R3',
    'Strela sa v hlavni rozbieha z pokoja; na konci hlavne dĺžky l má rýchlosť 150 m/s':
        'The bullet starts from rest in the barrel; at the end of the barrel of length l its speed is 150 m/s',
    'Vľavo prierez ihlou ležiacou na hladine, hladina je prehnutá a sily povrchového napätia držia ihlu; vpravo mydlová blana v drôtenom očku s nitkou, ktorá sa po prepichnutí blany vo vnútri slučky napne do kružnice':
        'Left: cross-section of a needle lying on the water surface, the surface is bent and surface tension forces hold the needle; right: soap film in a wire loop with a thread that pulls into a circle after the film inside the loop is pierced',
    'ihla na hladine (prierez)':
        'needle on the surface (cross-section)',
    'mydlová blana s nitkou':
        'soap film with a thread',
    'otvor':
        'hole',
    'blana':
        'film',
    'nitka':
        'thread',
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
