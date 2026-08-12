const http = require('http');
const fs = require('fs');
const path = require('path');

// El sitio se publica en https://powersemiotics.com/medsemiotics/, es decir
// bajo un subdirectorio del dominio. El servidor local monta el repositorio en
// ese mismo prefijo para que las rutas se comporten igual que en producción.
const port = process.env.PORT || 3000;
const basePath = process.env.BASE_PATH || '/medsemiotics';
// El servidor vive en tools/, pero sirve la raiz del repositorio.
const baseDir = path.resolve(__dirname, '..');

const mimeTypes = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.mjs': 'application/javascript; charset=utf-8',
  '.jsx': 'application/javascript; charset=utf-8',
  '.ts': 'application/javascript; charset=utf-8',
  '.tsx': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.csv': 'text/csv; charset=utf-8',
  '.txt': 'text/plain; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.gif': 'image/gif',
  '.webp': 'image/webp',
  '.ico': 'image/x-icon',
  '.pdf': 'application/pdf',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
};

function send(res, status, body, type = 'text/plain; charset=utf-8') {
  res.statusCode = status;
  res.setHeader('Content-Type', type);
  res.end(body);
}

const server = http.createServer((req, res) => {
  const url = new URL(req.url, `http://localhost:${port}`);
  let pathname = decodeURIComponent(url.pathname);

  // Fuera del prefijo no hay nada que servir: la raíz del dominio pertenece al
  // repositorio corporativo, no a este.
  if (pathname === '/' || pathname === basePath) {
    res.statusCode = 302;
    res.setHeader('Location', `${basePath}/`);
    res.end();
    return;
  }
  if (!pathname.startsWith(`${basePath}/`)) {
    console.log(`404 (fuera del prefijo ${basePath}/) ${pathname}`);
    send(res, 404, `Not Found: ${pathname} está fuera de ${basePath}/`);
    return;
  }

  let relative = pathname.slice(basePath.length + 1);
  if (relative === '' || relative.endsWith('/')) {
    relative += 'index.html';
  }

  const filePath = path.join(baseDir, relative);
  // No servir nada por encima del directorio del repositorio.
  if (!filePath.startsWith(baseDir)) {
    send(res, 403, 'Forbidden');
    return;
  }

  fs.stat(filePath, (statErr, stats) => {
    if (statErr) {
      console.log(`404 ${pathname}`);
      send(res, 404, `Not Found: ${pathname}`);
      return;
    }
    // Un directorio sin barra final se redirige, igual que hace GitHub Pages.
    if (stats.isDirectory()) {
      res.statusCode = 302;
      res.setHeader('Location', `${pathname}/`);
      res.end();
      return;
    }
    fs.readFile(filePath, (err, content) => {
      if (err) {
        send(res, 404, `Not Found: ${pathname}`);
        return;
      }
      const ext = path.extname(filePath).toLowerCase();
      res.statusCode = 200;
      res.setHeader('Content-Type', mimeTypes[ext] || 'application/octet-stream');
      res.end(content);
    });
  });
});

server.listen(port, () => {
  console.log(`Sitio disponible en http://localhost:${port}${basePath}/`);
});
