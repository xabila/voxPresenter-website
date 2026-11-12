(function(){
    const picker = document.getElementById('langPicker');
    const menu = document.getElementById('langMenu');
    const btn = document.getElementById('langPickerBtn');
    if (btn && picker && menu) {
        btn.addEventListener('click', function(e){
            e.stopPropagation();
            const isOpen = picker.classList.toggle('open');
            menu.style.display = isOpen ? 'flex' : 'none';
            btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        });
        document.addEventListener('click', function(e){
            if (!picker.contains(e.target)) {
                picker.classList.remove('open');
                menu.style.display = 'none';
                btn.setAttribute('aria-expanded', 'false');
            }
        });
    }

    const navbar = document.getElementById('navbar');
    const stickyBar = document.getElementById('stickyInstallBar');
    const downloadSec = document.getElementById('download');
    function onScroll() {
        const y = window.scrollY || 0;
        if (navbar) navbar.classList.toggle('scrolled', y > 20);
        if (stickyBar) {
            if (y <= 360) {
                stickyBar.classList.remove('visible');
            } else {
                let hideNearCta = false;
                if (downloadSec) {
                    const r = downloadSec.getBoundingClientRect();
                    hideNearCta = r.top < window.innerHeight - 40 && r.bottom > 40;
                }
                stickyBar.classList.toggle('visible', !hideNearCta);
            }
        }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    const mirrorImg = document.getElementById('mirrorDemoImg');
    const mirrorText = document.getElementById('mirrorStatusText');
    const mirrorBtns = document.querySelectorAll('.btn-mirror-toggle');
    if (mirrorImg && mirrorBtns.length) {
        mirrorBtns.forEach(function(b){
            b.addEventListener('click', function(){
                const mode = b.getAttribute('data-mode');
                mirrorBtns.forEach(function(x){ x.classList.toggle('active', x === b); });
                if (mode === 'vertical') {
                    mirrorImg.style.transform = 'scale(1, -1)';
                    if (mirrorText) mirrorText.textContent = mirrorImg.getAttribute('data-lbl-vertical') || '';
                } else if (mode === 'horizontal') {
                    mirrorImg.style.transform = 'scale(-1, 1)';
                    if (mirrorText) mirrorText.textContent = mirrorImg.getAttribute('data-lbl-horizontal') || '';
                } else {
                    mirrorImg.style.transform = 'scale(1, 1)';
                    if (mirrorText) mirrorText.textContent = mirrorImg.getAttribute('data-lbl-normal') || '';
                }
            });
        });
    }

    const calcInput = document.getElementById('calcInput');
    const outWords = document.getElementById('calcWords');
    const outNat = document.getElementById('calcNatural');
    const outCalm = document.getElementById('calcCalm');
    const outFast = document.getElementById('calcFast');
    const outSlides = document.getElementById('calcSlides');
    const presetBtns = document.querySelectorAll('.calc-preset-btn');

    function fmtTime(words, wpm) {
        if (!words) return '0:00';
        const totalSec = Math.max(1, Math.round((words / wpm) * 60));
        const m = Math.floor(totalSec / 60);
        const s = totalSec % 60;
        return m + 'm ' + (s < 10 ? '0' : '') + s + 's';
    }

    function updateCalc(overrideWords) {
        let words = 0;
        if (typeof overrideWords === 'number') {
            words = overrideWords;
        } else if (calcInput) {
            const trimmed = calcInput.value.trim();
            words = trimmed ? trimmed.split(/\s+/).length : 0;
        }
        if (outWords) outWords.textContent = String(words);
        if (outNat) outNat.textContent = fmtTime(words, 135);
        if (outCalm) outCalm.textContent = fmtTime(words, 110);
        if (outFast) outFast.textContent = fmtTime(words, 160);
        if (outSlides) {
            const slides = words > 0 ? Math.max(1, Math.round((words / 135) / 1.5)) : 0;
            outSlides.textContent = String(slides);
        }
    }

    if (calcInput) {
        calcInput.addEventListener('input', function(){
            presetBtns.forEach(function(p){ p.classList.remove('active'); });
            updateCalc();
        });
        presetBtns.forEach(function(p){
            p.addEventListener('click', function(){
                presetBtns.forEach(function(x){ x.classList.toggle('active', x === p); });
                const target = parseInt(p.getAttribute('data-words') || '0', 10);
                if (target > 0) updateCalc(target);
            });
        });
        updateCalc();
    }
})();
