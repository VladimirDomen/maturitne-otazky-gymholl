"""MO5_Dynamika.html (zdroje) -> Vzor5_zadanie.html + Vzor5_vypracovanie.html (FYZIKA).
Pôvodne 4 časti; teória a výpočet z dynamiky sú spojené do časti 1 (formát 3 častí).
Opravy: graf toku Φ(t) v mierke (8·10⁻³ bolo nakreslené vo výške 6·10⁻³),
v zadaní indukcie „pre zvolenú orientáciu“ (orientácia na obrázku nie je),
doplnená schéma jadrovej elektrárne (zadanie sa na obrázok odvoláva, v origináli chýbal).
Spustenie (z priečinka MATURITNE_OTAZKY): python -I zdroje/nastroje/gen5.py"""
import pathlib

DST = pathlib.Path('FYZIKA')
N = 5
TOPICS = ['Dynamika', 'Elektromagnetická indukcia', 'Jadrová elektráreň']

def page(kind, parts):
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
<title>Vzor {N} – {label}</title>
<link rel="stylesheet" href="mo.css">
</head>
<body class="{'vyp' if vyp else 'zad'}">

<header class="mo-head"><div class="mo-head-in">
<div class="mo-kicker"><span class="mo-num">VZOR {N}</span><span class="mo-kind">{label}</span></div>
<h1>{' · '.join(TOPICS)}</h1>
<p>{sub}</p>
</div></header>

<nav class="mo-bar"><div class="mo-bar-in">
<a class="mo-back" href="index.html">← Všetky vzory</a>
<div class="mo-switch"><a href="Vzor{N}_zadanie.html"{z_on}>Zadanie</a><a href="Vzor{N}_vypracovanie.html"{v_on}>Vypracovanie</a></div>
<button type="button" onclick="window.print()">Tlačiť / PDF</button>
<a class="mo-lang" href="en/Model{N}_{'solutions' if vyp else 'questions'}.html" hreflang="en" title="English version">EN</a>
</div></nav>

<main class="wrap">
{body}
</main>

<footer class="mo-foot"><a href="index.html">← Všetky vzory</a><span>Vzor {N} · {label}</span></footer>
<script src="mo.js"></script>
</body>
</html>
'''

# ---------- graf toku Φ(t) v mierke: 0 → y 267, 8·10⁻³ Wb → y 70 ----------
def y_fi(mwb):
    return 267 - (267 - 70) * mwb / 8
GRID = ' '.join(f'M98 {y_fi(k):.2f}H680' for k in (2, 4, 6, 8)) + ' M280 55V267 M462 55V267 M644 55V267'
SVG_TOK = (
    '<svg class="graph" viewBox="0 0 760 330" role="img" aria-label="Graf magnetického toku: od 0 do 0,01 s konštantný 0,002 Wb; od 0,01 do 0,02 s rastie lineárne na 0,008 Wb; od 0,02 do 0,03 s konštantný 0,008 Wb.">'
    f'<g stroke="#e4ebf1" stroke-width="1"><path d="{GRID}"/></g>'
    '<g stroke="#1c3043" stroke-width="2.5" fill="none"><path d="M98 47V267H698"/><path d="M91 57L98 42L105 57 M687 260L701 267L687 274"/></g>'
    '<g font-family="Arial" fill="#172f45" font-size="19"><text x="27" y="35">Φ (Wb)</text><text x="692" y="298">t (s)</text><text x="86" y="273" text-anchor="end">0</text>'
    + ''.join(f'<text x="86" y="{y_fi(k) + 6:.2f}" text-anchor="end">{k}·10⁻³</text>' for k in (2, 4, 6, 8)) +
    '<text x="280" y="298" text-anchor="middle">0,01</text><text x="462" y="298" text-anchor="middle">0,02</text><text x="644" y="298" text-anchor="middle">0,03</text></g>'
    f'<path d="M98 {y_fi(2):.2f}H280L462 {y_fi(8):.2f}H644" fill="none" stroke="#17669b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    f'<g fill="#17669b"><circle cx="280" cy="{y_fi(2):.2f}" r="5"/><circle cx="462" cy="{y_fi(8):.2f}" r="5"/></g></svg>')

SVG_NAPATIE = '''<svg class="graph" viewBox="0 0 760 300" role="img" aria-label="Riešenie: indukované napätie je nula do 0,01 s, mínus 0,6 voltu do 0,02 s a opäť nula do 0,03 s."><g stroke="#e4ebf1" stroke-width="1"><path d="M98 75H680 M98 145H680 M98 235H680 M280 48V245 M462 48V245 M644 48V245"/></g><path d="M98 43V250 M98 145H698" stroke="#1c3043" stroke-width="2.5" fill="none"/><g font-family="Arial" fill="#172f45" font-size="19"><text x="29" y="35">uᵢ (V)</text><text x="690" y="174">t (s)</text><text x="86" y="151" text-anchor="end">0</text><text x="86" y="242" text-anchor="end">−0,6</text><text x="280" y="280" text-anchor="middle">0,01</text><text x="462" y="280" text-anchor="middle">0,02</text><text x="644" y="280" text-anchor="middle">0,03</text></g><path d="M98 145H280 V235 H462 V145 H644" fill="none" stroke="#a43c36" stroke-width="4" stroke-linejoin="round"/><g fill="#fff" stroke="#a43c36" stroke-width="2"><circle cx="280" cy="235" r="3"/><circle cx="462" cy="235" r="3"/></g></svg>'''

# ---------- schéma jadrovej elektrárne (VVER) s číslami; legenda je v texte ----------
def cislo(x, y, n):
    return f'<circle cx="{x}" cy="{y}" r="12" fill="#152c4d"/><text x="{x}" y="{y + 5}" text-anchor="middle" font-size="14" font-weight="700" fill="#fff">{n}</text>'
SVG_JE = ('<svg class="diagram" viewBox="0 0 720 340" role="img" aria-label="Zjednodušená schéma jadrovej elektrárne s tlakovodným reaktorom" style="max-width:720px">'
    # ochranná obálka (kontajnment)
    '<path d="M30 305 V125 A125 95 0 0 1 280 125 V305 Z" fill="#f3f6f9" stroke="#8ca0b3" stroke-width="3"/>'
    # primárny okruh: horúca a studená vetva
    '<path d="M135 185 H205" stroke="#d0412f" stroke-width="7" fill="none"/>'
    '<path d="M205 262 H135" stroke="#e08a3c" stroke-width="7" fill="none"/><circle cx="170" cy="262" r="11" fill="#fff" stroke="#e08a3c" stroke-width="3"/>'
    # reaktor s palivom a regulačnými tyčami
    '<rect x="70" y="150" width="65" height="130" rx="26" fill="#fde8d8" stroke="#b5532d" stroke-width="3"/>'
    + ''.join(f'<line x1="{x}" y1="200" x2="{x}" y2="262" stroke="#d4842a" stroke-width="4"/>' for x in (86, 96, 106, 116, 126) if x < 127) +
    '<line x1="96" y1="112" x2="96" y2="215" stroke="#33414f" stroke-width="4"/><line x1="112" y1="112" x2="112" y2="215" stroke="#33414f" stroke-width="4"/>'
    # parogenerátor
    '<rect x="205" y="135" width="52" height="150" rx="24" fill="#fff" stroke="#375873" stroke-width="3"/>'
    + ''.join(f'<path d="M215 {y} q8 -8 16 0 t16 0" fill="none" stroke="#d0412f" stroke-width="2"/>' for y in (175, 195, 215, 235)) +
    # sekundárny okruh: para do turbíny, napájacia voda späť
    '<path d="M231 135 V88 H340" stroke="#9aa9b8" stroke-width="7" fill="none"/>'
    '<path d="M345 245 H300 V300 H231 V285" stroke="#2f6db3" stroke-width="5" fill="none"/><circle cx="300" cy="272" r="10" fill="#fff" stroke="#2f6db3" stroke-width="3"/>'
    # turbína, hriadeľ, generátor
    '<path d="M340 68 V108 L425 126 V50 Z" fill="#dfe7ef" stroke="#375873" stroke-width="3"/>'
    '<line x1="425" y1="88" x2="458" y2="88" stroke="#375873" stroke-width="5"/>'
    '<circle cx="486" cy="88" r="28" fill="#fff7e6" stroke="#a8721f" stroke-width="3"/>'
    '<path d="M514 88 H556 M548 80 L558 88 L548 96" stroke="#a8721f" stroke-width="3" fill="none"/>'
    # kondenzátor
    '<path d="M383 118 V200" stroke="#9aa9b8" stroke-width="7"/>'
    '<rect x="345" y="200" width="100" height="58" rx="6" fill="#e3f0fa" stroke="#375873" stroke-width="3"/>'
    # chladiaca voda a chladiaca veža
    '<path d="M445 215 H590 M598 250 H445" stroke="#2fa0b5" stroke-width="5" fill="none"/>'
    '<path d="M570 300 C598 238 598 196 582 140 H664 C648 196 648 238 676 300 Z" fill="#eef2f5" stroke="#6d8490" stroke-width="3"/>'
    '<path d="M600 128 c-14 -6 -6 -24 10 -18 c4 -16 26 -14 28 0 c16 -4 22 16 8 20 Z" fill="#fff" stroke="#b7c4cf" stroke-width="2"/>'
    + cislo(102, 300, 1) + cislo(130, 112, 2) + cislo(170, 170, 3) + cislo(231, 300, 4) + cislo(382, 88, 5)
    + cislo(486, 88, 6) + cislo(395, 229, 7) + cislo(623, 245, 8) + cislo(52, 150, 9) + cislo(290, 70, 10) +
    '</svg>')
LEGENDA = ('<p class="caption">1&nbsp;reaktor · 2&nbsp;regulačné tyče · 3&nbsp;primárny okruh · 4&nbsp;parogenerátor · 5&nbsp;turbína · '
           '6&nbsp;generátor · 7&nbsp;kondenzátor · 8&nbsp;chladiaca veža · 9&nbsp;ochranná obálka (kontajnment) · 10&nbsp;sekundárny okruh (para)</p>')

# ---------- zadanie ----------
Z = [
'''<h2>1. Dynamika</h2>
<h3>Teoretická časť</h3>
<div class="task"><p>Vysvetlite vzájomné pôsobenie telies a pojem <strong>izolovaná sústava</strong>.</p>
<p>Sformulujte a vysvetlite <strong>Newtonove pohybové zákony</strong>. Definujte hybnosť telesa a vysvetlite <strong>zákon zachovania hybnosti</strong>.</p>
<p>Charakterizujte <strong>dostredivú silu</strong>, určte jej smer a uveďte vzťah na výpočet jej veľkosti.</p>
</div>
<h3>Výpočtová úloha – pohyb vlečky</h3>
<div class="task"><p>Vlečka s hmotnosťou <strong>2 000 kg</strong> sa pohybuje po vodorovnej ceste. Vodorovne ju tlačia <strong>štyria robotníci</strong>, každý silou <strong>500 N</strong>, všetci rovnakým smerom.</p>
<p><strong>a)</strong> Vypočítajte zrýchlenie vlečky, ak odporové sily zanedbáme.</p>
<p><strong>b) Rozšírenie:</strong> Určte zrýchlenie, ak proti pohybu pôsobí celková odporová sila <strong>400 N</strong>.</p>
</div>''',
f'''<h2>2. Elektromagnetická indukcia</h2>
<h3>Grafická úloha</h3>
<div class="task"><p>Graf znázorňuje časový priebeh magnetického toku <strong>Φ</strong> cez plochu uzavretého vodiča (jedného závitu). <strong>Nakreslite graf indukovaného napätia u<sub>i</sub> v závislosti od času.</strong> Určte jeho hodnotu v jednotlivých časových intervaloch pre zvolenú orientáciu závitu.</p>
</div>
{SVG_TOK}
<p class="caption">Daný priebeh magnetického toku Φ(t).</p>''',
f'''<h2>3. Jadrová elektráreň</h2>
<div class="task"><p>Podľa obrázka jadrovej elektrárne <strong>Jaslovské Bohunice</strong> opíšte hlavné časti elektrárne a vysvetlite princíp jej činnosti.</p>
</div>
{SVG_JE}
{LEGENDA}''',
]

# ---------- vypracovanie ----------
V = [
'''<h2>1. Dynamika</h2>
<h3>Vzájomné pôsobenie telies a izolovaná sústava</h3>
<p>Telesá na seba pôsobia silami. Sila opisuje vzájomné pôsobenie telies; môže meniť pohybový stav alebo spôsobovať deformáciu. <strong>Izolovaná sústava</strong> je model sústavy, na ktorú nepôsobí výsledná vonkajšia sila (resp. vonkajšie pôsobenia možno zanedbať). Vtedy zostáva celková hybnosť sústavy zachovaná.</p>
<h3>Newtonove pohybové zákony</h3>
<p><strong>I. Zákon zotrvačnosti:</strong> V inerciálnej vzťažnej sústave teleso zostáva v pokoji alebo v rovnomernom priamočiarom pohybe, ak je výsledná sila pôsobiaca naň nulová.</p>
<p><strong>II. Zákon sily:</strong> Výsledná sila je rovná časovej zmene hybnosti. Pri konštantnej hmotnosti platí:</p>
<div class="formula">Σ<strong>F</strong> = m<strong>a</strong></div>
<p><strong>III. Zákon akcie a reakcie:</strong> Ak teleso A pôsobí na teleso B silou, teleso B pôsobí súčasne na A rovnako veľkou, opačne orientovanou silou. Sily pôsobia na <em>rôzne telesá</em>, a preto sa navzájom nerušia na jednom telese.</p>
<h3>Hybnosť a zákon zachovania hybnosti</h3>
<div class="formula"><strong>p</strong> = m<strong>v</strong> &nbsp;&nbsp; [p] = kg·m/s</div>
<p>Ak je výslednica vonkajších síl na sústavu nulová, jej celková vektorová hybnosť sa nemení:</p>
<div class="formula">Σ<strong>p</strong><sub>pred</sub> = Σ<strong>p</strong><sub>po</sub></div>
<h3>Dostredivá sila</h3>
<p>Pri pohybe po kružnici smeruje výsledná radiálna zložka sily vždy <strong>do stredu kružnice</strong>. Nejde o novú osobitnú silu; dostredivú silu môže zabezpečovať napríklad trenie, napätie vlákna alebo gravitačná sila.</p>
<div class="formula">F<sub>d</sub> = m v² / r = m ω²r</div>
<h3>Výpočtová úloha – vlečka</h3>
<p><strong>Dané:</strong> m = 2 000 kg, n = 4, sila jedného robotníka F₁ = 500 N.</p>
<p>Keďže všetci tlačia rovnakým smerom, sily sčítame:</p>
<div class="formula">F = 4 · 500 = 2 000 N</div>
<h4>a) Bez odporových síl</h4>
<div class="formula">a = F / m = 2 000 / 2 000 = <strong>1 m/s²</strong></div>
<div class="result">Odpoveď: Zrýchlenie vlečky je 1 m/s².</div>
<h4>b) S odporovou silou 400 N (rozšírenie)</h4>
<div class="formula">F<sub>výsl.</sub> = 2 000 − 400 = 1 600 N</div>
<div class="formula">a = 1 600 / 2 000 = <strong>0,8 m/s²</strong></div>
<div class="result">Odpoveď: Pri odporovej sile 400 N je zrýchlenie 0,8 m/s².</div>''',
f'''<h2>2. Elektromagnetická indukcia</h2>
{SVG_TOK}
<p class="caption">Daný priebeh magnetického toku Φ(t).</p>
<p>Pre jeden závit platí Faradayov zákon:</p>
<div class="formula">u<sub>i</sub> = − ΔΦ / Δt</div>
<p><strong>0 až 0,01 s:</strong> magnetický tok je konštantný, preto u<sub>i</sub> = 0 V.</p>
<p><strong>0,01 až 0,02 s:</strong> tok rastie lineárne z 2·10⁻³ Wb na 8·10⁻³ Wb:</p>
<div class="formula">u<sub>i</sub> = −(8−2)·10⁻³ / (0,02−0,01) = <strong>−0,6 V</strong></div>
<p><strong>0,02 až 0,03 s:</strong> tok je konštantný, preto u<sub>i</sub> = 0 V.</p>
{SVG_NAPATIE}
<p class="caption">Priebeh uᵢ(t). Zvislé prechody označujú skoky medzi intervalmi; hodnota presne v bodoch zlomu pri ideálnom grafe nie je podstatná.</p>
<p class="subtle">Znamienko závisí od zvolenej orientácie obiehania závitu. Bez určenej orientácie je fyzikálne jednoznačná veľkosť 0,6 V počas rastu magnetického toku, nie absolútne znamienko.</p>''',
f'''<h2>3. Jadrová elektráreň</h2>
{SVG_JE}
{LEGENDA}
<p>Elektráreň s tlakovodným reaktorom premieňa energiu uvoľnenú pri štiepení jadier na elektrickú energiu. Hlavné časti a postup:</p>
<ul><li><strong>Reaktor:</strong> v palive prebieha riadená štiepna reťazová reakcia. Regulačné tyče riadia výkon; voda slúži ako chladivo a moderátor.</li>
<li><strong>Primárny okruh:</strong> horúca voda pod vysokým tlakom odoberá teplo z reaktora a vedie ho do parogenerátora; za normálnych podmienok sa v reaktore nevarí.</li>
<li><strong>Parogenerátor:</strong> prenáša teplo z primárneho do oddeleného sekundárneho okruhu, v ktorom vzniká para.</li>
<li><strong>Turbína a generátor:</strong> para roztáča turbínu; generátor premieňa mechanickú energiu na elektrickú.</li>
<li><strong>Kondenzátor a chladiaci okruh:</strong> po prechode turbínou sa para ochladí a skondenzuje. Voda sa vracia do sekundárneho okruhu. Chladiace veže odvádzajú odpadové teplo do okolitého prostredia.</li>
<li><strong>Bezpečnostné systémy:</strong> obmedzujú riziká a zabezpečujú odstavenie a chladenie reaktora.</li>
</ul>
<div class="formula" style="font-size:18px">jadrová energia → tepelná energia → mechanická energia → elektrická energia</div>
<p class="subtle">Pri opise konkrétneho obrázka označte tie časti, ktoré sú na ňom skutočne zakreslené.</p>''',
]

for name, html in (('zadanie', page('zad', Z)), ('vypracovanie', page('vyp', V))):
    for bad in ('ekonštru', 'rukopis', 'MO5', 'MO 5', 'maturit', 'prekreslen', 'poznámk', 'fotograf', 'pôvodn'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
