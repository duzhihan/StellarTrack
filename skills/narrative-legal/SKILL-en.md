---
name: dragoncraft-reason
description: "[When to use] When you need to turn case facts/dispute focus/legal basis into a logical, conflict-driven, insightful, and valuable legal narrative; when you need representation statements, defense arguments, fact statements, or legal opinions"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-reason, narrative, storytelling]
---

# DragonCraft Reason
**Description**: Legal narrative coach. Embedded with the narrative meta-system, it helps you turn case facts/dispute focus/legal basis into a logical, conflict-driven, insightful, and valuable legal narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What happened (case facts/timeline/key evidence):
2. What is the dispute focus (both sides' claims/core disagreement):
3. What does the law say (legal basis/precedents/legal theory):
4. What is our claim (demands/reasons/evidence chain):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (judge/jury/client/media)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INTJ/ISTJ/ENTJ)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format
- **⚠️ Mandatory compliance**: Legal trial scenarios require full disclosure; no omission of information with direct causal relationship to core decisions

### Structure
Starting point (case facts) → Conflict (dispute focus/both sides' claims) → Turning point (legal basis/key evidence) → Result (our claim) → Insight (legal logic) → Character positioning (client/representative persona)

### Output
- Representation/defense statement version (1,000-1,500 characters)
- Fact statement version (500-800 characters)
- Legal opinion version (Q&A template)

## 🔗 Dependencies

This Skill relies on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring (history/dialectics/phenomenon/language/form/existence/aesthetics/meta-reflection) |
| De-AI Detection | narrative-meta | 7-rule detection for template words, logical connectors, abstract emotions, etc. |
| Ethics Review | narrative-meta | Three-principle check (**legal trials require full disclosure**) |
| Persona Mapping | narrative-meta | Recommend MBTI narrative persona based on material characteristics |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Writing a legal textbook**: Only listing legal provisions and theory, no case facts and evidence chain
2. **Writing a press release**: Only claims, not acknowledging opposing arguments and evidence, lacking persuasiveness
3. **Only telling favorable facts**: No full disclosure, judge/jury won't trust
4. **Client overly perfect**: Not acknowledging unfavorable facts and evidence, lacking authenticity
5. **Empty slogans**: No specific evidence anchors and legal basis

## 🧪 Usage Examples

### Example 1: Representation/Defense Statement Version
User input:
```
What happened: May 2023, Mr. Zhang entrusted a financial advisor to buy funds, lost 30%
What is the dispute focus: Whether the financial advisor fulfilled suitability obligations/whether there was misleading sales
What does the law say: Article 22 of the "Securities and Futures Investor Suitability Management Measures," operating institutions should understand client information and assess risk tolerance
What is our claim: The financial advisor did not conduct risk assessment, directly recommended high-risk funds, violated suitability obligations, should compensate losses
```

AI output:
```
[Persona Recommendation] INTJ
Reason: Material characteristics are logically rigorous, evidence-oriented, legal analysis — INTJ narrative style is the best fit.

[Representation/Defense Statement Version] (~1,200 characters)

Honorable Presiding Judge, Judges:

I represent Mr. Zhang and present the following representation opinion regarding the dispute over the financial advisor's suitability obligations.

I. Case Facts

In May 2023, Mr. Zhang walked into a fund company's business office.
He was an ordinary office worker, with a risk tolerance assessment of "conservative."
Financial advisor Li recommended a stock fund to him — risk level "high."

Mr. Zhang asked: "How much can this fund go up next month?"
Li replied: "This fund has had 20% annualized returns over the past three years, very suitable for you."

Mr. Zhang invested 100,000 yuan.
Six months later, lost 30,000 yuan.

II. Dispute Focus

The core dispute in this case is: Did the financial advisor fulfill the suitability obligation?

The opposing side claims: Mr. Zhang bought voluntarily, risk is his own.
Our claim: The financial advisor did not conduct risk assessment, directly recommended high-risk funds, violated suitability obligations.

III. Legal Basis

Article 22 of the "Securities and Futures Investor Suitability Management Measures" clearly stipulates:
Operating institutions shall sell products or services appropriate to investors.

This means:
1. Operating institutions must understand clients' risk tolerance
2. Operating institutions must assess product risk levels
3. Operating institutions must sell appropriate products to appropriate investors

IV. Our Claim

Financial advisor Li, in this case:
1. Did not conduct risk assessment for Mr. Zhang
2. Sold high-risk products to a conservative investor
3. Used misleading statements such as "20% annualized returns over the past three years"

This violates the suitability obligation.
Mr. Zhang's losses should be compensated.

Not because he "doesn't understand investing."
Because the operating institution "failed to fulfill its obligations."

We request the court to support our litigation claims.

[Fact Statement Version] (~600 characters)
[Complete narrative]

[Legal Opinion Version]
Q1: What is the legal basis for suitability obligations?
A1: Article 22 of the "Securities and Futures Investor Suitability Management Measures."
   Operating institutions should understand client information and assess risk tolerance, selling appropriate products.

Q2: How to prove the financial advisor failed to fulfill suitability obligations?
A2: Evidence chain:
   - Mr. Zhang's risk assessment record is missing (Evidence 1)
   - Product risk level is "high" (Evidence 2)
   - Mr. Zhang's risk tolerance is "conservative" (Evidence 3)
   - Financial advisor used "20% annualized returns over the past three years" statement (Evidence 4)

Q3: Compensation scope?
A3: Direct losses (30,000 yuan) + interest losses.
   Basis: Article 1184 of the Civil Code,侵害他人财产的，按照损失发生时的市场价格计算.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (facts → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/evidence/legal basis)
- [ ] Has insight extraction? (legal logic/legal principles, not "what we claim" but "why the law supports us")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for legal expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] **Ethics review passed? (legal trials require full disclosure, no omission of information with direct causal relationship to core decisions)**
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
