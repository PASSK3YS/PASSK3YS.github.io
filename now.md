---
layout: default
title: Now
permalink: /now/
last_updated: 2026-07-22
---

<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">

<style>
body, main, p, a, span, li {
    font-family: 'SUSE', sans-serif !important;
}
h1, h2, h3 {
    font-family: 'Staatliches', sans-serif !important;
}

.blinking-cursor {
    font-weight: 800;
    color: var(--accent-cyan);
    animation: blink 1s step-end infinite;
}

@keyframes blink {
    50% { opacity: 0; }
}

.unified-card {
    background: var(--nav-bg);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--border-color, var(--border));
    box-shadow: 6px 6px 0px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    margin-bottom: 20px;
}

[data-theme="dark"] .unified-card {
    border: 1px solid var(--border-color, var(--border));
    box-shadow: 6px 6px 0px rgba(255, 255, 255, 0.1);
}

.unified-row {
    padding: 30px 34px;
    border-bottom: 1px dashed var(--border-color, var(--border));
    display: grid;
    grid-template-columns: 240px 1fr;
    align-items: start;
    transition: background-color 0.1s ease, border-color 0.1s ease;
    border-left: 6px solid transparent;
}

.unified-row:last-child {
    border-bottom: none;
}

.unified-row.interactive-row:hover {
    background-color: rgba(42, 161, 152, 0.05);
    border-left-color: var(--accent-cyan);
}

[data-theme="dark"] .unified-row.interactive-row:hover {
    background-color: rgba(42, 161, 152, 0.1);
    border-left-color: var(--accent-cyan);
}

.interactive-row:hover .hacker-list li strong {
    color: var(--accent-cyan);
}

.soft-header {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    margin: 0;
    font-weight: 700;
    padding-top: 2px;
}

.unified-meta {
    font-size: 0.85rem;
    color: var(--accent-cyan);
    margin: 0;
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.hacker-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.hacker-list li {
    margin-bottom: 12px;
    opacity: 0.9;
    line-height: 1.4;
    position: relative;
    padding-left: 30px;
}

.hacker-list li::before {
    content: ">>";
    color: var(--accent-cyan);
    font-weight: 800;
    font-size: 0.9em;
    position: absolute;
    left: 0;
    top: 1px;
}

.hacker-list li:last-child {
    margin-bottom: 0;
}

.hacker-list li strong {
    color: var(--text);
    transition: color 0.1s ease;
}

@media (max-width: 850px) {
    .unified-row {
        grid-template-columns: 1fr;
        gap: 15px;
        padding: 25px 14px;
    }
}
</style>

<div class="page-content">
    <h1 style="margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px;">
        Now<span class="blinking-cursor">_</span>
    </h1>
    <p style="font-size: 1.05rem; opacity: 0.9; margin: 0 0 30px 0;">A snapshot of what is currently occupying my time and attention.</p>

    <div class="unified-card">
        
        <div class="unified-row interactive-row">
            <h3 class="soft-header">>_ Working on</h3>
            <ul class="hacker-list">
                <li><strong>Trying to lose weight</strong></li>
            </ul>
        </div>

        <div class="unified-row interactive-row">
            <h3 class="soft-header">>_ Playing</h3>
            <ul class="hacker-list">
                <li><strong>Dead By Daylight</strong></li>
            </ul>
        </div>

        <div class="unified-row interactive-row">
            <h3 class="soft-header">>_ Watching</h3>
            <ul class="hacker-list">
                <li><strong>House of the Dragon</strong> on HBO Max</li>
            </ul>
        </div>

        <div class="unified-row interactive-row">
            <h3 class="soft-header">>_ Listening to</h3>
            <ul class="hacker-list">
                <li><strong>Any Batmobile song</strong></li>
            </ul>
        </div>

    </div>

    <div style="text-align: right; margin-top: 10px;">
        <p class="unified-meta" style="opacity: 0.6; display: inline-block;">Last updated: {{ page.last_updated | date: "%d %m %Y" }}</p>
    </div>
</div>