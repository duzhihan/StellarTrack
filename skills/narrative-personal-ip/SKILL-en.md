---
name: dragoncraft-persona
description: "[When to use] When you need to turn personal experiences into a logical, conflict-driven, insightful, and valuable personal story; when you need to build a personal IP, create self-introductions, write public account articles, or short video scripts"
author: ant (CEO Assistant)
created: 2026-04-29
version: 1.1.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-persona, narrative, storytelling]
---

# DragonCraft Persona
**Description**: Personal IP narrative coach. Embedded with the narrative meta-system, it helps you turn scattered personal experiences into a logical, conflict-driven, insightful, and valuable personal story.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What have I done (experiences/achievements/failures):
2. What do I value (values/beliefs):
3. What have I encountered (key dilemmas/low points):
4. What have I learned (core insights/deliverable value):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INFP/INFJ/ENFP/ENFJ)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Starting point → Conflict → Turning point → Result → Insight → Character positioning

### Output
- Full version (800-1,500 characters)
- Short video version (300 characters)
- Personal bio version (within 150 characters)

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

1. **Writing a resume**: Only listing experiences, no conflict and insight
2. **Writing lyrical prose**: Only emotions, no logical progression
3. **Only telling what happened**: Not clarifying "why I thought this way at the time"
4. **Persona overly perfect**: Lacking vulnerability and authenticity
5. **Empty slogans**: No specific details and scene anchors

## 🧪 Usage Examples

### Example 1: Complete Personal IP Story
User input:
```
What have I done: Quit my job at a big tech company, took a gap year, transitioned to career planner
What do I value: Freedom is more important than stability, review is more valuable than success
What have I encountered: No income for half a year after quitting, startup failed, clients ran away
What have I learned: Failure doesn't give you bonus points, reviewing does; freedom isn't not working, it's deciding what to work on
Audience persona: 25-35 year old professionals, considering transition but afraid of risk
Narrative persona: INFP (optional, auto-recommended if not filled)
```

AI output:
```
[Persona Recommendation] INFP
Reason: Material characteristics are personal growth, vulnerable experiences, sincere reflection — INFP narrative style is the best fit.

[Memory Retrieval]
No related historical records found. Suggestion: This is a good starting point for a series story, consider forming a "Life Turning Points Trilogy."

[Full Version] (~1,200 characters)

The day I quit, I posted on WeChat Moments: "No more KPIs." Got 192 likes.

That was May 2023. I'd been a product manager at a big tech company in Shenzhen for three years. Arrived at 9 AM every morning, left at 10 PM, on call weekends. I thought this was "stability."

Until one day, working overtime until midnight, the security guard asked me: "Young lady, you're always this late, do you live here?"

I stood in the elevator, suddenly cried. Not from grievance, but from fear — I was afraid that 30 years from now I'd still be living like this.

In the first month after quitting, I worked from home, slept until I naturally woke up, went to cafes in the afternoon to write proposals. I thought this was freedom.

In the third month, my partner said there was no money to pay salaries. I realized I had never done the math. I thought starting a business was "have a good idea, then someone gives you money."

In the fifth month, we took on a small 100,000-yuan project. The client revised it 11 times, then didn't pay the balance. I squatted on the balcony of my rental apartment, smoking, thinking it would be better to go back to writing weekly reports.

That was the first time I realized: Quitting isn't courage. Starting a business isn't adventure. True courage is daring to admit "I don't even know how to do accounting."

Later, I printed out those 11 revision records and pasted them all over one wall. Every time I looked at them, I reminded myself: Failure doesn't give you bonus points. Reviewing does.

Now I'm a career planner, helping over 30 people find direction. I don't teach them "how to succeed." I teach them "how to face failure."

Because I know, true freedom isn't leaving somewhere. It's deciding where to go.

[Short Video Version] (~300 characters)

"Have you ever calculated how much money you can make in a month?"

That was the question my partner asked me in the third month after quitting.

I used to be a product manager at a big tech company, earning 300,000 a year. I thought I understood money.

Until I started my own business, took on a 100,000-yuan project, the client revised it 11 times, then didn't pay.

Squatting on the balcony, smoking, I suddenly understood one thing:

Quitting isn't courage. Admitting you can't do accounting is.

Now I'm a career planner. Don't teach people to succeed. Teach them to face failure.

Because true freedom isn't leaving somewhere. It's deciding where to go.

[Personal Bio Version] (~150 characters)

Former big tech product manager, quit in 2023, startup failed, now a career planner. Helped 30+ people find direction. Core philosophy: Failure doesn't give you bonus points, reviewing does; freedom isn't not working, it's deciding what to work on.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (scene/action/dialogue opening)
- [ ] Has logical progression? (starting point → conflict → turning point → result → insight)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/dialogue)
- [ ] Has insight extraction? (not "what I learned" but "how I changed because of it")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for personal IP expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.1.0 | Last updated: 2026-04-30*
