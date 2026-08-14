---
layout: default
title: Cinema Movie Ratings
permalink: /cy/cinema-movie-ratings/
---

<steil>

corff, prif, p, a, rhychwant, div, botwm, dewis, opsiwn {
        font-family: 'SUSE', sans-serif !pwysig;
    }
    h1, h2, h3 {
        ffont-teulu: 'Staatliches', sans-serif !important;
    }

.ratings-pennyn {
        arddangos: fflecs;
        cyfiawnhau-cynnwys: space-between;
        alinio-eitemau: canol;
        ymyl-gwaelod: 20px;
        fflecs-lapio: lapio;
        bwlch: 15px;
    }
    
    .year-filter-container dewis {
        cefndir: var(--nav-bg);
        hidlydd cefndir: niwlog(12px);
        -webkit-cefn-hidlo: aneglur(12px);
        lliw: var (--acen);
        ffin: var solet 1px (--ffin);
        border-radiws: 12px;
        padin: 10px 18px;
        ffont-pwysau: 700;
        cyrchwr: pwyntydd;
        amlinelliad: none;
        cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        trawsnewid: pob un o'r 0.3s ciwbig-bezier(0.4, 0, 0.2, 1);
    }

.year-filter-container dewis opsiwn {
        lliw cefndir: var (--bg-solid);
        lliw: var (--acen);
    }

[data-theme="dywyll"] .year-filter-container dewiswch {
        cysgod bocs: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
    }

.year-filter-container dewiswch:hofran, .year-filter-container dewiswch:focus {
        lliw border: var (--acen);
        cefndir: var (--accent-glow);
        trawsnewid: translateY(-1px);
    }

.featured-movie {
        arddangos: fflecs;
        bwlch: 25px;
        cefndir: var(--nav-bg);
        hidlydd cefndir: niwlog(12px);
        -webkit-cefn-hidlo: aneglur(12px);
        ffin: var solet 1px (--ffin);
        radiws ffin: 16px;
        padin: 25px;
        ymyl-gwaelod: 30px;
        cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        alinio-eitemau: canol;
        trawsnewid: pob un o'r 0.3s ciwbig-bezier(0.4, 0, 0.2, 1);
    }

[ data-theme = "tywyll"] .featured-movie {
        cysgod bocs: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
    }

.featured-movie: hofran {
        trawsnewid: translateY(-2px);
        cysgod blwch: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
        lliw border: var (--acen);
    }

.featured-poster {
        lled: 140px;
        uchder: auto;
        border-radiws: 12px;
        ffin: var solet 1px (--ffin);
        cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }

.featured-manylion {
        arddangos: fflecs;
        fflecs-cyfeiriad: colofn;
        bwlch: 10px;
    }

.graddfa enfawr {
        maint y ffont: 2.2rem;
        ffont-teulu: 'Staatliches', sans-serif;
        ffont-pwysau: 400;
        lliw: var (--testun);
        cefndir: var(--bg-solid);
        border: var solet 2px (--acen);
        padin: 8px 18px;
        border-radiws: 12px;
        arddangos: inline-bloc;
        lled: fit-content;
        ymyl-top: 5px;
    }

.haciwr-bwrdd {
        lled: 100%;
        border-cwymp: cwympo;
        ffont-teulu: 'SUSE', sans-serif;
        maint y ffont: 0.9rem;
        cefndir: var(--nav-bg);
        hidlydd cefndir: niwlog(12px);
        -webkit-cefn-hidlo: aneglur(12px);
        ffin: var solet 1px (--ffin);
        radiws ffin: 16px;
        gorlif: cudd;
        cysgod blwch: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

[ data-theme = "tywyll"] .haciwr-tabl {
        cysgod bocs: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
    }

.hacker-bwrdd fed, .hacker-tabl td {
        padin: 15px;
        testun-alinio: chwith;
        gwaelod ymyl: var doriad 1px (--ffin);
    }

.hacker-bwrdd th{
        lliw: var (--acen);
        testun-trawsnewid: priflythrennau;
        bylchau rhwng llythyrau: 1px;
        ffont-pwysau: 800;
        ffont-teulu: 'Staatliches', sans-serif;
        cefndir: rgba(0, 0, 0, 0.05);
    }

.hacker-bwrdd tr{
        pontio: cefndir-lliw 0.3s rhwyddineb;
    }

.hacker-bwrdd tr:hofran {
        lliw cefndir: var (--accent-glow);
    }

.hacker-bwrdd tr: last-plentyn td {
        border-gwaelod: dim;
    }

.rate-bathodyn {
        cefndir: var(--bg-solid);
        ffin: var solet 1px (--ffin);
        padin: 4px 12px;
        border-radiws: 12px;
        lliw: var (--testun);
        ffont-pwysau: 700;
    }

@media (lled-uchaf: 600px) {
        .featured-movie {
            fflecs-cyfeiriad: colofn;
            testun-alinio: canol;
        }
        .graddfa enfawr {
            ymyl: 10px awto 0;
        }
    }
</style>

<div class="page-content">
    
    <div class="ratings-header">
        <h1 style="margin: 0;">Sgoriau Ffilm Sinema</h1>
        
        <div class="year-hidlen-container">
            {% assign all_years = site.data["movie-ratings"] | map: "blwyddyn" | uniq | didoli | cefn %}
            <select id="filter-blwyddyn" aria-label="Hidlo yn ôl Blwyddyn">
                <option value="all">Dyddiad: Pob Blwyddyn</option>
                { % am flwyddyn ym mhob_blwyddyn %}
                    <option value="{{ year }}">Blwyddyn: {{ year }}</option>
                { % end for %}
            </select>
        </div>
    </div>

{% assign latest_movie = site.data[ "movie-ratings"] | %} cyntaf
    <div class="featured-movie">
        <img src="{{ latest_movie.poster }}" alt="{{ latest_movie.title }} Poster" class="featured-poster" onerror="this.style.display= 'dim'">
        <div class="featured-manylion">
            <h2 style="margin: 0; color: var(--accent);">{{ latest_movie.title }}</h2>
            <div style="font-size: 1.1rem; pwysau ffont: 800; lliw: var(--text);">{{ latest_movie.year }}</div>
            <p style="color: var(--text-muted); margin: 0; font-weight: 700;"> {{ latest_movie.notes }}</p>
            <div class="huge-rate">{{ latest_movie.rating }}</div>
        </div>
    </div>

<div style="overflow-x: auto; margin-top: 20px;">
        <table class="hacker-table">
            <pen>
                <tr>
                    <th>Teitl</th>
                    <fed>Blwyddyn</th>
                    <th>Sgoriad</th>
                    <th>Dyddiad Gwylio</th>
                </tr>
            </thead>
            <tbody id="movie-table-body">
                {% ar gyfer ffilm yn site.data["movie-ratings"] wrthbwyso: 1 %}
                <tr class="movie-row" data-year="{{ movie.year }}">
                    <td style="font-weight: 700; lliw: var(--text);"> {{ movie.title }}</ td>
                    <td style="color: var(--text-muted);"> {{ movie.year }}</ td>
                    <td><span class="rating-badge">{{ movie.rating }}</span></td>
                    <td style="color: var(--text-muted);"> {{ movie.notes }}</ td>
                </tr>
                { % end for %}
            </tbody>
        </table>
    </div>

</div>

<script>
    document.addEventListener("DOMContentLoaded", () => {
        const filter = document.getElementById('hidlo blwyddyn');
        const rows = document.querySelectorAll('.movie-row');

filter.addEventListener('newid', ffwythiant() {
            const selectedYear = this.value;
            
            rows.forEach(rhes => {
                os (selectedYear === 'holl' || row.getAttribute('data-year') === selectedYear) {
                    row.style.display = '' ;
                } arall {
                    row.style.display = 'dim';
                }
            });
        });
    });
</script>