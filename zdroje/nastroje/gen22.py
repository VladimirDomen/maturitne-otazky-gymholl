"""Vzor 22 podľa fotky 22 a MO22 (text písaný priamo). Oproti MO22: v časti 1 vynechané prečiarknuté body
(výroba energie, transformátor, elektrárne – sú vo Vzore 21), v časti 2 doplnený prípad ľadu pri 0 °C,
v časti 3 len výslednica dvoch síl (Youngov pokus na fotke nie je).
-> Vzor22_zadanie.html + Vzor22_vypracovanie.html.  Spustenie: python -I gen22.py <priečinok FYZIKA>"""
import sys, pathlib, math

DST = pathlib.Path(sys.argv[1])
N = 22
TOPICS = ['Striedavý prúd', 'Kalorimetrická rovnica', 'Výslednica dvoch síl']

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
def graf_ui():
    """u(t) a i(t) na ideálnej cievke: prúd zaostáva za napätím o T/4. Perióda T = 320 px, začiatok x = 60."""
    X = lambda t: 60 + 320 * t
    def krivka(amp, faza):
        return ' '.join(f'{X(k / 100):.1f},{120 - amp * math.sin(2 * math.pi * k / 100 - faza):.1f}' for k in range(0, 141))
    return ('<svg class="diagram" viewBox="0 0 560 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Časový priebeh napätia a prúdu na ideálnej cievke, prúd zaostáva o štvrtinu periódy">'
            '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M60 215V25M50 120H530M54 37L60 25L66 37M518 114L530 120L518 126"/></g>'
            '<g stroke="#e3eaf1"><path d="M220 30V210M380 30V210"/></g>'
            f'<polyline points="{krivka(80, 0)}" fill="none" stroke="#c0392b" stroke-width="3"/>'
            f'<polyline points="{krivka(50, math.pi / 2)}" fill="none" stroke="#2f6db3" stroke-width="3"/>'
            '<g stroke="#637889" stroke-width="1.5" fill="none" stroke-dasharray="4 4"><path d="M140 40V120M220 70V120"/></g>'
            '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M140 34H220M146 29L140 34L146 39M214 29L220 34L214 39"/></g>'
            '<g font-size="15"><text x="168" y="27" fill="#637889">T/4</text><text x="96" y="52" fill="#c0392b">u</text><text x="244" y="58" fill="#2f6db3">i</text>'
            '<text x="520" y="142" fill="#193b59">t</text><text x="214" y="140" fill="#637889">T/2</text><text x="374" y="140" fill="#637889">T</text></g></svg>')

def rovnobeznik():
    """F1 = 3 N vodorovne, F2 = 4 N pod uhlom 60°, mierka 50 px/N; F ≈ 6,08 N."""
    def sipka(x1, y1, x2, y2, farba, w=3):
        d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
        a = (x2 - 13 * ux + 6 * uy, y2 - 13 * uy - 6 * ux); b = (x2 - 13 * ux - 6 * uy, y2 - 13 * uy + 6 * ux)
        return (f'<path d="M{x1} {y1}L{x2 - 8 * ux:.1f} {y2 - 8 * uy:.1f}" stroke="{farba}" stroke-width="{w}"/>'
                f'<path d="M{x2} {y2}L{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}Z" fill="{farba}"/>')
    return ('<svg class="diagram" viewBox="0 0 440 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Skladanie dvoch síl pomocou rovnobežníka síl">'
            '<path d="M230 220L330 46.8L180 46.8" fill="none" stroke="#8297a6" stroke-width="2" stroke-dasharray="6 5"/>'
            + sipka(80, 220, 230, 220, '#2f6db3') + sipka(80, 220, 180, 46.8, '#2f6db3') + sipka(80, 220, 330, 46.8, '#c0392b', 3.5) +
            '<path d="M115 220A35 35 0 0 0 97.5 189.7" fill="none" stroke="#637889" stroke-width="1.5"/><circle cx="80" cy="220" r="4" fill="#193b59"/>'
            '<g font-size="16" fill="#193b59"><text x="148" y="246">F₁ = 3 N</text><text x="70" y="124">F₂ = 4 N</text><text x="120" y="208">α = 60°</text></g>'
            '<text x="336" y="104" font-size="16" fill="#c0392b">F ≈ 6,1 N</text></svg>')

GRAF = graf_ui()
ROVN = rovnobeznik()

# ---------- zadanie ----------
Z1 = '''<h2>1. Striedavý prúd</h2><div class="task"><ol><li>Opíšte vznik striedavého napätia. Vyjadrite okamžitú hodnotu striedavého napätia a prúdu ako funkciu času a nakreslite ich grafy.</li><li>Vysvetlite správanie rezistora, cievky a kondenzátora v obvode striedavého prúdu – ich vplyv na amplitúdu prúdu a na fázový posun medzi prúdom a napätím.</li></ol><p><strong>Úloha:</strong> Cievka so zanedbateľným odporom je pripojená na striedavé napätie <strong>230&nbsp;V</strong> s frekvenciou <strong>50&nbsp;Hz</strong>. Prechádza ňou prúd <strong>0,5&nbsp;A</strong>. Aká je indukčnosť cievky?</p></div>'''

Z2 = '''<h2>2. Molekulová fyzika a termodynamika – kalorimetrická rovnica</h2><div class="task"><ol><li>Vysvetlite vnútornú energiu, teplo a tepelnú kapacitu. Opíšte teplo potrebné na ohriatie látky a skupenské teplo topenia.</li><li>Napíšte kalorimetrickú rovnicu a vysvetlite, kedy platí.</li></ol><p><strong>Úloha:</strong> V kalorimetri s tepelnou kapacitou <strong>C = 90&nbsp;J/K</strong> je voda s hmotnosťou <strong>200&nbsp;g</strong> a teplotou <strong>80&nbsp;°C</strong>. Do vody vložíme ľad s hmotnosťou <strong>150&nbsp;g</strong>. Merné skupenské teplo topenia ľadu je 334&nbsp;kJ/kg, merná tepelná kapacita ľadu 2,1&nbsp;kJ/(kg·K) a vody 4,18&nbsp;kJ/(kg·K). Tepelné straty do okolia zanedbajte.</p><ol type="a"><li>Napíšte kalorimetrickú rovnicu a určte výslednú teplotu sústavy po dosiahnutí rovnovážneho stavu, ak mal ľad teplotu 0&nbsp;°C.</li><li>Určte výslednú teplotu sústavy, ak mal ľad teplotu −15&nbsp;°C.</li></ol></div>'''

Z3 = '''<h2>3. Experiment – výslednica dvoch síl</h2><div class="task"><p>Experimentálne určte výslednicu dvoch síl pôsobiacich v jednom bode pod rôznymi uhlami. Výsledok porovnajte s grafickým riešením pomocou rovnobežníka síl a s výpočtom.</p></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Striedavý prúd</h2><h3>1.1 Vznik striedavého napätia</h3><p>Závit (cievka s N závitmi) s plochou S sa rovnomerne otáča uhlovou rýchlosťou ω v homogénnom magnetickom poli s indukciou B. Magnetický indukčný tok závitom sa periodicky mení:</p><div class="formula">Φ = BS cos ωt</div><p>Podľa Faradayovho zákona elektromagnetickej indukcie sa v cievke indukuje napätie u = −N·dΦ/dt:</p><div class="formula">u = U<sub>m</sub> sin ωt, &nbsp;&nbsp; U<sub>m</sub> = NBSω, &nbsp;&nbsp; ω = 2πf = 2π/T</div><p>Na tomto princípe pracuje alternátor. V sieti je f = 50 Hz.</p><h3>1.2 Okamžitá a efektívna hodnota</h3><p>Okamžité hodnoty napätia a prúdu sú harmonické funkcie času:</p><div class="formula">u = U<sub>m</sub> sin ωt &nbsp;&nbsp;&nbsp; i = I<sub>m</sub> sin(ωt + φ)</div><p>U<sub>m</sub>, I<sub>m</sub> sú amplitúdy a φ je fázový posun prúdu voči napätiu. Grafom je sínusoida s periódou T. Efektívna hodnota je hodnota jednosmerného prúdu, ktorý by v rezistore vyvinul rovnaké teplo:</p><div class="formula">U = U<sub>m</sub>/√2 &nbsp;&nbsp;&nbsp; I = I<sub>m</sub>/√2</div><p>Sieťové napätie 230 V je efektívna hodnota; amplitúda je asi 325 V.</p><h3>1.3 R, L a C v obvode striedavého prúdu</h3><table><tr><th>Prvok</th><th>Odpor prvku</th><th>Fázový posun</th></tr><tr><td>rezistor</td><td>R (nezávisí od f)</td><td>prúd a napätie sú vo fáze, φ = 0</td></tr><tr><td>ideálna cievka</td><td>induktancia X<sub>L</sub> = ωL</td><td>prúd zaostáva za napätím o π/2 (T/4)</td></tr><tr><td>ideálny kondenzátor</td><td>kapacitancia X<sub>C</sub> = 1/(ωC)</td><td>prúd predbieha napätie o π/2 (T/4)</td></tr></table><p><strong>Vplyv na amplitúdu:</strong> pre každý prvok platí I<sub>m</sub> = U<sub>m</sub>/X. Cievka kladie väčší odpor pri vyššej frekvencii – indukované napätie pôsobí proti zmene prúdu. Kondenzátor naopak lepšie „prepúšťa“ vyššie frekvencie a jednosmerný prúd ním trvalo neprechádza.</p><p><strong>Vplyv na fázu:</strong> na cievke je napätie najväčšie vtedy, keď sa prúd mení najrýchlejšie – teda pri nulovom prúde. Preto prúd zaostáva o štvrtinu periódy:</p>{GRAF}<p>Pri sériovom spojení R, L a C je impedancia Z = √(R² + (X<sub>L</sub> − X<sub>C</sub>)²).</p><h3>1.4 Riešenie úlohy</h3><p>Cievka má zanedbateľný odpor, preto prúd obmedzuje len induktancia. Napätie a prúd sú efektívne hodnoty:</p><div class="formula">X<sub>L</sub> = U/I = 230 V / 0,5 A = 460 Ω</div><div class="formula">L = X<sub>L</sub>/(2πf) = 460 Ω / (2π · 50 Hz) ≈ 1,46 H</div><div class="result"><strong>Indukčnosť cievky je približne 1,46 H.</strong></div><p class="subtle">Skutočná cievka má aj odpor vinutia R. Potom U/I = Z = √(R² + X<sub>L</sub>²) a indukčnosť by vyšla o niečo menšia.</p>'''

V2 = '''<h2>2. Molekulová fyzika a termodynamika – kalorimetrická rovnica</h2><h3>2.1 Vnútorná energia a teplo</h3><p><strong>Vnútorná energia</strong> telesa je súčet kinetických energií neusporiadaného pohybu jeho častíc a potenciálnych energií ich vzájomného pôsobenia. <strong>Teplo</strong> Q je vnútorná energia, ktorú teleso odovzdá alebo prijme pri tepelnej výmene – bez konania práce, len vďaka rozdielu teplôt.</p><p>Na zmenu teploty telesa o Δt treba teplo:</p><div class="formula">Q = mcΔt = CΔt</div><p>c je merná tepelná kapacita látky [J/(kg·K)], C = mc tepelná kapacita telesa [J/K].</p><p>Pri topení sa teplota nemení, kým sa neroztopí celé teleso. Dodané teplo zväčšuje potenciálnu energiu častíc (rozrušuje kryštálovú mriežku):</p><div class="formula">L<sub>t</sub> = m · l<sub>t</sub></div><h3>2.2 Kalorimetrická rovnica</h3><p>V tepelne izolovanej sústave sa teplo odovzdané teplejšími telesami rovná teplu prijatému chladnejšími telesami, kým sa teploty nevyrovnajú:</p><div class="formula">Q<sub>odovzdané</sub> = Q<sub>prijaté</sub></div><p>Je to zákon zachovania energie pre tepelnú výmenu. Platí, ak zanedbáme výmenu tepla s okolím a sústava nekoná prácu.</p><h3>2.3 Riešenie úlohy</h3><p>m<sub>v</sub> = 0,200 kg, t<sub>v</sub> = 80 °C, m<sub>ľ</sub> = 0,150 kg, C = 90 J/K, c<sub>v</sub> = 4 180 J/(kg·K), c<sub>ľ</sub> = 2 100 J/(kg·K), l<sub>t</sub> = 334 000 J/kg. Kalorimeter mal na začiatku teplotu vody.</p><p><strong>Najprv overíme, či sa roztopí všetok ľad.</strong> Teplá voda s kalorimetrom môže pri ochladení na 0 °C odovzdať:</p><div class="formula">(m<sub>v</sub>c<sub>v</sub> + C) · 80 K = (836 + 90) J/K · 80 K = 74 080 J</div><p>Roztopenie ľadu pri 0 °C potrebuje m<sub>ľ</sub>l<sub>t</sub> = 50 100 J. Pri ľade s teplotou −15 °C treba ešte m<sub>ľ</sub>c<sub>ľ</sub> · 15 K = 4 725 J, spolu 54 825 J. V oboch prípadoch je to menej ako 74 080 J, preto sa všetok ľad roztopí a výsledná teplota t je nad 0 °C.</p><p><strong>a) Ľad pri 0 °C.</strong> Voda a kalorimeter sa ochladia z 80 °C na t. Ľad sa roztopí a vzniknutá voda sa ohreje z 0 °C na t:</p><div class="formula">(m<sub>v</sub>c<sub>v</sub> + C)(80 − t) = m<sub>ľ</sub>l<sub>t</sub> + m<sub>ľ</sub>c<sub>v</sub>(t − 0)</div><div class="formula">926(80 − t) = 50 100 + 627t<br>74 080 − 50 100 = 1 553t &nbsp; → &nbsp; t = 23 980/1 553 ≈ 15,4 °C</div><p><strong>b) Ľad pri −15 °C.</strong> Ľad sa najprv musí ohriať na 0 °C:</p><div class="formula">(m<sub>v</sub>c<sub>v</sub> + C)(80 − t) = m<sub>ľ</sub>c<sub>ľ</sub> · 15 + m<sub>ľ</sub>l<sub>t</sub> + m<sub>ľ</sub>c<sub>v</sub>t</div><div class="formula">926(80 − t) = 4 725 + 50 100 + 627t<br>74 080 − 54 825 = 1 553t &nbsp; → &nbsp; t = 19 255/1 553 ≈ 12,4 °C</div><div class="result"><strong>a) t ≈ 15,4 °C; b) t ≈ 12,4 °C.</strong> V oboch prípadoch sa všetok ľad roztopí a v kalorimetri je 350 g vody.</div><p>Studenší ľad potrebuje navyše 4 725 J na ohriatie na 0 °C, preto je výsledná teplota nižšia. Najviac tepla spotrebuje samotné topenie – asi 80 až 85 % tepla, ktoré ľad prijme.</p><p class="subtle">Tepelná kapacita kalorimetra patrí na stranu telies, ktoré teplo odovzdávajú, lebo kalorimeter mal na začiatku teplotu 80 °C.</p>'''

V3 = f'''<h2>3. Experiment – výslednica dvoch síl</h2><h3>3.1 Teória</h3><p>Sila je vektor. Výslednica dvoch síl pôsobiacich v jednom bode je ich vektorový súčet. Graficky je to uhlopriečka <strong>rovnobežníka síl</strong> zostrojeného zo síl F₁ a F₂. Ak zvierajú sily uhol α, veľkosť výslednice je:</p><div class="formula">F = √(F₁² + F₂² + 2F₁F₂ cos α)</div><p>Výslednica je najväčšia pri α = 0° (F = F₁ + F₂) a najmenšia pri α = 180° (F = |F₁ − F₂|). Pri α = 90° platí Pytagorova veta.</p>{ROVN}<h3>3.2 Pomôcky</h3><p>Tri silomery, malý krúžok, nite, tabuľa alebo doska s papierom, uhlomer, pravítko.</p><h3>3.3 Postup</h3><ol><li>Krúžok pripevníme niťami k trom silomerom ležiacim na papieri. Silomery napneme v rôznych smeroch, kým krúžok nie je v pokoji.</li><li>Krúžok je v rovnováhe, preto tretia sila F₃ má rovnakú veľkosť ako výslednica síl F₁ a F₂, ale opačný smer. F₃ je <strong>vyrovnávacia sila</strong>.</li><li>Na papier zaznačíme smery nití a odčítame veľkosti F₁, F₂ a F₃. Uhlomerom zmeriame uhol α medzi F₁ a F₂.</li><li>V zvolenej mierke (napr. 1 N = 2 cm) zostrojíme rovnobežník síl a odmeriame dĺžku uhlopriečky.</li><li>Výslednicu vypočítame aj zo vzťahu pre F a porovnáme všetky tri hodnoty. Meranie zopakujeme pre iné uhly.</li></ol><h3>3.4 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje pre F₁ = 3,0 N a F₂ = 4,0 N; nejde o skutočné meranie.</p><table><tr><th>α</th><th>F vypočítaná (N)</th><th>F₃ nameraná (N)</th></tr><tr><td>0°</td><td>7,00</td><td>6,9</td></tr><tr><td>60°</td><td>6,08</td><td>6,0</td></tr><tr><td>90°</td><td>5,00</td><td>5,1</td></tr><tr><td>120°</td><td>3,61</td><td>3,6</td></tr></table><p>Napríklad pre α = 60°:</p><div class="formula">F = √(3² + 4² + 2 · 3 · 4 · cos 60°) N = √37 N ≈ 6,08 N</div><p>Smer výslednice určuje uhol β, ktorý zviera so silou F₁: tg β = F₂ sin α/(F₁ + F₂ cos α). Pre α = 60° je β ≈ 34,7°.</p><div class="result"><strong>Záver:</strong> Nameraná vyrovnávacia sila sa v rámci presnosti silomerov zhoduje s výslednicou určenou graficky aj výpočtom. Sily sa skladajú ako vektory, nie ako čísla – s rastúcim uhlom α výslednica klesá.</div><h3>3.5 Nepresnosti</h3><p>Chyby spôsobuje odčítanie silomerov, trenie silomerov a krúžku o podložku, nepresné zaznačenie smerov nití a nepresná konštrukcia. Pomáha použiť silomery s vhodným rozsahom a väčšiu mierku výkresu.</p>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO22', 'Otázka', 'maturit'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
