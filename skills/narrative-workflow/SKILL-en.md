---
name: dragoncraft-studio
description: "[When to use] When you need to automate the full narrative generation pipeline; when you need to coordinate the workflow between meta-Skills, scenario Skills, interactive design Skills, and persona distillation Skills"
author: ant (CEO 助理)
created: 2026-04-29
version: 1.4.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-studio, narrative, storytelling]
---

# DragonCraft Studio
**Description**: Narrative automation workflow engine. Coordinates the pipeline between meta-Skills, scenario Skills, interactive design Skills, and persona distillation Skills.

## 🎯 Workflow Modes

### Mode A: Quick Output (default)
- Execute: Phase 0 → Phase 1 → Phase 4
- Skip: Phase 2, Phase 3
- Output: First draft + memory summary + brief optimization suggestions

### Mode B: Deep Polish
- Execute: Phase 0 → Phase 1 → Phase 2 → Phase 4
- Iterate until all Eight-Blade scores ≥ 7, de-AI detection passes
- Output: Final draft + iteration report + memory write

### Mode C: Interactive Design
- Execute: Phase 0 → Phase 1 → Phase 2 → Phase 3 → Phase 4
- Output: Complete narrative final draft + interactive design plan + fragment map + schedule + memory write

### Mode D: Interactive Design Only (existing narrative text)
- User provides narrative text directly, skip Phase 1
- Execute: Phase 0 → Phase 2 (quick assessment) → Phase 3 → Phase 4
- Output: Interactive design plan + memory write

## 🔗 Dependencies

This Skill orchestrates the following Skill modules:

| Dependency Skill | Module | Purpose | Invocation Phase |
|-----------|------|------|---------|
| narrative-meta | Eight-Blade Assessment | Narrative quality scoring (history/dialectics/phenomenology/language/form/existence/aesthetics/meta-reflection) | Phase 2 |
| narrative-meta | De-AI Detection | 7-rule detection for template words/logical connectors/abstract emotions, etc. | Phase 2 |
| narrative-meta | Ethics Review | Three-principle check (factual distortion/inappropriate omission/privacy leakage) | Phase 2 |
| narrative-meta | Persona Mapping | Recommend MBTI narrative persona based on material characteristics | Phase 0/Phase 1 |
| narrative-meta | Consistency Check | Cross-scenario comparison, output difference report | Phase 2 |
| narrative-meta | Memory Management | Store/retrieve user's historical narratives | Phase 0/Phase 4 |
| narrative-personal-ip | Scenario Generation | Personal IP narrative first draft generation | Phase 1 (personal IP scenario) |
| Interactive Design Skill | Interactive Design | Fragment map/schedule/reward mechanism | Phase 3 |
| **nuwa-skill** | **Persona Distillation** | **Extract persona expression DNA + mental model** | **Phase 0 (optional)** |

**Invocation path**: `narrative-workflow → narrative-meta (assessment/detection/review/memory) → narrative-personal-ip (generation)`
**Persona distillation path**: `narrative-workflow → nuwa-skill (persona distillation) → expression DNA injection into Phase 1`

## 📋 Input Validation Rules

- **Scene (scene)**: Required, enum values: personal IP/brand/product/funding/sales/organizational change/charity/legal/medical/social media/creative product/lifestyle/tech/controversial topic/art/psychology/sustainability
- **Mode (mode)**: Required, enum values: A/B/C/D, default A
- **Persona (persona)**: Optional, enum values: ENFJ/ENFP/INFJ/INFP/auto-recommend if not filled
- **Speaker (speaker)**: Optional, enum values: Luo Zhenyu/Yu Minhong/Lei Jun/Zhang Yiming/Li Jiaqi/Nadella/Han Hong/Luo Xiang/Tao Yong/papi Jiang/Philippe Starck/Li Ziqi/Musk/debate mode/Cai Guo-Qiang/Jordan Peterson/Yvon Chouinard/Zhang Xuefeng/Buffett/Wang Xing/custom/skip if not filled
  * If filled, system calls nuwa-skill to distill the corresponding persona, extracting expression DNA
  * If not filled, skip persona distillation, use default MBTI persona
  * View full list: `/persona list`
- **Material (material)**: Required, JSON object, must contain at least 2 fields
- **Validation failure handling**: Invalid scene/mode → prompt available values; empty material → refuse execution and guide
- **Length limit**: Each material field 20-500 characters, auto-truncate and warn if out of range

## 📋 Detailed Phase Instructions

### Phase 0: Memory Retrieval + Persona Distillation (optional)

#### Sub-step 0.1: Memory Retrieval (call meta-Skill memory module)
**Input**: User ID, current scene, material keywords
**Processing**:
- Retrieve story IDs for same-theme stories in user's historical narratives
- Retrieve user's preferred narrative persona, commonly used golden phrases
- Retrieve records of cross-scenario factual inconsistencies
**Output format**:
```json
{
  "similar_stories": [{"story_id": "xxx", "title": "xxx", "avoid_repeat": true/false, "suggested_reference": "quotable fragment"}],
  "preferred_persona": "ENFP",
  "inconsistencies": [],
  "pending_suggestions": ["Suggest completing the trilogy finale"]
}
```

#### Sub-step 0.2: Persona Distillation (optional, new)
**Trigger condition**: User specifies `speaker` parameter
**Input**: Speaker name (e.g., "Jobs", "Lei Jun")
**Processing**:
- Call nuwa-skill to distill the corresponding persona
- Extract five layers of information:
  1. **Expression DNA**: Tone, rhythm, word preferences, typical sentence patterns
  2. **Mental model**: Cognitive framework, thinking style
  3. **Decision heuristics**: Judgment criteria, priorities
  4. **Anti-patterns/values底线**: What not to do, what to refuse
  5. **Honest boundaries**: What can't be done, where limitations lie
- If speaker not specified, skip this step, output is empty
**Output format**:
```json
{
  "persona_name": "Steve Jobs",
  "source": "nuwa-skill",
  "expression_dna": {
    "typical_phrases": ["One more thing", "Simplicity is the ultimate sophistication"],
    "sentence_style": "Short sentences, likes to start with rhetorical questions",
    "analogy_type": "Analogies to everyday life,比喻 tech terms to daily things",
    "emotional_tone": "Calm but full of conviction, no nonsense",
    "forbidden_patterns": ["Wouldn't say 'empower''closed-loop''grip' and other internet jargon"]
  },
  "cognitive_framework": "Simplicity is the ultimate sophistication, end-to-end control, focus means saying no",
  "decision_heuristics": ["If something isn't good enough, redo it", "The best feature is no feature"],
  "anti_patterns": ["Don't innovate for innovation's sake", "Don't compromise taste for market share"],
  "honest_boundaries": [
    "Distilling public expression, not simulating private thoughts",
    "Cannot capture persona's personality shifts over time",
    "If persona said contradictory things, prioritize the most widely known version"
  ],
  "confidence": 0.85
}
```

### Phase 1: Scenario Skill Generation + Persona Style Injection
Call the corresponding scenario Skill based on user's selected scene. This Skill embeds the meta-Skill's structural generation capability.

**Persona style injection** (if Phase 0.2 has output):
```markdown
# Style Instructions (based on persona distillation)

You are writing in the narrative voice of 【{persona_name}】. Please follow these characteristics:

- {typical_phrases}
- {sentence_style}
- {analogy_type}
- {emotional_tone}
- Avoid using: {forbidden_patterns}
- Cognitive framework: {cognitive_framework}

If generated sentences don't match the above characteristics, self-correct.
```

**Output**: First draft (conforms to the scene's structural template + persona expression DNA)

### Phase 2: Meta-Skill Polish + Persona Consistency Detection
**Sub-steps**:
- 2.1 Eight-Blade Assessment: Score first draft (1-10), dimensions below 7 trigger revisions
- 2.2 De-AI Detection: Apply 7 rules, flag problem locations, auto-polish
- 2.3 Ethics Review: Check for violations of three principles, flag omissions
- 2.4 Cross-scenario consistency: Compare with historical facts in memory, output difference report
- **2.5 Persona consistency detection (new)**:
  - Detect if current text matches the persona's expression characteristics
  - Output: "This sentence doesn't sound like something {persona_name} would say, suggest changing to: ..."
  - Persona consistency score (1-10)

**Iteration control**: Max 3 rounds, each round focuses on modifying 1-2 lowest-scoring dimensions. If still below 7 after 3 rounds, output "suggest human intervention."

### Phase 3: Narrative Interactive Design
Call the interactive design Skill, output following the six-step structure (see narrative interactive design Skill).

### Phase 4: Memory Write
Call the meta-Skill's memory write interface, save:
- Core elements of this narrative (story_id, title, scene, core event/turning point/cognition, full text)
- If interactive design was generated, save design_id and fragment summaries
- Update user preferences (e.g., persona and speaker used this time)
- Generate "narrative universe map" incremental update suggestions

## 📝 User Interaction Interface

### User Guide
When you have a narrative need, tell me in this format:

1. Select scene: [personal IP/brand/product/funding/sales/organizational change/charity]
2. Select mode: A Quick Output / B Deep Polish / C Interactive Design / D Interactive Design Only
3. Select persona: [ENFJ/ENFP/INFJ/INFP/auto-recommend if not filled]
4. **Select speaker**: [Jobs/Lei Jun/Zhang Xuefeng/Nadella/Musk/Yu Minhong/Duan Yongping/Zhang Yiming/custom/skip if not filled]
5. Fill in material: [provide information based on scene]

### Example Invocation
```
Help me write a personal IP story, using B Deep Polish mode, told in Jobs' voice.
My material is:
Quit a big tech company without another job lined up, took a gap year, then transitioned to career planner, helped 30+ people find their direction.
```

AI output:
- Memory summary (if historical stories exist)
- Persona recommendation
- Persona distillation result (expression DNA)
- First draft
- Assessment report
- Iteration modification records
- Polished final draft
- De-AI detection result
- Persona consistency detection result
- Memory write confirmation

## 📊 Iteration Report Format
```
Round 1: [detected issue] → [modification action] → [score change]
Round 2: [detected issue] → [modification action] → [score change]
Round 3: [detected issue] → [modification action] → [score change]
```

## ⚠️ Common Mistakes

1. **Skipping Phase 0**: Generating without memory retrieval, leading to repetitive narratives or inconsistencies
2. **Over-iteration**: Exceeding 3 rounds with scores still below 7, should output "suggest human intervention"
3. **Ignoring ethics review**: Not checking for factual distortion or inappropriate omission
4. **Inconsistent persona**: Mixing multiple persona styles within the same narrative
5. **Memory not written**: Not saving story to memory after generation, preventing narrative universe formation
6. **Overdone persona style**: Speaker characteristics too deliberate, affecting narrative naturalness

## 🧪 Usage Examples

### Example 1: Quick Output Mode (no speaker)
User input:
```
Scene: Personal IP
Mode: A
Persona: Not filled
Speaker: Not filled
Material: Quit a big tech company without another job lined up, took a gap year, then transitioned to career planner, helped 30+ people find their direction
```

AI output:
```
📚 Memory Retrieval:
- No relevant historical records found
- Suggestion: This is a good starting point for a series

🎭 Persona Recommendation: INFP
Reason: Material characteristics are personal growth, vulnerable experience, sincere reflection

📝 First Draft:
[~1200 character personal IP story]

💾 Memory Write:
- story_id: story_001
- Status: Success
```

### Example 2: Deep Polish Mode (with speaker)
User input:
```
Scene: Personal IP
Mode: B
Persona: INFP
Speaker: Jobs
Material: Same as above
```

AI output:
```
📚 Memory Retrieval:
- No relevant historical records found

🎭 Persona Recommendation: INFP (user-specified)

🔍 Persona Distillation (Jobs):
- Expression DNA: Short sentences, rhetorical questions, "One more thing"
- Cognitive framework: Simplicity is the ultimate sophistication
- Forbidden words: empower, closed-loop, grip

📝 First Draft:
[~1200 character personal IP story, told in Jobs' voice]

🔍 Meta-Skill Polish:
- Eight-Blade Assessment: History 8/10, Dialectics 7/10, Phenomenology 6/10⚠️, Language 8/10, Form 8/10, Existence 9/10, Aesthetics 7/10, Meta-reflection 8/10
- De-AI Detection: Rule 4 triggered (lacks detail anchors)
- Ethics Review: All passed
- **Persona Consistency Detection: 8/10** ✅
  - "The phrase 'empower the team' doesn't sound like something Jobs would say, suggest changing to 'let the team do the right thing'"

🔄 Iteration Modifications:
- Round 1: Added anchors like "May 2023", "Shenzhen"
- Round 2: Phenomenology dimension improved from 6 to 8, persona consistency from 8 to 9

📝 Final Draft:
[~1500 character polished personal IP story, told in Jobs' voice]

💾 Memory Write:
- story_id: story_001
- Speaker: Jobs
- Status: Success
```

## 📋 Quality Checklist

- [ ] Phase 0 memory retrieval complete?
- [ ] Phase 0.2 persona distillation complete (if speaker specified)?
- [ ] Phase 1 scenario Skill generation complete?
- [ ] Phase 1 persona style injection complete (if speaker specified)?
- [ ] Phase 2 meta-Skill polish complete (Mode B/C/D)?
- [ ] All Eight-Blade dimensions ≥ 7?
- [ ] All 7 de-AI detection rules passed?
- [ ] Ethics review no violations?
- [ ] **Persona consistency detection passed (if speaker specified)?**
- [ ] Phase 3 interactive design complete (Mode C)?
- [ ] Phase 4 memory write complete?
- [ ] Iteration report complete?
- [ ] User interaction clear?

## 📚 Persona Expression DNA Library (L6 Module)

> Based on nuwa-skill distillation results, extensible.
> Full list at `persona-dna-library.md`

| # | Persona | Applicable Scene | Expression Characteristics | Cognitive Framework | Forbidden Words |
|---|------|---------|---------|---------|--------|
| 1 | Luo Zhenyu | Personal IP | "Relentless""Long-termism""Friends of time" | Long-termism, relentless spirit | Empower, closed-loop, grip |
| 2 | Yu Minhong | Brand | Graceful exit, no complaints, turn crisis into transformation story | Finding hope in despair | Complaints, unfairness, luck |
| 3 | Lei Jun | Product | "Are you OK", benchmark comparisons, self-deprecation | Touch hearts, fair pricing | High-end luxury, opulent |
| 4 | Zhang Yiming | Funding | Context not Control, rational, systems thinking | Rational decisions, systems thinking | Sentiment, emotion, intuition |
| 5 | Li Jiaqi | Sales | "All the girls""I'll state the flaws first" | Trust-based sales, scenario-based seeding | Empower, closed-loop, ecosystem |
| 6 | Nadella | Organizational Change | "I was wrong", empathy, growth mindset | From knowing everything to learning everything | Wolf-culture, hustle, 996 |
| 7 | Han Hong | Charity | "I'm on the ground, I need you" | Action before words | Empower, closed-loop, ecosystem |
| 8 | Luo Xiang | Legal | "Crazy lawyer Zhang San", case-based teaching | Law is the bottom line of morality | Empower, closed-loop, ecosystem |
| 9 | Tao Yong | Medical | Gentle, powerful, philosophical | Post-traumatic growth, doctor-patient trust | Empower, closed-loop, ecosystem |
| 10 | papi Jiang | Social Media | Humorous deconstruction, irony, fast-paced | Internet sense, content is product | Empower, closed-loop, ecosystem |
| 11 | Philippe Starck | Creative Product | Minimalist, philosophical, slightly provocative | Simplicity is the ultimate sophistication, design is philosophy | Empower, closed-loop, ecosystem |
| 12 | Li Ziqi | Lifestyle | No dialogue, slow narrative, visual expression | Silent narrative, Eastern aesthetics | Empower, closed-loop, ecosystem |
| 13 | Musk | Tech | Physics analogies, first principles, tweet-style humor | Asymptotic approach to limits | Industry best, leading |
| 14 | Debate Mode | Controversial Topic | "On one hand... on the other hand..." | Dialectical thinking, data-driven | Taking sides, emotional manipulation |
| 15 | Cai Guo-Qiang | Art | Poetic, philosophical, slightly mysterious | Creating beauty through destruction, instant is eternal | Empower, closed-loop, ecosystem |
| 16 | Jordan Peterson | Psychology | "Clean your room""Take risks" | Responsibility is freedom, meaning before happiness | Empower, closed-loop, ecosystem |
| 17 | Yvon Chouinard | Sustainability | "Don't buy this jacket" | Anti-consumerism, business and environment coexistence | Overconsumption, short-term interests |
| 18 | Zhang Xuefeng | Education | Hard truths, dialect, straight talk | ROI first, no BS | Dreams, sentiment, poetry and distance |
| 19 | Buffett | Investment | Plain, direct, slightly humorous | Value investing, long-term holding, circle of competence | Short-term, speculation, leverage |
| 20 | Wang Xing | Entrepreneurship | Rational, systems thinking, slightly philosophical | Long-termism, systems thinking | Sentiment, emotion, intuition |

## ⚠️ Honest Boundaries

**Limits of persona distillation** (inherited from nuwa-skill):
- Distilling public expression, not simulating private thoughts
- Cannot capture persona's personality shifts over time
- If persona said contradictory things, system prioritizes the most widely known version
- Expression DNA is a statistical feature, not a fixed template
- **A Skill that doesn't tell you its limitations isn't trustworthy**

## 🔒 Persona Library Usage Boundaries (Important)

**Core principle: The persona library only affects "how to tell," not "what to tell."**

### ✅ What the persona library CAN change
- Tone, rhythm, word preferences
- Sentence structure (short/long sentences, rhetorical/declarative)
- Analogy style (using everyday knowledge/tech terms/historical stories)
- Emotional tone (calm/enthusiastic/humorous/serious)
- Forbidden word substitution (avoiding certain words, using alternatives)

### ❌ What the persona library CANNOT change
- Core events (what happened)
- Turning point logic (why things changed)
- Cognitive upgrades (what was learned)
- Narrative structure (beginning/development/climax/conclusion, Eight-Blade framework)
- Meta-narrative elements (history/dialectics/phenomenology/existence/aesthetics)
- Factual content of user's original material

### Correct Usage Example
```
User material: Quit a Shenzhen big tech company in May 2023 without another job, took a gap year to transition to career planner

❌ Wrong usage (changes the narrative):
"In the spring of 2023, I stood on the streets of Shenzhen, like Jobs leaving Apple..."
(Problem: Changes the user's factual experience, fabricates a non-existent analogy)

✅ Correct usage (only changes expression):
"In May 2023, I made a decision. Left Shenzhen. Left the big tech company. Not impulsively, but after calculating the physical limit — staying here, three years from now I'd be no different from today."
(Problem: Preserves user's facts, just expressed in a more concise, powerful way)
```

### Execution Rules
1. **Complete narrative skeleton first**: Generate complete first draft using meta-narrative framework (without persona style injection)
2. **Then inject expression DNA**: On top of the skeleton, only adjust tone, sentence structure, word choice
3. **Zero factual modification**: Not a single word of the user's factual material can be changed
4. **Persona consistency detection**: Only detects if expression style is consistent, not narrative content

## /persona list Command

Lists all available speakers and their applicable scenes.

### Command Format
```
/persona list
```

### Output Format
```
📋 Available Speaker List (20 personas)

| # | Speaker | Applicable Scene | Reason to Choose |
|---|--------|---------|---------|
| 1 | Luo Zhenyu | Personal IP | "Relentless""Long-termism""Friends of time" |
| 2 | Yu Minhong | Brand | New Oriental → East Buy, graceful exit + cultural transformation |
| 3 | Lei Jun | Product | "Touch hearts, fair prices""Run a benchmark if you disagree" |
| 4 | Zhang Yiming | Funding | Replace tech terms with scenarios, early funding, contrarian positioning |
| 5 | Li Jiaqi | Sales | "All the girls""I'll state the flaws first" |
| 6 | Nadella | Organizational Change | "From knowing everything to learning everything" |
| 7 | Han Hong | Charity | "I'm on the ground, I need you" |
| 8 | Luo Xiang | Legal | "Crazy lawyer Zhang San" |
| 9 | Tao Yong | Medical | Returned after injury, wrote "Gaze" |
| 10 | papi Jiang | Social Media | Deconstruct daily life with humor |
| 11 | Philippe Starck | Creative Product | Famous industrial designer (Alien juicer) |
| 12 | Li Ziqi | Lifestyle | Pastoral life, slow narrative, no dialogue but global empathy |
| 13 | Musk | Tech | First principles, asymptotic approach to limits |
| 14 | Debate Mode | Controversial Topic | Not suitable for a single persona, use "both sides' perspectives" instead |
| 15 | Cai Guo-Qiang | Art | Gunpowder爆破 artist, creating beauty through destruction |
| 16 | Jordan Peterson | Psychology | "12 Rules for Life" |
| 17 | Yvon Chouinard | Sustainability | Patagonia founder, "Don't buy this jacket" |
| 18 | Zhang Xuefeng | Education | "Hard truths," college/graduate school guidance |
| 19 | Buffett | Investment | Value investing, long-term holding, circle of competence |
| 20 | Wang Xing | Entrepreneurship | Meituan founder, thousand-group battle, from 0 to 1 |

💡 Usage: /persona [speaker name]
Example: /persona Lei Jun
```

---

*Version: 1.4.0 | Last updated: 2026-04-30*
*Update content: Added persona distillation module (Phase 0.2), persona consistency detection (Phase 2.5), persona expression DNA library (L6), /persona list command*
