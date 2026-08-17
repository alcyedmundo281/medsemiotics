// Compara el EOL de cada archivo modificado contra su versión en HEAD y
// restaura CRLF donde se haya perdido.
import { execSync } from 'node:child_process';
import fs from 'node:fs';

const REPO = process.argv[2];
const APPLY = process.argv.includes('--apply');
process.chdir(REPO);

const changed = execSync('git diff --name-only', { encoding: 'utf8' })
  .split('\n').map((s) => s.trim()).filter(Boolean);

const rows = [];
for (const f of changed) {
  if (!fs.existsSync(f)) continue;
  let head;
  try { head = execSync(`git show HEAD:"${f}"`, { encoding: 'buffer', maxBuffer: 1e9 }); }
  catch { continue; }
  const disk = fs.readFileSync(f);

  const crlfOf = (buf) => {
    const s = buf.toString('latin1');
    const crlf = (s.match(/\r\n/g) || []).length;
    const lf = (s.match(/\n/g) || []).length;
    return { crlf, lf, ratio: lf ? crlf / lf : 0 };
  };
  const h = crlfOf(head), d = crlfOf(disk);
  const eraCRLF = h.ratio > 0.5;
  const esCRLF = d.ratio > 0.5;

  if (eraCRLF && !esCRLF) {
    rows.push({ f, estado: 'CONVERTIDO A LF', head: h.crlf, disco: d.crlf });
    if (APPLY) {
      const txt = disk.toString('utf8').replace(/\r?\n/g, '\r\n');
      fs.writeFileSync(f, txt, 'utf8');
    }
  } else if (!eraCRLF && esCRLF) {
    rows.push({ f, estado: 'CONVERTIDO A CRLF', head: h.crlf, disco: d.crlf });
  }
}

console.log(rows.length ? JSON.stringify(rows, null, 2) : 'ningun archivo con EOL alterado');
