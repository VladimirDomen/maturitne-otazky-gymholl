/* ============================================
   FYZIKA — VZOROVÉ ZADANIA — vykreslenie rozcestníka
   Dáta sú v data.js (načíta sa pred týmto súborom).
   ============================================ */

/* ---------- texty rozhrania ---------- */
const T = {
  sk: {
    vzor: 'Vzor', zad: 'Zadanie', vyp: 'Vypracovanie',
    linkZ: n => `Vzor${n}_zadanie.html`, linkV: n => `Vzor${n}_vypracovanie.html`,
    pocet: n => n === 1 ? 'vzor' : n < 5 ? 'vzory' : 'vzorov',
    tema: 'tema.html', otvorit: c => `Otvoriť všetky časti (${c}) →`,
    casti: 'tematických častí', oblasti: 'oblastí fyziky', vsetky: 'Všetky',
    prazdne: 'Pre túto oblasť zatiaľ nie je žiadny vzor.',
    info: (o, n) => `${o}: ${n} ${T.pocet(n)} · zvýraznené sú časti z tejto oblasti`,
  },
  en: {
    vzor: 'Model', zad: 'Questions', vyp: 'Solutions',
    linkZ: n => `Model${n}_questions.html`, linkV: n => `Model${n}_solutions.html`,
    pocet: n => n === 1 ? 'model' : 'models',
    tema: 'topic.html', otvorit: c => `Open all parts (${c}) →`,
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
          <div class="part-t"><a href="${T.linkZ(q.n)}?cast=${i + 1}">${esc(c[LANG][0])}</a></div>
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
  const c = k ? OTAZKY.reduce((s, q) => s + q.casti.filter(x => x.o.includes(k)).length, 0) : 0;
  $('info').innerHTML = k
    ? `<span>${esc(T.info(nazov(k), n))}</span><a class="info-link" href="${T.tema}?o=${k}">${T.otvorit(c)}</a>`
    : '';
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
