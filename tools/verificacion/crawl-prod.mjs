// Extrae toda referencia local de las páginas publicadas, la resuelve y la pide
// a producción. Es la prueba real de caja de nombres y de enlaces rotos.
import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';

const REPO = process.argv[2];
const BASE = process.argv[3];
process.chdir(REPO);

const pages = execSync('git ls-files "*.html"', { encoding: 'utf8' })
  .split('\n').map((s) => s.trim()).filter(Boolean);

const REF = /(?:href|src)\s*=\s*["']([^"'\s>]+)["']|url\(\s*['"]?([^'")\s]+)['"]?\s*\)/g;
const refs = new Map();   // url -> paginas que la piden
const externals = new Map();

for (const page of pages) {
  const dir = path.posix.dirname(page.replace(/\\/g, '/'));
  const txt = fs.readFileSync(page, 'utf8');
  for (const m of txt.matchAll(REF)) {
    let r = (m[1] ?? m[2] ?? '').trim();
    if (!r) continue;
    if (r.includes('${') || r.includes('{{')) continue;      // plantillas
    if (/^(data:|blob:|mailto:|tel:|javascript:|#)/i.test(r)) continue;
    if (/^https?:\/\//i.test(r)) {
      const h = new URL(r).hostname;
      if (!externals.has(h)) externals.set(h, new Set());
      externals.get(h).add(page);
      continue;
    }
    if (r.startsWith('//')) continue;
    const clean = r.split('#')[0].split('?')[0];
    if (!clean) continue;
    let resolved;
    if (clean.startsWith('/')) resolved = clean.replace(/^\//, '');   // absoluta: relativa al dominio
    else resolved = path.posix.normalize(path.posix.join(dir === '.' ? '' : dir, clean));
    if (resolved.startsWith('..')) continue;
    const key = (clean.startsWith('/') ? 'ABS:' : '') + resolved;
    if (!refs.has(key)) refs.set(key, new Set());
    refs.get(key).add(page);
  }
}

const list = [...refs.keys()];
console.error(`referencias locales distintas: ${list.length}`);

async function head(url) {
  for (let i = 0; i < 3; i++) {
    try {
      const r = await fetch(url, { method: 'HEAD', redirect: 'manual' });
      return r.status;
    } catch { await new Promise((r) => setTimeout(r, 400)); }
  }
  return 0;
}

const bad = [];
const CONC = 10;
let idx = 0;
async function worker() {
  while (idx < list.length) {
    const key = list[idx++];
    const isAbs = key.startsWith('ABS:');
    const p = isAbs ? key.slice(4) : key;
    // las absolutas cuelgan del dominio, no del prefijo del proyecto
    const url = isAbs
      ? `${new URL(BASE).origin}/${p}`
      : `${BASE}/${p}`;
    const st = await head(url);
    if (st !== 200 && st !== 301 && st !== 302) {
      bad.push({ url, status: st, pedida_por: [...refs.get(key)].slice(0, 3) });
    }
  }
}
await Promise.all(Array.from({ length: CONC }, worker));

console.log(JSON.stringify({
  referencias_locales: list.length,
  fallos: bad.length,
  detalle: bad,
  hosts_externos: [...externals.entries()].map(([h, p]) => ({ host: h, paginas: p.size })),
}, null, 2));
