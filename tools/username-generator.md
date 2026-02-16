---
layout: default
title: Username Generator
permalink: /tools/username-generator/
---

<div class="page-content">
  <a href="/tools/" style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.6; text-decoration: none; border-bottom: none;">&larr; Back to Tools</a>
  
  <h1 style="margin-top: 10px;">Username Generator</h1>
  <p>Generate unique, random usernames locally. Click any username to copy it to your clipboard.</p>

  <div style="margin-top: 30px;">
    <div style="display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap;">
        <input type="text" id="keyword-input" placeholder="Enter a keyword (optional)..." style="flex: 1; min-width: 200px; padding: 12px; border-radius: 4px; border: 1px solid var(--border); background: var(--nav-bg); color: var(--text); font-family: 'Space Grotesk', sans-serif; outline: none;">
        <button id="generate-btn" style="padding: 12px 24px; border-radius: 4px; border: 1px solid var(--accent); background: var(--accent); color: white; font-weight: bold; cursor: pointer; font-family: 'Space Grotesk', sans-serif; transition: all 0.2s;">Generate</button>
    </div>

    <div style="display: flex; gap: 20px; margin-bottom: 30px; font-size: 0.9em;">
        <label style="display: flex; align-items: center; gap: 8px; cursor: pointer;">
            <input type="checkbox" id="use-numbers" checked style="accent-color: var(--accent);"> Include Numbers
        </label>
        <label style="display: flex; align-items: center; gap: 8px; cursor: pointer;">
            <input type="checkbox" id="use-special"> Special Characters
        </label>
    </div>
    
    <div id="results-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px;"></div>
  </div>

  <div style="margin-top: 50px; text-align: center; font-size: 0.85rem; opacity: 0.5;">
    Open Source. <a href="https://github.com/PASSK3YS/PASSK3YS.github.io/blob/main/username-generator.md" target="_blank" style="color: inherit; border-bottom: 1px solid currentColor;">View source code</a>
  </div>
</div>

<script>
  (function() {
    const adjectives = ['Silent', 'Hidden', 'Secure', 'Private', 'Encrypted', 'Digital', 'Cyber', 'Neon', 'Rapid', 'Swift', 'Cosmic', 'Solar', 'Lunar', 'Arctic', 'Obsidian', 'Violet', 'Crimson', 'Azure', 'Shadow', 'Ghost', 'Zero', 'Binary', 'Quantum', 'Glitch', 'Hollow', 'Iron', 'Steel', 'Titanium', 'Velvet', 'Frost'];
    const nouns = ['Protocol', 'Signal', 'Node', 'Key', 'Lock', 'Vault', 'Cipher', 'Proxy', 'Router', 'Frame', 'Stack', 'Grid', 'Core', 'Link', 'Vector', 'Pixel', 'Byte', 'Echo', 'Pulse', 'Wave', 'Sphere', 'Orbit', 'Horizon', 'Nexus', 'Haven', 'Fortress', 'Citadel', 'Shield', 'Guard', 'Sentry', 'Falcon', 'Wolf', 'Hawk', 'Raven', 'Viper', 'Cobra', 'Phantom', 'Spectre', 'Nomad', 'Ronin'];
    
    const btn = document.getElementById('generate-btn');
    const input = document.getElementById('keyword-input');
    const results = document.getElementById('results-grid');
    const useNumbers = document.getElementById('use-numbers');
    const useSpecial = document.getElementById('use-special');

    function getRandom(arr) {
        return arr[Math.floor(Math.random() * arr.length)];
    }

    function generateName() {
        let name = "";
        const keyword = input.value.trim();
        
        if (keyword && Math.random() > 0.5) {
            name = keyword + getRandom(nouns);
        } else if (keyword) {
            name = getRandom(adjectives) + keyword;
        } else {
            name = getRandom(adjectives) + getRandom(nouns);
        }

        if (useNumbers.checked) {
            name += Math.floor(Math.random() * 99) + 1;
        }

        if (useSpecial.checked) {
            const chars = ['_', '.', '-', '!'];
            name = name.slice(0, Math.floor(name.length / 2)) + getRandom(chars) + name.slice(Math.floor(name.length / 2));
        }

        return name;
    }

    function createCard(text) {
        const div = document.createElement('div');
        div.textContent = text;
        div.style.cssText = "background: var(--nav-bg); border: 1px solid var(--border); padding: 15px; border-radius: 6px; text-align: center; cursor: pointer; transition: all 0.2s; user-select: none; position: relative; overflow: hidden;";
        
        div.addEventListener('mouseover', () => {
            div.style.borderColor = 'var(--accent)';
            div.style.color = 'var(--accent)';
        });
        
        div.addEventListener('mouseout', () => {
            div.style.borderColor = 'var(--border)';
            div.style.color = 'var(--text)';
        });

        div.addEventListener('click', () => {
            navigator.clipboard.writeText(text);
            const originalText = div.textContent;
            div.textContent = "Copied!";
            div.style.backgroundColor = 'var(--accent)';
            div.style.color = 'white';
            
            setTimeout(() => {
                div.textContent = originalText;
                div.style.backgroundColor = 'var(--nav-bg)';
                div.style.color = 'var(--text)';
            }, 1000);
        });

        return div;
    }

    btn.addEventListener('click', () => {
        results.innerHTML = '';
        for (let i = 0; i < 12; i++) {
            results.appendChild(createCard(generateName()));
        }
    });

    // Generate initial batch
    btn.click();
  })();
</script>