# paper-cn-to-en

把中文人文社科论文翻译成地道学术英文的 Claude Skill。

A Claude Skill that translates Chinese humanities papers (art history, visual culture, curatorial studies...) into natural academic English — not translationese.

## 适用范围

✅ 艺术史、视觉文化、策展研究、文化研究、电影研究等**人文社科**论文的中译英

❌ SCI / 理工科论文请绕道——本 skill 的文风原则（保留论证声音、领域术语不降级、句法节奏感）与理工写作规范相反，硬套会翻车

## 为什么不是又一个"翻译提示词"

网上流传的学术翻译提示词大多有两个问题：

1. **先直译再润色的三步法**：直译稿会锚定句子骨架，后续怎么修都还是中文语序，机翻味的病根就在这。本 skill 要求直接生成地道英文，以段落为单位重组逻辑。
2. **SCI 文风一刀切**："少用长难句、不用生僻词汇"对理工论文是美德，对人文写作是灾难——gaze、discipline、allegory 在艺术史里是吃饭的术语，不是需要简化的"深奥词汇"。

除此之外，这个 skill 把翻译当工程管：**先建术语表**（专有名词逐一查证官方英文名，黄炳是 Wong Ping 不是 Huang Bing，劏房是 subdivided unit 不是 partitioned room）、**先算词数预算**（有词数上限的作业按节分配、实测核对）、**交付前按术语表全篇检查一致性**（前后译法打架是机翻味的最大来源）。

## 使用

**Claude Code / Claude 客户端**：把 `SKILL.md` 装进你的 skills 目录（或直接让 Claude 保存为 skill），之后甩论文过去说"翻译成英文"即可自动触发。

**其他 AI**：用 [`prompt-universal.md`](./prompt-universal.md)，平台无关的提示词版本，开头粘贴进对话即可。

## License

MIT
