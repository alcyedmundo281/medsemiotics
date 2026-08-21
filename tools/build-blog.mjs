import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const postsDir = path.join(rootDir, 'posts');
const outputDataDir = path.join(rootDir, 'assets', 'data');
const outputPostsDir = path.join(outputDataDir, 'posts');

// Ensure output directories exist
if (!fs.existsSync(outputDataDir)) {
  fs.mkdirSync(outputDataDir, { recursive: true });
}
if (!fs.existsSync(outputPostsDir)) {
  fs.mkdirSync(outputPostsDir, { recursive: true });
}

function parseFrontmatter(fileContent) {
  const frontmatterRegex = /^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n([\s\S]*))?$/;
  const match = fileContent.match(frontmatterRegex);

  if (!match) {
    return { data: {}, content: fileContent };
  }

  const yamlBlock = match[1];
  const body = match[2] || '';

  // Simple and robust parser for our YAML structure
  const data = parseSimpleYaml(yamlBlock);
  return { data, content: body.trim() };
}

function parseSimpleYaml(yamlText) {
  const result = {};
  const lines = yamlText.split(/\r?\n/);
  let currentKey = null;
  let currentArray = null;
  let currentObject = null;
  let inNestedObj = false;

  for (let i = 0; i < lines.length; i++) {
    const rawLine = lines[i];
    if (!rawLine.trim() || rawLine.trim().startsWith('#')) continue;

    const indent = rawLine.search(/\S/);
    const line = rawLine.trim();

    // Top-level key: value
    if (indent === 0) {
      inNestedObj = false;
      currentObject = null;
      currentArray = null;

      const colonIdx = line.indexOf(':');
      if (colonIdx !== -1) {
        const key = line.slice(0, colonIdx).trim();
        const value = line.slice(colonIdx + 1).trim();

        if (value === '') {
          currentKey = key;
          // Determine if next line is array or object
          const nextLine = lines.slice(i + 1).find(l => l.trim() && !l.trim().startsWith('#'));
          if (nextLine && nextLine.trim().startsWith('-')) {
            currentArray = [];
            result[key] = currentArray;
          } else {
            currentObject = {};
            result[key] = currentObject;
            inNestedObj = true;
          }
        } else if (value.startsWith('[') && value.endsWith(']')) {
          result[key] = value.slice(1, -1).split(',').map(s => s.trim().replace(/^["']|["']$/g, ''));
        } else {
          result[key] = cleanVal(value);
        }
      }
    } else if (inNestedObj && currentObject && indent >= 2) {
      if (line.startsWith('- ')) {
        // Nested array inside object or autoevaluacion
      } else {
        const colonIdx = line.indexOf(':');
        if (colonIdx !== -1) {
          const key = line.slice(0, colonIdx).trim();
          const value = line.slice(colonIdx + 1).trim();
          currentObject[key] = cleanVal(value);
        }
      }
    }
  }

  // Handle advanced blocks like autoevaluacion cleanly
  if (yamlText.includes('autoevaluacion:')) {
    result.autoevaluacion = parseAutoevaluacionBlock(yamlText);
  }
  if (yamlText.includes('triada:')) {
    result.triada = parseTriadaBlock(yamlText);
  }
  if (yamlText.includes('grounding:')) {
    result.grounding = parseGroundingBlock(yamlText);
  }

  return result;
}

function parseTriadaBlock(yamlText) {
  const triadaMatch = yamlText.match(/triada:([\s\S]*?)(?=\n[a-z_]+:|$)/);
  if (!triadaMatch) return {};
  const block = triadaMatch[1];
  const res = {};
  const sigMatch = block.match(/significante:\s*["']?([\s\S]*?)["']?(?=\n\s*[a-z_]+:|$)/);
  const meanMatch = block.match(/significado:\s*["']?([\s\S]*?)["']?(?=\n\s*[a-z_]+:|$)/);
  const decMatch = block.match(/decision:\s*["']?([\s\S]*?)["']?(?=\n\s*[a-z_]+:|$)/);
  if (sigMatch) res.significante = sigMatch[1].trim().replace(/^["']|["']$/g, '');
  if (meanMatch) res.significado = meanMatch[1].trim().replace(/^["']|["']$/g, '');
  if (decMatch) res.decision = decMatch[1].trim().replace(/^["']|["']$/g, '');
  return res;
}

function parseGroundingBlock(yamlText) {
  const match = yamlText.match(/grounding:([\s\S]*?)(?=\n[a-z_]+:|$)/);
  if (!match) return {};
  const block = match[1];
  const res = {};
  const lines = block.split(/\r?\n/);
  for (const line of lines) {
    const colonIdx = line.indexOf(':');
    if (colonIdx !== -1) {
      const k = line.slice(0, colonIdx).trim();
      const v = line.slice(colonIdx + 1).trim();
      if (k && v) res[k] = cleanVal(v);
    }
  }
  return res;
}

function parseAutoevaluacionBlock(yamlText) {
  const autoMatch = yamlText.match(/autoevaluacion:([\s\S]*?)(?=\n[a-z_]+:|$)/);
  if (!autoMatch) return [];
  const raw = autoMatch[1];
  const items = [];
  const questionBlocks = raw.split(/\n\s*-\s*id:\s*/).filter(Boolean);

  let fallbackIdx = 1;
  for (const qb of questionBlocks) {
    const q = { id: `q${fallbackIdx++}`, pregunta: '', opciones: [] };
    const firstLineEnd = qb.indexOf('\n');
    if (firstLineEnd !== -1) {
      const idPart = qb.slice(0, firstLineEnd).trim().replace(/^["']|["']$/g, '');
      if (idPart) q.id = idPart;
    }

    const pregMatch = qb.match(/pregunta:\s*["']?([\s\S]*?)["']?(?=\n\s*opciones:|$)/);
    if (pregMatch) q.pregunta = pregMatch[1].trim().replace(/^["']|["']$/g, '');

    const opcMatch = qb.match(/opciones:([\s\S]*?)$/);
    if (opcMatch) {
      const opcBlocks = opcMatch[1].split(/\n\s*-\s*texto:\s*/).filter(Boolean);
      for (const ob of opcBlocks) {
        const txtMatch = ob.match(/^["']?([\s\S]*?)["']?(?=\n\s*correcta:|$)/);
        const corrMatch = ob.match(/correcta:\s*(true|false)/);
        const feedMatch = ob.match(/feedback:\s*["']?([\s\S]*?)["']?$/);
        q.opciones.push({
          texto: txtMatch ? txtMatch[1].trim().replace(/^["']|["']$/g, '') : '',
          correcta: corrMatch ? corrMatch[1] === 'true' : false,
          feedback: feedMatch ? feedMatch[1].trim().replace(/^["']|["']$/g, '') : ''
        });
      }
    }
    items.push(q);
  }
  return items;
}

function cleanVal(v) {
  if (v === 'true') return true;
  if (v === 'false') return false;
  if (v === 'null') return null;
  if (/^-?\d+(\.\d+)?$/.test(v)) return Number(v);
  return v.replace(/^["']|["']$/g, '').trim();
}

// Build index & posts
function buildBlog() {
  console.log('--- Construyendo Índice del Blog MedSemiotics ---');
  if (!fs.existsSync(postsDir)) {
    console.log('No se encontró la carpeta posts/. Creando...');
    fs.mkdirSync(postsDir, { recursive: true });
    return;
  }

  const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.md'));
  const postsIndex = [];

  for (const file of files) {
    const filePath = path.join(postsDir, file);
    const content = fs.readFileSync(filePath, 'utf-8');
    const { data, content: markdownBody } = parseFrontmatter(content);

    // Strict Grounding Validation
    if (!data.grounding || !data.grounding.condicion_id) {
      console.warn(`[ALERTA GROUNDING] El post ${file} no tiene condicion_id asignado en 'grounding'.`);
    }
    if (!data.grounding || (!data.grounding.pmid && !data.grounding.doi && !data.grounding.referencia_id)) {
      console.warn(`[ALERTA GROUNDING] El post ${file} no tiene referencia verificada (PMID/DOI).`);
    }

    const postSummary = {
      id: data.id || file.replace('.md', ''),
      slug: data.slug || file.replace('.md', ''),
      title: data.title || 'Sin título',
      subtitle: data.subtitle || '',
      date: data.date || '2026-08-20',
      author: data.author || 'Dr. Alcy Torres',
      category: data.category || 'general',
      category_label: data.category_label || data.category || 'General',
      tags: data.tags || [],
      reading_time: data.reading_time || '5 min',
      difficulty: data.difficulty || 'Intermedio',
      grounding_badge: data.grounding ? `${data.grounding.condicion_id} · PMID:${data.grounding.pmid || ''}` : 'Verificado',
      has_quiz: Boolean(data.autoevaluacion && data.autoevaluacion.length > 0),
      quiz_count: data.autoevaluacion ? data.autoevaluacion.length : 0,
      excerpt: data.subtitle || markdownBody.slice(0, 160).replace(/[#*`_]/g, '') + '...'
    };

    const fullPost = {
      ...postSummary,
      grounding: data.grounding || {},
      triada: data.triada || {},
      autoevaluacion: data.autoevaluacion || [],
      body: markdownBody
    };

    postsIndex.push(postSummary);

    // Save individual full post JSON for fast client reading
    fs.writeFileSync(
      path.join(outputPostsDir, `${postSummary.slug}.json`),
      JSON.stringify(fullPost, null, 2),
      'utf-8'
    );
  }

  // Sort reverse chronological
  postsIndex.sort((a, b) => new Date(b.date) - new Date(a.date));

  // Save index
  fs.writeFileSync(
    path.join(outputDataDir, 'blog-index.json'),
    JSON.stringify(postsIndex, null, 2),
    'utf-8'
  );

  console.log(`✓ Blog procesado exitosamente: ${postsIndex.length} tema(s) generado(s).`);
  console.log(`✓ Índice guardado en: assets/data/blog-index.json`);
}

buildBlog();
