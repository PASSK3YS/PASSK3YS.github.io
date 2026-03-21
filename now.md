---
layout: default
title: Now
permalink: /now/
---

<style>
  .now-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-top: 40px;
    margin-bottom: 40px;
  }
  .now-card {
    background-color: rgba(255, 255, 255, 0.02);
    border: 1px solid var(--border-color, #30363d);
    border-radius: 12px;
    padding: 24px;
    transition: transform 0.2s ease, border-color 0.2s ease;
  }
  .now-card:hover {
    border-color: #8b949e;
    transform: translateY(-2px);
  }
  .now-card h2 {
    font-size: 1.2rem;
    margin-top: 0;
    margin-bottom: 16px;
    border-bottom: none;
    display: flex;
    align-items: center;
    gap: 8px;
    padding-bottom: 0;
  }
  .now-card ul {
    margin: 0;
    padding-left: 20px;
  }
  .now-card li {
    margin-bottom: 10px;
    opacity: 0.9;
    line-height: 1.4;
  }
  .now-card li:last-child {
    margin-bottom: 0;
  }
</style>

<div class="page-content">
  <h1 style="margin-top: 0; margin-bottom: 10px;">What I'm doing right now</h1>
  <p style="opacity: 0.7; font-size: 1.1rem;">A snapshot of what is currently occupying my time and attention.</p>

  <div class="now-grid">
    
    <div class="now-card">
      <h2>💻 Working on</h2>
      <ul>
        <li>My website</li>
        <li>Creating new <strong>Standard Notes</strong> themes</li>
      </ul>
    </div>

    <div class="now-card">
      <h2>🎮 Playing</h2>
      <ul>
        <li><strong>Avatar: Frontiers of Pandora</strong></li>
        <li><strong>Fortnite</strong></li>
        <li><strong>Kingdom Come: Deliverance II</strong></li>
      </ul>
    </div>

    <div class="now-card">
      <h2>📺 Watching</h2>
      <ul>
        <li><strong>Daredevil: Born Again</strong> on Disney Plus</li>
        <li><strong>The Dinosaurs</strong> on Netflix</li>
      </ul>
    </div>

    <div class="now-card">
      <h2>🎧 Listening to</h2>
      <ul>
        <li>My <strong>Supermix</strong> playlist on YouTube Music</li>
      </ul>
    </div>

  </div>

  <div style="margin-top: 60px; padding-top: 20px; border-top: 1px solid var(--border-color, #30363d);">
    <p style="font-size: 0.85rem; opacity: 0.6; text-transform: uppercase; letter-spacing: 1px; margin: 0;">
      Last updated: {{ site.time | date: "%d-%m-%Y" }}
    </p>
  </div>
</div>