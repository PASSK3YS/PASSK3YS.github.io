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
            <a href="https://signal.org" target="_blank" class="directory-interactive-text">Signal</a>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 15px; margin-bottom: 0; line-height: 1.4;">
                Trusted contacts only.
            </p>
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

body, main, p, a, span, div, button {
    font-family: 'SUSE', 'JetBrains Mono', system-ui, -apple-system, sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Staatliches', 'SUSE', sans-serif !important;
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
    display: grid;
    grid-template-columns: 240px 1fr;
    align-items: center;
    transition: background-color 0.3s ease, border-color 0.3s ease;
    border-left: 6px solid transparent;
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
    transform: translate(-2px, -2px);
    box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.2);
}

.interactive-row:hover .directory-interactive-text {
    color: var(--accent);
}

.soft-header {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    margin: 0;
    font-weight: 700;
    font-family: 'Staatliches', 'SUSE', sans-serif !important;
}

.directory-interactive-text {
    font-size: 1.1rem;
    font-weight: 800;
    color: var(--text);
    text-decoration: none;
    transition: color 0.3s ease;
}

.directory-interactive-text:hover {
    color: var(--accent);
    text-decoration: underline;
}

.gamertag-label {
    font-size: 0.85rem;
    color: var(--text-muted);
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.gamertag-list a {
    color: var(--text);
    text-decoration: none;
    font-weight: 800;
    transition: color 0.3s ease;
    font-size: 1.1rem;
}

.gamertag-list a:hover {
    color: var(--accent);
}

@media (max-width: 850px) {
    .unified-row {
        grid-template-columns: 1fr;
        gap: 15px;
        padding: 25px 14px;
    }
}
</style>