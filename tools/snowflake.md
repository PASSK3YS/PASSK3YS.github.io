---
layout: default
title: Snowflake Proxy
permalink: /tools/snowflake/
---

<div class="sf-shell">
    <div class="sf-cmd">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">tor</span> --snowflake-proxy</span>
    </div>
    <p class="sf-intro">
        Help people in censored countries reach the open internet.
    </p>
</div>

<div class="sf-card">
    <div class="snowflake-section">
        <p style="font-size: 0.95rem; color: var(--text-muted); margin: 0 0 12px 0; line-height: 1.5;">
            Toggle the switch below and your browser becomes a temporary bridge, helping people
            in censored countries connect to the Tor network. You never see their traffic or
            identity, and they never see yours. Leave this tab open to keep helping.
        </p>
        <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0 0 20px 0; line-height: 1.5;">
            Nothing happens until you opt in, and you can switch off anytime. Please don't run a
            snowflake while on a VPN. A project of the
            <a href="https://torproject.org" rel="noopener noreferrer">Tor Project</a> &mdash;
            <a href="https://snowflake.torproject.org" rel="noopener noreferrer">learn more</a>.
        </p>
        <div class="snowflake-embed">
            <iframe
                src="https://snowflake.torproject.org/embed.html"
                width="340" height="300" frameborder="0"
                title="Tor Snowflake volunteer widget">
            </iframe>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/snowflake-extension/embed.js"></script>

<style>
.sf-shell { font-family: 'JetBrains Mono', monospace; margin-bottom: 26px; }
.sf-cmd { display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; flex-wrap: wrap; }
.sf-cmd .prompt { color: var(--accent); white-space: nowrap; }
.sf-cmd .cmd { color: var(--text); font-size: 1.1rem; font-weight: 700; }
.sf-cmd .command-name { color: var(--accent); }
.sf-intro {
    font-family: 'SUSE', sans-serif;
    font-size: 0.95rem;
    color: var(--text-muted);
    margin: 0;
}

.sf-card {
    background: var(--nav-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.snowflake-section { padding: 22px 24px; }
.snowflake-section a {
    color: var(--accent);
    text-decoration: none;
    border-bottom: 1px dashed var(--accent);
}
.snowflake-section a:hover {
    border-bottom-style: solid;
    text-shadow: 0 0 14px var(--accent-glow);
}

.snowflake-embed {
    display: flex;
    justify-content: center;
}

.snowflake-embed iframe {
    width: 340px;
    max-width: 100%;
    height: 300px;
    border: none;
    border-radius: 4px;
    background: transparent;
}

@media (max-width: 850px) {
    .snowflake-section {
        padding: 18px 14px;
    }
}
</style>
