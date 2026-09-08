---
layout: post
title: "Listed is shutting down: Finding a new home for your blog"
description: Listed by Standard Notes is shutting down. Here's what you can do if you're a Listed user.
image: "https://files.horizon.pics/4cda86a5-f81f-4186-a226-6c86c6c97b8d?a=480&region=eu-central&mime1=image&mime2=jpeg"
permalink: /blog/migrating-away-from-listed/
---

![Goodbye Listed](https://files.horizon.pics/4cda86a5-f81f-4186-a226-6c86c6c97b8d?a=480&region=eu-central&mime1=image&mime2=jpeg)

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

---

Another option is to host your blog using GitHub pages. GitHub pages is completely free and provides a static website which can be updated at any time. Here's how to set up a blogging website using GitHub pages.

### Step 1: Claim Your Space on GitHub
Create a free account at GitHub.com, or sign into your existing GitHub account.

a. Click the + icon in the top right corner and select New repository.

b. In the Repository name box, type `yourusername.github.io` (replace "yourusername" with your actual GitHub username). This exact naming convention is the specific trigger that tells GitHub to host this folder as a live website.

c. Check the box that says Add a README file.

d. Scroll to the bottom and click the green Create repository button.

### Step 2: Activate the Website
a. Inside your newly created repository, click the Settings tab (the gear icon near the top right).

b. On the left-hand sidebar, scroll down and click Pages.

c. Under the Build and deployment section, ensure the source is set to Deploy from a branch.

d. Under the Branch heading, select `main` from the dropdown menu and click Save.

e. Wait about two minutes. GitHub is now silently building your skeleton site in the background.

### Step 3: Write Your First Post

Because Listed.to relied on Markdown, you already know exactly how to write your content. GitHub Pages uses a background engine called Jekyll to turn those Markdown files into a styled blog.

a. Return to your repository's main page by clicking the <> Code tab.

b. Click Add file > Create new file.

c. In the file name box, type `_posts/2026-10-01-welcome.md`. Typing `_posts/` will automatically generate the required folder, and the strict `YYYY-MM-DD-title.md` naming format is required for Jekyll to recognize the file as a blog post.

d. At the very top of your file, you must include a hidden configuration block called "front matter." This tells the site how to handle the page. Paste this exactly:

```yaml
---
layout: post
title: "Finding a new home after Listed"
---
```
Below the second ``---``, write your blog post using standard Markdown.

e. Click the green Commit changes button at the top right to save and publish your post.

### Step 4: Apply a Theme

a. Return to your repository's main page by clicking the <> Code tab.

b. Click Add file > Create new file.

c. Name this file exactly _config.yml. This acts as the master control panel for your website.

d. On the first line, type the name of one of GitHub's supported starter themes, exactly like this:

`theme: jekyll-theme-minimal`

e. Click the green Commit changes button.

Once the background build finishes in a minute or two, your site will automatically pull the design files and transform your plain text into a styled web page.

If you want to experiment with different looks, you can edit that `_config.yml` file and swap `jekyll-theme-minimal` for other built-in options like: `jekyll-theme-cayman`, 
`jekyll-theme-hacker`, 
or `jekyll-theme-slate`.

---

If you need help with GitHub pages, please don't hesitate to [contact me](https://kieran.colfer.net/contact/){:target="_blank"}

Until next time...