---
name: dragoncraft-teach
description: "[When to use] When you need to turn course themes/student pain points/cognitive misconceptions into a logical, conflict-driven, insightful, and valuable education narrative; when you need course opening stories, training scripts, or course detail page copy"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.1.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-teach, narrative, storytelling]
---

# DragonCraft Teach
**Description**: Education narrative coach. Embedded with the narrative meta-system, it helps you turn course themes/student pain points/cognitive misconceptions into a logical, conflict-driven, insightful, and valuable education narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Course theme (core content/goal):
2. Target students (persona/background/pain points):
3. Cognitive misconceptions to correct (wrong beliefs/common traps):
4. Student dilemma cases (real/typical scenarios):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (ENFJ/ENTJ/INFJ)
- **Validation failure handling**: Missing field → **AI must actively ask for the missing field** until all 4 are provided; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Resonance scene → Protagonist tries and fails → Unexpected discovery → Benefits after transformation → Course promise

### Output
- Offline course opening script (5 minutes, with interaction design)
- Online course video opening copy (3 minutes, with screen prompts)
- Course detail page "What you'll learn" narrative version

## 🔗 Dependencies

This Skill relies on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring |
| De-AI Detection | narrative-meta | 7-rule detection |
| Ethics Review | narrative-meta | Three-principle check |
| Persona Mapping | narrative-meta | MBTI narrative persona recommendation |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Writing a course outline**: Only listing knowledge points, no story and conflict, lacking appeal
2. **Writing ad copy**: Only selling points, no student dilemmas and transformation, lacking authenticity
3. **Only telling success**: No failures and trial-and-error processes, reads like a robot wrote it
4. **Instructor overly perfect**: No vulnerability and uncertainty, students don't trust
5. **Empty slogans**: No specific scene anchors and interaction design

## 🧪 Usage Examples

### Example 1: Offline Course Opening Script
User input:
```
Course theme: Structured thinking and expression
Target students: Consulting advisors, product managers
Cognitive misconceptions to correct: Good logic equals good expression
Student dilemma case: Spent a week preparing materials, boss says "I can't understand what you're saying" during the presentation
```

AI output:
```
[Persona Recommendation] ENFJ
Reason: Material characteristics are inspiring narrative, collective action, education-oriented — ENFJ narrative style is the best fit.

[Offline Course Opening Script] (~5 minutes)

(Walks to the podium, silence for 3 seconds)

"Anyone here who's made a 50-slide PPT, and the boss says: 'Can you just get to the point?'"

(Audience raises hands)

"Last month, one of my students brought a full year of data, prepared 3 plans, spoke for 40 minutes.
The boss interrupted: 'So which one are you recommending?'
He said: 'I'm still论证.'
The boss: 'Then call me when you're done论证.'"

(Pause)

"He later debriefed with me: 'My logic was so tight, why did he think I was chaotic?'"

(Walks to whiteboard, draws two circles)

"Good logic is order in your world.
Good expression is order in others' worlds.
Today we're not talking about the Pyramid Principle — you've all read that book.
We're talking about how to put your logic into someone else's brain."

(Opens first PPT slide: "Make Your Boss Understand in One Shot")

"Former Google Product Manager Zhang Tao, one full day, deconstructing 15 real presentation cases. Let's begin."

[Online Course Video Opening Copy] (~3 minutes)
[Complete narrative]

[Course Detail Page "What You'll Learn" Narrative Version]
[Complete narrative]
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (resonance → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/student cases)
- [ ] Has insight extraction? (education philosophy/values, not "what we teach" but "why students need to learn")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for education expression? (matches target student persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
