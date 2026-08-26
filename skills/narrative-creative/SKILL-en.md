---
name: dragoncraft-dream
description: "[When to use] When you need to turn creative concepts/target users/differentiation into a logical, conflict-driven, insightful, and valuable creative product narrative; when you need creative briefs, user stories, visual scripts, or creative proposals"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-dream, narrative, storytelling]
---

# DragonCraft Dream
**Description**: Creative product narrative coach. Embedded with the narrative meta-system, it helps you turn creative concepts/target users/differentiation into a logical, conflict-driven, insightful, and valuable creative product narrative.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What is the creative idea (concept/inspiration/form):
2. Who is it for (target user/pain points/scenario):
3. Why is it different (differentiation/innovation/barriers):
4. How will users experience it (experience/change/value):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style (users/investors/partners/media)
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (ENFP/ENTP/INFP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point (creative concept) → Conflict (user needs/market gap) → Turning point (differentiation enters) → Result (user experience/change) → Insight (creative philosophy) → Character positioning (creative persona)

### Output
- Creative brief version (500-800 characters)
- User story version (300-500 characters)
- Visual script version (storyboard/copy/music)

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

1. **Writing a product manual**: Only listing features and specs, no creative inspiration or user stories
2. **Writing ad copy**: Only selling points without creative philosophy and values, lacking trust
3. **Only telling success**: No failures and iterations in the creative process, lacking authenticity
4. **Creative idea overly perfect**: Not acknowledging limitations and applicable boundaries, reads like a robot wrote it
5. **Empty slogans**: No specific scene anchors and user experience descriptions

## 🧪 Usage Examples

### Example 1: Creative Brief Version
User input:
```
What is the creative idea: An "investment framework self-check" tool, 3 questions to help you determine if you're investing or gambling
Who is it for: 25-35 year old professional women, anxious about finances but don't understand investing
Why is it different: Doesn't teach stock trading, only provides tools; not opinions but frameworks
How will users experience it: Build their own investment framework, no longer blindly follow trends, no longer anxious
```

AI output:
```
[Persona Recommendation] ENFP
Reason: Material characteristics are improvisational narrative, lively and跳跃, creativity-oriented — ENFP narrative style is the best fit.

[Creative Brief Version] (~600 characters)

This tool has only 3 questions.

But I thought about it for a year.

In 2023, I left the fund company.
Not because I was tired.
Because I was afraid —
I was afraid that those financial advisors sitting in offices,
using the question "how much will it go up next month,"
were misleading those who trusted them.

I tried starting my own business. Failed.
During that time I realized something:
The problem isn't "who's right or wrong."
It's "tools versus opinions" — opinions become outdated, tools don't.

So the "Investment Framework Self-Check" was born.

Only 3 questions:
1. What are you buying? (Product)
2. Why are you buying it? (Logic)
3. When are you selling? (Exit)

If you can't answer.
You're not investing.
You're gambling.

Not because you "don't understand."
Because no one taught you "how to think."

This tool doesn't teach you to trade stocks.
It helps you build thinking frameworks.

Tools are more important than opinions.
Opinions become outdated. Tools don't.

[User Story Version] (~400 characters)
[Complete narrative]

[Visual Script Version]
Storyboard 1: A girl looking at her phone, anxious expression
Copy: "What are you buying?"
Music: Tense rhythm

Storyboard 2: Girl scrolls through financial advisor's chat records
Copy: "Why are you buying it?"
Music: Rhythm accelerates

Storyboard 3: Girl looking out the window, thinking
Copy: "When are you selling?"
Music: Rhythm slows

Storyboard 4: Girl opens the "Investment Framework Self-Check"
Copy: "You're not investing. You're gambling."
Music: Turning point

Storyboard 5: Girl smiles, confident
Copy: "Tools are more important than opinions."
Music: Warm ending
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (creative idea → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/user experience)
- [ ] Has insight extraction? (creative philosophy/values, not "what we did" but "why we think this way")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for creative expression? (matches target user persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
