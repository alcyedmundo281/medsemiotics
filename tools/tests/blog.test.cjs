const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const yaml = require('js-yaml');

const root = path.resolve(__dirname, '../..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const json = file => JSON.parse(read(file));
const posts = fs.readdirSync(path.join(root, 'posts')).filter(f => f.endsWith('.md')).map(f =>
  yaml.load(read('posts/' + f).split(/^---\s*$/m)[1]));

test('Una condición, un artículo, una URL; preguntas sin ediciones independientes', () => {
  const index = json('assets/data/blog-index.json');
  const links = json('assets/data/condition-posts.json');
  const bank = json('assets/data/quiz-bank.json');
  assert.equal(new Set(posts.map(p => p.grounding.condicion_id)).size, posts.length);
  assert.equal(new Set(posts.map(p => p.slug)).size, posts.length);
  assert.equal(index.length, posts.length);
  assert.equal(links.length, posts.length);
  assert.equal(bank.length, posts.reduce((n, p) => n + p.autoevaluacion.length, 0));
  for (const p of posts) {
    const article = json('assets/data/posts/' + p.slug + '.json');
    assert.deepEqual(article.grounding, p.grounding);
    assert.deepEqual(article.evidencia, p.evidencia);
    assert.deepEqual(article.autoevaluacion, p.autoevaluacion);
    assert.deepEqual(article.fuente, p.fuente);
    assert.equal(article.publicacion.doi, yaml.load(read('CITATION.cff')).doi);
    assert.ok(article.fuente.doi);
    assert.equal(links.find(l => l.condicion_id === p.grounding.condicion_id).slug, p.slug);
    for (const q of p.autoevaluacion) {
      const actual = bank.find(b => b.id === p.slug + '-' + q.id);
      assert.equal(actual.pregunta, q.pregunta);
      assert.deepEqual(actual.opciones, q.opciones);
      assert.equal(actual.pmid, q.pmid);
      assert.equal(actual.doi, q.doi);
      assert.equal(actual.fuente_doi, p.fuente.doi);
      assert.deepEqual(actual.evidencia, q.evidencia);
      assert.equal(q.opciones.length, 3);
      // Una condición puede medir el mismo hallazgo en varias fuentes: la arista es concepto y ref.
      const questionSign = p.evidencia.find(s => s.concepto === q.concepto_id &&
        (!q.evidencia.campo || s[q.evidencia.campo]?.ref === q.referencia_id));
      assert.equal(q.evidencia.estado_lr, questionSign.estado_lr);
      if (q.evidencia.campo) assert.deepEqual(q.evidencia.dato, questionSign[q.evidencia.campo]);
      assert.equal(q.opciones.filter(o => o.correcta).length, 1);
    }
    for (const field of ['lr_positivo', 'lr_negativo']) {
      if (p.grounding[field] === null) continue;
      const sign = p.evidencia.find(s => s.concepto === p.grounding.concepto_id &&
        s[field]?.ref === p.grounding.referencia_id);
      assert.equal(sign.estado_lr, 'medido');
      assert.equal(sign[field].valor, p.grounding[field]);
      assert.ok(sign[field].ref);
    }
  }
});

test('La página distingue el DOI del material, el del conjunto de datos y el del estudio', async () => {
  const { context, element } = browser();
  context.fixture = { slug: 'prueba', title: 'Prueba', body: '',
    publicacion: { doi: '10.test/material' }, fuente: { doi: '10.test/datos' },
    grounding: { doi: '10.test/estudio' } };
  await vm.runInContext('currentPost = fixture; renderPost()', context);
  assert.equal(element('publicationDoiLink').href, 'https://doi.org/10.test/material');
  assert.equal(element('sourceDoiLink').href, 'https://doi.org/10.test/datos');
  assert.equal(element('doiLink').href, 'https://doi.org/10.test/estudio');
});

function browser() {
  const elements = new Map();
  function element(id) {
    if (!elements.has(id)) {
      const classes = new Set();
      elements.set(id, { textContent: '', innerHTML: '', value: '20',
        classList: { add: k => classes.add(k), remove: k => classes.delete(k),
          toggle: (k, yes) => yes ? classes.add(k) : classes.delete(k),
          contains: k => classes.has(k) },
        addEventListener() {}, });
    }
    return elements.get(id);
  }
  const context = vm.createContext({
    document: { getElementById: element, querySelector: element },
    window: { location: { search: '?slug=prueba' } },
    localStorage: { getItem: () => null }, URLSearchParams, console,
    fetch: async () => ({ ok: true, json: async () => [] }),
  });
  const scripts = [...read('post.html').matchAll(/<script>([\s\S]*?)<\/script>/g)];
  const script = scripts.find(m => m[1].includes('function setupCalculator'))[1];
  vm.runInContext(script.replace(/loadPost\(\);\s*$/, ''), context);
  return { context, element };
}

for (const [name, pos, neg, state, visible, positive, negative] of [
  ['no medido', null, null, 'no_medido', false, 'No calculable', 'No calculable'],
  ['no medible', null, null, 'no_medible', false, 'No calculable', 'No calculable'],
  ['LR+ solamente', 4, null, 'medido', true, '50.0%', 'No calculable'],
  ['LR- cero real', null, 0, 'medido', true, 'No calculable', '0.0%'],
  ['cadena no numérica', '4', null, 'medido', false, 'No calculable', 'No calculable'],
  ['rango sin estimación', null, null, 'medido', false, 'No calculable', 'No calculable'],
]) {
  test('Calculadora: ' + name, async () => {
    const { context, element } = browser();
    context.fixture = { slug: 'prueba', title: 'Prueba', body: 'Valor < 8; <script>no ejecutar</script>',
      grounding: { estado_lr: state, lr_positivo: pos, lr_negativo: neg } };
    await vm.runInContext('currentPost = fixture; renderPost()', context);
    assert.equal(element('calculatorSection').classList.contains('hidden'), !visible);
    assert.equal(element('postTestPosProb').textContent, positive);
    assert.equal(element('postTestNegProb').textContent, negative);
    assert.equal(element('pubmedLink').classList.contains('hidden'), true);
    assert.equal(element('doiLink').classList.contains('hidden'), true);
    assert.ok(!element('markdownBody').innerHTML.includes('<script>'));
    assert.ok(element('markdownBody').innerHTML.includes('&lt; 8'));
  });
}

test('El filtro bayesiano no considera que tener un ID HM sea evidencia cuantitativa', () => {
  const html = read('index.html');
  const block = html.slice(html.indexOf("if (activeEvidence === 'confirmatorio')"),
    html.indexOf("// 3. Dificultad"));
  const context = vm.createContext({ activeEvidence: 'confirmatorio',
    post: { grounding_badge: 'HM:6001', evidencia: [{ estado_lr: 'no_medido' }] }, matchEvidence: true });
  vm.runInContext(block, context);
  assert.equal(context.matchEvidence, false);
  context.post.evidencia = [{ estado_lr: 'medido', lr_positivo: { valor: 6.5 } }];
  vm.runInContext(block, context);
  assert.equal(context.matchEvidence, true);
});

test('El caso socrático se incorpora al artículo y su texto se escapa', async () => {
  const casosDir = path.join(root, 'assets/data/casos');
  const casos = fs.existsSync(casosDir) ? fs.readdirSync(casosDir) : [];
  for (const file of casos) {
    const caso = json('assets/data/casos/' + file);
    const article = json('assets/data/posts/' + caso.slug + '.json');
    assert.deepEqual(article.caso, caso);
    assert.equal(article.has_caso, true);
    assert.equal(article.fecha_revision, caso.publicacion.ultima_revision);
  }
  const { context, element } = browser();
  const hallazgo = { nombre: '<img onerror=x>', rol: 'Prueba', estado: 'LR medido',
    cifras: ['LR+ 3.1 (IC 95 %: 1.6–5.9)'], decision: 'aumenta', referencias: ['pmid:1'] };
  context.fixture = { slug: 'prueba', title: 'Prueba', body: '', fecha_publicacion: '2026-08-21',
    fecha_revision: '2026-09-21', version: 2, grounding: {},
    caso: { nivel: 'Pregrado', duracion_min: 45, aviso: 'Ficticio', publicacion: { version: 2 },
      objetivos: ['<b>obj</b>'], vineta: { titulo: 'V', texto: '<script>x</script>', datos: [] },
      etapas: [{ numero: 1, fase_etiqueta: 'F', titulo: 'T', informacion: null, datos: [],
        hallazgos: [hallazgo], preguntas: [{ pregunta: '¿P?', clave: 'C' }] }],
      cierre: { sintesis: 'S', necesidades_aprendizaje: ['N'] }, omitidos: [] } };
  await vm.runInContext('currentPost = fixture; renderPost()', context);
  const html = element('casoContenido').innerHTML;
  assert.equal(element('casoSection').classList.contains('hidden'), false);
  assert.ok(html.includes('LR+ 3.1 (IC 95 %: 1.6–5.9)'));
  assert.ok(html.includes('medsemiotics-db'));
  assert.ok(!html.includes('<script>') && !html.includes('<img') && !html.includes('<b>obj'));
  assert.equal(element('postRevised').textContent, '2026-09-21');
  assert.equal(element('metaCitationDate').content, '2026/08/21');
  assert.equal(JSON.parse(element('jsonLd').textContent).dateModified, '2026-09-21');
});

test('Imágenes destacadas: solo Wikimedia Commons en dominio público o CC0', () => {
  const images = json('assets/data/topic-images.json');
  for (const [key, image] of Object.entries(images)) {
    assert.ok(['Public domain', 'CC0'].includes(image.license), key);
    assert.ok(image.source.startsWith('https://commons.wikimedia.org/wiki/File:'), key);
    assert.ok(image.alt && image.author && image.verified, key);
  }
});
