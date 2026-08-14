---
layout: default
title: Guestbook
permalink: /cy/guestbook/
---

<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

<style>
body, main, h1, h2, h3, p, a, span, div, button {
    font-family: 'SUSE', sans-serif !important;
}

h1, h2, h3 {
    font-family: 'Staatliches', sans-serif !important;
}

pre, code {
    font-family: 'JetBrains Mono', monospace !important;
}

.blinking-cursor {
    font-weight: 800;
    color: var(--accent);
    animation: blink 1s step-end infinite;
}

@keyframes blink {
    50% { opacity: 0; }
}

.hacker-btn {
    font-size: 1.1rem;
    font-weight: 700;
    padding: 14px 28px;
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 12px;
    display: inline-block;
    text-decoration: none;
    background: var(--nav-bg);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    text-transform: uppercase;
    letter-spacing: 1px;
    cursor: pointer;
}

[data-theme="dark"] .hacker-btn {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
}

.hacker-btn:hover {
    border-color: var(--accent);
    color: var(--accent);
    box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.2);
    transform: translateY(-2px);
    background: rgba(99, 102, 241, 0.05);
}

.sign-form {
    max-width: 500px;
    margin: 0 auto 40px auto;
    display: flex;
    flex-direction: column;
    gap: 15px;
    background: var(--nav-bg);
    padding: 30px;
    border-radius: 16px;
    border: 1px solid var(--border);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

[data-theme="dark"] .sign-form {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
}

.sign-form input, .sign-form textarea {
    font-family: 'SUSE', sans-serif;
    background: var(--bg-solid);
    border: 1px solid var(--border);
    color: var(--text);
    padding: 14px;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
}

.sign-form input:focus, .sign-form textarea:focus {
    outline: none;
    border-color: var(--accent);
}

.carousel-wrapper {
    position: relative;
    width: 100%;
    padding: 0 50px;
    box-sizing: border-box;
    user-select: none;
}

.carousel-container {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
    gap: 20px;
    padding: 10px 0 20px 0;
    scrollbar-width: none; 
}

.carousel-container::-webkit-scrollbar {
    display: none; 
}

.carousel-item {
    flex: 0 0 100%; 
    scroll-snap-align: center;
    background: var(--nav-bg);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 40px 40px;
    box-sizing: border-box;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 250px;
    transition: border-color 0.3s ease, transform 0.3s ease, box-shadow 0.3s ease;
}

[data-theme="dark"] .carousel-item {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
}

.carousel-item:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
    box-shadow: 0 20px 25px -5px rgba(99, 102, 241, 0.2);
}

.nav-btn {
    position: absolute;
    top: 45%;
    transform: translateY(-50%);
    background: var(--nav-bg);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid var(--border);
    color: var(--text);
    font-size: 1.2rem;
    cursor: pointer;
    border-radius: 12px;
    width: 45px;
    height: 45px;
    z-index: 10;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

[data-theme="dark"] .nav-btn {
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3), 0 4px 6px -2px rgba(0, 0, 0, 0.1);
}

.nav-btn:hover {
    background: rgba(99, 102, 241, 0.05);
    color: var(--accent);
    border-color: var(--accent);
    box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.2);
    transform: translateY(-50%) translate(-2px, -2px);
}

#prevBtn {
    left: 0;
}

#nextBtn {
    right: 0;
}

.progress-wrapper {
    position: relative;
    height: 20px;
    margin-top: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
}

.progress-track {
    width: 100%;
    height: 6px;
    background: var(--nav-bg);
    border: 1px solid var(--border);
    border-radius: 0;
    overflow: hidden;
    transition: opacity 0.3s ease;
}

.progress-fill {
    height: 100%;
    width: 0%;
    background: var(--accent);
    transform-origin: left;
}

.progress-fill.animate {
    animation: fillProgress 10s linear forwards;
}

.progress-fill.paused {
    animation-play-state: paused;
}

@keyframes fillProgress {
    0% { width: 0%; }
    100% { width: 100%; }
}

.paused-indicator {
    position: absolute;
    font-size: 0.85rem;
    font-weight: 700;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 2px;
    opacity: 0;
    transition: opacity 0.3s ease;
    display: flex;
    align-items: center;
    pointer-events: none;
    background: var(--bg-solid);
    padding: 0 10px;
}

.carousel-wrapper.is-paused .progress-track {
    opacity: 0.15;
}

.carousel-wrapper.is-paused .paused-indicator {
    opacity: 1;
}

@media (max-width: 768px) {
    .carousel-wrapper {
        padding: 0;
    }
    #prevBtn, #nextBtn {
        display: none; 
    }
    .carousel-item {
        flex: 0 0 90%; 
        scroll-snap-align: center;
    }
    .carousel-container {
        padding: 10px 5% 20px 5%; 
    }
    .progress-wrapper {
        padding: 0 5%;
    }
}
</style>

<div class="page-content" style="max-width: 800px; margin: 0 auto; padding-top: 20px;">
  
    <h1 style="color: var(--accent); text-align: center; font-size: 2.2rem; font-weight: 800; letter-spacing: -1px; margin-bottom: 10px;">
        >_ Guestbook<span class="blinking-cursor">_</span>
    </h1>
  
    <p style="color: var(--text-muted); text-align: center; margin-bottom: 30px; font-size: 1.05rem;">
        Messages and greetings from visitors.
    </p>

    <form id="guestbook-form" class="sign-form">
        <input type="text" id="name" placeholder="Name" required>
        <textarea id="message" placeholder="Message" required></textarea>
        
        <div class="cf-turnstile" data-sitekey="0x4AAAAAAEEfCSzxCVuLiXl0" data-theme="auto" data-callback="unlockForm"></div>
        
        <button type="submit" id="submitBtn" class="hacker-btn" disabled>Sign Guestbook</button>
        <div id="formStatus" style="display: none; text-align: center; font-weight: 700;"></div>
    </form>

    <div class="carousel-wrapper">
        <button id="prevBtn" class="nav-btn">&#10094;</button>
        
        <div class="carousel-container" id="guestbook-carousel">
            <div class="carousel-item" style="justify-content: center; align-items: center;">
                <p style="color: var(--text); font-size: 1.1rem;">Initializing connection...</p>
            </div>
        </div>

        <button id="nextBtn" class="nav-btn">&#10095;</button>

        <div class="progress-wrapper">
            <div class="progress-track">
                <div class="progress-fill animate" id="progressBarFill"></div>
            </div>
            <div class="paused-indicator">
                [ PAUSED ]
            </div>
        </div>
    </div>
</div>

<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
<script>
const supabaseUrl = 'https://hnyokpvurntvxvhdvwii.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhueW9rcHZ1cm50dnh2aGR2d2lpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODU2NzQ0MzEsImV4cCI6MjEwMTI1MDQzMX0.NZLDRNPtWYH-_cvDovXkwyrR-SiT9HqvYnlfT2VpEyo';
const supabaseClient = window.supabase.createClient(supabaseUrl, supabaseKey);

let turnstileToken = "";
window.unlockForm = function(token) {
    turnstileToken = token;
    document.getElementById('submitBtn').disabled = false;
};

const container = document.getElementById('guestbook-carousel');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const wrapper = document.querySelector('.carousel-wrapper');
const fill = document.getElementById('progressBarFill');
const form = document.getElementById('guestbook-form');
const submitBtn = document.getElementById('submitBtn');
const formStatus = document.getElementById('formStatus');

let isLockedPause = false;
let isScrolling;

async function loadGuestbook() {
    const { data, error } = await supabaseClient
        .from('guestbook')
        .select('name, message, created_at')
        .order('created_at', { ascending: false });

    if (error) {
        container.innerHTML = `<div class="carousel-item" style="justify-content: center; align-items: center;"><p style="color: red;">Failed to retrieve records.</p></div>`;
        return;
    }

    container.innerHTML = '';

    if (data.length === 0) {
        container.innerHTML = `<div class="carousel-item" style="justify-content: center; align-items: center;"><p style="color: var(--text);">No records found.</p></div>`;
        return;
    }

    data.forEach(entry => {
        const dateStr = new Date(entry.created_at).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });

        const itemDiv = document.createElement('div');
        itemDiv.className = 'carousel-item';
        
        const messageP = document.createElement('p');
        messageP.style.cssText = 'color: var(--text); font-size: 1.1rem; margin-top: 0; line-height: 1.6; word-break: break-word;';
        messageP.textContent = `"${entry.message}"`;

        const metaDiv = document.createElement('div');
        metaDiv.style.marginTop = '20px';

        const nameP = document.createElement('p');
        nameP.style.cssText = 'color: var(--accent); margin-bottom: 0; font-weight: 800; text-transform: uppercase; letter-spacing: 1px;';
        nameP.textContent = `> ${entry.name}`;

        const dateSpan = document.createElement('span');
        dateSpan.style.cssText = 'color: var(--text-muted); font-size: 0.85rem; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase;';
        dateSpan.textContent = dateStr;

        metaDiv.appendChild(nameP);
        metaDiv.appendChild(dateSpan);
        itemDiv.appendChild(messageP);
        itemDiv.appendChild(metaDiv);
        container.appendChild(itemDiv);
    });

    resetAnimation();
}

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    if (!turnstileToken) {
        return;
    }

    const name = document.getElementById('name').value.trim();
    const message = document.getElementById('message').value.trim();

    if (!name || !message) return;

    submitBtn.disabled = true;
    formStatus.style.display = 'block';
    formStatus.style.color = 'var(--text)';
    formStatus.textContent = 'Transmitting...';

    const { error } = await supabaseClient
        .from('guestbook')
        .insert([{ name, message }]);

    if (error) {
        formStatus.textContent = 'Transmission failed. Try again.';
        formStatus.style.color = 'red';
        submitBtn.disabled = false;
    } else {
        formStatus.textContent = 'Record appended successfully.';
        formStatus.style.color = 'var(--accent)';
        form.reset();
        turnstileToken = "";
        window.turnstile.reset();
        await loadGuestbook();
        
        setTimeout(() => {
            formStatus.style.display = 'none';
        }, 3000);
    }
});

function scrollNext() {
    if (container.scrollLeft + container.clientWidth >= container.scrollWidth - 10) {
        container.scrollTo({ left: 0, behavior: 'smooth' });
    } else {
        container.scrollBy({ left: container.offsetWidth, behavior: 'smooth' });
    }
}

function scrollPrev() {
    if (container.scrollLeft <= 0) {
        container.scrollTo({ left: container.scrollWidth, behavior: 'smooth' });
    } else {
        container.scrollBy({ left: -container.offsetWidth, behavior: 'smooth' });
    }
}

function resetAnimation() {
    fill.classList.remove('animate');
    void fill.offsetWidth; 
    fill.classList.add('animate');
}

function pauseAnimation() {
    fill.classList.add('paused');
    wrapper.classList.add('is-paused');
}

function resumeAnimation() {
    if (isLockedPause) return;
    fill.classList.remove('paused');
    wrapper.classList.remove('is-paused');
}

fill.addEventListener('animationend', () => {
    scrollNext();
    resetAnimation();
});

nextBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    scrollNext();
    resetAnimation();
});

prevBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    scrollPrev();
    resetAnimation();
});

wrapper.addEventListener('mouseenter', pauseAnimation);
wrapper.addEventListener('mouseleave', resumeAnimation);

wrapper.addEventListener('click', () => {
    isLockedPause = !isLockedPause;
    if (isLockedPause) {
        pauseAnimation();
    } else {
        resumeAnimation();
    }
});

container.addEventListener('scroll', () => {
    window.clearTimeout(isScrolling);
    pauseAnimation();
    isScrolling = setTimeout(() => {
        resumeAnimation();
    }, 150);
}, { passive: true });

loadGuestbook();
</script>