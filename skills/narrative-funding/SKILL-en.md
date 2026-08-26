---
name: dragoncraft-quest
description: "[When to use] When you need to turn business models/market opportunities/team backgrounds into a logical, conflict-driven, insightful, and valuable funding story; when you need BP storylines, investor pitches, due diligence Q&A, or funding roadshows"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-quest, narrative, storytelling]
---

# DragonCraft Quest
**Description**: Funding narrative coach. Embedded with the narrative meta-system, it helps you turn business models/market opportunities/team backgrounds into a logical, conflict-driven, insightful, and valuable funding story.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What market opportunity exists (pain points/scale/trends):
2. Why can we do it (team background/technical barriers/resources):
3. How do we make money (business model/revenue model/growth logic):
4. What do we need (funding amount/use/milestones):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (VC/angel/strategic investors)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INTJ/ENTJ/ENTP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point (market opportunity) → Conflict (insufficiency of existing solutions/competitive landscape) → Turning point (team enters/technical breakthrough) → Result (business model/growth data) → Insight (investment logic) → Character positioning (founder/team persona)

### Output
- BP storyline version (800-1,200 characters)
- Investor pitch version (300-500 characters)
- Due diligence Q&A version (Q&A template)

## 🔗 Dependencies

This Skill relies on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring (history/dialectics/phenomenon/language/form/existence/aesthetics/meta-reflection) |
| De-AI Detection | narrative-meta | 7-rule detection for template words, logical connectors, abstract emotions, etc. |
| Ethics Review | narrative-meta | Three-principle check (fact distortion/inappropriate omission/privacy leakage) |
| Persona Mapping | narrative-meta | Recommend MBTI narrative persona based on material characteristics |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Writing a business plan**: Only listing data and models, no storyline and conflict
2. **Writing ad copy**: Only selling points, no investment logic and risk awareness
3. **Only telling success**: No lessons from failure and team struggles, lacking authenticity
4. **Team overly perfect**: Not acknowledging capability boundaries and needed resources, reads like a robot wrote it
5. **Empty slogans**: No specific data anchors and milestones

## 🧪 Usage Examples

### Example 1: BP Storyline Version
User input:
```
What market opportunity exists: Too many people misled by financial advisors, buying products unsuitable for them, trillion-yuan market scale
Why can we do it: 10 years in fund industry, from analyst to investment strategy lead, understand industry and users
How do we make money: Don't teach stock trading, only provide tools, monetize through knowledge communities/consulting/enterprise training
What do we need: 5 million yuan, for product development/content team/user growth, reach 100,000 paying users in 12 months
```

AI output:
```
[Persona Recommendation] INTJ
Reason: Material characteristics are systematic thinking, long-termism, strategic orientation — INTJ narrative style is the best fit.

[BP Storyline Version] (~1,000 characters)

Trillion-yuan market. Why are users still being misled?

In 2023, I left the fund company where I'd worked for ten years.

Not because I was tired.
Because I was afraid — afraid that those financial advisors sitting in offices,
using the question "how much will it go up next month,"
were misleading those who trusted them.

China has 300 million wealth management users. Annual market scale of trillions.
But 80% of users buy products unsuitable for them.

Why? Information asymmetry.

Financial advisors know what sells well. Users don't know what suits them.

I tried starting my own business. Failed. Clients left. Six months with no income.

During that time I realized something: The problem isn't "who's right or wrong,"
it's "tools versus opinions" — opinions become outdated, tools don't.

So "Optimal Life" was born.

We don't tell you what to buy. We help you build thinking frameworks.
We don't predict tomorrow's gains or losses. We help you understand market cycles.
We're not influencers. We're fellow travelers.

Because the real moat isn't information asymmetry.
It's cognitive asymmetry.

Business model: Don't teach stock trading, only provide tools.
- Knowledge community: 299/year, provides investment framework tools
- Consulting service: 999/session, personalized investment diagnosis
- Enterprise training: 5,000+/session, tool training for financial advisors

12-month goal: 100,000 paying users, ARR 30 million.

We need 5 million.
For product development (40%)/content team (30%)/user growth (30%).

If you also believe: tools are more important than opinions, action is more important than knowledge, walking together is more important than walking alone.

Welcome to walk with us.

[Investor Pitch Version] (~400 characters)
[Complete narrative]

[Due Diligence Q&A Version]
Q1: What's your competitive barrier?
A1: Not information asymmetry, but cognitive asymmetry. Our tools are the crystallization of 10 years of fund industry experience.
   Competitors can copy our content, but they can't copy our cognitive framework.

Q2: Why now?
A2: 300 million wealth management users, 80% bought the wrong products. Market education is complete, but tools are missing.
   Now is the best time for "from opinions to tools."

Q3: Team background?
A3: Founder has 10 years in fund industry, from analyst to investment strategy lead.
   Understands industry, understands users, understands tools.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (opportunity → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/team background)
- [ ] Has insight extraction? (investment logic/business model, not "what we did" but "why we can win")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for funding expression? (matches target investor persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
