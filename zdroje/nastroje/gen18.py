"""Vzor 18 (bez zdrojového HTML – obsah písaný priamo) -> Vzor18_zadanie.html + Vzor18_vypracovanie.html.
Spustenie: python -I gen18.py <priečinok FYZIKA>"""
import sys, math, pathlib

DST = pathlib.Path(sys.argv[1])
N = 18
TOPICS = ['Vlastné kmitanie', 'Pohyb v gravitačnom poli – vodorovný vrh', 'Priemer molekuly kyseliny olejovej']

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

PRUZINA = ('<svg class="diagram" viewBox="0 0 420 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Pružinový oscilátor: závažie na pružine kmitá okolo rovnovážnej polohy medzi výchylkami plus A a mínus A">'
           '<path d="M120 20H260" stroke="#193b59" stroke-width="4"/><g stroke="#637889" stroke-width="1.5"><path d="M128 20L118 8M148 20L138 8M168 20L158 8M188 20L178 8M208 20L198 8M228 20L218 8M248 20L238 8"/></g>'
           '<polyline points="190,20 190,40 172,50 208,62 172,74 208,86 172,98 208,110 172,122 190,132 190,140" fill="none" stroke="#193b59" stroke-width="2.5"/>'
           '<rect x="160" y="140" width="60" height="44" rx="4" fill="#9fb3c8" stroke="#375873" stroke-width="2"/><text x="182" y="168" font-size="16" fill="#193b59">m</text>'
           '<g stroke="#637889" stroke-width="1.5" stroke-dasharray="6 5"><path d="M120 162H160M220 162H300M120 92H300M120 232H300"/></g>'
           '<g stroke="#c0392b" stroke-width="2" fill="none"><path d="M320 162V98M314 108L320 96L326 108M320 162V226M314 216L320 228L326 216"/></g>'
           '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M90 270V70M84 82L90 70L96 82"/></g>'
           f'<g {T}><text x="330" y="134">A</text><text x="330" y="200">A</text><text x="100" y="80">y</text>'
           '<text x="124" y="84">+A</text><text x="124" y="252">−A</text><text x="230" y="290" font-size="14" fill="#637889">rovnovážna poloha: y = 0</text></g>'
           '<path d="M240 276L300 166" stroke="#637889" stroke-width="1" fill="none"/></svg>')

# graf y(t): 0–0,3 s -> 1200 px/s od x=70; ±90 mm -> 1 px/mm, stred y=130
def graf_y(vyp):
    X = lambda t: 70 + 1200 * t
    pts = ' '.join(f'{X(i / 1000):.1f},{130 - 90 * math.sin(10 * math.pi * i / 1000):.1f}' for i in range(0, 301, 2))
    grid = ''.join(f'M{X(t / 100):.0f} 30V230' for t in range(5, 31, 5)) + 'M70 85H440M70 175H440M70 40H440M70 220H440'
    extra = ''
    if vyp:
        extra = (f'<g stroke="#c0392b" stroke-width="2" fill="none"><path d="M{X(0.05):.0f} 130V44M{X(0.05) - 6:.0f} 54L{X(0.05):.0f} 42L{X(0.05) + 6:.0f} 54"/>'
                 f'<path d="M{X(0):.0f} 252H{X(0.2):.0f}M{X(0):.0f} 245V259M{X(0.2):.0f} 245V259"/></g>'
                 f'<text x="{X(0.05) + 6:.0f}" y="100" font-size="15" fill="#c0392b">A</text>'
                 f'<text x="{X(0.1) - 40:.0f}" y="272" font-size="15" fill="#c0392b">T = 0,2 s</text>')
    return ('<svg class="diagram" viewBox="0 0 500 ' + ('285' if vyp else '262') + '" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="'
            + ('Graf výchylky od času s vyznačenou amplitúdou 90 mm a periódou 0,2 s' if vyp else
               'Graf výchylky od času: sínusoida s maximom 90 mm, začína v nule a stúpa, prechody nulou v časoch 0,1 s, 0,2 s a 0,3 s')
            + f'"><g stroke="#e3eaf1" stroke-width="1"><path d="{grid}"/></g>'
            '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M70 236V18M60 130H480M64 30L70 18L76 30M468 124L480 130L468 136"/></g>'
            f'<polyline points="{pts}" fill="none" stroke="#2f6db3" stroke-width="3"/>{extra}'
            '<g font-size="14" fill="#253d51"><text x="40" y="45">90</text><text x="34" y="225">−90</text><text x="58" y="148">0</text>'
            f'<text x="{X(0.1) + 4:.0f}" y="124">0,1</text><text x="{X(0.2) - 28:.0f}" y="124">0,2</text><text x="{X(0.3) + 4:.0f}" y="124">0,3</text>'
            '<text x="80" y="18">y (mm)</text><text x="458" y="152">t (s)</text></g></svg>')

GRAF_Y_Z = graf_y(False)
GRAF_Y_V = graf_y(True)

# vodorovný vrh: 2,2 px/m, začiatok (90, 60), zem y = 192
def vrh(vyp):
    P = lambda t: (90 + 2.2 * 60 * t, 60 + 2.2 * 5 * t * t)
    td = math.sqrt(12)
    pts = ' '.join(f'{P(td * i / 60)[0]:.1f},{P(td * i / 60)[1]:.1f}' for i in range(61))
    x2, y2 = P(2)
    xd, yd = P(td)
    base = ('<path d="M20 192H630" stroke="#6b5232" stroke-width="4"/><rect x="40" y="60" width="50" height="132" fill="#c9b79c" stroke="#6b5232" stroke-width="2"/>'
            f'<polyline points="{pts}" fill="none" stroke="#2f6db3" stroke-width="2.5" stroke-dasharray="7 5"/>'
            '<circle cx="90" cy="60" r="7" fill="#c0392b"/>'
            '<g stroke="#c0392b" stroke-width="2.5" fill="none"><path d="M98 60H160M150 54L162 60L150 66"/></g>'
            '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M25 60V192M19 60H31M19 192H31"/></g>'
            '<g font-size="15" fill="#193b59"><text x="104" y="48" fill="#c0392b">v₀ = 60 m/s</text><text x="4" y="134" transform="rotate(-90 14 128)">h = 60 m</text></g>')
    if not vyp:
        return ('<svg class="diagram" viewBox="0 0 640 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Teleso vrhnuté vodorovne rýchlosťou 60 m/s z výšky 60 m; poloha v čase 2 s a miesto dopadu sú neznáme">'
                + base + f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="6" fill="#fff" stroke="#2f6db3" stroke-width="2"/>'
                f'<g font-size="15" fill="#193b59"><text x="{x2 - 10:.0f}" y="{y2 - 14:.0f}">t = 2 s</text><text x="{(90 + xd) / 2 - 20:.0f}" y="220">d = ?</text></g>'
                f'<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M90 205H{xd:.0f}M90 199V211M{xd:.0f} 199V211"/></g></svg>')
    vx, vy = 80, 80 * 20 / 60
    vyd = 80 * 10 * td / 60
    return ('<svg class="diagram" viewBox="0 0 640 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Trajektória vodorovného vrhu v mierke: v čase 2 s je teleso 120 m od okraja a 40 m nad zemou, dopadne 208 m od okraja pod uhlom 30 stupňov">'
            + base + f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="6" fill="#2f6db3"/><circle cx="{xd:.1f}" cy="{yd - 5:.1f}" r="6" fill="#2f6db3"/>'
            f'<g stroke="#637889" stroke-width="1.2" stroke-dasharray="4 4" fill="none"><path d="M{x2:.1f} {y2:.1f}V192M90 {y2:.1f}H{x2:.1f}"/></g>'
            f'<g stroke="#26724c" stroke-width="2.2" fill="none"><path d="M{x2:.1f} {y2:.1f}h{vx}M{x2 + vx - 10:.1f} {y2 - 5:.1f}L{x2 + vx:.1f} {y2:.1f}L{x2 + vx - 10:.1f} {y2 + 5:.1f}"/>'
            f'<path d="M{x2:.1f} {y2:.1f}v{vy:.1f}M{x2 - 5:.1f} {y2 + vy - 10:.1f}L{x2:.1f} {y2 + vy:.1f}L{x2 + 5:.1f} {y2 + vy - 10:.1f}"/></g>'
            f'<path d="M{x2:.1f} {y2:.1f}L{x2 + vx:.1f} {y2 + vy:.1f}" stroke="#c0392b" stroke-width="3"/>'
            f'<path d="M{x2 + vx - 9:.1f} {y2 + vy - 7:.1f}L{x2 + vx:.1f} {y2 + vy:.1f}L{x2 + vx - 11:.1f} {y2 + vy + 2:.1f}" stroke="#c0392b" stroke-width="3" fill="none"/>'
            f'<g font-size="14"><text x="{x2 + vx + 6:.0f}" y="{y2 - 4:.0f}" fill="#26724c">vₓ = 60 m/s</text><text x="{x2 - 76:.0f}" y="{y2 + vy + 4:.0f}" fill="#26724c">vᵧ = 20 m/s</text>'
            f'<text x="{x2 + 4:.0f}" y="{y2 + 50:.0f}" fill="#c0392b">v ≈ 63 m/s</text></g>'
            f'<g font-size="14" fill="#193b59"><text x="{x2 + 6:.0f}" y="{(y2 + 192) / 2 + 30:.0f}">40 m</text><text x="{(90 + x2) / 2 - 24:.0f}" y="{y2 - 6:.0f}">120 m</text>'
            f'<text x="462" y="232">dopad po 3,46 s</text><text x="{(90 + xd) / 2 - 30:.0f}" y="230">d ≈ 208 m</text></g>'
            f'<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M90 212H{xd:.0f}M90 206V218M{xd:.0f} 206V218"/></g></svg>')

VRH_Z = vrh(False)
VRH_V = vrh(True)

def skvrna():
    mol = ''.join(f'<circle cx="{x}" cy="196" r="5" fill="#c0392b"/><path d="M{x} 191V163" stroke="#9a6b12" stroke-width="3"/>' for x in range(380, 601, 14))
    return ('<svg class="diagram" viewBox="0 0 640 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vľavo pohľad zhora na vaničku s vodou posypanou práškom a kruhovou olejovou škvrnou s priemerom D; vpravo rez jednomolekulovou vrstvou hrúbky d na hladine vody">'
            '<rect x="20" y="40" width="300" height="200" rx="8" fill="#d6e8f5" stroke="#375873" stroke-width="2"/>'
            '<g fill="#d9c9a3">' + ''.join(f'<circle cx="{30 + (i * 37) % 280}" cy="{50 + (i * 53) % 180}" r="2.2"/>' for i in range(90)) + '</g>'
            '<circle cx="170" cy="140" r="62" fill="#eef5fb" stroke="#9a6b12" stroke-width="2"/>'
            '<g stroke="#193b59" stroke-width="1.5" fill="none"><path d="M108 140H232M114 134L106 140L114 146M226 134L234 140L226 146"/></g>'
            '<text x="162" y="132" font-size="16" fill="#193b59">D</text><text x="24" y="28" font-size="14" fill="#637889">pohľad zhora</text>'
            '<text x="360" y="28" font-size="14" fill="#637889">rez vrstvou (zväčšené)</text>'
            '<rect x="360" y="196" width="260" height="50" fill="#d6e8f5"/><path d="M360 196H620" stroke="#375873" stroke-width="1.5"/>'
            + mol +
            '<g stroke="#193b59" stroke-width="1.5" fill="none"><path d="M350 163V201M344 163H356M344 201H356"/></g>'
            '<g font-size="15" fill="#193b59"><text x="330" y="188">d</text><text x="500" y="236">voda</text></g>'
            '<g font-size="13" fill="#637889"><text x="460" y="110">molekuly kyseliny olejovej</text><text x="460" y="128">– polárna skupina vo vode</text></g>'
            '<path d="M458 132L430 160" stroke="#637889" stroke-width="1"/></svg>')

SKVRNA = skvrna()

# ---------- zadanie ----------
Z1 = f'''<h2>1. Vlastné kmitanie</h2><div class="task"><ol><li>Popíšte kmitavý pohyb a veličiny, ktoré ho opisujú (perióda, frekvencia, uhlová frekvencia, fáza).</li><li>Vysvetlite pojmy okamžitá výchylka a amplitúda výchylky.</li><li>Napíšte a vysvetlite kinematickú rovnicu harmonického kmitavého pohybu. Čo je vlastné kmitanie oscilátora?</li></ol><p><strong>Úloha:</strong> Graf znázorňuje závislosť výchylky závažia na pružine od času.</p>{GRAF_Y_Z}<ol type="a"><li>Určte amplitúdu výchylky A.</li><li>Určte periódu T a frekvenciu f kmitania.</li><li>Určte počiatočnú fázu φ₀ a napíšte rovnicu výchylky y(t).</li><li><em>Rozširujúca úloha:</em> Vypočítajte amplitúdu rýchlosti v<sub>max</sub> a amplitúdu zrýchlenia a<sub>max</sub>.</li></ol></div>'''

Z2 = f'''<h2>2. Pohyb v gravitačnom poli – vodorovný vrh</h2><div class="task"><ol><li>Opíšte pohyby telies v homogénnom tiažovom poli Zeme (voľný pád, vrhy).</li><li>Vysvetlite vodorovný vrh ako zložený pohyb a uveďte rovnice pre súradnice a rýchlosť.</li></ol><p><strong>Úloha:</strong> Teleso je vrhnuté vodorovne rýchlosťou <strong>v₀ = 60 m/s</strong> z výšky <strong>h = 60 m</strong> nad vodorovným terénom. Odpor vzduchu zanedbajte, g = 10 m/s².</p>{VRH_Z}<ol type="a"><li>Určte polohu telesa v čase t = 2 s.</li><li>Určte veľkosť rýchlosti telesa v čase t = 2 s.</li><li>Za aký čas teleso dopadne na zem?</li><li>V akej vodorovnej vzdialenosti od miesta vrhu dopadne?</li></ol></div>'''

Z3 = '''<h2>3. Experiment – priemer molekuly kyseliny olejovej</h2><div class="task"><p>Pomocou olejovej škvrny na vodnej hladine odhadnite priemer molekuly kyseliny olejovej. Navrhnite pomôcky, postup a vyhodnotenie. Uveďte predpoklady, na ktorých je metóda založená.</p></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Vlastné kmitanie</h2><h3>1.1 Kmitavý pohyb a jeho veličiny</h3><p><strong>Kmitavý pohyb</strong> je periodický pohyb telesa okolo rovnovážnej polohy. Teleso, ktoré kmitá, voláme <strong>oscilátor</strong> – napr. závažie na pružine alebo kyvadlo.</p>{PRUZINA}<ul><li><strong>Perióda T</strong> – čas jedného kmitu [s].</li><li><strong>Frekvencia f</strong> – počet kmitov za sekundu, f = 1/T [Hz].</li><li><strong>Uhlová frekvencia ω</strong> = 2πf = 2π/T [rad·s⁻¹].</li><li><strong>Fáza</strong> φ = ωt + φ₀ [rad] určuje okamžitý stav kmitania. <strong>Počiatočná fáza φ₀</strong> je fáza v čase t = 0.</li></ul><h3>1.2 Okamžitá výchylka a amplitúda</h3><p><strong>Okamžitá výchylka y</strong> je okamžitá vzdialenosť kmitajúceho telesa od rovnovážnej polohy, so znamienkom podľa strany. <strong>Amplitúda výchylky A</strong> je najväčšia hodnota výchylky. Pri netlmenom kmitaní je stála.</p><h3>1.3 Kinematická rovnica</h3><p>Harmonický kmitavý pohyb je priemetom rovnomerného pohybu po kružnici s polomerom A do priemeru kružnice. Odtiaľ:</p><div class="formula">y = A sin(ωt + φ₀)</div><p>Rýchlosť a zrýchlenie:</p><div class="formula">v = ωA cos(ωt + φ₀) &nbsp;&nbsp;&nbsp; a = −ω²A sin(ωt + φ₀) = −ω² y</div><p>Zrýchlenie je úmerné výchylke a smeruje vždy do rovnovážnej polohy. V rovnovážnej polohe je rýchlosť najväčšia a zrýchlenie nulové. V krajných polohách je rýchlosť nulová a zrýchlenie najväčšie.</p><p><strong>Vlastné kmitanie</strong> nastane, keď oscilátor vychýlime a necháme kmitať bez ďalšieho vonkajšieho pôsobenia. Kmitá s <strong>vlastnou frekvenciou</strong>, ktorá závisí len od vlastností oscilátora. Pre pružinový oscilátor:</p><div class="formula">T₀ = 2π √(m/k) &nbsp;&nbsp;&nbsp; f₀ = 1/(2π) · √(k/m)</div><p>Skutočné vlastné kmitanie je vplyvom odporových síl <strong>tlmené</strong> – amplitúda postupne klesá. Ideálne netlmené kmitanie má stálu amplitúdu.</p><h3>1.4 Riešenie úlohy</h3>{GRAF_Y_V}<p><strong>a)</strong> Najväčšia výchylka v grafe je 90 mm:</p><div class="formula">A = 90 mm = 0,09 m</div><p><strong>b)</strong> Graf sa začne opakovať v čase 0,2 s – za tento čas prebehne jeden celý kmit (napr. medzi časmi 0 s a 0,2 s alebo medzi dvoma susednými maximami):</p><div class="formula">T = 0,2 s &nbsp;&nbsp;&nbsp; f = 1/T = 1/0,2 s = 5 Hz &nbsp;&nbsp;&nbsp; ω = 2πf = 10π rad·s⁻¹ ≈ 31,4 rad·s⁻¹</div><p><strong>c)</strong> V čase t = 0 je výchylka nulová a teleso sa pohybuje v kladnom smere (graf stúpa). Platí to pre sin φ₀ = 0 s rastúcim sínusom:</p><div class="formula">φ₀ = 0 &nbsp;&nbsp; → &nbsp;&nbsp; y = 0,09 sin(10π t) m</div><p>Kontrola: v čase t = 0,05 s je y = 0,09 · sin(π/2) m = 0,09 m (maximum), ako v grafe.</p><p><strong>d)</strong> <em>Rozširujúca úloha:</em></p><div class="formula">v<sub>max</sub> = ωA = 10π · 0,09 m/s ≈ 2,83 m/s<br>a<sub>max</sub> = ω²A = (10π)² · 0,09 m/s² ≈ 88,8 m/s²</div><p>Najväčšiu rýchlosť má teleso pri prechode rovnovážnou polohou (t = 0; 0,1 s; 0,2 s …), najväčšie zrýchlenie v krajných polohách (t = 0,05 s; 0,15 s …).</p><div class="result"><strong>A = 90 mm, T = 0,2 s, f = 5 Hz, φ₀ = 0; y = 0,09 sin(10πt) m; v<sub>max</sub> ≈ 2,8 m/s, a<sub>max</sub> ≈ 89 m/s².</strong></div>'''

V2 = f'''<h2>2. Pohyb v gravitačnom poli – vodorovný vrh</h2><h3>2.1 Pohyby v homogénnom tiažovom poli</h3><p>Pri povrchu Zeme považujeme tiažové pole za homogénne: na teleso pôsobí stála tiažová sila mg a teleso má (bez odporu vzduchu) stále tiažové zrýchlenie g ≈ 9,81 m/s² nadol. Druh pohybu závisí od začiatočnej rýchlosti:</p><ul><li><strong>voľný pád</strong> – v₀ = 0, rovnomerne zrýchlený pohyb, s = ½gt², v = gt,</li><li><strong>zvislý vrh nahor</strong> – v₀ smeruje nahor, pohyb najprv spomalený, potom voľný pád,</li><li><strong>vodorovný vrh</strong> – v₀ je vodorovná,</li><li><strong>šikmý vrh</strong> – v₀ zviera s vodorovnou rovinou uhol α, trajektóriou je parabola.</li></ul><h3>2.2 Vodorovný vrh ako zložený pohyb</h3><p>Podľa princípu nezávislosti pohybov skladáme dva pohyby:</p><ul><li>vo vodorovnom smere <strong>rovnomerný pohyb</strong> rýchlosťou v₀ (vo vodorovnom smere nepôsobí žiadna sila),</li><li>vo zvislom smere <strong>voľný pád</strong>.</li></ul><p>Ak je začiatok sústavy súradníc pod miestom vrhu na zemi:</p><div class="formula">x = v₀ t &nbsp;&nbsp;&nbsp; y = h − ½ g t²<br>vₓ = v₀ &nbsp;&nbsp;&nbsp; vᵧ = g t (nadol) &nbsp;&nbsp;&nbsp; v = √(v₀² + g²t²)</div><p>Trajektóriou je časť paraboly. Čas dopadu nezávisí od v₀ – teleso padá rovnako dlho ako pri voľnom páde z rovnakej výšky:</p><div class="formula">t<sub>d</sub> = √(2h/g) &nbsp;&nbsp;&nbsp; d = v₀ t<sub>d</sub> = v₀ √(2h/g)</div><h3>2.3 Riešenie úlohy</h3><p>Zadané: v₀ = 60 m/s, h = 60 m, g = 10 m/s².</p>{VRH_V}<p><strong>a)</strong> Poloha v čase t = 2 s:</p><div class="formula">x = v₀ t = 60 m/s · 2 s = 120 m<br>pokles: ½ g t² = ½ · 10 · 2² m = 20 m &nbsp; → &nbsp; y = 60 m − 20 m = 40 m</div><p>Teleso je 120 m vodorovne od miesta vrhu a 40 m nad zemou.</p><p><strong>b)</strong> Rýchlosť v čase t = 2 s:</p><div class="formula">vₓ = 60 m/s &nbsp;&nbsp;&nbsp; vᵧ = g t = 10 · 2 m/s = 20 m/s<br>v = √(60² + 20²) m/s = √4 000 m/s ≈ 63,2 m/s</div><p>Smer rýchlosti zviera s vodorovnou rovinou uhol β, pre ktorý tg β = vᵧ/vₓ = 20/60, teda β ≈ 18,4° nadol.</p><p><strong>c)</strong> Čas dopadu (y = 0):</p><div class="formula">t<sub>d</sub> = √(2h/g) = √(2 · 60 / 10) s = √12 s ≈ 3,46 s</div><p><strong>d)</strong> Vzdialenosť dopadu:</p><div class="formula">d = v₀ t<sub>d</sub> = 60 m/s · 3,46 s ≈ 208 m</div><p>Pri dopade je vᵧ = g t<sub>d</sub> ≈ 34,6 m/s, rýchlosť v = √(60² + 34,6²) m/s ≈ 69,3 m/s a tg β = 34,6/60 ≈ 0,577, teda teleso dopadá pod uhlom 30°. Rovnakú rýchlosť dá zákon zachovania energie: v = √(v₀² + 2gh) = √(3 600 + 1 200) m/s ≈ 69,3 m/s.</p><div class="result"><strong>t = 2 s: x = 120 m, výška 40 m, v ≈ 63 m/s; dopad za t<sub>d</sub> ≈ 3,5 s vo vzdialenosti d ≈ 208 m.</strong></div><p class="subtle">Pri g = 9,81 m/s² je pokles za 2 s 19,6 m, v ≈ 63,1 m/s, t<sub>d</sub> ≈ 3,50 s a d ≈ 210 m.</p>'''

V3 = f'''<h2>3. Experiment – priemer molekuly kyseliny olejovej</h2><h3>3.1 Princíp</h3><p>Kyselina olejová sa vo vode nerozpúšťa a na vodnej hladine sa rozteká. Jej molekuly majú na jednom konci polárnu skupinu –COOH, ktorá sa viaže k vode, a dlhý nepolárny uhľovodíkový reťazec, ktorý od vody „odstáva“. Malé množstvo kyseliny sa preto rozprestrie do <strong>jednomolekulovej (monomolekulovej) vrstvy</strong>. Jej hrúbka d zodpovedá rozmeru jednej molekuly.</p>{SKVRNA}<p>Ak poznáme objem V kyseliny v kvapke a obsah S škvrny, hrúbku vrstvy určíme z objemu „valca“:</p><div class="formula">V = S · d &nbsp;&nbsp; → &nbsp;&nbsp; d = V/S, &nbsp;&nbsp; S = π D²/4</div><p>Čistá kvapka kyseliny by vytvorila škvrnu s priemerom niekoľko metrov. Preto používame <strong>zriedený roztok</strong> kyseliny olejovej v liehu. Lieh sa rozpustí vo vode a odparí a na hladine zostane len kyselina.</p><h3>3.2 Pomôcky</h3><p>Široká plytká vanička (aspoň 30 cm), voda, jemný prášok na posypanie hladiny (mastenec, lykopódium alebo detský púder), roztok kyseliny olejovej v liehu so známou koncentráciou (napr. 1 : 1 000), kvapkadlo alebo injekčná striekačka, odmerný valček, pravítko, priehľadná fólia so štvorcovou sieťou.</p><h3>3.3 Postup</h3><ol><li><strong>Objem kvapky:</strong> nakvapkáme do odmerného valčeka toľko kvapiek, aby sme odčítali objem (napr. 1 cm³), a kvapky spočítame. Objem jednej kvapky je V<sub>k</sub> = V/n.</li><li>Do čistej vaničky nalejeme vodu, necháme hladinu upokojiť a rovnomerne ju tenko posypeme práškom.</li><li>Z malej výšky kvapneme do stredu jednu kvapku roztoku. Kyselina rozhrnie prášok a vytvorí škvrnu.</li><li>Keď sa škvrna ustáli, zmeriame jej priemer v niekoľkých smeroch a spriemerujeme. Pri nepravidelnom tvare ju obkreslíme na fóliu a obsah určíme spočítaním štvorčekov.</li><li>Pokus zopakujeme s čistou vodou a novým práškom.</li></ol><h3>3.4 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje; nejde o skutočné meranie.</p><p>Do 1 cm³ sa zmestí 50 kvapiek, teda V<sub>k</sub> = 0,02 cm³. Roztok má koncentráciu 1 : 1 000, takže objem kyseliny v jednej kvapke je:</p><div class="formula">V = 0,02 cm³ / 1 000 = 2 · 10⁻⁵ cm³ = 2 · 10⁻¹¹ m³</div><table><tr><th>Meranie</th><th>1</th><th>2</th><th>3</th><th>priemer</th></tr><tr><td>D (cm)</td><td>12,8</td><td>13,4</td><td>13,0</td><td>13,1</td></tr></table><div class="formula">S = π D²/4 = π · (0,131 m)²/4 ≈ 1,34 · 10⁻² m²<br>d = V/S = 2 · 10⁻¹¹ m³ / 1,34 · 10⁻² m² ≈ 1,5 · 10⁻⁹ m = 1,5 nm</div><p>Výsledok ukazuje, že rozmery molekúl sú rádovo <strong>10⁻⁹ m</strong>. Dĺžka molekuly kyseliny olejovej je približne 2 nm. Metóda dáva správny rád, nie presnú hodnotu.</p><h3>3.5 Predpoklady a nepresnosti</h3><ul><li>Vrstva je presne jednomolekulová a súvislá, bez medzier a bez prekrývania molekúl.</li><li>Molekuly stoja kolmo na hladinu – v skutočnosti sú šikmo a d je skôr výška vrstvy ako dĺžka molekuly.</li><li>Najväčšiu nepresnosť spôsobuje určenie objemu kvapky a koncentrácie roztoku a nepravidelný tvar škvrny.</li><li>Nečistoty na hladine (mastnota z prstov) zmenšujú plochu škvrny. Vanička musí byť dôkladne čistá.</li></ul><div class="result"><strong>Záver:</strong> Z d = V/S vychádza hrúbka jednomolekulovej vrstvy d ≈ 1,5 · 10⁻⁹ m – priemer (dĺžka) molekuly kyseliny olejovej je rádovo nanometre.</div>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO18', 'Otázka', 'maturit'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
