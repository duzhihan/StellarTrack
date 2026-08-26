# C 环节 skill 注册表

> 建立：2026-08-23（殿下批准接口审计提案④⑤提前落刀）｜三库归属：T 工具箱的装配账本
> 作用：把散落在各工序条款的引擎引用收拢一表——工序开工查指令包→指令包查本表→本表定引擎。**子类目=工序×档位矩阵单元格**，新场景=新单元格，不新造工序。

## 三步嫁接环（工具自动增加机制）

1. **缺口探测（自动）**：引擎不可用/不适配 → 记一行入 `data/graft-log.md`；同单元格第 2 次命中 → 自动触发候选搜寻
2. **试挂（半自动）**：候选过安全审计 → 以〔试挂〕进本表试挂位，实战一稿；试挂不改正文条款
3. **转正（人裁）**：实战通过 → 走 T 准入四步（登记→审计→归属→殿下裁决）→ 试挂位转默认引擎；不通过 → 移除＋驳回原因入决策流水

**调优**：引擎实战纠偏 ≥3 分（加权制）→ 改调用参数/人设，登记变更史；连续 3 稿零调用 → 移入休眠区不删除。

## 注册总表

| 工序 | 档位 | 默认引擎 | 试挂位 |
|---|---|---|---|
| C2 检索 | 学术 | cnki-deepsearch／知网检索底座（kns8s） | — |
| C2 选题 | 学术 | 知网选题通道（x.cnki.net） | — |
| C3 综述 | 学术 | 离朱 literature-review-writer | — |
| C3 模型图 | 学术 | paper-mechanigraph-4ss | — |
| C3 故事主线 | 学术 | good-story | — |
| C4 标题 | 学术 | title-assessor | — |
| C6 文风 | 学术 | writing-dna-skill（三选一：现场蒸馏／龙王档案／现成档案） | — |
| C6 排版 | 全档位 | tencent-docx 线（仅 C8 终转 Word 一次） | — |
| C7 去AI化 | 全档位 | humanizer-zh → lieflat-less-ai-tone（冲突以蒸馏产物优先） | chinese-de-aigc（第三候选降级） |
| C8 引用 | 学术 | citation-format＋gbt7714-format | — |
| C9 评审 | 学术 | academic-paper-reviewer 五席（full/quick/re-review/Socratic/calibration 六模式） | — |
| C10 修改 | 学术 | duzhihan-paper-editor 六模式＋evidence-bound-revision＋nsfc-review-guide（对照标尺） | — |
| C11 摘要 | 学术 | abstract-checker（甲型对照工具；2026-08-26 补建实体——五维对照：主张回溯/数字口径/夸大措辞/四要素/体例；安装位 ~/.workbuddy/skills/abstract-checker/） | — |
| C2-C6 传播 | 传播 | 雕龙 narrative-suite（指令包主体·乙型） | — |
| C2 备料 | 传播 | wechat-article-search／douyin_copy_extract（素材采集） | — |
| C3 立骨 | 传播 | narrative-social（钩子—主体—收束结构） | — |
| C5 填充 | 传播 | ljg-writes／khazix-writer（按体量选） | human-writing |
| C6 文风 | 传播 | wenfeng-slime＋DNA 库 A 层 | — |
| C7 去AI化 | 传播 | oh-story 多视角去味（甲型） | — |
| C9 会审 | 传播 | 自读三遍·模拟读者（人工工序，无引擎） | — |
| C11 外延 | 传播 | ljg-card／ljg-present／lieflat-charts（丙型独立成品，点名直用） | — |
| C4/C10 可视化审稿 | 全档位 | human-review v0.6.1（丙型·浏览器改稿＋批注锚定＋JSON 批量回传；2026-08-24 安全审计＋全链路实测通过，用户裁决转正；安装位 ~/.workbuddy/skills/human-review/） | — |
| C1-C6 规范 | 规范 | gongwen-draft（指令包主体·乙型；述职/党建/通知/声明四场景并入） | — |
| C1-C6 教学 | 教学 | 〔占位〕引擎待首稿实测后经嫁接环补齐 | — |
| C1-C6 申报 | 申报 | nssfc（指令包主体·乙型） | — |
| C2 解析 | 规范档素材源 | 规范档解析（微信稿预处理＋会议通知/征稿要素抽取：会议名/截稿日/议题/邮箱/主办方偏好；W6 落刀 2026-08-23，回应实测断点 W6） | — |

**嵌入三型法指针**：已装固定流程 skill 入表前先判型——盖一格＝甲（单工序引擎），盖一排＝乙（档位指令包主体，到守门点必须停），不进楼＝丙（外延可选项）。详见《C环节母版适配_工序动词表与守门分级.md》第三节。

## 休眠区

（空——连续 3 稿零调用的引擎移入此处）
