// Comprueba el token de clase COMPLETO (con sus variantes) contra todos los
// selectores del CSS, incluidos los que viven dentro de @media.
import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];
const css = fs.readFileSync(path.join(REPO, 'assets/tailwind.css'), 'utf8');

// Todas las clases que aparecen en CUALQUIER posición de un selector,
// incluidas .group:hover .group-hover\:x y las que viven dentro de @media.
const present = new Set();
const selectorPart = css.replace(/\{[^{}]*\}/g, '{}');
for (const m of selectorPart.matchAll(/\.((?:[A-Za-z0-9_-]|\.)+)/g)) {
  present.add(m[1].replace(/\(.)/g, '$1'));
}

function walk(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (e.name === '.git' || e.name === 'node_modules' || e.name === 'dist') continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, a);
    else if (e.name.endsWith('.html') || e.name.endsWith('.jsx')) a.push(p);
  }
  return a;
}

const ATTR = /\bclass(?:Name)?\s*=\s*(?:"([^"]*)"|'([^']*)'|\{`([^`]*)`\}|`([^`]*)`)/g;
// Prefijos que identifican una utilidad de Tailwind (no una clase propia).
const TW = /^(?:-?(?:bg|text|border|divide|ring|shadow|drop-shadow|from|via|to|fill|stroke|p|px|py|pt|pb|pl|pr|m|mx|my|mt|mb|ml|mr|w|h|min-w|min-h|max-w|max-h|gap|grid-cols|grid-rows|col-span|row-span|flex|basis|grow|shrink|order|items|justify|self|place|content|rounded|opacity|font|leading|tracking|z|top|left|right|bottom|inset|space-x|space-y|translate-x|translate-y|scale|rotate|skew|origin|blur|brightness|contrast|saturate|backdrop|transition|duration|delay|ease|animate|cursor|select|resize|overflow|whitespace|break|list|align|table|object|aspect|columns|indent|decoration|underline|line-clamp|prose|form|container|block|inline|hidden|absolute|relative|fixed|sticky|static|visible|invisible|isolate|float|clear|box|truncate|uppercase|lowercase|capitalize|italic|antialiased|sr-only|not-sr-only|no-underline)(?:-|$|\/|\[))/;

const missing = new Map();
let total = 0;
for (const f of walk(REPO)) {
  const rel = path.relative(REPO, f).replace(/\\/g, '/');
  const txt = fs.readFileSync(f, 'utf8');
  for (const m of txt.matchAll(ATTR)) {
    const raw = (m[1] ?? m[2] ?? m[3] ?? m[4] ?? '').replace(/\$\{[^}]*\}/g, ' ');
    for (const tok of raw.split(/\s+/)) {
      if (!tok) continue;
      const base = tok.includes(':') ? tok.slice(tok.lastIndexOf(':') + 1) : tok;
      if (!TW.test(base)) continue;      // clase propia de la página: ignorar
      total++;
      if (present.has(tok) || present.has(base)) continue;
      if (!missing.has(tok)) missing.set(tok, new Set());
      missing.get(tok).add(rel);
    }
  }
}

const out = [...missing.entries()].map(([c, pages]) => ({ clase: c, paginas: [...pages] }));
console.log(JSON.stringify({
  utilidades_tailwind_comprobadas: total,
  selectores_en_css: present.size,
  FALTAN: out.length,
  detalle: out.slice(0, 60),
}, null, 2));
