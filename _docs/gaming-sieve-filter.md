---
layout: default
title: Gaming sieve filter for Proton Mail
description: Filters gaming related emails into a gaming folder
category: Proton Mail
type: Resource
---

# Gaming sieve filter for Proton Mail

Before using this filter, ensure you have created a folder named "Gaming" in your Proton Mail settings. If you prefer a different name, update the "Gaming" text in the code below to match your folder name exactly.

```
require ["fileinto", "imap4flags"];

if anyof (
    address :domain :contains "from" [
        "steampowered.com",
        "steamcommunity.com",
        "playstation.com",
        "sonyentertainmentnetwork.com",
        "xbox.com",
        "microsoft.com",
        "nintendo.net",
        "nintendo.com",
        "twitch.tv",
        "discord.com",
        "epicgames.com",
        "gog.com",
        "blizzard.com",
        "battle.net",
        "riotgames.com",
        "ubisoft.com",
        "ea.com",
        "e.ea.com",
        "itch.io",
        "humblebundle.com",
        "greenmangaming.com",
        "fanatical.com",
        "rockstargames.com",
        "bungie.net",
        "roblox.com"
    ],
    header :contains "Subject" [
        "Steam Wishlist",
        "PlayStation Store",
        "Xbox Game Pass",
        "Nintendo Switch",
        "Twitch Drop",
        "Humble Bundle",
        "Epic Games Store"
    ]
) {
    fileinto "Gaming";
    stop;
}
```

## How to apply

1. Click the settings icon -> All settings -> Filters
2. Click Add sieve filter.
3. Name the filter (e.g., "Gaming Filter"), and paste the code into the script editor.
4. Click save.