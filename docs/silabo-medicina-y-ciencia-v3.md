# UNIVERSIDAD CENTRAL DEL ECUADOR

## FACULTAD DE CIENCIAS MÉDICAS — CARRERA DE MEDICINA

### CÁTEDRA DE MEDICINA Y CIENCIA

**Sedes de práctica:** IESS San Francisco y MSP Calderón

> **Estado: BORRADOR v3.0 para revisión del docente.** Período, horario y fecha de inicio los
> confirmó el docente. Las ponderaciones se mantienen (40 % formativa, 60 % sumativa). Las fechas son todos los miércoles consecutivos desde el
> inicio; las del 23 y 30 de diciembre y las de carnaval deben confirmarse como clase o receso.

---

## 1. Datos informativos

| Parámetro               | Detalle                                                                                                                             |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| **Asignatura**          | Medicina y Ciencia: Ciencia de datos y estadística biomédica en el razonamiento clínico                                             |
| **Docente**             | Dr. Alcy Torres — Medicina Interna                                                                                                  |
| **Período**             | 2026-2027                                                                                                                            |
| **Horario**             | Miércoles 20:00–21:30 (1 sesión semanal de 90 min)                                                                                  |
| **Inicio / fin**        | 11 de noviembre de 2026 / 24 de febrero de 2027 (16 sesiones)                                                                       |
| **Plataforma web**      | <https://powersemiotics.com/medsemiotics/index.html> y <https://powersemiotics.com/medsemiotics/medicina_y_datos.html>             |
| **Aula virtual**        | Google Classroom de la cátedra                                                                                                      |
| **Fuente clínica**      | [medsemiotics-db](https://github.com/alcyedmundo281/medsemiotics-db): hallazgos, LR+, LR−, sensibilidad, especificidad y referencias |

## 2. Qué cambia respecto a la versión anterior

La versión 2 ordenaba el curso por **herramientas** (diseño epidemiológico, bases de datos,
RStudio y SQLite). Los estudiantes pidieron más componente clínico. La versión 3 invierte el
eje: **cada concepto estadístico se aprende resolviendo un caso clínico del blog**, y la
herramienta computacional entra cuando el caso la necesita.

| Antes (v2)                                  | Ahora (v3)                                                                          |
| :------------------------------------------ | :---------------------------------------------------------------------------------- |
| Estadística como fin                        | Estadística como **instrumento de decisión diagnóstica**                            |
| Un caso de práctica (Chimborazo)            | **48 condiciones** del blog con LR+/LR− documentados, usadas como casos de uso      |
| Evaluación centrada en protocolo y base CSV | Evaluación centrada en **razonar con probabilidades** y luego sustentar con datos   |
| Datos sintéticos como ejemplo único         | Evidencia publicada (JAMA Rational Clinical Examination y similares) + datos locales |

Se **conserva** lo que funcionó: PICO y estructura de datos (Evaluación 1), ENSANUT y MIMIC-IV
Demo con ética de datos (Deber de julio), DAGs y el caso TRH, y el Laboratorio de Código.

## 3. Resultados de aprendizaje

Al finalizar, el estudiante será capaz de:

1. **Calcular e interpretar** sensibilidad, especificidad, VPP, VPN, LR+ y LR− a partir de una tabla 2×2 y de la literatura.
2. **Actualizar la probabilidad** de enfermedad (pretest → postest) con odds, LR y nomograma de Fagan, y relacionarla con umbrales de decisión.
3. **Combinar hallazgos** con criterio, reconociendo cuándo el supuesto de independencia falla.
4. **Valorar críticamente** un estudio de exactitud diagnóstica (STARD, QUADAS-2, sesgo de espectro) y la incertidumbre de un LR (IC 95 %).
5. **Distinguir** diagnóstico, pronóstico y causalidad, y reconocer confusión, colisionadores y sesgos cognitivos.
6. **Manejar datos clínicos** con ética: estructurar, consultar (SQL) y analizar (R/Python) una base anonimizada.
7. **Evaluar y comunicar** modelos de predicción e IA clínica (discriminación, calibración, explicabilidad) y el riesgo al paciente.

## 4. Eje del curso: la ruta de un hallazgo

```
Hallazgo clínico → ¿qué tan frecuente es? (probabilidad basal)
                → ¿qué tan informativo es? (sens/esp → LR+ / LR−)
                → ¿qué tan seguro es ese número? (IC 95 %, calidad del estudio)
                → ¿cambia la conducta? (umbrales) → ¿cómo se lo digo al paciente?
```

Cada sesión usa **una condición del blog** como caso ancla. Los valores numéricos se toman
siempre del artículo correspondiente (que a su vez deriva de medsemiotics-db); el docente no
los sustituye por cifras de memoria.

## 5. Estructura de cada sesión (90 min)

| Min   | Momento                      | Descripción                                                                                                                      |
| :---- | :--------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| 0–10  | Caso socrático               | Viñeta del caso ABP (`casos/HM####`) sin revelar el cociente; el estudiante estima la probabilidad pretest.                       |
| 10–35 | Concepto                     | Mini-clase del concepto estadístico del día, anclado en el caso.                                                                 |
| 35–65 | Cálculo y debate             | Trabajo en parejas: tabla 2×2, LR, probabilidad postest. Herramienta: calculadora de *Estadísticos Clínicos* o código en R/Python. |
| 65–80 | Autoevaluación               | Preguntas del blog (`Reto clínico`) sobre el LR documentado.                                                                     |
| 80–90 | Cierre                       | «¿Qué cambia en la conducta?» y límites de la evidencia.                                                                         |

## 6. Cronograma de 16 semanas (miércoles 20:00–21:30)

### Unidad 1 — Del hallazgo al número (semanas 1–4)

| Sem. | Tema                                                                                                         | Caso ancla (blog)                                           | Recurso en el sitio                                          |
| :--: | :----------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- | :----------------------------------------------------------- |
| 1 · 11 nov 2026 | El razonamiento clínico como inferencia: abducción, deducción, inducción; qué es un hallazgo como evidencia  | Presentación del blog; recorrido por un artículo completo   | Fundamentos semióticos; Razonamiento clínico                 |
| 2 · 18 nov 2026 | Datos clínicos: tipos de variable, bases relacionales, ENSANUT, MIMIC-IV, desidentificación y ética          | Datos de Chimborazo (continuidad con el Deber de julio)     | Laboratorio de Código; Estadísticos Clínicos                 |
| 3 · 25 nov 2026 | Tabla 2×2: sensibilidad, especificidad, VPP y VPN; por qué el VPP depende de la prevalencia                  | HM6009 Faringitis estreptocócica                            | Cuantificando la incertidumbre                               |
| 4 · 02 dic 2026 | De sens/esp a **LR+ y LR−**: definición, interpretación, magnitudes que cambian la conducta                  | HM6007 Síndrome coronario agudo (descenso del ST)           | Cuantificando la incertidumbre; artículo HM6007              |

### Unidad 2 — Razonar con probabilidades (semanas 5–8)

| Sem. | Tema                                                                                          | Caso ancla (blog)                                              | Recurso en el sitio                |
| :--: | :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------- | :--------------------------------- |
| 5 · 09 dic 2026 | Probabilidad pretest, odds y nomograma de Fagan; intuición bayesiana y falacia de la tasa base | HM6043 Apendicitis aguda                                       | La Intuición Bayesiana             |
| 6 · 16 dic 2026 | Combinar hallazgos: producto de LR, independencia condicional y sus límites                    | HM6040 Pancreatitis aguda; HM6042 Colecistitis aguda           | Artículos HM6040 y HM6042          |
| 7 · 23 dic 2026 | Umbrales de prueba y de tratamiento; cuándo una prueba no debe pedirse                         | HM6044 Tromboembolia pulmonar; HM6035 Trombosis venosa profunda | Artículos HM6044 y HM6035          |
| 8 · 30 dic 2026 | **Evaluación 1:** razonamiento bayesiano sobre casos nuevos                                    | Casos no vistos de la lista de condiciones                     | Reto clínico                       |

### Unidad 3 — Cuán seguro es el número (semanas 9–12)

| Sem. | Tema                                                                                                              | Caso ancla (blog)                                         | Recurso en el sitio                          |
| :--: | :---------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- | :------------------------------------------- |
| 9 · 06 ene 2027 | Incertidumbre estadística: IC 95 %, valor p, tamaño de efecto; leer el IC de un LR                                | HM6007 (LR+ 5.3, IC 2.1–8.6) y HM6036 Neumonía infantil   | Cuantificando la incertidumbre               |
| 10 · 13 ene 2027 | Calidad de los estudios de exactitud: STARD, QUADAS-2, sesgo de espectro y de verificación                        | HM6034 Cáncer de mama                                     | Artículo HM6034                              |
| 11 · 20 ene 2027 | Reglas de decisión clínica, puntos de corte y curvas ROC                                                          | HM6038 Lesión intracraneal en TCE leve                    | Artículo HM6038                              |
| 12 · 27 ene 2027 | Sesgos cognitivos (anclaje, disponibilidad) y **causalidad**: confusión, colisionadores, DAG                      | CausalMed: el caso TRH; reingresos y TEV en Chimborazo    | Sesgos de la mente; Inferencia causal        |

### Unidad 4 — Datos, IA y comunicación (semanas 13–16)

| Sem. | Tema                                                                                                    | Caso ancla (blog)                                       | Recurso en el sitio                          |
| :--: | :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------ | :------------------------------------------- |
| 13 · 03 feb 2027 | Laboratorio de datos: consultas SQL y análisis en R/Python; calcular sens/esp/LR desde una base         | Base anonimizada de Chimborazo                          | Laboratorio de Código                        |
| 14 · 10 feb 2027 | Modelos de predicción e IA clínica: discriminación, calibración, validación externa, explicabilidad    | HM6030 Infarto agudo de miocardio                       | Razonamiento clínico: IA explicable          |
| 15 · 17 feb 2027 | Comunicar el riesgo: frecuencias naturales, visualización y decisión compartida                         | HM6029 Hipertensión arterial esencial                   | Comunicación y visualización                 |
| 16 · 24 feb 2027 | **Evaluación final / proyecto integrador** (ver §7)                                                     | Caso elegido por el grupo                               | Todos                                        |

> La lista de casos ancla es una propuesta. Cualquiera de las 48 condiciones puede
> sustituirla; conviene preferir las que ya tienen caso socrático publicado (`casos/`) y
> LR con IC documentado.

## 6 bis. Asistente del curso (agente con los estudiantes)

El repositorio `medsemiotics-copilot` funciona como asistente de la cátedra con los estudiantes.
Reglas: (1) responde desde los artículos del blog y medsemiotics-db, citando PMID/DOI; si no hay
cifra documentada, lo dice; (2) hace preguntas socráticas y no entrega la respuesta de las
evaluaciones; (3) no recibe ni almacena datos de pacientes ni de estudiantes; (4) su salida es un
borrador, no una fuente; (5) los casos nuevos se publican solo con revisor humano nominado.

## 7. Sistema de evaluación

Se **mantienen las ponderaciones** de la cátedra y de los sílabos de Neurología y Gastroenterología v2: 40 % formativa y 60 % sumativa (escala sobre 20). Esta regla no cambia entre versiones del sílabo.

| Componente                   | Peso | Instrumento                                                                                                                         |
| :--------------------------- | :--: | :---------------------------------------------------------------------------------------------------------------------------------- |
| **Formativa**                | 40 % | Informes de caso (rúbrica abajo), autoevaluaciones del *Reto clínico*, participación en el caso socrático                           |
| **Sumativa 1** (sem. 8)      | 25 % | Razonamiento bayesiano: dado un caso, estimar pretest, aplicar LR y justificar conducta                                             |
| **Sumativa final** (sem. 16) | 35 % | Proyecto integrador en parejas: pregunta clínica (PICO), base anonimizada, medidas diagnósticas con IC, límites y comunicación al paciente |

**Rúbrica del informe de caso (20 puntos, 6–6–4–4):**

| Criterio                                                                      | Puntos |
| :---------------------------------------------------------------------------- | :----: |
| Estimación y justificación de la probabilidad pretest                         | 6      |
| Cálculo e interpretación correctos (sens/esp, LR, probabilidad postest)       | 6      |
| Valoración crítica de la evidencia (IC, calidad del estudio, aplicabilidad)   | 4      |
| Decisión clínica y comunicación; referencias en formato verificable           | 4      |

**Reglas de la cátedra**

1. Todo dato de paciente debe estar **anonimizado**; no se cargan nombres, cédulas ni identificadores.
2. Las cifras diagnósticas se citan **con su referencia** (PMID/DOI); un número sin fuente no puntúa.
3. El uso de IA generativa se declara; la salida de un LLM es un borrador, no una fuente.
4. Las entregas se gestionan en Classroom; la asistencia, mediante el formulario de la cátedra.

## 8. Bibliografía y fuentes

- Simel DL, Rennie D, Bossuyt PM (eds.). *The Rational Clinical Examination: Evidence-Based Clinical Diagnosis*. JAMA/McGraw-Hill.
- Fanaroff AC, et al. Does this patient with chest pain have acute coronary syndrome? *JAMA*. 2015. doi:10.1001/jama.2015.12735 (PMID 26547467).
- Bossuyt PM, et al. STARD 2015. *BMJ*. 2015;351:h5527.
- Whiting PF, et al. QUADAS-2. *Ann Intern Med*. 2011;155:529-536.
- Johnson AEW, et al. MIMIC-IV. *Sci Data*. 2023;10:1. doi:10.1038/s41597-022-01899-x.
- INEC. ENSANUT 2018. Ecuador.
- Fuente clínica de los casos: medsemiotics-db (DOI 10.5281/zenodo.22064424).

## 9. Pendientes para el docente

1. Confirmar si el 23 y 30 de diciembre (sesiones 7 y 8, esta última con la Evaluación 1) y el carnaval de 2027 son clase o receso; si hay receso, el curso se corre o se acorta.
2. Confirmar la lista de casos ancla y si algún caso socrático nuevo debe redactarse (skill `caso-socratico`; requiere revisor humano nominado).
3. Decidir si el sílabo se publica en el sitio o se archiva como documento docente (ver `MIGRATION.md`: el sílabo de Gastroenterología se marcó «Archivar»).
4. Revisar las referencias de las sesiones 10–15, que son propuestas y no han sido verificadas contra PubMed en este borrador.
