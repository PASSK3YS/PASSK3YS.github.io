---
layout: default
title: Contact
permalink: /contact/
---

<div class="section-cmd tline" style="margin-top: 0;">
    <div class="prompt-line">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">contact</span> --methods</span>
    </div>
    <p class="dim" style="margin: 2px 0 0 0;">You can reach me using the following...</p>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">email</span> --encrypt</span>
    </div>
    <div class="tr">
        <span class="tr-v"><a href="mailto:hi@colfer.net">hi@colfer.net</a></span>
    </div>
    <p class="dim tr-note">If you use Proton Mail, all email communications will be end-to-end encrypted.</p>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">secure-chat</span></span>
    </div>
    <div class="tr">
        <span class="tr-v"><a href="https://signal.org" target="_blank">Signal</a></span>
    </div>
    <p class="dim tr-note">Trusted contacts only.</p>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">discord</span> --servers</span>
    </div>
    <div class="tr">
        <span class="tr-k">[proton]</span>
        <span class="tr-v"><a href="https://discord.com/invite/proton" target="_blank">Join Server</a></span>
    </div>
    <div class="tr">
        <span class="tr-k">[standard-notes]</span>
        <span class="tr-v"><a href="https://discord.com/invite/fxjJFxkRkY" target="_blank">Join Server</a></span>
    </div>
    <div class="prompt-line" style="margin-top: 22px;">
        <span class="prompt">$</span><span class="term-cursor"></span>
    </div>
</div>

<style>
    /* Contact page — terminal styling (shared with homepage) */
    .prompt-line { display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; }
    .prompt { color: var(--accent); white-space: nowrap; }
    .cmd { color: var(--text); font-family: 'JetBrains Mono', monospace; }
    .command-name { color: var(--accent); }

    .dim { color: var(--text-muted); font-family: 'JetBrains Mono', monospace; }

    .tr .tr-v a {
        color: var(--accent);
        text-decoration: none;
        border-bottom: 1px dashed var(--accent);
        transition: border-color 0.2s ease, text-shadow 0.2s ease;
    }
    .tr .tr-v a:hover {
        border-bottom-style: solid;
        text-shadow: 0 0 14px var(--accent-glow);
    }

    .term-cursor {
        display: inline-block;
        width: 0.55em; height: 1.05em;
        background: var(--accent);
        vertical-align: text-bottom;
        animation: term-blink 1s step-end infinite;
    }
    @keyframes term-blink { 50% { opacity: 0; } }

    .tr {
        display: flex;
        gap: 12px;
        align-items: center;
        padding: 5px 0;
        width: fit-content;
        max-width: 100%;
        transition: transform 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
    }
    .tr:hover { transform: translateX(8px); }
    .tr .tr-k { color: var(--accent); opacity: 0.75; transition: color 0.25s ease, opacity 0.25s ease; font-family: 'JetBrains Mono', monospace; }
    .tr:hover .tr-k { opacity: 1; }
    .tr .tr-v { color: var(--text); font-family: 'JetBrains Mono', monospace; }

    .tr-note {
        font-size: 0.8rem;
        margin: 2px 0 0 0;
        line-height: 1.5;
        width: fit-content;
        max-width: 100%;
    }

    .tline { opacity: 0; animation: contact-type-in 0.4s ease forwards; }
    @keyframes contact-type-in { to { opacity: 1; } }
</style>
