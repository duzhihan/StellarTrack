---
name: oh-story-review
description: ［oh-story·多视角审查］7个专业Agent从不同视角审查章节质量：架构师/角色设计师/叙事作家/一致性检查员/研究者/探索者/提取器
version: 1.0.0
disable: true
---

# Story Review | 7Agent多视角审查

## 7个审查Agent

| Agent | 审查视角 | 核心问题 |
|------|------|------|
| **story-architect** (架构师) | 故事结构 | 大纲是否被执行？章节在整体中的位置是否正确？ |
| **character-designer** (角色设计师) | 人物一致性 | 角色的性格/语言/行为是否符合设定？ |
| **narrative-writer** (叙事作家) | 文笔质量 | 描写是否生动？节奏是否恰当？去AI味是否到位？ |
| **consistency-checker** (一致性检查员) | 前后矛盾 | 伏笔是否回收？角色状态是否矛盾？世界观是否冲突？ |
| **story-researcher** (研究者) | 事实准确性 | 引用的知识/数据/历史是否准确？ |
| **story-explorer** (探索者) | 读者体验 | 如果我是第一次读的读者，这章吸引人吗？ |
| **chapter-extractor** (提取器) | 信息密度 | 本章的有效信息量？有无灌水？ |

## 集成位置
06-审稿 Phase 4 → 在47+10+8维之后，追加7个Agent审查维度。

## 输出
```
[7Agent 多视角审查]
story-architect: ✅/⚠️ {comments}
character-designer: ✅/⚠️ {comments}
narrative-writer: ✅/⚠️ {comments}
consistency-checker: ✅/⚠️ {comments}
story-researcher: ✅/⚠️ {comments}
story-explorer: ✅/⚠️ {comments}
chapter-extractor: ✅/⚠️ {comments}
```
