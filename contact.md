---
layout: default
title: Contact
permalink: /contact/
---

<div class="bio-container">
    <div class="bio-text">
        <h1 style="margin: 0 0 10px 0; font-size: 2.2rem; font-weight: 800; letter-spacing: -0.5px;">Contact</h1>
        <p style="font-size: 1.1rem; opacity: 0.9; margin: 0;">
            Feel free to reach out via any of the secure platforms below.
        </p>
    </div>
</div>

<div class="soft-grid-container">

    <div class="soft-card">
        <h3 class="soft-header">Email</h3>
        <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: center;">
            <a href="mailto:hi@colfer.net" class="directory-interactive-text">hi@colfer.net</a>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 15px; margin-bottom: 0; line-height: 1.4;">
                If you use Proton Mail, all email communications will be end-to-end encrypted.
            </p>
        </div>
    </div>

    <div class="soft-card">
        <h3 class="soft-header">Secure Chat</h3>
        <div style="flex-grow: 1; display: flex; flex-direction: column; justify-content: center;">
            <a href="https://smp11.simplex.im/a#TyDMLK6GvVA62_9o1S4lvOVG-cBoBMyIUDxvHHpg5jA" target="_blank" class="directory-interactive-text">SimpleX Chat &rarr;</a>
        </div>
    </div>

    <div class="soft-card" style="grid-column: 1 / -1;">
        <h3 class="soft-header">Discord Community</h3>
        <div class="gamertag-list" style="flex-grow: 1; gap: 20px;">
            <span class="gamertag-label" style="width: auto;">Proton</span> 
            <a href="https://discord.com/invite/proton" target="_blank" class="directory-interactive-text">Join Server</a>
            
            <span class="gamertag-label" style="width: auto;">Standard Notes</span> 
            <a href="https://discord.com/invite/fxjJFxkRkY" target="_blank" class="directory-interactive-text">Join Server</a>
        </div>
    </div>

</div>

<style>
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

.soft-grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
}

.soft-card {
    background: var(--nav-bg);
    border-radius: 24px;
    padding: 30px;
    display: flex;
    flex-direction: column;
    box-shadow: 0 8px 30px rgba(0,0,0,0.04);
    border: 1px solid rgba(128,128,128,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

[data-theme="dark"] .soft-card {
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.05);
}

.soft-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.08);
    border-color: var(--accent);
}

[data-theme="dark"] .soft-card:hover {
    box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}

.soft-header {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: var(--text-muted);
    margin: 0 0 20px 0;
    font-weight: 700;
}

.directory-interactive-text {
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--text);
    text-decoration: none;
    transition: color 0.2s ease;
}

.directory-interactive-text:hover {
    color: var(--accent);
    text-decoration: underline;
}

.gamertag-list {
    display: grid;
    grid-template-columns: 140px 1fr;
    gap: 15px 10px;
    align-items: center;
}

.gamertag-label {
    opacity: 0.6; 
    font-size: 0.9em;
    color: var(--text);
    text-transform: uppercase;
    letter-spacing: 1px;
}

@media (max-width: 600px) {
    .soft-grid-container {
        grid-template-columns: 1fr;
    }
    .gamertag-list {
        grid-template-columns: 1fr;
        gap: 5px;
    }
    .gamertag-label {
        margin-top: 10px;
    }
}
</style>