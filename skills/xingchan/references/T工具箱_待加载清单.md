# T 工具箱 · 待加载清单

> 性质：候选工具登记册——**只登记不安装**。每条须过《MKT库管理规范.md》T 库准入流程（安全审计→档位归属→用户裁决）方可转正。
> **投影说明（v12.6.1）**：本清单为外部 skill 台账 `data/skill-tracker.md` 的**候选池投影**（台账 C 组）——权威字段（开发者/许可/版本 pin/活跃度/实用证据）以台账为准，本清单只保留候选语义与对照结论；新增候选一律先登记台账。
> 登记日期：2026-08-23 ｜ 登记人：星躔维护者

## 待载-01 water-koubo（短视频爆款口播二创 Skill）

- **来源**：老肖·肖Sensei 公众号（2026-08-21），https://mp.weixin.qq.com/s/XeBCHGEylRLoUTzY_YeUtw
- **开源地址**：https://github.com/waterbrojx/water-koubo（v1.0.0，2026-08-18 开源）
- **功能**：输入一篇完整参考稿 → 拆解爆款写法（观点/结构/案例/爆点/结尾）→ 重写为可拍口播稿＋标题＋封面文字；五步法（参考稿→找写法→重创作→核归属→成稿）
- **许可**：CC BY-NC 4.0（非商用免费；商用需作者授权，微信 Waterbro_jx）
- **自述边界**：不联网、不调外部服务器、不索取 API Key、不遥测（安装前仍须走安全审计实测）
- **预判归属**：传播档（口播/短视频二创）——与演讲档口播场景近缘，与传播叙事引擎可互补
- **风险点**：二创归属校准是其卖点，但“参考稿→重写”管线与作者反搬运红线需对表；NC 许可对非商业场景（公众号/口播非商业）暂不冲突

## 待载-02 学术科研写作八大 Skill 清单（淘项有术）

- **来源**：淘项有术社区公众号（2026-08-07），https://mp.weixin.qq.com/s/yZ7ZSHinWSkpt-xwOuIxTg
- **内容**：约 20 个学术写作 skill 的清单文（文献调研/正文撰写/润色去AI/图表/查重合规/投稿答辩/格式/翻译八类）
- **许可**：未标注，各仓库需逐一核查
- **与星躔已有资产对照预判**（逐项判定按四级：已有互证/可补/转译/不入）：

| 清单项 | 预判 | 说明 |
|---|---|---|
| literature-summary-skill | 已有互证 | 星躔 C2 文献条目三字段＋篇级时间盒已覆盖同类功能 |
| literature-gap-miner | 已有互证 | C3 缺口卡三条件＋缺口公式已覆盖 |
| citation-formatter-pro | 可补候选 | gbt7714-format 已有；若需多格式切换（APA/MLA）可评估 |
| thesis-outline-builder / research-intro-writer | 已有互证 | C4 大纲协商＋引言五阶段法方法卡已覆盖 |
| academic-humanizer-zh/en | 已有互证 | humanizer-zh＋lieflat-less-ai-tone 双检已在 C7 |
| paraphrase-academic | 可补候选 | 降重改写——但 C7 查重走官方 AMLC，自建降重与既有裁决（不开发自建查重）需对表 |
| academic-fact-verifier | 可补候选 | claim-audit 已覆盖回源核验，重叠度高 |
| response-to-reviewer | **可补** | C10 改论文缺“审稿回复信”产物模板，唯一明确缺口 |
| cover-letter-generator | 可补候选 | C8 投稿配套文书，星躔现无此产物 |
| 其余（答辩PPT/格式检查/翻译等） | 暂不入 | 与学术档主场景（期刊论文）错位 |

- **风险点**：清单文为推荐性质，未附各仓库地址与许可；转正前须逐个找到原始仓库＋安全审计

## 已转正台账

| 工具 | 转正日期 | 结果 |
|---|---|---|
| human-review v0.6.1 | 2026-08-24 | 安全审计（零遥测零外传）＋全链路实测（MD 渲染/直接改字/before-after 锚定 JSON 回传 38s）双过，用户裁决“可行则转正”→ 已装 `~/.workbuddy/skills/human-review/`，入注册表 C4/C10 可视化审稿（丙型） |
| nature-skills 六件（polishing/writing/reviewer/response/data/shared） | 2026-10-15 | 安全审计 P0=0（零网络面零密钥，纯规则文档型；scripts 全为开发校验脚本）→ 用户“同意，执行吧”照准 → 已装 `<技能根>/nature-skills/skills/`（保留 nature-shared 同级），入注册表学术英文轨（乙型/甲型混合），学术档翻译装载增场景三；figure/academic-search 等其余 17 件归外延可选；**本机（WorkBuddy）2026-10-17 重取 GitHub 快照安装**（`main`，六件 205 文件／733 KB，`LICENSE` Apache-2.0 随附），本次新建聚合路由壳 `nature-skills/SKILL.md`（含乙型守门停顿条款与四件边界裁定）；**2026-10-17 外延 17 件已启用**（用户指令“启用”），壳升 v0.2.0 共 23 件，补入检索获取／阅读解析／核验／产出转换／分析审查五组路由、PaddleOCR 云端 OCR 红线、缺图说明与七条防撞车裁定 |
| humanities-tools（review.py＋search.py＋术语表） | 2026-10-15 | 安全审计 P0=0（review.py 纯本地标准库零网络零密钥；search.py 密钥全走环境变量；cnki/wanfang/google_scholar 源需用户自持凭据，无凭据自动跳过）＋实测（构造样例 13 处违规全部命中）→ 用户”同意，继续”照准 → 已装 `<技能根>/humanities-tools/`，入注册表 C2/C7/C9 确定性机检辅助（甲型）；**本机 2026-10-17 重取安装**（`ganzhi-black/humanities-thesis-skill` 39 文件／238 KB），frontmatter `name` 由 `humanities-thesis` 对齐为 `humanities-tools`（使名与安装位一致，防加载唤不起） |
| **research-ideation**（claude-scholar 单 skill） | 2026-10-16 | 安全审计（纯规则文档型，无 scripts 可执行件；引用文件 7 件＋示例 2 件，零网络面零密钥）→ 用户”进一步增加社科选题 skill”照准 → 已装 `<技能根>/research-ideation/`（MIT，454★，来源 Galaxy-Dawn/claude-scholar v2026-04-22 轻量核心版），入注册表 C1 ②⑤（乙型），蒸馏件＝方法卡18（RQ Card＋四支柱） |
| paper-cn-to-en v1.0（乙型全稿中译英＋甲型题目摘要关键词英译） | 2026-10-15 | 安全审计：4 文件纯文档零脚本零网络零密钥 → 用户拍板配置入系统 → 入注册表学术·翻译装载；**本机 2026-10-17 重取安装**（`wave2234/paper-cn-to-en` `master`，4 文件／8 KB，MIT 随附） |

## 待载候选（2026-10-16 批次 · 社科选题技术性增强）

| # | 候选 | 来源 | 预判价值 | 处置建议 |
|---|---|---|---|---|
| 待载-03 | **Awesome-Agent-Skills-for-Empirical-Research**（119 仓库/23,000+ skill 索引图，newarle） | gitee.com/newarl/Awesome-Agent-Skills-for-Empirical-Research | T 库检索索引：按研究流程 01-10 分类（01 选题与研究设计），社科实证全流程可查 | 登记为”检索入口”（非安装），T 管道查新时先查此图 |
| 待载-04 | **CoPaper.AI 方法论套件**（20 个实证方法论 skill：OLS/DID/IV/RDD/PSM/DML 等） | 见 Awesome 图内条目 | 实证方法侧参考（C5 分析阶段）；对 C1 方法轨预锁有”成熟先例”佐证价值 | 暂不安装；C5 实证轨缺方法引擎时再评估 |
| 待载-05 | **SGHA**（arXiv 2608.17501，证据锚定研究问题发现，本地 LLM） | arxiv.org/html/2608.17501 | 方法论蒸馏（”验证先于公式化”已入方法卡18 §五） | 不安装，蒸馏吸收 |
| 待载-06 | **Tree-of-Ideas / EvoAgent**（arXiv 2608.10740，四种 Idea 类型） | arxiv.org/html/2608.10740 | 方法论蒸馏（四种 Idea 类型已补入方法卡05 §三） | 不安装，蒸馏吸收 |
| 待载-07 | **IdeaAnchor**（arXiv 2610.08781，文献条件研究构思） | arxiv.org/html/2610.08781 | 方法论蒸馏（idea anchor 规范已入方法卡05 来源格强化思路） | 不安装，蒸馏吸收 |
| 待载-08 | **research-question-refiner**（研究问题精炼器 · SkillMD 构建指南） | skillmd.ai/pt/how-to-build/research-question-refiner/ | 关键词头脑风暴 3-7 词法（已入证据链锚1 关键词组合纪律） | 不安装，蒸馏吸收 |
| 待载-08a | **research-question-refiner**（LobeHub 版 · 三阶段法，2026-10-16 新发现） | lobehub.com/skills/neversight-learn-skills.dev-research-question-refiner | 三阶段：挖掘兴趣（Excavating）→绘制领地（Mapping，knowns/unknowns/controversies）→找缺口（Finding Gap，新颖性/难度/影响/范围四评）——与星躔两阶段化（PRQ→综述→双检查）结构同源，可作 ④′c 再推敲的外部视角核对 | **已蒸馏挂载**：方法卡18 §七 再推敲可选框架（三阶段法并入）；无 GitHub 源码页，不安装 |
| 待载-08b | **research-question-refiner**（FindSkill 版 · PICO/SPIDER/PEO/FINER 框架，Verified 4.5/5，2026-10-12） | findskill.ai/skills/research-question-refiner/ | PICO(T)/SPIDER/PEO（人群/暴露/结果）三结构框架＋FINER 粗筛——结构框架可转译为人文社科问法（星躔已用 FINER，PICO/SPIDER 偏医学，仅吸收“结构提问”思想） | 不安装，蒸馏吸收（FINER 已在方法卡05 附二） |

## 处置纪律

1. 待载条目均**不安装**，待用户点名评估时再走准入流程
2. 转正动作＝安全审计（skills-security-check）→ 档位归属裁决 → 登记转正日期 → **从待载区移除、转入“已转正台账”留痕**（原措辞为“从本清单移除”，与已转正台账并存相抵，2026-10-26 校正：留痕是审计需要，移除仅指待载区）
3. 本清单由 E1 沉淀路由器 T 管道维护，新增候选随时登记
