#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check-engines.py — 星躔引擎依赖体检
对照《skills/xingchan/references/C环节skill注册表.md》扫描本机技能目录，
输出各工序默认引擎的就绪/缺失报表。新机器部署后先跑这个。

用法: python check-engines.py [--skills-dir <路径>]
退出码: 0 全就绪；1 有缺失。
"""
import sys, re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

DEFAULT_SKILLS_DIR = Path.home() / ".workbuddy" / "skills"
REGISTRY = Path(__file__).parent / "skills" / "xingchan" / "references" / "C环节skill注册表.md"
STOP = {"full", "quick", "review", "mode", "modes", "line", "only", "json"}

def registry_engines() -> dict:
    if not REGISTRY.exists():
        print(f"ERROR: 找不到注册表 {REGISTRY}", file=sys.stderr)
        sys.exit(2)
    engines = {}
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if set(cells[0]) <= {"-", ":", " "} or cells[0] == "工序":
            continue
        names = sorted({t.lower() for t in re.findall(r"[a-z][a-z0-9\-]{3,}", cells[2]) if t.lower() not in STOP})
        if names:
            engines[cells[0] + " · " + cells[1]] = names
    return engines

def main() -> int:
    skills_dir = DEFAULT_SKILLS_DIR
    if "--skills-dir" in sys.argv:
        skills_dir = Path(sys.argv[sys.argv.index("--skills-dir") + 1])
    installed = {d.name.lower() for d in skills_dir.iterdir() if d.is_dir()} if skills_dir.exists() else set()
    norm = lambda s: s.replace("-", "")
    installed_n = {norm(i) for i in installed}
    engines = registry_engines()
    ready, missing = [], []
    for cell, names in engines.items():
        hit = next((n for n in names if n in installed or norm(n) in installed_n), None)
        (ready if hit else missing).append((cell, ", ".join(names), hit or "-"))
    print(f"本机技能目录: {skills_dir} ({len(installed)} 个)")
    print(f"注册表单元格: {len(engines)} | 就绪: {len(ready)} | 缺失: {len(missing)}")
    for label, rows in (("✅ 就绪", ready), ("❌ 缺失", missing)):
        print(f"-- {label} --")
        for cell, names, hit in rows:
            print(f"  {cell:<26} 引擎: {names}" + (f"  [命中: {hit}]" if hit else ""))
    return 0 if not missing else 1

if __name__ == "__main__":
    sys.exit(main())
