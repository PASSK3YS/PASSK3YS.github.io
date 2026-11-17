---
layout: default
title: Tools
permalink: /tools/
---

<div class="section-cmd tline" style="margin-top: 0;">
    <div class="prompt-line">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">tools</span> --list</span>
    </div>
    <p class="dim" style="margin: 2px 0 0 0;">A collection of privacy-focused, client-side tools and resources.</p>
</div>

<div class="section-cmd tline">
    <a class="doc-tr" href="/tools/standard-notes-themes/">
        <span class="tr-k">[themes]</span>
        <span class="doc-main">
            <span class="doc-title">Standard Notes Themes</span>
            <span class="doc-desc dim">A collection of custom themes including Standard Blue, Dark Mint, and Lights Out.</span>
            <span class="read-more">View Themes &rarr;</span>
        </span>
    </a>
</div>

<div class="section-cmd tline">
    <a class="doc-tr" href="/tools/username-generator/">
        <span class="tr-k">[gen]</span>
        <span class="doc-main">
            <span class="doc-title">Username Generator</span>
            <span class="doc-desc dim">Generate secure, random usernames with optional keywords and numbers.</span>
            <span class="read-more">Open Tool &rarr;</span>
        </span>
    </a>
</div>

<div class="section-cmd tline">
    <a class="doc-tr" href="/tools/snowflake/">
        <span class="tr-k">[tor]</span>
        <span class="doc-main">
            <span class="doc-title">Tor Snowflake Proxy</span>
            <span class="doc-desc dim">Opt in to become a Snowflake volunteer and help people in censored countries reach the open internet.</span>
            <span class="read-more">Volunteer &rarr;</span>
        </span>
    </a>
</div>

<div class="section-cmd tline">
    <a class="doc-tr" href="/tools/recommendations/">
        <span class="tr-k">[recs]</span>
        <span class="doc-main">
            <span class="doc-title">Recommendations</span>
            <span class="doc-desc dim">My curated list of tools, software, and services I use and recommend.</span>
            <span class="read-more">View List &rarr;</span>
        </span>
    </a>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-top: 22px;">
        <span class="prompt">$</span><span class="term-cursor"></span>
    </div>
</div>

<style>
    /* Tools page — terminal styling (shared with homepage) */
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
        animation: tools-blink 1s step-end infinite;
    }
    @keyframes tools-blink { 50% { opacity: 0; } }

    .tline { opacity: 0; animation: tools-type-in 0.4s ease forwards; }
    @keyframes tools-type-in { to { opacity: 1; } }
</style>
