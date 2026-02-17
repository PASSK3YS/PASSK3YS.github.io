---
layout: default
title: Contact
permalink: /contact/
---

<div class="page-content">
    <h1>Contact</h1>

    <div class="grid-container">
        
        <div class="grid-item">
            <h3>Email</h3>
            <ul>
                <li><a href="mailto:hi@colfer.net" target="blank">hi@colfer.net</a></li>
            </ul>
        </div>

        <div class="grid-item">
            <h3>Secure Chat</h3>
            <ul>
                <li><a href="https://smp11.simplex.im/a#TyDMLK6GvVA62_9o1S4lvOVG-cBoBMyIUDxvHHpg5jA" target="_blank">SimpleX Chat</a></li>
            </ul>
        </div>

        <div class="grid-item">
            <h3>Discord</h3>
            <ul>
                <li><a href="https://discord.com/invite/proton" target="_blank">Proton Discord Server</a></li>
                <li><a href="https://discord.com/invite/fxjJFxkRkY" target="_blank">Standard Notes Discord Server</a></li>
            </ul>
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
</style>