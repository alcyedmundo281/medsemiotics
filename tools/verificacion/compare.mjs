// Compara el render antes (:3001) y después (:3000) midiendo la caja de los
// elementos clave y las fuentes efectivamente cargadas.
import puppeteer from 'puppeteer';

const PAGES = [
  'index.html',
  'neurologia.html',
  'gastroenterologia.html',
  'farmacoterapia_racional.html',
  'inmunologia_clinica.html',
  'medicina_y_datos.html',
  'medicina_e_implementacion.html',
  'neurologia/cefaleas/index.html',
  'gastroenterologia/cirrosis.html',
  'medicamentos_cronicos.html',
  'neurologia/epilepsia-ii/index.html',
  'medicina_e_implementacion/implementacion_no_reforma/index.html',
];

const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });

async function measure(port, page, blockExternal) {
  const p = await browser.newPage();
  const external = [];
  if (blockExternal) {
    await p.setRequestInterception(true);
    p.on('request', (req) => {
      const u = new URL(req.url());
      if (u.hostname !== 'localhost' && u.protocol !== 'data:') {
        external.push(u.hostname + u.pathname.slice(0, 40));
        req.abort();
      } else req.continue();
    });
  }
  await p.setViewport({ width: 1280, height: 900 });
  try {
    await p.goto(`http://localhost:${port}/medsemiotics/${page}`, {
      waitUntil: 'networkidle2', timeout: 25000,
    });
  } catch (e) { /* seguimos con lo que haya cargado */ }
  await new Promise((r) => setTimeout(r, 700));

  const data = await p.evaluate(() => {
    const box = (sel) => {
      const el = document.querySelector(sel);
      if (!el) return null;
      const r = el.getBoundingClientRect();
      return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    };
    const fams = new Set();
    document.querySelectorAll('h1,h2,h3,p,body,.gradient-text').forEach((el) => {
      fams.add(getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim());
    });
    // ¿Se renderizó algún icono de Font Awesome con glifo real?
    const icons = [...document.querySelectorAll('i.fas,i.fa-solid,i[class*="fa-"]')].slice(0, 5)
      .map((el) => { const r = el.getBoundingClientRect(); return Math.round(r.width); });
    return {
      title: document.title,
      body: box('body'),
      h1: box('h1'),
      main: box('main'),
      firstCard: box('main a, main .card, main div[class*="rounded"]'),
      scrollH: document.documentElement.scrollHeight,
      families: [...fams].sort(),
      iconWidths: icons,
      fontsLoaded: document.fonts ? document.fonts.size : -1,
    };
  });
  await p.close();
  return { ...data, external };
}

const rows = [];
for (const page of PAGES) {
  const before = await measure(3001, page, false);
  const after = await measure(3000, page, true);
  const dH = after.scrollH - before.scrollH;
  const dH1 = before.h1 && after.h1 ? after.h1.h - before.h1.h : null;
  rows.push({
    page,
    scrollH: `${before.scrollH} -> ${after.scrollH} (${dH >= 0 ? '+' : ''}${dH})`,
    h1_alto: dH1 === null ? 'n/a' : `${dH1 >= 0 ? '+' : ''}${dH1}px`,
    familias_antes: before.families.join('|'),
    familias_despues: after.families.join('|'),
    iconos: `${before.iconWidths.join(',')} -> ${after.iconWidths.join(',')}`,
    externas_bloqueadas: after.external.length,
    hosts: [...new Set(after.external.map((e) => e.split('/')[0]))].join(','),
  });
}

await browser.close();
console.log(JSON.stringify(rows, null, 2));
