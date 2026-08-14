---
layout: default
title: Guestbook
permalink: /cy/guestbook/
---

<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"> </script>

<steil>
corff, prif, h1, h2, h3, p, a, rhychwant, div, botwm {
    font-family: 'SUSE', sans-serif !pwysig;
}

h1, h2, h3 {
    ffont-teulu: 'Staatliches', sans-serif !important;
}

cyn, cod {
    ffont-teulu: 'JetBrains Mono', monospace !pwysig;
}

.blinking-cursor {
    ffont-pwysau: 800;
    lliw: var (--acen);
    animeiddiad: amrantiad 1s cam-diwedd anfeidrol;
}

@keyframes blink {
    50% { didreiddedd: 0; }
}

.hacker-btn {
    maint y ffont: 1.1rem;
    ffont-pwysau: 700;
    padin: 14px 28px;
    ffin: var solet 1px (--ffin);
    lliw: var (--testun);
    border-radiws: 12px;
    arddangos: inline-bloc;
    addurno testun: dim;
    cefndir: var(--nav-bg);
    hidlydd cefndir: niwlog(12px);
    -webkit-cefn-hidlo: aneglur(12px);
    cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    trawsnewid: pob un o'r 0.3s ciwbig-bezier(0.4, 0, 0.2, 1);
    testun-trawsnewid: priflythrennau;
    bylchau rhwng llythyrau: 1px;
    cyrchwr: pwyntydd;
}

[ data-theme = "tywyll"] .hacker-btn {
    cysgod bocs: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
}

.hacker-btn:hofran {
    lliw border: var (--acen);
    lliw: var (--acen);
    blwch-cysgod: 0 20px 25px -5px rgba(99, 102, 241, 0.2);
    trawsnewid: translateY(-2px);
    cefndir: rgba(99, 102, 241, 0.05);
}

.sign-form {
    uchafswm-lled: 500px;
    ymyl: 0 auto 40px awto;
    arddangos: fflecs;
    fflecs-cyfeiriad: colofn;
    bwlch: 15px;
    cefndir: var(--nav-bg);
    padin: 30px;
    radiws ffin: 16px;
    ffin: var solet 1px (--ffin);
    hidlydd cefndir: niwlog(12px);
    -webkit-cefn-hidlo: aneglur(12px);
    cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

[ data-theme = "tywyll"] .sign-form {
    cysgod blwch: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
}

mewnbwn .sign-form, .sign-form textarea {
    ffont-teulu: 'SUSE', sans-serif;
    cefndir: var(--bg-solid);
    ffin: var solet 1px (--ffin);
    lliw: var (--testun);
    padin: 14px;
    radiws ffin: 8px;
    maint y ffont: 1rem;
    pontio: border-lliw 0.3s rhwyddineb;
}

mewnbwn .sign-form:focus, .sign-form textarea:focus {
    amlinelliad: none;
    lliw border: var (--acen);
}

.carousel-lapiwr {
    sefyllfa: perthynas;
    lled: 100%;
    padin: 0 50px;
    blwch-sizing: border-box;
    defnyddiwr-dewis: dim;
}

.carousel-container {
    arddangos: fflecs;
    gorlif-x: auto;
    sgrolio-snap-type: x gorfodol;
    sgrolio-ymddygiad: llyfn;
    -webkit-gorlif-sgrolio: cyffwrdd;
    bwlch: 20px;
    padin: 10px 0 20px 0;
    bar sgrolio-lled: dim; 
}

.carousel-container::-webkit-scrollbar {
    arddangos: dim; 
}

.carousel-item {
    fflecs: 0 0 100%; 
    sgrolio-snap-align: canol;
    cefndir: var(--nav-bg);
    hidlydd cefndir: niwlog(12px);
    -webkit-cefn-hidlo: aneglur(12px);
    ffin: var solet 1px (--ffin);
    radiws ffin: 16px;
    padin: 40px 40px;
    blwch-sizing: border-box;
    cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    arddangos: fflecs;
    fflecs-cyfeiriad: colofn;
    cyfiawnhau-cynnwys: space-between;
    Isafswm uchder: 250px;
    pontio: ffin-lliw 0.3s rhwyddineb, trawsnewid rhwyddineb 0.3s, blwch-cysgod 0.3s rhwyddineb;
}

[ data-theme = "tywyll"] .carousel-item {
    cysgod bocs: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
}

.carousel-item: hofran {
    lliw border: var (--acen);
    trawsnewid: translateY(-2px);
    blwch-cysgod: 0 20px 25px -5px rgba(99, 102, 241, 0.2);
}

.nav-btn{
    sefyllfa: absoliwt;
    uchaf: 45%;
    trawsnewid: translateY(-50%);
    cefndir: var(--nav-bg);
    hidlydd cefndir: niwlog(12px);
    -webkit-cefn-hidlo: aneglur(12px);
    ffin: var solet 1px (--ffin);
    lliw: var (--testun);
    maint y ffont: 1.2rem;
    cyrchwr: pwyntydd;
    border-radiws: 12px;
    lled: 45px;
    uchder: 45px;
    z-mynegai: 10;
    arddangos: fflecs;
    alinio-eitemau: canol;
    cyfiawnhau-cynnwys: center;
    trawsnewid: pob un o'r 0.3s ciwbig-bezier(0.4, 0, 0.2, 1);
    cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

[ data-theme = "tywyll"] .nav-btn {
    cysgod bocs: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
}

.nav-btn:hofran {
    cefndir: rgba(99, 102, 241, 0.05);
    lliw: var (--acen);
    lliw border: var (--acen);
    blwch-cysgod: 0 10px 15px -3px rgba(99, 102, 241, 0.2);
    trawsnewid: translateY(-50%) translate(-2px, -2px);
}

#prevBtn {
    chwith: 0;
}

#nesafBtn {
    dde: 0;
}

.progress-lapper {
    sefyllfa: perthynas;
    uchder: 20px;
    ymyl-brig: 15px;
    arddangos: fflecs;
    alinio-eitemau: canol;
    cyfiawnhau-cynnwys: center;
    cyrchwr: pwyntydd;
}

.progress-track {
    width: 100%;
    height: 6px;
    background: var(--nav-bg);
    border: 1px solid var(--border);
    border-radius: 0;
    overflow: hidden;
    transition: opacity 0.3s ease;
}

.cynnydd-lenwi {
    uchder: 100%;
    lled: 0%;
    cefndir: var (--acen);
    trawsnewid-tarddiad: chwith;
}

.progress-fill.animate {
    animeiddiad: fillProgress 10s llinol ymlaen;
}

.progress-fill.paused {
    animeiddiad-chwarae-cyflwr: seibio;
}

@keyframes fillProgress {
    0% { lled: 0%; }
    100% { lled: 100%; }
}

.dangosydd wedi'i seibio {
    sefyllfa: absoliwt;
    maint y ffont: 0.85rem;
    ffont-pwysau: 700;
    lliw: var (--acen);
    testun-trawsnewid: priflythrennau;
    bylchau rhwng llythyrau: 2px;
    didreiddedd: 0;
    pontio: didreiddedd 0.3s rhwyddineb;
    arddangos: fflecs;
    alinio-eitemau: canol;
    digwyddiadau pwyntydd: dim;
    cefndir: var(--bg-solid);
    padin: 0 10px;
}

.carousel-wrapper.is-saib .progress-track {
    didreiddedd: 0.15;
}

.carousel-wrapper.is-saib .paused-indicator {
    didreiddedd: 1;
}

@cyfryngau (uchafswm-lled: 768px) {
    .carousel-lapiwr {
        padin: 0;
    }
    #prevBtn, #nextBtn {
        arddangos: dim; 
    }
    .carousel-item {
        fflecs: 0 0 90%; 
        sgrolio-snap-align: canol;
    }
    .carousel-container {
        padin: 10px 5% 20px 5%; 
    }
    .progress-lapper {
        padin: 0 5%;
    }
}
</style>

<div class="page-content" style="uch-lled: 800px; ymyl: 0 auto; padin-top: 20px;">
  
    <h1 style="color: var(--accent); text-align: center; maint y ffont: 2.2rem; pwysau ffont: 800; bylchau rhwng llythrennau: -1px; ymyl-gwaelod: 10px;">
        >_ Llyfr Gwesteion <span class="blinking-cursor">_</span>
    </h1>
  
    <p style="color: var(--text-muted); text-align: center; ymyl-gwaelod: 30px; maint y ffont: 1.05rem;">
        Negeseuon a chyfarchion gan ymwelwyr.
    </p>

<form id="ffurflen llyfr gwesteion" class="sign-form">
        <input type="text" id="name" placeholder="Angen enw">
        <textarea id="message" placeholder="Angen neges"></textarea>
        
        <div class="cf-turnstile" data-sitekey="0x4AAAAAAEEfCSzxCVuLiXl0" data-theme="auto" data-callback="unlockForm"></div>
        
        <button type="submit" id="submitBtn" class="hacker-btn" wedi'i analluogi>Llofnodi Llyfr Gwesteion</button>
        <div id="formStatus" style="display: none; text-align: center; font-weight: 700;"> </div>
    </form>

<div class="carousel-lapper">
        <botwm id="prevBtn" class="nav-btn">&#10094;</button>
        
        <div class="carousel-container" id="guestbook-carousel">
            <div class="carousel-item" style="cyfiawnhau-cynnwys: canol; alinio-eitemau: canol;">
                <p style="color: var(--text); font-size: 1.1rem;"> Cychwyn cysylltiad...</p>
            </div>
        </div>

        <button id="nextBtn" class="nav-btn">&#10095;</button>

<div class="progress-lapper">
            <div class="progress-track">
                <div class="progress-fill animate" id="progressBarFill"></div>
            </div>
            <div class="dangosydd wedi'i seibio">
                [ WEDI EI SEIB ]
            </div>
        </div>
    </div>
</div>

<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" gohirio async></script>
<script>
const supabaseUrl = ' https://hnyokpvurntvxvhdvwii.supabase.co ' ;
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhueW9rcHZ1cm50dnh2aGR2d2lpIiwicm9 sZSI6ImFub24iLCJpYXQiOjE3ODU2NzQ0MzEsImV4cCI6MjEwMTI1MDQzMX0.NZLDRNPtWYH-_cvDovXkwyrR-SiT9HqvYnlfT2VpEyo';
const supabaseClient = window.supabase.createClient(supabaseUrl, supabaseKey);

gadewch turnstileToken = "" ;
window.unlockForm = swyddogaeth (tocyn) {
    turnstileToken = tocyn;
    document.getElementById('submitBtn').disabled = ffug;
};

const container = document.getElementById('guestbook-carousel');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const wrapper = document.querySelector('.carousel-wrapper');
const fill = document.getElementById('progressBarFill');
const form = document.getElementById('llyfr gwesteion-ffurf');
const submitBtn = document.getElementById('submitBtn');
const formStatus = document.getElementById('formStatus');

gadewch isLockedPause = ffug;
gadewch i isScrolling;

swyddogaeth async loadGuestbook() {
    const { data , error } = aros am supabaseClient
        .o('llyfr gwesteion')
        .select('enw, neges, creu_at')
        .order ('creu_at', { esgynnol: ffug });

os (gwall) {
        container.innerHTML = `<div class="carousel-item" style="cyfiawnhau-cynnwys: canol; alinio-eitemau: canol;" <p style="color: red;"> Methwyd ag adalw cofnodion.</p></div>`;
        dychwelyd;
    }

container.innerHTML = '' ;

os (data.length === 0) {
        container.innerHTML = `<div class="carousel-item" style="cyfiawnhau-cynnwys: canol; alinio-eitemau: canol;" <p style="color: var(--text);">Ni chafwyd hyd i gofnodion.</p></div>`;
        dychwelyd;
    }

data.forEach(mynediad => {
        const dateStr = dyddiad newydd(entry.created_at).toLocaleDateString('en-US', {
            blwyddyn: 'rhifol',
            mis: 'hir',
            diwrnod: 'numeric'
        });

const itemDiv = document.createElement('div');
        itemDiv.className = 'carousel-item';
        
        const messageP = document.createElement('p');
        messageP.style.cssText = 'lliw: var(--text); maint y ffont: 1.1rem; ymyl-brig: 0; uchder llinell: 1.6; toriad gair: break-word;';
        messageP.textContent = `"${entry.message}"`;

const metaDiv = document.createElement('div');
        metaDiv.style.marginTop = '20px';

const nameP = document.createElement('p');
        nameP.style.cssText = 'lliw: var(--acen); ymyl-gwaelod: 0; ffont-pwysau: 800; testun-trawsnewid: priflythrennau; bylchau rhwng llythyrau: 1px;';
        nameP.textContent = `> ${entry.name}`;

        const dateSpan = document.createElement('span');
        dateSpan.style.cssText = 'color: var(--text-muted); font-size: 0.85rem; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase;';
        dateSpan.textContent = dateStr;

metaDiv.appendChild(enwP);
        metaDiv.appendChild(dateSspan);
        itemDiv.appendChild(messageP);
        itemDiv.appendChild(metaDiv);
        container.appendChild(itemDiv);
    });

resetAnimation();
}

form.addEventListener('cyflwyno', async(e) => {
    e.preventDefault();
    
    os (!turnstileToken) {
        dychwelyd;
    }

const name = document.getElementById('name').value.trim();
    const message = document.getElementById('message').value.trim();

os bydd (!enw || !neges) yn dychwelyd;

submitBtn.disabled = gwir;
    formStatus.style.display = 'bloc';
    formStatus.style.color = 'var(--text)';
    formStatus.textContent = 'Trosglwyddo...';

const { error } = aros am supabaseClient
        .o('llyfr gwesteion')
        .insert([{ enw, neges }]);

os (gwall) {
        formStatus.textContent = 'Methwyd y trosglwyddiad. Ceisiwch eto.';
        formStatus.style.color = 'coch';
        submitBtn.disabled = ffug;
    } arall {
        formStatus.textContent = 'Cofnod wedi'i atodi'n llwyddiannus.';
        formStatus.style.color = 'var(--acen)';
        ffurflen.reset();
        turnstileToken = "";
        ffenestr.turnstile.reset();
        aros llwythGuestbook();
        
        setTimeout(() => {
            formStatus.style.display = 'dim';
        }, 3000);
    }
});

swyddogaeth sgrolioNext() {
    os (container.scrollLeft + container.clientWidth >= container.scrollWidth - 10) {
        container.scrollTo({ chwith: 0, ymddygiad: 'llyfn' });
    } arall {
        container.scrollBy({ chwith: container.offsetWidth, ymddygiad: 'llyfn' });
    }
}

swyddogaeth scrollPrev() {
    os (container.scrollLeft <= 0) {
        container.scrollTo({ chwith: container.scrollWidth, ymddygiad: 'llyfn' });
    } arall {
        container.scrollBy({ chwith: -container.offsetWidth, ymddygiad: 'llyfn' });
    }
}

swyddogaeth resetAnimation() {
    fill.classList.remove('animate');
    llenwi gwag.offsetWidth; 
    fill.classList.add('animate');
}

seibiant ffwythiantAnimation() {
    fill.classList.add('saib');
    wrapper.classList.add('yn-saib');
}

ailddechrau swyddogaeth Animeiddiad() {
    os (isLockedPause) dychwelyd;
    fill.classList.remove('saib');
    wrapper.classList.remove('yn-saib');
}

fill.addEventListener('animationend', () => {
    sgroliwchNext();
    resetAnimation();
});

nextBtn.addEventListener('clic', (e) => {
    e.stopPropagation();
    sgroliwchNext();
    resetAnimation();
});

prevBtn.addEventListener('clic', (e) => {
    e.stopPropagation();
    sgrolioPrev();
    resetAnimation();
});

wrapper.addEventListener('llygoden', pauseAnimation);
wrapper.addEventListener('mouseleave', resumeAnimation);

wrapper.addEventListener('clic', () => {
    isLockedPause = !isLockedPause;
    os (isLockedPause) {
        saibAnimation();
    } arall {
        ailddechrauAnimeiddio();
    }
});

container.addEventListener( 'scroll', () => {
    window.clearTimeout(isScrolling);
    saibAnimation();
    isScrolling = setTimeout(() => {
        ailddechrauAnimeiddio();
    }, 150) ;
}, { goddefol: true });

loadGuestbook();
</script>