# 未随包发布的资产（平台限制说明）

> 本安装包面向 SkillHub 发布，平台对包内文件扩展名有**白名单限制**（不支持图片、Office 文档、PDF、字体、YAML、CSV、TOML 等）。
> 因此本仓库中的部分资产未随包发布。下方按“是否影响功能”分栏，避免把展示性配图误当缺口。

## 一、影响功能（2 项，均非阻断）

| 技能 | 缺失资产 | 影响 | 替代方案 |
|---|---|---|---|
| `evidence-bound-revision` | `assets/defensive-writing-audit-template.csv`（264 B 表头模板） | 该技能第 4 步原建议以它为候选表底稿 | **SKILL.md 原文即写明“or an equivalent table”**——按正文列出的字段自建表格即可，流程不受阻 |
| `gongwen-draft` | `assets/fonts/catalog.toml` ＋ `*.TTF` 字体文件 | `scripts/font_guard.py` 的字体校验无法运行 | 公文排版字体需自备（字体授权本就属使用者事项）；本技能其余工序不受影响 |

## 二、参考资产（未随包；对应技能正文未依赖，属附加阅读）

- `nsfc-review-guide`：6 份申请书自检指南 `.docx`（约 47 万字节）
- `nssfc-topic-to-idea`：`references/2026年国家社会科学基金重点研究项目.pdf`
- `nssfc-proposal-writing`：`references/课题论证活页.doc`（其 SKILL.md 已标注“可选”）
- `paper-mechanigraph-4ss`：`examples/*.svg` 示例图 8 张 ＋ `resources/academic_defs.svg`

## 三、展示性配图与仓库元文件（无功能影响）

约 60 件，仅出现在 README 封面、示意图与文件树说明中：`assets/readme/*.png|svg`、`assets/*-banner*.png|webp`、`assets/agent-logos/*`、`docs/assets/*.gif`（`lieflat-charts` 文档动图 58 张）、`agents/openai.yaml`（OpenAI Agents 展示元数据）、`.gitignore`、`.gitattributes`。

## 四、取件方式

以上原文件均在本仓库对应路径下；本地完整版（含全部资产）另存于作者工作区。

## 五、有意剔除（非缺陷）

`thinking-protocols/data/`（视角银行、认知偏好画像、思维轨迹档案、摩擦登记）属**个人运行数据**，有意不随任何公网包发布。

## 六、2026-10-17 新增三引擎的未随包资产

| 技能 | 未随包 | 影响 | 替代方案 |
|---|---|---|---|
| `nature-skills`（23 件） | 12 个 `manifest.yaml`（各件的静态/动态加载声明）＋ 12 个 `agents/openai.yaml`（平台展示元数据） | 平台不支持 YAML。**`nature-writing`／`nature-polishing`／`nature-response`／`nature-data` 四件的 SKILL.md 会读 manifest 决定加载哪些 fragment**——缺 manifest 时须由 SKILL.md 正文推断加载顺序，**加载策略退化为静态全文加载，不影响正确性，只影响上下文效率** | 需要精确静态/动态分层时，从上游仓库 `skills/<件>/manifest.yaml` 取回；或按 SKILL.md 正文的 references 索引顺序加载 |
| `nature-skills`（23 件） | 56 张图片资产（约 35.8 MB，以 `nature-figure` 示例图为主） | **无功能影响**：各件机制、模板与脚本均为文本件；缺图仅影响 README 示例与 banner 展示 | 示例图非运行必需；需要时按上游 raw 路径直取 |
| `humanities-tools` | `.gitignore`、`scripts/.env.example` | **无功能影响**：前者为版本控制元文件；后者为**凭据配置模板**（示例值，非真实凭据） | 配置 `search.py` 的 API 源时，按 `README.md`／`references/literature-review.md` 列出的变量名（`CNKI_COOKIE`／`SERPAPI_KEY`／`S2_API_KEY`）自行在环境变量或 `scripts/.env` 中设置 |

> **许可说明**：`nature-skills` 为 Apache-2.0，`LICENSE` 已随包（重命名为 `LICENSE.md`）；`humanities-tools` 与 `paper-cn-to-en` 为 MIT，`LICENSE` 同样随包。三者均允许再分发，须保留许可与版权声明。
