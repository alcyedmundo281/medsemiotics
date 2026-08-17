// Extrae clases SOLO de atributos class/className (incluido dentro de strings
// JS), y comprueba cuáles faltan en el tailwind.css local.
import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];
const css = fs.readFileSync(path.join(REPO, 'assets/tailwind.css'), 'utf8');

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

// class="..." | className="..." | className={`...`} | class="${x} literal"
const ATTR = /\bclass(?:Name)?\s*=\s*(?:"([^"]*)"|'([^']*)'|\{`([^`]*)`\}|`([^`]*)`)/g;

const missing = new Map();
const seen = new Set();

for (const f of cdnPages) {
  const rel = path.relative(REPO, f).replace(/\\/g, '/');
  const txt = fs.readFileSync(f, 'utf8');
  for (const m of txt.matchAll(ATTR)) {
    const raw = m[1] ?? m[2] ?? m[3] ?? m[4] ?? '';
    // quita las interpolaciones ${...}: su contenido se analiza aparte
    const cleaned = raw.replace(/\$\{[^}]*\}/g, ' ');
    for (const tok of cleaned.split(/\s+/)) {
      if (!tok) continue;
      // separa variantes: hover:bg-x -> comprobamos la utilidad final
      const base = tok.includes(':') ? tok.slice(tok.lastIndexOf(':') + 1) : tok;
      if (!base || base.length < 2) continue;
      if (!/^[a-z!-]/.test(base)) continue;
      seen.add(base);
      if (present.has(base) || present.has(tok)) continue;
      if (!missing.has(base)) missing.set(base, new Set());
      missing.get(base).add(rel);
    }
  }
}

// Clases completas que viven dentro de literales JS (los ternarios del punto A)
const STRLIT = /['"`]((?:(?:bg|text|border|from|via|to|ring|shadow|fill|stroke)-[a-z0-9/\[\].-]+\s*)+)['"`]/g;
const fromJs = new Map();
for (const f of cdnPages) {
  const rel = path.relative(REPO, f).replace(/\\/g, '/');
  const txt = fs.readFileSync(f, 'utf8');
  for (const m of txt.matchAll(STRLIT)) {
    for (const tok of m[1].trim().split(/\s+/)) {
      const base = tok.includes(':') ? tok.slice(tok.lastIndexOf(':') + 1) : tok;
      if (present.has(base) || present.has(tok)) continue;
      if (!fromJs.has(base)) fromJs.set(base, new Set());
      fromJs.get(base).add(rel);
    }
  }
}

const arb = [...missing.keys()].filter((c) => c.includes('['));
const plain = [...missing.keys()].filter((c) => !c.includes('['));

console.log(JSON.stringify({
  paginas: cdnPages.length,
  clases_distintas_usadas: seen.size,
  FALTAN_total: missing.size,
  FALTAN_arbitrarias: arb.length,
  FALTAN_planas: plain.length,
  arbitrarias: arb.sort(),
  planas: plain.sort(),
  faltan_en_literales_JS: [...fromJs.keys()].sort(),
}, null, 2));
