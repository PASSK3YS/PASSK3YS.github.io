---
layout: default
title: Contact
permalink: /cy/contact/
---

<div class="bio-container"><div class="bio-text"><h1 style="margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px;">Cysylltwch â<span class="blinking-cursor">_</span></h1><p style="font-size: 1.05rem; opacity: 0.9; margin: 0;">Gallwch chi fy nghyrraedd gan ddefnyddio'r canlynol ...</p></div></div>

<div class="unified-card">

<div class="unified-row interactive-row"><h3 class="soft-header">>_ E-bost</h3><div style="display: flex; flex-direction: column; justify-content: center;"><a href="mailto:hi@colfer.net" class="directory-interactive-text">hi@colfer.net</a><p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 15px; margin-bottom: 0; line-height: 1.4;">Os ydych chi'n defnyddio Proton Mail, bydd pob cyfathrebiad e-bost yn cael ei amgryptio o'r dechrau i'r diwedd.</p></div></div>

<div class="unified-row interactive-row"><h3 class="soft-header">> _ Sgwrs Ddiogel</h3><div style="display: flex; flex-direction: column; justify-content: center;">Signal<a href="https://signal.org" target="_blank" class="directory-interactive-text"></a><p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 15px; margin-bottom: 0; line-height: 1.4;">Cysylltiadau dibynadwy yn unig.</p></div></div>

<div class="unified-row"><h3 class="soft-header">> _ Cymuned Discord</h3><div class="gamertag-list" style="display: flex; gap: 30px; align-items: center; flex-wrap: wrap;"><div style="display: flex; align-items: center; gap: 10px;"><span class="gamertag-label">Proton</span><a href="https://discord.com/invite/proton" target="_blank" class="directory-interactive-text">Ymunwch â Gweinydd</a></div><div style="display: flex; align-items: center; gap: 10px;">Nodiadau Safonol<span class="gamertag-label"></span><a href="https://discord.com/invite/fxjJFxkRkY" target="_blank" class="directory-interactive-text">Ymunwch â Gweinydd</a></div></div></div>

</div>

<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">

<style>

corff, prif, p, a, rhychwant, div, botwm {
    ffont-teulu: 'SUSE', 'JetBrains Mono', system-ui, -apple-system, sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Staatliches', 'SUSE', sans-serif !pwysig;
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

.bio-gynhwysydd {
    arddangos: fflecs;
    alinio-eitemau: canol;
    bwlch: 30px;
    ymyl-gwaelod: 40px;
}

.bio-destun {
    arddangos: fflecs;
    fflecs-cyfeiriad: colofn;
}

.unified-card {
    cefndir: var(--nav-bg);
    hidlydd cefndir: niwlog(12px);
    -webkit-cefn-hidlo: aneglur(12px);
    radiws ffin: 16px;
    arddangos: fflecs;
    fflecs-cyfeiriad: colofn;
    ffin: var solet 1px (--ffin);
    cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    gorlif: cudd;
}

[ data-theme = "tywyll"] .unified-card {
    ffin: var solet 1px (--ffin);
    cysgod bocs: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
}

.unified-res {
    padin: 30px 34px;
    gwaelod ymyl: var doriad 1px (--ffin);
    arddangos: grid;
    grid-templed-colofnau: 240px 1fr;
    alinio-eitemau: canol;
    pontio: cefndir-lliw 0.3s rhwyddineb, border-lliw 0.3s rhwyddineb;
    border-chwith: 6px solet tryloyw;
}

[ data-theme = "tywyll"] .unified-row {
    pontio: cefndir-lliw 0.3s rhwyddineb, border-lliw 0.3s rhwyddineb, blwch-cysgod 0.3s rhwyddineb;
}

.unified-res: last-plentyn {
    border-gwaelod: dim;
}

.unified-row.interactive-row {
    cyrchwr: pwyntydd;
}

.unified-row.interactive-row:hover {
    lliw cefndir: rgba(99, 102, 241, 0.05);
    lliw border-chwith: var (--acen);
}

[data-theme="tywyll"] .unified-row.interactive-row:hover {
    lliw cefndir: rgba(99, 102, 241, 0.1);
    lliw border-chwith: var (--acen);
    trawsnewid: cyfieithu (-2px, -2px);
    blwch-cysgod: 0 10px 15px -3px rgba(99, 102, 241, 0.2);
}

.interactive-row:hover .directory-interactive-text {
    lliw: var (--acen);
}

pennyn .soft {
    maint y ffont: 0.85rem;
    testun-trawsnewid: priflythrennau;
    bylchau rhwng llythyrau: 1px;
    lliw: var (--testun-tewi);
    ymyl: 0;
    ffont-pwysau: 700;
    font-family: 'Staatliches', 'SUSE', sans-serif !pwysig;
}

.directory-interactive-text {
    maint y ffont: 1.1rem;
    ffont-pwysau: 800;
    lliw: var (--testun);
    addurno testun: dim;
    pontio: lliw 0.3s rhwyddineb;
}

.directory-interactive-text:hofran {
    lliw: var (--acen);
    testun-addurn: tanlinellu;
}

.gamertag-label {
    maint y ffont: 0.85rem;
    lliw: var (--testun-tewi);
    testun-trawsnewid: priflythrennau;
    ffont-pwysau: 700;
    bylchau rhwng llythyrau: 0.5px;
}

.gamertag-rhestr a {
    lliw: var (--testun);
    addurno testun: dim;
    ffont-pwysau: 800;
    pontio: lliw 0.3s rhwyddineb;
    maint y ffont: 1.1rem;
}

.gamertag-list a:hofran {
    lliw: var (--acen);
}

@cyfryngau (uchafswm lled: 850px) {
    .unified-res {
        grid-templed-colofnau: 1fr;
        bwlch: 15px;
        padin: 25px 14px;
    }
}</style>