// Sustituye el <script> del CDN de Tailwind por el tailwind.css local y
// retira el bloque tailwind.config en línea. Preserva finales de línea.
import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];

// Tipografía que cada página tenía por su config en línea o por su CSS propio.
// Se aplica como utilidad explícita en <body> para que la migración no la
// desplace hacia font-sans (Outfit) del config global.
const FONT_CLASS = {
  'gastroenterologia/fundamentos-de-gastroenterologia.html': 'font-inter',
  'gastroenterologia/helicobacter_pylori.html': 'font-inter',
  'gastroenterologia/trastornos-estomacales.html': 'font-lexend',
  'neurologia/epilepsia-ii/epilepsia-2-actividad-interactiva.html': 'font-jakarta',
  'neurologia/epilepsia-ii/epilepsia-2-pagina-conocimiento.html': 'font-jakarta',
  'neurologia/epilepsia-ii/epilepsia-2-autoevaluacion.html': 'font-jakarta',
  'neurologia/epilepsia-ii/epilepsia-2-presentacion.html': 'font-jakarta',
  'neurologia/epilepsia-ii/masterclass.html': 'font-jakarta',
  // Las 12 sin config en línea corrían con la pila del sistema de Tailwind,
  // pero su CSS propio ya fijaba Inter; se hace explícito.
  'farmacoterapia_racional/apixaban.html': 'font-inter',
  'farmacoterapia_racional/paliperidona.html': 'font-inter',
  'gastroenterologia/cirrosis.html': 'font-inter',
  'inmunologia/alergias-alimentarias.html': 'font-inter',
  'inmunologia/hipersensibilidad-farmacos.html': 'font-inter',
  'inmunologia/inmunologia-trasplante.html': 'font-inter',
  'inmunologia/laboratorio-inmunologia.html': 'font-inter',
  'inmunologia/vacunas.html': 'font-inter',
  'medicina_y_datos/estadisticos_descubiertos/index.html': 'font-inter',
  'medicina_y_datos/probabilidad_estadistica/index.html': 'font-inter',
  'neurologia/acv-isquemico.html': 'font-inter',
  'neurologia/neuromusculares.html': 'font-inter',
};

function walk(d, a = []) {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    if (e.name === '.git' || e.name === 'node_modules' || e.name === 'dist') continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, a);
    else if (e.name.endsWith('.html')) a.push(p);
  }
  return a;
}

const report = [];
for (const file of walk(REPO)) {
  const orig = fs.readFileSync(file, 'utf8');
  if (!orig.includes('cdn.tailwindcss.com')) continue;
  const rel = path.relative(REPO, file).replace(/\\/g, '/');
  const crlf = orig.includes('\r\n');
  let s = orig;
  const did = [];

  const depth = path.relative(REPO, path.dirname(file)).split(path.sep).filter(Boolean).length;
  const up = depth === 0 ? '' : '../'.repeat(depth);

  // 1. El <script> del CDN pasa a <link> del CSS local.
  const before = s;
  s = s.replace(
    /[ \t]*<script src="https:\/\/cdn\.tailwindcss\.com[^"]*"><\/script>/,
    `    <link href="${up}assets/tailwind.css" rel="stylesheet" />`,
  );
  if (s !== before) did.push('cdn->css');
  // Si quedara alguna otra ocurrencia, se elimina.
  s = s.replace(/[ \t]*<script src="https:\/\/cdn\.tailwindcss\.com[^"]*"><\/script>\r?\n?/g, '');

  // 2. Fuera el bloque tailwind.config en línea (ya fundido en el config).
  const b2 = s;
  s = s.replace(/[ \t]*<script id="tailwind-config">[\s\S]*?<\/script>\r?\n?/g, '');
  s = s.replace(/[ \t]*<script>\s*tailwind\.config\s*=\s*\{[\s\S]*?\}\s*;?\s*<\/script>\r?\n?/g, '');
  if (s !== b2) did.push('config-inline-fuera');

  // 3. Comentario huérfano "<!-- Tailwind ... -->"
  s = s.replace(/[ \t]*<!--\s*Tailwind(?:\s+(?:CSS|Configuration))?\s*-->\r?\n?/gi, '');

  // 4. Utilidad de tipografía en <body> para no derivar hacia Outfit.
  const fc = FONT_CLASS[rel];
  if (fc) {
    const m = s.match(/<body([^>]*)>/);
    if (m) {
      if (/\bclass="/.test(m[1])) {
        if (!m[1].includes(fc)) {
          s = s.replace(/<body([^>]*)class="/, `<body$1class="${fc} `);
          did.push('font:' + fc);
        }
      } else {
        s = s.replace(/<body([^>]*)>/, `<body$1 class="${fc}">`);
        did.push('font:' + fc);
      }
    }
  }

  if (crlf) s = s.replace(/\r?\n/g, '\r\n');
  if (s !== orig) { fs.writeFileSync(file, s, 'utf8'); report.push({ page: rel, did }); }
}

console.log(JSON.stringify({ migradas: report.length, detalle: report }, null, 2));
