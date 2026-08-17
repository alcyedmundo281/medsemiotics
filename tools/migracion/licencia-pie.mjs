// Sustituye el "Todos los derechos reservados" del pie por el aviso de licencia
// CC BY-SA 4.0. Se trabaja siempre con \n y al final se restituye el fin de
// línea original del archivo, para no dejarlo mezclado.
import fs from 'node:fs';

const ARCHIVOS = [
  'index.html',
  'neurologia.html',
  'gastroenterologia.html',
  'farmacoterapia_racional.html',
  'medicina_y_datos.html',
  'medicina_e_implementacion.html',
  'inmunologia_clinica.html',
];

// El año se conserva tal cual estuviera en cada página; solo cambia la cláusula.
const RE = /^([ \t]*)<p([^>]*)>&copy; (\d{4}) Powersemiotics\. Todos los derechos reservados\.<\/p>/m;

let hechos = 0;
const fallos = [];

for (const f of ARCHIVOS) {
  const original = fs.readFileSync(f, 'utf8');
  const eraCRLF = original.includes('\r\n');
  // Normalizar a \n para operar sin ambigüedad.
  let s = original.split('\r\n').join('\n');

  if (!RE.test(s)) { fallos.push(f); continue; }

  s = s.replace(RE, (_, sangria, attrs, anio) => [
    `${sangria}<p${attrs}>&copy; ${anio} Alcy Edmundo Torres Guerrero.</p>`,
    `${sangria}<p class="mt-2 text-sm">`,
    `${sangria}  Contenido bajo licencia`,
    `${sangria}  <a`,
    `${sangria}    rel="license"`,
    `${sangria}    href="https://creativecommons.org/licenses/by-sa/4.0/deed.es"`,
    `${sangria}    class="font-semibold text-indigo-700 hover:text-indigo-500 transition-colors"`,
    `${sangria}    >Creative Commons Atribución-CompartirIgual 4.0</a`,
    `${sangria}  >.`,
    `${sangria}</p>`,
  ].join('\n'));

  if (eraCRLF) s = s.split('\n').join('\r\n');
  fs.writeFileSync(f, s, 'utf8');
  hechos++;
}

console.log(`pies actualizados: ${hechos}/${ARCHIVOS.length}`);
if (fallos.length) console.log('  sin coincidencia: ' + fallos.join(', '));
