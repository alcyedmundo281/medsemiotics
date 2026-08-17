// Sustituye font-display / font-sans por la utilidad que reproduce la
// tipografía que la página tenía con su config en línea. Preserva EOL.
import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];

// pagina -> { 'font-display': nueva, 'font-sans': nueva }
const MAP = {
  'gastroenterologia-autoevaluacion.html': { 'font-display': 'font-lexend' },
  'gastroenterologia/reflujo-gastroesofagico.html': { 'font-display': 'font-lexend' },
  'gastroenterologia/trastornos-estomacales.html': { 'font-display': 'font-lexend', 'font-sans': 'font-lexend' },
  'neurologia/acv.html': { 'font-display': 'font-lexend' },
  'gastroenterologia/fundamentos-de-gastroenterologia.html': { 'font-display': 'font-outfit', 'font-sans': 'font-inter' },
  'gastroenterologia/helicobacter_pylori.html': { 'font-sans': 'font-inter' },
  'neurologia/acv-isquemico.html': { 'font-sans': 'font-system' },
  'neurologia/epilepsia-ii/epilepsia-2-actividad-interactiva.html': { 'font-sans': 'font-jakarta' },
  'neurologia/epilepsia-ii/epilepsia-2-pagina-conocimiento.html': { 'font-sans': 'font-jakarta' },
  'neurologia/epilepsia-ii/epilepsia-2-autoevaluacion.html': { 'font-sans': 'font-jakarta' },
  'neurologia/epilepsia-ii/epilepsia-2-presentacion.html': { 'font-sans': 'font-jakarta' },
  'neurologia/epilepsia-ii/masterclass.html': { 'font-sans': 'font-jakarta' },
};

const out = [];
for (const [rel, subs] of Object.entries(MAP)) {
  // La clase puede vivir en el .html o en el .jsx hermano.
  const targets = [path.join(REPO, rel)];
  const jsx = path.join(REPO, rel.replace(/\.html$/, '.jsx'));
  if (fs.existsSync(jsx)) targets.push(jsx);

  for (const file of targets) {
    if (!fs.existsSync(file)) continue;
    const orig = fs.readFileSync(file, 'utf8');
    const crlf = orig.includes('\r\n');
    let s = orig;
    const hits = {};
    for (const [from, to] of Object.entries(subs)) {
      // solo dentro de atributos class/className, como token completo
      const re = new RegExp(`(\\bclass(?:Name)?\\s*=\\s*["'\`{][^"'\`]*?)\\b${from}\\b`, 'g');
      let n = 0;
      let prev;
      do { prev = s; s = s.replace(re, (m0, p1) => { n++; return p1 + to; }); } while (s !== prev);
      if (n) hits[from + ' -> ' + to] = n;
    }
    if (s !== orig) {
      if (crlf) s = s.replace(/\r?\n/g, '\r\n');
      fs.writeFileSync(file, s, 'utf8');
      out.push({ file: path.relative(REPO, file).replace(/\\/g, '/'), hits });
    }
  }
}
console.log(JSON.stringify(out, null, 2));
