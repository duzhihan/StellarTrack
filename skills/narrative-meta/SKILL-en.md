---
name: dragoncraft-core
description: "[When to use] When you need to evaluate narrative quality, generate narrative skeletons, detect AI-ness, recommend narrative personas, conduct ethics reviews, perform cross-scenario consistency checks, or retrieve memories"
author: ant (CEO Assistant)
created: 2026-04-29
version: 3.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-core, narrative, storytelling]
---

# DragonCraft Core
**Description**: The underlying operating system of narrative. Provides theoretical support, aesthetic judgment, ethical benchmarks, and quality checks for all scene Skills. Does not directly output content, but is called by scene Skills as an "operating system."

## 🎯 Core Capabilities

1. **Narrative Assessment**: Output assessment reports using the Eight-Blade framework.
2. **Knowledge Retrieval**: Provide theoretical basis for scene Skills.
3. **Structure Generation**: Generate skeletons based on Labov's formula.
4. **De-AI Detection**: 7-rule detection with revision suggestions.
5. **Persona Mapping**: Recommend the most suitable MBTI narrative persona.
6. **Ethics Review**: Apply three principles, mark omissions and risks.
7. **Consistency Check**: Cross-scenario comparison, output difference reports.
8. **Memory Management**: Store and retrieve users' historical narratives for continuity and consistency.

## 📚 Built-in Knowledge Base

### Module 1: Narrative Instinct Formula
Narrative = (event + causality + intention) → temporalization → transmissible experience unit

### Module 2: Labov's Minimal Story Formula
(abstract) → orientation → complicating action → evaluation → resolution → coda

### Module 3: Narrative Eight-Blade Assessment Framework
| Eight-Blade Dimension | Assessment Rule | Detection Method |
|----------|---------|---------|
| History | Does the narrative conform to human cognitive habits? Any forced distortion? | Check if causal chain is self-consistent |
| Dialectics | Is the balance between narrative and logic/data broken? | Check if narrative overwrites facts |
| Phenomenon | Is the narrative's starting point real and perceptible? | Check for specific scene anchors |
| Language | Is the language natural, warm, free of template traces? | AI-ness detection |
| Form | Does it conform to Labov's minimal story formula? | Structure completeness check |
| Existence | Does the narrative serve self-identity or social collaboration? | Goal matching check |
| Aesthetics | Does the narrative have aesthetic value? | Golden quote density, imagery quality |
| Meta-reflection | Are there obvious fictional parts the author is unaware of? | Fact-narrative separation detection |

### Module 4: MBTI Narrative Persona Mapping
| Type | Narrative Style | Typical Scenarios |
|------|---------|---------|
| ENFJ | Inspiring narrative, calls for collective action | Brand mission, team mobilization, charity, education |
| ENFP | Improvisational narrative, lively and跳跃 | Social media, creative products, lifestyle IP |
| INFJ | Metaphorical narrative, deep healing | Brand philosophy, psychology, art, sustainability |
| INFP | Autobiographical narrative, sincere and gentle | Personal IP, healing blogs, creators |
| INTJ | Calm, far-sighted strategist | Tech funding, industry analysis, hardcore knowledge |
| ENTP | Challenger, disruptor | Controversy topics, counterintuitive viewpoints, debate |
| ESFP | Enthusiastic, present-focused performer | Live streaming, store exploration, entertainment short videos |
| ISFJ | Silent guardian, doer | Service industry, healthcare, traditional crafts |

### Module 5: Exploratory Narrative Design Principles
Fragmented distribution → user exploration and assembly → sense of ownership

### Module 6: De-AI Detection Rules Checklist (7 Rules)
| Rule | Detection Content | Automated Judgment Method | Polishing Action |
|------|---------|---------------|---------|
| Rule 1 | Overuse of template words | Match against word bank: "在当今时代", "值得注意的是", etc. | Delete or convert to colloquial |
| Rule 2 | Every sentence too neat | Detect sentence length variance; triggers if variance < 1.5 | Split long sentences, insert short sentences, colloquial interruptions |
| Rule 3 | Logical connectors too dense | Detect density of "因此→所以→然后" | Delete unnecessary logical connectors, replace with line breaks/dashes |
| Rule 4 | Lacking detail anchors | Detect presence of names/times/locations/numbers | Prompt user to supplement anchors, or auto-generate placeholders [please supplement] |
| Rule 5 | Abstract emotions | Detect abstract expressions like "我很感动", "我很震撼" | Prompt conversion to concrete descriptions |
| Rule 6 | Persona inconsistency | Use consistency scoring model to detect tone/perspective jumps | Unify to selected narrative persona |
| Rule 7 | Over-explanation | Detect "explaining too much" words like "这意味着", "换句话说" | Delete or convert to white space |

### Module 7: Narrative Ethics Module
**Three Core Principles**
- **Principle 1: Don't fabricate, but don't tell the whole truth** → Facts cannot be distorted; omitted information must not have a direct causal relationship with the audience's core decisions; the following scenarios require mandatory full disclosure (legal trials, medical informed consent, funding due diligence, product safety).
- **Principle 2: Target audience oriented (not mandatory)** → If the user provides an audience persona, the narrative will be adjusted to address their concerns; if not provided, general best practices are used.
- **Principle 3: Scene-adapted framework/thinking/method** → Each scene has its own independent structure template and knowledge base; cross-scenario consistency checks are provided.

**Execution Method**
- After generating a narrative, automatically scan for potentially misleading omissions, mark [omitted X here, please inform if you need complete information].
- Users can choose "waive ethics check" or "force complete version."

### Module 8: Cross-Scenario Consistency Check
When the same material is used across multiple scenes, this function can be called to output:
- Factual difference points
- Value orientation differences
- Recommended unification items

### Module 9: Memory and Continuous Narrative
- Each user has an independent narrative memory bank, recording:
  - Generated story themes, key events, character cores
  - User-preferred narrative personas, commonly used golden quotes, typical structures
  - Past feedback and revision records
- When the user creates again, the meta-system automatically retrieves memories to ensure:
  - The same theme is not repeated (or forms a series)
  - Characters' values remain consistent across narratives
  - New narratives can reference/echo past narratives (forming a "narrative universe")
- Supports cross-scenario memory invocation (e.g., cognitive points from personal IP stories can be reused in brand stories or product narratives)

## ⚠️ Common Mistakes

1. **Over-instrumentalization**: When the motivation for "self-narrative" slides from "sharing inspiration" to "building IP," the narrative automatically applies a filter that makes you look more successful and more dramatic.
2. **Narratives lie**: The narrative instinct cannot handle true randomness or pure repetition. When patterns don't exist, people still force stories.
3. **Risk of instrumentalization**: Being completely dominated means the "story" you ultimately create completely swallows your true self.

## 🧪 Usage Examples

### Example 1: Narrative Assessment
User input:
```
Material: After quitting my job at a big tech company, I had no income for half a year, sold hand-drip coffee at a street stall while being chased by city management, then discovered I was good at "building order out of chaos"
```

AI output:
```
Narrative Assessment Report:
- History dimension: 7/10 (causal chain is basically self-consistent, but the turning point from "no income for half a year" to "discovered my strength" needs more detail support)
- Dialectics dimension: 8/10 (good balance between narrative and facts, no obvious distortion)
- Phenomenon dimension: 6/10 (starting point is real and perceptible, but lacks specific scene anchors)
- Language dimension: 7/10 (overall natural, but "building order out of chaos" is slightly abstract)
- Form dimension: 8/10 (conforms to Labov's formula, structure complete)
- Existence dimension: 9/10 (serves self-identity, clear goal)
- Aesthetics dimension: 7/10 (has golden quote potential, but imagery quality can be improved)
- Meta-reflection dimension: 8/10 (no obvious fabrication, self-awareness is clear)

Recommended persona: INFP (sincere, delicate, autobiographical)
Labov skeleton:
- Abstract: Confusion after quitting
- Orientation: Specific scene of selling coffee at a street stall
- Complicating action: Dilemma of being chased by city management
- Evaluation: Discovering the ability to "build order out of chaos"
- Resolution: Transitioning to career planner
- Coda: Helping 30+ people find direction

Ethics review:
- Principle 1: No fact distortion, omitted information is "specific company name," no direct causal relationship with core decisions, marked [omitted company name here, please inform if you need complete information]
- Principle 2: No audience persona provided, general best practices used
- Principle 3: Scene is personal IP, using hero's journey variant framework

De-AI detection:
- Rule 4 triggered: Lacks specific detail anchors (suggest supplementing time, location, specific numbers)
- Rule 5 triggered: "Building order out of chaos" is too abstract (suggest converting to concrete description)

Memory retrieval:
- No related historical records found
- Suggestion: This is a good starting point for a series story, consider forming a "Life Turning Points Trilogy"
```

### Example 2: Persona Recommendation
User input:
```
Scene: Brand story
Material: A studio that does old clothes改造, doesn't sell new clothes, helps customers transform old clothes into new designs
```

AI output:
```
Persona Recommendation: INFJ
Reason:
- Scene characteristics: Brand philosophy, deep healing, sustainable philosophy
- Material characteristics: Old clothes transformation, time continuation, unfinished stories
- INFJ narrative style: Gentle but profound, likes to tell metaphors and healing stories, suitable for brand core narrative

Recommended narrative angles:
- "Inside every piece of clothing sent to us lives a chapter someone couldn't bear to delete"
- "We don't make new clothes. We just help time continue its sentences"
```

## 📋 Quality Checklist

- [ ] All Eight-Blade dimensions ≥ 7 points?
- [ ] Labov structure complete?
- [ ] Persona recommendation has reasons?
- [ ] All 7 De-AI detection rules passed?
- [ ] Ethics review no violations?
- [ ] Cross-scenario consistency check passed (if history exists)?
- [ ] Memory retrieval complete?
- [ ] Has specific detail anchors?
- [ ] Has white space?
- [ ] De-AI'd?

---

*Version: 3.0.0 | Last updated: 2026-04-29*
