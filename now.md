---
layout: default
title: Now
permalink: /now/
last_updated: 2026-11-27
---

<style>
.now-shell { font-family: 'JetBrains Mono', monospace; }

.now-cmd {
    display: flex;
    gap: 10px;
    align-items: baseline;
    margin: 0 0 6px 0;
    flex-wrap: wrap;
}
.now-cmd .prompt { color: var(--accent); white-space: nowrap; }
.now-cmd .cmd { color: var(--text); }
.now-cmd .command-name { color: var(--accent); }

.now-intro {
    font-family: 'SUSE', sans-serif;
    color: var(--text-muted);
    font-size: 0.95rem;
    margin: 0 0 30px 0;
}

.now-section {
    margin-top: 26px;
}

.now-section .sec-head {
    font-size: 0.8rem;
    color: var(--accent);
    opacity: 0.75;
    text-transform: lowercase;
    letter-spacing: 0.5px;
    font-weight: 700;
    margin: 0 0 4px 0;
    transition: opacity 0.25s ease;
}
.now-section:hover .sec-head { opacity: 1; }

.now-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.now-list li {
    display: flex;
    gap: 12px;
    align-items: baseline;
    padding: 5px 0;
    opacity: 0.9;
    line-height: 1.4;
    font-family: 'SUSE', sans-serif;
    font-size: 0.95rem;
    transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
    width: fit-content;
    max-width: 100%;
}
.now-list li:hover { transform: translateX(8px); }

.now-list li::before {
    content: ">>";
    color: var(--accent);
    font-family: 'JetBrains Mono', monospace;
    font-weight: 800;
    font-size: 0.9em;
    opacity: 0.75;
    transition: opacity 0.25s ease;
}
.now-list li:hover::before { opacity: 1; }

.now-list li strong { color: var(--text); }

.now-meta {
    text-align: right;
    margin-top: 30px;
    font-size: 0.75rem;
    color: var(--text-muted);
    opacity: 0.6;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.term-cursor {
    display: inline-block;
    width: 0.55em; height: 1.05em;
    background: var(--accent);
    vertical-align: text-bottom;
    animation: now-blink 1s step-end infinite;
}
@keyframes now-blink { 50% { opacity: 0; } }
</style>

<div class="page-content now-shell">
    <div class="now-cmd">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">cat</span> /now/whats-new.txt</span>
    </div>
    <p class="now-intro">A snapshot of what is currently occupying my time and attention.</p>

    <div class="now-section">
        <h3 class="sec-head">&gt;_ working on</h3>
        <ul class="now-list">
            <li><strong>Editing my website</strong></li>
        </ul>
    </div>

    <div class="now-section">
        <h3 class="sec-head">&gt;_ playing</h3>
        <ul class="now-list">
            <li><strong>Grand Theft Auto VI</strong></li>
        </ul>
    </div>

    <div class="now-section">
        <h3 class="sec-head">&gt;_ watching</h3>
        <ul class="now-list">
            <li><strong>A Knight of the Seven Kingdoms </strong> on HBO Max</li>
        </ul>
    </div>

    <div class="now-section">
        <h3 class="sec-head">&gt;_ listening to</h3>
        <ul class="now-list">
            <li><strong>Any Batmobile song</strong></li>
        </ul>
    </div>

    <div style="display: flex; gap: 10px; align-items: baseline; margin-top: 34px;">
        <span style="color: var(--accent); font-family: 'JetBrains Mono', monospace;">$</span>
        <span class="term-cursor"></span>
    </div>

    <div class="now-meta">
        <p style="margin: 0;">Last updated: {{ page.last_updated | date: "%d %m %Y" }}</p>
    </div>
</div>
