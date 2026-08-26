---
name: dragoncraft-debate
description: "[When to use] When you need to turn controversy focus/stance/evidence into a logical, conflict-driven, insightful, and valuable controversy narrative; when you need position statements, debate scripts, response strategies, or controversy management"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-debate, narrative, storytelling]
---

# DragonCraft Debate
**Description**: Controversy narrative coach. Embedded with the narrative meta-system, it helps you turn controversy focus/stance/evidence into a logical, conflict-driven, insightful, and valuable controversy narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What is the controversy (focus/both sides' claims/public sentiment):
2. Where do we stand (stance/values/bottom line):
3. What is the evidence (data/facts/logical chain):
4. What do we want to achieve (goal/action/room for compromise):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (public/media/opponents/supporters)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (ENTP/INTJ/ENTJ)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format
- **⚠️ Mandatory compliance**: Controversy scenarios must acknowledge the validity of opposing viewpoints; no malicious attacks or personal attacks allowed

### Structure
Starting point (controversy focus) → Conflict (both sides' claims/public sentiment) → Turning point (evidence enters/stance clarified) → Result (our claim) → Insight (controversy philosophy) → Character positioning (controversy persona)

### Output
- Position statement version (500-800 characters)
- Debate script version (300-500 characters)
- Response strategy version (Q&A template)

## 🔗 Dependencies

This Skill relies on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring (history/dialectics/phenomenon/language/form/existence/aesthetics/meta-reflection) |
| De-AI Detection | narrative-meta | 7-rule detection for template words, logical connectors, abstract emotions, etc. |
| Ethics Review | narrative-meta | Three-principle check (**controversy scenarios must acknowledge the validity of opposing viewpoints**) |
| Persona Mapping | narrative-meta | Recommend MBTI narrative persona based on material characteristics |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Writing attack copy**: Only attacking the other side without acknowledging the validity of opposing viewpoints, lacking grace
2. **Writing a press release**: Only stance without evidence and logic, lacking persuasiveness
3. **Only saying we're right**: Not acknowledging complexity and room for compromise, reads like a robot wrote it
4. **Stance too rigid**: No room left for dialogue, invites backlash
5. **Empty slogans**: No specific evidence anchors and logical chains

## 🧪 Usage Examples

### Example 1: Position Statement Version
User input:
```
What is the controversy: Should financial advisors recommend high-risk products to conservative investors
Where do we stand: No. Suitability obligation is the bottom line; cannot sacrifice client interests for commissions
What is the evidence: Article 22 of the "Securities and Futures Investor Suitability Management Measures," 80% of users bought wrong products
What do we want to achieve: Promote industry suitability obligation implementation, protect investor rights
```

AI output:
```
[Persona Recommendation] ENTP
Reason: Material characteristics are challenging authority, counterintuitive viewpoints, debate-oriented — ENTP narrative style is the best fit.

[Position Statement Version] (~600 characters)

We don't take sides. We take the law.

Recently, "should financial advisors recommend high-risk products to conservative investors" has sparked controversy.

The other side says: Investors buy voluntarily, risk is their own.
We say: The premise of voluntary is informed consent. The premise of informed consent is suitability.

Article 22 of the "Securities and Futures Investor Suitability Management Measures" clearly stipulates:
Operating institutions shall sell products or services appropriate to investors.

This isn't "protecting the weak."
This is "protecting the rules."

Data doesn't lie:
300 million wealth management users. 80% bought the wrong products.
Not because they "don't understand."
Because no one told them "what's suitable."

Our stance is clear:
Suitability obligation is the bottom line.
Cannot sacrifice client interests for commissions.

We're not trying to "eliminate high-risk products."
We want "appropriate products sold to appropriate investors."

This isn't "over-regulation."
This is "returning to rules."

We call for:
Industry implements suitability obligations.
Investors learn to say "no."
Regulators strengthen enforcement.

Because the market doesn't need "heroes."
It needs "rules."

[Debate Script Version] (~400 characters)
[Complete narrative]

[Response Strategy Version]
Q1: Are you attacking financial advisors?
A1: No. We're attacking "inappropriate sales," not the "financial advisor" profession.
   The vast majority of financial advisors are professional. But rules need to be implemented.

Q2: Investors don't read risk levels themselves, whose fault is that?
A2: Blame information asymmetry. Financial advisors know product risks. Investors don't.
   Suitability obligation is about eliminating this asymmetry.

Q3: What goals do you want to achieve?
A3: Three goals:
   1. Industry implements suitability obligations
   2. Investors learn to say "no"
   3. Regulators strengthen enforcement
   This isn't a "zero-sum game." This is "win-win."
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (controversy → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/data/legal basis)
- [ ] Has insight extraction? (controversy philosophy/values, not "what we oppose" but "what we support")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for controversy expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] **Ethics review passed? (controversy scenarios must acknowledge the validity of opposing viewpoints; no malicious attacks or personal attacks allowed)**
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
