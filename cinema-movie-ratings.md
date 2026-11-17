---
layout: default
title: Cinema Movie Ratings
permalink: /cinema-movie-ratings/
---

<style>
    .section-cmd { margin-top: 26px; font-family: 'JetBrains Mono', monospace; }
    .prompt-line { display: flex; gap: 10px; align-items: baseline; margin-bottom: 6px; flex-wrap: wrap; }
    .prompt { color: var(--accent); white-space: nowrap; }
    .cmd { color: var(--text); }
    .command-name { color: var(--accent); }
    .dim { color: var(--text-muted); }

    .ratings-head {
        font-family: 'JetBrains Mono', monospace;
        margin: 0 0 20px 0;
    }

    .yr-filter select {
        background: transparent;
        color: var(--accent);
        border: 1px dashed var(--border);
        border-radius: 4px;
        padding: 6px 14px;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        font-weight: 700;
        cursor: pointer;
        outline: none;
        transition: all 0.2s ease;
        appearance: none;
        -webkit-appearance: none;
    }

    .yr-filter select option {
        background-color: var(--bg-solid);
        color: var(--accent);
    }

    .yr-filter select:hover, .yr-filter select:focus {
        border-color: var(--accent);
        border-style: solid;
        box-shadow: 0 0 10px var(--accent-glow);
    }

    .featured-movie {
        display: flex;
        gap: 20px;
        background: var(--nav-bg);
        border: 1px solid var(--border);
        border-radius: 6px;
        padding: 18px;
        margin-bottom: 26px;
        align-items: center;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
    }

    .featured-movie:hover {
        transform: translateY(-3px);
        border-color: var(--accent);
        box-shadow: 0 0 20px -6px var(--accent-glow);
    }

    .featured-poster {
        width: 120px;
        height: auto;
        border-radius: 4px;
        border: 1px solid var(--border);
        filter: grayscale(0.35) contrast(1.05);
        transition: filter 0.3s ease;
        flex-shrink: 0;
    }

    .featured-movie:hover .featured-poster { filter: grayscale(0) contrast(1); }

    .featured-details {
        display: flex;
        flex-direction: column;
        gap: 8px;
        font-family: 'JetBrains Mono', monospace;
        min-width: 0;
    }

    .featured-details h2 {
        margin: 0;
        color: var(--accent);
        font-size: 1.05rem;
        font-family: 'JetBrains Mono', monospace;
        text-shadow: 0 0 14px var(--accent-glow);
    }

    .huge-rating {
        font-size: 1.7rem;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        color: var(--text);
        background: var(--bg-solid);
        border: 1px dashed var(--accent);
        padding: 4px 16px;
        border-radius: 4px;
        display: inline-block;
        width: fit-content;
        margin-top: 6px;
    }

    .ratings-table {
        width: 100%;
        border-collapse: collapse;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.82rem;
        background: var(--nav-bg);
        border: 1px solid var(--border);
        border-radius: 6px;
        overflow: hidden;
    }

    .ratings-table th, .ratings-table td {
        padding: 12px 14px;
        text-align: left;
        border-bottom: 1px dashed var(--border);
        white-space: nowrap;
    }

    .ratings-table td:last-child { white-space: normal; min-width: 160px; }

    .ratings-table th {
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 0.72rem;
        font-weight: 700;
        background: rgba(139, 124, 255, 0.06);
    }

    .ratings-table tr {
        transition: background-color 0.2s ease;
    }

    .ratings-table tbody tr:hover {
        background-color: var(--accent-glow);
    }

    .ratings-table tr:last-child td {
        border-bottom: none;
    }

    .rating-badge {
        background: transparent;
        border: 1px dashed var(--accent);
        padding: 2px 10px;
        border-radius: 4px;
        color: var(--accent);
        font-weight: 700;
        font-size: 0.78rem;
    }

    .term-cursor {
        display: inline-block;
        width: 0.55em; height: 1.05em;
        background: var(--accent);
        vertical-align: text-bottom;
        animation: mr-blink 1s step-end infinite;
    }
    @keyframes mr-blink { 50% { opacity: 0; } }
    .tline { opacity: 0; animation: mr-in 0.4s ease forwards; }
    @keyframes mr-in { to { opacity: 1; } }

    @media (max-width: 600px) {
        .featured-movie {
            flex-direction: column;
            text-align: center;
        }
        .featured-details { align-items: center; }
        .huge-rating { margin: 10px auto 0 auto; }
    }
</style>

<div class="ratings-head tline">
    <div class="prompt-line">
        <span class="prompt">$</span><span class="cmd"><span class="command-name">cinema-ratings</span> --all</span>
        <span class="yr-filter">
            {% assign all_years = site.data["movie-ratings"] | map: "year" | uniq | sort | reverse %}
            <select id="year-filter" aria-label="Filter by Year">
                <option value="all">Date: All Years</option>
                {% for year in all_years %}
                    <option value="{{ year }}">Year: {{ year }}</option>
                {% endfor %}
            </select>
        </span>
    </div>
</div>

{% assign latest_movie = site.data["movie-ratings"] | first %}
<div class="featured-movie tline">
    <img src="{{ latest_movie.poster }}" alt="{{ latest_movie.title }} Poster" class="featured-poster" onerror="this.style.display='none'">
    <div class="featured-details">
        <h2>{{ latest_movie.title }}</h2>
        <div style="font-size: 0.9rem; font-weight: 700; color: var(--text);">{{ latest_movie.year }}</div>
        <p style="color: var(--text-muted); margin: 0; font-size: 0.8rem;">{{ latest_movie.notes }}</p>
        <div class="huge-rating">{{ latest_movie.rating }}</div>
    </div>
</div>

<div style="overflow-x: auto; margin-top: 20px;" class="tline">
    <table class="ratings-table">
        <thead>
            <tr>
                <th>Title</th>
                <th>Year</th>
                <th>Rating</th>
                <th>Date Watched</th>
            </tr>
        </thead>
        <tbody id="movie-table-body">
            {% for movie in site.data["movie-ratings"] offset: 1 %}
            <tr class="movie-row" data-year="{{ movie.year }}">
                <td style="font-weight: 700; color: var(--text);">{{ movie.title }}</td>
                <td style="color: var(--text-muted);">{{ movie.year }}</td>
                <td><span class="rating-badge">{{ movie.rating }}</span></td>
                <td style="color: var(--text-muted);">{{ movie.notes }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>

<div class="section-cmd tline">
    <div class="prompt-line" style="margin-top: 22px;">
        <span class="prompt">$</span><span class="term-cursor"></span>
    </div>
</div>

<script>
    document.addEventListener("DOMContentLoaded", () => {
        const filter = document.getElementById('year-filter');
        const rows = document.querySelectorAll('.movie-row');

        filter.addEventListener("change", function() {
            const selectedYear = this.value;
            
            rows.forEach(row => {
                if (selectedYear === 'all' || row.getAttribute('data-year') === selectedYear) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
            });
        });
    });
</script>
