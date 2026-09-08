---
layout: post
title: "Listed is shutting down: Finding a new home for your blog"
description: Listed by Standard Notes is shutting down. Here's what you can do if you're a Listed user.
---

[Standard Notes recently announced](https://listed.to/@Listed/76799/an-update-about-listed){:target="_blank"} that the intergrated minimalistic blogging platform, Listed.to will permanently shut down on December 31, 2026. 

If you have been using Listed, your writing isn't lost. All your past posts will remain safely and privately stored in your Standard Notes account. However, your public blog, guestbook, and any custom domain routing will go dark at the end of the year. The team is retiring the platform to focus on the core Standard Notes application.

If you are looking for a new home for your writing, you have two primary paths: adopting another minimalist platform, or taking full control by hosting a static blog yourself.

## Minimalist Alternatives to Listed.to
If you want a hosted platform that maintains the distraction-free, privacy-conscious ethos of Listed, consider these options:

**[Write.as](https://write.as){:target="_blank"}**
*   **Pricing:** A free tier provides a basic blog with platform branding. The Pro tier starts at $6/month, and a Team tier starts at $25/month.
*   **Features:** The editor supports standard Markdown and MathJax. It features built in ActivityPub federation, meaning users on platforms like Mastodon can follow the blog directly. The Pro tier unlocks custom domains, themes, code injection, and native photo hosting.
*   **Export & Data:** Writing can be exported as an ePub file, and the platform offers an open developer API for programmatic data access.

**[Bear Blog](https://bearblog.dev){:target="_blank"}**
*   **Pricing:** A free tier is available on a `bearblog.dev` subdomain. The Pro tier costs $5/month.
*   **Features:** It utilizes a pure Markdown editor and native browser rendering for maximum speed. It includes a built in "Discovery feed" that exposes writing to the broader Bear Blog community to help build an initial audience. Upgrading to Pro enables custom domains and custom CSS.
*   **Export & Data:** Built in tools provide easy export functionalities and full-content RSS feeds.

**[Micro.blog](https://micro.blog){:target="_blank"}**
*   **Pricing:** Hosting costs $5/month. There is no free hosted tier, though the social community features are free if the blog is hosted elsewhere.
*   **Features:** It operates as both a standalone blogging platform and a social network. It accommodates short, title-less posts as well as long-form essays using either a rich text or Markdown editor. The platform fully supports custom domains.
*   **Export & Data:** A core feature is automated cross-posting, allowing users to syndicate posts directly to other social networks and platforms via RSS.

**[Mataroa](https://mataroa.blog){:target="_blank"}**
*   **Pricing:** A free tier operates on a `mataroa.blog` subdomain. The premium version is $9/year, and 5% of all revenue funds CO₂ removal initiatives.
*   **Features:** It uses the Python-Markdown library and explicitly enforces minimalism. There are zero ads, tracking cookies, or analytics. To prevent design distractions, it intentionally lacks support for custom CSS, rich editors, pagination, and custom favicons. It includes native RSS feeds and a built in plain-text email newsletter for subscribers.
*   **Export & Data:** Users can export the entire blog at any time as a zip archive containing all raw Markdown files, making self-hosting migrations completely trivial.

## Taking Control: Hosting on GitHub Pages
If you want absolute control over your content, building a static site on GitHub Pages is a fantastic long-term solution. GitHub Pages natively supports a tool called Jekyll. Think of Jekyll as a robot that takes your simple text files and automatically stitches them together into a fully functioning website, without forcing you into a rigid platform.

### 1. Create your website's main folder (Repository)
Go to GitHub.com and sign up or log in. Click the "+" button at the top right and select "New repository". A repository is just a project folder. You must name it exactly like this to tell GitHub it is a website: yourusername.github.io (replace "yourusername" with your actual GitHub account name). Leave it public and click "Create".

### 2. Set up the website settings
In your new repository, click "Add file" and then "Create new file". Name this file `_config.yml`. This acts as the master settings file for the blog. Paste this exact text inside:

```yaml
title: "YOUR BLOG NAME HERE"
description: "DESCRIPTION OF YOUR BLOG HERE"
theme: jekyll-theme-minimal