# -*- coding: utf-8 -*-
"""星躔状态看板生成器（可选配套 · 丙型外延）· v2 美化版（深空星轨主题）
读：工作区 .xingchan-state.md（状态盘）＋ data/skill-tracker.md（引擎台账）＋ references/methods/（M 库卡）
出：tools/dashboard/星躔_状态看板.html（自包含单页，file:// 离线可用，数据内联）
用法：python build_dashboard.py [--state <状态盘路径>] [--out <html路径>]
默认：--state 当前目录 .xingchan-state.md；--out 本目录 星躔_状态看板.html
"""
import io, os, re, sys, glob, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
XC = os.path.dirname(os.path.dirname(BASE))  # xingchan 根
DEFAULT_STATE = os.path.join(os.getcwd(), '.xingchan-state.md')
DEFAULT_OUT = os.path.join(BASE, '星躔_状态看板.html')


def parse_state(path):
    """宽容解析状态盘：档位/稿件名/当前工序/守门进度"""
    d = {'exists': False, 'mode': None, 'title': None, 'stage': None, 'gates': [], 'raw': []}
    if not path or not os.path.exists(path):
        return d
    try:
        lines = io.open(path, encoding='utf-8').read().splitlines()
    except Exception:
        return d
    d['exists'] = True
    d['raw'] = lines[:40]
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith('#') or s.startswith('|') or s.startswith('---'):
            continue
        if '档位' in s:
            m = re.search(r'[:：]\s*([^\s|]+)', s)
            if m:
                d['mode'] = m.group(1)
        if '稿件' in s or '标题' in s or '论文' in s:
            m = re.search(r'[:：]\s*(.{2,60})', s)
            if m and not m.group(1).startswith('《'):
                d['title'] = m.group(1)
        if '工序' in s:
            m = re.search(r'C\d+', s)
            if m:
                d['stage'] = m.group(0)
        for g in ('守门③', '守门④', '守门⑤', '守门⑥', '守门⑦', '守门⑧', '守门⑨', '守门⑩', '守门⑪', '守门⑫', '守门⑬'):
            if g in s:
                passed = any(k in s for k in ('✓', '✔', '通过', '放行', 'PASS', '已过'))
                d['gates'].append((g, passed))
    return d


def parse_tracker():
    """解析台账 A 组（转正在用引擎）"""
    eng = []
    p = os.path.join(XC, 'data', 'skill-tracker.md')
    if not os.path.exists(p):
        return eng
    for ln in io.open(p, encoding='utf-8').read().splitlines():
        if not ln.startswith('|'):
            continue
        cells = [c.strip() for c in ln.strip('|').split('|')]
        if len(cells) < 10 or cells[0] in ('标识', '---'):
            continue
        name, dev, src, lic = cells[0], cells[1], cells[2], cells[3]
        if '转正' in cells[8] or '充分吸收' in cells[8]:
            eng.append({'name': name, 'dev': dev, 'lic': lic, 'ev': cells[9][:40]})
    return eng


def parse_methods():
    """扫描 M 库方法卡（references/methods/*.md）"""
    cards = []
    md = os.path.join(XC, 'references', 'methods')
    if not os.path.isdir(md):
        return cards
    for f in sorted(glob.glob(os.path.join(md, '*.md'))):
        base = os.path.basename(f)
        title = base[:-3]
        for ln in io.open(f, encoding='utf-8').read().splitlines()[:3]:
            if ln.startswith('# '):
                title = ln[2:].strip()
                break
        cards.append({'file': base, 'title': title})
    return cards


def esc(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def ev_badge(ev):
    """实用证据列 → 状态徽章（待实战=琥珀 / 实测·已落盘=绿）"""
    ev = ev or ''
    if '待实战' in ev or '未装' in ev or '待测' in ev:
        return 'amber'
    if '实测' in ev or '已落盘' in ev or '已转正' in ev or '配置就位' in ev:
        return 'green'
    return 'grey'


def parse_system():
    """统计系统进化数据：规则库/失败档/不做清单/引擎缺口/待载候选"""
    sysd = {'rules': 0, 'fail': 0, 'nogo': 0, 'gaps': 0, 'pending': 0}
    def cnt(path, pat):
        if not os.path.exists(path):
            return 0
        try:
            return sum(1 for l in io.open(path, encoding='utf-8') if re.search(pat, l))
        except Exception:
            return 0
    sysd['rules'] = cnt(os.path.join(XC, 'references', 'rule-base.md'), r'^\|\s*(S-\d+|O-\d+)\s*\|')
    sysd['fail'] = cnt(os.path.join(XC, 'data', 'failure-archive.md'), r'^#+\s*F-\d+')
    sysd['nogo'] = cnt(os.path.join(XC, 'data', 'no-go-list.md'), r'^\|\s*NG-\d+\s*\|')
    sysd['gaps'] = cnt(os.path.join(XC, 'data', 'engine-gaps.md'), r'^[-*]\s')
    sysd['pending'] = cnt(os.path.join(XC, 'references', 'T工具箱_待加载清单.md'), r'^##\s*待载')
    return sysd


def build_html(st, eng, cards, now):
    has_state = st['exists']
    mode = esc(st['mode']) or '—'
    title = esc(st['title']) or '—'
    stage = esc(st['stage']) or '—'
    n_gate = len(st['gates'])
    passed_gates = sum(1 for _, ok in st['gates'] if ok)
    gate_txt = '%d/%d' % (passed_gates, n_gate) if n_gate else '0/0'

    # 守门链 11 道（学术档基准）· 附带核心检查项（hover 提示）
    gates = [('C1 选题', '三维评测达标 ＋ 用户拍板 ＋ 标题打磨留痕'),
             ('C2 材料建档', '判断句-证据覆盖率 ≥80% ＋ 关键论点高可信证据'),
             ('C3 综述·模型·引言', '证据强度三标 ＋ 检索留痕三行 ＋ R1-R4 防幻觉'),
             ('C4 论证框架', '核心论证链完整 ＋ 大纲段落五元组预分配'),
             ('C5 材料填充', '五卡装配完整 ＋ 双向完整性核对'),
             ('C6 正式撰写', '每节强制操作 ＋ R-10 写入时检查 ＋ 作者姿态'),
             ('C7 净化', 'L1/L2 两层清稿 ＋ humanizer 双轨 ＋ L4 机检闸'),
             ('C8 格式校验', 'GB/T 7714 著录 ＋ AI 披露 ＋ 合卷'),
             ('C9 联合评审', '五席评审全过 ＋ 审稿立场三件套 ＋ 评分维度库'),
             ('C10 修改沟通', '审稿回复信 ＋ 证据绑定返修'),
             ('C11 最终精校', '三件套终检 ＋ 一致性全维核查')]
    gate_html = []
    for i, (g, check) in enumerate(gates):
        gid = '守门' + chr(0x2460 + i + 2)  # ③④⑤…⑬（与状态盘圈号口径一致）
        status = 'idle'
        for gname, ok in st['gates']:
            if gname == gid:
                status = 'pass' if ok else 'hold'
                break
        cls = {'pass': 'g-pass', 'hold': 'g-hold', 'idle': 'g-idle'}[status]
        lab = {'pass': '已过', 'hold': '挂起', 'idle': '未到'}[status]
        gate_html.append('<div class="gate %s" title="%s：%s"><i class="g-dot"></i><b>%s</b><span class="g-name">%s</span><span class="g-lab">%s</span></div>'
                         % (cls, gid, check, gid, g, lab))

    # 引擎台账
    eng_html = []
    if eng:
        for e in eng:
            badge = ev_badge(e['ev'])
            eng_html.append('<tr><td class="mono"><i class="bd bd-%s"></i>%s</td><td>%s</td><td>%s</td><td class="ev">%s</td></tr>'
                            % (badge, esc(e['name']), esc(e['dev']), esc(e['lic']), esc(e['ev'])))
    else:
        eng_html.append('<tr><td colspan="4" class="empty">台账未找到转正在用引擎（检查 data/skill-tracker.md）</td></tr>')

    # M 库卡（按 01-16 顺序，卡名含适用工序）
    cards_html = []
    if cards:
        for c in cards:
            cards_html.append('<span class="chip">%s</span>' % esc(c['title']))
    else:
        cards_html.append('<p class="empty">未扫描到方法卡（检查 references/methods/）</p>')

    # 状态盘原文
    raw_html = ''.join('<div class="rawln">%s</div>' % esc(l) for l in st['raw']) if has_state else ''

    # 当前工序高亮：四层横条
    layer = 'idle'
    if stage:
        layer = 'c' if stage.startswith('C') else stage[0].lower()
    layers_html = []
    for code, nm, tag, desc in (('O', '目标定向', 'Objective', '定位场景 · 锚定目标'),
                                ('S', '思考决策', 'Spirit', '论证锚定 · 拍板方向'),
                                ('C', '认知建构', 'Cognition', 'C1–C11 工序链'),
                                ('E', '经验共创', 'Experience', '沉淀 · 复盘 · 进化')):
        on = (code.lower() == layer)
        layers_html.append(
            '<div class="layer %s"><span class="l-ring">%s</span><b>%s</b><em>%s</em><small>%s</small>%s</div>'
            % ('l-on' if on else '', code, nm, tag, desc,
               '<i class="l-here">当前</i>' if on else ''))

    empty_card = ''
    if not has_state:
        empty_card = ('<div class="empty-card"><b>尚未检测到 .xingchan-state.md</b>'
                      'O2 定稿后星躔会落状态盘；若已有产物却无状态盘，先提示契约 5 未执行、从产物反推补盘，再看板即恢复。'
                      '也可用 <code>--state 路径</code> 指向已有状态盘。</div>')

    html = u'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>星躔 · 状态看板</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23e8b25c' d='M12 2l2.4 6.2L21 9l-5 4.2 1.6 6.8L12 16l-5.6 4L8 13.2 3 9l6.6-.8z'/%3E%3C/svg%3E">
<style>
:root{--bg:#070b1f;--panel:rgba(19,26,56,.72);--panel2:#141c40;--line:#2c376b;--line2:#3a4787;--tx:#eef1ff;--mut:#9aa6d8;--acc:#e8b25c;--acc2:#f6d68a;--ok:#4fd18e;--hold:#f0b64a;--warn:#e06c75;--mono:'Cascadia Mono','Consolas',ui-monospace,monospace;}
*{margin:0;padding:0;box-sizing:border-box}
html{background:var(--bg)}
body{font-family:'Microsoft YaHei','PingFang SC',system-ui,sans-serif;color:var(--tx);line-height:1.6;padding:0;min-height:100vh}
.sky{position:fixed;inset:0;z-index:0;pointer-events:none;background:
 radial-gradient(1200px 600px at 78% -10%,rgba(232,178,92,.10),transparent 60%),
 radial-gradient(900px 500px at 8% 18%,rgba(79,209,142,.05),transparent 60%),
 linear-gradient(180deg,#0a0f26 0%,#070b1f 55%,#0b1230 100%)}
.sky::before{content:'';position:absolute;inset:0;
 background-image:
  radial-gradient(1.4px 1.4px at 12% 22%,rgba(238,241,255,.55),transparent 55%),
  radial-gradient(1.2px 1.2px at 33% 11%,rgba(238,241,255,.4),transparent 55%),
  radial-gradient(1.6px 1.6px at 52% 26%,rgba(238,241,255,.5),transparent 55%),
  radial-gradient(1px 1px at 71% 9%,rgba(238,241,255,.35),transparent 55%),
  radial-gradient(1.3px 1.3px at 88% 19%,rgba(238,241,255,.45),transparent 55%),
  radial-gradient(1px 1px at 22% 63%,rgba(238,241,255,.3),transparent 55%),
  radial-gradient(1.5px 1.5px at 64% 52%,rgba(238,241,255,.35),transparent 55%),
  radial-gradient(1.1px 1.1px at 44% 84%,rgba(238,241,255,.3),transparent 55%),
  radial-gradient(1.4px 1.4px at 82% 74%,rgba(238,241,255,.4),transparent 55%),
  radial-gradient(1.2px 1.2px at 93% 41%,rgba(238,241,255,.35),transparent 55%),
  radial-gradient(1px 1px at 5% 88%,rgba(238,241,255,.25),transparent 55%);
 opacity:.7}
.wrap{position:relative;z-index:1;max-width:1100px;margin:0 auto;padding:22px 18px 44px}
.hero{display:flex;justify-content:space-between;align-items:flex-end;gap:14px;flex-wrap:wrap;padding-bottom:16px;border-bottom:1px solid var(--line);position:relative}
.hero::after{content:'';position:absolute;left:0;bottom:-1px;width:120px;height:2px;background:linear-gradient(90deg,var(--acc),transparent)}
.hero h1{font-size:26px;font-weight:800;letter-spacing:1px;line-height:1.25}
.hero h1 .zh{color:var(--acc2)}
.hero .sub{font-size:13px;color:var(--mut);margin-top:4px}
.hero .sub b{color:#c6cff2;font-weight:600}
.stamp{font-family:var(--mono);font-size:12px;color:var(--mut);display:flex;align-items:center;gap:7px;padding:6px 12px;border:1px solid var(--line);border-radius:999px;background:var(--panel)}
.stamp i{width:6px;height:6px;border-radius:50%;background:var(--acc);box-shadow:0 0 8px var(--acc)}
.empty-card{background:rgba(224,108,117,.09);border:1px solid var(--warn);color:#f3c2c6;border-radius:12px;padding:14px 16px;font-size:13px;margin-top:18px;line-height:1.75}
.empty-card b{display:block;margin-bottom:4px;color:#ffd7da}
.empty-card code{font-family:var(--mono);background:rgba(224,108,117,.15);padding:0 5px;border-radius:4px}
.head{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:18px}
.hcard{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px;position:relative;overflow:hidden;backdrop-filter:blur(4px)}
.hcard::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,var(--acc),transparent 60%)}
.hcard .k{font-size:12px;color:var(--mut);display:flex;align-items:center;gap:6px}
.hcard .k i{width:5px;height:5px;border-radius:50%;background:var(--acc);opacity:.8}
.hcard .v{font-size:17px;font-weight:700;margin-top:4px;word-break:break-all;color:var(--acc2)}
.hcard .v.plain{color:var(--tx)}
.hcard .gv{font-family:var(--mono);font-size:22px;font-weight:700;color:var(--acc)}
.prog{background:#0c1330;border-radius:7px;height:9px;margin-top:12px;overflow:hidden;border:1px solid var(--line)}
.prog i{display:block;height:100%;background:linear-gradient(90deg,var(--acc),var(--acc2));border-radius:7px;width:0%;box-shadow:0 0 10px rgba(232,178,92,.5)}
.sec{margin-top:26px}
.sec-title{font-size:15px;font-weight:700;display:flex;align-items:center;gap:9px;margin-bottom:12px;color:var(--acc2)}
.sec-title .no{font-family:var(--mono);font-size:11px;color:var(--acc);border:1px solid var(--line2);border-radius:6px;padding:2px 7px;letter-spacing:1px}
.sec-title::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,var(--line),transparent)}
.layers{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;position:relative}
.layers::before{content:'';position:absolute;top:34px;left:6%;right:6%;height:1px;background:linear-gradient(90deg,var(--line2),var(--line2));z-index:0}
.layer{position:relative;z-index:1;border:1px solid var(--line);border-radius:14px;padding:16px 14px 14px;text-align:center;background:var(--panel);backdrop-filter:blur(4px);transition:transform .18s ease,border-color .18s ease}
.layer:hover{transform:translateY(-2px);border-color:var(--line2)}
.l-ring{width:42px;height:42px;margin:0 auto 8px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:17px;font-weight:700;color:var(--mut);border:1px solid var(--line2);background:#0c1330;position:relative}
.layer b{display:block;font-size:16px;font-weight:700}
.layer em{display:block;font-size:11px;color:var(--mut);font-style:normal;letter-spacing:2px;text-transform:uppercase;margin:2px 0 6px}
.layer small{display:block;font-size:12px;color:var(--mut);line-height:1.5}
.l-on{border-color:var(--acc);background:linear-gradient(180deg,rgba(232,178,92,.10),rgba(19,26,56,.85));box-shadow:0 0 24px rgba(232,178,92,.12)}
.l-on .l-ring{color:#1c1405;background:var(--acc);border-color:var(--acc);box-shadow:0 0 16px rgba(232,178,92,.55)}
.l-on b{color:var(--acc2)}
.l-here{display:inline-block;margin-top:8px;font-size:11px;font-style:normal;color:#1c1405;background:var(--acc);border-radius:999px;padding:1px 10px;font-weight:700;letter-spacing:1px}
.gates{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}
.gate{display:flex;align-items:center;gap:7px;border:1px solid var(--line);border-radius:11px;padding:10px 12px;font-size:12px;background:var(--panel);backdrop-filter:blur(4px);min-width:0}
.g-dot{width:9px;height:9px;border-radius:50%;flex:none}
.g-pass{border-color:#24463a;background:rgba(79,209,142,.05)}
.g-pass .g-dot{background:var(--ok);box-shadow:0 0 9px rgba(79,209,142,.7)}
.g-hold{border-color:#5c4d22;background:rgba(240,182,74,.06)}
.g-hold .g-dot{background:var(--hold);box-shadow:0 0 9px rgba(240,182,74,.6)}
.g-idle{border-color:var(--line);background:var(--panel)}
.g-idle .g-dot{background:#33407a}
.gate b{font-family:var(--mono);font-size:12px;color:var(--acc2);flex:none}
.g-name{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--mut)}
.g-lab{font-size:11px;border-radius:999px;padding:1px 8px;white-space:nowrap;flex:none}
.g-pass .g-lab{background:rgba(79,209,142,.16);color:var(--ok)}
.g-hold .g-lab{background:rgba(240,182,74,.16);color:var(--hold)}
.g-idle .g-lab{background:#28325f;color:var(--mut)}
.tbl-wrap{overflow-x:auto}
.tbl{width:100%;border-collapse:collapse;font-size:13px;table-layout:fixed}
.tbl th,.tbl td{border-bottom:1px solid var(--line);padding:11px 12px;text-align:left;vertical-align:top;word-break:break-all}
.tbl th{color:var(--mut);font-weight:500;font-size:12px;background:var(--panel2);letter-spacing:.5px}
.tbl td{background:transparent}
.tbl tbody tr{transition:background .15s ease}
.tbl tbody tr:hover{background:rgba(232,178,92,.05)}
.tbl td.mono{font-family:var(--mono);font-size:12px;color:var(--acc2)}
.tbl td.ev{color:var(--mut);font-size:12px}
.bd{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:8px;vertical-align:middle}
.bd-green{background:var(--ok);box-shadow:0 0 7px rgba(79,209,142,.6)}
.bd-amber{background:var(--hold);box-shadow:0 0 7px rgba(240,182,74,.55)}
.bd-grey{background:#46538f}
.tabs{display:flex;gap:8px;margin-bottom:0}
.tab{border:1px solid var(--line);background:var(--panel);color:var(--mut);border-radius:10px 10px 0 0;padding:9px 18px;font-size:13px;cursor:pointer;font-family:inherit;letter-spacing:.5px;transition:all .15s ease}
.tab:hover{color:var(--tx);border-color:var(--line2)}
.tab.on{background:var(--acc);color:#241a05;border-color:var(--acc);font-weight:700;box-shadow:0 -4px 14px rgba(232,178,92,.15)}
.pane{background:var(--panel);border:1px solid var(--line);border-radius:0 12px 12px 12px;padding:16px;backdrop-filter:blur(4px)}
.pane.hidden{display:none}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{font-size:12px;border:1px solid var(--line);background:#0c1330;border-radius:999px;padding:5px 13px;color:#c6cff2;transition:all .15s ease;cursor:default}
.chip:hover{border-color:var(--acc);color:var(--acc2)}
.kpi{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.kpi5{grid-template-columns:repeat(5,1fr)}
.kpi div{background:#0c1330;border:1px solid var(--line);border-radius:12px;padding:16px;text-align:center}
.kpi b{font-size:26px;display:block;color:var(--acc);font-family:var(--mono);font-weight:700}
.kpi span{font-size:12px;color:var(--mut)}
.kpi .ksub{font-size:11px;color:#5d6aa8;margin-top:4px}
.raw{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:12px 16px;overflow-x:auto}
.rawln{font-family:var(--mono);font-size:12px;color:var(--mut);border-bottom:1px dashed #232c55;padding:5px 0}
.rawln:last-child{border-bottom:none}
.empty{color:var(--mut);font-size:13px;padding:8px 0}
@media (max-width:900px){
 .head{grid-template-columns:repeat(2,1fr)}
 .gates{grid-template-columns:repeat(3,1fr)}
 .kpi5{grid-template-columns:repeat(3,1fr)}
}
@media (max-width:640px){
 .wrap{padding:16px 12px 36px}
 .hero h1{font-size:22px}
 .head,.kpi{grid-template-columns:1fr 1fr}
 .kpi5{grid-template-columns:repeat(2,1fr)}
 .gates{grid-template-columns:repeat(2,1fr)}
 .layers{grid-template-columns:repeat(2,1fr)}
 .layers::before{display:none}
 .tab{padding:8px 12px}
}
@media (prefers-reduced-motion:reduce){
 *{transition:none!important;box-shadow:none!important}
}
</style>
</head>
<body>
<div class="sky" aria-hidden="true"></div>
<div class="wrap">
<div class="hero">
  <div>
    <h1><span class="zh">星躔</span> · 状态看板</h1>
    <div class="sub">O–S–C–E 写作系统 · 运行轨迹 <b>@@MODE@@</b> 档</div>
  </div>
  <div class="stamp"><i></i>生成 @@NOW@@</div>
</div>
@@EMPTY@@
<div class="head">
  <div class="hcard"><div class="k"><i></i>当前工序</div><div class="v plain">@@STAGE@@</div></div>
  <div class="hcard"><div class="k"><i></i>守门进度</div><div class="gv">@@GATES@@</div>
    <div class="prog"><i style="width:@@GPCT@@%"></i></div></div>
  <div class="hcard" style="grid-column:span 2"><div class="k"><i></i>稿件</div><div class="v">@@TITLE@@</div></div>
</div>
<div class="sec">
  <div class="sec-title"><span class="no">PIPELINE</span>四层管线</div>
  <div class="layers">@@LAYERS_HTML@@</div>
</div>
<div class="sec">
  <div class="sec-title"><span class="no">GATES</span>守门链 · 学术档 11 道基准</div>
  <div class="gates">@@GATES_HTML@@</div>
</div>
<div class="sec">
  <div class="sec-title"><span class="no">ENGINES</span>引擎台账 · A 组转正在用</div>
  <div class="tbl-wrap"><table class="tbl"><colgroup><col style="width:26%"><col style="width:20%"><col style="width:16%"><col style="width:38%"></colgroup>
  <thead><tr><th>引擎</th><th>开发者</th><th>许可</th><th>实用证据</th></tr></thead>
  <tbody>@@ENG_HTML@@</tbody></table></div>
</div>
<div class="sec">
  <div class="sec-title"><span class="no">LIBRARY</span>三库与方法卡</div>
  <div class="tabs">
    <button class="tab on" type="button" onclick="showTab(0)">M 库方法卡 · @@KPI_M@@</button>
    <button class="tab" type="button" onclick="showTab(1)">三库速览</button>
  </div>
  <div class="pane" id="p0"><div class="chips">@@CARDS_HTML@@</div></div>
  <div class="pane hidden" id="p1"><div class="kpi">
    <div><b>L1–L5</b><span>K 库知识库</span><div class="ksub">词法区 · 正反库 · 机检闸</div></div>
    <div><b>@@KPI_M@@</b><span>M 库方法卡</span><div class="ksub">references/methods/</div></div>
    <div><b>@@KPI_T@@</b><span>T 库工具箱</span><div class="ksub">注册表 · 待加载清单</div></div>
  </div></div>
</div>
<div class="sec">
  <div class="sec-title"><span class="no">EVOLVE</span>系统进化 · E 层沉淀</div>
  <div class="kpi kpi5">
    <div><b>@@RULES@@</b><span>规则库条目</span><div class="ksub">rule-base · 条件化启发式</div></div>
    <div><b>@@FAIL@@</b><span>失败档</span><div class="ksub">failure-archive · 教训留痕</div></div>
    <div><b>@@NOGO@@</b><span>不做清单</span><div class="ksub">no-go-list · 决策禁区</div></div>
    <div><b>@@GAPS@@</b><span>引擎缺口</span><div class="ksub">engine-gaps · 降级声明</div></div>
    <div><b>@@PEND@@</b><span>待载候选</span><div class="ksub">T 库 · 转正四步前</div></div>
  </div>
</div>
<div class="sec">
  <div class="sec-title"><span class="no">STATE</span>状态盘原文 · 前 40 行</div>
  <div class="raw">@@RAW_HTML@@<div class="rawln" style="border:none;color:#5d6aa8">— 共 @@RAW_N@@ 行 ——</div></div>
</div>
</div>
<script>
function showTab(i){var t=document.querySelectorAll('.tab');var p=document.querySelectorAll('.pane');for(var k=0;k<t.length;k++){t[k].classList.toggle('on',k===i);p[k].classList.toggle('hidden',k!==i);}}
</script>
</body>
</html>'''

    gnum = len(gates)
    gpct = round(passed_gates * 100.0 / gnum) if gnum else 0
    kpi_t = '—'
    tfile = os.path.join(XC, 'references', 'T工具箱_待加载清单.md')
    if os.path.exists(tfile):
        kpi_t = str(sum(1 for l in io.open(tfile, encoding='utf-8') if l.startswith('## 待载')))
    sysd = parse_system()
    reps = {
        '@@NOW@@': now, '@@EMPTY@@': empty_card,
        '@@MODE@@': mode, '@@STAGE@@': stage, '@@TITLE@@': title, '@@GATES@@': gate_txt,
        '@@GPCT@@': str(gpct),
        '@@LAYERS_HTML@@': ''.join(layers_html),
        '@@GATES_HTML@@': ''.join(gate_html), '@@ENG_HTML@@': ''.join(eng_html),
        '@@CARDS_HTML@@': ''.join(cards_html), '@@RAW_HTML@@': raw_html,
        '@@RAW_N@@': str(len(st['raw'])),
        '@@KPI_M@@': str(len(cards)), '@@KPI_T@@': kpi_t,
        '@@RULES@@': str(sysd['rules']), '@@FAIL@@': str(sysd['fail']),
        '@@NOGO@@': str(sysd['nogo']), '@@GAPS@@': str(sysd['gaps']),
        '@@PEND@@': str(sysd['pending']),
    }
    for k, v in reps.items():
        html = html.replace(k, v)
    return html


def main():
    state = DEFAULT_STATE
    out = DEFAULT_OUT
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == '--state' and i + 1 < len(args):
            state = args[i + 1]
        if a == '--out' and i + 1 < len(args):
            out = args[i + 1]
    st = parse_state(state)
    eng = parse_tracker()
    cards = parse_methods()
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    html = build_html(st, eng, cards, now)
    io.open(out, 'w', encoding='utf-8', newline='').write(html)
    print('state=%s eng=%d cards=%d gates=%d -> %s' % (
        'FOUND' if st['exists'] else 'MISSING', len(eng), len(cards), len(st['gates']), out))


if __name__ == '__main__':
    main()
