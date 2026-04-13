---
layout: default
title: About
---

<style>
.hero-section {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 2rem 0 4rem 0;
}

.hero-greeting {
    font-size: 3.5rem;
    font-weight: 700;
    color: var(--text-heading);
    margin-bottom: 1rem;
    line-height: 1.1;
    letter-spacing: -1.5px;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: var(--text-main);
    max-width: 600px;
    margin-bottom: 2rem;
    font-weight: 300;
}

.hero-links {
    display: flex;
    gap: 1.5rem;
}

.primary-btn {
    background-color: var(--accent-cyan);
    color: var(--bg-base);
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    font-weight: 700;
    text-decoration: none;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.primary-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px var(--accent-glow);
    color: var(--bg-base);
}

.secondary-btn {
    background-color: transparent;
    color: var(--text-heading);
    padding: 0.8rem 1.5rem;
    border-radius: 8px;
    font-weight: 600;
    border: 1px solid var(--border-color);
    text-decoration: none;
    transition: border-color 0.2s ease, color 0.2s ease;
}

.secondary-btn:hover {
    border-color: var(--accent-cyan);
    color: var(--accent-cyan);
}

.content-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.card-title {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: var(--text-heading);
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.card-text {
    color: var(--text-muted);
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}

.card-link {
    font-weight: 600;
    font-size: 0.9rem;
    color: var(--accent-cyan);
    text-transform: uppercase;
    letter-spacing: 1px;
    display: inline-flex;
    align-items: center;
    gap: 5px;
}

.card-link:hover {
    color: var(--accent-blue);
}

@media (max-width: 768px) {
    .hero-greeting {
        font-size: 2.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
    }
    
    .hero-links {
        flex-direction: column;
        width: 100%;
        gap: 1rem;
    }
    
    .primary-btn, .secondary-btn {
        width: 100%;
        text-align: center;
        box-sizing: border-box;
    }
}
</style>

<div class="hero-section">
    <h1 class="hero-greeting">Hi, I'm Kieran. 👋</h1>
    <p class="hero-subtitle">I build things for the web, advocate for privacy, and tinker with open-source tech. Welcome to my digital space.</p>
    
    <div class="hero-links">
        <a href="/contact/" class="primary-btn">Get in touch</a>
        <a href="/blog/" class="secondary-btn">Read my blog</a>
    </div>
</div>

<div class="content-grid">
    <div class="card">
        <h2 class="card-title">Latest Tools</h2>
        <p class="card-text">Explore the custom scripts, widgets, and workflow improvements I've been building recently.</p>
        <a href="/tools/" class="card-link">View Tools →</a>
    </div>

    <div class="card">
        <h2 class="card-title">Documentation</h2>
        <p class="card-text">My personal wiki. A collection of guides, server setups, and technical notes I refer back to.</p>
        <a href="/docs/" class="card-link">Read Docs →</a>
    </div>
</div>