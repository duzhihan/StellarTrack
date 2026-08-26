# StellarTrack · 星躔

> 跨场景学术写作系统（O-S-C-E 架构）。出门称星躔（StellarTrack），代码层标识 paper-factory。
> 四段管线：O 目标定向 → S 思考决策 → C 认知建构（C1-C11 带号流转）→ E 经验共创。

## 这是什么

一套以「工序流水线 × 档位装载」为骨架的社科写作 Agent 技能集：

- **C 骨架文体无关**——换文体只换装载（学术档／传播档／规范档／申报档／回溯档／演讲档），不换流水线
- **三层能力 M-K-T**：方法库（方法卡）／知识库（按需检索）／工具箱（本仓库 skills/ 即其装配实体）
- **守门分级**：学术档全强度七要素守门，其他档轻量三项
- **嵌入三型法**：甲＝单工序引擎｜乙＝档位指令包主体｜丙＝外延点名直用

## 目录结构

```
skills/
├── paper-factory/        # 星躔本体：SKILL.md＋六档工作流＋references 全套
├── abstract-checker      # C11 摘要↔正文一致性对照器
├── claim-audit           # 承重主张回源核验
├── manuscript-review     # 交稿前自审
├── journal-fit           # 目标期刊要求对标
├── reference-check       # 参考文献逐笔查核
├── research-design       # 研究方法设计
├── theoretical-framework # 理论框架建构
├── title-assessor        # 标题评估
├── cnki-deepsearch       # 知网检索底座（需自备账号）
├── gongwen-draft         # 规范公文写作
├── nssfc-*（6件）        # 国家社科基金申报全管线
└── …                     # 其余见 NOTICE.md 来源清单
```

## 环境绑定件说明（不在本仓库、也无法打包）

| 组件 | 说明 |
|---|---|
| C2 知网选题通道 | 协议全文在 `skills/paper-factory/references/学术档工作流.md`，需 Chrome 远程调试＋本人知网账号会话 |
| C6 排版 tencent-docx 线 | WorkBuddy 平台内置组件；其他平台用各自的 docx 导出方案替代 |
| 公文字体 | `gongwen-draft/assets/fonts/` 因版权未随仓库分发，使用前自行安装仿宋_GB2312、方正小标宋等并放回该目录 |

## 私有运行时数据未随仓库分发

`paper-factory/data/`（偏好画像、思维轨迹、摩擦台账）、校准台账、反馈日志均为个人运行时产物，不入库。

## 许可

见 [NOTICE.md](NOTICE.md)——各子组件来源与许可状态逐项列明，第三方待核件使用前请自查。
