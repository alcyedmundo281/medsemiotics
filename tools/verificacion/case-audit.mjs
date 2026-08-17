// Windows no distingue mayúsculas; GitHub Pages sí. Comprueba que la caja de
// cada referencia local coincide EXACTAMENTE con el nombre real del archivo.
import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';

const REPO = process.argv[2];
process.chdir(REPO);

// Índice de rutas reales tal y como las tiene git (respeta la caja).
const tracked = execSync('git ls-files', { encoding: 'utf8', maxBuffer: 1e8 })
  .split('\n').map((s) => s.trim()).filter(Boolean);
const exact = new Set(tracked);
const lower = new Map();
for (const f of tracked) lower.set(f.toLowerCase(), f);

function walk(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (['.git', 'node_modules'].includes(e.name)) continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, a);
    else if (/\.(html|css|js|jsx)$/.test(e.name)) a.push(p);
  }
  return a;
}

const REF = /(?:href|src)\s*=\s*["']([^"'#?]+)["']|url\(\s*['"]?([^'")?#]+)['"]?\s*\)/g;

const caseIssues = [];
const missing = [];

for (const file of walk('.')) {
  const rel = path.relative('.', file).replace(/\\/g, '/');
  const dir = path.posix.dirname(rel);
  const txt = fs.readFileSync(file, 'utf8');
  for (const m of txt.matchAll(REF)) {
    let ref = (m[1] ?? m[2] ?? '').trim();
    if (!ref) continue;
    if (/^(https?:|data:|mailto:|tel:|blob:|javascript:|#|\/\/)/i.test(ref)) continue;
    if (ref.startsWith('/')) continue;      // absolutas: se tratan aparte
    const resolved = path.posix.normalize(path.posix.join(dir, ref));
    if (resolved.startsWith('..')) continue;
    // los directorios se resuelven a index.html
    const cands = [resolved, path.posix.join(resolved, 'index.html')];
    if (cands.some((c) => exact.has(c))) continue;
    const hit = cands.map((c) => lower.get(c.toLowerCase())).find(Boolean);
    if (hit) caseIssues.push({ archivo: rel, ref, real: hit });
    else if (!fs.existsSync(resolved)) missing.push({ archivo: rel, ref, resuelto: resolved });
  }
}

// Colisiones de caja entre archivos del propio repo
const dupes = {};
for (const f of tracked) {
  const k = f.toLowerCase();
  (dupes[k] ||= []).push(f);
}
const collisions = Object.values(dupes).filter((v) => v.length > 1);

console.log(JSON.stringify({
  referencias_con_caja_incorrecta: caseIssues,
  referencias_a_archivos_inexistentes: missing.slice(0, 40),
  total_inexistentes: missing.length,
  colisiones_de_caja_en_el_repo: collisions,
}, null, 2));
