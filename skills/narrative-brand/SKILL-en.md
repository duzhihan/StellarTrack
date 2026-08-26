---
name: dragoncraft-soul
description: "[When to use] When you need to turn a brand's origin/mission/values into a logical, conflict-driven, insightful, and valuable brand story; when you need to build brand image, create brand manifestos, brand manuals, or founder stories"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-soul, narrative, storytelling]
---

# DragonCraft Soul
**Description**: Brand narrative coach. Embedded with the narrative meta-system, it helps you turn a brand's origin/mission/values into a logical, conflict-driven, insightful, and valuable brand story.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Why does the brand exist (mission/original intention/problem solved):
2. What do we believe in (values/principles/bottom lines):
3. What have we experienced (origin story/key turning points/lessons from failure):
4. What have we become (current state/achievements/user testimonials):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (ENFJ/INFJ/ENFP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point (brand's original intention) → Conflict (market pain points/internal struggles) → Turning point (key decision/epiphany) → Result (product/service/user change) → Insight (brand philosophy) → Character positioning (brand persona)

### Output
- Brand manifesto version (300-500 characters)
- Founder story version (800-1,500 characters)
- Brand manual summary version (within 150 characters)

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

1. **Writing a company introduction**: Only listing founding date and business, no conflict or insight
2. **Writing ad copy**: Only selling points without brand philosophy and values
3. **Only telling success**: No lessons from failure and internal struggles, lacking authenticity
4. **Brand overly perfect**: Lacking vulnerability and humanity, reads like a robot wrote it
5. **Empty slogans**: No specific scene anchors and user testimonials

## 🧪 Usage Examples

### Example 1: Brand Manifesto Version
User input:
```
Why does the brand exist: Seeing too many people misled by financial advisors, buying products unsuitable for them
What do we believe in: Tools are more important than opinions, action is more important than knowledge, walking together is more important than walking alone
What have we experienced: Quitting a fund company to start a business, failed, discovered "teaching people to trade stocks" doesn't work
What have we become: "Optimal Life" — doesn't teach stock trading, only provides tools, helped 1,000+ people build investment frameworks
```

AI output:
```
[Persona Recommendation] INFJ
Reason: Material characteristics are deep thinking, values-driven, sustainable philosophy — INFJ narrative style is the best fit.

[Brand Manifesto Version] (~400 characters)

We don't make predictions. We provide frameworks.

In 2023, I left the fund company where I'd worked for ten years.

Not because I was tired.
Because I was afraid — afraid that those financial advisors sitting in offices,
using the question "how much will it go up next month,"
were misleading those who trusted them.

I tried starting my own business. Failed. Clients left. Six months with no income.

During that time I realized something: The problem isn't "who's right or wrong,"
it's "tools versus opinions" — opinions become outdated, tools don't.

So "Optimal Life" was born.

We don't tell you what to buy. We help you build thinking frameworks.
We don't predict tomorrow's gains or losses. We help you understand market cycles.
We're not influencers. We're fellow travelers.

Because the real moat isn't information asymmetry.
It's cognitive asymmetry.

If you're also looking for a path that's "no gambling, no anxiety, no following the herd."

Welcome to walk with us.

[Founder Story Version] (~1,200 characters)
[Complete narrative]

[Brand Manual Summary Version] (~150 characters)
"Optimal Life" — doesn't teach stock trading, only provides tools. Core philosophy: tools are more important than opinions, action is more important than knowledge, walking together is more important than walking alone. The real moat isn't information asymmetry, it's cognitive asymmetry.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (original intention → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/user testimonials)
- [ ] Has insight extraction? (brand philosophy/values, not "what we did" but "why we exist")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for brand expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
