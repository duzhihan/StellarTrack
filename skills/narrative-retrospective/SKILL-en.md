---
name: dragoncraft-review
description: "[When to use] When you need to turn project experiences/failure lessons/success stories into logical, conflict-driven, insightful, and valuable retrospective narratives; when you need retrospective meeting scripts, written retrospective stories, or counterfactual checklists"
author: ant (CEO 助理)
created: 2026-04-30
version: 1.1.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-review, narrative, storytelling]
---

# DragonCraft Review
**Description**: Retrospective narrative coach. Embeds the narrative meta-system to help users turn project experiences/failure lessons/success stories into logical, conflict-driven, insightful, and valuable retrospective narratives.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Project name/event (background/goals):
2. Actual results (gap from goals):
3. Key turning point (a specific moment/decision):
4. Decision rationale and emotions at the time:

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; missing any item requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires extracting the core
- **Format requirement**: User input is in natural language; AI automatically parses it into structured material
- **Audience persona** (optional): When provided, used to adjust narrative angle and language style (team/leadership/external)
- **Narrative persona** (optional): If not filled, automatically recommended based on material characteristics (INTJ/ISTJ/ENTJ)
- **Validation failure handling**: Missing field → **AI must proactively ask for the missing field** until all 4 fields are provided; insufficient length → follow up for details; format error → guide to correct format

### Structure
Expected story → Reality check → Key turning point → Post-event reflection → New rule extraction

### Output
- Retrospective meeting script (10 minutes)
- Written retrospective story (suitable for internal sharing)
- Extracted "if only... then..." counterfactual checklist

## 🔗 Dependencies

This Skill depends on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring |
| De-AI Detection | narrative-meta | 7-rule detection |
| Ethics Review | narrative-meta | Three-principle check |
| Persona Mapping | narrative-meta | MBTI narrative persona recommendation |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Written as a data report**: Only listing data and metrics, without story and reflection, lacking warmth
2. **Written as blame-shifting**: Only external causes, no self-reflection, lacking accountability
3. **Only telling about success**: No failure and trial-and-error process, sounding robotic
4. **Overly perfect team**: Not acknowledging decision mistakes and emotional fluctuations, lacking authenticity
5. **Empty slogans**: No specific scene anchors or counterfactual checklist

## 🧪 Usage Examples

### Example 1: Retrospective Meeting Script
User input:
```
Project name/event: 2024 Double 11 promotional campaign
Actual results: GMV 3.2 million (target 5 million)
Key turning point: November 10, 8 PM, server crashed for 2 hours
Decision rationale and emotions at the time: Tech lead insisted on scaling up, boss thought it was too expensive and didn't approve. After the crash, the whole team was devastated.
```

AI output:
```
[Persona Recommendation] INTJ
Reason: Material characteristics are logically rigorous, data-driven, reflective. INTJ narrative style is most suitable.

[Retrospective Meeting Script] (approx. 10 minutes)

"A week before Double 11, our tech director Lao Li came to me: 'Traffic estimate is 3 million, servers can only handle 2 million, we must scale up.'

I did the math at the time: scaling up would cost 150,000. If we didn't scale up, worst case it'd be a bit slow, losing just a few orders.

November 10, 8 PM. Traffic came in, servers went 502 directly.
Down for a full 2 hours.
Customer service messages 99+.
Users calling us 'fake promotion.'

Lao Li said nothing in front of the screen.
I looked at the back of his head, thinking that 150,000 would've been so cheap.

Later we calculated: those 2 hours cost us 800,000 in GMV.
And a dozen returning customers never came back.

150,000 vs 800,000.
I still remember that math today.

So the first thing from our retrospective today:
From now on, tech has veto power on all capacity decisions.

Second thing:
Monthly stress tests, results copied directly to me.

Lao Li, next month's stress test report, you make me the first to see it."

[Written Retrospective Story] (approx. 800 characters)
[Full narrative]

[Counterfactual Checklist]
- If we had scaled up → 0 loss, GMV could've reached 4.5 million
- If we hadn't scaled but added page caching in advance → loss could've been reduced to 300,000
- If we had elastic cloud resources ready → loss of 100,000
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Opening hook? (scene/action/dialogue opening)
- [ ] Logical progression? (expectation → conflict → turning point → reflection → rules)
- [ ] Authenticity? (specific detail anchors: time/location/numbers/emotions)
- [ ] Cognitive extraction? (retrospective philosophy/new rules, not "we were wrong," but "what we learned")
- [ ] Value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for retrospective expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no factual distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field length within 20-500 characters?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
