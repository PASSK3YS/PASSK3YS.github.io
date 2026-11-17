---
layout: default
title: Username Generator
permalink: /tools/username-generator/
---

<style>
.ug-shell { font-family: 'JetBrains Mono', monospace; }
.ug-shell p { font-family: 'SUSE', sans-serif; }

.ug-cmd {
    display: flex;
    gap: 10px;
    align-items: baseline;
    margin: 0 0 6px 0;
    flex-wrap: wrap;
}
.ug-cmd .prompt { color: var(--accent); white-space: nowrap; }
.ug-cmd .cmd { color: var(--text); }
.ug-cmd .command-name { color: var(--accent); }

.ug-back {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--text-muted);
    text-decoration: none;
    letter-spacing: 0.5px;
    transition: color 0.2s ease, text-shadow 0.2s ease;
    display: inline-block;
    margin-bottom: 18px;
}
.ug-back:hover { color: var(--accent); text-shadow: 0 0 12px var(--accent-glow); }

.ug-intro { color: var(--text-muted); font-size: 0.95rem; margin: 0 0 30px 0; }

.ug-controls { display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap; }

.ug-input {
    flex: 1;
    min-width: 200px;
    padding: 10px 14px;
    border-radius: 4px;
    border: 1px dashed var(--border);
    background: transparent;
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    outline: none;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.ug-input:focus {
    border-color: var(--accent);
    border-style: solid;
    box-shadow: 0 0 10px var(--accent-glow);
}
.ug-input::placeholder { color: var(--text-muted); opacity: 0.7; }

.ug-btn {
    padding: 10px 22px;
    border-radius: 4px;
    border: 1px solid var(--accent);
    background: var(--accent);
    color: #ffffff;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    font-weight: bold;
    letter-spacing: 1px;
    text-transform: uppercase;
    cursor: pointer;
    transition: all 0.2s;
}
.ug-btn:hover { box-shadow: 0 0 14px var(--accent-glow); }

.ug-options {
    display: flex;
    gap: 20px;
    margin-bottom: 30px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: var(--text-muted);
}
.ug-options label {
    display: flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
}
.ug-options input[type="checkbox"] { accent-color: var(--accent); }

#results-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 12px;
}

.ug-footer {
    margin-top: 50px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    opacity: 0.6;
    color: var(--text-muted);
    letter-spacing: 0.5px;
}
.ug-footer a { color: inherit; border-bottom: 1px solid currentColor; }
</style>

<div class="page-content ug-shell">
<a href="/tools/" class="ug-back">&larr; cd /tools/</a>

  <div class="ug-cmd">
    <span class="prompt">$</span><span class="cmd"><span class="command-name">gen</span> --username</span>
  </div>
  <p class="ug-intro">Generate unique, random usernames locally. Click any username to copy it to your clipboard.</p>

  <div>
    <div class="ug-controls">
        <input type="text" id="keyword-input" class="ug-input" placeholder="Enter a keyword (optional)...">
        <button id="generate-btn" class="ug-btn">Generate</button>
    </div>

    <div class="ug-options">
        <label>
            <input type="checkbox" id="use-numbers" checked> Include Numbers
        </label>
        <label>
            <input type="checkbox" id="use-special"> Special Characters
        </label>
    </div>
    
    <div id="results-grid"></div>
  </div>

  <div class="ug-footer">
    Open Source. <a href="https://github.com/PASSK3YS/PASSK3YS.github.io/blob/main/tools/username-generator.md" target="_blank">View source code</a>
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
        div.style.cssText = "background: var(--nav-bg); border: 1px dashed var(--border); padding: 12px; border-radius: 4px; text-align: center; cursor: pointer; transition: all 0.2s; user-select: none; position: relative; overflow: hidden; font-family: 'JetBrains Mono', monospace; font-size: 0.82rem;";
        
        div.addEventListener('mouseover', () => {
            div.style.borderColor = 'var(--accent)';
            div.style.borderStyle = 'solid';
            div.style.color = 'var(--accent)';
            div.style.boxShadow = '0 0 10px var(--accent-glow)';
        });
        
        div.addEventListener('mouseout', () => {
            div.style.borderColor = 'var(--border)';
            div.style.borderStyle = 'dashed';
            div.style.color = 'var(--text)';
            div.style.boxShadow = 'none';
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

    btn.click();
  })();
</script>
