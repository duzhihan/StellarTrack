---
name: dragoncraft-shield
description: "[When to use] When you need to turn negative events/facts/affected parties/core commitments into a logical, conflict-driven, insightful, and valuable crisis PR narrative; when you need public statements, internal communication letters, or post-crisis live stream scripts"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.1.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-shield, narrative, storytelling]
---

# DragonCraft Shield
**Description**: Crisis PR narrative coach. Embedded with the narrative meta-system, it helps you turn negative events/facts/affected parties/core commitments into a logical, conflict-driven, insightful, and valuable crisis PR narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Event summary (what happened/timeline):
2. Confirmed facts (data/evidence/third-party conclusions):
3. Affected parties (users/public/employees/partners):
4. Brand/individual's core commitment (values/bottom line):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (public/media/internal)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INTJ/ISTJ/ENTJ)
- **Validation failure handling**: Missing field → **AI must actively ask for the missing field** until all 4 are provided; insufficient length → follow up for details; wrong format → guide to correct format
- **⚠️ Mandatory compliance**: Crisis PR scenarios must acknowledge mistakes; no deflection or fact concealment allowed

### Structure
Acknowledge fault → Explain what happened (no deflection) → Our emotions and reflection → Specific change actions (three points) → Compensation plan → Future commitment

### Output
- Public statement (social media/official website)
- Internal employee communication letter
- Post-crisis first live stream/interview script

## 🔗 Dependencies

This Skill relies on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring |
| De-AI Detection | narrative-meta | 7-rule detection |
| Ethics Review | narrative-meta | Three-principle check (**crisis scenarios require full disclosure**) |
| Persona Mapping | narrative-meta | MBTI narrative persona recommendation |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Writing blame-shifting copy**: Only external reasons, no self-reflection, lacking accountability
2. **Writing ad copy**: Only promises, no specific actions and compensation, lacking credibility
3. **Only saying we're right**: Not acknowledging mistakes and emotions, reads like a robot wrote it
4. **Brand overly perfect**: No vulnerability and reflection, public doesn't trust
5. **Empty slogans**: No specific action lists and compensation plans

## 🧪 Usage Examples

### Example 1: Public Statement
User input:
```
Event summary: A children's food brand was exposed by a user for finding a hair in the packaging
Confirmed facts: It was a hair about 2cm long, testing confirmed it wasn't from the production line (possibly mixed in during later packaging)
Affected parties: 1,000+ users who purchased this batch
Brand/individual's core commitment: Safety, transparency
```

AI output:
```
[Persona Recommendation] INTJ
Reason: Material characteristics are logically rigorous, data-oriented, reflective — INTJ narrative style is the best fit.

[Public Statement - WeChat/Weibo]

Title: Statement Regarding Foreign Object Found in XX Puffed Rice Packaging

Body:

"First, I'm sorry.

We received feedback from Ms. Li about finding a hair in the XX puffed rice packaging she purchased.
Regardless of the cause, this should not have happened.

Second, what we've done.

That day, we suspended sales of this batch and engaged a third-party agency for testing.
Results confirmed: The hair was not left on the production line (all production staff wear protective caps),
推测 it was accidentally mixed in during packaging.

But we won't blame 'accidents.'

We've upgraded the packaging process:
1. Added a manual light inspection, sampling once every 200 packages
2. For users who purchased this batch: full unconditional refunds plus a free sample of our new product

Third, our reflection.

We've always said 'nothing but the best for kids,' but we did slip up this one time.
Ms. Li's feedback taught us that safety isn't挂在 on the wall — it's checked package by package.

Starting today, we'll publish quality inspection records monthly. Welcome everyone to supervise.

Finally, Ms. Li, thank you for telling us.
We'll do better."

[Internal Employee Communication Letter] (excerpt)
[Complete narrative]

[Post-Crisis First Live Stream/Interview Script]
[Complete narrative]
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (starts with acknowledgment, no beating around the bush)
- [ ] Has logical progression? (acknowledge → explain → reflect → act → compensate → commit)
- [ ] Has authenticity? (specific detail anchors: time/place/data/affected parties)
- [ ] Has insight extraction? (crisis philosophy/new rules, not "we were wrong" but "how we'll prevent it from happening again")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for crisis expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] **Ethics review passed? (crisis scenarios require full disclosure, no fact concealment allowed)**
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
