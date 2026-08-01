---
layout: default
title: Guestbook
permalink: /guestbook/
---

<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">

<style>
body, main, h1, h2, h3, p, a, span, div, button {
    font-family: 'SUSE', sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Staatliches', sans-serif !important;
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

.giscus-wrapper {
    background: var(--nav-bg);
    padding: 30px;
    border-radius: 16px;
    border: 1px solid var(--border);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    margin-top: 40px;
}

[data-theme="dark"] .giscus-wrapper {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
}
</style>

<div class="page-content" style="max-width: 800px; margin: 0 auto; padding-top: 20px;">
  
    <h1 style="color: var(--accent); text-align: center; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 10px;">
        >_ Guestbook<span class="blinking-cursor">_</span>
    </h1>
  
    <p style="color: var(--text-muted); text-align: center; margin-bottom: 30px; font-size: 1.05rem;">
        Messages and greetings from visitors.
    </p>

    <div class="giscus-wrapper">
    <script src="https://giscus.app/client.js"
            data-repo="PASSK3YS/PASSK3YS.GITHUB.IO"
            data-repo-id="R_kgDORKZKwQ"
            data-category="General"
            data-category-id="DIC_kwDORKZKwc4DCdwh"
            data-mapping="pathname"
            data-strict="0"
            data-reactions-enabled="1"
            data-emit-metadata="0"
            data-input-position="top"
            data-theme="transparent_dark"
            data-lang="en"
            crossorigin="anonymous"
            async>
    </script>
</div>

<script>
function updateGiscusTheme() {
    const targetElement = document.documentElement.hasAttribute('data-theme') ? document.documentElement : document.body;
    const currentTheme = targetElement.getAttribute('data-theme');
    const giscusTheme = currentTheme === 'light' ? 'light' : 'dark';
    const iframe = document.querySelector('iframe.giscus-frame');
    
    if (iframe) {
        iframe.contentWindow.postMessage(
            { giscus: { setConfig: { theme: giscusTheme } } },
            'https://giscus.app'
        );
    }
}

const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.attributeName === 'data-theme') {
            updateGiscusTheme();
        }
    });
});

observer.observe(document.documentElement, { attributes: true });
observer.observe(document.body, { attributes: true });

window.addEventListener('message', (event) => {
    if (event.origin === 'https://giscus.app' && event.data && event.data.giscus) {
        updateGiscusTheme();
    }
});
</script>

</div>