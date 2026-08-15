import globals from 'globals';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import js from '@eslint/js';
import { FlatCompat } from '@eslint/eslintrc';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all,
});

export default [
  {
    // Third-party libraries and generated bundles are build outputs, not
    // lintable source. Their corresponding editable sources remain in the
    // repository and are covered by the configurations below.
    ignores: [
      '**/dist/',
      '**/node_modules/',
      'assets/vendor/',
      '**/*.bundle.js',
      'gastroenterologia/pancreatitis_aguda/assets/',
      'medicina_y_datos/estadisticos_descubiertos/assets/',
    ],
  },
  ...compat.extends('eslint:recommended'),
  {
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.node,
      },
      ecmaVersion: 'latest',
      sourceType: 'module',
    },
    rules: {},
  },
];
