---
id: "HM6010-01"
slug: "sincope-cardiaco-vs-vasovagal-anamnesis"
title: "Síncope en urgencias: Cómo diferenciar el origen arrítmico del síncope vasovagal"
subtitle: "Análisis bayesiano de los pródromos neurovegetativos y la cianosis según la serie Rational Clinical Examination."
date: "2026-08-21"
author: "Dr. Alcy Torres"
category: "cardiologia"
category_label: "Cardiología y Urgencias"
tags: ["cardiologia", "urgencias", "sincope", "arritmias", "semiologia"]
reading_time: "6 min"
difficulty: "Intermedio"
grounding:
  condicion_id: "HM:6010"
  condicion_nombre: "Síncope cardíaco"
  concepto_id: "HM:3032"
  concepto_nombre: "Antecedente de fibrilación o flutter auricular"
  sensibilidad: 0.13
  especificidad: 0.98
  lr_positivo: 7.3
  lr_negativo: 0.89
  poblacion: "Adultos evaluados en urgencias tras un episodio de pérdida transitoria de conciencia"
  referencia_id: "pmid:31237649"
  referencia_cita: "Albassam OT, Redelmeier RJ, Shadowitz S, Husain AM, Simel D, Etchells EE. Did This Patient Have Cardiac Syncope?: The Rational Clinical Examination Systematic Review. JAMA. 2019;321(24):2448-57."
  doi: "10.1001/jama.2019.8001"
  pmid: "31237649"

triada:
  significante: "Pérdida transitoria de la conciencia de instauración súbita sin pródromos autonómicos, o precedida inmediatamente por palpitaciones rápidas, con presencia de cardiopatía estructural o FA conocida."
  significado: "Caída crítica y brusca del gasto cardíaco y del flujo sanguíneo cerebral secundario a taquiarritmia, bradiarritmia o cardiopatía estructural."
  decision: "La presencia de palpitaciones previas (LR+ 2.7) o antecedente de FA (LR+ 7.3) aumenta marcadamente la probabilidad cardíaca y exige monitorización; en contraste, pródromos autonómicos de calor/frío/diaforesis disminuyen drásticamente el riesgo cardíaco (LR+ 0.16) apuntando a síncope reflejo."

autoevaluacion:
  - id: "q1"
    pregunta: "Un paciente de 72 años sufre una caída al suelo con pérdida de conciencia mientras estaba sentado viendo televisión. No hubo mareo previo, náuseas ni sudoración. Tiene antecedentes de fibrilación auricular. Según la revisión sistemática de JAMA (PMID: 31237649), ¿qué valor tiene el antecedente de FA?"
    opciones:
      - texto: "Presenta una especificidad del 98% con un LR+ de 7.3, elevando sustancialmente la sospecha de síncope arrítmico o de origen cardíaco."
        correcta: true
        feedback: "¡Correcto! Albassam et al. demuestran que el antecedente de cardiopatía o arritmia auricular previa es el factor anamnésico que más desplaza hacia etiología cardíaca (LR+ 7.3)."
      - texto: "Indica un síncope vasovagal benigno sin necesidad de telemetría."
        correcta: false
        feedback: "Incorrecto. La ausencia de pródromos autonómicos y el antecedente de arritmia obligan a descartar síncope cardíaco de alto riesgo."
      - texto: "Descarta cualquier causa arrítmica."
        correcta: false
        feedback: "Incorrecto. Todo lo contrario, es el principal predictor positivo."

  - id: "q2"
    pregunta: "¿Por qué en la semiología del síncope un hallazgo como 'sensación prodrómica de calor, náuseas o sudoración fría' tiene un LR de 0.16 para síncope cardíaco?"
    opciones:
      - texto: "Porque su presencia argumenta fuertemente EN CONTRA del origen cardíaco, siendo un potente indicador de activación parasimpática y síncope reflejo (vasovagal)."
        correcta: true
        feedback: "¡Exacto! Un LR < 1 significa que la presencia del síntoma aleja la enfermedad analizada (reduce la probabilidad de síncope cardíaco en ~85%)."
      - texto: "Porque es un error estadístico del metaanálisis."
        correcta: false
        feedback: "Incorrecto. En razonamiento bayesiano, los síntomas protectores o típicos de patología benigna tienen LR < 1."
---

## El desafío del síncope en la práctica médica

El síncope representa entre el 1% y el 3% de todas las consultas en urgencias. La prioridad clínica consiste en responder una sola pregunta crítica: **¿es un síncope de origen cardíaco (asociado a muerte súbita) o es un síncope vasovagal/reflejo (benigno)?**

---

## La paradoja bayesiana: Hallazgos que descartan al estar presentes

La revisión sistemática de 11 estudios y 4,317 pacientes publicada en *JAMA* (2019) reveló datos semiológicos esenciales:

### Factores que AUMENTAN la probabilidad cardíaca:
- **Antecedente de fibrilación o flutter auricular:** LR+ **7.3** (Esp. 98%).
- **Cianosis presenciada durante el episodio:** LR+ **6.2** (Esp. 99%).
- **Palpitaciones inmediatamente previas:** LR+ **2.7**.
- **Síncope durante el esfuerzo físico:** Alarma roja cardiovascular.

### Factores que DISMINUYEN la probabilidad cardíaca (Apuntan a Vasovagal):
- **Pródromos autonómicos (sensación de calor, frío, diaforesis, náusea):** LR+ **0.16**.
- **Bipedestación prolongada o ambiente caluroso:** LR+ **0.38**.

```
                   [ Pérdida Transitoria de Conciencia ]
                                    │
                ┌───────────────────┴───────────────────┐
                ▼                                       ▼
     Súbito / Sin Pródromo                 Pródromo Autonómico Florido
    (Palpitaciones, FA, Esfuerzo)          (Diaforesis, calor, náusea previa)
                │                                       │
     Alta Sospecha Cardíaca                  Baja Probabilidad Cardíaca
     (LR+ = 7.3 con FA)                     (LR+ = 0.16 para causa cardíaca)
     Requiere ECG, Telemetría,               Orientar hacia síncope vasovagal /
     Troponina y Ecocardiograma.             ortostático benigno.
```

---

## Evidencia Cuantitativa y Fuentes

Parámetros diagnósticos validados en la literatura médica (serie *The Rational Clinical Examination*, JAMA):

- **Cociente de Verosimilitud Positivo (FA previa):** 7.30 [Albassam et al., JAMA 2019]
- **Especificidad de FA previa para síncope cardíaco:** 0.98 (98%)
- **Cociente de Verosimilitud de Pródromos Autonómicos:** 0.16 [Albassam et al., JAMA 2019]
- **Población evaluada:** 4,317 pacientes adultos atendidos en urgencias por síncope.

---

## Conclusión Semiótica

En el síncope, la **anamnesis meticulosa** es el mejor estratificador de riesgo. La ausencia de aviso prodrómico es una bandera roja, mientras que la sudoración y el mareo progresivo tranquilizan hacia etiología refleja.
