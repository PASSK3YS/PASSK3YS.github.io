---
layout: doc
title: Basic Standard Notes theme template
description: A Standard Notes theme CSS template you can use.
category: Standard Notes
image: https://kieran.colfer.net/assets/docs-thumbnail.png
---

Mae croeso i chi gopïo ac addasu'r templed CSS hwn ar gyfer eich thema Nodiadau Safonol eich hun.

'' css
:gwraidd
  {/* =======================================================
     1. diffiniadau palet craidd
     Diffiniwch eich lliwiau amrwd yma. Gweddill y thema
     cyfeiriwch at y newidynnau hyn.
     ======================================================= */

/* Cefndir Cysgodion (Ysgafnaf i Tywyllaf ar gyfer Modd Golau) */
  -- c - bg - deep: #ffffff ;/* Prif faes cynnwys/cefndir Golygydd */
  -- c - bg - sidebar: # f7f9f8 ;/* Sidebar / Tag rhestr cefndir */
  -- c - bg - active: # eef3f1;    /* Eitem a ddewiswyd/Cefndir cyflwr gweithredol */

/* Testun a Chysgodion Acen (Tywyllaf i Ysgafnaf ar gyfer Modd Golau) */
  -- c - mint - bright: # 153826;  /* Testun cyferbyniad uchel (Penawdau, Teitlau gweithredol) */
  -- c - mint - mun: # 456e5a;   /* Testun corff safonol/ Eiconau */
  -- c - mint - dim: # a8c2b6; /* Deiliaid lleoedd/Testun cynnil/ Bariau sgrolio */
  -- border: # e1e8e5 ;/* Rhannau a borderi */

/* Lliwiau Statws Swyddogaethol */
  -- c -anger: # d32f2f ;/* Mae gwall yn nodi / Dileu botymau */
  -- c - rhybuddio: # 00796b;      /* Mae rhybudd yn nodi */

/* =======================================================
     2. METADATA
     ======================================================= THEMA */
  -- sn - stylekit - theme - type: light ;/* Rhaid iddo fod yn 'ysgafn' neu'n 'dywyll '*/
  -- sn - stylekit - theme - name:sol - mint - refined;

/* =======================================================
     3. MAPIO RHYNGWLAD APP
     Mapio'r palet craidd i'r prif gydrannau rhyngwyneb.
     ======================================================= */

/* Prif Cais Shell (Paneli, Rhestrau) */
  -- sn - stylekit - background - color: var (-- c - bg - deep);
  -- sn - stylekit - preground - color: var (-- c - mint - mun);
  -- sn - stylekit border - color:VAR (-- border);
  -- sn - stylekit - shadeow- color: var (-- border);

/* Cyferbyniad Uchel/Gwladwriaethau Gweithredol (ee, Hofran neu Ddewis) */
  -- sn - stylekit contrast - background - color: var (-- c - bg - active);
  -- sn - stylekit contrast -foreground - color: var (-- c - mint - bright);
  -- sn - stylekit contrast border - color: var (-- border);

/* Manylebau Bar Ochr (panel Leftmost fel arfer) */
  -- sn - stylekit - secondary - background - color: var (-- c - bg - sidebar);
  -- sn - stylekit - secondary -foreground - color: var (-- c - mint - mun);
  -- sn - stylekit - secondary border - color: var (-- border);

/* Y stribed llywio tenau ar y chwith pell */
  -- navigation - item - selected - background - color: var (-- c - bg - active);

/* =======================================================
     4. Arddulliau penodol golygydd
     Yn benodol ar gyfer yr ardal ysgrifennu nodiadau.
     ======================================================= */
  -- sn - stylekit - editor - background - color: var (-- c - bg - deep);
  -- sn - stylekit - editor -foreground - color: var (-- c - mint - bright); /* Prif Lliw Teipio */
  -- sn - stylekit - paragraph - text - color: var (-- c - mint - muted);

/* =======================================================
     5. Adborth a rhybuddion UI
     Botymau, Toast, a dangosyddion Statws     ======================================================= */

  /* Negeseuon Niwtral / Gwybodaeth */
  -- sn - stylekit - niwtral - color: var (-- c - mint - mun);
  -- sn - stylekit - niwtral - cyferbyniad - lliw: gwyn; /* Lliw testun ar ben niwtral */

-- sn - stylekit - info - color: var (-- c - mint - mun);
  -- sn - stylekit - info - contrast - color: gwyn;
  -- sn - stylekit - info - backdrop - color: var (-- c - bg - active);

/* Negeseuon llwyddiant */
  -- sn - stylekit - success -color:VAR (-- c - mint - mun);
  -- sn - stylekit - success - contrast - color: gwyn;

/* Negeseuon rhybuddio */
  -- sn - stylekit - warning - color: var (-- c - warning);
  -- sn - stylekit - warning - contrast - color: gwyn;

/* Negeseuon Perygl / Gwall */
  -- sn - stylekit -anger - color: var (-- c -anger);
  -- sn - stylekit - danger contrast - color: gwyn;

/* =======================================================
     6. mewnbynnau a bariau sgrolio
     ======================================================= */
  /* Ffurflen Mewnbynnau (Bariau chwilio, golygiadau teitl) */
  -- sn - stylekit - input - placeholder - color: var (-- c - mint - dim);
  -- sn - stylekit - input border - color: var (-- c - mint - dim);

/* Lliwio Bar Sgrolio Safonol */
  -- sn - stylekit - scrollbar - thumb - color: var (-- c - mint - dim);
  -- sn - stylekit - scrollbar - track border - color: tryloyw;

/* =======================================================
     7. Lliwiau goddefol a chyfleustodau
     Defnyddir ar gyfer eiconau, rhanwyr, ac elfennau cynnil     ======================================================= .*

  -- sn - stylekit - passive - color -0: var (-- c - mint - muted); /* Eiconau aml */
  -- sn - stylekit - passive - color -1: var (-- c - mint - mun);
  -- sn - stylekit - passive - color -3: var (-- border);

-- sn - stylekit - passive - color -4: var (-- c - bg - active);

* Defnyddir ar gyfer cylchoedd ffocws neu uchafbwyntiau cynnil.
     (Cyfrifwyd fel: Gwyrdd tywyll gyda didreiddedd isel) */
  -- sn - stylekit - passive - color -4 - opacity - variant: rgba(21, 56, 38, 0.1);

-- sn - stylekit - passive - color -5: var (-- c - bg -
deep);}

/* =======================================================
   8. DERBYNIADAU CYFANSWM
   Mae CSS penodol yn tweaks ar gyfer elfennau nad ydynt yn defnyddio newidynnau.
   ======================================================= */

/* Lliwio'r llinell Rheol Llorweddol yn y Golygydd Bloc */
# blociau - golygydd hr:ar ôl {
  cefndir - lliw: var(-- c - mint -
dim);}

/* Styling Bar Sgrolio Webkit (Chrome/Edge/App Penbwrdd) */
:- webkit -scrollbar {
    lled: 8px;
    uchder: 8px;
    lliw cefndir: tryloyw;}

::- webkit - scrollbar- bawd {
    cefndir - lliw: var (--c - mint - dim);
    border - radius: 4px;}

```