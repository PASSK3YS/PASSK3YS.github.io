---
layout: default
title: Documentation
permalink: /docs/
---

<div class="page-content">
  <h1>Documentation</h1>
  <p>Tutorials, guides, and resources.</p>

  {% assign grouped_docs = site.docs | group_by: "category" %}

  {% for group in grouped_docs %}
    <div class="docs-section" style="margin-top: 40px;">
      <h2 style="border-bottom: 1px solid var(--border-color); padding-bottom: 10px; margin-bottom: 20px;">
        {{ group.name | default: "General" }}
      </h2>
      
      <ul class="post-list" style="list-style: none; padding: 0;">
        {% for doc in group.items %}
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
  {% endfor %}

</div>