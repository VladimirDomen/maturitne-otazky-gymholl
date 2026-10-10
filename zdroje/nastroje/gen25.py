"""Vzor 25 z fotky 25 (bez zdrojového HTML – obsah písaný priamo)
-> Vzor25_zadanie.html + Vzor25_vypracovanie.html.
Spustenie: python -I gen25.py <priečinok FYZIKA>"""
import sys, pathlib

DST = pathlib.Path(sys.argv[1])
N = 25
TOPICS = ['Atómové jadro', 'Elektrický prúd v elektrolytoch – poniklovanie', 'Meranie posuvným meradlom a chyby merania']

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

def vazbova():
    body = [(2, 1.11), (3, 2.57), (4, 7.07), (6, 5.33), (7, 5.61), (9, 6.46), (12, 7.68), (16, 7.98), (20, 8.03), (28, 8.45), (40, 8.55), (56, 8.79),
            (80, 8.71), (100, 8.60), (120, 8.51), (140, 8.38), (170, 8.18), (200, 7.92), (238, 7.57)]
    X = lambda a: 70 + 1.75 * a
    Y = lambda e: 260 - 25 * e
    pts = ' '.join(f'{X(a):.1f},{Y(e):.1f}' for a, e in body)
    znac = ''.join(f'<circle cx="{X(a):.1f}" cy="{Y(e):.1f}" r="4.5" fill="#c0392b"/>' for a, e in ((4, 7.07), (56, 8.79), (238, 7.57)))
    return ('<svg class="diagram" viewBox="0 0 520 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graf väzbovej energie na jeden nukleón od nukleónového čísla: maximum asi 8,8 MeV pri železe 56, hélium 4 má 7,1 MeV, urán 238 asi 7,6 MeV">'
            '<g stroke="#e3eaf1" stroke-width="1"><path d="M70 210H490M70 160H490M70 110H490M70 60H490"/></g>'
            '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M70 272V25M60 260H500M64 37L70 25L76 37M488 254L500 260L488 266"/></g>'
            f'<polyline points="{pts}" fill="none" stroke="#2f6db3" stroke-width="2.5"/>{znac}'
            '<g font-size="14" fill="#253d51"><text x="52" y="215">2</text><text x="52" y="165">4</text><text x="52" y="115">6</text><text x="52" y="65">8</text>'
            f'<text x="{X(50) - 8:.0f}" y="280">50</text><text x="{X(100) - 12:.0f}" y="280">100</text><text x="{X(150) - 12:.0f}" y="280">150</text><text x="{X(200) - 12:.0f}" y="280">200</text>'
            '<text x="80" y="22">B/A (MeV)</text><text x="490" y="250">A</text></g>'
            f'<g font-size="14" fill="#c0392b"><text x="{X(4) + 8:.0f}" y="{Y(7.07) + 18:.0f}">⁴He</text><text x="{X(56) - 14:.0f}" y="{Y(8.79) - 10:.0f}">⁵⁶Fe</text><text x="{X(238) - 34:.0f}" y="{Y(7.57) - 10:.0f}">²³⁸U</text></g>'
            f'<g font-size="13" fill="#637889"><text x="{X(8):.0f}" y="245">syntéza →</text><text x="{X(150):.0f}" y="245">← štiepenie</text></g></svg>')

VAZBOVA = vazbova()

def retazova():
    def jadro(x, y):
        return f'<circle cx="{x}" cy="{y}" r="16" fill="#9fb3c8" stroke="#375873" stroke-width="2"/><text x="{x - 11}" y="{y + 5}" font-size="12" fill="#193b59">²³⁵U</text>'
    def neutron(x1, y1, x2, y2):
        return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#2f6db3" stroke-width="1.8"/><circle cx="{x1}" cy="{y1}" r="4" fill="#2f6db3"/>'
    s = neutron(30, 150, 84, 150) + jadro(100, 150)
    s += '<circle cx="138" cy="122" r="11" fill="#e8a093"/><circle cx="138" cy="178" r="11" fill="#e8a093"/>'
    for y2 in (70, 150, 230):
        s += neutron(140, 150, 214, y2 if y2 != 150 else 150) + jadro(230, y2)
        for dy in (-36, 0, 36):
            s += neutron(270, y2, 340, y2 + dy)
    return ('<svg class="diagram" viewBox="0 0 440 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Reťazová štiepna reakcia: neutrón rozštiepi jadro uránu 235, vzniknú dva úlomky a tri neutróny, ktoré štiepia ďalšie jadrá">'
            + s + '<g font-size="13" fill="#637889"><text x="20" y="136">n</text><text x="120" y="210">úlomky</text><text x="290" y="22">ďalšie neutróny</text>'
            '<text x="150" y="292">k &gt; 1 lavína, k = 1 reaktor</text></g></svg>')

RETAZOVA = retazova()

PRENIKANIE = ('<svg class="diagram" viewBox="0 0 560 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Prenikavosť žiarenia: alfa zastaví papier, beta hliníkový plech, gama zoslabí až hrubá vrstva olova alebo betónu">'
              '<rect x="20" y="70" width="40" height="60" rx="6" fill="#4f5d73"/><text x="24" y="106" font-size="13" fill="#fff">zdroj</text>'
              '<rect x="160" y="30" width="6" height="140" fill="#f4ecd8" stroke="#9a6b12"/><rect x="270" y="30" width="14" height="140" fill="#c9d6e2" stroke="#637889"/><rect x="390" y="30" width="34" height="140" fill="#8a96a3" stroke="#4f5d73"/>'
              '<g stroke-width="2.5" fill="none"><path d="M60 70H158" stroke="#c0392b"/><path d="M60 100H268" stroke="#2f6db3"/><path d="M60 130H390" stroke="#26724c"/><path d="M424 130H520" stroke="#26724c" stroke-dasharray="6 4"/></g>'
              '<g font-size="15"><text x="80" y="62" fill="#c0392b">α</text><text x="80" y="92" fill="#2f6db3">β</text><text x="80" y="150" fill="#26724c">γ</text></g>'
              '<g font-size="13" fill="#637889"><text x="136" y="188">papier</text><text x="240" y="188">hliník (mm)</text><text x="380" y="188">olovo, betón</text></g></svg>')

NIKLOVANIE = ('<svg class="diagram" viewBox="0 0 520 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Poniklovanie: predmet je katóda, niklová doska je anóda, v roztoku síranu nikelnatého sa ióny niklu pohybujú ku katóde a usadzujú sa na predmete">'
              '<rect x="82" y="110" width="356" height="128" fill="#d9efe4"/><path d="M80 90V240H440V90" fill="none" stroke="#193b59" stroke-width="3"/>'
              '<rect x="130" y="70" width="18" height="150" fill="#9aa4ad" stroke="#4f5d73" stroke-width="2"/>'
              '<rect x="340" y="120" width="70" height="80" rx="8" fill="#c9a77c" stroke="#7a5230" stroke-width="2"/><rect x="336" y="116" width="78" height="88" rx="10" fill="none" stroke="#9aa4ad" stroke-width="4"/>'
              '<g stroke="#193b59" stroke-width="2.5" fill="none"><path d="M139 70V40H230M260 40H375V116"/><path d="M230 26V54"/><path d="M244 32V48" stroke-width="7"/></g>'
              '<g stroke="#26724c" stroke-width="2.5" fill="none"><path d="M200 160H300M290 154L302 160L290 166"/></g>'
              '<g font-size="15"><text x="210" y="152" fill="#26724c">Ni²⁺</text><text x="220" y="22" fill="#193b59">+</text><text x="250" y="22" fill="#193b59">−</text></g>'
              '<g font-size="13" fill="#637889"><text x="96" y="256">anóda: Ni</text><text x="326" y="256">katóda: predmet</text><text x="190" y="228">roztok NiSO₄</text></g></svg>')

def meradlo():
    hl = ''.join(f'<path d="M{60 + 10 * i} 92V{80 if i % 10 == 0 else (84 if i % 5 == 0 else 86)}"/>' for i in range(0, 41))
    cis = ''.join(f'<text x="{60 + 100 * k - 4}" y="76">{k}</text>' for k in range(0, 5))
    # nónius 10 dielikov na 9 mm, 0 nónia pri 19,9 mm (x = 60 + 199)
    x0 = 60 + 199
    non = ''.join(f'<path d="M{x0 + 9 * i:.0f} 92V{104 if i in (0, 10) else 100}"/>' for i in range(0, 11))
    return ('<svg class="diagram" viewBox="0 0 520 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Posuvné meradlo s nóniom: nula nónia je tesne pred 20 mm a s hlavnou stupnicou sa kryje 9. dielik nónia, výsledok 19,9 mm">'
            '<rect x="40" y="60" width="440" height="32" fill="#eef2f6" stroke="#637889"/><rect x="250" y="92" width="120" height="30" fill="#dbe5ee" stroke="#637889"/>'
            '<path d="M40 60V160H60V92" fill="#c9d6e2" stroke="#637889"/><path d="M259 122V160H275V122" fill="#c9d6e2" stroke="#637889"/>'
            f'<g stroke="#193b59" stroke-width="1.2">{hl}{non}</g><g font-size="12" fill="#193b59">{cis}</g>'
            f'<path d="M{x0 + 81:.0f} 84V112" stroke="#c0392b" stroke-width="2"/>'
            '<rect x="60" y="126" width="199" height="30" fill="#c9a77c" stroke="#7a5230"/>'
            '<g font-size="13" fill="#637889"><text x="300" y="54">hlavná stupnica (cm), dielik 1 mm</text><text x="290" y="140">nónius (10 dielikov)</text><text x="110" y="176">valček</text></g>'
            '<text x="280" y="200" font-size="15" fill="#c0392b">19 mm + 9 · 0,1 mm = 19,9 mm</text></svg>')

MERADLO = meradlo()

# ---------- zadanie ----------
Z1 = '''<h2>1. Atómové jadro</h2><div class="task"><ol><li>Opíšte stavbu atómového jadra a vlastnosti jadrových síl.</li><li>Vysvetlite pojmy hmotnostný úbytok a väzbová energia jadra.</li><li>Charakterizujte prirodzenú a umelú rádioaktivitu a uveďte jej využitie.</li><li>Opíšte reťazovú štiepnu reakciu.</li><li>Uveďte využitie rádionuklidov, spôsoby ich kontroly a ochrany pred žiarením.</li></ol><p><em>Rozširujúca úloha:</em> Vypočítajte hmotnostný úbytok a väzbovú energiu jadra hélia ⁴₂He a väzbovú energiu pripadajúcu na jeden nukleón (m<sub>p</sub> = 1,007 276 u, m<sub>n</sub> = 1,008 665 u, m<sub>jadra He</sub> = 4,001 506 u, 1 u zodpovedá energii 931,5 MeV).</p></div>'''

Z2 = '''<h2>2. Elektrický prúd v elektrolytoch – poniklovanie</h2><div class="task"><ol><li>Vysvetlite vedenie elektrického prúdu v elektrolytoch a sformulujte Faradayove zákony elektrolýzy.</li></ol><p><strong>Úloha:</strong> Kovový predmet s povrchom <strong>S = 120 cm²</strong> sa poniklováva <strong>t = 5 hodín</strong> prúdom <strong>I = 0,3 A</strong>. Molárna hmotnosť niklu je <strong>M = 58,69 · 10⁻³ kg·mol⁻¹</strong>, nikel je v roztoku dvojmocný, hustota niklu je <strong>ρ = 8,8 · 10³ kg·m⁻³</strong>, F = 96 485 C·mol⁻¹.</p><ol type="a"><li>Vypočítajte hmotnosť vylúčeného niklu.</li><li>Akú hrúbku má vrstva niklu vylúčená na predmete?</li><li>Akú hmotnosť a hrúbku bude mať vrstva, ak poniklovanie trvá t = 10 hodín pri prúde I = 0,3 A?</li><li>Akú hmotnosť a hrúbku bude mať vrstva pri prúde I = 0,6 A a čase 5 hodín? Porovnajte výsledky c) a d).</li></ol></div>'''

Z3 = '''<h2>3. Experiment – meranie posuvným meradlom a chyby merania</h2><div class="task"><p>Posuvným meradlom zmerajte rozmery valčeka a určte jeho objem. Vysvetlite, ako sa odčíta údaj na nóniu. Spracujte opakované merania, určte absolútnu a relatívnu chybu merania a výsledok zapíšte v správnom tvare. Rozšírenie: valček zvážte, určte hustotu a odhadnite materiál.</p></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Atómové jadro</h2><h3>1.1 Stavba jadra a jadrové sily</h3><p>Jadro tvorí takmer celú hmotnosť atómu, no jeho rozmer je len rádovo 10⁻¹⁵ m (atóm 10⁻¹⁰ m). Skladá sa z <strong>nukleónov</strong> – kladne nabitých <strong>protónov</strong> a elektricky neutrálnych <strong>neutrónov</strong>. Jadro označujeme <sup>A</sup><sub>Z</sub>X, kde <strong>Z</strong> je protónové číslo (určuje prvok), <strong>N</strong> neutrónové číslo a <strong>A = Z + N</strong> nukleónové číslo. Jadrá s rovnakým Z a rôznym N sú <strong>izotopy</strong> (napr. ¹²C a ¹⁴C).</p><p>Protóny sa elektricky odpudzujú, jadro preto drží pohromade <strong>jadrová (silná) sila</strong>:</p><ul><li>je <strong>príťažlivá</strong> a oveľa silnejšia ako elektrostatické odpudzovanie,</li><li>má <strong>veľmi krátky dosah</strong> (asi 10⁻¹⁵ m) – pôsobí len medzi susednými nukleónmi (nasýtenosť),</li><li>nezávisí od náboja – pôsobí rovnako medzi protónmi aj neutrónmi.</li></ul><h3>1.2 Hmotnostný úbytok a väzbová energia</h3><p>Hmotnosť jadra je <strong>menšia</strong> ako súčet hmotností voľných nukleónov. Rozdiel je <strong>hmotnostný úbytok</strong>:</p><div class="formula">Δm = Z m<sub>p</sub> + N m<sub>n</sub> − m<sub>j</sub></div><p><strong>Väzbová energia</strong> je energia, ktorá sa uvoľní pri vzniku jadra z nukleónov – a ktorú treba dodať na jeho rozloženie. Podľa Einsteinovho vzťahu:</p><div class="formula">E<sub>v</sub> = Δm c²</div><p>Mierou stability je väzbová energia na jeden nukleón E<sub>v</sub>/A. Najväčšia je pri jadrách okolo železa (asi 8,8 MeV). Preto sa energia uvoľňuje <strong>štiepením</strong> ťažkých jadier aj <strong>syntézou</strong> ľahkých jadier.</p>{VAZBOVA}<h3>1.3 Prirodzená a umelá rádioaktivita</h3><p><strong>Prirodzená rádioaktivita</strong> (H. Becquerel 1896, M. a P. Curieovci) je samovoľná premena nestabilných jadier spojená s vyžarovaním:</p><ul><li><strong>α</strong> – jadrá hélia ⁴₂He, malá prenikavosť,</li><li><strong>β⁻</strong> – elektróny (neutrón sa mení na protón), <strong>β⁺</strong> – pozitróny,</li><li><strong>γ</strong> – elektromagnetické žiarenie veľkej energie, veľká prenikavosť.</li></ul><p>Rozpad je náhodný, pre veľký počet jadier platí zákon rádioaktívnej premeny N = N₀ · 2<sup>−t/T</sup>, kde T je polčas premeny. Aktivitu meriame v becquereloch (Bq = 1 premena za sekundu).</p><p><strong>Umelá rádioaktivita</strong> (I. a F. Joliot-Curieovci 1934) vzniká ostreľovaním stabilných jadier časticami (neutróny v reaktore, urýchľovače). Tak sa vyrábajú rádionuklidy, ktoré sa v prírode nevyskytujú.</p><h3>1.4 Reťazová štiepna reakcia</h3><p>Jadro uránu ²³⁵U po zachytení pomalého neutrónu sa rozštiepi na dva ľahšie úlomky, uvoľní 2 – 3 neutróny a asi 200 MeV energie, napr.:</p><div class="formula">²³⁵U + n → ¹⁴¹Ba + ⁹²Kr + 3 n + energia</div><p>Uvoľnené neutróny môžu štiepiť ďalšie jadrá – vznikne <strong>reťazová reakcia</strong>. Rozhoduje <strong>multiplikačný koeficient k</strong> (počet neutrónov z jedného štiepenia, ktoré spôsobia ďalšie štiepenie). Pri k = 1 je reakcia <strong>riadená</strong> (jadrový reaktor – moderátor spomaľuje neutróny, regulačné tyče ich pohlcujú), pri k &gt; 1 <strong>neriadená</strong> (jadrová bomba). Reťazová reakcia je možná len nad kritickou hmotnosťou štiepneho materiálu.</p>{RETAZOVA}<h3>1.5 Využitie rádionuklidov a ochrana pred žiarením</h3><ul><li><strong>Medicína:</strong> rádioterapia nádorov (⁶⁰Co, urýchľovače), diagnostika (⁹⁹ᵐTc, PET s ¹⁸F), sterilizácia nástrojov.</li><li><strong>Technika:</strong> defektoskopia zvarov, hrúbkomery a hladinomery, značkované atómy (sledovanie únikov), dymové hlásiče.</li><li><strong>Veda:</strong> rádiouhlíková metóda datovania (¹⁴C), datovanie hornín.</li><li><strong>Energetika:</strong> jadrové elektrárne.</li></ul><p>Ionizujúce žiarenie poškodzuje bunky. Účinok na organizmus vyjadruje <strong>dávka</strong> (gray, Gy) a <strong>ekvivalentná dávka</strong> (sievert, Sv). Ochrana: <strong>čas</strong> (čo najkratší pobyt), <strong>vzdialenosť</strong> (intenzita klesá so štvorcom vzdialenosti) a <strong>tienenie</strong>. Pracovníci nosia osobné dozimetre, pracoviská sa monitorujú a rádioaktívne látky sa evidujú a skladujú v tienených obaloch. Nebezpečné je najmä vdýchnutie alebo požitie žiaričov α.</p>{PRENIKANIE}<h3>1.6 Rozširujúca úloha – väzbová energia ⁴He</h3><div class="formula">Δm = 2 m<sub>p</sub> + 2 m<sub>n</sub> − m<sub>He</sub> = 2 · 1,007 276 u + 2 · 1,008 665 u − 4,001 506 u = 0,030 376 u</div><div class="formula">E<sub>v</sub> = 0,030 376 · 931,5 MeV ≈ 28,3 MeV &nbsp;&nbsp;&nbsp; E<sub>v</sub>/A = 28,3 MeV / 4 ≈ 7,1 MeV</div><p>To je asi 0,75 % hmotnosti nukleónov. Jadro ⁴He je mimoriadne stabilné, preto sa ako celok vyžaruje pri rozpade α.</p><div class="result"><strong>Δm ≈ 0,0304 u, E<sub>v</sub> ≈ 28,3 MeV ≈ 4,5 · 10⁻¹² J, na nukleón ≈ 7,1 MeV.</strong></div>'''

V2 = f'''<h2>2. Elektrický prúd v elektrolytoch – poniklovanie</h2><h3>2.1 Teória</h3><p>V elektrolyte (roztok alebo tavenina kyselín, zásad a solí) sú nosičmi náboja <strong>ióny</strong>, ktoré vznikajú elektrolytickou disociáciou. Katióny sa pohybujú ku katóde (−), anióny k anóde (+). Na elektródach sa látky vylučujú – <strong>elektrolýza</strong>.</p><p><strong>1. Faradayov zákon:</strong> hmotnosť vylúčenej látky je úmerná prenesenému náboju, m = A Q = A I t. <strong>2. Faradayov zákon:</strong> elektrochemický ekvivalent A = M/(zF). Spolu:</p><div class="formula">m = M I t / (z F)</div><p><strong>Galvanické pokovovanie:</strong> predmet je zapojený ako <strong>katóda</strong>, anóda je z kovu, ktorým pokovujeme (nikel), elektrolytom je roztok jeho soli (NiSO₄). Na katóde sa vylučuje nikel: Ni²⁺ + 2e⁻ → Ni. Anóda sa rozpúšťa a dopĺňa ióny do roztoku. Poniklovanie chráni pred koróziou a zlepšuje vzhľad.</p>{NIKLOVANIE}<h3>2.2 Riešenie úlohy</h3><p>Zadané: S = 120 cm² = 1,2 · 10⁻² m², t = 5 h = 18 000 s, I = 0,3 A, M = 58,69 · 10⁻³ kg/mol, z = 2, ρ = 8,8 · 10³ kg/m³.</p><p><strong>a)</strong> Prenesený náboj a hmotnosť niklu:</p><div class="formula">Q = I t = 0,3 A · 18 000 s = 5 400 C<br>m = M Q / (z F) = 58,69 · 10⁻³ · 5 400 / (2 · 96 485) kg ≈ 1,64 · 10⁻³ kg = 1,64 g</div><p>Elektrochemický ekvivalent niklu je A = M/(zF) ≈ 3,04 · 10⁻⁷ kg/C.</p><p><strong>b)</strong> Vrstva niklu tvorí „platňu“ s obsahom S a hrúbkou d, jej objem je V = S d = m/ρ:</p><div class="formula">d = m / (ρ S) = 1,64 · 10⁻³ kg / (8 800 kg/m³ · 1,2 · 10⁻² m²) ≈ 1,56 · 10⁻⁵ m ≈ 16 μm</div><p><strong>c)</strong> t = 10 h = 36 000 s, I = 0,3 A:</p><div class="formula">Q = 10 800 C &nbsp; → &nbsp; m ≈ 3,28 g, d ≈ 31 μm</div><p><strong>d)</strong> I = 0,6 A, t = 5 h:</p><div class="formula">Q = 0,6 A · 18 000 s = 10 800 C &nbsp; → &nbsp; m ≈ 3,28 g, d ≈ 31 μm</div><p><strong>Porovnanie:</strong> v oboch prípadoch prejde elektrolytom rovnaký náboj Q = It = 10 800 C, preto sa vylúči rovnaká hmotnosť niklu – dvojnásobná oproti a). Podľa 1. Faradayovho zákona nezáleží na tom, či zdvojnásobíme čas alebo prúd, rozhoduje len súčin I · t. V praxi je však pri väčšej prúdovej hustote vrstva menej kvalitná (hrubozrnná, prepálená), preto sa pokovuje radšej menším prúdom dlhší čas.</p><div class="result"><strong>a) m ≈ 1,64 g; b) d ≈ 16 μm; c) aj d) m ≈ 3,28 g, d ≈ 31 μm – rovnaký náboj, rovnaký výsledok.</strong></div>'''

V3 = f'''<h2>3. Experiment – meranie posuvným meradlom a chyby merania</h2><h3>3.1 Posuvné meradlo a nónius</h3><p>Posuvné meradlo má hlavnú milimetrovú stupnicu a posuvnú časť s pomocnou stupnicou – <strong>nóniom</strong>. Bežný nónius má 10 dielikov na dĺžke 9 mm, jeden dielik nónia je teda o 0,1 mm kratší ako milimeter. Meradlo umožňuje merať vonkajšie rozmery, vnútorné rozmery (horné čeľuste) aj hĺbku (hĺbkomer).</p><p><strong>Odčítanie:</strong> celé milimetre odčítame na hlavnej stupnici pred nulou nónia. Desatiny milimetra určuje číslo dielika nónia, ktorý sa <strong>kryje</strong> s niektorou čiarou hlavnej stupnice. Presnosť je 0,1 mm (pri nóniu s 20 dielikmi 0,05 mm, s 50 dielikmi 0,02 mm).</p>{MERADLO}<h3>3.2 Chyby merania</h3><ul><li><strong>Hrubé chyby</strong> – omyl pri odčítaní alebo zápise. Takú hodnotu z merania vylúčime.</li><li><strong>Systematické chyby</strong> – pri opakovaní sa prejavia rovnako (nenulová poloha meradla, nepresná stupnica, nevhodná metóda). Odstránime ich kontrolou a opravou prístroja.</li><li><strong>Náhodné chyby</strong> – menia sa nepredvídateľne (nerovnosť telesa, nerovnaký prítlak čeľustí). Zmenšíme ich opakovaním merania.</li></ul><p>Pri n opakovaných meraniach je najlepším odhadom <strong>aritmetický priemer</strong> x̄. Ako odhad <strong>absolútnej chyby</strong> Δx použijeme priemernú odchýlku (priemer z |x<sub>i</sub> − x̄|). Nesmie byť menšia ako presnosť meradla. <strong>Relatívna chyba</strong> δx = Δx/x̄. Výsledok zapisujeme v tvare</p><div class="formula">x = (x̄ ± Δx) jednotka, &nbsp;&nbsp; δx = … %</div><p>Pri súčine a podiele sa sčítajú relatívne chyby, pri mocnine sa relatívna chyba násobí exponentom.</p><h3>3.3 Postup</h3><ol><li>Skontrolujeme nulovú polohu meradla (pri zovretých čeľustiach sa nula nónia kryje s nulou stupnice).</li><li>Priemer d valčeka zmeriame 5-krát na rôznych miestach a v rôznych smeroch, výšku h tiež 5-krát.</li><li>Vypočítame priemery, odchýlky, absolútnu a relatívnu chybu.</li><li>Vypočítame objem V = π d² h / 4 a jeho chybu.</li><li>Valček zvážime a vypočítame hustotu ρ = m/V.</li></ol><h3>3.4 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje (presnosť meradla 0,05 mm); nejde o skutočné meranie.</p><table><tr><th>Meranie</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>priemer</th></tr><tr><td>d (mm)</td><td>19,95</td><td>20,00</td><td>19,90</td><td>20,05</td><td>20,00</td><td>19,98</td></tr><tr><td>|d<sub>i</sub> − d̄| (mm)</td><td>0,03</td><td>0,02</td><td>0,08</td><td>0,07</td><td>0,02</td><td>0,044</td></tr><tr><td>h (mm)</td><td>40,10</td><td>40,05</td><td>40,15</td><td>40,10</td><td>40,00</td><td>40,08</td></tr><tr><td>|h<sub>i</sub> − h̄| (mm)</td><td>0,02</td><td>0,03</td><td>0,07</td><td>0,02</td><td>0,08</td><td>0,044</td></tr></table><p>Priemerná odchýlka 0,044 mm je menšia ako presnosť meradla, preto berieme Δd = Δh = 0,05 mm:</p><div class="formula">d = (19,98 ± 0,05) mm, &nbsp; δd = 0,05/19,98 ≈ 0,25 %<br>h = (40,08 ± 0,05) mm, &nbsp; δh = 0,05/40,08 ≈ 0,12 %</div><div class="formula">V = π d² h / 4 = π · 19,98² · 40,08 / 4 mm³ ≈ 12 570 mm³ = 12,57 cm³<br>δV = 2 δd + δh ≈ 2 · 0,25 % + 0,12 % ≈ 0,62 % &nbsp; → &nbsp; ΔV ≈ 0,08 cm³</div><div class="formula">V = (12,57 ± 0,08) cm³</div><p>Priemer vystupuje v druhej mocnine, preto jeho chyba ovplyvňuje objem dvojnásobne – priemer treba merať najstarostlivejšie.</p><p><strong>Rozšírenie – hustota:</strong> hmotnosť valčeka m = (34,0 ± 0,1) g, δm ≈ 0,3 %.</p><div class="formula">ρ = m / V = 34,0 g / 12,57 cm³ ≈ 2,71 g/cm³, &nbsp; δρ = δm + δV ≈ 0,9 % &nbsp; → &nbsp; ρ = (2,71 ± 0,03) g/cm³</div><p>Tabuľková hustota hliníka je 2,70 g/cm³ – valček je pravdepodobne z hliníka.</p><div class="result"><strong>d = (19,98 ± 0,05) mm, h = (40,08 ± 0,05) mm, V = (12,57 ± 0,08) cm³ (δV ≈ 0,6 %), ρ = (2,71 ± 0,03) g/cm³ – hliník.</strong></div>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO25', 'Otázka', 'maturit', 'riginál'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
