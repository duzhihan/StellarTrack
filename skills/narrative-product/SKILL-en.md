---
name: dragoncraft-create
description: "[When to use] When you need to turn product positioning/user pain points/solutions into a logical, conflict-driven, insightful, and valuable product story; when you need product launch copy, user stories, competitive comparisons, or product manuals"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-create, narrative, storytelling]
---

# DragonCraft Create
**Description**: Product narrative coach. Embedded with the narrative meta-system, it helps you turn product positioning/user pain points/solutions into a logical, conflict-driven, insightful, and valuable product story.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What problem does the user have (pain points/scenarios/current state):
2. Why did we make this product (motivation/insights/differentiation):
3. How did we solve it (solution/technology/design):
4. What changed for users (results/data/testimonials):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (ENTP/ENFP/INTJ)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point (user pain points) → Conflict (insufficiency of existing solutions/technical bottlenecks) → Turning point (product birth/key breakthrough) → Result (user change/data validation) → Insight (product philosophy) → Character positioning (product persona)

### Output
- Product launch copy version (500-800 characters)
- User story version (800-1,200 characters)
- Product manual summary version (within 150 characters)

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

1. **Writing a product manual**: Only listing features and specs, no user scenarios and pain points
2. **Writing ad copy**: Only selling points, no product philosophy and user stories
3. **Only telling success**: No failures and iterations in the R&D process, lacking authenticity
4. **Product overly perfect**: Not acknowledging limitations and applicable boundaries, reads like a robot wrote it
5. **Empty slogans**: No specific user testimonials and data anchors

## 🧪 Usage Examples

### Example 1: Product Launch Copy Version
User input:
```
What problem does the user have: Too many people misled by financial advisors, buying products unsuitable for them
Why did we make this product: Tools are more important than opinions, action is more important than knowledge, walking together is more important than walking alone
How did we solve it: "Optimal Life" — doesn't teach stock trading, only provides tools, helps build investment frameworks
What changed for users: 1,000+ people built their own investment frameworks, no longer blindly follow trends
```

AI output:
```
[Persona Recommendation] ENTP
Reason: Material characteristics are disruptive innovation, problem-solving oriented, counterintuitive viewpoints — ENTP narrative style is the best fit.

[Product Launch Copy Version] (~600 characters)

We don't predict the market. We provide frameworks.

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

1,000+ people have built their own investment frameworks.
No longer blindly follow trends. No longer anxious. No longer gamble.

If you're also looking for a path that's "no gambling, no anxiety, no following the herd."

Welcome to walk with us.

[User Story Version] (~1,000 characters)
[Complete narrative]

[Product Manual Summary Version] (~150 characters)
"Optimal Life" — doesn't teach stock trading, only provides tools. Core philosophy: tools are more important than opinions, action is more important than knowledge, walking together is more important than walking alone. The real moat isn't information asymmetry, it's cognitive asymmetry.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (pain points → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/user testimonials)
- [ ] Has insight extraction? (product philosophy/values, not "what we did" but "why we exist")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for product expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
