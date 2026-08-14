---
layout: doc
title: Basic Standard Notes theme template
description: A Standard Notes theme CSS template you can use.
category: Standard Notes
image: https://kieran.colfer.net/assets/docs-thumbnail.png
---

Mae croeso i chi gopïo ac addasu'r templed CSS hwn ar gyfer eich thema Nodiadau Safonol eich hun.

``` css
: gwraidd {
  /* ===========================================
     1. DIFFINIADAU PALET CRAIDD
     Diffiniwch eich lliwiau amrwd yma. Gweddill y thema
     yn cyfeirio at y newidynnau hyn.
     ======================================================

/* Arlliwiau Cefndir (Yr Ysgafn i'r Tywyllaf ar gyfer Modd Golau) */
  --c-bg-dwfn: #ffffff;      /* Prif faes cynnwys / cefndir golygydd */
  --c-bg-bar ochr: #f7f9f8;   /* Bar Ochr / Cefndir rhestr Tag */
  --c-bg-weithredol: #eef3f1;    /* Eitem a ddewiswyd / Cefndir cyflwr gweithredol */

/* Arlliwiau Testun ac Acen (Tywyllaf i Ysgafnaf ar gyfer Modd Ysgafn) */
  --c-mint-llachar: #153826;  /* Testun cyferbyniad uchel (Penawdau, Teitlau Actif) */
  --c-mint-tawel: #456e5a;   /* Testun corff safonol / Eiconau */
  --c-mint-dim: #a8c2b6;     /* Dalfannau / Testun cynnil / Barrau sgrolio */
  --c-ffin: #e1e8e5;       /* Rhanwyr a borderi */

/* Lliwiau Statws Swyddogaethol */
  --c-perygl: #d32f2f;       /* Gwall yn nodi / Dileu botymau */
  --c-rhybudd: #00796b;      /* Cyflyrau rhybudd */

/* ===========================================
     2. METADATA THEMA
     ======================================================
  --sn-stylekit-thema-math: golau; /* Rhaid bod yn 'ysgafn' neu'n 'dywyll' */
  --sn-stylekit-theme-name: light-mint-fined;

/* ===========================================
     3. MAPIO RHYNGWYNEB APP
     Mapio'r palet craidd i'r prif gydrannau UI.
     ======================================================

/* Cragen Prif Gais (Paneli, Rhestrau) */
  --sn-stylekit-background-color: var(--c-bg-dwfn);
  --sn-stylekit-blaendir-lliw: var(--c-mint-muted);
  --sn-stylekit-border-color: var(--c- border);
  --sn-stylekit-cysgod-lliw: var(--c-ffin);

/* Cyferbyniad Uchel / Cyflyrau Gweithredol (e.e., Hofran neu Dethol) */
  --sn-stylekit-cyferbyniad-cefndir-lliw: var(--c-bg-active);
  --sn-stylekit-cyferbyniad-blaendir-lliw: var(--c-mint-bright);
  --sn-stylekit-cyferbyniad-ffin-lliw: var(--c-ffin);

/* Manylion y Bar Ochr (Panel mwyaf chwith fel arfer) */
  --sn-stylekit-uwchradd-cefndir-lliw: var (--c-bg-bar ochr);
  --sn-stylekit-uwchradd-blaendir-lliw: var(--c-mint-muted);
  --sn-stylekit-uwchradd-ffin-lliw: var(--c-ffin);

/* Y stribed llywio tenau ar y chwith eithaf */
  --llywio-eitem-dewis-cefndir-lliw: var(--c-bg-active);

/* ===========================================
     4. ARDDULLIAU PENODOL I'R GOLYGYDD
     Lliwiau yn benodol ar gyfer yr ardal ysgrifennu nodiadau.
     ======================================================
  --sn-stylekit-golygydd-cefndir-lliw: var(--c-bg-dwfn);
  --sn-stylekit-golygydd-blaendir-lliw: var(--c-mint-bright); /* Prif Lliw Teipio */
  --sn-stylekit-paragraff-testun-lliw: var(--c-mint-muted);

/* ===========================================
     5. ADBORTH UI & RHYBUDDION
     Botymau, Tostau, a Dangosyddion Statws.
     ======================================================
  /* Negeseuon niwtral / gwybodaeth */
  --sn-stylekit-niwtral-lliw: var(--c-mint-muted);
  --sn-stylekit-niwtral-cyferbyniad-lliw: gwyn; /* Lliw testun ar ben niwtral */

--sn-stylekit-info-color: var(--c-mint-muted);
  --sn-stylekit-info-cyferbyniad-lliw: gwyn;
  --sn-stylekit-info-backdrop-color: var(--c-bg-active);

/* Negeseuon llwyddiant */
  --sn-stylekit-llwyddiant-lliw: var(--c-mint-muted);
  --sn-stylekit-llwyddiant-cyferbyniad-lliw: gwyn;

/* Negeseuon rhybudd */
  --sn-stylekit-rhybudd-lliw: var(--c-rhybudd);
  --sn-stylekit-rhybudd-cyferbyniad-lliw: gwyn;

/* Negeseuon Perygl / Gwall */
  --sn-stylekit-perygl-lliw: var(--c-perygl);
  --sn-stylekit-perygl-cyferbyniad-lliw: gwyn;

/* ===========================================
     6. MEWNBWN A SCROLIAU
     ======================================================
  /* Mewnbynnau Ffurflen (Bariau chwilio, golygiadau teitl) */
  --sn-stylekit-input-placeholder-color: var(--c-mint-dim);
  --sn-stylekit-mewnbwn-ffin-lliw: var(--c-mint-dim);

/* Lliwio bar sgrolio safonol */
  --sn-stylekit-scrollbar-thumb-color: var(--c-mint-dim);
  --sn-stylekit-scrollbar-track-border-color: tryloyw;

/* ===========================================
     7. LLIWIAU Goddefol & UTILITY
     Defnyddir ar gyfer eiconau, rhanwyr, ac elfennau cynnil.
     ======================================================
  --sn-stylekit-goddefol-lliw-0: var(--c-mint-muted); /* Eiconau yn aml */
  --sn-stylekit-goddefol-lliw-1: var(--c-mint-muted);
  --sn-stylekit-goddefol-lliw-3: var(--c-ffin);

--sn-stylekit-goddefol-lliw-4: var(--c-bg-active);

/* Defnyddir ar gyfer cylchoedd ffocws neu uchafbwyntiau cynnil.
     (Wedi'i gyfrifo fel: Gwyrdd tywyll gyda didreiddedd isel) */
  --sn-stylekit-goddefol-lliw-4-anhryloywder-amrywiad: rgba(21, 56, 38, 0.1);

--sn-stylekit-goddefol-lliw-5: var(--c-bg-dwfn);
}

/* ===========================================
   8. GORCHYMYN CYDRANNOL
   Tweaks CSS penodol ar gyfer elfennau nad ydynt yn defnyddio newidynnau.
   ======================================================

/* Lliwio'r llinell Rheol Llorweddol yn y Golygydd Bloc */
#blocks-golygydd awr: ar ôl {
  lliw cefndir: var (--c-mint-dim);
}

/* Steilio Bar Sgrolio Webkit (Chrome/Edge/Desktop App) */
::-webkit-scrollbar {
    lled: 8px;
    uchder: 8px;
    cefndir-lliw: tryloyw;
}
::-webkit-scrollbar-thumb {
    lliw cefndir: var (--c-mint-dim);
    border-radiws: 4px;
}```