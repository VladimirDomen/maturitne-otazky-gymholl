"""Vzor 30 podľa fotky 30 a MO30 (text písaný priamo). Časť 2 podľa fotky a popisu používateľa: sériový obvod
so zdrojom, reostatom R1, R2 a R3, voltmeter V1 na R1 a V2 krížom (na R1 + R2); hodnoty doplnené (12 V; 10, 20, 30 Ω).
V časti 1 opravené: 390 nm je fialové viditeľné svetlo (MO30 uvádzal UV). V časti 3 doplnené modelové údaje.
-> Vzor30_zadanie.html + Vzor30_vypracovanie.html.  Spustenie: python -I gen30.py <priečinok FYZIKA>"""
import sys, pathlib, math

DST = pathlib.Path(sys.argv[1])
N = 30
TOPICS = ['Kvantová optika', 'Elektrický prúd v kovoch – obvod', 'Kmitanie vzduchového stĺpca']

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
    d = math.hypot(ux, uy); ux, uy = ux / d, uy / d
    a = (x - l * ux + w * uy, y - l * uy - w * ux); b = (x - l * ux - w * uy, y - l * uy + w * ux)
    return f'<path d="M{x:.1f} {y:.1f}L{a[0]:.1f} {a[1]:.1f}L{b[0]:.1f} {b[1]:.1f}Z" fill="{farba}"/>'

# ---------- obrázky ----------
def obvod():
    """Uzly: A (120,60) hore vľavo, B (120,240), C (460,240), D (460,60). Zdroj hore, R1 vľavo (reostat), R2 dole, R3 vpravo.
    V1 paralelne k R1, V2 krížom z A do C."""
    ux, uy = 340 / math.hypot(340, 180), 180 / math.hypot(340, 180)
    p1 = (290 - 18 * ux, 150 - 18 * uy); p2 = (290 + 18 * ux, 150 + 18 * uy)
    return ('<svg class="diagram" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sériový obvod so zdrojom, reostatom R1 a rezistormi R2 a R3; voltmeter V1 na R1, voltmeter V2 medzi začiatkom R1 a koncom R2">'
            '<g stroke="#193b59" stroke-width="3" fill="none"><path d="M120 110V60H250M268 60H460V110M460 190V240H330M250 240H120V190"/>'
            '<path d="M120 60H50V134M50 166V240H120"/>'
            f'<path d="M120 60L{p1[0]:.1f} {p1[1]:.1f}M{p2[0]:.1f} {p2[1]:.1f}L460 240"/>'
            '<rect x="108" y="110" width="24" height="80" fill="#fff"/><rect x="250" y="228" width="80" height="24" fill="#fff"/><rect x="448" y="110" width="24" height="80" fill="#fff"/>'
            '<path d="M250 38V82"/><path d="M268 48V72" stroke-width="7"/>'
            '<circle cx="50" cy="150" r="16" fill="#fff"/><circle cx="290" cy="150" r="18" fill="#fff"/></g>'
            '<path d="M98 202L140 104" stroke="#c0392b" stroke-width="2"/>' + hrot(142, 99, 42, -98, '#c0392b', 9, 4.5) +
            '<g fill="#193b59"><circle cx="120" cy="60" r="4.5"/><circle cx="120" cy="240" r="4.5"/><circle cx="460" cy="240" r="4.5"/></g>'
            '<g font-size="15" fill="#193b59"><text x="39" y="156">V₁</text><text x="279" y="156">V₂</text>'
            '<text x="232" y="30">U</text><text x="240" y="100">+</text><text x="276" y="100">−</text>'
            '<text x="144" y="160">R₁</text><text x="276" y="276">R₂</text><text x="480" y="156">R₃</text>'
            '<text x="102" y="52">A</text><text x="102" y="262">B</text><text x="466" y="262">C</text></g></svg>')

def trubica():
    """Trubica s vodou: pri vode uzol, pri otvorenom konci kmitňa; L = λ/4."""
    return ('<svg class="diagram" viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Rezonančná trubica s vodou: pri hladine je uzol, pri otvorenom konci kmitňa stojatého vlnenia">'
            '<rect x="102" y="180" width="126" height="70" fill="#cfe7f6" stroke="#375873" stroke-width="2"/>'
            '<rect x="132" y="180" width="66" height="55" fill="#cfe7f6"/>'
            '<g stroke="#375873" stroke-width="3"><path d="M130 30V235M200 30V235"/></g>'
            '<path d="M132 180H198" stroke="#2f6db3" stroke-width="2.5"/>'
            '<g fill="none" stroke="#c4661b" stroke-width="2.5"><path d="M165 180Q165 90 188 40"/><path d="M165 180Q165 90 142 40" stroke-dasharray="6 5"/></g>'
            '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M240 40V180M233 40H247M233 180H247"/></g>'
            '<path d="M70 40L104 40" stroke="#193b59" stroke-width="2"/>' + hrot(112, 40, 1, 0, '#193b59') +
            '<g font-size="15" fill="#193b59"><text x="250" y="116">L</text><text x="22" y="30">zdroj zvuku</text><text x="240" y="236">voda</text>'
            '<text x="300" y="48">kmitňa (otvorený koniec)</text><text x="300" y="186">uzol (hladina vody)</text><text x="300" y="116">L = λ/4, f = v/(4L)</text></g></svg>')

OBVOD = obvod()
TRUBICA = trubica()

# ---------- zadanie ----------
Z1 = '''<h2>1. Kvantová optika</h2><div class="task"><ol><li>Vysvetlite podstatu fotoelektrického javu: kvantum energie, fotón, medzná frekvencia a medzná vlnová dĺžka.</li><li>Opíšte vonkajší a vnútorný fotoelektrický jav a ich využitie.</li><li>Napíšte a vysvetlite Einsteinovu rovnicu fotoelektrického javu.</li><li>Vysvetlite korpuskulárno-vlnový dualizmus a de Broglieho vlnu.</li></ol><p><strong>Úloha:</strong> Vypočítajte energiu fotónu svetla s vlnovou dĺžkou <strong>λ₁ = 390&nbsp;nm</strong> a <strong>λ₂ = 790&nbsp;nm</strong>. Energiu vyjadrite v jouloch aj v elektrónvoltoch. Použite h = 6,626 · 10⁻³⁴&nbsp;J·s, c = 3 · 10⁸&nbsp;m/s, 1&nbsp;eV = 1,602 · 10⁻¹⁹&nbsp;J.</p></div>'''

Z2 = f'''<h2>2. Elektrický prúd v kovoch – obvod</h2><div class="task"><p>Zdroj s napätím <strong>U = 12&nbsp;V</strong> (vnútorný odpor zanedbajte) je v sérii s reostatom <strong>R₁ = 10&nbsp;Ω</strong> a rezistormi <strong>R₂ = 20&nbsp;Ω</strong> a <strong>R₃ = 30&nbsp;Ω</strong>. Voltmeter V₁ je pripojený k R₁, voltmeter V₂ medzi body A a C. Voltmetre považujte za ideálne.</p>{OBVOD}<ol type="a"><li>Určte celkový odpor obvodu.</li><li>Vypočítajte prúd v obvode.</li><li>Určte napätie, ktoré ukazujú voltmetre V₁ a V₂.</li><li>Ako sa zmenia údaje voltmetrov, ak jazdcom reostatu zväčšíme R₁ na 30&nbsp;Ω?</li></ol></div>'''

Z3 = '''<h2>3. Experiment – kmitanie vzduchového stĺpca</h2><div class="task"><p>Experimentálne preskúmajte kmitanie vzduchového stĺpca ako zdroja vlnenia. Zistite, ako závisí frekvencia vlnenia od výšky (dĺžky) vzduchového stĺpca. Navrhnite pomôcky, postup a spracovanie výsledkov.</p></div>'''

# ---------- vypracovanie ----------
V1 = '''<h2>1. Kvantová optika</h2><h3>1.1 Kvantum a fotón</h3><p>Planck zistil, že teleso vyžaruje a pohlcuje energiu len po celistvých dávkach – <strong>kvantách</strong>. Einstein vysvetlil, že aj samotné svetlo sa skladá z kvánt – <strong>fotónov</strong>. Fotón sa pohybuje rýchlosťou svetla a má energiu a hybnosť:</p><div class="formula">E = hf = hc/λ &nbsp;&nbsp;&nbsp; p = h/λ</div><p>h = 6,626 · 10⁻³⁴ J·s je Planckova konštanta. Energia fotónu rastie s frekvenciou – fotón fialového svetla má väčšiu energiu ako fotón červeného.</p><h3>1.2 Fotoelektrický jav</h3><p><strong>Vonkajší fotoelektrický jav:</strong> svetlo uvoľňuje elektróny z povrchu kovu. Pozorovania, ktoré vlnová teória nevysvetlí:</p><ul><li>elektróny sa uvoľnia len vtedy, keď je frekvencia svetla väčšia ako <strong>medzná frekvencia</strong> f₀ daného kovu – pri menšej frekvencii nepomôže ani veľká intenzita,</li><li>kinetická energia elektrónov závisí od frekvencie, nie od intenzity svetla,</li><li>intenzita svetla určuje len počet uvoľnených elektrónov,</li><li>jav nastáva okamžite.</li></ul><p>Vysvetlenie: jeden fotón odovzdá celú energiu jednému elektrónu. Ak energia fotónu stačí na prekonanie väzby (výstupná práca W<sub>v</sub>), elektrón kov opustí. Medzná frekvencia a <strong>medzná vlnová dĺžka</strong>:</p><div class="formula">f₀ = W<sub>v</sub>/h &nbsp;&nbsp;&nbsp; λ₀ = hc/W<sub>v</sub></div><p>Fotoelektrický jav nastáva len pri λ &lt; λ₀.</p><p><strong>Vnútorný fotoelektrický jav:</strong> v polovodiči fotón uvoľní elektrón z väzby, elektrón však zostane vo vnútri látky. Vznikne pár elektrón – diera a vodivosť sa zväčší. Využitie: fotorezistor, fotodióda, fotovoltický článok, snímač vo fotoaparáte. Vonkajší jav sa využíva vo fotonásobiči.</p><h3>1.3 Einsteinova rovnica</h3><div class="formula">hf = W<sub>v</sub> + ½mv²<sub>max</sub></div><p>Energia fotónu sa spotrebuje na výstupnú prácu a zvyšok tvorí maximálnu kinetickú energiu elektrónu.</p><h3>1.4 Dualizmus a de Broglieho vlna</h3><p>Svetlo má vlnové vlastnosti (interferencia, ohyb) aj časticové (fotoelektrický jav). Tento <strong>korpuskulárno-vlnový dualizmus</strong> rozšíril de Broglie na všetky častice. Častici s hybnosťou p = mv priradil vlnovú dĺžku:</p><div class="formula">λ = h/p = h/(mv)</div><p>Vlnové vlastnosti elektrónov potvrdila difrakcia elektrónov na kryštáloch. Využíva ich elektrónový mikroskop.</p><h3>1.5 Riešenie úlohy</h3><div class="formula">E₁ = hc/λ₁ = (6,626 · 10⁻³⁴ · 3 · 10⁸)/(390 · 10⁻⁹) J ≈ 5,10 · 10⁻¹⁹ J ≈ 3,18 eV<br>E₂ = hc/λ₂ = (6,626 · 10⁻³⁴ · 3 · 10⁸)/(790 · 10⁻⁹) J ≈ 2,52 · 10⁻¹⁹ J ≈ 1,57 eV</div><div class="result"><strong>E₁ ≈ 5,10 · 10⁻¹⁹ J = 3,18 eV; E₂ ≈ 2,52 · 10⁻¹⁹ J = 1,57 eV.</strong></div><p>Energia je nepriamo úmerná vlnovej dĺžke: E₁/E₂ = λ₂/λ₁ ≈ 2. Žiarenie s 390 nm je fialové svetlo na krátkovlnnom okraji viditeľného spektra, 790 nm je už blízke infračervené žiarenie za červeným okrajom.</p><p class="subtle">Užitočný vzťah: E (eV) ≈ 1 240/λ (nm). Fotón s 3,18 eV uvoľní elektróny napríklad z cézia (W<sub>v</sub> ≈ 2,1 eV, λ₀ ≈ 590 nm); fotón s 1,57 eV nie.</p>'''

V2 = f'''<h2>2. Elektrický prúd v kovoch – obvod</h2><h3>2.1 Teória</h3><p>V kovoch prenášajú náboj voľné elektróny. Pri stálej teplote platí <strong>Ohmov zákon</strong> I = U/R. Pri <strong>sériovom</strong> zapojení prechádza všetkými rezistormi rovnaký prúd, napätia sa sčítajú a celkový odpor je súčtom odporov: R = R₁ + R₂ + R₃. Reostat je rezistor s premenlivým odporom – posunutím jazdca meníme dĺžku drôtu, ktorou prechádza prúd. Ideálny voltmeter má veľmi veľký odpor, preto ním prúd neprechádza a obvod neovplyvní.</p><h3>2.2 Riešenie úlohy</h3>{OBVOD}<p><strong>a)</strong> Rezistory sú v sérii:</p><div class="formula">R = R₁ + R₂ + R₃ = 10 Ω + 20 Ω + 30 Ω = 60 Ω</div><p><strong>b)</strong> Prúd v obvode:</p><div class="formula">I = U/R = 12 V / 60 Ω = 0,2 A</div><p><strong>c)</strong> Voltmeter V₁ meria napätie na reostate:</p><div class="formula">U₁ = R₁I = 10 Ω · 0,2 A = 2 V</div><p>Voltmeter V₂ je pripojený krížom medzi body A a C. Po dolnej ceste medzi nimi sú R₁ a R₂:</p><div class="formula">U<sub>AC</sub> = (R₁ + R₂)I = 30 Ω · 0,2 A = 6 V</div><p>Kontrola po hornej ceste cez zdroj a R₃: U<sub>AC</sub> = U − R₃I = 12 V − 6 V = 6 V. Napätie medzi dvoma bodmi nezávisí od cesty, po ktorej ho počítame.</p><p><strong>d)</strong> Pri R₁ = 30 Ω:</p><div class="formula">R = 80 Ω, &nbsp; I = 12 V / 80 Ω = 0,15 A<br>U₁ = 30 Ω · 0,15 A = 4,5 V, &nbsp; U<sub>AC</sub> = 50 Ω · 0,15 A = 7,5 V</div><div class="result"><strong>a) R = 60 Ω; b) I = 0,2 A; c) V₁ ukazuje 2 V, V₂ ukazuje 6 V; d) prúd klesne na 0,15 A, V₁ ukáže 4,5 V a V₂ 7,5 V.</strong></div><p>Zväčšením odporu reostatu klesne prúd, ale napätie na reostate stúpne – reostat „berie“ väčšiu časť napätia zdroja. Tak sa reostat používa ako regulátor prúdu.</p>'''

V3 = f'''<h2>3. Experiment – kmitanie vzduchového stĺpca</h2><h3>3.1 Princíp</h3><p>Vzduch v trubici je pružné prostredie. Zvukové vlnenie (pozdĺžne) sa na koncoch trubice odráža a priame a odrazené vlnenie vytvoria <strong>stojaté vlnenie</strong>. Vzduchový stĺpec silno zaznie – rezonuje – len pri určitých frekvenciách. Na uzavretom konci (hladina vody) je uzol výchylky, na otvorenom konci kmitňa.</p>{TRUBICA}<p>Pre trubicu uzavretú na jednom konci je pri základnom kmitaní dĺžka stĺpca štvrtinou vlnovej dĺžky:</p><div class="formula">L = λ/4 &nbsp; → &nbsp; f₁ = v/(4L) &nbsp;&nbsp;&nbsp; vyššie: f = (2k + 1)v/(4L)</div><p>Pre trubicu otvorenú na oboch koncoch je L = λ/2 a f₁ = v/(2L). V oboch prípadoch platí: <strong>čím kratší vzduchový stĺpec, tým vyššia frekvencia</strong>. Na tomto princípe fungujú píšťaly organa, flauta a fľaše s rôznou výškou vody.</p><h3>3.2 Pomôcky</h3><p>Sklenená alebo plastová trubica ponorená do vysokého valca s vodou (vysúvaním trubice meníme L), generátor zvuku s reproduktorom alebo aplikácia v mobile, meter. Ako doplnok ladička so známou frekvenciou alebo niekoľko rovnakých fliaš s rôznym množstvom vody.</p><h3>3.3 Postup</h3><ol><li>Nad otvorený koniec trubice umiestnime reproduktor.</li><li>Nastavíme dĺžku vzduchového stĺpca L (od hladiny po okraj trubice).</li><li>Plynule meníme frekvenciu generátora a hľadáme najnižšiu frekvenciu, pri ktorej zvuk výrazne zosilnie – rezonanciu.</li><li>Meranie zopakujeme pre niekoľko dĺžok L.</li><li>Vypočítame súčin f·L a z neho rýchlosť zvuku v = 4fL.</li></ol><p>S ladičkou postupujeme naopak: frekvencia je stála a meníme L, kým stĺpec nezaznie. Pri 440 Hz nastane prvá rezonancia pri L ≈ 19,5 cm a ďalšia pri L ≈ 58,5 cm (3λ/4).</p><h3>3.4 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje; nejde o skutočné meranie.</p><table><tr><th>L (m)</th><th>f (Hz)</th><th>f·L (m/s)</th><th>v = 4fL (m/s)</th></tr><tr><td>0,20</td><td>420</td><td>84,0</td><td>336</td></tr><tr><td>0,30</td><td>282</td><td>84,6</td><td>338</td></tr><tr><td>0,40</td><td>212</td><td>84,8</td><td>339</td></tr><tr><td>0,50</td><td>170</td><td>85,0</td><td>340</td></tr></table><p>Súčin f·L je približne stály, frekvencia je teda nepriamo úmerná dĺžke stĺpca. Pri dvojnásobnej dĺžke (0,20 → 0,40 m) klesne frekvencia približne na polovicu.</p><div class="result"><strong>Záver:</strong> Kratší vzduchový stĺpec kmitá s vyššou frekvenciou, f ≈ v/(4L). Z meraní vychádza rýchlosť zvuku asi 340 m/s.</div><h3>3.5 Nepresnosti</h3><p>Kmitňa nie je presne na okraji trubice, ale kúsok nad ním. Účinná dĺžka stĺpca je preto o niečo väčšia (koncová korekcia asi 0,6 polomeru trubice), a rýchlosť zvuku vychádza mierne menšia ako 343 m/s – najmä pri krátkych stĺpcoch. Ďalej sa prejavuje nepresné určenie maxima hlasitosti, teplota vzduchu (rýchlosť zvuku s ňou rastie) a meranie dĺžky.</p>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO30', 'Otázka', 'maturit', 'poznámk'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
