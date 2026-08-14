---
layout: default
title: Documentation
description: "My personal knowledge base: Tutorials, guides, and technical resources."
permalink: /cy/docs/
---

<div class="bio-container">
    <div class="bio-text">
        <h1 style="margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px;">
            Docs<span class="blinking-cursor">_</span>
        </h1>
        <p style="font-size: 1.05rem; opacity: 0.9; margin: 0;">
            {{ page.description }}
        </p>
    </div>
</div>

<div class="unified-card">

    <a href="/docs/standard-notes/" class="unified-row interactive-row">
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <h2 class="directory-interactive-text" style="margin: 0 0 10px 0;">Standard Notes</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0; line-height: 1.5;">
                An end-to-end encrypted note taking application.
            </p>
            <span class="read-more">View resources &rarr;</span>
        </div>
    </a>

    <a href="/docs/proton-mail/" class="unified-row interactive-row">
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <h2 class="directory-interactive-text" style="margin: 0 0 10px 0;">Proton Mail</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0; line-height: 1.5;">
                A privacy focused email service.
            </p>
            <span class="read-more">View resources &rarr;</span>
        </div>
    </a>

        <a href="/docs/discord/" class="unified-row interactive-row">
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <h2 class="directory-interactive-text" style="margin: 0 0 10px 0;">Discord</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0; line-height: 1.5;">
                A platform for chats and communities.
            </p>
            <span class="read-more">View resources &rarr;</span>
        </div>
    </a>

</div>

<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">

<style>

body, main, h1, h2, h3, p, a, span, div, button {
    font-family: 'SUSE', sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Staatliches', sans-serif !important;
}

pre, code {
    font-family: 'JetBrains Mono', monospace !important;
}

.blinking-cursor {
    font-weight: 800;
    color: var(--accent);
    animation: blink 1s step-end infinite;
}

@keyframes blink {
    50% { opacity: 0; }
}

.bio-container {
    display: flex;
    align-items: center;
    gap: 30px;
    margin-bottom: 40px;
}

.bio-text {
    display: flex;
    flex-direction: column;
}

.unified-card {
    background: var(--nav-bg);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    overflow: hidden;
}

[data-theme="dark"] .unified-card {
    border: 1px solid var(--border);
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
}

.unified-row {
    padding: 30px 34px;
    border-bottom: 1px dashed var(--border);
    display: block;
    transition: background-color 0.3s ease, border-color 0.3s ease;
    border-left: 6px solid transparent;
    text-decoration: none;
    color: inherit;
}

[data-theme="dark"] .unified-row {
    transition: background-color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}

.unified-row:last-child {
    border-bottom: none;
}

.unified-row.interactive-row {
    cursor: pointer;
}

.unified-row.interactive-row:hover {
    background-color: rgba(99, 102, 241, 0.05);
    border-left-color: var(--accent);
}

[data-theme="dark"] .unified-row.interactive-row:hover {
    background-color: rgba(99, 102, 241, 0.1);
    border-left-color: var(--accent);
}

.interactive-row:hover .directory-interactive-text {
    color: var(--accent);
}

.interactive-row:hover .read-more {
    color: var(--accent);
    transform: translateX(5px);
}

.directory-interactive-text {
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--text);
    text-decoration: none;
    transition: color 0.3s ease;
    line-height: 1.3;
}

.read-more {
    display: inline-block;
    margin-top: 15px;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: color 0.3s ease, transform 0.3s ease;
}

@media (max-width: 850px) {
    .unified-row {
        padding: 25px 14px;
    }
}
</style>