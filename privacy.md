---
layout: default
title: Privacy Policy
permalink: /privacy/
---

<div class="section-cmd tline" style="margin-top: 0;">
    <div class="prompt-line">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">cat</span> /legal/privacy.txt</span>
    </div>
    <p class="dim" style="margin: 2px 0 0 0;">Last updated: November 17, 2026</p>
</div>

<div class="policy tline">

  <h3 class="pol-head"><span class="prompt">$</span> 1. The Short Version</h3>
  <p>I respect your privacy. This website does not use tracking cookies, does not run invasive analytics, and does not sell your personal data. It is designed to be as lightweight and privacy-respecting as possible.</p>

  <h3 class="pol-head"><span class="prompt">$</span> 2. Data Collection</h3>
  <p>Because this is a static website, the personal information I collect is what you voluntarily choose to share with me:</p>
  <ul>
    <li><strong>Email Communications:</strong> If you email me via my contact page, I will receive your email address and any information you include in your message.</li>
    <li><strong>Upvote System:</strong> To prevent spam and ensure each visitor can only vote once per blog post, the custom Cloudflare Worker powering the upvote button processes your IP address. Your IP is instantly cryptographically hashed; it is never stored in plain text. Only this anonymized hash is securely stored in a Cloudflare KV database to prevent duplicate votes.</li>
    <li><strong>GitHub Contributions:</strong> If you submit an edit or contribute to a document on this website via GitHub, your public GitHub profile (including your username and avatar) will be automatically fetched and displayed on the relevant page as a contributor.</li>
    <li><strong>Server Logs:</strong> This website is hosted on GitHub Pages. Like all web hosts, GitHub automatically collects standard server logs, which may include your IP address, browser type, and the pages you visit. This is required for security and to serve the website to you.</li>
  </ul>

  <h3 class="pol-head"><span class="prompt">$</span> 3. Third-Party Services &amp; Security</h3>
  <p>To protect my website from spam and bot abuse, I use <strong>Cloudflare Turnstile</strong>. Turnstile is a privacy-first alternative to traditional CAPTCHAs. It verifies that you are a real human without tracking you across the web or using your data for targeted advertising. Cloudflare may process some standard technical data (like device or browser characteristics) strictly for the purpose of bot detection.</p>
  <p>The <strong>Tor Snowflake</strong> page embeds a widget from the Tor Project (<em>snowflake.torproject.org</em>). If you <em>choose</em> to opt in, your browser connects to Tor's infrastructure and temporarily proxies traffic for Tor users in censored regions. This only happens after you explicitly toggle the widget on, and you can turn it off at any time by leaving the page or toggling off. Snowflake never reveals your IP address to the people you help, and you never see their traffic or identity. The Tor Project's own <a href="https://support.torproject.org/" class="pol-link">privacy policy</a> applies to that connection.</p>

  <h3 class="pol-head"><span class="prompt">$</span> 4. How Your Data is Used</h3>
  <p>Email correspondence is used strictly to reply to your inquiries. If you contribute to a document on this website, your public avatar and username are displayed to credit your edits. The upvote system processes and stores anonymized hash data solely to maintain accurate vote counts and prevent spam abuse. Snowflake proxying is voluntary and is used only to relay encrypted traffic between Tor users and the Tor network.</p>

  <h3 class="pol-head"><span class="prompt">$</span> 5. Cookies and Trackers</h3>
  <p>This site does not set any tracking cookies, advertising cookies, or third-party analytics scripts. You are completely free to browse without being followed. The Snowflake widget is an embedded third-party element, but it is opt-in only and performs no tracking or analytics.</p>

  <h3 class="pol-head"><span class="prompt">$</span> 6. Your Rights</h3>
  <p>If you have sent me an email and would like your information permanently deleted from my records, simply <a href="/contact/" class="pol-link">contact me</a> and I will remove it immediately.</p>

  <div class="prompt-line" style="margin-top: 26px;">
    <span class="prompt">$</span><span class="term-cursor"></span>
  </div>

</div>

<style>
    /* Privacy page — terminal styling (shared with homepage) */
    .prompt-line { display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; }
    .prompt { color: var(--accent); white-space: nowrap; font-family: 'JetBrains Mono', monospace; }
    .cmd { color: var(--text); font-family: 'JetBrains Mono', monospace; }
    .command-name { color: var(--accent); }

    .dim { color: var(--text-muted); font-family: 'JetBrains Mono', monospace; }

    .policy {
        max-width: 780px;
        color: var(--text);
        line-height: 1.7;
        font-size: 0.95rem;
    }

    .pol-head {
        color: var(--accent);
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.95rem;
        font-weight: 700;
        margin: 34px 0 10px 0;
        display: flex;
        gap: 10px;
        align-items: baseline;
        text-shadow: 0 0 14px var(--accent-glow);
    }
    .pol-head:first-child { margin-top: 30px; }

    .policy ul {
        padding-left: 22px;
        margin: 10px 0;
    }
    .policy li { margin-bottom: 10px; }

    .pol-link {
        color: var(--accent);
        text-decoration: none;
        border-bottom: 1px dashed var(--accent);
        transition: border-color 0.2s ease, text-shadow 0.2s ease;
    }
    .pol-link:hover {
        border-bottom-style: solid;
        text-shadow: 0 0 14px var(--accent-glow);
    }

    .term-cursor {
        display: inline-block;
        width: 0.55em; height: 1.05em;
        background: var(--accent);
        vertical-align: text-bottom;
        animation: priv-blink 1s step-end infinite;
    }
    @keyframes priv-blink { 50% { opacity: 0; } }

    .tline { opacity: 0; animation: priv-type-in 0.4s ease forwards; }
    @keyframes priv-type-in { to { opacity: 1; } }
</style>
