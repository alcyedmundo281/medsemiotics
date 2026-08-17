import fs from 'node:fs';
const S = process.argv[2];
const a = JSON.parse(fs.readFileSync(S + '/base.json', 'utf8'));
const b = JSON.parse(fs.readFileSync(S + '/after.json', 'utf8'));

const CONTROL = ['index.html', 'neurologia.html', 'gastroenterologia.html',
  'medicina_y_datos.html', 'neurologia/cefaleas/index.html'];
const REACT = ['gastroenterologia/trastornos-estomacales.html',
  'inmunologia/alergias-alimentarias.html', 'inmunologia/hipersensibilidad-farmacos.html',
  'inmunologia/inmunologia-trasplante.html', 'inmunologia/laboratorio-inmunologia.html',
  'inmunologia/vacunas.html', 'neurologia/acv-isquemico.html',
  'neurologia/epilepsia-ii/masterclass.html'];

const rows = [];
for (const page of Object.keys(a)) {
  const A = a[page], B = b[page];
  const tipo = CONTROL.includes(page) ? 'CONTROL' : 'MIGRADA';

  const fontDiff = [];
  for (const k of ['body', 'h1', 'h2', 'h3', 'p']) {
    const x = A[k], y = B[k];
    if (!x && !y) continue;
    if (!x || !y) { fontDiff.push(`${k}: ${x ? 'existia' : 'no existia'} -> ${y ? 'existe' : 'no existe'}`); continue; }
    if (x.font !== y.font) fontDiff.push(`${k}.fuente ${x.font} -> ${y.font}`);
    if (x.size !== y.size) fontDiff.push(`${k}.tam ${x.size} -> ${y.size}`);
    if (x.color !== y.color) fontDiff.push(`${k}.color ${x.color} -> ${y.color}`);
    if (x.weight !== y.weight) fontDiff.push(`${k}.peso ${x.weight} -> ${y.weight}`);
  }

  // diff de la muestra de estilos computados
  const sa = A.sample || [], sb = B.sample || [];
  const changed = [];
  for (let i = 0; i < Math.min(sa.length, sb.length); i++) {
    if (sa[i] !== sb[i]) {
      const pa = sa[i].split('|'), pb = sb[i].split('|');
      const campos = ['sel', 'fuente', 'tam', 'peso', 'color', 'fondo', 'display', 'caja'];
      const d = [];
      for (let j = 1; j < campos.length; j++) if (pa[j] !== pb[j]) d.push(`${campos[j]}: ${pa[j]} -> ${pb[j]}`);
      if (d.length) changed.push(pa[0].slice(0, 46) + ' :: ' + d.join(', '));
    }
  }

  rows.push({
    page, tipo,
    scrollH: `${A.scrollH} -> ${B.scrollH}`,
    deltaH: (B.scrollH ?? 0) - (A.scrollH ?? 0),
    tipografia: fontDiff,
    elementos_cambiados: changed.length,
    ejemplos: changed.slice(0, 5),
    react: REACT.includes(page) ? `#root hijos ${A.rootHasContent} -> ${B.rootHasContent}` : null,
    externas: B.externals,
    errores: B.errors.filter((e) => !/favicon/i.test(e)),
  });
}

fs.writeFileSync(S + '/diff.json', JSON.stringify(rows, null, 2));

console.log('=== CONTROL (no deben cambiar) ===');
for (const r of rows.filter((r) => r.tipo === 'CONTROL')) {
  console.log(`${r.page.padEnd(34)} dH=${String(r.deltaH).padStart(5)}  elem_cambiados=${String(r.elementos_cambiados).padStart(3)}  tipo=${r.tipografia.length ? r.tipografia.join('; ') : 'sin cambios'}  ext=${r.externas.length}`);
}
console.log('\n=== REACT ===');
for (const r of rows.filter((r) => r.react)) {
  console.log(`${r.page.padEnd(46)} ${r.react}  errores=${r.errores.length}  ext=${r.externas.length}`);
}
console.log('\n=== MIGRADAS: tipografia y cajas ===');
for (const r of rows.filter((r) => r.tipo === 'MIGRADA')) {
  console.log(`${r.page.padEnd(56)} dH=${String(r.deltaH).padStart(5)} elem=${String(r.elementos_cambiados).padStart(3)} ext=${r.externas.length} err=${r.errores.length}`);
  if (r.tipografia.length) console.log('    TIPO: ' + r.tipografia.join(' | '));
}
console.log('\n=== TOTAL peticiones externas: ' +
  rows.reduce((s, r) => s + r.externas.length, 0) + ' ===');
