# C 环节 skill 注册表

> 建立：2026-08-23（用户批准接口审计提案④⑤提前落刀）｜三库归属：T 工具箱的装配账本
> 作用：把散落在各工序条款的引擎引用收拢一表——工序开工查指令包→指令包查本表→本表定引擎。**子类目=工序×档位矩阵单元格**，新场景=新单元格，不新造工序。

**三本台账各管一段（2026-10-26 定 · 防“一物两处记状态”）**

| 台账 | 管什么 | 唯一权威字段 |
|---|---|---|
| `data/skill-tracker.md` | 候选池**权威**（开发者／许可／版本 pin／活跃度／实用证据） | 候选的原始事实 |
| `references/T工具箱_待加载清单.md` | 候选池**投影**（候选语义＋对照结论）；转正后从待载区移入其“已转正台账”留痕 | 无（投影） |
| **本表** | **已装引擎的工序位**（默认引擎／试挂位／休眠区） | 引擎落点与形态（甲/乙/丙） |

**判读规则**：某引擎“是否已装”只看本表；“是否值得装”只看台账；“待载区仍列某引擎”不等于它没转正——须回本表核对。

## 三步嫁接环（工具自动增加机制）

1. **缺口探测（自动）**：引擎不可用/不适配 → 记一行入 `data/graft-log.md`；同单元格第 2 次命中 → 自动触发候选搜寻
2. **试挂（半自动）**：候选过安全审计 → 以〔试挂〕进本表试挂位，实战一稿；试挂不改正文条款
3. **转正（人裁）**：实战通过 → 走 T 准入四步（登记→审计→归属→用户裁决）→ 试挂位转默认引擎；不通过 → 移除＋驳回原因入决策流水

**调优**：引擎实战纠偏 ≥3 分（加权制）→ 改调用参数/人设，登记变更史；连续 3 稿零调用 → 移入休眠区不删除。

## 注册总表

| 工序 | 档位 | 默认引擎 | 试挂位 |
|---|---|---|---|
| C2 检索 | 学术 | cnki-deepsearch／知网检索底座（kns8s） | — |
| C1 选题 | 学术 | **双轨**：轨A 研学智得全流程（机构会员）；轨B 研究态势免费＋本地替代（方法卡05 生成→方法卡17 路由→方法卡18 契约卡）。知网选题通道 x.cnki.net 四环节（研究态势→选题推荐→定题评测→标题打磨，浏览器自动化优先，不可用降级本地化）；**research-ideation（乙型 · 转正 2026-10-16 · MIT · 安装位 `<技能根>/research-ideation/` · 来源 Galaxy-Dawn/claude-scholar 454★）**：5W1H 头脑风暴＋五类 Gap＋SMART 问题公式化＋RQ Card（假设/证据/证伪）＋Proposal Readiness Gate——挂 C1 ②⑤，先契约后表达，与 title-assessor 分工 | — |
| C3 综述 | 学术 | literature-review-writer 综述引擎（**综述引擎 v2.2.0 · 自研 · 已安装三处齐备（v12.6.3 安装补齐）：作者技能根＋运行时技能根＋发布包 mirror**；综述材料来源纪律常态保留——承重命题须 C2 A-LIT 账本 asset_id 可回查，禁网上资料直接成文，产物头部声明材料基线） | — |
| C3 模型图 | 学术 | paper-mechanigraph-4ss | — |
| C3 故事主线／C4 叙事线复核 | 学术 | good-story（C3：2-4 条脊线→用户择优；C4：中心贡献一句话测试／证据阶梯／主张边界） | — |
| C4 标题 | 学术 | title-assessor | — |
| C6 文风 | 学术 | writing-dna-skill（三选一：现场蒸馏／龙王档案／现成档案） | — |
| C8 定稿转换 | 全档位 | tencent-docx 线（**仅用户当轮点名时启用，默认不产 Word**） | — |
| C7 去AI化 | 全档位 | humanizer-zh → lieflat-less-ai-tone（冲突以蒸馏产物优先） | chinese-de-aigc（第三候选降级） |
| **C2/C7/C9 确定性机检辅助** | 学术 | **humanities-tools（甲型 · 转正 2026-10-15 · MIT · 安装位 `<技能根>/humanities-tools/`）**：`review.py` 21 条确定性文本评估（正则＋术语表，不依赖模型自评；R1 模糊引用/R3 过度断言/T 术语漂移/F 格式/S 语体/L 论证逻辑/ST 结构；`python review.py 稿件.md --format json`）＋`search.py` 英文文献搜索（OpenAlex/Semantic Scholar/CORE/CrossRef 免费 API，密钥走环境变量）＋350+ 术语对照表（terminology-bilingual.md，19 学科，供方法卡07 术语表工程取例） | — |
| C8 引用 | 学术 | citation-format＋gbt7714-format | — |
| C9 评审 | 学术 | academic-paper-reviewer 五席（full/quick/re-review/Socratic/calibration 六模式） | — |
| C10 修改 | 学术 | paper-editor 六模式＋evidence-bound-revision＋nsfc-review-guide（对照标尺） | — |
| **C6/C7/C9/C10 英文轨** | 学术 | **nature-skills 六件（乙型/甲型混合 · 转正 2026-10-15 · Apache-2.0 · 安全审计 P0=0）：polishing（C6/C7/C10 润色翻译）＋writing（C6 起草）＋reviewer（C9 评审）＋response（C10 回复）＋data（C8 数据声明）＋shared（共享依赖）**；安装位 `<技能根>/nature-skills/skills/`；触发=Nature 系目标刊或点名“Nature 风格”；乙型流程到守门点必须停下交验 | — |
| C11 摘要 | 学术 | abstract-checker（甲型对照工具；2026-08-26 补建实体——五维对照：主张回溯/数字口径/夸大措辞/四要素/体例；安装位 ~/.workbuddy/skills/abstract-checker/） | — |
| C2-C6 传播 | 传播 | 传播叙事引擎 narrative-suite（指令包主体·乙型） | — |
| C2 备料 | 传播 | wechat-article-search／douyin_copy_extract（素材采集） | — |
| C3 立骨 | 传播 | narrative-social（钩子—主体—收束结构） | — |
| C5 填充 | 传播 | 〔已休眠〕ljg-writes／khazix-writer（见休眠区） | human-writing |
| C6 文风 | 传播 | wenfeng-slime＋DNA 库 A 层 | — |
| C7 去AI化 | 传播 | oh-story 多视角去味（甲型） | — |
| C9 会审 | 传播 | 自读三遍·模拟读者（人工工序，无引擎） | — |
| C11 外延 | 传播 | ljg-card／ljg-present／lieflat-charts（丙型独立成品，点名直用） | — |
| C4/C10 可视化审稿 | 全档位 | human-review v0.6.1（丙型·浏览器改稿＋批注锚定＋JSON 批量回传；2026-08-24 安全审计＋全链路实测通过，用户裁决转正；安装位 ~/.workbuddy/skills/human-review/） | — |
| **O1／S／C 全道** | 全档位 | **thinking-protocols 认知演进器**（**C1／C4／C9 三道 🔴 强制在场**，其余各道随叫随到；O1 轻助产＋S 层完整六环挂载；人机分工铁律：能辅助的辅助，思考决策不能代；**未挂载须显式声明**，见 SKILL.md §〇 契约 3） | — |
| C1-C6 规范 | 规范 | gongwen-draft（指令包主体·乙型；述职/党建/通知/声明四场景并入） | — |
| C1-C6 教学 | 教学 | 〔占位·档位已补全〕引擎待首稿实测后经嫁接环补齐（档位工作流见 `references/教学档工作流.md`；守门中强度·教学四检） | — |
| C1-C6 申报 | 申报 | 申报指令包（乙型；安装名 6 件：nssfc-topic-to-idea→nssfc-idea-to-perspective→nssfc-literature-to-design→nssfc-perspective-to-literature→nssfc-proposal-writing→nssfc-writing-polish） | — |
| C2 解析 | 规范档素材源 | 规范档解析（微信稿预处理＋会议通知/征稿要素抽取：会议名/截稿日/议题/邮箱/主办方偏好；W6 落刀 2026-08-23，回应实测断点 W6） | — |
| C1-C6 创作·小说 | 创作·小说 | chinese-novelist-dragon（指令包主体·乙型；七 Phase ↔ 星躔工序映射见 references/创作档_小说子类.md） | — |
| **C1 理论转化／C2 材料设计／C5 数据与编码／C8 可复现交付／C10 稳健性／C11 证据核对** | 学术·**实证轨** | 〔试挂〕`sociology-research-methods` v0.1.0（26 法／7 域；装于 `~/.workbuddy/skills/sociology-research-methods/`；2026-09-14 安全审计通过 P0=0／P1=0） | 待实战一稿后转正 |
| **C1/C11 英译辅助＋全稿中译英** | 学术·**翻译装载** | 〔转正〕`paper-cn-to-en` v1.0（乙型·全稿中译英指令包＋甲型·C1/C11 题目摘要关键词英译辅助；wave2234/paper-cn-to-en · MIT；2026-10-15 用户拍板配置入系统；术语表/词数预算见方法卡07/08，装载细则见 `references/学术档工作流.md`“学术·翻译装载”节） | — |

| **C1／C2／C4／C6／C8／C9 创作·歌词** | 创作·**歌词** | **lyrics-writing（乙型 · 转正 2026-10-26 · 自建蒸馏件）**：十三辙韵表＋情感匹配、句式／段式／曲式与建构组织十一法、十六种修辞、歌名与词眼、写作流程与填词四步、成稿七查、评审模式六层、反模式清单；安装位 `references/engines/lyrics-writing/`（12 件 · 84 KB · 纯 Markdown）；工序映射见 `references/创作档_歌词子类.md` §〇 | — |

**嵌入三型法指针**：已装固定流程 skill 入表前先判型——盖一格＝甲（单工序引擎），盖一排＝乙（档位指令包主体，到守门点必须停），不进楼＝丙（外延可选项）。详见《C环节母版适配_工序动词表与守门分级.md》第三节。

**实证轨挂载条件（2026-09-14 立 · `sociology-research-methods`）**：本引擎为**条件引擎，非默认常挂**——三问判据（① 本研究是否自行产生一手经验材料 ② 交付物是否含需识别策略或统计推断的主张 ③ 是否需要可复现交付）**全为“是”方挂**；**用户铁律“理论分析型论文只用文献／案例／公开数据，禁用访谈与问卷”优先级高于本表**，三项有任一为“否”即不挂。其 3 件与星躔既有引擎重叠项（`literature-review-writing`／`scientific-writing-guide`／`systematic-review-guide`）**已降为参照，不占工序引擎位**。**发布纪律**：该包为混合许可（20 件 MIT·Wentor AI ＋ 7 件自建无明示许可），**整体禁入 StellarTrack 发布派生物**。

## 休眠区

- **ljg-writes／khazix-writer**（C5 填充 · 传播）：2026-10-26 移入。理由——传播档工序路径为 C2→C4→C6，**无 C5 填充工序**，引擎在档位内零落点（挂而不用）。恢复条件：传播档新增 C5 工序，或长文写作确需分两段填充时，经嫁接环试挂一稿后转正。
- （其余空——连续 3 稿零调用的引擎移入此处）
