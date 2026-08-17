// Genera el sitemap de medsemiotics a partir de las páginas versionadas.
// Se excluyen los 6 índices de sección: son redirecciones con noindex, y anunciar
// en el sitemap una URL que pide no ser indexada es una contradicción que Search
// Console marca como incidencia.
import fs from 'node:fs';
import { execSync } from 'node:child_process';

const BASE = 'https://powersemiotics.com/medsemiotics/';
const REDIRECCIONES = new Set([
  'neurologia/index.html',
  'gastroenterologia/index.html',
  'farmacoterapia_racional/index.html',
  'medicina_y_datos/index.html',
  'medicina_e_implementacion/index.html',
  'inmunologia/index.html',
]);

const paginas = execSync('git ls-files "*.html"', { encoding: 'utf8' })
  .split('\n').map((s) => s.trim().split('\\').join('/')).filter(Boolean);

const incluidas = paginas.filter((p) => !REDIRECCIONES.has(p));

function url(p) {
  if (p === 'index.html') return BASE;
  if (p.endsWith('/index.html')) return BASE + p.slice(0, -'index.html'.length);
  return BASE + p;
}

// Fecha del último commit que tocó cada archivo: más honesto que la fecha de hoy.
function fecha(p) {
  try {
    const d = execSync(`git log -1 --format=%cs -- "${p}"`, { encoding: 'utf8' }).trim();
    return d || new Date().toISOString().slice(0, 10);
  } catch { return new Date().toISOString().slice(0, 10); }
}

const entradas = incluidas.map((p) => {
  const prioridad = p === 'index.html' ? '1.0'
    : !p.includes('/') ? '0.8'
    : '0.6';
  return `  <url>\n    <loc>${url(p)}</loc>\n    <lastmod>${fecha(p)}</lastmod>\n    <priority>${prioridad}</priority>\n  </url>`;
}).join('\n');

const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${entradas}\n</urlset>\n`;
fs.writeFileSync('sitemap.xml', xml.replace(/\n/g, '\r\n'), 'utf8');

console.log(`sitemap.xml: ${incluidas.length} URLs (de ${paginas.length} páginas; ${REDIRECCIONES.size} redirecciones excluidas)`);
