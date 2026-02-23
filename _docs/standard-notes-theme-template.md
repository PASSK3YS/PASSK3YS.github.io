---
layout: default
title: Basic Standard Notes theme template
description: A Standard Notes theme CSS template you can use.
category: Standard Notes
---

Feel free to copy and modify this CSS template for your own Standard Notes theme.

```css
:root {
  --c-bg-deep: #ffffff;
  --c-bg-sidebar: #f7f9f8;
  --c-bg-active: #eef3f1;

  --c-mint-bright: #153826;
  --c-mint-muted: #456e5a;
  --c-mint-dim: #a8c2b6;
  --c-border: #e1e8e5;

  --c-danger: #d32f2f;
  --c-warning: #00796b;

  --sn-stylekit-theme-type: light;
  --sn-stylekit-theme-name: light-mint-refined;

  --sn-stylekit-background-color: var(--c-bg-deep);
  --sn-stylekit-foreground-color: var(--c-mint-muted);
  --sn-stylekit-border-color: var(--c-border);
  --sn-stylekit-shadow-color: var(--c-border);

  --sn-stylekit-contrast-background-color: var(--c-bg-active);
  --sn-stylekit-contrast-foreground-color: var(--c-mint-bright);
  --sn-stylekit-contrast-border-color: var(--c-border);

  --sn-stylekit-secondary-background-color: var(--c-bg-sidebar);
  --sn-stylekit-secondary-foreground-color: var(--c-mint-muted);
  --sn-stylekit-secondary-border-color: var(--c-border);

  --navigation-item-selected-background-color: var(--c-bg-active);

  --sn-stylekit-editor-background-color: var(--c-bg-deep);
  --sn-stylekit-editor-foreground-color: var(--c-mint-bright);
  --sn-stylekit-paragraph-text-color: var(--c-mint-muted);

  --sn-stylekit-neutral-color: var(--c-mint-muted);
  --sn-stylekit-neutral-contrast-color: white;

  --sn-stylekit-info-color: var(--c-mint-muted);
  --sn-stylekit-info-contrast-color: white;
  --sn-stylekit-info-backdrop-color: var(--c-bg-active);

  --sn-stylekit-success-color: var(--c-mint-muted);
  --sn-stylekit-success-contrast-color: white;

  --sn-stylekit-warning-color: var(--c-warning);
  --sn-stylekit-warning-contrast-color: white;

  --sn-stylekit-danger-color: var(--c-danger);
  --sn-stylekit-danger-contrast-color: white;

  --sn-stylekit-input-placeholder-color: var(--c-mint-dim);
  --sn-stylekit-input-border-color: var(--c-mint-dim);

  --sn-stylekit-scrollbar-thumb-color: var(--c-mint-dim);
  --sn-stylekit-scrollbar-track-border-color: transparent;

  --sn-stylekit-passive-color-0: var(--c-mint-muted);
  --sn-stylekit-passive-color-1: var(--c-mint-muted);
  --sn-stylekit-passive-color-3: var(--c-border);

  --sn-stylekit-passive-color-4: var(--c-bg-active);

  --sn-stylekit-passive-color-4-opacity-variant: rgba(21, 56, 38, 0.1);

  --sn-stylekit-passive-color-5: var(--c-bg-deep);
}

#blocks-editor hr:after {
  background-color: var(--c-mint-dim);
}

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