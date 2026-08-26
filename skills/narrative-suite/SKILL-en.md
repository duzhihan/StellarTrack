---
name: dragoncraft-hub
description: "[When to use] When you need to manage/navigate/query 17 narrative scenario skills; when you need a unified entry point, scenario comparison, or dependency graph"
author: ant (CEO 助理)
created: 2026-04-30
version: 1.0.0
skill_type: 核心🔴
allowed-tools: [Bash, Read, Write, Exec]
tags: [dragoncraft, dragoncraft-hub, narrative, storytelling]
---

# DragonCraft Hub
**Description**: Narrative Skill suite manager. Centrally manages 17 scenario skills, providing navigation, comparison, and dependency graphs.

## 🎯 Features

### Scenario List

| # | Skill | Scenario | Core Input | Output Format | Special Compliance |
|---|-------|------|---------|---------|---------|
| 1 | narrative-personal-ip | Personal IP | Done/Care about/Encountered/Learned | Full version/Short video version/Bio version | None |
| 2 | narrative-brand | Brand | Why exist/What believe/What experienced/What became | Brand manifesto/Founder story/Manual excerpt | None |
| 3 | narrative-product | Product | User problem/Product motivation/Solution/User change | Launch copy/User story/Manual excerpt | None |
| 4 | narrative-funding | Funding | Market opportunity/Team capability/Business model/Funding needs | BP storyline/Pitch/DD Q&A | None |
| 5 | narrative-sales | Sales | Customer problem/Customer hesitation/Persuasion method/Customer change | Customer case/Sales script/Objection handling | None |
| 6 | narrative-organization | Organizational Change | Change driver/Change content/Resistance points/Target state | Internal letter/Roadmap/FAQ | None |
| 7 | narrative-charity | Charity | Beneficiary group/Action/Change/Call to action | Charity story/Fundraising copy/Volunteer recruitment | None |
| 8 | narrative-legal | Legal | Case facts/Dispute focus/Legal basis/Claims | Representation statement/Fact statement/Legal opinion | **Mandatory full disclosure** |
| 9 | narrative-medical | Medical | Condition/Treatment plan/Doctor-patient decision/Result | Communication script/Patient story/Informed consent | **Mandatory full disclosure** |
| 10 | narrative-social | Social Media | Platform/Audience/Trends/Persona | Viral copy/Hashtags/Interactive design | None |
| 11 | narrative-creative | Creative Product | Creative concept/Target user/Differentiation/User experience | Creative brief/User story/Visual script | None |
| 12 | narrative-lifestyle | Lifestyle | Daily life/Values/Aesthetics/Target of influence | Manifesto/Content planning/Visual guide | None |
| 13 | narrative-tech | Tech | Tech pain point/Tech barrier/Market opportunity/Business model | Tech story/Pitch/Competitor analysis | None |
| 14 | narrative-controversy | Controversial Topic | Controversy focus/Stance/Evidence/Goal | Position statement/Debate script/Response strategy | **Acknowledge validity of opposing views** |
| 15 | narrative-art | Art | Work/Creative philosophy/Audience experience/Work impact | Artist statement/Exhibition preface/Work interpretation | None |
| 16 | narrative-psychology | Psychology | Psychological struggle/Healing process/Growth change/Help target | Healing story/Psychology education/Mutual support guide | **Must not replace professional medical advice** |
| 17 | narrative-sustainable | Sustainability | Environmental issue/Action/Change/Next steps | Sustainability report/Call to action/Brand commitment | **Must not "greenwash"** |

### Dependency Graph

```
narrative-suite (manager)
  ↓
narrative-workflow (orchestration engine)
  ↓
narrative-meta (underlying OS)
  ├── Eight-Blade Assessment
  ├── De-AI Detection
  ├── Ethics Review
  ├── Persona Mapping
  └── Memory Management
  ↓
17 scenario skills (call narrative-meta modules)
```

### Usage Methods

1. **Navigation**: Tell me your scenario, I recommend the corresponding skill
2. **Comparison**: Tell me two scenarios, I output a comparison table
3. **Dependency query**: Tell me a skill name, I output the dependency relationship
4. **Batch generation**: Tell me multiple scenarios, I batch-generate narratives

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

---

*Version: 1.0.0 | Last updated: 2026-04-30*
