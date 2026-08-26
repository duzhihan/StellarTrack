---
name: oh-story-deslop
description: ［oh-story·去AI味］oh-story-claudecode的去AI味引擎——词汇层+句法层+结构层三重过滤。作为07-去AI味L1的第四引擎。
version: 1.0.0
disable: true
---

# Story Deslop | 去AI味 (oh-story增强版)

## 核心规则（来自 oh-story-claudecode story-deslop）

### 词汇层
- 禁用AI高频形容词："璀璨"、"瑰丽"、"深邃"、"复杂"（作万能修饰时）
- 禁用AI高频副词："缓缓"、"微微"、"隐隐"、"莫名"
- 禁用万能量词："一股"、"一抹"、"一丝"
- 禁用情绪标签："心中一惊"、"心中一喜"、"心中涌起"

### 句法层
- 禁用"不仅……而且……"句式（AI最爱）
- 禁用"或许……也许……可能……"三重不确定
- 禁用"仿佛"、"宛如"、"如同"连续使用
- 禁用"在……之中"、"在……之下"句式

### 结构层
- 禁用"随着……"开段
- 禁用"然而"、"不过"、"与此同时"连续3段开头
- 禁用"综上所述"、"总而言之"结尾
- 禁用"这便是"、"这便是为什么"解释性结尾

## 集成位置
07-去AI味 L1 词汇层 → 第四引擎（排在 avoid-ai-writing / shuorenhua / ai-speech-detector 之后）

## 执行
L1四引擎按顺序执行：avoid-ai-writing → shuorenhua → ai-speech-detector → **story-deslop**
