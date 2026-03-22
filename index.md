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
    <div class="grid-item" id="spotify-card" style="grid-column: 1 / -1; position: relative; overflow: hidden;">
        <div id="spotify-bg-layer"></div>
        <div style="position: relative; z-index: 1;">
            <h3>I'm currently listening to...</h3>
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
    filter: blur(25px) brightness(0.35);
    z-index: 0;
    opacity: 0;
    transition: opacity 0.8s ease, background-image 0.8s ease;
    pointer-events: none;
}

.spotify-active #spotify-bg-layer {
    opacity: 1;
}

.spotify-active h3 {
    color: #ffffff !important;
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
const lastFmUsername = 'passkeys';
const lastFmApiKey = 'f2c5cc826164e5dd05f8fb573083b524';
let currentSpotifyState = '';

function fetchSpotifyData() {
    fetch(`https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=${lastFmUsername}&api_key=${lastFmApiKey}&format=json&limit=1`)
        .then(response => response.json())
        .then(data => {
            const spotifyCard = document.getElementById('spotify-card');
            const spotifyBgLayer = document.getElementById('spotify-bg-layer');

            if (data.error || !data.recenttracks || !data.recenttracks.track || data.recenttracks.track.length === 0) {
                if (currentSpotifyState !== 'error') {
                    document.getElementById('spotify-container').innerHTML = '<p style="font-size: 0.9em; color: var(--text-muted);">Spotify unavailable</p>';
                    spotifyCard.classList.remove('spotify-active');
                    currentSpotifyState = 'error';
                }
                return;
            }

            const track = data.recenttracks.track[0];
            const title = track.name;
            const artist = track.artist['#text'];
            const img = track.image[3]['#text'] || track.image[2]['#text'] || 'https://via.placeholder.com/85x85/1a1a1a/ffffff?text=Spotify';
            const isPlaying = track['@attr'] && track['@attr'].nowplaying === 'true';
            
            const newState = `${title}-${artist}-${isPlaying}`;
            if (currentSpotifyState === newState) {
                return; 
            }
            currentSpotifyState = newState;
            
            const searchQuery = encodeURIComponent(`${title} ${artist}`);
            const url = `https://open.spotify.com/search/${searchQuery}`;
            
            spotifyBgLayer.style.backgroundImage = `url('${img}')`;
            
            let statusTextHTML = '';
            
            if (isPlaying) {
                spotifyCard.classList.add('spotify-active');
                statusTextHTML = `Now Playing <span class="playing-indicator"><span class="bar"></span><span class="bar"></span><span class="bar"></span></span>`;
            } else {
                spotifyCard.classList.add('spotify-active');
                let timeString = '';
                if (track.date && track.date.uts) {
                    const diffMins = Math.floor((Date.now() - (track.date.uts * 1000)) / 60000);
                    if (diffMins < 1) timeString = ' • JUST NOW';
                    else if (diffMins < 60) timeString = ` • ${diffMins} MINS AGO`;
                    else if (diffMins < 1440) timeString = ` • ${Math.floor(diffMins / 60)} HRS AGO`;
                    else timeString = ` • ${Math.floor(diffMins / 1440)} DAYS AGO`;
                }
                statusTextHTML = `Last Played${timeString}`;
            }
            
            const statusColor = isPlaying ? '#1DB954' : 'rgba(255, 255, 255, 0.7)';

            document.getElementById('spotify-container').innerHTML = `
                <a href="${url}" target="_blank" class="latest-movie-link-wrapper">
                    <div class="latest-movie-content">
                        <img src="${img}" alt="${title}" class="spotify-thumb-large">
                        <div class="latest-movie-info">
                            <p style="font-size: 0.75rem; font-weight: bold; text-transform: uppercase; color: ${statusColor}; margin: 0 0 4px 0; display: flex; align-items: center;">${statusTextHTML}</p>
                            <p class="latest-movie-title">${title}</p>
                            <p class="latest-movie-date" style="text-transform: none;">${artist}</p>
                        </div>
                    </div>
                </a>
            `;
        })
        .catch(() => {});
}

fetchSpotifyData();
setInterval(fetchSpotifyData, 5000);

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
            
            document.getElementById('latest-movie-container').innerHTML = `
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
    .catch(() => {
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
            
            document.getElementById('latest-blog-container').innerHTML = `
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
    .catch(() => {
        document.getElementById('latest-blog-container').innerHTML = '<a href="/blog/" style="color: var(--accent);">Visit Blog</a>';
    });
</script>