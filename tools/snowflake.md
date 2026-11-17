---
layout: default
title: Snowflake Proxy
permalink: /tools/snowflake/
---

<div class="bio-container">
    <div class="bio-text">
        <h1 style="margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px;">
            Tor Snowflake<span class="blinking-cursor">_</span>
        </h1>
        <p style="font-size: 1.05rem; opacity: 0.9; margin: 0;">
            Help people in censored countries reach the open internet.
        </p>
    </div>
</div>

<div class="unified-card">
    <div class="snowflake-section" style="padding: 30px 34px;">
        <h2 style="margin: 0 0 10px 0;">Become a Snowflake volunteer</h2>
        <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0 0 20px 0; line-height: 1.5;">
            Snowflake is a pluggable transport for Tor. When you turn it on below, your browser
            acts as a temporary, disposable proxy that helps someone in a censored network
            connect to the Tor network. Your connection is used only as a bridge &mdash; you never
            see their traffic or their identity, and they never see yours. To keep helping,
            simply leave this tab open.
        </p>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0 0 20px 0; line-height: 1.5;">
            <strong>Things to know:</strong> nothing happens until you opt in with the button
            below, and you can turn it off at any time. Tor asks volunteers not to run a
            snowflake proxy while connected to a VPN, and visitors on networks that block
            WebRTC won't be able to participate. Snowflake is a project of the
            <a href="https://torproject.org" rel="noopener noreferrer">Tor Project</a> &mdash;
            learn more at
            <a href="https://snowflake.torproject.org" rel="noopener noreferrer">snowflake.torproject.org</a>.
        </p>
        <iframe
            src="https://embed-snowflake.torproject.org/embed.html"
            width="320" height="240" frameborder="0" scrolling="no"
            style="max-width: 100%; border-radius: 8px;">
        </iframe>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/snowflake-extension/embed.js"></script>

<style>

body, main, p, a, span, div, button {
    font-family: 'Atkinson Hyperlegible Next', sans-serif !important
}

h1, h2, h3 {
    font-family: 'Staatliches', sans-serif !important;
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

.snowflake-section a {
    color: var(--accent);
}

@media (max-width: 850px) {
    .snowflake-section {
        padding: 25px 14px;
    }
}
</style>