---
name: dragoncraft-life
description: "[When to use] When you need to turn lifestyle/values/aesthetics into a logical, conflict-driven, insightful, and valuable life narrative; when you need lifestyle manifestos, content planning, visual guides, or brand collaboration copy"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-life, narrative, storytelling]
---

# DragonCraft Life
**Description**: Lifestyle narrative coach. Embedded with the narrative meta-system, it helps you turn lifestyle/values/aesthetics into a logical, conflict-driven, insightful, and valuable life narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What kind of life do I live (daily routine/habits/rituals):
2. What do I believe in (values/principles/bottom lines):
3. What aesthetics do I pursue (visual/style/tone):
4. Who do I want to influence (audience/resonance points/action):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INFP/INFJ/ENFP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point (daily life) → Conflict (value collision/aesthetic choices) → Turning point (epiphany/change) → Result (lifestyle established) → Insight (life philosophy) → Character positioning (lifestyle persona)

### Output
- Lifestyle manifesto version (500-800 characters)
- Content planning version (300-500 characters)
- Visual guide version (colors/fonts/style/tone)

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

1. **Writing a diary**: Only listing daily routines, no values and aesthetics, lacking depth
2. **Writing ad copy**: Only selling points, no life philosophy and values, lacking trust
3. **Only telling success**: No struggles and choices, reads like a robot wrote it
4. **Lifestyle overly perfect**: No vulnerability and authenticity, fans don't trust
5. **Empty slogans**: No specific scene anchors and aesthetic details

## 🧪 Usage Examples

### Example 1: Lifestyle Manifesto Version
User input:
```
What kind of life do I live: Wake up at 6 AM daily, exercise 1 hour, work in library 3 hours, execute in afternoon, accompany child in evening
What do I believe in: Tools are more important than opinions, action is more important than knowledge, walking together is more important than walking alone
What aesthetics do I pursue: Minimalism, white space, short sentences, dialogue format
Who do I want to influence: 25-35 year old professionals, anxious but wanting to change
```

AI output:
```
[Persona Recommendation] INFP
Reason: Material characteristics are sincere, delicate, autobiographical, values-driven — INFP narrative style is the best fit.

[Lifestyle Manifesto Version] (~600 characters)

My daily routine has only four things.

Wake up at 6. Exercise 1 hour.
Not because I'm disciplined.
Because I know the body is the only "permanent asset."

9 AM at the library. Work 3 hours.
No phone scrolling. No message replies.
Only one thing: turn complex problems into tools.

Execute in the afternoon.
Tools made but not used equal nothing.
Action is more important than knowledge.

Evening with the kid.
No work. No reading.
Just playing with him.

Many people ask me: Aren't you tired?
Yes.
But tired and anxious are two different things.

Anxiety comes from not knowing what you want.
Tiredness comes from doing what you believe in.

I believe in three things:
Tools are more important than opinions.
Action is more important than knowledge.
Walking together is more important than walking alone.

If you also believe.
Welcome to walk with us.

[Content Planning Version] (~400 characters)
[Complete narrative]

[Visual Guide Version]
- Colors: Black, white, gray as primary, with warm accents (#F5F5F0 / #333333 / #E8B87A)
- Fonts: Source Han Serif (headings) + Source Han Sans (body)
- Style: Minimalism, white space, short sentences, dialogue format
- Tone: Rational but warm, not sentimental, not preachy
- Images: Natural light, real scenes, no filters
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (daily life → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/aesthetic details)
- [ ] Has insight extraction? (life philosophy/values, not "what I did" but "why I live this way")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for lifestyle expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
