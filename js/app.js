const translations = {
    fr: {
        "download": "Télécharger",
        "hero-title": "Arrêtez de manipuler l'écran.<br><span class='highlight'>Votre voix contrôle le prompteur.</span>",
        "hero-subtitle": "VoxPresenter écoute votre lecture et avance automatiquement au bon paragraphe. Présentez avec aisance, sans jamais toucher votre iPhone.",
        "hero-cta": "Obtenir VoxPresenter",
        "features-title": "Pourquoi VoxPresenter ?",
        "feat1-title": "Reconnaissance vocale locale",
        "feat1-desc": "L'application écoute votre discours et compare ce qui est dit au texte courant, le tout directement sur votre appareil.",
        "feat2-title": "100% Automatique",
        "feat2-desc": "L'app avance automatiquement au paragraphe suivant quand elle reconnaît suffisamment la lecture. Plus besoin de scroller.",
        "feat3-title": "Tolérant & Intelligent",
        "feat3-desc": "Hésitations, petites reformulations, ou sauts dans le texte ? VoxPresenter s'adapte et retrouve le fil de votre discours.",
        "mac-title": "Pilotez vos slides depuis votre iPhone",
        "mac-desc": "L'application compagnon macOS, VoxPresenterRemote, transforme votre iPhone en télécommande magique. Chaque changement de paragraphe sur l'iPhone passe la slide suivante sur votre Mac (PowerPoint, Keynote, Canva...).",
        "mac-mockup": "VoxPresenterRemote sur Mac",
        "cta-title": "Prêt à transformer vos présentations ?",
        "cta-desc": "Téléchargez VoxPresenter dès aujourd'hui et concentrez-vous sur votre public, pas sur votre écran.",
        "download-btn": "Télécharger sur l'App Store"
    },
    en: {
        "download": "Download",
        "hero-title": "Stop swiping the screen.<br><span class='highlight'>Your voice controls the prompter.</span>",
        "hero-subtitle": "VoxPresenter listens as you read and automatically advances to the right paragraph. Present smoothly without ever touching your iPhone.",
        "hero-cta": "Get VoxPresenter",
        "features-title": "Why VoxPresenter?",
        "feat1-title": "On-Device Speech Recognition",
        "feat1-desc": "The app listens to your speech and matches it with the current text, all processed securely on your device.",
        "feat2-title": "100% Automatic",
        "feat2-desc": "It seamlessly moves to the next paragraph when it recognizes enough of what you're reading. No more manual scrolling.",
        "feat3-title": "Forgiving & Smart",
        "feat3-desc": "Hesitations, minor rephrasing, or skipped lines? VoxPresenter adapts and finds your place effortlessly.",
        "mac-title": "Control slides from your iPhone",
        "mac-desc": "The macOS companion app, VoxPresenterRemote, turns your iPhone into a magical remote. Every paragraph change on iOS triggers the next slide on your Mac (PowerPoint, Keynote, Canva...).",
        "mac-mockup": "VoxPresenterRemote for Mac",
        "cta-title": "Ready to upgrade your presentations?",
        "cta-desc": "Download VoxPresenter today and focus entirely on your audience, not your screen.",
        "download-btn": "Download on the App Store"
    }
};

let currentLang = 'fr';

function setLanguage(lang) {
    currentLang = lang;
    document.documentElement.lang = lang;
    
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });
}

function toggleLanguage() {
    const newLang = currentLang === 'fr' ? 'en' : 'fr';
    setLanguage(newLang);
}

// Initial setup
document.addEventListener('DOMContentLoaded', () => {
    // Detect browser language or default to 'fr'
    const browserLang = navigator.language.slice(0, 2);
    const initialLang = (browserLang === 'en') ? 'en' : 'fr';
    setLanguage(initialLang);
});
