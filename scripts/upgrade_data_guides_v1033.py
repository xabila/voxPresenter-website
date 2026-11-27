#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upgrades site-web/scripts/data_guides.py for VoxPresenter v1.0.33:
1. Purges all em-dashes (—) across all 5 languages (impeccable compliance).
2. Injects v1.0.33 Live Stage Mode (# Cue Sheet, 1-tap Voice Pause, Bluetooth Clickers)
   into COMPARE_GUIDE and automatic .pptx # chapter bookmarks into PPTX_GUIDE.
3. Injects Apple Watch Series 9+ / Ultra 2 one-handed Double Tap into WATCH_GUIDE.
4. Adds the 5th localized bottom-of-funnel SEO/GEO authority guide: STAGE_EMCEE_GUIDE
   (stage-emcee-bluetooth-clicker-teleprompter.html) across FR, EN, ES, DE, PT.
"""

import pprint
import sys
from pathlib import Path

SCRIPTS_DIR = Path("/Users/xabi/DEV/EyePrompteur/site-web/scripts")
sys.path.insert(0, str(SCRIPTS_DIR))

import data_guides as dg


def clean_obj(obj):
    if isinstance(obj, str):
        # Replace em-dash and spaced en-dash with clean editorial punctuation
        s = obj.replace(" — ", " : ").replace("—", ", ").replace(" – ", ", ")
        return s
    if isinstance(obj, list):
        return [clean_obj(x) for x in obj]
    if isinstance(obj, tuple):
        return tuple(clean_obj(x) for x in obj)
    if isinstance(obj, dict):
        return {k: clean_obj(v) for k, v in obj.items()}
    return obj


COMPARE = clean_obj(dg.COMPARE_GUIDE)
PPTX = clean_obj(dg.PPTX_GUIDE)
WATCH = clean_obj(dg.WATCH_GUIDE)
YOUTUBE = clean_obj(dg.YOUTUBE_STUDIO_GUIDE)

# 1. Enrich COMPARE_GUIDE with Live Stage & Bluetooth Clicker row (inserted at index 2)
STAGE_CMP_ROW = {
    "fr": (
        "Mode Scène Live : Signets #, Pause Voix & Clicker Bluetooth",
        "✓ Vue continue, saut 1 tap aux chapitres #, pause micro & clickers Bluetooth (touche B / .)",
        "✗ Défilement simple sans conducteur ni clicker dédiés",
        "✗ Non conçu pour la scène live",
        "Télécommande de vitesse basique uniquement",
    ),
    "en": (
        "Live Stage Mode: # Cue Jumps, Voice Pause & Bluetooth Clicker",
        "✓ Continuous lookahead, 1-tap # cue jumps, 1-tap mic mute & HID Bluetooth clickers (B / . key)",
        "✗ Plain scroll without stage cue sheet",
        "✗ Not built for live stages",
        "Basic timer speed remote only",
    ),
    "es": (
        "Modo Escena Live: Marcadores #, Pausa Voz y Clicker Bluetooth",
        "✓ Vista continua, salto 1 toque a capítulos #, pausa de micro y clickers Bluetooth (tecla B / .)",
        "✗ Scroll simple sin escaleta de escena",
        "✗ No diseñado para eventos en directo",
        "Solo mando básico de velocidad",
    ),
    "de": (
        "Live-Bühnenmodus: #-Marken, Sprachpause & Bluetooth-Clicker",
        "✓ Fließtext-Vorschau, 1-Tipp #-Kapitelsprung, Mikrofon-Pause & HID-Bluetooth-Clicker (Taste B / .)",
        "✗ Einfacher Bildlauf ohne Regie-Marken",
        "✗ Nicht für Live-Bühnen konzipiert",
        "Nur einfache Tempotaste",
    ),
    "pt": (
        "Modo Palco Live: Favoritos #, Pausa Voz e Passador Bluetooth",
        "✓ Visão contínua, salto 1 toque a capítulos #, pausa de microfone e passadores Bluetooth (tecla B / .)",
        "✗ Rolagem simples sem capítulos de palco",
        "✗ Não projetado para eventos ao vivo",
        "Apenas controle básico de velocidade",
    ),
}

for lang, row in STAGE_CMP_ROW.items():
    mat = COMPARE[lang]["matrix"]
    if not any("Bluetooth" in r[0] for r in mat):
        mat.insert(2, row)

# 2. Enrich PPTX_GUIDE with automatic slide-title # chapter bookmarks
PPTX_CHAPTER_ROW = {
    "fr": (
        "Chapitres & Signets # automatiques par slide",
        "✓ Extrait chaque titre de diapositive en signet # pour sauter en 1 tap en direct",
        "Grille miniature sur l'ordinateur uniquement",
        "✗ Navigation linéaire uniquement",
    ),
    "en": (
        "Automatic # Cue Bookmarks from Slide Titles",
        "✓ Turns every .pptx slide title into a 1-tap # stage chapter for live order changes",
        "Laptop screen thumbnail grid only",
        "✗ Linear slide-by-slide only",
    ),
    "es": (
        "Capítulos y Marcadores # automáticos por diapositiva",
        "✓ Convierte cada título .pptx en marcador # para saltar en 1 toque en directo",
        "Solo cuadrícula en la pantalla del portátil",
        "✗ Solo avance lineal",
    ),
    "de": (
        "Automatische #-Kapitelmarken aus Folientiteln",
        "✓ Wandelt jeden .pptx-Folientitel in eine 1-Tipp #-Sprungmarke für Live-Änderungen um",
        "Nur Folienübersicht am Laptop",
        "✗ Nur lineares Blättern",
    ),
    "pt": (
        "Capítulos e Favoritos # automáticos por slide",
        "✓ Transforma cada título .pptx em favorito # para pular em 1 toque ao vivo",
        "Apenas grade na tela do notebook",
        "✗ Apenas avanço linear",
    ),
}

for lang, row in PPTX_CHAPTER_ROW.items():
    rows = PPTX[lang]["tbl_rows"]
    if not any("#" in r[0] for r in rows):
        rows.insert(1, row)

# 3. Enrich WATCH_GUIDE with Series 9+ / Ultra 2 one-handed Double Tap FAQ & lead note
WATCH_DT_FAQ = {
    "fr": (
        "Puis-je avancer sur scène d'une seule main avec le geste Double Tap sans croiser les bras ?",
        "Oui (nouveauté v1.0.33). Sur Apple Watch Series 9, Series 10, Series 11 et Apple Watch Ultra 2+, pincez simplement deux fois l'index et le pouce (Double Tap) pour déclencher l'action principale sans ramener l'autre bras devant vous ni baisser les yeux, en gardant une posture ouverte face au public.",
    ),
    "en": (
        "Can I advance onstage one-handed using Apple Watch Double Tap without crossing my arm?",
        "Yes (new in v1.0.33). On Apple Watch Series 9, Series 10, Series 11, and Ultra 2+, simply pinch your index finger and thumb twice (Double Tap) to trigger your primary slide or cue action one-handed, keeping a natural, open body posture toward your audience.",
    ),
    "es": (
        "¿Puedo avanzar en el escenario con una sola mano usando Double Tap sin cruzar el brazo?",
        "Sí (novedad v1.0.33). En Apple Watch Series 9, Series 10, Series 11 y Ultra 2+, junta dos veces el índice y el pulgar (Double Tap) para activar la acción principal con una sola mano y mantener una postura abierta ante el público.",
    ),
    "de": (
        "Kann ich auf der Bühne einhändig per Apple Watch Double Tap weiterschalten, ohne den Arm zu kreuzen?",
        "Ja (neu in v1.0.33). Auf Apple Watch Series 9, Series 10, Series 11 und Ultra 2+ genügt ein Doppeltipp mit Zeigefinger und Daumen (Double Tap), um einhändig weiterzuschalten und eine offene Körperhaltung vor dem Publikum zu bewahren.",
    ),
    "pt": (
        "Posso avançar no palco com uma só mão usando o Double Tap sem cruzar o braço?",
        "Sim (novidade v1.0.33). No Apple Watch Series 9, Series 10, Series 11 e Ultra 2+, toque duas vezes o indicador e o polegar (Double Tap) para acionar a ação principal com uma única mão, mantendo postura aberta diante da plateia.",
    ),
}

for lang, fq in WATCH_DT_FAQ.items():
    fqs = WATCH[lang]["faqs"]
    if not any("Double Tap" in q for q, _ in fqs):
        fqs.append(fq)

# 4. Brand-new 5th localized authority guide: STAGE_EMCEE_GUIDE
STAGE_EMCEE_GUIDE = {
    "fr": {
        "nav_label": "Scène & Clicker Bluetooth",
        "title": "Prompteur de Scène Live, Conférence & Clicker Bluetooth sur iPhone et iPad · VoxPresenter",
        "desc": "Le téléprompteur pensé pour les conférenciers, maîtres de cérémonie (MC) et animateurs : vue continue, signets # de conducteur, pause voix 1 tap pour co-orateurs, clickers Bluetooth de poche et Apple Watch Double Tap.",
        "keywords": "prompteur conférence scène iPhone, téléprompteur clicker Bluetooth iPhone iPad, prompteur maître de cérémonie conducteur, signets téléprompteur live, pause reconnaissance vocale co-animateur, Logitech Spotlight téléprompteur iOS",
        "eyebrow": "Guide Scène Live, Maîtres de Cérémonie (MC) & Clickers Bluetooth",
        "h1": "Téléprompteur de Scène Live : Signets de Conducteur, Pause Voix & Clicker Bluetooth sur iPhone et iPad",
        "lead": "Sur une vraie scène devant 500 personnes, tout ne se passe jamais comme prévu : la salle applaudit, un co-animateur prend la parole, ou la régie inverse deux séquences en dernière minute. Voici comment le Mode Scène Live de VoxPresenter allie suivi vocal hors-ligne et contrôle manuel infaillible.",
        "sum_h2": "Pourquoi les orateurs professionnels ne peuvent pas dépendre d'un simple défilement automatique",
        "sum_p1": "<strong>Les limites des prompteurs classiques sur scène :</strong> une vue bloquée sur un seul paragraphe empêche d'anticiper la suite pour couper une transition à la volée, et un micro resté actif risque d'avancer si votre co-animateur prononce un mot du conducteur.",
        "sum_p2": "<strong>La réponse VoxPresenter v1.0.33 (conçue avec des maîtres de cérémonie) :</strong> profitez d'une <strong>vue continue avec anticipation</strong>, sautez à n'importe quel <strong>signet <code># Chapitre</code> en 1 tap</strong> avec resynchronisation immédiate de la voix, et gardez un <strong>clicker Bluetooth en poche</strong> pour avancer, reculer ou couper l'écoute vocale (touche <code>B</code> / <code>.</code>) sans jamais regarder l'écran.",
        "steps_h2": "4 Réflexes Pro pour Sécuriser un Direct sur Scène",
        "steps": [
            (
                "Balisez votre conducteur avec des signets # ou un import .pptx",
                "Écrivez simplement # Ouverture, # Remise des prix ou [CUE: Clôture] dans votre script (ou importez un fichier .pptx dont chaque titre de slide devient automatiquement un signet).",
            ),
            (
                "Lisez en Vue Continue et sautez à la volée en 1 tap",
                "Voyez toujours les phrases suivantes sous le paragraphe actif. Si l'ambiance de la salle vous pousse à abréger, touchez directement un paragraphe plus bas : la voix repart de ce point exact.",
            ),
            (
                "Glissez un clicker Bluetooth standard dans votre poche",
                "Appairez n'importe quelle télécommande Bluetooth HID (Logitech Spotlight, R400/R500, Kensington, Satechi). Flèches Suivant/Précédent pour naviguer, et touche écran noir (B ou .) pour mettre la voix en pause quand un invité parle.",
            ),
            (
                "Gardez une posture ouverte avec Apple Watch Double Tap",
                "Sur Apple Watch Series 9+ et Ultra 2, un double pincement index-pouce d'une seule main fait avancer votre repère sans croiser les bras devant vous.",
            ),
        ],
        "tbl_h2": "VoxPresenter Mode Scène Live face aux Prompteurs Classiques & Fiches Papier",
        "tbl_cols": [
            "Imprévu en Direct sur Scène",
            "VoxPresenter v1.0.33 (Scène Live)",
            "Prompteurs Vocaux Classiques",
            "Timers Fixes & Fiches Papier",
        ],
        "tbl_rows": [
            (
                "Couper un paragraphe selon la réaction du public",
                "✓ Vue continue + tap sur le paragraphe voulu avec resynchro vocale immédiate",
                "✗ Paragraphe isolé ou perte du fil vocal",
                "✗ Le timer continue de défiler dans le vide",
            ),
            (
                "Changement d'ordre du conducteur en régie",
                "✓ Tiroir de signets # (et chapitres .pptx auto) accessible en 1 tap",
                "✗ Défilement manuel laborieux à l'écran",
                "✗ Feuilles papier mélangées au pupitre",
            ),
            (
                "Co-animateur au micro ou salle très bruyante",
                "✓ Pause voix 1 tap à l'écran OU touche B / . du clicker Bluetooth en poche",
                "✗ Risque d'avance intempestive par l'autre micro",
                "Sans objet (aucun suivi vocal)",
            ),
            (
                "Secours manuel discret sans baisser les yeux",
                "✓ Clicker Bluetooth HID en poche + Apple Watch Double Tap 1 main",
                "✗ Oblige à toucher l'écran de l'iPad / iPhone",
                "Télécommande de vitesse imprécise",
            ),
            (
                "Interface épurée sur pupitre ou retour de scène",
                "✓ Contrôles distillés : maximum d'espace pour le texte, Mode Avion 100 % local",
                "Menus denses et boutons ambigus",
                "Lisibilité réduite sous projecteurs",
            ),
        ],
        "faqs": [
            (
                "Quels clickers Bluetooth sont compatibles avec VoxPresenter sur iPhone et iPad ?",
                "Toute télécommande de présentation Bluetooth reconnue comme clavier HID standard par iOS et iPadOS fonctionne immédiatement sans configuration : Logitech Spotlight, Logitech R500s, Kensington, Satechi, Targus ou anneaux Bluetooth. Les touches Suivant/Précédent (Flèches, Page Down/Up, Espace) déplacent le script et la touche écran noir (B ou .) coupe ou relance l'écoute vocale.",
            ),
            (
                "Comment éviter que la voix de mon co-animateur ne fasse avancer mon texte ?",
                "Touchez le bouton ambre Pause en haut du prompteur (ou pressez la touche B / . de votre clicker Bluetooth dans votre poche) dès que vous passez la parole. Le prompteur se fige proprement sur votre prochaine réplique jusqu'à votre reprise.",
            ),
            (
                "Comment créer des signets de chapitres pour une remise de prix ou une plénière ?",
                "Commencez simplement une ligne par # suivi du nom de la séquence (par exemple # Introduction Keynote ou # Prix Innovation), ou importez votre présentation PowerPoint (.pptx) pour générer automatiquement tous les chapitres à partir des titres de diapositives.",
            ),
            (
                "Puis-je combiner suivi vocal hors-ligne et clicker manuel dans la même session ?",
                "Oui, c'est tout l'esprit du Mode Scène Live : laissez votre voix faire défiler le texte naturellement à 95 % du temps, et reprenez la main à tout instant d'un geste au doigt, au clicker Bluetooth ou sur l'Apple Watch sans interrompre la session.",
            ),
        ],
    },
    "en": {
        "nav_label": "Live Stage & Clicker",
        "title": "Live Stage, Emcee & Bluetooth Clicker Teleprompter App for iPhone & iPad · VoxPresenter",
        "desc": "Built with professional keynote speakers and live event emcees: continuous script lookahead, 1-tap # cue bookmarks, voice-tracking pause for co-hosts, pocket Bluetooth clicker control, and 1-handed Apple Watch Double Tap.",
        "keywords": "teleprompter with bluetooth clicker iPhone iPad, live stage emcee teleprompter app, cue sheet teleprompter bookmarks, pause voice tracking co-host teleprompter, Logitech Spotlight teleprompter iOS, Apple Watch Double Tap presenter",
        "eyebrow": "Live Stage, Conference Emcee (MC) & Bluetooth Clicker Guide",
        "h1": "Live Stage & Emcee Teleprompter: # Cue Sheet, Voice Pause & Bluetooth Clicker Control on iPhone & iPad",
        "lead": "In front of a live audience, shows rarely stay 100% on script: applause runs long, a co-host shares the stage, or the producer swaps two segments mid-event. Here is how VoxPresenter Live Stage Mode pairs offline voice tracking with instant, eyes-free manual control.",
        "sum_h2": "Why Professional Speakers & Emcees Need More Than Auto-Scroll Alone",
        "sum_p1": "<strong>Where standard teleprompter apps break onstage:</strong> single-paragraph views hide upcoming transitions when you want to cut a section on the fly, and an always-hot mic can advance prematurely if a co-host speaks a word from your script.",
        "sum_p2": "<strong>The VoxPresenter v1.0.33 Live Stage workflow:</strong> read ahead in <strong>Continuous Script View</strong>, jump straight to any <strong><code># Cue</code> bookmark in 1 tap</strong> with instant voice resync, and keep a <strong>Bluetooth clicker in your pocket</strong> to step forward, back, or mute voice listening (via the <code>B</code> / <code>.</code> blackout key) without ever looking down.",
        "steps_h2": "4 Onstage Habits for Bulletproof Live Shows",
        "steps": [
            (
                "Mark sections with # Cue Headings or import .pptx chapters",
                "Type # Speaker Intro, # Award Presentation, or [CUE: Closing] anywhere in your script, or import a PowerPoint (.pptx) deck to turn every slide title into a chapter automatically.",
            ),
            (
                "Read in Continuous View & tap any paragraph to jump live",
                "Upcoming sentences stay visible beneath your active block. Reading the room and cutting a paragraph? Tap where you want to pick up and voice tracking locks on from that exact spot.",
            ),
            (
                "Keep a Bluetooth presentation clicker in your pocket",
                "Pair any standard Bluetooth HID clicker (Logitech Spotlight, R500s, Kensington, Satechi). Use Next/Back to move paragraph by paragraph, and press the blackout button (B or .) to pause voice listening when a co-host has the mic.",
            ),
            (
                "Maintain an open stance with Apple Watch Double Tap",
                "On Apple Watch Series 9+ and Ultra 2, a subtle one-handed Double Tap pinch advances your script or slides without bringing your other arm across your body.",
            ),
        ],
        "tbl_h2": "VoxPresenter Live Stage vs. Voice-Only & Timer Teleprompters",
        "tbl_cols": [
            "Live Onstage Scenario",
            "VoxPresenter v1.0.33 (Live Stage)",
            "Voice-Only Teleprompters",
            "Fixed-Timer Apps & Paper Cards",
        ],
        "tbl_rows": [
            (
                "Cutting a paragraph based on audience energy",
                "✓ Continuous lookahead + 1-tap paragraph jump & instant voice resync",
                "✗ Blind to upcoming lines or loses voice sync",
                "✗ Timer keeps scrolling past your spot",
            ),
            (
                "Producer changes the running order live",
                "✓ 1-tap # Cue Sheet drawer (plus automatic .pptx slide chapters)",
                "✗ Frantic manual scrolling mid-show",
                "✗ Shuffling printed index cards onstage",
            ),
            (
                "Sharing the stage with a co-host or loud room",
                "✓ 1-tap HUD Pause OR pocket Bluetooth clicker B / . mute toggle",
                "✗ Co-host speech can advance your script early",
                "N/A (no voice tracking)",
            ),
            (
                "Eyes-free manual backup without looking down",
                "✓ Pocket Bluetooth HID clicker + 1-handed Apple Watch Double Tap",
                "✗ Must reach out and touch the iPhone/iPad glass",
                "Clunky speed-slider remotes",
            ),
            (
                "Stage monitor & confidence screen clarity",
                "✓ Distilled compact HUD maximizing script space, 100% Airplane-Mode offline",
                "Crowded toolbars and ambiguous buttons",
                "Hard to read under stage lights",
            ),
        ],
        "faqs": [
            (
                "Which Bluetooth clickers work with VoxPresenter on iPhone and iPad?",
                "Any Bluetooth presentation clicker that pairs as a standard HID keyboard on iOS and iPadOS works out of the box with zero proprietary dongle setup, including Logitech Spotlight, Logitech R500s, Satechi, Kensington, and Bluetooth finger rings. Next/Back keys advance or rewind paragraphs, while the B or . blackout key toggles voice-tracking pause.",
            ),
            (
                "What if I share the stage and my co-host says a line that appears in my script?",
                "Simply tap the amber Pause pill in the prompter HUD (or click the B / . button on your pocket Bluetooth clicker) whenever someone else has the mic. VoxPresenter holds your exact line frozen until you unpause.",
            ),
            (
                "How do I set up cue points or chapters before an event?",
                "Start any line with # followed by the section name (such as # Opening Remarks or # Fireside Q&A), use [CUE: Title], or import a .pptx file where slide titles automatically populate the stage cue drawer.",
            ),
            (
                "Can I mix automatic voice tracking and manual Bluetooth clicker stepping in the same talk?",
                "Yes. Let on-device voice tracking carry you naturally when reading verbatim, and press your Bluetooth clicker or tap any paragraph whenever you go off-script or want manual control.",
            ),
        ],
    },
    "es": {
        "nav_label": "Escena Live y Clicker",
        "title": "Teleprónter de Escenario Live, Presentadores y Clicker Bluetooth en iPhone y iPad · VoxPresenter",
        "desc": "Diseñado para maestros de ceremonias, conferenciantes y moderadores: vista continua, marcadores # de escaleta, pausa de voz en 1 toque para copresentadores, mando clicker Bluetooth de bolsillo y Apple Watch Double Tap.",
        "keywords": "teleprompter clicker Bluetooth iPhone iPad, teleprónter maestro de ceremonias escenario, marcadores escaleta teleprónter, pausar voz copresentador teleprompter, Logitech Spotlight teleprompter iOS",
        "eyebrow": "Guía Escena Live, Maestros de Ceremonias (MC) y Clickers Bluetooth",
        "h1": "Teleprónter de Escena Live: Escaleta con Marcadores #, Pausa de Voz y Clicker Bluetooth en iPhone e iPad",
        "lead": "Ante un auditorio en directo, el guion cambia sobre la marcha: aplausos largos, otro ponente compartiendo micrófono o un cambio de orden de última hora. Así combina el Modo Escena Live de VoxPresenter seguimiento por voz offline y respaldo manual inmediato.",
        "sum_h2": "Por qué en eventos en vivo no basta con el desplazamiento automático",
        "sum_p1": "<strong>El fallo de los teleprónteres comunes en directo:</strong> ver solo un párrafo impide anticipar cortes según reaccione el público, y dejar el micrófono siempre activo puede adelantar tu texto si habla un copresentador.",
        "sum_p2": "<strong>El flujo Escena Live v1.0.33 de VoxPresenter:</strong> lee con antelación en <strong>Vista Continua</strong>, salta a cualquier <strong>marcador <code># Sección</code> en 1 toque</strong> resincronizando la voz al instante, y lleva un <strong>clicker Bluetooth en el bolsillo</strong> para avanzar, retroceder o pausar la escucha vocal (tecla <code>B</code> / <code>.</code>) sin bajar la vista.",
        "steps_h2": "4 Claves para Dominar Cualquier Evento en Directo",
        "steps": [
            (
                "Marca tu escaleta con # Títulos o importa un .pptx",
                "Escribe # Apertura, # Entrega de Premios o [CUE: Cierre] en tu guion, o importa tu presentación .pptx para crear capítulos automáticamente con los títulos de cada diapositiva.",
            ),
            (
                "Usa la Vista Continua y salta en 1 toque",
                "Visualiza siempre los párrafos siguientes. Si decides acortar una intervención en vivo, toca el párrafo donde quieras retomar y la voz seguirá desde ahí.",
            ),
            (
                "Guarda un clicker Bluetooth estándar en el bolsillo",
                "Conecta cualquier mando Bluetooth HID (Logitech Spotlight, R500s, Kensington, Satechi). Avanza o retrocede párrafos sin mirar y pulsa la tecla de pantalla negra (B o .) para silenciar el seguimiento vocal cuando hable otro invitado.",
            ),
            (
                "Mantén postura abierta con Apple Watch Double Tap",
                "En Apple Watch Series 9+ y Ultra 2, junta índice y pulgar dos veces con una sola mano sin cruzar el brazo frente al cuerpo.",
            ),
        ],
        "tbl_h2": "VoxPresenter Escena Live frente a Teleprónteres Comunes y Tarjetas de Papel",
        "tbl_cols": [
            "Situación Real en Escenario",
            "VoxPresenter v1.0.33 (Escena Live)",
            "Apps Solo por Voz",
            "Temporizador Fijo y Papel",
        ],
        "tbl_rows": [
            (
                "Saltar un párrafo según la respuesta del público",
                "✓ Vista continua + toque directo al párrafo con resincronización vocal",
                "✗ Sin vista previa o pierde el hilo",
                "✗ El temporizador sigue corriendo solo",
            ),
            (
                "Cambio de orden de la escaleta en directo",
                "✓ Panel de marcadores # (y capítulos .pptx auto) en 1 toque",
                "✗ Scroll manual lento en mitad del acto",
                "✗ Buscar hojas sueltas en el atril",
            ),
            (
                "Copresentador hablando o sala muy ruidosa",
                "✓ Pausa en 1 toque o tecla B / . del clicker Bluetooth en el bolsillo",
                "✗ La voz del compañero puede mover tu texto",
                "No aplica (sin reconocimiento vocal)",
            ),
            (
                "Control manual sin mirar la pantalla",
                "✓ Clicker Bluetooth HID + Apple Watch Double Tap a 1 mano",
                "✗ Obliga a tocar el cristal del iPhone/iPad",
                "Mandos de velocidad imprecisos",
            ),
        ],
        "faqs": [
            (
                "¿Qué mandos o clickers Bluetooth funcionan con VoxPresenter en iPhone e iPad?",
                "Cualquier presentador Bluetooth compatible con perfil de teclado HID estándar en iOS e iPadOS funciona al instante (Logitech Spotlight, Logitech R500s, Satechi, Kensington). Las flechas avanzan o retroceden párrafos y la tecla B o . pausa o reanuda el seguimiento por voz.",
            ),
            (
                "¿Qué pasa si comparto escenario y mi compañero dice una frase de mi guion?",
                "Pulsa el botón ámbar Pausa en pantalla o la tecla B / . de tu clicker Bluetooth cuando cedas el turno. Tu guion quedará fijo en tu siguiente intervención hasta que vuelvas a activarlo.",
            ),
            (
                "¿Cómo creo marcadores de capítulos para una gala o congreso?",
                "Empieza cualquier línea con # seguido del título (# Bienvenida, # Panel Central) o importa un archivo PowerPoint (.pptx) para generar los capítulos automáticamente.",
            ),
        ],
    },
    "de": {
        "nav_label": "Live-Bühne & Clicker",
        "title": "Live-Bühnen-, Moderations- & Bluetooth-Clicker-Teleprompter für iPhone & iPad · VoxPresenter",
        "desc": "Entwickelt für Keynote-Speaker, Moderatoren und Events: kontinuierliche Fließtext-Vorschau, 1-Tipp #-Sprungmarken, Sprachpause bei Co-Moderation, Bluetooth-Clicker in der Tasche und einhändiger Apple Watch Double Tap.",
        "keywords": "Teleprompter mit Bluetooth Clicker iPhone iPad, Moderation Bühnen Teleprompter App, Kapitelmarken Regieplan Teleprompter, Spracherkennung pausieren Co-Moderator, Logitech Spotlight Teleprompter iOS",
        "eyebrow": "Ratgeber Live-Bühne, Event-Moderation & Bluetooth-Clicker",
        "h1": "Live-Bühnen- & Moderations-Teleprompter: #-Sprungmarken, Sprachpause & Bluetooth-Clicker auf iPhone & iPad",
        "lead": "Vor echtem Publikum läuft kein Abend starr nach Plan: Applaus dauert länger, ein Co-Moderator übernimmt das Mikrofon oder die Regie tauscht kurzfristig zwei Programmpunkte. So kombiniert VoxPresenter Offline-Sprachfluss mit sofortiger manueller Kontrolle.",
        "sum_h2": "Warum Profis auf der Bühne mehr als reinen Automatik-Scroll brauchen",
        "sum_p1": "<strong>Wo herkömmliche Teleprompter live scheitern:</strong> Einzelabsatz-Ansichten verbergen den kommenden Text bei spontanen Kürzungen, und ein dauerhaft aktives Mikrofon kann weiterspringen, wenn Ihr Co-Moderator spricht.",
        "sum_p2": "<strong>Der VoxPresenter v1.0.33 Live-Bühnen-Workflow:</strong> Lesen Sie vorausschauend in der <strong>kontinuierlichen Ansicht</strong>, springen Sie in <strong>1 Tipp zu jeder <code>#-Kapitelmarke</code></strong> mit sofortigem Sprach-Resync und nutzen Sie einen <strong>Bluetooth-Clicker in der Tasche</strong> zum Vor-/Zurückspringen oder zum Pausieren der Spracherkennung (Taste <code>B</code> / <code>.</code>).",
        "steps_h2": "4 Praxis-Schritte für maximale Live-Sicherheit",
        "steps": [
            (
                "Regieplan mit #-Marken oder .pptx-Kapiteln strukturieren",
                "Schreiben Sie # Begrüßung, # Ehrung oder [CUE: Finale] ins Skript oder importieren Sie eine .pptx-Datei, deren Folientitel automatisch als Kapitelmarken angelegt werden.",
            ),
            (
                "Kontinuierliche Vorschau nutzen & per Tipp springen",
                "Kommende Absätze bleiben stets sichtbar. Möchten Sie live abkürzen, tippen Sie einfach den gewünschten Absatz an und die Spracherkennung übernimmt exakt ab dort.",
            ),
            (
                "Bluetooth-Presenter blind in der Tasche nutzen",
                "Koppeln Sie jeden Standard-Bluetooth-HID-Clicker (Logitech Spotlight, R500s, Kensington, Satechi). Vor/Zurück schaltet Absätze, und die Blackout-Taste (B oder .) pausiert das Mikrofon bei Co-Moderation.",
            ),
            (
                "Offene Bühnenhaltung dank Apple Watch Double Tap",
                "Auf Apple Watch Series 9+ und Ultra 2 genügt ein einhändiger Doppeltipp mit Zeigefinger und Daumen, ohne den anderen Arm vor dem Körper zu kreuzen.",
            ),
        ],
        "tbl_h2": "VoxPresenter Live-Bühne im Vergleich zu Standard-Apps & Moderationskarten",
        "tbl_cols": [
            "Live-Situation auf der Bühne",
            "VoxPresenter v1.0.33 (Live-Bühne)",
            "Reine Sprach-Apps",
            "Starre Timer & Papierkarten",
        ],
        "tbl_rows": [
            (
                "Spontan einen Absatz kürzen",
                "✓ Fließtext-Vorschau + 1-Tipp-Sprung mit sofortigem Sprach-Resync",
                "✗ Keine Vorschau oder Verlust der Synchronisation",
                "✗ Timer läuft ungebremst weiter",
            ),
            (
                "Kurzfristige Änderung im Programmablauf",
                "✓ #-Kapitelliste (inkl. Auto-.pptx-Kapitel) in 1 Tipp",
                "✗ Hektisches Suchen und Wischen",
                "✗ Blättern in gedruckten Karten",
            ),
            (
                "Co-Moderator spricht oder lauter Saal",
                "✓ 1-Tipp Pause am Bildschirm ODER B / . Taste am Bluetooth-Clicker",
                "✗ Fremdstimmen können Text vorschieben",
                "Entfällt (keine Spracherkennung)",
            ),
            (
                "Blinde manuelle Steuerung ohne Hinsehen",
                "✓ Bluetooth-HID-Clicker + einhändiger Apple Watch Double Tap",
                "✗ Griff zum iPhone-/iPad-Display nötig",
                "Ungenaue Tempo-Regler",
            ),
        ],
        "faqs": [
            (
                "Welche Bluetooth-Clicker sind mit VoxPresenter auf iPhone und iPad kompatibel?",
                "Jeder Bluetooth-Presenter mit Standard-HID-Tastaturprofil für iOS und iPadOS funktioniert sofort ohne Zusatztreiber, darunter Logitech Spotlight, Logitech R500s, Satechi und Kensington. Vor/Zurück steuert Absätze, die Taste B oder . pausiert und startet die Spracherkennung.",
            ),
            (
                "Wie verhindere ich bei Doppelmoderation, dass mein Co-Moderator das Skript weiterschaltet?",
                "Tippen Sie auf die gelbe Pause-Taste im HUD oder drücken Sie blind die B / . Taste Ihres Bluetooth-Clickers in der Tasche, solange Ihr Gesprächspartner das Wort hat.",
            ),
            (
                "Wie lege ich Sprungmarken für eine Gala oder Konferenz an?",
                "Beginnen Sie eine Zeile mit # gefolgt vom Abschnittsnamen (z. B. # Eröffnung oder # Preisverleihung) oder importieren Sie eine PowerPoint-Datei (.pptx) für automatische Folienkapitel.",
            ),
        ],
    },
    "pt": {
        "nav_label": "Palco Live e Passador",
        "title": "Teleprompter de Palco Live, Mestre de Cerimônias e Passador Bluetooth no iPhone e iPad · VoxPresenter",
        "desc": "Criado para palestrantes, mestres de cerimônias (MC) e apresentadores de eventos: visão contínua, favoritos # de roteiro, pausa de voz em 1 toque para coapresentadores, passador Bluetooth de bolso e Apple Watch Double Tap.",
        "keywords": "teleprompter passador Bluetooth iPhone iPad, teleprompter mestre de cerimônias palco, favoritos capítulos teleprompter ao vivo, pausar voz coapresentador teleprompter, Logitech Spotlight teleprompter iOS",
        "eyebrow": "Guia Palco Live, Mestres de Cerimônias (MC) e Passadores Bluetooth",
        "h1": "Teleprompter de Palco Live: Favoritos #, Pausa de Voz e Passador Bluetooth no iPhone e iPad",
        "lead": "Diante de uma plateia ao vivo, o evento nunca segue um cronômetro rígido: aplausos se estendem, um coapresentador divide o microfone ou a produção altera a ordem dos blocos. Veja como o Modo Palco Live do VoxPresenter une voz offline e controle manual imediato.",
        "sum_h2": "Por que apresentadores de eventos precisam de mais do que rolagem automática",
        "sum_p1": "<strong>Onde teleprompters comuns falham no palco:</strong> ver apenas um parágrafo impede antecipar cortes conforme a reação do público, e o microfone sempre aberto pode avançar o texto se o coapresentador falar.",
        "sum_p2": "<strong>O fluxo Palco Live v1.0.33 do VoxPresenter:</strong> enxergue adiante na <strong>Visão Contínua</strong>, pule para qualquer <strong>favorito <code># Capítulo</code> em 1 toque</strong> ressincronizando a voz na hora, e leve um <strong>passador Bluetooth no bolso</strong> para avançar, voltar ou pausar a escuta de voz (tecla <code>B</code> / <code>.</code>) sem olhar para baixo.",
        "steps_h2": "4 Práticas para Eventos Ao Vivo Sem Imprevistos",
        "steps": [
            (
                "Marque seções com # Favoritos ou importe um .pptx",
                "Digite # Abertura, # Premiação ou [CUE: Encerramento] no roteiro, ou importe sua apresentação .pptx para transformar cada título de slide em capítulo automaticamente.",
            ),
            (
                "Leia em Visão Contínua e pule em 1 toque",
                "Veja sempre as próximas frases abaixo do bloco ativo. Precisa cortar um trecho ao vivo? Toque no parágrafo desejado e o rastreamento de voz retoma exatamente dali.",
            ),
            (
                "Use um passador Bluetooth padrão no bolso",
                "Pareie qualquer controle Bluetooth HID (Logitech Spotlight, R500s, Kensington, Satechi). Avance ou volte parágrafos sem olhar e aperte a tecla de tela preta (B ou .) para pausar a voz quando outro convidado falar.",
            ),
            (
                "Postura aberta com Apple Watch Double Tap",
                "No Apple Watch Series 9+ e Ultra 2, um toque duplo entre indicador e polegar avança com uma só mão sem cruzar o braço na frente do corpo.",
            ),
        ],
        "tbl_h2": "VoxPresenter Palco Live vs. Apps Comuns e Fichas de Papel",
        "tbl_cols": [
            "Situação Real no Palco",
            "VoxPresenter v1.0.33 (Palco Live)",
            "Apps Apenas por Voz",
            "Timer Fixo e Fichas Impressas",
        ],
        "tbl_rows": [
            (
                "Cortar um parágrafo conforme a energia da plateia",
                "✓ Visão contínua + toque direto no parágrafo com ressincronia de voz",
                "✗ Sem visão prévia ou perde o ponto",
                "✗ O timer continua correndo sozinho",
            ),
            (
                "Mudança na ordem do cerimonial ao vivo",
                "✓ Gaveta de favoritos # (e capítulos .pptx auto) em 1 toque",
                "✗ Rolagem manual demorada no palco",
                "✗ Embaralhar fichas de papel no púlpito",
            ),
            (
                "Coapresentador falando ou auditório barulhento",
                "✓ Pausa em 1 toque ou tecla B / . do passador Bluetooth no bolso",
                "✗ Fala do colega pode avançar seu roteiro",
                "Não se aplica (sem voz)",
            ),
            (
                "Controle manual discreto sem olhar para a tela",
                "✓ Passador Bluetooth HID + Apple Watch Double Tap de 1 mão",
                "✗ Obriga a tocar na tela do iPhone/iPad",
                "Controles de velocidade imprecisos",
            ),
        ],
        "faqs": [
            (
                "Quais passadores Bluetooth funcionam com o VoxPresenter no iPhone e iPad?",
                "Qualquer passador de slides Bluetooth compatível com teclado HID padrão no iOS e iPadOS funciona imediatamente (Logitech Spotlight, Logitech R500s, Satechi, Kensington). As setas avançam ou voltam parágrafos e a tecla B ou . pausa ou retoma o rastreamento de voz.",
            ),
            (
                "Como evitar que a voz do meu coapresentador avance o meu texto?",
                "Toque no botão âmbar Pausa no topo da tela ou pressione a tecla B / . do seu passador Bluetooth no bolso sempre que passar a palavra. O texto ficará travado na sua próxima fala até você retomar.",
            ),
            (
                "Como criar capítulos ou favoritos antes de uma cerimônia?",
                "Comece qualquer linha com # seguido do título (# Boas-vindas, # Homenagem) ou importe um arquivo PowerPoint (.pptx) para gerar os capítulos automaticamente.",
            ),
        ],
    },
}

out_code = (
    "# -*- coding: utf-8 -*-\n"
    '"""\n'
    "Localized bottom-of-funnel SEO & GEO authority guides for FR, EN, ES, DE, PT (v1.0.33):\n"
    "1. compare.html — Full 2026 Teleprompter Benchmark\n"
    "2. powerpoint-keynote-teleprompter.html — PowerPoint (.pptx) & Keynote Speaker Notes + Auto Chapters\n"
    "3. apple-watch-teleprompter-remote.html — 3-Mode Studio Noir Apple Watch + Double Tap\n"
    "4. youtube-studio-mirror-teleprompter.html — 45° Beam-Splitter Studio Mirror Rig Guide\n"
    "5. stage-emcee-bluetooth-clicker-teleprompter.html — Live Stage, Emcee, # Cue Sheet & Bluetooth Clickers\n"
    '"""\n\n'
    f"COMPARE_GUIDE = {pprint.pformat(COMPARE, width=140, sort_dicts=False)}\n\n"
    f"PPTX_GUIDE = {pprint.pformat(PPTX, width=140, sort_dicts=False)}\n\n"
    f"WATCH_GUIDE = {pprint.pformat(WATCH, width=140, sort_dicts=False)}\n\n"
    f"YOUTUBE_STUDIO_GUIDE = {pprint.pformat(YOUTUBE, width=140, sort_dicts=False)}\n\n"
    f"STAGE_EMCEE_GUIDE = {pprint.pformat(STAGE_EMCEE_GUIDE, width=140, sort_dicts=False)}\n"
)

# Clean docstring em-dashes too so zero em-dashes exist anywhere in data_guides.py!
out_code = out_code.replace("—", "-")
(SCRIPTS_DIR / "data_guides.py").write_text(out_code, encoding="utf-8")
print("✓ Upgraded data_guides.py with 5 localized guides and zero em-dashes!")
