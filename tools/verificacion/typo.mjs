// Vuelca la tipografía computada de body y encabezados de cada página.
import puppeteer from 'puppeteer';
import fs from 'node:fs';

const PORT = process.argv[2];
const OUT = process.argv[3];
const PAGES = JSON.parse(fs.readFileSync(process.argv[4], 'utf8'));

const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const out = {};

for (const page of PAGES) {
  const p = await browser.newPage();
  await p.setViewport({ width: 1280, height: 900 });
  const externals = [];
  await p.setRequestInterception(true);
  p.on('request', (req) => {
    const u = new URL(req.url());
    if (u.hostname !== 'localhost' && u.protocol !== 'data:' && u.protocol !== 'blob:') {
      externals.push(u.hostname);
      req.abort();
    } else req.continue();
  });
  const errors = [];
  p.on('pageerror', (e) => errors.push(String(e).slice(0, 140)));
  p.on('console', (m) => { if (m.type() === 'error') errors.push('console: ' + m.text().slice(0, 140)); });

  try {
    await p.goto(`http://localhost:${PORT}/medsemiotics/${page}`, {
      waitUntil: 'networkidle2', timeout: 30000,
    });
  } catch (e) { errors.push('GOTO ' + String(e.message).slice(0, 80)); }
  await new Promise((r) => setTimeout(r, 900));

  const data = await p.evaluate(() => {
    const fam = (el) => el ? getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim() : null;
    const g = (sel) => { const el = document.querySelector(sel); return el ? {
      font: fam(el),
      size: getComputedStyle(el).fontSize,
      weight: getComputedStyle(el).fontWeight,
      color: getComputedStyle(el).color,
    } : null; };
    // muestreo de estilo computado de los primeros 60 elementos con clase
    const sample = [...document.querySelectorAll('[class]')].slice(0, 60).map((el) => {
      const cs = getComputedStyle(el);
      return [
        el.tagName + '.' + (el.className.baseVal ?? el.className).toString().slice(0, 50),
        cs.fontFamily.split(',')[0].replace(/["']/g, ''),
        cs.fontSize, cs.fontWeight, cs.color, cs.backgroundColor, cs.display,
        Math.round(el.getBoundingClientRect().width) + 'x' + Math.round(el.getBoundingClientRect().height),
      ].join('|');
    });
    return {
      title: document.title,
      body: g('body'), h1: g('h1'), h2: g('h2'), h3: g('h3'), p: g('p'),
      scrollH: document.documentElement.scrollHeight,
      rootHasContent: (document.getElementById('root') || document.getElementById('root-app'))
        ? (document.getElementById('root') || document.getElementById('root-app')).children.length : -1,
      sample,
    };
  }).catch((e) => ({ error: String(e).slice(0, 120) }));

  out[page] = { ...data, externals: [...new Set(externals)], errors };
  await p.close();
}

await browser.close();
fs.writeFileSync(OUT, JSON.stringify(out, null, 2));
console.log('escrito', OUT, '-', Object.keys(out).length, 'paginas');
