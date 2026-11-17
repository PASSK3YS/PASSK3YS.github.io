<script>
document.addEventListener("DOMContentLoaded", () => {
    // mark the About tab as active on this page
    document.querySelectorAll('.term-tabs a').forEach(a => {
        if (a.getAttribute('href') === '/') a.classList.add('active');
    });

    // sequential line entrance
    document.querySelectorAll('.tline').forEach((el, i) => {
        el.style.animationDelay = (0.05 + i * 0.12) + 's';
    });

    // NOTE: theme toggle logic lives in _layouts/default.html — do not add it here,
    // or the click handler would fire twice and the theme would never change.

    fetch('/feed.json')
        .then(res => res.json())
        .then(data => {
            if (data.items && data.items.length > 0) {
                const firstPost = data.items[0];
                let dateStr = "";
                if (firstPost.date_published) {
                    const date = new Date(firstPost.date_published);
                    dateStr = date.toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }).toUpperCase();
                }
                const c = document.getElementById('latest-blog-container');
                c.classList.remove('dim');
                c.innerHTML = `${firstPost.title} <span class="dim">// ${dateStr}</span>`;
                document.getElementById('latest-blog-link').href = firstPost.url;
            }
        })
        .catch(() => {});

    fetch('/cinema-watchlist/2026/')
        .then(res => res.text())
        .then(pageHtml => {
            const firstMovie = new DOMParser().parseFromString(pageHtml, 'text/html').querySelector('.movie-card');
            if (firstMovie) {
                const c = document.getElementById('latest-movie-container');
                c.classList.remove('dim');
                c.innerHTML = `${firstMovie.querySelector('.movie-title').textContent} <span class="dim">// ${firstMovie.querySelector('.movie-date').textContent}</span>`;
            }
        })
        .catch(() => {});

    fetch('https://api.github.com/repos/PASSK3YS/PASSK3YS.github.io/commits/main')
        .then(res => res.json())
        .then(data => {
            if (data && data.sha) {
                document.getElementById('version-link').href =
                    'https://github.com/PASSK3YS/PASSK3YS.github.io/commit/' + data.sha;
                document.getElementById('version-text').textContent = 'v.' + data.sha.substring(0, 7);
            }
        })
        .catch(() => {});
});
</script>