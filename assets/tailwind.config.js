module.exports = {
  darkMode: "class",
  // Directorios reales de contenido. Se evita "./**/*.html" porque arrastraba
  // node_modules y los dist/ de las sub-apps Vite.
  // Los .jsx son la fuente de los módulos interactivos: las clases viven ahí,
  // no en el .bundle.js minificado.
  content: [
    "./*.html",
    "./farmacoterapia_racional/**/*.html",
    "./gastroenterologia/**/*.html",
    "./inmunologia/**/*.html",
    "./medicina_e_implementacion/**/*.html",
    "./medicina_y_datos/**/*.html",
    "./neurologia/**/*.html",
    "./**/*.jsx",
    "!./**/node_modules/**",
    "!./**/dist/**",
  ],
  theme: {
    extend: {
      colors: {
        // --- Claves originales: gobiernan las ~77 páginas que ya usaban
        // tailwind.css local. NO se tocan. ---
        primary: "#8B3DFF",
        secondary: "#FF4081",
        "background-light": "#F8FAFC",
        "background-dark": "#0F172A",
        "card-light": "#FFFFFF",
        "card-dark": "#1E293B",
        "text-light": "#334155",
        "text-dark": "#E2E8F0",

        // --- Añadidas al absorber las 23 páginas del CDN ---
        danger: "#ef4444",
        success: "#10b981",
        warning: "#f59e0b",
        alert: "#ef4444",
        gold: "#f59e0b",
        "primary-hover": "#7C3AED",
        "surface-light": "#ffffff",
        "surface-dark": "#1a242d",
        "border-light": "#e2e8f0",
        "border-dark": "#2d3748",
        "text-primary-light": "#1E293B",
        "text-primary-dark": "#F8FAFC",
        "text-secondary-light": "#64748B",
        "text-secondary-dark": "#94A3B8",
        medical: {
          50: "#f0f9ff",
          100: "#e0f2fe",
          600: "#0284c7",
          800: "#075985",
          900: "#0c4a6e",
        },
        slate: {
          950: "#020617",
        },
      },
      fontFamily: {
        // Originales, intactas.
        display: ['Playfair Display', 'serif'],
        sans: ['Outfit', 'sans-serif'],
        // Añadidas: cada página que traía su propia tipografía la conserva
        // con una utilidad explícita en vez de redefinir font-sans.
        lexend: ['Lexend', 'sans-serif'],
        jakarta: ['Plus Jakarta Sans', 'sans-serif'],
        outfit: ['Outfit', 'sans-serif'],
        inter: ['Inter', 'system-ui', 'sans-serif'],
        // Pila por defecto de Tailwind: la conservan las paginas que corrian
        // con la configuracion de fabrica del CDN.
        // Utilidades dedicadas: NO se redefine font-serif/font-mono, que ya
        // existen en el tema por defecto y gobiernan las paginas ya migradas.
        dmserif: ["'DM Serif Display'", 'serif'],
        jetbrains: ['JetBrains Mono', 'monospace'],
        system: ['ui-sans-serif','system-ui','-apple-system','Segoe UI','Roboto','Helvetica Neue','Arial','sans-serif'],
      },
      borderRadius: {
        // DEFAULT permanece en 1rem: lo usan las páginas ya migradas.
        DEFAULT: "1rem",
        lg: "0.75rem",
        xl: "1rem",
        full: "9999px",
      },
      boxShadow: {
        'soft': '0 4px 20px -2px rgba(0, 0, 0, 0.05)',
        'hover': '0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)',
      }
    },
  },
  plugins: [
    // strategy 'class' evita el reset global de input/select/textarea, que
    // repintaría formularios en las ~77 páginas que nunca lo tuvieron.
    require('@tailwindcss/forms')({ strategy: 'class' }),
    require('@tailwindcss/typography'),
    require('@tailwindcss/container-queries'),
  ],
};
