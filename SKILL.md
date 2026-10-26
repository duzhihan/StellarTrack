---
name: StellarTrack 星躔
description: 杜智瀚老师的跨场景写作与知识管理系统“星躔”（StellarTrack）。覆盖学术论证、课题申报、公文党建、媒体传播、结题回溯、演讲口播、文学创作的六类文体，内置 O-S-C-E 四层架构、C1–C11 认知建构流水线、心月狐思考决策引擎、七库知识沉淀与女娲思维蒸馏流水线。安装后在 WorkBuddy 中获得 O-S-C-E 写作工作流与 66 个配套技能；其中 C3–C11 开箱即跑，C1–C2 知网自动化需额外前置（见“前置依赖”）。
version: 12.5.21
---

# StellarTrack 星躔

杜智瀚老师的跨场景写作系统“星躔”（StellarTrack）的完整安装包。它不是单个技能，而是一套可插接的写作与知识管理基础设施：从一次选题到最终精校，从文献检索到对外传播，全部工序都已固化为可调用的工作流。

## 一句话定位

把“写什么、怎么想、怎么写、怎么沉淀”四件事，变成一条在 WorkBuddy 里跑得通的生产线。

## 前置依赖（第三方安装必读）

本安装包装的是“给 AI 的工作流指令 + 66 个配套技能”，**不是自带知网账号的闭源软件**。请按自己要用的环节确认前置：

- **C3–C11（综述／大纲／撰写／出图／改稿／格式／评审）**：开箱即跑。这些环节依赖已打包的技能（离朱、paper-mechanigraph-4ss、good-story、docx 等）与宿主 AI 本身，无需额外配置。
- **C1 选题 / C2 检索的“知网原生自动化”**：需要三项外部条件，**本包不内含、也无法替你配置**：
  1. 本机已安装 Google Chrome；
  2. 宿主已接入“Chrome DevTools MCP”（如 `chrome-devtools-mcp@latest`）并信任重载——配置模板见 `skills/cnki-deepsearch/Google Chrome MCP Config.md`；
  3. 你本人的知网账号登录态（cookie）。
  - **缺任何一项时系统不会卡死**：会自动转“合法降级”——你粘贴知网题录/PDF，或走 WebSearch 学术检索，并在产出标注“降级检索·来源X”。配置好上述三项后，原生知网通道即自动启用。
- **K 库 LLM-Wiki 语义挂载**：可选，依赖你本机 :19828 服务；缺省不影响主线，按 K 铁律退回 keyword 检索。

> 一句话：装完就能写（C3–C11）；要用“知网自动搜”得先接 Chrome MCP + 登知网，否则系统会带标注地降级跑，绝不静默假装用了知网。

## 四层架构（O-S-C-E）

- **O 目标定向**：场景识别与锚定，≤2 轮对话锁定写作场景与读者、目标、文体。
- **S 思考决策**：任务级一次全心月狐（S-layer 思考引擎），产出论证锚定卡与结果稿，含视角银行、模式库、偏好回显。
- **C 认知建构**：C1 选题 → C2 材料建档 → C3 综述·模型·引言 → C4 大纲协商 → C5 血脉填充 → C6 正式撰写 → C7 净化 → C8 格式校验与合卷 → C9 初稿联合评审 → C10 改论文 → C11 最终精校。
- **E 经验共创**：E1 反思对齐、E2 发布复盘、E3 外部反馈环，含置信加权与校准台账。

## 六档位

| 档位 | 核心动作 | 范式 | 典型产出 |
| --- | --- | --- | --- |
| 学术档 | 论证 | 学术期刊 | 论文 |
| 申报档 | 说服 | 评审系统 | 活页标书 |
| 传播档 | 传播说服 | 大众媒体 | 公众号评论 |
| 规范档 | 传达记录 | 政府公文 | 公文党建 |
| 回溯档 | 记录 | 管理部门 | 结题调研 |
| 演讲档 | 传播+现场 | 讲话稿口播 | 演讲稿 |
| 创作档 | 母版壳 | 文学场域 | 诗歌小说散文剧本歌词 |

（创作档为母版壳，与文体无关的流水线可换装载而不换骨架。）

## 关键能力

- **心月狐（S 层）**：苏格拉底式助产对话，全环节追问化，不确定时明示不确定。
- **七库 + M-K-T 三层能力**：方法库（怎么写）、知识库（关联检索）、工具箱（规范/申报/创作/学术各档指令包）。
- **女娲思维蒸馏**：把人物/作者的思维模型蒸馏成可运行的方法卡，八字段登记入册。
- **知网原生通道**：选题走知网官方前端，检索走合规路线，LLM 只负责写作与叙事。
- **哲学观基座**：以关系优先于实体、技术被资本决定且持续被协商为底层立场，让 AI 充当工具与对手功能而非代脑。

## 内含技能（66 个）

学术写作与评审（xingchan、abstract-checker、academic-paper-reviewer、citation-format、claim-audit、duzhihan-paper-editor、evidence-bound-revision、journal-fit、literature-review-writer、manuscript-review、reference-check、research-design、theoretical-framework、title-assessor、paper-mechanigraph-4ss、writing-dna-skill、lieflat-less-ai-tone）；课题申报（nssfc-* 系列、nsfc-review-guide）；公文党建（gongwen-draft）；叙事与传播（narrative-* 系列、human-writing、human-review、khazix-writer、good-story、wechat-article-search、douyin-copy-extract、lieflat-charts）；认知与工具（thinking-protocols、ljg-*、oh-story、wenfeng-slime、cnki-deepsearch）；创作辅助（gushi-namer·古诗文起名，创作档·起名子类 T 层挂载）。详见各 `skills/<name>/SKILL.md` 与根目录 `README.zh-CN.md`。

## 使用说明

1. 在 WorkBuddy 中加载本技能后，从“学术档 / 申报档 / 传播档 / 规范档 / 回溯档 / 演讲档 / 创作档”任一档位入口发起任务。
2. 系统按 O-S-C-E 四层依次推进；每个守门点会停下交验，确认后再继续。
3. 需要蒸馏新作者思维或扩充方法库时，走女娲（nuwa）流程。

## 许可与署名

完整许可与第三方组件声明见 `NOTICE.md`，作者杜智瀚（暗黑无敌龙王）。本安装包与其余技能遵循各自目录内的许可条款。
