// ¿Qué clases usadas en las 23 páginas del CDN de Tailwind NO están en el
// tailwind.css local? Esa es la deuda real del punto C.
import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];
const css = fs.readFileSync(path.join(REPO, 'assets/tailwind.css'), 'utf8');

// Selectores de clase presentes en el CSS, desescapados.
const present = new Set();
for (const m of css.matchAll(/^\.((?:[^\s{,:]|\\.)+)/gm)) {
  present.add(m[1].replace(/\\(.)/g, '$1'));
}

function walk(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (e.name === '.git' || e.name === 'node_modules' || e.name === 'dist') continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, a);
    else if (e.name.endsWith('.html')) a.push(p);
  }
  return a;
}

const cdnPages = walk(REPO).filter((f) =>
  fs.readFileSync(f, 'utf8').includes('cdn.tailwindcss.com'));

// Extrae candidatos como lo hace Tailwind: cualquier token plausible.
const CANDIDATE = /[a-z][a-z0-9]*(?:-[a-z0-9.]+)*(?:-\[[^\]\s"'`]+\])?(?:\/[0-9]+)?/g;
const PREFIXES = /^(bg|text|border|p|px|py|pt|pb|pl|pr|m|mx|my|mt|mb|ml|mr|w|h|min|max|gap|grid|flex|items|justify|rounded|shadow|opacity|font|leading|tracking|z|top|left|right|bottom|inset|space|divide|ring|outline|transition|duration|delay|ease|animate|transform|scale|rotate|translate|skew|origin|cursor|select|resize|overflow|whitespace|break|truncate|list|align|table|order|col|row|object|fill|stroke|blur|brightness|contrast|grayscale|invert|saturate|sepia|backdrop|from|via|to|sr|not|placeholder|caret|accent|decoration|underline|uppercase|lowercase|capitalize|italic|antialiased|container|block|inline|hidden|absolute|relative|fixed|sticky|static|visible|invisible|isolate|float|clear|box|aspect|columns|basis|grow|shrink|self|content|place|indent|align)(-|$)/;

const missing = new Map();
for (const f of cdnPages) {
  const rel = path.relative(REPO, f).replace(/\\/g, '/');
  const txt = fs.readFileSync(f, 'utf8');
  for (const m of txt.matchAll(CANDIDATE)) {
    let c = m[0];
    if (!PREFIXES.test(c)) continue;
    if (c.length < 3 || c.endsWith('-')) continue;
    // quita variantes (hover:, md:, dark:) — buscamos la utilidad base
    if (present.has(c)) continue;
    if (!missing.has(c)) missing.set(c, new Set());
    missing.get(c).add(rel);
  }
}

// También comprobamos las variantes con prefijo tal cual aparecen en el HTML
const arbitrary = [...missing.keys()].filter((c) => c.includes('['));
const plain = [...missing.keys()].filter((c) => !c.includes('['));

console.log(JSON.stringify({
  paginas_cdn: cdnPages.length,
  selectores_en_css: present.size,
  candidatos_ausentes_total: missing.size,
  ausentes_arbitrarios: arbitrary.length,
  ausentes_planos: plain.length,
  muestra_arbitrarios: arbitrary.slice(0, 25),
  muestra_planos: plain.slice(0, 40),
}, null, 2));
