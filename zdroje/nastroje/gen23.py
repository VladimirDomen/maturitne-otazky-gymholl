"""Vzor 23 z fotky 23 (bez zdrojového HTML – obsah písaný priamo; t₀ strely = 40 °C podľa používateľa)
-> Vzor23_zadanie.html + Vzor23_vypracovanie.html.
Spustenie: python -I gen23.py <priečinok FYZIKA>"""
import sys, pathlib

DST = pathlib.Path(sys.argv[1])
N = 23
TOPICS = ['Mechanika kvapalín – prúdenie', 'Zmena skupenstva – zahriatie strely', 'Šmykové trenie a valivý odpor']

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

def trubica(vyp):
    p2 = 'p₂ = 1,32 · 10⁵ Pa' if vyp else 'p₂ = ?'
    return ('<svg class="diagram" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vodorovná trubica sa rozširuje: v užšej časti voda prúdi rýchlosťou 8 m/s pri tlaku 1,08 · 10⁵ Pa, v širšej časti rýchlosťou 4 m/s">'
            '<path d="M40 80H250L320 60H560V140H320L250 120H40Z" fill="#d6e8f5"/>'
            '<g stroke="#193b59" stroke-width="3" fill="none"><path d="M40 80H250L320 60H560M40 120H250L320 140H560"/></g>'
            '<g stroke="#c0392b" stroke-width="3" fill="none"><path d="M70 100H150M140 93L152 100L140 107M380 100H420M410 93L422 100L410 107"/></g>'
            f'<g {T}><text x="70" y="70">S₁</text><text x="400" y="50">S₂</text></g>'
            '<g font-size="15" fill="#c0392b"><text x="60" y="148">v₁ = 8 m/s</text><text x="370" y="168">v₂ = 4 m/s</text></g>'
            f'<g font-size="15" fill="#193b59"><text x="150" y="148">p₁ = 1,08 · 10⁵ Pa</text><text x="440" y="190">{p2}</text></g></svg>')

TRUBICA_Z = trubica(False)
TRUBICA_V = trubica(True)

def profil():
    sip = lambda x0, y, d: f'M{x0} {y}H{x0 + d}M{x0 + d - 8} {y - 5}L{x0 + d} {y}L{x0 + d - 8} {y + 5}'
    ideal = ''.join(sip(60, y, 90) for y in (62, 82, 102, 122, 142))
    real = ''.join(sip(340, y, d) for y, d in ((62, 34), (82, 74), (102, 92), (122, 74), (142, 34)))
    return ('<svg class="diagram" viewBox="0 0 600 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Rýchlostný profil: pri ideálnej kvapaline majú všetky vrstvy rovnakú rýchlosť, pri reálnej je rýchlosť najväčšia v strede a pri stenách nulová">'
            '<g stroke="#193b59" stroke-width="3"><path d="M40 50H260M40 154H260M320 50H540M320 154H540"/></g>'
            '<rect x="40" y="52" width="220" height="100" fill="#eef5fb"/><rect x="320" y="52" width="220" height="100" fill="#eef5fb"/>'
            f'<g stroke="#2f6db3" stroke-width="2.5" fill="none"><path d="{ideal}"/></g><g stroke="#c0392b" stroke-width="2.5" fill="none"><path d="{real}"/>'
            '<path d="M340 52Q470 102 340 152" stroke-dasharray="4 4" stroke-width="1.5"/></g>'
            '<g font-size="15" fill="#193b59"><text x="70" y="36">ideálna kvapalina</text><text x="356" y="36">reálna kvapalina</text></g>'
            '<g font-size="13" fill="#637889"><text x="64" y="182">rovnaká rýchlosť vo všetkých vrstvách</text><text x="330" y="182">pri stene v = 0, v strede najväčšia</text></g></svg>')

PROFIL = profil()

def ohrev():
    # t (°C) vs pridaná energia na 1 kg: 0–45 kJ/kg
    X = lambda e: 70 + 8.5 * e
    Y = lambda t: 250 - 0.5 * t
    e1 = 125 * 287 / 1000
    pts = f'{X(0)},{Y(40)} {X(e1):.1f},{Y(327)} {X(45):.1f},{Y(327)}'
    return ('<svg class="diagram" viewBox="0 0 520 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graf teploty olova od dodanej energie na kilogram: ohrev zo 40 °C na 327 °C spotrebuje 35,9 kJ/kg, zvyšok do 45 kJ/kg sa spotrebuje na topenie pri stálej teplote">'
            '<g stroke="#e3eaf1" stroke-width="1"><path d="M70 200H480M70 150H480M70 100H480M70 50H480"/></g>'
            '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M70 262V25M60 250H500M64 37L70 25L76 37M488 244L500 250L488 256"/></g>'
            f'<polyline points="{pts}" fill="none" stroke="#c0392b" stroke-width="3"/>'
            f'<g stroke="#637889" stroke-width="1.2" stroke-dasharray="4 4" fill="none"><path d="M70 {Y(327)}H{X(e1):.0f}M{X(e1):.0f} {Y(327)}V250M{X(45):.0f} {Y(327)}V250"/></g>'
            f'<g font-size="14" fill="#253d51"><text x="38" y="{Y(40) + 5}">40</text><text x="30" y="{Y(327) + 5}">327</text><text x="{X(e1) - 16:.0f}" y="270">35,9</text><text x="{X(45) - 6:.0f}" y="270">45</text>'
            '<text x="80" y="22">t (°C)</text><text x="408" y="286">E/m (kJ/kg)</text></g>'
            f'<g font-size="13" fill="#c0392b"><text x="{X(8):.0f}" y="{Y(240):.0f}">ohrev olova</text><text x="{X(e1) + 4:.0f}" y="{Y(327) - 10:.0f}">topenie</text></g></svg>')

OHREV = ohrev()

KVADER = ('<svg class="diagram" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kváder ťahaný silomerom po vodorovnej podložke: ťažná sila F, trecia sila Ft proti pohybu, tiaž G a tlaková sila podložky Fn">'
          '<rect x="20" y="150" width="560" height="22" fill="#d9c9a3" stroke="#9a6b12"/>'
          '<rect x="200" y="90" width="140" height="60" fill="#c9a77c" stroke="#7a5230" stroke-width="2"/>'
          '<rect x="390" y="108" width="110" height="24" rx="5" fill="#fff" stroke="#193b59" stroke-width="2"/><path d="M398 120H470" stroke="#193b59" stroke-width="1.5"/>'
          '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M340 120H390M500 120H540"/></g>'
          '<g stroke="#c0392b" stroke-width="3" fill="none"><path d="M540 120H580M570 113L582 120L570 127"/><path d="M220 150H160M170 143L158 150L170 157"/></g>'
          '<g stroke="#193b59" stroke-width="3" fill="none"><path d="M270 120V205M263 195L270 207L277 195"/></g>'
          '<g stroke="#26724c" stroke-width="3" fill="none"><path d="M300 150V50M293 60L300 48L307 60"/></g>'
          '<g font-size="16"><text x="556" y="104" fill="#c0392b">F</text><text x="150" y="140" fill="#c0392b">Fₜ</text><text x="280" y="214" fill="#193b59">G</text><text x="310" y="58" fill="#26724c">Fₙ</text>'
          '<text x="404" y="100" font-size="13" fill="#637889">silomer</text><text x="40" y="196" font-size="13" fill="#637889">podložka</text></g></svg>')

def graf_t():
    X = lambda f: 70 + 50 * f
    Y = lambda f: 250 - 80 * f
    body = ''.join(f'<circle cx="{X(n):.0f}" cy="{Y(t):.0f}" r="5" fill="#c0392b"/>' for n, t in ((2, 0.6), (4, 1.2), (6, 1.8), (8, 2.4)))
    return ('<svg class="diagram" viewBox="0 0 520 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graf trecej sily od tlakovej sily: priamka cez počiatok so smernicou 0,30">'
            '<g stroke="#e3eaf1" stroke-width="1"><path d="M70 202H480M70 154H480M70 106H480M70 58H480M170 250V40M270 250V40M370 250V40M470 250V40"/></g>'
            '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M70 262V25M60 250H500M64 37L70 25L76 37M488 244L500 250L488 256"/></g>'
            f'<path d="M70 250L{X(8.5):.0f} {Y(2.55):.0f}" stroke="#2f6db3" stroke-width="2.5"/>{body}'
            '<g font-size="14" fill="#253d51"><text x="40" y="207">0,6</text><text x="40" y="159">1,2</text><text x="40" y="111">1,8</text><text x="40" y="63">2,4</text>'
            '<text x="164" y="270">2</text><text x="264" y="270">4</text><text x="364" y="270">6</text><text x="464" y="270">8</text>'
            '<text x="80" y="22">Fₜ (N)</text><text x="440" y="240">Fₙ (N)</text></g>'
            '<text x="300" y="200" font-size="15" fill="#2f6db3">f = Fₜ / Fₙ ≈ 0,30</text></svg>')

GRAF_T = graf_t()

# ---------- zadanie ----------
Z1 = f'''<h2>1. Mechanika kvapalín – prúdenie</h2><div class="task"><ol><li>Vysvetlite rozdiel medzi ustáleným a neustáleným prúdením kvapaliny.</li><li>Sformulujte rovnicu spojitosti toku a Bernoulliho rovnicu a vysvetlite ich fyzikálny význam.</li><li>Aký je rozdiel medzi prúdením ideálnej a reálnej kvapaliny?</li></ol><p><strong>Úloha:</strong> Vodorovnou trubicou prúdi voda. V užšej časti má rýchlosť <strong>v₁ = 8 m/s</strong> a tlak <strong>p₁ = 1,08 · 10⁵ Pa</strong>. V rozšírenej časti prúdi rýchlosťou <strong>v₂ = 4 m/s</strong>. Vodu považujte za ideálnu kvapalinu, ρ = 1 000 kg/m³.</p>{TRUBICA_Z}<ol type="a"><li>Koľkokrát je prierez rozšírenej časti väčší ako prierez užšej časti?</li><li>Aký je tlak vody p₂ v rozšírenej časti?</li></ol></div>'''

Z2 = '''<h2>2. Zmena skupenstva – zahriatie strely</h2><div class="task"><ol><li>Vysvetlite pojmy vnútorná energia, teplo a merná tepelná kapacita.</li><li>Opíšte zmeny skupenstva látky. Čo je teplota topenia a merné skupenské teplo topenia?</li></ol><p><strong>Úloha:</strong> Olovená strela s teplotou <strong>t₀ = 40 °C</strong> narazí rýchlosťou <strong>v = 300 m/s</strong> na oceľovú dosku a zastaví sa. Predpokladajte, že celá jej kinetická energia sa premení na vnútornú energiu strely. Merná tepelná kapacita olova je <strong>c = 125 J·kg⁻¹·K⁻¹</strong>, teplota topenia olova <strong>327 °C</strong>, merné skupenské teplo topenia olova <strong>l<sub>t</sub> = 23 kJ/kg</strong>.</p><ol type="a"><li>Vysvetlite zahriatie strely z energetického hľadiska.</li><li>O koľko by sa strela zohriala, keby sa neroztápala?</li><li>Akou najmenšou rýchlosťou musí strela naraziť, aby sa zohriala na teplotu topenia 327 °C?</li><li>Čo sa stane s energiou, ak je rýchlosť strely väčšia ako vypočítaná? Aká časť strely sa pri rýchlosti 300 m/s roztopí?</li></ol></div>'''

Z3 = '''<h2>3. Experiment – šmykové trenie a valivý odpor</h2><div class="task"><p>Vysvetlite šmykové trenie a valivý odpor. Experimentálne overte, od čoho závisí veľkosť trecej sily pri šmykovom trení:</p><ol type="a"><li>od veľkosti kolmej tlakovej sily,</li><li>od obsahu styčných plôch,</li><li>od druhu a vlastností styčných plôch,</li><li>od rýchlosti telesa voči podložke.</li></ol></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Mechanika kvapalín – prúdenie</h2><h3>1.1 Ustálené a neustálené prúdenie</h3><p>Pri <strong>ustálenom (stacionárnom) prúdení</strong> sa rýchlosť, tlak a hustota kvapaliny v ľubovoľnom mieste nemenia s časom – v danom mieste prechádzajú všetky častice rovnakou rýchlosťou (voda v potrubí pri otvorenom kohútiku). Pri <strong>neustálenom prúdení</strong> sa veličiny v danom mieste s časom menia (otváranie kohútika, vytekanie z nádoby, prúdenie krvi v tepnách).</p><p>Prúdenie znázorňujeme <strong>prúdnicami</strong> – čiarami, ktorých dotyčnica má v každom bode smer rýchlosti častice. Pri ustálenom prúdení sa prúdnice nemenia a nepretínajú. Sústava prúdnic ohraničuje <strong>prúdovú trubicu</strong>.</p><h3>1.2 Rovnica spojitosti toku a Bernoulliho rovnica</h3><p><strong>Rovnica spojitosti toku</strong> (kontinuity) vyjadruje zákon zachovania hmotnosti pre nestlačiteľnú kvapalinu. Každým prierezom trubice pretečie za rovnaký čas rovnaký objem:</p><div class="formula">Q<sub>V</sub> = S₁ v₁ = S₂ v₂ = konšt.</div><p>V užšom mieste prúdi kvapalina rýchlejšie, v širšom pomalšie.</p><p><strong>Bernoulliho rovnica</strong> vyjadruje zákon zachovania mechanickej energie pre ideálnu kvapalinu. Súčet tlakovej, kinetickej a tiažovej potenciálnej energie objemovej jednotky je stály:</p><div class="formula">p + ½ ρ v² + ρ g h = konšt. &nbsp;&nbsp; (vodorovná trubica: p₁ + ½ρv₁² = p₂ + ½ρv₂²)</div><p>Kde kvapalina prúdi rýchlejšie, je v nej menší tlak – <strong>hydrodynamický paradox</strong>. Využitie: Venturiho trubica na meranie rýchlosti prúdenia, vodná vývevka, rozprašovač, karburátor, vztlak krídla.</p><h3>1.3 Ideálna a reálna kvapalina</h3><p><strong>Ideálna kvapalina</strong> je nestlačiteľná a bez vnútorného trenia. Všetky jej vrstvy v trubici prúdia rovnakou rýchlosťou a pri prúdení vodorovnou trubicou stálym prierezom sa tlak nemení.</p><p><strong>Reálna kvapalina</strong> má <strong>viskozitu</strong> (vnútorné trenie). Vrstva pri stene sa nepohybuje a rýchlosť rastie smerom k osi trubice – rýchlostný profil je parabolický. Na prekonanie trenia sa spotrebúva energia, preto tlak pozdĺž trubice stálym prierezom klesá. Pri malých rýchlostiach je prúdenie <strong>laminárne</strong> (vrstvy sa nepremiešavajú), pri veľkých <strong>turbulentné</strong> (vznikajú víry). Na teleso v prúdiacej reálnej tekutine pôsobí odporová sila.</p>{PROFIL}<h3>1.4 Riešenie úlohy</h3>{TRUBICA_V}<p><strong>a)</strong> Z rovnice spojitosti toku:</p><div class="formula">S₁ v₁ = S₂ v₂ &nbsp; → &nbsp; S₂ / S₁ = v₁ / v₂ = 8 / 4 = 2</div><p>Prierez rozšírenej časti je dvojnásobný.</p><p><strong>b)</strong> Z Bernoulliho rovnice pre vodorovnú trubicu:</p><div class="formula">p₂ = p₁ + ½ ρ (v₁² − v₂²) = 1,08 · 10⁵ Pa + ½ · 1 000 · (8² − 4²) Pa<br>p₂ = 1,08 · 10⁵ Pa + 24 000 Pa = 1,32 · 10⁵ Pa</div><p>V širšej časti voda prúdi pomalšie, jej kinetická energia sa čiastočne mení na tlakovú energiu – tlak vzrastie.</p><div class="result"><strong>S₂ = 2S₁; p₂ = 1,32 · 10⁵ Pa.</strong></div>'''

V2 = f'''<h2>2. Zmena skupenstva – zahriatie strely</h2><h3>2.1 Vnútorná energia a teplo</h3><p><strong>Vnútorná energia</strong> telesa je súčet kinetických energií neusporiadaného pohybu jeho častíc a potenciálnych energií ich vzájomného pôsobenia. Mení sa <strong>konaním práce</strong> (trenie, náraz, stláčanie) alebo <strong>tepelnou výmenou</strong>. Energia odovzdaná tepelnou výmenou je <strong>teplo Q</strong>. Teplo potrebné na zmenu teploty telesa:</p><div class="formula">Q = m c Δt</div><p><strong>Merná tepelná kapacita c</strong> je teplo potrebné na zohriatie 1 kg látky o 1 K [J·kg⁻¹·K⁻¹].</p><h3>2.2 Zmeny skupenstva</h3><p>Látka môže prechádzať medzi pevným, kvapalným a plynným skupenstvom: <strong>topenie</strong> a tuhnutie, <strong>vyparovanie</strong> (var) a kondenzácia, <strong>sublimácia</strong> a desublimácia. Kryštalická látka sa topí pri <strong>teplote topenia</strong>, ktorá sa počas topenia nemení. Dodaná energia rozrušuje kryštálovú mriežku – zväčšuje potenciálnu energiu častíc. Teplo potrebné na roztopenie telesa s teplotou topenia:</p><div class="formula">L<sub>t</sub> = m l<sub>t</sub></div><p><strong>Merné skupenské teplo topenia l<sub>t</sub></strong> je teplo potrebné na roztopenie 1 kg látky pri teplote topenia [J·kg⁻¹]. Pri tuhnutí sa rovnaké teplo uvoľní.</p><h3>2.3 Riešenie úlohy</h3><p><strong>a)</strong> Pri náraze sa strela prudko zastaví a deformuje. Jej kinetická energia sa mení – prácou deformačných síl – na <strong>vnútornú energiu</strong> strely (a čiastočne dosky). Častice olova sa začnú pohybovať rýchlejšie a teplota strely vzrastie. Nejde o tepelnú výmenu, ale o zmenu vnútornej energie konaním práce. Hmotnosť strely sa pri výpočte vykráti.</p><p><strong>b)</strong> Ak by sa celá kinetická energia spotrebovala na ohriatie:</p><div class="formula">½ m v² = m c Δt &nbsp; → &nbsp; Δt = v² / (2c) = 300² / (2 · 125) K = 90 000 / 250 K = 360 K</div><p>Strela by mala teplotu 40 °C + 360 °C = 400 °C. To je však viac ako teplota topenia olova (327 °C). Strela sa preto ohreje len na 327 °C a zvyšok energie sa spotrebuje na topenie.</p><p><strong>c)</strong> Najmenšia rýchlosť na zohriatie na teplotu topenia (Δt = 327 °C − 40 °C = 287 K):</p><div class="formula">½ v² = c Δt &nbsp; → &nbsp; v = √(2 c Δt) = √(2 · 125 · 287) m/s = √71 750 m/s ≈ 268 m/s</div><p><strong>d)</strong> Pri väčšej rýchlosti strela dosiahne 327 °C a nadbytočná energia sa spotrebuje na <strong>topenie</strong> – mení sa skupenstvo, teplota zostáva 327 °C. Energia na 1 kg strely:</p><div class="formula">kinetická energia: ½ v² = ½ · 300² J/kg = 45 000 J/kg<br>ohrev na 327 °C: c Δt = 125 · 287 J/kg = 35 875 J/kg<br>zostáva na topenie: 45 000 − 35 875 = 9 125 J/kg</div><div class="formula">roztopená časť: 9 125 / 23 000 ≈ 0,40 = 40 %</div>{OHREV}<p>Na úplné roztopenie strely by bola potrebná rýchlosť v = √(2(cΔt + l<sub>t</sub>)) = √(2 · 58 875) m/s ≈ 343 m/s.</p><div class="result"><strong>b) Δt = 360 K (bez topenia); c) v ≈ 268 m/s; d) strela sa zohreje na 327 °C a asi 40 % olova sa roztopí.</strong></div><p class="subtle">V skutočnosti časť energie prejde do dosky, zvuku a deformácie, preto sa strela zohreje menej. Výpočet dáva hornú hranicu.</p>'''

V3 = f'''<h2>3. Experiment – šmykové trenie a valivý odpor</h2><h3>3.1 Teória</h3><p><strong>Šmykové trenie</strong> vzniká pri posúvaní telesa po povrchu iného telesa. Príčinou sú nerovnosti styčných plôch, ktoré sa do seba zachytávajú, a príťažlivé sily medzi časticami povrchov. Trecia sila pôsobí v styčnej ploche <strong>proti smeru pohybu</strong>:</p><div class="formula">Fₜ = f · Fₙ</div><p>Fₙ je veľkosť kolmej tlakovej sily, ktorou teleso tlačí na podložku (na vodorovnej podložke Fₙ = G). <strong>Súčiniteľ šmykového trenia f</strong> je bezrozmerný a závisí od materiálov a úpravy styčných plôch (drevo po dreve asi 0,3, oceľ po ľade asi 0,02, guma po suchom asfalte asi 0,7). Na uvedenie telesa do pohybu treba prekonať <strong>pokojové (statické) trenie</strong>, ktoré je väčšie ako trenie pri pohybe.</p><p><strong>Valivý odpor</strong> vzniká pri valení telesa (koleso, valec, guľa), lebo sa teleso aj podložka v mieste dotyku deformujú. Odporová sila je</p><div class="formula">F<sub>v</sub> = ξ · Fₙ / R</div><p>ξ je rameno valivého odporu [m] a R polomer valiaceho sa telesa. Valivý odpor je oveľa menší ako šmykové trenie – preto sa používajú kolesá a guľkové ložiská.</p><h3>3.2 Pomôcky</h3><p>Drevený kváder s háčikom, ktorý má steny s rôznym obsahom a jednu stenu potiahnutú gumou alebo plsťou, závažia, silomer (rozsah 0–5 N), rôzne podložky (drevená doska, sklo, látka), niekoľko okrúhlych ceruziek alebo valčekov, váha.</p><h3>3.3 Usporiadanie a postup</h3>{KVADER}<p>Kváder ťaháme silomerom vodorovne <strong>rovnomerným pohybom</strong>. Vtedy je výslednica síl nulová a silomer ukazuje práve veľkosť trecej sily (F = Fₜ). Silu odčítame počas pohybu, nie pri rozbehu.</p><ol type="a"><li><strong>Tlaková sila:</strong> na kváder pridávame závažia a meriame Fₜ pre rôzne Fₙ = G<sub>kvádra</sub> + G<sub>závaží</sub>.</li><li><strong>Obsah styčnej plochy:</strong> kváder s rovnakou záťažou položíme raz na veľkú, raz na malú stenu.</li><li><strong>Druh povrchu:</strong> pri rovnakej Fₙ meníme podložku a stenu kvádra (drevo, guma, sklo).</li><li><strong>Rýchlosť:</strong> kváder ťaháme pomaly a potom rýchlejšie. Zvlášť zmeriame silu potrebnú na rozbeh.</li></ol><p>Na porovnanie s valivým odporom položíme kváder na ceruzky a zmeriame ťažnú silu pri rovnomernom pohybe.</p><h3>3.4 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje pre drevený kváder s tiažou 2,0 N; nejde o skutočné meranie.</p><p><strong>a) Závislosť od tlakovej sily</strong> (drevo po dreve):</p><table><tr><th>Fₙ (N)</th><th>2,0</th><th>4,0</th><th>6,0</th><th>8,0</th></tr><tr><td>Fₜ (N)</td><td>0,6</td><td>1,2</td><td>1,8</td><td>2,4</td></tr><tr><td>f = Fₜ/Fₙ</td><td>0,30</td><td>0,30</td><td>0,30</td><td>0,30</td></tr></table>{GRAF_T}<p>Trecia sila je priamo úmerná tlakovej sile – graf je priamka cez počiatok so smernicou f ≈ 0,30.</p><p><strong>b) Obsah styčnej plochy</strong> (Fₙ = 4,0 N): veľká stena Fₜ = 1,2 N, malá stena Fₜ = 1,2 N – trecia sila od obsahu styčnej plochy nezávisí. Pri menšej ploche je väčší tlak, takže skutočná plocha dotyku nerovností zostáva približne rovnaká.</p><p><strong>c) Druh povrchu</strong> (Fₙ = 4,0 N):</p><table><tr><th>Styčné plochy</th><th>Fₜ (N)</th><th>f</th></tr><tr><td>drevo po dreve</td><td>1,2</td><td>0,30</td></tr><tr><td>drevo po skle</td><td>0,8</td><td>0,20</td></tr><tr><td>guma po dreve</td><td>2,4</td><td>0,60</td></tr></table><p><strong>d) Rýchlosť:</strong> pri pomalom aj rýchlejšom ťahaní ukazuje silomer asi 1,2 N – trecia sila od rýchlosti (pri malých rýchlostiach) takmer nezávisí. Na rozbeh bolo treba asi 1,6 N – pokojové trenie je väčšie.</p><p><strong>Valivý odpor:</strong> kváder na ceruzkách (Fₙ = 4,0 N) sa dal ťahať silou asi 0,1 N, teda asi dvanásťkrát menšou ako pri šmykovom trení.</p><h3>3.5 Nepresnosti</h3><ul><li>Je ťažké ťahať úplne rovnomerne – ručička silomera kolíše, odčítame strednú hodnotu z viacerých meraní.</li><li>Silomer musí byť vodorovný, inak sa mení tlaková sila.</li><li>Povrchy musia byť čisté a suché, prach a vlhkosť menia súčiniteľ trenia.</li></ul><div class="result"><strong>Záver:</strong> Trecia sila pri šmykovom trení je priamo úmerná kolmej tlakovej sile (Fₜ = fFₙ), závisí od druhu a úpravy styčných plôch, nezávisí od ich obsahu a (pri malých rýchlostiach) takmer nezávisí od rýchlosti. Pokojové trenie je väčšie ako trenie pri pohybe a valivý odpor je oveľa menší ako šmykové trenie.</div>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO23', 'Otázka', 'maturit', 'riginál'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
