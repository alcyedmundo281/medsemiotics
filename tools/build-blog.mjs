import yaml from 'js-yaml';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const postsDir = path.join(rootDir, 'posts');
const outputDataDir = path.join(rootDir, 'assets', 'data');
const outputPostsDir = path.join(outputDataDir, 'posts');
// Casos socráticos compilados y validados por `python -m casos build` (solo los publicados).
const casosDir = path.join(outputDataDir, 'casos');
// Política de imágenes destacadas: Wikimedia Commons en dominio público o CC0.
const imageLicenses = new Set(['Public domain', 'CC0']);
const checkOnly = process.argv.includes('--check');
const pendingOutputs = new Map();
const publicationCitation = yaml.load(fs.readFileSync(path.join(rootDir, 'CITATION.cff'), 'utf8'));
if (!publicationCitation.doi) throw new Error('Medsemiotics no declara su DOI en CITATION.cff');

function emitJson(filename, data) {
  pendingOutputs.set(filename, JSON.stringify(data, null, 2) + '\n');
}

// Ensure output directories exist
if (!checkOnly && !fs.existsSync(outputDataDir)) {
  fs.mkdirSync(outputDataDir, { recursive: true });
}
if (!checkOnly && !fs.existsSync(outputPostsDir)) {
  fs.mkdirSync(outputPostsDir, { recursive: true });
}

function parseFrontmatter(fileContent) {
  const match = fileContent.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n([\s\S]*))?$/);
  if (!match) throw new Error('Artículo sin metadatos YAML');
  const data = yaml.load(match[1]);
  if (!data?.grounding?.condicion_id || !data?.fuente?.revision) {
    throw new Error('Artículo sin procedencia de medsemiotics-db: ejecutar topics:sync');
  }
  return { data, content: (match[2] || '').trim() };
}
// Build index & posts
function buildBlog() {
  console.log('--- Construyendo Índice del Blog MedSemiotics ---');
  if (!fs.existsSync(postsDir)) {
    console.log('No se encontró la carpeta posts/. Creando...');
    throw new Error('No existe posts/: ejecutar topics:sync');
  }

  const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.md'));
  const postsIndex = [];

  // Imágenes registradas y verificadas con `python -m imagenes asignar`.
  const imagesJsonPath = path.join(outputDataDir, 'topic-images.json');
  const topicImages = fs.existsSync(imagesJsonPath)
    ? JSON.parse(fs.readFileSync(imagesJsonPath, 'utf-8'))
    : {};
  for (const [key, image] of Object.entries(topicImages)) {
    if (!imageLicenses.has(image.license)) {
      throw new Error(`${key}: imagen con licencia «${image.license}»; solo dominio público o CC0`);
    }
  }
  const casos = new Map();
  if (fs.existsSync(casosDir)) {
    for (const file of fs.readdirSync(casosDir).filter(f => f.endsWith('.json'))) {
      const caso = JSON.parse(fs.readFileSync(path.join(casosDir, file), 'utf-8'));
      casos.set(caso.slug, caso);
    }
  }

  for (const file of files) {
    const filePath = path.join(postsDir, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const { data, content: markdownBody } = parseFrontmatter(content);

    // Match image from topicImages
    const condKey = data.grounding && data.grounding.condicion_id ? data.grounding.condicion_id.replace(':', '') : file.split('-')[0];
    const imgData = topicImages[condKey] || null;

    const hasScalarLR = ['lr_positivo', 'lr_negativo'].some(
      key => typeof data.grounding[key] === 'number' && Number.isFinite(data.grounding[key]),
    );
    if (hasScalarLR && (data.grounding.estado_lr !== 'medido' || !data.grounding.referencia_id)) {
      throw new Error(`${file}: LR sin estado medido y referencia.`);
    }

    const caso = casos.get(data.slug) || null;
    if (caso && caso.condicion_id !== data.grounding.condicion_id) {
      throw new Error(`${file}: el caso ${caso.condicion_id} no corresponde a este artículo`);
    }
    casos.delete(data.slug);

    const postSummary = {
      id: data.id || file.replace('.md', ''),
      slug: data.slug || file.replace('.md', ''),
      title: data.title || 'Sin título',
      subtitle: data.subtitle || '',
      date: data.date || '2026-08-20',
      // Fechas editoriales: primera publicación de la URL y última revisión del caso.
      fecha_publicacion: String(data.date),
      fecha_revision: caso ? caso.publicacion.ultima_revision : null,
      version: caso ? caso.publicacion.version : null,
      has_caso: Boolean(caso),
      author: data.author || 'Dr. Alcy Torres',
      category: data.category || 'general',
      category_label: data.category_label || data.category || 'General',
      tags: data.tags || [],
      reading_time: data.reading_time || '5 min',
      difficulty: data.difficulty || 'Intermedio',
      grounding_badge: `${data.grounding.condicion_id} · ${data.grounding.pmid ? 'PMID:' + data.grounding.pmid : 'Sin LR medidos'}`,
      grounding: data.grounding,
      evidencia: data.evidencia || [],
      fuente: data.fuente,
      publicacion: { titulo: publicationCitation.title, doi: publicationCitation.doi },
      has_quiz: Boolean(data.autoevaluacion && data.autoevaluacion.length > 0),
      quiz_count: data.autoevaluacion ? data.autoevaluacion.length : 0,
      featured_image: data.image || (imgData ? (imgData.thumb || imgData.url) : null),
      image_source: imgData ? imgData.source : null,
      image_license: imgData ? imgData.license : null,
      image_title: imgData ? imgData.title.replace('File:', '') : null,
      image_alt: imgData ? imgData.alt || null : null,
      image_author: imgData ? imgData.author || null : null,
      excerpt: data.subtitle || markdownBody.slice(0, 160).replace(/[#*`_]/g, '') + '...'
    };

    const fullPost = {
      ...postSummary,
      grounding: data.grounding || {},
      triada: data.triada || {},
      autoevaluacion: data.autoevaluacion || [],
      caso,
      body: markdownBody
    };

    postsIndex.push(postSummary);

    // Save individual full post JSON for fast client reading
    emitJson(
      path.join(outputPostsDir, `${postSummary.slug}.json`),
      fullPost,
    );
  }

  if (casos.size) {
    throw new Error('Casos compilados sin artículo: ' + [...casos.keys()].join(', '));
  }

  // Sort reverse chronological
  postsIndex.sort((a, b) => new Date(b.date) - new Date(a.date));

  // Extract unified Question Bank (Quiz Bank)
  const quizBank = [];
  for (const file of files) {
    const filePath = path.join(postsDir, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const { data } = parseFrontmatter(content);
    if (data.autoevaluacion && Array.isArray(data.autoevaluacion)) {
      data.autoevaluacion.forEach((q, idx) => {
        quizBank.push({
          id: `${data.slug}-q${idx + 1}`,
          post_slug: data.slug,
          post_title: data.title,
          category: data.category || 'general',
          category_label: data.category_label || 'Clínica',
          condicion_id: data.grounding ? data.grounding.condicion_id : null,
          condicion_nombre: data.grounding ? data.grounding.condicion_nombre : data.title,
          concepto_id: q.concepto_id,
          evidencia: q.evidencia,
          fuente_doi: q.fuente_doi,
          referencia_id: q.referencia_id,
          pmid: q.pmid || null,
          doi: q.doi || null,
          referencia_cita: q.referencia_id === data.grounding.referencia_id ? data.grounding.referencia_cita : null,
          triada: data.triada || null,
          pregunta: q.pregunta,
          opciones: q.opciones
        });
      });
    }
  }

  // Save index
  emitJson(
    path.join(outputDataDir, 'blog-index.json'),
    postsIndex,
  );

  // Save Quiz Bank
  emitJson(
    path.join(outputDataDir, 'quiz-bank.json'),
    quizBank,
  );

  emitJson(path.join(outputDataDir, 'condition-posts.json'), postsIndex.map(p => ({
    condicion_id: p.grounding.condicion_id,
    archivo: p.fuente.condicion,
    slug: p.slug,
    url: `https://powersemiotics.com/medsemiotics/post.html?slug=${p.slug}`,
  })).sort((a, b) => a.condicion_id.localeCompare(b.condicion_id)));
  const sitemapPath = path.join(rootDir, 'sitemap.xml');
  const sitemap = fs.readFileSync(sitemapPath, 'utf8');
  // sitemap.mjs escribe el archivo entero con CRLF: el bloque del blog conserva
  // el mismo fin de línea para no reescribir todo el sitemap en cada build.
  const eol = sitemap.includes('\r\n') ? '\r\n' : '\n';
  const blogUrls = '<!-- BLOG-START -->' + eol + postsIndex.map(p =>
    `  <url><loc>https://powersemiotics.com/medsemiotics/post.html?slug=${p.slug}</loc></url>`,
  ).sort().join(eol) + eol + '<!-- BLOG-END -->';
  const updatedSitemap = sitemap.includes('<!-- BLOG-START -->')
    ? sitemap.replace(/<!-- BLOG-START -->[\s\S]*?<!-- BLOG-END -->/, blogUrls)
    : sitemap.replace('</urlset>', blogUrls + eol + '</urlset>');
  pendingOutputs.set(sitemapPath, updatedSitemap);
  const stale = [];
  for (const [filename, text] of pendingOutputs) {
    if (!fs.existsSync(filename) || fs.readFileSync(filename, 'utf8') !== text) {
      if (checkOnly) stale.push(path.relative(rootDir, filename));
      else fs.writeFileSync(filename, text, 'utf8');
    }
  }
  if (stale.length) throw new Error('JSON desactualizados: ' + stale.join(', '));

  console.log(`✓ Blog procesado exitosamente: ${postsIndex.length} tema(s) generado(s).`);
  console.log(`✓ Banco de Autoevaluación generado: ${quizBank.length} pregunta(s) indexada(s).`);
  console.log(`✓ Índices guardados en: assets/data/blog-index.json y quiz-bank.json`);
}

buildBlog();
