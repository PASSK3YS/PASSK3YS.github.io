---
layout: default
title: Documentation
permalink: /docs/
---

<div class="page-content">
  <h1>Documentation</h1>
  <p>Guides and resources.</p>

  <ul class="post-list" style="list-style: none; padding: 0;">
    {% for doc in site.docs %}
      <li style="margin-bottom: 20px;">
        <span class="post-meta" style="font-size: 0.85em; opacity: 0.7;">DOC</span>
        <h3>
          <a class="post-link" href="{{ doc.url }}" style="text-decoration: none; font-size: 1.2em; font-weight: bold;">
            {{ doc.title }}
          </a>
        </h3>
        {% if doc.description %}
          <p style="margin-top: 5px;">{{ doc.description }}</p>
        {% endif %}
      </li>
    {% endfor %}
  </ul>
</div>