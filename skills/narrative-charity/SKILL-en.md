---
name: dragoncraft-love
description: "[When to use] When you need to turn beneficiary groups/change stories/calls to action into a logical, conflict-driven, insightful, and valuable charity narrative; when you need charity stories, fundraising copy, volunteer recruitment, or charity reports"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-love, narrative, storytelling]
---

# DragonCraft Love
**Description**: Charity narrative coach. Embedded with the narrative meta-system, it helps you turn beneficiary groups/change stories/calls to action into a logical, conflict-driven, insightful, and valuable charity narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Who has what problem (beneficiary group/dilemma/current state):
2. What have we done (action/solution/investment):
3. What has changed (results/data/testimonials):
4. What else is needed (call to action/gap/participation method):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (donors/volunteers/media/government)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (ENFJ/INFJ/INFP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point (beneficiary dilemma) → Conflict (problem severity/insufficiency of existing solutions) → Turning point (charity action enters) → Result (change/data/testimonials) → Insight (charity philosophy) → Character positioning (call to action)

### Output
- Charity story version (800-1,200 characters)
- Fundraising copy version (300-500 characters)
- Volunteer recruitment version (150-300 characters)

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

1. **Writing a tragedy**: Only渲染 suffering, without action and change, lacking hope
2. **Writing a press release**: Only achievements, without the real voice of beneficiaries, reads like a robot wrote it
3. **Only telling success**: Not acknowledging the complexity and limitations of charity, lacking authenticity
4. **Organization overly perfect**: Not acknowledging funding gaps and execution difficulties, donors don't trust
5. **Empty slogans**: No specific beneficiary testimonials and data anchors

## 🧪 Usage Examples

### Example 1: Charity Story Version
User input:
```
Who has what problem: Mountain area children have no extracurricular books, reading volume is only 1/10 of urban children
What have we done: Established the "Book Bridge" project, donated 10,000 books, trained 50 rural teachers
What has changed: 500 children developed reading habits, essay skills improved by 30%
What else is needed: Still need 5,000 more books, recruit 100 volunteers, donation channel is open
```

AI output:
```
[Persona Recommendation] ENFJ
Reason: Material characteristics are inspiring narrative, collective action, hope transmission — ENFJ narrative style is the best fit.

[Charity Story Version] (~1,000 characters)

In Li Xiaomei's essays, only one animal has ever appeared: a chicken.

She's a fourth-grade student in a mountain area in Yunnan.
Her reading volume is one-tenth that of urban children.

Not because she doesn't want to read. Because there are no books to read.

In March 2024, we went to her school.
The library had 200 books. Most donated ten years ago, covers already moldy.

"Teacher, I want to read Harry Potter," Li Xiaomei said.
The teacher smiled: "What's that?"

In that moment, I knew we had to do something.

So the "Book Bridge" project was born.

In the first year, we donated 10,000 books.
Trained 50 rural teachers, teaching them how to guide children to read.

Today, in Li Xiaomei's essays, dinosaurs, astronauts, and flying fish appear.
Her essay skills improved by 30%.

500 children developed reading habits.

But it's not enough.

We still need 5,000 books.
We still need 100 volunteers.
We still need you.

One book, 20 yuan.
One volunteer, one hour.

You can donate. You can participate. You can change a child's world.

Because one book might be the first window a child sees through.

[Fundraising Copy Version] (~400 characters)
[Complete narrative]

[Volunteer Recruitment Version] (~200 characters)
[Complete narrative]
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (dilemma → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/beneficiary testimonials)
- [ ] Has insight extraction? (charity philosophy/values, not "what we did" but "why we must do it")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for charity expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
