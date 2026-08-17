// Segunda pasada: pulsa un control DISTINTO del ya activo y compara el contenido
// real (hash del innerHTML + texto), no la longitud.
import puppeteer from 'puppeteer';
import crypto from 'node:crypto';

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

  await p.goto(`${BASE}/${page}`, { waitUntil: 'networkidle2', timeout: 40000 }).catch(() => {});
  await new Promise((r) => setTimeout(r, 1000));

  const res = await p.evaluate(async () => {
    const root = document.getElementById('root') || document.getElementById('root-app');
    const scope = root || document.body;
    const ctrls = [...scope.querySelectorAll('button, [role="button"], input[type="radio"], select')]
      .filter((el) => el.offsetParent !== null);
    if (ctrls.length < 2) return { controles: ctrls.length, nota: 'menos de 2 controles visibles' };

    const snap = () => ({ html: scope.innerHTML, text: document.body.innerText });
    const a = snap();
    // elegir un control cuyo texto NO aparezca ya marcado como activo
    const target = ctrls[Math.min(2, ctrls.length - 1)];
    const label = (target.innerText || target.value || target.tagName).slice(0, 40).replace(/\s+/g, ' ');
    target.click();
    await new Promise((r) => setTimeout(r, 900));
    const b = snap();
    return {
      controles: ctrls.length,
      pulsado: label,
      htmlCambio: a.html !== b.html,
      textoCambio: a.text !== b.text,
      deltaTexto: b.text.length - a.text.length,
    };
  }).catch((e) => ({ error: String(e).slice(0, 100) }));

  const ok = res.htmlCambio || res.textoCambio;
  console.log(`${page.padEnd(46)} n=${String(res.controles).padStart(3)} "${(res.pulsado || '—').padEnd(26)}" html=${res.htmlCambio} texto=${res.textoCambio} Δ=${res.deltaTexto ?? '—'} => ${ok ? 'RESPONDE' : 'sin cambio'} err=${errors.length}`);
  await p.close();
}
await browser.close();
