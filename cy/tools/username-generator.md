---
layout: default
title: Username Generator
permalink: /cy/tools/username-generator/
---

<div class="page-content">
<a href="/tools/" class="back-link">&larr; Yn ôl i Offer</a>
  
  <h1 style="margin-top: 10px;"> Cynhyrchydd Enw Defnyddiwr</ h1>
  <p>Cynhyrchu enwau defnyddwyr unigryw, ar hap yn lleol. Cliciwch unrhyw enw defnyddiwr i'w gopïo i'ch clipfwrdd.</p>

<div style="margin-top: 30px;">
    <div style="display: flex; gap: 10px; ymyl-gwaelod: 20px; flex-wrap: wrap;">
        <input type="text" id="keyword-input" placeholder="Rhowch allweddair (dewisol)..." style="flex: 1; lled min: 200px; padin: 12px; radiws ffin: 4px; border: 1px solid var(--border); cefndir: var(--nav-bg--color); Grotesk', sans-serif; amlinelliad: dim;">
        <button id="generate-btn" style="padding: 12px 24px; border-radius: 4px; border: 1px solid var(--accent); cefndir: var(--acen); lliw: gwyn; pwysau ffont: trwm; cyrchwr: pwyntydd; ffont-teulu: 'Space san-skrif; 0.2s;"> Cynhyrchu </botwm>
    </div>

<div style="display: flex; gap: 20px; ymyl-gwaelod: 30px; maint y ffont: 0.9em;">
        <label style="display: flex; alinio-eitemau: canol; bwlch: 8px; cyrchwr: pwyntydd;">
            <input type="checkbox" id="defnydd-rhifau" wedi'i wirio style=" accent-color: var(--accent);"> Cynnwys Rhifau
        </label>
        <label style="display: flex; alinio-eitemau: canol; bwlch: 8px; cyrchwr: pwyntydd;">
            <input type="checkbox" id="use-special"> Cymeriadau Arbennig
        </label>
    </div>
    
    <div id="results-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 15px;"> </div>
  </div>

<div style="margin-top: 50px; text-align: center; maint y ffont: 0.85rem; didreiddedd: 0.5;">
    Ffynhonnell Agored. <a href="https://github.com/PASSK3YS/PASSK3YS.github.io/blob/main/tools/username-generator.md" target="_blank" style="color: inherit; border-bottom: 1px solid currentColor;">Gweld y cod ffynhonnell</a>
  </div>
</div>

<script>
  (swyddogaeth () {
    const adjectives = [ 'Tawel', 'Cudd', 'Diogel', 'Preifat', 'Amgryptio', 'Digidol', 'Cyber', 'Neon', 'Cyflym', 'Swift', 'Cosmic', 'Solar', 'Lunar', 'Arctic', 'Obsidianson', 'Obsidrian' 'Azure', 'Cysgod', 'Ysbryd', 'Zero', 'Deuaidd', 'Cwantwm', 'Glitch', 'Hollow', 'Haearn', 'Dur', 'Titaniwm', 'Melfed', 'Frost'];
    const nouns = [ 'Protocol', 'Signal', 'Node', 'Key', 'Lock', 'Vault', 'Cipher', 'Proxy', 'Router', 'Frame', 'Stack', 'Grid', 'Core', 'Link', 'Vector', 'Pixel', 'Pixel', 'By', 'Pixel', 'By' 'Wave', 'Sphere', 'Orbit', 'Horizon', 'Nexus', 'Haven', 'Fortress', 'Citadel', 'Shield', 'Guard', 'Sentry', 'Hebog', 'Wolf', 'Hawk', 'Cigfran', 'Viper', 'Phanpectom', 'Spectobra', 'Cobra', 'Spaint' 'Ronin'];
    
    const btn = document.getElementById('generate-btn');
    const mewnbwn = document.getElementById('keyword-input');
    const results = document.getElementById('results-grid');
    const useNumbers = document.getElementById('defnydd-rhifau');
    const useSpecial = document.getElementById('use-special');

swyddogaeth getRandom(arr) {
        dychwelyd arr[Math.floor(Math.random() * arr.length)];
    }

ffwythiant cynhyrchu Enw() {
        gadewch enw = "";
        const keyword = mewnbwn.value.trim();
        
        os (allweddair && Math.random() > 0.5) {
            enw = allweddair + getRandom (enwau);
        } arall os (allweddair) {
            enw = getRandom(ansoddeiriau) + allweddair;
        } arall {
            enw = getRandom(ansoddeiriau) + getRandom(enwau);
        }

os (useNumbers.checked) {
            enw += Math.floor(Math.random() * 99) + 1;
        }

os (useSpecial.checked) {
            const chars = [ '_', '.', '-', '!'];
            enw = name.slice(0, Math.floor(name.length / 2)) + getRandom(chars) + name.slice(Math.floor(name.length/2));
        }

dychwelyd enw;
    }

swyddogaeth createCard(testun) {
        const div = document.createElement('div');
        div.textContent = testun;
        div.style.cssText = "cefndir: var(--nav-bg); border: 1px solid var(--border); padin: 15px; radiws ffin: 6px; aliniad testun: canol; cyrchwr: pwyntydd; trawsnewid: pob un o'r 0.2s; defnyddiwr-dewis: dim; lleoliad: cymharol; gorlif: cudd;"
        
        div.addEventListener('mouseover', () => {
            div.style.borderColor = 'var(--acen)';
            div.style.color = 'var(--acen)';
        });
        
        div.addEventListener('mouseout', () => {
            div.style.borderColor = 'var(--ffin)';
            div.style.color = 'var(--text)';
        });

div.addEventListener('clic', () => {
            navigator.clipboard.writeText(testun);
            const originalText = div.textContent;
            div.textContent = "Wedi'i Gopïo!";
            div.style.backgroundColor = 'var(--acen)';
            div.style.color = 'gwyn';
            
            setTimeout(() => {
                div.textContent = originalText;
                div.style.backgroundColor = 'var(--nav-bg)';
                div.style.color = 'var(--text)';
            }, 1000);
        });

dychwelyd div;
    }

btn.addEventListener('clic', () => {
        results.innerHTML = '' ;
        ar gyfer (gadewch i = 0; i < 12; i ++) {
            results.appendChild(createCard(generateName()));
        }
    });

btn.clic();
  })();
</script>