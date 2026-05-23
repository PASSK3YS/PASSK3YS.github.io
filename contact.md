---
layout: default
title: Contact
permalink: /contact/
---

<div class="bio-container">
    <div class="bio-text">
        <h1 style="margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px;">
            Contact<span class="blinking-cursor">_</span>
        </h1>
        <p style="font-size: 1.05rem; opacity: 0.9; margin: 0;">
            You can reach me using the following...
        </p>
    </div>
</div>

<div class="unified-card">

    <div class="unified-row interactive-row">
        <h3 class="soft-header">>_ Email</h3>
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <a href="mailto:hi@colfer.net" class="directory-interactive-text">hi@colfer.net</a>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 15px; margin-bottom: 0; line-height: 1.4;">
                If you use Proton Mail, all email communications will be end-to-end encrypted.
            </p>
        </div>
    </div>

    <div class="unified-row interactive-row">
        <h3 class="soft-header">>_ Secure Chat</h3>
        <div style="display: flex; flex-direction: column; justify-content: center;">
            <a href="https://smp11.simplex.im/a#TyDMLK6GvVA62_9o1S4lvOVG-cBoBMyIUDxvHHpg5jA" target="_blank" class="directory-interactive-text">SimpleX Chat &rarr;</a>
        </div>
    </div>

    <div class="unified-row">
        <h3 class="soft-header">>_ Discord Community</h3>
        <div class="gamertag-list" style="display: flex; gap: 30px; align-items: center; flex-wrap: wrap;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span class="gamertag-label">Proton</span> 
                <a href="https://discord.com/invite/proton" target="_blank" class="directory-interactive-text">Join Server</a>
            </div>
            <div style="display: flex; align-items: center; gap: 10px;">
                <span class="gamertag-label">Standard Notes</span> 
                <a href="https://discord.com/invite/fxjJFxkRkY" target="_blank" class="directory-interactive-text">Join Server</a>
            </div>
        </div>
    </div>

</div>

<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">

<style>
body, main, h1, h2, h3, p, a, span {
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
    display: grid;
    grid-template-columns: 240px 1fr;
    align-items: center;
    transition: background-color 0.1s ease, border-color 0.1s ease;
    border-left: 6px solid transparent;
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

.soft-header {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    margin: 0;
    font-weight: 700;
}

.directory-interactive-text {
    font-size: 1.1rem;
    font-weight: 800;
    color: var(--text);
    text-decoration: none;
    transition: color 0.1s ease;
}

.directory-interactive-text:hover {
    color: var(--accent-cyan);
    text-decoration: underline;
}

.gamertag-label {
    font-size: 0.85rem;
    color: var(--text-muted);
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.5px;
}

@media (max-width: 850px) {
    .unified-row {
        grid-template-columns: 1fr;
        gap: 15px;
        padding: 25px 14px;
    }
}
</style>