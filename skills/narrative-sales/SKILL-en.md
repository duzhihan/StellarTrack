---
name: dragoncraft-persuade
description: "[When to use] When you need to turn customer pain points/purchase barriers/success cases into logical, conflict-driven, insightful, and valuable sales stories; when you need customer cases, sales scripts, objection handling, or sales training"
author: ant (CEO 助理)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-persuade, narrative, storytelling]
---

# DragonCraft Persuade
**Description**: Sales narrative coach. Embeds the narrative meta-system to help users turn customer pain points/purchase barriers/success cases into logical, conflict-driven, insightful, and valuable sales stories.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What problem did the customer encounter (pain points/scenarios/current state):
2. Why was the customer hesitant (barriers/concerns/competitors):
3. How did we persuade them (value proposition/proof/cases):
4. What changed for the customer (results/data/testimonials):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; missing any item requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires extracting the core
- **Format requirement**: User input is in natural language; AI automatically parses it into structured material
- **Audience persona** (optional): When provided, used to adjust narrative angle and language style (decision-maker/user/influencer)
- **Narrative persona** (optional): If not filled, automatically recommended based on material characteristics (ENFJ/ESFJ/ENTJ)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; format error → guide to correct format

### Structure
Starting point (customer pain point) → Conflict (hesitation/concerns/competitor comparison) → Turning point (value proposition/proof) → Result (customer change/data validation) → Cognition (sales philosophy) → Character positioning (sales persona)

### Output
- Customer case version (800-1200 characters)
- Sales script version (300-500 characters)
- Objection handling version (Q&A template)

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

1. **Written as a product manual**: Only listing features and specs, without customer scenarios and pain points
2. **Written as ad copy**: Only selling points, without customer stories and testimonials
3. **Only telling about success**: No customer hesitation or objection handling process, lacking authenticity
4. **Overly satisfied customer**: Not acknowledging product limitations and applicable boundaries, sounding robotic
5. **Empty slogans**: No specific customer testimonials or data anchors

## 🧪 Usage Examples

### Example 1: Customer Case Version
User input:
```
What problem did the customer encounter: Financial advisor recommended unsuitable products, customer lost 30%
Why was the customer hesitant: Worried "Optimal Life" was also selling courses, no trust
How did we persuade them: Don't teach stock picking, only provide tools; free 30-day trial first, decide after seeing results
What changed for the customer: Paid after 30 days, built own investment framework, no longer blindly following trends
```

AI output:
```
[Persona Recommendation] ENFJ
Reason: Material characteristics are inspirational narrative, trust-building, collective action. ENFJ narrative style is most suitable.

[Customer Case Version] (approx. 1000 characters)

"Aren't you another course-selling operation?"

That was the first question Mr. Zhang asked me.

March 2024, he came to me. Previously his financial advisor had recommended a fund.
Lost 30%. The advisor said: "Market's bad, just wait."

Mr. Zhang didn't want to wait anymore.

He tried cutting expenses. Tried researching on his own. Tried following big influencers.
Same result every time: losing money.

"Aren't you 'Optimal Life' also just selling courses?"

I said: "No. We don't teach stock picking, we only provide tools.
Try it free for 30 days. See the results, then decide."

30 days later, Mr. Zhang came back.

"I built my own investment framework," he said. "No longer blindly following trends. No longer anxious. No longer gambling."

He paid. Annual fee 299.

Not because of what we said.
Because of what he achieved.

[Sales Script Version] (approx. 400 characters)
[Full narrative]

[Objection Handling Version]
Q1: Aren't you selling courses?
A1: No. We don't teach stock picking, we only provide tools. Free 30-day trial first, decide after seeing results.

Q2: What's the difference from a financial advisor?
A2: Financial advisors tell you what to buy. We help you build a thinking framework.
   Opinions become outdated. Tools don't.

Q3: Does it really work?
A3: 1000+ users have built their own investment frameworks. Mr. Zhang is one of them.
   Try it for 30 days, decide after seeing results.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Opening hook? (scene/action/dialogue opening)
- [ ] Logical progression? (pain point → conflict → turning point → result → cognition)
- [ ] Authenticity? (specific detail anchors: time/location/numbers/customer testimonials)
- [ ] Cognitive extraction? (sales philosophy/value proposition, not "what we did," but "why customers chose us")
- [ ] Value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for sales expression? (matches target customer persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no factual distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field length within 20-500 characters?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
