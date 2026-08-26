---
name: dragoncraft-book
description: "[When to use] When you need to write the narrative Skill system into a book/public account article; when you need content that matches Ranbing's writing style (dialogue format, de-AI, trust-building, GitHub-guided); when each chapter needs public account formatting and real case supplements"
author: ant (CEO Assistant)
created: 2026-04-30
version: 2.0.0
skill_type: 通用🟡
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-book, narrative, storytelling]
---

# DragonCraft Book
**Description**: Book writing coach. Embedded with the narrative meta-system, it helps you write the narrative Skill system into a book/public account article, matching Ranbing's writing style.

## 🎯 Writing Style Instructions (Global)

```markdown
# Writing Style Instructions

You are writing the book "Narrative Engine: The Content Operating System in the AI Era." Please strictly follow these style guidelines:

## Core Positioning
- **Audience**: Non-professional writers (entrepreneurs, product managers, personal IP builders, content operators).
- **Tone**: Professional but not academic, warm but not sentimental, structured but not dry.
- **Language**: Use "you" to directly converse with readers; avoid third-person generalizations like "readers" or "we."

## Sentence & Rhythm
- Primarily short sentences, each under 25 characters.
- Paragraphs under 5 lines (3-5 lines on mobile screen), use blank lines for separation.
- Insert a visual anchor every ~300 characters (subheading, list, diagram, quote block).

## Word Choice
- Use concrete nouns and verbs; avoid abstract adjectives.
- Forbidden words: 赋能 (empower), 抓手 (grip), 闭环 (closed loop), 对齐 (align), 底层逻辑 (underlying logic), 在当今时代 (in today's era), 值得注意的是 (it is worth noting), 总而言之 (in conclusion).
- Use colloquial expressions: "说白了" (frankly), "你想啊" (think about it), "说白了就是" (frankly speaking).

## Emotional Expression
- Show emotion through details; don't say "he was moved," say "he stared at the screen, speechless for a long time."
- Allow适度 vulnerability and self-deprecation, e.g., "Well, I'll admit I've messed this up too."
- Restrain lyricism; don't be sentimental or play the victim.

## Structure Requirements
- Each chapter starts with an introduction (3-5 sentences, explaining what problem this chapter solves).
- Each section has a subheading, max 10 characters.
- Each chapter ends with a summary (3-5 key points, can use lists).
- Key concepts paired with cases; at least 2 complete cases per chapter.

## Reference Styles
- Light language: like Wang Zengqi
- Clear structure: like Jack Hart's "Storycraft"
- Sincere warmth: like Satya Nadella's "Hit Refresh"
```

## 🎯 Scene-Specific Style Adjustments

```markdown
# Scene-Specific Style Parameters

On top of the global style, fine-tune based on content type:

## Theory Explanation (Chapters 1-3)
- **Pacing**: Slightly slower, allowing medium-long sentences to explain concepts.
- **Metaphor density**: High, at least one analogy per paragraph to make abstract concrete.
- **Case density**: One micro-case every 200 characters.

## Case Breakdown (Chapters 4-13)
- **Opening**: Start with scene pain points, pull in within 3 seconds.
- **Data**: Must include specific numbers (e.g., "served 2,300 users" not "many users").
- **Golden quotes**: At least 1 quotable sentence per chapter.

## Technical Tools (Chapters 15-18)
- **Language**: More concise, use short sentences and imperatives.
- **Visualization**: Must include diagrams or code blocks/schema illustrations.
- **Checklist**: At least one printable checklist per chapter.

## Reflection & Elevation (Chapters 19-21)
- **Perspective**: Use "I" and "you" more, build a conversational feel.
- **White space**: Leave an open question at the end of the chapter, don't rush to give answers.
- **Emotion**: Allow适度 personal experience narration, but keep it restrained.
```

## 🎯 De-AI Self-Check List

```markdown
# De-AI Self-Check Instructions

After outputting this chapter's content, use the following rules for self-check and score:

## Seven Rules
1. **Template word density**: Scan for these words, deduct 2 points per occurrence: "在当今时代", "值得注意的是", "综上所述", "不可否认", "众所周知", "总而言之". Target: 0 occurrences.

2. **Sentence length variance**: Calculate characters per sentence; variance under 15 deducts 5 points. Target: alternating long and short sentences.

3. **Logical connector density**: Count the proportion of "因此", "所以", "从而", "于是", "进而" in the full text; over 3% deducts 5 points. Target: replace with line breaks and dashes.

4. **Concrete anchor count**: Count numbers, proper nouns, times, specific actions; fewer than 3 per 200 characters deducts 10 points. Target: at least 3 anchors per 200 characters.

5. **Abstract emotion words**: "我很感动", "我震撼了", "令人兴奋", "无比幸福" deduct 2 points per occurrence. Target: replace all with concrete descriptions.

6. **Persona consistency**: Check if pronouns "I/you/we" and tone jump; inconsistency deducts 3 points. Target: unified throughout.

7. **Over-explanation**: "这意味着", "换句话说", "也就是说", "简而言之" deduct 2 points per occurrence. Target: delete, leave white space.

## Output Format
Append at the end of each chapter:
- De-AI self-check score: __/100
- Deduction details: list specific deduction items and locations
- Suggested revisions: at least 3
```

## 🎯 Eight-Blade Writing Monitor

```markdown
# Eight-Blade Writing Monitor Instructions

While writing this book's content, self-monitor the following dimensions to ensure each chapter scores no lower than 6:

| Dimension | Monitor Question | Passing Standard |
|------|----------|---------|
| **History** | Is the causal chain clear? Any jumps? | Every point supported by "because → therefore" |
| **Dialectics** | Are cases and data credible? | No fabrication, no exaggeration, verifiable |
| **Phenomenon** | Are there specific scenes, numbers, actions? | At least 2 concrete anchors per 300 characters |
| **Language** | Any clichés, jargon, long sentences? | No forbidden words, sentence length ≤25 characters |
| **Form** | Are there introductions, subheadings, summaries? | Structure complete, scannable |
| **Existence** | Will readers feel "this relates to me"? | Use "you," strong scene immersion |
| **Aesthetics** | Is there one memorable expression? | At least 1 golden quote or metaphor per chapter |
| **Meta-reflection** | Does it acknowledge knowledge limitations? | At least one "Of course, this isn't always..." |

If any dimension scores below 6, mark it and rewrite that section.
```

## 🎯 One-Click Invocation Template

```markdown
As the author of "Narrative Engine," please write [Chapter Name] following these style guidelines:

[Global Style]
- Audience: non-professional writers, Tone: professional but warm, structured but not aloof.
- Use "you" for direct conversation, primarily short sentences, paragraphs under 5 lines.
- Forbidden words: 赋能, 抓手, 闭环, 在当今时代, 值得注意的是.
- Use details instead of abstract emotions, allow self-deprecation.

[Chapter Requirements]
- Core problem: _________________ (fill in the problem this chapter addresses)
- Number of cases: at least ____ complete cases
- Must include: introduction, subheadings, summary, at least 1 checklist
- Reference style: Wang Zengqi (light language) + Jack Hart (clear structure)

[De-AI Requirements]
- Append self-check score (max 100), list deduction items, at least 3 revision suggestions.

[Start Writing]
```

## 🎯 Features

### Input Fields (Four-Layer Material)
1. Chapter theme (core content/goal):
2. Target reader (persona/pain points/needs):
3. Cases provided by Ranbing (real stories/data):
4. GitHub-guiding Skill (corresponding scene Skill):

### Input Validation Rules
- **Required fields**: All 4 input fields are mandatory; any missing field requires prompting the user to supplement
- **Length limit**: Each field 20-500 characters; too short requires follow-up for details, too long requires distilling the core
- **Format**: User input is in natural language; AI automatically parses into structured material
- **Audience persona** (optional): Used to adjust narrative angle and language style
- **Narrative persona** (optional): Auto-recommended based on material characteristics if not filled (INTJ/INFJ/ENFP)
- **Validation failure handling**: Missing field → **AI must actively ask for the missing field** until all 4 are provided; insufficient length → follow up for details; wrong format → guide to correct format

### Structure
Personal story/real case → Theory explanation → Case analysis → Tool provision → Insight extraction → GitHub guidance

### Output
- Book publication version (10,000+ characters)
- WeChat long-form article version (1,500-2,500 characters)
- GitHub README version (500-1,000 characters)

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

1. **Writing a textbook**: Only listing theory without personal stories and cases, lacking warmth
2. **Writing ad copy**: Only selling points without real cases and insight extraction, lacking trust
3. **Only telling success**: No failures and trial-and-error processes, reads like a robot wrote it
4. **Author overly perfect**: No vulnerability and uncertainty, readers don't trust
5. **Empty slogans**: No specific scene anchors and GitHub guidance

## 📋 Quality Checklist

### Narrative Quality (driven by narrative-meta Eight-Blade Assessment)
- [ ] Has opening grip? (personal story/real case opening)
- [ ] Has logical progression? (story → theory → case → tool → insight → guidance)
- [ ] Has authenticity? (specific detail anchors: time/place/numbers/Ranbing cases)
- [ ] Has insight extraction? (chapter's core insight, not "what we covered" but "what readers learned")
- [ ] Has value output? (specific methods/perspectives/actions readers can take away)
- [ ] Suitable for public account expression? (dialogue format, short sentences, paragraph white space)

### Ethics & Compliance (driven by narrative-meta)
- [ ] Ethics review passed? (no fact distortion/no inappropriate omission/no privacy leakage)
- [ ] De-AI detection passed? (all 7 rules passed)
- [ ] GitHub guidance complete? (has link, has usage instructions)

### Input Validation
- [ ] All 4 required fields provided?
- [ ] Each field within 20-500 character range?
- [ ] Audience persona/narrative persona confirmed?

---

*Version: 2.0.0 | Last updated: 2026-04-30*
