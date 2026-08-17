// Diff de estilos computados alineando por SELECTOR, no por índice: añadir una
// clase al <body> desplazaba la muestra y producía diferencias falsas.
import fs from 'node:fs';
const S = process.argv[2];
const a = JSON.parse(fs.readFileSync(S + '/base.json', 'utf8'));
const b = JSON.parse(fs.readFileSync(S + '/after.json', 'utf8'));

const CONTROL = ['index.html', 'neurologia.html', 'gastroenterologia.html',
  'medicina_y_datos.html', 'neurologia/cefaleas/index.html'];
const CAMPOS = ['sel', 'fuente', 'tam', 'peso', 'color', 'fondo', 'display', 'caja'];

const rows = [];
for (const page of Object.keys(a)) {
  const A = a[page], B = b[page];
  const idx = (arr) => {
    const m = new Map();
    for (const s of arr || []) {
      const sel = s.split('|')[0];
      if (!m.has(sel)) m.set(sel, s);   // primera aparición de cada selector
    }
    return m;
  };
  const ma = idx(A.sample), mb = idx(B.sample);
  const changed = [];
  for (const [sel, va] of ma) {
    const vb = mb.get(sel);
    if (!vb) continue;                   // no medido en la otra corrida
    if (va === vb) continue;
    const pa = va.split('|'), pb = vb.split('|');
    const d = [];
    for (let j = 1; j < CAMPOS.length; j++) if (pa[j] !== pb[j]) d.push(`${CAMPOS[j]}: ${pa[j]} -> ${pb[j]}`);
    if (d.length) changed.push({ sel: sel.slice(0, 60), cambios: d });
  }
  rows.push({
    page,
    tipo: CONTROL.includes(page) ? 'CONTROL' : 'MIGRADA',
    deltaH: (B.scrollH ?? 0) - (A.scrollH ?? 0),
    n: changed.length,
    changed: changed.slice(0, 6),
    ext: B.externals.length,
  });
}
fs.writeFileSync(S + '/diff2.json', JSON.stringify(rows, null, 2));

console.log('PAGINA'.padEnd(58) + 'dH'.padStart(6) + '  elem_cambiados  externas');
for (const t of ['CONTROL', 'MIGRADA']) {
  console.log('\n--- ' + t + ' ---');
  for (const r of rows.filter((x) => x.tipo === t)) {
    console.log(r.page.padEnd(58) + String(r.deltaH).padStart(6) + String(r.n).padStart(15) + String(r.ext).padStart(10));
  }
}
console.log('\n=== detalle de los que cambiaron ===');
for (const r of rows.filter((x) => x.n > 0)) {
  console.log('\n### ' + r.page + '  (' + r.n + ')');
  r.changed.forEach((c) => console.log('   ' + c.sel + '\n      ' + c.cambios.join('; ')));
}
