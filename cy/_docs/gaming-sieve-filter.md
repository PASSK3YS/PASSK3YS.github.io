---
layout: doc
title: Gaming sieve filter for Proton Mail
description: Filters gaming related emails into a gaming folder
category: Proton Mail
type: Resource
image: https://kieran.colfer.net/assets/docs-thumbnail.png
---

Cyn defnyddio'r hidlydd hwn, gwnewch yn siŵr eich bod wedi creu ffolder o'r enw "Gaming" yn eich gosodiadau Proton Mail. Os yw'n well gennych enw gwahanol, diweddarwch y testun "Hapchwarae" yn y cod isod i gyd-fynd yn union ag enw'ch ffolder.

```
angen ["fileleinto", "imap4flags"];

os o gwbl (
    cyfeiriad :domain :contains "from" [
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
        "brwydr.net",
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
    pennawd : yn cynnwys "Pwnc" [
        "Rhestr dymuniadau Stêm",
        "PlayStation Store",
        "Tocyn Gêm Xbox",
        "Switsh Nintendo",
        "Twitch Drop",
        "Bwndel Humble",
        "Storfa Gemau Epig"
    ]
) {
    ffeil "Hapchwarae";
    stopio;
}
```

## Sut i wneud cais

1. Cliciwch yr eicon gosodiadau -> Pob gosodiad -> Hidlau
2. Cliciwch Ychwanegu hidlydd ridyll.
3. Enwch yr hidlydd (e.e., "Hidlydd Hapchwarae"), a gludwch y cod i'r golygydd sgript.
4. Cliciwch arbed.