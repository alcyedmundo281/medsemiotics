// Inserta o normaliza el <link rel="canonical"> absoluto en cada página,
// respetando el final de línea que ya tenga el archivo.
import fs from 'node:fs';
import { execSync } from 'node:child_process';

const BASE = 'https://powersemiotics.com/medsemiotics/';
const paginas = execSync('git ls-files "*.html"', { encoding: 'utf8' })
  .split('\n').map((s) => s.trim()).filter(Boolean);

// Los índices de sección son redirecciones: su canónica apunta al hub.
const HUB = {
  neurologia: 'neurologia.html',
  gastroenterologia: 'gastroenterologia.html',
  farmacoterapia_racional: 'farmacoterapia_racional.html',
  medicina_y_datos: 'medicina_y_datos.html',
  medicina_e_implementacion: 'medicina_e_implementacion.html',
  inmunologia: 'inmunologia_clinica.html',
};

function canonicalDe(p) {
  const r = p.split('\\').join('/');
  const m = r.match(/^([^/]+)\/index\.html$/);
  if (m && HUB[m[1]]) return BASE + HUB[m[1]];
  if (r === 'index.html') return BASE;
  if (r.endsWith('/index.html')) return BASE + r.slice(0, -'index.html'.length);
  return BASE + r;
}

let insertados = 0, sustituidos = 0;
const sinSitio = [];

for (const p of paginas) {
  const buf = fs.readFileSync(p);
  const crlf = buf.includes(13);
  const nl = crlf ? '\r\n' : '\n';
  let s = buf.toString('utf8');
  const tag = `<link rel="canonical" href="${canonicalDe(p)}" />`;

  if (/<link\s+rel="canonical"[^>]*\/?>/i.test(s)) {
    s = s.replace(/<link\s+rel="canonical"[^>]*\/?>/i, tag);
    sustituidos++;
  } else if (/<\/title>/i.test(s)) {
    s = s.replace(/<\/title>/i, (m2) => m2 + nl + '    ' + tag);
    insertados++;
  } else if (/<\/head>/i.test(s)) {
    s = s.replace(/<\/head>/i, '  ' + tag + nl + '</head>');
    insertados++;
  } else {
    sinSitio.push(p);
    continue;
  }
  fs.writeFileSync(p, s, 'utf8');
}

console.log(`canonical insertados: ${insertados}  sustituidos: ${sustituidos}  sin sitio: ${sinSitio.length}`);
if (sinSitio.length) console.log('  ' + sinSitio.join('\n  '));
