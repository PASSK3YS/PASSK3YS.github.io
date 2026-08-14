---
layout: doc
title: Gaming sieve filter for Proton Mail
description: Filters gaming related emails into a gaming folder
category: Proton Mail
type: Resource
image: https://kieran.colfer.net/assets/docs-thumbnail.png
---

Cyn defnyddio'r hidlydd hwn, sicrhewch eich bod wedi creu ffolder o'r enw "Hapchwarae" yn eich gosodiadau Post Proton. Os yw'n well gennych enw gwahanol, diweddarwch y testun "Hapchwarae" yn y cod isod i gyd - fynd ag enw eich ffolder yn union.

```
angen [" fileinto ", "imap4flags "];

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

Sut i Ymgeisio

1. Cliciwch yr eicon gosodiadau -> Pob gosodiad -> Hidlau
2. Cliciwch Ychwanegu hidlydd gogr.
3. Enwch yr hidlydd (ee, "Hidlo Hapchwarae "), a gludwch y cod i'r golygydd sgript.
4. Cliciwch arbed.