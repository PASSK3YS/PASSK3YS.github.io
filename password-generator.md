---
layout: default
title: Password Generator
permalink: /tools/password-generator/
---

<div class="page-content">
  <a href="/tools/" style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.6; text-decoration: none; border-bottom: none;">&larr; Back to Tools</a>
  
  <h1 style="margin-top: 10px;">Password Generator</h1>
  <p>Generate cryptographically strong passwords locally in your browser.</p>

  <div style="margin-top: 30px;">
    
    <div style="position: relative; margin-bottom: 30px;">
        <input type="text" id="password-output" readonly value="Generating..." style="width: 100%; padding: 20px; border-radius: 8px; border: 2px solid var(--border); background: var(--nav-bg); color: var(--accent); font-family: 'Space Grotesk', monospace; font-size: 1.4rem; text-align: center; outline: none; cursor: pointer; transition: all 0.2s;">
        <div id="copy-msg" style="position: absolute; top: -30px; left: 50%; transform: translateX(-50%); background: var(--accent); color: white; padding: 4px 10px; border-radius: 4px; font-size: 0.8rem; opacity: 0; transition: opacity 0.2s; pointer-events: none;">Copied!</div>
        <p style="text-align: center; font-size: 0.8rem; opacity: 0.5; margin-top: 8px;">Click to copy</p>
    </div>

    <div style="background: var(--nav-bg); padding: 20px; border-radius: 8px; border: 1px solid var(--border);">
        <div style="margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                <label style="font-weight: bold;">Length</label>
                <span id="length-val" style="color: var(--accent); font-weight: bold;">16</span>
            </div>
            <input type="range" id="length-range" min="8" max="64" value="16" style="width: 100%; cursor: pointer;">
        </div>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 25px;">
            <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; user-select: none;">
                <input type="checkbox" id="use-upper" checked style="width: 18px; height: 18px; accent-color: var(--accent);">
                <span>A-Z</span>
            </label>
            <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; user-select: none;">
                <input type="checkbox" id="use-lower" checked style="width: 18px; height: 18px; accent-color: var(--accent);">
                <span>a-z</span>
            </label>
            <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; user-select: none;">
                <input type="checkbox" id="use-numbers" checked style="width: 18px; height: 18px; accent-color: var(--accent);">
                <span>0-9</span>
            </label>
            <label style="display: flex; align-items: center; gap: 10px; cursor: pointer; user-select: none;">
                <input type="checkbox" id="use-symbols" checked style="width: 18px; height: 18px; accent-color: var(--accent);">
                <span>!@#</span>
            </label>
        </div>

        <button id="generate-btn" style="width: 100%; padding: 15px; border-radius: 6px; border: none; background: var(--accent); color: white; font-weight: bold; font-size: 1rem; cursor: pointer; font-family: 'Space Grotesk', sans-serif; transition: opacity 0.2s;">
            Generate New Password
        </button>
    </div>

  </div>

  <div style="margin-top: 50px; text-align: center; font-size: 0.85rem; opacity: 0.5;">
    Open Source. <a href="https://github.com/PASSK3YS/PASSK3YS.github.io/blob/main/password-generator.md" target="_blank" style="color: inherit; border-bottom: 1px solid currentColor;">View source code</a>
  </div>
</div>

<script>
  (function() {
    const output = document.getElementById('password-output');
    const lengthRange = document.getElementById('length-range');
    const lengthVal = document.getElementById('length-val');
    const btn = document.getElementById('generate-btn');
    const copyMsg = document.getElementById('copy-msg');

    const chars = {
        upper: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        lower: 'abcdefghijklmnopqrstuvwxyz',
        number: '0123456789',
        symbol: '!@#$%^&*()_+~`|}{[]:;?><,./-='
    };

    function generate() {
        const length = parseInt(lengthRange.value);
        const useUpper = document.getElementById('use-upper').checked;
        const useLower = document.getElementById('use-lower').checked;
        const useNumber = document.getElementById('use-numbers').checked;
        const useSymbol = document.getElementById('use-symbols').checked;

        let charset = '';
        if (useUpper) charset += chars.upper;
        if (useLower) charset += chars.lower;
        if (useNumber) charset += chars.number;
        if (useSymbol) charset += chars.symbol;

        if (charset === '') {
            output.value = 'Select at least one option';
            return;
        }

        let password = '';
        const array = new Uint32Array(length);
        window.crypto.getRandomValues(array);

        for (let i = 0; i < length; i++) {
            password += charset[array[i] % charset.length];
        }

        output.value = password;
    }

    lengthRange.addEventListener('input', (e) => {
        lengthVal.textContent = e.target.value;
        generate();
    });

    output.addEventListener('click', () => {
        if (!output.value) return;
        navigator.clipboard.writeText(output.value);
        
        output.style.borderColor = 'var(--accent)';
        copyMsg.style.opacity = '1';
        copyMsg.style.top = '-40px';
        
        setTimeout(() => {
            output.style.borderColor = 'var(--border)';
            copyMsg.style.opacity = '0';
            copyMsg.style.top = '-30px';
        }, 1500);
    });

    btn.addEventListener('click', () => {
        generate();
    });

    generate();
  })();
</script>