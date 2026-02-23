---
layout: default
title: Basic Standard Notes theme template
description: A Standard Notes theme CSS template you can use.
category: Standard Notes
---

# Basic Standard Notes theme template

Feel free to copy and modify this CSS template for your own Standard Notes theme.

```css
:root {
  /* =======================================================
     1. CORE PALETTE DEFINITIONS
     Define your raw colors here. The rest of the theme
     references these variables.
     ======================================================= */

  /* Background Shades (Lightest to Darkest for Light Mode) */
  --c-bg-deep: #ffffff;      /* Main content area / Editor background */
  --c-bg-sidebar: #f7f9f8;   /* Sidebar / Tag list background */
  --c-bg-active: #eef3f1;    /* Selected item / Active state background */

  /* Text & Accent Shades (Darkest to Lightest for Light Mode) */
  --c-mint-bright: #153826;  /* High contrast text (Headers, Active titles) */
  --c-mint-muted: #456e5a;   /* Standard body text / Icons */
  --c-mint-dim: #a8c2b6;     /* Placeholders / Subtle text / Scrollbars */
  --c-border: #e1e8e5;       /* Dividers and borders */

  /* Functional Status Colors */
  --c-danger: #d32f2f;       /* Error states / Delete buttons */
  --c-warning: #00796b;      /* Warning states */


  /* =======================================================
     2. THEME METADATA
     ======================================================= */
  --sn-stylekit-theme-type: light; /* Must be 'light' or 'dark' */
  --sn-stylekit-theme-name: light-mint-refined;


  /* =======================================================
     3. APP INTERFACE MAPPING
     Mapping the core palette to the main UI components.
     ======================================================= */

  /* Main Application Shell (Panels, Lists) */
  --sn-stylekit-background-color: var(--c-bg-deep);
  --sn-stylekit-foreground-color: var(--c-mint-muted);
  --sn-stylekit-border-color: var(--c-border);
  --sn-stylekit-shadow-color: var(--c-border);

  /* High Contrast / Active States (e.g., Hovering or Selected) */
  --sn-stylekit-contrast-background-color: var(--c-bg-active);
  --sn-stylekit-contrast-foreground-color: var(--c-mint-bright);
  --sn-stylekit-contrast-border-color: var(--c-border);

  /* Sidebar Specifics (Leftmost panel usually) */
  --sn-stylekit-secondary-background-color: var(--c-bg-sidebar);
  --sn-stylekit-secondary-foreground-color: var(--c-mint-muted);
  --sn-stylekit-secondary-border-color: var(--c-border);

  /* The thin navigation strip on the far left */
  --navigation-item-selected-background-color: var(--c-bg-active);


  /* =======================================================
     4. EDITOR SPECIFIC STYLES
     Colors specifically for the note-writing area.
     ======================================================= */
  --sn-stylekit-editor-background-color: var(--c-bg-deep);
  --sn-stylekit-editor-foreground-color: var(--c-mint-bright); /* Main Typing Color */
  --sn-stylekit-paragraph-text-color: var(--c-mint-muted);


  /* =======================================================
     5. UI FEEDBACK & ALERTS
     Buttons, Toasts, and Status indicators.
     ======================================================= */
  /* Neutral / Info messages */
  --sn-stylekit-neutral-color: var(--c-mint-muted);
  --sn-stylekit-neutral-contrast-color: white; /* Text color on top of neutral */

  --sn-stylekit-info-color: var(--c-mint-muted);
  --sn-stylekit-info-contrast-color: white;
  --sn-stylekit-info-backdrop-color: var(--c-bg-active);

  /* Success messages */
  --sn-stylekit-success-color: var(--c-mint-muted);
  --sn-stylekit-success-contrast-color: white;

  /* Warning messages */
  --sn-stylekit-warning-color: var(--c-warning);
  --sn-stylekit-warning-contrast-color: white;

  /* Danger / Error messages */
  --sn-stylekit-danger-color: var(--c-danger);
  --sn-stylekit-danger-contrast-color: white;


  /* =======================================================
     6. INPUTS & SCROLLBARS
     ======================================================= */
  /* Form Inputs (Search bars, title edits) */
  --sn-stylekit-input-placeholder-color: var(--c-mint-dim);
  --sn-stylekit-input-border-color: var(--c-mint-dim);

  /* Standard Scrollbar coloring */
  --sn-stylekit-scrollbar-thumb-color: var(--c-mint-dim);
  --sn-stylekit-scrollbar-track-border-color: transparent;


  /* =======================================================
     7. PASSIVE & UTILITY COLORS
     Used for icons, dividers, and subtle elements.
     ======================================================= */
  --sn-stylekit-passive-color-0: var(--c-mint-muted); /* Often icons */
  --sn-stylekit-passive-color-1: var(--c-mint-muted);
  --sn-stylekit-passive-color-3: var(--c-border);

  --sn-stylekit-passive-color-4: var(--c-bg-active);

  /* Used for focus rings or subtle highlights.
     (Calculated as: A dark green with low opacity) */
  --sn-stylekit-passive-color-4-opacity-variant: rgba(21, 56, 38, 0.1);

  --sn-stylekit-passive-color-5: var(--c-bg-deep);
}


/* =======================================================
   8. COMPONENT OVERRIDES
   Specific CSS tweaks for elements that don't use variables.
   ======================================================= */

/* Coloring the Horizontal Rule line in the Block Editor */
#blocks-editor hr:after {
  background-color: var(--c-mint-dim);
}

/* Webkit Scrollbar Styling (Chrome/Edge/Desktop App) */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
    background-color: transparent;
}
::-webkit-scrollbar-thumb {
    background-color: var(--c-mint-dim);
    border-radius: 4px;
}
```