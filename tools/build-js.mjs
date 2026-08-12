// Compila los módulos interactivos React (.jsx) a bundles planos.
// El navegador no ve JSX: Babel standalone ya no interviene.
// React y ReactDOM llegan como globales UMD, así que se marcan como externos.
import { build } from 'esbuild';
import path from 'node:path';

const ENTRIES = [
  'gastroenterologia/trastornos-estomacales.jsx',
  'inmunologia/alergias-alimentarias.jsx',
  'inmunologia/hipersensibilidad-farmacos.jsx',
  'inmunologia/inmunologia-trasplante.jsx',
  'inmunologia/laboratorio-inmunologia.jsx',
  'inmunologia/vacunas.jsx',
  'neurologia/acv-isquemico.jsx',
  'neurologia/epilepsia-ii/masterclass.jsx',
];

let failed = 0;
for (const entry of ENTRIES) {
  const out = entry.replace(/\.jsx$/, '.bundle.js');
  try {
    await build({
      entryPoints: [entry],
      outfile: out,
      bundle: true,
      format: 'iife',
      target: ['es2018'],
      minify: true,
      loader: { '.jsx': 'jsx' },
      jsx: 'transform',
      jsxFactory: 'React.createElement',
      jsxFragment: 'React.Fragment',
      logLevel: 'warning',
      banner: { js: '/* Generado por `npm run build:js` desde ' + path.basename(entry) + '. No editar. */' },
    });
    console.log('OK  ' + out);
  } catch (e) {
    failed++;
    console.error('FALLO ' + entry + ': ' + (e.message || e).toString().slice(0, 300));
  }
}
if (failed) process.exit(1);
