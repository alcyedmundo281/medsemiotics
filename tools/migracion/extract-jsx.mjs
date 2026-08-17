// Extrae el <script type="text/babel"> de cada página a un .jsx hermano y
// deja en la página una referencia al bundle compilado.
import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];
const PAGES = [
  'gastroenterologia/trastornos-estomacales.html',
  'inmunologia/alergias-alimentarias.html',
  'inmunologia/hipersensibilidad-farmacos.html',
  'inmunologia/inmunologia-trasplante.html',
  'inmunologia/laboratorio-inmunologia.html',
  'inmunologia/vacunas.html',
  'neurologia/acv-isquemico.html',
  'neurologia/epilepsia-ii/masterclass.html',
];

const report = [];

for (const rel of PAGES) {
  const file = path.join(REPO, rel);
  const eol = fs.readFileSync(file, 'utf8').includes('\r\n') ? '\r\n' : '\n';
  let html = fs.readFileSync(file, 'utf8');

  const m = html.match(/[ \t]*<script type="text\/babel">\r?\n?([\s\S]*?)<\/script>/);
  if (!m) { report.push({ page: rel, error: 'sin bloque text/babel' }); continue; }

  let jsx = m[1];

  // Reindenta a columna 0 quitando el sangrado común.
  const lines = jsx.split(/\r?\n/);
  const indents = lines.filter((l) => l.trim()).map((l) => l.match(/^[ \t]*/)[0].length);
  const cut = indents.length ? Math.min(...indents) : 0;
  jsx = lines.map((l) => l.slice(cut)).join('\n').trim() + '\n';

  const base = path.basename(rel, '.html');
  const dir = path.dirname(file);
  const jsxPath = path.join(dir, base + '.jsx');
  const outPath = path.join(dir, base + '.bundle.js');

  const header =
    `// Fuente del módulo interactivo de ${path.basename(rel)}.\n` +
    `// Se compila con \`npm run build:js\` a ${base}.bundle.js; la página carga\n` +
    `// el bundle, no este archivo. React y ReactDOM llegan como globales UMD.\n\n`;

  fs.writeFileSync(jsxPath, header + jsx, 'utf8');

  // Sustituye el <script type="text/babel"> por el bundle.
  const depth = path.relative(REPO, dir).split(path.sep).filter(Boolean).length;
  const up = depth === 0 ? '' : '../'.repeat(depth);
  const indent = m[0].match(/^[ \t]*/)[0];
  html = html.replace(m[0], `${indent}<script src="${base}.bundle.js"></script>`);

  // Babel fuera; React/ReactDOM a local con versión fijada.
  html = html.replace(/[ \t]*<!--[^>]*Babel[^>]*-->\r?\n?/gi, '');
  html = html.replace(/[ \t]*<script[^>]*unpkg\.com\/@babel\/standalone[^>]*><\/script>\r?\n?/g, '');
  html = html.replace(
    /https:\/\/unpkg\.com\/react@18\/umd\/react\.(?:production\.min|development)\.js/g,
    `${up}assets/vendor/react/react-18.3.1.production.min.js`,
  );
  html = html.replace(
    /https:\/\/unpkg\.com\/react-dom@18\/umd\/react-dom\.(?:production\.min|development)\.js/g,
    `${up}assets/vendor/react/react-dom-18.3.1.production.min.js`,
  );

  if (eol === '\r\n') html = html.replace(/\r?\n/g, '\r\n');
  fs.writeFileSync(file, html, 'utf8');

  report.push({
    page: rel,
    jsx: path.relative(REPO, jsxPath).replace(/\\/g, '/'),
    bundle: path.relative(REPO, outPath).replace(/\\/g, '/'),
    lineas_jsx: jsx.split('\n').length,
    eol,
  });
}

console.log(JSON.stringify(report, null, 2));
