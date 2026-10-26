# StellarTrack — A Cross-Genre Academic Writing System

![License](https://img.shields.io/badge/License-MIT-yellow.svg) ![Version](https://img.shields.io/badge/version-v12.5.21-blue) ![Agent Skill](https://img.shields.io/badge/Agent%20Skill-O--S--C--E-green)

<div align="center">

<img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/hero.svg" alt="StellarTrack" width="100%"/>

**A writing pipeline with gates: AI does the labor, you sign off.**

O Orientation → S Strategy → C Construction (C1–C11) → E Experience ｜ [Quick Start](#installation) · [60-Second Demo](#a-60-second-demo) · [Comparison](#how-it-compares)

</div>

[简体中文](README.zh-CN.md) | **English**

---

## The Problem It Solves

Ask a large model to “write my paper” and it produces something that *looks* like a paper in ten seconds. But you don't dare submit it — because it never walked through your thinking process, so every conclusion feels borrowed.

What's missing is not text. It is **process**: topic selection that survives falsification, literature that gets verified against sources, frameworks that hold up, de-AI-ified prose, citations checked line by line, abstracts that match the body.

StellarTrack's answer is one principle: **change the genre by swapping the payload, never the pipeline.**

## Why I Built It

Writing papers, grant proposals, and long-form articles, I kept hitting the same wall:

- Halfway through, the argument collapses and I start over;
- Delegating to AI yields “the average text anyone could write” — it doesn't survive a reviewer's first glance;
- A pit I fixed last time, I fall into again next time — close the chat, lessons gone.

Existing tools come in two flavors: polishers and full-auto generators. **The former ignore process; the latter steal your thinking.** I wanted a third kind: break my workflow into eleven stations, each with a gate — AI does the grunt work (searching, drafting, formatting), but every key decision stops and waits for my signature.

| Your recurring pain | StellarTrack's fix |
|---|---|
| Chaotic process, constant rewrites | Eleven stations in strict order, each with acceptance checks |
| AI flavor that won't wash out | Two purification passes: semantic scan + rule re-check, item by item |
| Lessons never stick | Post-mortem after every piece; only validated lessons enter the rule base |

## Proof, Not Promises

Not paper architecture — real manuscripts from development:

| Path | Manuscript | Result |
|---|---|---|
| Second half of pipeline | Forum submission, 3,739 chars | All de-AI-flavor checks passed |
| First half of pipeline | Research proposal, 5,692 chars | Correctly identified early-stage draft |
| Full chain | Long manuscript, 31,783 chars | All eleven stations completed, incl. genuine 637-char continuation |
| Expert panel review | v12.3 six-seat re-evaluation | Six-dimension weighted **8.1/10** |

> All self-evaluated during development. **No external user validation yet** — that's the honest truth, and first on the roadmap.

## A 60-Second Demo

> **Me**: Write a course-ideology teaching case for me, due next week.
>
> **StellarTrack**: Got it — official-document genre, teaching scenario. Two questions: ① course name and major? ② which ideology mapping points have you chosen?
>
> **Me**: *Introduction to Digital Media Art*, three points.
>
> **StellarTrack**: That's all I need. Starting… Materials station done — three gaps filled, cleared for pass-through. Next: literature review.

Progress is visible at all times:

```
[✓]Orientation [✓]Strategy [✓]Topic [⏳]Materials [ ]Review …
▌Station Card▌ Materials complete ｜ Gate passed ｜ Next: Literature Review
```

When information is sufficient it doesn't ramble; when it must ask, at most two rounds, each with a recommended answer; wherever it guesses it says “I assumed X” — overrule anytime.

## How It Works

![C1–C11 construction pipeline](https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/workflow.svg)

| Phase | What it does | Key mechanism |
|---|---|---|
| **O — Orientation** | Converge vague intent into a real research question | Five-step listen-guess-restate loop |
| **S — Strategy** | Thesis sentence first; cheap falsification before drafting | Argument-anchoring card + 7-element gate |
| **C — Construction** | C1–C11 station pipeline | Numbered artifacts, tiered gates, three-layer loading (fixed skeleton / verb translation / registry matrix) |
| **E — Experience** | The system sharpens with use | Calibration ledger + confidence-weighted writeback |

Theory doc: [docs/THEORY.md](docs/THEORY.md) (design principles of the DiTing six-loop cognitive engine); runtime data templates in `data/_templates/`.

Mechanism overview — how gates bite and artifacts flow:

<img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/mechanism.svg" alt="Mechanism overview" width="100%"/>

Three standing rules:

1. AI may participate in thinking but cannot replace understanding — every critical decision point halts for the human.
2. Retrieval runs through real channels (native CNKI browser automation); the LLM never fabricates literature.
3. De-AI-flavoring is a station, not a slogan — C7 runs dedicated dual engines.

## When to Reach for It

| Where you're stuck | Where it takes over |
|---|---|
| Staring at a blank page | Asks “what are you arguing” before writing a word |
| A pile of literature, no gap statement | Three search rounds + gap formula force one sentence |
| Draft reads less like you with every edit | Dual purification gates strip AI flavor item by item |
| Five revisions in, can't tell good from bad | Every version numbered and scored; comparison returns to facts |
| Dozens of revision comments incoming | Mode-split revision: paragraph-level or global diagnosis |
| Last paper's pit, this paper again | The rule base is full of lessons already paid for |

In one sentence: **writing like this deserves your thinking**.

## Openness: Zero-Dependency Skeleton, Opt-In Engines

The pipeline has two layers. **The skeleton layer has zero dependencies** — download and run: O-to-E flow, thirteen gates, numbered artifact trails all live inside `skills/xingchan/`, needing nothing external.

**The engine layer mounts on demand.** Each station can take a dedicated skill for heavy lifting (search, review-writing, de-AI-flavoring, mechanism diagrams, evaluation…). This repo ships all default engines; the mapping lives in `skills/xingchan/references/C环节skill注册表.md`:

| You want to… | Do this |
|---|---|
| Just run it | Install all skills for full coverage; missing engines degrade gracefully anyway |
| See what's missing | `python check-engines.py` — readiness report per station |
| Add an engine | Find the registry row, install that skill, done |
| Bring your own keys | CNKI account, embedding keys etc. are yours; credentials go to env vars or interactive input only, **never into files or artifacts** |

**Explore & extend**:

- Teach it your method → write method cards in `skills/xingchan/references/methods/` (six-field format; existing cards serve as samples);
- New genre/register → seven register workflow packs in `skills/xingchan/references/` (academic, official, social-media, proposal, retrospective, speech, creative); copy the structure;
- Engine not cutting it → log a line in `data/graft-log.md`; two hits in the same cell auto-trigger candidate search (gap → trial mount → tenure);
- Loose ideas → `data/insight-inbox.md` staging box, reviewed monthly.

## Six Registers, One Pipeline

Papers are the mother template; other genres swap content directives, never the flow.

Academic (papers) ｜ Proposal (grants) ｜ Social media (long-form posts) ｜ Official (documents) ｜ Retrospective (project reports) ｜ Creative (fiction & poetry)

## Repository Layout

```
skills/                  # 66 components, all six registers fully engined
├── xingchan/        # Core: SKILL.md + six register workflows + references
├── thinking-protocols/   # DiTing cognitive engine: Socratic pipeline + mode cards + S-layer seven cards
├── Academic line         # abstract-checker / claim-audit / journal-fit / manuscript-review /
│                         # reference-check / research-design / theoretical-framework /
│                         # title-assessor / literature-review-writer / paper-mechanigraph-4ss /
│                         # cnki-deepsearch / citation-format / good-story
├── Revision line         # duzhihan-paper-editor / evidence-bound-revision /
│                         # nsfc-review-guide / academic-paper-reviewer / human-review
├── Proposal line         # nssfc-* (6 skills) / gongwen-draft
└── Media line            # narrative-suite + narrative-* (26 dragoncraft skills) / oh-story /
                          # wenfeng-slime / khazix-writer / ljg-writes / human-writing /
                          # wechat-article-search / douyin-copy-extract / ljg-card /
                          # ljg-present / lieflat-charts
check-engines.py         # One-shot engine dependency check
wordcount.py             # Character count (CJK-aware)
data/                    # Runtime seeds: graft log + insight inbox + templates
docs/THEORY.md           # DiTing six-loop cognitive engine theory
```

## Installation

1. Copy everything under `skills/` into your agent platform's skill directory (WorkBuddy: `~/.workbuddy/skills/`)
2. Two Node tools need dependencies: run `npm install` inside `skills/human-review/` and `skills/ljg-card/`
3. Reload the skill list and start — trigger phrases are in each SKILL.md, or just say “use StellarTrack”
4. (Optional) Run `python check-engines.py` to confirm engine readiness per station

## How It Compares

| | Academic helpers | Research multi-agents | Prompt frameworks | Workflow platforms | **StellarTrack** |
|---|---|---|---|---|---|
| Essence | Polish & format | Auto-generation | Input templates | Node orchestration | **End-to-end pipeline + quality gates** |
| Weakness | Ignores process | Steals thinking | No process constraint | No writing criteria | Zero community validation |

Versus prompt frameworks: **LangGPT teaches you to speak well; StellarTrack gets the paper finished.** Versus automation platforms: Dify orchestrates API nodes; StellarTrack orchestrates cognitive stations with acceptance gates. The cost, stated plainly: high design watermark, shallow battle record so far.

## Before You Use It

**What runs out of the box**: the whole writing pipeline C3–C11 (review synthesis, outline, drafting, mechanism diagrams, revision, formatting, review) — every skill needed is bundled and runs on your host's AI alone.

**What needs your environment**: the CNKI-native automation inside C1 (topic channel) and C2 (literature retrieval) requires three things this package cannot include: ① Google Chrome installed, ② a Chrome DevTools MCP connected in your host (config template: `skills/cnki-deepsearch/Google Chrome MCP Config.md`), ③ your own CNKI account login. **Missing any of them does not block the pipeline** — StellarTrack auto-falls back to a disclosed mode: you paste CNKI records/PDFs, or it uses WebSearch labeled `degraded retrieval · source X`. Configure all three and the native CNKI channel activates automatically.

- When the progress bar shows `[⏸]`, come back and decide — your call unlocks the next step;
- A rejection isn't a malfunction; it's the gate working;
- External accounts (CNKI etc.) are bring-your-own; passwords and tokens never enter the repo;
- If you find any personal-data residue, please open an Issue — handled immediately.
- Some binary assets (images, Office docs, PDFs, fonts) are not bundled because the platform restricts bundled file types — see `MISSING-ASSETS.md` for the full list and why nothing functional is blocked.

**Roadmap**: first external user case study → English docs → contribution guide.

## Environment-Bound Components (not distributable)

| Component | Note |
|---|---|
| C1–C2 CNKI channels (topic + retrieval) | Protocol lives in `skills/xingchan/references/学术档工作流.md`; needs Chrome DevTools MCP + your own CNKI session. Without it, the pipeline auto-degrades to a disclosed fallback (pasted records / labeled WebSearch) — it never silently fakes CNKI |
| C6 tencent-docx typesetting | WorkBuddy built-in plugin; substitute your platform's docx exporter |
| Gongwen fonts | `gongwen-draft/assets/fonts/` excluded for font licensing; install 仿宋_GB2312 / 方正小标宋 yourself |

Private runtime data (preference profiles, traces, calibration ledgers) is not included.

## License & Provenance

See [NOTICE.md](NOTICE.md). Components are listed per-item as original vs third-party-pending-verification; check licenses before using third-party items.

## License

MIT © 2026 Ruojun（duzhihan）
