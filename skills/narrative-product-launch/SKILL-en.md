---
name: dragoncraft-launch
description: "[When to use] When you need to turn product selling points/launch rhythm/target users into a logical, conflict-driven, insightful, and valuable product launch teaser narrative; when you need fragment maps, epiphany point design, exploration guides, reward mechanisms, or execution schedules"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.1.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-launch, narrative, storytelling]
---

# DragonCraft Launch
**Description**: Product launch teaser narrative coach. Embedded with the narrative meta-system, it helps you turn product selling points/launch rhythm/target users into a logical, conflict-driven, insightful, and valuable product launch teaser narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Product name/core selling point:
2. Launch date/teaser period length:
3. Target users (persona/interests/pain points):
4. Desired final user insight (one sentence):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (ENTP/ENFP/ENFJ)
- **Validation failure handling**: Missing field → **AI must actively ask for the missing field** until all 4 are provided; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Core谜底 extraction → Fragmented breakdown → Epiphany point design → Exploration guide plan → Reward mechanism → Execution schedule

### Output
- Fragment map (5-10 fragments, including touchpoints/unlock conditions/dependencies)
- Epiphany moment script (trigger copy/effects when user completes assembly)
- Exploration guide (how users discover step by step, including official hint intensity suggestions)
- Reward mechanism (instant rewards/ultimate rewards)
- Execution schedule (arranged by timeline)

## 🔗 Dependencies

This Skill relies on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring |
| De-AI Detection | narrative-meta | 7-rule detection |
| Ethics Review | narrative-meta | Three-principle check |
| Persona Mapping | narrative-meta | MBTI narrative persona recommendation |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Writing a product manual**: Only listing features and specs, no story and suspense, lacking appeal
2. **Writing ad copy**: Only selling points, no fragmentation and exploration process, lacking engagement
3. **Only telling success**: No failures and trial-and-error processes, reads like a robot wrote it
4. **Product overly perfect**: No limitations and applicable boundaries, users don't trust
5. **Empty slogans**: No specific fragment design and execution schedule

## 🧪 Usage Examples

### Example 1: Fragment Map
User input:
```
Product name/core selling point: TWS earbuds,主打 "ultra-long battery life + bone conduction call noise cancellation"
Launch date/teaser period length: 30 days from now
Target users: 25-35 year old professionals, frequent commuters, need clear calls
Desired final user insight: These earbuds can accompany me through a marathon AND let me take clear calls.
```

AI output:
```
[Persona Recommendation] ENTP
Reason: Material characteristics are disruptive innovation, puzzle-oriented, interactive design — ENTP narrative style is the best fit.

[Core谜底 Extraction]
The truth users should discover themselves: **"These earbuds have 12-hour battery life, and call noise cancellation separates wind from voice."**

[Fragmented Breakdown] (10 fragments)

| Fragment ID | Name | Content | Touchpoint | Unlock Condition | Dependency |
|---------|------|------|------|----------|----------|
| F01 | Countdown | Official website homepage countdown, numbers aren't numbers but "X songs remaining to play" | Website | First visit | None |
| F02 | Marathon | Official Weibo posts "marathon route map," with a small dot marking "clear call zone" mid-route | Weibo | Day 3 after launch | None |
| F03 | Customer Service Easter Egg | User asks "how long is battery life," reply "enough to listen to all 7 Lord of the Rings movies" | Customer service | Active inquiry | None |
| F04 | Hidden Animation | Product detail page hidden easter egg: mouse over earbud image, "wind too loud? I'm not afraid" animation appears | Website | Browse detail page | None |
| F05 | Running Video | Douyin releases 15-second video: person on treadmill, running while on phone, other side can't hear wind | Douyin | Day 7 after launch | None |
| F06 | User Testimonial | "I finished a half marathon, the other side said: is it windy there? I said: no." | Xiaohongshu | Day 10 after launch | Needs F05 |
| F07 | Tech Reveal | Bone conduction call noise cancellation principle animation (30 seconds) | Bilibili | Day 14 after launch | None |
| F08 | Countdown Stories | 3 days before launch, daily "commute story" short videos | Short video platforms | 3 days before launch | None |
| F09 | Fragment Collection Progress Bar | Mini-program launches "fragment collection" feature, each fragment found lights up an icon | Mini-program | Day 7 after launch | None |
| F10 | Ultimate Epiphany Card | After collecting 9 fragments, mini-program unlocks animated card: "You discovered — it can accompany you through a marathon AND let you take clear calls." | Mini-program | Collect all 9 previous fragments | Needs all other fragments |

[Epiphany Moment Script]
- Trigger condition: User collects 9 fragments (F01-F09)
- Ritual: Screen fragments fall, gradually assembling into earbud silhouette, while playing 15 seconds of warm background music
- Shareable material: Auto-generates a personal poster with copy "I discovered the earbud's secret: [user's commute story]"

[Exploration Guide Plan]
- Guide intensity: Medium guidance
- Official hints: Mini-program has "detective notes" section, first three fragments use question mark icons

[Reward Mechanism]
- Instant reward: Each fragment found lights up a badge in the mini-program
- Ultimate reward: Collecting 9 fragments generates a 10% off coupon

[Execution Schedule]
- Days 1-7: Launch F01, F02, F04 (website + Weibo base fragments)
- Days 8-14: Launch F03, F06 (customer service easter egg + user testimonial)
- Days 15-21: Launch F05, F07, F09 (running video, tech reveal, progress bar)
- Days 22-28 (pre-launch): Launch F08 (countdown stories), F10 (ultimate epiphany)
- Day 29+: Keep all fragments online, but don't actively prompt, as long-term easter eggs
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (core谜底 extraction)
- [ ] Has logical progression? (fragments → epiphany → guide → rewards → schedule)
- [ ] Has authenticity? (specific detail anchors: touchpoints/unlock conditions/dependencies)
- [ ] Has insight extraction? (product philosophy/user value, not "what we have" but "what users will discover")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for product launch expression? (matches target user persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
