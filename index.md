---
layout: default
title: About
---

<div class="bio-container">
    <img src="https://files.horizon.pics/0e37ee6c-1ef1-42f5-bd17-eff9acba2211?a=480&region=eu-central&mime1=image&mime2=jpeg" alt="Kieran" class="profile-img">
    <div class="bio-text">
        <p><strong>Hi, I'm Kieran. 👋 Welcome to my personal website.</strong></p>
        <p>Overall swell guy, avid beer drinker & privacy advocate.</p>
        <p>Hobbies include playing video games, watching wrestling & photography.</p>
        <p>Server admin / moderator for <a href="https://standardnotes.com" target="_blank">Standard Notes</a> & <a href="https://proton.me" target="_blank">Proton</a>.</p>
    </div>
</div>

<div class="grid-container">
    <div class="grid-item">
        <h3>My Socials</h3>
        <ul>
            <li>X: <a href="https://x.com/PASSK3YS" target="_blank">@PASSK3YS</a></li>
            <li>Discord: passkeys</li>
            <li>Reddit: <a href="https://reddit.com/u/PASSK3YS" target="_blank">PASSK3YS</a></li>
        </ul>
    </div>
    <div class="grid-item">
        <h3>Music</h3>
        <ul>
            <li>Spotify: <a href="https://open.spotify.com/user/iplkfu8oka623d0rj6p7xsfyh?si=9452da697dd143af" target="_blank">Kieran Colfer</a></li>
            <li>Stats: <a href="https://stats.fm/passkey" target="_blank">Stats.fm</a></li>
        </ul>
    </div>
    <div class="grid-item">
        <h3>Gamertags</h3>
        <ul>
            <li>Xbox: <a href="https://www.xbox.com/en-GB/play/user/m00t" target="_blank">m00t</a></li>
            <li>Steam: <a href="https://steamcommunity.com/id/m00t316/" target="_blank">m00t316</a></li>
        </ul>
    </div>
    <div class="grid-item">
        <h3>Latest watch at Cinema</h3>
        <div id="latest-movie-container">
            <p style="font-size: 0.9em; color: var(--text-muted);">Loading latest...</p>
        </div>
    </div>
    <div class="grid-item">
        <h3>Latest post</h3>
        <div id="latest-blog-container">
            <p style="font-size: 0.9em; color: var(--text-muted);">Loading latest...</p>
        </div>
    </div>
</div>

<style>
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 30px;
}

.grid-item {
    background: var(--nav-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 20px;
    transition: transform 0.2s ease, border-color 0.2s ease;
}

.grid-item:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
}

.grid-item h3 {
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 1.1rem;
    border-bottom: 1px solid var(--border);
    padding-bottom: 10px;
}

.grid-item ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.grid-item li {
    margin-bottom: 8px;
}

.grid-item a {
    text-decoration: none;
    opacity: 0.8;
    transition: opacity 0.2s;
}

.grid-item a:hover {
    opacity: 1;
    color: var(--accent);
    text-decoration: underline;
}

.latest-movie-content {
    display: flex;
    align-items: center;
    gap: 15px;
    text-decoration: none !important;
}

.latest-movie-thumb {
    width: 60px;
    height: 90px;
    object-fit: cover;
    border-radius: 4px;
    border: 1px solid var(--border);
}

.latest-movie-info {
    display: flex;
    flex-direction: column;
}

.latest-movie-title {
    font-weight: bold;
    font-size: 1rem;
    margin: 0 0 5px 0;
    color: var(--text);
    line-height: 1.2;
}

.latest-movie-date {
    font-size: 0.8rem;
    color: var(--accent);
    margin: 0;
    text-transform: uppercase;
    font-weight: bold;
}

.latest-movie-link-wrapper, .latest-blog-link-wrapper {
    text-decoration: none !important;
    display: block;
    opacity: 1 !important;
}

.latest-movie-link-wrapper:hover .latest-movie-title, 
.latest-blog-link-wrapper:hover .latest-blog-title {
    color: var(--accent);
    text-decoration: underline;
}

.latest-blog-content {
    display: flex;
    flex-direction: column;
    padding: 10px 0;
}

.latest-blog-title {
    font-weight: bold;
    font-size: 1.2rem;
    margin: 0 0 8px 0;
    color: var(--text);
    line-height: 1.3;
}

.latest-blog-date {
    font-size: 0.85rem;
    color: var(--accent);
    margin: 0;
    text-transform: uppercase;
    font-weight: bold;
}
</style>

<script>
fetch('/cinema-watchlist/2026/')
    .then(response => response.text())
    .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const firstMovie = doc.querySelector('.movie-card');

        if (firstMovie) {
            const imgSrc = firstMovie.querySelector('.movie-thumbnail').src;
            const title = firstMovie.querySelector('.movie-title').textContent;
            const date = firstMovie.querySelector('.movie-date').textContent;
            const container = document.getElementById('latest-movie-container');
            
            container.innerHTML = `
                <a href="/cinema-watchlist/2026/" class="latest-movie-link-wrapper">
                    <div class="latest-movie-content">
                        <img src="${imgSrc}" alt="${title}" class="latest-movie-thumb">
                        <div class="latest-movie-info">
                            <p class="latest-movie-title">${title}</p>
                            <p class="latest-movie-date">${date}</p>
                        </div>
                    </div>
                </a>
            `;
        }
    })
    .catch(error => {
        document.getElementById('latest-movie-container').innerHTML = '<p style="font-size: 0.9em; color: var(--text-muted);">Watchlist unavailable</p>';
    });

fetch('/blog/')
    .then(response => response.text())
    .then(html => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const firstPost = doc.querySelector('.post-list > div');

        if (firstPost) {
            const titleElement = firstPost.querySelector('h2 a');
            const title = titleElement ? titleElement.textContent.trim() : 'Latest Post';
            const url = titleElement ? titleElement.getAttribute('href') : '/blog/';
            
            const dateElement = firstPost.querySelector('div');
            const date = dateElement ? dateElement.textContent.trim() : 'Recent';
            
            const container = document.getElementById('latest-blog-container');
            
            container.innerHTML = `
                <a href="${url}" class="latest-blog-link-wrapper">
                    <div class="latest-blog-content">
                        <p class="latest-blog-title">${title}</p>
                        <p class="latest-blog-date">${date}</p>
                    </div>
                </a>
            `;
        } else {
            document.getElementById('latest-blog-container').innerHTML = `
                <a href="/blog/" class="latest-blog-link-wrapper">
                    <div class="latest-blog-content">
                        <p class="latest-blog-title">Check out my latest thoughts</p>
                        <p class="latest-blog-date">Read the Blog →</p>
                    </div>
                </a>
            `;
        }
    })
    .catch(error => {
        document.getElementById('latest-blog-container').innerHTML = '<a href="/blog/" style="color: var(--accent);">Visit Blog</a>';
    });
</script>