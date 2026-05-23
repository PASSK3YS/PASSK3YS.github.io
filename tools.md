---
layout: default
title: Tools
permalink: /tools/
---

<div class="bio-container">
    <div class="bio-text">
        <h1 style="margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px;">
            Tools<span class="blinking-cursor">_</span>
        </h1>
        <p style="font-size: 1.05rem; opacity: 0.9; margin: 0;">
            A collection of privacy-focused, client-side tools and resources.
        </p>
    </div>
</div>

<div class="unified-card">

    <a href="/tools/standard-notes-themes/" class="unified-row interactive-row">
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <h2 class="directory-interactive-text" style="margin: 0 0 10px 0;">Standard Notes Themes</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0; line-height: 1.5;">
                A collection of custom themes including Standard Blue, Dark Mint, and Lights Out.
            </p>
            <span class="read-more">View Themes &rarr;</span>
        </div>
    </a>

    <a href="/tools/vivaldi-themes/" class="unified-row interactive-row">
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <h2 class="directory-interactive-text" style="margin: 0 0 10px 0;">Vivaldi browser themes</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0; line-height: 1.5;">
                A collection of my custom Vivaldi Browser Themes.
            </p>
            <span class="read-more">View Themes &rarr;</span>
        </div>
    </a>

    <a href="/tools/username-generator/" class="unified-row interactive-row">
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <h2 class="directory-interactive-text" style="margin: 0 0 10px 0;">Username Generator</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0; line-height: 1.5;">
                Generate secure, random usernames with optional keywords and numbers.
            </p>
            <span class="read-more">Open Tool &rarr;</span>
        </div>
    </a>

    <a href="/tools/recommendations/" class="unified-row interactive-row">
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <h2 class="directory-interactive-text" style="margin: 0 0 10px 0;">Recommendations</h2>
            <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0; line-height: 1.5;">
                My curated list of tools, software, and services I use and recommend.
            </p>
            <span class="read-more">View List &rarr;</span>
        </div>
    </a>

</div>

<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">

<style>
body, main, h1, h2, h3, p, a, span, div {
    font-family: 'JetBrains Mono', monospace !important;
}

.blinking-cursor {
    font-weight: 800;
    color: var(--accent-cyan);
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
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border-color);
    box-shadow: 6px 6px 0px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

[data-theme="dark"] .unified-card {
    border: 1px solid var(--border-color);
    box-shadow: 6px 6px 0px rgba(0, 0, 0, 0.3);
}

.unified-row {
    padding: 30px 34px;
    border-bottom: 1px dashed var(--border-color);
    display: block;
    transition: background-color 0.1s ease, border-color 0.1s ease;
    border-left: 6px solid transparent;
    text-decoration: none;
    color: inherit;
}

.unified-row:last-child {
    border-bottom: none;
}

.unified-row.interactive-row {
    cursor: pointer;
}

.unified-row.interactive-row:hover {
    background-color: rgba(42, 161, 152, 0.05);
    border-left-color: var(--accent-cyan);
}

[data-theme="dark"] .unified-row.interactive-row:hover {
    background-color: rgba(42, 161, 152, 0.1);
    border-left-color: var(--accent-cyan);
}

.interactive-row:hover .directory-interactive-text {
    color: var(--accent-cyan);
}

.interactive-row:hover .read-more {
    color: var(--accent-cyan);
    transform: translateX(5px);
}

.directory-interactive-text {
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--text);
    text-decoration: none;
    transition: color 0.1s ease;
    line-height: 1.3;
}

.read-more {
    display: inline-block;
    margin-top: 15px;
    font-size: 0.85rem;
    font-weight: 800;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: color 0.1s ease, transform 0.1s ease;
}

@media (max-width: 850px) {
    .unified-row {
        padding: 25px 14px;
    }
}
</style>