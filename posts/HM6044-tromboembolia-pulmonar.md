---
id: HM6044-01
slug: tromboembolia-pulmonar-precision-semiotica
title: 'Tromboembolia pulmonar: hallazgos y evidencia clínica'
subtitle: Hallazgos, cocientes documentados y límites de la evidencia.
date: '2026-09-21'
author: Dr. Alcy Torres
category: medicina_interna
category_label: Medicina Interna
tags:
- medicina_interna
- semiologia
- tromboembolia-pulmonar
reading_time: 8 min
difficulty: Intermedio
fuente:
  repositorio: alcyedmundo281/medsemiotics-db
  revision: 1d33074a25224a006e43e010c4be6ad39a771e7e
  doi: 10.5281/zenodo.22064424
  condicion: condiciones/HM6044-tromboembolia-pulmonar.yaml
  archivos:
    CITATION.cff: 6e9c73a515bb6225965edda4efc52104a4e3b9776dab1bd4fce8e643d86eb1d2
    conceptos/HM0100-signo-vital-alterado.yaml: 3e0914bff0c0dc8f1a07185d49c70c4ee7dcf11cfa7ebc3281d611f5abb4f504
    conceptos/HM0104-taquicardia.yaml: a71b0c60cea7fec615df5f089557df4c7275da3ab54bb060c0651c5ff79f15d6
    conceptos/HM0110-hipoxemia.yaml: 618b916bc8d46710e8ad723489a7e11b4428f5bf9680f2a7df81ede750ed150d
    conceptos/HM0206-dolor-toracico.yaml: b0ab2dde126e6fb4d8543adeb2d5fce843a1ce51a2de62c293deda255cc1973f
    conceptos/HM0400-sintoma-respiratorio.yaml: 437414db42a3586a5896d3f91e90ee8ed51c7baef7b67741067b3ee04ca7a53b
    conceptos/HM0401-disnea.yaml: 8d19bcb0b5f9365e8826c374183983f6c79cd6a6050a5447b59aa51ffe8076b9
    conceptos/HM0710-alteracion-hematologica.yaml: 8779ebf74773e0648f4a534cb7c6528ec05cfc16c33123eb06d539cc1aa0e3ad
    conceptos/HM0900-hallazgo-de-imagen.yaml: 0b40c9368c746533cc335071c04e027c4465fb29158ed2cc747d65b9bb573e67
    conceptos/HM3133-dolor-toracico-pleuritico.yaml: 3f1683fbafaa904023e35502ef85c1178268756e609583348f81d467c6547726
    conceptos/HM3144-dimero-d-elevado.yaml: 562847ffb143450d77bfd4dc14af14cd221e5bd31c55bc6f3c386792364f4de2
    conceptos/HM3162-ventriculo-derecho-dilatado.yaml: bfbfab4ea78921d69f2891162121e678a9686759e3c10007725acb3228e09134
    conceptos/HM3163-taponamiento-cardiaco-en-ecografia.yaml: 8b19b30092dd4dd2ab9455f9084a4bcd322b5e3e1dbe77821ae96cfea200f621
    condiciones/HM6044-tromboembolia-pulmonar.yaml: 1e40d97372e03221c49c3cad5669fc8b8e3b544924b78966385f46feaa10aed5
    referencias/pmid-16403932.yaml: a1beeb62b2b79417da89d0d1c48e8c62313e13b7e7cc1f9669b44dde5c3cc789
    referencias/pmid-28495379.yaml: 94dd6cc6490001dc513f3e588d2b3b055644113f7874d72b9f9e244143affb93
    referencias/pmid-9786377.yaml: a744bdfe061bea39eeebdfeb75c36d78c863cb9fb6a8a848d121b42024f1665f
grounding:
  condicion_id: HM:6044
  condicion_nombre: Tromboembolia pulmonar
  concepto_id: HM:3162
  concepto_nombre: Ventrículo derecho dilatado en ecografía
  estado_lr: medido
  lr_positivo: 3.12
  lr_negativo: 0.57
  lr_positivo_rango: null
  lr_negativo_rango: null
  poblacion: pacientes con sospecha clínica de embolia pulmonar evaluados mediante ecocardiografía transtorácica a pie de cama; metaanálisis de estudios de exactitud diagnóstica (Fields 2017)
  referencia_id: pmid:28495379
  referencia_cita: 'Fields JM, Davis J, Girson L, Au A, Potts J, Morgan CJ, Vetter I, Riesenberg LA Transthoracic Echocardiography for Diagnosing Pulmonary Embolism: A Systematic Review and Meta-Analysis J Am Soc Echocardiogr 2017'
  pmid: '28495379'
  doi: 10.1016/j.echo.2017.03.004
  sensibilidad: 0.53
  especificidad: 0.83
triada:
  significante: Ventrículo derecho dilatado (su diámetro se acerca o supera al del ventrículo izquierdo), tabique interventricular aplanado o desplazado hacia el ventrículo izquierdo en sístole (signo de la D), TAPSE reducido y, en algunos casos, acinesia de la pared libre media del VD con el ápex conservado (signo de McConnell).
  significado: El ventrículo derecho, de pared delgada y diseñado para bajas presiones, se dilata y falla agudamente ante un aumento súbito de la resistencia vascular pulmonar —típicamente una tromboembolia pulmonar que obstruye una porción significativa del lecho vascular.
  decision: en el paciente inestable hemodinámicamente (shock o hipotensión arterial), el hallazgo inequívoco de sobrecarga del VD (relación VD/VI ≥ 1, aplanamiento septal o McConnell) apoya fuertemente la embolia pulmonar masiva y justifica considerar tratamiento de reperfusión de emergencia si la angio-TC es inviable
evidencia:
- concepto: HM:3162
  rol: imagen
  estado_lr: medido
  poblacion: pacientes con sospecha clínica de embolia pulmonar evaluados mediante ecocardiografía transtorácica a pie de cama; metaanálisis de estudios de exactitud diagnóstica (Fields 2017)
  ref: pmid:28495379
  sensibilidad: 0.53
  ic95_sensibilidad:
  - 0.45
  - 0.61
  especificidad: 0.83
  ic95_especificidad:
  - 0.74
  - 0.9
  lr_positivo: &id001
    valor: 3.12
    ic95:
    - 1.96
    - 4.97
    ref: pmid:28495379
  lr_negativo:
    valor: 0.57
    ic95:
    - 0.47
    - 0.68
    ref: pmid:28495379
  decision: en el paciente inestable hemodinámicamente (shock o hipotensión arterial), el hallazgo inequívoco de sobrecarga del VD (relación VD/VI ≥ 1, aplanamiento septal o McConnell) apoya fuertemente la embolia pulmonar masiva y justifica considerar tratamiento de reperfusión de emergencia si la angio-TC es inviable
  advertencia: sensibilidad limitada (53%, LR− 0.57); un ventrículo derecho de tamaño y función normales NO descarta TEP submasiva o de bajo riesgo hemodinámico
- concepto: HM:3144
  rol: prueba_sensible
  estado_lr: medido
  ref: pmid:16403932
  lr_negativo: &id002
    valor: 0.1
    ref: pmid:16403932
  poblacion: pacientes con sospecha de TEP y baja o intermedia probabilidad clínica pretest
  decision: un valor de dímero D por debajo del umbral de corte ajustado por edad descarta el diagnóstico sin necesidad de angiografía por tomografía
- concepto: HM:0401
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:0104
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:3133
  rol: manifestacion
  estado_lr: no_medido
- concepto: HM:0110
  rol: apoyo
  estado_lr: no_medido
autoevaluacion:
- id: q1
  pregunta: 'En Tromboembolia pulmonar, ¿cuál es el resultado documentado del LR positivo para «Ventrículo derecho dilatado en ecografía»? Población: pacientes con sospecha clínica de embolia pulmonar evaluados mediante ecocardiografía transtorácica a pie de cama; metaanálisis de estudios de exactitud diagnóstica (Fields 2017).'
  concepto_id: HM:3162
  referencia_id: pmid:28495379
  pmid: '28495379'
  doi: 10.1016/j.echo.2017.03.004
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6044
    concepto_id: HM:3162
    estado_lr: medido
    campo: lr_positivo
    dato: *id001
    poblacion: pacientes con sospecha clínica de embolia pulmonar evaluados mediante ecocardiografía transtorácica a pie de cama; metaanálisis de estudios de exactitud diagnóstica (Fields 2017)
    motivo: null
    decision: en el paciente inestable hemodinámicamente (shock o hipotensión arterial), el hallazgo inequívoco de sobrecarga del VD (relación VD/VI ≥ 1, aplanamiento septal o McConnell) apoya fuertemente la embolia pulmonar masiva y justifica considerar tratamiento de reperfusión de emergencia si la angio-TC es inviable
    advertencia: sensibilidad limitada (53%, LR− 0.57); un ventrículo derecho de tamaño y función normales NO descarta TEP submasiva o de bajo riesgo hemodinámico
  opciones:
  - texto: 'LR positivo: 3.12.'
    correcta: true
    feedback: 'LR positivo: 3.12. IC del 95 %: 1.96 a 4.97. Población: pacientes con sospecha clínica de embolia pulmonar evaluados mediante ecocardiografía transtorácica a pie de cama; metaanálisis de estudios de exactitud diagnóstica (Fields 2017). Interpretación registrada: en el paciente inestable hemodinámicamente (shock o hipotensión arterial), el hallazgo inequívoco de sobrecarga del VD (relación VD/VI ≥ 1, aplanamiento septal o McConnell) apoya fuertemente la embolia pulmonar masiva y justifica considerar tratamiento de reperfusión de emergencia si la angio-TC es inviable. Advertencia: sensibilidad limitada (53%, LR− 0.57); un ventrículo derecho de tamaño y función normales NO descarta TEP submasiva o de bajo riesgo hemodinámico.'
  - texto: El valor 3.12 corresponde al LR negativo y no al LR positivo.
    correcta: false
    feedback: 'Ese número corresponde al LR positivo, no al LR negativo. LR positivo: 3.12. IC del 95 %: 1.96 a 4.97. Población: pacientes con sospecha clínica de embolia pulmonar evaluados mediante ecocardiografía transtorácica a pie de cama; metaanálisis de estudios de exactitud diagnóstica (Fields 2017). Interpretación registrada: en el paciente inestable hemodinámicamente (shock o hipotensión arterial), el hallazgo inequívoco de sobrecarga del VD (relación VD/VI ≥ 1, aplanamiento septal o McConnell) apoya fuertemente la embolia pulmonar masiva y justifica considerar tratamiento de reperfusión de emergencia si la angio-TC es inviable. Advertencia: sensibilidad limitada (53%, LR− 0.57); un ventrículo derecho de tamaño y función normales NO descarta TEP submasiva o de bajo riesgo hemodinámico.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR positivo: 3.12. LR positivo: 3.12. IC del 95 %: 1.96 a 4.97. Población: pacientes con sospecha clínica de embolia pulmonar evaluados mediante ecocardiografía transtorácica a pie de cama; metaanálisis de estudios de exactitud diagnóstica (Fields 2017). Interpretación registrada: en el paciente inestable hemodinámicamente (shock o hipotensión arterial), el hallazgo inequívoco de sobrecarga del VD (relación VD/VI ≥ 1, aplanamiento septal o McConnell) apoya fuertemente la embolia pulmonar masiva y justifica considerar tratamiento de reperfusión de emergencia si la angio-TC es inviable. Advertencia: sensibilidad limitada (53%, LR− 0.57); un ventrículo derecho de tamaño y función normales NO descarta TEP submasiva o de bajo riesgo hemodinámico.'
- id: q2
  pregunta: 'En Tromboembolia pulmonar, ¿cuál es el resultado documentado del LR negativo para «Dímero D elevado»? Población: pacientes con sospecha de TEP y baja o intermedia probabilidad clínica pretest.'
  concepto_id: HM:3144
  referencia_id: pmid:16403932
  pmid: '16403932'
  doi: 10.1001/jama.295.2.199
  fuente_doi: 10.5281/zenodo.22064424
  evidencia:
    condicion_id: HM:6044
    concepto_id: HM:3144
    estado_lr: medido
    campo: lr_negativo
    dato: *id002
    poblacion: pacientes con sospecha de TEP y baja o intermedia probabilidad clínica pretest
    motivo: null
    decision: un valor de dímero D por debajo del umbral de corte ajustado por edad descarta el diagnóstico sin necesidad de angiografía por tomografía
    advertencia: null
  opciones:
  - texto: El valor 0.1 corresponde al LR positivo y no al LR negativo.
    correcta: false
    feedback: 'Ese número corresponde al LR negativo, no al LR positivo. LR negativo: 0.1. Población: pacientes con sospecha de TEP y baja o intermedia probabilidad clínica pretest. Interpretación registrada: un valor de dímero D por debajo del umbral de corte ajustado por edad descarta el diagnóstico sin necesidad de angiografía por tomografía.'
  - texto: La fuente no dispone de un cociente medido para este hallazgo.
    correcta: false
    feedback: 'Sí hay una medición documentada: LR negativo: 0.1. LR negativo: 0.1. Población: pacientes con sospecha de TEP y baja o intermedia probabilidad clínica pretest. Interpretación registrada: un valor de dímero D por debajo del umbral de corte ajustado por edad descarta el diagnóstico sin necesidad de angiografía por tomografía.'
  - texto: 'LR negativo: 0.1.'
    correcta: true
    feedback: 'LR negativo: 0.1. Población: pacientes con sospecha de TEP y baja o intermedia probabilidad clínica pretest. Interpretación registrada: un valor de dímero D por debajo del umbral de corte ajustado por edad descarta el diagnóstico sin necesidad de angiografía por tomografía.'
---

# Tromboembolia pulmonar

Hallazgos, cocientes documentados y límites de la evidencia.

## Nombre en inglés

Pulmonary embolism

## Sinónimos

embolia pulmonar

TEP

tromboembolismo pulmonar

## Códigos

Snomed: 59282003; Cie10: I26.9

## Factores de riesgo

trombosis venosa profunda previa o concomitante

inmovilización prolongada o reposo en cama

cirugía ortopédica o abdominopélvica reciente

neoplasia maligna activa

terapia con estrógenos o anticonceptivos orales

## Hallazgos clínicos

### Ventrículo derecho dilatado en ecografía (HM:3162)

**Significante:** Ventrículo derecho dilatado (su diámetro se acerca o supera al del ventrículo izquierdo), tabique interventricular aplanado o desplazado hacia el ventrículo izquierdo en sístole (signo de la D), TAPSE reducido y, en algunos casos, acinesia de la pared libre media del VD con el ápex conservado (signo de McConnell).

**Significado:** El ventrículo derecho, de pared delgada y diseñado para bajas presiones, se dilata y falla agudamente ante un aumento súbito de la resistencia vascular pulmonar —típicamente una tromboembolia pulmonar que obstruye una porción significativa del lecho vascular.

**Falsos positivos:** Cor pulmonale crónico (EPOC, hipertensión pulmonar crónica, cardiopatía congénita): dilata el VD de forma crónica; pared libre gruesa (>5 mm) y aurícula derecha mayor que la izquierda orientan a cronicidad, no a un evento agudo / Signo de McConnell descrito también en infarto del ventrículo derecho: no es exclusivo de tromboembolia pulmonar / Ventana subóptima o corte oblicuo del ápex que simula una relación VD:VI aumentada sin serlo / TAPSE reducido por disfunción del ventrículo izquierdo que arrastra secundariamente al derecho / Ausencia de todos estos hallazgos no descarta tromboembolia pulmonar submasiva o de bajo riesgo hemodinámico

**Rol:** Imagen

**Estado del LR:** LR medido

**Población:** pacientes con sospecha clínica de embolia pulmonar evaluados mediante ecocardiografía transtorácica a pie de cama; metaanálisis de estudios de exactitud diagnóstica (Fields 2017)

**Referencia:** pmid:28495379

**Sensibilidad:** 0.53

**Ic95 sensibilidad:** 0.45 / 0.61

**Especificidad:** 0.83

**Ic95 especificidad:** 0.74 / 0.9

**LR positivo:** Valor: 3.12; IC del 95 %: 1.96 / 4.97; Referencia: pmid:28495379

**LR negativo:** Valor: 0.57; IC del 95 %: 0.47 / 0.68; Referencia: pmid:28495379

**Decisión:** en el paciente inestable hemodinámicamente (shock o hipotensión arterial), el hallazgo inequívoco de sobrecarga del VD (relación VD/VI ≥ 1, aplanamiento septal o McConnell) apoya fuertemente la embolia pulmonar masiva y justifica considerar tratamiento de reperfusión de emergencia si la angio-TC es inviable

**Advertencia:** sensibilidad limitada (53%, LR− 0.57); un ventrículo derecho de tamaño y función normales NO descarta TEP submasiva o de bajo riesgo hemodinámico

### Dímero D elevado (HM:3144)

**Rol:** Prueba sensible

**Estado del LR:** LR medido

**Referencia:** pmid:16403932

**LR negativo:** Valor: 0.1; Referencia: pmid:16403932

**Población:** pacientes con sospecha de TEP y baja o intermedia probabilidad clínica pretest

**Decisión:** un valor de dímero D por debajo del umbral de corte ajustado por edad descarta el diagnóstico sin necesidad de angiografía por tomografía

### Disnea (HM:0401)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Taquicardia (HM:0104)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Dolor torácico pleurítico (HM:3133)

**Rol:** Manifestación

**Estado del LR:** LR no medido

### Hipoxemia (HM:0110)

**Rol:** Apoyo diagnóstico

**Estado del LR:** LR no medido

## Conclusión de la fuente

La ecocardiografía a pie de cama muestra especificidad útil y sensibilidad baja (53%) para la sospecha de TEP; su mayor utilidad reside en guiar el manejo inmediato del paciente en shock o con contraindicación para tomografía.

## Referencias y procedencia

**pmid:16403932:** Does this patient have deep vein thrombosis?. JAMA, 2006. DOI: 10.1001/jama.295.2.199.

**pmid:28495379:** Transthoracic Echocardiography for Diagnosing Pulmonary Embolism: A Systematic Review and Meta-Analysis. J Am Soc Echocardiogr, 2017. DOI: 10.1016/j.echo.2017.03.004.

**pmid:9786377:** The rational clinical examination. Is this patient having a myocardial infarction?. JAMA, 1998. DOI: 10.1001/jama.280.14.1256.

Fuente clínica: medsemiotics-db, condición HM:6044.
