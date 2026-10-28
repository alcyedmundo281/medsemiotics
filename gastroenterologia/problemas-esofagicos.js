/* Complemento autónomo: guías directas autorizadas; no modifica el banco del blog. */
const diseases = {
  boerhaave: {
    name: 'Boerhaave',
    label: 'Pared · Perforación transmural',
    ref: 'wses',
    source: '[1]',
    mechanism:
      'Rotura espontánea de todo el espesor de la pared, frecuentemente tras vómitos intensos. Puede contaminar mediastino y pleura.',
    pattern:
      'Dolor torácico o epigástrico brusco tras el vómito; puede acompañarse de disnea o deterioro sistémico. La ausencia de enfisema subcutáneo no la descarta.',
    test: 'TC con contraste y TC-esofagografía ante sospecha de perforación, según estabilidad y recursos. Evaluación especializada urgente.',
    action:
      'Estabilización, ayuno, antibióticos y control de la fuga/contaminación por un equipo experto. El tratamiento puede ser quirúrgico, endoscópico o no operatorio en pacientes seleccionados con vigilancia estrecha.',
    pitfall:
      'Esperar una tríada clásica completa o tratar como una laceración superficial puede retrasar la atención.',
  },
  mallory: {
    name: 'Mallory-Weiss',
    label: 'Mucosa · Hemorragia',
    ref: 'mallory',
    source: '[2]',
    mechanism:
      'Desgarro longitudinal de la mucosa cerca de la unión esofagogástrica, asociado a incrementos bruscos de presión por vómitos o arcadas.',
    pattern:
      'Hematemesis después de arcadas orienta a esta lesión. El antecedente por sí solo no establece el origen del sangrado.',
    test: 'Endoscopia digestiva alta para identificar la lesión y valorar sangrado, tras evaluar y estabilizar al paciente.',
    action:
      'Muchos episodios cesan espontáneamente, pero el sangrado persistente o de alto riesgo requiere tratamiento. La guía recomienda hemostasia mecánica endoscópica en esos escenarios.',
    pitfall:
      'Llamarlo “benigno” sin valorar estabilidad, persistencia de la hemorragia y comorbilidades.',
  },
  acalasia: {
    name: 'Acalasia',
    label: 'Motilidad · Vaciamiento alterado',
    ref: 'acg',
    source: '[3]',
    mechanism:
      'Relajación inadecuada del esfínter esofágico inferior con pérdida de peristalsis normal.',
    pattern:
      'Disfagia para sólidos y líquidos, regurgitación y, a veces, pérdida de peso o dolor torácico.',
    test: 'Endoscopia para excluir una obstrucción o pseudoacalasia. La manometría de alta resolución confirma y clasifica; el esofagograma baritado es complementario.',
    action:
      'Reducir la resistencia de la unión esofagogástrica mediante dilatación neumática, miotomía de Heller o POEM, según subtipo, paciente y experiencia del centro. La toxina botulínica se reserva especialmente para quienes no son candidatos a tratamientos definitivos.',
    pitfall:
      'Asumir que un “pico de pájaro” basta para excluir una causa tumoral.',
  },
};

const questions = [
  {
    text: '¿Qué diferencia anatómica separa Boerhaave de Mallory-Weiss?',
    options: [
      'Boerhaave afecta todo el espesor; Mallory-Weiss, la mucosa.',
      'Ambos son trastornos exclusivos de la motilidad.',
      'Mallory-Weiss siempre perfora la pared.',
    ],
    correct: 0,
    reason:
      'La profundidad de la lesión explica el riesgo de fuga en Boerhaave. Un antecedente compartido, como el vómito, no los vuelve equivalentes.',
    ref: 'wses',
    source: '[1]',
  },
  {
    text: 'Ante sospecha de perforación esofágica, ¿qué estudio busca la fuga y su extensión?',
    options: [
      'Manometría ambulatoria como primer paso.',
      'TC con contraste / TC-esofagografía, con evaluación urgente.',
      'Esperar a que aparezca enfisema subcutáneo.',
    ],
    correct: 1,
    reason:
      'La imagen y la valoración especializada no deben esperar la aparición de todos los signos clásicos. La prioridad incluye estabilizar al paciente.',
    ref: 'wses',
    source: '[1]',
  },
  {
    text: '¿Qué afirmación es adecuada sobre Mallory-Weiss?',
    options: [
      'Nunca necesita tratamiento endoscópico.',
      'El antecedente de arcadas excluye otras causas de hemorragia.',
      'El sangrado persistente o de alto riesgo puede requerir hemostasia endoscópica.',
    ],
    correct: 2,
    reason:
      'Que muchos sangrados se detengan espontáneamente no elimina el riesgo individual. Hay que evaluar la hemorragia y tratarla según sus características.',
    ref: 'mallory',
    source: '[2]',
  },
  {
    text: '¿Qué prueba confirma y clasifica la acalasia?',
    options: [
      'La respuesta a un antiácido.',
      'La manometría de alta resolución.',
      'Una radiografía simple normal.',
    ],
    correct: 1,
    reason:
      'La manometría caracteriza la alteración motora; la endoscopia y el esofagograma aportan información complementaria. Antes debe excluirse una obstrucción mecánica.',
    ref: 'acg',
    source: '[3]',
  },
  {
    text: '¿Qué hacer si una posible acalasia se acompaña de pérdida de peso rápida en una persona mayor?',
    options: [
      'Investigar pseudoacalasia y causas obstructivas.',
      'Dar por confirmado un trastorno motor primario.',
      'Descartar enfermedad tumoral solo por el patrón de disfagia.',
    ],
    correct: 0,
    reason:
      'Una causa mecánica puede imitar la acalasia. La endoscopia y los estudios adicionales indicados por la sospecha ayudan a evitar ese error.',
    ref: 'acg',
    source: '[3]',
  },
  {
    text: '¿Qué se necesita para diagnosticar esofagitis eosinofílica?',
    options: [
      'Solo una historia de alergia.',
      'Una manometría aislada.',
      'Síntomas de disfunción esofágica, biopsias compatibles y evaluación de otras causas.',
    ],
    correct: 2,
    reason:
      'Es un diagnóstico clinicopatológico. Los síntomas y la impresión endoscópica por sí solos no sustituyen el estudio histológico.',
    ref: 'eoe',
    source: '[5]',
  },
];

const detail = document.getElementById('disease-detail');
const selectors = document.querySelectorAll('[data-disease]');
function showDisease(key) {
  const item = diseases[key];
  selectors.forEach((button) =>
    button.setAttribute('aria-pressed', String(button.dataset.disease === key)),
  );
  // Solo se insertan constantes editoriales locales; no se usa entrada del alumno como HTML.
  detail.innerHTML = `<p class="eyebrow">${item.label}</p><h3>${item.name}</h3><div class="detail-grid">${[
    ['Qué ocurre', item.mechanism],
    ['Qué orienta', item.pattern],
    ['Qué prueba responde', item.test],
    ['Qué cambia la conducta', item.action],
  ]
    .map(([title, body]) => `<div><h4>${title}</h4><p>${body}</p></div>`)
    .join(
      '',
    )}</div><p class="pitfall"><strong>Error que evitar:</strong> ${item.pitfall}</p><a href="#ref-${item.ref}">Guía de referencia ${item.source} →</a>`;
}
selectors.forEach((button) =>
  button.addEventListener('click', () => showDisease(button.dataset.disease)),
);
showDisease('boerhaave');

const form = document.getElementById('quiz');
const result = document.getElementById('quiz-result');
document.getElementById('questions').innerHTML = questions
  .map(
    (question, index) => `
  <fieldset><legend>${index + 1}. ${question.text}</legend>${question.options
    .map(
      (option, optionIndex) => `
    <label class="answer"><input type="radio" name="q${index}" value="${optionIndex}" required /><span>${option}</span></label>`,
    )
    .join('')}
    <div class="feedback" id="feedback-${index}" hidden></div></fieldset>`,
  )
  .join('');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  let score = 0;
  const answers = new FormData(form);
  questions.forEach((question, index) => {
    const correct = Number(answers.get(`q${index}`)) === question.correct;
    if (correct) score += 1;
    const feedback = document.getElementById(`feedback-${index}`);
    feedback.hidden = false;
    feedback.classList.toggle('incorrect', !correct);
    feedback.innerHTML = `<strong>${correct ? 'Correcto.' : 'Revisa esta decisión.'}</strong> Respuesta: ${question.options[question.correct]} ${question.reason} <a href="#ref-${question.ref}">${question.source}</a>`;
  });
  result.textContent = `${score} de ${questions.length} respuestas correctas. Revisa el razonamiento de cada pregunta y vuelve a intentarlo si lo necesitas.`;
  result.focus();
});
form.addEventListener('change', () => {
  // Una selección nueva invalida la corrección anterior: nunca mostrar una nota obsoleta.
  result.textContent = '';
  document.querySelectorAll('.feedback').forEach((element) => {
    element.hidden = true;
  });
});
form.addEventListener('reset', () => {
  result.textContent = '';
  document.querySelectorAll('.feedback').forEach((element) => {
    element.hidden = true;
  });
});
document
  .getElementById('print')
  .addEventListener('click', () => window.print());

// El repaso impreso incluye las rutas y la tabla aunque estén plegadas en pantalla.
let previouslyOpen = [];
window.addEventListener('beforeprint', () => {
  previouslyOpen = [...document.querySelectorAll('details')].filter(
    (element) => element.open,
  );
  document.querySelectorAll('details').forEach((element) => {
    element.open = true;
  });
});
window.addEventListener('afterprint', () => {
  document.querySelectorAll('details').forEach((element) => {
    element.open = previouslyOpen.includes(element);
  });
});
