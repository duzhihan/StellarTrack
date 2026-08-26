---
name: dragoncraft-geek
description: "[When to use] When you need to turn tech barriers/market opportunities/team backgrounds into logical, conflict-driven, insightful, and valuable tech narratives; when you need tech stories, investor pitches, competitor analysis, or technical whitepapers"
author: ant (CEO 助理)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-geek, narrative, storytelling]
---

# DragonCraft Geek
**Description**: Tech narrative coach. Embeds the narrative meta-system to help users turn tech barriers/market opportunities/team backgrounds into logical, conflict-driven, insightful, and valuable tech narratives.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What problem does the technology solve (pain points/scenarios/insufficient existing solutions):
2. What are our tech barriers (patents/algorithms/data/team):
3. How big is the market opportunity (scale/trends/competitive landscape):
4. How do we monetize (business model/revenue model/growth logic):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; missing any item requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires extracting the core
- **Format requirement**: User input is in natural language; AI automatically parses it into structured material
- **Audience persona** (optional): When provided, used to adjust narrative angle and language style (VC/tech co-founder/customers/media)
- **Narrative persona** (optional): If not filled, automatically recommended based on material characteristics (INTJ/ENTJ/ENTP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; format error → guide to correct format

### Structure
Starting point (tech pain point) → Conflict (insufficient existing solutions/tech bottlenecks) → Turning point (tech breakthrough/team entry) → Result (market opportunity/business model) → Cognition (tech philosophy) → Character positioning (tech persona)

### Output
- Tech story version (800-1200 characters)
- Investor pitch version (300-500 characters)
- Competitor analysis version (comparison matrix)

## 🔗 Dependencies

This Skill depends on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring (history/dialectics/phenomenology/language/form/existence/aesthetics/meta-reflection) |
| De-AI Detection | narrative-meta | 7-rule detection for template words, logical connectors, abstract emotions, etc. |
| Ethics Review | narrative-meta | Three-principle check (factual distortion/inappropriate omission/privacy leakage) |
| Persona Mapping | narrative-meta | Recommend MBTI narrative persona based on material characteristics |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Written as a technical document**: Only listing technical specs and architecture, without storyline and market opportunity
2. **Written as ad copy**: Only selling points, no tech philosophy or values, lacking trust
3. **Only telling about success**: No failures and iterations during R&D, lacking authenticity
4. **Overly perfect technology**: Not acknowledging tech limitations and applicable boundaries, sounding robotic
5. **Empty slogans**: No specific data anchors or user testimonials

## 🧪 Usage Examples

### Example 1: Tech Story Version
User input:
```
What problem does the technology solve: Financial advisor recommended unsuitable products, information asymmetry leads to losses
What are our tech barriers: 10 years in fund industry, advisory strategy framework, tool-based methodology
How big is the market opportunity: 300 million finance users, trillion-yuan market, 80% buy wrong products
How do we monetize: Knowledge planet annual fee 299, consulting service 999, enterprise training 5000+
```

AI output:
```
[Persona Recommendation] INTJ
Reason: Material characteristics are systematic thinking, tech-oriented, strategic analysis. INTJ narrative style is most suitable.

[Tech Story Version] (approx. 1000 characters)

The problem isn't "who's right or wrong."
It's "tools vs. opinions."

In 2023, I left the fund company where I'd worked for 10 years.

Not because I was tired.
But because I was afraid—
I was afraid those financial advisors sitting in offices,
using the question "how much will it go up next month," were misleading people who trusted them.

China has 300 million finance users.
A trillion-yuan market every year.
But 80% of users buy products that don't suit them.

Why?

Because of information asymmetry.

Financial advisors know what sells.
Users don't know what suits them.

I tried starting my own business. Failed.
During that period I realized one thing:
Opinions become outdated. Tools don't.

So 「Optimal Life」 was born.

Our tech barrier isn't algorithms, isn't data.
It's the crystallization of 10 years in the fund industry.

From analyst to advisory strategy lead.
I've seen too many "good products"
eventually become users' "losses."

Why?

Because a good product doesn't mean it suits you.

Our tools don't tell you what to buy.
They help you build a thinking framework.

3 questions:
1. What are you buying? (product)
2. Why are you buying it? (logic)
3. When are you selling? (exit)

If you can't answer these.
You're not investing.
You're gambling.

Business model:
- Knowledge planet: annual fee 299, investment framework tools
- Consulting service: single session 999, personalized diagnosis
- Enterprise training: single session 5000+, financial advisor tool training

12-month target: 100,000 paying users, ARR 30 million.

Because the real moat isn't information asymmetry.
It's cognitive asymmetry.

[Investor Pitch Version] (approx. 400 characters)
[Full narrative]

[Competitor Analysis Version]
| Dimension | Financial Advisors | Big Influencers | Optimal Life |
|------|---------|---------|-----------|
| Core | Selling products | Selling opinions | Providing tools |
| Revenue | Commissions | Ads/courses | Annual fee/consulting |
| Users | Passive | Following trends | Proactive |
| Barrier | Channels | Traffic | Cognition |
| Risk | Compliance | Trust | Execution |
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Opening hook? (scene/action/dialogue opening)
- [ ] Logical progression? (pain point → conflict → turning point → result → cognition)
- [ ] Authenticity? (specific detail anchors: time/location/numbers/tech details)
- [ ] Cognitive extraction? (tech philosophy/values, not "what we did," but "why we can win")
- [ ] Value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for tech expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no factual distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field length within 20-500 characters?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
