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

/* horizontal bar rows */
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

{% comment %}=====================================================
     Aggregate prep — all numbers derived from the data file.
     Ratings look like "8/10": strip "/10" and coerce to number.
     ====================================================={% endcomment %}
{% assign all_movies = site.data["movie-ratings"] %}
{% assign total = all_movies | size %}

{% assign grand_sum = 0 %}
{% for movie in all_movies %}
    {% assign grand_sum = grand_sum | plus: movie.year_num %}
{% endfor %}
{% comment %}above loop is a placeholder pattern only; real sum below{% endcomment %}
{% assign grand_sum = 0 %}
{% for movie in all_movies %}
    {% assign val = movie.rating | remove: "/10" | plus: 0 %}
    {% assign grand_sum = grand_sum | plus: val %}
{% endfor %}
{% assign grand_avg_times100 = grand_sum | times: 100 | divided_by: total %}
{% assign grand_avg_whole = grand_avg_times100 | divided_by: 100 %}
{% assign grand_avg_frac = grand_avg_times100 | modulo: 100 %}

<div class="cs-panels">

{% comment %}================== hero stats =================={% endcomment %}
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
            <div class="stat-value">{{ grand_avg_whole }}.{% if grand_avg_frac < 10 %}0{% endif %}{{ grand_avg_frac }}/10</div>
            <div class="stat-sub">across all years</div>
        </div>
    </div>
</div>

{% comment %}================== per-year breakdown ==================
     Loop over years present in the data so future years appear
     automatically. Bar width = avg rating × 10 (so 10/10 = 100%).
     ====================================================={% endcomment %}
<div class="cs-panel tline">
    <div class="cs-panel-head"><span class="prompt">$</span><h2>cinema-stats --by-year</h2></div>

    {% assign years = all_movies | map: "year" | uniq | sort %}
    {% for yr in years reversed %}
        {% assign year_movies = all_movies | where: "year", yr %}
        {% assign year_count = year_movies | size %}
        {% assign year_sum = 0 %}
        {% for m in year_movies %}
            {% assign v = m.rating | remove: "/10" | plus: 0 %}
            {% assign year_sum = year_sum | plus: v %}
        {% endfor %}
        {% assign avg_x100 = year_sum | times: 100 | divided_by: year_count %}
        {% assign avg_whole = avg_x100 | divided_by: 100 %}
        {% assign avg_frac = avg_x100 | modulo: 100 %}
        {% assign bar_width = avg_whole | times: 10 %}
        <div class="cs-bar-row">
            <span class="cs-bar-year">{{ yr }}</span>
            <div class="cs-bar-track"><div class="cs-bar-fill" style="width: {{ bar_width }}%"></div></div>
            <span class="cs-bar-metric">{{ avg_whole }}.{% if avg_frac < 10 %}0{% endif %}{{ avg_frac }}/10 <span class="dim">({{ year_count }} films)</span></span>
        </div>
    {% endfor %}
</div>

{% comment %}================== top-rated =================={% endcomment %}
<div class="cs-panel tline">
    <div class="cs-panel-head"><span class="prompt">$</span><h2>cinema-stats --top-rated</h2></div>
    <ul class="cs-list">
        {% assign rank = 0 %}
        {% for m in all_movies %}
            {% if m.rating == "10/10" %}
                {% assign rank = rank | plus: 1 %}
                <li><span class="rank">[{{ rank }}]</span> {{ m.title }} <span class="cs-dim">(watched {{ m.notes | remove: "Watched " }})</span></li>
            {% endif %}
        {% endfor %}
        {% if rank == 0 %}<li><span class="cs-dim">no perfect scores yet</span></li>{% endif %}
    </ul>
</div>

</div>

<div class="cs-mono tline" style="margin-top: 22px;">
    <span class="cs-prompt">$</span><span class="term-cursor"></span>
</div>
</div>
