/* ============================================
   FYZIKA — VZOROVÉ ZADANIA — všetky časti jednej oblasti
   tema.html?o=elektrina (SK), en/topic.html?o=elektrina (EN);
   &v=1 = vypracovania namiesto zadaní.
   Časti sa načítajú priamo zo stránok vzorov (fetch), takže pri novom
   vzore stačí záznam v data.js.
   ============================================ */
(function () {
  const en = LANG === 'en';
  const T = en ? {
    self: 'topic.html', other: '../tema.html',
    linkZ: n => `Model${n}_questions.html`, linkV: n => `Model${n}_solutions.html`,
    oblast: 'Area', zad: 'Questions', vyp: 'Solutions', vzor: 'Model', cast: 'part',
    pocet: (c, v) => `${c} ${c === 1 ? 'part' : 'parts'} from ${v} ${v === 1 ? 'model' : 'models'}`,
    nacitavam: 'Loading…', chyba: 'This part could not be loaded.',
    nic: 'Unknown area. Go back to the overview and choose an area in the filter.',
    obsah: 'Contents', title: 'Worked Examples in Physics',
  } : {
    self: 'tema.html', other: 'en/topic.html',
    linkZ: n => `Vzor${n}_zadanie.html`, linkV: n => `Vzor${n}_vypracovanie.html`,
    oblast: 'Oblasť', zad: 'Zadania', vyp: 'Vypracovania', vzor: 'Vzor', cast: 'časť',
    pocet: (c, v) => `${c} ${c === 1 ? 'časť' : c < 5 ? 'časti' : 'častí'} z ${v} ${v === 1 ? 'vzoru' : 'vzorov'}`,
    nacitavam: 'Načítavam…', chyba: 'Túto časť sa nepodarilo načítať.',
    nic: 'Neznáma oblasť. Vráťte sa na prehľad a vyberte oblasť vo filtri.',
    obsah: 'Obsah', title: 'Vzorové zadania z fyziky',
  };

  const $ = id => document.getElementById(id);
  const par = new URLSearchParams(location.search);
  const k = par.get('o');
  const vyp = par.get('v') === '1';
  const main = document.querySelector('main.wrap');

  if (!OBLASTI[k]) { main.innerHTML = `<div class="mo-cast">${T.nic}</div>`; return; }

  const nazov = OBLASTI[k][LANG];
  const zoznam = OTAZKY.flatMap(q => q.casti.map((c, i) => ({ n: q.n, i: i + 1, spolu: q.casti.length, c })))
    .filter(x => x.c.o.includes(k));
  const vzorov = new Set(zoznam.map(x => x.n)).size;

  document.title = `${nazov} – ${vyp ? T.vyp : T.zad} · ${T.title}`;
  document.body.classList.add(vyp ? 'vyp' : 'zad');
  $('t-kind').textContent = vyp ? T.vyp : T.zad;
  $('t-h1').textContent = nazov;
  $('t-p').textContent = T.pocet(zoznam.length, vzorov);
  document.querySelector('.mo-head').style.setProperty('--oblast', OBLASTI[k].farba);

  const q = v => `?o=${encodeURIComponent(k)}${v ? '&v=1' : ''}`;
  $('t-zad').href = T.self + q(false);
  $('t-vyp').href = T.self + q(true);
  (vyp ? $('t-vyp') : $('t-zad')).classList.add('on');
  $('t-lang').href = T.other + q(vyp);

  // obsah + miesta pre časti (poradie podľa data.js)
  main.innerHTML =
    `<nav class="mo-cast t-obsah"><b>${T.obsah}:</b><span class="mo-cast-nav">` +
    zoznam.map((x, j) => `<a href="#t-${j + 1}">${T.vzor} ${x.n} · ${x.c[LANG][0]}</a>`).join('') +
    `</span></nav>` +
    zoznam.map((x, j) => `<section class="sheet" id="t-${j + 1}"><div class="topline">${T.nacitavam}</div></section>`).join('');

  const stranky = {};
  const nacitaj = subor => stranky[subor] ||= fetch(subor).then(r => {
    if (!r.ok) throw new Error(r.status);
    return r.text();
  }).then(html => new DOMParser().parseFromString(html, 'text/html'));

  zoznam.forEach((x, j) => {
    const subor = vyp ? T.linkV(x.n) : T.linkZ(x.n);
    const ciel = $(`t-${j + 1}`);
    nacitaj(subor).then(doc => {
      const sec = doc.getElementById(`cast-${x.i}`);
      if (!sec) throw new Error('cast');
      sec.querySelector('.topline')?.remove();
      // id v obrázkoch (napr. šípky) musia byť na stránke jedinečné
      const pre = `t${j + 1}-`;
      sec.querySelectorAll('[id]').forEach(el => {
        const stare = el.id, nove = pre + stare;
        el.id = nove;
        sec.querySelectorAll('*').forEach(e => [...e.attributes].forEach(a => {
          if (a.value.includes(`#${stare}`)) a.value = a.value.split(`url(#${stare})`).join(`url(#${nove})`).replace(new RegExp(`^#${stare}$`), `#${nove}`);
        }));
      });
      ciel.innerHTML =
        `<div class="topline"><a href="${subor}?cast=${x.i}">${T.vzor} ${x.n} · ${T.cast} ${x.i}/${x.spolu}</a></div>` +
        sec.innerHTML;
    }).catch(() => {
      ciel.innerHTML = `<div class="topline">${T.vzor} ${x.n} · ${T.cast} ${x.i}/${x.spolu}</div><p>${T.chyba} <a href="${subor}?cast=${x.i}">${subor}</a></p>`;
    });
  });
})();
