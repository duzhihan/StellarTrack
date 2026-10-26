# -*- coding: utf-8 -*-
"""星躔状态看板生成器（可选配套 · 丙型外延）
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


def build_html(st, eng, cards, now):
    has_state = st['exists']
    mode = esc(st['mode']) or '—'
    title = esc(st['title']) or '—'
    stage = esc(st['stage']) or '—'
    n_gate = len(st['gates'])
    passed_gates = sum(1 for _, ok in st['gates'] if ok)
    gate_txt = '%d/%d' % (passed_gates, n_gate) if n_gate else '0/0'

    # 守门链 11 道（学术档基准）
    gates = ['C1 选题', 'C2 材料建档', 'C3 综述·模型·引言', 'C4 论证框架', 'C5 材料填充',
             'C6 正式撰写', 'C7 净化', 'C8 格式校验', 'C9 联合评审', 'C10 修改沟通', 'C11 最终精校']
    gate_html = []
    for i, g in enumerate(gates):
        gid = '守门' + chr(0x2460 + i + 2)  # ③④⑤…⑬（与状态盘圈号口径一致）
        status = 'idle'
        for gname, ok in st['gates']:
            if gname == gid:
                status = 'pass' if ok else 'hold'
                break
        cls = {'pass': 'g-pass', 'hold': 'g-hold', 'idle': 'g-idle'}[status]
        lab = {'pass': '已过', 'hold': '挂起', 'idle': '未到'}[status]
        gate_html.append('<div class="gate %s"><b>%s</b><span class="g-lab">%s</span></div>' % (cls, gid, lab))

    # 引擎台账
    eng_html = []
    if eng:
        for e in eng:
            eng_html.append('<tr><td class="mono">%s</td><td>%s</td><td>%s</td><td class="ev">%s</td></tr>'
                            % (esc(e['name']), esc(e['dev']), esc(e['lic']), esc(e['ev'])))
    else:
        eng_html.append('<tr><td colspan="4" class="empty">台账未找到转正在用引擎（检查 data/skill-tracker.md）</td></tr>')

    # M 库卡
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
    lcls = {'o': 'l-o', 's': 'l-s', 'c': 'l-c', 'e': 'l-e'}.get(layer, 'l-idle')

    empty_card = ''
    if not has_state:
        empty_card = ('<div class="empty-card">尚未检测到 <code>.xingchan-state.md</code>。'
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
:root{--bg:#0b1026;--panel:#131a38;--panel2:#1a2347;--line:#2a3566;--tx:#e8ecfb;--mut:#9aa6d8;--acc:#e8b25c;--ok:#4fd18e;--hold:#f0b64a;--warn:#e06c75;--mono:'Cascadia Mono','Consolas',ui-monospace,monospace;}
*{margin:0;padding:0;box-sizing:border-box}
html{background:var(--bg)}
body{font-family:'Microsoft YaHei','PingFang SC',system-ui,sans-serif;color:var(--tx);line-height:1.55;padding:16px;max-width:1080px;margin:0 auto}
h1{font-size:20px;font-weight:700;letter-spacing:.5px}
h1 small{color:var(--mut);font-weight:400;font-size:13px;margin-left:10px}
h2{font-size:15px;font-weight:700;margin:22px 0 10px;display:flex;align-items:center;gap:8px}
h2::before{content:'';width:4px;height:14px;background:var(--acc);border-radius:2px;display:inline-block}
.top{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.top .stamp{font-family:var(--mono);font-size:12px;color:var(--mut)}
.head{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-top:14px}
.hcard{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:12px 14px}
.hcard .k{font-size:12px;color:var(--mut)}
.hcard .v{font-size:16px;font-weight:600;margin-top:2px;word-break:break-all}
.prog{background:var(--panel2);border-radius:6px;height:10px;margin-top:10px;overflow:hidden;border:1px solid var(--line)}
.prog i{display:block;height:100%;background:linear-gradient(90deg,var(--acc),#f6d68a);border-radius:6px;width:0%}
.empty-card{background:rgba(224,108,117,.08);border:1px solid var(--warn);color:#f0b9bc;border-radius:10px;padding:12px 14px;font-size:13px;margin-top:14px;line-height:1.7}
.layers{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:14px}
.layer{border:1px solid var(--line);border-radius:10px;padding:12px;background:var(--panel);text-align:center}
.layer b{display:block;font-size:15px}
.layer span{font-size:12px;color:var(--mut)}
.layer.l-c{background:linear-gradient(180deg,var(--panel),#243055);border-color:var(--acc)}
.layer.l-c b,.layer.l-c span{color:#ffe9bd}
.gates{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:6px}
.gate{border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:12px;display:flex;justify-content:space-between;align-items:center;gap:4px}
.gate b{font-family:var(--mono);font-size:12px}
.gate .g-lab{font-size:11px;border-radius:4px;padding:1px 6px;white-space:nowrap}
.g-pass{border-color:#2b5c47;background:rgba(79,209,142,.06)}
.g-pass .g-lab{background:var(--ok);color:#04230f}
.g-hold{border-color:#6a5a26;background:rgba(240,182,74,.07)}
.g-hold .g-lab{background:var(--hold);color:#33260a}
.g-idle{border-color:var(--line);background:var(--panel)}
.g-idle .g-lab{background:#2a3566;color:var(--mut)}
.tbl{width:100%;border-collapse:collapse;font-size:13px;margin-top:6px;table-layout:fixed}
.tbl th,.tbl td{border-bottom:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top;word-break:break-all}
.tbl th{color:var(--mut);font-weight:500;font-size:12px;background:var(--panel2)}
.tbl td.mono,.tbl .mono{font-family:var(--mono);font-size:12px}
.tbl td.ev{color:var(--mut);font-size:12px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.chip{font-size:12px;border:1px solid var(--line);background:var(--panel);border-radius:999px;padding:3px 10px;color:#c6cff2}
.empty{color:var(--mut);font-size:13px;padding:8px 0}
.rawln{font-family:var(--mono);font-size:12px;color:var(--mut);border-bottom:1px dashed #232c55;padding:4px 0}
.kpi{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:6px}
.kpi div{background:var(--panel2);border:1px solid var(--line);border-radius:8px;padding:10px;text-align:center}
.kpi b{font-size:18px;display:block;color:var(--acc)}
.kpi span{font-size:12px;color:var(--mut)}
.tabs{display:flex;gap:6px;margin-top:6px}
.tab{border:1px solid var(--line);background:var(--panel);color:var(--tx);border-radius:8px 8px 0 0;padding:7px 14px;font-size:13px;cursor:pointer;font-family:inherit}
.tab.on{background:var(--acc);color:#2b2106;border-color:var(--acc);font-weight:600}
.tabpane{display:none}
.tabpane.on{display:block}
@media (max-width:640px){
 body{padding:10px}
 .head,.kpi{grid-template-columns:1fr 1fr}
 .gates{grid-template-columns:repeat(2,1fr)}
 .layers{grid-template-columns:repeat(2,1fr)}
}
</style>
</head>
<body>
<div class="top"><h1>星躔 · 状态看板<small>O-S-C-E 写作系统</small></h1><div class="stamp">生成 @@@NOW@@@</div></div>
@@EMPTY@@
<div class="head">
  <div class="hcard"><div class="k">档位</div><div class="v">@@MODE@@</div></div>
  <div class="hcard"><div class="k">当前工序</div><div class="v">@@STAGE@@</div></div>
  <div class="hcard"><div class="k">稿件</div><div class="v">@@TITLE@@</div></div>
  <div class="hcard"><div class="k">守门进度</div><div class="v">@@GATES@@</div>
    <div class="prog"><i style="width:@@GPCT@@%"></i></div></div>
</div>
<h2>四层管线</h2>
<div class="layers">
  <div class="layer @@LCLS@@"><b>O 目标定向</b><span>定位场景·锚定目标</span></div>
  <div class="layer @@LCLS@@"><b>S 思考决策</b><span>论证锚定·拍板方向</span></div>
  <div class="layer @@LCLS@@"><b>C 认知建构</b><span>C1–C11 工序链</span></div>
  <div class="layer @@LCLS@@"><b>E 经验共创</b><span>沉淀·复盘·进化</span></div>
</div>
<h2>守门链（学术档 11 道基准）</h2>
<div class="gates">@@GATES_HTML@@</div>
<h2>引擎台账（A 组转正在用）</h2>
<div class="tbl-wrap"><table class="tbl"><colgroup><col style="width:26%"><col style="width:20%"><col style="width:16%"><col style="width:38%"></colgroup>
<thead><tr><th>引擎</th><th>开发者</th><th>许可</th><th>实用证据</th></tr></thead>
<tbody>@@ENG_HTML@@</tbody></table></div>
<div class="tabs" role="tablist">
  <button class="tab on" onclick="showTab(0)">M 库方法卡</button>
  <button class="tab" onclick="showTab(1)">三库速览</button>
</div>
<div class="tabpane on" id="tp0"><div class="chips">@@CARDS_HTML@@</div></div>
<div class="tabpane" id="tp1"><div class="kpi">
  <div><b>@@KPI_K@@</b><span>K 库知识库</span></div>
  <div><b>@@KPI_M@@</b><span>M 库方法卡</span></div>
  <div><b>@@KPI_T@@</b><span>T 库工具箱</span></div>
</div></div>
<h2>状态盘原文（前 40 行）</h2>
<div>@@RAW_HTML@@</div>
<script>
function showTab(i){var b=document.querySelectorAll('.tab');var p=document.querySelectorAll('.tabpane');for(var k=0;k<b.length;k++){b[k].classList.toggle('on',k===i);p[k].classList.toggle('on',k===i);}}
</script>
</body>
</html>'''

    gnum = len(gates)
    gpct = round(passed_gates * 100.0 / gnum) if gnum else 0
    kpi_k = '—'; kpi_t = '—'
    tfile = os.path.join(XC, 'references', 'T工具箱_待加载清单.md')
    if os.path.exists(tfile):
        kpi_t = str(sum(1 for l in io.open(tfile, encoding='utf-8') if l.startswith('## 待载')))
    kfile = os.path.join(XC, 'references', 'ai-vocabulary-filter.md')
    if os.path.exists(kfile):
        kpi_k = 'L1-L5'
    reps = {
        '@@NOW@@': now, '@@EMPTY@@': empty_card,
        '@@MODE@@': mode, '@@STAGE@@': stage, '@@TITLE@@': title, '@@GATES@@': gate_txt,
        '@@GPCT@@': str(gpct), '@@LCLS@@': lcls,
        '@@GATES_HTML@@': ''.join(gate_html), '@@ENG_HTML@@': ''.join(eng_html),
        '@@CARDS_HTML@@': ''.join(cards_html), '@@RAW_HTML@@': raw_html,
        '@@KPI_K@@': kpi_k, '@@KPI_M@@': str(len(cards)), '@@KPI_T@@': kpi_t,
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
