#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wordcount.py — 星躔字数实测工具（Word 三口径）

SKILL.md 运行纪律③要求一切字数登记以本脚本实测为准，禁止 len() 汉字串或目标配比充当实绩。

三口径定义（对齐 Microsoft Word 底部统计栏习惯）:
  1. 字数              : 每个 CJK 汉字计 1；连续的拉丁字母/数字串计 1 词；CJK 标点不计入
  2. 字符数(不计空格)   : 除空白符外的所有字符逐一计数（含标点）
  3. 字符数(计空格)     : 除换行外所有字符计数（空格计入）

用法:
  python wordcount.py <文件> [更多文件...] [--json]
  支持多文件求和；--json 输出机器可读结果供工序产物嵌入。
退出码: 0 正常；1 文件不可读。
"""
import sys, json, re
from pathlib import Path

CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
LATIN_WORD_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9'\-]*")

def count(text: str) -> dict:
    cjk = len(CJK_RE.findall(text))
    latin_words = len(LATIN_WORD_RE.findall(text))
    no_space = sum(1 for ch in text if not ch.isspace())
    with_space = sum(1 for ch in text if ch not in "\r\n")
    return {
        "zishu": cjk + latin_words,          # 口径1: 字数
        "chars_no_space": no_space,           # 口径2: 字符数(不计空格)
        "chars_with_space": with_space,       # 口径3: 字符数(计空格)
        "cjk_chars": cjk,
        "latin_words": latin_words,
    }

def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--json"]
    as_json = "--json" in sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    total = {"zishu": 0, "chars_no_space": 0, "chars_with_space": 0}
    per_file = {}
    for arg in args:
        try:
            text = Path(arg).read_text(encoding="utf-8")
        except OSError as e:
            print(f"ERROR: 无法读取 {arg}: {e}", file=sys.stderr)
            return 1
        c = count(text)
        per_file[arg] = c
        for k in total:
            total[k] += c[k]
    if as_json:
        print(json.dumps({"total": total, "files": per_file}, ensure_ascii=False, indent=2))
    else:
        for f, c in per_file.items():
            print(f"{f}: 字数 {c['zishu']} | 字符(不计空格) {c['chars_no_space']} | 字符(计空格) {c['chars_with_space']}")
        if len(per_file) > 1:
            print(f"合计: 字数 {total['zishu']} | 字符(不计空格) {total['chars_no_space']} | 字符(计空格) {total['chars_with_space']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
