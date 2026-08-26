---
name: dragoncraft-brand
description: "[When to use] When you need to build a continuous, consistent, evolving personal narrative universe; when you need new stories, historical reference annotations, narrative universe maps, or next-topic suggestions"
author: ant (CEO Assistant)
created: 2026-04-30
version: 1.1.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-brand, narrative, storytelling]
---

# DragonCraft Brand
**Description**: Personal brand continuous narrative coach. Embedded with the narrative meta-system, it doesn't just generate stories one-time, but helps you build a continuous, consistent, evolving personal narrative universe.

## 🎯 Features

### Core Mechanism
- Before each creation, the meta-system automatically retrieves the user's historical narrative memory bank
- Output will be annotated: "You previously told [topic] on [time], suggest extending from [new angle] this time" or "Avoid repeating [event], consider using [adjacent details] instead"
- Supports serialized narrative planning (e.g., "My Three Failures," "Five Teachers I've Known")

### Input Fields (Three-Layer Material)
1. Theme/event to tell this time:
2. New insight or values to convey:
3. Whether to continue previous work (yes/no, if yes, select the historical narrative ID to reference):

### Input Validation Rules
- **Required fields**: All 3 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INFP/INFJ/ENFP)
- **Validation failure handling**: Missing field → **AI must actively ask for the missing field** until all 3 are provided; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Historical memory retrieval → New story generation → Historical reference annotation → Narrative universe map → Next-topic suggestion

### Output
- New story (following personal IP structure)
- Historical reference annotations (which sentences echo old stories)
- Narrative universe map (visualized user's established story nodes and connections)
- Next-topic suggestion (recommended based on current narrative gaps)

## 🔗 Dependencies

This Skill relies on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring |
| De-AI Detection | narrative-meta | 7-rule detection |
| Ethics Review | narrative-meta | Three-principle check |
| Persona Mapping | narrative-meta | MBTI narrative persona recommendation |
| Memory Management | narrative-meta | **Core dependency**: Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Writing isolated stories**: No historical narrative references, lacking continuity
2. **Writing repetitive narratives**: Repeating the same events without new angles
3. **Only telling success**: No failures and trial-and-error processes, reads like a robot wrote it
4. **Character overly perfect**: No vulnerability and uncertainty, fans don't trust
5. **Empty slogans**: No specific scene anchors and insight extraction

## 🧪 Usage Examples

### Example 1: New Story + Historical Reference Annotations
User input:
```
Theme/event to tell this time: After quitting my job at a big tech company, my first startup failed
New insight/values to convey: Failure is not wealth; what comes after failure — the review — is
Whether to continue previous work: Yes, reference the previous "quitting big tech" story (historical ID: story_001)
```

AI output:
```
[Persona Recommendation] INFP
Reason: Material characteristics are sincere, delicate, autobiographical, reflection-oriented — INFP narrative style is the best fit.

[Historical Memory Retrieval Summary]
You previously told "Why I Quit My Job at Tencent" on 2024-11-20, with the main emotion being "relief and freedom."
This time, suggest forming the second part of a "trilogy": from freedom to disillusionment.
Avoid repeating the excitement of quitting, jump directly to "the first month of starting up" details.

[New Story Excerpt]
(Continuing from story_001)

The day I quit, I posted on WeChat Moments: "No more KPIs." Got 192 likes.

In the first month of starting up, I worked from home, slept until I naturally woke up, went to cafes in the afternoon to write proposals.
I thought this was freedom.

In the third month, my partner said there was no money to pay salaries.
I realized I had never done the math.
I thought starting a business was "have a good idea, then someone gives you money."

In the fifth month, we took on a small 100,000-yuan project. The client revised it 11 times, then didn't pay the balance.
I squatted on the balcony of my rental apartment, smoking, thinking it would be better to go back to writing weekly reports.

That was the first time I realized: Quitting isn't courage. Starting a business isn't adventure.
True courage is daring to admit "I don't even know how to do accounting."

Later, I printed out those 11 revision records and pasted them all over one wall.
Every time I looked at them, I reminded myself: Failure doesn't give you bonus points. Reviewing does.

If you also want to start a business, don't quit yet.
Answer me one question first: Where is your first client?

[Historical Reference Annotations]
- "The day I quit, I posted on WeChat Moments" → echoes story_001's quitting decision
- "I thought this was freedom" → contrasts with story_001's "relief and freedom" emotion
- Suggested next topic: How to climb out of disillusionment (continuing the trilogy finale)

[Narrative Universe Map]
story_001: Quitting → Emotion: Relief
story_002: Startup failure → Emotion: Disillusionment, Insight: Value of review
Suggested next topic: How to climb out of disillusionment (continuing the trilogy finale)
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (history → new story → reference annotations → universe map → next topic suggestion)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/emotions)
- [ ] Has insight extraction? (personal philosophy/values, not "what I did" but "what I learned")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for personal brand expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 3 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
