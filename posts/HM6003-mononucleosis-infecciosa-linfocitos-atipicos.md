---
id: "HM6003-01"
slug: "mononucleosis-infecciosa-adenopatias-linfocitos-atipicos"
title: "Mononucleosis infecciosa en jóvenes: Precisión diagnóstica de las adenopatías y la linfocitosis atípica"
subtitle: "De la exploración de la cadena cervical posterior al frotis de sangre periférica según la evidencia de JAMA."
date: "2026-08-21"
author: "Dr. Alcy Torres"
category: "infectologia"
category_label: "Infectología y Medicina Interna"
tags: ["infecciosas", "mononucleosis", "hematologia", "pediatria", "semiologia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding:
  condicion_id: "HM:6003"
  condicion_nombre: "Mononucleosis infecciosa"
  concepto_id: "HM:3001"
  concepto_nombre: "Adenopatía cervical posterior"
  sensibilidad: 0.55
  especificidad: 0.87
  lr_positivo: 3.1
  lr_negativo: 0.52
  poblacion: "Adolescentes y adultos jóvenes de 16 a 20 años que consultan por odinofagia y fiebre"
  referencia_id: "pmid:27115266"
  referencia_cita: "Ebell MH, Call M, Shinholser J, Gardner J. Does This Patient Have Infectious Mononucleosis?: The Rational Clinical Examination Systematic Review. JAMA. 2016;315(14):1502-9."
  doi: "10.1001/jama.2016.4501"
  pmid: "27115266"

triada:
  significante: "Palpación de ganglios linfáticos aumentados de tamaño y moderadamente sensibles a lo largo del borde anterior del músculo trapecio (cadena cervical posterior) o axilares/inguinales, asociada a faringitis exudativa y esplenomegalia palpable."
  significado: "Proliferación policlonal masiva de linfocitos T citotóxicos CD8+ en respuesta a la infección primaria de linfocitos B por el Virus de Epstein-Barr (VEB)."
  decision: "La adenopatía cervical posterior orienta fuertemente (LR+ 3.1) frente a la faringitis estreptocócica común; la presencia de linfocitos atípicos ≥20% en el frotis periférico ofrece una confirmación casi definitiva (LR+ 54.0)."

autoevaluacion:
  - id: "q1"
    pregunta: "Un joven de 19 años consulta por fiebre de 8 días de evolución, malestar general intenso y dolor de garganta. En el examen físico se palpan adenopatías en la cadena cervical posterior y polo de bazo palpable bajo el reborde costal. ¿Cuál es el significado de estos hallazgos según la revisión sistemática de JAMA (PMID: 27115266)?"
    opciones:
      - texto: "La combinación de adenopatías cervicales posteriores (LR+ 3.1) y esplenomegalia (LR+ 6.6) eleva sustancialmente la probabilidad de mononucleosis infecciosa por encima del 70%."
        correcta: true
        feedback: "¡Correcto! En jóvenes con odinofagia, las adenopatías posteriores y la esplenomegalia son los signos físicos de mayor especificidad para mononucleosis infecciosa."
      - texto: "Descarta mononucleosis porque no presenta exantema maculopapular."
        correcta: false
        feedback: "Incorrecto. El exantema solo aparece espontáneamente en un 5% de los pacientes (o >80% si reciben amoxicilina por error)."
      - texto: "Confirma infección por estreptococo del grupo A sin necesidad de más estudios."
        correcta: false
        feedback: "Incorrecto. El estreptococo cursa típicamente con adenopatías submandibulares y cervicales anteriores, no posteriores ni esplenomegalia."

  - id: "q2"
    pregunta: "¿Qué parámetro de laboratorio básico en sangre periférica ofrece el mayor Likelihood Ratio positivo (LR+ > 50) para confirmar mononucleosis infecciosa en atención primaria?"
    opciones:
      - texto: "Linfocitosis con presencia de linfocitos atípicos o reactivos (células de Downey) ≥ 20% en el frotis sanguíneo."
        correcta: true
        feedback: "¡Exacto! Un recuento de linfocitos atípicos ≥ 20% tiene una especificidad cercana al 99% con un LR+ de 54.0, siendo prácticamente diagnóstico de infección aguda por VEB o CMV."
      - texto: "Trombocitosis reactiva aislada con neutrofilia del 90%."
        correcta: false
        feedback: "Incorrecto. La mononucleosis cursa con predominio linfocitario, no neutrofílico."
---

## El reto de la odinofagia en adolescentes y adultos jóvenes

Aproximadamente **1 de cada 13 pacientes entre 16 y 20 años** que consultan por dolor de garganta y fiebre tiene en realidad **Mononucleosis Infecciosa (MI)**, causada principalmente por el virus de Epstein-Barr (VEB).

El error habitual es tratar empíricamente con aminopenicilinas (amoxicilina), lo que desencadena con frecuencia un exantema medicamentoso aparatoso.

---

## Semiología Clave: Cadenas Ganglionares y Esplenomegalia

La revisión sistemática de la serie *The Rational Clinical Examination* (JAMA 2016) evaluó la capacidad discriminativa de cada hallazgo:

### Exploración Física:
- **Esplenomegalia palpable:** LR+ **6.6** (Esp. 98%, el hallazgo físico más potente).
- **Adenopatías cervicales posteriores:** LR+ **3.1** (Esp. 87%, distingue de faringitis bacteriana).
- **Adenopatías axilares o inguinales:** LR+ **3.0**.
- **Petequias en paladar:** LR+ **5.3**.

### Laboratorio Básico:
- **Linfocitos atípicos $\ge 20\%$:** LR+ **54.0** (Esp. 99%, confirmatorio).
- **Linfocitosis absoluta $> 4,000/\mu\text{L}$ o $\ge 50\%$ del recuento total:** LR+ **26.0**.

```
                   [ Joven (16-20 años) con Odinofagia y Fiebre ]
                                       │
                 ┌─────────────────────┴─────────────────────┐
                 ▼                                           ▼
       Adenopatías Cervicales                      Adenopatías Cervicales
       POSTERIORES o Esplenomegalia                 ANTERIORES Aisladas
                 │                                           │
      Alta Sospecha de Mononucleosis               Mayor Sospecha de Faringitis
      (LR+ = 3.1 a 6.6)                           Bacteriana o Viral Común
                 │                                           │
      Solicitar Hemograma (Linfocitos atípicos)    Aplicar Centor / Test Antígeno Rápido
      y Anticuerpos Heterófilos (Monospot)        (Evitar amoxicilina si hay duda)
```

---

## Evidencia Cuantitativa y Fuentes

Parámetros diagnósticos validados en la literatura médica (serie *The Rational Clinical Examination*, JAMA):

- **Prevalencia en jóvenes de 16 a 20 años:** ~0.077 (7.7%)
- **Cociente de Verosimilitud Positivo (Esplenomegalia):** 6.6 [Ebell et al., JAMA 2016]
- **Cociente de Verosimilitud Positivo (Adenopatía posterior):** 3.1 [Ebell et al., JAMA 2016]
- **Cociente de Verosimilitud Positivo (Linfocitos atípicos ≥20%):** 54.0 [Ebell et al., JAMA 2016]
- **Población evaluada:** Pacientes que consultan por odinofagia aguda en consultas ambulatorias y urgencias.

---

## Conclusión Semiótica

La exploración minuciosa de las **cadenas cervicales posteriores** y la palpación del hipocondrio izquierdo orientan rápidamente hacia etiología viral por VEB. El frotis periférico con linfocitos atípicos sella el diagnóstico y evita el uso innecesario de antibióticos.
