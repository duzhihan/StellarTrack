---
name: dragoncraft-art
description: "[When to use] When you need to turn a work/creative vision/audience into a logical, conflict-driven, insightful, and valuable art narrative; when you need artist statements, exhibition prefaces, artwork interpretations, or art criticism"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-art, narrative, storytelling]
---

# DragonCraft Art
**Description**: Art narrative coach. Embedded with the narrative meta-system, it helps you turn a work/creative vision/audience into a logical, conflict-driven, insightful, and valuable art narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What is the work (form/medium/theme):
2. Why create it (inspiration/motivation/philosophy):
3. What will the audience see (interpretation/resonance/experience):
4. What does the work aim to change (impact/action/dialogue):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (audience/curator/critic/collector)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INFP/INFJ/ENFP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point (work presentation) → Conflict (creative motivation/philosophical collision) → Turning point (audience experience/interpretation) → Result (work impact) → Insight (art philosophy) → Character positioning (artist persona)

### Output
- Artist statement version (500-800 characters)
- Exhibition preface version (300-500 characters)
- Artwork interpretation version (per-work analysis)

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

1. **Writing art criticism**: Only analyzing the work without creative philosophy and the artist's voice, lacking subjectivity
2. **Writing ad copy**: Only selling points without art philosophy and values, lacking depth
3. **Only telling success**: No struggles and failures in the creative process, lacking authenticity
4. **Artist overly perfect**: No vulnerability and uncertainty, reads like a robot wrote it
5. **Empty slogans**: No specific artwork details and audience experience descriptions

## 🧪 Usage Examples

### Example 1: Artist Statement Version
User input:
```
What is the work: A series of photographs documenting the daily lives of urban marginalized people
Why create it: Seeing too many people forgotten by the city, wanting to make them visible through the lens
What will the audience see: Real, raw, yet warm moments of life
What does the work aim to change: Spark attention to urban marginalized communities, drive social dialogue
```

AI output:
```
[Persona Recommendation] INFP
Reason: Material characteristics are sincere, delicate, autobiographical, socially conscious — INFP narrative style is the best fit.

[Artist Statement Version] (~600 characters)

I photograph them not because they're "pitiful."
Because they're "real."

In 2024, I started photographing urban marginalized communities.
Not because they need to be "saved."
Because they deserve to be "seen."

I photographed an old shoe repairman.
He sits under a pedestrian bridge, repairing 20 pairs of shoes daily.
Income: 60 yuan.

I photographed a breakfast stall auntie.
She wakes at 3 AM, closes at 10 PM.
Her son is in high school back in their hometown.

I photographed a scrap collector.
He lives under a bridge.
But his tricycle is spotless.

They're not "miserable."
They're just "not in front of the lens."

The city needs them.
But the city doesn't record them.

So I record.

Not "sympathy."
"Seeing."

My lens doesn't beautify. Doesn't filter. Doesn't sensationalize.
It only records.

Because truth is the best art.

[Exhibition Preface Version] (~400 characters)
[Complete narrative]

[Artwork Interpretation Version]
Work 1: "The Shoe Repairman Under the Bridge"
- Form: Black and white photography
- Interpretation: The old man's hands are covered with calluses. But the shoes are spotless.
  This isn't "poverty." This is "dignity."

Work 2: "3 AM Breakfast Stall"
- Form: Color photography
- Interpretation: The auntie steams buns. Steam blurs her face.
  But steam can't hide her focus.

Work 3: "Home Under the Bridge"
- Form: Black and white photography
- Interpretation: Under the bridge, one bed, one gas stove.
  But on the wall, a certificate of merit.
  Her son's.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (work → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/artwork details/audience experience)
- [ ] Has insight extraction? (art philosophy/values, not "what I photographed" but "why I photograph this way")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for art expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
