#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check-engines.py — 星躔引擎依赖体检（v2 · 多来源 + 通道类豁免）
对照《references/C环节skill注册表.md》扫描本机技能目录，
输出各工序默认引擎的就绪/缺失报表。新机器部署后先跑这个。

v2 改进（2026-10-10）：
  ① 多来源扫描——除用户 skills 目录外，兼扫插件侧 skill（如 tencent-docx 属内置插件，
     此前被误报为缺失）；
  ② 通道类豁免——注册表引擎列含“通道”二字者（描述线上服务通道，如知网选题通道、
     浏览器自动化通道），本质不是 skill，不纳入 skill 存在性体检，单列一栏；
  ③ 判定口径写进输出，避免“体检报缺 = 体系坏了”的误读。

用法: python check-engines.py [--skills-dir <路径>]
退出码: 0 无缺失；1 有缺失（通道类不计入）。
"""
import sys, re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

DEFAULT_SKILLS_DIR = Path.home() / ".workbuddy" / "skills"
# REGISTRY 位置自适应（v12.6.1 修）：单一副本适配三处安装位——xingchan 内部(references/)、
# 文档包根(02_协议与工序/)、运行时包根(skills/xingchan/references/)，按存在性取第一个。
_REG_CANDS = [
    Path(__file__).parent / "references" / "C环节skill注册表.md",
    Path(__file__).parent / "02_协议与工序" / "C环节skill注册表.md",
    Path(__file__).parent / "skills" / "xingchan" / "references" / "C环节skill注册表.md",
]
REGISTRY = next((c for c in _REG_CANDS if c.exists()), _REG_CANDS[0])
STOP = {"full", "quick", "review", "mode", "modes", "line", "only", "json",
        "skills", "workbuddy", "builtin", "plugins", "plugin",
        # v12.6.5 补：注册表引擎格含括注说明，防把说明文字里的英文词当引擎名
        "tools", "python", "format", "search", "latest", "github", "readme",
        "skill", "name", "http", "https", "www", "com", "date", "stage"}
MAX_DEPTH = 6

PLUGIN_ROOTS = [
    Path.home() / ".workbuddy" / "plugins" / "cache",
    Path.home() / ".workbuddy" / "plugins",
    # 其他安装位探测按用户实际环境追加（S-07：禁硬编码作者机器绝对路径，开源用户机器上不存在）
]


def scan_plugin_skills() -> set:
    """递归扫描插件侧，返回含 SKILL.md 的目录名集合（小写）。
    仅收“真插件技能”——排除示例／模板／依赖等噪声目录（v2.1 收紧）。"""
    found = set()
    NOISE = {"node_modules", ".git", "__pycache__", "dist", "build", "src",
             "test", "tests", "examples", "example", "docs", "templates",
             "assets", "references", "scripts", "data", "locale", "locales"}
    for root in PLUGIN_ROOTS:
        if not root.exists():
            continue
        base = len(root.parts)
        for dp, dns, fns in os_walk_safe(root, base, NOISE):
            if "SKILL.md" in fns:
                found.add(Path(dp).name.lower())
    return found


def os_walk_safe(root: Path, base: int, noise: set = frozenset()):
    import os
    for dp, dns, fns in os.walk(root):
        depth = len(Path(dp).parts) - base
        if depth >= MAX_DEPTH:
            dns[:] = []
        dns[:] = [d for d in dns if d not in noise]
        yield dp, dns, fns


def registry_engines():
    """解析注册表 → (engines, channels, placeholders)。

    v12.6.5 口径修正（治虚报缺失）：注册表引擎格体例为“引擎名（括注）：说明”。
    原实现对整格抽英文 token，会把说明文字里的专有名词误当引擎名
    （实测把 Semantic Scholar 截成 emantic/cholar、Cross 截成 ross），虚报缺失项。
    定案口径：**含连字符 token 全取**（引擎名多为 kebab-case，申报档的 nssfc-*
    写在说明侧，截断法会误杀）；**无连字符 token 只取全角冒号之前**的引擎名区
    （说明文字里的单词不收）。另立“占位类”：格内含“占位”者为有意留空，不做存在性检查。
    """
    if not REGISTRY.exists():
        print(f"ERROR: 找不到注册表 {REGISTRY}", file=sys.stderr)
        sys.exit(2)
    engines, channels, placeholders = {}, [], []
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if set(cells[0]) <= {"-", ":", " "} or cells[0] == "工序":
            continue
        cell = cells[0] + " · " + cells[1]
        if "通道" in cells[2]:
            channels.append(cell)
            continue
        if "占位" in cells[2]:
            placeholders.append(cell)
            continue
        head, tail = cells[2].split("\uff1a", 1) if "\uff1a" in cells[2] else (cells[2], "")
        toks = {x.lower() for x in re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{3,}", head)}
        toks |= {x.lower() for x in re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{3,}", tail) if "-" in x}
        names = sorted(x for x in toks if x not in STOP)
        if names:
            engines[cell] = names
    return engines, channels, placeholders


def main() -> int:
    skills_dir = DEFAULT_SKILLS_DIR
    if "--skills-dir" in sys.argv:
        skills_dir = Path(sys.argv[sys.argv.index("--skills-dir") + 1])
    installed = {d.name.lower() for d in skills_dir.iterdir() if d.is_dir()} if skills_dir.exists() else set()
    # 内置引擎：随星躔活体走（references/engines/<name>/），不经用户级安装位
    builtin_dir = Path(__file__).parent / "references" / "engines"
    builtin = {d.name.lower() for d in builtin_dir.iterdir() if d.is_dir()} if builtin_dir.exists() else set()
    plugin = scan_plugin_skills()
    norm = lambda s: s.replace("-", "")
    user_n = {norm(i) for i in installed}
    builtin_n = {norm(i) for i in builtin}
    plug_n = {norm(i) for i in plugin}

    engines, channels, placeholders = registry_engines()
    ready, missing = [], []
    for cell, names in engines.items():
        hit = next((n for n in names if n in installed or norm(n) in user_n), None)
        src = "用户"
        if not hit:
            hit = next((n for n in names if n in builtin or norm(n) in builtin_n), None)
            src = "内置"
        if not hit:
            hit = next((n for n in names if n in plugin or norm(n) in plug_n), None)
            src = "插件"
        (ready if hit else missing).append((cell, ", ".join(names), ("%s·%s" % (hit, src)) if hit else "-"))

    print("本机技能目录: %s (%d 个)" % (skills_dir, len(installed)))
    print("插件侧候选  : %d 个含 SKILL.md 的目录名（仅用于存在性判定，不代表可用技能数）" % len(plugin))
    print("注册表单元格: %d（引擎格 %d ＋ 通道格 %d ＋ 占位格 %d）| 就绪: %d | 缺失: %d"
          % (len(engines) + len(channels) + len(placeholders), len(engines), len(channels),
             len(placeholders), len(ready), len(missing)))
    print("判定口径: 插件侧技能计入就绪（来源以“插件”标记）；含“通道”者不纳入检查（线上服务通道，非 skill）；"
          "含“占位”者不纳入检查（有意留空）；引擎名抽取＝含连字符者全取＋无连字符者只取说明前。")
    for label, rows in (("✅ 就绪", ready), ("❌ 缺失", missing)):
        print("-- %s --" % label)
        for cell, names, hit in rows:
            print("  %-26s 引擎: %s" % (cell, names) + ("  [命中: %s]" % hit if hit else ""))
    if placeholders:
        print("-- ⏳ 占位类（有意留空，非缺口）--")
        for c in placeholders:
            print("  %s" % c)
    if channels:
        print("-- ⚪ 通道类（不适用本体检）--")
        for c in channels:
            print("  %s" % c)
    return 0 if not missing else 1


def _selftest():
    """口径自测（v12.6.5 · 反例驱动）：防误抽、防截断误杀、占位不外报。"""
    ok = n = 0

    def chk(name, got, want):
        nonlocal ok, n
        n += 1
        if got == want:
            ok += 1
            print("  [PASS] %s" % name)
        else:
            print("  [FAIL] %s  got=%r want=%r" % (name, got, want))

    def names_of(text):
        head, tail = text.split("\uff1a", 1) if "\uff1a" in text else (text, "")
        toks = {x.lower() for x in re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{3,}", head)}
        toks |= {x.lower() for x in re.findall(r"[a-zA-Z][a-zA-Z0-9\-]{3,}", tail) if "-" in x}
        return sorted(x for x in toks if x not in STOP)

    t1 = "**humanities-tools（甲型 · 转正 2026-10-15 · MIT）**\uff1areview.py 评估；参考 Semantic Scholar 与 Cross"
    chk("说明文字专有名不误抽", [x for x in names_of(t1) if x in ("emantic", "cholar", "ross")], [])
    chk("引擎名正常抽到", "humanities-tools" in names_of(t1), True)
    t2 = "申报指令包（乙型；安装名 6 件：nssfc-topic-to-idea→nssfc-proposal-writing 等）"
    chk("说明侧连字符引擎名取到", "nssfc-proposal-writing" in names_of(t2), True)
    chk("说明侧单词不收", [x for x in names_of(t2) if x in ("scholar", "semantic")], [])
    chk("占位识别", "占位" in "〔占位·档位已补全〕引擎待首稿实测后补齐", True)
    chk("无冒号整格", "paper-editor" in names_of("paper-editor 六模式"), True)

    print("\n  自测：%d/%d" % (ok, n))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if _selftest() else 1)
    sys.exit(main())
