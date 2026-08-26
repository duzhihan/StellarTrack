---
name: dragoncraft-heal
description: "[When to use] When you need to turn psychological struggles/healing processes/growth into logical, conflict-driven, insightful, and valuable psychological narratives; when you need healing stories, psychology education, mutual support guides, or counseling scripts"
author: ant (CEO 助理)
created: 2026-04-30
version: 1.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-heal, narrative, storytelling]
---

# DragonCraft Heal
**Description**: Psychological narrative coach. Embeds the narrative meta-system to help users turn psychological struggles/healing processes/growth into logical, conflict-driven, insightful, and valuable psychological narratives.

## 🎯 Features

### Input Fields (Four-Layer Material)
1. What psychological struggle did you encounter (symptoms/triggers/impact):
2. How did you face and heal from it (methods/process/turning points):
3. What growth and change occurred (cognition/behavior/relationships):
4. Who do you want to help (target audience/resonance points/action):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; missing any item requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires extracting the core
- **Format requirement**: User input is in natural language; AI automatically parses it into structured material
- **Audience persona** (optional): When provided, used to adjust narrative angle and language style (patient/family member/counselor/public)
- **Narrative persona** (optional): If not filled, automatically recommended based on material characteristics (INFP/INFJ/ENFJ)
- **Validation failure handling**: Missing field → prompt to supplement; insufficient length → follow up for details; format error → guide to correct format
- **⚠️ Mandatory compliance**: Psychological narratives must not replace professional medical advice; must include the disclaimer "For professional help, please consult a psychological counselor"

### Structure
Starting point (psychological struggle) → Conflict (symptoms/triggers/impact) → Turning point (healing method/turning point) → Result (growth/change) → Cognition (psychological philosophy) → Character positioning (healing persona)

### Output
- Healing story version (800-1200 characters)
- Psychology education version (500-800 characters)
- Mutual support guide version (action checklist)

## 🔗 Dependencies

This Skill depends on the following meta-Skill modules:

| Dependency Module | Source Skill | Purpose |
|---------|-----------|------|
| Eight-Blade Assessment | narrative-meta | Quality scoring (history/dialectics/phenomenology/language/form/existence/aesthetics/meta-reflection) |
| De-AI Detection | narrative-meta | 7-rule detection for template words, logical connectors, abstract emotions, etc. |
| Ethics Review | narrative-meta | Three-principle check (**psychological narratives must not replace professional medical advice**) |
| Persona Mapping | narrative-meta | Recommend MBTI narrative persona based on material characteristics |
| Memory Management | narrative-meta | Store/retrieve user's historical narratives to ensure cross-scenario consistency |

**Invocation method**: Orchestrate through narrative-workflow, or directly call the corresponding narrative-meta module.

## ⚠️ Common Mistakes

1. **Written as a medical report**: Only listing symptoms and diagnoses, without story and emotional connection, lacking warmth
2. **Written as a success story**: Only "I got through it," without the struggle and setbacks in the healing process, lacking authenticity
3. **Only telling about success**: Not acknowledging the complexity and long-term nature of psychological issues, sounding robotic
4. **Over-self-disclosure**: Not protecting privacy and boundaries, potentially causing secondary harm
5. **Empty slogans**: No specific healing methods or action guides

## 🧪 Usage Examples

### Example 1: Healing Story Version
User input:
```
What psychological struggle did you encounter: Anxiety disorder, insomnia, palpitations, affecting work and life
How did you face and heal from it: Psychological counseling + mindfulness meditation + exercise, gradually improved over 6 months
What growth and change occurred: Learned to accept uncertainty, stopped pursuing perfection, established boundaries
Who do you want to help: Fellow professionals struggling with anxiety, want them to know "you're not alone"
```

AI output:
```
[Persona Recommendation] INFP
Reason: Material characteristics are sincere,细腻, autobiographical, healing-oriented. INFP narrative style is most suitable.

[Healing Story Version] (approx. 1000 characters)

My first panic attack was on the subway.

October 2023, Shenzhen Metro Line 1.
Suddenly, heart racing. Breathing fast. Hands shaking.
I thought I was going to die.

Actually, no.
It was anxiety disorder.

During that period, I was "afraid" every day.
Afraid of doing my job poorly. Afraid of others' judgments. Afraid of an uncertain future.

Then my body told me: enough.

I went to see a psychologist.
She said: "You're not 'sick.' You're 'tired.'"

The healing process is not "getting better all at once."
It's "slowly learning to live with it."

Psychological counseling: once a week, for 6 months.
Mindfulness meditation: 10 minutes daily, still doing it now.
Exercise: 3 times a week, running/swimming/yoga.

After 6 months, I no longer have panic attacks.
But the anxiety is still there.

It's just that I no longer "fear the anxiety."
I know it's my body saying: "You need to rest."

I learned three things:
1. Accept uncertainty. Not "everything will be fine," but "even if it's not, I can handle it."
2. Stop pursuing perfection. Not "I must do my best," but "I've already done well enough."
3. Establish boundaries. Not "I must satisfy everyone," but "I must satisfy myself first."

I want to tell you who are also anxious:
You're not alone.
You're not "sick."
You're "tired."

Resting is not giving up.
It's "to set off better."

⚠️ For professional help, please consult a psychological counselor or psychiatrist.

[Psychology Education Version] (approx. 600 characters)
[Full narrative]

[Mutual Support Guide Version]
Action checklist:
1. Identify triggers: Record what situations trigger anxiety (work/relationships/finances)
2. Build a routine: 10 minutes of mindfulness meditation daily, exercise 3 times a week
3. Seek support: Psychological counselor/support groups/trusted friends
4. Accept uncertainty: Not "everything will be fine," but "even if it's not, I can handle it."
5. Establish boundaries: Learn to say "no," prioritize taking care of yourself

⚠️ This guide cannot replace professional medical advice. For help, please consult a psychological counselor or psychiatrist.
```

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Opening hook? (scene/action/dialogue opening)
- [ ] Logical progression? (struggle → conflict → turning point → result → cognition)
- [ ] Authenticity? (specific detail anchors: time/location/symptoms/healing methods)
- [ ] Cognitive extraction? (psychological philosophy/values, not "I'm better," but "what I learned")
- [ ] Value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for psychological expression? (matches target audience persona)

### Ethics & Compliance (driven by narrative-meta)
- [ ] **Ethics review passed? (psychological narratives must not replace professional medical advice; must include "For professional help, please consult a psychological counselor")**
- [ ] De-AI detection passed? (all 7 rules passed)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field length within 20-500 characters?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 1.0.0 | Last updated: 2026-04-30*
