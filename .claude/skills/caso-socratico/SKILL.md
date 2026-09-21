---
name: caso-socratico
description: Redacta, revisa o actualiza el caso clínico socrático (ABP dirigido) de un artículo del blog de Medsemiotics, con su imagen destacada de Wikimedia Commons en dominio público. Usar cuando se pida editar un post del blog, darle contexto clínico, escribir un caso socrático/ABP, pasar al siguiente artículo, o poner la imagen que falta a un post.
---

# Caso socrático (ABP dirigido) para un artículo del blog

Cada artículo de `posts/` es un derivado de medsemiotics-db: evidencia sin prosa. El caso
socrático **no reemplaza esa evidencia: la contextualiza**. El foco del aprendizaje sigue siendo
lo que registra la base (hallazgos, LR, sensibilidad, especificidad, estados del LR y sus
límites); el caso aporta el paciente, la secuencia y las preguntas que obligan a usarla.

Se trabaja **un artículo por vez**, en una rama de trabajo, y con un commit por artículo.

## Reglas que el compilador hace cumplir

`uv run python -m casos check` falla si se incumple cualquiera de estas reglas:

- **Cifras solo por token.** LR, sensibilidad, especificidad, IC, PMID o IDs `HM:` nunca se
  escriben a mano. Se usan `{{lr+ HM:####}}`, `{{lr- HM:####}}`, `{{sens HM:####}}`,
  `{{esp HM:####}}`, `{{hallazgo HM:####}}` y `{{estado HM:####}}`, que se resuelven contra la
  base con su IC 95 % o su rango. Si la base corrige un valor, el caso se actualiza solo.
- **Cobertura total.** Todo hallazgo de la evidencia del artículo aparece en alguna etapa
  (`hallazgos:`) o en `omitidos:` con un motivo docente. El hallazgo principal del artículo
  (el de la calculadora) debe revelarse siempre.
- **Sin adelantar evidencia.** Un token solo puede citar hallazgos ya revelados en esa etapa o en
  las anteriores. La viñeta y los objetivos no citan evidencia.
- **Secuencia ABP:** `activacion` → `exploracion` → `discriminacion` → `decision`. Debe haber al
  menos una etapa de `discriminacion`, y las de exploración o discriminación ponen en juego al
  menos un hallazgo de la base.
- **Aprobación humana.** `estado: publicado` exige `autoria.revisor` (persona nominada) y
  `publicacion.fecha`. Solo los casos publicados llegan al sitio.

## Flujo

1. **Elegir el artículo.** `npm run casos:estado` lista los artículos con y sin caso.
2. **Leer la fuente.** Leer `posts/HM####-*.md` completo: frontmatter `evidencia` y cuerpo
   (probabilidad basal, factores de riesgo, signos de alarma, reglas, notas de uso, límites).
   Si hace falta más contexto, leer `condiciones/HM####-*.yaml` en medsemiotics-db (checkout
   local `../medsemiotics-db` o GitHub). **No se edita `posts/`**: lo regenera
   `generate_topic.py`. Un error clínico de la fuente se corrige en medsemiotics-db.
3. **Crear el borrador.** `uv run python -m casos nuevo HM####` crea `casos/HM####.yaml` con
   todos los hallazgos de la base listados en comentarios. Nunca sobrescribe.
4. **Redactar el caso** (ver «Diseño docente»). Validar a menudo con
   `uv run python -m casos check`.
5. **Imagen destacada: obligatoria, Wikimedia Commons en dominio público o CC0.**
   - `uv run python -m imagenes buscar HM#### "<término en inglés>"` lista solo candidatas PD/CC0.
     Probar varias consultas (el signo, la maniobra, la enfermedad, grabados históricos).
   - Elegir una imagen **clínicamente pertinente** al tema o a su hallazgo principal: que no
     muestre otra entidad (p. ej., líneas B de Kerley no ilustran un derrame pleural). Si no
     hay ninguna adecuada, decirlo al usuario; no forzar una imagen irrelevante.
   - `uv run python -m imagenes asignar HM#### "File:…" --alt "<descripción en español>"`
     vuelve a verificar la licencia en la API de Commons y registra autor y fecha.
   - Nunca CC BY, CC BY-SA, GFDL ni imágenes sin licencia declarada, aunque sean mejores.
6. **Revisión.** `uv run python -m casos preview HM####` imprime el caso compilado. Mostrarlo
   al usuario con la imagen elegida y pedir su revisión. Iterar.
7. **Publicación (solo con aprobación explícita del usuario en el chat).** Poner
   `estado: publicado`, `autoria.revisor: <nombre que indique el usuario>` y
   `publicacion.fecha: <fecha de hoy>`. El agente nunca se nombra revisor ni publica por su
   cuenta. Para corregir un caso ya publicado, se añade una entrada a
   `publicacion.revisiones` (fecha y nota) y no se cambia la fecha original: la versión sube sola.
8. **Compilar y pasar los gates.**
   ```bash
   npm run casos:build
   npm run build:blog
   npm run gates
   ```
   `gates` ejecuta Ruff, formato, mypy estricto, pytest, `casos check`, `imagenes check`, ESLint,
   `build-blog --check` y los tests del blog. No se hace commit con un gate en rojo.
9. **Commit** de `casos/HM####.yaml`, `assets/data/casos/`, `assets/data/topic-images.json` y
   los JSON regenerados, con un mensaje como `feat(casos): caso socrático de <tema> (HM:####)`.

## Diseño docente

Modelo de referencia: los casos de `medsemiotics-copilot/docs/caso_clinico_socratico_*.md`
(viñeta, examen dirigido, preguntas socráticas por etapas y clave docente). Aquí se adapta a
un blog público y a la evidencia de la base.

- **Objetivos (1–6):** verbos observables («interpretar», «estimar», «decidir»), centrados en
  los hallazgos de la base.
- **Viñeta:** paciente ficticio y verosímil, sin datos identificables. Motivo de consulta,
  cronología y contexto. Los signos vitales y resultados de laboratorio del relato pueden
  llevar números. No debe contradecir la población de los estudios de la base (edad, ámbito).
- **Activación:** hipótesis iniciales y conocimientos previos. Preguntas abiertas.
- **Exploración:** los hallazgos de la base aparecen como datos del paciente. El sitio muestra
  al lado de cada uno su ficha de medsemiotics-db (rol, cifras, decisión, referencia).
- **Discriminación:** el estudiante razona con los cocientes: qué hallazgo desplaza más la
  probabilidad, qué descarta, por qué un rango no es una estimación puntual, qué significa
  «sin efecto discriminativo» o «LR no medido». Remitir a la calculadora bayesiana del artículo.
- **Decisión:** juicio clínico y conducta, con los límites de la evidencia.
- **Preguntas socráticas:** una idea por pregunta, que no se respondan con la memoria. La
  `clave` es la respuesta docente razonada y se muestra plegada («razónalo primero»).
- **Cierre:** síntesis y necesidades de aprendizaje (lo que la base no responde).
- **Fisiopatología y conducta:** conocimiento clínico estándar, sin cifras ni referencias
  inventadas. Si una afirmación necesita respaldo que la base no tiene, se plantea como
  necesidad de aprendizaje o se propone añadirla a medsemiotics-db.

## Fechas e ISSN

La fecha de publicación del artículo es el `date` del post (primera aparición de su URL, que
`generate_topic.py` preserva). El caso aporta la fecha de revisión y la versión. `post.html`
expone ambas en metadatos Highwire (`citation_*`), Dublin Core y JSON-LD `ScholarlyArticle`.
No inventar ni retrotraer fechas.
