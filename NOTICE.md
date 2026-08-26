# NOTICE · 组件来源与许可清单

> 登记口径：自研＝本系统作者原创；第三方＝源自社区/他人项目，按「已声明许可」与「待溯源」两档登记。无许可文件的第三方件默认原作者保留权利，本仓库仅作集成收录；如有侵权请联系删除。

## 一、自研件（星躔体系原创）

paper-factory（本体）、abstract-checker、claim-audit、reference-check、journal-fit、manuscript-review、research-design、theoretical-framework、title-assessor、literature-review-writer（离朱）、paper-mechanigraph-4ss、duzhihan-paper-editor、nssfc-*（六件）、gongwen-draft、citation-format

## 二、第三方件 · 许可已确认

| 组件 | 许可 | 版权方 |
|---|---|---|
| good-story | MIT | Rimagination |
| lieflat-less-ai-tone | MIT | shiujan |
| writing-dna-skill | MIT | （见其 LICENSE） |
| cnki-deepsearch | MIT | Random Art Lab |
| human-review | MIT | Peter Yang |
| evidence-bound-revision | MIT | lensback940701 |
| human-writing | MIT | Human Writing Skill contributors |
| oh-story | MIT | worldwonderer/oh-story-claudecode |
| lieflat-charts | PolyForm Noncommercial 1.0.0（**禁商用**） | lieflat |

## 三、第三方件 · 无许可文件（集成收录，原作者保留权利）

| 组件 | 已知信息 |
|---|---|
| ljg-writes / ljg-card / ljg-present | 李继刚系社区提示词工程组件 |
| khazix-writer | 卡兹克公众号写作 skill |
| narrative-suite ＋ narrative-*（26 件，雕龙叙事系） | author: ant |
| wechat-article-search | 微信文章检索工具 |
| douyin-copy-extract__skillhub | 抖音文案提取工具 |
| nsfc-review-guide | 申请书自检指南文档集 |

## 四、组件形态与安装说明

- 多数组件以 `SKILL.md` 为入口；`human-review` 与 `nsfc-review-guide` 为**资源型组件**（入口 `README.md`）。human-review 为 Node 工具，使用前需在其目录执行 `npm install`
- `ljg-card` 的 node_modules 未随仓库分发，同样需 `npm install`

## 五、分发剔除项

- `gongwen-draft/assets/fonts/`：仿宋_GB2312、方正小标宋简等商业授权字体
- 各组件 `.git/`、`node_modules/`、构建产物
- `lieflat-charts/docs/assets/`：示例动图（约 20M，非运行必需）
- 个人运行时数据：偏好画像、思维轨迹、校准台账、反馈日志等
