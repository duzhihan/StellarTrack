# NOTICE · 组件来源与许可清单

> 登记口径：自研＝本系统作者原创；第三方＝源自社区/他人项目，发布前应补溯源五件套（作者/链接/许可/原理/日期），未核者使用前请自行确认许可。

## 自研件（可放心使用）

| 组件 | 说明 |
|---|---|
| paper-factory | 星躔本体 |
| abstract-checker | C11 摘要对照器 |
| claim-audit / reference-check / journal-fit / manuscript-review | 学术诚信与投稿四件 |
| research-design / theoretical-framework / title-assessor | 研究设计三件 |
| duzhihan-paper-editor / evidence-bound-revision / nsfc-review-guide | 修改与申报对标 |
| nssfc-*（六件） | 国家社科基金申报管线 |
| gongwen-draft | 规范公文写作 |
| citation-format | 引用格式统一 |

## 第三方件（来源待补全，用前自查）

| 组件 | 已知信息 | 待办 |
|---|---|---|
| cnki-deepsearch | 知网检索封装 | 溯源五件套待补 |
| literature-review-writer | 文献综述引擎（离朱） | 同上 |
| paper-mechanigraph-4ss | 社科机制图生成 | 同上 |
| good-story | 故事方法引擎 | 同上 |
| writing-dna-skill | 写作 DNA 蒸馏 | 同上 |
| lieflat-less-ai-tone | 去 AI 味规则集 | 同上 |
| human-review | 浏览器可视化审稿（v0.6.1） | 同上 |

## 组件形态说明

- `human-review` 与 `nsfc-review-guide` 为**资源型组件**：入口是 `README.md`（非 SKILL.md）。human-review 为 Node 工具，使用前需在其目录执行 `npm install` 装依赖；nsfc-review-guide 主体为各类申请书自检指南文档集。

## 分发剔除项

- `gongwen-draft/assets/fonts/`：仿宋_GB2312、方正小标宋简、楷体_GB2312 等商业授权字体
- 各组件 `.git/`、`node_modules/`、构建产物
- `paper-factory/_backups/`、`archive/`、`references/archive/`、`data/`、校准台账、反馈日志等个人运行时数据
