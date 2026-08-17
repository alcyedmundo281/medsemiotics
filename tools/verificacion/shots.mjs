import puppeteer from 'puppeteer';
import fs from 'node:fs';

const PAGES = [
  ['index', 'index.html'],
  ['neurologia', 'neurologia.html'],
  ['gastroenterologia', 'gastroenterologia.html'],
  ['farmacoterapia', 'farmacoterapia_racional.html'],
  ['inmunologia', 'inmunologia_clinica.html'],
  ['medicina_y_datos', 'medicina_y_datos.html'],
  ['implementacion', 'medicina_e_implementacion.html'],
];

fs.mkdirSync('shots', { recursive: true });
const browser = await puppeteer.launch({ headless: 'new', args: ['--no-sandbox'] });

for (const [name, page] of PAGES) {
  for (const [label, port] of [['antes', 3001], ['despues', 3000]]) {
    const p = await browser.newPage();
    await p.setViewport({ width: 1280, height: 860 });
    try {
      await p.goto(`http://localhost:${port}/medsemiotics/${page}`, {
        waitUntil: 'networkidle2', timeout: 25000,
      });
    } catch (e) { /* capturamos lo que haya */ }
    await new Promise((r) => setTimeout(r, 800));
    await p.screenshot({ path: `shots/${name}-${label}.png` });
    await p.close();
  }
  console.log('capturado', name);
}
await browser.close();
