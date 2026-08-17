import fs from 'node:fs';
import path from 'node:path';

const REPO = process.argv[2];
process.chdir(REPO);

// Solo las páginas que declaraban estas fuentes en su config en línea.
const MONO = [
  'neurologia/epilepsia-ii/epilepsia-2-actividad-interactiva.html',
  'neurologia/epilepsia-ii/epilepsia-2-pagina-conocimiento.html',
  'neurologia/epilepsia-ii/epilepsia-2-autoevaluacion.html',
  'neurologia/epilepsia-ii/epilepsia-2-presentacion.html',
  'neurologia/epilepsia-ii/masterclass.html',
  'gastroenterologia/fundamentos-de-gastroenterologia.html',
  'inmunologia/vacunas.html',
];
const SERIF = ['neurologia/acv.html'];

const out = [];
function swap(file, from, to) {
  const targets = [file, file.replace(/\.html$/, '.jsx')].filter((f) => fs.existsSync(f));
  for (const t of targets) {
    const o = fs.readFileSync(t, 'utf8');
    const crlf = o.includes('\r\n');
    // token completo, sin tocar variantes como font-mono-lab
    const re = new RegExp('\\b' + from + '\\b(?![\\w-])', 'g');
    let n = 0;
    const s0 = o.replace(re, () => { n++; return to; });
    if (n) {
      let s = s0;
      if (crlf) s = s.replace(/\r?\n/g, '\r\n');
      fs.writeFileSync(t, s, 'utf8');
      out.push(`${t}: ${from} -> ${to} x${n}`);
    }
  }
}
MONO.forEach((f) => swap(f, 'font-mono', 'font-jetbrains'));
SERIF.forEach((f) => swap(f, 'font-serif', 'font-dmserif'));
console.log(out.length ? out.join('\n') : 'sin cambios');
