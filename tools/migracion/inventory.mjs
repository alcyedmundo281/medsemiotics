// Extrae y compara los tailwind.config en línea de las páginas que usan el CDN.
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const REPO = process.argv[2];

function walk(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (e.name === '.git' || e.name === 'node_modules') continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, a);
    else if (e.name.endsWith('.html')) a.push(p);
  }
  return a;
}

const pages = walk(REPO).filter((f) => fs.readFileSync(f, 'utf8').includes('cdn.tailwindcss.com'));
const configs = {};
const noConfig = [];
const plugins = {};

for (const f of pages) {
  const rel = path.relative(REPO, f).replace(/\\/g, '/');
  const html = fs.readFileSync(f, 'utf8');

  const pm = html.match(/cdn\.tailwindcss\.com\?plugins=([^"']+)/);
  plugins[rel] = pm ? pm[1].split(',').sort().join(',') : '(ninguno)';

  // El bloque puede ser <script id="tailwind-config"> o un <script> suelto
  // que asigna tailwind.config = {...}
  const m = html.match(/tailwind\.config\s*=\s*(\{[\s\S]*?\n\s*\})\s*(?:<\/script>|;?\s*<\/script>)/);
  if (!m) { noConfig.push(rel); continue; }
  try {
    const obj = vm.runInNewContext('(' + m[1] + ')');
    configs[rel] = obj;
  } catch (e) {
    noConfig.push(rel + '  [NO PARSEABLE: ' + e.message.slice(0, 50) + ']');
  }
}

// Aplana el objeto a rutas -> valor
function flat(o, prefix = '', out = {}) {
  for (const [k, v] of Object.entries(o || {})) {
    const key = prefix ? prefix + '.' + k : k;
    if (v && typeof v === 'object' && !Array.isArray(v)) flat(v, key, out);
    else out[key] = Array.isArray(v) ? JSON.stringify(v) : String(v);
  }
  return out;
}

const byKey = {};
for (const [page, cfg] of Object.entries(configs)) {
  for (const [k, v] of Object.entries(flat(cfg))) {
    (byKey[k] ||= {});
    (byKey[k][v] ||= []).push(page);
  }
}

const collisions = {};
const agreed = {};
for (const [k, vals] of Object.entries(byKey)) {
  if (Object.keys(vals).length > 1) collisions[k] = vals;
  else agreed[k] = { valor: Object.keys(vals)[0], paginas: Object.values(vals)[0].length };
}

console.log(JSON.stringify({
  paginas_con_config: Object.keys(configs).length,
  paginas_sin_config: noConfig,
  plugins_por_pagina: plugins,
  claves_en_conflicto: collisions,
  claves_sin_conflicto: agreed,
}, null, 2));
