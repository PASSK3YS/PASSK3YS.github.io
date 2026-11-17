---
layout: default
title: Standard Notes Themes
permalink: /tools/standard-notes-themes/
---

<style>
.sn-shell { font-family: 'JetBrains Mono', monospace; }
.sn-shell p { font-family: 'SUSE', sans-serif; }
.sn-shell p code { font-family: 'JetBrains Mono', monospace !important; font-size: 0.8rem; }

.sn-back {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    color: var(--text-muted);
    text-decoration: none;
    letter-spacing: 0.5px;
    transition: color 0.2s ease, text-shadow 0.2s ease;
    display: inline-block;
}
.sn-back:hover { color: var(--accent); text-shadow: 0 0 12px var(--accent-glow); }

.sn-cmd {
    display: flex;
    gap: 10px;
    align-items: baseline;
    margin: 18px 0 6px 0;
    flex-wrap: wrap;
}
.sn-cmd .prompt { color: var(--accent); white-space: nowrap; }
.sn-cmd .cmd { color: var(--text); font-size: 1.1rem; font-weight: 700; }
.sn-cmd .command-name { color: var(--accent); }

.sn-intro { color: var(--text); font-size: 0.95rem; margin: 0 0 6px 0; }
.sn-license { color: var(--text-muted); font-size: 0.85rem; margin: 0; }

.sn-support {
    margin-top: 30px;
    border-top: 1px dashed var(--border);
    padding-top: 18px;
    font-size: 0.8rem;
    font-family: 'JetBrains Mono', monospace;
    opacity: 0.7;
}
.sn-support a {
    color: var(--accent);
    text-decoration: none;
    display: inline-flex;
    align-items: center;
}
.sn-support a:hover { text-shadow: 0 0 12px var(--accent-glow); }

.sn-theme-section { margin-top: 34px; }
.sn-theme-section hr { border: 0; border-top: 1px dashed var(--border); margin: 34px 0 30px 0; }

.sn-theme-head {
    display: flex;
    gap: 10px;
    align-items: baseline;
    font-family: 'JetBrains Mono', monospace;
    margin: 0 0 4px 0;
}
.sn-theme-head .prompt { color: var(--accent); white-space: nowrap; font-size: 1.1rem; font-weight: 700; }

.sn-theme-head h3 {
    margin: 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--accent);
}

.sn-theme-section img {
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 3px;
    background: var(--accent-glow);
    transition: box-shadow 0.25s ease, border-color 0.25s ease;
}
.sn-theme-section img:hover {
    border-color: var(--accent);
    box-shadow: 0 0 20px -6px var(--accent-glow);
}

.sn-theme-section p { font-size: 0.9rem; color: var(--text); }
.sn-theme-section p strong { color: var(--text); }

.sn-more {
    margin-top: 30px;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text-muted);
    font-size: 0.85rem;
}
</style>

<div class="page-content sn-shell">
<a href="/tools/" class="sn-back">&larr; cd /tools/</a>

  <div class="sn-cmd">
    <span class="prompt">$</span><span class="cmd"><span class="command-name">cat</span> /sn/themes.txt</span>
  </div>
  <p class="sn-intro">This page contains a collection of my <a href="https://standardnotes.com">Standard Notes</a> themes.</p>
  <p class="sn-license"><strong>All of my themes are published under the <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">GPL-3.0 License</a>.</strong></p>

  <div class="sn-support" style="display: flex; align-items: center;">
      <a href="https://buymeacoffee.com/passkeys" target="_blank">
          <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor" style="margin-right: 6px;"><path d="M19,10.01C19.82,10.01 20.61,10.23 21.31,10.63C22.31,11.22 23,12.28 23,13.5C23,14.73 22.31,15.78 21.31,16.37C20.61,16.77 19.82,17 19,17H18V18.5C18,20.43 16.43,22 14.5,22H6.5C4.57,22 3,20.43 3,18.5V4C3,2.9 3.9,2 5,2H16C17.1,2 18,2.9 18,4V10.01H19M16,18.5V4H5V18.5C5,19.33 5.67,20 6.5,20H14.5C15.33,20 16,19.33 16,18.5M19,15C19.55,15 20,14.55 20,14C20,13.45 19.55,13 19,13H18V15H19Z"/></svg>
          If you like my themes, buy me a beer
      </a>
  </div>

  <hr>

  <div class="sn-theme-section">
    <div class="sn-theme-head">
        <span class="prompt">$</span><h3>Standard Blue</h3>
    </div>
    <p>A light blue theme for Standard Notes.</p>

    <img src="https://files.horizon.pics/becc01e8-60e7-4b1c-b278-27ed17765201?a=480&region=eu-central&mime1=image&mime2=jpeg" alt="Standard Blue Preview">

    <p>To install, go to <strong>Preferences > Plugins > Install Custom Plugin</strong></p>
    <p>Paste the following link in the text box:<br>
    <code>https://listed.to/p/gWG2LYgCPH</code></p>
    <p>Alternatively, this theme is now included in the official Standard Notes Community Plugins repository.</p>
    <p>GitHub: <a href="https://github.com/PASSK3YS/standard-blue">PASSK3YS/standard-blue</a></p>
  </div>

  <div class="sn-theme-section">
    <hr>
    <div class="sn-theme-head">
        <span class="prompt">$</span><h3>Standard Blue Dark</h3>
    </div>
    <p>Dark mode version of Standard Blue theme.</p>

    <img src="https://files.horizon.pics/78705c14-553e-41d3-ad68-42389101deaa?a=480&region=eu-central&mime1=image&mime2=jpeg" alt="Standard Blue Dark Preview">

    <p>To install, go to <strong>Preferences > Plugins > Install Custom Plugin</strong></p>
    <p>Paste the following link in the text box:<br>
    <code>https://passk3ys.github.io/standard-blue-dark/ext.json</code></p>
    <p>Alternatively, this theme is now included in the official Standard Notes Community Plugins repository.</p>
    <p>GitHub: <a href="https://github.com/PASSK3YS/standard-blue-dark">PASSK3YS/standard-blue-dark</a></p>
  </div>

  <div class="sn-theme-section">
    <hr>
    <div class="sn-theme-head">
        <span class="prompt">$</span><h3>Dark Mint</h3>
    </div>
    <p>Dark Mint theme for Standard Notes.</p>

    <img src="https://files.horizon.pics/b2c6acf1-a8a6-41ae-adaf-9b2372e70428?a=480&region=eu-central&mime1=image&mime2=jpeg" alt="Dark Mint Preview">

    <p>To install, go to <strong>Preferences > Plugins > Install Custom Plugin</strong></p>
    <p>Paste the following link in the text box:<br>
    <code>https://passk3ys.github.io/dark-mint-theme/ext.json</code></p>
    <p>Alternatively, this theme is now included in the official Standard Notes Community Plugins repository.</p>
    <p>GitHub: <a href="https://github.com/PASSK3YS/dark-mint-theme">PASSK3YS/dark-mint-theme</a></p>
  </div>

  <div class="sn-theme-section">
    <hr>
    <div class="sn-theme-head">
        <span class="prompt">$</span><h3>Lights Out</h3>
    </div>
    <p>A pure black dark theme for Standard Notes.</p>

    <img src="https://files.horizon.pics/9bfda3fd-6a24-4cfc-ad4c-8bac6c1e7f41?a=480&region=eu-central&mime1=image&mime2=jpeg" alt="Lights Out Preview">

    <p>To install, go to <strong>Preferences > Plugins > Install Custom Plugin</strong></p>
    <p>Paste the following link in the text box:<br>
    <code>https://listed.to/p/rna5qVOnkD</code></p>
    <p>Alternatively, this theme is now included in the official Standard Notes Community Plugins repository.</p>
    <p>GitHub: <a href="https://github.com/PASSK3YS/lights-out">PASSK3YS/lights-out</a></p>
  </div>

  <div class="sn-theme-section">
    <hr>
    <div class="sn-theme-head">
        <span class="prompt">$</span><h3>Coffee</h3>
    </div>
    <p>A coffee inspired theme for Standard Notes</p>

    <img src="https://files.horizon.pics/51070bc4-e9eb-4841-9ca1-ac90b134ca99?a=480&region=eu-central&mime1=image&mime2=jpeg" alt="Coffee Preview">

    <p>To install, go to <strong>Preferences > Plugins > Install Custom Plugin</strong></p>
    <p>Paste the following link in the text box:<br>
    <code>https://listed.to/p/ufaeQELob3</code></p>
    <p>GitHub: <a href="https://github.com/PASSK3YS/coffee">PASSK3YS/coffee</a></p>
  </div>

  <hr>

  <p class="sn-more">More themes to be added soon. Check back later :-)</p>
</div>
