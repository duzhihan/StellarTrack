---
name: nature-skills
description: Nature 系学术写作与研究全家桶（23 件聚合路由）：英文写作/润色/模拟评审/审稿回复/数据声明为六件核心，另有文献检索获取、精读解析、参考文献核验、科研绘图、论文转 PPT/专利、统计审查、社科选题论证共 17 件外延。当目标刊为 Nature 系、或需英文轨写作、或需文献检索核验与图表产出时使用。中文写作主轨仍归星躔，本栈不替代。
metadata:
  version: 0.2.0
  upstream: Yuan1z0825/nature-skills
  license: Apache-2.0
  installed: 2026-10-17
  placement: 23 件实体在 skills/nature-*/，本源文件为聚合路由壳
  scope: 六件核心（英文轨）＋ 17 件外延（检索/阅读/核验/图表/写作扩展）
---

# Nature 系研究栈 · 路由壳

> 本文件是**聚合路由层**，不含方法论本体。23 件实体在 `skills/nature-*/`，各件自带 SKILL.md。
> 安装动机：星躔学术档在**英文轨**缺 C6 起草／C9 评审／C10 回复的可挂载引擎；另在文献检索核验、图表产出、统计审查三处缺工具。中文写作主轨由离朱与 C6 骨架承担，不换。

---

## 一、六件核心（英文轨 · 与星躔工序对应）

| 件 | 职能 | 星躔工序 | 嵌入型 |
|---|---|---|---|
| `nature-writing` | 从作者已给证据起草／重构章节与首投材料 | **C6 正式撰写** | 乙型 |
| `nature-polishing` | 润色／中译英／收紧既有英文散文 | **C6 / C7 / C10** | 甲型 |
| `nature-reviewer` | 证据锚定的模拟同行评审 | **C9 联合评审**（外审席） | 甲型 |
| `nature-response` | 逐点回复、返修信、LaTeX 修订包 | **C10 修改沟通** | 乙型 |
| `nature-data` | Data／Code Availability、FAIR 元数据 | **C8 格式校验与合卷** | 甲型 |
| `nature-shared` | 共享参考件（被其余件引用） | 不单独挂载 | 依赖 |

---

## 二、17 件外延（分五组）

### A 组 · 检索与获取（4 件）

| 件 | 职能 | 建议工序 |
|---|---|---|
| `nature-academic-search` | 多源文献检索、引文核对、参考文献管理、MeSH 策略、引文影响审计 | **C2 材料** |
| `nature-citation` | Nature／CNS 系定向引用，claim→source 映射，可导出文献管理器 | **C2 / C8 引用** |
| `nature-downloader` | 合法全文获取（CNKI 机构访问、OA、出版商 API、机构浏览器兜底、支撑材料） | **C2 材料**（获取动作） |
| `nature-literature-pipeline` | 全自动文献发现管线：多源检索→六维打分→精读→格式化交付→归档 | **C2 材料**（批量化） |

> **与既有引擎分工**：知网检索仍走 `cnki-deepsearch`（本机有头浏览器＋登录态，见星躔 R-07）；`nature-downloader` 只在需要**出版商 API／OA 全文**时补位，**不替代 cnki 通道**。`nature-academic-search` 的检索结果须回 C2 材料门做来源分级。

### B 组 · 阅读与解析（5 件）

| 件 | 职能 | 建议工序 |
|---|---|---|
| `nature-reader` | 中英对照全文阅读器（文段／图表／公式对齐） | C2 精读 |
| `nature-paper-xray` | 单篇深读：还原作者真实路径，而非复述摘要主张 | C2 精读 |
| `nature-paper-card` | 结构化精读卡（方法拆解／证据链／局限／研究想法） | C2 → 方法卡产出 |
| `nature-paper-trans` | 英文论文 PDF → 简体中文**图片型** PDF 逐页翻译（保版式） | C2 辅助阅读 |
| `nature-experiment-log` | 实验日志标准化（图片／语音／文字 → 带 frontmatter 的 Markdown） | C5 数据与编码 |

### C 组 · 核验（1 件）

| 件 | 职能 | 建议工序 |
|---|---|---|
| `nature-ref-verifier` | 参考文献逐条多源交叉验证：作者／标题／年份／卷期／页码逐字段比对，标卷年与 DOI 年冲突、作者顺序异常、页码偏差 | **C8 引用**（终检） |

> **与 `reference-check` 的关系**：星躔自有的 `reference-check`／`claim-audit` 是本机主引擎；`nature-ref-verifier` 为**多源交叉**加强件，只在参考文献量大或跨库冲突多时启用，不重复跑。

### D 组 · 产出与转换（5 件）

| 件 | 职能 | 建议工序 |
|---|---|---|
| `nature-figure` | 科研绘图（Python／R）：多面板图、投稿级图、机制示意图 | C3 模型图 / C6 配图 |
| `nature-paper2ppt` | 论文 → 中文汇报 PPTX（配源图与讲者备注） | C11 外延 |
| `nature-image2ppt` | 图片／截图／扫描 PDF／图片型 PPTX → 对象级可编辑 PPT | C11 外延 |
| `nature-paper-to-patent` | 论文 → 中文发明专利草案与技术交底书 | 独立线（非论文） |
| `nature-proposal-writer` | 研究计划、开题报告、科研项目申请书 | **申报档** |

> **与既有件分工**：`paper-mechanigraph-4ss` 已负责 C3 模型图，`nature-figure` 在需要**投稿级多面板图或 R 语言**时补位，二者不并用；`lieflat-charts`／`ljg-present` 仍负责传播档可视化，本组不接管。

### E 组 · 分析与审查（2 件）

| 件 | 职能 | 建议工序 |
|---|---|---|
| `nature-statistics` | 统计报告审查：实验单元、重复、不确定性、检验、图注统计 | **C9 评审**（方法席） |
| `nature-social-science` | 社科选题论证工作台：选题构思→文献梳理→论证组织→学术表达；含新颖性审计与“审稿人 2”式攻击 | **C1 选题 / C3 论证** |

> ⚠️ `nature-social-science` 的选题方法论与星躔 **C1 两阶段化＋方法卡 05/18** 高度重叠。**星躔优先**：本件只作外部视角核对（尤其“审稿人 2 式攻击”可作 C1 ⑤ 前的对抗检查），**不接管 C1 流程、不替代方法卡**。

---

## 三、挂载条件

**六件核心**（三条全满足）：
1. 目标刊为 Nature 系，或用户显式点名“Nature 风格”“英文期刊”；
2. 稿件已有可用证据与数据（本栈只做表达与结构，不产生证据）；
3. 用户已确认走英文轨。

**17 件外延**：按需单点挂载，**不受上述三条限制**——但每件启用前须声明落在哪个工序、产出交给谁。**默认不自动触发**（中文任务不唤起）。

---

## 四、乙型纪律

`nature-writing` 与 `nature-response` 属**乙型**：自带完整流程，启用即覆盖星躔本工序默认动作。

> **铁律：乙型流程到守门点必须停下交验**——产出回星躔守门判定（C6 后过六维打分，C10 后过 C9 复核水位），**不得由本栈自行宣告完成**。

其余各件为**甲型**（只盖一格，不接管流程）；`nature-proposal-writer` 因覆盖申报档全链，按**乙型**对待。

---

## 五、红线：云端 OCR 与材料外传

`nature-image2ppt/cli/image2ppt/runtime/paddle_text_hints.py` 是**可选的云端 OCR 增强**（默认路径为离线 `image2ppt page hints`）：

- 该脚本向 `paddleocr.aistudio-app.com` **上传整幅图片**，需显式提供 `PADDLE_OCR_TOKEN` 才可用；
- **与星躔“文档摄取红线”等同**：未发表论文稿件与申报书、含学生个人信息的材料、党内文件与内部纪要、用户未授权外传的任何文档，**一律禁用**；
- 需要 OCR 时走本地路径（`--ocr local` 或 `image2ppt page hints` 离线模式），或先报用户转人工。

`nature-downloader` 的凭据（Elsevier／Springer／IEEE 等）由 `scripts/configure_credentials.py` 存**本地配置**，走环境变量或本地文件，**不随包分发、不上传**。

---

## 六、与既有引擎的边界（防撞车）

| 已有件 | 重叠处 | 裁定 |
|---|---|---|
| 离朱 `literature-review-writer` | 综述撰写 | **星躔优先**；本栈不做综述，只做综述之后的英文表达 |
| `cnki-deepsearch` | 知网检索 | **星躔优先**（有登录态＋R-07 判定纪律）；`nature-downloader` 只补全文获取 |
| `reference-check`／`claim-audit` | 引用与主张核验 | 本机为主；`nature-ref-verifier` 仅多源交叉加强 |
| `paper-mechanigraph-4ss` | C3 模型图 | 本机为主；`nature-figure` 仅投稿级多面板补位 |
| `lieflat-charts`／`ljg-*` | 可视化 | **传播档归它们**，本栈不接管 |
| 方法卡 05／18 | 选题方法论 | **星躔优先**；`nature-social-science` 只作外部核对 |
| `humanities-tools` | 文本确定性机检 | **互补**：它查规则命中，本栈查表达质量 |

---

## 七、许可、来源与缺失资产

- **来源**：`github.com/Yuan1z0825/nature-skills`（★48.4k）
- **许可**：Apache-2.0（可商用、可再分发，须保留 LICENSE 与声明）；`LICENSE` 已随附本目录
- **版本**：上游 2026 持续更新；本地为 2026-10-17 抓取快照（`main`）
- **安装规模**：23 件 / 740 文件；六件 205 件 ＋ 外延 533 件
- **安全审计**（2026-10-17，468 文件关键词扫描）：
  - **P0 = 0**：唯一“硬编码凭据”命中在 `nature-downloader/tests/` 的**测试夹具**（值 `publisher-secret-12345678`，明显为占位）；无远程下载执行、无隐蔽破坏组合
  - **P1 外发 = 1 处**：即第五节所列 PaddleOCR，**条件性、需 token、默认不触发**，已列红线
  - `pip install` 11 处全为**ImportError 提示文案**或文档示例，非自动执行；`sudo apt-get` 在 `references/runtime-dependencies.md` 属人类阅读的安装说明
  - **P2 执行面 107 处** `subprocess`：多为调用本地工具（ImageMagick／LibreOffice／mermaid-cli／本地 python 脚本），参数由本件模板给定，非外部输入直通
- **未随包下载**：56 张图片资产（35.8 MB，以 `nature-figure` 示例图为主）。经核查，缺图仅影响**示例与 banner 展示**，各件机制、模板与脚本均为文本件，**不影响功能**。清单见 `_skipped_images.txt`（工作区 `outputs/_nature_ext_20261017/`），需要时可按 raw 直取。

---

## 八、格式约定

本壳与星躔接口一致：散文区一律全角引号；对外交付正文字数、术语与体例仍以星躔 C11 硬检为准（本栈不替代终校）。
