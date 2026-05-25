---
layout: doc
title: Server moderation regex patterns
description: A list of useful Discord regex patterns to fight against Discord scammers and spammers.
category: Discord
type: Resource
---

This document contains useful regex patterns you can use in your Discord servers to block and prevent scammers and spammers from targeting your server members.

## Fake Support & "Open a Ticket" Scams
This regex pattern blocks scammers trying to mimic official Discord system messages, fake "open a ticket" prompts, and malicious "Contact Support" bots.

```
(?i)0p£n-a-tlck£t|official discord support|x\.com/(?:Support|CreateCase2|ticket)|twitter\.com/(?:Support|ticket)|/CreateCase2|☎️ TALK WITH SUPPORT|SUPP0RT TICK£T|T£AM|TlCK£T|open-a?-t!cket|O𝐏ΕΝ ΤlCΚΕΤ|CREATE A TICKETT|CRE\*T T!CKE\.T|Raise-A-Ticket|PROMPT ASS!STANCE|hit up the team|Talk to the Mod|Share your questions|Submit your questions ?/ ?Issues below|ASK here Please|Get InTouch|REQUEST HELP|For quick resolution|admin/mod will guide you|Connect with the Admin|Consult the team|Post Questions to the Team|relay query to the crew|Relay your quer(?:y|ies)|Direct Your Issue/Question|For any issues and inquiries use|KINDLY RELATE YOUR ISSUES HERE|(?:live )?(?:help|support) desk|support team|𝐑𝐞𝐥𝐚𝐲 𝐲𝐨𝐮𝐫 𝐪𝐮𝐞𝐫𝐲|accidentally reported you
```

## Financial, Crypto & "Get Rich Quick" Scams
This regex pattern blocks complex, multi-line paragraph scripts used by crypto bots, fake blockchain developers, and "passive income" recruiters.

```
(?i)earn \$[0-9]+k|\$[0-9]+k or more within 72hours|10% of your profit|Crypto Market|partnered with OpenSea|collaborated with OPENSEA|We are an Metaverse brand|(?:pay|reimburse) me 10% of your profit|𝗽𝗮𝘆 𝗺𝗲 𝟭𝟬% 𝗼𝗳 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗳𝗶𝘁|\b(?:\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s+(?:daily|weekly|monthly|guaranteed)\b|\b(?:serious\s+inquiries|serious\s+people\s+only|guaranteed\s+earnings|instant\s+profit)\b.*?\b(?:earn|make|invest|profit)\b|\b(?:make|earn)\s+(?:\$?\d+k|\$\d{1,3}(?:,\d{3})*)\b|\b(?:retire\s+(?:your\s+)?parents|passive\s+income|investment\s+opportunity)\b|\b(?:made|earned)\s+\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s+(?:from|in)\s+(?:\d+\s+(?:days?|hours?|weeks?))\b.*?\b(?:first\s+\d+\s+persons?|people)\b.*?\b(?:\d+%|percent)\s+(?:profit|commission|earnings)\b.*?\b(?:dm|message|contact)\s+(?:me|us|now)\b|\b(?:teach|earn|help|learn|made)\b.*?\b(?:(?:\d+k|\$\d+(?:,\d{3})*(?:\.\d{2})?)|crypto|bitcoin|eth|(?:crypto)?currency|market|within\s+\d+\s+(?:hours?|days?)|first\s+\d+\s+people)\b.*?\b(?:dm|[mp][ae]ssage|contact|telegram|t\.me)\b|\b(?:help|learn|earn|profit|invest|wealth|mentor)\b.*?\b(?:\d+k|\$\d+(?:,\d{3})*(?:\.\d{2})?|crypto|bitcoin|eth|(?:crypto)?currency|market)\b.*?\b(?:dm|[mp][ae]ssage|contact|telegram|t\.me|ask\s+how)\b|As a blockchain developer|help (?:the first )?20 people|teach 10 people to earn|interested people should send a friend request|𝗡𝗼𝘁𝗲 𝗼𝗻𝗹𝘆 𝗶𝗻𝘁𝗲𝗿𝗲𝘀𝘁𝗲𝗱|My basic skills are as follows|enthusiastic people for a paid internship program
```

## Malicious Links, Invites & Phishing Domains
This regex pattern blocks known URL shorteners frequently abused by bots, dynamic GitHub Pages clones, and hidden Discord invite links.

```
(?i)stackhubs|technicalinquiry\.vercel\.app|technical.*\.github\.io/core|140\.99\.164\.68|84\.200\.91\.213|easyurl\.cc|share\.google/|t\.me/|tr\.ee/|dsc\.gg|(?:discordapp|discord)\.com/(?:invite|oauth2/authorize)|\bdiscord(?:app)?\.com\/invite\/\S+\b|%64%69%73%63%6f%72%64%2e%67%67|%64%73%63%2e%67%67|(?:discord|mailto|sms):/+(?:#@)?(?:discord\.gg|discord\.com|AmupQpGY8d)|\b(?:https?://[^\s<>\x60"]+?|www\.[^\s<>\x60"]+?)\s*(?:earn|help|teach|learn|crypto|bitcoin|eth|(?:crypto)?currency|market|giveaway)\s*(?:dm|[mp][ae]ssage|contact|telegram|t\.me)\b|https?://[^\s<>\x60"]+?\.(?:info|biz|io|me|ru|pw|gy|xyz|tk|ga|to|cf|ml|gq|stream|club|online|site|review|click|work)\b
```

## Fake Gift Cards & Steam Scams
This regex pattern blocks automated "Free Nitro," "Steam Community Event," and fake gift card drop links, including those using Cyrillic homoglyphs to bypass standard filters (e.g., `s7e@m`).

```
(?i)[\$€£¥₹]?\d+[\$€£¥₹]?\s*gift.*(steam[a-z]*\.(com|net|org|gift|site|shop|store|online|link|click|xyz|io|to|ru|cn|de|uk|us|info|biz|co|live|top|vip|pro|fun|cloud|app|tech|world|today|center|games|download|digital|key|promo|event|redeem|claim))|\b(?:[\$€£¥₹]\s*\d+(?:,\d{3})*(?:\.\d+)?(?:[kK])?\s*(?:gift(?:s?|card))|(?:\d+(?:,\d{3})*(?:\.\d+)?(?:[kK])?\s*(?:[\$€£¥₹])\s*(?:gift(?:s?|card))))\b|(s[t7][e3][a@][mrn][cс][o0][mrn][m]{0,2}[uµv][nµv][i1l!][t7y][y]?\.(com|io|net)\b)
```

## Formatting Hacks, Obfuscation & Mass Pings
This regex pattern blocks scammers from bypassing filters using fake system brackets, zero-width URL encoding payloads, fake Markdown hyperlinks, or unauthorized `@everyone` pings.

```
(?i)─ ◆ ─|ᵐᵉˢˢᵃᵍᵉ ʷⁱˡˡ ᵃᵘᵗᵒ-ᵈᵉˡᵉᵗᵉ|><>|go here for 👉|🔗👇|📨👉|📥👇|📥👉|ht, tp, s:/|message will auto-?delete|ᵀʰᶦˢ ᵐᵉˢˢᵃᵍᵉ ʷᶦˡˡ ᵃᵘᵗᵒ⁻ᵈᵉˡᵉᵗᵉ|@(?:here|everyone)\b|<https?:\/\/(?:[^\s<>]*%[0-9A-Fa-f]{2}[^\s<>]*)+>|<https?:\/\/[^\s<>]*[A-Za-z0-9+/=]{20,}[^\s<>]*>|(\[.+\]\(.+\))
```

## NSFW, "Link in Bio", & Known Actors
This regex pattern blocks specific known scam accounts, fake phone numbers, explicit links, and the classic "check my bio" pivot used to evade chat filters.

```
(?i)pornhub\.com|\b(?:onlyfans|uwu|channn)\b|:peach:|\b(?:telegram|t\.me|link\s*in\s*bio\s*(?:bio|profile))\b|\(HOW\).*telegram|telegram link on my bio|asking \(HOW\)|scan this qr|\+1\s*\(424\)\s*424[‑-]6672|Jack_Cortez01|Albertnguyen23|Jonathanman123|andrealgoodwin|Nicholas_Wallace2|Tradewith_Hugo1|Robinsonmanae_0
```
