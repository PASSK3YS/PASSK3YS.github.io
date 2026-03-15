---
layout: default
title: About
---

<div class="bio-container">
    <img src="https://files.horizon.pics/0e37ee6c-1ef1-42f5-bd17-eff9acba2211?a=480&region=eu-central&mime1=image&mime2=jpeg" alt="Kieran" class="profile-img">
    <div class="bio-text">
        <p><strong>Hi, I'm Kieran. 👋 Welcome to my personal website.</strong></p>
        <p>Overall swell guy, avid beer drinker & privacy advocate.</p>
        <p>Hobbies include playing video games, watching wrestling & <a href="https://drive.proton.me/urls/A9J5Q9MZ34#Ht8OgEvmUwp1" target="_blank">photography</a>.</p>
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
</style>