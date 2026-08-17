// Verificación con navegador contra producción: peticiones externas, montaje de
// React, errores de consola y fuentes realmente aplicadas.
import puppeteer from 'puppeteer';
import fs from 'node:fs';

const BASE = process.argv[2];
const PAGES = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const HOST = new URL(BASE).hostname;

const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });
const out = {};

for (const page of PAGES) {
  const p = await browser.newPage();
  await p.setViewport({ width: 1280, height: 900 });
  const externals = new Set();
  const failed = [];
  const errors = [];

  p.on('request', (r) => {
    const u = new URL(r.url());
    if (u.hostname !== HOST && !['data:', 'blob:', 'about:'].includes(u.protocol)) {
      externals.add(u.hostname);
    }
  });
  p.on('requestfailed', (r) => failed.push(`${r.url().slice(0, 90)} :: ${r.failure()?.errorText}`));
  p.on('response', (r) => { if (r.status() >= 400) failed.push(`${r.status()} ${r.url().slice(0, 90)}`); });
  p.on('pageerror', (e) => errors.push(String(e).slice(0, 160)));
  p.on('console', (m) => { if (m.type() === 'error') errors.push('console: ' + m.text().slice(0, 160)); });

  try {
    await p.goto(`${BASE}/${page}`, { waitUntil: 'networkidle2', timeout: 40000 });
  } catch (e) { errors.push('GOTO ' + e.message.slice(0, 80)); }
  await new Promise((r) => setTimeout(r, 1200));

  const data = await p.evaluate(async () => {
    if (document.fonts && document.fonts.ready) { try { await document.fonts.ready; } catch (e) { /* noop */ } }
    const fam = (el) => el ? getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim() : null;
    // ¿alguna de las fuentes declaradas se cargó de verdad?
    const loaded = [];
    if (document.fonts) {
      document.fonts.forEach((f) => { if (f.status === 'loaded') loaded.push(f.family.replace(/["']/g, '')); });
    }
    const root = document.getElementById('root') || document.getElementById('root-app');
    return {
      title: document.title,
      body: fam(document.body),
      h1: fam(document.querySelector('h1')),
      p: fam(document.querySelector('p')),
      fuentesCargadas: [...new Set(loaded)].sort(),
      totalFontFaces: document.fonts ? document.fonts.size : -1,
      reactRoot: root ? root.children.length : null,
      textoVisible: document.body.innerText.trim().length,
    };
  }).catch((e) => ({ error: String(e).slice(0, 120) }));

  out[page] = { ...data, externals: [...externals], failed: failed.slice(0, 6), errors: errors.slice(0, 6) };
  await p.close();
}

await browser.close();
console.log(JSON.stringify(out, null, 2));
