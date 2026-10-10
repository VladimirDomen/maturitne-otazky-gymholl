/* ============================================
   FYZIKA — VZOROVÉ ZADANIA — dáta a vykreslenie rozcestníka
   Používa ho index.html (SK) aj en/index.html (EN);
   jazyk sa berie z <html lang="…">.
   Nový vzor = nový záznam v OTAZKY (texty sk + en)
   a súbory VzorN_zadanie/vypracovanie.html + en/ModelN_questions/solutions.html.
   ============================================ */

const LANG = document.documentElement.lang === 'en' ? 'en' : 'sk';

/* ---------- oblasti fyziky ---------- */
const OBLASTI = {
  mechanika:   { sk: 'Mechanika',         en: 'Mechanics',          farba: '#2f6db3' },
  gravitacia:  { sk: 'Gravitácia',        en: 'Gravitation',        farba: '#6a4fc4' },
  tekutiny:    { sk: 'Kvapaliny a plyny', en: 'Fluids',             farba: '#14879b' },
  termika:     { sk: 'Termika',           en: 'Thermal physics',    farba: '#9a6b12' },
  vlnenie:     { sk: 'Vlnenie',           en: 'Waves',              farba: '#2e8b57' },
  optika:      { sk: 'Optika',            en: 'Optics',             farba: '#c4661b' },
  elektrina:   { sk: 'Elektrina',         en: 'Electricity',        farba: '#c0392b' },
  magnetizmus: { sk: 'Magnetizmus',       en: 'Magnetism',          farba: '#a03c8c' },
  mikrosvet:   { sk: 'Mikrosvet',         en: 'Atomic physics',     farba: '#4f5d73' },
};

/* ---------- vzory (nový vzor = nový záznam) ---------- */
const OTAZKY = [
  { n: 1, casti: [
    { o: ['tekutiny'],
      sk: ['Mechanika kvapalín a plynov', 'Hydrostatický tlak, Pascalov a Archimedov zákon, hustota gule vo vode'],
      en: ['Mechanics of fluids', 'Hydrostatic pressure, Pascal’s law and Archimedes’ principle, density of a sphere in water'] },
    { o: ['elektrina', 'magnetizmus'],
      sk: ['Striedavý prúd – transformátor', 'Efektívne hodnoty, transformačný pomer, výkon ideálneho transformátora'],
      en: ['Alternating current – transformer', 'RMS values, turns ratio, power of an ideal transformer'] },
    { o: ['optika'],
      sk: ['Disperzia svetla', 'Praktická úloha: ohnisková vzdialenosť spojky pre modré a červené svetlo'],
      en: ['Dispersion of light', 'Practical task: focal length of a converging lens for blue and red light'] },
  ]},
  { n: 2, casti: [
    { o: ['gravitacia'],
      sk: ['Gravitačné pole', 'Newtonov gravitačný zákon, intenzita, Keplerove zákony, pole vo výške h'],
      en: ['Gravitational field', 'Newton’s law of gravitation, field strength, Kepler’s laws, field at height h'] },
    { o: ['vlnenie'],
      sk: ['Mechanické vlnenie', 'Rovnica postupnej vlny, polohový a časový graf, λ, T, f, v'],
      en: ['Mechanical waves', 'Progressive wave equation, position and time graphs, λ, T, f, v'] },
    { o: ['elektrina'],
      sk: ['Elektrický prúd', 'Ohmov zákon, meranie odporu ampérmetrom a voltmetrom'],
      en: ['Electric current', 'Ohm’s law, measuring resistance with an ammeter and a voltmeter'] },
  ]},
  { n: 3, casti: [
    { o: ['gravitacia', 'mechanika'],
      sk: ['Pohyb v gravitačnom poli', 'Vrhy v homogénnom poli, kozmické rýchlosti, zvislý vrh nahor'],
      en: ['Motion in a gravitational field', 'Projectiles in a uniform field, cosmic velocities, vertical upward projection'] },
    { o: ['vlnenie'],
      sk: ['Interferencia vlnenia', 'Superpozícia, odraz a lom, stojaté vlnenie, uzly a kmitne'],
      en: ['Interference of waves', 'Superposition, reflection and refraction, standing waves, nodes and antinodes'] },
    { o: ['elektrina', 'magnetizmus'],
      sk: ['Vznik elektrického prúdu', 'Elektromagnetická indukcia, Faradayov a Lenzov zákon, zelektrizovanie dotykom'],
      en: ['Origin of electric current', 'Electromagnetic induction, Faraday’s and Lenz’s laws, charging by contact'] },
  ]},
  { n: 4, casti: [
    { o: ['mechanika'],
      sk: ['Kinematika hmotného bodu', 'Vzťažná sústava, dráha, rýchlosť, zrýchlenie, brzdná dráha'],
      en: ['Kinematics of a particle', 'Frame of reference, distance, velocity, acceleration, braking distance'] },
    { o: ['magnetizmus'],
      sk: ['Stacionárne magnetické pole', 'Pole priameho vodiča, pravidlo pravej ruky, indukcia medzi vodičmi'],
      en: ['Stationary magnetic field', 'Field of a straight wire, right-hand grip rule, flux density between wires'] },
    { o: ['mikrosvet'],
      sk: ['Mikrosvet', 'Stavba atómu, rádioaktivita, zákon rozpadu, polčas'],
      en: ['The microworld', 'Structure of the atom, radioactivity, decay law, half-life'] },
  ]},
  { n: 26, casti: [
    { o: ['mikrosvet', 'optika'],
      sk: ['Elektrónový obal atómu', 'Kvantovanie energie, emisné a absorpčné spektrum, energia fotónu'],
      en: ['Electron shell of the atom', 'Quantised energy, emission and absorption spectra, photon energy'] },
    { o: ['elektrina'],
      sk: ['Elektrický prúd', 'Príčina odporu kovov, rezistivita, odpor a teplota, zdroj s vnútorným odporom'],
      en: ['Electric current', 'Resistance of metals, resistivity, resistance and temperature, internal resistance'] },
    { o: ['termika'],
      sk: ['Vlastnosti plynov', 'Experiment: teplota plynu pri rýchlom stláčaní a rozpínaní, 1. termodynamický zákon'],
      en: ['Properties of gases', 'Experiment: gas temperature in rapid compression and expansion, first law of thermodynamics'] },
  ]},
];

/* ---------- texty rozhrania ---------- */
const T = {
  sk: {
    vzor: 'Vzor', zad: 'Zadanie', vyp: 'Vypracovanie',
    linkZ: n => `Vzor${n}_zadanie.html`, linkV: n => `Vzor${n}_vypracovanie.html`,
    pocet: n => n === 1 ? 'vzor' : n < 5 ? 'vzory' : 'vzorov',
    casti: 'tematických častí', oblasti: 'oblastí fyziky', vsetky: 'Všetky',
    prazdne: 'Pre túto oblasť zatiaľ nie je žiadny vzor.',
    info: (o, n) => `${o}: ${n} ${T.pocet(n)} · zvýraznené sú časti z tejto oblasti`,
  },
  en: {
    vzor: 'Model', zad: 'Questions', vyp: 'Solutions',
    linkZ: n => `Model${n}_questions.html`, linkV: n => `Model${n}_solutions.html`,
    pocet: n => n === 1 ? 'model' : 'models',
    casti: 'topic parts', oblasti: 'areas of physics', vsetky: 'All',
    prazdne: 'There is no model for this area yet.',
    info: (o, n) => `${o}: ${n} ${T.pocet(n)} · parts from this area are highlighted`,
  },
}[LANG];

/* ---------- vykreslenie ---------- */
const $ = id => document.getElementById(id);
const farba = k => OBLASTI[k].farba;
const nazov = k => OBLASTI[k][LANG];
const esc = s => s.replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

const pocetCasti = OTAZKY.reduce((s, q) => s + q.casti.length, 0);
const pouzite = Object.keys(OBLASTI).filter(k => OTAZKY.some(q => q.casti.some(c => c.o.includes(k))));
$('stats').innerHTML =
  `<div class="stat"><b>${OTAZKY.length}</b><span>${T.pocet(OTAZKY.length)}</span></div>` +
  `<div class="stat"><b>${pocetCasti}</b><span>${T.casti}</span></div>` +
  `<div class="stat"><b>${pouzite.length}</b><span>${T.oblasti}</span></div>`;

$('grid').innerHTML = OTAZKY.map(q => {
  const hlavne = q.casti.map(c => farba(c.o[0]));
  const vsetky = [...new Set(q.casti.flatMap(c => c.o))];
  return `
  <article class="card" data-o="${vsetky.join(' ')}" style="--c1:${hlavne[0]};--c2:${hlavne[1]};--c3:${hlavne[2]}">
    <div class="card-head">
      <div><div class="card-label">${T.vzor}</div><div class="card-num">${q.n}</div></div>
      <div class="card-btns">
        <a class="btn btn-z" href="${T.linkZ(q.n)}">${T.zad}</a>
        <a class="btn btn-v" href="${T.linkV(q.n)}">${T.vyp}</a>
      </div>
    </div>
    <ol class="parts">
      ${q.casti.map((c, i) => `
      <li class="part" data-o="${c.o.join(' ')}">
        <span class="part-n" style="--c:${farba(c.o[0])}">${i + 1}</span>
        <div>
          <div class="part-t">${esc(c[LANG][0])}</div>
          <div class="part-d">${esc(c[LANG][1])}</div>
          <div class="tags">${c.o.map(k => `<span class="tag" style="--c:${farba(k)}">${nazov(k)}</span>`).join('')}</div>
        </div>
      </li>`).join('')}
    </ol>
  </article>`;
}).join('') + `<div class="empty" id="empty" hidden>${T.prazdne}</div>`;

const chip = (k, text, f, cnt) =>
  `<button type="button" class="chip${k === '' ? ' on' : ''}" data-a="${k}" ${f ? `style="--c:${f}"` : ''}>` +
  `${f ? '<span class="dot"></span>' : ''}${text}<span class="cnt">${cnt}</span></button>`;

$('chips').innerHTML = chip('', T.vsetky, '', OTAZKY.length) + pouzite.map(k =>
  chip(k, nazov(k), farba(k), OTAZKY.filter(q => q.casti.some(c => c.o.includes(k))).length)
).join('');

function filtruj(k) {
  document.querySelectorAll('.chip').forEach(c => c.classList.toggle('on', c.dataset.a === k));
  $('grid').classList.toggle('filtering', !!k);
  let n = 0;
  document.querySelectorAll('.card').forEach(card => {
    const ok = !k || card.dataset.o.split(' ').includes(k);
    card.classList.toggle('hidden', !ok);
    if (ok) n++;
    card.querySelectorAll('.part').forEach(p => {
      const hit = !!k && p.dataset.o.split(' ').includes(k);
      p.classList.toggle('hit', hit);
      p.classList.toggle('dim', !!k && !hit);
    });
  });
  $('empty').hidden = n > 0;
  $('info').textContent = k ? T.info(nazov(k), n) : '';
  try { history.replaceState(null, '', k ? '#' + k : location.pathname); } catch (e) {}
  // prepínač jazyka zachová zvolený filter
  const l = document.querySelector('.lang a:not(.on)');
  if (l) l.hash = k ? k : '';
}

$('chips').addEventListener('click', e => {
  const b = e.target.closest('.chip');
  if (!b) return;
  filtruj(b.classList.contains('on') && b.dataset.a ? '' : b.dataset.a);
});

const z = decodeURIComponent(location.hash.slice(1));
if (OBLASTI[z]) filtruj(z);
