---
id: HM6045-01
slug: taponamiento-cardiaco-precision-semiotica
title: 'Taponamiento cardíaco: hallazgos y evidencia clínica'
subtitle: Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.
date: '2026-09-21'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- semiologia
- taponamiento-cardiaco
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 9c9015322734168fe0328362950237f8ad296a55
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6045-taponamiento-cardiaco.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0100-signo-vital-alterado.yaml: 3e0914bff0c0dc8f1a07185d49c70c4ee7dcf11cfa7ebc3281d611f5abb4f504
    conceptos/HM0104-taquicardia.yaml: a71b0c60cea7fec615df5f089557df4c7275da3ab54bb060c0651c5ff79f15d6
    conceptos/HM0109-hipotension-arterial.yaml: 934b7dadbc768a08d34a84a322bb11c8008218f7b111b1bba2b766e67f4db7cc
    conceptos/HM0600-signo-de-exploracion.yaml: 86a2ac9babe66028eecc797ddbf4d9ea382a6fd685e9cb8df91bb959029d62bf
    conceptos/HM0900-hallazgo-de-imagen.yaml: 0b40c9368c746533cc335071c04e027c4465fb29158ed2cc747d65b9bb573e67
    conceptos/HM3146-ingurgitacion-yugular.yaml: 68f00e3333cd5790afa7a4f9a6a550b2feee50898fb40eda646b356d00312ab0
    conceptos/HM3155-derrame-pericardico-en-ecografia.yaml: 049d32edd47c084b8b87549994e90e0b312f7c07a6c83683b35bd30eb35825c4
    conceptos/HM3162-ventriculo-derecho-dilatado.yaml: bfbfab4ea78921d69f2891162121e678a9686759e3c10007725acb3228e09134
    conceptos/HM3163-taponamiento-cardiaco-en-ecografia.yaml: 8b19b30092dd4dd2ab9455f9084a4bcd322b5e3e1dbe77821ae96cfea200f621
    condiciones/HM6045-taponamiento-cardiaco.yaml: 9968e16d03dba30116bdc00d69ac12b38601117eab695d5827c675c9f2b28e19
    referencias/pmid-35696801.yaml: d2c0807fd4b21b2c1693489c411d348016f85e8b910cf65c9b8ae1afed98dcd2
    referencias/pmid-41729549.yaml: a3b8210b679e9dff1f5671c3127d08ad54fcd26329cfe6735e29183e0cc98937
grounding:
  condicion_id: HM:6045
  condicion_nombre: Taponamiento cardíaco
  concepto_id: HM:3163
  concepto_nombre: Taponamiento cardíaco en ecografía
  estado_lr: no_medido
  lr_positivo: null
  lr_negativo: null
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: pacientes con derrame pericárdico evaluados en urgencias o cuidados críticos mediante ecocardiografía a pie de cama; revisión de Alerhand 2022
  referencia_id: pmid:35696801
  referencia_cita: 'Alerhand S, Adrian RJ, Long B, Avila J Pericardial tamponade: A comprehensive emergency medicine and echocardiography review Am J Emerg Med 2022'
  pmid: '35696801'
  doi: 10.1016/j.ajem.2022.05.001
triada:
  significante: Derrame pericárdico con colapso diastólico del ventrículo derecho, colapso sistólico de la aurícula derecha, vena cava inferior dilatada (pletórica) sin colapso inspiratorio y, en derrames grandes, corazón oscilante (swinging heart).
  significado: 'Presión intrapericárdica elevada que restringe el llenado de las cavidades derechas: fisiología de taponamiento, distinta de solo tener líquido pericárdico.'
  decision: la presencia de colapso diastólico del ventrículo derecho o colapso sistólico de la aurícula derecha en un paciente con inestabilidad hemodinámica acelera de inmediato la activación del equipo para pericardiocentesis evacuadora o ventana pericárdica quirúrgica de emergencia
evidencia:
- concepto: HM:3163
  rol: imagen
  estado_lr: no_medido
  sostiene: consenso_con_afirmacion
  ref: pmid:35696801
  poblacion: pacientes con derrame pericárdico evaluados en urgencias o cuidados críticos mediante ecocardiografía a pie de cama; revisión de Alerhand 2022
  decision: la presencia de colapso diastólico del ventrículo derecho o colapso sistólico de la aurícula derecha en un paciente con inestabilidad hemodinámica acelera de inmediato la activación del equipo para pericardiocentesis evacuadora o ventana pericárdica quirúrgica de emergencia
  advertencia: la ausencia de colapso de cavidades derechas puede ocurrir en hipertensión pulmonar grave o hipertrofia ventricular derecha previa debido a presiones diastólicas basales elevadas (falso negativo); no descarta taponamiento ante shock clínico evidente
- concepto: HM:3155
  rol: prueba_sensible
  estado_lr: no_medido
  sostiene: mecanismo
  motivo: 'precondición fisiopatológica sine qua non: no puede existir taponamiento cardíaco en ausencia de líquido o coágulo en el espacio pericárdico que eleve la presión intrapericárdica'
- concepto: HM:0109
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:3146
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:0104
  rol: apoyo
  estado_lr: no_medido
autoevaluacion:
- id: q1
  pregunta: En Taponamiento cardíaco, ¿qué estado de la evidencia corresponde a «Taponamiento cardíaco en ecografía» según la fuente?
  concepto_id: HM:3163
  referencia_id: pmid:35696801
  pmid: '35696801'
  doi: 10.1016/j.ajem.2022.05.001
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6045
    concepto_id: HM:3163
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: pacientes con derrame pericárdico evaluados en urgencias o cuidados críticos mediante ecocardiografía a pie de cama; revisión de Alerhand 2022
    motivo: null
    decision: la presencia de colapso diastólico del ventrículo derecho o colapso sistólico de la aurícula derecha en un paciente con inestabilidad hemodinámica acelera de inmediato la activación del equipo para pericardiocentesis evacuadora o ventana pericárdica quirúrgica de emergencia
    advertencia: la ausencia de colapso de cavidades derechas puede ocurrir en hipertensión pulmonar grave o hipertrofia ventricular derecha previa debido a presiones diastólicas basales elevadas (falso negativo); no descarta taponamiento ante shock clínico evidente
  opciones:
  - texto: LR no medible
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Población: pacientes con derrame pericárdico evaluados en urgencias o cuidados críticos mediante ecocardiografía a pie de cama; revisión de Alerhand 2022. Interpretación registrada: la presencia de colapso diastólico del ventrículo derecho o colapso sistólico de la aurícula derecha en un paciente con inestabilidad hemodinámica acelera de inmediato la activación del equipo para pericardiocentesis evacuadora o ventana pericárdica quirúrgica de emergencia. Advertencia: la ausencia de colapso de cavidades derechas puede ocurrir en hipertensión pulmonar grave o hipertrofia ventricular derecha previa debido a presiones diastólicas basales elevadas (falso negativo); no descarta taponamiento ante shock clínico evidente.'
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Población: pacientes con derrame pericárdico evaluados en urgencias o cuidados críticos mediante ecocardiografía a pie de cama; revisión de Alerhand 2022. Interpretación registrada: la presencia de colapso diastólico del ventrículo derecho o colapso sistólico de la aurícula derecha en un paciente con inestabilidad hemodinámica acelera de inmediato la activación del equipo para pericardiocentesis evacuadora o ventana pericárdica quirúrgica de emergencia. Advertencia: la ausencia de colapso de cavidades derechas puede ocurrir en hipertensión pulmonar grave o hipertrofia ventricular derecha previa debido a presiones diastólicas basales elevadas (falso negativo); no descarta taponamiento ante shock clínico evidente.'
  - texto: LR no medido
    correcta: true
    feedback: 'LR no medido Población: pacientes con derrame pericárdico evaluados en urgencias o cuidados críticos mediante ecocardiografía a pie de cama; revisión de Alerhand 2022. Interpretación registrada: la presencia de colapso diastólico del ventrículo derecho o colapso sistólico de la aurícula derecha en un paciente con inestabilidad hemodinámica acelera de inmediato la activación del equipo para pericardiocentesis evacuadora o ventana pericárdica quirúrgica de emergencia. Advertencia: la ausencia de colapso de cavidades derechas puede ocurrir en hipertensión pulmonar grave o hipertrofia ventricular derecha previa debido a presiones diastólicas basales elevadas (falso negativo); no descarta taponamiento ante shock clínico evidente.'
- id: q2
  pregunta: En Taponamiento cardíaco, ¿qué estado de la evidencia corresponde a «Derrame pericárdico en ecografía» según la fuente?
  concepto_id: HM:3155
  referencia_id: null
  pmid: null
  doi: null
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6045
    concepto_id: HM:3155
    estado_lr: no_medido
    campo: null
    dato: null
    poblacion: null
    motivo: 'precondición fisiopatológica sine qua non: no puede existir taponamiento cardíaco en ausencia de líquido o coágulo en el espacio pericárdico que eleve la presión intrapericárdica'
    decision: null
    advertencia: null
  opciones:
  - texto: Sin efecto discriminativo
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Motivo: precondición fisiopatológica sine qua non: no puede existir taponamiento cardíaco en ausencia de líquido o coágulo en el espacio pericárdico que eleve la presión intrapericárdica.'
  - texto: LR no medido
    correcta: true
    feedback: 'LR no medido Motivo: precondición fisiopatológica sine qua non: no puede existir taponamiento cardíaco en ausencia de líquido o coágulo en el espacio pericárdico que eleve la presión intrapericárdica.'
  - texto: LR no medible
    correcta: false
    feedback: 'La fuente clasifica este hallazgo como «LR no medido». LR no medido Motivo: precondición fisiopatológica sine qua non: no puede existir taponamiento cardíaco en ausencia de líquido o coágulo en el espacio pericárdico que eleve la presión intrapericárdica.'
---

# Taponamiento cardíaco

Hallazgos y criterios clínicos sin cocientes de verosimilitud medidos.

## Nombre en inglés

Cardiac tamponade

## Sinónimos

taponamiento pericárdico

compromiso hemodinámico por derrame pericárdico

## Códigos

Snomed: 42232009; Cie10: I31.4

## Factores de riesgo

neoplasia maligna con metástasis pericárdicas

pericarditis aguda o recurrente

insuficiencia renal crónica terminal o uremia

traumatismo torácico penetrante o cerrado

procedimiento invasivo cardiovascular o cirugía cardíaca reciente

disección aórtica tipo A con hemopericardio retrógrado

## Hallazgos clínicos

### Taponamiento cardíaco en ecografía (HM:3163)

**Significante:** Derrame pericárdico con colapso diastólico del ventrículo derecho, colapso sistólico de la aurícula derecha, vena cava inferior dilatada (pletórica) sin colapso inspiratorio y, en derrames grandes, corazón oscilante (swinging heart).

**Significado:** Presión intrapericárdica elevada que restringe el llenado de las cavidades derechas: fisiología de taponamiento, distinta de solo tener líquido pericárdico.

**Falsos positivos:** Colapso de cavidades derechas por hipovolemia grave —el 'síndrome del corazón vacío'—, sin taponamiento real / Hipertensión pulmonar o hipertrofia del ventrículo derecho: retrasan o enmascaran el colapso (falso negativo, no una tranquilidad) / Derrame loculado o coágulo posquirúrgico que comprime una sola cámara: no produce el patrón circunferencial clásico / Coágulo o hematoma pericárdico posquirúrgico ecogénico: puede parecer tejido sólido y pasar inadvertido por vía transtorácica —otro falso negativo, distinto al del punto anterior / Vena cava inferior dilatada por falla derecha o ventilación con presión positiva, sin taponamiento / Ventana única, mala calidad de imagen o taquicardia extrema que dificulta juzgar el momento del ciclo cardíaco

**Rol:** Imagen

**Estado del LR:** LR no medido

**Sostiene:** Afirmación respaldada por consenso

**Referencia:** pmid:35696801

**Población:** pacientes con derrame pericárdico evaluados en urgencias o cuidados críticos mediante ecocardiografía a pie de cama; revisión de Alerhand 2022

**Decisión:** la presencia de colapso diastólico del ventrículo derecho o colapso sistólico de la aurícula derecha en un paciente con inestabilidad hemodinámica acelera de inmediato la activación del equipo para pericardiocentesis evacuadora o ventana pericárdica quirúrgica de emergencia

**Advertencia:** la ausencia de colapso de cavidades derechas puede ocurrir en hipertensión pulmonar grave o hipertrofia ventricular derecha previa debido a presiones diastólicas basales elevadas (falso negativo); no descarta taponamiento ante shock clínico evidente

### Derrame pericárdico en ecografía (HM:3155)

**Significante:** Espacio anecoico o hipoecoico entre el miocardio y el pericardio, visible y confirmable en más de una ventana cardíaca.

**Significado:** Líquido en el espacio pericárdico; su presencia no demuestra por sí sola fisiología de taponamiento.

**Falsos positivos:** Grasa epicárdica o pericárdica / Derrame pleural visto detrás de la aorta descendente / Ascitis adyacente a la ventana subcostal / Quiste o masa mediastínica / Ganancia excesiva o plano oblicuo que crea un espacio oscuro

**Rol:** Prueba sensible

**Estado del LR:** LR no medido

**Sostiene:** mecanismo

**Motivo:** precondición fisiopatológica sine qua non: no puede existir taponamiento cardíaco en ausencia de líquido o coágulo en el espacio pericárdico que eleve la presión intrapericárdica

### Hipotensión arterial (HM:0109)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Ingurgitación yugular (HM:3146)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Taquicardia (HM:0104)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

## Notas de uso

RENDIMIENTO POR RANGOS DE LA REVISIÓN DE ALERHAND 2022 (pmid:35696801): el colapso diastólico del ventrículo derecho presenta sensibilidad del 48% al 100% y especificidad del 72% al 100% entre series; el colapso sistólico de la aurícula derecha rinde sensibilidad del 50% al 100% y especificidad del 33% al 100%. La vena cava inferior pletórica sin colapso inspiratorio aporta alta sensibilidad (>95%) para descartar taponamiento cuando es normal. No se calculan cocientes agrupados sintéticos: los estudios originales publican rangos de sensibilidad y especificidad sin metaanálisis de LR.

## Conclusión de la fuente

El colapso de cavidades derechas y la pletora de la vena cava inferior en presencia de derrame pericárdico son los pilares ecocardiográficos que definen la fisiología de taponamiento; integrados con la inestabilidad hemodinámica, guían la indicación de descompresión pericárdica urgente.

## Referencias y procedencia

**pmid:35696801:** Pericardial tamponade: A comprehensive emergency medicine and echocardiography review. Am J Emerg Med, 2022. DOI: 10.1016/j.ajem.2022.05.001.

**pmid:41729549:** Does This Patient Have Volume Overload?: The Rational Clinical Examination. JAMA, 2026. DOI: 10.1001/jama.2026.0446.

Fuente clínica: medsemiotics-db, condición HM:6045.
