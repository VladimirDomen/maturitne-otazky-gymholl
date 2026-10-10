/* ============================================
   FYZIKA — VZOROVÉ ZADANIA — zobrazenie jednej časti
   Adresa …_zadanie.html?cast=2 ukáže (aj vytlačí) len časť 2.
   Prepínač Zadanie/Vypracovanie a SK/EN si časť zapamätá.
   Používajú ho všetky stránky vzorov (SK aj EN).
   ============================================ */
(function () {
  const en = document.documentElement.lang === 'en';
  const T = en
    ? { len: 'Showing only part', z: 'of', cela: 'Show the whole model', pred: k => `‹ Part ${k}`, dalej: k => `Part ${k} ›` }
    : { len: 'Zobrazená je len časť', z: 'z', cela: 'Zobraziť celý vzor', pred: k => `‹ Časť ${k}`, dalej: k => `Časť ${k} ›` };

  const casti = [...document.querySelectorAll('section.sheet')];
  const n = parseInt(new URLSearchParams(location.search).get('cast'), 10);
  if (!(n >= 1 && n <= casti.length)) return;

  document.body.classList.add('jedna-cast');
  casti[n - 1].classList.add('vybrana');

  // prepínače Zadanie/Vypracovanie a SK/EN zachovajú vybranú časť
  document.querySelectorAll('.mo-switch a, a.mo-lang').forEach(a =>
    a.setAttribute('href', a.getAttribute('href').split('?')[0] + '?cast=' + n));

  const subor = location.pathname.split('/').pop();
  const link = k => subor + (k ? '?cast=' + k : '');
  const nazov = (casti[n - 1].querySelector('h2')?.textContent || '').replace(/^\d+\.\s*/, '');
  const lista = document.createElement('div');
  lista.className = 'mo-cast';
  lista.innerHTML =
    `<span><b>${T.len} ${n} ${T.z} ${casti.length}</b> · ${nazov}</span>` +
    `<span class="mo-cast-nav">` +
    (n > 1 ? `<a href="${link(n - 1)}">${T.pred(n - 1)}</a>` : '') +
    (n < casti.length ? `<a href="${link(n + 1)}">${T.dalej(n + 1)}</a>` : '') +
    `<a class="mo-cela" href="${link(0)}">${T.cela}</a></span>`;
  document.querySelector('main.wrap').prepend(lista);
})();
