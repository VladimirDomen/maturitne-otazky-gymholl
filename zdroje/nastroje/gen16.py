"""Vzor 16 (bez zdrojového HTML – obsah písaný priamo) -> Vzor16_zadanie.html + Vzor16_vypracovanie.html.
Spustenie: python -I gen16.py <priečinok FYZIKA>"""
import sys, pathlib

DST = pathlib.Path(sys.argv[1])
N = 16
TOPICS = ['Elektrický prúd', 'Kinematika – graf v(t)', 'Vlnová dĺžka svetla']

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
OS = '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M70 {y0}V{y1}M60 {ya}H490M64 {y2}L70 {y1}L76 {y2}M478 {yb}L490 {ya}L478 {yc}"/></g>'

def osi(ya, ytop, ybot=None):
    return OS.format(y0=ybot if ybot else ya + 12, y1=ytop, y2=ytop + 12, ya=ya, yb=ya - 6, yc=ya + 6)

OBVOD = ('<svg class="diagram" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Uzavretý obvod: zdroj s elektromotorickým napätím a vnútorným odporom, ampérmeter, vonkajší rezistor R a voltmeter na svorkách zdroja">'
         '<rect x="55" y="40" width="120" height="180" fill="#f3f6f9" stroke="#637889" stroke-width="1.5" stroke-dasharray="6 5"/>'
         '<g stroke="#193b59" stroke-width="3" fill="none"><path d="M100 60V110M100 124V150M100 186V200M100 60H175M100 200H175"/>'
         '<path d="M181 60H316M344 60H480V100M480 160V200H181"/><path d="M240 60V116M240 144V200"/>'
         '<path d="M80 110H120"/><path d="M90 124H110" stroke-width="7"/>'
         '<rect x="88" y="150" width="24" height="36" fill="#fff"/><rect x="468" y="100" width="24" height="60" fill="#fff"/>'
         '<circle cx="330" cy="60" r="14" fill="#fff"/><circle cx="240" cy="130" r="14" fill="#fff"/></g>'
         '<g fill="#fff" stroke="#193b59" stroke-width="2"><circle cx="178" cy="60" r="4"/><circle cx="178" cy="200" r="4"/></g>'
         '<g fill="#193b59"><circle cx="240" cy="60" r="4"/><circle cx="240" cy="200" r="4"/></g>'
         '<path d="M392 48H420M412 42L422 48L412 54" stroke="#c0392b" stroke-width="2.5" fill="none"/>'
         f'<g {T}><text x="324" y="66">A</text><text x="234" y="136">V</text><text x="64" y="114">+</text><text x="66" y="136">−</text>'
         '<text x="126" y="124">Uₑ</text><text x="122" y="174">Rᵢ</text><text x="502" y="136">R</text><text x="262" y="136">U</text>'
         '<text x="186" y="52">+</text><text x="186" y="222">−</text><text x="60" y="32">zdroj</text></g>'
         '<text x="398" y="40" font-size="16" fill="#c0392b">I</text></svg>')

CHARAKTERISTIKA = ('<svg class="diagram" viewBox="0 0 520 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Zaťažovacia charakteristika zdroja: svorkové napätie lineárne klesá od elektromotorického napätia pri nulovom prúde po nulu pri skratovom prúde">'
                   + osi(240, 30) +
                   '<path d="M70 150H250V240" stroke="#637889" stroke-width="1.5" stroke-dasharray="5 4" fill="none"/>'
                   '<path d="M70 60L430 240" stroke="#c0392b" stroke-width="3"/><circle cx="250" cy="150" r="5" fill="#c0392b"/>'
                   '<g font-size="15" fill="#253d51"><text x="80" y="30">U</text><text x="474" y="262">I</text><text x="38" y="65">Uₑ</text>'
                   '<text x="44" y="155">U</text><text x="246" y="262">I</text><text x="422" y="262">Iₖ</text></g>'
                   '<text x="270" y="100" font-size="15" fill="#c0392b">U = Uₑ − Rᵢ I</text>'
                   '<g font-size="14" fill="#637889"><text x="84" y="52">naprázdno</text><text x="440" y="230">skrat</text></g></svg>')

# graf v(t): t 0–16 s -> 25 px/s od x=70, v 0–9 m/s -> 22 px na 1 m/s od y=260
X = lambda t: 70 + 25 * t
V = lambda v: 260 - 22 * v

def graf_v(vyp):
    plochy = ''
    if vyp:
        plochy = (f'<path d="M70 260V{V(4)}H{X(3)}V260Z" fill="#d6e8f5"/>'
                  f'<path d="M{X(3)} 260V{V(4)}L{X(7)} {V(8)}V260Z" fill="#f6dccd"/>'
                  f'<path d="M{X(7)} 260V{V(8)}L{X(15)} 260Z" fill="#dcefe2"/>'
                  f'<g font-size="15" fill="#193b59"><text x="{X(1.5) - 16}" y="225">12 m</text><text x="{X(5) - 16}" y="215">24 m</text>'
                  f'<text x="{X(9.3) - 16}" y="235">32 m</text></g>')
    grid = ''.join(f'M70 {V(v)}H480' for v in (2, 4, 6, 8)) + ''.join(f'M{X(t)} 260V40' for t in range(1, 17))
    return (f'<svg class="diagram" viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="'
            + ('Graf rýchlosti od času s vyznačenými dráhami ako plochami pod grafom: 12 m, 24 m a 32 m' if vyp else
               'Graf rýchlosti od času: od 0 do 3 s rýchlosť 4 m/s, od 3 do 7 s rastie na 8 m/s, od 7 do 15 s klesá na nulu')
            + f'"><g stroke="#e3eaf1" stroke-width="1"><path d="{grid}"/></g>{plochy}' + osi(260, 25)
            + f'<path d="M70 {V(4)}H{X(3)}M70 {V(8)}H{X(7)}M{X(3)} {V(4)}V260M{X(7)} {V(8)}V260" stroke="#637889" stroke-width="1.5" stroke-dasharray="5 4" fill="none"/>'
            f'<polyline points="70,{V(4)} {X(3)},{V(4)} {X(7)},{V(8)} {X(15)},260" fill="none" stroke="#c0392b" stroke-width="3"/>'
            f'<g font-size="14" fill="#253d51"><text x="62" y="278">0</text><text x="{X(3) - 4}" y="278">3</text><text x="{X(7) - 4}" y="278">7</text>'
            f'<text x="{X(15) - 8}" y="278">15</text><text x="50" y="{V(4) + 5}">4</text><text x="50" y="{V(8) + 5}">8</text>'
            '<text x="80" y="24">v (m/s)</text><text x="462" y="282">t (s)</text></g></svg>')

GRAF_V_Z = graf_v(False)
GRAF_V_V = graf_v(True)

def s(t):
    if t <= 3:
        return 4 * t
    if t <= 7:
        return 12 + 4 * (t - 3) + 0.5 * (t - 3) ** 2
    if t <= 15:
        return 36 + 8 * (t - 7) - 0.5 * (t - 7) ** 2
    return 68

def graf_s():
    S = lambda x: 260 - 3 * x
    pts = ' '.join(f'{X(t / 10):.1f},{S(s(t / 10)):.1f}' for t in range(0, 161))
    grid = ''.join(f'M70 {S(x)}H480' for x in (10, 20, 30, 40, 50, 60, 70)) + ''.join(f'M{X(t)} 260V40' for t in range(1, 17))
    yl = ''.join(f'<text x="{40 if x < 100 else 32}" y="{S(x) + 5}">{x}</text>' for x in (12, 36, 68))
    return ('<svg class="diagram" viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graf dráhy od času: priamka do 3 s, potom parabola so stúpajúcou strmosťou do 7 s a parabola s klesajúcou strmosťou do 15 s, kde dráha dosiahne 68 m">'
            f'<g stroke="#e3eaf1" stroke-width="1"><path d="{grid}"/></g>' + osi(260, 25)
            + f'<path d="M70 {S(12)}H{X(3)}V260M70 {S(36)}H{X(7)}V260M70 {S(68)}H{X(15)}V260" stroke="#637889" stroke-width="1.5" stroke-dasharray="5 4" fill="none"/>'
            f'<polyline points="{pts}" fill="none" stroke="#2f6db3" stroke-width="3"/>'
            f'<g font-size="14" fill="#253d51"><text x="62" y="278">0</text><text x="{X(3) - 4}" y="278">3</text><text x="{X(7) - 4}" y="278">7</text>'
            f'<text x="{X(15) - 8}" y="278">15</text>{yl}<text x="80" y="24">s (m)</text><text x="462" y="282">t (s)</text></g></svg>')

GRAF_S = graf_s()

def graf_a():
    A = lambda a: 150 - 50 * a
    return ('<svg class="diagram" viewBox="0 0 520 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graf zrýchlenia od času: 0 do 3 s nulové, od 3 do 7 s 1 m/s², od 7 do 15 s mínus 1 m/s², potom nulové">'
            f'<g stroke="#e3eaf1" stroke-width="1"><path d="M70 {A(1)}H480M70 {A(-1)}H480"/></g>' + osi(150, 25, 225)
            + f'<path d="M{X(3)} 150V{A(1)}M{X(7)} {A(1)}V{A(-1)}M{X(15)} {A(-1)}V150" stroke="#637889" stroke-width="1.5" stroke-dasharray="5 4" fill="none"/>'
            f'<path d="M70 150H{X(3)}M{X(3)} {A(1)}H{X(7)}M{X(7)} {A(-1)}H{X(15)}M{X(15)} 150H{X(16)}" stroke="#26724c" stroke-width="3.5" fill="none"/>'
            f'<g font-size="14" fill="#253d51"><text x="58" y="168">0</text><text x="{X(3) - 4}" y="168">3</text><text x="{X(7) + 4}" y="168">7</text>'
            f'<text x="{X(15) + 4}" y="168">15</text><text x="50" y="{A(1) + 5}">1</text><text x="44" y="{A(-1) + 5}">−1</text>'
            '<text x="80" y="24">a (m/s²)</text><text x="462" y="138">t (s)</text></g></svg>')

GRAF_A = graf_a()

# mriežka: L = 1 m -> 320 px, stred y = 170
MRIEZKA = ('<svg class="diagram" viewBox="0 0 640 345" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Laser, optická mriežka a tienidlo vo vzdialenosti L; na tienidle stredové maximum a maximá 1. a 2. rádu vo vzdialenostiach x1 a x2">'
           '<rect x="30" y="155" width="90" height="30" rx="4" fill="#4f5d73"/><path d="M120 170H200" stroke="#e53935" stroke-width="3"/>'
           '<rect x="197" y="110" width="6" height="120" fill="#9fb3c8" stroke="#375873"/>'
           '<g stroke="#e53935" stroke-width="1.6" opacity=".85"><path d="M200 170L520 170M200 170L520 106M200 170L520 234M200 170L520 35M200 170L520 305"/></g>'
           '<path d="M520 15V325" stroke="#193b59" stroke-width="4"/>'
           '<g fill="#e53935"><circle cx="520" cy="170" r="6"/><circle cx="520" cy="106" r="5"/><circle cx="520" cy="234" r="5"/><circle cx="520" cy="35" r="4"/><circle cx="520" cy="305" r="4"/></g>'
           '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M542 170V106M536 106H548M536 170H548M572 170V35M566 35H578"/><path d="M200 334H520M200 327V341M520 327V341"/>'
           '<path d="M262 170A62 62 0 0 0 260.8 157.6"/></g>'
           f'<g {T}><text x="548" y="143">x₁</text><text x="578" y="108">x₂</text><text x="352" y="325">L</text><text x="270" y="164">α₁</text>'
           '<text x="44" y="146">laser</text><text x="160" y="100">mriežka</text><text x="456" y="12">tienidlo</text></g>'
           '<g font-size="13" fill="#637889"><text x="596" y="40">k = 2</text><text x="596" y="111">k = 1</text><text x="596" y="175">k = 0</text>'
           '<text x="596" y="239">k = 1</text><text x="596" y="309">k = 2</text></g></svg>')

# ---------- zadanie ----------
Z1 = '''<h2>1. Elektrický prúd</h2><div class="task"><ol><li>Opíšte elektrický prúd ako fyzikálny jav. Aké podmienky sú potrebné na jeho vznik? Definujte veličinu elektrický prúd.</li><li>Uveďte zdroje napätia a vysvetlite, akú úlohu má zdroj v elektrickom obvode.</li><li>Vysvetlite pojmy elektromotorické napätie a svorkové napätie a vzťah medzi nimi.</li></ol><p><strong>Úloha:</strong> Prierezom vodiča prejde za čas <strong>t = 2 min</strong> náboj <strong>Q = 30 C</strong>.</p><ol type="a"><li>Aký prúd prechádza vodičom?</li><li>Koľko elektrónov prejde prierezom vodiča za tento čas?</li><li>Prúd odoberáme z batérie s elektromotorickým napätím 4,5 V a vnútorným odporom 1 Ω. Aké je svorkové napätie batérie a aký je odpor vonkajšej časti obvodu?</li></ol></div>'''

Z2 = f'''<h2>2. Kinematika – graf v(t)</h2><div class="task"><ol><li>Charakterizujte rovnomerný a rovnomerne zrýchlený (spomalený) priamočiary pohyb a uveďte vzťahy pre rýchlosť a dráhu.</li><li>Ako sa z grafu závislosti rýchlosti od času určí zrýchlenie a dráha?</li></ol><p><strong>Úloha:</strong> Graf znázorňuje závislosť rýchlosti priamočiaro sa pohybujúceho telesa od času.</p>{GRAF_V_Z}<ol type="a"><li>Určte charakter pohybu v jednotlivých úsekoch a vypočítajte zrýchlenie v každom z nich.</li><li>Určte dráhy, ktoré teleso prešlo v jednotlivých úsekoch, a celkovú dráhu.</li><li>Načrtnite graf závislosti dráhy od času s(t).</li><li>Načrtnite graf závislosti zrýchlenia od času a(t).</li></ol></div>'''

Z3 = '''<h2>3. Experiment – vlnová dĺžka svetla</h2><div class="task"><p>Experimentálne určte vlnovú dĺžku svetla. Zvoľte pomôcky, navrhnite usporiadanie a postup merania a vyhodnoťte výsledky. Vysvetlite fyzikálny jav, na ktorom je meranie založené.</p></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Elektrický prúd</h2><h3>1.1 Elektrický prúd ako jav</h3><p><strong>Elektrický prúd</strong> je usporiadaný (usmernený) pohyb voľných častíc s elektrickým nábojom. Na jeho vznik sú potrebné:</p><ul><li><strong>voľné nosiče náboja</strong> – v kovoch voľné elektróny, v elektrolytoch ióny, v plynoch ióny a elektróny, v polovodičoch elektróny a diery,</li><li><strong>elektrické pole</strong> v látke, teda napätie medzi koncami vodiča – dodáva ho zdroj,</li><li><strong>uzavretý</strong> elektrický obvod (pri trvalom prúde).</li></ul><p>Veličina <strong>elektrický prúd</strong> I udáva náboj, ktorý prejde prierezom vodiča za jednotku času:</p><div class="formula">I = Q/t &nbsp;&nbsp; [I] = A (ampér, základná jednotka SI)</div><p>Dohodnutý smer prúdu je smer pohybu kladných nábojov, teda od kladného pólu zdroja cez vonkajší obvod k zápornému. Elektróny sa v kovoch pohybujú opačne. Ich unášavá rýchlosť je veľmi malá (rádovo zlomky milimetra za sekundu). Elektrické pole sa však v obvode šíri takmer rýchlosťou svetla, preto prúd tečie v celom obvode prakticky okamžite.</p><p>Prúd sa prejavuje účinkami: <strong>tepelným</strong> (varič, žiarovka, poistka), <strong>magnetickým</strong> (elektromagnet, motor), <strong>chemickým</strong> (elektrolýza, nabíjanie akumulátora) a <strong>svetelným</strong> (výbojka, LED). Podľa priebehu rozlišujeme prúd jednosmerný a striedavý.</p><h3>1.2 Zdroje napätia</h3><p>Zdroj premieňa inú formu energie na elektrickú. Neelektrickými (vonkajšími) silami oddeľuje kladné a záporné náboje a udržiava medzi svorkami napätie:</p><ul><li><strong>galvanické články a akumulátory</strong> – chemická energia (batéria, autobatéria, Li-ion článok),</li><li><strong>generátory (alternátory, dynamá)</strong> – mechanická energia cez elektromagnetickú indukciu (elektrárne),</li><li><strong>fotovoltické články</strong> – energia svetla,</li><li><strong>termočlánky</strong> – vnútorná energia (rozdiel teplôt dvoch spojov rôznych kovov),</li><li><strong>piezoelektrické zdroje</strong> – mechanická deformácia kryštálu (zapaľovač).</li></ul><h3>1.3 Elektromotorické a svorkové napätie</h3>{OBVOD}<p><strong>Elektromotorické napätie U<sub>e</sub></strong> je podiel práce W<sub>z</sub>, ktorú vykonajú neelektrické sily zdroja pri prenesení náboja Q vnútri zdroja, a tohto náboja:</p><div class="formula">U<sub>e</sub> = W<sub>z</sub>/Q</div><p>Je to charakteristika zdroja a nezávisí od pripojeného obvodu.</p><p><strong>Svorkové napätie U</strong> je napätie medzi svorkami zdroja, keď zdroj dodáva prúd. Prúd prechádza aj zdrojom, ktorý má <strong>vnútorný odpor R<sub>i</sub></strong>, a na ňom vzniká úbytok napätia R<sub>i</sub>I:</p><div class="formula">U = U<sub>e</sub> − R<sub>i</sub> I &nbsp;&nbsp;&nbsp; I = U<sub>e</sub>/(R + R<sub>i</sub>)</div><p>Druhý vzťah je <strong>Ohmov zákon pre uzavretý obvod</strong>.</p>{CHARAKTERISTIKA}<ul><li><strong>Naprázdno</strong> (I = 0) sa svorkové napätie rovná elektromotorickému: U = U<sub>e</sub>. Približne ho zmeriame voltmetrom s veľkým odporom.</li><li>Čím väčší prúd odoberáme, tým je svorkové napätie menšie.</li><li><strong>Skrat</strong> (R = 0): U = 0 a prúd je najväčší, I<sub>k</sub> = U<sub>e</sub>/R<sub>i</sub>. Pri akumulátoroch je to nebezpečné.</li></ul><h3>1.4 Riešenie úlohy</h3><p>Zadané: t = 2 min = 120 s, Q = 30 C, e = 1,602 · 10⁻¹⁹ C.</p><p><strong>a)</strong> Elektrický prúd:</p><div class="formula">I = Q/t = 30 C / 120 s = 0,25 A</div><p><strong>b)</strong> Náboj je celistvým násobkom elementárneho náboja, Q = N<sub>e</sub> · e:</p><div class="formula">N<sub>e</sub> = Q/e = 30 C / 1,602 · 10⁻¹⁹ C ≈ 1,87 · 10²⁰</div><p><strong>c)</strong> Svorkové napätie a odpor vonkajšej časti obvodu:</p><div class="formula">U = U<sub>e</sub> − R<sub>i</sub> I = 4,5 V − 1 Ω · 0,25 A = 4,25 V<br>R = U/I = 4,25 V / 0,25 A = 17 Ω</div><p>Kontrola Ohmovým zákonom pre uzavretý obvod: I = U<sub>e</sub>/(R + R<sub>i</sub>) = 4,5 V / 18 Ω = 0,25 A.</p><div class="result"><strong>I = 0,25 A; N<sub>e</sub> ≈ 1,9 · 10²⁰ elektrónov; U = 4,25 V, R = 17 Ω.</strong></div>'''

V2 = f'''<h2>2. Kinematika – graf v(t)</h2><h3>2.1 Teória</h3><p><strong>Rovnomerný priamočiary pohyb:</strong> rýchlosť je stála, zrýchlenie nulové:</p><div class="formula">v = konšt. &nbsp;&nbsp; s = v t &nbsp;&nbsp; a = 0</div><p><strong>Rovnomerne zrýchlený (spomalený) priamočiary pohyb:</strong> zrýchlenie je stále, rýchlosť sa mení lineárne s časom:</p><div class="formula">a = Δv/Δt = konšt. &nbsp;&nbsp; v = v₀ + a t &nbsp;&nbsp; s = v₀ t + ½ a t²</div><p>Pri spomalenom pohybe je zrýchlenie opačne orientované ako rýchlosť (a &lt; 0).</p><p><strong>Z grafu v(t):</strong> zrýchlenie je smernica (sklon) grafu a = Δv/Δt. <strong>Dráha</strong> sa rovná obsahu plochy pod grafom (ak sa teleso pohybuje stále jedným smerom). Pri pohybe so stálym zrýchlením je to obsah lichobežníka, teda s = ½ (v₁ + v₂) Δt.</p><h3>2.2 Charakter pohybu a zrýchlenia</h3><table><tr><th>Úsek</th><th>Čas</th><th>Rýchlosť</th><th>Pohyb</th><th>Zrýchlenie</th></tr><tr><td>I</td><td>0 – 3 s</td><td>4 m/s stále</td><td>rovnomerný</td><td>a₁ = 0</td></tr><tr><td>II</td><td>3 – 7 s</td><td>4 → 8 m/s</td><td>rovnomerne zrýchlený</td><td>a₂ = (8 − 4)/(7 − 3) = 1 m/s²</td></tr><tr><td>III</td><td>7 – 15 s</td><td>8 → 0 m/s</td><td>rovnomerne spomalený</td><td>a₃ = (0 − 8)/(15 − 7) = −1 m/s²</td></tr></table><p>V čase 15 s sa teleso zastaví.</p><h3>2.3 Dráhy</h3>{GRAF_V_V}<p>Dráhy určíme ako obsahy plôch pod grafom:</p><div class="formula">s₁ = v t₁ = 4 m/s · 3 s = 12 m (obdĺžnik)<br>s₂ = ½ (4 + 8) m/s · 4 s = 24 m (lichobežník)<br>s₃ = ½ · 8 m/s · 8 s = 32 m (trojuholník)</div><p>Rovnaký výsledok dajú vzťahy pre zrýchlený pohyb, napr. s₂ = v₀t + ½at² = 4 · 4 + ½ · 1 · 4² = 24 m a s₃ = 8 · 8 − ½ · 1 · 8² = 32 m.</p><div class="formula">s = s₁ + s₂ + s₃ = 12 m + 24 m + 32 m = 68 m</div><p>Priemerná rýchlosť na celej dráhe: v<sub>p</sub> = s/t = 68 m / 15 s ≈ 4,5 m/s.</p><h3>2.4 Graf s(t)</h3>{GRAF_S}<ul><li><strong>0 – 3 s:</strong> s = 4t, priamka. V čase 3 s je s = 12 m.</li><li><strong>3 – 7 s:</strong> s = 12 + 4(t − 3) + ½(t − 3)², parabola, graf je čoraz strmší. V čase 7 s je s = 36 m.</li><li><strong>7 – 15 s:</strong> s = 36 + 8(t − 7) − ½(t − 7)², parabola, graf je čoraz menej strmý. V čase 15 s je s = 68 m a dotyčnica je vodorovná (v = 0).</li></ul><p>Graf je spojitý a nemá zlomy: smernica s(t) je rýchlosť a tá sa nemení skokom.</p><h3>2.5 Graf a(t)</h3>{GRAF_A}<p>Zrýchlenie je v každom úseku stále, preto graf a(t) tvoria vodorovné úsečky: 0, potom 1 m/s² a potom −1 m/s². Po zastavení je zrýchlenie opäť nulové. V časoch 3 s, 7 s a 15 s sa zrýchlenie mení skokom (idealizácia).</p><div class="result"><strong>a₁ = 0, a₂ = 1 m/s², a₃ = −1 m/s²; s₁ = 12 m, s₂ = 24 m, s₃ = 32 m, spolu s = 68 m.</strong></div>'''

V3 = f'''<h2>3. Experiment – vlnová dĺžka svetla</h2><h3>3.1 Princíp – ohyb svetla na optickej mriežke</h3><p>Svetlo je elektromagnetické vlnenie. Viditeľné svetlo má vlnovú dĺžku približne 380–760 nm, čo je príliš málo na priame meranie. Využijeme <strong>ohyb (difrakciu) a interferenciu</strong> svetla na optickej mriežke.</p><p><strong>Optická mriežka</strong> je sústava veľkého počtu rovnobežných štrbín v rovnakých vzdialenostiach. Vzdialenosť susedných štrbín je <strong>mriežková konštanta d</strong>. Ak má mriežka N vrypov na 1 mm, platí d = 1 mm / N.</p><p>Svetlo sa za každou štrbinou ohýba. Vlnenia z jednotlivých štrbín sa skladajú a v smeroch, v ktorých je dráhový rozdiel susedných lúčov celistvým násobkom vlnovej dĺžky, vznikajú svetlé <strong>maximá</strong>:</p><div class="formula">d · sin α<sub>k</sub> = k · λ &nbsp;&nbsp;&nbsp; k = 0, 1, 2, …</div><p>k je rád maxima a α<sub>k</sub> uhol, pod ktorým maximum vidíme. Ak je tienidlo vo vzdialenosti L a maximum k-teho rádu je vo vzdialenosti x<sub>k</sub> od stredového maxima, potom:</p><div class="formula">tg α<sub>k</sub> = x<sub>k</sub>/L &nbsp;&nbsp; → &nbsp;&nbsp; λ = d · sin α<sub>k</sub> / k</div><p>Pre malé uhly je sin α ≈ tg α, takže λ ≈ d x<sub>k</sub>/(k L).</p><h3>3.2 Pomôcky</h3><p>Laserové ukazovátko (napr. červené), optická mriežka so známym počtom vrypov (napr. 300 vrypov na mm), stojany na upevnenie, tienidlo (stena s papierom), zvinovací meter alebo dlhé pravítko, ceruzka. Ako náhrada mriežky môže poslúžiť CD (rozostup stôp 1,6 μm) v odraze.</p><h3>3.3 Usporiadanie</h3>{MRIEZKA}<p>Laserový lúč dopadá kolmo na mriežku a tienidlo je rovnobežné s mriežkou. Na tienidle vidíme rad svetlých bodov: stredové maximum (k = 0) a symetricky po stranách maximá 1., 2., … rádu.</p><h3>3.4 Postup</h3><ol><li>Upevníme laser a mriežku tak, aby lúč dopadal na mriežku kolmo. Tienidlo umiestnime do vzdialenosti L (napr. 1 m) a vzdialenosť zmeriame.</li><li>Na papieri vyznačíme polohy maxím. Zmeriame vzdialenosť <strong>2x<sub>k</sub></strong> medzi symetrickými maximami toho istého rádu – je to presnejšie, ako hľadať stred.</li><li>Meranie zopakujeme pre maximá 2. rádu a pre inú vzdialenosť L.</li><li>Pre každé meranie vypočítame tg α<sub>k</sub> = x<sub>k</sub>/L, uhol α<sub>k</sub>, sin α<sub>k</sub> a λ = d sin α<sub>k</sub>/k. Výsledky spriemerujeme.</li></ol><h3>3.5 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje pre mriežku s 300 vrypmi na mm, d = 1/300 mm ≈ 3,333 μm; nejde o skutočné meranie.</p><table><tr><th>L (m)</th><th>k</th><th>2x<sub>k</sub> (cm)</th><th>tg α<sub>k</sub></th><th>α<sub>k</sub></th><th>sin α<sub>k</sub></th><th>λ (nm)</th></tr><tr><td>1,00</td><td>1</td><td>39,8</td><td>0,199</td><td>11,25°</td><td>0,1952</td><td>651</td></tr><tr><td>1,00</td><td>2</td><td>84,6</td><td>0,423</td><td>22,93°</td><td>0,3896</td><td>649</td></tr><tr><td>0,50</td><td>1</td><td>19,8</td><td>0,198</td><td>11,20°</td><td>0,1942</td><td>647</td></tr></table><p>Napríklad pre prvý riadok:</p><div class="formula">x₁ = 39,8 cm / 2 = 0,199 m &nbsp; → &nbsp; tg α₁ = 0,199 / 1,00 &nbsp; → &nbsp; α₁ ≈ 11,25°<br>λ = d sin α₁ / 1 = 3,333 · 10⁻⁶ m · 0,1952 ≈ 6,51 · 10⁻⁷ m = 651 nm</div><p>Priemer: λ ≈ 649 nm. Výrobca udáva pre červený laser 650 nm – výsledok dobre súhlasí.</p><p>Pri maximách 2. rádu je uhol väčší a už neplatí sin α ≈ tg α (0,390 oproti 0,423). Preto treba počítať cez uhol, nie len zo vzťahu λ ≈ dx/(kL).</p><h3>3.6 Nepresnosti a bezpečnosť</h3><p><strong>Do laserového lúča sa nikdy nepozeráme</strong> a nemierime ním na ľudí. Používame laser triedy 2 (do 1 mW) a pozor dávame aj na odrazy od lesklých plôch. Nepresnosť spôsobuje meranie polohy maxím (sú to škvrny s istou šírkou), meranie L a neskolmý dopad lúča. Presnosť zvýšime väčšou vzdialenosťou L a meraním vyšších rádov.</p><p>Ak namiesto lasera použijeme <strong>biele svetlo</strong>, každé maximum (okrem stredového) sa rozloží na spektrum. Fialová je najbližšie k stredu a červená najďalej, lebo väčšej vlnovej dĺžke zodpovedá väčší uhol. Na tomto princípe pracujú mriežkové spektroskopy.</p><div class="result"><strong>Záver:</strong> Vlnovú dĺžku určíme z d sin α<sub>k</sub> = kλ, kde tg α<sub>k</sub> = x<sub>k</sub>/L. Pre červený laser vychádza λ ≈ 650 nm.</div>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO16', 'Otázka', 'maturit'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
