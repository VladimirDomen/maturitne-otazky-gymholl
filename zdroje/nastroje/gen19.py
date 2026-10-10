"""Vzor 19 (bez zdrojového HTML – obsah písaný priamo) -> Vzor19_zadanie.html + Vzor19_vypracovanie.html.
Spustenie: python -I gen19.py <priečinok FYZIKA>"""
import sys, pathlib

DST = pathlib.Path(sys.argv[1])
N = 19
TOPICS = ['Magnetické pole', 'Mechanika tekutín – prúdenie v trubici', 'Merné skupenské teplo topenia ľadu']

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
SIP = lambda x, y, d: (f'M{x - 5} {y - 9}L{x + 5} {y}L{x - 5} {y + 9}' if d == 'r' else f'M{x + 5} {y - 9}L{x - 5} {y}L{x + 5} {y + 9}')

def magnet():
    hore = ''.join(f'M200 124C{200 - k} {c},{360 + k} {c},360 124' for k, c in ((40, 95), (80, 40), (140, -20)))
    dole = ''.join(f'M200 136C{200 - k} {c},{360 + k} {c},360 136' for k, c in ((40, 165), (80, 220), (140, 280)))
    sipky = ''.join(SIP(280, y, 'r') for y in (102, 61, 16, 158, 199, 244))
    return ('<svg class="diagram" viewBox="0 0 560 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Indukčné čiary tyčového magnetu vychádzajú zo severného pólu a vstupujú do južného pólu">'
            f'<g stroke="#637889" stroke-width="1.6" fill="none"><path d="{hore}{dole}M200 130H40M520 130H360"/></g>'
            f'<g stroke="#637889" stroke-width="1.6" fill="none"><path d="{sipky}{SIP(110, 130, "l")}{SIP(450, 130, "l")}"/></g>'
            '<rect x="200" y="115" width="80" height="30" fill="#c0392b"/><rect x="280" y="115" width="80" height="30" fill="#2f6db3"/>'
            '<g font-size="18" fill="#fff" font-weight="bold"><text x="232" y="137">N</text><text x="313" y="137">S</text></g></svg>')

MAGNET = magnet()

def vodice():
    def panel(x1, x2, hore2, f_dnu, popis, px):
        s = (f'<g stroke="#193b59" stroke-width="3" fill="none"><path d="M{x1} 40V190M{x2} 40V190"/>'
             f'<path d="M{x1 - 7} 72L{x1} 58L{x1 + 7} 72"/>'
             + (f'<path d="M{x2 - 7} 72L{x2} 58L{x2 + 7} 72"/>' if hore2 else f'<path d="M{x2 - 7} 58L{x2} 72L{x2 + 7} 58"/>') + '</g>')
        if f_dnu:
            f = f'M{x1} 125H{x1 + 36}M{x1 + 28} 119L{x1 + 38} 125L{x1 + 28} 131M{x2} 125H{x2 - 36}M{x2 - 28} 119L{x2 - 38} 125L{x2 - 28} 131'
            fl = (x1 + 6, x2 - 34)
        else:
            f = f'M{x1} 125H{x1 - 36}M{x1 - 28} 119L{x1 - 38} 125L{x1 - 28} 131M{x2} 125H{x2 + 36}M{x2 + 28} 119L{x2 + 38} 125L{x2 + 28} 131'
            fl = (x1 - 36, x2 + 10)
        return (s + f'<path d="{f}" stroke="#c0392b" stroke-width="2.5" fill="none"/>'
                f'<g font-size="15" fill="#c0392b"><text x="{fl[0]}" y="116">F₁</text><text x="{fl[1]}" y="116">F₂</text></g>'
                f'<g {T}><text x="{x1 + 8}" y="56">I₁</text><text x="{x2 + 8}" y="56">I₂</text></g>'
                f'<text x="{px}" y="220" font-size="14" fill="#637889">{popis}</text>')
    return ('<svg class="diagram" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dva rovnobežné vodiče: pri prúdoch rovnakého smeru sa priťahujú, pri prúdoch opačného smeru sa odpudzujú">'
            + panel(110, 210, True, True, 'rovnaký smer: priťahujú sa', 66)
            + panel(400, 500, False, False, 'opačný smer: odpudzujú sa', 360) + '</svg>')

VODICE = vodice()

def cievka():
    zavity = ''.join(f'<ellipse cx="{x}" cy="115" rx="10" ry="45"/>' for x in range(180, 381, 25))
    vnutri = ''.join(f'M130 {y}H436' for y in (100, 115, 130))
    sip = ''.join(SIP(436, y, 'r') for y in (100, 115, 130))
    von = 'M446 110C506 0,64 0,124 110M446 120C506 230,64 230,124 120'
    return ('<svg class="diagram" viewBox="0 0 560 230" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Indukčné čiary cievky s prúdom: vo vnútri rovnobežné, zvonka sa uzatvárajú ako pri tyčovom magnete">'
            f'<g stroke="#637889" stroke-width="1.6" fill="none"><path d="{vnutri}{von}"/><path d="{sip}{SIP(280, 28, "l")}{SIP(280, 202, "l")}"/></g>'
            f'<g stroke="#b87333" stroke-width="3" fill="none">{zavity}<path d="M180 160V205M380 160V205"/></g>'
            f'<g {T}><text x="458" y="121">N</text><text x="94" y="121">S</text><text x="190" y="205">I</text><text x="390" y="205">I</text></g></svg>')

CIEVKA = cievka()

def lorentz():
    kr = ''.join(f'<g transform="translate({x} {y})"><circle r="7"/><path d="M-4 -4L4 4M-4 4L4 -4"/></g>' for x in range(40, 380, 60) for y in (30, 90, 150))
    return ('<svg class="diagram" viewBox="0 0 400 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kladne nabitá častica v homogénnom magnetickom poli kolmom na nákresňu sa pohybuje po kružnici; Lorentzova sila smeruje do stredu">'
            f'<g stroke="#9fb3c8" stroke-width="1.4" fill="none">{kr}</g>'
            '<circle cx="200" cy="130" r="80" fill="none" stroke="#2f6db3" stroke-width="2" stroke-dasharray="7 5"/>'
            '<path d="M200 130V210" stroke="#637889" stroke-width="1.5" stroke-dasharray="4 4"/>'
            '<g stroke="#26724c" stroke-width="3" fill="none"><path d="M200 210H262M252 203L264 210L252 217"/></g>'
            '<g stroke="#c0392b" stroke-width="3" fill="none"><path d="M200 210V162M193 172L200 160L207 172"/></g>'
            '<circle cx="200" cy="210" r="9" fill="#c0392b"/><text x="194" y="215" font-size="14" fill="#fff">+</text>'
            '<g font-size="15"><text x="268" y="215" fill="#26724c">v</text><text x="208" y="174" fill="#c0392b">F</text><text x="184" y="190" fill="#637889">r</text>'
            '<text x="290" y="252" fill="#193b59">B (do nákresne)</text></g></svg>')

LORENTZ = lorentz()

def trubica(vyp):
    if vyp:
        t1, t2, t3, t4 = 'S₁ = 20 cm²', 'S₂ = 40 cm²', 'v₁ = 8 m/s', 'v₂ = 4 m/s'
    else:
        t1, t2, t3, t4 = 'S₁ = 20 cm²', 'S₂ = 40 cm²', 'v₁ = 8 m/s', 'v₂ = ?'
    return ('<svg class="diagram" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vodorovná trubica: užšia časť s prierezom 20 cm² a rýchlosťou vody 8 m/s prechádza do širšej časti s prierezom 40 cm²">'
            '<path d="M40 80H250L320 60H560V140H320L250 120H40Z" fill="#d6e8f5"/>'
            '<g stroke="#193b59" stroke-width="3" fill="none"><path d="M40 80H250L320 60H560M40 120H250L320 140H560"/></g>'
            '<g stroke="#637889" stroke-width="1.5" stroke-dasharray="5 4" fill="none"><path d="M150 80V120M440 60V140"/></g>'
            '<g stroke="#c0392b" stroke-width="3" fill="none"><path d="M70 100H150M140 93L152 100L140 107M380 100H420M410 93L422 100L410 107"/></g>'
            f'<g {T}><text x="120" y="70">{t1}</text><text x="400" y="50">{t2}</text></g>'
            f'<g font-size="15" fill="#c0392b"><text x="70" y="148">{t3}</text><text x="380" y="168">{t4}</text></g></svg>')

TRUBICA_Z = trubica(False)
TRUBICA_V = trubica(True)

KALORIMETER = ('<svg class="diagram" viewBox="0 0 440 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kalorimeter: vonkajšia a vnútorná nádoba, voda, kúsok ľadu, teplomer a miešačka">'
               '<rect x="60" y="80" width="240" height="200" rx="6" fill="#eef2f6" stroke="#375873" stroke-width="2"/>'
               '<rect x="90" y="100" width="180" height="160" fill="#fff" stroke="#375873" stroke-width="2"/>'
               '<rect x="92" y="140" width="176" height="118" fill="#d6e8f5"/>'
               '<rect x="148" y="146" width="38" height="34" rx="4" fill="#f4fbff" stroke="#7fa6c4" stroke-width="2"/>'
               '<path d="M50 80H310" stroke="#375873" stroke-width="5"/>'
               '<g stroke="#637889" stroke-width="3" fill="none"><path d="M120 30V228"/><ellipse cx="120" cy="232" rx="20" ry="5"/></g>'
               '<rect x="214" y="30" width="12" height="206" rx="6" fill="#fff" stroke="#c0392b" stroke-width="2"/><circle cx="220" cy="240" r="10" fill="#c0392b"/>'
               '<path d="M220 236V150" stroke="#c0392b" stroke-width="4"/>'
               '<g stroke="#637889" stroke-width="1" fill="none"><path d="M232 50H330M188 160H330M270 210H330M300 120H330M130 30H140"/></g>'
               '<g font-size="15" fill="#193b59"><text x="336" y="55">teplomer</text><text x="336" y="165">ľad</text><text x="336" y="215">voda</text>'
               '<text x="336" y="125">kalorimeter</text><text x="146" y="35">miešačka</text></g></svg>')

# ---------- zadanie ----------
Z1 = '''<h2>1. Magnetické pole</h2><div class="task"><ol><li>Opíšte magnetické pole permanentného magnetu. Ako znázorňujeme magnetické pole a čo sú magnetické indukčné čiary?</li><li>Opíšte magnetické pole priameho vodiča s prúdom a cievky. Ako určíme smer indukčných čiar?</li><li>Popíšte vzájomné pôsobenie dvoch rovnobežných vodičov s prúdom, ak majú prúdy rovnaký a ak majú opačný smer.</li><li>Popíšte pôsobenie magnetického poľa na častice s elektrickým nábojom. Kde sa to využíva?</li></ol></div>'''

Z2 = f'''<h2>2. Mechanika tekutín – prúdenie v trubici</h2><div class="task"><ol><li>Vysvetlite pojmy ideálna kvapalina, ustálené prúdenie a prúdnica.</li><li>Definujte objemový a hmotnostný tok a sformulujte rovnicu spojitosti toku.</li><li>Sformulujte Bernoulliho rovnicu.</li></ol><p><strong>Úloha:</strong> Vodorovnou trubicou s prierezom <strong>S₁ = 20 cm²</strong> prúdi voda rýchlosťou <strong>v₁ = 8 m/s</strong>. Tlak vody v tomto mieste je <strong>p₁ = 1,08 · 10⁵ Pa</strong>. Ďalej sa trubica rozširuje na prierez <strong>S₂ = 40 cm²</strong>. Vodu považujte za ideálnu kvapalinu, ρ = 1 000 kg/m³.</p>{TRUBICA_Z}<ol type="a"><li>Vypočítajte objemový tok vody.</li><li>Vypočítajte hmotnostný tok vody.</li><li>Akou rýchlosťou prúdi voda v rozšírenom mieste?</li><li><em>Rozširujúca úloha:</em> Aký je tlak vody v rozšírenom mieste?</li></ol></div>'''

Z3 = '''<h2>3. Experiment – merné skupenské teplo topenia ľadu</h2><div class="task"><p>Experimentálne určte merné skupenské teplo topenia ľadu. Navrhnite pomôcky, postup merania a vyhodnotenie. Zostavte kalorimetrickú rovnicu a vysvetlite pojmy vnútorná energia, práca a teplo, ktoré pri jej odvodení používate.</p></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Magnetické pole</h2><h3>1.1 Magnetické pole permanentného magnetu</h3><p>Permanentný magnet (z ocele, feritu, zliatin neodýmu) vytvára vo svojom okolí <strong>magnetické pole</strong>. Prejavuje sa silovým pôsobením na iné magnety, feromagnetické látky a vodiče s prúdom. Magnet má dva póly – <strong>severný N</strong> a <strong>južný S</strong>. Nesúhlasné póly sa priťahujú, súhlasné odpudzujú. Póly sa nedajú oddeliť: rozlomením magnetu vzniknú dva menšie magnety, každý s oboma pólmi.</p><p>Pole znázorňujeme <strong>magnetickými indukčnými čiarami</strong>. Ich dotyčnica v danom bode má smer osi voľne otočnej magnetky a orientácia čiary je od jej južného k severnému pólu. Indukčné čiary sú <strong>uzavreté</strong> – mimo magnetu vychádzajú zo severného pólu a vstupujú do južného, vo vnútri magnetu pokračujú od S k N. Kde sú čiary hustejšie, je pole silnejšie.</p>{MAGNET}<p>Silové pôsobenie poľa vyjadruje vektorová veličina <strong>magnetická indukcia B</strong> s jednotkou tesla (T). Magnetické pole má aj Zem – jej južný magnetický pól je pri severnom zemepisnom póle, preto severný pól strelky kompasu ukazuje na sever.</p><h3>1.2 Magnetické pole vodiča s prúdom a cievky</h3><p>Okolo každého vodiča s prúdom vzniká magnetické pole (Oerstedov pokus – vodič vychýli magnetku). Indukčné čiary priameho vodiča sú sústredné kružnice v rovinách kolmých na vodič. Ich orientáciu určuje <strong>Ampérovo pravidlo pravej ruky</strong>: ak palec ukazuje smer prúdu, prsty ukazujú orientáciu indukčných čiar. Veľkosť indukcie vo vzdialenosti d od dlhého priameho vodiča:</p><div class="formula">B = μ₀ I / (2π d) &nbsp;&nbsp;&nbsp; μ₀ = 4π · 10⁻⁷ T·m·A⁻¹</div><p><strong>Cievka (solenoid)</strong> s prúdom má pole podobné tyčovému magnetu. Vo vnútri dlhej cievky je pole <strong>homogénne</strong> – indukčné čiary sú rovnobežné:</p><div class="formula">B = μ₀ μᵣ N I / l</div><p>N je počet závitov, l dĺžka cievky a μᵣ relatívna permeabilita jadra. Póly cievky určíme pravidlom pravej ruky: prsty v smere prúdu v závitoch, palec ukazuje severný pól. Feromagnetické jadro pole mnohonásobne zosilní – <strong>elektromagnet</strong>.</p>{CIEVKA}<h3>1.3 Dva rovnobežné vodiče s prúdom</h3><p>Na vodič s prúdom I a dĺžkou l v magnetickom poli s indukciou B pôsobí sila (Flemingovo pravidlo ľavej ruky určuje smer):</p><div class="formula">F = B I l sin α</div><p>Každý z dvoch rovnobežných vodičov sa nachádza v magnetickom poli druhého vodiča, preto na seba pôsobia silami rovnakej veľkosti a opačného smeru (zákon akcie a reakcie):</p><div class="formula">F = μ₀ I₁ I₂ l / (2π d)</div>{VODICE}<ul><li>prúdy <strong>rovnakého smeru</strong> – vodiče sa <strong>priťahujú</strong>,</li><li>prúdy <strong>opačného smeru</strong> – vodiče sa <strong>odpudzujú</strong>.</li></ul><p>Sila je úmerná súčinu prúdov a nepriamo úmerná vzdialenosti vodičov. Na tomto pôsobení bola pôvodne založená definícia ampéra.</p><h3>1.4 Pôsobenie magnetického poľa na nabité častice</h3><p>Na časticu s nábojom Q, ktorá sa pohybuje rýchlosťou v v magnetickom poli, pôsobí <strong>Lorentzova (magnetická) sila</strong>:</p><div class="formula">F<sub>m</sub> = Q v B sin α</div><p>α je uhol medzi rýchlosťou a indukciou. Sila je kolmá na rýchlosť aj na indukciu, preto mení len smer rýchlosti, nie jej veľkosť – nekoná prácu. Na časticu, ktorá sa pohybuje v smere indukčných čiar, pole nepôsobí. Ak častica vletí kolmo na indukčné čiary homogénneho poľa, pohybuje sa po <strong>kružnici</strong>. Lorentzova sila je silou dostredivou:</p>{LORENTZ}<div class="formula">Q v B = m v²/r &nbsp;&nbsp; → &nbsp;&nbsp; r = m v / (Q B)</div><p><strong>Využitie a prejavy:</strong> hmotnostný spektrometer (oddelenie izotopov podľa polomeru dráhy), cyklotrón a iné urýchľovače, vychyľovanie elektrónového zväzku v starších obrazovkách, Hallova sonda na meranie indukcie. Magnetické pole Zeme odkláňa nabité častice slnečného vetra – pri póloch vzniká <strong>polárna žiara</strong>.</p><div class="result"><strong>Zhrnutie:</strong> Zdrojom magnetického poľa sú magnety a pohybujúce sa náboje (prúdy). Pole pôsobí na vodiče s prúdom silou F = BIl sin α a na pohybujúce sa nabité častice Lorentzovou silou F = QvB sin α. Rovnobežné vodiče s prúdmi rovnakého smeru sa priťahujú, s opačnými sa odpudzujú.</div>'''

V2 = f'''<h2>2. Mechanika tekutín – prúdenie v trubici</h2><h3>2.1 Ideálna kvapalina a prúdenie</h3><p><strong>Ideálna kvapalina</strong> je dokonale tekutá (bez vnútorného trenia) a nestlačiteľná. Pri <strong>ustálenom prúdení</strong> sa rýchlosť v danom mieste nemení s časom. <strong>Prúdnica</strong> je čiara, ktorej dotyčnica v každom bode má smer rýchlosti pohybujúcej sa častice. Prúdnice sa nepretínajú.</p><h3>2.2 Objemový a hmotnostný tok, rovnica spojitosti</h3><p><strong>Objemový tok</strong> je objem kvapaliny, ktorý pretečie prierezom trubice za jednotku času. <strong>Hmotnostný tok</strong> je hmotnosť kvapaliny, ktorá pretečie za jednotku času:</p><div class="formula">Q<sub>V</sub> = V/t = S v &nbsp;[m³·s⁻¹] &nbsp;&nbsp;&nbsp; Q<sub>m</sub> = m/t = ρ S v &nbsp;[kg·s⁻¹]</div><p>Ideálna kvapalina sa nikde nehromadí ani neubúda, preto každým prierezom trubice pretečie za rovnaký čas rovnaký objem – <strong>rovnica spojitosti toku</strong>:</p><div class="formula">S₁ v₁ = S₂ v₂ = konšt.</div><p>V užšom mieste prúdi kvapalina rýchlejšie, v širšom pomalšie.</p><h3>2.3 Bernoulliho rovnica</h3><p>Zo zákona zachovania mechanickej energie pre vodorovnú trubicu vyplýva, že súčet kinetickej energie objemovej jednotky kvapaliny a tlakovej potenciálnej energie objemovej jednotky je stály:</p><div class="formula">½ ρ v₁² + p₁ = ½ ρ v₂² + p₂</div><p>Kde kvapalina prúdi rýchlejšie, je v nej menší tlak (hydrodynamický paradox). Využíva sa vo vodnej vývevke, rozprašovači, karburátore, pri meraní rýchlosti prúdenia (Venturiho trubica) a vysvetľuje vztlak krídla lietadla.</p><h3>2.4 Riešenie úlohy</h3><p>Zadané: S₁ = 20 cm² = 2 · 10⁻³ m², v₁ = 8 m/s, S₂ = 40 cm² = 4 · 10⁻³ m², p₁ = 1,08 · 10⁵ Pa, ρ = 1 000 kg/m³.</p>{TRUBICA_V}<p><strong>a)</strong> Objemový tok:</p><div class="formula">Q<sub>V</sub> = S₁ v₁ = 2 · 10⁻³ m² · 8 m/s = 1,6 · 10⁻² m³/s = 16 l/s</div><p><strong>b)</strong> Hmotnostný tok:</p><div class="formula">Q<sub>m</sub> = ρ Q<sub>V</sub> = 1 000 kg/m³ · 1,6 · 10⁻² m³/s = 16 kg/s</div><p><strong>c)</strong> Z rovnice spojitosti toku:</p><div class="formula">v₂ = S₁ v₁ / S₂ = 20 cm² · 8 m/s / 40 cm² = 4 m/s</div><p>Prierez sa zdvojnásobil, preto sa rýchlosť zmenšila na polovicu. Objemový aj hmotnostný tok sú v rozšírenom mieste rovnaké ako v užšom.</p><p><strong>d)</strong> <em>Rozširujúca úloha</em> – z Bernoulliho rovnice:</p><div class="formula">p₂ = p₁ + ½ ρ (v₁² − v₂²) = 1,08 · 10⁵ Pa + ½ · 1 000 · (8² − 4²) Pa<br>p₂ = 1,08 · 10⁵ Pa + 0,24 · 10⁵ Pa = 1,32 · 10⁵ Pa</div><p>V širšom mieste voda prúdi pomalšie, a preto je v nej väčší tlak.</p><div class="result"><strong>Q<sub>V</sub> = 1,6 · 10⁻² m³/s = 16 l/s; Q<sub>m</sub> = 16 kg/s; v₂ = 4 m/s; p₂ = 1,32 · 10⁵ Pa.</strong></div>'''

V3 = f'''<h2>3. Experiment – merné skupenské teplo topenia ľadu</h2><h3>3.1 Teoretický základ</h3><p><strong>Vnútorná energia U</strong> telesa je súčet kinetických energií neusporiadaného pohybu jeho častíc a potenciálnych energií ich vzájomného pôsobenia. Vnútornú energiu môžeme zmeniť dvoma spôsobmi:</p><ul><li><strong>konaním práce W</strong> – napr. trením, stláčaním plynu,</li><li><strong>tepelnou výmenou</strong> – teleso s vyššou teplotou odovzdá časť vnútornej energie telesu s nižšou teplotou. Energia odovzdaná takto sa volá <strong>teplo Q</strong>.</li></ul><p>Obe spôsoby spája 1. termodynamický zákon: ΔU = W + Q. Teplo potrebné na zmenu teploty telesa a teplo potrebné na roztopenie telesa s teplotou topenia:</p><div class="formula">Q = m c Δt &nbsp;&nbsp;&nbsp; L<sub>t</sub> = m l<sub>t</sub></div><p><strong>Merné skupenské teplo topenia l<sub>t</sub></strong> je teplo potrebné na roztopenie 1 kg látky pri teplote topenia [J·kg⁻¹]. Pri topení sa teplota nemení, dodaná energia zväčšuje potenciálnu energiu častíc (rozrušuje kryštálovú mriežku).</p><p>V tepelne izolovanej sústave (kalorimetri) platí <strong>kalorimetrická rovnica</strong>: teplo odovzdané teplejšími telesami sa rovná teplu prijatému chladnejšími telesami.</p><h3>3.2 Pomôcky</h3><p>Kalorimeter s miešačkou (so známou tepelnou kapacitou C alebo ju určíme vopred), teplomer s delením 0,1 °C alebo 0,5 °C, digitálna váha, teplá voda (asi 30 °C), kúsky ľadu z mrazničky, ktoré necháme nahriať na 0 °C (začnú sa topiť), papierová utierka.</p><h3>3.3 Usporiadanie</h3>{KALORIMETER}<h3>3.4 Postup</h3><ol><li>Odvážime prázdnu vnútornú nádobu kalorimetra, nalejeme vodu a znovu odvážime – určíme hmotnosť vody m₁.</li><li>Po premiešaní zmeriame počiatočnú teplotu vody t₁.</li><li>Kúsky ľadu s teplotou 0 °C osušíme utierkou (voda na povrchu by skreslila výsledok) a hneď vložíme do kalorimetra. Kalorimeter zakryjeme.</li><li>Miešame a sledujeme teplotu. Keď sa všetok ľad roztopí, zapíšeme najnižšiu ustálenú teplotu t.</li><li>Kalorimeter s vodou znovu odvážime. Z rozdielu hmotností určíme hmotnosť ľadu m₂.</li><li>Meranie zopakujeme aspoň dvakrát a výsledky spriemerujeme.</li></ol><h3>3.5 Kalorimetrická rovnica a vyhodnotenie</h3><p>Teplá voda a kalorimeter odovzdajú teplo. Ľad ho prijme najprv na roztopenie (pri 0 °C) a potom voda z ľadu na ohriatie z 0 °C na t:</p><div class="formula">(m₁ c + C)(t₁ − t) = m₂ l<sub>t</sub> + m₂ c (t − 0 °C)</div><div class="formula">l<sub>t</sub> = [(m₁ c + C)(t₁ − t) − m₂ c t] / m₂</div><p class="subtle">Nasledujúce čísla sú modelové údaje; nejde o skutočné meranie. c = 4 180 J·kg⁻¹·K⁻¹.</p><table><tr><th>m₁ (kg)</th><th>t₁ (°C)</th><th>C (J/K)</th><th>m₂ (kg)</th><th>t (°C)</th></tr><tr><td>0,200</td><td>30,0</td><td>80</td><td>0,040</td><td>13,0</td></tr></table><div class="formula">odovzdané teplo: (0,200 · 4 180 + 80) J/K · 17,0 K = 916 · 17,0 J ≈ 15 570 J<br>ohriatie vody z ľadu: 0,040 · 4 180 · 13,0 J ≈ 2 170 J<br>l<sub>t</sub> = (15 570 − 2 170) J / 0,040 kg ≈ 3,35 · 10⁵ J/kg = 335 kJ/kg</div><p>Tabuľková hodnota je 334 kJ/kg – výsledok dobre súhlasí.</p><h3>3.6 Zdroje nepresností</h3><ul><li><strong>Tepelná výmena s okolím</strong> – kalorimeter nie je dokonale izolovaný. Preto volíme t₁ približne o toľko nad teplotou okolia, o koľko bude t pod ňou – straty a zisky sa čiastočne vyrovnajú.</li><li><strong>Voda na povrchu ľadu</strong> – zväčší m₂ bez toho, aby spotrebovala skupenské teplo; výsledok by vyšiel menší.</li><li><strong>Ľad s teplotou pod 0 °C</strong> – časť tepla by sa spotrebovala na jeho ohriatie; výsledok by vyšiel väčší.</li><li>Presnosť teplomera a váhy, zanedbanie tepelnej kapacity teplomera a miešačky.</li></ul><div class="result"><strong>Záver:</strong> Z kalorimetrickej rovnice (m₁c + C)(t₁ − t) = m₂l<sub>t</sub> + m₂ct vychádza merné skupenské teplo topenia ľadu približne 335 kJ/kg (tabuľková hodnota 334 kJ/kg).</div>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO19', 'Otázka', 'maturit'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
