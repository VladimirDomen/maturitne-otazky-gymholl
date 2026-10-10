"""Vzor 24 podľa MO24 a fotky 24 (text písaný priamo; doplnený benzín a úloha na Mesiaci z fotky)
-> Vzor24_zadanie.html + Vzor24_vypracovanie.html.
Spustenie: python -I gen24.py <priečinok FYZIKA>"""
import sys, pathlib

DST = pathlib.Path(sys.argv[1])
N = 24
TOPICS = ['Mechanické vlnenie', 'Kapilarita', 'Koeficient šmykového trenia']

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
VLNA = ('<svg class="diagram" viewBox="0 0 600 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stojaté vlnenie: susedné uzly vzdialené 1,5 m">'
        '<path d="M30 90H570" stroke="#9aaabb" stroke-width="1.5" stroke-dasharray="5 5"/>'
        '<path d="M60 90Q140 10 220 90Q300 170 380 90Q460 10 540 90" fill="none" stroke="#2e8b57" stroke-width="3"/>'
        '<path d="M60 90Q140 170 220 90Q300 10 380 90Q460 170 540 90" fill="none" stroke="#2e8b57" stroke-width="2" stroke-dasharray="7 5" opacity=".6"/>'
        '<g fill="#193b59"><circle cx="60" cy="90" r="5"/><circle cx="220" cy="90" r="5"/><circle cx="380" cy="90" r="5"/><circle cx="540" cy="90" r="5"/></g>'
        '<g stroke="#c0392b" stroke-width="2"><path d="M140 52V128M300 52V128M460 52V128" stroke-dasharray="3 4"/></g>'
        '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M220 150H380M220 142V158M380 142V158"/></g>'
        '<g font-size="14" fill="#253d51"><text x="48" y="116">uzol</text><text x="208" y="116">uzol</text><text x="118" y="44" fill="#c0392b">kmitňa</text>'
        '<text x="278" y="176">1,5 m</text></g></svg>')

def kapilara():
    # vľavo zvislá kapilára, vpravo kapilára sklonená o 30° k hladine; zvislý výstup h = 60 px v oboch
    return ('<svg class="diagram" viewBox="0 0 640 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kapilárna elevácia v zvislej a v šikmej kapiláre">'
            '<g stroke="#375873" stroke-width="2"><path d="M30 150V255H270V150M330 150V255H610V150" fill="none"/></g>'
            '<path d="M32 170H268V253H32Z M332 170H608V253H332Z" fill="#fdecc8"/>'
            '<path d="M32 170H268M332 170H608" stroke="#bb7728" stroke-width="2"/>'
            # zvislá kapilára
            '<path d="M141 112Q148 120 155 112V245H141Z" fill="#fdecc8"/>'
            '<g stroke="#375873" stroke-width="2.5"><path d="M140 40V245M156 40V245"/></g>'
            '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M160 112H215M199 170H215M207 112V170"/><path d="M140 32H156M140 27V37M156 27V37"/></g>'
            # šikmá kapilára (smer 30°): stredová čiara z (344,242) hore doprava
            '<path d="M340 235L556 110L564 124L348 249Z" fill="#fdecc8"/>'
            '<g stroke="#375873" stroke-width="2.5"><path d="M340 235L582 95M348 249L590 109"/></g>'
            '<g stroke="#637889" stroke-width="1.5" fill="none"><path d="M614 170H630M622 117V170"/><path d="M566 117H630" stroke-dasharray="4 3"/><path d="M519 170A50 50 0 0 0 512.3 145"/></g>'
            '<g font-size="15" fill="#193b59"><text x="214" y="146">h</text><text x="143" y="22">d</text><text x="526" y="165">30°</text>'
            '<text x="496" y="128">s</text><text x="627" y="148">h</text><text x="60" y="210">benzín</text></g></svg>')

def kvader(vyp):
    ft = '<text x="78" y="110">F<tspan font-size="11" dy="4">t</tspan></text>'
    return ('<svg class="diagram" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Kváder na vodorovnej podložke ťahaný silomerom">'
            '<path d="M30 150H570" stroke="#646c78" stroke-width="4"/>'
            '<rect x="170" y="90" width="120" height="58" fill="#d8bb90" stroke="#65492e" stroke-width="2"/>'
            '<g stroke="#1682b5" stroke-width="3" fill="none"><path d="M290 119H390M462 119H520"/><path d="M510 111L522 119L510 127"/></g>'
            '<rect x="390" y="103" width="72" height="32" rx="15" fill="#f4f9fc" stroke="#1682b5" stroke-width="2"/>'
            '<g stroke="#1682b5" stroke-width="1.5"><path d="M402 112V126M414 112V126M426 112V126M438 112V126M450 112V126"/></g>'
            '<g stroke="#c0392b" stroke-width="3" fill="none"><path d="M170 140H104M114 133L102 140L114 147"/></g>'
            '<g stroke="#26724c" stroke-width="3" fill="none"><path d="M230 90V40M223 51L230 39L237 51"/></g>'
            '<g stroke="#a57820" stroke-width="3" fill="none"><path d="M230 148V200M223 189L230 201L237 189"/></g>'
            '<g font-size="15" fill="#193b59"><text x="400" y="94">silomer</text><text x="526" y="112">F</text>'
            '<text x="240" y="48">F<tspan font-size="11" dy="4">N</tspan></text><text x="240" y="198">G = mg</text>'
            f'{ft}</g></svg>')

GRAF = ('<svg class="diagram" viewBox="0 0 520 290" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Graf trecej sily od tlakovej sily, priamka so smernicou 0,30">'
        '<g stroke="#e3eaf1" stroke-width="1"><path d="M70 200H460M70 150H460M70 100H460M70 50H460M170 250V35M270 250V35M370 250V35"/></g>'
        '<g stroke="#193b59" stroke-width="2" fill="none"><path d="M70 262V25M60 250H480M64 37L70 25L76 37M468 244L480 250L468 256"/></g>'
        '<path d="M70 250L430 34" stroke="#2f6db3" stroke-width="2.5"/>'
        '<g fill="#c0392b"><circle cx="168.1" cy="191" r="5"/><circle cx="266.2" cy="134" r="5"/><circle cx="364.3" cy="72" r="5"/></g>'
        '<g font-size="14" fill="#253d51"><text x="38" y="205">0,5</text><text x="38" y="155">1,0</text><text x="38" y="105">1,5</text><text x="38" y="55">2,0</text>'
        '<text x="165" y="270">2</text><text x="265" y="270">4</text><text x="365" y="270">6</text>'
        '<text x="80" y="24">F<tspan font-size="10" dy="4">t</tspan><tspan dy="-4"> (N)</tspan></text>'
        '<text x="430" y="238">F<tspan font-size="10" dy="4">N</tspan><tspan dy="-4"> (N)</tspan></text></g>'
        '<text x="300" y="200" font-size="14" fill="#2f6db3">smernica = μ ≈ 0,30</text></svg>')

# body grafu = modelová tabuľka; priamka F_t = 0,30 F_N po F_N = 7,2 N (x = 70 + 50 F_N, y = 250 − 100 F_t)

KAP = kapilara()

# ---------- zadanie ----------
Z1 = f'''<h2>1. Mechanické vlnenie</h2><div class="task"><ol><li>Vysvetlite podmienky vzniku mechanického vlnenia. Porovnajte pozdĺžne a priečne vlnenie a definujte vlnovú dĺžku.</li><li>Napíšte rovnicu postupnej mechanickej vlny a vysvetlite veličiny, ktoré vlnenie charakterizujú.</li><li>Opíšte základné vlastnosti vlnenia: odraz, lom, ohyb a interferenciu.</li><li>Vysvetlite vznik a vlastnosti stojatého vlnenia.</li></ol><p><strong>Úloha:</strong> Stojaté vlnenie vzniklo interferenciou dvoch rovnakých postupných vĺn, ktoré sa šíria proti sebe. Perióda kmitania je <strong>T = 21 · 10⁻⁴ s</strong>, vzdialenosť dvoch susedných uzlov je <strong>1,5 m</strong>. Akou rýchlosťou sa šíri postupné vlnenie?</p>{VLNA}</div>'''

Z2 = f'''<h2>2. Štruktúra a vlastnosti kvapalín – kapilarita</h2><div class="task"><ol><li>Opíšte povrchovú vrstvu kvapaliny. Vysvetlite povrchovú silu a povrchové napätie.</li><li>Vysvetlite zmáčanie, kapilárnu eleváciu a kapilárnu depresiu.</li></ol><p><strong>Úloha:</strong> Sklenená kapilára s vnútorným priemerom <strong>d = 0,2&nbsp;mm</strong> je ponorená do benzínu s teplotou 18&nbsp;°C. Hustota benzínu je <strong>ρ = 820&nbsp;kg/m³</strong>, povrchové napätie <strong>σ = 29,1&nbsp;mN/m</strong>. Benzín stenu kapiláry dokonale zmáča, g = 9,81&nbsp;m/s².</p>{KAP}<ol type="a"><li>Do akej výšky vystúpi benzín v kapiláre?</li><li>Aká bude výška, ak použijeme kapiláru s dvojnásobným priemerom d₂ = 2d₁?</li><li>Ako sa zmení výstup benzínu, ak kapiláru skloníme tak, že zviera s voľným povrchom kvapaliny uhol 30°?</li><li>Do akej výšky by benzín vystúpil v pôvodnej kapiláre na Mesiaci, kde g<sub>M</sub> = g/6?</li></ol></div>'''

Z3 = f'''<h2>3. Experiment – koeficient šmykového trenia</h2><div class="task"><p>Experimentálne určte koeficient šmykového trenia medzi kvádrom a vodorovnou podložkou. Navrhnite pomôcky, postup merania a spracovanie výsledkov. Vysvetlite, prečo musí byť pohyb kvádra pri meraní rovnomerný.</p>{kvader(False)}</div>'''

# ---------- vypracovanie ----------
V1 = f'''<h2>1. Mechanické vlnenie</h2><h3>1.1 Vznik vlnenia</h3><p>Mechanické vlnenie je dej, pri ktorom sa kmitanie šíri pružným prostredím. Potrebujeme <strong>zdroj kmitania</strong> a <strong>pružné prostredie</strong>, ktorého častice sú navzájom viazané. Kmitajúca častica prostredníctvom väzieb rozkmitá susedné častice, každá ďalšia začne kmitať s oneskorením. Vlnenie prenáša energiu, nie látku – častice kmitajú okolo svojich rovnovážnych polôh.</p><p><strong>Priečne vlnenie:</strong> častice kmitajú kolmo na smer šírenia (vlnenie na lane či strune). Vzniká v pevných látkach a na povrchu kvapalín.</p><p><strong>Pozdĺžne vlnenie:</strong> častice kmitajú v smere šírenia a vznikajú zhustenia a zriedenia (zvuk). Šíri sa v pevných látkach, kvapalinách aj plynoch.</p><p><strong>Vlnová dĺžka λ</strong> je vzdialenosť, do ktorej sa vlnenie rozšíri za jednu periódu. Je to aj vzdialenosť dvoch najbližších bodov, ktoré kmitajú s rovnakou fázou:</p><div class="formula">λ = vT = v/f</div><h3>1.2 Rovnica postupnej vlny</h3><p>Ak zdroj v mieste x = 0 kmitá podľa y = y<sub>m</sub> sin ωt, bod vo vzdialenosti x kmitá s oneskorením x/v:</p><div class="formula">y = y<sub>m</sub> sin 2π(t/T − x/λ)</div><p>y je okamžitá výchylka, y<sub>m</sub> amplitúda, T perióda, f = 1/T frekvencia, λ vlnová dĺžka a v rýchlosť vlnenia. Výraz 2π(t/T − x/λ) je fáza vlnenia.</p><h3>1.3 Základné vlastnosti vlnenia</h3><ul><li><strong>Odraz:</strong> na pevnom konci sa vlnenie odráža s opačnou fázou, na voľnom konci s rovnakou fázou.</li><li><strong>Lom:</strong> pri prechode do iného prostredia sa mení rýchlosť a smer šírenia; frekvencia ostáva rovnaká.</li><li><strong>Ohyb:</strong> vlnenie sa šíri aj za prekážku, výrazne najmä vtedy, keď je prekážka alebo otvor porovnateľný s λ.</li><li><strong>Interferencia:</strong> skladanie vlnení. Výchylky sa sčítajú; vlnenia sa zosilňujú alebo zoslabujú podľa fázového rozdielu.</li></ul><p>Šírenie vlnenia vysvetľuje Huygensov princíp: každý bod, do ktorého vlnenie dospeje, je zdrojom elementárneho vlnenia.</p><h3>1.4 Stojaté vlnenie</h3><p>Stojaté vlnenie vzniká interferenciou dvoch vlnení s rovnakou frekvenciou a amplitúdou, ktoré sa šíria proti sebe – typicky priameho a odrazeného vlnenia.</p><ul><li><strong>Uzly</strong> trvalo nekmitajú; <strong>kmitne</strong> kmitajú s najväčšou amplitúdou.</li><li>Susedné uzly sú od seba vzdialené <strong>λ/2</strong>, uzol a susedná kmitňa λ/4.</li><li>Body medzi dvoma susednými uzlami kmitajú s rovnakou fázou, body v susedných úsekoch s opačnou fázou.</li><li>Stojaté vlnenie neprenáša energiu. Napríklad na strune upevnenej na oboch koncoch platí l = kλ/2.</li></ul><h3>1.5 Riešenie úlohy</h3>{VLNA}<p>Susedné uzly sú od seba vzdialené polovicu vlnovej dĺžky:</p><div class="formula">λ/2 = 1,5 m &nbsp; → &nbsp; λ = 3,0 m</div><p>Perióda stojatého vlnenia je rovnaká ako perióda postupných vĺn, z ktorých vzniklo:</p><div class="formula">v = λ/T = 3,0 m / (21 · 10⁻⁴ s) ≈ 1 430 m/s</div><div class="result"><strong>Postupné vlnenie sa šíri rýchlosťou približne 1,43 · 10³ m/s.</strong></div><p class="subtle">Frekvencia je f = 1/T ≈ 476 Hz. Rýchlosť približne zodpovedá rýchlosti zvuku vo vode.</p>'''

V2 = f'''<h2>2. Štruktúra a vlastnosti kvapalín – kapilarita</h2><h3>2.1 Povrchová vrstva a povrchové napätie</h3><p>Molekula vo vnútri kvapaliny je priťahovaná susednými molekulami zo všetkých strán rovnako. Molekula v <strong>povrchovej vrstve</strong> (hrúbka približne dosahu molekulových síl) má susedov len zdola, preto výslednica síl smeruje do kvapaliny. Povrchová vrstva sa správa ako napnutá blana a kvapalina sa snaží zmenšiť svoj povrch – preto má malá kvapka tvar gule.</p><p>Na okraj povrchovej vrstvy pôsobí <strong>povrchová sila</strong> F, ktorá je dotyčnicou k povrchu a kolmá na okraj. <strong>Povrchové napätie</strong> je podiel tejto sily a dĺžky okraja:</p><div class="formula">σ = F/l &nbsp;&nbsp; [σ] = N/m</div><p>Povrchové napätie závisí od druhu kvapaliny a s rastúcou teplotou klesá.</p><h3>2.2 Zmáčanie a kapilarita</h3><p>Ak sú príťažlivé sily medzi molekulami kvapaliny a steny väčšie ako medzi molekulami kvapaliny navzájom, kvapalina stenu <strong>zmáča</strong> a tvorí dutý meniskus (voda alebo benzín na skle). Ak sú menšie, kvapalina stenu nezmáča a meniskus je vypuklý (ortuť na skle).</p><p>V úzkej trubici – kapiláre – zmáčajúca kvapalina vystúpi nad okolitú hladinu (<strong>kapilárna elevácia</strong>), nezmáčajúca klesne pod ňu (<strong>kapilárna depresia</strong>). Pri dokonalom zmáčaní vyrovnáva povrchová sila po obvode kapiláry tiaž stĺpca kvapaliny:</p><div class="formula">2πrσ = πr²hρg &nbsp; → &nbsp; h = 2σ/(rρg) = 4σ/(dρg)</div><p>Kapilarita sa uplatňuje pri vzlínaní vody v pôde a v rastlinách, v knôte, pri nasiakavosti papiera a textílií.</p><h3>2.3 Riešenie úlohy</h3>{KAP}<p>Dosadíme v základných jednotkách: d = 0,2 mm = 2 · 10⁻⁴ m, σ = 29,1 mN/m = 0,0291 N/m.</p><p><strong>a)</strong></p><div class="formula">h = 4σ/(dρg) = (4 · 0,0291)/(2 · 10⁻⁴ · 820 · 9,81) m ≈ 0,0723 m = 7,23 cm</div><p><strong>b)</strong> Výška je nepriamo úmerná priemeru kapiláry. Pri dvojnásobnom priemere:</p><div class="formula">h₂ = h/2 ≈ 3,62 cm</div><p><strong>c)</strong> Výstup určuje rovnováha tlakov, preto rozhoduje <strong>zvislá</strong> výška hladiny nad voľným povrchom – tá sa nezmení a ostáva h ≈ 7,23 cm. Benzín však vystúpi ďalej pozdĺž kapiláry. Dĺžka stĺpca nad hladinou:</p><div class="formula">s = h/sin 30° = 7,23 cm / 0,5 ≈ 14,5 cm</div><p><strong>d)</strong> Výška je nepriamo úmerná tiažovému zrýchleniu. Povrchové napätie a hustota sa na Mesiaci nemenia:</p><div class="formula">h<sub>M</sub> = 4σ/(dρg<sub>M</sub>) = 6h ≈ 43,4 cm</div><div class="result"><strong>a) 7,23 cm; b) 3,62 cm; c) zvislá výška sa nezmení, stĺpec pozdĺž kapiláry má asi 14,5 cm; d) asi 43,4 cm.</strong></div><p class="subtle">Výpočet predpokladá dostatočne dlhú kapiláru a zanedbáva objem menisku. Ak by bola kapilára kratšia ako potrebná výška, kvapalina z nej nevytečie – meniskus sa na konci kapiláry len menej zakriví.</p>'''

V3 = f'''<h2>3. Experiment – koeficient šmykového trenia</h2><h3>3.1 Teória</h3><p>Pri šmýkaní telesa po podložke pôsobí proti pohybu trecia sila F<sub>t</sub>. Jej veľkosť je priamo úmerná tlakovej (normálovej) sile F<sub>N</sub>, ktorou teleso tlačí na podložku:</p><div class="formula">F<sub>t</sub> = μF<sub>N</sub></div><p>μ je koeficient šmykového trenia. Závisí od materiálu a úpravy stykových plôch, takmer nezávisí od veľkosti stykovej plochy a od rýchlosti. Na vodorovnej podložke pri vodorovnom ťahu je F<sub>N</sub> = G = mg.</p><h3>3.2 Pomôcky</h3><p>Drevený kváder s háčikom, silomer, sada závaží, váhy, vodorovná doska.</p><h3>3.3 Zapojenie</h3>{kvader(True)}<h3>3.4 Postup</h3><ol><li>Zvážime kváder a určíme jeho tiaž G = mg.</li><li>Silomer držíme vodorovne a ťaháme kváder <strong>rovnomerným priamočiarym pohybom</strong>. Odčítame ustálenú hodnotu sily F.</li><li>Meranie zopakujeme niekoľkokrát a určíme priemer.</li><li>Na kváder pridávame závažia a meranie opakujeme pre rôzne tlakové sily.</li><li>Vypočítame μ = F/F<sub>N</sub> a zostrojíme graf F<sub>t</sub> v závislosti od F<sub>N</sub>.</li></ol><h3>3.5 Prečo rovnomerný pohyb</h3><p>Pri rovnomernom priamočiarom pohybe je podľa prvého Newtonovho zákona výslednica síl nulová. Ťahová sila silomera sa preto rovná trecej sile: F = F<sub>t</sub>. Keby kváder zrýchľoval, bola by ťahová sila väčšia ako trecia a výsledok by vyšiel nesprávne veľký.</p><p>Sila potrebná na <strong>rozbehnutie</strong> kvádra je väčšia – zodpovedá pokojovému (statickému) treniu. Preto ju na určenie šmykového trenia nepoužívame.</p><h3>3.6 Ukážka vyhodnotenia</h3><p class="subtle">Nasledujúce čísla sú modelové údaje; nejde o skutočné meranie. Kváder má hmotnosť 0,20 kg, g = 9,81 m/s².</p><table><tr><th>m (kg)</th><th>F<sub>N</sub> = mg (N)</th><th>F (N)</th><th>μ = F/F<sub>N</sub></th></tr><tr><td>0,20</td><td>1,96</td><td>0,59</td><td>0,30</td></tr><tr><td>0,40</td><td>3,92</td><td>1,16</td><td>0,30</td></tr><tr><td>0,60</td><td>5,89</td><td>1,78</td><td>0,30</td></tr></table>{GRAF}<p>Body ležia približne na priamke prechádzajúcej počiatkom. Jej smernica je koeficient šmykového trenia.</p><div class="result"><strong>Záver:</strong> V modelových údajoch vyšlo μ ≈ 0,30. Trecia sila je priamo úmerná tlakovej sile.</div><h3>3.7 Nepresnosti a iná metóda</h3><p>Chyby spôsobuje nerovnomerné ťahanie, šikmo držaný silomer, nerovnaký povrch dosky a odčítanie kmitajúcej ručičky silomera. Pomáha opakovanie merania a pomalý ťah.</p><p>Koeficient sa dá určiť aj na naklonenej rovine: zväčšujeme sklon dosky, kým kváder po malom postrčení nekĺže rovnomerne. Potom mg sin α = μmg cos α, teda μ = tg α.</p>'''

for name, html in (('zadanie', page(N, 'zad', [Z1, Z2, Z3])), ('vypracovanie', page(N, 'vyp', [V1, V2, V3]))):
    for bad in ('ekonštru', 'rukopis', 'MO24', 'Otázka', 'maturit'):
        assert bad not in html, (name, bad)
    (DST / f'Vzor{N}_{name}.html').write_text(html, encoding='utf-8', newline='\n')
    print('ok', name, len(html))
