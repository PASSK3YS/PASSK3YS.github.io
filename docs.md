---
layout: default
title: Documentation
description: "My personal knowledge base: Tutorials, guides, and technical resources."
permalink: /docs/
---

<div class="section-cmd tline" style="margin-top: 0;">
    <div class="prompt-line">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">docs</span> --list</span>
    </div>
    <p class="dim" style="margin: 2px 0 0 0;">{{ page.description }}</p>
</div>

<div class="section-cmd tline">
    <a class="doc-tr" href="/docs/standard-notes/">
        <span class="tr-k">[sn]</span>
        <span class="doc-main">
            <span class="doc-title">Standard Notes</span>
            <span class="doc-desc dim">An end-to-end encrypted note taking application.</span>
            <span class="read-more">View resources &rarr;</span>
        </span>
    </a>
</div>

<div class="section-cmd tline">
    <a class="doc-tr" href="/docs/proton-mail/">
        <span class="tr-k">[pm]</span>
        <span class="doc-main">
            <span class="doc-title">Proton Mail</span>
            <span class="doc-desc dim">A privacy focused email service.</span>
            <span class="read-more">View resources &rarr;</span>
        </span>
    </a>
</div>

<div class="section-cmd tline">
    <a class="doc-tr" href="/docs/discord/">
        <span class="tr-k">[dc]</span>
        <span class="doc-main">
            <span class="doc-title">Discord</span>
            <span class="doc-desc dim">A platform for chats and communities.</span>
            <span class="read-more">View resources &rarr;</span>
        </span>
    </a>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-top: 22px;">
        <span class="prompt">$</span><span class="term-cursor"></span>
    </div>
</div>

<style>
    /* Docs page — terminal styling (shared with homepage) */
    .prompt-line { display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; }
    .prompt { color: var(--accent); white-space: nowrap; font-family: 'JetBrains Mono', monospace; }
    .cmd { color: var(--text); font-family: 'JetBrains Mono', monospace; }
    .command-name { color: var(--accent); }

    .dim { color: var(--text-muted); font-family: 'JetBrains Mono', monospace; }

    .doc-tr {
        display: flex;
        gap: 14px;
        align-items: flex-start;
        padding: 5px 0;
        width: fit-content;
        max-width: 100%;
        text-decoration: none;
        transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
        font-family: 'JetBrains Mono', monospace;
    }
    .doc-tr:hover { transform: translateX(8px); }
    .doc-tr .tr-k { color: var(--accent); opacity: 0.75; transition: opacity 0.25s ease; }
    .doc-tr:hover .tr-k { opacity: 1; }

    .doc-main { display: flex; flex-direction: column; min-width: 0; }
    .doc-title {
        font-family: 'JetBrains Mono', monospace;
        font-size: 1rem;
        color: var(--text);
        transition: color 0.2s ease;
    }
    .doc-tr:hover .doc-title { color: var(--accent); }
    .doc-desc {
        font-size: 0.82rem;
        line-height: 1.5;
        margin-top: 2px;
    }
    .read-more {
        display: inline-block;
        margin-top: 8px;
        font-size: 0.7rem;
        color: var(--text-muted);
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: color 0.25s ease, transform 0.25s ease;
    }
    .doc-tr:hover .read-more {
        color: var(--accent);
        transform: translateX(4px);
    }

    .term-cursor {
        display: inline-block;
        width: 0.55em; height: 1.05em;
        background: var(--accent);
        vertical-align: text-bottom;
        animation: docs-blink 1s step-end infinite;
    }
    @keyframes docs-blink { 50% { opacity: 0; } }

    .tline { opacity: 0; animation: docs-type-in 0.4s ease forwards; }
    @keyframes docs-type-in { to { opacity: 1; } }
</style>
