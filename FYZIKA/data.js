/* ============================================
   FYZIKA — VZOROVÉ ZADANIA — dáta (SK aj EN)
   Používa ho rozcestník (rozcestnik.js) aj stránka oblasti (tema.js).
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
  vlnenie:     { sk: 'Kmitanie a vlnenie', en: 'Oscillations and waves', farba: '#2e8b57' },
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
  { n: 5, casti: [
    { o: ['mechanika'],
      sk: ['Dynamika', 'Newtonove zákony, hybnosť a jej zachovanie, dostredivá sila, zrýchlenie vlečky'],
      en: ['Dynamics', 'Newton’s laws, momentum and its conservation, centripetal force, acceleration of a trailer'] },
    { o: ['magnetizmus', 'elektrina'],
      sk: ['Elektromagnetická indukcia', 'Grafická úloha: z priebehu toku Φ(t) nakresliť indukované napätie'],
      en: ['Electromagnetic induction', 'Graphical task: induced voltage from the graph of flux Φ(t)'] },
    { o: ['mikrosvet'],
      sk: ['Jadrová elektráreň', 'Tlakovodný reaktor, primárny a sekundárny okruh, premeny energie'],
      en: ['Nuclear power plant', 'Pressurised water reactor, primary and secondary circuit, energy conversions'] },
  ]},
  { n: 6, casti: [
    { o: ['mechanika'],
      sk: ['Energia hmotného bodu', 'Práca, kinetická a potenciálna energia, zákon zachovania energie, výkon a účinnosť'],
      en: ['Energy of a particle', 'Work, kinetic and potential energy, conservation of energy, power and efficiency'] },
    { o: ['vlnenie'],
      sk: ['Oscilátor', 'Graf harmonického kmitania: amplitúda, perióda, fáza, rovnica, v_max a a_max'],
      en: ['Oscillator', 'Graph of harmonic oscillation: amplitude, period, phase, equation, v_max and a_max'] },
    { o: ['elektrina'],
      sk: ['Elektrický obvod', 'Meranie napätia a prúdu, overenie Ohmovho zákona, graf I = f(U)'],
      en: ['Electric circuit', 'Measuring voltage and current, verifying Ohm’s law, graph of I against U'] },
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
