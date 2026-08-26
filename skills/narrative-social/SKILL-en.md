---
name: dragoncraft-voice
description: "[When to use] When you need to turn platform features/audience personas/trending topics/persona positioning into logical, conflict-driven, insightful, and valuable social media narratives; when you need viral copy, hashtags, interactive design, or content planning"
author: ant (CEO 助理)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-voice, narrative, storytelling]
---

# DragonCraft Voice
**Description**: Social media narrative coach. Embeds the narrative meta-system to help users turn platform features/audience personas/trending topics/persona positioning into logical, conflict-driven, insightful, and valuable social media narratives.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Which platform to post on (platform/algorithms/content format):
2. Who to post for (audience persona/pain points/interests):
3. What trends to follow (trends/topics/timing):
4. Who am I (persona/values/differentiation):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; missing any item requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires extracting the core
- **Format requirement**: User input is in natural language; AI automatically parses it into structured material
- **Audience persona** (optional): When provided, used to adjust narrative angle and language style
- **Narrative persona** (optional): If not filled, automatically recommended based on material characteristics (ENFP/ENTP/ESFP)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; format error → guide to correct format

### Structure
Starting point (trends/topics) → Conflict (audience pain points/insufficient existing content) → Turning point (persona entry/unique perspective) → Result (engagement/virality/conversion) → Cognition (content philosophy) → Character positioning (social media persona)

### Output
- Viral copy version (300-500 characters)
- Hashtag version (10-20 hashtags + usage guide)
- Interactive design version (comment/share/DM strategy)

## 🔗 Dependencies

This Skill depends on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring (history/dialectics/phenomenology/language/form/existence/aesthetics/meta-reflection) |
| De-AI Detection | narrative-meta | 7-rule detection for template words, logical connectors, abstract emotions, etc. |
| Ethics Review | narrative-meta | Three-principle check (factual distortion/inappropriate omission/privacy leakage) |
| Persona Mapping | narrative-meta | Recommend MBTI narrative persona based on material characteristics |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Written as marketing copy**: Only selling points, no persona or values, lacking trust
2. **Written as trend-chasing**: Only following the crowd, no unique perspective or insight, lacking differentiation
3. **Only telling about success**: No failure lessons or iteration process, sounding robotic
4. **Overly perfect persona**: No vulnerability or authenticity, followers don't trust
5. **Empty slogans**: No specific scene anchors or interactive design

## 🧪 Usage Examples

### Example 1: Viral Copy Version
User input:
```
Which platform to post on: Xiaohongshu (RED), image+text + short video
Who to post for: 25-35 year old working women, anxious about finances but不懂 investment
What trends to follow: "Making money" topic, women's financial awareness awakening
Who am I: 10 years in fund industry, don't teach stock picking only provide tools, rational but warm
```

AI output:
```
[Persona Recommendation] ENFP
Reason: Material characteristics are improvisational narrative, lively and跳跃, social media-oriented. ENFP narrative style is most suitable.

[Viral Copy Version] (approx. 400 characters)

Girls who are making money are secretly learning this.

Not stock picking. Not mutual funds.
It's "tools."

I've been in the fund industry for 10 years. I've seen too many girls:
- Following big influencers, lost money and不敢 to say
- Financial advisor recommendations, bought what didn't suit them
- Researching on their own, couldn't understand financial statements

Then they discovered one thing:
The problem isn't "what to buy."
It's "how to think."

So I created 「Optimal Life」.
Don't teach stock picking. Only provide tools.

Tools matter more than opinions.
Opinions become outdated. Tools don't.

Today I'm sharing a tool I've used for 10 years:
"Investment Framework Self-Check Sheet."

3 questions to help you judge:
1. What are you buying? (product)
2. Why are you buying it? (logic)
3. When are you selling? (exit)

If you can't answer these.
You're not investing.
You're gambling.

Reply "tool" in the comments, I'll send you the template.

[Hashtag Version]
#MakingMoneyGirls #WomenFinance #InvestmentTools #FinanceFramework #NoStockPickingOnlyTools
#10YearsInFunds #InvestmentSelfCheck #MakingMoneyDaily #FinanceTips #WomenGrowth
#InvestmentThinking #FinanceBeginner #MakingMoneyManual #InvestmentFramework #FinanceTools

[Interactive Design Version]
- Comments: Reply "tool" to get template (auto-reply + manual follow-up)
- Shares: Share to bestie groups, get the complete "Investment Framework Self-Check Sheet"
- DMs: Book a free 15-minute investment diagnosis
- Live stream: Every Wednesday 8 PM, "Making Money Girls' Investment Class"
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Opening hook? (scene/action/dialogue opening)
- [ ] Logical progression? (trends → conflict → turning point → result → cognition)
- [ ] Authenticity? (specific detail anchors: time/location/numbers/user testimonials)
- [ ] Cognitive extraction? (content philosophy/persona values, not "what I posted," but "why I posted it this way")
- [ ] Value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for social media expression? (matches platform algorithms and audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no factual distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field length within 20-500 characters?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
