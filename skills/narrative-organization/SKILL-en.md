---
name: dragoncraft-shift
description: "[When to use] When you need to turn change drivers/resistance points/target states into a logical, conflict-driven, insightful, and valuable organizational change narrative; when you need internal letters, all-hands speeches, change FAQs, or change roadmaps"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-shift, narrative, storytelling]
---

# DragonCraft Shift
**Description**: Organizational change narrative coach. Embedded with the narrative meta-system, it helps you turn change drivers/resistance points/target states into a logical, conflict-driven, insightful, and valuable organizational change narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Why must we change (drivers/crisis/opportunities):
2. What are we changing (scope/impact):
3. What is everyone worried about (resistance/concerns/uncertainty):
4. What will it be like after change (vision/milestones/support):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (management/frontline employees/external stakeholders)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (ENFJ/ENTJ/INFJ)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point (change drivers) → Conflict (current pain points/resistance points) → Turning point (change decision/key actions) → Result (target state/milestones) → Insight (change philosophy) → Character positioning (organization persona)

### Output
- Internal letter/all-hands speech version (800-1,200 characters)
- Change roadmap version (500-800 characters)
- Change FAQ version (Q&A template)

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

1. **Writing an announcement**: Only listing change items and schedules, no storyline and emotional connection
2. **Writing a press release**: Only vision, not acknowledging resistance and uncertainty, lacking authenticity
3. **Only telling success**: No past failures and current struggles, reads like a robot wrote it
4. **Organization overly perfect**: Not acknowledging change risks and growing pains, employees don't trust
5. **Empty slogans**: No specific milestones and support measures

## 🧪 Usage Examples

### Example 1: Internal Letter/All-Hands Speech Version
User input:
```
Why must we change: Traditional fund sales model declining, users no longer trust financial advisors
What are we changing: From sales-oriented to tool-oriented, building the "Optimal Life" brand
What is everyone worried about: Income decline, skill mismatch, new business uncertainty
What will it be like after change: Build new business model within 12 months, provide training and support, grow together
```

AI output:
```
[Persona Recommendation] ENFJ
Reason: Material characteristics are inspiring narrative, collective action, trust building — ENFJ narrative style is the best fit.

[Internal Letter/All-Hands Speech Version] (~1,000 characters)

Dear colleagues:

Today I want to talk to you about something big.

Over the past three years, our traditional fund sales model has been declining.
Not because we're not working hard. Because users no longer trust financial advisors.

They've been misled. They've lost money. They're afraid.

During the half year I left the fund company to start my own business, I saw an even harsher reality:
300 million wealth management users, 80% bought products unsuitable for them.

The problem isn't "who's right or wrong."
It's "tools versus opinions" — opinions become outdated, tools don't.

So we must change.

From sales-oriented to tool-oriented.
From "telling you what to buy" to "helping you build thinking frameworks."
From "financial advisors" to "fellow travelers."

I know what you're worried about.

Will income decline? Yes. In the first 6 months, possibly down 30%.
Skill mismatch? Right. So we'll provide training to help you transition.
New business uncertain? Yes. But not changing is even more uncertain.

What will it be like after change?

Within 12 months, we'll build a new business model.
"Optimal Life" — doesn't teach stock trading, only provides tools.
Tools are more important than opinions. Action is more important than knowledge. Walking together is more important than walking alone.

We'll provide:
- Transition training (3 months)
- New business revenue share (guaranteed minimum for first 6 months)
- Team support (weekly reviews)

This isn't one person's change.
It's all of our change.

If you also believe: tools are more important than opinions.

Welcome to walk with us.

[Change Roadmap Version] (~600 characters)
[Complete narrative]

[Change FAQ Version]
Q1: How much will my income decline?
A1: Possibly down 30% in the first 6 months. We provide a guaranteed minimum plan to ensure basic income.

Q2: Do I need to learn new skills?
A2: Yes. But we'll provide 3 months of training, weekly reviews, to help you transition.

Q3: Can the new business really succeed?
A3: Uncertain. But not changing is even more uncertain. The traditional model has been declining for 3 years.
   Let's try together. If it fails, I take responsibility. If it succeeds, we share the成果.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (drivers → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/milestones)
- [ ] Has insight extraction? (change philosophy/values, not "we must change" but "why we must change")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for organizational expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
