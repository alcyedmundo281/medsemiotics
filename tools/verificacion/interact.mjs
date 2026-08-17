// Pulsa el primer control interactivo de cada módulo React y comprueba que el
// DOM cambia y no aparecen errores.
import puppeteer from 'puppeteer';

const BASE = 'https://alcyedmundo281.github.io/medsemiotics';
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

const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
for (const page of PAGES) {
  const p = await browser.newPage();
  await p.setViewport({ width: 1280, height: 900 });
  const errors = [];
  p.on('pageerror', (e) => errors.push(String(e).slice(0, 120)));
  p.on('console', (m) => { if (m.type() === 'error' && !/favicon/.test(m.text())) errors.push(m.text().slice(0, 120)); });

  await p.goto(`${BASE}/${page}`, { waitUntil: 'networkidle2', timeout: 40000 }).catch(() => {});
  await new Promise((r) => setTimeout(r, 1000));

  const res = await p.evaluate(async () => {
    const root = document.getElementById('root') || document.getElementById('root-app');
    const before = root ? root.innerHTML.length : 0;
    const beforeText = document.body.innerText.slice(0, 200);
    // primer control pulsable dentro de la app
    const ctrls = [...(root || document).querySelectorAll('button, [role="button"], a[href="#"], input[type="radio"], select')]
      .filter((el) => el.offsetParent !== null);
    if (!ctrls.length) return { controles: 0 };
    const label = (ctrls[0].innerText || ctrls[0].value || ctrls[0].tagName).slice(0, 40).replace(/\s+/g, ' ');
    ctrls[0].click();
    await new Promise((r) => setTimeout(r, 700));
    const after = root ? root.innerHTML.length : 0;
    return {
      controles: ctrls.length,
      pulsado: label,
      domAntes: before,
      domDespues: after,
      cambio: after !== before || document.body.innerText.slice(0, 200) !== beforeText,
    };
  }).catch((e) => ({ error: String(e).slice(0, 100) }));

  console.log(`${page.padEnd(48)} controles=${String(res.controles).padStart(3)}  pulsado="${res.pulsado || '—'}"  DOM ${res.domAntes}->${res.domDespues}  reacciona=${res.cambio}  errores=${errors.length}`);
  if (errors.length) console.log('    ' + errors.join(' | '));
  await p.close();
}
await browser.close();
