"""Vzor 28 podľa fotky 28 a MO28 (text písaný priamo). Doplnené z fotky: znamienková konvencia a priečne zväčšenie;
v časti 2c dopočítaný nulový bod pre náboje opačného znamienka; obrázky prekreslené.
-> Vzor28_zadanie.html + Vzor28_vypracovanie.html.  Spustenie: python -I gen28.py <priečinok FYZIKA>"""
import sys, pathlib, math

DST = pathlib.Path(sys.argv[1])
N = 28
TOPICS = ['Optické zobrazovanie', 'Elektrické pole dvoch nábojov', 'Merná tepelná kapacita pevnej látky']

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

def hrot(x1, y1, x2, y2, farba, l=12, w=6):
    d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
    a = (x2 - l * ux + w * uy, y2 - l * uy - w * ux); b = (x2 - l * ux - w * uy, y2 - l * uy + w * ux)
    return f'<path d="M{x2:.1f} {y2:.1f}L{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}Z" fill="{farba}"/>'

# ---------- obrázky ----------
def sosovka(vyp):
    """Mierka 10 px = 1 cm: f = 8 cm, predmet a = 20 cm, výška 7 cm -> obraz a′ = 13,3 cm, výška −4,7 cm."""
    O, Y = 330, 145
    lucy = ''
    if vyp:
        lucy = ('<g fill="none" stroke-width="2"><path d="M130 75H330L463.3 191.7" stroke="#d37820"/><path d="M130 75L463.3 191.7" stroke="#2e8b57"/>'
                '<path d="M130 75L330 191.7H463.3" stroke="#6a4fc4"/></g>'
                '<path d="M463.3 145V185" stroke="#c0392b" stroke-width="3"/>' + hrot(463.3, 145, 463.3, 191.7, '#c0392b') +
                '<text x="474" y="206" font-size="14" fill="#c0392b">obraz</text>')
    return ('<svg class="diagram" viewBox="0 0 620 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Spojná šošovka, predmet za dvojnásobnou ohniskovou vzdialenosťou">'
            f'<path d="M25 {Y}H600" stroke="#637889" stroke-width="1.5"/>'
            '<path d="M330 22Q306 145 330 236Q354 145 330 22Z" fill="#dcebf7" stroke="#2f6db3" stroke-width="2"/>'
            '<g stroke="#193b59" stroke-width="2"><path d="M250 139V151M410 139V151M170 139V151M490 139V151"/></g>'
            '<path d="M130 145V86" stroke="#193b59" stroke-width="3"/>' + hrot(130, 145, 130, 75, '#193b59') + lucy +
            '<g font-size="14" fill="#193b59"><text x="245" y="166">F</text><text x="405" y="166">F′</text><text x="160" y="166">2F</text><text x="480" y="166">2F′</text>'
            '<text x="104" y="66">predmet</text><text x="338" y="18">spojná šošovka</text><text x="336" y="162">O</text></g></svg>')

def naboje(vyp):
    X1, X2, Yl = 115, 505, 60
    M = (X1 + X2) / 2
    extra = ''
    if vyp:
        nx = X1 + (X2 - X1) * 7 / 21
        extra = ('<path d="M310 92H324" stroke="#2f6db3" stroke-width="3"/>' + hrot(310, 92, 334, 92, '#2f6db3') +
                 '<path d="M310 110H240" stroke="#c0392b" stroke-width="3"/>' + hrot(310, 110, 230, 110, '#c0392b') +
                 '<g font-size="14"><text x="340" y="97" fill="#2f6db3">E₁</text><text x="206" y="115" fill="#c0392b">E₂</text></g>'
                 f'<circle cx="{nx:.0f}" cy="{Yl}" r="5" fill="#26724c"/><text x="{nx - 5:.0f}" y="{Yl - 12}" font-size="14" fill="#26724c">N</text>')
    return ('<svg class="diagram" viewBox="0 0 620 170" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dva kladné bodové náboje vo vzdialenosti 21 cm a stred ich spojnice M">'
            f'<path d="M{X1} {Yl}H{X2}" stroke="#637889" stroke-width="2"/>'
            f'<circle cx="{X1}" cy="{Yl}" r="18" fill="#fde3cf" stroke="#c0392b" stroke-width="2"/><circle cx="{X2}" cy="{Yl}" r="24" fill="#fde3cf" stroke="#c0392b" stroke-width="2"/>'
            f'<circle cx="{M:.0f}" cy="{Yl}" r="5" fill="#193b59"/>'
            '<g font-size="15" fill="#193b59"><text x="109" y="66">+</text><text x="499" y="66">+</text><text x="70" y="25">Q₁ = 2 · 10⁻⁸ C</text><text x="440" y="25">Q₂ = 8 · 10⁻⁸ C</text>'
            f'<text x="{M - 5:.0f}" y="{Yl - 12}">M</text><text x="276" y="160">d = 21 cm</text></g>'
            '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M115 136V148H505V136"/></g>' + extra + '</svg>')

KALORIMETER = ('<svg class="diagram" viewBox="0 0 540 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Zmiešavací kalorimeter s vodou, teplomerom, miešadlom a zahriatym telesom">'
               '<rect x="140" y="50" width="200" height="130" rx="10" fill="#eef2f6" stroke="#475569" stroke-width="4"/>'
               '<rect x="154" y="62" width="172" height="106" rx="6" fill="#fff" stroke="#94a3b8" stroke-width="2"/>'
               '<rect x="156" y="90" width="168" height="76" fill="#cfe7f6"/>'
               '<rect x="262" y="112" width="56" height="36" rx="6" fill="#9aa4ae" stroke="#566374" stroke-width="1.5"/>'
               '<path d="M215 14V150" stroke="#c0392b" stroke-width="5"/><circle cx="215" cy="152" r="6" fill="#c0392b"/>'
               '<path d="M175 30V150H200" stroke="#475569" stroke-width="2.5" fill="none"/>'
               '<g stroke="#637889" stroke-width="1.2"><path d="M223 26H380M320 130H380M181 40H110M330 175H380"/></g>'
               '<g font-size="14" fill="#193b59"><text x="386" y="30">teplomer</text><text x="386" y="134">zahriate teleso</text><text x="44" y="44">miešadlo</text>'
               '<text x="386" y="179">kalorimeter</text><text x="236" y="106">voda</text></g></svg>')

# ---------- zadanie ----------
Z1 = f'''<h2>1. Optické zobrazovanie</h2><div class="task"><ol><li>Vysvetlite základné princípy optického zobrazovania. Kedy vzniká skutočný a kedy zdanlivý obraz?</li><li>Napíšte zobrazovaciu rovnicu zrkadla a vysvetlite veličiny v nej.</li><li>Opíšte zobrazovanie lomom – spojnou a rozptylnou šošovkou.</li><li>Vysvetlite znamienkovú konvenciu a priečne zväčšenie.</li></ol><p><strong>Úloha:</strong> Zostrojte obraz predmetu spojnou šošovkou podľa obrázka. Opíšte vlastnosti obrazu a vysvetlite, ako sa obraz mení, keď predmet približujeme k šošovke.</p>{sosovka(False)}</div>'''

Z2 = f'''<h2>2. Elektrické pole</h2><div class="task"><p>Dva kladné bodové náboje <strong>Q₁ = 2 · 10⁻⁸&nbsp;C</strong> a <strong>Q₂ = 8 · 10⁻⁸&nbsp;C</strong> sú vo vákuu vo vzdialenosti <strong>d = 21&nbsp;cm</strong>. Použite k = 9 · 10⁹&nbsp;N·m²/C².</p>{naboje(False)}<ol type="a"><li>Vypočítajte výslednú intenzitu elektrického poľa v strede M spojnice nábojov a určte smer jej vektora.</li><li>Určte bod na priamke nábojov, v ktorom je výsledná intenzita nulová.</li><li>Čo by sa zmenilo, keby jeden z nábojov mal opačné znamienko?</li></ol></div>'''

Z3 = '''<h2>3. Experiment – merná tepelná kapacita pevnej látky</h2><div class="task"><p>Pomocou zmiešavacieho kalorimetra určte mernú tepelnú kapacitu pevnej látky (napríklad kovového valčeka). Uveďte pomôcky a postup merania, zostavte kalorimetrickú rovnicu a vyjadrite z nej hľadanú veličinu. Uveďte hlavné zdroje chýb.</p></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Optické zobrazovanie</h2><h3>1.1 Princípy zobrazovania</h3><p>Optická sústava (zrkadlo, šošovka) mení smer lúčov, ktoré vychádzajú z bodov predmetu. Ak sa lúče po odraze alebo lome skutočne pretnú v jednom bode, vzniká <strong>skutočný obraz</strong> – dá sa zachytiť na tienidle. Ak sa pretínajú len ich predĺženia, vzniká <strong>zdanlivý obraz</strong> – vidíme ho, ale na tienidle sa nezobrazí.</p><p>Obraz konštruujeme pomocou význačných lúčov. Pri guľových zrkadlách a tenkých šošovkách uvažujeme len lúče blízke optickej osi (paraxiálne), inak je obraz neostrý.</p><p><strong>Rovinné zrkadlo</strong> vytvára obraz zdanlivý, priamy, rovnako veľký, súmerne združený s predmetom podľa roviny zrkadla.</p><h3>1.2 Zobrazovacia rovnica zrkadla</h3><div class="formula">1/a + 1/a′ = 1/f &nbsp;&nbsp;&nbsp; f = r/2</div><p>a je predmetová vzdialenosť (predmet – vrchol zrkadla), a′ obrazová vzdialenosť, f ohnisková vzdialenosť a r polomer krivosti. Duté zrkadlo má ohnisko pred zrkadlom, vypuklé za zrkadlom.</p><h3>1.3 Zobrazovanie šošovkami</h3><p>Šošovka zobrazuje <strong>lomom</strong> svetla na dvoch guľových plochách. <strong>Spojná šošovka</strong> (spojka) je v strede hrubšia, rovnobežné lúče sa po lome stretnú v obrazovom ohnisku F′. <strong>Rozptylná šošovka</strong> (rozptylka) je v strede tenšia, rovnobežné lúče z nej vychádzajú rozbiehavo, akoby vychádzali z ohniska pred šošovkou. Pre tenkú šošovku platí rovnaká zobrazovacia rovnica 1/a + 1/a′ = 1/f.</p><p>Význačné lúče spojky:</p><ul><li>lúč rovnobežný s optickou osou sa láme do obrazového ohniska F′,</li><li>lúč cez optický stred O prechádza bez zmeny smeru,</li><li>lúč cez predmetové ohnisko F sa láme rovnobežne s osou.</li></ul><h3>1.4 Znamienková konvencia a priečne zväčšenie</h3><ul><li>a &gt; 0 pre skutočný predmet (pred zrkadlom alebo šošovkou),</li><li>a′ &gt; 0 pre skutočný obraz, a′ &lt; 0 pre zdanlivý obraz,</li><li>f &gt; 0 pre duté zrkadlo a spojku, f &lt; 0 pre vypuklé zrkadlo a rozptylku,</li><li>rozmer nad optickou osou je kladný, pod osou záporný.</li></ul><p><strong>Priečne zväčšenie</strong> je pomer veľkosti obrazu y′ a predmetu y:</p><div class="formula">Z = y′/y = −a′/a</div><p>Z &gt; 0 znamená priamy obraz, Z &lt; 0 prevrátený. |Z| &gt; 1 je obraz zväčšený, |Z| &lt; 1 zmenšený.</p><h3>1.5 Riešenie úlohy</h3>{sosovka(True)}<p>Na obraz stačia dva z troch význačných lúčov; tretí slúži ako kontrola. Predmet je ďalej ako 2f, preto je obraz <strong>skutočný, prevrátený a zmenšený</strong> a vzniká medzi F′ a 2F′.</p><p>Obrázok je nakreslený v mierke: f = 8 cm, a = 20 cm. Výpočtom:</p><div class="formula">1/a′ = 1/f − 1/a = 1/8 − 1/20 = 3/40 &nbsp; → &nbsp; a′ ≈ 13,3 cm<br>Z = −a′/a = −13,3/20 ≈ −0,67</div><p><strong>Pri približovaní predmetu</strong> k šošovke:</p><table><tr><th>Poloha predmetu</th><th>Obraz</th></tr><tr><td>a &gt; 2f</td><td>skutočný, prevrátený, zmenšený, medzi F′ a 2F′</td></tr><tr><td>a = 2f</td><td>skutočný, prevrátený, rovnako veľký, v 2F′</td></tr><tr><td>f &lt; a &lt; 2f</td><td>skutočný, prevrátený, zväčšený, za 2F′ (projektor)</td></tr><tr><td>a = f</td><td>lúče sú rovnobežné, obraz nevzniká (v nekonečne)</td></tr><tr><td>a &lt; f</td><td>zdanlivý, priamy, zväčšený, na strane predmetu (lupa)</td></tr></table><div class="result"><strong>Obraz je skutočný, prevrátený a zmenšený (a′ ≈ 13,3 cm, Z ≈ −0,67).</strong> Približovaním predmetu sa obraz vzďaľuje od šošovky a zväčšuje sa.</div>'''

V2 = f'''<h2>2. Elektrické pole</h2><h3>2.1 Intenzita poľa bodového náboja</h3><p>Intenzita elektrického poľa bodového náboja Q vo vzdialenosti r má veľkosť:</p><div class="formula">E = k|Q|/r² &nbsp;&nbsp;&nbsp; k = 1/(4πε₀) ≈ 9 · 10⁹ N·m²/C²</div><p>Vektor intenzity smeruje od kladného náboja a ku zápornému. Výsledná intenzita viacerých nábojov je <strong>vektorový súčet</strong> intenzít jednotlivých nábojov (princíp superpozície).</p><h3>2.2 Riešenie úlohy</h3>{naboje(True)}<p><strong>a)</strong> Bod M je od oboch nábojov vzdialený r = d/2 = 0,105 m:</p><div class="formula">E₁ = kQ₁/r² = 9 · 10⁹ · 2 · 10⁻⁸ / 0,105² N/C ≈ 1,63 · 10⁴ N/C<br>E₂ = kQ₂/r² = 9 · 10⁹ · 8 · 10⁻⁸ / 0,105² N/C ≈ 6,53 · 10⁴ N/C</div><p>Oba náboje sú kladné, preto E₁ v bode M smeruje od Q₁ (k Q₂) a E₂ od Q₂ (k Q₁) – majú opačný smer:</p><div class="formula">E = E₂ − E₁ ≈ 4,9 · 10⁴ N/C</div><p>Výsledná intenzita smeruje od väčšieho náboja Q₂ k menšiemu náboju Q₁.</p><p><strong>b)</strong> Intenzity sa môžu vyrušiť len tam, kde majú opačný smer – medzi nábojmi. Bod N je vo vzdialenosti x od Q₁:</p><div class="formula">kQ₁/x² = kQ₂/(d − x)² &nbsp; → &nbsp; (d − x)/x = √(Q₂/Q₁) = 2 &nbsp; → &nbsp; x = d/3 = 7 cm</div><p>Nulový bod je bližšie k menšiemu náboju – 7 cm od Q₁ a 14 cm od Q₂.</p><p><strong>c)</strong> Ak by bol napríklad Q₂ záporný, intenzity v bode M by mali rovnaký smer (od Q₁ k Q₂) a sčítali by sa:</p><div class="formula">E = E₁ + E₂ ≈ 8,2 · 10⁴ N/C</div><p>Medzi nábojmi by nulový bod nebol. Intenzity by sa vyrušili mimo úsečky, na strane menšieho náboja Q₁, vo vzdialenosti x od neho:</p><div class="formula">(d + x)/x = 2 &nbsp; → &nbsp; x = d = 21 cm</div><div class="result"><strong>a) E ≈ 4,9 · 10⁴ N/C, smer od Q₂ k Q₁; b) 7 cm od Q₁ medzi nábojmi; c) v M by bolo E ≈ 8,2 · 10⁴ N/C a nulový bod by bol 21 cm za Q₁.</strong></div>'''

V3 = f'''<h2>3. Experiment – merná tepelná kapacita pevnej látky</h2><h3>3.1 Princíp</h3><p>Zahriate teleso vložíme do studenej vody v kalorimetri. Teleso sa ochladzuje, voda a kalorimeter sa ohrievajú, kým nenastane rovnovážna teplota t. Pri zanedbaní výmeny tepla s okolím platí kalorimetrická rovnica – teplo odovzdané telesom sa rovná teplu prijatému vodou a kalorimetrom:</p><div class="formula">m<sub>t</sub>c<sub>t</sub>(t<sub>t</sub> − t) = (m<sub>v</sub>c<sub>v</sub> + C<sub>k</sub>)(t − t<sub>v</sub>)</div><p>Odtiaľ hľadaná merná tepelná kapacita:</p><div class="formula">c<sub>t</sub> = (m<sub>v</sub>c<sub>v</sub> + C<sub>k</sub>)(t − t<sub>v</sub>) / [m<sub>t</sub>(t<sub>t</sub> − t)] &nbsp;&nbsp; [c] = J/(kg·K)</div><p>Index t označuje teleso, v vodu a k kalorimeter.</p><h3>3.2 Pomôcky</h3><p>Zmiešavací kalorimeter s miešadlom, teplomer (najlepšie digitálny), váhy, kovové teleso na nitke, kadička s vriacou vodou alebo vodný kúpeľ, studená voda.</p>{KALORIMETER}<h3>3.3 Postup</h3><ol><li>Odvážime teleso (m<sub>t</sub>) a vodu v kalorimetri (m<sub>v</sub>). Tepelnú kapacitu kalorimetra C<sub>k</sub> poznáme alebo ju určíme vopred.</li><li>Zmeriame počiatočnú teplotu vody t<sub>v</sub>.</li><li>Teleso zohrejeme vo vriacej vode niekoľko minút; jeho teplota t<sub>t</sub> sa rovná teplote kúpeľa.</li><li>Teleso rýchlo prenesieme do kalorimetra, zakryjeme a miešame.</li><li>Zapíšeme najvyššiu ustálenú teplotu t a vypočítame c<sub>t</sub>.</li></ol><h3>3.4 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje; nejde o skutočné meranie.</p><table><tr><th>Veličina</th><th>Hodnota</th></tr><tr><td>teleso: m<sub>t</sub>, t<sub>t</sub></td><td>0,200 kg; 90 °C</td></tr><tr><td>voda: m<sub>v</sub>, t<sub>v</sub></td><td>0,250 kg; 20 °C</td></tr><tr><td>kalorimeter: C<sub>k</sub></td><td>80 J/K</td></tr><tr><td>rovnovážna teplota t</td><td>25 °C</td></tr></table><div class="formula">c<sub>t</sub> = (0,250 · 4 180 + 80) · 5 / (0,200 · 65) J/(kg·K) ≈ 433 J/(kg·K)</div><div class="result"><strong>Záver:</strong> Modelová hodnota 433 J/(kg·K) je blízko tabuľkovej hodnote pre oceľ (asi 450 J/(kg·K)), teleso je teda pravdepodobne oceľové.</div><h3>3.5 Zdroje chýb</h3><p>Teleso sa ochladí pri prenose a prenesie so sebou trochu horúcej vody. Kalorimeter vymieňa teplo s okolím, teplomer reaguje s oneskorením a voda nemusí byť dobre premiešaná. Chybu zmenšíme rýchlym prenosom, zakrytím kalorimetra, dôkladným miešaním a tým, že studenú vodu pripravíme o niečo chladnejšiu, ako je teplota miestnosti – straty a zisky tepla sa potom čiastočne vyrovnajú.</p>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO28', 'Otázka', 'maturit'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
