"""Vzor 20 zo zdrojov MO20_zadanie.html + MO20_riesenie.html a fotky 20 (text prepísaný a doplnený, obrázky prekreslené)
-> Vzor20_zadanie.html + Vzor20_vypracovanie.html.
Spustenie: python -I gen20.py <priečinok FYZIKA>"""
import sys, pathlib

DST = pathlib.Path(sys.argv[1])
N = 20
TOPICS = ['Elektromagnetická indukcia', 'Gravitačné pole', 'Povrchové napätie z kapilárnej elevácie']

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
KRIZIK = lambda x, y: f'<g transform="translate({x} {y})"><circle r="8"/><path d="M-4.5 -4.5L4.5 4.5M-4.5 4.5L4.5 -4.5"/></g>'

def vodic(vyp):
    kr = ''.join(KRIZIK(x, y) for x in range(50, 600, 70) for y in (34, 186))
    ui = 'Uᵢ = 0,01 V' if vyp else 'Uᵢ = 0,01 V'
    vv = 'v = 0,5 m/s' if vyp else 'v = ?'
    return ('<svg class="diagram" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Priamy vodič dĺžky 20 cm sa pohybuje rýchlosťou v kolmo na indukčné čiary homogénneho magnetického poľa smerujúceho do nákresne">'
            '<rect x="10" y="10" width="580" height="200" rx="8" fill="#f3f7fb" stroke="#bccbdc"/>'
            f'<g stroke="#9fb3c8" stroke-width="1.4" fill="none">{kr}</g>'
            '<path d="M220 60V160" stroke="#b87333" stroke-width="9" stroke-linecap="round"/>'
            '<g stroke="#c0392b" stroke-width="3" fill="none"><path d="M234 110H340M328 103L342 110L328 117"/></g>'
            '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M190 60V160M184 60H196M184 160H196"/></g>'
            '<g fill="#193b59" font-size="13"><text x="226" y="58">+</text><text x="228" y="172">−</text></g>'
            f'<g {T}><text x="120" y="115">l = 20 cm</text><text x="350" y="116" fill="#c0392b">{vv}</text><text x="420" y="78">B = 0,1 T</text>'
            f'<text x="250" y="160">{ui}</text><text x="420" y="152" font-size="13" fill="#637889">B do nákresne</text></g></svg>')

VODIC_Z = vodic(False)
VODIC_V = vodic(True)

LENZ = ('<svg class="diagram" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Magnet sa severným pólom približuje k cievke; indukovaný prúd vytvorí v cievke severný pól oproti magnetu, ktorý ho odpudzuje">'
        '<rect x="40" y="80" width="70" height="36" fill="#2f6db3"/><rect x="110" y="80" width="70" height="36" fill="#c0392b"/>'
        '<g font-size="18" font-weight="bold" fill="#fff"><text x="68" y="105">S</text><text x="138" y="105">N</text></g>'
        '<g stroke="#193b59" stroke-width="2.5" fill="none"><path d="M120 140H200M190 134L202 140L190 146"/></g>'
        + '<g stroke="#b87333" stroke-width="3" fill="none">' + ''.join(f'<ellipse cx="{x}" cy="98" rx="9" ry="40"/>' for x in range(280, 421, 20)) + '<path d="M280 138V175H520V150M420 58V44H520V110"/></g>'
        '<circle cx="520" cy="130" r="20" fill="#fff" stroke="#193b59" stroke-width="2.5"/><text x="512" y="136" font-size="16" fill="#193b59">G</text>'
        '<g font-size="15"><text x="140" y="160" fill="#193b59">v</text><text x="244" y="60" fill="#c0392b">N</text><text x="434" y="150" fill="#2f6db3">S</text></g>'
        '<g stroke="#c0392b" stroke-width="2" fill="none"><path d="M262 98H214M224 92L212 98L224 104"/></g>'
        '<text x="150" y="22" font-size="13" fill="#637889">indukovaný prúd vytvorí pól, ktorý magnet odpudzuje</text></svg>')

def telesa():
    return ('<svg class="diagram" viewBox="0 0 650 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Dve telesá sa navzájom gravitačne priťahujú silami s veľkosťou 12 N; vzdialenosť ich stredov je r">'
            '<circle cx="120" cy="64" r="30" fill="#d6e7f5" stroke="#2f6db3" stroke-width="2"/><circle cx="520" cy="64" r="38" fill="#dbe9e2" stroke="#427866" stroke-width="2"/>'
            '<g stroke="#2f6db3" stroke-width="3" fill="none"><path d="M152 64H262M250 57L264 64L250 71"/></g>'
            '<g stroke="#427866" stroke-width="3" fill="none"><path d="M480 64H370M382 57L368 64L382 71"/></g>'
            '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M120 120H520M120 113V127M520 113V127"/></g>'
            f'<g {T}><text x="108" y="70">m₁</text><text x="508" y="70">m₂</text><text x="314" y="142">r</text>'
            '<text x="168" y="96">F₁ = 12 N</text><text x="380" y="96">F₂ = 12 N</text></g></svg>')

TELESA = telesa()

def graf_f():
    X = lambda q: 70 + 140 * q
    Y = lambda f: 250 - 4 * f
    pts = ' '.join(f'{X(q / 100):.1f},{Y(12 / (q / 100) ** 2):.1f}' for q in range(49, 301, 3))
    body = ''.join(f'<circle cx="{X(q):.0f}" cy="{Y(f):.0f}" r="5" fill="#c0392b"/>' for q, f in ((0.5, 48), (1, 12), (2, 3)))
    return ('<svg class="diagram" viewBox="0 0 520 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graf gravitačnej sily od vzdialenosti: pri vzdialenosti r je sila 12 N, pri r/2 je 48 N, pri 2r je 3 N">'
            '<g stroke="#e3eaf1" stroke-width="1"><path d="M70 202H480M70 154H480M70 106H480M70 58H480M140 250V40M210 250V40M350 250V40M490 250V40"/></g>'
            '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M70 262V25M60 250H500M64 37L70 25L76 37M488 244L500 250L488 256"/></g>'
            f'<polyline points="{pts}" fill="none" stroke="#2f6db3" stroke-width="3"/>{body}'
            '<g stroke="#637889" stroke-width="1.2" stroke-dasharray="4 4" fill="none"><path d="M70 58H140V250M70 202H210V250M70 238H350V250"/></g>'
            '<g font-size="14" fill="#253d51"><text x="40" y="63">48</text><text x="40" y="207">12</text><text x="48" y="242">3</text>'
            '<text x="128" y="270">r/2</text><text x="206" y="270">r</text><text x="340" y="270">2r</text><text x="484" y="270">3r</text>'
            '<text x="80" y="22">F (N)</text><text x="496" y="228">r</text></g>'
            '<text x="250" y="110" font-size="15" fill="#2f6db3">F ~ 1/r²</text></svg>')

GRAF_F = graf_f()

KAPILARA = ('<svg class="diagram" viewBox="0 0 600 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Voda vystúpi v tenkej sklenenej kapiláre do výšky h nad hladinu v nádobe">'
            '<path d="M90 45V210H510V45" fill="none" stroke="#61758b" stroke-width="4"/>'
            '<rect x="92" y="134" width="416" height="74" fill="#d6e8f5"/><path d="M92 134H508" stroke="#3279a8" stroke-width="2"/>'
            '<path d="M270 65Q283 75 296 65V182H270Z" fill="#b4def5"/><path d="M270 65Q283 75 296 65" fill="none" stroke="#3279a8" stroke-width="2"/>'
            '<path d="M266 22V182M300 22V182" fill="none" stroke="#567083" stroke-width="5"/>'
            '<g stroke="#c0392b" stroke-width="2" fill="none"><path d="M335 70V133M328 80L335 68L342 80M328 123L335 135L342 123"/>'
            '<path d="M296 70H335M296 134H335" stroke-dasharray="3 3" stroke-width="1.2"/></g>'
            '<g stroke="#193b59" stroke-width="1.5" fill="none"><path d="M270 196H296M270 191V201M296 191V201"/></g>'
            f'<g {T}><text x="350" y="108">h</text><text x="312" y="34">kapilára</text><text x="106" y="124">hladina</text><text x="304" y="202">2r</text></g></svg>')

# ---------- zadanie ----------
Z1 = f'''<h2>1. Elektromagnetická indukcia</h2><div class="task"><ol><li>Charakterizujte magnetický indukčný tok. Ako sa môže meniť s časom?</li><li>Opíšte jav elektromagnetickej indukcie. Za akých podmienok vzniká indukované napätie?</li><li>Sformulujte Faradayov zákon elektromagnetickej indukcie a Lenzov zákon. Vysvetlite význam znamienka mínus vo Faradayovom zákone.</li></ol><p><strong>Úloha:</strong> Priamy vodič s dĺžkou <strong>l = 20 cm</strong> sa pohybuje rovnomerne v homogénnom magnetickom poli s indukciou <strong>B = 0,1 T</strong>. Vodič, jeho rýchlosť a indukčné čiary sú navzájom kolmé. Medzi koncami vodiča sa indukuje napätie <strong>Uᵢ = 0,01 V</strong>.</p>{VODIC_Z}<ol type="a"><li>Akou rýchlosťou sa vodič pohybuje?</li></ol></div>'''

Z2 = f'''<h2>2. Gravitačné pole</h2><div class="task"><ol><li>Sformulujte Newtonov gravitačný zákon a vysvetlite, od čoho závisí veľkosť gravitačnej sily.</li><li>Charakterizujte gravitačné pole a jeho intenzitu.</li></ol><p><strong>Úloha:</strong> Dve telesá sa navzájom gravitačne priťahujú. Prvé teleso pôsobí na druhé silou s veľkosťou <strong>F = 12 N</strong>.</p>{TELESA}<ol type="a"><li>Akou silou pôsobí druhé teleso na prvé? Vysvetlite smery oboch síl.</li><li>Akou silou sa budú telesá priťahovať, ak (každý prípad posudzujte samostatne voči pôvodnému stavu):<ul><li>sa vzdialenosť zdvojnásobí, r′ = 2r,</li><li>sa vzdialenosť zmenší na polovicu, r′ = r/2,</li><li>sa hmotnosť jedného telesa zdvojnásobí, m₁′ = 2m₁,</li><li>sa zdvojnásobí vzdialenosť aj hmotnosť jedného telesa, r′ = 2r, m₁′ = 2m₁,</li><li>sa zdvojnásobí vzdialenosť aj hmotnosti oboch telies, r′ = 2r, m₁′ = 2m₁, m₂′ = 2m₂?</li></ul></li></ol></div>'''

Z3 = '''<h2>3. Experiment – povrchové napätie z kapilárnej elevácie</h2><div class="task"><p>Experimentálne určte povrchové napätie vody z výšky, do ktorej voda vystúpi v tenkej sklenenej kapiláre.</p><ol><li>Navrhnite pomôcky a postup merania kapilárnej elevácie h.</li><li>Ako určíte vnútorný polomer kapiláry r a prečo ho potrebujete?</li><li>Odvoďte vzťah na výpočet povrchového napätia z rovnováhy síl.</li><li>Výsledok porovnajte s tabuľkovou hodnotou a uveďte hlavné zdroje nepresnosti.</li></ol></div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Elektromagnetická indukcia</h2><h3>1.1 Magnetický indukčný tok</h3><p><strong>Magnetický indukčný tok Φ</strong> plochou S v homogénnom magnetickom poli s indukciou B:</p><div class="formula">Φ = B S cos α &nbsp;&nbsp; [Φ] = T·m² = Wb (weber)</div><p>α je uhol medzi indukciou B a normálou (kolmicou) plochy. Názorne udáva „počet indukčných čiar“, ktoré plochou prechádzajú. Tok je najväčší, keď je plocha kolmá na indukčné čiary (α = 0), a nulový, keď sú čiary s plochou rovnobežné.</p><p>Tok sa môže meniť s časom tromi spôsobmi: zmenou <strong>indukcie B</strong> (približovanie magnetu, zmena prúdu v susednej cievke), zmenou <strong>plochy S</strong> (pohyb vodiča, zmena tvaru závitu) alebo zmenou <strong>uhla α</strong> (otáčanie závitu v poli – generátor).</p><h3>1.2 Jav elektromagnetickej indukcie</h3><p>Ak sa mení magnetický indukčný tok plochou ohraničenou vodičom, indukuje sa vo vodiči <strong>elektromotorické napätie</strong>. V uzavretom obvode ním tečie <strong>indukovaný prúd</strong>. Rozhodujúca je <strong>zmena</strong> toku, nie jeho veľkosť: stály magnet v pokoji pri cievke napätie neindukuje. Jav objavil M. Faraday v roku 1831. Pokusy: zasúvanie magnetu do cievky, zapínanie a vypínanie prúdu v susednej cievke, otáčanie cievky v magnetickom poli.</p><h3>1.3 Faradayov a Lenzov zákon</h3><p><strong>Faradayov zákon:</strong> indukované napätie sa rovná zápornej časovej zmene magnetického indukčného toku. Pre cievku s N závitmi:</p><div class="formula">Uᵢ = −N · ΔΦ / Δt</div><p><strong>Lenzov zákon:</strong> indukovaný prúd má taký smer, že svojím magnetickým poľom pôsobí <strong>proti zmene</strong>, ktorá ho vyvolala. Znamienko mínus vo Faradayovom zákone vyjadruje práve Lenzov zákon. Je to dôsledok zákona zachovania energie: keby indukovaný prúd zmenu podporoval, energia by vznikala z ničoho.</p>{LENZ}<p>Využitie: generátory v elektrárňach, transformátory, dynamo, indukčný varič, elektromagnetická brzda (vírivé prúdy), indukčné nabíjanie, snímače (elektrická gitara, mikrofón).</p><h3>1.4 Napätie na pohybujúcom sa vodiči</h3><p>Ak sa vodič s dĺžkou l pohybuje rýchlosťou v kolmo na indukčné čiary, za čas Δt opíše plochu ΔS = l v Δt. Tok ňou je ΔΦ = B l v Δt, a preto:</p><div class="formula">Uᵢ = ΔΦ / Δt = B l v</div><p>Rovnaký výsledok dostaneme z Lorentzovej sily: na voľné elektróny vo vodiči pôsobí sila evB pozdĺž vodiča. Elektróny sa hromadia na jednom konci, kým ich elektrické pole nevyrovná magnetickú silu.</p><h3>1.5 Riešenie úlohy</h3><p>Zadané: l = 20 cm = 0,20 m, B = 0,1 T, Uᵢ = 0,01 V.</p>{VODIC_V}<div class="formula">Uᵢ = B l v &nbsp; → &nbsp; v = Uᵢ / (B l) = 0,01 V / (0,1 T · 0,20 m) = 0,5 m/s</div><p>Kontrola jednotiek: V/(T·m) = V/(V·s·m⁻²·m) = m/s.</p><div class="result"><strong>Vodič sa pohybuje rýchlosťou v = 0,5 m/s.</strong></div>'''

V2 = f'''<h2>2. Gravitačné pole</h2><h3>2.1 Newtonov gravitačný zákon</h3><p>Každé dve telesá sa navzájom priťahujú gravitačnými silami. Pre hmotné body (aj pre homogénne gule, r je vzdialenosť stredov):</p><div class="formula">F = G · m₁ m₂ / r² &nbsp;&nbsp;&nbsp; G = 6,67 · 10⁻¹¹ N·m²·kg⁻²</div><p>Veľkosť sily je <strong>priamo úmerná súčinu hmotností</strong> a <strong>nepriamo úmerná druhej mocnine vzdialenosti</strong>. Gravitačná konštanta G je veľmi malá, preto sú gravitačné sily medzi bežnými predmetmi nepostrehnuteľné. Výrazné sú, až keď je aspoň jedno teleso veľmi hmotné (Zem, Slnko).</p><h3>2.2 Gravitačné pole a jeho intenzita</h3><p>Gravitačné pole je priestor okolo telesa, v ktorom pôsobí gravitačná sila na iné telesá. Opisuje ho <strong>intenzita gravitačného poľa</strong> – sila pôsobiaca na teleso s hmotnosťou 1 kg:</p><div class="formula">K = F<sub>g</sub> / m = G M / r² &nbsp;&nbsp; [K] = N·kg⁻¹ = m·s⁻²</div><p>Intenzita smeruje do stredu telesa, ktoré pole vytvára. Pole hmotného bodu (gule) je <strong>radiálne</strong>, v malej oblasti pri povrchu Zeme ho považujeme za <strong>homogénne</strong>. Na povrchu Zeme je K ≈ 9,8 N/kg.</p><h3>2.3 Riešenie úlohy</h3>{TELESA}<p><strong>a)</strong> Podľa 3. Newtonovho zákona (akcia a reakcia) pôsobí druhé teleso na prvé rovnako veľkou silou <strong>12 N</strong>, opačného smeru. Obe sily ležia na spojnici stredov a smerujú k druhému telesu – telesá sa priťahujú. Každá pôsobí na iné teleso, preto sa nerušia. Sily sú rovnaké aj vtedy, keď sú hmotnosti telies rôzne. Rôzne sú len zrýchlenia, ktoré telesám udelia.</p><p><strong>b)</strong> Novú silu určíme z pomeru, konštanta G sa vykráti:</p><div class="formula">F′ / F = (m₁′ / m₁) · (m₂′ / m₂) · (r / r′)²</div><table><tr><th>Zmena oproti pôvodnému stavu</th><th>Výpočet</th><th>Nová sila</th></tr><tr><td>r′ = 2r</td><td>12 N · 1/2²</td><td><strong>3 N</strong></td></tr><tr><td>r′ = r/2</td><td>12 N · 2²</td><td><strong>48 N</strong></td></tr><tr><td>m₁′ = 2m₁</td><td>12 N · 2</td><td><strong>24 N</strong></td></tr><tr><td>r′ = 2r, m₁′ = 2m₁</td><td>12 N · 2/2²</td><td><strong>6 N</strong></td></tr><tr><td>r′ = 2r, m₁′ = 2m₁, m₂′ = 2m₂</td><td>12 N · 2 · 2/2²</td><td><strong>12 N</strong></td></tr></table>{GRAF_F}<p>Vzdialenosť má väčší vplyv ako hmotnosť – vystupuje v druhej mocnine. Dvojnásobnú vzdialenosť práve vyrovná zdvojnásobenie oboch hmotností, preto v poslednom prípade zostane sila 12 N.</p><div class="result"><strong>a) 12 N, opačný smer; b) 3 N, 48 N, 24 N, 6 N a 12 N.</strong></div>'''

V3 = f'''<h2>3. Experiment – povrchové napätie z kapilárnej elevácie</h2><h3>3.1 Princíp</h3><p>Voda dobre zmáča čisté sklo – molekuly vody sa priťahujú k sklu viac ako navzájom. Povrch vody v úzkej trubici (kapiláre) je preto vydutý nadol (dutý meniskus) a voda v kapiláre vystúpi nad okolitú hladinu – <strong>kapilárna elevácia</strong>. Kvapalina, ktorá stenu nezmáča (ortuť v skle), v kapiláre naopak klesne – <strong>kapilárna depresia</strong>.</p>{KAPILARA}<h3>3.2 Odvodenie vzťahu</h3><p>Na obvode menisku (dĺžka 2πr) pôsobí povrchová sila F = σ · 2πr. Pri dokonalom zmáčaní (styčný uhol θ ≈ 0°) smeruje zvislo nahor. Voda vystupuje, kým táto sila nevyrovná tiaž stĺpca vody s výškou h:</p><div class="formula">2π r σ = ρ π r² h g</div><div class="formula">σ = ρ g r h / 2 &nbsp;&nbsp;&nbsp; h = 2σ / (ρ g r)</div><p>Pri nedokonalom zmáčaní treba sílu násobiť cos θ, potom σ = ρgrh / (2 cos θ). Výška stĺpca je nepriamo úmerná polomeru kapiláry: čím tenšia kapilára, tým vyššie voda vystúpi. Preto je potrebné poznať vnútorný polomer r.</p><h3>3.3 Pomôcky</h3><p>Niekoľko čistých sklenených kapilár s rôznym vnútorným priemerom (0,5–2 mm), široká nádoba s vodou, stojan s držiakom, pravítko s milimetrovou stupnicou alebo meracia lupa, teplomer. Vnútorný polomer určíme meracou lupou na reze kapiláry, alebo nepriamo: kapiláru naplníme vodou, zvážime vodu s dĺžkou stĺpca L a z objemu V = πr²L vypočítame r.</p><h3>3.4 Postup</h3><ol><li>Kapiláry vyčistíme (napr. saponátom a dôkladne opláchneme destilovanou vodou), aby bolo zmáčanie dokonalé.</li><li>Kapiláru upevníme zvislo a dolný koniec ponoríme do vody. Vodu v kapiláre nasajeme trochu vyššie a necháme ju klesnúť do rovnovážnej polohy – meniskus sa tak ustáli spoľahlivejšie.</li><li>Odčítame výšku h od vonkajšej hladiny po spodok menisku.</li><li>Meranie zopakujeme pre ďalšie kapiláry a zapíšeme teplotu vody.</li><li>Pre každú kapiláru vypočítame σ = ρgrh/2 a výsledky spriemerujeme.</li></ol><h3>3.5 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje pre vodu s teplotou 20 °C, ρ = 998 kg/m³, g = 9,81 m/s²; nejde o skutočné meranie.</p><table><tr><th>Kapilára</th><th>r (mm)</th><th>h (mm)</th><th>r · h (mm²)</th><th>σ (N/m)</th></tr><tr><td>1</td><td>0,25</td><td>59,4</td><td>14,9</td><td>0,0727</td></tr><tr><td>2</td><td>0,50</td><td>29,7</td><td>14,9</td><td>0,0727</td></tr><tr><td>3</td><td>1,00</td><td>14,9</td><td>14,9</td><td>0,0729</td></tr></table><p>Napríklad pre kapiláru 2:</p><div class="formula">σ = ρ g r h / 2 = 998 · 9,81 · 0,50 · 10⁻³ · 29,7 · 10⁻³ / 2 N/m ≈ 0,0727 N/m</div><p>Súčin r · h je pre všetky kapiláry rovnaký, čo potvrdzuje nepriamu úmernosť h ~ 1/r. Priemer σ ≈ 0,073 N/m dobre súhlasí s tabuľkovou hodnotou 0,0728 N/m pri 20 °C.</p><h3>3.6 Zdroje nepresností</h3><ul><li>Nečistoty a mastnota na stenách kapiláry zhoršia zmáčanie (cos θ &lt; 1) a výsledok vyjde menší. Saponát znižuje povrchové napätie vody.</li><li>Najväčšiu relatívnu chybu spôsobuje určenie vnútorného polomeru – je malý a vystupuje vo vzťahu priamo.</li><li>Odčítanie výšky h (paralaxa, zakrivenie menisku), nezvislá poloha kapiláry.</li><li>Teplota – povrchové napätie s rastúcou teplotou klesá.</li></ul><div class="result"><strong>Záver:</strong> Z rovnováhy povrchovej sily a tiaže stĺpca vody vyplýva σ = ρgrh/2. Meraním kapilárnej elevácie v kapilárach so známym polomerom dostaneme pre vodu σ ≈ 0,073 N/m.</div>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO20', 'Otázka', 'maturit', 'riginál'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
