---
layout: default
title: Cinema Stats
permalink: /cinema-stats/
---

<style>
.cs-prompt-line { display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; flex-wrap: wrap; font-family: 'JetBrains Mono', monospace; }
.cs-prompt { color: var(--accent); white-space: nowrap; }
.cs-command-name { color: var(--accent); }
.cs-cmd { color: var(--text); }

.cs-panels { display: grid; grid-template-columns: 1fr; gap: 22px; margin-top: 26px; }

.cs-panel {
    background: var(--nav-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 20px 22px;
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}
.cs-panel:hover {
    transform: translateY(-3px);
    border-color: var(--accent);
    box-shadow: 0 0 20px -6px var(--accent-glow);
}

.cs-panel-head {
    display: flex; gap: 10px; align-items: baseline;
    font-family: 'JetBrains Mono', monospace;
    margin: 0 0 14px 0;
}
.cs-panel-head .prompt { color: var(--accent); white-space: nowrap; font-size: 0.95rem; font-weight: 700; }
.cs-panel-head h2 {
    margin: 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--accent);
    text-transform: lowercase;
    letter-spacing: 0.5px;
}

.cs-hero {
    display: flex;
    gap: 26px;
    flex-wrap: wrap;
}
.cs-stat { min-width: 110px; }
.cs-stat .stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--text-muted);
    margin-bottom: 4px;
}
.cs-stat .stat-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--text);
    line-height: 1.1;
}
.cs-stat .stat-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--text-muted);
    margin-top: 2px;
}

/* horizontal bar "chart" rows */
.cs-bar-row {
    display: grid;
    grid-template-columns: 52px 1fr 96px;
    gap: 10px;
    align-items: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    padding: 6px 0;
}
.cs-bar-year { color: var(--text-muted); font-weight: 700; }
.cs-bar-track {
    background: var(--bg-solid);
    border: 1px solid var(--border);
    border-radius: 3px;
    overflow: hidden;
    height: 14px;
}
.cs-bar-fill {
    height: 100%;
    background: var(--accent);
    box-shadow: 0 0 10px var(--accent-glow);
    border-radius: 2px;
}
.cs-bar-metric { color: var(--text); white-space: nowrap; }
.cs-bar-metric .dim { color: var(--text-muted); }

.cs-list { list-style: none; padding: 0; margin: 0; }
.cs-list li {
    display: flex;
    gap: 8px;
    align-items: baseline;
    padding: 5px 0;
    font-size: 0.85rem;
    color: var(--text);
}
.cs-list li::before {
    content: ">>";
    color: var(--accent);
    opacity: 0.6;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8em;
}
.cs-list .rank { color: var(--text-muted); font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; min-width: 2.4em; }

.cs-mono { font-family: 'JetBrains Mono', monospace; }
.cs-dim { color: var(--text-muted); }

.cs-back {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--text-muted);
    text-decoration: none;
    letter-spacing: 0.5px;
    margin-bottom: 18px;
    transition: color 0.2s ease, text-shadow 0.2s ease;
}
.cs-back:hover { color: var(--accent); text-shadow: 0 0 12px var(--accent-glow); }

.term-cursor {
    display: inline-block;
    width: 0.55em; height: 1.05em;
    background: var(--accent);
    vertical-align: text-bottom;
    animation: cs-blink 1s step-end infinite;
}
@keyframes cs-blink { 50% { opacity: 0; } }
.tline { opacity: 0; animation: cs-in 0.4s ease forwards; }
@keyframes cs-in { to { opacity: 1; } }
</style>

<div class="cs-mono tline">
<a href="/cinema-watchlist/2026/" class="cs-back">&larr; cd /cinema/</a>

<div class="cs-prompt-line">
    <span class="cs-prompt">$</span><span class="cs-cmd"><span class="cs-command-name">cinema-stats</span> --all-years</span>
</div>

{% comment %}========== aggregate prep, computed once =========={% endcomment %}
{% assign all_movies = site.data["movie-ratings"] %}
{% assign total = all_movies | size %}

{% assign sum = 0 %}
{% assign decade_counter = 0 %}
{% for movie in all_movies %}
    {% assign value = movie.rating | slice: 0, 2 | plus: 0 %}
    {% assign sum = sum | plus: value %}
{% endfor %}
{% assign grand_avg = sum | divided_by: 110.0 %}

{% comment %}================== hero stats =================={% endcomment %}
<div class="cs-panels">

<div class="cs-panel tline">
    <div class="cs-panel-head"><span class="prompt">$</span><h2>cinema --summary</h2></div>
    <div class="cs-hero">
        <div class="cs-stat">
            <div class="stat-label">Films rated</div>
            <div class="stat-value">{{ total }}</div>
            <div class="stat-sub">2022 &ndash; 2026</div>
        </div>
        <div class="cs-stat">
            <div class="stat-label">Average score</div>
            <div class="stat-value">{{ grand_avg | round: 2 }}/10</div>
            <div class="stat-sub">across all years</div>
        </div>
        <div class="cs-stat">
            <div class="stat-label">First logged</div>
            <div class="stat-value">2022</div>
            <div class="stat-sub">DC League of Super-Pets</div>
        </div>
    </div>
</div>

{% comment %}================== per-year breakdown =================={% endcomment %}
<div class="cs-panel tline">
    <div class="cs-panel-head"><span class="prompt">$</span><h2>cinema-stats --by-year</h2></div>

    {% assign y2026 = all_movies | where: "year", 2026 %}
    {% assign y2025 = all_movies | where: "year", 2025 %}
    {% assign y2024 = all_movies | where: "year", 2024 %}
    {% assign y2023 = all_movies | where: "year", 2023 %}
    {% assign y2022 = all_movies | where: "year", 2022 %}

    {% assign c2026 = y2026 | size %}
    {% assign c2025 = y2025 | size %}
    {% assign c2024 = y2024 | size %}
    {% assign c2023 = y2023 | size %}
    {% assign c2022 = y2022 | size %}

    {% comment %}average per year: ratings look like "8/10", so slice the leading number{% endcomment %}
    {% assign s2026 = 0 %}{% assign s2025 = 0 %}{% assign s2024 = 0 %}{% assign s2023 = 0 %}{% assign s2022 = 0 %}
    {% for m in y2026 %}{% assign s2026 = s2026 | plus: m.rating[0] %}{% endfor %}
    {% for m in y2025 %}{% assign s2025 = s2025 | plus: m.rating[0] %}{% endfor %}
    {% for m in y2024 %}{% assign s2024 = s2024 | plus: m.rating[0] %}{% endfor %}
    {% for m in y2023 %}{% assign s2023 = s2023 | plus: m.rating[0] %}{% endfor %}
    {% for m in y2022 %}{% assign s2022 = s2022 | plus: m.rating[0] %}{% endfor %}

    {% assign a2026 = s2026 | divided_by: c2026 | round: 2 %}
    {% assign a2025 = s2025 | divided_by: c2025 | round: 2 %}
    {% assign a2024 = s2024 | divided_by: c2024 | round: 2 %}
    {% assign a2023 = s2023 | divided_by: c2023 | round: 2 %}
    {% assign a2022 = s2022 | divided_by: c2022 | round: 2 %}

    {% comment %}bar widths scaled so 10/10 = 100%; widths in px via inline style{% endcomment %}
    {% assign w2026 = a2026 | times: 10.0 %}
    {% assign w2025 = a2025 | times: 10.0 %}
    {% assign w2024 = a2024 | times: 10.0 %}
    {% assign w2023 = a2023 | times: 10.0 %}
    {% assign w2022 = a2022 | times: 10.0 %}

    <div class="cs-bar-row"><span class="cs-bar-year">2026</span><div class="cs-bar-track"><div class="cs-bar-fill" style="width: {{ w2026 }}%"></div></div><span class="cs-bar-metric">{{ a2026 }}/10 <span class="dim">({{ c2026 }} films)</span></span></div>
    <div class="cs-bar-row"><span class="cs-bar-year">2025</span><div class="cs-bar-track"><div class="cs-bar-fill" style="width: {{ w2025 }}%"></div></div><span class="cs-bar-metric">{{ a2025 }}/10 <span class="dim">({{ c2025 }} films)</span></span></div>
    <div class="cs-bar-row"><span class="cs-bar-year">2024</span><div class="cs-bar-track"><div class="cs-bar-fill" style="width: {{ w2024 }}%"></div></div><span class="cs-bar-metric">{{ a2024 }}/10 <span class="dim">({{ c2024 }} films)</span></span></div>
    <div class="cs-bar-row"><span class="cs-bar-year">2023</span><div class="cs-bar-track"><div class="cs-bar-fill" style="width: {{ w2023 }}%"></div></div><span class="cs-bar-metric">{{ a2023 }}/10 <span class="dim">({{ c2023 }} films)</span></span></div>
    <div class="cs-bar-row"><span class="cs-bar-year">2022</span><div class="cs-bar-track"><div class="cs-bar-fill" style="width: {{ w2022 }}%"></div></div><span class="cs-bar-metric">{{ a2022 }}/10 <span class="dim">({{ c2022 }} films)</span></span></div>
</div>

{% comment %}================== leaderboard =================={% endcomment %}
<div class="cs-panel tline">
    <div class="cs-panel-head"><span class="prompt">$</span><h2>cinema-stats --top-rated</h2></div>
    <ol class="cs-list">
        {% assign perfects = all_movies | where_exp: "m", "m.rating == '10/10'" %}
        {% assign tens = perfects | size %}
        {% for m in all_movies reversed %}
            {% if m.rating == '10/10' %}
                <li><span class="rank">[{{ forloop.index }}]</span> {{ m.title }} <span class="cs-dim">(2024)</span></li>
            {% endif %}
        {% endfor %}
    </ol>
</div>

</div>

<div class="cs-mono tline" style="margin-top: 22px;">
    <span class="cs-prompt">$</span><span class="term-cursor"></span>
</div>
</div>
