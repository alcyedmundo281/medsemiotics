// Fuente del módulo interactivo de trastornos-estomacales.html.
// Se compila con `npm run build:js` a trastornos-estomacales.bundle.js; la página carga
// el bundle, no este archivo. React y ReactDOM llegan como globales UMD.

// Alias React to react for Lucide UMD compatibility
window.react = React;

const { useState, useEffect } = React;
const {
    BookOpen, Activity, Search, AlertCircle, Play,
    CheckCircle, XCircle, ChevronRight, ChevronDown,
    Pill, Stethoscope, Sandwich
} = LucideReact;

// --- Components ---

const Navigation = ({ activeTab, setActiveTab }) => {
    const tabs = [
        { id: 'learn', label: 'Notas de Estudio', icon: BookOpen },
        { id: 'microscope', label: 'Laboratorio de Microscopio', icon: Search },
        { id: 'simulator', label: 'Simulador de Dolor', icon: Activity },
        { id: 'clinic', label: 'La Clínica', icon: Stethoscope },
    ];

    return (
        <nav className="bg-slate-900 text-white p-4 shadow-lg sticky top-[73px] z-40">
            <div className="max-w-6xl mx-auto flex flex-wrap justify-between items-center">
                <div className="flex items-center space-x-2 mb-2 md:mb-0">
                    <div className="bg-red-500 p-2 rounded-lg">
                        <Activity size={24} className="text-white" />
                    </div>
                    <span className="text-xl font-bold tracking-tight">GastroMaster <span className="text-red-400 text-sm font-normal">Trastornos Estomacales</span></span>
                </div>
                <div className="flex space-x-1 md:space-x-4 overflow-x-auto">
                    {tabs.map((tab) => (
                        <button
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id)}
                            className={`flex items-center space-x-2 px-4 py-2 rounded-full transition-all text-sm md:text-base whitespace-nowrap ${activeTab === tab.id
                                ? 'bg-red-600 text-white shadow-md'
                                : 'hover:bg-slate-800 text-slate-300'
                                }`}
                        >
                            <tab.icon size={16} />
                            <span>{tab.label}</span>
                        </button>
                    ))}
                </div>
            </div>
        </nav>
    );
};

const StudyNotes = () => {
    const [openSection, setOpenSection] = useState('gastritis');

    const sections = [
        {
            id: 'gastritis',
            title: 'Gastritis vs. Enfermedad de Úlcera Péptica (EUP)',
            content: (
                <div className="space-y-4">
                    <p className="text-slate-600 dark:text-slate-400">La gastritis y la EUP comparten una fisiopatología similar pero difieren en profundidad y gravedad.</p>
                    <div className="grid md:grid-cols-2 gap-4">
                        <div className="bg-orange-50 dark:bg-orange-900/10 p-4 rounded-lg border border-orange-100 dark:border-orange-900/20">
                            <h4 className="font-bold text-orange-800 dark:text-orange-400 mb-2">Gastritis</h4>
                            <ul className="list-disc list-inside text-sm space-y-1 text-slate-700 dark:text-slate-300">
                                <li><strong>Ubicación:</strong> Comúnmente en el Antro.</li>
                                <li><strong>Inflamación:</strong> Inflamación mucosa generalizada.</li>
                                <li><strong>Profundidad:</strong> Erosiones superficiales. <span className="text-red-600 font-semibold">NUNCA</span> atraviesa la muscularis mucosae.</li>
                                <li><strong>Microscópico:</strong> Capa de moco delgada, erosiones superficiales.</li>
                                <li><strong>Dolor:</strong> Epigástrico. Sin relación específica con los alimentos.</li>
                            </ul>
                        </div>
                        <div className="bg-red-50 dark:bg-red-900/10 p-4 rounded-lg border border-red-100 dark:border-red-900/20">
                            <h4 className="font-bold text-red-800 dark:text-red-400 mb-2">Enfermedad de Úlcera Péptica (EUP)</h4>
                            <ul className="list-disc list-inside text-sm space-y-1 text-slate-700 dark:text-slate-300">
                                <li><strong>Ubicación:</strong> Duodeno (más común) o Estómago (Antro).</li>
                                <li><strong>Profundidad:</strong> Úlceras profundas. Se extiende a la <span className="text-red-600 font-semibold">Submucosa</span> y más allá.</li>
                                <li><strong>Dolor:</strong> Epigástrico. <span className="font-bold">Relación específica con los alimentos.</span></li>
                                <li><strong>Riesgo:</strong> Alto riesgo de sangrado y perforación.</li>
                            </ul>
                        </div>
                    </div>
                </div>
            )
        },
        {
            id: 'etiology',
            title: 'Etiología y Fisiopatología',
            content: (
                <div className="space-y-4">
                    <h4 className="font-bold text-slate-800 dark:text-slate-200">Las "4 Causas Principales":</h4>
                    <ul className="space-y-3">
                        <li className="flex items-start">
                            <span className="bg-blue-100 dark:bg-blue-900/30 text-blue-800 dark:text-blue-400 px-2 py-1 rounded text-xs font-bold mr-2 mt-1">AINEs y Alcohol</span>
                            <span className="text-sm text-slate-700 dark:text-slate-300">Inhiben la enzima COX → Disminución de Prostaglandinas → Aumento de HCl y Disminución del Moco Protector.</span>
                        </li>
                        <li className="flex items-start">
                            <span className="bg-purple-100 dark:bg-purple-900/30 text-purple-800 dark:text-purple-400 px-2 py-1 rounded text-xs font-bold mr-2 mt-1">H. Pylori</span>
                            <div className="text-sm text-slate-700 dark:text-slate-300">
                                <p>1. Aumenta la Gastrina → Aumenta el HCl.</p>
                                <p>2. <strong>Enzima Ureasa:</strong> Convierte la Urea → Amoníaco (alcalino) → Permite la supervivencia bacteriana y citotoxicidad.</p>
                            </div>
                        </li>
                        <li className="flex items-start">
                            <span className="bg-yellow-100 dark:bg-yellow-900/30 text-yellow-800 dark:text-yellow-400 px-2 py-1 rounded text-xs font-bold mr-2 mt-1">Úlceras por Estrés</span>
                            <div className="text-sm text-slate-700 dark:text-slate-300">
                                <p><strong>Curling (Quemaduras):</strong> Hipovolemia → Isquemia Mucosa.</p>
                                <p><strong>Cushing (Cerebro):</strong> PIC Alta → Estimulación Vagal → Liberación de Ach → HCl Alto.</p>
                            </div>
                        </li>
                        <li className="flex items-start">
                            <span className="bg-green-100 dark:bg-green-900/30 text-green-800 dark:text-green-400 px-2 py-1 rounded text-xs font-bold mr-2 mt-1">Gastrinoma</span>
                            <span className="text-sm text-slate-700 dark:text-slate-300">Síndrome de Zollinger-Ellison. El tumor secreta gastrina masiva. Piense en: Úlceras refractarias.</span>
                        </li>
                    </ul>
                </div>
            )
        },
        {
            id: 'complications',
            title: 'Complicaciones y Emergencias',
            content: (
                <div className="grid md:grid-cols-3 gap-4 text-sm">
                    <div className="p-3 bg-slate-100 dark:bg-slate-800 rounded border border-slate-200 dark:border-slate-700">
                        <h5 className="font-bold mb-2">Sangrado GI</h5>
                        <p>Erosión en las arterias (Curvatura Menor/Mayor).</p>
                        <p className="mt-2 text-red-600 font-semibold">Signos: Hematemesis, Melena.</p>
                    </div>
                    <div className="p-3 bg-slate-100 dark:bg-slate-800 rounded border border-slate-200 dark:border-slate-700">
                        <h5 className="font-bold mb-2">Perforación</h5>
                        <p>Erosión a través de la Serosa. El contenido se filtra al peritoneo.</p>
                        <p className="mt-2 text-red-600 font-semibold">Signos: Neumoperitoneo (Aire bajo el diafragma), Abdomen en tabla.</p>
                    </div>
                    <div className="p-3 bg-slate-100 dark:bg-slate-800 rounded border border-slate-200 dark:border-slate-700">
                        <h5 className="font-bold mb-2">Obstrucción de la Salida Gástrica</h5>
                        <p>El edema/fibrosis bloquea el píloro.</p>
                        <p className="mt-2 text-red-600 font-semibold">Signos: Chapoteo de sucusión, Vómito en proyectil.</p>
                    </div>
                </div>
            )
        }
    ];

    return (
        <div className="max-w-4xl mx-auto p-6 fade-in">
            <h2 className="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-6 font-lexend">Notas de Clase</h2>
            <div className="space-y-4">
                {sections.map((section) => (
                    <div key={section.id} className="border border-slate-200 dark:border-slate-700 rounded-lg overflow-hidden shadow-sm bg-white dark:bg-surface-dark">
                        <button
                            onClick={() => setOpenSection(openSection === section.id ? null : section.id)}
                            className="w-full flex justify-between items-center p-4 bg-slate-50 dark:bg-slate-800/50 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors"
                        >
                            <span className="font-semibold text-slate-700 dark:text-slate-200">{section.title}</span>
                            {openSection === section.id ? <ChevronDown size={20} /> : <ChevronRight size={20} />}
                        </button>
                        {openSection === section.id && (
                            <div className="p-6 border-t border-slate-100 dark:border-slate-700 bg-white dark:bg-surface-dark animate-fadeIn">
                                {section.content}
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
};

const MicroscopeLab = () => {
    const [zoomLevel, setZoomLevel] = useState('sano');

    return (
        <div className="max-w-4xl mx-auto p-6 fade-in">
            <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-bold text-slate-800 dark:text-slate-200 font-lexend">Laboratorio de Histología</h2>
                <div className="flex space-x-2 bg-slate-100 dark:bg-slate-800 p-1 rounded-lg">
                    {['sano', 'gastritis', 'úlcera'].map((mode) => (
                        <button
                            key={mode}
                            onClick={() => setZoomLevel(mode)}
                            className={`px-4 py-2 rounded-md text-sm font-medium transition-all ${zoomLevel === mode ? 'bg-white dark:bg-surface-dark text-blue-600 dark:text-blue-400 shadow' : 'text-slate-500 hover:text-slate-700 dark:text-slate-400'
                                }`}
                        >
                            {mode.charAt(0).toUpperCase() + mode.slice(1)}
                        </button>
                    ))}
                </div>
            </div>

            <div className="bg-white dark:bg-surface-dark p-8 rounded-xl shadow-lg border border-slate-200 dark:border-slate-700 relative overflow-hidden h-96">
                <div className="flex flex-col h-full relative">
                    <div className="absolute top-4 right-4 bg-black/70 text-white text-xs p-2 rounded z-10">
                        Vista Actual: <span className="font-bold text-yellow-300">{zoomLevel.toUpperCase()}</span>
                    </div>

                    <div className="flex-1 bg-pink-300 relative border-b-2 border-pink-400 flex items-center justify-center transition-all duration-500">
                        <span className="absolute right-2 bottom-2 text-pink-700 text-xs font-bold opacity-50">Mucosa</span>

                        <div
                            className={`absolute top-0 w-32 h-16 bg-red-500/80 rounded-b-full blur-sm transition-all duration-700 ${zoomLevel === 'sano' ? 'opacity-0 -translate-y-full' : 'opacity-100 translate-y-0'
                                }`}
                        ></div>

                        <div
                            className={`absolute top-0 w-48 bg-red-800 shadow-inner rounded-b-full transition-all duration-700 ${zoomLevel === 'úlcera' ? 'h-full translate-y-0 opacity-100' : 'h-0 opacity-0'
                                }`}
                        ></div>

                        <div className={`absolute top-0 left-0 right-0 bg-blue-200/50 backdrop-blur-sm transition-all duration-500 ${zoomLevel === 'sano' ? 'h-8' : 'h-2'
                            }`}>
                            <span className="absolute left-2 top-1 text-blue-800 text-[10px] font-bold">
                                {zoomLevel === 'sano' ? 'Capa Gruesa de Moco Alcalino' : 'Capa Delgada de Moco'}
                            </span>
                        </div>
                    </div>

                    <div className="h-24 bg-blue-100 relative border-b-2 border-blue-200 flex items-center justify-center transition-all">
                        <span className="absolute right-2 bottom-2 text-blue-400 text-xs font-bold opacity-50">Submucosa</span>
                        <div className="w-full h-2 bg-red-400/30 absolute top-1/2 transform -translate-y-1/2"></div>

                        <div
                            className={`absolute top-0 w-40 bg-red-800 shadow-inner rounded-b-full transition-all duration-700 z-10 ${zoomLevel === 'úlcera' ? 'h-16 opacity-100' : 'h-0 opacity-0'
                                }`}
                        ></div>
                    </div>

                    <div className="h-32 bg-red-400 relative flex items-center justify-center border-b-2 border-red-500">
                        <span className="absolute right-2 bottom-2 text-red-900 text-xs font-bold opacity-50">Muscularis Externa</span>
                        <div className="w-full h-full bg-[url('./images/texture-diagmonds-light.svg')] opacity-10"></div>
                    </div>

                    <div className="h-4 bg-yellow-100">
                        <span className="absolute right-2 top-0 text-yellow-600 text-[10px] font-bold opacity-50">Serosa</span>
                    </div>
                </div>
            </div>

            <div className="mt-6 bg-blue-50 dark:bg-blue-900/10 p-4 rounded-lg border border-blue-100 dark:border-blue-900/20">
                <h3 className="font-bold text-blue-800 dark:text-blue-400 flex items-center"><AlertCircle size={18} className="mr-2" /> Clave Diagnóstica</h3>
                <p className="text-sm text-blue-900 dark:text-blue-300 mt-1">
                    {zoomLevel === 'sano' && "El revestimiento normal del estómago consiste en una barrera gruesa de moco que protege el epitelio."}
                    {zoomLevel === 'gastritis' && "La gastritis implica inflamación y erosiones superficiales. Tenga en cuenta que la erosión NO atraviesa la muscularis mucosae (la parte inferior de la capa rosa)."}
                    {zoomLevel === 'úlcera' && "La enfermedad de úlcera péptica implica una excavación profunda. La lesión penetra a través de la mucosa y llega a la submucosa (capa azul) o más profundamente."}
                </p>
            </div>
        </div>
    );
};

const PainSimulator = () => {
    const [diagnosis, setDiagnosis] = useState(null);
    const [feedback, setFeedback] = useState(null);

    const handleDiagnose = (type) => {
        if (type === 'gastric') {
            setFeedback({ correct: true, text: "¡Correcto! Las úlceras gástricas causan dolor MIENTRAS se come (el ácido aumenta inmediatamente)." });
        } else {
            setFeedback({ correct: false, text: "Incorrecto. Mire la curva de nuevo. ¿El dolor SUBE o BAJA cuando entra la comida?" });
        }
    };

    const handleDiagnoseDuodenal = (type) => {
        if (type === 'duodenal') {
            setFeedback({ correct: true, text: "¡Correcto! Las úlceras duodenales se sienten MEJOR con la comida (el esfínter pilórico se cierra, el ácido se queda en el estómago), pero duelen más tarde." });
        } else {
            setFeedback({ correct: false, text: "Incorrecto. El dolor DISMINUYÓ cuando comieron. ¿Qué tipo hace eso?" });
        }
    }

    return (
        <div className="max-w-4xl mx-auto p-6 fade-in">
            <h2 className="text-2xl font-bold text-slate-800 dark:text-slate-200 mb-2 font-lexend">Simulador de Patrones de Dolor</h2>
            <p className="text-slate-600 dark:text-slate-400 mb-6">Diferencie la úlcera basándose en la relación "Comida vs. Dolor".</p>

            <div className="grid md:grid-cols-2 gap-8">
                <div className="bg-white dark:bg-surface-dark p-6 rounded-xl shadow-md border border-slate-200 dark:border-slate-700">
                    <h3 className="font-bold text-lg mb-4 text-slate-700 dark:text-slate-200">Paciente A</h3>
                    <div className="h-40 bg-slate-50 dark:bg-slate-800/50 border border-slate-200 dark:border-slate-700 rounded-lg relative flex items-end justify-between px-4 pb-2 mb-4 overflow-hidden">
                        <svg className="absolute inset-0 w-full h-full" preserveAspectRatio="none">
                            <path d="M0,100 C50,100 100,20 150,20 L300,20" stroke="red" strokeWidth="3" fill="none" strokeDasharray="5,5" />
                            <text x="10" y="90" fontSize="12" fill="gray">Nivel Dolor</text>
                        </svg>
                        <div className="absolute inset-0 flex items-center justify-center">
                            <span className="bg-white/80 dark:bg-black/60 p-2 rounded text-red-600 font-bold animate-pulse">El Dolor Aumenta c/ la Comida</span>
                        </div>
                    </div>
                    <div className="flex space-x-2">
                        <button onClick={() => handleDiagnose('gastric')} className="flex-1 bg-slate-800 dark:bg-slate-700 text-white py-2 rounded hover:bg-slate-700 text-sm">Úlcera Gástrica</button>
                        <button onClick={() => handleDiagnose('duodenal')} className="flex-1 bg-slate-800 dark:bg-slate-700 text-white py-2 rounded hover:bg-slate-700 text-sm">Úlcera Duodenal</button>
                    </div>
                </div>

                <div className="bg-white dark:bg-surface-dark p-6 rounded-xl shadow-md border border-slate-200 dark:border-slate-700">
                    <h3 className="font-bold text-lg mb-4 text-slate-700 dark:text-slate-200">Paciente B</h3>
                    <div className="h-40 bg-slate-50 dark:bg-slate-800/50 border border-slate-200 dark:border-slate-700 rounded-lg relative flex items-end justify-between px-4 pb-2 mb-4 overflow-hidden">
                        <svg className="absolute inset-0 w-full h-full" preserveAspectRatio="none">
                            <path d="M0,20 C50,20 100,120 150,120 C200,120 250,50 300,20" stroke="blue" strokeWidth="3" fill="none" strokeDasharray="5,5" />
                            <text x="10" y="30" fontSize="12" fill="gray">Nivel Dolor</text>
                        </svg>
                        <div className="absolute inset-0 flex items-center justify-center">
                            <span className="bg-white/80 dark:bg-black/60 p-2 rounded text-blue-600 font-bold animate-pulse">El Dolor Disminuye c/ la Comida</span>
                        </div>
                    </div>
                    <div className="flex space-x-2">
                        <button onClick={() => handleDiagnoseDuodenal('gastric')} className="flex-1 bg-slate-800 dark:bg-slate-700 text-white py-2 rounded hover:bg-slate-700 text-sm">Úlcera Gástrica</button>
                        <button onClick={() => handleDiagnoseDuodenal('duodenal')} className="flex-1 bg-slate-800 dark:bg-slate-700 text-white py-2 rounded hover:bg-slate-700 text-sm">Úlcera Duodenal</button>
                    </div>
                </div>
            </div>

            {feedback && (
                <div className={`mt-6 p-4 rounded-lg flex items-start ${feedback.correct ? 'bg-green-100 dark:bg-green-900/20 text-green-800 dark:text-green-400' : 'bg-red-100 dark:bg-red-900/20 text-red-800 dark:text-red-400'}`}>
                    {feedback.correct ? <CheckCircle className="mr-2 flex-shrink-0" /> : <XCircle className="mr-2 flex-shrink-0" />}
                    <div>
                        <p className="font-bold">{feedback.correct ? '¡Correcto!' : 'Inténtelo de nuevo'}</p>
                        <p>{feedback.text}</p>
                    </div>
                </div>
            )}

            <div className="mt-8 bg-yellow-50 dark:bg-yellow-900/10 p-4 rounded border-l-4 border-yellow-400">
                <h4 className="font-bold text-yellow-800 dark:text-yellow-400">Mnemotecnia</h4>
                <ul className="mt-2 text-sm text-yellow-900 dark:text-yellow-300 space-y-2">
                    <li><strong>Gástrica</strong> = <strong>Ganancia</strong> (mayor) de dolor con la comida.</li>
                    <li><strong>Duodenal</strong> = <strong>Disminuye</strong> el dolor con la comida.</li>
                </ul>
            </div>
        </div>
    );
};

const TheClinic = () => {
    const cases = [
        {
            id: 1,
            patient: "Hombre de 45 años, antecedentes de EUP",
            symptoms: "Dolor abdominal intenso de inicio súbito, abdomen rígido 'en tabla'.",
            vitals: "FC 110, TA 90/60, Temp 38.5°C",
            imaging: "La radiografía muestra aire bajo el diafragma.",
            question: "¿Cuál es el diagnóstico?",
            options: ["Obstrucción de la salida gástrica", "Perforación", "Sangrado GI", "Zollinger-Ellison"],
            answer: "Perforación",
            explanation: "Aire bajo el diafragma (neumoperitoneo) + abdomen rígido + signos de sepsis = perforación. Esta es una emergencia quirúrgica."
        },
        {
            id: 2,
            patient: "Mujer de 60 años, usuaria de AINEs",
            symptoms: "Vómitos de comida no digerida, saciedad temprana, pérdida de peso.",
            vitals: "Estable",
            exam: "Sonido de 'chapoteo' audible en el epigastrio al sacudir al paciente (Chapoteo de Sucusión).",
            question: "¿Qué complicación es esta?",
            options: ["Obstrucción de la salida gástrica", "Perforación", "Gastritis", "Linfoma MALT"],
            answer: "Obstrucción de la salida gástrica",
            explanation: "El edema y la fibrosis cerca del píloro bloquean el vaciamiento gástrico. El 'Chapoteo de Sucusión' es el signo clásico de líquido atrapado en el estómago."
        },
        {
            id: 3,
            patient: "Hombre de 35 años, úlceras refractarias",
            symptoms: "Múltiples úlceras en el duodeno y el yeyuno. No responde a la terapia estándar con IBP.",
            labs: "Gastrina sérica > 1000 pg/mL",
            test: "Prueba de estimulación con secretina: Los niveles de gastrina permanecen altos.",
            question: "¿Cuál es la causa subyacente?",
            options: ["H. Pylori", "Abuso de AINEs", "Síndrome de Zollinger-Ellison", "Gastritis Autoinmune"],
            answer: "Síndrome de Zollinger-Ellison",
            explanation: "Úlceras refractarias + niveles masivos de gastrina = gastrinoma (Zollinger-Ellison). El tumor secreta gastrina sin control."
        }
    ];

    const [currentCase, setCurrentCase] = useState(0);
    const [selectedOption, setSelectedOption] = useState(null);
    const [showExplanation, setShowExplanation] = useState(false);

    const handleSelect = (option) => {
        setSelectedOption(option);
        setShowExplanation(true);
    };

    const nextCase = () => {
        setCurrentCase((prev) => (prev + 1) % cases.length);
        setSelectedOption(null);
        setShowExplanation(false);
    };

    const activeCase = cases[currentCase];

    return (
        <div className="max-w-3xl mx-auto p-6 fade-in">
            <div className="bg-white dark:bg-surface-dark rounded-xl shadow-xl overflow-hidden border border-slate-200 dark:border-slate-700">
                <div className="bg-slate-800 dark:bg-slate-900 text-white p-4 flex justify-between items-center">
                    <h2 className="text-xl font-bold flex items-center"><Stethoscope className="mr-2" /> Expediente del Caso #{activeCase.id}</h2>
                    <span className="text-slate-400 text-sm">Ronda {currentCase + 1} de {cases.length}</span>
                </div>

                <div className="p-6">
                    <div className="mb-6 space-y-3 text-slate-700 dark:text-slate-300">
                        <div className="flex border-b border-slate-100 dark:border-slate-800 pb-2">
                            <span className="w-24 font-bold text-slate-500">Paciente:</span>
                            <span>{activeCase.patient}</span>
                        </div>
                        <div className="flex border-b border-slate-100 dark:border-slate-800 pb-2">
                            <span className="w-24 font-bold text-slate-500">Síntomas:</span>
                            <span>{activeCase.symptoms}</span>
                        </div>
                        {activeCase.vitals && (
                            <div className="flex border-b border-slate-100 dark:border-slate-800 pb-2">
                                <span className="w-24 font-bold text-slate-500">Signos V:</span>
                                <span className="text-red-600 dark:text-red-400 font-mono">{activeCase.vitals}</span>
                            </div>
                        )}
                        {activeCase.exam && (
                            <div className="flex border-b border-slate-100 dark:border-slate-800 pb-2">
                                <span className="w-24 font-bold text-slate-500">Examen:</span>
                                <span>{activeCase.exam}</span>
                            </div>
                        )}
                        {activeCase.imaging && (
                            <div className="flex border-b border-slate-100 dark:border-slate-800 pb-2">
                                <span className="w-24 font-bold text-slate-500">Imagen:</span>
                                <span>{activeCase.imaging}</span>
                            </div>
                        )}
                        {activeCase.labs && (
                            <div className="flex border-b border-slate-100 dark:border-slate-800 pb-2">
                                <span className="w-24 font-bold text-slate-500">Labs:</span>
                                <span>{activeCase.labs}</span>
                            </div>
                        )}
                        {activeCase.test && (
                            <div className="flex border-b border-slate-100 dark:border-slate-800 pb-2">
                                <span className="w-24 font-bold text-slate-500">Pruebas:</span>
                                <span>{activeCase.test}</span>
                            </div>
                        )}
                    </div>

                    <h3 className="font-bold text-lg mb-4 text-slate-900 dark:text-white uppercase tracking-tight">{activeCase.question}</h3>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mb-6">
                        {activeCase.options.map((option) => (
                            <button
                                key={option}
                                onClick={() => handleSelect(option)}
                                disabled={showExplanation}
                                className={`p-3 rounded-lg border text-left transition-all ${showExplanation
                                    ? option === activeCase.answer
                                        ? 'bg-green-100 dark:bg-green-900/20 border-green-500 text-green-800 dark:text-green-400'
                                        : option === selectedOption
                                            ? 'bg-red-100 dark:bg-red-900/20 border-red-500 text-red-800 dark:text-red-400'
                                            : 'bg-slate-50 dark:bg-slate-800/50 border-slate-200 dark:border-slate-700 opacity-50'
                                    : 'hover:bg-blue-50 dark:hover:bg-blue-900/20 hover:border-blue-300 dark:hover:border-blue-700 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300'
                                    }`}
                            >
                                {option}
                            </button>
                        ))}
                    </div>

                    {showExplanation && (
                        <div className="animate-fadeIn bg-blue-50 dark:bg-blue-900/10 border border-blue-200 dark:border-blue-800 p-4 rounded-lg mb-4">
                            <h4 className="font-bold text-blue-800 dark:text-blue-400 mb-1">Análisis:</h4>
                            <p className="text-blue-900 dark:text-blue-300">{activeCase.explanation}</p>
                            <div className="mt-4 flex justify-end">
                                <button
                                    onClick={nextCase}
                                    className="bg-primary hover:bg-secondary text-white px-6 py-2 rounded-lg transition-all font-semibold"
                                >
                                    Siguiente Caso
                                </button>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

const App = () => {
    const [activeTab, setActiveTab] = useState('learn');

    return (
        <div className="min-h-screen bg-slate-50 dark:bg-background-dark font-lexend text-slate-900 dark:text-slate-100">
            <Navigation activeTab={activeTab} setActiveTab={setActiveTab} />

            <main className="container mx-auto py-8 px-4">
                {activeTab === 'learn' && <StudyNotes />}
                {activeTab === 'microscope' && <MicroscopeLab />}
                {activeTab === 'simulator' && <PainSimulator />}
                {activeTab === 'clinic' && <TheClinic />}
            </main>

            <footer className="bg-slate-900 text-slate-400 py-6 text-center text-sm mt-12 border-t border-slate-800">
                <p>Artefacto educativo basado en "Stomach Disorders" de Ninja Nerd.</p>
                <p className="mt-2">Aviso: Solo para fines educativos. No es consejo médico.</p>
            </footer>
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
