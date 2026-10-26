# 星躔 StellarTrack

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/hero.svg" alt="StellarTrack" width="100%"/>
</p>

<p align="center">
  <b>给 AI 一套写论文的流程，而不是让它猜。</b><br/>
  <sub>一条带关卡的写作流水线：AI 干活，你在每个关卡签字。</sub>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"/></a>
  <img src="https://img.shields.io/badge/version-v12.6.14-blue.svg" alt="version"/>
  <img src="https://img.shields.io/badge/Agent%20Skill-Claude%20Code%20%7C%20WorkBuddy-2f6feb.svg" alt="Agent Skill"/>
  <img src="https://img.shields.io/badge/lang-%E4%B8%AD%E6%96%87%20%7C%20English-informational.svg" alt="lang"/>
</p>

<p align="center">
  <b>简体中文</b> ｜ <a href="README.md">English</a>
</p>

---

## 你可能正卡在这儿

- 让大模型“写篇论文”，十秒给你一篇像论文的东西——**但你不敢投**。它没走过你的思考，每个结论都像借来的。
- 想让它按你的思路改，改到第三轮它就忘了前两轮定了什么，越改越远。
- 写完了心里没底：引证是真的吗？摘要和正文对得上吗？这一稿到底够不够投出去？

问题不在文字生成。**在过程**。

## 它怎么工作

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/overview.svg" alt="O-S-C-E 流程" width="100%"/>
</p>

四个字概括：**定目标、想清楚、搭结构、留经验**。

先把“这篇要解决什么”钉死（定不下来不许动笔），再把核心判断句锚住（配一个能被证伪的验证方式），然后把写作拆成十一道工序——选题、材料、综述、大纲、填充、撰写、净化、校验、评审、修改、精校。

**每道工序末尾有一道关卡**。判据不过，回退重做，不许“先写着再说”。这就是它跟“直接问大模型”最大的区别：**它不让你跳步**。

## 能写什么

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/tracks.svg" alt="13 个档位" width="100%"/>
</p>

十三个档位共用同一套骨架，**换的是文体，不换流程**。

学术论文要证据和规范，公众号要可读和钩子，小说要画面和节奏——骨架一样，权重和执行方式不同。你不需要为每种文体学一套新工具。

## 它凭什么说自己可靠

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/scoring.svg" alt="六维评分" width="100%"/>
</p>

打分只有一把尺：六个维度固定权重，1／3／5／7／9 五档锚点，**7 分才放行**。同一稿由两个席位背靠背打分，分差超过阈值就进复核，不许一个人说了算。

另有封顶条款：假引证、关键数据没来源、通篇只夸不批——命中即封顶，不给高分蒙混过去。

## 三库供血

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/libraries.svg" alt="三库" width="100%"/>
</p>

写作不是凭空生成。每个工序开工先去库里取料：方法库给打法，知识库给材料，工具库给引擎。**取不到就走降级，并且必须声明**——不许假装调用过。

## 规模与自检

<p align="center">
  <img src="https://raw.githubusercontent.com/duzhihan/StellarTrack/main/assets/readme/stats.svg" alt="规模" width="100%"/>
</p>

69 个 Skill、13 个档位、11 道工序、29 个引擎位。系统自己带体检脚本：版本一致性、引号合规、引用能否解析、结构是否完整、语义层有没有自相矛盾——**改完不跑体检不算改完**。

## 三步上手

**1. 拿到它**

```bash
git clone https://github.com/duzhihan/StellarTrack.git
```

**2. 放到你的 Agent 技能目录**

```bash
# Claude Code / WorkBuddy 等支持 Agent Skill 的客户端
cp -r StellarTrack/skills/xingchan ~/.workbuddy/skills/
```

**3. 说一句人话**

```
帮我写一篇论文，主题是「短视频平台上的戏曲传播」
```

它会先问你几个问题（投什么刊、想要什么判断、材料有哪些），然后从 C1 开始，一道工序一道工序往下走。**每过一道关卡都会停下来等你确认**——不会一口气写完甩给你。

> 想先看效果？让它跑“帮我捋一捋这个选题行不行”，这个模式只思考不出稿。

## 你会得到什么

- 每一步都有产物：选题卡、材料账本、结构大纲、评审清单、修改记录。
- 全部是 Markdown，能进 Git，能贴进 Word，能发给导师。
- 中途断了不丢进度：状态写在磁盘上，换个会话接着走。

## 常见问题

**它会替我写论文吗？**
它替你干重复劳动，但**判断句必须是你的**。选题、核心论点、要不要发，它只给候选和理由，不替你拍板。

**要不要 API key？**
核心流程不需要。部分外挂引擎（文献检索、语义检索）需要你自己配，配不了就自动降级并告诉你。

**中文写作行不行？**
本来就是为中文人文社科写的。术语、体例、引证格式按中文期刊惯例。

**为什么默认只给 Markdown？**
因为大部分 Word 排版是白费功夫。真要交 Word，明确说一声，它再转。

## 诚实说明

- **还没有外部用户验证**。这是一个人的系统，跑过真实稿件，但没有社区规模的使用反馈——这是路线图第一项。
- 它拦得住“跳步”和“假装引用”，拦不住“选题本身没价值”。判断力仍是你的。
- 打分尺子经过校准，但校准样本来自作者自己的稿件，不是第三方盲测。

## 许可

MIT。可商用、可修改、可分发。逐项来源与授权说明见 [NOTICE.md](NOTICE.md)。
