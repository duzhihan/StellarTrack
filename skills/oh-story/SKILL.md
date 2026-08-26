---
name: oh-story
description: ［oh-story-claudecode 精简版］来自 worldwonderer/oh-story-claudecode
  (2,148★,
  MIT)。仅取4个不冲突模块：story-import(导入续写)、story-deslop(去AI味增强)、story-review(7Agent审查)、story-cover(封面)。不取扫榜/拆文/写作等已由chinese-novelist覆盖的模块。
source: worldwonderer/oh-story-claudecode (MIT)
version: 1.0.0-selective
disable-model-invocation: true
---

# oh-story · Selective Integration

本Skill是 oh-story-claudecode 的选择性集成。原项目13个sub-skill，我们取4个与现有系统无冲突的模块。

## 取舍清单

| 模块 | 决策 | 原因 |
|------|:--:|------|
| story-setup | ❌ | Phase 0 已覆盖 |
| story-long-scan/short-scan | ❌ | 01-扫榜 已覆盖 |
| story-long-analyze/short-analyze | ❌ | 02-拆文 已覆盖 |
| story-long-write/short-write | ❌ | chinese-novelist Phase 3 已覆盖 |
| **story-import** | ✅ | **独有能力**：导入已有作品，自动重建结构化状态 |
| **story-deslop** | ✅ | **增强L1**：去AI味规则比我们的更细粒 |
| **story-review** | ✅ | **增强审稿**：7个Agent多视角审查 |
| **story-cover** | ✅ | **增强封面**：网文封面提示词库 |
| browser-cdp | ⚠️ | 保留备用 |

## 子模块

| 模块 | 路径 | 功能 | 调用者 |
|------|------|------|------|
| story-import | `skills/story-import/SKILL.md` | 导入已有小说→重建状态→续写 | Phase 0 新增选项 |
| story-deslop | `skills/story-deslop/SKILL.md` | 去AI味规则(词汇+句法+结构) | 07-去AI味 L1 第四引擎 |
| story-review | `skills/story-review/SKILL.md` | 7Agent多视角审查 | 06-审稿 追加维度 |
| story-cover | `skills/story-cover/SKILL.md` | 网文封面提示词库 | 08-封面 增强 |
