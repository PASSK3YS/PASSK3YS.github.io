---
layout: default
title: Password Strength Tester
permalink: /password-tester/
---

<div class="page-content">
  <a href="/tools/" style="font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; opacity: 0.6; text-decoration: none; border-bottom: none;">&larr; Back to Tools</a>
  
  <h1 style="margin-top: 10px;">Password Strength Tester</h1>
  <p>Check the strength of your passwords locally in your browser. No data is ever sent to a server.</p>

  <div style="margin-top: 30px; position: relative;">
    <div style="position: relative; display: flex; align-items: center;">
        <input type="password" id="password-input" placeholder="Enter password..." style="width: 100%; padding: 12px 45px 12px 12px; border-radius: 4px; border: 1px solid var(--border); background: var(--nav-bg); color: var(--text); font-family: 'Space Grotesk', sans-serif; font-size: 1.1rem; outline: none; transition: border-color 0.2s;">
        <button id="toggle-visibility" style="position: absolute; right: 10px; background: none; border: none; color: var(--accent); cursor: pointer; padding: 5px; display: flex; align-items: center; opacity: 0.7; transition: opacity 0.2s;">
            <svg id="eye-icon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle></svg>
        </button>
    </div>
    
    <div id="strength-meter" style="height: 8px; width: 0%; background-color: #ff4d4d; margin-top: 10px; border-radius: 4px; transition: all 0.3s ease;"></div>
    
    <div id="results" style="margin-top: 20px; display: grid; gap: 10px; font-size: 0.9rem;">
      <p id="crack-time" style="margin: 0; opacity: 0.8;"></p>
      <p id="feedback" style="margin: 0; color: var(--accent); font-weight: bold;"></p>
    </div>
  </div>

  <div style="margin-top: 50px; text-align: center; font-size: 0.85rem; opacity: 0.5;">
    Open Source. <a href="https://github.com/PASSK3YS/PASSK3YS.github.io/blob/main/password-tester.md" target="_blank" style="color: inherit; border-bottom: 1px solid currentColor;">View source code</a>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/zxcvbn/4.4.2/zxcvbn.js"></script>

<script>
  (function() {
    const input = document.getElementById('password-input');
    const meter = document.getElementById('strength-meter');
    const crackTime = document.getElementById('crack-time');
    const feedback = document.getElementById('feedback');
    const toggleBtn = document.getElementById('toggle-visibility');
    const eyeIcon = document.getElementById('eye-icon');

    const strengthColors = { 0: '#ff4d4d', 1: '#ff4d4d', 2: '#ffad33', 3: '#99cc33', 4: '#33cc33' };
    const strengthLabels = { 0: 'Very Weak', 1: 'Weak', 2: 'Fair', 3: 'Strong', 4: 'Very Strong' };

    toggleBtn.addEventListener('click', () => {
      const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
      input.setAttribute('type', type);
      toggleBtn.style.opacity = type === 'password' ? '0.7' : '1';
      
      if (type === 'text') {
        eyeIcon.innerHTML = '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line>';
      } else {
        eyeIcon.innerHTML = '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>';
      }
    });

    input.addEventListener('input', () => {
      const val = input.value;
      const result = zxcvbn(val);
      
      if (val !== "") {
        meter.style.width = ((result.score + 1) / 5) * 100 + '%';
        meter.style.background = strengthColors[result.score];
        crackTime.innerText = "Estimated time to crack: " + result.crack_times_display.offline_slow_hashing_1e4_per_second;
        
        let advice = strengthLabels[result.score];
        if (result.feedback.warning) { advice += " - " + result.feedback.warning; }
        feedback.innerText = advice;
      } else {
        meter.style.width = '0%';
        crackTime.innerText = '';
        feedback.innerText = '';
      }
    });
  })();
</script>