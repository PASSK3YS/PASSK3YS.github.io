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
        <h3>My socials</h3>
        <ul>
            <li>X: <a href="https://x.com/PASSK3YS" target="_blank">@PASSK3YS</a></li>
            <li>Discord: passkeys</li>
            <li>Reddit: <a href="https://reddit.com/u/PASSK3YS" target="_blank">PASSK3YS</a></li>
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
        <h3>Guestbook</h3>
        <a href="/guestbook/" class="latest-blog-link-wrapper">
            <div class="latest-blog-content">
                <p class="latest-blog-title">Sign my guestbook</p>
            </div>
        </a>
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
    <div class="grid-item">
        <h3>Last played game</h3>
        <div id="xbox-container">
            <p style="font-size: 0.9em; color: var(--text-muted);">Loading Xbox...</p>
        </div>
    </div>
    <div class="grid-item" id="spotify-card" style="grid-column: 1 / -1; position: relative; overflow: hidden;">
        <div id="spotify-bg-layer"></div>
        <div style="position: relative; z-index: 1;">
            <div class="spotify-header">
                <h3>I'm currently listening to...</h3>
                <a href="https://open.spotify.com/user/iplkfulloba6z3ld0rgbp?si=9452da897dd143af" target="_blank" class="spotify-logo-link">
                    <svg viewBox="0 0 24 24" width="26" height="26" fill="#1DB954">
                        <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.84.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.6.18-1.2.72-1.38 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"/>
                    </svg>
                </a>
            </div>
            <div id="spotify-container">
                <p style="font-size: 0.9em; color: var(--text-muted);">Loading Spotify...</p>
            </div>
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
    transition: color 0.5s ease, border-color 0.5s ease;
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

.spotify-thumb-large {
    width: 85px;
    height: 85px;
    object-fit: cover;
    border-radius: 8px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.4);
    border: none;
}

.latest-movie-info {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.latest-movie-title {
    font-weight: bold;
    font-size: 1rem;
    margin: 0 0 5px 0;
    color: var(--text);
    line-height: 1.2;
    transition: color 0.5s ease;
}

.latest-movie-date {
    font-size: 0.8rem;
    color: var(--accent);
    margin: 0;
    text-transform: uppercase;
    font-weight: bold;
    transition: color 0.5s ease;
}

.latest-movie-link-wrapper, .latest-blog-link-wrapper {
    text-decoration: none !important;
    border-bottom: none !important;
    display: block;
    opacity: 1 !important;
    position: relative;
    overflow: hidden;
    padding-bottom: 5px;
}

.latest-movie-link-wrapper:hover, 
.latest-blog-link-wrapper:hover {
    text-decoration: none !important;
    border-bottom: none !important;
}

.latest-movie-link-wrapper:hover .latest-movie-title, 
.latest-blog-link-wrapper:hover .latest-blog-title {
    color: var(--accent) !important;
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

.playing-indicator {
    display: inline-flex;
    align-items: flex-end;
    gap: 3px;
    height: 10px;
    margin-left: 6px;
}

.playing-indicator .bar {
    width: 3px;
    background-color: #1DB954;
    animation: eq-bounce 1s infinite ease-in-out;
    transform-origin: bottom;
    border-radius: 2px;
}

.playing-indicator .bar:nth-child(1) { height: 8px; animation-delay: 0s; }
.playing-indicator .bar:nth-child(2) { height: 11px; animation-delay: 0.2s; }
.playing-indicator .bar:nth-child(3) { height: 7px; animation-delay: 0.4s; }

@keyframes eq-bounce {
    0%, 100% { transform: scaleY(0.4); }
    50% { transform: scaleY(1); }
}

#spotify-bg-layer {
    position: absolute;
    top: -30px;
    left: -30px;
    right: -30px;
    bottom: -30px;
    background-size: cover;
    background-position: center;
    filter: blur(25px) brightness(0.45);
    z-index: 0;
    opacity: 0;
    transition: opacity 0.8s ease, background-image 0.8s ease;
    pointer-events: none;
}

.spotify-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid var(--border);
    transition: border-color 0.5s ease;
}

.grid-item .spotify-header h3 {
    margin: 0;
    padding: 0;
    border-bottom: none;
}

.spotify-logo-link {
    display: flex;
    align-items: center;
    opacity: 0.8;
    transition: opacity 0.2s, transform 0.2s;
    text-decoration: none !important;
    border-bottom: none !important;
}

.spotify-logo-link:hover {
    opacity: 1;
    transform: scale(1.1);
    text-decoration: none !important;
    border-bottom: none !important;
}

.spotify-active #spotify-bg-layer {
    opacity: 1;
}

.spotify-active h3 {
    color: #ffffff !important;
}

.spotify-active .spotify-header {
    border-bottom-color: rgba(255, 255, 255, 0.2) !important;
}

.spotify-active .latest-movie-title {
    color: #ffffff !important;
}

.spotify-active .latest-movie-date {
    color: rgba(255, 255, 255, 0.7) !important;
}
</style>

<script>
const workerUrl = 'https://xbox-tracker.snowy-scene-5750.workers.dev';
let currentSpotifyState = '';

function fetchData() {
    fetch(workerUrl)
        .then(res => res.json())
        .then(data => {
            if (data.xbox) {
                document.getElementById('xbox-container').innerHTML = `
                    <a href="https://account.xbox.com/en-gb/profile?gamertag=m00t" target="_blank" class="latest-movie-link-wrapper">
                        <div class="latest-movie-content">
                            <img src="${data.xbox.image}" alt="${data.xbox.name}" class="latest-movie-thumb">
                            <div class="latest-movie-info">
                                <p class="latest-movie-title">${data.xbox.name}</p>
                                <p class="latest-movie-date">Xbox</p>
                            </div>
                        </div>
                    </a>`;
            }

            if (data.music && typeof data.music === 'object') {
                const card = document.getElementById('spotify-card');
                const bg = document.getElementById('spotify-bg-layer');
                const newState = `${data.music.title}-${data.music.isPlaying}`;
                
                if (currentSpotifyState !== newState) {
                    currentSpotifyState = newState;
                    bg.style.backgroundImage = `url('${data.music.image}')`;
                    card.classList.add('spotify-active');

                    let statusText = data.music.isPlaying ? 
                        `Now Playing <span class="playing-indicator"><span class="bar"></span><span class="bar"></span><span class="bar"></span></span>` : 
                        "Last Played";

                    if (!data.music.isPlaying && data.music.uts) {
                        const diffMins = Math.floor((Date.now() - (data.music.uts * 1000)) / 60000);
                        if (diffMins < 1) statusText += ' • JUST NOW';
                        else if (diffMins < 60) statusText += ` • ${diffMins} MINS AGO`;
                        else if (diffMins < 1440) statusText += ` • ${Math.floor(diffMins / 60)} HRS AGO`;
                        else statusText += ` • ${Math.floor(diffMins / 1440)} DAYS AGO`;
                    }

                    const searchUrl = `https://open.spotify.com/search/${encodeURIComponent(data.music.title + ' ' + data.music.artist)}`;
                    const statusColor = data.music.isPlaying ? '#1DB954' : 'rgba(255, 255, 255, 0.7)';

                    document.getElementById('spotify-container').innerHTML = `
                        <a href="${searchUrl}" target="_blank" class="latest-movie-link-wrapper">
                            <div class="latest-movie-content">
                                <img src="${data.music.image}" alt="${data.music.title}" class="spotify-thumb-large">
                                <div class="latest-movie-info">
                                    <p style="font-size: 0.75rem; font-weight: bold; text-transform: uppercase; color: ${statusColor}; margin: 0 0 4px 0; display: flex; align-items: center;">${statusText}</p>
                                    <p class="latest-movie-title">${data.music.title}</p>
                                    <p class="latest-movie-date" style="text-transform: none;">${data.music.artist}</p>
                                </div>
                            </div>
                        </a>`;
                }
            }
        })
        .catch(err => console.error("Fetch error:", err));
}

fetchData();
setInterval(fetchData, 5000);

fetch('/cinema-watchlist/2026/')
    .then(res => res.text())
    .then(html => {
        const firstMovie = new DOMParser().parseFromString(html, 'text/html').querySelector('.movie-card');
        if (firstMovie) {
            document.getElementById('latest-movie-container').innerHTML = `
                <a href="/cinema-watchlist/2026/" class="latest-movie-link-wrapper">
                    <div class="latest-movie-content">
                        <img src="${firstMovie.querySelector('.movie-thumbnail').src}" alt="${firstMovie.querySelector('.movie-title').textContent}" class="latest-movie-thumb">
                        <div class="latest-movie-info">
                            <p class="latest-movie-title">${firstMovie.querySelector('.movie-title').textContent}</p>
                            <p class="latest-movie-date">${firstMovie.querySelector('.movie-date').textContent}</p>
                        </div>
                    </div>
                </a>`;
        }
    });

fetch('/blog/')
    .then(res => res.text())
    .then(html => {
        const firstPost = new DOMParser().parseFromString(html, 'text/html').querySelector('.post-list > div');
        if (firstPost) {
            const link = firstPost.querySelector('h2 a');
            document.getElementById('latest-blog-container').innerHTML = `
                <a href="${link.getAttribute('href')}" class="latest-blog-link-wrapper">
                    <div class="latest-blog-content">
                        <p class="latest-blog-title">${link.textContent.trim()}</p>
                        <p class="latest-blog-date">${firstPost.querySelector('div').textContent.trim()}</p>
                    </div>
                </a>`;
        }
    });
</script>