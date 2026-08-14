---
layout: doc
title: Server moderation regex patterns
description: A list of useful Discord regex patterns to fight against Discord scammers and spammers.
category: Discord
type: Resource
image: https://kieran.colfer.net/assets/docs-thumbnail.png
---

Mae'r ddogfen hon yn cynnwys patrymau regex defnyddiol y gallwch eu defnyddio yn eich gweinyddwyr Discord i rwystro ac atal sgamwyr a sbamwyr rhag targedu aelodau'ch gweinydd.

## Cymorth Ffug a "Agor Tocyn" Sgamiau
Mae'r patrwm regex hwn yn blocio sgamwyr sy'n ceisio dynwared negeseuon system swyddogol Discord, awgrymiadau ffug "agor tocyn ," a bots" Cymorth Cyswllt "maleisus.

```
(?i)0p£n-a-tlck£t|official discord support|x\.com/(?:Support|CreateCase2|ticket)|twitter\.com/(?:Support|ticket)|/CreateCase2|☎️ TALK WITH SUPPORT|SUPP0RT TICK£T|T£AM|TlCK£T|open-a?-t!cket|O𝐏ΕΝ ΤlCΚΕΤ|CREATE A TICKETT|CRE\*T T!CKE\.T|Raise-A-Ticket|PROMPT ASS!STANCE|hit up the team|Talk to the Mod|Share your questions|Submit your questions ?/ ?Issues below|ASK here Please|Get InTouch|REQUEST HELP|For quick resolution|admin/mod will guide you|Connect with the Admin|Consult the team|Post Questions to the Team|relay query to the crew|Relay your quer(?:y|ies)|Direct Your Issue/Question|For any issues and inquiries use|KINDLY RELATE YOUR ISSUES HERE|(?:live )?(?:help|support) desk|support team|𝐑𝐞𝐥𝐚𝐲 𝐲𝐨𝐮𝐫 𝐪𝐮𝐞𝐫𝐲|accidentally reported you
```

## Ariannol, Crypto & "Get Rich Cyflym" Sgamiau
Mae'r patrwm regex hwn yn blocio sgriptiau paragraff cymhleth, aml - linell a ddefnyddir gan fotiau crypto, datblygwyr blockchain ffug, a recriwtwyr "incwm goddefol ."

```
(?i)earn \$[0-9]+k|\$[0-9]+k or more within 72hours|10% of your profit|Crypto Market|partnered with OpenSea|collaborated with OPENSEA|We are an Metaverse brand|(?:pay|reimburse) me 10% of your profit|𝗽𝗮𝘆 𝗺𝗲 𝟭𝟬% 𝗼𝗳 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗳𝗶𝘁|\b(?:\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s+(?:daily|weekly|monthly|guaranteed)\b|\b(?:serious\s+inquiries|serious\s+people\s+only|guaranteed\s+earnings|instant\s+profit)\b.*?\b(?:earn|make|invest|profit)\b|\b(?:make|earn)\s+(?:\$?\d+k|\$\d{1,3}(?:,\d{3})*)\b|\b(?:retire\s+(?:your\s+)?parents|passive\s+income|investment\s+opportunity)\b|\b(?:made|earned)\s+\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s+(?:from|in)\s+(?:\d+\s+(?:days?|hours?|weeks?))\b.*?\b(?:first\s+\d+\s+persons?|people)\b.*?\b(?:\d+%|percent)\s+(?:profit|commission|earnings)\b.*?\b(?:dm|message|contact)\s+(?:me|us|now)\b|\b(?:teach|earn|help|learn|made)\b.*?\b(?:(?:\d+k|\$\d+(?:,\d{3})*(?:\.\d{2})?)|crypto|bitcoin|eth|(?:crypto)?currency|market|within\s+\d+\s+(?:hours?|days?)|first\s+\d+\s+people)\b.*?\b(?:dm|[mp][ae]ssage|contact|telegram|t\.me)\b|\b(?:help|learn|earn|profit|invest|wealth|mentor)\b.*?\b(?:\d+k|\$\d+(?:,\d{3})*(?:\.\d{2})?|crypto|bitcoin|eth|(?:crypto)?currency|market)\b.*?\b(?:dm|[mp][ae]ssage|contact|telegram|t\.me|ask\s+how)\b|As a blockchain developer|help (?:the first )?20 people|teach 10 people to earn|interested people should send a friend request|𝗡𝗼𝘁𝗲 𝗼𝗻𝗹𝘆 𝗶𝗻𝘁𝗲𝗿𝗲𝘀𝘁𝗲𝗱|My basic skills are as follows|enthusiastic people for a paid internship program
```

## Dolenni maleisus, Gwahoddiadau a Parth Gwe - rwydo
Mae'r patrwm regex hwn yn blocio byrlymwyr URL hysbys a gaiff eu cam - drin yn aml gan fotiau, clonau deinamig GitHub Pages, a chysylltiadau gwahodd Discord cudd.

```
(?i)stackhubs|technicalinquiry\.vercel\.app|technical.*\.github\.io/core|140\.99\.164\.68|84\.200\.91\.213|easyurl\.cc|share\.google/|t\.me/|tr\.ee/|dsc\.gg|(?:discordapp|discord)\.com/(?:invite|oauth2/authorize)|\bdiscord(?:app)?\.com\/invite\/\S+\b|%64%69%73%63%6f%72%64%2e%67%67|%64%73%63%2e%67%67|(?:discord|mailto|sms):/+(?:#@)?(?:discord\.gg|discord\.com|AmupQpGY8d)|\b(?:https?://[^\s<>\x60"]+?|www\.[^\s<>\x60"]+?)\s*(?:earn|help|teach|learn|crypto|bitcoin|eth|(?:crypto)?currency|market|giveaway)\s*(?:dm|[mp][ae]ssage|contact|telegram|t\.me)\b|https?://[^\s<>\x60"]+?\.(?:info|biz|io|me|ru|pw|gy|xyz|tk|ga|to|cf|ml|gq|stream|club|online|site|review|click|work)\b
```

## Cardiau Rhodd Ffug a Sgamiau Stêm
Mae'r patrwm regex hwn yn blocio dolenni galw heibio "Nitro am ddim ,"" Digwyddiad Cymunedol Stêm ," a chardiau rhodd ffug awtomataidd, gan gynnwys y rhai sy'n defnyddio homoglyffs Cyrilig i osgoi hidlwyr safonol (ee, `s7e @m ').

```&#10; (?i)[\$€£¥₹]?\d+[\$€£¥₹]?\s*rhodd.*(steam[az]*\.(com|net|org|rhodd|safle|siop|siop|ar-lein|dolen|cliciwch|xyz|io|to|ru|cn|de|uk|us|info|biz|co|byw|top|vip|pro|hwyl|cwmwl|ap|technoleg|byd|heddiw|canolfan|gemau|lawrlwytho|digidol|allwedd|promo|digwyddiad|adbrynu|c laim))|\b(?:[\$€£¥₹]\s*\d+(?:,\d{3})*(?:\.\d+)?(?:[kK])?\s*(?:rhodd(?:s?|cerdyn))|(?:\d+(?:,\d{3})*(?:\.\d+)?(?:[kK])?\s*(?:[\$€£¥₹])\s*(?:rhodd(?:s?|cerdyn))))\b|(s[t7][e3][a@][mrn][cс][o0][mrn][m]{0,2}[uµv][nµv][i1l!][t7y][y]?\.(com|io|net)\b)&#10; ```

## Fformatio Haciau, Obfuscation & Pings Offeren
Mae'r patrwm regex hwn yn rhwystro sgamwyr rhag osgoi hidlwyr gan ddefnyddio cromfachau system ffug, llwythi tâl amgodio URL dim lled, hypergysylltiadau Markdown ffug, neu bings '@everyone `anawdurdodedig.

Bydd y neges yn awtomatig -? dileu─ ◆ ─| | | | | | | | | | | | | | | | 👉| | |🔗👇|📨👉| |📥👇📥👉| Ht, tp, s :/ |neges yn awtomatig -? | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |<https?:\/\/(?:[^\s<> | | | |{{{ Za - Z0 -9 +/==}{<https?:\/\/[^\s<> 20,} [[{\ s |}}}}*[ 0 -9A - Fa - f ]{ 2 }[^\ s &lt;&gt;]]}}*[ A - Za - Za - Z0 -9 +/=]{ 20 ,}[^\ s
<>]*>|(\[.+\]\(.+\)) "&gt;'

## NSFW, "Cyswllt mewn Bio ," & Actorion Hysbys
Mae'r patrwm regex hwn yn blocio cyfrifon sgam penodol hysbys, rhifau ffôn ffug, dolenni penodol, a'r colyn clasurol "gwirio fy bio" a ddefnyddir i osgoi hidlwyr sgwrsio.

```
(?i)pornhub\. com |\ b (?: onlyfans| uwu | channn)\b |: eirin gwlanog: |\ b (?: telegram|t \.me |link\s*in\s* bio\s* (?: bio|proffil))\ b |\ (sut\). *telegram| cyswllt telegram ar fy bio|gofyn \( sut\) | sganio'r qr |\+1\s *\ (424\)\ s*424[-] 6672 | Jack_Cortez01 | Albertnguyen23 | Jonathanman123 | andrealgoodwin | Nicholas_Wallace2 | Tradewith_Hugo1 | Robinsonmanae_ 0
```