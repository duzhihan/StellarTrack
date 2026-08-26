---
name: dragoncraft-care
description: "[When to use] When you need to turn medical conditions/treatment plans/risks and benefits into a logical, conflict-driven, insightful, and valuable medical narrative; when you need informed consent forms, doctor-patient communication scripts, medical education, or patient stories"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-care, narrative, storytelling]
---

# DragonCraft Care
**Description**: Medical narrative coach. Embedded with the narrative meta-system, it helps you turn medical conditions/treatment plans/risks and benefits into a logical, conflict-driven, insightful, and valuable medical narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What problem does the patient have (condition/symptoms/diagnosis):
2. What treatment options exist (options/risks/benefits):
3. How did patient and doctor decide (communication/consensus/values):
4. What was the result (efficacy/side effects/quality of life):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (patient/family/medical students/public)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INFJ/ISFJ/ENFJ)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format
- **⚠️ Mandatory compliance**: Medical informed consent scenarios require full disclosure; no omission of risk information with direct causal relationship to core decisions

### Structure
Starting point (condition/symptoms) → Conflict (treatment choices/risks vs benefits trade-off) → Turning point (doctor-patient communication/decision) → Result (efficacy/quality of life) → Insight (medical philosophy) → Character positioning (patient/doctor persona)

### Output
- Doctor-patient communication script version (500-800 characters)
- Patient story version (800-1,200 characters)
- Informed consent form version (structured template)

## 🔗 Dependencies

This Skill relies on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring (history/dialectics/phenomenon/language/form/existence/aesthetics/meta-reflection) |
| De-AI Detection | narrative-meta | 7-rule detection for template words, logical connectors, abstract emotions, etc. |
| Ethics Review | narrative-meta | Three-principle check (**medical informed consent requires full disclosure**) |
| Persona Mapping | narrative-meta | Recommend MBTI narrative persona based on material characteristics |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Writing a medical textbook**: Only listing medical terminology and plans, no patient stories and emotional connection
2. **Writing a press release**: Only efficacy, not acknowledging risks and side effects, lacking authenticity
3. **Only telling success**: No struggles and uncertainty in the treatment process, reads like a robot wrote it
4. **Doctor/patient overly perfect**: Not acknowledging the complexity of decisions and value conflicts, lacking authenticity
5. **Empty slogans**: No specific patient testimonials and data anchors

## 🧪 Usage Examples

### Example 1: Doctor-Patient Communication Script Version
User input:
```
What problem does the patient have: 65-year-old male, early-stage lung cancer, smoking history
What treatment options exist: Surgical resection (high risk/high cure rate)/radiation therapy (low risk/high recurrence rate)/conservative treatment
How did patient and doctor decide: Doctor explained risks and benefits of three options in detail, patient chose surgery
What was the result: Surgery successful, good recovery, successfully quit smoking
```

AI output:
```
[Persona Recommendation] INFJ
Reason: Material characteristics are deep healing, trust building, values alignment — INFJ narrative style is the best fit.

[Doctor-Patient Communication Script Version] (~700 characters)

Dr. Wang: Mr. Zhang, your test results are in. Early-stage lung cancer.

Mr. Zhang: (silence) ...Is it serious?

Dr. Wang: Early stage, detected in time. Cure rate is very high. But we need to discuss treatment options.

Mr. Zhang: What are the choices?

Dr. Wang: Three.
First, surgical resection. Highest cure rate, over 85%. But also the highest risk,
   given your age and smoking history, surgical complication risk is about 15%.
Second, radiation therapy. Lower risk, but higher recurrence rate, about 30% within 5 years.
Third, conservative treatment. No intervention, but the tumor will grow.

Mr. Zhang: ...Which do you recommend?

Dr. Wang: As a doctor, I recommend surgery. But as a person, I need to know your values.
   Do you value cure rate more, or surgical safety?

Mr. Zhang: My grandson was just born. I want to watch him grow up.

Dr. Wang: Then surgery is the better choice. We'll prepare thoroughly before surgery to reduce risk.

Mr. Zhang: OK. I'll have the surgery.

[Patient Story Version] (~1,000 characters)
[Complete narrative]

[Informed Consent Form Version]
Disease diagnosis: Early-stage lung cancer (T1N0M0)
Treatment plan: Surgical resection (lobectomy + lymph node dissection)

Risk description:
- Surgical complication risk: approximately 15% (infection/bleeding/air leak)
- Anesthesia risk: approximately 1% (severe adverse reactions)
- Mortality rate: approximately 0.5%

Benefit description:
- Cure rate: over 85%
- 5-year survival rate: over 90%

Alternative options:
- Radiation therapy: lower risk, 30% recurrence rate
- Conservative treatment: no intervention, tumor will grow

Patient statement:
I have fully understood the above information, understand the risks and benefits, and voluntarily choose the surgical option.

Patient signature:_________ Date:_________
Doctor signature:_________ Date:_________
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (condition → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/data/patient testimonials)
- [ ] Has insight extraction? (medical philosophy/doctor-patient relationship, not "what we did" but "why we chose this way")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for medical expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] **Ethics review passed? (medical informed consent requires full disclosure, no omission of risk information with direct causal relationship to core decisions)**
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
