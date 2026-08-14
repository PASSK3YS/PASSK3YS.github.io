---
layout: doc
title: Server moderation regex patterns
description: A list of useful Discord regex patterns to fight against Discord scammers and spammers.
category: Discord
type: Resource
image: https://kieran.colfer.net/assets/docs-thumbnail.png
---

Mae'r ddogfen hon yn cynnwys patrymau regex defnyddiol y gallwch eu defnyddio yn eich gweinyddwyr Discord i rwystro ac atal sgamwyr a sbamwyr rhag targedu aelodau eich gweinydd.

## Cefnogaeth Ffug & Sgamiau "Agor Tocyn".
Mae'r patrwm regex hwn yn blocio sgamwyr sy'n ceisio dynwared negeseuon system swyddogol Discord, awgrymiadau ffug "agor tocyn", a botiau "Cysylltu â Chymorth" maleisus.

```
(?i)0p£n-a-tlck£t|cymorth anghytgord swyddogol|x\.com/(?:Support|CreateCase2|tocyn)|twitter\.com/(?:Support|tocyn)|/CreateCase2|☎️ SIARAD GYDA CHEFNOGAETH|CEFNOGAETH TIC£T|T£AM|TlCK£T|agored-a?-t!cket|O𝐏ΕΝ ΤlCΚΕΤ| CREU TOCYN|CRE\*T T!CKE\.T|Codi-A-Tocyn|Safiad ASS!Cyrchwch y tîm|Siaradwch â'r ModS|Rhannwch eich cwestiynau isod|Rhannwch eich cwestiynau? Os gwelwch yn dda|Cysylltwch â Ni|CAIS AM GYMORTH|I'w ddatrys yn gyflym|Bydd admin/mod yn eich arwain|Cysylltu â'r Gweinyddol|Ymgynghorwch â'r tîm|Post Cwestiynau i'r Tîm| Ymholiad cyfnewid i'r criw|Cyfnewid eich ymholiad(?:y|ies)|Cyfarwyddwch Eich Mater/Cwestiwn|Ar gyfer unrhyw faterion ac ymholiadau defnyddiwch|Cynorthwyo|Byw'n BERTHNASOL CHI?(Cymorth) desg|tîm cymorth|𝐑𝐞𝐥𝐚𝐲 𝐲𝐨𝐮𝐫 𝐪𝐮𝐞𝐫𝐲|wedi eich adrodd yn ddamweiniol
```

## Sgamiau Ariannol, Crypto a "Get Rich Quick".
Mae'r patrwm regex hwn yn blocio sgriptiau paragraff cymhleth, aml-linell a ddefnyddir gan bots crypto, datblygwyr blockchain ffug, a recriwtwyr "incwm goddefol".

```
(?i)ennill \$[0-9]+k|\$[0-9]+k neu fwy o fewn 72 awr|10% o'ch elw|Marchnad Crypto|mewn partneriaeth ag OpenSea|cydweithio ag OPENSEA|Rydym yn frand Metaverse|(?:talu|ad-daliad) i mi 10% o'ch elw | 𝗗𗝲 𝟭𝟬 % 𝗼𝗳 𝘆𝗼𝘂𝗿 𝗽𝗿𝗼𝗳𝗶𝘁|\b(?:\$\d{1,3}(?:,\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?)\s+(?:yn ddyddiol|wythnosol|misol|gwarantedig)\b|\b(?:seriously|pobl-ymchwil" s+yn unig|gwarantu\s+enillion|ar unwaith\s+elw)\b.*?\b(?:ennill|gwneud|buddsoddi|elw)\b|\b(?:gwneud|ennill)\s+(?:\$?\d+k|\$\d{1,3}(?:,\d{ 3})*)\b|\b(?:retire\s+(?:your\s+)?rieni|goddefol\s+incwm|cyfle buddsoddi\s+)\b|\b(?:gwnaed|ennill)\s+\$\d{1,3}(?:,\d{3})*( ?:\.\d{2})?\s+(?:from|in)\s+(?:\d+\s+(?:days?|oriau?|wythnosau?))\b.*?\b(?:first\s+\d+\s+personau?|pobl)\b.*?\b(?:\d+%(percent)) ?: elw $\d+(?:,\d{3})*(?:\.\d{2})?)|crypto|bitcoin|eth|(?:crypto)?currency|marchnad|o fewn\s+\d+\s+(?:oriau?|diwrnodau?)|cyntaf\s+\d+\s+bobl) \b.*?\b(?:dm|[mp][ae]ssage|cysylltu|telegram|t\.me)\b|\b(?:help|dysgu|ennill|elw|buddsoddi|cyfoeth|mentor)\b.*?\b(?:\d+k|\$\d+(?:,\d) {3})*(?:\.\d{2})?|crypto|bitcoin|eth|(?:crypto)?currency|marchnad)\b.*?\b(?:dm|[mp][ae]ssage|cyswllt|telegram|t\.me|gofynnwch\s+sut)\b|As datblygwr blockchain|cymorth (?:y cyntaf )?20 o bobl|dysgu 10 o bobl i ennill|dylai pobl â diddordeb anfon cais ffrind|𝗡𝗼𝘁𝗲 𝗼𝗻𝗹𝘆 𝗶𝗻𝘁𝗲𝗿𝗘𝗲𝗿𝗘𝗲𝗿𝗘𝗲 yn dilyn|pobl frwdfrydig ar gyfer rhaglen interniaeth â thâl
```

## Dolenni Maleisus, Gwahoddiadau a Pharthau Gwe-rwydo
Mae'r patrwm regex hwn yn blocio byrwyr URL hysbys sy'n cael eu cam-drin yn aml gan bots, clonau deinamig GitHub Pages, a dolenni gwahoddiad cudd Discord.

```
(?i)stackhubs|technicalinquiry\.vercel\.app|technical.*\.github\.io/core|140\.99\.164\.68|84\.200\.91\.213|easyurl\.cc|share\.google/|t\.me/|tr\dissee.| pp|discord)\.com/(?:invite|oauth2/authorize)|\bdiscord(?:app)?\.com\/invite\/\S+\b|% 64%69%73%63%6f%72%64%2e%67%67|%64%73%63%2e%67%67|(?:discord|mailto|sms):/+(?:#@)?(?: discord\.gg|discord\.com|AmupQpGY8d)|\b(?:https?://[^\s<>\x60"]+?|www\.[^\s<>\x60"]+?)\s*(?:earn|help|teach|dysgu|crypto|bitcoin|eth|(?:crypto)currencywaymarket| )\s*(?:dm|[mp][ae]ssage|cyswllt|telegram|t\.me)\b|https?://[^\s<>\x60"]+?\.(?:info|biz|io|me|ru|pw|gy|xyz|tk|ga|to|cf|ml|gq|stream|review|clwb|c|
```

## Cardiau Anrheg Ffug a Sgamiau Stêm
Mae'r patrwm regex hwn yn blocio awtomataidd "Nitro Am Ddim," "Digwyddiad Cymunedol Steam," a dolenni gollwng cerdyn rhodd ffug, gan gynnwys y rhai sy'n defnyddio homoglyffau Cyrillig i osgoi hidlwyr safonol (ee, `s7e@m`).

```
(?i)[\$€£¥₹]?\d+[\$€£¥₹]?\s*rhodd.*(stêm[a-z]*\.(com|net|org|anrheg|safle|siop|siop|ar-lein|dolen|cliciwch|xyz|io|i|ru|cn|de| uk | ni laim))|\b(?:[\$€£¥₹]\s*\d+(?:,\d{3})*(?:\.\d+)?(?:[kK])?\s*(?:gift(?:s?|cerdyn))|(?:\d+(?:,\d{3})*(?)(?) ?:[\$€£¥₹])\s*(?:anrheg(?:s?|card)))\b|(s[t7][e3][a@][mrn][cс][o0][mrn][m]{0,2}[uµv][nµv][i1l!][t7y][y]?\net.(b) |
```

## Fformatio Hacau, Obfuscation & Mass Pings
Mae'r patrwm regex hwn yn rhwystro sgamwyr rhag osgoi hidlwyr gan ddefnyddio cromfachau system ffug, llwythi tâl amgodio URL sero lled, hypergysylltiadau Markdown ffug, neu pings `@pawb` anawdurdodedig.

```
(?i)─ ◆ ─|ᵐᵉˢˢᵃᵍᵉ ʷⁱˡˡ ᵃᵘᵗᵒ-ᵈᵉˡᵉᵗᵉ|><>|ewch yma am 👉|🔗👇|📨👉|📥👇|📥👉|ht, tp, s:/|bydd neges yn awto-?dileer|ᵀʰᶦˢ ᵐᵉˢˢᵃᵍᵉʷ ᵃᵘᵗᵒ⁻ᵈᵉˡᵉᵗᵉ|@(?:yma|pawb)\b|< https?:\/\/(?:[^\s<>]*%[0-9A-Fa-f]{2}[^ \s<>]*)+>|<https?:\/\/[^\s<>]*[A-Za-z0-9+/=]{20,}[^\s<>]*>|(\[.+\]\(.+\))
```

## NSFW, "Link in Bio", ac Actorion Hysbys
Mae'r patrwm regex hwn yn blocio cyfrifon sgam hysbys penodol, rhifau ffôn ffug, dolenni penodol, a'r colyn "gwirio fy bio" clasurol a ddefnyddir i osgoi ffilterau sgwrsio.

```
(?i)pornhub\.com|\b(?:onlyfans|uwu|channn)\b|:peach:|\b(?:telegram|t\.me|link\s*in\s*bio\s*(?:bio|profile))\b|\(SUT\).*telegram|telegram \ dolen ar fy bio| gofyn hyn HO| qr|\+1\s*\(424\)\s*424[--]6672|Jack_Cortez01|Albertnguyen23|Jonathanman123|andrealgoodwin|Nicholas_Wallace2|Masnach gyda_Hugo1|Robinsonmanae_0
```