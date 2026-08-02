---
layout: default
title: Cinema Movie Ratings
permalink: /cinema-movie-ratings/
---

<style>

    body, main, p, a, span, div, button, select, option {
        font-family: 'SUSE', sans-serif !important;
    }
    h1, h2, h3 {
        font-family: 'Staatliches', sans-serif !important;
    }

    .ratings-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        flex-wrap: wrap;
        gap: 15px;
    }
    
    .year-filter-container select {
        background: var(--nav-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        color: var(--accent);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 10px 18px;
        font-weight: 700;
        cursor: pointer;
        outline: none;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .year-filter-container select option {
        background-color: var(--bg-solid);
        color: var(--accent);
    }

    [data-theme="dark"] .year-filter-container select {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
    }

    .year-filter-container select:hover, .year-filter-container select:focus {
        border-color: var(--accent);
        background: var(--accent-glow);
        transform: translateY(-1px);
    }

    .featured-movie {
        display: flex;
        gap: 25px;
        background: var(--nav-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        align-items: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    [data-theme="dark"] .featured-movie {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
    }

    .featured-movie:hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
        border-color: var(--accent);
    }

    .featured-poster {
        width: 140px;
        height: auto;
        border-radius: 12px;
        border: 1px solid var(--border);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }

    .featured-details {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .huge-rating {
        font-size: 2.2rem;
        font-family: 'Staatliches', sans-serif;
        font-weight: 400;
        color: var(--text);
        background: var(--bg-solid);
        border: 2px solid var(--accent);
        padding: 8px 18px;
        border-radius: 12px;
        display: inline-block;
        width: fit-content;
        margin-top: 5px;
    }

    .hacker-table {
        width: 100%;
        border-collapse: collapse;
        font-family: 'SUSE', sans-serif;
        font-size: 0.9rem;
        background: var(--nav-bg);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border);
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    [data-theme="dark"] .hacker-table {
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
    }

    .hacker-table th, .hacker-table td {
        padding: 15px;
        text-align: left;
        border-bottom: 1px dashed var(--border);
    }

    .hacker-table th {
        color: var(--accent);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 800;
        font-family: 'Staatliches', sans-serif;
        background: rgba(0, 0, 0, 0.05);
    }

    .hacker-table tr {
        transition: background-color 0.3s ease;
    }

    .hacker-table tr:hover {
        background-color: var(--accent-glow);
    }

    .hacker-table tr:last-child td {
        border-bottom: none;
    }

    .rating-badge {
        background: var(--bg-solid);
        border: 1px solid var(--border);
        padding: 4px 12px;
        border-radius: 12px;
        color: var(--text);
        font-weight: 700;
    }

    @media (max-width: 600px) {
        .featured-movie {
            flex-direction: column;
            text-align: center;
        }
        .huge-rating {
            margin: 10px auto 0 auto;
        }
    }
</style>

<div class="page-content">
    
    <div class="ratings-header">
        <h1 style="margin: 0;">Cinema Movie Ratings</h1>
        
        <div class="year-filter-container">
            {% assign all_years = site.data["movie-ratings"] | map: "year" | uniq | sort | reverse %}
            <select id="year-filter" aria-label="Filter by Year">
                <option value="all">Date: All Years</option>
                {% for year in all_years %}
                    <option value="{{ year }}">Year: {{ year }}</option>
                {% endfor %}
            </select>
        </div>
    </div>

    {% assign latest_movie = site.data["movie-ratings"] | first %}
    <div class="featured-movie">
        <img src="{{ latest_movie.poster }}" alt="{{ latest_movie.title }} Poster" class="featured-poster" onerror="this.style.display='none'">
        <div class="featured-details">
            <h2 style="margin: 0; color: var(--accent);">{{ latest_movie.title }}</h2>
            <div style="font-size: 1.1rem; font-weight: 800; color: var(--text);">{{ latest_movie.year }}</div>
            <p style="color: var(--text-muted); margin: 0; font-weight: 700;">{{ latest_movie.notes }}</p>
            <div class="huge-rating">{{ latest_movie.rating }}</div>
        </div>
    </div>

    <div style="overflow-x: auto; margin-top: 20px;">
        <table class="hacker-table">
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

</div>

<script>
    document.addEventListener("DOMContentLoaded", () => {
        const filter = document.getElementById('year-filter');
        const rows = document.querySelectorAll('.movie-row');

        filter.addEventListener('change', function() {
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