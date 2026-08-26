#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文风量化分析脚本 — Style Analyzer
对文本进行 15 维度量化分析，输出 JSON 格式风格报告。

用法：
    python style_analyzer.py --file <文本文件路径> [--output json|text]
    python style_analyzer.py --text <直接输入文本> [--output json|text]
    python style_analyzer.py --compare <文件1> <文件2>  # 对比两个文本
"""

import re
import sys
import json
import math
import argparse
from collections import Counter
from pathlib import Path


# ── 文言虚词/古语词库 ──
CLASSICAL_WORDS = set("之乎者也矣焉哉欤兮耳耶而乃其以于与则因故虽然若使非".split())
CLASSICAL_PATTERNS = [
    r'之\w', r'以\w{2}', r'所\w', r'为\w{2}所', r'不\w{2}不',
    r'而\w{2}', r'其\w{2}', r'乃\w', r'于\w{2}'
]

# ── 网络用语/口语标记 ──
NET_WORDS = {
    '真的', '绝了', '太可', '了吧', '爆款', '炸裂', '封神',
    '上头', '下头', '破防', '摆烂', '内卷', '躺平', 'emo',
    'yyds', 'nb', '栓Q', '绝绝子', '拿捏', '种草', '拔草',
}
ORAL_MARKERS = set("的了呢吗吧啊呀哇嘛呗".split())

# ── 学术术语种子（传播学/艺术学/哲学/媒介学） ──
# 分为高频通用词（日常文本也常见，权重×0.3）和低频学科词（权重×1.0）
ACADEMIC_SEEDS_HIGHFREQ = re.compile(
    r'(?:结构|功能|系统|模式|现象|逻辑|变量|指标|参数)'
)
ACADEMIC_SEEDS_LOWFREQ = re.compile(
    r'(?:传播|媒介|叙事|话语|主体|客体|范式|机制|框架|维度|视角|'
    r'语境|场域|编码|解码|认同|建构|解构|重构|异化|规训|资本|惯习|本体|认识|'
    r'本质|辩证|因果|阈值|模型|算法)'
)
ACADEMIC_PATTERN = re.compile('|'.join([
    r'(?:传播|媒介|叙事|话语|主体|客体|范式|结构|功能|系统|机制|模式|框架|维度|视角',
    r'语境|场域|编码|解码|认同|建构|解构|重构|异化|规训|资本|场域|惯习|本体|认识',
    r'现象|本质|辩证|逻辑|因果|变量|指标|参数|阈值|模型|算法)'
]))

# ── 修辞标记 ──
METAPHOR_MARKERS = re.compile(r'如同|仿佛|好像|像是|好比|宛若|犹如|似|化作|成了|就是.*的')
PARALLELISM_MARKERS = re.compile(r'(?:[^。！？\n]+[，；][^。！？\n]+[，；][^。！？\n]+[。！？\n])')
RHETORICAL_QUESTION = re.compile(r'(?:难道|何以|如何|为何|怎能|岂|怎[么能])')
HYPOPHORA = re.compile(r'(?:什么是|什么叫|何为|什么是.*呢.*是|.*吗.*不)')
IRONY_MARKERS = re.compile(r'(?:所谓|号称|美其名曰|正人君子|堂堂|居然|竟然|可真是)')

# ── 情感词库 ──
POSITIVE_WORDS = set("美好温暖幸福快乐感动热爱希望光明辉煌灿烂卓越伟大精彩".split())
NEGATIVE_WORDS = set("痛苦悲伤绝望恐惧愤怒焦虑压抑黑暗失落失败残酷冷漠悲哀".split())
INTENSIFIERS = set("非常极其格外特别十分极度绝顶万分无比".split())

# ── 逻辑连接词 ──
LOGIC_CONNECTORS = {
    '因果': re.compile(r'(?:因为|所以|因此|由于|故而|于是|从而|致使|导致)'),
    '转折': re.compile(r'(?:但是|然而|可是|不过|却|而|反倒|反而)'),
    '让步': re.compile(r'(?:虽然|尽管|即使|即便|哪怕|固然|纵使)'),
    '递进': re.compile(r'(?:不仅|不但|而且|况且|何况|更|甚至|进而)'),
    '并列': re.compile(r'(?:一方面|另一方面|同时|与此同时|此外|另外|再者)'),
    '条件': re.compile(r'(?:如果|假如|倘若|只要|只有|除非|无论)'),
}

# ── 引用模式 ──
CITATION_PATTERNS = {
    'named': re.compile(r'(?:[^\s]{2,4}[（(]\d{4}[）)])|(?:[A-Z][a-z]+[（(]\d{4}[）)])'),
    'bracket_quote': re.compile(r'「[^」]+」'),
    'western_quote': re.compile(r'"[^"]{10,}"'),
    'concept_quote': re.compile(r'(?:所谓的|即|就是说|也就是说|指的是)'),
}

# ── 人称模式 ──
PERSON_PATTERNS = {
    'explicit_i': re.compile(r'(?:我认为|我觉得|笔者|在我看来|就我而言|个人认为)'),
    'implicit_i': re.compile(r'(?:应当|必须|不可|显然|无疑|值得注意)'),
    'we_community': re.compile(r'(?:我们|学界|研究者们|学术界)'),
}


def load_text(filepath=None, direct_text=None):
    """加载文本"""
    if direct_text:
        return direct_text
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    return None


def split_sentences(text):
    """分句（分号是句中停顿，不作为句末标点）"""
    sentences = re.split(r'[。！？\n]+', text)
    return [s.strip() for s in sentences if s.strip() and len(s.strip()) > 2]


def split_paragraphs(text):
    """分段"""
    paragraphs = re.split(r'\n\s*\n', text)
    return [p.strip() for p in paragraphs if p.strip() and len(p.strip()) > 20]


def count_chars(text):
    """统计中文字符数（不含标点和空白）"""
    return len(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))


def count_words(text):
    """统计词数（中文按字符近似，英文按空格）"""
    chinese_chars = len(re.findall(r'[\u4e00-\u9fff\u3400-\u4dbf]', text))
    english_words = len(re.findall(r'[a-zA-Z]+', text))
    return chinese_chars + english_words


# ══════════════════════════════════════════════
#  L1 表层特征分析
# ══════════════════════════════════════════════

def analyze_sentence_length(sentences):
    """1. 句长特征"""
    if not sentences:
        return {'mean': 0, 'std': 0, 'median': 0, 'min': 0, 'max': 0, 'score': 0, 'desc': '无数据'}
    
    lengths = [count_chars(s) for s in sentences]
    lengths.sort()
    n = len(lengths)
    mean_len = sum(lengths) / n
    std_len = (sum((l - mean_len) ** 2 for l in lengths) / n) ** 0.5
    median_len = lengths[n // 2] if n % 2 else (lengths[n//2 - 1] + lengths[n//2]) / 2
    
    # 评分
    if mean_len <= 15:
        score, desc = 1, '极短句主导'
    elif mean_len <= 25:
        score, desc = 2, '短句为主'
    elif mean_len <= 40:
        score, desc = 3, '中句为主'
    elif mean_len <= 60:
        score, desc = 4, '长句为主'
    else:
        score, desc = 5, '超长句主导'
    
    return {
        'mean': round(mean_len, 1),
        'std': round(std_len, 1),
        'median': round(median_len, 1),
        'min': lengths[0],
        'max': lengths[-1],
        'score': score,
        'desc': desc,
        'distribution': {
            'short_lt15': sum(1 for l in lengths if l < 15),
            'medium_15_40': sum(1 for l in lengths if 15 <= l <= 40),
            'long_40_60': sum(1 for l in lengths if 40 < l <= 60),
            'xlong_gt60': sum(1 for l in lengths if l > 60),
        }
    }


def analyze_paragraph_length(paragraphs):
    """2. 段落长度"""
    if not paragraphs:
        return {'mean_sentences': 0, 'score': 0, 'desc': '无数据'}
    
    para_sent_counts = []
    for para in paragraphs:
        sents = split_sentences(para)
        para_sent_counts.append(len(sents))
    
    mean_sents = sum(para_sent_counts) / len(para_sent_counts) if para_sent_counts else 0
    
    if mean_sents <= 3:
        score, desc = 1, '单句/短段为主'
    elif mean_sents <= 5:
        score, desc = 2, '短段为主'
    elif mean_sents <= 10:
        score, desc = 3, '中段为主'
    elif mean_sents <= 15:
        score, desc = 4, '长段为主'
    else:
        score, desc = 5, '超长段'
    
    return {
        'mean_sentences_per_para': round(mean_sents, 1),
        'paragraph_count': len(paragraphs),
        'score': score,
        'desc': desc,
    }


def analyze_punctuation(text):
    """3. 标点习惯"""
    total_chars = count_chars(text)
    if total_chars == 0:
        return {}
    
    comma_count = text.count('，') + text.count(',')
    semicolon_count = text.count('；') + text.count(';')
    dash_count = text.count('——') + text.count('—') + text.count('--')
    exclaim_count = text.count('！') + text.count('!')
    question_count = text.count('？') + text.count('?')
    bracket_quote_count = len(re.findall(r'「[^」]*」', text))
    western_quote_count = len(re.findall(r'"[^"]*"', text))
    
    # 每千字密度
    scale = total_chars / 1000 if total_chars > 0 else 1
    
    return {
        'comma_per_kchars': round(comma_count / scale, 1),
        'semicolon_per_kchars': round(semicolon_count / scale, 1),
        'dash_per_kchars': round(dash_count / scale, 1),
        'exclaim_per_kchars': round(exclaim_count / scale, 1),
        'question_per_kchars': round(question_count / scale, 1),
        'bracket_quote_count': bracket_quote_count,
        'western_quote_count': western_quote_count,
    }


def analyze_vocabulary_register(text):
    """4. 词汇层级"""
    total_chars = count_chars(text)
    if total_chars == 0:
        return {}
    
    # 文言比率
    classical_count = sum(1 for c in text if c in CLASSICAL_WORDS)
    classical_ratio = classical_count / total_chars
    
    # 口语标记率
    oral_count = sum(1 for c in text if c in ORAL_MARKERS)
    oral_ratio = oral_count / total_chars
    
    # 学术术语密度（加权：高频通用词×0.3，低频学科词×1.0）
    highfreq_hits = len(ACADEMIC_SEEDS_HIGHFREQ.findall(text))
    lowfreq_hits = len(ACADEMIC_SEEDS_LOWFREQ.findall(text))
    weighted_academic_hits = highfreq_hits * 0.3 + lowfreq_hits * 1.0
    academic_density = weighted_academic_hits / (total_chars / 1000) if total_chars > 0 else 0
    
    # 网络用语率
    net_count = sum(1 for w in NET_WORDS if w in text)
    net_ratio = net_count / total_chars if total_chars > 0 else 0
    
    return {
        'classical_ratio': round(classical_ratio, 4),
        'oral_ratio': round(oral_ratio, 4),
        'academic_term_density': round(academic_density, 2),
        'net_ratio': round(net_ratio, 4),
    }


def analyze_modal_particles(text):
    """5. 语气词与虚词密度"""
    total_chars = count_chars(text)
    if total_chars == 0:
        return {'score': 0, 'desc': '无数据'}
    
    modal_count = sum(1 for c in text if c in ORAL_MARKERS)
    density = modal_count / (total_chars / 1000) if total_chars > 0 else 0
    
    if density < 2:
        score, desc = 1, '极克制'
    elif density < 5:
        score, desc = 2, '克制'
    elif density < 10:
        score, desc = 3, '适度'
    elif density < 20:
        score, desc = 4, '频繁'
    else:
        score, desc = 5, '高频'
    
    return {'density_per_kchars': round(density, 1), 'score': score, 'desc': desc}


# ══════════════════════════════════════════════
#  L2 中层技法分析
# ══════════════════════════════════════════════

def analyze_rhetorical_devices(text):
    """6. 修辞密度"""
    total_kchars = max(count_chars(text) / 1000, 0.001)
    
    metaphor_hits = len(METAPHOR_MARKERS.findall(text))
    parallelism_hits = len(PARALLELISM_MARKERS.findall(text))
    rhetorical_q_hits = len(RHETORICAL_QUESTION.findall(text))
    hypophora_hits = len(HYPOPHORA.findall(text))
    irony_hits = len(IRONY_MARKERS.findall(text))
    
    total_devices = metaphor_hits + parallelism_hits + rhetorical_q_hits + hypophora_hits + irony_hits
    density = total_devices / total_kchars
    
    return {
        'total_per_kchars': round(density, 2),
        'breakdown': {
            'metaphor': round(metaphor_hits / total_kchars, 2),
            'parallelism': round(parallelism_hits / total_kchars, 2),
            'rhetorical_question': round(rhetorical_q_hits / total_kchars, 2),
            'hypophora': round(hypophora_hits / total_kchars, 2),
            'irony': round(irony_hits / total_kchars, 2),
        }
    }


def analyze_emotional_temperature(text):
    """7. 情感温度"""
    total_chars = count_chars(text)
    if total_chars == 0:
        return {'score': 0, 'desc': '中性'}
    
    pos_count = sum(1 for w in POSITIVE_WORDS if w in text)
    neg_count = sum(1 for w in NEGATIVE_WORDS if w in text)
    intensifier_count = sum(1 for w in INTENSIFIERS if w in text)
    exclaim_count = text.count('！') + text.count('!')
    
    # 情感倾向值 (-2 到 +2)
    net_sentiment = pos_count - neg_count
    intensity = intensifier_count + exclaim_count
    
    # 综合评分（修复：处理 net_sentiment==0 的边界情况）
    if net_sentiment == 0:
        # 中性情感 + 高感叹号 → 偏向激昂（如演讲、新媒体）
        if intensity > 10:
            raw_score = 1
        elif intensity > 5:
            raw_score = 0
        else:
            raw_score = 0  # 低强度中性 → 冷峻克制倾向
    elif intensity > 15:
        raw_score = 2 if net_sentiment > 0 else -2
    elif intensity > 8:
        raw_score = 1 if net_sentiment > 0 else (-1 if net_sentiment < 0 else 0)
    elif intensity > 3:
        raw_score = 1 if net_sentiment > 3 else (-1 if net_sentiment < -3 else 0)
    else:
        raw_score = 0 if abs(net_sentiment) < 2 else (1 if net_sentiment > 0 else -1)
    
    desc_map = {-2: '冷峻克制', -1: '冷静理性', 0: '中性均衡', 1: '温情热忱', 2: '激昂炽烈'}
    
    return {
        'positive_words': pos_count,
        'negative_words': neg_count,
        'intensifier_count': intensifier_count,
        'exclaim_count': exclaim_count,
        'score': raw_score,
        'desc': desc_map.get(raw_score, '中性'),
    }


def analyze_logic_density(text):
    """8. 逻辑密度"""
    total_sentences = max(len(split_sentences(text)), 1)
    
    logic_counts = {}
    total_logic = 0
    for name, pattern in LOGIC_CONNECTORS.items():
        count = len(pattern.findall(text))
        logic_counts[name] = count
        total_logic += count
    
    density = total_logic / total_sentences
    
    if density < 0.2:
        score, desc = 1, '直觉跳跃'
    elif density < 0.5:
        score, desc = 2, '简单因果'
    elif density < 0.8:
        score, desc = 3, '双链推理'
    elif density < 1.2:
        score, desc = 4, '多链嵌套'
    else:
        score, desc = 5, '体系化推理'
    
    return {
        'connectors_per_sentence': round(density, 2),
        'breakdown': logic_counts,
        'total_logic_markers': total_logic,
        'score': score,
        'desc': desc,
    }


def analyze_person_perspective(text):
    """9. 人称与视角"""
    explicit_i = len(PERSON_PATTERNS['explicit_i'].findall(text))
    implicit_i = len(PERSON_PATTERNS['implicit_i'].findall(text))
    we_community = len(PERSON_PATTERNS['we_community'].findall(text))
    
    total = explicit_i + implicit_i + we_community + 1
    
    if explicit_i > implicit_i and explicit_i > we_community:
        person_type = '显性"我"'
    elif implicit_i > explicit_i:
        person_type = '隐性"我"'
    elif we_community > explicit_i:
        person_type = '"我们"共同体'
    else:
        person_type = '全隐'
    
    return {
        'person_type': person_type,
        'explicit_i_count': explicit_i,
        'implicit_i_count': implicit_i,
        'we_community_count': we_community,
    }


def analyze_structure_pattern(text):
    """10. 结构模式（基于段落开头的模式识别）"""
    paragraphs = split_paragraphs(text)
    if not paragraphs:
        return {'pattern': '未识别', 'confidence': 0}
    
    first_words = []
    for p in paragraphs[:10]:  # 前10段
        sents = split_sentences(p)
        if sents:
            first_words.append(sents[0][:15])
    
    # 检测诊断式：现象→断裂→问题
    diagnostic_signals = 0
    for fw in first_words:
        if re.search(r'(?:当前|近年来|随着|在.*背景下)', fw):
            diagnostic_signals += 1
        if re.search(r'(?:然而|但是|不过|问题在于|遗憾的是)', fw):
            diagnostic_signals += 2
    
    # 检测总分式
    zongfen_signals = sum(1 for fw in first_words if re.search(r'(?:首先|第一|其一)', fw))
    
    # 检测递进式
    dijin_signals = sum(1 for fw in first_words if re.search(r'(?:进一步|更深|更.*的是)', fw))
    
    if diagnostic_signals >= 4:
        pattern = '诊断式'
        confidence = min(diagnostic_signals / 6, 1.0)
    elif zongfen_signals >= 2:
        pattern = '总分式'
        confidence = min(zongfen_signals / 4, 1.0)
    elif dijin_signals >= 2:
        pattern = '递进式'
        confidence = min(dijin_signals / 4, 1.0)
    else:
        pattern = '散点式/混合'
        confidence = 0.3
    
    return {'pattern': pattern, 'confidence': round(confidence, 2)}


# ══════════════════════════════════════════════
#  L3 深层基因分析
# ══════════════════════════════════════════════

def analyze_citation_pattern(text):
    """11. 知识引用模式"""
    named = len(CITATION_PATTERNS['named'].findall(text))
    bracket_quote = len(CITATION_PATTERNS['bracket_quote'].findall(text))
    western_quote = len(CITATION_PATTERNS['western_quote'].findall(text))
    
    if bracket_quote > named and bracket_quote > western_quote:
        mode = '隐名引述型'
    elif named > bracket_quote:
        mode = '具名对话型'
    elif western_quote > 0 and named == 0 and bracket_quote == 0:
        mode = '概念援引型'
    else:
        mode = '默默消化型'
    
    return {
        'mode': mode,
        'named_citations': named,
        'bracket_quotes': bracket_quote,
        'western_quotes': western_quote,
    }


def analyze_concept_creation(text):
    """12. 概念创造倾向"""
    # 检测自定义术语（「」或引号中的新概念）
    custom_terms = re.findall(r'「[^」]{2,10}」', text)
    custom_terms += re.findall(r'"[^"]{2,10}"', text)
    
    # 过滤掉明显的引用（含年份或学者名）
    filtered = [t for t in custom_terms if not re.search(r'\d{4}', t)]
    
    total_kchars = max(count_chars(text) / 1000, 0.001)
    density = len(filtered) / total_kchars
    
    if density < 0.5:
        score, desc = 1, '极少使用新概念'
    elif density < 1.5:
        score, desc = 2, '偶尔使用'
    elif density < 3:
        score, desc = 3, '适度创造'
    elif density < 5:
        score, desc = 4, '高度倾向'
    else:
        score, desc = 5, '概念生产力极高'
    
    return {
        'custom_terms': filtered[:10],  # 展示前10个
        'custom_term_count': len(filtered),
        'density_per_kchars': round(density, 2),
        'score': score,
        'desc': desc,
    }


def analyze_rhythm_pattern(text):
    """13. 节奏模式"""
    sentences = split_sentences(text)
    if len(sentences) < 5:
        return {'pattern': '样本不足', 'desc': '需要更多句子'}
    
    lengths = [count_chars(s) for s in sentences]
    
    # 计算句长变化系数
    if len(lengths) > 1:
        diffs = [abs(lengths[i+1] - lengths[i]) for i in range(len(lengths)-1)]
        avg_diff = sum(diffs) / len(diffs)
        mean_len = sum(lengths) / len(lengths)
        variation_coefficient = avg_diff / mean_len if mean_len > 0 else 0
    else:
        variation_coefficient = 0
    
    if variation_coefficient < 0.3:
        pattern, desc = '匀速型', '句长波动小，稳定推进'
    elif variation_coefficient < 0.6:
        pattern, desc = '起伏型', '长短交替，节奏丰富'
    else:
        # 检测加速/阻滞
        first_half = sum(lengths[:len(lengths)//2]) / max(len(lengths)//2, 1)
        second_half = sum(lengths[len(lengths)//2:]) / max(len(lengths) - len(lengths)//2, 1)
        if second_half < first_half * 0.7:
            pattern, desc = '加速型', '段落内句长渐缩'
        else:
            pattern, desc = '阻滞型', '长句密集，多停顿'
    
    return {
        'pattern': pattern,
        'desc': desc,
        'variation_coefficient': round(variation_coefficient, 2),
    }


def analyze_information_density(text):
    """14. 信息密度"""
    total_chars = count_chars(text)
    total_sentences = max(len(split_sentences(text)), 1)
    
    # 基于学术术语（加权）+ 逻辑连接词 + 专有名词的密度
    highfreq_hits = len(ACADEMIC_SEEDS_HIGHFREQ.findall(text))
    lowfreq_hits = len(ACADEMIC_SEEDS_LOWFREQ.findall(text))
    academic_hits = highfreq_hits * 0.3 + lowfreq_hits * 1.0
    logic_hits = sum(len(p.findall(text)) for p in LOGIC_CONNECTORS.values())
    proper_nouns = len(re.findall(r'[A-Z][a-z]+|[《「][^》」]+[》」]', text))
    
    info_markers = academic_hits + logic_hits + proper_nouns
    density = info_markers / total_sentences
    
    if density < 2:
        score, desc = 1, '低密度'
    elif density < 4:
        score, desc = 2, '中低密度'
    elif density < 6:
        score, desc = 3, '中等密度'
    elif density < 8:
        score, desc = 4, '高密度'
    else:
        score, desc = 5, '极高密度'
    
    return {
        'info_markers_per_sentence': round(density, 2),
        'score': score,
        'desc': desc,
    }


def analyze_cultural_dna(text):
    """15. 文化基因（初步检测）"""
    signals = {}
    
    # 地域色彩
    southern_markers = ['岭南', '粤', '广府', '潮汕', '客家', '珠三角']
    signals['southern_china'] = sum(1 for m in southern_markers if m in text)
    
    # 学科印记
    discipline_signals = {
        'communication': sum(1 for m in ['传播', '媒介', '受众', '议程', '框架'] if m in text),
        'art_studies': sum(1 for m in ['艺术', '美学', '审美', '戏曲', '非遗'] if m in text),
        'philosophy': sum(1 for m in ['主体', '客体', '本体', '现象', '存在'] if m in text),
        'digital_humanities': sum(1 for m in ['数字', '算法', 'AI', '智能', '平台'] if m in text),
    }
    signals.update(discipline_signals)
    
    # 代际标记
    gen_z_markers = sum(1 for m in ['Z世代', '00后', '破防', '上头', 'emo'] if m in text)
    signals['gen_z'] = gen_z_markers
    
    return signals


# ══════════════════════════════════════════════
#  综合报告
# ══════════════════════════════════════════════

def full_analysis(text):
    """执行全维度分析"""
    sentences = split_sentences(text)
    paragraphs = split_paragraphs(text)
    
    report = {
        'meta': {
            'total_chars': count_chars(text),
            'total_sentences': len(sentences),
            'total_paragraphs': len(paragraphs),
            'text_length': len(text),
        },
        'L1_surface': {
            '1_sentence_length': analyze_sentence_length(sentences),
            '2_paragraph_length': analyze_paragraph_length(paragraphs),
            '3_punctuation': analyze_punctuation(text),
            '4_vocabulary_register': analyze_vocabulary_register(text),
            '5_modal_particles': analyze_modal_particles(text),
        },
        'L2_technique': {
            '6_rhetorical_devices': analyze_rhetorical_devices(text),
            '7_emotional_temperature': analyze_emotional_temperature(text),
            '8_logic_density': analyze_logic_density(text),
            '9_person_perspective': analyze_person_perspective(text),
            '10_structure_pattern': analyze_structure_pattern(text),
        },
        'L3_deep': {
            '11_citation_pattern': analyze_citation_pattern(text),
            '12_concept_creation': analyze_concept_creation(text),
            '13_rhythm_pattern': analyze_rhythm_pattern(text),
            '14_information_density': analyze_information_density(text),
            '15_cultural_dna': analyze_cultural_dna(text),
        }
    }
    
    return report


def format_text_report(report):
    """格式化文本报告"""
    lines = []
    lines.append("=" * 60)
    lines.append("文风15维量化分析报告")
    lines.append("=" * 60)
    lines.append(f"\n文本规模：{report['meta']['total_chars']}字 | {report['meta']['total_sentences']}句 | {report['meta']['total_paragraphs']}段\n")
    
    # L1
    lines.append("── L1 表层特征 ──")
    l1 = report['L1_surface']
    
    sl = l1['1_sentence_length']
    lines.append(f"1. 句长特征 [{sl['score']}/5] {sl['desc']}")
    lines.append(f"   均值{sl['mean']}字 | 中位数{sl['median']}字 | 范围[{sl['min']}-{sl['max']}]")
    lines.append(f"   短句<15:{sl['distribution']['short_lt15']} | 中句15-40:{sl['distribution']['medium_15_40']} | 长句40-60:{sl['distribution']['long_40_60']} | 超长>60:{sl['distribution']['xlong_gt60']}")
    
    pl = l1['2_paragraph_length']
    lines.append(f"\n2. 段落长度 [{pl['score']}/5] {pl['desc']}")
    lines.append(f"   平均{pl['mean_sentences_per_para']}句/段 | 共{pl['paragraph_count']}段")
    
    punc = l1['3_punctuation']
    lines.append(f"\n3. 标点习惯")
    lines.append(f"   逗号{punc.get('comma_per_kchars','-')}/千字 | 分号{punc.get('semicolon_per_kchars','-')}/千字 | 破折号{punc.get('dash_per_kchars','-')}/千字")
    lines.append(f"   感叹号{punc.get('exclaim_per_kchars','-')}/千字 | 问号{punc.get('question_per_kchars','-')}/千字")
    lines.append(f"   「」引用{punc.get('bracket_quote_count','-')}处 | 西式引号{punc.get('western_quote_count','-')}处")
    
    vr = l1['4_vocabulary_register']
    lines.append(f"\n4. 词汇层级")
    lines.append(f"   文言比率:{vr.get('classical_ratio','-')} | 口语率:{vr.get('oral_ratio','-')} | 术语密度:{vr.get('academic_term_density','-')}/千字 | 网络用语率:{vr.get('net_ratio','-')}")
    
    mp = l1['5_modal_particles']
    lines.append(f"\n5. 语气词密度 [{mp['score']}/5] {mp['desc']} ({mp.get('density_per_kchars','-')}/千字)")
    
    # L2
    lines.append("\n── L2 中层技法 ──")
    l2 = report['L2_technique']
    
    rd = l2['6_rhetorical_devices']
    lines.append(f"6. 修辞密度: {rd['total_per_kchars']}次/千字")
    bd = rd['breakdown']
    lines.append(f"   比喻{bd['metaphor']} | 排比{bd['parallelism']} | 反问{bd['rhetorical_question']} | 设问{bd['hypophora']} | 反讽{bd['irony']}")
    
    et = l2['7_emotional_temperature']
    lines.append(f"\n7. 情感温度 [{et['score']:+d}] {et['desc']}")
    lines.append(f"   正面词{et['positive_words']} | 负面词{et['negative_words']} | 程度副词{et['intensifier_count']} | 感叹号{et['exclaim_count']}")
    
    ld = l2['8_logic_density']
    lines.append(f"\n8. 逻辑密度 [{ld['score']}/5] {ld['desc']} ({ld['connectors_per_sentence']}逻辑连接词/句)")
    
    pp = l2['9_person_perspective']
    lines.append(f"\n9. 人称视角: {pp['person_type']}")
    lines.append(f"   显性'我'{pp['explicit_i_count']} | 隐性'我'{pp['implicit_i_count']} | '我们'{pp['we_community_count']}")
    
    sp = l2['10_structure_pattern']
    lines.append(f"\n10. 结构模式: {sp['pattern']} (置信度{sp['confidence']})")
    
    # L3
    lines.append("\n── L3 深层基因 ──")
    l3 = report['L3_deep']
    
    cp = l3['11_citation_pattern']
    lines.append(f"11. 引用模式: {cp['mode']}")
    lines.append(f"    具名引用{cp['named_citations']} | 「」引用{cp['bracket_quotes']} | 西式引用{cp['western_quotes']}")
    
    cc = l3['12_concept_creation']
    lines.append(f"\n12. 概念创造倾向 [{cc['score']}/5] {cc['desc']}")
    lines.append(f"    自定义术语{cc['custom_term_count']}个 ({cc['density_per_kchars']}/千字)")
    if cc['custom_terms']:
        lines.append(f"    示例: {', '.join(cc['custom_terms'][:5])}")
    
    rp = l3['13_rhythm_pattern']
    lines.append(f"\n13. 节奏模式: {rp['pattern']} — {rp['desc']}")
    
    id_ = l3['14_information_density']
    lines.append(f"\n14. 信息密度 [{id_['score']}/5] {id_['desc']} ({id_['info_markers_per_sentence']}标记/句)")
    
    cd = l3['15_cultural_dna']
    lines.append(f"\n15. 文化基因信号:")
    for k, v in cd.items():
        if v > 0:
            lines.append(f"    {k}: {v}")
    
    lines.append("\n" + "=" * 60)
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='文风量化分析工具 — 15维风格检测')
    parser.add_argument('--file', type=str, help='文本文件路径')
    parser.add_argument('--text', type=str, help='直接输入文本')
    parser.add_argument('--compare', nargs=2, help='对比两个文本文件')
    parser.add_argument('--output', type=str, default='text', choices=['json', 'text'],
                        help='输出格式 (default: text)')
    
    args = parser.parse_args()
    
    if args.compare:
        text1 = load_text(filepath=args.compare[0])
        text2 = load_text(filepath=args.compare[1])
        report1 = full_analysis(text1)
        report2 = full_analysis(text2)
        
        comparison = {
            'file1': args.compare[0],
            'file2': args.compare[1],
            'report1': report1,
            'report2': report2,
        }
        
        if args.output == 'json':
            print(json.dumps(comparison, ensure_ascii=False, indent=2))
        else:
            print(f"文件1: {args.compare[0]}")
            print(format_text_report(report1))
            print(f"\n文件2: {args.compare[1]}")
            print(format_text_report(report2))
        return
    
    text = load_text(filepath=args.file, direct_text=args.text)
    if not text:
        print("错误：未提供文本。使用 --file 或 --text 参数。", file=sys.stderr)
        sys.exit(1)
    
    report = full_analysis(text)
    
    if args.output == 'json':
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(format_text_report(report))


if __name__ == '__main__':
    main()
