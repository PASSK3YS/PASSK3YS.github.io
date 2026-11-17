---
layout: default
title: About
---

<div class="output about-output tline">
    <div class="bio-frame">
        <img src="https://files.horizon.pics/e3915a41-a35d-4f53-8041-df90f652947a?a=480&region=eu-central&mime1=image&mime2=jpeg" alt="Kieran">
    </div>
    <div class="about-text">
        <p>Hi, I'm Kieran<span class="term-cursor"></span></p>
        <p>Welcome to my personal website. Overall swell guy, avid beer drinker &amp; privacy advocate.</p>
        <p>Hobbies include playing video games, watching wrestling &amp; photography.</p>
        <p class="dim">Server admin / moderator for <a href="https://standardnotes.com" target="_blank">Standard Notes</a> &amp; <a href="https://proton.me" target="_blank">Proton</a>.</p>
    </div>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">socials</span> --list</span>
    </div>
    <div class="tr">
        <span class="tr-k">[x]</span>
        <span class="tr-v"><a href="https://x.com/PASSK3YS" target="_blank">@PASSK3YS</a></span>
    </div>
    <div class="tr">
        <span class="tr-k">[discord]</span>
        <span class="tr-v"><a href="https://discord.com/users/passkeys" target="_blank">passkeys</a></span>
    </div>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">gamertags</span></span>
    </div>
    <div class="tr">
        <span class="tr-k">[xbox]</span>
        <span class="tr-v"><a href="https://www.xbox.com/en-GB/play/user/m00t" target="_blank">m00t</a></span>
    </div>
    <div class="tr">
        <span class="tr-k">[steam]</span>
        <span class="tr-v"><a href="https://steamcommunity.com/id/m00t316/" target="_blank">m00t316</a></span>
    </div>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">latest-post</span></span>
    </div>
    <a class="tr" href="#" id="latest-blog-link">
        <span class="tr-k">[blog]</span>
        <span class="tr-v dim" id="latest-blog-container">Loading latest...</span>
    </a>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">latest-cinema-watch</span></span>
    </div>
    <a class="tr" href="/cinema-watchlist/2026/" id="latest-movie-link">
        <span class="tr-k">[film]</span>
        <span class="tr-v dim" id="latest-movie-container">Loading latest...</span>
    </a>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">now</span></span>
    </div>
    <a class="tr" href="/now/">
        <span class="tr-k">[status]</span>
        <span class="tr-v">What I'm doing now &rarr;</span>
    </a>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-bottom: 2px;">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">tip-jar</span></span>
    </div>
    <div class="tr" style="max-width: 100%;">
        <span class="tr-k">[xmr]</span>
        <span class="xmr">46yuchLT4YATJjWkSFAD9LeNbD9jCtJHU9Vn3FhRsDJ95GHaDvp8ppzfd3u2L7hZ1DSB8n1kQPMrmeu5zQA9oT8XFv2ka4R</span>
    </div>
    <div class="prompt-line" style="margin-top: 22px;">
        <span class="prompt">$</span><span class="term-cursor"></span>
    </div>
</div>

<style>
    /* Homepage-specific terminal styling (window/chrome now in the layout) */
    .prompt-line { display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; }
    .prompt { color: var(--accent); white-space: nowrap; }
    .cmd { color: var(--text); }

    .output { color: var(--text); margin: 2px 0 18px 0; }
    .output a, .tr .tr-v a, .about-text a { color: var(--accent); text-decoration: none; border-bottom: 1px dashed var(--accent); transition: border-color 0.2s ease, text-shadow 0.2s ease; }
    .output a:hover, .tr .tr-v a:hover, .about-text a:hover { border-bottom-style: solid; text-shadow: 0 0 14px var(--accent-glow); }

    .dim { color: var(--text-muted); }

    .term-cursor {
        display: inline-block;
        width: 0.55em; height: 1.05em;
        background: var(--accent);
        vertical-align: text-bottom;
        animation: term-blink 1s step-end infinite;
    }
    @keyframes term-blink { 50% { opacity: 0; } }

    .about-output {
        display: flex;
        gap: 22px;
        align-items: flex-start;
    }

    /* Photo frame hugs the image: tight padding, no caption */
    .bio-frame {
        flex-shrink: 0;
        padding: 3px;
        border: 1px solid var(--accent);
        border-radius: 4px;
        background: var(--accent-glow);
        line-height: 0;
    }
    .bio-frame img {
        display: block;
        width: 150px;
        height: auto;
        border-radius: 2px;
        filter: saturate(0.9) contrast(1.05);
        transition: filter 0.3s ease;
    }
    .bio-frame:hover img { filter: saturate(1.1) contrast(1.05); }

    .about-text { min-width: 0; }
    .about-text p { margin: 0 0 4px 0; }

    .section-cmd { margin-top: 26px; color: var(--text); }
    .command-name { color: var(--accent); }

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
    .tr .tr-k { color: var(--accent); opacity: 0.75; transition: color 0.25s ease, opacity 0.25s ease; }
    .tr:hover .tr-k { opacity: 1; }
    .tr .tr-v { color: var(--text); }

    a.tr { text-decoration: none; }
    a.tr .tr-v { color: var(--text); transition: color 0.2s ease; }
    a.tr:hover .tr-v { color: var(--accent); }

    .xmr {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.78rem;
        color: var(--text-muted);
        word-break: break-all;
        display: block;
        margin-top: 2px;
    }

    @media (max-width: 640px) {
        .about-output { flex-direction: column; align-items: center; text-align: center; }
        .bio-frame img { width: 120px; }
    }
</style>

<script>
document.addEventListener("DOMContentLoaded", () => {
    fetch('/feed.json')
        .then(res => res.json())
        .then(data => {
            if (data.items && data.items.length > 0) {
                const firstPost = data.items[0];
                let dateStr = "";
                if (firstPost.date_published) {
                    const date = new Date(firstPost.date_published);
                    dateStr = date.toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }).toUpperCase();
                }
                const c = document.getElementById('latest-blog-container');
                c.classList.remove('dim');
                c.innerHTML = `${firstPost.title} <span class="dim">// ${dateStr}</span>`;
                document.getElementById('latest-blog-link').href = firstPost.url;
            }
        })
        .catch(() => {});

    fetch('/cinema-watchlist/2026/')
        .then(res => res.text())
        .then(pageHtml => {
            const firstMovie = new DOMParser().parseFromString(pageHtml, 'text/html').querySelector('.movie-card');
            if (firstMovie) {
                const c = document.getElementById('latest-movie-container');
                c.classList.remove('dim');
                c.innerHTML = `${firstMovie.querySelector('.movie-title').textContent} <span class="dim">// ${firstMovie.querySelector('.movie-date').textContent}</span>`;
            }
        })
        .catch(() => {});
});
</script>
