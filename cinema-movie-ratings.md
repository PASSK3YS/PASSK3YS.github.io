---
layout: default
title: Cinema Movie Ratings
permalink: /cinema-movie-ratings/
---

<style>
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
        color: var(--accent);
        border: 1px solid var(--border);
        border-radius: 4px;
        padding: 8px 15px;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        cursor: pointer;
        outline: none;
        box-shadow: 4px 4px 0px rgba(0, 0, 0, 0.1);
        transition: all 0.1s ease;
    }

    [data-theme="dark"] .year-filter-container select {
        box-shadow: 4px 4px 0px rgba(255, 255, 255, 0.1);
    }

    .year-filter-container select:hover, .year-filter-container select:focus {
        border-color: var(--accent);
        background: var(--accent-glow);
    }

    .hacker-table {
        width: 100%;
        border-collapse: collapse;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.9rem;
        background: var(--nav-bg);
        border: 1px solid var(--border);
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 6px 6px 0px rgba(0, 0, 0, 0.1);
    }

    [data-theme="dark"] .hacker-table {
        box-shadow: 6px 6px 0px rgba(255, 255, 255, 0.1);
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
        background: rgba(0, 0, 0, 0.05);
    }

    .hacker-table tr {
        transition: background-color 0.1s ease;
    }

    .hacker-table tr:hover {
        background-color: var(--accent-glow);
    }

    .hacker-table tr:last-child td {
        border-bottom: none;
    }

    .rating-badge {
        background: var(--bg);
        border: 1px solid var(--border);
        padding: 4px 8px;
        border-radius: 4px;
        color: var(--text);
        font-weight: 700;
    }
</style>

<div class="page-content">
    
    <div class="ratings-header">
        <h1 style="margin: 0;">CINEMA MOVIE RATINGS</h1>
        
        <div class="year-filter-container">
            {% assign all_years = site.data["movie-ratings"] | map: "year" | uniq | sort | reverse %}
            <select id="year-filter" aria-label="Filter by Year">
                <option value="all">DATE: ALL YEARS</option>
                {% for year in all_years %}
                    <option value="{{ year }}">YEAR: {{ year }}</option>
                {% endfor %}
            </select>
        </div>
    </div>

    <div style="overflow-x: auto; margin-top: 20px;">
        <table class="hacker-table">
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Year</th>
                    <th>Rating</th>
                    <th>Notes</th>
                </tr>
            </thead>
            <tbody id="movie-table-body">
                {% for movie in site.data["movie-ratings"] %}
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