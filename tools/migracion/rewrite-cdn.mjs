// Reescribe todas las referencias a CDN por rutas locales relativas.
// Preserva los finales de línea originales de cada archivo.
import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];
const DRY = process.argv.includes('--dry');

function walk(dir, acc = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.name === '.git' || e.name === 'node_modules') continue;
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, acc);
    else if (e.name.endsWith('.html')) acc.push(p);
  }
  return acc;
}

const files = walk(REPO);
const changes = [];

for (const file of files) {
  const original = fs.readFileSync(file, 'utf8');
  let s = original;

  // Prefijo relativo desde este archivo hasta la raíz del repo.
  const depth = path.relative(REPO, path.dirname(file)).split(path.sep).filter(Boolean).length;
  const up = depth === 0 ? '' : '../'.repeat(depth);
  const hits = [];

  const sub = (re, to, label) => {
    const before = s;
    s = s.replace(re, to);
    if (s !== before) hits.push(label);
  };

  // --- Font Awesome: 3 versiones -> build local 6.5.1 ---
  sub(
    /https:\/\/cdnjs\.cloudflare\.com\/ajax\/libs\/font-awesome\/[0-9.]+\/css\/all\.min\.css/g,
    `${up}assets/vendor/fontawesome/css/all.min.css`,
    'fontawesome',
  );

  // --- Google Fonts: el <link> al CSS pasa al CSS local de fuentes ---
  sub(
    /https:\/\/fonts\.googleapis\.com\/css2\?[^"'\s>]*/g,
    `${up}assets/fonts/fonts.css`,
    'googlefonts',
  );
  // preconnect/dns-prefetch a los hosts de Google ya no sirven para nada
  sub(
    /\s*<link[^>]*(?:rel=["'](?:preconnect|dns-prefetch)["'][^>]*fonts\.(?:googleapis|gstatic)\.com|fonts\.(?:googleapis|gstatic)\.com[^>]*rel=["'](?:preconnect|dns-prefetch)["'])[^>]*\/?>/g,
    '',
    'preconnect',
  );

  // --- Chart.js -> 4.4.0 local ---
  sub(
    /https:\/\/cdn\.jsdelivr\.net\/npm\/chart\.js(@[0-9.]+\/dist\/chart\.umd\.min\.js)?/g,
    `${up}assets/vendor/chartjs/chart.umd.min.js`,
    'chartjs',
  );

  // --- Lucide: @latest era una bomba de relojería ---
  sub(
    /https:\/\/unpkg\.com\/lucide-react@[^/]+\/dist\/umd\/lucide-react\.js/g,
    `${up}assets/vendor/lucide/lucide-react-0.263.1.umd.js`,
    'lucide-react',
  );
  sub(
    /https:\/\/unpkg\.com\/lucide-react@latest\/dist\/umd\/lucide\.min\.js/g,
    `${up}assets/vendor/lucide/lucide-react-0.263.1.umd.js`,
    'lucide-react',
  );
  sub(
    /https:\/\/unpkg\.com\/lucide@[^/]+\/dist\/umd\/lucide\.min\.js/g,
    `${up}assets/vendor/lucide/lucide-1.31.0.umd.min.js`,
    'lucide',
  );

  // --- Bootstrap 5.3.0 ---
  sub(
    /https:\/\/cdn\.jsdelivr\.net\/npm\/bootstrap@5\.3\.0\/dist\/css\/bootstrap\.min\.css/g,
    `${up}assets/vendor/bootstrap/bootstrap.min.css`,
    'bootstrap',
  );

  // --- Imágenes externas ---
  sub(/https:\/\/placehold\.co\/1600x900\/1e3a8a\/ffffff\?text=DNA/g, `${up}assets/images/placeholder-dna-1600x900.svg`, 'placehold');
  sub(/https:\/\/placehold\.co\/1600x900\/4f46e5\/ffffff\?text=Rx/g, `${up}assets/images/placeholder-rx-1600x900.svg`, 'placehold');
  sub(/https:\/\/flagcdn\.com\/w20\/ec\.png/g, `${up}assets/images/flag-ec-w20.png`, 'flagcdn');
  sub(/https:\/\/www\.transparenttextures\.com\/patterns\/diagmonds-light\.png/g, `${up}assets/images/texture-diagmonds-light.svg`, 'textura');

  // --- YouTube: contenido, no infraestructura. Solo al dominio sin cookies. ---
  sub(/https:\/\/www\.youtube\.com\/embed\//g, 'https://www.youtube-nocookie.com/embed/', 'youtube-nocookie');

  if (s !== original) {
    changes.push({ file: path.relative(REPO, file), hits: [...new Set(hits)] });
    if (!DRY) fs.writeFileSync(file, s, 'utf8');
  }
}

const byKind = {};
for (const c of changes) for (const h of c.hits) byKind[h] = (byKind[h] || 0) + 1;
console.log(JSON.stringify({ archivos_modificados: changes.length, por_tipo: byKind }, null, 2));
