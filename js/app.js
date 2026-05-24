const translations = {
    fr: {
        "nav-download":  "Télécharger",
        "hero-badge":    "✦ Pour iPhone & iPad",
        "hero-line1":    "Arrêtez de scroller.",
        "hero-line2":    "Lisez, l'app avance.",
        "hero-subtitle": "VoxPresenter reconnaît votre voix et défile automatiquement au bon paragraphe. Concentrez-vous sur votre public, pas sur votre écran.",
        "hero-cta":      "Télécharger sur l'App Store",

        "how-label":   "COMMENT ÇA MARCHE",
        "how-title":   "Simple. Automatique. Efficace.",
        "step1-title": "Collez votre texte",
        "step1-desc":  "Importez votre discours, vos notes ou tout texte à lire depuis votre bibliothèque.",
        "step2-title": "Parlez naturellement",
        "step2-desc":  "L'app écoute votre voix en temps réel, sur votre appareil. Pas de cloud, zéro latence.",
        "step3-title": "Le prompteur suit",
        "step3-desc":  "Chaque paragraphe est mis en évidence automatiquement. Posez l'iPhone et présentez.",

        "feat-label":     "FONCTIONNALITÉS",
        "features-title": "Conçu pour les présentateurs",
        "feat1-title": "Reconnaissance locale",
        "feat1-desc":  "Tout se passe sur votre appareil. Vos mots restent privés, même sans connexion.",
        "feat2-title": "Défilement automatique",
        "feat2-desc":  "L'app avance au bon paragraphe sans aucune interaction. Posez votre iPhone et lisez.",
        "feat3-title": "Tolérant & intelligent",
        "feat3-desc":  "Hésitations, reformulations, sauts ? VoxPresenter s'adapte et retrouve votre fil.",

        "mac-label":      "APPLICATION MAC",
        "mac-title":      "Contrôlez vos slides depuis l'iPhone",
        "mac-desc":       "L'app compagnon macOS transforme votre iPhone en télécommande sans fil. Chaque changement de paragraphe fait avancer votre présentation sur le Mac.",
        "mac-connected":  "Connecté",
        "mac-f1": "Keynote, PowerPoint, Canva et plus",
        "mac-f2": "Connexion Wi-Fi locale automatique",
        "mac-f3": "Gratuit pour les utilisateurs VoxPresenter",

        "cta-title":    "Prêt pour votre prochaine présentation ?",
        "cta-desc":     "Gratuit sur l'App Store pour iPhone et iPad.",
        "download-btn": "Télécharger sur l'App Store",

        "sc-label":    "L'APP EN ACTION",
        "sc-title":    "Comme dans votre main",
        "sc1-caption": "Tableau de bord",
        "sc2-caption": "Lecture automatique",

        "footer-privacy": "Confidentialité",
        "footer-terms": "CGU",
        "footer-legal": "Mentions légales",
        "footer-contact": "Contact"
    },
    en: {
        "nav-download":  "Download",
        "hero-badge":    "✦ For iPhone & iPad",
        "hero-line1":    "Stop swiping.",
        "hero-line2":    "Speak, the app follows.",
        "hero-subtitle": "VoxPresenter listens as you read and automatically advances to the right paragraph. Focus on your audience, not your screen.",
        "hero-cta":      "Download on the App Store",

        "how-label":   "HOW IT WORKS",
        "how-title":   "Simple. Automatic. Effortless.",
        "step1-title": "Paste your text",
        "step1-desc":  "Import your speech, notes, or any text you want to read from your library.",
        "step2-title": "Speak naturally",
        "step2-desc":  "The app listens in real time, on your device. No cloud, zero latency.",
        "step3-title": "The prompter follows",
        "step3-desc":  "Each paragraph is highlighted automatically. Put down your iPhone and present.",

        "feat-label":     "FEATURES",
        "features-title": "Built for real presenters",
        "feat1-title": "On-device recognition",
        "feat1-desc":  "Everything happens on your device. Your words stay private, even offline.",
        "feat2-title": "Automatic scrolling",
        "feat2-desc":  "The app advances to the right paragraph with zero interaction. Put it down and read.",
        "feat3-title": "Forgiving & smart",
        "feat3-desc":  "Hesitations, rephrasing, skips? VoxPresenter adapts and finds your place.",

        "mac-label":      "MAC APP",
        "mac-title":      "Control slides from your iPhone",
        "mac-desc":       "The macOS companion turns your iPhone into a wireless remote. Every paragraph change advances your presentation on Mac.",
        "mac-connected":  "Connected",
        "mac-f1": "Keynote, PowerPoint, Canva and more",
        "mac-f2": "Automatic local Wi-Fi connection",
        "mac-f3": "Free for VoxPresenter users",

        "cta-title":    "Ready for your next presentation?",
        "cta-desc":     "Free on the App Store for iPhone and iPad.",
        "download-btn": "Download on the App Store",

        "sc-label":    "THE APP IN ACTION",
        "sc-title":    "Right in your hand",
        "sc1-caption": "Dashboard",
        "sc2-caption": "Automatic reading",

        "footer-privacy": "Privacy",
        "footer-terms": "Terms",
        "footer-legal": "Legal",
        "footer-contact": "Contact"
    }
};

let currentLang = 'fr';

function setLanguage(lang) {
    currentLang = lang;
    document.documentElement.lang = lang;

    const btn = document.getElementById('langBtn');
    if (btn) btn.textContent = lang === 'fr' ? '🇬🇧' : '🇫🇷';

    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        const val = translations[lang]?.[key];
        if (val !== undefined) el.innerHTML = val;
    });

    // Switch screenshots based on language
    const isEn = lang === 'en';
    const dashboard = document.getElementById('sc-dashboard');
    const prompter  = document.getElementById('sc-prompter');
    const hero      = document.getElementById('hero-img');
    if (dashboard) dashboard.src = isEn ? 'assets/screenshot-dashboard.png_EN.PNG' : 'assets/screenshot-dashboard.png';
    if (prompter)  prompter.src  = isEn ? 'assets/screenshot-prompter_EN.PNG'       : 'assets/screenshot-prompter.png';
    if (hero)      hero.src      = isEn ? 'assets/screenshot-prompter_EN.PNG'        : 'assets/screenshot-prompter.png';
}

function toggleLanguage() {
    setLanguage(currentLang === 'fr' ? 'en' : 'fr');
}

// Scroll effect on navbar
window.addEventListener('scroll', () => {
    document.getElementById('navbar')?.classList.toggle('scrolled', window.scrollY > 20);
});

// Language auto-detection on load
document.addEventListener('DOMContentLoaded', () => {
    const preferred = navigator.languages ?? [navigator.language ?? 'fr'];
    const hasFr = preferred.some(l => l.startsWith('fr'));
    const hasEn = preferred.some(l => l.startsWith('en'));
    setLanguage(hasEn && !hasFr ? 'en' : 'fr');
});
