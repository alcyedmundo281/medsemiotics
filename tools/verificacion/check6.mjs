import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];
const css = fs.readFileSync(path.join(REPO, 'assets/tailwind.css'), 'utf8');

// Vacía los cuerpos de regla para quedarnos con los selectores, y recoge toda
// clase en cualquier posición: .a .b\:c, .group:hover .group-hover\:x, etc.
const selectorPart = css.replace(/\{[^{}]*\}/g, '{}');
const present = new Set();
const CLASS_IN_SEL = /\.((?:[A-Za-z0-9_-]|\\[^\\])+)/g;
for (const m of selectorPart.matchAll(CLASS_IN_SEL)) {
  present.add(m[1].replace(/\\(.)/g, '$1'));
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
const TW = /^(?:-?(?:bg|text|border|divide|ring|shadow|drop-shadow|from|via|to|fill|stroke|p|px|py|pt|pb|pl|pr|m|mx|my|mt|mb|ml|mr|w|h|min-w|min-h|max-w|max-h|gap|grid-cols|grid-rows|col-span|row-span|flex|basis|grow|shrink|order|items|justify|self|place|rounded|opacity|font|leading|tracking|z|top|left|right|bottom|inset|space-x|space-y|translate-x|translate-y|scale|rotate|skew|origin|blur|brightness|contrast|saturate|backdrop|transition|duration|delay|ease|animate|cursor|select|resize|overflow|whitespace|break|list|align|table|object|aspect|columns|indent|decoration|underline|line-clamp|prose|container|block|inline|hidden|absolute|relative|fixed|sticky|static|visible|invisible|isolate|float|clear|box|truncate|uppercase|lowercase|capitalize|italic|antialiased|sr-only)(?:-|$|\/|\[))/;

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
      if (!TW.test(base)) continue;
      total++;
      if (present.has(tok) || present.has(base)) continue;
      if (!missing.has(tok)) missing.set(tok, new Set());
      missing.get(tok).add(rel);
    }
  }
}

console.log(JSON.stringify({
  utilidades_comprobadas: total,
  selectores_en_css: present.size,
  FALTAN: missing.size,
  detalle: [...missing.entries()].map(([c, p]) => ({ clase: c, paginas: [...p] })),
}, null, 2));
