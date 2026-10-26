# StellarTrack

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/hero.svg" alt="StellarTrack" width="100%"/>
</p>

<p align="center">
  <b>Give the model a writing process, not a wish.</b><br/>
  <sub>A writing pipeline with gates: the AI does the labor, you sign off at every checkpoint.</sub>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"/></a>
  <img src="https://img.shields.io/badge/version-v12.6.14-blue.svg" alt="version"/>
  <img src="https://img.shields.io/badge/Agent%20Skill-Claude%20Code%20%7C%20WorkBuddy-2f6feb.svg" alt="Agent Skill"/>
  <img src="https://img.shields.io/badge/lang-English%20%7C%20%E4%B8%AD%E6%96%87-informational.svg" alt="lang"/>
</p>

<p align="center">
  <b>English</b> ｜ <a href="README.zh-CN.md">简体中文</a>
</p>

---

## What usually goes wrong

- You ask a model to “write my paper”. Ten seconds later you have something that *looks* like a paper — and you don't dare submit it, because it never walked through your reasoning.
- You ask for a revision; by round three it has forgotten what you locked in earlier and drifts further away.
- You finish and can't tell: are the citations real? Does the abstract match the body? Is this actually submittable?

The bottleneck is not text generation. **It is process.**

## How it works

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/overview.svg" alt="O-S-C-E pipeline" width="100%"/>
</p>

Four movements: **orient, commit, construct, accumulate.**

Lock what this piece is actually arguing before a single sentence is written. Anchor the core claim to a falsifiable test. Then construct in eleven stages — topic, materials, literature, outline, drafting, writing, de-AI cleanup, format check, panel review, revision, final polish.

**Every stage ends with a gate.** Miss the criteria and you go back; “just keep writing” is not an option. That is the single biggest difference from prompting a model directly: **it will not let you skip steps.**

## What it writes

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/tracks.svg" alt="13 tracks" width="100%"/>
</p>

Thirteen tracks share one skeleton — **swap the payload, never the pipeline**.

An academic paper needs evidence and citation discipline; a public article needs a hook; fiction needs scene and rhythm. The skeleton holds; the weights and execution change. You don't relearn a new tool per genre.

## Why you can trust the verdict

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/scoring.svg" alt="six-dimension rubric" width="100%"/>
</p>

One ruler only: six fixed-weight dimensions scored on a 1/3/5/7/9 anchor scale, with 7 as the pass line. Two reviewers score blind and independently; disagreement beyond a threshold triggers a reconciliation pass.

There are also hard caps — fake citations, load-bearing numbers with no source, praise-only reviews. Hit one and the score is capped, no matter how polished the prose looks.

## Three libraries feed it

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/libraries.svg" alt="three libraries" width="100%"/>
</p>

Nothing is invented from thin air. Every stage pulls from a library first: methods give the playbook, knowledge gives the material, tools give the engine. **If an engine is unavailable it degrades — and must say so.** Pretending to call one is a gate failure.

## Scale and self-check

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/stats.svg" alt="scale" width="100%"/>
</p>

69 skills, 13 tracks, 11 stages, 29 engine slots. The system ships with its own audit: version consistency, quote compliance, resolvable references, structural completeness, semantic contradictions. **If the audit doesn't pass, the change isn't done.**

## Get started in three steps

**1. Clone**

```bash
git clone https://github.com/duzhihan/StellarTrack.git
```

**2. Drop it into your agent's skill directory**

```bash
cp -r StellarTrack/skills/xingchan ~/.workbuddy/skills/
```

**3. Ask in plain language**

```
Write a paper on opera dissemination on short-video platforms.
```

It asks a few questions first (target journal, the claim you want, what materials exist), then walks C1 onward, pausing at each gate for your sign-off. It will not dump a finished draft on you in one shot.

> Want a dry run? Ask it to “stress-test this topic” — that mode reasons only, and writes nothing.

## What you get

- An artefact per stage: topic card, material ledger, outline, review checklist, revision log.
- Everything in Markdown: version-controllable, pasteable into Word, emailable to your supervisor.
- Progress survives interruption: state is written to disk, so a new session can pick up where you left off.

## FAQ

**Will it write the paper for me?**
It absorbs the repetitive labor. **The judgement stays yours** — topic choice, core claim, whether to submit. It offers candidates and reasons, never the final call.

**Do I need API keys?**
Not for the core pipeline. Some optional engines (literature search, semantic retrieval) need your own credentials; without them it degrades and tells you.

**Does it work in Chinese?**
It was built for Chinese humanities and social science writing: terminology, citation format, and journal conventions are Chinese-first.

**Why Markdown by default?**
Because most Word formatting is wasted effort. Ask explicitly and it will convert.

## Honest limits

- **No external user validation yet.** This is one person's system, tested on real manuscripts, without community-scale feedback — that is item one on the roadmap.
- It stops you from skipping steps and from faking citations. It cannot stop a topic that wasn't worth writing.
- The rubric is calibrated, but on the author's own manuscripts, not on a third-party blind set.

## License

MIT — commercial use, modification, and redistribution permitted. Per-item provenance and licensing: see [NOTICE.md](NOTICE.md).
