---
name: dragoncraft-green
description: "[When to use] When you need to turn environmental concepts/actions/impact into logical, conflict-driven, insightful, and valuable sustainability narratives; when you need sustainability reports, calls to action, brand commitments, or ESG narratives"
author: ant (CEO 助理)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-green, narrative, storytelling]
---

# DragonCraft Green
**Description**: Sustainability narrative coach. Embeds the narrative meta-system to help users turn environmental concepts/actions/impact into logical, conflict-driven, insightful, and valuable sustainability narratives.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What environmental issue do we care about (topic/scenario/severity):
2. What did we do (actions/investment/collaboration):
3. What changed (results/data/impact):
4. What's next (commitments/goals/participation methods):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; missing any item requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires extracting the core
- **Format requirement**: User input is in natural language; AI automatically parses it into structured material
- **Audience persona** (optional): When provided, used to adjust narrative angle and language style (consumers/investors/regulators/NGOs)
- **Narrative persona** (optional): If not filled, automatically recommended based on material characteristics (INFJ/ENFJ/INFP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; format error → guide to correct format
- **⚠️ Mandatory compliance**: Sustainability narratives must not "greenwash"; must be supported by specific data and actions

### Structure
Starting point (environmental issue) → Conflict (current pain points/insufficient existing solutions) → Turning point (action entry/key breakthrough) → Result (change/data/impact) → Cognition (sustainability philosophy) → Character positioning (sustainability persona)

### Output
- Sustainability report version (800-1200 characters)
- Call to action version (300-500 characters)
- Brand commitment version (150-300 characters)

## 🔗 Dependencies

This Skill depends on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring (history/dialectics/phenomenology/language/form/existence/aesthetics/meta-reflection) |
| De-AI Detection | narrative-meta | 7-rule detection for template words, logical connectors, abstract emotions, etc. |
| Ethics Review | narrative-meta | Three-principle check (**sustainability narratives must not "greenwash"; must be supported by specific data and actions**) |
| Persona Mapping | narrative-meta | Recommend MBTI narrative persona based on material characteristics |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Written as PR copy**: Only listing environmental actions, without specific data and impact, lacking credibility
2. **Written as a tragedy**: Only dramatizing environmental crisis, without action and change, lacking hope
3. **Only telling about success**: Not acknowledging the complexity and long-term nature of sustainability, sounding robotic
4. **Overly perfect organization**: Not acknowledging shortcomings and areas for improvement, consumers don't trust
5. **Empty slogans**: No specific data anchors or action guides ("greenwashing" risk)

## 🧪 Usage Examples

### Example 1: Sustainability Report Version
User input:
```
What environmental issue do we care about: Plastic pollution, 8 million tons of plastic enter the ocean annually
What did we do: Launched biodegradable packaging, reduced plastic use by 50%, partnered with NGOs to clean oceans
What changed: 1 million users participated, 100 tons of plastic reduced, 10 km of coastline cleaned
What's next: Achieve 100% biodegradable packaging by 2026, invite user participation
```

AI output:
```
[Persona Recommendation] INFJ
Reason: Material characteristics are deep thinking, sustainability philosophy, long-termism. INFJ narrative style is most suitable.

[Sustainability Report Version] (approx. 1000 characters)

8 million tons.

That's the amount of plastic entering the ocean every year.
Equivalent to one garbage truck of plastic dumped into the ocean every minute.

We are not "victims."
We are "contributors."

In 2023, we did something:
We switched our product packaging from plastic to biodegradable materials.

Not "marketing."
"Must-do."

In the first year, we reduced plastic use by 50%.
Not "easy."
"Must do."

We partnered with NGOs to clean coastlines.
1 million users participated.
100 tons of plastic reduced.
10 km of coastline cleaned.

Data doesn't lie.
But data isn't everything.

More importantly:
1 million people started thinking about the "plastic" problem.
Not "others should do it."
"I should do it."

By 2026, we will achieve 100% biodegradable packaging.
Not "a goal."
"A commitment."

We invite you:
Participate. Supervise. Improve.

Because sustainability is not "our" business.
It's "all of our" business.

⚠️ Data in this report has been audited by a third party and is verifiable.

[Call to Action Version] (approx. 400 characters)
[Full narrative]

[Brand Commitment Version] (approx. 200 characters)
We commit to:
- Achieving 100% biodegradable packaging by 2026
- Publishing annual sustainability reports with third-party audited data
- Inviting user participation and oversight
- No "greenwashing," only action
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Opening hook? (scene/action/dialogue opening)
- [ ] Logical progression? (issue → conflict → turning point → result → cognition)
- [ ] Authenticity? (specific detail anchors: time/location/data/actions)
- [ ] Cognitive extraction? (sustainability philosophy/values, not "what we did," but "why we must do it")
- [ ] Value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for sustainability expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] **Ethics review passed? (sustainability narratives must not "greenwash"; must be supported by specific data and actions)**
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field length within 20-500 characters?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
