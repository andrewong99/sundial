#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日晷 · 六分仪 · 星空月相 模拟器
================================================================
三个页签:
  1. 日晷 Sundial —— 水平 / 赤道 / 垂直朝南 三种晷面, 2D 平面图与 3D 立体图。
     3D: 左键拖动转视角(松开即固定, 显示视线方位角与俯仰角), 右键拖动平移,
     滚轮可放大到 32× (赤道附近时线极密, 放大才看得清), 仰角限 2°~88°。
     刻度有两套并存: 蓝色 = 真太阳时 (晷面固有), 橙色 = 当地标准时
     (按当日均时差与经度差画, 每天略移) —— 这样晷面读数与手表就对得上;
     可选 24 小时制或 12 时辰制, 并可画"刻"(15 分一刻, 一时辰八刻);
     时辰起算可选「中天起午」(太阳中天=午时之始, 底天=子时之始/日始)
     或传统 (午时含中天); 面板给出今日 12 时辰 ↔ 钟表时刻对照表,
     以及晷面半径、晷针长度/高度、此刻影长等实际尺寸;
     换地点后会按纬度自动推荐并换上合适的晷面;
     赤道晷半年照上面半年照下面, 勾"自动转到有影子的一面"即可免去手动找面。
     时间默认跟着真实时间走, 可暂停 / 加速 / 跳转。

  2. 六分仪 Sextant —— 一台可以用鼠标或键盘操作的六分仪:
     直接拖动金色指标臂、按 ◀◀◀▶▶▶ 按钮、或用键盘 ← → (0.1′) /
     Shift+← → (1′) / Ctrl 或 ↑↓ (1°) 把天体"带下来"; 画面上方有
     ①对平海平线 ②转指标臂 ③微动螺旋切平 ④读数记录 的步骤指引;
     另有「自动测量演示」自动把指标臂转到正确读数并记录, 以及
     「摆动演示」重现实船上摆动六分仪让天体划弧的动作。
     旁边同时画出望远镜视场与双反射光路图 (光路随指标臂一起转)。
     可观测 日/月/金/火/木/土 + 北极星、南十字等导航星。
     右侧「航海历」页给出当日 GHA/Dec/v/d/HP 表、恒星 SHA 表、增量改正,
     并直接标出此刻的正确读数 Hs; 「定位」页用截距法解出经纬度。

  4. 太阳视运动 · 24 节气 Sun Track —— 站在天穹中心朝西看的固定视角模型:
     东在近前(面向自己), 南在左, 北在右, 西在远处, 地面为浅青色椭圆(水平圆的
     正交投影)。旁边可填年月日时、经纬度、时区并选地点(预设吉隆坡, 含郑州等),
     再直接勾选 24 节气中的任意几个, 即按上图方式画出该日太阳东升西落的轨迹;
     每条轨迹标出日出/日落时刻与方位、中天时刻与正午高度角, 并按所填时刻画出
     太阳当时的具体位置(红日)。时刻可选 标准时(时区) / 地方平太阳时 / 真太阳时,
     面板同时给出三者换算与均时差。周边画满 1°/5°/10° 刻度(方位角一圈、高度角
     沿南北子午圈), 放大后可直接读度数。图形固定, 只能缩放平移, 一键清空。

  7. 轨道 Orbits —— 以太阳为中心的公转盘, 三种画法可切换, 全部是平面/正投影
     (角度写死, 不给自由三维, 只能缩放与拖动平移):
       ① 实际距离图: 上下左右各 11 AU (全幅 22 AU, 土星远日点 10.1 AU 刚好装下),
          轨道由 VSOP87 逐点采样画出 —— 该偏心就偏心, 该椭圆就椭圆; 每颗星按
          「自输入的日期起算的一个恒星周期」画满一圈, 并高亮已走过的那一段弧。
       ② 等距示意图: 轨道画成等间距同心圆, 只看相对方位, 不看距离。
       ③ 侧面图: 以「当时的太阳—地球连线」为水平轴, 从黄道面内看过去, 一眼看出
          谁高过日地线、谁低过。横轴仍是真实的 22 AU, 竖轴 z 真值只有 0.0x AU,
          故另给 1~200× 的竖向放大 (数字标注仍是真值)。
     只画 日、月、五大行星 (+ 地球); 月亮按真方向、固定像素距离示意放大。
     定盘二选一, 子 0° 恒在图面正下方:
       日地恒定 (预设): 太阳、地球都不动, 地球恒在子 0°, 日地虚线永远对准子 0°;
          其余行星按「日心黄经 − 地球日心黄经」绕着走, 专看它们相对日地的运动
          (已走过的轨迹也画在这个随地球转的盘上, 留最近一个会合周期)。
       大寒定盘: 子宫 0° (= 自定的 水瓶座 0° = 大寒) 固定在正下方, 大寒那天地球
          在子宫 0°, 之后地球照常绕太阳 360°。
     全部可动画: 预设 真实 1 秒 = 星图 1 日 (地球 365 秒转一圈), 可选或自填倍速
     (100× 则 3.65 秒一圈); 输入日期后画面静止, 按 ▶ 才走, 随时可暂停。

  3. 星空 · 月相 Sky —— 站在地面看天 (Stellarium 式): 鼠标拖动改变视线,
     松开固定并显示方位/高度; 点选任一天体可看它的赤经赤纬、黄经黄纬、
     时角、距离、视半径、升落中天时刻。地平线用青色加粗, 地平线以下也有
     网格; 日月五星与内置亮星 (含北极星、南十字) 位置皆算准, 月相的形状
     与倾斜方向 (χ 与视差角 q) 亦准确。右侧四页: 本朔望月逐日月相 (29~30 天)、
     月相成因图、轨道展开图、朔望周期; 鼠标移到任一月相上会浮出提示,
     告诉你这一轮朔望月是"公历几年几月几日几点"进入该相位的。
     同目录放 stars.csv (name, ra/ra_h, dec, mag) 可加载自己的星表。

界面语言: 窗口最上方可切换「中英文 (预设)」与「English」(全英文)。英文模式只换显示文字,
  内部数据与计算完全相同; 切换时界面按新语言重建 (各页回到初始状态, 页签保持不变)。

天文算法 (全部内置, 无外部依赖):
  * 太阳与五大行星: VSOP87D 截断级数 + 光行时 + 周年光行差 + 章动
  * 月亮          : 截断 ELP-2000/82 (Meeus 第47章)
  * 章动/黄赤交角/恒星时/岁差: IAU 简化式
  与 ERFA (IAU SOFA 的 C 实现) 及完整 VSOP87 逐点比对, 视位置误差:
      太阳 <0.4″  月亮 <0.2″  金星 <1″  水星 <1.5″  火星 <4.5″
      木星 <1.5″  土星 <2″    格林尼治真恒星时 <0.3″
  * 内置 26 颗亮星 (J2000, 约 ±0.5′) 经岁差+章动+光行差换算到当日视位置
  * 若系统装有 skyfield 且能取得 JPL 星历 de421.bsp, 可在右上角勾选切换。

运行:  python sundial_sextant.py
自检:  python sundial_sextant.py --selftest     (不开界面, 跑一遍数值验证)
依赖:  仅需 Python 3.8+ 标准库 (tkinter)。skyfield 可选。
"""

import sys
import math
import datetime as dt

try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except ImportError:                      # 少数 Linux 发行版未随 Python 装 tk
    if "--selftest" not in sys.argv:
        print("找不到 tkinter。Debian/Ubuntu: sudo apt install python3-tk\n"
              "                  Fedora:      sudo dnf install python3-tkinter\n"
              "                  macOS/Win:   官方 python.org 安装包自带")
        raise
    import types
    tk = messagebox = None
    ttk = types.SimpleNamespace(Frame=object)     # 仅供 --selftest 时占位


# ===========================================================================
#  界面语言 —— "zh" = 中英参杂 (预设, 即原来的界面); "en" = 全英文。
#  英文模式不改动任何内部数据、键名与计算: 只在「显示」那一刻把中文换成英文
#  (控件文字、画布文字、表格、文本框、对话框、窗口标题); 带 % 的格式模板先用
#  T() 换成英文模板再代入数字。控件内容读回程序时 (StringVar / Combobox /
#  Treeview) 再换回中文原文, 因此程序逻辑在两种语言下完全一样。
#  预设 zh 时这一层完全不介入 (钩子只在第一次切到英文时才装上)。
# ===========================================================================
import re as _re

LANG = "zh"
_EN = {}                 # 中文原文 -> 英文 (文件末尾 _EN_DATA 载入)
_EN_REV = {}             # 已显示的英文 -> 中文原文 (读回控件内容时还原)
_TR_CACHE = {}
_TR_MISSING = set()      # 英文模式下查不到的中文片段 (自检/调试用)
_TR_SEGMENTED = set()    # 靠拆词拼出来的片段 (自检/调试用)
_CJK_CHARS = ("\u2e80-\u2fdf\u3000-\u303f\u3040-\u30ff\u3400-\u9fff"
              "\uf900-\ufaff\ufe30-\ufe4f\uff00-\uffef")
_CJK_RE = _re.compile("[%s]" % _CJK_CHARS)
_CJK_RUN_RE = _re.compile("[%s]+" % _CJK_CHARS)
_CJK_PUNCT = {"，": ", ", "、": ", ", "。": ". ", "：": ": ", "；": "; ",
              "！": "! ", "？": "? ", "（": " (", "）": ") ", "「": "\"",
              "」": "\"", "『": "\"", "』": "\"", "【": "[", "】": "] ",
              "《": "\"", "》": "\"", "〈": "<", "〉": ">", "～": "~",
              "　": " ", "％": "%", "＋": "+", "－": "-", "＝": "=", "／": "/",
              "＜": "<", "＞": ">", "：": ": ", "·": "·"}
_PUNCT_SPLIT_RE = _re.compile("([%s])" % _re.escape(
    "".join(k for k in _CJK_PUNCT if _CJK_RE.match(k))))


def _T(s):
    """格式模板: 英文模式下换成英文模板 (占位符与次序不变), 中英模式原样返回。"""
    if LANG == "en":
        return _EN.get(s, s)
    return s


def _en(zh, en):
    """同一个中文在不同处要译法不同时, 就地指定英文。"""
    return en if LANG == "en" else zh


def _tr_run(run):
    """翻译一段连续的中文 (查表 → 按中文标点切开 → 最长匹配拆词)。"""
    r = _EN.get(run)
    if r is not None:
        return r
    parts = _PUNCT_SPLIT_RE.split(run)
    if len(parts) > 1:
        out = []
        for part in parts:
            if not part:
                continue
            if part in _CJK_PUNCT:
                out.append(_CJK_PUNCT[part])
            else:
                out.append(_tr_run(part))
        return _re.sub(r"  +", " ", "".join(out))
    res, i, n = [], 0, len(run)
    while i < n:
        for j in range(n, i, -1):
            v = _EN.get(run[i:j])
            if v is not None:
                res.append(v)
                i = j
                break
        else:
            _TR_MISSING.add(run[i])
            res.append(run[i])
            i += 1
    if len(res) > 1:
        _TR_SEGMENTED.add(run)
    return " ".join(res)


_KEY_RE = None


def _key_re():
    """所有已知原文 (按长度由长到短) 合成一个正则, 用来在拼接句里找出整段原文。"""
    global _KEY_RE
    if _KEY_RE is None:
        keys = sorted((k for k in _EN if _CJK_RE.search(k) and "\n" not in k),
                      key=len, reverse=True)
        _KEY_RE = _re.compile("|".join(_re.escape(k) for k in keys))
    return _KEY_RE


def _join_en(out, rep, nxt):
    """把译文接到 out 后面, 必要时与左右的字母数字之间补一个空格。"""
    prev = out[-1][-1:] if out and out[-1] else ""
    if rep and prev and (prev.isalnum() or prev in ")]°′″%,;:") \
            and (rep[0].isalnum() or rep[0] == "("):
        rep = " " + rep
    elif rep and prev == " " and rep[0] == " ":
        rep = rep.lstrip(" ")
    if rep and nxt and (nxt.isalnum() or nxt in "([") \
            and (rep[-1].isalnum() or rep[-1] in ")]."):
        rep = rep + " "
    out.append(rep)


def _tr_runs(text):
    """把一段里剩下的中文片段逐段译出 (标点表 / 拆词)。"""
    out, pos = [], 0
    for m in _CJK_RUN_RE.finditer(text):
        out.append(text[pos:m.start()])
        nxt = text[m.end()] if m.end() < len(text) else ""
        _join_en(out, _tr_run(m.group(0)), nxt)
        pos = m.end()
    out.append(text[pos:])
    return "".join(out)


def _tr_line(line):
    if not _CJK_RE.search(line):
        return line
    r = _EN.get(line)
    if r is not None:
        return r
    core = line.strip()
    if core != line:
        r = _EN.get(core)
        if r is not None:
            k = line.index(core)
            return line[:k] + r + line[k + len(core):]
    # 拼接出来的句子: 先找出其中整段的已知原文 (最长优先、自左而右) 换掉,
    # 剩下零星的中文再逐段处理。
    out, pos = [], 0
    for m in _key_re().finditer(line):
        if m.start() > pos:
            out.append(_tr_runs(line[pos:m.start()]))
        nxt = line[m.end()] if m.end() < len(line) else ""
        _join_en(out, _EN[m.group(0)], nxt)
        pos = m.end()
    if pos < len(line):
        out.append(_tr_runs(line[pos:]))
    return "".join(out)


def tr(s):
    """显示用: 英文模式下把一段文字 (可多行) 译成英文; 中英模式原样返回。"""
    if LANG != "en" or not isinstance(s, str) or not _CJK_RE.search(s):
        return s
    r = _TR_CACHE.get(s)
    if r is None:
        r = _EN.get(s)
        if r is None:
            r = "\n".join(_tr_line(x) for x in s.split("\n"))
        if len(_TR_CACHE) > 60000:
            _TR_CACHE.clear()
        _TR_CACHE[s] = r
    return r


def _reg(s, owner=None):
    """
    译出并登记反查 (StringVar / Combobox / Treeview 的值要能读回中文)。
    owner = 该值所属的变量或控件: 反查表挂在它身上, 不同控件里碰巧译成同一个
    英文词的不同原文 (如「北京」与「北京 Beijing」) 就不会互相串。
    """
    e = tr(s)
    if e != s:
        _EN_REV[e] = s
        if owner is not None:
            try:
                m = owner.__dict__.setdefault("_zh_rev", {})
                m[e] = s
            except Exception:
                pass
    return e


def untr(s, *owners):
    if LANG == "en" and isinstance(s, str):
        for o in owners:
            m = getattr(o, "_zh_rev", None) if o is not None else None
            if m and s in m:
                return m[s]
        return _EN_REV.get(s, s)
    return s


# ---------------------------------------------------------------------------
#  画布文字排版 (中英文通用): 字宽一律按「实际显示的那种语言」量, 不按中文原文量
# ---------------------------------------------------------------------------
def text_size(font, s):
    """显示出来的宽、高 (像素): 英文模式量译文; 多行取最宽一行, 高 = 行数 × 行距。"""
    lines = tr(s).split("\n") if isinstance(s, str) else [""]
    return (max(font.measure(x) for x in lines),
            font.metrics("linespace") * len(lines))


def anchor_box(x, y, anc, w, h):
    """按 tkinter 的 anchor 求文字框 (x0, y0, x1, y1)。"""
    if anc == "center":
        return (x - w / 2.0, y - h / 2.0, x + w / 2.0, y + h / 2.0)
    x0 = x if "w" in anc else (x - w if "e" in anc else x - w / 2.0)
    y0 = y if anc.startswith("n") else (y - h if anc.startswith("s") else y - h / 2.0)
    return (x0, y0, x0 + w, y0 + h)


def box_ov(a, b):
    """两框重叠面积 (不重叠为 0)。"""
    w = min(a[2], b[2]) - max(a[0], b[0])
    h = min(a[3], b[3]) - max(a[1], b[1])
    return w * h if (w > 0 and h > 0) else 0.0


def seg_boxes(x0, y0, x1, y1, pad=3.0, step=10.0):
    """一条线段沿途切成小框 (给文字让路用)。"""
    n = max(1, int(math.hypot(x1 - x0, y1 - y0) / step))
    out = []
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        y = y0 + (y1 - y0) * i / n
        out.append((x - pad, y - pad, x + pad, y + pad))
    return out


def place_text(c, cands, text, font, taken=None, bounds=None, **kw):
    """
    从候选位置 [(x, y, anchor), …] 里按顺序挑第一个「不压别的字/元件、不出界」的
    摆上; 都不行就挑压得最少的。第一个候选就是原来的位置 —— 摆得下就不动。
    taken: 已占的框 (这次的框会加进去); bounds: (x0, y0, x1, y1) 可用范围。
    """
    w, h = text_size(font, text)
    best = None
    for k, (x, y, anc) in enumerate(cands):
        b = anchor_box(x, y, anc, w, h)
        bad = sum(box_ov(b, t) for t in (taken or ()))
        if bounds is not None:
            bad += ((max(0.0, bounds[0] - b[0]) + max(0.0, b[2] - bounds[2])) * h
                    + (max(0.0, bounds[1] - b[1]) + max(0.0, b[3] - bounds[3])) * w)
        score = bad * 1000.0 + k
        if best is None or score < best[0]:
            best = (score, x, y, anc, b)
        if bad == 0:
            break
    _sc, x, y, anc, b = best
    if taken is not None:
        taken.append(b)
    return c.create_text(x, y, text=text, anchor=anc, font=font, **kw)


def fit_text(c, x, y, text, font, xmin, xmax, anchor="center", alt_fonts=(), **kw):
    """
    画一行字, 保证整段落在 [xmin, xmax] 之内: 放得下就原位 (超界才平移);
    放不下先换小一号的字体 (alt_fonts), 再不行就在该宽度内折行。
    返回 (item, 实际用的字体, 文字框)。
    """
    avail = max(20.0, xmax - xmin)
    for f in (font,) + tuple(alt_fonts):
        w, h = text_size(f, text)
        if w <= avail:
            b = anchor_box(x, y, anchor, w, h)
            dx = (xmin - b[0]) if b[0] < xmin else ((xmax - b[2]) if b[2] > xmax else 0.0)
            it = c.create_text(x + dx, y, text=text, anchor=anchor, font=f, **kw)
            return it, f, (b[0] + dx, b[1], b[2] + dx, b[3])
    f = font
    kw.setdefault("justify", "left" if "w" in anchor else
                  ("right" if "e" in anchor and anchor != "center" else "center"))
    it = c.create_text(xmin if "w" in anchor else (xmax if ("e" in anchor and anchor != "center")
                                                   else (xmin + xmax) / 2.0),
                       y, text=text, anchor=anchor, font=f, width=avail, **kw)
    b = c.bbox(it) or (xmin, y, xmax, y)
    return it, f, b


def autosize_tree(tree, cell_font, head_font, maxw=240):
    """
    表格各栏按「标题 / 内容」实际显示出来的宽度放宽 —— 只放宽、不收窄, 所以中文原本
    放得下的栏宽一点不变; 英文字长就自动加宽。加起来超过表的可见宽度时, 表下露出
    横向滚动条 (tree._hbar, 建表时给)。
    """
    def _i(v):
        try:
            return int(float(str(v) or 0))
        except Exception:
            return 0
    total = 0
    kids = tree.get_children()
    for cid in tree["columns"]:
        cur = _i(tree.column(cid, "width"))
        need = head_font.measure(str(tree.heading(cid, "text"))) + 16
        for iid in kids:
            need = max(need, cell_font.measure(str(tree.set(iid, cid))) + 14)
        w = max(cur, min(maxw, need))
        if w != cur:
            tree.column(cid, width=w)
        total += w
    tree._cols_total = total
    _tree_hbar(tree)


def _tree_hbar(tree, _e=None):
    hb = getattr(tree, "_hbar", None)
    if hb is None:
        return
    try:
        vis = tree.winfo_width()
        need = getattr(tree, "_cols_total", 0) > vis + 2 and vis > 1
        if need and not hb.winfo_ismapped():
            hb.pack(side="top", fill="x", after=tree)
        elif not need and hb.winfo_ismapped():
            hb.pack_forget()
    except Exception:
        pass


def tree_hscroll(tree, master):
    """给表配一条横向滚动条 (平时不显示, 栏宽超出可见宽度才露出来)。"""
    hb = ttk.Scrollbar(master, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=hb.set)
    tree._hbar = hb
    tree.bind("<Configure>", lambda e, t=tree: _tree_hbar(t), add="+")
    return hb


_I18N_PATCHED = False


def _install_i18n():
    """第一次切到英文时, 给 tkinter 的「显示出口」装上翻译钩子。
    钩子在中英模式下一律直通, 所以切回中英后行为与从未切换过完全相同。"""
    global _I18N_PATCHED
    if _I18N_PATCHED or tk is None:
        return
    _I18N_PATCHED = True
    import tkinter.font as _tkfont
    from tkinter import messagebox as _mb

    def tr_opts(d, ttk_widget, owner=None):
        if not d or LANG != "en" or not isinstance(d, dict):
            return d
        d = dict(d)
        var = d.get("variable")
        var = var if isinstance(var, tk.Variable) else None
        tvar = d.get("textvariable")
        tvar = tvar if isinstance(tvar, tk.Variable) else None
        for k in ("text", "label", "title", "message"):
            v = d.get(k)
            if isinstance(v, str) and _CJK_RE.search(v):
                d[k] = tr(v)
                w = d.get("width")
                if (ttk_widget and k == "text" and isinstance(w, int) and w > 0
                        and len(d[k]) > w):
                    d["width"] = -w        # ttk: 负宽度 = 最小宽度, 英文长了就撑开
        v = d.get("value")
        if isinstance(v, str) and _CJK_RE.search(v):
            d["value"] = _reg(v, var)
        v = d.get("values")
        if isinstance(v, (list, tuple)) and any(
                isinstance(x, str) and _CJK_RE.search(x) for x in v):
            vals = []
            for x in v:
                if isinstance(x, str):
                    e = _reg(x, owner)
                    if tvar is not None:
                        _reg(x, tvar)
                    vals.append(e)
                else:
                    vals.append(x)
            d["values"] = vals
            w = d.get("width")
            if ttk_widget and isinstance(w, int) and w > 0:
                longest = max(len(str(x)) for x in d["values"])
                d["width"] = max(w, min(int(w * 1.8) + 1, longest + 1))
        return d

    _bw_init = tk.BaseWidget.__init__

    def bw_init(self, master, widgetName, cnf={}, kw={}, extra=()):
        if LANG == "en":
            is_ttk = str(widgetName).startswith("ttk::")
            cnf = tr_opts(cnf, is_ttk, self)
            kw = tr_opts(kw, is_ttk, self)
        _bw_init(self, master, widgetName, cnf, kw, extra)
    tk.BaseWidget.__init__ = bw_init

    _cfg = tk.Misc._configure

    def cfg(self, cmd, cnf, kw):
        if LANG == "en":
            is_ttk = (cmd == "configure"
                      and str(getattr(self, "widgetName", "")).startswith("ttk::"))
            cnf = tr_opts(cnf, is_ttk, self)
            kw = tr_opts(kw, is_ttk, self)
        return _cfg(self, cmd, cnf, kw)
    tk.Misc._configure = cfg

    _create = tk.Canvas._create

    def create(self, itemType, args, kw):
        if LANG == "en" and itemType == "text":
            if kw and "text" in kw:
                kw = dict(kw)
                kw["text"] = tr(kw["text"])
            if args and isinstance(args[-1], dict) and "text" in args[-1]:
                d = dict(args[-1])
                d["text"] = tr(d["text"])
                args = tuple(args[:-1]) + (d,)
        return _create(self, itemType, args, kw)
    tk.Canvas._create = create

    _title = tk.Wm.wm_title

    def title(self, string=None):
        return _title(self, tr(string) if string is not None else None)
    tk.Wm.wm_title = title
    tk.Wm.title = title

    _show = _mb._show

    def show(title=None, message=None, _icon=None, _type=None, **options):
        return _show(tr(title), tr(message), _icon, _type, **options)
    _mb._show = show

    SV = tk.StringVar
    _sv_init, _sv_set, _sv_get = SV.__init__, SV.set, SV.get

    def sv_init(self, master=None, value=None, name=None):
        if LANG == "en" and isinstance(value, str):
            value = _reg(value, self)
        _sv_init(self, master, value, name)

    def sv_set(self, value):
        if LANG == "en" and isinstance(value, str):
            value = _reg(value, self)
        return _sv_set(self, value)

    def sv_get(self):
        return untr(_sv_get(self), self)
    SV.__init__, SV.set, SV.get = sv_init, sv_set, sv_get

    CB = ttk.Combobox
    _cb_get, _cb_set = CB.get, CB.set
    CB.get = lambda self: untr(_cb_get(self), self)
    CB.set = lambda self, value: _cb_set(
        self, _reg(value, self) if (LANG == "en" and isinstance(value, str)) else value)

    TV = ttk.Treeview
    _tv_heading, _tv_insert, _tv_item = TV.heading, TV.insert, TV.item

    def tv_vals(v, owner=None):
        return tuple(_reg(x, owner) if isinstance(x, str) else x for x in v)

    def tv_heading(self, column, option=None, **kw):
        if LANG == "en" and "text" in kw:
            kw["text"] = tr(kw["text"])
        return _tv_heading(self, column, option, **kw)

    def tv_insert(self, parent, index, iid=None, **kw):
        if LANG == "en":
            if "values" in kw:
                kw["values"] = tv_vals(kw["values"], self)
            if "text" in kw:
                kw["text"] = tr(kw["text"])
        return _tv_insert(self, parent, index, iid, **kw)

    def tv_item(self, item, option=None, **kw):
        if LANG == "en" and kw:
            if "values" in kw:
                kw["values"] = tv_vals(kw["values"], self)
            if "text" in kw:
                kw["text"] = tr(kw["text"])
        r = _tv_item(self, item, option, **kw)
        if LANG == "en":
            if option == "values" and isinstance(r, (tuple, list)):
                r = tuple(untr(x, self) for x in r)
            elif option is None and not kw and isinstance(r, dict) and r.get("values"):
                r = dict(r)
                r["values"] = [untr(x, self) for x in r["values"]]
        return r
    TV.heading, TV.insert, TV.item = tv_heading, tv_insert, tv_item

    NB = ttk.Notebook
    _nb_add, _nb_tab = NB.add, NB.tab

    def nb_add(self, child, **kw):
        if LANG == "en" and "text" in kw:
            kw["text"] = tr(kw["text"])
        return _nb_add(self, child, **kw)

    def nb_tab(self, tab_id, option=None, **kw):
        if LANG == "en" and "text" in kw:
            kw["text"] = tr(kw["text"])
        return _nb_tab(self, tab_id, option, **kw)
    NB.add, NB.tab = nb_add, nb_tab

    _txt_insert = tk.Text.insert

    def txt_insert(self, index, chars, *args):
        if LANG == "en":
            chars = tr(chars)
            args = tuple(tr(a) if (i % 2 == 1 and isinstance(a, str)) else a
                         for i, a in enumerate(args))
        return _txt_insert(self, index, chars, *args)
    tk.Text.insert = txt_insert

    _measure = _tkfont.Font.measure

    def measure(self, text, displayof=None):
        return _measure(self, tr(text), displayof)
    _tkfont.Font.measure = measure


def utcnow():
    """当前世界时 (naive)。datetime.utcnow() 在 Python 3.12 起会告警, 故自建。"""
    return dt.datetime.now(dt.timezone.utc).replace(tzinfo=None)


D2R = math.pi / 180.0
R2D = 180.0 / math.pi

APP_TITLE = ("日晷 · 六分仪 · 星空月相 · 太阳视运动 · 土圭 · 日月食 · 轨道  模拟器"
             "  ·  Sundial / Sextant / Sky / Gnomon / Eclipse Simulator")

# ---------------------------------------------------------------------------
# 预设地点  (名称, 纬度°(N+), 经度°(E+), 标准时区 UTC 偏移小时)
# ---------------------------------------------------------------------------
CITIES = [
    ("吉隆坡 Kuala Lumpur",      3.1390,  101.6869,  8.0),
    ("新加坡 Singapore",         1.3521,  103.8198,  8.0),
    ("槟城 George Town",         5.4141,  100.3288,  8.0),
    ("哥打京那巴鲁 Kota Kinabalu", 5.9804, 116.0735,  8.0),
    ("北京 Beijing",            39.9042,  116.4074,  8.0),
    ("香港 Hong Kong",          22.3193,  114.1694,  8.0),
    ("台北 Taipei",             25.0330,  121.5654,  8.0),
    ("东京 Tokyo",              35.6762,  139.6503,  9.0),
    ("雅加达 Jakarta",          -6.2088,  106.8456,  7.0),
    ("悉尼 Sydney",            -33.8688,  151.2093, 10.0),
    ("伦敦 London",             51.5074,   -0.1278,  0.0),
    ("格林尼治 Greenwich",      51.4779,    0.0000,  0.0),
    ("纽约 New York",           40.7128,  -74.0060, -5.0),
    ("赤道·东经101°",            0.0000,  101.0000,  8.0),
]
DEFAULT_CITY = 0            # 吉隆坡

# 页面用到的天体列表在 p1b 中按用途定义 (NAV_BODIES / SKY_BODIES)
BODY_EN = {"太阳": "Sun", "月亮": "Moon", "水星": "Mercury", "金星": "Venus",
           "火星": "Mars", "木星": "Jupiter", "土星": "Saturn"}


# ===========================================================================
#  基础时间与角度工具
# ===========================================================================
def norm360(x):
    return x % 360.0


def az_fmt(a, nd=2):
    """仅供显示: 方位归一到 [0, 360), 且四舍五入到 nd 位小数后不会印成 360.00 (改印 0.00)。"""
    v = a % 360.0
    return 0.0 if round(v, nd) >= 360.0 else v


def norm180(x):
    x = (x + 180.0) % 360.0 - 180.0
    return x


def dsin(x):
    return math.sin(x * D2R)


def dcos(x):
    return math.cos(x * D2R)


def dtan(x):
    return math.tan(x * D2R)


def julian_day(utc):
    """由 UTC datetime 求儒略日 (UT)。"""
    y, m = utc.year, utc.month
    d = (utc.day + (utc.hour + utc.minute / 60.0 +
                    (utc.second + utc.microsecond / 1e6) / 3600.0) / 24.0)
    if m <= 2:
        y -= 1
        m += 12
    a = y // 100
    b = 2 - a + a // 4                       # 格里高利历
    if (utc.year, utc.month, utc.day) < (1582, 10, 15):
        b = 0                                # 儒略历
    return (math.floor(365.25 * (y + 4716)) + math.floor(30.6001 * (m + 1))
            + d + b - 1524.5)


def jd_to_datetime(jd):
    """儒略日 -> UTC datetime。"""
    jd = jd + 0.5
    z = math.floor(jd)
    f = jd - z
    if z >= 2299161:
        alpha = math.floor((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - math.floor(alpha / 4)
    else:
        a = z
    b = a + 1524
    c = math.floor((b - 122.1) / 365.25)
    d = math.floor(365.25 * c)
    e = math.floor((b - d) / 30.6001)
    day = b - d - math.floor(30.6001 * e) + f
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715
    di = int(math.floor(day))
    frac = (day - di) * 24.0
    hh = int(frac)
    mm_f = (frac - hh) * 60.0
    mm = int(mm_f)
    ss = (mm_f - mm) * 60.0
    si = int(ss)
    us = int(round((ss - si) * 1e6))
    if us >= 1000000:
        us -= 1000000
        si += 1
    return (dt.datetime(int(year), int(month), di, 0, 0, 0)
            + dt.timedelta(hours=hh, minutes=mm, seconds=si, microseconds=us))


def delta_t_seconds(utc):
    """TT - UT1 的近似值 (秒)。Espenak & Meeus 多项式。"""
    return delta_t_year(utc.year + (utc.month - 0.5) / 12.0)


def delta_t_year(y):
    """TT - UT1 (秒), 自变量为「小数年」。Espenak & Meeus 长期多项式。
    y < 1900 与 y > 2150 用抛物线 -20 + 32t² (t = (y-1820)/100)，
    这是历史日月食推算的标准长期模型 (公元前误差可达数十分钟)。"""
    if y < 1900:
        t = (y - 1820) / 100.0
        return -20 + 32 * t * t
    if y < 1920:
        t = y - 1900
        return (-2.79 + 1.494119 * t - 0.0598939 * t * t
                + 0.0061966 * t ** 3 - 0.000197 * t ** 4)
    if y < 1941:
        t = y - 1920
        return 21.20 + 0.84493 * t - 0.076100 * t * t + 0.0020936 * t ** 3
    if y < 1961:
        t = y - 1950
        return 29.07 + 0.407 * t - t * t / 233.0 + t ** 3 / 2547.0
    if y < 1986:
        t = y - 1975
        return 45.45 + 1.067 * t - t * t / 260.0 - t ** 3 / 718.0
    if y < 2005:
        t = y - 2000
        return (63.86 + 0.3345 * t - 0.060374 * t * t + 0.0017275 * t ** 3
                + 0.000651814 * t ** 4 + 0.00002373599 * t ** 5)
    if y < 2050:
        t = y - 2000
        return 62.92 + 0.32217 * t + 0.005589 * t * t
    if y < 2150:
        return -20 + 32 * ((y - 1820) / 100.0) ** 2 - 0.5628 * (2150 - y)
    t = (y - 1820) / 100.0
    return -20 + 32 * t * t


def nutation(T):
    """章动 (简化, 精度约 0.5"): 返回 (Δψ 度, Δε 度, Ω 度)。"""
    om = 125.04452 - 1934.136261 * T + 0.0020708 * T * T + T ** 3 / 450000.0
    L = 280.4665 + 36000.7698 * T          # 太阳平黄经
    Lp = 218.3165 + 481267.8813 * T        # 月亮平黄经
    dpsi = (-17.20 * dsin(om) - 1.32 * dsin(2 * L)
            - 0.23 * dsin(2 * Lp) + 0.21 * dsin(2 * om)) / 3600.0
    deps = (9.20 * dcos(om) + 0.57 * dcos(2 * L)
            + 0.10 * dcos(2 * Lp) - 0.09 * dcos(2 * om)) / 3600.0
    return dpsi, deps, om


def mean_obliquity(T):
    """平黄赤交角 (度), Laskar 多项式。"""
    U = T / 100.0
    e0 = (23.0 + 26.0 / 60.0 + 21.448 / 3600.0)
    e0 += (-4680.93 * U - 1.55 * U ** 2 + 1999.25 * U ** 3 - 51.38 * U ** 4
           - 249.67 * U ** 5 - 39.05 * U ** 6 + 7.12 * U ** 7
           + 27.87 * U ** 8 + 5.79 * U ** 9 + 2.45 * U ** 10) / 3600.0
    return e0


def gmst_deg(jd_ut):
    """格林尼治平恒星时 (度)。"""
    T = (jd_ut - 2451545.0) / 36525.0
    th = (280.46061837 + 360.98564736629 * (jd_ut - 2451545.0)
          + 0.000387933 * T * T - T ** 3 / 38710000.0)
    return norm360(th)


# ===========================================================================
#  内置星历
# ===========================================================================
class BodyPos:
    """某时刻某天体的地心视位置。"""
    __slots__ = ("name", "ra", "dec", "gha", "dist_km", "sd_arcmin",
                 "hp_arcmin", "phase", "illum", "kind")

    def __init__(self, name, ra, dec, gha, dist_km, sd, hp, phase=0.0, illum=1.0):
        self.name = name
        self.ra = ra                 # 视赤经 (度)
        self.dec = dec               # 视赤纬 (度)
        self.gha = gha               # 格林尼治时角 (度, 西为正)
        self.dist_km = dist_km
        self.sd_arcmin = sd          # 视半径 (角分)
        self.hp_arcmin = hp          # 地平视差 (角分)
        self.phase = phase           # 相位角 (度)
        self.illum = illum           # 被照亮比例 0..1
        self.kind = "body"           # body / star


AU_KM = 149597870.7
EARTH_RADIUS_KM = 6378.14


# ---------------------------------------------------------------------------
#  VSOP87D 截断级数 (地球 + 金星)。振幅 >= 2e-7 弧度的项全部保留,
#  截断误差约 0.1″; 单位 1e-8 弧度 / AU, 自变量 τ = 儒略千年 (自 J2000 TT)。
#  数据源: VSOP87 (Bretagnon & Francou, Bureau des Longitudes)。
# ---------------------------------------------------------------------------
_V_L = [
    [  # T^0
      (317614666.8,0.00000000,0.00000000), (1353968.4,5.59313320,10213.28554621),
      (89891.6,5.30650048,20426.57109242), (5477.2,4.41630653,7860.41939244),
      (3455.7,2.69964471,11790.62908866), (2372.1,2.99377540,3930.20969622),
      (1317.1,5.18668219,26.29831980), (1664.1,4.25018935,1577.34354245),
      (1438.3,4.15745044,9683.59458112), (1200.5,6.15357115,30639.85663863),
      (761.4,1.95014702,529.69096509), (707.7,1.06466707,775.52261132),
      (584.8,3.99839885,191.44826611), (769.3,0.81629616,9437.76293489),
      (499.9,4.12340210,15720.83878488), (326.2,4.59056473,10404.73381232),
      (429.5,3.58642860,19367.18916223), (327.0,5.67736584,5507.55323867),
      (231.9,3.16251057,9153.90361602), (179.7,4.65337916,1109.37855209),
      (128.3,4.22604494,20.77539549), (155.5,5.57043889,19651.04848110),
      (127.9,0.96209823,5661.33204915), (105.5,1.53721191,801.82093112),
      (85.7,0.35589250,3154.68708490), (99.1,0.83288185,213.29909544),
      (98.8,5.39389656,13367.97263111), (82.1,3.21596991,18837.49819714),
      (88.0,3.88868860,9999.98645077), (71.6,0.11145739,11015.10647733),
      (56.1,4.24039855,7.11354700), (70.2,0.67458813,23581.25817732),
      (50.8,0.24531603,11322.66409830), (46.1,5.31576466,18073.70493865),
      (44.6,6.06282202,40853.14218484), (42.6,5.32873337,2352.86615377),
      (42.6,1.79955422,7084.89678112), (41.2,0.36240972,382.89653222),
      (35.7,2.70448479,10206.17199921), (33.9,2.02347322,6283.07584999),
      (29.1,3.59230926,22003.91463487), (28.5,2.22375414,1059.38193019),
      (29.9,4.02176977,10239.58386601), (33.3,2.10025597,27511.46787354),
      (30.2,4.94191920,13745.34623902), (29.3,3.51392388,283.85931887),
      (24.4,2.70177494,8624.21265093), (20.3,3.79493638,14143.49524243),
      (24.3,4.27814493,5.52292431), (26.3,0.54067588,17298.18232733),
      (20.5,0.58547075,38.02767264), (23.7,4.82870798,6872.67311951),
    ],
    [  # T^1
      (1021352943052.9,0.00000000,0.00000000), (95707.7,2.46424449,10213.28554621),
      (14445.0,0.51624565,20426.57109242), (213.4,1.79547929,30639.85663863),
      (151.7,6.10635282,1577.34354245), (173.9,2.65535879,26.29831980),
      (82.2,5.70234134,191.44826611), (69.7,2.68136035,9437.76293489),
      (52.4,3.60013088,775.52261132), (38.3,1.03379038,529.69096509),
      (29.6,1.25056322,5507.55323867), (25.1,6.10664793,10404.73381232),
    ],
    [  # T^2
      (54127.1,0.00000000,0.00000000), (3891.5,0.34514360,10213.28554621),
      (1337.9,2.02011286,20426.57109242), (23.8,2.04592119,26.29831980),
    ],
    [  # T^3
      (135.7,4.80389021,10213.28554621), (77.8,3.66876372,20426.57109242),
      (26.0,0.00000000,0.00000000),
    ],
    [  # T^4
      (114.0,3.14159265,0.00000000),
    ],
    [  # T^5
    ],
]
_V_B = [
    [  # T^0
      (5923638.5,0.26702776,10213.28554621), (40108.0,1.14737178,20426.57109242),
      (32814.9,3.14159265,0.00000000), (1011.4,1.08946123,30639.85663863),
      (149.5,6.25390296,18073.70493865), (137.8,0.86020147,1577.34354245),
      (130.0,3.67152484,9437.76293489), (119.5,3.70468813,2352.86615377),
      (108.0,4.53903678,22003.91463487), (92.0,1.53954563,9153.90361602),
      (53.0,2.28138172,5507.55323867), (45.6,0.72319642,10239.58386601),
      (38.9,2.93437865,10186.98722641), (43.5,6.14015777,11790.62908866),
      (41.7,5.99126845,19896.88012733), (39.6,3.86842096,8635.94200376),
      (39.2,3.94960351,529.69096509), (33.3,4.83194910,14143.49524243),
      (23.7,2.90646621,10988.80815754), (23.5,2.00770618,13367.97263111),
      (21.8,2.69701425,19651.04848110), (20.7,0.98666685,775.52261132),
    ],
    [  # T^1
      (513347.6,1.80364311,10213.28554621), (4380.1,3.38615712,20426.57109242),
      (196.6,2.53001197,30639.85663863), (199.2,0.00000000,0.00000000),
    ],
    [  # T^2
      (22377.7,3.38509144,10213.28554621), (281.7,0.00000000,0.00000000),
      (173.2,5.25563767,20426.57109242), (26.9,3.87040892,30639.85663863),
    ],
    [  # T^3
      (646.7,4.99166565,10213.28554621),
    ],
    [  # T^4
    ],
    [  # T^5
    ],
]
_V_R = [
    [  # T^0
      (72334820.9,0.00000000,0.00000000), (489824.2,4.02151832,10213.28554621),
      (1658.1,4.90206728,20426.57109242), (1632.1,2.84548852,7860.41939244),
      (1378.0,1.12846591,11790.62908866), (498.4,2.58682188,9683.59458112),
      (374.0,1.42314837,3930.20969622), (263.6,5.52938186,9437.76293489),
      (237.5,2.55135904,15720.83878488), (222.0,2.01346777,19367.18916223),
      (119.5,3.01975365,10404.73381232), (125.9,2.72769834,1577.34354245),
      (76.2,1.59577224,9153.90361602), (85.3,3.98607954,19651.04848110),
      (74.3,4.11957854,5507.55323867), (41.9,1.64273363,18837.49819714),
      (42.5,3.81864531,13367.97263111), (39.4,5.39019422,23581.25817732),
      (29.0,5.67739529,5661.33204915), (27.6,5.72392408,775.52261132),
      (27.3,4.82151813,11015.10647733), (31.3,2.31806720,9999.98645077),
    ],
    [  # T^1
      (34551.0,0.89198711,10213.28554621), (234.2,1.77224943,20426.57109242),
      (234.0,3.14159265,0.00000000), (23.9,1.11274503,9437.76293489),
    ],
    [  # T^2
      (1406.6,5.06366395,10213.28554621),
    ],
    [  # T^3
      (49.6,3.22263555,10213.28554621),
    ],
    [  # T^4
    ],
    [  # T^5
    ],
]
_E_L = [
    [  # T^0
      (175347045.7,0.00000000,0.00000000), (3341656.5,4.66925680,6283.07584999),
      (34894.3,4.62610242,12566.15169998), (3417.6,2.82886580,3.52311835),
      (3497.1,2.74411801,5753.38488490), (3135.9,3.62767042,77713.77146812),
      (2676.2,4.41808351,7860.41939244), (2342.7,6.13516238,3930.20969622),
      (1273.2,2.03709656,529.69096509), (1324.3,0.74246356,11506.76976979),
      (901.9,2.04505444,26.29831980), (1199.2,1.10962944,1577.34354245),
      (857.2,3.50849157,398.14900341), (779.8,1.17882652,5223.69391980),
      (990.2,5.23268130,5884.92684658), (753.1,2.53339054,5507.55323867),
      (505.3,4.58292563,18849.22754997), (492.4,4.20506640,775.52261132),
      (356.7,2.91954117,0.06731030), (284.1,1.89869034,796.29800682),
      (242.8,0.34481141,5486.77784318), (317.1,5.84901952,11790.62908866),
      (271.0,0.31488608,10977.07880470), (206.2,4.80646606,2544.31441988),
      (205.4,1.86947814,5573.14280143), (202.3,2.45767795,6069.77675455),
      (126.2,1.08302630,20.77539549), (155.5,0.83306074,213.29909544),
      (115.1,0.64544912,0.98032107), (102.9,0.63599847,4694.00295471),
      (101.7,4.26679821,7.11354700), (99.2,6.20992940,2146.16541648),
      (132.2,3.41118276,2942.46342329), (97.6,0.68101272,155.42039943),
      (85.1,1.29870743,6275.96230299), (74.7,1.75508916,5088.62883977),
      (101.9,0.97569222,15720.83878488), (84.7,3.67080093,71430.69561813),
      (73.5,4.67926565,801.82093112), (73.9,3.50319443,3154.68708490),
      (78.8,3.03698313,12036.46073489), (79.6,1.80791331,17260.15465469),
      (85.8,5.98322631,161000.68573767), (57.0,2.78430398,6286.59896834),
      (61.1,1.81839811,7084.89678112), (69.6,0.83297597,9437.76293489),
      (56.1,4.38694881,14143.49524243), (62.4,3.97763881,8827.39026987),
      (51.1,0.28306865,5856.47765912), (55.6,3.47006009,6279.55273164),
      (41.0,5.36817351,8429.24126647), (51.6,1.33282747,1748.01641307),
      (52.0,0.18914946,12139.55350911), (49.0,0.48735065,1194.44701022),
      (39.2,6.16832995,10447.38783960), (35.6,1.77597315,6812.76681509),
      (36.8,6.04133859,10213.28554621), (36.6,2.56955239,1059.38193019),
      (33.3,0.59309499,17789.84561978), (36.0,1.70876112,2352.86615377),
      (40.9,2.39850882,19651.04848110), (30.0,2.73975124,1349.86740966),
      (30.4,0.44294464,83996.84731811), (23.7,0.48473568,8031.09226306),
      (23.6,2.06527720,3340.61242670), (21.1,4.14825464,951.71840625),
      (24.7,0.21484762,3.59042865), (25.4,3.16470953,4690.47983636),
      (22.8,5.22197888,4705.73230754), (21.4,1.42563736,16730.46368960),
      (21.9,5.55594303,553.56940284), (20.3,0.37133793,283.85931887),
    ],
    [  # T^1
      (628331966747.5,0.00000000,0.00000000), (206058.9,2.67823456,6283.07584999),
      (4303.4,2.63512650,12566.15169998), (425.3,1.59046981,3.52311835),
      (109.0,2.96618002,1577.34354245), (93.5,2.59212835,18849.22754997),
      (119.3,5.79557488,26.29831980), (72.1,1.13846158,529.69096509),
      (67.8,1.87472305,398.14900341), (67.3,4.40918235,5507.55323867),
      (59.0,2.88797038,5223.69391980), (56.0,2.17471680,155.42039943),
      (45.4,0.39803080,796.29800682), (36.4,0.46624740,775.52261132),
      (29.0,2.64707384,7.11354700), (20.8,5.34138275,0.98032107),
    ],
    [  # T^2
      (52918.9,0.00000000,0.00000000), (8719.8,1.07209665,6283.07584999),
      (309.1,0.86728819,12566.15169998), (27.3,0.05297872,3.52311835),
    ],
    [  # T^3
      (289.2,5.84384199,6283.07584999), (35.0,0.00000000,0.00000000),
    ],
    [  # T^4
      (114.1,3.14159265,0.00000000),
    ],
    [  # T^5
    ],
]
_E_B = [
    [  # T^0
      (279.6,3.19870156,84334.66158131), (101.6,5.42248619,5507.55323867),
      (80.4,3.88013204,5223.69391980), (43.8,3.70444690,2352.86615377),
      (31.9,4.00026370,1577.34354245), (22.7,3.98473832,1047.74731175),
    ],
    [  # T^1
    ],
    [  # T^2
    ],
    [  # T^3
    ],
    [  # T^4
    ],
]
_E_R = [
    [  # T^0
      (100013988.8,0.00000000,0.00000000), (1670699.6,3.09846351,6283.07584999),
      (13956.0,3.05524610,12566.15169998), (3083.7,5.19846674,77713.77146812),
      (1628.5,1.17387749,5753.38488490), (1575.6,2.84685246,7860.41939244),
      (924.8,5.45292234,11506.76976979), (542.4,4.56409150,3930.20969622),
      (472.1,3.66100022,5884.92684658), (328.8,5.89983646,5223.69391980),
      (346.0,0.96368618,5507.55323867), (306.8,0.29867140,5573.14280143),
      (174.8,3.01193637,18849.22754997), (243.2,4.27349536,11790.62908866),
      (211.8,5.84714540,1577.34354245), (185.8,5.02194447,10977.07880470),
      (109.8,5.05510636,5486.77784318), (98.3,0.88681311,6069.77675455),
      (86.5,5.68959778,15720.83878488), (85.8,1.27083733,161000.68573767),
      (62.9,0.92177109,529.69096509), (57.1,2.01374292,83996.84731811),
      (64.9,0.27250614,17260.15465469), (49.4,3.24501240,2544.31441988),
      (55.7,5.24159799,71430.69561813), (42.5,6.01110242,6275.96230299),
      (47.0,2.57805070,775.52261132), (39.0,5.36071738,4694.00295471),
      (44.7,5.53715807,9437.76293489), (35.7,1.67468059,12036.46073489),
      (31.9,0.18368230,5088.62883977), (31.8,1.77775642,398.14900341),
      (33.2,0.24370300,7084.89678112), (38.2,2.39255344,8827.39026987),
      (28.5,1.21344868,6286.59896834), (37.5,0.82952922,19651.04848110),
      (37.0,4.90107592,12139.55350911), (34.5,1.84270693,2942.46342329),
      (26.3,4.58896850,10447.38783960), (24.6,3.78660875,8429.24126647),
      (23.6,0.26866117,796.29800682), (27.8,1.89934331,6279.55273164),
      (23.9,4.99598548,5856.47765912), (20.3,4.65267995,2146.16541648),
      (23.3,2.80783651,14143.49524243), (22.1,1.95004703,3154.68708490),
    ],
    [  # T^1
      (103018.6,1.10748970,6283.07584999), (1721.2,1.06442301,12566.15169998),
      (702.2,3.14159265,0.00000000), (32.3,1.02169059,18849.22754997),
      (30.8,2.84353805,5507.55323867), (25.0,1.31906709,5223.69391980),
    ],
    [  # T^2
      (4359.4,5.78455134,6283.07584999), (123.6,5.57934722,12566.15169998),
    ],
    [  # T^3
      (144.6,4.27319435,6283.07584999),
    ],
    [  # T^4
    ],
    [  # T^5
    ],
]

C_LIGHT_AUD = 173.1446326847     # 光速, AU/日


def _vsop(series, tau):
    """求 VSOP87 级数值 (弧度 或 AU)。"""
    total = 0.0
    tp = 1.0
    for terms in series:
        s = 0.0
        for a, b, c in terms:
            s += a * math.cos(b + c * tau)
        total += s * tp
        tp *= tau
    return total * 1e-8


def helio_ecl(planet, jd_tt):
    """日心黄道坐标 (当日平黄道分点): 返回 (L 度, B 度, R AU)。"""
    tau = (jd_tt - 2451545.0) / 365250.0
    if planet == "earth":
        L, B, R = _vsop(_E_L, tau), _vsop(_E_B, tau), _vsop(_E_R, tau)
    else:
        L, B, R = _vsop(_V_L, tau), _vsop(_V_B, tau), _vsop(_V_R, tau)
    return norm360(math.degrees(L)), math.degrees(B), R


def _rect(L, B, R):
    return (R * dcos(B) * dcos(L), R * dcos(B) * dsin(L), R * dsin(B))


def _earth_rect(jd_tt):
    return _rect(*helio_ecl("earth", jd_tt))


def _earth_velocity(jd_tt, h=0.05):
    """地球日心速度 (AU/日), 数值微分。"""
    p1 = _earth_rect(jd_tt - h)
    p2 = _earth_rect(jd_tt + h)
    return tuple((b - a) / (2 * h) for a, b in zip(p1, p2))


def _vector_to_apparent(name, vec, jd_tt, jd_ut, sd, hp, phase, illum,
                        aberration=True):
    """由地心几何向量(黄道系, AU) 求视赤经赤纬与 GHA。"""
    px, py, pz = vec
    dist = math.sqrt(px * px + py * py + pz * pz)
    ux, uy, uz = px / dist, py / dist, pz / dist
    if aberration:                                   # 周年光行差 (一阶)
        vx, vy, vz = _earth_velocity(jd_tt)
        ux += vx / C_LIGHT_AUD
        uy += vy / C_LIGHT_AUD
        uz += vz / C_LIGHT_AUD
        n = math.sqrt(ux * ux + uy * uy + uz * uz)
        ux, uy, uz = ux / n, uy / n, uz / n
    T = (jd_tt - 2451545.0) / 36525.0
    dpsi, deps, om = nutation(T)
    lam = norm360(math.degrees(math.atan2(uy, ux))) + dpsi     # 加章动
    beta = math.degrees(math.asin(max(-1.0, min(1.0, uz))))
    eps = mean_obliquity(T) + deps
    ra = norm360(math.degrees(math.atan2(
        dsin(lam) * dcos(eps) - dtan(beta) * dsin(eps), dcos(lam))))
    dec = math.degrees(math.asin(dsin(beta) * dcos(eps)
                                 + dcos(beta) * dsin(eps) * dsin(lam)))
    gast = norm360(gmst_deg(jd_ut) + dpsi * dcos(eps))
    gha = norm360(gast - ra)
    return BodyPos(name, ra, dec, gha, dist * AU_KM, sd, hp, phase, illum)


def sun_apparent(jd_tt, jd_ut):
    ex, ey, ez = _earth_rect(jd_tt)
    R = math.sqrt(ex * ex + ey * ey + ez * ez)
    sd = 959.63 / R / 60.0                            # 视半径, 角分
    hp = 8.794 / R / 60.0                             # 地平视差, 角分
    return _vector_to_apparent("太阳", (-ex, -ey, -ez), jd_tt, jd_ut,
                               sd, hp, 0.0, 1.0)


def sun_lambda_of(jd_tt):
    """太阳视黄经 (度) —— 供月相计算。"""
    ex, ey, ez = _earth_rect(jd_tt)
    return norm360(math.degrees(math.atan2(-ey, -ex)))


# --- 月亮: Meeus 47 章 (截断 ELP-2000/82) ------------------------------------
# (D, M, M', F, Σl[1e-6 度], Σr[1e-3 km])
_MOON_LR = [
    (0, 0, 1, 0, 6288774, -20905355), (2, 0, -1, 0, 1274027, -3699111),
    (2, 0, 0, 0, 658314, -2955968),   (0, 0, 2, 0, 213618, -569925),
    (0, 1, 0, 0, -185116, 48888),     (0, 0, 0, 2, -114332, -3149),
    (2, 0, -2, 0, 58793, 246158),     (2, -1, -1, 0, 57066, -152138),
    (2, 0, 1, 0, 53322, -170733),     (2, -1, 0, 0, 45758, -204586),
    (0, 1, -1, 0, -40923, -129620),   (1, 0, 0, 0, -34720, 108743),
    (0, 1, 1, 0, -30383, 104755),     (2, 0, 0, -2, 15327, 10321),
    (0, 0, 1, 2, -12528, 0),          (0, 0, 1, -2, 10980, 79661),
    (4, 0, -1, 0, 10675, -34782),     (0, 0, 3, 0, 10034, -23210),
    (4, 0, -2, 0, 8548, -21636),      (2, 1, -1, 0, -7888, 24208),
    (2, 1, 0, 0, -6766, 30824),       (1, 0, -1, 0, -5163, -8379),
    (1, 1, 0, 0, 4987, -16675),       (2, -1, 1, 0, 4036, -12831),
    (2, 0, 2, 0, 3994, -10445),       (4, 0, 0, 0, 3861, -11650),
    (2, 0, -3, 0, 3665, 14403),       (0, 1, -2, 0, -2689, -7003),
    (2, 0, -1, 2, -2602, 0),          (2, -1, -2, 0, 2390, 10056),
    (1, 0, 1, 0, -2348, 6322),        (2, -2, 0, 0, 2236, -9884),
    (0, 1, 2, 0, -2120, 5751),        (0, 2, 0, 0, -2069, 0),
    (2, -2, -1, 0, 2048, -4950),      (2, 0, 1, -2, -1773, 4130),
    (2, 0, 0, 2, -1595, 0),           (4, -1, -1, 0, 1215, -3958),
    (0, 0, 2, 2, -1110, 0),           (3, 0, -1, 0, -892, 3258),
    (2, 1, 1, 0, -810, 2616),         (4, -1, -2, 0, 759, -1897),
    (0, 2, -1, 0, -713, -2117),       (2, 2, -1, 0, -700, 2354),
    (2, 1, -2, 0, 691, 0),            (2, -1, 0, -2, 596, 0),
    (4, 0, 1, 0, 549, -1423),         (0, 0, 4, 0, 537, -1117),
    (4, -1, 0, 0, 520, -1571),        (1, 0, -2, 0, -487, -1739),
    (2, 1, 0, -2, -399, 0),           (0, 0, 2, -2, -381, -4421),
    (1, 1, 1, 0, 351, 0),             (3, 0, -2, 0, -340, 0),
    (4, 0, -3, 0, 330, 0),            (2, -1, 2, 0, 327, 0),
    (0, 2, 1, 0, -323, 1165),         (1, 1, -1, 0, 299, 0),
    (2, 0, 3, 0, 294, 0),             (2, 0, -1, -2, 0, 8752),
]
# (D, M, M', F, Σb[1e-6 度])
_MOON_B = [
    (0, 0, 0, 1, 5128122), (0, 0, 1, 1, 280602), (0, 0, 1, -1, 277693),
    (2, 0, 0, -1, 173237), (2, 0, -1, 1, 55413), (2, 0, -1, -1, 46271),
    (2, 0, 0, 1, 32573),   (0, 0, 2, 1, 17198),  (2, 0, 1, -1, 9266),
    (0, 0, 2, -1, 8822),   (2, -1, 0, -1, 8216), (2, 0, -2, -1, 4324),
    (2, 0, 1, 1, 4200),    (2, 1, 0, -1, -3359), (2, -1, -1, 1, 2463),
    (2, -1, 0, 1, 2211),   (2, -1, -1, -1, 2065), (0, 1, -1, -1, -1870),
    (4, 0, -1, -1, 1828),  (0, 1, 0, 1, -1794),  (0, 0, 0, 3, -1749),
    (0, 1, -1, 1, -1565),  (1, 0, 0, 1, -1491),  (0, 1, 1, 1, -1475),
    (0, 1, 1, -1, -1410),  (0, 1, 0, -1, -1344), (1, 0, 0, -1, -1335),
    (0, 0, 3, 1, 1107),    (4, 0, 0, -1, 1021),  (4, 0, -1, 1, 833),
    (0, 0, 1, -3, 777),    (4, 0, -2, 1, 671),   (2, 0, 0, -3, 607),
    (2, 0, 2, -1, 596),    (2, -1, 1, -1, 491),  (2, 0, -2, 1, -451),
    (0, 0, 3, -1, 439),    (2, 0, 2, 1, 422),    (2, 0, -3, -1, 421),
    (2, 1, -1, 1, -366),   (2, 1, 0, 1, -351),   (4, 0, 0, 1, 331),
    (2, -1, 1, 1, 315),    (2, -2, 0, -1, 302),  (0, 0, 1, 3, -283),
    (2, 1, 1, -1, -229),   (1, 1, 0, -1, 223),   (1, 1, 0, 1, 223),
    (0, 1, -2, -1, -220),  (2, 1, -1, -1, -220), (1, 0, 1, 1, -185),
    (2, -1, -2, -1, 181),  (0, 1, 2, 1, -177),   (4, 0, -2, -1, 176),
    (4, -1, -1, -1, 166),  (1, 0, 1, -1, -164),  (4, 0, 1, -1, 132),
    (1, 0, -1, -1, -119),  (4, -1, 0, -1, 115),  (2, -2, 0, 1, 107),
]


def moon_apparent(jd_tt, jd_ut, sun_lambda=None):
    T = (jd_tt - 2451545.0) / 36525.0
    Lp = norm360(218.3164477 + 481267.88123421 * T - 0.0015786 * T * T
                 + T ** 3 / 538841.0 - T ** 4 / 65194000.0)
    D = norm360(297.8501921 + 445267.1114034 * T - 0.0018819 * T * T
                + T ** 3 / 545868.0 - T ** 4 / 113065000.0)
    M = norm360(357.5291092 + 35999.0502909 * T - 0.0001536 * T * T
                + T ** 3 / 24490000.0)
    Mp = norm360(134.9633964 + 477198.8675055 * T + 0.0087414 * T * T
                 + T ** 3 / 69699.0 - T ** 4 / 14712000.0)
    F = norm360(93.2720950 + 483202.0175233 * T - 0.0036539 * T * T
                - T ** 3 / 3526000.0 + T ** 4 / 863310000.0)
    A1 = norm360(119.75 + 131.849 * T)
    A2 = norm360(53.09 + 479264.290 * T)
    A3 = norm360(313.45 + 481266.484 * T)
    E = 1 - 0.002516 * T - 0.0000074 * T * T

    sl = sr = 0.0
    for d_, m_, mp_, f_, cl, cr in _MOON_LR:
        arg = d_ * D + m_ * M + mp_ * Mp + f_ * F
        ecc = E ** abs(m_) if m_ else 1.0
        sl += cl * ecc * dsin(arg)
        sr += cr * ecc * dcos(arg)
    sb = 0.0
    for d_, m_, mp_, f_, cb in _MOON_B:
        arg = d_ * D + m_ * M + mp_ * Mp + f_ * F
        ecc = E ** abs(m_) if m_ else 1.0
        sb += cb * ecc * dsin(arg)

    sl += 3958 * dsin(A1) + 1962 * dsin(Lp - F) + 318 * dsin(A2)
    sb += (-2235 * dsin(Lp) + 382 * dsin(A3) + 175 * dsin(A1 - F)
           + 175 * dsin(A1 + F) + 127 * dsin(Lp - Mp) - 115 * dsin(Lp + Mp))

    lam = norm360(Lp + sl / 1e6)
    beta = sb / 1e6
    dist = 385000.56 + sr / 1000.0                       # km

    dpsi, deps, om = nutation(T)
    lam_app = lam + dpsi
    eps = mean_obliquity(T) + deps
    ra = norm360(math.degrees(math.atan2(
        dsin(lam_app) * dcos(eps) - dtan(beta) * dsin(eps), dcos(lam_app))))
    dec = math.degrees(math.asin(dsin(beta) * dcos(eps)
                                 + dcos(beta) * dsin(eps) * dsin(lam_app)))
    hp = math.degrees(math.asin(EARTH_RADIUS_KM / dist)) * 60.0   # 角分
    sd = 0.2725 * hp
    if sun_lambda is None:
        sun_lambda = sun_lambda_of(jd_tt)
    elong = norm360(lam - sun_lambda)
    illum = (1 - dcos(elong)) / 2.0
    gast = norm360(gmst_deg(jd_ut) + dpsi * dcos(eps))
    gha = norm360(gast - ra)
    return BodyPos("月亮", ra, dec, gha, dist, sd, hp, elong, illum)


# ===========================================================================
#  星历接口 (内置 / skyfield 自动切换)
# ===========================================================================
class Ephemeris:
    def __init__(self):
        self.use_skyfield = False
        self._sf = None
        self.status = "内置星历 VSOP87/ELP (对比 ERFA: 日<0.4″ 月<0.2″ 金<3″)"

    def try_skyfield(self, allow_download=True):
        """
        尝试启用 skyfield 高精度星历。
        allow_download=False 时只在本机已有 de421.bsp 的情况下启用 (启动时用),
        绝不联网, 以免开程序时卡住。
        """
        try:
            from skyfield.api import Loader                # noqa
        except Exception:
            return False, "未安装 skyfield (pip install skyfield)"
        import os
        from skyfield.api import Loader
        here = os.path.dirname(os.path.abspath(sys.argv[0] or "."))
        cands = [os.getcwd(), here, os.path.expanduser("~"),
                 os.path.expanduser("~/.skyfield")]
        seen = []
        for d in cands:
            if d in seen or not os.path.isdir(d):
                continue
            seen.append(d)
            if not os.path.exists(os.path.join(d, "de421.bsp")):
                continue
            try:
                load = Loader(d, verbose=False)
                ts = load.timescale()
                eph = load("de421.bsp")
                self._sf = {"ts": ts, "eph": eph, "load": load}
                self.use_skyfield = True
                self.status = _T("Skyfield + JPL DE421 (角秒级) · %s") % d
                return True, _T("已启用 Skyfield / DE421 (%s)") % d
            except Exception:
                continue
        if not allow_download:
            return False, "本机没有 de421.bsp (勾选开关可联网下载约 17 MB)"
        try:
            from skyfield.api import load
            ts = load.timescale()
            eph = load("de421.bsp")
            self._sf = {"ts": ts, "eph": eph, "load": load}
            self.use_skyfield = True
            self.status = "Skyfield + JPL DE421 星历 (角秒级)"
            return True, "已启用 Skyfield / DE421 高精度星历"
        except Exception as ex:
            return False, _T("无法载入 de421.bsp: %s") % ex

    def disable_skyfield(self):
        self.use_skyfield = False
        self.status = "内置星历 VSOP87/ELP (对比 ERFA: 日<0.4″ 月<0.2″ 金<3″)"

    # -- 主接口 --------------------------------------------------------------
    def get(self, body, utc):
        """返回 BodyPos (地心视位置 + GHA)。"""
        if self.use_skyfield and self._sf:
            try:
                return self._get_sf(body, utc)
            except Exception:
                pass
        jd_ut = julian_day(utc)
        jd_tt = jd_ut + delta_t_seconds(utc) / 86400.0
        if body == "太阳":
            return sun_apparent(jd_tt, jd_ut)
        if body == "月亮":
            return moon_apparent(jd_tt, jd_ut)
        if is_star(body):
            return star_apparent(body, jd_tt, jd_ut)
        return planet_apparent(body, jd_tt, jd_ut)

    def _get_sf(self, body, utc):
        if is_star(body):
            jd_ut = julian_day(utc)
            return star_apparent(body, jd_ut + delta_t_seconds(utc) / 86400.0, jd_ut)
        sf = self._sf
        ts, eph = sf["ts"], sf["eph"]
        t = ts.utc(utc.year, utc.month, utc.day, utc.hour, utc.minute,
                   utc.second + utc.microsecond / 1e6)
        earth = eph['earth']
        tgt = {"太阳": 'sun', "月亮": 'moon'}.get(body) or PLANET_SF[body]
        astrometric = earth.at(t).observe(eph[tgt]).apparent()
        ra_obj, dec_obj, dist = astrometric.radec('date')
        ra = norm360(ra_obj._degrees)
        dec = dec_obj.degrees
        dist_km = dist.km
        radius_km = ({"太阳": 695700.0, "月亮": 1737.4}.get(body)
                     or PLANET_RADIUS_KM[body])
        sd = math.degrees(math.asin(min(1.0, radius_km / dist_km))) * 60.0
        hp = math.degrees(math.asin(min(1.0, EARTH_RADIUS_KM / dist_km))) * 60.0
        gast = t.gast * 15.0
        gha = norm360(gast - ra)
        illum, phase = 1.0, 0.0
        if body != "太阳":
            s = earth.at(t).observe(eph['sun']).apparent()
            sep = astrometric.separation_from(s).degrees
            phase = sep
            illum = (1 - math.cos(sep * D2R)) / 2.0
        return BodyPos(body, ra, dec, gha, dist_km, sd, hp, phase, illum)


EPH = Ephemeris()


# ===========================================================================
#  地平坐标 / 折射 / 视差
# ===========================================================================
def altaz_from_hadec(lha_deg, dec_deg, lat_deg):
    """由地方时角 LHA(西正)、赤纬、纬度求 (真高度角, 方位角 北起顺时针)。"""
    sh = (dsin(lat_deg) * dsin(dec_deg)
          + dcos(lat_deg) * dcos(dec_deg) * dcos(lha_deg))
    sh = max(-1.0, min(1.0, sh))
    alt = math.degrees(math.asin(sh))
    y = -dcos(dec_deg) * dsin(lha_deg)
    x = (dsin(dec_deg) * dcos(lat_deg)
         - dcos(dec_deg) * dsin(lat_deg) * dcos(lha_deg))
    az = norm360(math.degrees(math.atan2(y, x)))
    return alt, az


def refraction_bennett(h_app_deg, pressure=1010.0, temp_c=10.0):
    """Bennett 折射公式: 输入 *视* 高度角(度), 返回折射量(角分)。"""
    if h_app_deg < -2.0:
        h_app_deg = -2.0
    r = 1.0 / dtan(h_app_deg + 7.31 / (h_app_deg + 4.4))
    f = (pressure / 1010.0) * (283.0 / (273.0 + temp_c))
    return r * f


def refraction_true_to_app(h_true_deg, pressure=1010.0, temp_c=10.0):
    """真高度 -> 视高度 的折射量 (角分), 迭代求解。"""
    h = h_true_deg
    for _ in range(5):
        r = refraction_bennett(h, pressure, temp_c)
        h = h_true_deg + r / 60.0
    return (h - h_true_deg) * 60.0


def dip_arcmin(height_eye_m):
    """眼高造成的地平线俯角 (角分)。"""
    if height_eye_m <= 0:
        return 0.0
    return 1.758 * math.sqrt(height_eye_m)


def topocentric_alt(pos, lat, lon, utc, height_eye_m=0.0,
                    pressure=1010.0, temp_c=10.0):
    """
    返回 dict: 地心真高度 / 站心真高度 / 站心视高度(经折射) / 方位角 / LHA。
    """
    lha = norm360(pos.gha + lon)
    alt_geo, az = altaz_from_hadec(lha, pos.dec, lat)
    # 高度视差 (使天体降低)
    par = (pos.hp_arcmin / 60.0) * dcos(alt_geo)
    alt_topo = alt_geo - par
    r = refraction_true_to_app(alt_topo, pressure, temp_c)
    alt_app = alt_topo + r / 60.0
    return {"lha": lha, "az": az, "alt_geo": alt_geo, "alt_topo": alt_topo,
            "alt_app": alt_app, "refr": r, "parallax": par * 60.0}


# ===========================================================================
#  其余大行星的 VSOP87D 截断级数 (水星/火星/木星/土星)
#  截断门限: L,B 振幅 >= 2e-6 弧度 (0.4″); 外行星 R >= 1.2e-5 AU
#  (距离误差 δr 造成的地心方向误差 ≈ δr/Δ, 对木土远小于 0.5″)
# ===========================================================================
_ME_L = [
    [(440250710.1,0.0000000,0.0000000),(40989415.0,1.4830203,26087.9031416),(5046294.2,4.4778549,52175.8062831),
     (855346.8,1.1652032,78263.7094247),(165590.4,4.1196916,104351.6125663),(34561.9,0.7793077,130439.5157079),
     (7583.5,3.7134840,156527.4188494),(3559.7,1.5120267,1109.3785521),(1726.0,0.3583224,182615.3219910),
     (1803.5,4.1033318,5661.3320492),(1364.7,4.5991832,27197.2816937),(1589.9,2.9951042,25028.5212114),
     (1017.3,0.8803144,31749.2351907),(714.2,1.5414487,24978.5245895),(643.8,5.3026611,21535.9496445),
     (404.2,3.2822885,208703.2251326),(352.4,5.2415630,20426.5710924),(343.3,5.7653189,955.5997416),
     (339.2,5.8632776,25558.2121765),(451.1,6.0498928,51116.4243530),(325.3,1.3367433,53285.1848352),
     (259.6,0.9873243,4551.9534971),(345.2,2.7921190,15874.6175954),(272.9,2.4945116,529.6909651),
     (234.8,0.2667212,11322.6640983),(238.8,0.1134395,1059.3819302),(264.3,3.9170509,57837.1383323),
     (216.6,0.6598721,13521.7514416),(209.0,2.0917823,47623.8527861),],
    [(2608814706222.7,0.0000000,0.0000000),(1126007.8,6.2170397,26087.9031416),(303471.4,3.0556547,52175.8062831),
     (80538.5,6.1045474,78263.7094247),(21245.0,2.8353193,104351.6125663),(5592.1,5.8267567,130439.5157079),
     (1472.2,2.5184546,156527.4188494),(352.2,3.0523809,1109.3785521),(388.3,5.4803923,182615.3219910),],
    [(53049.8,0.0000000,0.0000000),(16903.7,4.6907230,26087.9031416),(7396.7,1.3473562,52175.8062831),
     (3018.3,4.4564354,78263.7094247),(1107.4,1.2622654,104351.6125663),(378.2,4.3199806,130439.5157079),],
    [],
    [],
    [],
]
_ME_B = [
    [(11737529.0,1.9835750,26087.9031416),(2388077.0,5.0373896,52175.8062831),(1222839.5,3.1415927,0.0000000),
     (543251.8,1.7964436,78263.7094247),(129778.8,4.8323250,104351.6125663),(31866.9,1.5808850,130439.5157079),
     (7963.3,4.6097213,156527.4188494),(2014.2,1.3532416,182615.3219910),(514.0,4.3783541,208703.2251326),
     (207.7,4.9177256,27197.2816937),(208.6,2.0202029,24978.5245895),],
    [(429151.4,3.5016978,26087.9031416),(146233.7,3.1415927,0.0000000),(22675.3,0.0151537,52175.8062831),
     (10895.0,0.4854017,78263.7094247),(6353.5,3.4294392,104351.6125663),(2495.7,0.1605121,130439.5157079),
     (859.6,3.1845243,156527.4188494),(277.5,6.2102077,182615.3219910),],
    [(11830.9,4.7906559,26087.9031416),(1913.5,0.0000000,0.0000000),(1044.8,1.2121654,52175.8062831),
     (266.2,4.4341834,78263.7094247),],
    [(235.4,0.3538752,26087.9031416),],
    [],
    [],
]
_ME_R = [
    [(39528271.7,0.0000000,0.0000000),(7834131.8,6.1923372,26087.9031416),(795525.6,2.9598969,52175.8062831),
     (121281.8,6.0106415,78263.7094247),(21922.0,2.7782009,104351.6125663),(4354.1,5.8289454,130439.5157079),
     (918.2,2.5965056,156527.4188494),(260.0,3.0281775,27197.2816937),(290.0,1.4244194,25028.5212114),
     (201.9,5.6472504,182615.3219910),(201.5,5.5922772,31749.2351907),],
    [(217347.7,4.6561716,26087.9031416),(44141.8,1.4238554,52175.8062831),(10094.5,4.4746633,78263.7094247),
     (2432.8,1.2422608,104351.6125663),(1624.4,0.0000000,0.0000000),(604.0,4.2930312,130439.5157079),],
    [(3117.9,3.0823184,26087.9031416),(1245.4,6.1518332,52175.8062831),(424.8,2.9258335,78263.7094247),],
    [],
    [],
    [],
]
_MA_L = [
    [(620347711.6,0.0000000,0.0000000),(18656368.1,5.0503710,3340.6124267),(1108216.8,5.4009984,6681.2248534),
     (91798.4,5.7547875,10021.8372801),(27745.0,5.9704951,3.5231183),(10610.2,2.9395852,2281.2304965),
     (12315.9,0.8495608,2810.9214616),(8926.8,4.1569785,0.0172537),(8715.7,6.1100516,13362.4497068),
     (6797.6,0.3646224,398.1490034),(7774.9,3.3396866,5621.8429232),(3575.1,1.6618654,2544.3144199),
     (4161.1,0.2281498,2942.4634233),(3075.2,0.8569660,191.4482661),(2628.1,0.6480614,3337.0893084),
     (2937.5,6.0789371,0.0673103),(2389.4,5.0389640,796.2980068),(2579.8,0.0299671,3344.1355450),
     (1528.1,1.1497931,6151.5338883),(1798.8,0.6563403,529.6909651),(1264.4,3.6227509,5092.1519581),
     (1286.2,3.0679592,2146.1654165),(1546.4,2.9157963,1751.5395314),(1024.9,3.6933429,8962.4553499),
     (891.6,0.1829390,16703.0621335),(858.8,2.4009370,2914.0142358),(832.7,2.4641859,3340.5951730),
     (832.7,4.4949575,3340.6296804),(712.9,3.6633601,1059.3819302),(748.7,3.8224840,155.4203994),
     (723.9,0.6749757,3738.7614301),(635.6,2.9218270,8432.7643848),(655.2,0.4886408,3127.3133313),
     (550.5,3.8100121,0.9803211),(552.7,4.4747886,1748.0164131),(426.0,0.5536514,6283.0758500),
     (415.1,0.4966231,213.2990954),(472.2,3.6254782,1194.4470102),(306.6,0.3805286,6684.7479717),
     (312.1,0.9985332,6677.7017351),(293.2,4.2213128,20.7753955),(302.4,4.4861815,3532.0606928),
     (274.0,0.5422214,3340.5451164),(281.1,5.8816337,1349.8674097),(231.2,1.2824069,3870.3033918),
     (283.6,5.7688549,3149.1641606),(236.1,5.7550452,3333.4988797),(274.0,0.1337250,3340.6797370),
     (299.4,2.7832371,6254.6266625),(204.2,2.8213327,1221.8485663),(238.9,5.3715547,4136.9104335),
     (221.2,3.5046667,382.8965322),],
    [(334085627474.3,0.0000000,0.0000000),(1458227.1,3.6042605,3340.6124267),(164901.3,3.9263125,6681.2248534),
     (19963.3,4.2659406,10021.8372801),(3452.4,4.7321039,3.5231183),(2485.5,4.6127757,13362.4497068),
     (841.6,4.4585826,2281.2304965),(537.6,5.0158973,398.1490034),(521.0,4.9942268,3344.1355450),
     (432.6,2.5606640,191.4482661),(429.7,5.3164616,155.4203994),(381.7,3.5388129,796.2980068),
     (314.1,4.9633527,16703.0621335),(282.8,3.1596752,2544.3144199),(205.7,4.5689146,2146.1654165),],
    [(58015.8,2.0497946,3340.6124267),(54187.6,0.0000000,0.0000000),(13908.4,2.4574236,6681.2248534),
     (2465.1,2.8000002,10021.8372801),(398.4,3.1411843,13362.4497068),(222.0,3.1943608,3.5231183),],
    [(1482.4,0.4443469,3340.6124267),(662.1,0.8846918,6681.2248534),],
    [],
    [],
]
_MA_B = [
    [(3197135.0,3.7683204,3340.6124267),(298033.2,4.1061700,6681.2248534),(289104.7,0.0000000,0.0000000),
     (31365.5,4.4465105,10021.8372801),(3484.1,4.7881255,13362.4497068),(443.0,5.6523302,3337.0893084),
     (443.4,5.0264262,3344.1355450),(399.1,5.1305681,16703.0621335),(292.5,3.7929064,2281.2304965),],
    [(350068.8,5.3684784,3340.6124267),(14116.0,3.1415927,0.0000000),(9670.8,5.4787779,6681.2248534),
     (1471.9,3.2020577,10021.8372801),(425.9,3.4084381,13362.4497068),],
    [(16726.7,0.6022139,3340.6124267),(4986.8,3.1415927,0.0000000),(302.1,5.5587128,6681.2248534),],
    [(606.5,1.9805063,3340.6124267),],
    [],
    [],
]
_MA_R = [
    [(153033488.3,0.0000000,0.0000000),(14184953.2,3.4797128,3340.6124267),(660776.4,3.8178344,6681.2248534),
     (46179.1,4.1559532,10021.8372801),(8109.7,5.5595846,2810.9214616),(7485.3,1.7723900,5621.8429232),
     (5523.2,1.3643632,2281.2304965),(3825.2,4.4940718,13362.4497068),(2306.5,0.0908174,2544.3144199),
     (1999.4,5.3605961,3337.0893084),(2484.4,4.9254558,2942.4634233),(1960.2,4.7424939,3344.1355450),
     (1167.1,2.1126150,5092.1519581),(1102.8,5.0090826,398.1490034),(899.1,4.4079043,529.6909651),
     (992.3,5.8386240,6151.5338883),(807.3,2.1021665,1059.3819302),(797.9,3.4483903,796.2980068),
     (741.0,1.4990634,2146.1654165),(692.3,2.1337881,8962.4553499),(633.1,0.8935329,3340.5951730),
     (725.6,1.2451691,8432.7643848),(633.1,2.9243045,3340.6296804),(574.4,0.8289620,2914.0142358),
     (526.2,5.3829228,3738.7614301),(630.0,1.2873814,1751.5395314),(472.8,5.1985046,3127.3133313),
     (348.1,4.8321920,16703.0621335),(283.7,2.9069229,3532.0606928),(279.6,5.2574925,6283.0758500),
     (233.8,5.1054649,5486.7778432),(219.4,5.5834025,191.4482661),(269.9,3.7639473,5884.9268466),
     (208.3,5.2547608,3340.5451164),(275.2,2.9081888,1748.0164131),(275.5,1.2176797,6254.6266625),
     (239.1,2.0366990,1194.4470102),(223.2,4.1986159,3149.1641606),(208.3,4.8462644,3340.6797370),
     (228.1,3.2552902,6872.6731195),],
    [(1107433.3,2.0325052,3340.6124267),(103175.9,2.3707185,6681.2248534),(12877.2,0.0000000,0.0000000),
     (10815.9,2.7088809,10021.8372801),(1194.5,3.0470218,13362.4497068),(438.6,2.8883507,2281.2304965),
     (395.7,3.4232461,3344.1355450),],
    [(44242.2,0.4793060,3340.6124267),(8138.0,0.8699840,6681.2248534),(1274.9,1.2259405,10021.8372801),],
    [(1113.1,5.1498735,3340.6124267),(424.4,5.6134377,6681.2248534),],
    [],
    [],
]
_JU_L = [
    [(59954691.5,0.0000000,0.0000000),(9695898.7,5.0619179,529.6909651),(573610.1,1.4440621,7.1135470),
     (306389.2,5.4173473,1059.3819302),(97178.3,4.1426471,632.7837393),(72903.1,3.6404291,522.5774181),
     (64264.0,3.4114519,103.0927742),(39806.1,2.2937674,419.4846439),(38857.8,1.2723172,316.3918697),
     (27964.6,1.7845459,536.8045121),(13589.7,5.7748103,1589.0728953),(8246.4,3.5822796,206.1855484),
     (8768.7,3.6300032,949.1756090),(7368.1,5.0810113,735.8765135),(6263.2,0.0249764,213.2990954),
     (6114.1,4.5131953,1162.4747044),(4905.4,1.3208463,110.2063212),(5305.3,1.3067124,14.2270940),
     (5305.5,4.1862505,1052.2683832),(4647.2,4.6995811,3.9321533),(3045.0,4.3167596,426.5981909),
     (2610.0,1.5666759,846.0828348),(2028.2,1.0637655,3.1813937),(1764.8,2.1414808,1066.4954772),
     (1723.0,3.8803601,1265.5674786),(1921.0,0.9716893,639.8972863),(1633.2,3.5820109,515.4638711),
     (1432.0,4.2968369,625.6701923),(973.3,4.0976496,95.9792272),(884.4,2.4370143,412.3710969),
     (732.9,6.0853411,838.9692878),(731.1,3.8059123,1581.9593483),(691.9,6.1336822,2118.7638604),
     (709.2,1.2927257,742.9900605),(614.5,4.1085350,1478.8665741),(495.2,3.7556746,323.5054167),
     (581.9,4.5396772,309.2783227),(375.7,4.7029912,1368.6602528),(389.9,4.8971611,1692.1656695),
     (341.0,5.7145253,533.6231184),(330.5,4.7404982,0.0481841),(440.9,2.9581846,454.9093665),
     (417.3,1.0355443,2.4476806),(244.2,5.2202088,728.7629665),(261.5,1.8765246,0.9632078),
     (256.6,3.7241072,199.0720014),(261.0,0.8204725,380.1277680),(220.4,1.6511502,543.9180591),
     (202.0,1.8068457,1375.7737998),(207.3,1.8546167,525.7588118),(235.1,1.2269391,909.8187331),],
    [(52993480757.5,0.0000000,0.0000000),(489741.2,4.2206669,529.6909651),(228918.5,6.0264746,7.1135470),
     (27655.4,4.5726596,1059.3819302),(20720.9,5.4593894,522.5774181),(12105.7,0.1698577,536.8045121),
     (6068.1,4.4241950,103.0927742),(5433.9,3.9847838,419.4846439),(4237.8,5.8900935,14.2270940),
     (2211.9,5.2677145,206.1855484),(1295.8,5.5513277,3.1813937),(1745.9,4.9266938,1589.0728953),
     (1163.4,0.5145090,3.9321533),(1007.2,0.4647840,735.8765135),(1173.1,5.8564730,1052.2683832),
     (847.7,5.7580585,110.2063212),(827.3,4.8031202,213.2990954),(1003.6,3.1504030,426.5981909),
     (1098.7,5.3070498,515.4638711),(816.4,0.5864305,1066.4954772),(725.4,5.5182747,639.8972863),
     (567.8,5.9886705,625.6701923),(474.2,4.1324527,412.3710969),(412.9,5.7365289,95.9792272),
     (335.8,3.7324875,1162.4747044),(345.2,4.2415957,632.7837393),(234.1,6.2430223,309.2783227),
     (234.3,4.0346997,949.1756090),],
    [(47233.6,4.3214832,7.1135470),(30629.1,2.9302144,529.6909651),(38965.6,0.0000000,0.0000000),
     (3189.3,1.0550462,522.5774181),(2723.4,3.4141153,1059.3819302),(2729.3,4.8454548,536.8045121),
     (1721.1,4.1873439,14.2270940),(383.3,5.7679071,419.4846439),(367.5,6.0550912,103.0927742),
     (377.5,0.7604896,515.4638711),(337.4,3.7864438,3.1813937),(308.2,0.6935665,206.1855484),
     (218.4,3.8138919,1589.0728953),],
    [(6501.7,2.5986288,7.1135470),(1356.5,1.3463589,529.6909651),(470.7,2.4750398,14.2270940),
     (417.0,3.2445124,536.8045121),(352.9,2.9736016,522.5774181),],
    [(669.5,0.8528242,7.1135470),],
    [],
]
_JU_B = [
    [(2268615.7,3.5585261,529.6909651),(109971.6,3.9080935,1059.3819302),(110090.4,0.0000000,0.0000000),
     (8101.4,3.6050957,522.5774181),(6044.0,4.2588311,1589.0728953),(6437.8,0.3062712,536.8045121),
     (1106.9,2.9853442,1162.4747044),(941.7,2.9361907,1052.2683832),(894.1,1.7544743,7.1135470),
     (767.3,2.1547359,632.7837393),(944.3,1.6752229,426.5981909),(684.2,3.6780877,213.2990954),
     (629.2,0.6434328,1066.4954772),(835.9,5.1788197,103.0927742),(531.7,2.7030595,110.2063212),
     (558.5,0.0135483,846.0828348),(464.4,1.1733725,949.1756090),(431.1,2.6082500,419.4846439),
     (351.4,4.6106299,2118.7638604),],
    [(177351.8,5.7016649,529.6909651),(3230.2,5.7794162,1059.3819302),(3081.4,5.4746430,522.5774181),
     (2211.9,4.7347748,536.8045121),(1694.2,3.1415927,0.0000000),(346.4,4.7459517,1052.2683832),
     (234.3,5.1885610,1066.4954772),],
    [(8094.1,1.4632284,529.6909651),(742.4,0.9569164,522.5774181),(813.2,3.1415927,0.0000000),
     (399.0,2.8988867,536.8045121),(342.2,1.4468379,1059.3819302),],
    [(251.6,3.3808792,529.6909651),],
    [],
    [],
]
_JU_R = [
    [(520887429.5,0.0000000,0.0000000),(25209327.0,3.4910864,529.6909651),(610599.9,3.8411537,1059.3819302),
     (282029.5,2.5741988,632.7837393),(187647.4,2.0759038,522.5774181),(86792.9,0.7100109,419.4846439),
     (72062.9,0.2146569,536.8045121),(65517.2,5.9799585,316.3918697),(29134.6,1.6775924,103.0927742),
     (30135.3,2.1613206,949.1756090),(23453.2,3.5402315,735.8765135),(22283.7,4.1936277,1589.0728953),
     (23947.3,0.2745785,7.1135470),(13032.6,2.9604306,1162.4747044),(9703.3,1.9066957,206.1855484),
     (12749.0,2.7155010,1052.2683832),(9161.4,4.4135262,213.2990954),(7894.5,2.4790755,426.5981909),
     (7058.0,2.1818475,1265.5674786),(6137.8,6.2641754,846.0828348),(5477.1,5.6572933,639.8972863),
     (3502.5,0.5653130,1066.4954772),(4136.9,2.7221998,625.6701923),(4170.0,2.0160503,515.4638711),
     (2500.0,4.5518206,838.9692878),(2617.0,2.0099397,1581.9593483),(1911.9,0.8562193,412.3710969),
     (2127.6,6.1275146,742.9900605),(1610.5,3.0886779,1368.6602528),(1479.5,2.6802619,1478.8665741),
     (1230.7,1.8904298,323.5054167),(1216.8,1.8017156,110.2063212),],
    [(1271801.6,2.6493751,529.6909651),(61661.8,3.0007625,1059.3819302),(53443.6,3.8971764,522.5774181),
     (31185.2,4.8827666,536.8045121),(41390.3,0.0000000,0.0000000),(11847.2,2.4132959,419.4846439),
     (9166.4,4.7597941,7.1135470),(3175.8,2.7929799,103.0927742),(3203.4,5.2108329,735.8765135),
     (3403.6,3.3468854,1589.0728953),(2600.0,3.6343510,206.1855484),(2412.2,1.4694731,426.5981909),
     (2806.1,3.7422369,515.4638711),(2676.6,4.3305288,1052.2683832),(2100.5,3.9276268,639.8972863),
     (1646.2,5.3095351,1066.4954772),(1641.3,4.4162867,625.6701923),],
    [(79644.8,1.3586590,529.6909651),(8251.6,5.7777394,522.5774181),(7029.9,3.2747697,536.8045121),
     (5314.0,1.8383511,1059.3819302),(1860.8,2.9768214,7.1135470),],
    [(3519.3,6.0580063,529.6909651),],
    [],
    [],
]
_SA_L = [
    [(87401354.0,0.0000000,0.0000000),(11107659.8,3.9620509,213.2990954),(1414151.0,4.5858152,7.1135470),
     (398379.4,0.5211203,206.1855484),(350769.2,3.3032990,426.5981909),(206816.3,0.2465837,103.0927742),
     (79271.3,3.8400708,220.4126424),(23990.3,4.6697693,110.2063212),(16573.6,0.4371912,419.4846439),
     (14907.0,5.7690328,316.3918697),(15820.3,0.9380895,632.7837393),(14609.6,1.5651857,3.9321533),
     (13160.3,4.4489118,14.2270940),(15053.5,2.7167003,639.8972863),(13005.3,5.9811907,11.0457003),
     (10725.1,3.1293960,202.2533952),(5863.2,0.2365703,529.6909651),(5227.8,4.2078316,3.1813937),
     (6126.3,1.7632850,277.0349937),(5019.7,3.1778792,433.7117379),(4592.5,0.6197642,199.0720014),
     (4005.9,2.2447989,63.7358983),(2953.8,0.9828039,95.9792272),(3873.7,3.2228269,138.5174969),
     (2461.2,2.0316363,735.8765135),(3269.5,0.7749190,949.1756090),(1758.1,3.2658051,522.5774181),
     (1640.2,5.5050497,846.0828348),(1391.3,4.0233198,323.5054167),(1580.6,4.3726631,309.2783227),
     (1123.5,2.8372679,415.5524906),(1017.3,3.7169815,227.5261894),(848.6,3.1914983,209.3669422),
     (1087.2,4.1834323,2.4476806),(956.8,0.5074089,1265.5674786),(789.2,5.0074512,0.9632078),
     (687.0,1.7471441,1052.2683832),(654.5,1.5988933,0.0481841),(748.8,2.1439815,853.1963818),
     (634.0,2.2988990,412.3710969),(743.6,5.2527695,224.3447957),(852.7,3.4214135,175.1660598),
     (579.9,3.0925901,74.7815986),(624.9,0.9704683,210.1177017),(529.9,4.4493890,117.3198682),
     (542.6,1.5182432,9.5612276),(474.3,5.4752719,742.9900605),(448.5,1.2899042,127.4717966),
     (546.4,2.1267855,350.3321196),(478.1,2.9648805,137.0330242),(354.9,3.0128648,838.9692878),
     (451.8,1.0443666,490.3340892),(347.4,1.5392823,340.7708920),(343.5,0.2460404,0.5212649),
     (309.0,3.4948673,216.4804892),(322.2,0.9613746,203.7378679),(372.3,2.2781911,217.2312487),
     (321.5,2.5718235,647.0108333),(330.2,0.2471562,1581.9593483),(249.1,1.4701053,1368.6602528),
     (286.7,2.3704375,351.8165923),(220.2,4.2042242,200.7689225),(277.8,0.4002041,211.8146227),
     (204.5,6.0108221,265.9892935),(207.7,0.4834982,1162.4747044),(208.7,1.3451626,625.6701923),
     (226.6,4.9100316,12.5301730),(207.7,1.2830222,39.3568759),],
    [(21354295596.0,0.0000000,0.0000000),(1296855.0,1.8282054,213.2990954),(564347.6,2.8850014,7.1135470),
     (98323.0,1.0807006,426.5981909),(107678.8,2.2776991,206.1855484),(40254.6,2.0412826,220.4126424),
     (19941.7,1.2795466,103.0927742),(10511.7,2.7488039,14.2270940),(6939.2,0.4049308,639.8972863),
     (4803.3,2.4419410,419.4846439),(4056.3,2.9216662,110.2063212),(3768.6,3.6496563,3.9321533),
     (3384.7,2.4169425,3.1813937),(3302.2,1.2625649,433.7117379),(3071.4,2.3273932,199.0720014),
     (1953.0,3.5639468,11.0457003),(1249.3,2.6280374,95.9792272),(921.7,1.9608983,227.5261894),
     (705.6,4.4168925,529.6909651),(649.7,6.1741809,202.2533952),(627.6,6.1108823,309.2783227),
     (486.8,6.0399820,853.1963818),(468.4,4.6170784,63.7358983),(478.5,4.9877699,522.5774181),
     (417.0,2.1170817,323.5054167),(407.6,1.2994956,209.3669422),(343.8,3.9585418,412.3710969),
     (339.7,3.6339640,316.3918697),(335.9,3.7717307,735.8765135),(331.9,2.8607770,210.1177017),
     (352.5,2.3170708,632.7837393),(289.4,2.7326308,117.3198682),(265.8,0.5434463,647.0108333),
     (230.5,1.6442888,216.4804892),(280.9,5.7439885,2.4476806),],
    [(116441.2,1.1798785,7.1135470),(91920.8,0.0742526,213.2990954),(90592.3,0.0000000,0.0000000),
     (15276.9,4.0649201,206.1855484),(10631.4,0.2577828,220.4126424),(10605.0,5.4096360,426.5981909),
     (4265.4,1.0459556,14.2270940),(1215.5,2.9186004,103.0927742),(1164.7,4.6094213,639.8972863),
     (1082.0,5.6913035,433.7117379),(1020.1,0.6336918,3.1813937),(1044.8,4.0420645,199.0720014),
     (633.6,4.3882541,419.4846439),(549.3,5.5730313,3.9321533),(456.9,1.2684097,110.2063212),
     (425.1,0.2093550,227.5261894),(273.7,4.2884101,95.9792272),],
    [(16038.7,5.7394538,7.1135470),(4249.8,4.5853968,213.2990954),(1906.5,4.7608205,220.4126424),
     (1465.7,5.9132668,206.1855484),(1162.0,5.6197313,14.2270940),(1066.6,3.6081653,426.5981909),
     (239.4,3.8608827,433.7117379),(237.0,5.7682645,199.0720014),],
    [(1661.9,3.9982625,7.1135470),(257.1,2.9843650,220.4126424),(236.3,3.9024143,14.2270940),],
    [],
]
_SA_B = [
    [(4330678.0,3.6028443,213.2990954),(240348.3,2.8523849,426.5981909),(84745.9,0.0000000,0.0000000),
     (30863.4,3.4844150,220.4126424),(34116.1,0.5729731,206.1855484),(14734.1,2.1184660,639.8972863),
     (9916.7,5.7900319,419.4846439),(6993.6,4.7360469,7.1135470),(4807.6,5.4330532,316.3918697),
     (4788.4,4.9651293,110.2063212),(3432.1,2.7325575,433.7117379),(1506.1,6.0130454,103.0927742),
     (1060.3,5.6309929,529.6909651),(969.1,5.2043497,632.7837393),(942.0,1.3964668,853.1963818),
     (707.6,3.8030233,323.5054167),(552.3,5.1314911,202.2533952),(399.7,3.3589141,227.5261894),
     (316.1,1.9971676,647.0108333),(319.4,3.6257155,209.3669422),(284.5,4.8864848,224.3447957),
     (314.2,0.4651027,217.2312487),(236.4,2.1388747,11.0457003),(215.4,5.9498261,846.0828348),
     (208.5,2.1200389,415.5524906),(207.2,0.7302146,199.0720014),],
    [(397555.0,5.3328999,213.2990954),(49478.6,3.1415927,0.0000000),(18571.6,6.0991921,426.5981909),
     (14800.6,2.3058606,206.1855484),(9644.0,1.6967466,220.4126424),(3757.2,1.2542951,419.4846439),
     (2716.6,5.9116666,639.8972863),(1455.3,0.8516162,433.7117379),(1290.6,2.9177086,7.1135470),
     (852.6,0.4357208,316.3918697),(284.4,1.6188175,227.5261894),(292.2,5.3157425,853.1963818),
     (275.1,3.8886414,103.0927742),(297.7,0.9190921,632.7837393),],
    [(20630.0,0.5048242,213.2990954),(3719.6,3.9983348,206.1855484),(1627.2,6.1818994,220.4126424),
     (1346.1,0.0000000,0.0000000),(705.8,3.0391431,419.4846439),(365.0,5.0992868,426.5981909),
     (329.6,5.2789921,433.7117379),(219.3,3.8284153,639.8972863),],
    [(666.3,1.9900634,213.2990954),(632.4,5.6977832,206.1855484),(398.1,0.0000000,0.0000000),],
    [],
    [],
]
_SA_R = [
    [(955758135.8,0.0000000,0.0000000),(52921382.5,2.3922622,213.2990954),(1873679.9,5.2354961,206.1855484),
     (1464664.0,1.6476305,426.5981909),(821891.1,5.9352003,316.3918697),(547506.9,5.0153263,103.0927742),
     (371684.4,2.2711483,220.4126424),(361778.4,3.1390430,7.1135470),(140617.5,5.7040665,632.7837393),
     (108974.7,3.2931360,110.2063212),(69007.0,5.9409962,419.4846439),(61053.3,0.9403776,639.8972863),
     (48913.0,1.5573339,202.2533952),(34143.8,0.1951855,277.0349937),(32401.7,5.4708461,949.1756090),
     (20936.6,0.4634916,735.8765135),(20839.1,1.5210259,433.7117379),(20746.7,5.3325567,199.0720014),
     (15298.5,3.0594365,529.6909651),(14296.5,2.6043354,323.5054167),(11993.3,5.9805142,846.0828348),
     (11380.3,1.7310575,522.5774181),(12884.1,1.6489231,138.5174969),(7752.8,5.8519132,95.9792272),
     (9796.1,5.2047586,1265.5674786),(6466.0,0.1773316,1052.2683832),(6770.6,3.0043348,14.2270940),
     (5850.4,1.4551964,415.5524906),(5307.5,0.5973753,63.7358983),(4695.7,2.1491904,227.5261894),
     (4044.0,1.6401032,209.3669422),(3688.1,0.7801613,412.3710969),(3376.5,3.6952848,224.3447957),
     (2885.3,1.3876408,838.9692878),(2976.0,5.6846793,210.1177017),(3419.6,4.9454915,1581.9593483),
     (3460.9,1.8508880,175.1660598),(3400.6,0.5538675,350.3321196),(2507.6,3.5385186,742.9900605),
     (2448.3,6.1841239,1368.6602528),(2406.1,2.9655922,117.3198682),(2881.2,0.1796076,853.1963818),
     (2174.0,0.0150859,340.7708920),(2024.5,5.0541127,11.0457003),(1740.3,2.3465704,309.2783227),
     (1861.4,5.9336164,625.6701923),(1888.4,0.0296844,3.9321533),(1610.9,1.1730246,74.7815986),
     (1462.6,1.9258813,216.4804892),(1474.5,5.6767046,203.7378679),(1395.1,5.9366940,127.4717966),
     (1781.2,0.7631439,217.2312487),(1817.2,5.7771323,490.3340892),(1472.4,1.4006492,137.0330242),
     (1304.1,0.7723561,647.0108333),(1277.5,2.9841259,1059.3819302),(1207.1,0.7528593,351.8165923),
     (1315.0,5.1120257,211.8146227),(1295.6,4.6918414,1898.3512179),],
    [(6182981.3,0.2584352,213.2990954),(506577.6,0.7111465,206.1855484),(341394.1,5.7963577,426.5981909),
     (188491.4,0.4721572,220.4126424),(186261.5,3.1415927,0.0000000),(143891.2,1.4074486,7.1135470),
     (49621.1,6.0174447,103.0927742),(20928.2,5.0924565,639.8972863),(19952.6,1.1756013,419.4846439),
     (18839.6,1.6081956,110.2063212),(12892.8,5.9433026,433.7117379),(13876.6,0.7588620,199.0720014),
     (5396.7,1.2885241,14.2270940),(4869.3,0.8679389,323.5054167),(4247.5,0.3929938,227.5261894),
     (3252.1,1.2585347,95.9792272),(2856.0,2.1673141,735.8765135),(2909.4,4.6067915,202.2533952),
     (3081.4,3.4366256,522.5774181),(1987.7,2.4505420,412.3710969),(1941.3,6.0239339,209.3669422),
     (1581.4,1.2919179,210.1177017),(1339.5,4.3080182,853.1963818),(1315.6,1.2529645,117.3198682),
     (1203.1,1.8665467,316.3918697),],
    [(436902.5,4.7867167,213.2990954),(71922.8,2.5006999,206.1855484),(49766.8,4.9716815,220.4126424),
     (43220.9,3.8694044,426.5981909),(29645.6,5.9631026,7.1135470),(4141.6,4.1067094,433.7117379),
     (4720.9,2.4752799,199.0720014),(3789.4,3.0977103,639.8972863),(2964.0,1.3720625,103.0927742),
     (2556.4,2.8506572,419.4846439),(2208.5,6.2758886,110.2063212),(2187.6,5.8554583,14.2270940),
     (1956.9,4.9244862,227.5261894),(2326.8,0.0000000,0.0000000),],
    [(20315.0,3.0218663,213.2990954),(8923.6,3.1914421,220.4126424),(6908.7,4.3517489,206.1855484),
     (4087.1,4.2240693,7.1135470),(3879.0,2.0105645,426.5981909),],
    [(1202.0,1.4149945,220.4126424),],
    [],
]

_PLANET_SERIES = {}          # 在 p1 表定义之后填充 (见下)
PLANET_RADIUS_KM = {"水星": 2439.7, "金星": 6051.8, "火星": 3396.2,
                    "木星": 71492.0, "土星": 60268.0}
PLANET_SF = {"水星": "mercury", "金星": "venus", "火星": "mars barycenter",
             "木星": "jupiter barycenter", "土星": "saturn barycenter"}

# 航海历所列的四颗"航海行星" + 日月
NAV_BODIES = ["太阳", "月亮", "金星", "火星", "木星", "土星"]
BODIES = NAV_BODIES                      # 六分仪页可观测的天体
# 星空页可见的全部天体
SKY_BODIES = ["太阳", "月亮", "水星", "金星", "火星", "木星", "土星"]
BODY_COLOR = {"太阳": "#ffd257", "月亮": "#e8e6df", "水星": "#c9c2b6",
              "金星": "#fff3c4", "火星": "#ff8f63", "木星": "#ffe2ad",
              "土星": "#f0dfa8"}
# 视星等 (最亮时的典型值, 仅用于画点大小)
BODY_MAG = {"水星": -0.2, "金星": -4.1, "火星": 0.7, "木星": -2.2, "土星": 0.5}


def _init_planet_series():
    _PLANET_SERIES.update({
        "水星": (_ME_L, _ME_B, _ME_R),
        "金星": (_V_L, _V_B, _V_R),
        "火星": (_MA_L, _MA_B, _MA_R),
        "木星": (_JU_L, _JU_B, _JU_R),
        "土星": (_SA_L, _SA_B, _SA_R),
    })


def planet_helio(name, jd_tt):
    """行星日心黄道坐标 (当日平黄道分点) —— (L 度, B 度, R AU)。"""
    if not _PLANET_SERIES:
        _init_planet_series()
    L, B, R = _PLANET_SERIES[name]
    tau = (jd_tt - 2451545.0) / 365250.0
    return (norm360(math.degrees(_vsop(L, tau))),
            math.degrees(_vsop(B, tau)), _vsop(R, tau))


def planet_apparent(name, jd_tt, jd_ut):
    """任意大行星的地心视位置 (光行时迭代 + 周年光行差 + 章动)。"""
    ex, ey, ez = _earth_rect(jd_tt)
    R = math.sqrt(ex * ex + ey * ey + ez * ez)
    tau = 0.0
    for _ in range(5):
        Lp, Bp, rp = planet_helio(name, jd_tt - tau)
        px, py, pz = _rect(Lp, Bp, rp)
        dx, dy, dz = px - ex, py - ey, pz - ez
        delta = math.sqrt(dx * dx + dy * dy + dz * dz)
        tau = delta / C_LIGHT_AUD
    rad = PLANET_RADIUS_KM[name]
    sd = math.degrees(math.asin(rad / (delta * AU_KM))) * 60.0
    hp = (8.794 / delta) / 60.0
    cos_i = (rp * rp + delta * delta - R * R) / (2 * rp * delta)
    cos_i = max(-1.0, min(1.0, cos_i))
    phase = math.degrees(math.acos(cos_i))
    illum = (1 + cos_i) / 2.0
    return _vector_to_apparent(name, (dx, dy, dz), jd_tt, jd_ut,
                               sd, hp, phase, illum)


# ===========================================================================
#  黄道坐标 / 月相 / 朔弦望
# ===========================================================================
def true_obliquity(jd_tt):
    T = (jd_tt - 2451545.0) / 36525.0
    dpsi, deps, om = nutation(T)
    return mean_obliquity(T) + deps


def equ_to_ecl(ra, dec, eps):
    """赤道坐标 -> 黄道坐标 (度)。"""
    lam = norm360(math.degrees(math.atan2(
        dsin(ra) * dcos(eps) + dtan(dec) * dsin(eps), dcos(ra))))
    beta = math.degrees(math.asin(dsin(dec) * dcos(eps)
                                  - dcos(dec) * dsin(eps) * dsin(ra)))
    return lam, beta


def elongation_deg(utc):
    """月亮与太阳的视黄经差 (0..360°) —— 0=朔, 90=上弦, 180=望, 270=下弦。"""
    jd_ut = julian_day(utc)
    jd_tt = jd_ut + delta_t_seconds(utc) / 86400.0
    eps = true_obliquity(jd_tt)
    s = EPH.get("太阳", utc)
    m = EPH.get("月亮", utc)
    ls, _ = equ_to_ecl(s.ra, s.dec, eps)
    lm, _ = equ_to_ecl(m.ra, m.dec, eps)
    return norm360(lm - ls)


PHASE_NAMES = [
    (0.0, "朔 (新月)"), (0.5, "娥眉月 (蛾眉月)"), (90.0, "上弦月"),
    (135.0, "盈凸月"), (180.0, "望 (满月)"), (225.0, "亏凸月"),
    (270.0, "下弦月"), (315.0, "残月 (蛾眉月)"),
]


def phase_name(elong):
    e = norm360(elong)
    if e < 6 or e >= 354:
        return "朔 · 新月"
    if e < 84:
        return "娥眉月 (盈)"
    if e < 96:
        return "上弦月"
    if e < 174:
        return "盈凸月"
    if e < 186:
        return "望 · 满月"
    if e < 264:
        return "亏凸月"
    if e < 276:
        return "下弦月"
    return "残月 (亏娥眉月)"


def moon_phase_info(utc):
    """
    月相详情。返回 dict:
      elong  月日视黄经差 (度)
      i      相位角 (度, 0=满月, 180=新月)
      k      被照亮比例 0..1
      chi    明亮边缘的方位角 (自天北极起, 向东为正, 度)
      sep    月日角距 (度)
    """
    s = EPH.get("太阳", utc)
    m = EPH.get("月亮", utc)
    cos_psi = (dsin(s.dec) * dsin(m.dec)
               + dcos(s.dec) * dcos(m.dec) * dcos(s.ra - m.ra))
    cos_psi = max(-1.0, min(1.0, cos_psi))
    psi = math.degrees(math.acos(cos_psi))
    R = s.dist_km
    D = m.dist_km
    i = math.degrees(math.atan2(R * dsin(psi), D - R * dcos(psi)))
    k = (1 + dcos(i)) / 2.0
    chi = norm360(math.degrees(math.atan2(
        dcos(s.dec) * dsin(s.ra - m.ra),
        dsin(s.dec) * dcos(m.dec)
        - dcos(s.dec) * dsin(m.dec) * dcos(s.ra - m.ra))))
    return {"elong": elongation_deg(utc), "i": i, "k": k, "chi": chi,
            "sep": psi, "sun": s, "moon": m}


def parallactic_angle(lha, dec, lat):
    """视差角 q: 天体处"天北极方向"与"天顶方向"的夹角 (度)。"""
    return math.degrees(math.atan2(
        dsin(lha), dtan(lat) * dcos(dec) - dsin(dec) * dcos(lha)))


def find_phase_time(t_start, target_deg, forward=True, max_days=40.0):
    """
    求视黄经差经过 target_deg 的时刻 (UTC)。月亮的相对黄经始终单调增加
    (约 12.19°/日), 故用 0.2 日步长找符号变化再二分。
    """
    step = dt.timedelta(hours=4.8) * (1 if forward else -1)

    def g(t):
        return norm180(elongation_deg(t) - target_deg)

    t0 = t_start
    g0 = g(t0)
    n = int(max_days * 5) + 1
    for _ in range(n):
        t1 = t0 + step
        g1 = g(t1)
        if forward and g0 < 0 <= g1 and (g1 - g0) < 180:
            break
        if (not forward) and g1 < 0 <= g0 and (g0 - g1) < 180:
            break
        t0, g0 = t1, g1
    else:
        return None
    lo, hi = (t0, t1) if forward else (t1, t0)
    for _ in range(50):
        mid = lo + (hi - lo) / 2
        if g(mid) < 0:
            lo = mid
        else:
            hi = mid
    return lo + (hi - lo) / 2


def lunation(utc):
    """
    本朔望月的四相时刻 (UTC)。返回 dict:
      new0 本次朔, first 上弦, full 望, last 下弦, new1 下次朔, length 长度(日)
    """
    new0 = find_phase_time(utc - dt.timedelta(days=31), 0.0, True)
    while new0 is not None:
        nxt = find_phase_time(new0 + dt.timedelta(hours=6), 0.0, True)
        if nxt is None or nxt > utc:
            break
        new0 = nxt
    new1 = find_phase_time(utc, 0.0, True) if new0 else None
    if new0 is None or new1 is None:
        return None
    res = {"new0": new0, "new1": new1}
    for key, tgt in (("first", 90.0), ("full", 180.0), ("last", 270.0)):
        res[key] = find_phase_time(new0 + dt.timedelta(hours=6), tgt, True)
    res["length"] = (new1 - new0).total_seconds() / 86400.0
    return res


CN_DAY = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十",
          "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
          "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十"]


def lunar_day_index(utc, tz, lun=None):
    """
    农历日序 (1 = 初一 = 含朔的那一天)。返回 (日序, 本月总天数, lunation)。
    朔所在的"当地日期"定为初一 —— 与中国农历的定朔规则一致。
    """
    lun = lun or lunation(utc)
    if lun is None:
        return None, None, None
    d0 = (lun["new0"] + dt.timedelta(hours=tz)).date()
    d1 = (lun["new1"] + dt.timedelta(hours=tz)).date()
    dnow = (utc + dt.timedelta(hours=tz)).date()
    return (dnow - d0).days + 1, (d1 - d0).days, lun


# ===========================================================================
#  岁差 (J2000 -> 当日) —— 供可选的星表使用
# ===========================================================================
def precess_j2000(ra, dec, jd_tt):
    T = (jd_tt - 2451545.0) / 36525.0
    z1 = (2306.2181 * T + 0.30188 * T * T + 0.017998 * T ** 3) / 3600.0
    z2 = (2306.2181 * T + 1.09468 * T * T + 0.018203 * T ** 3) / 3600.0
    th = (2004.3109 * T - 0.42665 * T * T - 0.041833 * T ** 3) / 3600.0
    A = dcos(dec) * dsin(ra + z1)
    B = dcos(th) * dcos(dec) * dcos(ra + z1) - dsin(th) * dsin(dec)
    C = dsin(th) * dcos(dec) * dcos(ra + z1) + dcos(th) * dsin(dec)
    C = max(-1.0, min(1.0, C))
    return norm360(math.degrees(math.atan2(A, B)) + z2), math.degrees(math.asin(C))


STAR_FILE_HINT = ("把星表放成同目录下的 stars.csv 即可显示恒星\n"
                  "列名支持: name/名称, ra 或 ra_deg 或 ra_h, dec/dec_deg, mag/星等")


def load_star_catalogue(path):
    """
    读入可选星表 CSV。返回 [(name, ra_j2000_deg, dec_j2000_deg, mag), ...]
    容错处理: 缺列或格式错误的行直接跳过。
    """
    import csv
    stars = []
    try:
        with open(path, "r", encoding="utf-8-sig", newline="") as f:
            sample = f.read(4096)
            f.seek(0)
            try:
                dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
            except Exception:
                dialect = csv.excel
            rd = csv.DictReader(f, dialect=dialect)
            if not rd.fieldnames:
                return []
            cols = {c.strip().lower(): c for c in rd.fieldnames}

            def pick(*names):
                for n in names:
                    if n in cols:
                        return cols[n]
                return None

            c_name = pick("name", "名称", "星名", "star", "id")
            c_ra = pick("ra_deg", "ra", "赤经", "rah", "ra_h")
            c_dec = pick("dec_deg", "dec", "赤纬", "de")
            c_mag = pick("mag", "星等", "vmag", "v")
            if not c_ra or not c_dec:
                return []
            ra_in_hours = c_ra.strip().lower() in ("ra_h", "rah")
            rows = []
            for row in rd:
                try:
                    ra = float(row[c_ra])
                    dec = float(row[c_dec])
                except (TypeError, ValueError):
                    continue
                try:
                    mag = float(row[c_mag]) if c_mag else 4.0
                except (TypeError, ValueError):
                    mag = 4.0
                rows.append((row.get(c_name, "") if c_name else "", ra, dec, mag))
            if rows and not ra_in_hours and max(r[1] for r in rows) <= 24.0:
                ra_in_hours = True          # 全部 <=24, 判定为"时"
            for nm, ra, dec, mag in rows:
                stars.append((nm, norm360(ra * 15.0 if ra_in_hours else ra),
                              dec, mag))
    except Exception:
        return []
    return stars


def gha_aries(utc):
    """白羊宫(春分点)的格林尼治时角 = 格林尼治真恒星时 (度)。"""
    jd_ut = julian_day(utc)
    jd_tt = jd_ut + delta_t_seconds(utc) / 86400.0
    T = (jd_tt - 2451545.0) / 36525.0
    dpsi, deps, om = nutation(T)
    eps = mean_obliquity(T) + deps
    return norm360(gmst_deg(jd_ut) + dpsi * dcos(eps))


def fmt_dm(x, width=3):
    """度分格式 123°45.6′ (航海历风格)。"""
    neg = x < 0
    x = abs(x)
    d = int(x)
    m = (x - d) * 60.0
    if m >= 59.95:
        d += 1
        m = 0.0
    return "%s%*d°%04.1f′" % ("-" if neg else "", width, d, m)


def fmt_dec(x):
    """赤纬格式 N 12°34.5′。"""
    return "%s %s" % ("N" if x >= 0 else "S", fmt_dm(abs(x), 2))


def hourly_v_d(body, utc):
    """
    航海历的 v 与 d: v = GHA 每小时变化超出标称值的部分 (角分/时),
    d = 赤纬每小时变化 (角分/时)。标称值: 日/行星 15°/h, 月 14°19.0′/h。
    """
    p0 = EPH.get(body, utc)
    p1 = EPH.get(body, utc + dt.timedelta(hours=1))
    dgha = norm180(p1.gha - p0.gha) + 360.0 if norm180(p1.gha - p0.gha) < 0 else norm180(p1.gha - p0.gha)
    nominal = 14.0 + 19.0 / 60.0 if body == "月亮" else 15.0
    v = (dgha - nominal) * 60.0
    d = (p1.dec - p0.dec) * 60.0
    return v, d


# ===========================================================================
#  内置亮星 (J2000.0, ICRS)  —— 北极星、南十字与航海常用一等星
#  坐标取自常见星表, 精度约 ±0.5′; 需要完整星表请放 stars.csv
#  (名称, 赤经 h, m, s, 赤纬 sign, °, ′, ″, 视星等)
# ===========================================================================
_STAR_RAW = [
    ("北极星 Polaris",      2, 31, 49.1, +1, 89, 15, 51, 1.98),
    ("北极二 Kochab",      14, 50, 42.3, +1, 74,  9, 20, 2.08),
    ("十字架二 Acrux",     12, 26, 35.9, -1, 63,  5, 57, 0.77),
    ("十字架三 Mimosa",    12, 47, 43.3, -1, 59, 41, 19, 1.25),
    ("十字架一 Gacrux",    12, 31, 10.0, -1, 57,  6, 48, 1.63),
    ("十字架四 Imai",      12, 15,  8.7, -1, 58, 44, 56, 2.79),
    ("十字架五 εCru",      12, 21, 21.6, -1, 60, 24,  4, 3.59),
    ("南门二 Rigil Kent",  14, 39, 36.5, -1, 60, 50,  2, -0.27),
    ("马腹一 Hadar",       14,  3, 49.4, -1, 60, 22, 22, 0.61),
    ("天狼 Sirius",         6, 45,  8.9, -1, 16, 42, 58, -1.46),
    ("老人 Canopus",        6, 23, 57.1, -1, 52, 41, 44, -0.74),
    ("大角 Arcturus",      14, 15, 39.7, +1, 19, 10, 57, -0.05),
    ("织女一 Vega",        18, 36, 56.3, +1, 38, 47,  1, 0.03),
    ("五车二 Capella",      5, 16, 41.4, +1, 45, 59, 53, 0.08),
    ("参宿七 Rigel",        5, 14, 32.3, -1,  8, 12,  6, 0.13),
    ("南河三 Procyon",      7, 39, 18.1, +1,  5, 13, 30, 0.34),
    ("水委一 Achernar",     1, 37, 42.8, -1, 57, 14, 12, 0.46),
    ("参宿四 Betelgeuse",   5, 55, 10.3, +1,  7, 24, 25, 0.50),
    ("河鼓二 Altair",      19, 50, 47.0, +1,  8, 52,  6, 0.77),
    ("毕宿五 Aldebaran",    4, 35, 55.2, +1, 16, 30, 33, 0.85),
    ("角宿一 Spica",       13, 25, 11.6, -1, 11,  9, 41, 0.97),
    ("心宿二 Antares",     16, 29, 24.5, -1, 26, 25, 55, 1.09),
    ("北河三 Pollux",       7, 45, 18.9, +1, 28,  1, 34, 1.14),
    ("北落师门 Fomalhaut", 22, 57, 39.0, -1, 29, 37, 20, 1.16),
    ("天津四 Deneb",       20, 41, 25.9, +1, 45, 16, 49, 1.25),
    ("轩辕十四 Regulus",   10,  8, 22.3, +1, 11, 58,  2, 1.35),
]

BUILTIN_STARS = []          # [(名称, RA°, Dec°, mag)]
for _nm, _h, _m, _s, _sg, _d, _dm, _ds, _mg in _STAR_RAW:
    BUILTIN_STARS.append((_nm,
                          (_h + _m / 60.0 + _s / 3600.0) * 15.0,
                          _sg * (_d + _dm / 60.0 + _ds / 3600.0),
                          _mg))
STAR_BY_NAME = {s[0]: s for s in BUILTIN_STARS}
# 六分仪常用的两颗定纬星
SEXTANT_STARS = ["北极星 Polaris", "十字架二 Acrux", "十字架三 Mimosa",
                 "南门二 Rigil Kent", "天狼 Sirius", "老人 Canopus",
                 "织女一 Vega", "大角 Arcturus"]


def star_apparent(name, jd_tt, jd_ut, ra0=None, dec0=None):
    """恒星视位置: 岁差(J2000→当日) + 章动 + 周年光行差。"""
    if ra0 is None:
        nm, ra0, dec0, mag = STAR_BY_NAME[name]
    ra, dec = precess_j2000(ra0, dec0, jd_tt)
    T = (jd_tt - 2451545.0) / 36525.0
    eps0 = mean_obliquity(T)
    # 赤道(当日平分点) -> 黄道 单位向量
    x = dcos(dec) * dcos(ra)
    y = dcos(dec) * dsin(ra) * dcos(eps0) + dsin(dec) * dsin(eps0)
    z = -dcos(dec) * dsin(ra) * dsin(eps0) + dsin(dec) * dcos(eps0)
    pos = _vector_to_apparent(name, (x, y, z), jd_tt, jd_ut, 0.0, 0.0, 0.0, 1.0)
    pos.kind = "star"
    return pos


def is_star(name):
    return name in STAR_BY_NAME


def lunation_octants(lun):
    """
    本朔望月八个相位 (每 45°) 的时刻。一次扫描 + 二分, 比逐个求根快。
    返回 [t0(朔), t45, t90(上弦), t135, t180(望), t225, t270(下弦), t315]
    """
    if not lun:
        return None
    t0, t1 = lun["new0"], lun["new1"]
    step = dt.timedelta(hours=4.0)
    samples = []
    t = t0
    while t <= t1 + step:
        samples.append((t, elongation_deg(t)))
        t += step
    out = []
    for k in range(8):
        target = k * 45.0
        found = None
        for i in range(len(samples) - 1):
            a = norm180(samples[i][1] - target)
            b = norm180(samples[i + 1][1] - target)
            if a < 0 <= b and (b - a) < 180:
                lo, hi = samples[i][0], samples[i + 1][0]
                for _ in range(40):
                    mid = lo + (hi - lo) / 2
                    if norm180(elongation_deg(mid) - target) < 0:
                        lo = mid
                    else:
                        hi = mid
                found = lo + (hi - lo) / 2
                break
        out.append(found)
    return out


OCTANT_NAMES = ["朔 · 新月", "娥眉月 (盈)", "上弦月", "盈凸月",
                "望 · 满月", "亏凸月", "下弦月", "残月 (亏娥眉)"]


def body_events(body, date_local, lat, lon, tzoff):
    """任意天体的出/中天/落 (当地标准时)。"""
    base = dt.datetime(date_local.year, date_local.month, date_local.day)
    start = base - dt.timedelta(hours=tzoff)
    step = dt.timedelta(minutes=10)
    N = 24 * 6

    def h0_of(p):
        if body == "月亮":
            return 0.7275 * p.hp_arcmin / 60.0 - 0.5667
        if body == "太阳":
            return -0.833
        return -0.5667

    def alt_at(t):
        p = EPH.get(body, t)
        a, _ = altaz_from_hadec(norm360(p.gha + lon), p.dec, lat)
        return a - h0_of(p)

    vals = [(start + step * i, alt_at(start + step * i)) for i in range(N + 1)]

    def refine(ta, tb):
        for _ in range(28):
            tm = ta + (tb - ta) / 2
            if (alt_at(ta) < 0) == (alt_at(tm) < 0):
                ta = tm
            else:
                tb = tm
        return ta + (tb - ta) / 2

    rise = sett = tr = None
    for i in range(N):
        if vals[i][1] < 0 <= vals[i + 1][1]:
            rise = refine(vals[i][0], vals[i + 1][0])
        if vals[i][1] >= 0 > vals[i + 1][1]:
            sett = refine(vals[i][0], vals[i + 1][0])
    prev = None
    for t, _a in vals:
        h = norm180(EPH.get(body, t).gha + lon)
        if prev is not None and prev[1] < 0 <= h and (h - prev[1]) < 180:
            ta, tb = prev[0], t
            for _ in range(28):
                tm = ta + (tb - ta) / 2
                if norm180(EPH.get(body, tm).gha + lon) < 0:
                    ta = tm
                else:
                    tb = tm
            tr = ta + (tb - ta) / 2
        prev = (t, h)

    def loc(t):
        return None if t is None else t + dt.timedelta(hours=tzoff)
    return loc(rise), loc(tr), loc(sett)


def canvas_tooltip(canvas, x, y, lines, font, W, H, fill="#101a24",
                   outline="#c9a227", text_fill="#e8eef4", tag="__tip__"):
    """在 Canvas 上画一个跟随鼠标的提示框。"""
    canvas.delete(tag)
    if not lines:
        return
    pad = 6
    wdt = max(font.measure(t) for t in lines) + pad * 2
    hgt = len(lines) * (font.metrics("linespace") + 2) + pad * 2
    bx = min(max(4, x + 14), W - wdt - 4)
    by = min(max(4, y + 14), H - hgt - 4)
    canvas.create_rectangle(bx, by, bx + wdt, by + hgt, fill=fill,
                            outline=outline, tags=tag)
    for i, t in enumerate(lines):
        canvas.create_text(bx + pad, by + pad + i * (font.metrics("linespace") + 2),
                           text=t, anchor="nw", fill=text_fill, font=font, tags=tag)


# ===========================================================================
#  时间引擎: 默认跟着真实时间走, 可暂停 / 加速 / 跳转
# ===========================================================================
class TimeEngine:
    def __init__(self, speed=1.0):
        self.speed = speed
        self.paused = False
        self._offset = dt.timedelta(0)      # 模拟 UTC = 真实 UTC + offset
        self._frozen = None                 # 暂停时锁定的模拟 UTC
        self._last = None

    # -- 查询 --
    def utc(self):
        if self._frozen is not None:
            return self._frozen
        return utcnow() + self._offset

    def local(self, tz):
        return self.utc() + dt.timedelta(hours=tz)

    # -- 推进 (每帧调用一次) --
    def tick(self):
        now = utcnow()
        if self._last is None:
            self._last = now
            return
        real = now - self._last
        self._last = now
        if self._frozen is None and self.speed != 1.0:
            self._offset += real * (self.speed - 1.0)

    # -- 控制 --
    def set_paused(self, flag):
        if flag and self._frozen is None:
            self._frozen = self.utc()
        elif (not flag) and self._frozen is not None:
            self._offset = self._frozen - utcnow()
            self._frozen = None
        self.paused = flag

    def toggle_pause(self):
        self.set_paused(not self.paused)
        return self.paused

    def jump(self, delta):
        if self._frozen is not None:
            self._frozen += delta
        else:
            self._offset += delta

    def set_utc(self, t):
        if self._frozen is not None:
            self._frozen = t
        else:
            self._offset = t - utcnow()

    def set_local(self, t, tz):
        self.set_utc(t - dt.timedelta(hours=tz))

    def now(self):
        """回到真实当前时刻。"""
        self._offset = dt.timedelta(0)
        if self._frozen is not None:
            self._frozen = utcnow()

    def is_realtime(self):
        return (self._frozen is None
                and abs(self._offset.total_seconds()) < 1.5 and self.speed == 1.0)


SPEEDS = [("1× 实时", 1.0), ("60×", 60.0), ("300×", 300.0), ("600×", 600.0),
          ("1800×", 1800.0), ("3600×", 3600.0), ("1日/秒", 86400.0)]


# ===========================================================================
#  简易三维引擎 (球面相机 + 透视投影 + 画家算法)
#  世界坐标 = 当地地平系 ENU:  x=东  y=北  z=天顶
# ===========================================================================
class Camera3D:
    EL_MIN, EL_MAX = 2.0, 88.0            # 仰角限制: 不能转到晷面底下

    def __init__(self, az=205.0, el=26.0, dist=5.2, fov=42.0, target=(0, 0, 0.25)):
        self.az = az                      # 相机所在的方位 (自北顺时针)
        self.el = el                      # 相机的仰角
        self.dist = dist
        self.fov = fov
        self.target = list(target)

    def clone_from(self, other):
        self.az, self.el, self.dist, self.fov = other.az, other.el, other.dist, other.fov
        self.target = list(other.target)

    def orbit(self, d_az, d_el):
        self.az = norm360(self.az + d_az)
        self.el = max(self.EL_MIN, min(self.EL_MAX, self.el + d_el))

    FOV_MIN, FOV_MAX = 1.2, 70.0

    def zoom(self, factor):
        """缩放 = 改变视场角(长焦), 可以无限放大又不会穿进模型。"""
        self.fov = max(self.FOV_MIN, min(self.FOV_MAX, self.fov * factor))

    def dolly(self, factor):
        self.dist = max(0.6, min(40.0, self.dist * factor))

    def mag(self):
        """相对 38° 标准视场的放大倍数。"""
        return 38.0 / self.fov

    def eye(self):
        t = self.target
        return (t[0] + self.dist * dsin(self.az) * dcos(self.el),
                t[1] + self.dist * dcos(self.az) * dcos(self.el),
                t[2] + self.dist * dsin(self.el))

    def basis(self):
        e = self.eye()
        t = self.target
        f = (t[0] - e[0], t[1] - e[1], t[2] - e[2])
        n = math.sqrt(f[0] ** 2 + f[1] ** 2 + f[2] ** 2) or 1.0
        f = (f[0] / n, f[1] / n, f[2] / n)
        r = _cross(f, (0.0, 0.0, 1.0))
        rn = math.sqrt(_dot(r, r)) or 1.0
        r = (r[0] / rn, r[1] / rn, r[2] / rn)
        u = _cross(r, f)
        return e, r, u, f

    def look_dir(self):
        """相机的视线方向 (方位角, 俯仰角) —— 显示给用户看的"实际视角"。"""
        e, r, u, f = self.basis()
        alt = math.degrees(math.asin(max(-1.0, min(1.0, f[2]))))
        az = norm360(math.degrees(math.atan2(f[0], f[1])))
        return az, alt


class Painter3D:
    """把三维图元按深度排序后画到 Canvas 上。"""

    def __init__(self, canvas, cam, W, H):
        self.c = canvas
        self.cam = cam
        self.W, self.H = W, H
        self.items = []
        self._avoid = []               # 屏幕上要让开的框 (标注 dodge 时不许压)
        e, r, u, f = cam.basis()
        self.eye_p, self.rv, self.uv, self.fv = e, r, u, f
        self.k = (H / 2.0) / math.tan(cam.fov / 2.0 * D2R)

    # -- 投影 --
    def project(self, p):
        v = (p[0] - self.eye_p[0], p[1] - self.eye_p[1], p[2] - self.eye_p[2])
        zc = _dot(v, self.fv)
        if zc <= 0.02:
            return None
        return (self.W / 2.0 + _dot(v, self.rv) / zc * self.k,
                self.H / 2.0 - _dot(v, self.uv) / zc * self.k, zc)

    def depth(self, p):
        v = (p[0] - self.eye_p[0], p[1] - self.eye_p[1], p[2] - self.eye_p[2])
        return _dot(v, self.fv)

    def _clip_seg(self, p1, p2):
        """近平面裁剪, 返回可见线段或 None。"""
        z1, z2 = self.depth(p1), self.depth(p2)
        near = 0.05
        if z1 <= near and z2 <= near:
            return None
        if z1 < near:
            t = (near - z1) / (z2 - z1)
            p1 = tuple(p1[i] + (p2[i] - p1[i]) * t for i in range(3))
        elif z2 < near:
            t = (near - z2) / (z1 - z2)
            p2 = tuple(p2[i] + (p1[i] - p2[i]) * t for i in range(3))
        return p1, p2

    # -- 图元 --
    def poly(self, pts, bias=0.0, **kw):
        scr = []
        zs = []
        for p in pts:
            q = self.project(p)
            if q is None:
                return
            scr += [q[0], q[1]]
            zs.append(q[2])
        self.items.append((sum(zs) / len(zs) + bias, len(self.items), "poly", scr, kw))

    def line(self, p1, p2, bias=0.0, **kw):
        seg = self._clip_seg(p1, p2)
        if not seg:
            return
        a = self.project(seg[0])
        b = self.project(seg[1])
        if a is None or b is None:
            return
        self.items.append(((a[2] + b[2]) / 2.0 + bias, len(self.items), "line",
                           [a[0], a[1], b[0], b[1]], kw))

    def polyline(self, pts, bias=0.0, **kw):
        for i in range(len(pts) - 1):
            self.line(pts[i], pts[i + 1], bias, **kw)

    def dot(self, p, r_px, bias=0.0, **kw):
        q = self.project(p)
        if q is None:
            return
        self.items.append((q[2] + bias, len(self.items), "oval",
                           [q[0] - r_px, q[1] - r_px, q[0] + r_px, q[1] + r_px], kw))

    def text(self, p, txt, bias=0.0, dodge=False, **kw):
        """dodge=True: 画之前在屏幕上挪开, 不压别的字和 avoid() 登记的框。"""
        q = self.project(p)
        if q is None:
            return
        kw = dict(kw)
        kw["text"] = txt
        if dodge:
            kw["_dodge"] = True
        self.items.append((q[2] + bias, len(self.items), "text", [q[0], q[1]], kw))

    def avoid_pts(self, pts, pad=3.0):
        """把一组三维点投影后的外接框登记为「标注不许压」。"""
        qs = [q for q in (self.project(p) for p in pts) if q is not None]
        if qs:
            xs = [q[0] for q in qs]
            ys = [q[1] for q in qs]
            self._avoid.append((min(xs) - pad, min(ys) - pad, max(xs) + pad, max(ys) + pad))

    def _dodge_labels(self):
        """标了 dodge 的字: 若压到别的字或登记的框, 就上下 (再左右) 挪到最近的空处。"""
        fixed = list(self._avoid)
        movers = []
        for it in self.items:
            if it[2] != "text":
                continue
            kw = it[4]
            f = kw.get("font")
            if f is None or not hasattr(f, "measure"):
                continue
            w, h = text_size(f, kw["text"])
            if kw.get("_dodge"):
                movers.append((it, w, h))
            else:
                fixed.append(anchor_box(it[3][0], it[3][1], kw.get("anchor", "center"), w, h))
        for it, w, h in movers:
            x, y = it[3]
            anc = it[4].get("anchor", "center")
            best = None
            k = 0
            for dy in (0, 1, -1, 2, -2, 3, -3):
                for dx in (0, 1, -1):
                    bx, by = x + dx * (w * 0.5 + 8), y + dy * (h + 2)
                    b = anchor_box(bx, by, anc, w, h)
                    bad = sum(box_ov(b, o) for o in fixed)
                    if b[0] < 0 or b[2] > self.W or b[1] < 0 or b[3] > self.H:
                        bad += w * h
                    sc = bad * 1000.0 + k
                    k += 1
                    if best is None or sc < best[0]:
                        best = (sc, bx, by, b)
                if best[0] < 1000.0:
                    break
            _sc, bx, by, b = best
            it[3][0], it[3][1] = bx, by
            fixed.append(b)

    # -- 输出 --
    def flush(self):
        self.items.sort(key=lambda it: (-it[0], it[1]))
        if any(it[2] == "text" and it[4].get("_dodge") for it in self.items):
            self._dodge_labels()
            for it in self.items:
                if it[2] == "text":
                    it[4].pop("_dodge", None)
        c = self.c
        for _, _, kind, coords, kw in self.items:
            if kind == "poly":
                c.create_polygon(coords, **kw)
            elif kind == "line":
                c.create_line(coords, **kw)
            elif kind == "oval":
                c.create_oval(coords, **kw)
            elif kind == "text":
                c.create_text(coords[0], coords[1], **kw)
        self.items = []


class OrbitMouse:
    """给 Canvas 装上"按住拖动转视角, 松开固定"的交互。"""

    def __init__(self, canvas, cam, on_change=None, sensitivity=0.42):
        self.cam = cam
        self.on_change = on_change
        self.sens = sensitivity
        self.dragging = False
        self._last = None
        canvas.bind("<ButtonPress-1>", self._press)
        canvas.bind("<B1-Motion>", self._drag)
        canvas.bind("<ButtonRelease-1>", self._release)
        canvas.bind("<MouseWheel>", self._wheel)
        canvas.bind("<Button-4>", lambda e: self._zoom(1 / 1.12))
        canvas.bind("<Button-5>", lambda e: self._zoom(1.12))
        canvas.bind("<ButtonPress-3>", self._press3)
        canvas.bind("<B3-Motion>", self._pan)
        canvas.bind("<ButtonRelease-3>", self._release)
        self.canvas = canvas
        self.on_pan = None
        self.on_click = None
        self._press_xy = None
        self._moved = 0.0

    def _press(self, e):
        self.dragging = True
        self._last = (e.x, e.y)
        self._press_xy = (e.x, e.y)
        self._moved = 0.0

    def _drag(self, e):
        if not self.dragging or self._last is None:
            return
        dx = e.x - self._last[0]
        dy = e.y - self._last[1]
        self._moved = getattr(self, "_moved", 0.0) + abs(dx) + abs(dy)
        self._last = (e.x, e.y)
        self.cam.orbit(-dx * self.sens, dy * self.sens)
        if self.on_change:
            self.on_change()

    def _release(self, e):
        self.dragging = False
        self._last = None
        if getattr(self, "_moved", 99) < 4 and getattr(self, "on_click", None):
            self.on_click(e.x, e.y)
        if self.on_change:
            self.on_change()

    def _press3(self, e):
        self.dragging = True
        self._last = (e.x, e.y)

    def _pan(self, e):
        """右键拖动: 平移相机注视点 (放大后用来看晷面的不同部位)。"""
        if self._last is None:
            return
        dx = e.x - self._last[0]
        dy = e.y - self._last[1]
        self._last = (e.x, e.y)
        eye, r, u, f = self.cam.basis()
        H = max(self.canvas.winfo_height(), 100)
        k = 2.0 * self.cam.dist * math.tan(self.cam.fov / 2.0 * D2R) / H
        for i in range(3):
            self.cam.target[i] -= (r[i] * dx - u[i] * dy) * k
        if self.on_pan:
            self.on_pan()
        if self.on_change:
            self.on_change()

    def _wheel(self, e):
        self._zoom(1 / 1.12 if e.delta > 0 else 1.12)

    def _zoom(self, f):
        self.cam.zoom(f)
        if self.on_change:
            self.on_change()


# ===========================================================================
#  时辰 / 24 小时 刻度
# ===========================================================================
SHICHEN = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
SHICHEN_FULL = ["子时 23–01", "丑时 01–03", "寅时 03–05", "卯时 05–07",
                "辰时 07–09", "巳时 09–11", "午时 11–13", "未时 13–15",
                "申时 15–17", "酉时 17–19", "戌时 19–21", "亥时 21–23"]


def shichen_of_hour(h):
    """真太阳时(小时, 0-24) -> (序号 0=子, 名称)。子时以 24:00/0:00 为中心。"""
    idx = int(math.floor((h + 1.0) % 24.0 / 2.0)) % 12
    return idx, SHICHEN[idx]


def dial_marks(system, show_ke=True, sc_mode="midculm"):
    """
    晷面刻度 (真太阳时)。返回 [(真太阳时小时, 类型, 标签)]:
      'major'  粗线   'hour' 细线   'ke' 刻线(15分)   'label' 只写字不画线
    sc_mode: 时辰起算方式
      'midculm' 中天起午 —— 太阳中天(真太阳时 12:00)为午时之始, 底天(0:00)为子时之始
      'trad'    传统     —— 午时含中天 (11-13 时), 子时跨半夜 (23-1 时)
    """
    marks = []
    if system == "12sc":
        if sc_mode == "trad":
            for i in range(12):
                marks.append((((i * 2 - 1) % 24), "major", ""))   # 分界在奇数时
                marks.append((((i * 2) % 24), "label", SHICHEN[i]))
        else:
            for i in range(12):
                marks.append(((i * 2) % 24, "major", ""))         # 分界在偶数时
                marks.append(((i * 2 + 1) % 24, "label", SHICHEN[i]))
    else:
        for h in range(24):
            marks.append((h, "major" if h % 6 == 0 else "hour",
                          "%d" % (h if h else 24)))
    if show_ke:
        for q in range(96):
            hh = q * 0.25
            if abs(hh - round(hh)) < 1e-9:
                continue
            marks.append((hh, "ke", ""))
    return marks


def shichen_of(lat_hours, sc_mode="midculm"):
    """真太阳时(小时) -> (时辰序号 0=子, 名称, 该时辰内第几刻 1..8)"""
    h = lat_hours % 24.0
    if sc_mode == "trad":
        idx = int(math.floor((h + 1.0) % 24.0 / 2.0)) % 12
        start = (idx * 2 - 1) % 24
    else:
        idx = int(math.floor(h / 2.0)) % 12
        start = idx * 2
    into = (h - start) % 24.0
    ke = int(into * 4) + 1
    return idx, SHICHEN[idx], min(8, max(1, ke))


def shichen_table(sc_mode="midculm"):
    """返回 [(名称, 起始真太阳时小时, 结束小时)]"""
    out = []
    for i in range(12):
        start = (i * 2 - 1) % 24 if sc_mode == "trad" else (i * 2) % 24
        out.append((SHICHEN[i] + "时", start, (start + 2) % 24))
    return out


def hour_marks(system):                        # 向下兼容
    return [(h, lbl, kind == "major")
            for h, kind, lbl in dial_marks(system, False) if kind != "ke"]


# ===========================================================================
#  可滚动侧栏 (窗口较小时不至于挤掉下方内容)
# ===========================================================================
class VScrollFrame(ttk.Frame):
    def __init__(self, master, width=430, bg="#161c22"):
        super().__init__(master)
        if LANG == "en":                  # 英文字比中文长, 右栏放宽 25%
            width = int(width * 1.25)
        self.canvas = tk.Canvas(self, width=width, highlightthickness=0, bg=bg)
        self.vs = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.body = ttk.Frame(self.canvas)
        self.body.bind("<Configure>", self._on_body)
        self._win = self.canvas.create_window((0, 0), window=self.body, anchor="nw")
        self._fit_job = None
        self._fit_w = None
        self.canvas.bind("<Configure>", self._on_canvas)
        self.canvas.configure(yscrollcommand=self.vs.set)
        self.canvas.pack(side="left", fill="both", expand=True)
        self.vs.pack(side="right", fill="y")
        for w in (self.canvas, self.body):
            w.bind("<MouseWheel>", self._wheel)
            w.bind("<Button-4>", lambda e: self.canvas.yview_scroll(-2, "units"))
            w.bind("<Button-5>", lambda e: self.canvas.yview_scroll(2, "units"))

    def _on_body(self, _e=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _wheel(self, e):
        self.canvas.yview_scroll(-2 if e.delta > 0 else 2, "units")

    # ---- 右栏装不下的就地重排 (英文字长; 中文原本装得下的一概不动) ----
    def _on_canvas(self, e):
        self.canvas.itemconfigure(self._win, width=e.width)
        if e.width != self._fit_w:
            self._fit_w = e.width
            if self._fit_job is not None:
                try:
                    self.after_cancel(self._fit_job)
                except Exception:
                    pass
            self._fit_job = self.after(60, self.fit)

    def fit(self):
        """
        让右栏里的控件都落在栏宽之内:
          · 横排一行 (pack 到左/右) 摆不下 → 折成几行
          · 同一种按钮 / 勾选框排成的网格摆不下 → 少排几列
          · 单个勾选框、单选钮太长 → 字折行
          · 文字标签一律设折行宽度 (= 到栏右缘的距离); 原本放得下的不受影响
        """
        self._fit_job = None
        try:
            self.update_idletasks()
            bw = self.body.winfo_width()
        except Exception:
            return
        if bw < 60 or not self.body.winfo_ismapped():
            return
        right = self.body.winfo_rootx() + bw - 6
        for _ in range(4):
            if not self._fit_walk(self.body, right):
                break
            self.update_idletasks()

    def _fit_walk(self, w, right):
        changed = False
        for ch in w.winfo_children():
            try:
                if not ch.winfo_ismapped():
                    continue
                changed = self._fit_one(ch, right) or changed
                changed = self._fit_walk(ch, right) or changed
            except Exception:
                continue
        return changed

    @staticmethod
    def _int(v):
        try:
            return int(float(str(v) or 0))
        except Exception:
            return 0

    def _fit_one(self, ch, right):
        cls = ch.winfo_class()
        x = ch.winfo_rootx()
        room = right - x
        if cls in ("TLabel", "Label"):
            t = ch.cget("text")
            if not isinstance(t, str) or room < 40:   # 空标签也设, 日后填进长字就会折行
                return False
            wl = self._int(ch.cget("wraplength"))
            if wl == 0 or wl > room:
                ch.configure(wraplength=max(40, room))
                return ch.winfo_reqwidth() > room + 2 or wl != 0
            return False
        over = ch.winfo_reqwidth() > room + 1
        if not over:
            return False
        if cls in ("TCheckbutton", "TRadiobutton") and room >= 60:
            base = "TCheckbutton" if cls == "TCheckbutton" else "TRadiobutton"
            sty = "W%d.%s" % (room - 26, base)
            try:
                ttk.Style().configure(sty, wraplength=room - 26)
                ch.configure(style=sty)
                return True
            except Exception:
                return False
        if cls in ("TFrame", "Frame"):
            return self._flow(ch, room) or self._regrid(ch, room)
        return False

    @staticmethod
    def _padx(v):
        if isinstance(v, (tuple, list)):
            return sum(VScrollFrame._int(a) for a in v)
        parts = str(v).split()
        return sum(VScrollFrame._int(a) for a in parts) * (1 if len(parts) > 1 else 2)

    def _flow(self, fr, room):
        """一排横着 pack 的控件摆不下: 折成几行 (控件还是原来那些, 只是改 pack 到行框里)。"""
        slaves = fr.pack_slaves()
        if len(slaves) < 2:
            return False
        infos = [s.pack_info() for s in slaves]
        if any(str(i.get("side")) not in ("left", "right") for i in infos):
            return False
        order = ([(s, i) for s, i in zip(slaves, infos) if str(i["side"]) == "left"]
                 + [(s, i) for s, i in zip(slaves, infos) if str(i["side"]) == "right"])
        rows, cur, used = [], None, 0
        for s, i in order:
            wpx = s.winfo_reqwidth() + self._padx(i.get("padx", 0))
            if cur is None or (used > 0 and used + wpx > room):
                cur = ttk.Frame(fr)
                rows.append(cur)
                used = 0
            used += wpx
            opts = {k: i[k] for k in ("side", "padx", "pady", "ipadx", "ipady",
                                      "fill", "expand", "anchor") if k in i}
            s.pack_forget()
            s.pack(in_=cur, **opts)
            s.lift(cur)                    # 行框后建, 要把控件提到它上面才看得见
        if len(rows) < 2:
            return False
        for r in rows:
            r.pack(side="top", fill="x", anchor="w")
        return True

    @staticmethod
    def refit(widget):
        """控件是事后才加进右栏的 (如日食的接触时刻按钮): 找到所在的右栏, 再排一次。"""
        w = widget
        while w is not None and not isinstance(w, VScrollFrame):
            w = getattr(w, "master", None)
        if w is not None:
            w.after_idle(w.fit)

    def _regrid(self, fr, room):
        """同一种按钮 / 勾选框排成的网格摆不下: 按原来的阅读顺序少排几列。"""
        slaves = fr.grid_slaves()
        if len(slaves) < 3:
            return False
        infos = [s.grid_info() for s in slaves]
        if any(self._int(i.get("columnspan", 1)) != 1 or self._int(i.get("rowspan", 1)) != 1
               for i in infos):
            return False
        kinds = set(s.winfo_class() for s in slaves)
        if len(kinds) != 1 or not kinds <= {"TCheckbutton", "TButton", "TRadiobutton"}:
            return False
        order = sorted(zip(slaves, infos),
                       key=lambda t: (self._int(t[1]["row"]), self._int(t[1]["column"])))
        ncol_old = max(self._int(i["column"]) for i in infos) + 1
        cw = max(s.winfo_reqwidth() + self._padx(i.get("padx", 0)) for s, i in order)
        ncol = max(1, int(room // max(1, cw)))
        if ncol >= ncol_old:
            return False
        for k, (s, i) in enumerate(order):
            s.grid_configure(row=k // ncol, column=k % ncol)
        return True


# ===========================================================================
#  日晷几何
# ===========================================================================
def _enu_from_altaz(alt, az):
    """地平坐标 -> ENU 单位向量 (E, N, U)。"""
    return (dcos(alt) * dsin(az), dcos(alt) * dcos(az), dsin(alt))


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0])


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def polar_axis(lat):
    """晷针(高纬度侧天极)方向的 ENU 单位向量。"""
    v = (0.0, dcos(lat), dsin(lat))          # 指向北天极
    if lat < 0:
        v = (-v[0], -v[1], -v[2])            # 南半球指向南天极
    return v


def style_shadow_on_plane(lat, H, plane_normal, right_vec, up_vec):
    """
    晷针(极轴)在任意晷面上的影线方向。
    H 为时角(度, 西为正)。返回晷面内的单位向量 (x_right, y_up);
    若太阳照不到该面或退化则返回 None。
    """
    alt, az = altaz_from_hadec(H, 0.0, lat)      # 天赤道上的点即可定义时线
    s = _enu_from_altaz(alt, az)
    g = polar_axis(lat)
    n = _cross(g, s)                              # 影面法线
    d = _cross(n, plane_normal)                   # 影面 ∩ 晷面
    mag = math.sqrt(_dot(d, d))
    if mag < 1e-9:
        return None
    d = (d[0] / mag, d[1] / mag, d[2] / mag)
    # 影子背向太阳: 取与太阳在晷面内投影相反的方向
    sp = tuple(s[i] - _dot(s, plane_normal) * plane_normal[i] for i in range(3))
    if _dot(d, sp) > 0:
        d = (-d[0], -d[1], -d[2])
    return (_dot(d, right_vec), _dot(d, up_vec))


def nodus_shadow_horizontal(lat, alt, az, nodus_len):
    """
    晷针上距原点 nodus_len 处的珠(nodus)在水平晷面上的投影 (E, N)。
    alt/az 为太阳位置; 太阳在地平以下返回 None。
    """
    if alt <= 0.1:
        return None
    g = polar_axis(lat)
    P = (g[0] * nodus_len, g[1] * nodus_len, g[2] * nodus_len)
    s = _enu_from_altaz(alt, az)
    if s[2] <= 1e-6:
        return None
    t = P[2] / s[2]
    return (P[0] - s[0] * t, P[1] - s[1] * t)


# ---------------------------------------------------------------------------
#  太阳时刻 (日出/中天/日落)
# ---------------------------------------------------------------------------
def sun_hour_limit(lat, dec):
    """当日太阳可见的最大时角 (度): 极昼返回 180, 极夜返回 0。"""
    denom = dcos(lat) * dcos(dec)
    if abs(denom) < 1e-9:
        return 180.0
    x = (dsin(-0.833) - dsin(lat) * dsin(dec)) / denom
    if x <= -1.0:
        return 180.0
    if x >= 1.0:
        return 0.0
    return math.degrees(math.acos(x))


def sun_alt_at(utc, lat, lon):
    p = EPH.get("太阳", utc)
    lha = norm360(p.gha + lon)
    alt, az = altaz_from_hadec(lha, p.dec, lat)
    return alt


def solar_events(date_local, lat, lon, tzoff):
    """
    求某地方日期的日出/中天/日落 (返回本地标准时 datetime, 可能为 None)。
    以太阳中心视高度 -0.833° 为地平判据。
    """
    base = dt.datetime(date_local.year, date_local.month, date_local.day)
    start_utc = base - dt.timedelta(hours=tzoff)
    N = 24 * 6                     # 10 分钟步长
    step = dt.timedelta(minutes=10)
    alts = []
    for i in range(N + 1):
        t = start_utc + step * i
        alts.append((t, sun_alt_at(t, lat, lon)))

    def refine(t0, t1, target):
        for _ in range(40):
            tm = t0 + (t1 - t0) / 2
            a = sun_alt_at(tm, lat, lon) - target
            a0 = sun_alt_at(t0, lat, lon) - target
            if (a0 < 0) == (a < 0):
                t0 = tm
            else:
                t1 = tm
        return t0 + (t1 - t0) / 2

    rise = sett = None
    tgt = -0.833
    for i in range(N):
        a0, a1 = alts[i][1], alts[i + 1][1]
        if a0 < tgt <= a1:
            rise = refine(alts[i][0], alts[i + 1][0], tgt)
        if a0 >= tgt > a1:
            sett = refine(alts[i][0], alts[i + 1][0], tgt)
    # 中天: 时角过 0
    noon = None
    prev = None
    for i in range(N + 1):
        t = start_utc + step * i
        p = EPH.get("太阳", t)
        h = norm180(p.gha + lon)
        if prev is not None and prev[1] < 0 <= h and (h - prev[1]) < 180:
            t0, t1 = prev[0], t
            for _ in range(40):
                tm = t0 + (t1 - t0) / 2
                hm = norm180(EPH.get("太阳", tm).gha + lon)
                if hm < 0:
                    t0 = tm
                else:
                    t1 = tm
            noon = t0 + (t1 - t0) / 2
        prev = (t, h)

    def to_local(t):
        return None if t is None else t + dt.timedelta(hours=tzoff)

    polar = None
    if rise is None and sett is None:
        polar = "极昼" if max(a for _, a in alts) > tgt else "极夜"
    return to_local(rise), to_local(noon), to_local(sett), polar


def fmt_hm(t):
    return "—" if t is None else t.strftime("%H:%M:%S")


def deg_dm(x, pos="N", neg="S"):
    """十进制度 -> 度分格式, 带方位字母。"""
    h = pos if x >= 0 else neg
    x = abs(x)
    d = int(x)
    m = (x - d) * 60.0
    return "%d°%05.2f′%s" % (d, m, h)


def hm_from_hours(h):
    h = h % 24.0
    hh = int(h)
    mm = (h - hh) * 60
    mi = int(mm)
    ss = (mm - mi) * 60
    return "%02d:%02d:%05.2f" % (hh, mi, ss)



# ---------------------------------------------------------------------------
#  三维晷面几何
# ---------------------------------------------------------------------------
LAY_SHADOW = -1.2       # 与晷面共面的图元: 用较大的偏置压过晷面本身
LAY_LINE = -1.5
LAY_GNOMON = -3.0


def dial_geom3d(kind, lat):
    """
    返回某种晷面的三维定义 (世界坐标 = 地平系 ENU, 单位任意):
      center 晷面中心, n 晷面外法线, r/u 晷面内的右/上基矢,
      shape  'disc'/'rect', size 半径或 (半宽, 半高),
      root   晷针根部, gdir 晷针方向, glen 晷针长度, tri 是否三角形晷针
    """
    g = polar_axis(lat)
    if kind.startswith("水平"):
        return dict(tag="h", center=(0.0, 0.0, 0.03), n=(0.0, 0.0, 1.0),
                    r=(1.0, 0.0, 0.0), u=(0.0, 1.0, 0.0), shape="disc",
                    size=1.05, root=(0.0, 0.0, 0.03), gdir=g, glen=0.9,
                    tri=True, target_z=0.05)
    if kind.startswith("赤道"):
        s0 = (0.0, -dsin(lat), dcos(lat))          # 正午时太阳在盘内的方向
        n = g
        u = s0
        r = _cross(s0, g)                          # = 西
        return dict(tag="e", center=(0.0, 0.0, 0.85), n=n, r=r, u=u,
                    shape="disc", size=0.95, root=(0.0, 0.0, 0.85),
                    gdir=g, glen=0.55, tri=False, target_z=0.85)
    # 垂直晷朝向赤道: 北半球墙面朝南, 南半球墙面朝北 (朝南的墙在南半球中午
    # 晒不到太阳)。晷针平行地轴, 自墙面伸出指向「低于地平的那个天极」。
    #   r = 站在墙前、面对墙时的「右」: 北半球面朝北看 → 东; 南半球面朝南看 → 西
    if lat >= 0:
        n, r = (0.0, -1.0, 0.0), (1.0, 0.0, 0.0)
    else:
        n, r = (0.0, 1.0, 0.0), (-1.0, 0.0, 0.0)
    return dict(tag="v", center=(0.0, 0.0, 0.95), n=n,
                r=r, u=(0.0, 0.0, 1.0), shape="rect",
                size=(1.15, 0.95), root=(0.0, 0.0, 1.82),
                gdir=(-g[0], -g[1], -g[2]), glen=0.85, tri=False,
                target_z=1.30)


def style_tip_on_lit_side(geo, sn):
    """
    受照那一面上的晷针端点。sn = 太阳方向 · 晷面外法线。
    赤道晷的极轴贯穿盘面, 两面各一段等长; 水平/垂直晷只有一面有针,
    阳光照在没有针的那一面时返回 None (此刻晷面无影)。
    """
    root, gd, glen, ctr, n = (geo["root"], geo["gdir"], geo["glen"],
                              geo["center"], geo["n"])
    tip = tuple(root[i] + gd[i] * glen for i in range(3))
    h = _dot((tip[0] - ctr[0], tip[1] - ctr[1], tip[2] - ctr[2]), n)
    if h * sn > 0:
        return tip
    if geo["tag"] == "e":
        return tuple(root[i] - gd[i] * glen for i in range(3))
    return None


def plate_ray_len(geo, ox, oy, dx, dy):
    """晷面内从 (ox,oy) 沿 (dx,dy) 到边界的长度。"""
    if geo["shape"] == "disc":
        R = geo["size"]
        b = ox * dx + oy * dy
        cc = ox * ox + oy * oy - R * R
        disc = b * b - cc
        if disc < 0:
            return 0.0
        return max(0.0, -b + math.sqrt(disc))
    hw, hh = geo["size"]
    t = 1e9
    if dx > 1e-9:
        t = min(t, (hw - ox) / dx)
    elif dx < -1e-9:
        t = min(t, (-hw - ox) / dx)
    if dy > 1e-9:
        t = min(t, (hh - oy) / dy)
    elif dy < -1e-9:
        t = min(t, (-hh - oy) / dy)
    return max(0.0, t)



MARK_COLOR = {
    "solar": {"major": "#a8cde8", "hour": "#6f9ec0", "ke": "#3f6480",
              "label": "#9fc0da", "text": "#9fc0da"},
    "clock": {"major": "#f0a24a", "hour": "#c9803c", "ke": "#7a5228",
              "label": "#f0b877", "text": "#f0b877"},
}
MARK_WIDTH = {"major": 2, "hour": 1, "ke": 1, "label": 0}
MARK_FRAC = {"major": 1.0, "hour": 1.0, "ke": 0.55, "label": 0.0}


def eq2d_sign(dec):
    """
    赤道晷平面图的左右手性: 正对受照面看、正午影线朝下时,
    照北面 (δ≥0) 上午影在右 (+1), 照南面上午影在左 (−1)。
    画面位置 = (cx − R·sin(sign·H), cy + R·cos(sign·H))。
    """
    return 1.0 if dec >= 0 else -1.0


def face_name(nv):
    """由晷面外法线说出是哪一面: 北面/南面 + 上面/下面 (水平分量太小就只说上下)。"""
    parts = []
    if abs(nv[1]) > 0.2:
        parts.append("北面" if nv[1] > 0 else "南面")
    if abs(nv[2]) > 0.2:
        parts.append("上面" if nv[2] > 0 else "下面")
    return "/".join(parts) if parts else ("东面" if nv[0] > 0 else "西面")


def vertical_dial_name(lat):
    """垂直晷按半球的名字: 北半球朝南, 南半球朝北 (都是朝向赤道)。"""
    return "垂直朝南晷" if lat >= 0 else "垂直朝北晷"


def recommend_dial(lat):
    """按纬度推荐晷面 (名称前缀, 理由)。"""
    a = abs(lat)
    if a < 20:
        return "赤道晷", (_T("低纬度 |φ|=%.1f°: 水平晷的时线挤成一束几乎读不出, "
                        "赤道晷每小时正好 15° 均匀") % a)
    if a > 66:
        return "赤道晷", (_T("极区 |φ|=%.1f°: 太阳可整日不落, 赤道晷绕一圈都均匀") % a)
    if a < 55:
        return "水平晷", (_T("中纬度 |φ|=%.1f°: 水平晷时线张得开, 也最常见") % a)
    return "垂直朝南晷", (_T("高纬度 |φ|=%.1f°: 太阳终日偏低, %s面受光角度好")
                       % (a, _en("垂直朝南", "a vertical south-facing") if lat >= 0
                          else _en("垂直朝北 (南半球)",
                                   "a vertical north-facing (southern hemisphere)")))


def dial_metrics(kind, lat, alt, az, r_cm):
    """
    晷面与晷针的实际尺寸 (厘米) 及此刻影长。
    返回 dict: plate_r, style_len, tip_height, base_len, shadow_len, nodus_shadow
    """
    geo = dial_geom3d(kind, lat)
    size = geo["size"] if geo["shape"] == "disc" else geo["size"][0]
    k = float(r_cm) / max(1e-6, size)          # 模型单位 -> 厘米
    ctr, n, root, gd, glen = (geo["center"], geo["n"], geo["root"],
                              geo["gdir"], geo["glen"])
    tip = tuple(root[i] + gd[i] * glen for i in range(3))
    h = _dot((tip[0] - ctr[0], tip[1] - ctr[1], tip[2] - ctr[2]), n)
    proj = tuple((tip[i] - ctr[i]) - n[i] * h for i in range(3))
    base = math.sqrt(_dot(proj, proj))
    out = {"plate_r": float(r_cm), "style_len": glen * k,
           "tip_height": abs(h) * k, "base_len": base * k,
           "shadow_len": None, "nodus_shadow": None,
           "kind": geo["tag"], "style_angle": 90.0 - abs(lat)}
    s = _enu_from_altaz(alt, az)
    sn = _dot(s, n)
    tip_lit = style_tip_on_lit_side(geo, sn) if abs(sn) > 1e-4 else None
    if alt > 0 and tip_lit is not None:
        t = _dot((tip_lit[0] - ctr[0], tip_lit[1] - ctr[1],
                  tip_lit[2] - ctr[2]), n) / sn
        tipS = tuple(tip_lit[i] - s[i] * t for i in range(3))
        d = tuple(tipS[i] - root[i] for i in range(3))
        out["shadow_len"] = math.sqrt(_dot(d, d)) * k
        if geo["tag"] == "h" and s[2] > 1e-6:
            nod = tuple(root[i] + gd[i] * glen * 0.62 for i in range(3))
            tn = _dot((nod[0] - ctr[0], nod[1] - ctr[1], nod[2] - ctr[2]), n) / sn
            nS = tuple(nod[i] - s[i] * tn for i in range(3))
            dn = tuple(nS[i] - root[i] for i in range(3))
            out["nodus_shadow"] = math.sqrt(_dot(dn, dn)) * k
            out["nodus_height"] = _dot((nod[0] - ctr[0], nod[1] - ctr[1],
                                        nod[2] - ctr[2]), n) * k
    return out



def solar_time_to_clock(date_local, target_lat_hours, lat, lon, tz,
                        window_hours=36.0):
    """
    求"地方真太阳时 = target"的那个瞬间, 返回当地标准时 datetime。
    做法: 对太阳的地方时角求根 (不是用平均均时差近似), 所以是精确值。
    """
    Ht = norm180((target_lat_hours - 12.0) * 15.0)

    def f(t_utc):
        p = EPH.get("太阳", t_utc)
        return norm180(norm180(p.gha + lon) - Ht)

    base = dt.datetime(date_local.year, date_local.month, date_local.day)
    start = base - dt.timedelta(hours=tz) - dt.timedelta(hours=2)
    step = dt.timedelta(minutes=20)
    n = int(window_hours * 3)
    prev_t, prev_v = start, f(start)
    for i in range(1, n + 1):
        t = start + step * i
        v = f(t)
        if prev_v < 0 <= v and (v - prev_v) < 180:
            lo, hi = prev_t, t
            for _ in range(40):
                mid = lo + (hi - lo) / 2
                if f(mid) < 0:
                    lo = mid
                else:
                    hi = mid
            res = (lo + (hi - lo) / 2) + dt.timedelta(hours=tz)
            if res.date() == date_local or abs((res.date() - date_local).days) <= 1:
                return res
        prev_t, prev_v = t, v
    return None


STD_DIAL_SIZES = [("袖珍 10 cm", 10.0), ("桌面 15 cm", 15.0), ("常用 30 cm", 30.0),
                  ("庭园 60 cm", 60.0), ("广场 150 cm", 150.0)]


def hour_line_angle(geo, lat, H):
    """
    时线与正午线 (子午线) 的夹角 θ (度), 在晷面内量, 下午一侧为正。
    (按晷面「上」方向量出来的角在赤道晷、垂直晷、南半球水平晷上
     会差 180°, 不能直接拿来刻晷面。)
    """
    n, r, u = geo["n"], geo["r"], geo["u"]
    d0 = style_shadow_on_plane(lat, 0.0, n, r, u)
    d = style_shadow_on_plane(lat, H, n, r, u)
    d15 = style_shadow_on_plane(lat, 15.0, n, r, u)
    if d0 is None or d is None or d15 is None:
        return None

    def ang(a, b):
        return math.degrees(math.atan2(a[0] * b[1] - a[1] * b[0],
                                       a[0] * b[0] + a[1] * b[1]))
    sgn = 1.0 if ang(d0, d15) > 0 else -1.0
    t = sgn * ang(d0, d)
    return 0.0 if abs(t) < 5e-9 else t          # 正午印 +0.000°, 不印 −0.000°


def dial_spec_lines(kind, lat, r_cm, hour_sys="24h", sc_mode="midculm"):
    """晷面制作规格 (可直接照着做一个)。"""
    L = []
    A = L.append
    geo = dial_geom3d(kind, lat)
    m = dial_metrics(kind, lat, 45.0, 180.0, r_cm)
    name = {"h": "水平晷", "e": "赤道晷", "v": vertical_dial_name(lat)}[geo["tag"]]
    north = lat >= 0
    P = _en("北", "north") if north else _en("南", "south")   # 升起的天极一侧
    Q = _en("南", "south") if north else _en("北", "north")   # 垂直晷墙面朝向 (朝赤道)
    A("═" * 66)
    A(_T("  %s  制作规格   纬度 φ = %s   晷面半径 R = %.1f cm")
      % (name, deg_dm(lat, "N", "S"), r_cm))
    A("═" * 66)
    A(_T("  晷面形状      %s") % (_T("圆盘, 直径 %.1f cm") % (2 * r_cm)
                            if geo["shape"] == "disc"
                            else _T("矩形, 宽 %.1f cm × 高 %.1f cm")
                                 % (2 * r_cm, 2 * r_cm * geo["size"][1] / geo["size"][0])))
    if geo["tag"] == "h":
        A(_T("  晷针形状      直角三角形 (指%s的三角板)") % P)
        A(_T("  晷针仰角      %.4f°  = 当地纬度 |φ|") % abs(lat))
        A(_T("  三角形底边    %.2f cm  (沿子午线由中心向%s量)") % (m["base_len"], P))
        A(_T("  三角形高      %.2f cm  (%s端垂直立起)") % (m["tip_height"], P))
        A(_T("  斜边(晷针)长  %.2f cm") % m["style_len"])
        A(_T("  安装          底边压在子午线上, 直角在%s端, 斜边朝%s天极") % (P, P))
    elif geo["tag"] == "e":
        A("  晷针形状      垂直穿过盘心的细杆 (两面都要露出)")
        A(_T("  盘面倾角      %.4f°  = 90° − |φ| (盘面平行天赤道)") % (90 - abs(lat)))
        A(_T("  杆长          每面露出 %.2f cm 即可") % m["style_len"])
        A(_T("  安装          杆指向天极, 盘心在杆上; 春分后看%s面, 秋分后看%s面")
          % ((_en("上", "upper"), _en("下", "lower")) if north
             else (_en("下", "lower"), _en("上", "upper"))))
    else:
        A("  晷针形状      自墙面伸出的斜杆 (指向天极)")
        A(_T("  杆与墙面夹角  %.4f°  = 90° − |φ|") % (90 - abs(lat)))
        A(_T("  杆长          %.2f cm") % m["style_len"])
        A(_T("  安装          墙面正%s, 杆根在盘面上缘中点, 斜向下方伸出 (指向%s天极)")
          % (Q, Q))
    A("")
    A("  时线角度表 (θ 自子午线量起, 正值向下午一侧)")
    A("  " + "-" * 62)
    if geo["tag"] == "h":
        A("  公式: tanθ = sinφ · tanH      (H = 时角 = (真太阳时 − 12)×15°)")
    elif geo["tag"] == "e":
        A("  公式: θ = H                   (每小时正好 15°, 均匀)")
    else:
        A("  公式: tanθ = cosφ · tanH")
    A("  " + "-" * 62)
    A("   真太阳时    时角 H        θ (度)      每刻 (15分) 的 θ")
    for hh in range(0, 24):
        H = (hh - 12) * 15.0
        if abs(H) > 135:
            continue
        d = style_shadow_on_plane(lat, H, geo["n"], geo["r"], geo["u"])
        if d is None:
            continue
        th = hour_line_angle(geo, lat, H)
        kes = []
        for q in (1, 2, 3):
            tq = hour_line_angle(geo, lat, H + q * 3.75)
            if tq is not None:
                kes.append("%+7.3f" % tq)
        A("     %02d:00    %+7.2f°    %+8.3f°   %s"
          % (hh, H, th, " ".join(kes)))
    A("  " + "-" * 62)
    A("  注: 时线只与纬度有关, 与日期无关; 刻 = 15 分 = 时角 3.75°")
    return L


# ===========================================================================
#  日晷页签
# ===========================================================================
class SundialTab(ttk.Frame):
    DIAL_TYPES = ["水平晷 Horizontal", "赤道晷 Equatorial", "垂直朝南晷 Vertical South"]

    def __init__(self, master, app):
        super().__init__(master, padding=6)
        self.app = app
        self._events_cache = {}
        self.clock = TimeEngine()
        self.cam = Camera3D(az=200.0, el=24.0, dist=6.6, fov=38.0,
                            target=(0, 0, 0.32))
        self._mark_hits = []
        self._hover_mark = None       # (H角度, 组) 鼠标掠过的刻度
        self._pin_mark = None         # 点选钉住的刻度
        self._hot_mark = None
        self._mark_pos = None
        self._spec_win = None
        self._build()
        self.mouse = OrbitMouse(self.canvas, self.cam, self.redraw)
        self.mouse.on_pan = self._mark_panned
        self.mouse.on_click = self._on_click_mark
        self.canvas.bind("<Motion>", self._on_hover_mark)
        self.canvas.bind("<Leave>", lambda e: self._on_hover_mark(None))
        self._apply_recommend()          # 一开程序就按本地纬度选好晷面
        self.after(200, self._tick)

    # -- 界面 ---------------------------------------------------------------
    def _build(self):
        scroll = VScrollFrame(self, width=410)
        scroll.pack(side="right", fill="y")
        right = scroll.body
        left = ttk.Frame(self)
        left.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(left, bg="#101418", highlightthickness=0,
                                width=620, height=620)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.redraw())

        # ---- 地点 ----
        loc = ttk.LabelFrame(right, text=" 观测地点 ", padding=6)
        loc.pack(fill="x", pady=(0, 6))
        self.city_var = tk.StringVar(value=CITIES[DEFAULT_CITY][0])
        cb = ttk.Combobox(loc, textvariable=self.city_var, width=26,
                          values=[c[0] for c in CITIES] + ["自定义 Custom"],
                          state="readonly")
        cb.grid(row=0, column=0, columnspan=4, sticky="we", pady=2)
        cb.bind("<<ComboboxSelected>>", self._on_city)

        self.lat_var = tk.StringVar(value="%.4f" % CITIES[DEFAULT_CITY][1])
        self.lon_var = tk.StringVar(value="%.4f" % CITIES[DEFAULT_CITY][2])
        self.tz_var = tk.StringVar(value="%.2f" % CITIES[DEFAULT_CITY][3])
        ttk.Label(loc, text="纬度 φ (N+)").grid(row=1, column=0, sticky="w")
        ttk.Entry(loc, textvariable=self.lat_var, width=11).grid(row=1, column=1, sticky="w")
        ttk.Label(loc, text="经度 λ (E+)").grid(row=1, column=2, sticky="w", padx=(8, 0))
        ttk.Entry(loc, textvariable=self.lon_var, width=11).grid(row=1, column=3, sticky="w")
        ttk.Label(loc, text="时区 UTC±").grid(row=2, column=0, sticky="w")
        ttk.Entry(loc, textvariable=self.tz_var, width=11).grid(row=2, column=1, sticky="w")
        ttk.Button(loc, text="按经度取时区", width=14,
                   command=self._tz_from_lon).grid(row=2, column=2, columnspan=2,
                                                   sticky="we", padx=(8, 0))
        for v in (self.lat_var, self.lon_var, self.tz_var):
            v.trace_add("write", lambda *a: (self._invalidate(),
                                             self._apply_recommend()))

        # ---- 晷面 ----
        dial = ttk.LabelFrame(right, text=" 晷面与视图 ", padding=6)
        dial.pack(fill="x", pady=(0, 6))
        self.dial_var = tk.StringVar(value=self.DIAL_TYPES[0])
        self._dial_rbs = {}
        for i, name in enumerate(self.DIAL_TYPES):
            rb = ttk.Radiobutton(dial, text=name, value=name, variable=self.dial_var,
                                 command=self.redraw)
            rb.grid(row=i, column=0, sticky="w")
            self._dial_rbs[name] = rb
        self._dial_hemi = None
        self.show_lines = tk.BooleanVar(value=True)
        self.show_nodus = tk.BooleanVar(value=True)
        self.show_path = tk.BooleanVar(value=True)
        ttk.Checkbutton(dial, text="显示时线", variable=self.show_lines,
                        command=self.redraw).grid(row=0, column=1, sticky="w", padx=10)
        ttk.Checkbutton(dial, text="显示珠影(nodus)", variable=self.show_nodus,
                        command=self.redraw).grid(row=1, column=1, sticky="w", padx=10)
        ttk.Checkbutton(dial, text="显示太阳日行轨迹", variable=self.show_path,
                        command=self.redraw).grid(row=2, column=1, sticky="w", padx=10)
        ttk.Separator(dial, orient="horizontal").grid(row=3, column=0, columnspan=2,
                                                      sticky="we", pady=4)
        self.view_var = tk.StringVar(value="3D")
        ttk.Label(dial, text="视图").grid(row=4, column=0, sticky="w")
        vf = ttk.Frame(dial)
        vf.grid(row=4, column=1, sticky="w", padx=10)
        ttk.Radiobutton(vf, text="3D 立体", value="3D", variable=self.view_var,
                        command=self.redraw).pack(side="left")
        ttk.Radiobutton(vf, text="2D 平面", value="2D", variable=self.view_var,
                        command=self.redraw).pack(side="left", padx=(8, 0))
        self.hour_sys = tk.StringVar(value="24h")
        ttk.Label(dial, text="时制").grid(row=5, column=0, sticky="w")
        hf = ttk.Frame(dial)
        hf.grid(row=5, column=1, sticky="w", padx=10)
        ttk.Radiobutton(hf, text="24 小时", value="24h", variable=self.hour_sys,
                        command=self.redraw).pack(side="left")
        ttk.Radiobutton(hf, text="12 时辰", value="12sc", variable=self.hour_sys,
                        command=self.redraw).pack(side="left", padx=(8, 0))
        self.scale_mode = tk.StringVar(value="both")
        ttk.Label(dial, text="刻度").grid(row=10, column=0, sticky="w")
        sf = ttk.Frame(dial)
        sf.grid(row=10, column=1, sticky="w", padx=10)
        for txt, val in (("真太阳时", "solar"), ("标准时", "clock"), ("两者", "both")):
            ttk.Radiobutton(sf, text=txt, value=val, variable=self.scale_mode,
                            command=self.redraw).pack(side="left")
        self.sc_mode = tk.StringVar(value="midculm")
        ttk.Label(dial, text="时辰").grid(row=11, column=0, sticky="w")
        cf = ttk.Frame(dial)
        cf.grid(row=11, column=1, sticky="w", padx=10)
        ttk.Radiobutton(cf, text="中天起午 (你的用法)", value="midculm",
                        variable=self.sc_mode,
                        command=self.redraw).pack(side="left")
        ttk.Radiobutton(cf, text="传统", value="trad", variable=self.sc_mode,
                        command=self.redraw).pack(side="left", padx=(6, 0))
        szf = ttk.Frame(dial)
        szf.grid(row=12, column=0, columnspan=2, sticky="we", pady=(3, 0))
        ttk.Label(szf, text="晷面半径 cm").pack(side="left")
        self.size_var = tk.StringVar(value="30")
        e_sz = ttk.Entry(szf, textvariable=self.size_var, width=5)
        e_sz.pack(side="left", padx=(3, 4))
        self.size_var.trace_add("write", lambda *a: self.redraw())
        self.std_size = tk.StringVar(value=STD_DIAL_SIZES[2][0])
        cb_sz = ttk.Combobox(szf, textvariable=self.std_size, width=11,
                             state="readonly",
                             values=[n for n, _v in STD_DIAL_SIZES])
        cb_sz.pack(side="left", padx=(0, 6))
        cb_sz.bind("<<ComboboxSelected>>", self._on_std_size)
        ttk.Button(szf, text="规格表", width=7,
                   command=self.open_spec).pack(side="left")
        self.auto_dial = tk.BooleanVar(value=True)
        ttk.Checkbutton(szf, text="按纬度自动选晷面", variable=self.auto_dial,
                        command=self._apply_recommend).pack(side="left")
        self.all_hours = tk.BooleanVar(value=False)
        ttk.Checkbutton(dial, text="画满 24 时线 (极地/极昼时有用)",
                        variable=self.all_hours,
                        command=self.redraw).grid(row=6, column=0, columnspan=2,
                                                  sticky="w", pady=(2, 0))
        self.show_ke = tk.BooleanVar(value=True)
        ttk.Checkbutton(dial, text="显示刻 (15 分一刻, 一时辰八刻)",
                        variable=self.show_ke,
                        command=self.redraw).grid(row=7, column=0, columnspan=2,
                                                  sticky="w")
        self.auto_face = tk.BooleanVar(value=True)
        ttk.Checkbutton(dial, text="赤道晷自动转到有影子的一面",
                        variable=self.auto_face,
                        command=self.redraw).grid(row=8, column=0, columnspan=2,
                                                  sticky="w")
        vb = ttk.Frame(dial)
        vb.grid(row=9, column=0, columnspan=2, sticky="we", pady=(4, 0))
        ttk.Button(vb, text="放大", width=6,
                   command=lambda: self._zoom(1 / 1.6)).pack(side="left")
        ttk.Button(vb, text="缩小", width=6,
                   command=lambda: self._zoom(1.6)).pack(side="left", padx=2)
        ttk.Button(vb, text="正对晷面", width=9,
                   command=self._face_on).pack(side="left", padx=2)
        ttk.Button(vb, text="重置视角", width=9,
                   command=self._reset_view).pack(side="left")

        # ---- 时间 ----
        tm = ttk.LabelFrame(right, text=" 时间 (当地标准时, 默认随真实时间走) ", padding=6)
        tm.pack(fill="x", pady=(0, 6))
        row0 = ttk.Frame(tm)
        row0.grid(row=0, column=0, columnspan=4, sticky="we")
        self.pause_btn = ttk.Button(row0, text="⏸ 暂停", width=9,
                                    command=self._toggle_pause)
        self.pause_btn.pack(side="left")
        ttk.Label(row0, text="速度").pack(side="left", padx=(8, 2))
        self.speed_var = tk.StringVar(value=SPEEDS[0][0])
        cbs = ttk.Combobox(row0, textvariable=self.speed_var, width=9, state="readonly",
                           values=[s[0] for s in SPEEDS])
        cbs.pack(side="left")
        cbs.bind("<<ComboboxSelected>>", self._on_speed)
        ttk.Button(row0, text="回到现在", width=9,
                   command=self._go_now).pack(side="left", padx=(8, 0))
        self.date_var = tk.StringVar()
        self.time_var = tk.StringVar()
        ttk.Label(tm, text="日期").grid(row=1, column=0, sticky="w", pady=(4, 0))
        self.date_ent = ttk.Entry(tm, textvariable=self.date_var, width=12)
        self.date_ent.grid(row=1, column=1, sticky="w", pady=(4, 0))
        ttk.Label(tm, text="时刻").grid(row=1, column=2, sticky="w", padx=(8, 0), pady=(4, 0))
        self.time_ent = ttk.Entry(tm, textvariable=self.time_var, width=10)
        self.time_ent.grid(row=1, column=3, sticky="w", pady=(4, 0))
        ttk.Button(tm, text="跳到该时刻", command=self._jump_to).grid(
            row=2, column=0, columnspan=4, sticky="we", pady=3)
        btns = ttk.Frame(tm)
        btns.grid(row=3, column=0, columnspan=4, sticky="we")
        for txt, delta in (("−1日", -1440), ("−1时", -60), ("−1分", -1),
                           ("+1分", 1), ("+1时", 60), ("+1日", 1440)):
            ttk.Button(btns, text=txt, width=6,
                       command=lambda d=delta: self._nudge(d)).pack(side="left")
        tm.columnconfigure(3, weight=1)

        # ---- 数据 ----
        info = ttk.LabelFrame(right, text=" 计算结果 ", padding=4)
        info.pack(fill="both", expand=True)
        self.info = tk.Text(info, width=46, height=34, bg="#0d1117", fg="#d8e0e8",
                            font=self.app.mono_font, relief="flat", wrap="word")
        self.info.pack(fill="both", expand=True)
        self.info.configure(state="disabled")

        now = self.local_time()
        self.date_var.set(now.strftime("%Y-%m-%d"))
        self.time_var.set(now.strftime("%H:%M:%S"))


    # -- 参数读写 -----------------------------------------------------------
    def _invalidate(self):
        self._events_cache.clear()

    def _on_city(self, *_):
        name = self.city_var.get()
        for c in CITIES:
            if c[0] == name:
                self.lat_var.set("%.4f" % c[1])
                self.lon_var.set("%.4f" % c[2])
                self.tz_var.set("%.2f" % c[3])
                break
        self._invalidate()
        self._apply_recommend()
        self.redraw()

    def _apply_recommend(self):
        """按纬度换上合适的晷面 (可关掉)。"""
        if not self.auto_dial.get():
            return
        p = self.params()
        if not p:
            return
        kind, why = recommend_dial(p[0])
        for k in self.DIAL_TYPES:
            if k.startswith(kind):
                if self.dial_var.get() != k:
                    self.dial_var.set(k)
                    self._reset_view()
                break

    def _tz_from_lon(self):
        try:
            lon = float(self.lon_var.get())
        except ValueError:
            return
        self.tz_var.set("%.2f" % round(lon / 15.0))
        self._invalidate()
        self.redraw()

    def _on_std_size(self, *_):
        for n, v in STD_DIAL_SIZES:
            if n == self.std_size.get():
                self.size_var.set("%g" % v)
                break
        self.redraw()

    def _mark_panned(self):
        self._panned = True

    def _zoom(self, f):
        self.cam.zoom(f)
        self.redraw()

    def _reset_view(self):
        kind = self.dial_var.get()
        self.cam.fov = 38.0
        self.cam.dist = 6.6
        self._panned = False
        if kind.startswith("垂直"):
            p = self.params()
            south = bool(p) and p[0] < 0               # 南半球墙面朝北
            self.cam.az, self.cam.el = (0.0 if south else 180.0), 18.0
        elif kind.startswith("赤道"):
            self._face_on()
            return
        else:
            self.cam.az, self.cam.el = 200.0, 30.0
        self.redraw()

    def _face_on(self):
        """把相机移到"正对受照面"的方向 (略偏一点便于看出立体)。"""
        p = self.params()
        if not p:
            return
        lat, lon, tz = p
        utc = self.local_time() - dt.timedelta(hours=tz)
        sun = EPH.get("太阳", utc)
        geo = dial_geom3d(self.dial_var.get(), lat)
        n = geo["n"]
        s = _enu_from_altaz(*altaz_from_hadec(norm180(sun.gha + lon), sun.dec, lat))
        if _dot(n, s) < 0:                      # 受照的是背面
            n = (-n[0], -n[1], -n[2])
        self.cam.az = norm360(math.degrees(math.atan2(n[0], n[1])))
        self.cam.el = max(Camera3D.EL_MIN + 6,
                          min(Camera3D.EL_MAX - 6,
                              math.degrees(math.asin(max(-1.0, min(1.0, n[2])))) + 10))
        self.redraw()

    def _toggle_pause(self):
        paused = self.clock.toggle_pause()
        self.pause_btn.configure(text="▶ 继续" if paused else "⏸ 暂停")
        self.redraw()

    def _on_speed(self, *_):
        for name, val in SPEEDS:
            if name == self.speed_var.get():
                self.clock.speed = val
                break

    def _go_now(self):
        self.clock.now()
        self.clock.speed = 1.0
        self.speed_var.set(SPEEDS[0][0])
        self.redraw()

    def _jump_to(self):
        p = self.params()
        tz = p[2] if p else 8.0
        try:
            d = dt.datetime.strptime(self.date_var.get().strip(), "%Y-%m-%d")
            parts = self.time_var.get().strip().split(":")
            hh = int(parts[0])
            mm = int(parts[1]) if len(parts) > 1 else 0
            ss = float(parts[2]) if len(parts) > 2 else 0.0
            t = d + dt.timedelta(hours=hh, minutes=mm, seconds=ss)
        except Exception:
            messagebox.showwarning("时刻格式", "日期请用 2026-08-30, 时刻请用 16:20:00")
            return
        self.clock.set_local(t, tz)
        self.redraw()

    def _nudge(self, minutes):
        self.clock.jump(dt.timedelta(minutes=minutes))
        self.redraw()

    def params(self):
        try:
            lat = float(self.lat_var.get())
            lon = float(self.lon_var.get())
            tz = float(self.tz_var.get())
        except ValueError:
            return None
        lat = max(-89.9, min(89.9, lat))
        return lat, lon, tz

    def local_time(self):
        p = self.params()
        tz = p[2] if p else 8.0
        return self.clock.local(tz)

    # -- 主循环 -------------------------------------------------------------
    def _tick(self):
        self.clock.tick()
        if not self.winfo_ismapped():
            self.after(400, self._tick)
            return
        # 用户没在编辑时间框时, 让它跟着走
        try:
            foc = self.focus_get()
        except Exception:
            foc = None
        if foc not in (self.date_ent, self.time_ent):
            t = self.local_time()
            self.date_var.set(t.strftime("%Y-%m-%d"))
            self.time_var.set(t.strftime("%H:%M:%S"))
        self.redraw()
        self.after(200, self._tick)

    # -- 绘图 ---------------------------------------------------------------
    def redraw(self):
        p = self.params()
        if not p:
            return
        lat, lon, tz = p
        loc_t = self.local_time()
        utc = loc_t - dt.timedelta(hours=tz)
        sun = EPH.get("太阳", utc)
        lha = norm180(sun.gha + lon)                    # 地方真时角
        alt_geo, az = altaz_from_hadec(lha, sun.dec, lat)
        refr = refraction_true_to_app(alt_geo) if alt_geo > -2 else 0.0
        alt_app = alt_geo + refr / 60.0

        hemi = lat >= 0
        if hemi != getattr(self, "_dial_hemi", None) and getattr(self, "_dial_rbs", None):
            self._dial_hemi = hemi
            self._dial_rbs[self.DIAL_TYPES[2]].configure(
                text="垂直朝南晷 Vertical South" if hemi else "垂直朝北晷 Vertical North")
        self._marks = self.build_marks(sun, utc, lon, tz)
        self._mark_hits = []
        self._hot_mark = self._pin_mark or self._hover_mark
        c = self.canvas
        c.delete("all")
        W = c.winfo_width() or 620
        Hgt = c.winfo_height() or 620
        kind = self.dial_var.get()
        if self.view_var.get() == "3D":
            self._draw_3d(W, Hgt, lat, lha, alt_app, az, sun.dec, kind)
        elif kind.startswith("水平"):
            self._draw_horizontal(W, Hgt, lat, lha, alt_app, az, sun.dec)
        elif kind.startswith("赤道"):
            self._draw_equatorial(W, Hgt, lat, lha, sun.dec, alt_app)
        else:
            self._draw_vertical(W, Hgt, lat, lha, alt_app, az)

        mode = self.scale_mode.get()
        leg = []
        if mode in ("solar", "both"):
            leg.append(("蓝 = 真太阳时 (晷面固有刻度)", MARK_COLOR["solar"]["major"]))
        if mode in ("clock", "both"):
            leg.append(("橙 = 当地标准时 (按今日均时差画, 每天略移)",
                        MARK_COLOR["clock"]["major"]))
        lx = 12
        if leg:                                  # 图例垫一条底色, 三维场景的字母不会和它叠在一起
            lw = sum(text_size(self.app.ui_font, t)[0] + 20 for t, _c in leg)
            lh = text_size(self.app.ui_font, "Ag")[1]
            c.create_rectangle(lx - 6, Hgt - 12 - lh / 2 - 2, lx + lw - 14,
                               Hgt - 12 + lh / 2 + 2, fill=c.cget("bg"), outline="")
        for txt, col in leg:
            c.create_text(lx, Hgt - 12, anchor="w", text=txt, fill=col,
                          font=self.app.ui_font)
            lx += text_size(self.app.ui_font, txt)[0] + 20     # 量实际显示的那种语言
        if self._hot_mark and self._mark_pos:
            lines = self.mark_detail(self._hot_mark, lat, lon, tz, loc_t)
            if lines:
                canvas_tooltip(c, self._mark_pos[0], self._mark_pos[1], lines,
                               self.app.tip_font, W, Hgt)
        self._update_info(lat, lon, tz, loc_t, utc, sun, lha, alt_geo,
                          alt_app, az, refr)




    # ---- 刻度点选 ----
    def _find_mark(self, x, y, rad=14.0):
        best, bd = None, rad * rad
        for mx, my, Hh, kind_m, lbl, grp in getattr(self, "_mark_hits", []):
            d = (mx - x) ** 2 + (my - y) ** 2
            if d < bd:
                bd = d
                best = (Hh, grp, kind_m, lbl, mx, my)
        return best

    def _on_hover_mark(self, e):
        if e is None:
            if self._hover_mark:
                self._hover_mark = None
                self.redraw()
            return
        hit = self._find_mark(e.x, e.y)
        newv = (hit[0], hit[1]) if hit else None
        if newv != self._hover_mark:
            self._hover_mark = newv
            if hit:
                self._mark_pos = (hit[4], hit[5])
                self._mark_kind = (hit[2], hit[3])
            self.redraw()
        elif hit:
            self._mark_pos = (hit[4], hit[5])

    def _on_click_mark(self, x, y):
        hit = self._find_mark(x, y, 16.0)
        if hit:
            key = (hit[0], hit[1])
            self._pin_mark = None if self._pin_mark == key else key
            self._mark_pos = (hit[4], hit[5])
            self._mark_kind = (hit[2], hit[3])
        else:
            self._pin_mark = None
        self.redraw()

    def mark_detail(self, key, lat, lon, tz, loc_t):
        """某条刻度的详细时刻 (真太阳时 + 精确钟表时刻)。"""
        Hh, grp = key
        kind_m, lbl = getattr(self, "_mark_kind", ("hour", ""))
        lat_h = norm180(Hh) / 15.0 + 12.0
        date = loc_t.date()
        out = []
        scm = self.sc_mode.get()

        def clk(target):
            t = solar_time_to_clock(date, target, lat, lon, tz)
            return t.strftime("%H:%M:%S") if t else "—"

        if grp == "clock":
            out.append(_T("【钟表刻度】当地标准时 %s:00") % (lbl if lbl else "—"))
            out.append(_T("  对应真太阳时 %s") % hm_from_hours(lat_h))
            out.append("  (橙色刻度按今日均时差画, 每天会略移)")
            return out
        # 真太阳时一侧
        idx, nm, ke = shichen_of(lat_h % 24.0, scm)
        if kind_m == "label" or self.hour_sys.get() == "12sc":
            start = (idx * 2 - 1) % 24 if scm == "trad" else (idx * 2) % 24
            end = (start + 2) % 24
            out.append(_T("【%s时】起算: %s") % (nm, "传统(午含中天)" if scm == "trad"
                                        else "中天起午"))
            out.append(_T("  真太阳时  %02d:00:00 → %02d:00:00") % (start, end))
            out.append(_T("  当地钟表  %s → %s   ← 实际进出该时辰的时刻")
                       % (clk(start), clk(end)))
            out.append("  八刻的钟表时刻:")
            for q in range(8):
                out.append(_T("    第%d刻 %s") % (q + 1, clk((start + q * 0.25) % 24)))
        elif kind_m == "ke":
            base = math.floor(lat_h * 4) / 4.0
            out.append(_T("【刻】真太阳时 %s") % hm_from_hours(base))
            out.append(_T("  当地钟表 %s") % clk(base))
            out.append(_T("  属 %s时 第 %d 刻") % (nm, ke))
        else:
            out.append(_T("【真太阳时刻度】%s:00") % (lbl if lbl else "%d" % round(lat_h)))
            out.append(_T("  真太阳时 %s") % hm_from_hours(lat_h))
            out.append(_T("  当地钟表 %s   ← 晷影指到这条线时手表的读数")
                       % clk(round(lat_h) % 24))
            out.append(_T("  属 %s时 第 %d 刻") % (nm, ke))
        out.append("  (点一下钉住/取消; 空白处点一下取消)")
        return out

    def open_spec(self):
        """晷面制作规格窗口。"""
        p = self.params()
        if not p:
            return
        try:
            r_cm = float(self.size_var.get())
        except ValueError:
            r_cm = 30.0
        win = tk.Toplevel(self)
        win.title("晷面制作规格 Dial Spec")
        win.geometry("760x620")
        win.configure(bg="#161c22")
        txt = tk.Text(win, bg="#0d1117", fg="#d8e0e8", font=self.app.mono_font,
                      relief="flat", wrap="word")
        ysb = ttk.Scrollbar(win, orient="vertical", command=txt.yview)
        txt.configure(yscrollcommand=ysb.set)
        ysb.pack(side="right", fill="y")
        txt.pack(side="left", fill="both", expand=True)
        lines = dial_spec_lines(self.dial_var.get(), p[0], r_cm,
                                self.hour_sys.get(), self.sc_mode.get())
        # 今日时辰对照
        loc_t = self.local_time()
        lines.append("")
        lines.append(_T("  今日 (%s) 12 时辰的钟表时刻 —— 逐个求根解出, 非近似")
                     % loc_t.strftime("%Y-%m-%d"))
        lines.append("  " + "-" * 62)
        for name, s0, s1 in shichen_table(self.sc_mode.get()):
            t0 = solar_time_to_clock(loc_t.date(), s0, p[0], p[1], p[2])
            t1 = solar_time_to_clock(loc_t.date(), s1, p[0], p[1], p[2])
            lines.append(_T("    %s  真太阳时 %02d:00–%02d:00   钟表 %s – %s")
                         % (name, int(s0), int(s1),
                            t0.strftime("%H:%M:%S") if t0 else "—",
                            t1.strftime("%H:%M:%S") if t1 else "—"))
        txt.insert("1.0", "\n".join(lines))
        txt.configure(state="disabled")
        return win

    # ---- 刻度 ----
    def clock_to_lat_offset(self, sun, utc, lon, tz):
        """标准时 -> 真太阳时 的偏移(小时):  真太阳时 = 标准时 + off"""
        ut_h = (utc.hour + utc.minute / 60.0 + utc.second / 3600.0
                + utc.microsecond / 3.6e9)
        eot_min = norm180((sun.gha + 180.0) - ut_h * 15.0) * 4.0
        lon_corr_min = (lon - tz * 15.0) * 4.0
        return (eot_min + lon_corr_min) / 60.0, eot_min, lon_corr_min

    def build_marks(self, sun, utc, lon, tz):
        """返回 [(时角H, 类型, 标签, 'solar'/'clock')]"""
        out = []
        mode = self.scale_mode.get()
        if mode in ("solar", "both"):
            for hh, kind, lbl in dial_marks(self.hour_sys.get(),
                                            self.show_ke.get(),
                                            self.sc_mode.get()):
                out.append(((hh - 12.0) * 15.0, kind, lbl, "solar"))
        if mode in ("clock", "both"):
            off = self.clock_to_lat_offset(sun, utc, lon, tz)[0]
            for t in range(24):
                lh = t + off
                out.append(((lh - 12.0) * 15.0,
                            "major" if t % 6 == 0 else "hour",
                            "%d" % (t if t else 24), "clock"))
            if self.show_ke.get() and mode == "clock":
                for q in range(48):            # 只在单独看钟表刻度时画半小时刻
                    t = q * 0.5
                    if abs(t - round(t)) < 1e-9:
                        continue
                    out.append(((t + off - 12.0) * 15.0, "ke", "", "clock"))
        return out

    # ---- 通用 ----
    def hour_limit(self, lat, dec):
        """当日应画出的最大时角 (度)。"""
        if self.all_hours.get():
            return 180.0
        return sun_hour_limit(lat, dec) + 7.5

    # ---- 三维视图 ----
    def _draw_3d(self, W, H, lat, lha, alt, az, dec, kind):
        c = self.canvas
        geo = dial_geom3d(kind, lat)
        if not getattr(self, "_panned", False):
            self.cam.target[0] = 0.0
            self.cam.target[1] = 0.0
            self.cam.target[2] = geo["target_z"]
        pt = Painter3D(c, self.cam, W, H)
        n, rv, uv, ctr = geo["n"], geo["r"], geo["u"], geo["center"]

        def plate_pt(x, y, lift=0.0):
            return (ctr[0] + rv[0] * x + uv[0] * y + n[0] * lift,
                    ctr[1] + rv[1] * x + uv[1] * y + n[1] * lift,
                    ctr[2] + rv[2] * x + uv[2] * y + n[2] * lift)

        # ---- 地面 ----
        GR = 2.05
        ring = [(GR * dsin(a), GR * dcos(a), 0.0) for a in range(0, 360, 5)]
        pt.poly(ring, bias=90.0, fill="#0e161d", outline="#1d2c38")
        for rr in (0.7, 1.4, 2.0):
            pts = [(rr * dsin(a), rr * dcos(a), 0.004) for a in range(0, 361, 5)]
            pt.polyline(pts, bias=88.0, fill="#1b2b36")
        for a in range(0, 360, 15):
            pt.line((0.35 * dsin(a), 0.35 * dcos(a), 0.004),
                    (GR * dsin(a), GR * dcos(a), 0.004), bias=88.0,
                    fill="#182530" if a % 45 else "#22364a")
        for lbl, a in (("N", 0), ("E", 90), ("S", 180), ("W", 270)):
            pt.text(((GR + 0.16) * dsin(a), (GR + 0.16) * dcos(a), 0.06), lbl,
                    fill="#8fb3d0" if lbl == "N" else "#5f7c93",
                    font=self.app.ui_font_b)

        # ---- 立柱 (赤道晷) ----
        if geo["tag"] == "e":
            pt.line((0, 0, 0), ctr, fill="#3b4d5c", width=8)
        if geo["tag"] == "v":                       # 墙体侧面
            hw, hh = geo["size"]
            pt.poly([plate_pt(-hw, -hh), plate_pt(hw, -hh),
                     plate_pt(hw, -hh, -0.12), plate_pt(-hw, -hh, -0.12)],
                    fill="#151f28", outline="#28323b")

        # ---- 晷面 ----
        if geo["shape"] == "disc":
            R = geo["size"]
            rim = [plate_pt(R * dsin(a), R * dcos(a)) for a in range(0, 360, 5)]
        else:
            hw, hh = geo["size"]
            rim = [plate_pt(-hw, -hh), plate_pt(hw, -hh),
                   plate_pt(hw, hh), plate_pt(-hw, hh)]
        pt.poly(rim, fill="#33475699".replace("99",""), outline="#5b7d94", width=2)
        pt.polyline(rim + [rim[0]], bias=-0.001, fill="#4d6d82")

        # ---- 时线 ----
        ro = (geo["root"][0] - ctr[0], geo["root"][1] - ctr[1],
              geo["root"][2] - ctr[2])
        ox, oy = _dot(ro, rv), _dot(ro, uv)
        h0 = self.hour_limit(lat, dec)
        if self.show_lines.get():
            for Hh, kind_m, lbl, grp in getattr(self, "_marks", []):
                Hh = norm180(Hh)
                if abs(Hh) > h0:
                    continue
                d = style_shadow_on_plane(lat, Hh, n, rv, uv)
                if d is None:
                    continue
                if geo["tag"] == "v" and d[1] > -0.02:
                    continue
                t = plate_ray_len(geo, ox, oy, d[0], d[1])
                if t < 0.05:
                    continue
                frac = MARK_FRAC[kind_m]
                hot = (self._hot_mark is not None
                       and abs(norm180(self._hot_mark[0] - Hh)) < 1e-6
                       and self._hot_mark[1] == grp)
                if frac > 0:
                    p1 = plate_pt(ox + d[0] * t * (1 - frac),
                                  oy + d[1] * t * (1 - frac), 0.004)
                    p2 = plate_pt(ox + d[0] * t, oy + d[1] * t, 0.004)
                    pt.line(p1, p2, bias=LAY_LINE - (0.5 if hot else 0.0),
                            fill="#ffffff" if hot else MARK_COLOR[grp][kind_m],
                            width=(MARK_WIDTH[kind_m] + 2) if hot else MARK_WIDTH[kind_m])
                    q = pt.project(p2)
                    if q:
                        self._mark_hits.append((q[0], q[1], Hh, kind_m, lbl, grp))
                if lbl:
                    off_l = 0.12 if grp == "solar" else 0.22
                    p3 = plate_pt(ox + d[0] * (t + off_l),
                                  oy + d[1] * (t + off_l), 0.02)
                    pt.text(p3, lbl, bias=LAY_LINE, fill=MARK_COLOR[grp]["text"],
                            font=self.app.ui_font)

        # ---- 晷针 ----
        root3 = geo["root"]
        gd = geo["gdir"]
        tip = (root3[0] + gd[0] * geo["glen"], root3[1] + gd[1] * geo["glen"],
               root3[2] + gd[2] * geo["glen"])
        foot = None
        if geo["tri"]:
            dn = _dot((tip[0] - ctr[0], tip[1] - ctr[1], tip[2] - ctr[2]), n)
            foot = (tip[0] - n[0] * dn, tip[1] - n[1] * dn, tip[2] - n[2] * dn)

        # ---- 影子 ----
        s = _enu_from_altaz(alt, az)
        sn = _dot(s, n)
        # 赤道晷: 半年照上面半年照下面 —— 自动把相机搬到有影子的那一面
        if (geo["tag"] == "e" and self.auto_face.get() and alt > 0
                and abs(sn) > 1e-4 and not getattr(getattr(self, 'mouse', None),
                                                  'dragging', False)
                and not getattr(self, "_flipping", False)):
            e0 = self.cam.eye()
            if sn * _dot(n, (e0[0] - ctr[0], e0[1] - ctr[1], e0[2] - ctr[2])) < 0:
                nn = n if sn > 0 else (-n[0], -n[1], -n[2])
                self.cam.az = norm360(math.degrees(math.atan2(nn[0], nn[1])))
                self.cam.el = max(Camera3D.EL_MIN + 4,
                                  min(Camera3D.EL_MAX - 4,
                                      math.degrees(math.asin(
                                          max(-1.0, min(1.0, nn[2])))) + 10.0))
                self._flipping = True
                try:
                    c.delete("all")
                    return self._draw_3d(W, H, lat, lha, alt, az, dec, kind)
                finally:
                    self._flipping = False
        eye = self.cam.eye()
        cam_side = _dot(n, (eye[0] - ctr[0], eye[1] - ctr[1], eye[2] - ctr[2]))
        # 投影必须用「受照那一面」上的那段晷针:
        #   赤道晷的极轴贯穿盘面, 两面各有一段 —— 太阳在赤道以南 (秋分→春分)
        #   照的是南(下)面, 投影要用伸向南天极的那段; 若仍用北段, 投影点会
        #   穿过盘面落到太阳那一侧, 影子就「指向太阳」了 (旧版的错)。
        #   水平晷 / 垂直晷只有一面有针: 阳光照在另一面时根本没有影。
        tip_lit = style_tip_on_lit_side(geo, sn)
        style_lit = tip_lit is not None
        # 影子只在受照的那一面; 若视角在背面, 影子被晷面本身挡住
        lit_face_visible = (sn * cam_side) > 0
        shadow_ok = (alt > 0 and abs(sn) > 1e-4 and style_lit
                     and lit_face_visible)
        self._back_face = (alt > 0 and abs(sn) > 1e-4 and style_lit
                           and not lit_face_visible)
        self._no_style_side = alt > 0 and abs(sn) > 1e-4 and not style_lit
        if shadow_ok:
            def shade(P):
                t = _dot((P[0] - ctr[0], P[1] - ctr[1], P[2] - ctr[2]), n) / sn
                return (P[0] - s[0] * t, P[1] - s[1] * t, P[2] - s[2] * t)
            tipS = shade(tip_lit)
            lx = _dot((tipS[0] - ctr[0], tipS[1] - ctr[1], tipS[2] - ctr[2]), rv)
            ly = _dot((tipS[0] - ctr[0], tipS[1] - ctr[1], tipS[2] - ctr[2]), uv)
            dx, dy = lx - ox, ly - oy
            ln = math.hypot(dx, dy)
            clipped = False
            if ln > 1e-9:
                tmax = plate_ray_len(geo, ox, oy, dx / ln, dy / ln)
                if ln > tmax:
                    clipped = True
                    lx, ly = ox + dx / ln * tmax, oy + dy / ln * tmax
            tipS_draw = plate_pt(lx, ly, 0.006)
            if geo["tri"] and foot is not None:
                pt.poly([plate_pt(ox, oy, 0.006), foot, tipS_draw],
                        bias=LAY_SHADOW, fill="#0b1116", outline="#141d24")
            else:
                pt.line(plate_pt(ox, oy, 0.006), tipS_draw, bias=LAY_SHADOW,
                        fill="#0b1116", width=9)
            if self.show_path.get():
                far = (tip_lit[0] + s[0] * 1.5, tip_lit[1] + s[1] * 1.5,
                       tip_lit[2] + s[2] * 1.5)
                pt.line(far, tip_lit, bias=LAY_GNOMON, fill="#7a6a28", dash=(4, 4))
                pt.line(tip_lit, tipS_draw if not clipped else tipS,
                        bias=LAY_GNOMON, fill="#7a6a28", dash=(4, 4))

        # 晷针本体 (画在影子之后, 保证盖在上面)
        if geo["tri"] and foot is not None:
            pt.poly([root3, foot, tip], bias=LAY_GNOMON, fill="#8a7326",
                    outline="#d6b34a", width=2)
        else:
            pt.line(root3, tip, bias=LAY_GNOMON, fill="#d6b34a", width=6)
            if geo["tag"] == "e":            # 极轴贯穿盘面: 另一面那段等长
                back = (root3[0] - gd[0] * geo["glen"],
                        root3[1] - gd[1] * geo["glen"],
                        root3[2] - gd[2] * geo["glen"])
                lit_back = (tip_lit is not None and max(
                    abs(tip_lit[i] - back[i]) for i in range(3)) < 1e-9)
                pt.line(root3, back, bias=LAY_GNOMON,
                        fill="#d6b34a" if lit_back else "#8a7326", width=5)
        pt.dot(root3, 4, bias=LAY_GNOMON - 0.2, fill="#f0d67a", outline="")

        # ---- 珠影 (nodus) ----
        if self.show_nodus.get() and shadow_ok and geo["tag"] == "h":
            nod = (root3[0] + gd[0] * geo["glen"] * 0.62,
                   root3[1] + gd[1] * geo["glen"] * 0.62,
                   root3[2] + gd[2] * geo["glen"] * 0.62)
            tn = _dot((nod[0] - ctr[0], nod[1] - ctr[1], nod[2] - ctr[2]), n) / sn
            nS = (nod[0] - s[0] * tn, nod[1] - s[1] * tn, nod[2] - s[2] * tn)
            pt.dot(nod, 5, bias=LAY_GNOMON - 0.4, fill="#ffcf5c", outline="#5a4a10")
            pt.dot(nS, 4, bias=LAY_LINE - 0.1, fill="#c8a44a", outline="")

        # ---- 太阳与日行轨迹 ----
        SKY = 2.35
        if self.show_path.get():
            path = []
            for HH in range(-180, 181, 3):
                a2, z2 = altaz_from_hadec(HH, dec, lat)
                if a2 > -0.5:
                    path.append((SKY * dcos(a2) * dsin(z2),
                                 SKY * dcos(a2) * dcos(z2), SKY * dsin(a2)))
                elif path:
                    pt.polyline(path, fill="#4a4326")
                    path = []
            if path:
                pt.polyline(path, fill="#4a4326")
        if alt > -1:
            sun3 = (s[0] * SKY, s[1] * SKY, s[2] * SKY)
            pt.dot(sun3, 11, fill="#ffd257", outline="#8a6b12")
            pt.text((sun3[0], sun3[1], sun3[2] + 0.28),
                    _T("太阳 h=%.1f° Az=%.1f°") % (alt, az),
                    fill="#c8a44a", font=self.app.ui_font)

        pt.flush()

        # ---- 平面 HUD ----
        vaz, vel = self.cam.look_dir()
        state = ("拖动中…" if getattr(getattr(self, "mouse", None),
                                  "dragging", False) else "已固定")
        c.create_text(12, 14, anchor="w", font=self.app.ui_font_b, fill="#8fb3d0",
                      text=_T("视角 %s: 视线方位 %.1f°  俯仰 %+.1f°   (相机在方位 %.1f°, 仰角 %.1f°)   放大 %.1f×  视场 %.1f°")
                           % (state, vaz, vel, self.cam.az, self.cam.el,
                              self.cam.mag(), self.cam.fov))
        c.create_text(12, 32, anchor="w", font=self.app.ui_font, fill="#5f7c93",
                      text=_T("左键拖动转视角(松开即固定) · 右键拖动平移 · 滚轮/「放大」可放到 %.0f× (低纬度看时线要用) · 仰角限 %d°~%d°")
                           % (38.0 / Camera3D.FOV_MIN, Camera3D.EL_MIN,
                              Camera3D.EL_MAX))
        if alt <= 0:
            c.create_text(W / 2, 56, font=self.app.ui_font_b, fill="#c96f6f",
                          text="太阳在地平线以下 —— 无日影")
        elif getattr(self, "_no_style_side", False):
            c.create_text(W / 2, 56, font=self.app.ui_font_b, fill="#c98f3c",
                          text="此刻阳光照在晷面背后 (没有晷针的那一面) —— 晷面上无影")
        elif getattr(self, "_back_face", False):
            c.create_text(W / 2, 56, font=self.app.ui_font_b, fill="#c98f3c",
                          text=_T("此刻阳光照在晷面的另一面 (%s) —— 拖动视角转到那一面才看得到影子")
                               % face_name(n if sn > 0 else (-n[0], -n[1], -n[2])))
        elif abs(sn) <= 1e-4:
            c.create_text(W / 2, 56, font=self.app.ui_font_b, fill="#c98f3c",
                          text="阳光几乎平行于晷面 —— 影线消失 (赤道晷在二分点前后会这样)")
        if geo["tag"] == "h" and abs(lat) < 12:
            # 放在底下图例那一行之上, 免得两行叠在一起
            c.create_text(W / 2, H - 34, font=self.app.ui_font, fill="#c98f3c",
                          text=_T("低纬度(|φ|=%.1f°)水平晷时线极密集, 建议改用赤道晷") % abs(lat))

    # ---- 水平晷 ----
    def _draw_horizontal(self, W, H, lat, lha, alt, az, dec):
        c = self.canvas
        cx, cy = W / 2, H / 2 + 10
        R = min(W, H) * 0.40
        c.create_oval(cx - R, cy - R, cx + R, cy + R, outline="#3d4b57",
                      width=2, fill="#161c22")
        c.create_oval(cx - R * .93, cy - R * .93, cx + R * .93, cy + R * .93,
                      outline="#28323b")
        # 方位
        for lbl, ang in (("N", 0), ("E", 90), ("S", 180), ("W", 270)):
            x = cx + (R + 48) * dsin(ang)
            y = cy - (R + 48) * dcos(ang)
            c.create_text(x, y, text=lbl, fill="#7f9bb3",
                          font=self.app.ui_font_b)
        pn = (0.0, 0.0, 1.0)
        rv = (1.0, 0.0, 0.0)          # 画布 +x = 东
        uv = (0.0, 1.0, 0.0)          # 画布 -y = 北
        h0 = self.hour_limit(lat, dec)            # 只画当日有日照的时线
        if self.show_lines.get():
            placed, cands = [], []
            for Hh, kind_m, lbl, grp in getattr(self, "_marks", []):
                Hh = norm180(Hh)
                if abs(Hh) > h0:
                    continue
                d = style_shadow_on_plane(lat, Hh, pn, rv, uv)
                if d is None:
                    continue
                hot = (self._hot_mark is not None
                       and abs(norm180(self._hot_mark[0] - Hh)) < 1e-6
                       and self._hot_mark[1] == grp)
                self._mark_hits.append((cx + R * d[0], cy - R * d[1],
                                        Hh, kind_m, lbl, grp))
                if kind_m == "ke":
                    c.create_line(cx + R * 0.82 * d[0], cy - R * 0.82 * d[1],
                                  cx + R * d[0], cy - R * d[1],
                                  fill="#ffffff" if hot else MARK_COLOR[grp]["ke"],
                                  width=3 if hot else 1)
                    continue
                if kind_m != "label":
                    c.create_line(cx, cy, cx + R * d[0], cy - R * d[1],
                                  fill="#ffffff" if hot else MARK_COLOR[grp][kind_m],
                                  width=(MARK_WIDTH[kind_m] + 2) if hot
                                  else MARK_WIDTH[kind_m])
                if lbl:
                    rr = R + (24 if grp == "solar" else 44)
                    cands.append((Hh / 15.0 + 12.0, lbl, grp,
                                  cx + rr * d[0], cy - rr * d[1]))
            # 低纬度时线极密: 按 正午/6/18 优先, 重叠者跳过
            cands.sort(key=lambda t: (abs(t[0] - round(t[0])) > 1e-6,
                                      round(t[0]) % 6 != 0,
                                      round(t[0]) % 3 != 0, abs(t[0] - 12)))
            for hh, lbl, grp, lx, ly in cands:
                if any((lx - px) ** 2 + (ly - py) ** 2 < 15 ** 2 for px, py in placed):
                    continue
                placed.append((lx, ly))
                c.create_text(lx, ly, text=lbl, fill=MARK_COLOR[grp]["text"],
                              font=self.app.ui_font)
        # 晷针 (极轴在盘面的投影 = 子午线)
        g = polar_axis(lat)
        gx, gy = g[0], g[1]
        gl = math.hypot(gx, gy)
        if gl > 1e-9:
            c.create_line(cx, cy, cx + R * .9 * gx / gl, cy - R * .9 * gy / gl,
                          fill="#c9a227", width=4)
        c.create_oval(cx - 4, cy - 4, cx + 4, cy + 4, fill="#c9a227", outline="")
        # 影
        if alt > 0:
            d = style_shadow_on_plane(lat, lha, pn, rv, uv)
            if d:
                x2 = cx + R * .95 * d[0]
                y2 = cy - R * .95 * d[1]
                c.create_line(cx, cy, x2, y2, fill="#f2f2f2", width=7,
                              capstyle="round")
                c.create_line(cx, cy, x2, y2, fill="#8a8f94", width=3,
                              capstyle="round")
            if self.show_nodus.get():
                nod = nodus_shadow_horizontal(lat, alt, az, 0.55)
                if nod:
                    scale = R * 0.9
                    nx, ny = cx + nod[0] * scale, cy - nod[1] * scale
                    if abs(nx - cx) < R * 2 and abs(ny - cy) < R * 2:
                        c.create_line(cx, cy, nx, ny, fill="#4a5a68", dash=(3, 3))
                        c.create_oval(nx - 5, ny - 5, nx + 5, ny + 5,
                                      fill="#ffcf5c", outline="#5a4a10")
                        c.create_text(nx, ny - 14, text="珠影", fill="#c8a44a",
                                      font=self.app.ui_font)
            self._sun_marker(cx, cy, R, az, alt)
        else:
            c.create_text(cx, cy - R - 40, text="太阳在地平线以下 —— 无日影",
                          fill="#c96f6f", font=self.app.ui_font_b)
        if abs(lat) < 12:
            c.create_text(cx, cy + R + 34,
                          text=_T("低纬度(|φ|=%.1f°)水平晷时线极度密集, 建议改用赤道晷") % abs(lat),
                          fill="#c98f3c", font=self.app.ui_font)

    def _sun_marker(self, cx, cy, R, az, alt):
        """在盘外圈标出太阳方位, 亮度随高度。"""
        c = self.canvas
        rr = R + 46
        x = cx + rr * dsin(az)
        y = cy - rr * dcos(az)
        c.create_oval(x - 9, y - 9, x + 9, y + 9, fill="#ffd257", outline="#8a6b12")
        c.create_text(x, y + 18, text="h=%.1f°" % alt, fill="#c8a44a",
                      font=self.app.ui_font)

    # ---- 赤道晷 ----
    def _draw_equatorial(self, W, H, lat, lha, dec, alt):
        c = self.canvas
        cx, cy = W / 2, H / 2 + 10
        R = min(W, H) * 0.38
        # 受照面: 太阳在天赤道以北 (δ≥0) 照北面, 以南照南面。北半球北面朝上
        # (朝北天极), 南半球南面朝上 (朝南天极)。
        north_face = dec >= 0
        upper = (north_face == (lat >= 0))
        if LANG == "en":
            face = "%s (%s) face" % ("upper" if upper else "lower",
                                     "north" if north_face else "south")
        else:
            face = "%s(%s)面" % ("上" if upper else "下", "北" if north_face else "南")
        c.create_oval(cx - R, cy - R, cx + R, cy + R, outline="#3d4b57",
                      width=2, fill="#161c22")
        # 正对受照面看、正午影线朝下时: 照北面 (δ≥0) 上午影在右, 照南面上午影在左
        # —— 两面互为镜像, 与南北半球无关 (见自检 18)。
        sign = eq2d_sign(dec)
        h0 = self.hour_limit(lat, dec)
        if self.show_lines.get():
            for Hh, kind_m, lbl, grp in getattr(self, "_marks", []):
                Hh = norm180(Hh)
                if abs(Hh) > h0:
                    continue
                ang = sign * Hh
                frac = MARK_FRAC[kind_m]
                hot = (self._hot_mark is not None
                       and abs(norm180(self._hot_mark[0] - Hh)) < 1e-6
                       and self._hot_mark[1] == grp)
                self._mark_hits.append((cx - R * dsin(ang), cy + R * dcos(ang),
                                        Hh, kind_m, lbl, grp))
                if frac > 0:
                    c.create_line(cx - R * (1 - frac) * dsin(ang),
                                  cy + R * (1 - frac) * dcos(ang),
                                  cx - R * dsin(ang), cy + R * dcos(ang),
                                  fill="#ffffff" if hot else MARK_COLOR[grp][kind_m],
                                  width=(MARK_WIDTH[kind_m] + 2) if hot
                                  else MARK_WIDTH[kind_m])
                if lbl:
                    rr = R + (22 if grp == "solar" else 42)
                    c.create_text(cx - rr * dsin(ang), cy + rr * dcos(ang),
                                  text=lbl, fill=MARK_COLOR[grp]["text"],
                                  font=self.app.ui_font)
        c.create_oval(cx - 5, cy - 5, cx + 5, cy + 5, fill="#c9a227", outline="")
        c.create_text(cx, cy - R - 42,
                      text=_T("赤道晷 · 盘面倾角 = 余纬 %.2f°, 晷针垂直盘面指向天极")
                           % (90 - abs(lat)), fill="#7f9bb3", font=self.app.ui_font)
        c.create_text(cx, cy - R - 26,
                      text=_T("(正对受照的%s看: 正午影线朝下, 上午在%s侧, 下午在%s侧)")
                           % (face, _en("右", "right") if sign > 0 else _en("左", "left"),
                              _en("左", "left") if sign > 0 else _en("右", "right")),
                      fill="#5f7c93", font=self.app.ui_font)
        # 盘下的说明行: 让开盘下方的时刻数字 (真太阳时 R+22, 标准时 R+42),
        # 也不许压到最底下的图例; 实在放不下就挪到盘上方的标题之上
        lh = text_size(self.app.ui_font, "Ag")[1]
        y_txt = cy + R + (46 if self.scale_mode.get() == "solar" else 62)
        n_lines = 1 + (1 if abs(dec) < 0.6 else 0)
        if y_txt + (n_lines - 1) * 18 + lh / 2.0 > H - 26:
            y_txt = cy - R - 42 - 18 * n_lines
        if alt > 0:
            ang = sign * lha
            x2 = cx - R * .95 * dsin(ang)
            y2 = cy + R * .95 * dcos(ang)
            c.create_line(cx, cy, x2, y2, fill="#f2f2f2", width=7, capstyle="round")
            c.create_line(cx, cy, x2, y2, fill="#8a8f94", width=3, capstyle="round")
            c.create_text(cx, y_txt,
                          text=_T("此刻太阳赤纬 δ=%+.2f° → 光照 %s") % (dec, face),
                          fill="#8fa9bf", font=self.app.ui_font)
        else:
            c.create_text(cx, y_txt, text="太阳在地平线以下 —— 无日影",
                          fill="#c96f6f", font=self.app.ui_font_b)
        if abs(dec) < 0.6:
            c.create_text(cx, y_txt + 18,
                          text="接近二分点: 阳光近乎平行盘面, 影线消失",
                          fill="#c98f3c", font=self.app.ui_font)

    # ---- 垂直朝南晷 ----
    def _draw_vertical(self, W, H, lat, lha, alt, az):
        c = self.canvas
        cx = W / 2
        top = H * 0.16
        R = min(W, H) * 0.62
        x0, y0 = cx - R * .58, top
        x1, y1 = cx + R * .58, top + R * .86
        c.create_rectangle(x0, y0, x1, y1, outline="#3d4b57", width=2, fill="#161c22")
        north = lat >= 0
        # 墙面朝赤道: 北半球朝南 (人站在南边朝北看), 南半球朝北 (站在北边朝南看)。
        # 上午太阳在东, 影子落在墙的西侧: 朝北看时西在左, 朝南看时西在右。
        c.create_text(cx, top - 30,
                      text="垂直朝南晷面 (自南向北看墙面)" if north
                      else "垂直朝北晷面 (自北向南看墙面, 南半球)",
                      fill="#7f9bb3", font=self.app.ui_font_b)
        c.create_text(cx, top - 14,
                      text="左=西 (上午影)   右=东 (下午影)" if north
                      else "左=东 (下午影)   右=西 (上午影)",
                      fill="#5f7c93", font=self.app.ui_font)
        ox, oy = cx, top + 12                 # 晷针根部在墙面顶部中央
        geo = dial_geom3d("垂直", lat)
        pn = geo["n"]                         # 墙面外法线: 北半球指南, 南半球指北
        rv = geo["r"]                         # 面对墙时的「右」: 东 / 西
        uv = (0.0, 0.0, 1.0)                  # 上

        def clip(dx, dy):
            """把从 (ox,oy) 出发方向 (dx,dy) 的射线截到墙面矩形内。"""
            t = 1e9
            if dx > 1e-9:
                t = min(t, (x1 - ox) / dx)
            elif dx < -1e-9:
                t = min(t, (x0 - ox) / dx)
            if dy > 1e-9:
                t = min(t, (y1 - oy) / dy)
            elif dy < -1e-9:
                t = min(t, (y0 - oy) / dy)
            return ox + dx * t, oy + dy * t

        if self.show_lines.get():
            for Hh, kind_m, lbl, grp in getattr(self, "_marks", []):
                Hh = norm180(Hh)
                d = style_shadow_on_plane(lat, Hh, pn, rv, uv)
                if d is None or d[1] > -0.02:     # 只画落在晷针根部下方的时线
                    continue
                x2, y2 = clip(d[0], -d[1])
                hot = (self._hot_mark is not None
                       and abs(norm180(self._hot_mark[0] - Hh)) < 1e-6
                       and self._hot_mark[1] == grp)
                self._mark_hits.append((x2, y2, Hh, kind_m, lbl, grp))
                if MARK_FRAC[kind_m] > 0:
                    f = MARK_FRAC[kind_m]
                    c.create_line(ox + (x2 - ox) * (1 - f), oy + (y2 - oy) * (1 - f),
                                  x2, y2, fill="#ffffff" if hot else MARK_COLOR[grp][kind_m],
                                  width=(MARK_WIDTH[kind_m] + 2) if hot
                                  else MARK_WIDTH[kind_m])
                if lbl:
                    ly = min(y2 + (10 if grp == "solar" else 22), y1 - 6)
                    c.create_text(x2, ly, text=lbl, fill=MARK_COLOR[grp]["text"],
                                  font=self.app.ui_font)
        c.create_oval(ox - 5, oy - 5, ox + 5, oy + 5, fill="#c9a227", outline="")
        sv = _enu_from_altaz(alt, az)
        lit = _dot(sv, pn) > 0 and alt > 0                 # 太阳在墙面那一侧
        if alt > 0 and lit:
            d = style_shadow_on_plane(lat, lha, pn, rv, uv)
            if d and d[1] <= 0:
                x2, y2 = clip(d[0], -d[1])
                c.create_line(ox, oy, x2, y2, fill="#f2f2f2", width=7, capstyle="round")
                c.create_line(ox, oy, x2, y2, fill="#8a8f94", width=3, capstyle="round")
        else:
            c.create_text(cx, y1 + 26,
                          text="此刻阳光照不到朝南墙面 (太阳在北侧或已落下)" if north
                          else "此刻阳光照不到朝北墙面 (太阳在南侧或已落下)",
                          fill="#c96f6f", font=self.app.ui_font_b)
        c.create_text(cx, y1 + 50,
                      text=_T("晷针与墙面夹角 = %.2f° (指向天极)") % (90 - abs(lat)),
                      fill="#7f9bb3", font=self.app.ui_font)

    # -- 数据面板 -----------------------------------------------------------
    def _update_info(self, lat, lon, tz, loc_t, utc, sun, lha, alt_geo,
                     alt_app, az, refr):
        # 真太阳时 / 平太阳时 / 均时差
        lat_app_hours = (norm180(sun.gha + lon)) / 15.0 + 12.0      # 地方真太阳时
        ut_hours = utc.hour + utc.minute / 60.0 + utc.second / 3600.0 \
            + utc.microsecond / 3.6e9
        eot_min = norm180((sun.gha + 180.0) - ut_hours * 15.0) * 4.0
        lmt_hours = ut_hours + lon / 15.0                            # 地方平太阳时
        lon_corr_min = (lon - tz * 15.0) * 4.0
        key = (loc_t.date(), round(lat, 4), round(lon, 4), tz)
        if key not in self._events_cache:
            self._events_cache.clear()
            self._events_cache[key] = solar_events(loc_t.date(), lat, lon, tz)
        rise, noon, sett, polar = self._events_cache[key]

        shadow = ("%.3f" % (1.0 / dtan(alt_app))) if alt_app > 0.5 else "—"
        L = []
        A = L.append
        A("【时间】")
        A(_T("  当地标准时  %s  (UTC%+.2f)") % (loc_t.strftime("%Y-%m-%d %H:%M:%S"), tz))
        A(_T("  世界时 UTC  %s") % utc.strftime("%Y-%m-%d %H:%M:%S"))
        A(_T("  儒略日 JD   %.6f") % julian_day(utc))
        A("  ΔT ≈ %.1f s" % delta_t_seconds(utc))
        A("")
        A("【日晷读数】")
        A(_T("  地方真太阳时(晷面读数)  %s") % hm_from_hours(lat_app_hours))
        A(_T("  地方平太阳时            %s") % hm_from_hours(lmt_hours))
        A(_T("  均时差 EoT  = %+.2f 分") % eot_min)
        A(_T("  经度改正    = %+.2f 分  (λ−15°×tz)") % lon_corr_min)
        A(_T("  晷面读数 − 钟表 = %+.2f 分   ← 晷面永远比钟表%s这么多")
          % (eot_min + lon_corr_min, "快" if (eot_min + lon_corr_min) > 0 else "慢"))
        A("")
        # ---- 时辰 ----
        scm = self.sc_mode.get()
        idx, nm, ke = shichen_of(lat_app_hours, scm)
        A(_T("【时辰】起算方式: %s")
          % ("中天起午 (太阳中天=午时之始, 底天=子时之始/日始)" if scm == "midculm"
             else "传统 (午时含中天, 子时跨半夜)"))
        A(_T("  此刻 %s时 第 %d 刻   (真太阳时 %s)") % (nm, ke, hm_from_hours(lat_app_hours)))
        A("  今日 12 时辰 ↔ 当地标准时 (钟表) 对照:")
        off = eot_min + lon_corr_min                      # 真太阳时 = 钟表 + off/60
        for name, s0, s1 in shichen_table(scm):
            c0 = (s0 - off / 60.0) % 24.0
            c1 = (s1 - off / 60.0) % 24.0
            cur = " ←现在" if name[0] == nm else ""
            A(_T("    %s  真太阳时 %02d:00–%02d:00   钟表 %s–%s%s")
              % (name, int(s0), int(s1), hm_from_hours(c0)[:5],
                 hm_from_hours(c1)[:5], cur))
        A("")
        A("【太阳位置】")
        A(_T("  视赤经 α = %s") % hm_from_hours(sun.ra / 15.0))
        A(_T("  视赤纬 δ = %s") % deg_dm(sun.dec, "N", "S"))
        A(_T("  格林时角 GHA = %.4f°") % sun.gha)
        A(_T("  地方时角 LHA = %+.4f°  (%+.3f h)") % (lha, lha / 15.0))
        A(_T("  真高度 h  = %+.4f°") % alt_geo)
        A(_T("  视高度 h′ = %+.4f°   (蒙气差 %.2f′)") % (alt_app, refr))
        A(_T("  方位角 Az = %.3f°  (北起顺时针)") % az)
        A(_T("  视半径 SD = %.2f′   日地距 %.6f AU") % (sun.sd_arcmin,
                                                  sun.dist_km / AU_KM))
        A(_T("  杆影长/杆高 = %s") % shadow)
        A("")
        A("【当日太阳时刻 · 当地标准时】")
        if polar:
            A("  %s" % polar)
        A(_T("  日出 %s   中天 %s   日落 %s") % (fmt_hm(rise), fmt_hm(noon), fmt_hm(sett)))
        if rise and sett:
            A(_T("  昼长 %.3f 小时") % ((sett - rise).total_seconds() / 3600.0))
        if noon:
            nalt, _ = altaz_from_hadec(0.0, EPH.get("太阳", noon - dt.timedelta(hours=tz)).dec, lat)
            A(_T("  中天高度 %.3f°") % nalt)
        A("")
        A("【晷面与晷针实际尺寸】")
        try:
            r_cm = float(self.size_var.get())
        except ValueError:
            r_cm = 30.0
        m = dial_metrics(self.dial_var.get(), lat, alt_app, az, r_cm)
        rec, why = recommend_dial(lat)
        A(_T("  晷面半径 %.1f cm      推荐晷面: %s") % (m["plate_r"], rec))
        A("    (%s)" % why)
        A(_T("  晷针(style)长 %.2f cm   晷针与晷面夹角 %.2f°")
          % (m["style_len"], m["style_angle"] if m["kind"] != "h" else abs(lat)))
        if m["kind"] == "h":
            A(_T("  三角晷针: 底边 %.2f cm   尖端高 %.2f cm   仰角 = |φ| = %.3f°")
              % (m["base_len"], m["tip_height"], abs(lat)))
        else:
            A(_T("  晷针垂直晷面伸出 %.2f cm") % m["tip_height"])
        if m["shadow_len"] is not None:
            A(_T("  此刻晷针影长 %.2f cm   影长/晷针高 = %.3f")
              % (m["shadow_len"],
                 m["shadow_len"] / max(1e-6, m["tip_height"])))
            if m.get("nodus_shadow") is not None:
                A(_T("  珠(nodus)高 %.2f cm  珠影长 %.2f cm")
                  % (m.get("nodus_height", 0.0), m["nodus_shadow"]))
        else:
            A("  此刻晷面无影 (太阳在地平下, 或阳光照在另一面)")
        A("")
        A("【晷面公式】")
        A(_T("  晷针仰角 = |φ| = %.4f°") % abs(lat))
        A("  水平晷时线: tanθ = sinφ·tanH")
        A(_T("  %s: tanθ = cosφ·tanH") % vertical_dial_name(lat))
        A("  赤道晷时线: θ = H (每小时 15° 均匀)")
        A("")
        A(_T("【星历】%s") % EPH.status)

        self.info.configure(state="normal")
        self.info.delete("1.0", "end")
        self.info.insert("1.0", "\n".join(L))
        self.info.configure(state="disabled")


# ===========================================================================
#  六分仪: 观测改正与截距法定位
# ===========================================================================
def semidiameter_augmented(sd_arcmin, hp_arcmin, alt_deg):
    """半径增大改正 (月亮显著): SD_topo ≈ SD·(1 + sin h · sin HP)。"""
    return sd_arcmin * (1.0 + dsin(alt_deg) * math.sin(hp_arcmin / 60.0 * D2R))


def required_reading(pos, lat, lon, utc, limb, height_eye, index_err,
                     pressure=1010.0, temp_c=10.0):
    """
    正演: 在真实位置、该时刻, 六分仪应当读到多少。
    做法是把标准改正链 (Hs→Ha→Ho) 严格反解, 因此与 reduce_sight() 精确互逆:
        Ho = Ha − R(Ha) + s·SD(Ha) + HP·cos(Ha)        (s: 下缘+1 上缘−1 中心0)
        Hs = Ha + dip + IE
    其中 Ho 即地心真高度, 与由 GHA/Dec 算出的 Hc 属同一定义。
    返回 dict。
    """
    topo = topocentric_alt(pos, lat, lon, utc, height_eye, pressure, temp_c)
    alt_geo = topo["alt_geo"]                    # 地心真高度 = 目标 Ho
    dipv = dip_arcmin(height_eye)

    def ha_for(sign):
        ha = alt_geo
        for _ in range(10):
            sd = semidiameter_augmented(pos.sd_arcmin, pos.hp_arcmin, ha)
            r = refraction_bennett(ha, pressure, temp_c)
            par = pos.hp_arcmin * dcos(ha)
            ha_new = alt_geo + (r - sign * sd - par) / 60.0
            if abs(ha_new - ha) < 1e-9:
                ha = ha_new
                break
            ha = ha_new
        return ha

    off = (dipv + index_err) / 60.0
    ha_c, ha_l, ha_u = ha_for(0.0), ha_for(1.0), ha_for(-1.0)
    sign = {"下边缘": 1.0, "上边缘": -1.0}.get(limb, 0.0)
    ha = {1.0: ha_l, -1.0: ha_u}.get(sign, ha_c)
    sd_c = semidiameter_augmented(pos.sd_arcmin, pos.hp_arcmin, ha_c)
    return {"hs": ha + off, "hs_center": ha_c + off, "hs_lower": ha_l + off,
            "hs_upper": ha_u + off, "sd": sd_c, "dip": dipv, "topo": topo,
            "ha": ha}


def reduce_sight(pos, hs_deg, limb, height_eye, index_err,
                 pressure=1010.0, temp_c=10.0):
    """
    反演(标准航海改正): Hs -> Ho (真高度, 地心, 相对真地平)。
    返回 (Ho, 各项改正 dict)。
    """
    dipv = dip_arcmin(height_eye)
    ha = hs_deg - index_err / 60.0 - dipv / 60.0      # 视高度
    refr = refraction_bennett(ha, pressure, temp_c)
    ho = ha - refr / 60.0
    sd = semidiameter_augmented(pos.sd_arcmin, pos.hp_arcmin, ha)
    if limb == "下边缘":
        ho += sd / 60.0
    elif limb == "上边缘":
        ho -= sd / 60.0
    par = pos.hp_arcmin * dcos(ha)                    # 高度视差
    ho += par / 60.0
    return ho, {"dip": dipv, "IE": index_err, "refr": refr, "SD": sd,
                "PA": par, "Ha": ha}


def compute_fix(obs_list, lat0, lon0, iterations=6):
    """
    Marcq St Hilaire 截距法 + 最小二乘。
    obs_list: [{'utc','body','ho','pos'}...]
    返回 (lat, lon, info dict)
    """
    lat, lon = lat0, lon0
    info = {"rows": [], "rms": None, "n": len(obs_list), "warn": ""}
    if len(obs_list) < 2:
        info["warn"] = "至少需要 2 个不同方位的天体(或同一天体不同时刻)才能定出船位。"
        return lat, lon, info
    for it in range(iterations):
        A11 = A12 = A22 = B1 = B2 = 0.0
        rows = []
        for o in obs_list:
            pos = o["pos"]
            lha = norm360(pos.gha + lon)
            hc, zn = altaz_from_hadec(lha, pos.dec, lat)
            a = (o["ho"] - hc) * 60.0                 # 截距, 海里
            c, s = dcos(zn), dsin(zn)
            A11 += c * c
            A12 += c * s
            A22 += s * s
            B1 += c * a
            B2 += s * a
            rows.append((o, hc, zn, a))
        det = A11 * A22 - A12 * A12
        if abs(det) < 1e-9:
            info["warn"] = "各天体方位太接近, 位置线近乎平行, 无法定位。"
            return lat, lon, info
        dlat = (B1 * A22 - B2 * A12) / det            # 海里
        ddep = (A11 * B2 - A12 * B1) / det            # 海里 (东西向)
        lat += dlat / 60.0
        lat = max(-89.9, min(89.9, lat))
        cl = dcos(lat)
        if abs(cl) < 1e-6:
            cl = 1e-6
        lon = norm180(lon + (ddep / 60.0) / cl)
        if abs(dlat) < 1e-6 and abs(ddep) < 1e-6:
            break
    # 残差
    res = []
    rows = []
    for o in obs_list:
        pos = o["pos"]
        lha = norm360(pos.gha + lon)
        hc, zn = altaz_from_hadec(lha, pos.dec, lat)
        a = (o["ho"] - hc) * 60.0
        rows.append((o, hc, zn, a))
        res.append(a)
    info["rows"] = rows
    info["rms"] = math.sqrt(sum(r * r for r in res) / len(res))
    return lat, lon, info




# ===========================================================================
#  遮光镜 (shades) 与目镜视场模型
# ===========================================================================
# 真实六分仪: 指标镜前 3~4 片深浅不同的滤光片, 地平镜前 2~3 片, 逐片翻下叠加。
# 以光学密度 D 描述 (透过率 T = 10^-D); 叠片时 D 相加。
INDEX_SHADES = [("#1 浅", 0.55, "#8a7340"),
                ("#2 中", 1.15, "#7a4526"),
                ("#3 深", 1.75, "#4d2418"),
                ("#4 最深", 2.30, "#2e1411")]
HORIZON_SHADES = [("H1 浅", 0.45, "#4a6f5c"),
                  ("H2 中", 0.95, "#2c4a3c"),
                  ("H3 深", 1.50, "#1b3128")]

# 各天体安全/清晰观测所需的大致密度
BODY_NEED_D = {"太阳": 3.05, "月亮": 0.30}


def shade_density(kind, n):
    tbl = INDEX_SHADES if kind == "index" else HORIZON_SHADES
    return sum(s[1] for s in tbl[:max(0, min(len(tbl), n))])


def shade_advice(body, alt_app):
    """给定天体与视高度, 建议翻下几片指标遮光片。"""
    need = BODY_NEED_D.get(body, 0.0)
    if body == "太阳":
        # 低空太阳被大气消光, 需要的密度下降 (地平线附近可只用一片)
        need -= max(0.0, (12.0 - max(alt_app, 0.0))) * 0.11
    best, bd = 0, 1e9
    for n in range(len(INDEX_SHADES) + 1):
        d = abs(shade_density("index", n) - need)
        if d < bd:
            bd, best = d, n
    return best, need


def shade_state(body, n_index, n_hor, alt_app):
    """返回遮光片状态: 密度、明暗判定、天体呈色。"""
    Di = shade_density("index", n_index)
    Dh = shade_density("horizon", n_hor)
    _, need = shade_advice(body, alt_app)
    excess = Di - need                       # >0 太暗, <0 太亮
    if body == "太阳" and excess < -1.30:
        level = "danger"                     # 未加/不足遮光片直视太阳
    elif excess < -0.45:
        level = "bright"
    elif excess > 1.05:
        level = "dark"
    else:
        level = "ok"
    return {"Di": Di, "Dh": Dh, "need": need, "excess": excess, "level": level,
            "n_index": n_index, "n_hor": n_hor}


def _hex_rgb(h):
    return (int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16))


def _rgb_hex(t):
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(round(v)))) for v in t)


def mix_color(c1, c2, f):
    a, b = _hex_rgb(c1), _hex_rgb(c2)
    return _rgb_hex([a[i] + (b[i] - a[i]) * f for i in range(3)])


def dim_color(c, f):
    """f<1 变暗; 透过滤光片后的景物亮度。"""
    return _rgb_hex([v * f for v in _hex_rgb(c)])


def shaded_scene_color(base, D, tint=None):
    """景物经过密度 D 的滤光片后的呈色 (含滤光片本身的色调)。"""
    t = 10.0 ** (-0.55 * max(0.0, D))        # 视觉上比线性透过率亮 (眼睛适应)
    out = dim_color(base, max(0.06, t))
    if tint and D > 0.01:
        out = mix_color(out, tint, min(0.55, 0.28 * D))
    return out


# 太阳盘面透过不同密度滤光片后的颜色 (与真实目镜所见一致: 白 → 黄 → 橙 → 红)
_SUN_RAMP = [(0.0, "#fffdf2"), (0.6, "#ffef9a"), (1.2, "#ffcf5c"),
             (1.9, "#ff9a3c"), (2.6, "#ef5f2a"), (3.2, "#d63a24"),
             (4.0, "#8e1f16"), (5.5, "#3d0d0a")]


def sun_disc_color(D):
    for i in range(len(_SUN_RAMP) - 1):
        d0, c0 = _SUN_RAMP[i]
        d1, c1 = _SUN_RAMP[i + 1]
        if D <= d1:
            f = 0.0 if d1 <= d0 else (max(D, d0) - d0) / (d1 - d0)
            return mix_color(c0, c1, f)
    return _SUN_RAMP[-1][1]
# ===========================================================================
#  六分仪页签
# ===========================================================================
class SextantTab(ttk.Frame):
    LIMBS = ["下边缘", "上边缘", "中心"]
    STEPS = ["① 放下遮光镜", "② 望远镜对平海平线", "③ 松开夹钳 · 转臂把天体带下来",
             "④ 夹紧 · 微动螺旋切于海平线", "⑤ 左右摆动取最低点", "⑥ 读数并记录"]

    def __init__(self, master, app):
        super().__init__(master, padding=6)
        self.app = app
        self.f_small = _pick_font(app.root, CJK_FONTS, 8)     # 画布上挤不下时退一号
        self.obs = []
        self.last_fix = None
        self.clock = TimeEngine()
        self._swing_t0 = None
        self._auto = None            # 自动演示状态
        self._drag_mode = None       # 'arm' / 'drum'
        self._arm_geom = None        # 弧的屏幕几何 (供拖动用)
        self._clamp_hit = None       # 夹钳的点击区
        self._press_key = None       # 正被按住的控件 (按下要变色)
        self._repeat_job = None
        self._shade_hits = []        # 遮光片的点击区
        self._hint = None            # (文字, 颜色, 到期时间)
        self._build()
        self.after(200, self._tick)

    # ==================================================================
    #  界面
    # ==================================================================
    def _build(self):
        scroll = VScrollFrame(self, width=460)
        scroll.pack(side="right", fill="y")
        right = scroll.body
        left = ttk.Frame(self)
        left.pack(side="left", fill="both", expand=True)

        fo = ttk.LabelFrame(left, text=" 计算结果 ", padding=4)
        fo.pack(fill="x", side="bottom")
        self.out = tk.Text(fo, height=8, bg="#0d1117", fg="#d8e0e8",
                           font=self.app.mono_font, relief="flat", wrap="word")
        osb = ttk.Scrollbar(fo, orient="vertical", command=self.out.yview)
        osb.pack(side="right", fill="y")
        self.out.configure(yscrollcommand=osb.set)
        self.out.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(left, bg="#0b0f13", highlightthickness=0,
                                width=520, height=520)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.redraw())
        self.canvas.bind("<ButtonPress-1>", self._press)
        self.canvas.bind("<B1-Motion>", self._motion)
        self.canvas.bind("<ButtonRelease-1>", self._release)
        self.canvas.bind("<Button-4>", lambda e: self._wheel(1))
        self.canvas.bind("<Button-5>", lambda e: self._wheel(-1))
        self.canvas.bind("<MouseWheel>",
                         lambda e: self._wheel(1 if e.delta > 0 else -1))
        self.canvas.configure(takefocus=1)
        self.canvas.bind("<Enter>", lambda e: self.canvas.focus_set())
        self.canvas.bind("<Left>", lambda e: self._key_adj(-1, e))
        self.canvas.bind("<Right>", lambda e: self._key_adj(+1, e))
        self.canvas.bind("<Down>", lambda e: self._key_adj(-60, e))
        self.canvas.bind("<Up>", lambda e: self._key_adj(+60, e))

        # ---- 真实位置 ----
        f1 = ttk.LabelFrame(right, text=" 观测者真实位置 (模拟视场用) ", padding=6)
        f1.pack(fill="x", pady=(0, 5))
        self.city_var = tk.StringVar(value=CITIES[DEFAULT_CITY][0])
        cb = ttk.Combobox(f1, textvariable=self.city_var, width=28, state="readonly",
                          values=[c[0] for c in CITIES] + ["自定义 Custom"])
        cb.grid(row=0, column=0, columnspan=4, sticky="we")
        cb.bind("<<ComboboxSelected>>", self._on_city)
        self.tlat = tk.StringVar(value="%.4f" % CITIES[DEFAULT_CITY][1])
        self.tlon = tk.StringVar(value="%.4f" % CITIES[DEFAULT_CITY][2])
        ttk.Label(f1, text="纬度 φ").grid(row=1, column=0, sticky="w")
        ttk.Entry(f1, textvariable=self.tlat, width=11).grid(row=1, column=1)
        ttk.Label(f1, text="经度 λ").grid(row=1, column=2, sticky="w", padx=(6, 0))
        ttk.Entry(f1, textvariable=self.tlon, width=11).grid(row=1, column=3)
        self.eye = tk.StringVar(value="2.5")
        self.ie = tk.StringVar(value="0.0")
        self.press = tk.StringVar(value="1010")
        self.temp = tk.StringVar(value="28")
        ttk.Label(f1, text="眼高 m").grid(row=2, column=0, sticky="w")
        ttk.Entry(f1, textvariable=self.eye, width=11).grid(row=2, column=1)
        ttk.Label(f1, text="指标差 ′").grid(row=2, column=2, sticky="w", padx=(6, 0))
        ttk.Entry(f1, textvariable=self.ie, width=11).grid(row=2, column=3)
        ttk.Label(f1, text="气压 hPa").grid(row=3, column=0, sticky="w")
        ttk.Entry(f1, textvariable=self.press, width=11).grid(row=3, column=1)
        ttk.Label(f1, text="气温 ℃").grid(row=3, column=2, sticky="w", padx=(6, 0))
        ttk.Entry(f1, textvariable=self.temp, width=11).grid(row=3, column=3)

        # ---- 观测 ----
        f2 = ttk.LabelFrame(right, text=" 观测 ", padding=6)
        f2.pack(fill="x", pady=(0, 5))
        self.body_var = tk.StringVar(value="太阳")
        ttk.Label(f2, text="天体").grid(row=0, column=0, sticky="w")
        self.body_cb = ttk.Combobox(f2, textvariable=self.body_var, width=18,
                                    state="readonly",
                                    values=NAV_BODIES + SEXTANT_STARS)
        self.body_cb.grid(row=0, column=1, columnspan=3, sticky="we")
        self.body_cb.bind("<<ComboboxSelected>>", self._on_body)
        self.limb_var = tk.StringVar(value="下边缘")
        ttk.Label(f2, text="切点").grid(row=1, column=0, sticky="w")
        self.limb_cb = ttk.Combobox(f2, textvariable=self.limb_var,
                                    values=self.LIMBS, width=8, state="readonly")
        self.limb_cb.grid(row=1, column=1, sticky="w")
        self.swing = tk.BooleanVar(value=False)
        ttk.Checkbutton(f2, text="摆动演示 (swing)", variable=self.swing).grid(
            row=1, column=2, columnspan=2, sticky="w")
        tr = ttk.Frame(f2)
        tr.grid(row=2, column=0, columnspan=4, sticky="we", pady=(3, 0))
        self.pause_btn = ttk.Button(tr, text="⏸ 暂停", width=8,
                                    command=self._toggle_pause)
        self.pause_btn.pack(side="left")
        self.speed_var = tk.StringVar(value=SPEEDS[0][0])
        cbs = ttk.Combobox(tr, textvariable=self.speed_var, width=8, state="readonly",
                           values=[sp[0] for sp in SPEEDS])
        cbs.pack(side="left", padx=(4, 0))
        cbs.bind("<<ComboboxSelected>>", self._on_speed)
        ttk.Button(tr, text="回到现在", width=8,
                   command=self._go_now).pack(side="left", padx=(4, 0))
        self.utc_var = tk.StringVar(
            value=utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        ttk.Label(f2, text="观测时刻 UTC").grid(row=3, column=0, sticky="w")
        self.utc_ent = ttk.Entry(f2, textvariable=self.utc_var, width=20)
        self.utc_ent.grid(row=3, column=1, columnspan=2, sticky="we")
        ttk.Button(f2, text="跳转", width=5,
                   command=self._jump_to).grid(row=3, column=3, sticky="we")
        nb = ttk.Frame(f2)
        nb.grid(row=4, column=0, columnspan=4, sticky="we")
        for txt, d in (("−1时", -60), ("−10分", -10), ("−1分", -1),
                       ("+1分", 1), ("+10分", 10), ("+1时", 60)):
            ttk.Button(nb, text=txt, width=6,
                       command=lambda dd=d: self._nudge(dd)).pack(side="left")
        f2.columnconfigure(2, weight=1)

        # ---- 遮光镜 / 夹钳 / 目镜 ----
        f2b = ttk.LabelFrame(right, text=" 遮光镜 Shades · 夹钳 Clamp · 目镜 ",
                             padding=6)
        f2b.pack(fill="x", pady=(0, 5))
        self.n_index = tk.IntVar(value=3)
        self.n_hor = tk.IntVar(value=0)
        ttk.Label(f2b, text="指标镜滤片").grid(row=0, column=0, sticky="w")
        srow = ttk.Frame(f2b)
        srow.grid(row=0, column=1, columnspan=3, sticky="w")
        self._ish_btns = []
        for i, (nm, dv, col) in enumerate(INDEX_SHADES):
            b = ttk.Checkbutton(srow, text=nm,
                                command=lambda k=i: self._toggle_shade("index", k))
            b.state(["!alternate"])
            b.grid(row=0, column=i, padx=(0, 4))
            self._ish_btns.append(b)
        ttk.Label(f2b, text="地平镜滤片").grid(row=1, column=0, sticky="w")
        hrow = ttk.Frame(f2b)
        hrow.grid(row=1, column=1, columnspan=3, sticky="w")
        self._hsh_btns = []
        for i, (nm, dv, col) in enumerate(HORIZON_SHADES):
            b = ttk.Checkbutton(hrow, text=nm,
                                command=lambda k=i: self._toggle_shade("hor", k))
            b.state(["!alternate"])
            b.grid(row=0, column=i, padx=(0, 4))
            self._hsh_btns.append(b)
        sb = ttk.Frame(f2b)
        sb.grid(row=2, column=0, columnspan=4, sticky="we", pady=(3, 0))
        ttk.Button(sb, text="建议滤片", width=9,
                   command=self.apply_advised_shades).pack(side="left")
        ttk.Button(sb, text="全部翻起", width=9,
                   command=lambda: self.set_shades(0, 0)).pack(side="left", padx=3)
        self.shade_lbl = ttk.Label(sb, text="", foreground="#c9a227")
        self.shade_lbl.pack(side="left", padx=(6, 0))

        cl = ttk.Frame(f2b)
        cl.grid(row=3, column=0, columnspan=4, sticky="we", pady=(4, 0))
        self.clamped = tk.BooleanVar(value=True)
        self.clamp_btn = ttk.Button(cl, text="🔒 夹钳: 夹紧 (点此松开)", width=24,
                                    command=self.toggle_clamp)
        self.clamp_btn.pack(side="left")
        self.strict_clamp = tk.BooleanVar(value=True)
        ttk.Checkbutton(cl, text="严格模拟", variable=self.strict_clamp,
                        command=self.redraw).pack(side="left", padx=(4, 0))
        ttk.Label(f2b, foreground="#5f7c93", justify="left",
                  text="夹紧时只能用微动螺旋(细调); 松开后指标臂可沿弧自由滑动(粗调)。\n"
                       "画布上直接点遮光片或夹钳也可以操作。").grid(
            row=4, column=0, columnspan=4, sticky="w", pady=(3, 0))

        ev = ttk.Frame(f2b)
        ev.grid(row=5, column=0, columnspan=4, sticky="we", pady=(4, 0))
        self.real_view = tk.BooleanVar(value=True)
        ttk.Checkbutton(ev, text="真实目镜视场", variable=self.real_view,
                        command=self.redraw).pack(side="left")
        self.hmirror = tk.StringVar(value="split")
        ttk.Label(ev, text="地平镜").pack(side="left", padx=(6, 2))
        cbm = ttk.Combobox(ev, textvariable=self.hmirror, width=11, state="readonly",
                           values=["split", "whole"])
        cbm.pack(side="left")
        cbm.bind("<<ComboboxSelected>>", lambda e: self.redraw())
        self.mirror_left = tk.BooleanVar(value=False)
        ttk.Checkbutton(ev, text="镜面在左(反装)", variable=self.mirror_left,
                        command=self.redraw).pack(side="left", padx=(4, 0))
        f2b.columnconfigure(3, weight=1)

        # ---- 读数 ----
        f3 = ttk.LabelFrame(right, text=" 六分仪读数 Hs (也可直接拖动左边的指标臂) ",
                            padding=6)
        f3.pack(fill="x", pady=(0, 5))
        self.deg_var = tk.IntVar(value=30)
        self.min_var = tk.DoubleVar(value=0.0)
        ttk.Label(f3, text="度").grid(row=0, column=0)
        ttk.Spinbox(f3, from_=0, to=120, textvariable=self.deg_var, width=6,
                    command=self.redraw).grid(row=0, column=1)
        ttk.Label(f3, text="分").grid(row=0, column=2)
        ttk.Spinbox(f3, from_=0.0, to=59.9, increment=0.1, format="%.1f",
                    textvariable=self.min_var, width=7,
                    command=self.redraw).grid(row=0, column=3)
        self.deg_var.trace_add("write", lambda *a: self.redraw())
        self.min_var.trace_add("write", lambda *a: self.redraw())
        self.coarse = ttk.Scale(f3, from_=0, to=90, orient="horizontal",
                                command=self._on_coarse)
        self.coarse.grid(row=1, column=0, columnspan=4, sticky="we", pady=3)
        self.coarse.set(30)
        self.fine = ttk.Scale(f3, from_=0, to=60, orient="horizontal",
                              command=self._on_fine)
        self.fine.grid(row=2, column=0, columnspan=4, sticky="we")
        ttk.Label(f3, text="上=度 粗调  下=分 微动螺旋 (画布上滚轮 = 0.1′)",
                  foreground="#7f9bb3").grid(row=3, column=0, columnspan=4, sticky="w")
        f3.columnconfigure(3, weight=1)

        bb = ttk.Frame(right)
        bb.pack(fill="x", pady=(0, 5))
        ttk.Button(bb, text="自动测量演示", command=self.auto_demo).pack(side="left")
        ttk.Button(bb, text="立即对准", command=self.auto_align).pack(side="left", padx=3)
        self.noise_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(bb, text="随机误差 σ=", variable=self.noise_var).pack(side="left")
        self.sigma = tk.StringVar(value="0.3")
        ttk.Entry(bb, textvariable=self.sigma, width=4).pack(side="left")
        ttk.Label(bb, text="′").pack(side="left")
        ttk.Button(bb, text="记录本次观测", command=self.record).pack(side="right")

        # ---- 三个页: 观测记录 / 航海历 / 归算 ----
        nbk = ttk.Notebook(right)
        self.nbk = nbk
        nbk.pack(fill="both", expand=True)
        p_obs = ttk.Frame(nbk, padding=4)
        p_alm = ttk.Frame(nbk, padding=4)
        p_fix = ttk.Frame(nbk, padding=4)
        nbk.add(p_obs, text=" 观测记录 ")
        nbk.add(p_alm, text=" 航海历 ")
        nbk.add(p_fix, text=" 定位 ")

        cols = ("body", "utc", "hs", "ho", "zn", "a")
        self.tree = ttk.Treeview(p_obs, columns=cols, show="headings", height=7)
        for c_, t_, w_ in (("body", "天体", 60), ("utc", "UTC", 120), ("hs", "Hs", 74),
                           ("ho", "Ho", 74), ("zn", "Zn", 48), ("a", "截距′", 52)):
            self.tree.heading(c_, text=t_)
            self.tree.column(c_, width=w_, anchor="center")
        self.tree.pack(fill="x")
        tree_hscroll(self.tree, p_obs)
        tb = ttk.Frame(p_obs)
        tb.pack(fill="x", pady=(3, 0))
        ttk.Button(tb, text="一键多星演练", command=self.demo_three).pack(side="left")
        ttk.Button(tb, text="删除选中", command=self.del_sel).pack(side="left", padx=3)
        ttk.Button(tb, text="清空", command=self.clear_obs).pack(side="left")

        top = ttk.Frame(p_alm)
        top.pack(fill="x")
        ttk.Button(top, text="刷新", width=6,
                   command=self.refresh_almanac).pack(side="right")
        ttk.Button(top, text="大窗口", width=8,
                   command=self.open_almanac).pack(side="right", padx=3)
        self.alm_hdr = ttk.Label(top, text="", foreground="#e8c56a",
                                 font=self.app.ui_font_b, justify="left")
        self.alm_hdr.pack(side="left", fill="x", expand=True)
        self.alm = tk.Text(p_alm, height=14, bg="#0d1117", fg="#d8e0e8",
                           font=self.app.mono_font, relief="flat", wrap="none")
        ay = ttk.Scrollbar(p_alm, orient="vertical", command=self.alm.yview)
        ax = ttk.Scrollbar(p_alm, orient="horizontal", command=self.alm.xview)
        self.alm.configure(yscrollcommand=ay.set, xscrollcommand=ax.set)
        ay.pack(side="right", fill="y")
        ax.pack(side="bottom", fill="x")
        self.alm.pack(side="left", fill="both", expand=True)
        self.alm.insert("1.0", "按「刷新」生成本日航海历。\n")
        self.alm.configure(state="disabled")

        self.dlat = tk.StringVar(value="0.0")
        self.dlon = tk.StringVar(value="100.0")
        ttk.Label(p_fix, text="推测位置 DR  φ").grid(row=0, column=0, sticky="w")
        ttk.Entry(p_fix, textvariable=self.dlat, width=10).grid(row=0, column=1)
        ttk.Label(p_fix, text="λ").grid(row=0, column=2)
        ttk.Entry(p_fix, textvariable=self.dlon, width=10).grid(row=0, column=3)
        ttk.Button(p_fix, text="计算船位", command=self.do_fix).grid(
            row=1, column=0, columnspan=2, sticky="we", pady=3)
        ttk.Button(p_fix, text="DR ← 真位置", command=self._dr_from_true).grid(
            row=1, column=2, columnspan=2, sticky="we", pady=3)
        ttk.Label(p_fix, foreground="#7f9bb3", justify="left",
                  text="每次观测给出一条位置线; 2 条以上交会出船位。\n"
                       "详细解算过程见左下「计算结果」与航海历页。").grid(
            row=2, column=0, columnspan=4, sticky="w")
        p_fix.columnconfigure(3, weight=1)

        self._sync_shade_ui()
        self._update_clamp_btn()
        self._write_out(
            "六分仪操作 (与真船上一样):\n"
            "  ① 先把遮光镜翻下来 —— 测太阳必须遮光, 否则灼伤眼睛。\n"
            "     按「建议滤片」会按太阳高度自动选深浅; 也可以直接点画面上的滤片。\n"
            "  ② 望远镜对平海平线 —— 本模拟里海平线永远在视场正中。\n"
            "  ③ 松开夹钳(点画面上红色的夹钳), 拖动金色指标臂把天体带下来。\n"
            "  ④ 夹紧夹钳, 用微动螺旋(分盘/箭头/键盘←→)把下边缘正好切在海平线上。\n"
            "  ⑤ 左右缓缓摆动六分仪(勾「摆动演示」), 天体划弧, 弧的最低点才是真高度。\n"
            "  ⑥ 记下 Hs 与秒表时刻 → 按「记录本次观测」。\n"
            "  ⑦ 记 2~3 个方位不同的天体, 到「定位」页按「计算船位」。\n"
            "  「自动测量演示」会把①~⑥整套动作演一遍。\n")

    # ==================================================================
    #  参数与时间
    # ==================================================================
    def _fnum(self, var, default=0.0):
        try:
            return float(var.get())
        except Exception:
            return default

    def true_pos(self):
        return (max(-89.9, min(89.9, self._fnum(self.tlat, 3.139))),
                self._fnum(self.tlon, 101.6869))

    def obs_utc(self):
        return self.clock.utc()

    def _on_body(self, *_):
        if is_star(self.body_var.get()):
            self.limb_var.set("中心")
            self.limb_cb.configure(state="disabled")
        else:
            self.limb_cb.configure(state="readonly")
        self.redraw()

    def _toggle_pause(self):
        paused = self.clock.toggle_pause()
        self.pause_btn.configure(text="▶ 继续" if paused else "⏸ 暂停")
        self.redraw()

    def _on_speed(self, *_):
        for name, val in SPEEDS:
            if name == self.speed_var.get():
                self.clock.speed = val
                break

    def _go_now(self):
        self.clock.now()
        self.clock.speed = 1.0
        self.speed_var.set(SPEEDS[0][0])
        self.redraw()

    def _jump_to(self):
        txt = self.utc_var.get().strip()
        for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
            try:
                self.clock.set_utc(dt.datetime.strptime(txt, fmt))
                self.redraw()
                return
            except ValueError:
                continue
        messagebox.showwarning("时刻格式", "请用 2026-08-30 08:20:00 这样的格式")

    def _nudge(self, minutes):
        self.clock.jump(dt.timedelta(minutes=minutes))
        self.redraw()

    def _on_city(self, *_):
        for c in CITIES:
            if c[0] == self.city_var.get():
                self.tlat.set("%.4f" % c[1])
                self.tlon.set("%.4f" % c[2])
                break
        self.redraw()

    def _dr_from_true(self):
        lat, lon = self.true_pos()
        self.dlat.set("%.4f" % (lat + 0.5))
        self.dlon.set("%.4f" % (lon - 0.5))

    # ---- 遮光镜 ----
    def set_shades(self, n_index=None, n_hor=None, quiet=False):
        if n_index is not None:
            self.n_index.set(max(0, min(len(INDEX_SHADES), int(n_index))))
        if n_hor is not None:
            self.n_hor.set(max(0, min(len(HORIZON_SHADES), int(n_hor))))
        self._sync_shade_ui()
        if not quiet:
            self.redraw()

    def _toggle_shade(self, kind, k):
        """点第 k 片: 若它已翻下则翻起它及以后各片, 否则翻下到第 k 片 (真实叠片)。"""
        var = self.n_index if kind == "index" else self.n_hor
        n = var.get()
        var.set(k if n >= k + 1 else k + 1)
        self._sync_shade_ui()
        self.redraw()

    def _sync_shade_ui(self):
        for i, b in enumerate(getattr(self, "_ish_btns", [])):
            b.state(["selected"] if i < self.n_index.get() else ["!selected"])
        for i, b in enumerate(getattr(self, "_hsh_btns", [])):
            b.state(["selected"] if i < self.n_hor.get() else ["!selected"])

    def apply_advised_shades(self):
        try:
            sc = self.scene()
            alt = sc["topo"]["alt_app"]
        except Exception:
            alt = 30.0
        n, _ = shade_advice(self.body_var.get(), alt)
        self.set_shades(n, 1 if self.body_var.get() == "太阳" else 0)
        self._say(_T("已翻下 %d 片指标遮光镜") % n, "#6fc96f")

    def shades(self, sc=None):
        alt = 30.0
        if sc:
            alt = sc["topo"]["alt_app"]
        return shade_state(self.body_var.get(), self.n_index.get(),
                           self.n_hor.get(), alt)

    # ---- 夹钳 ----
    def toggle_clamp(self):
        self.clamped.set(not self.clamped.get())
        self._update_clamp_btn()
        self._say("夹钳已夹紧 — 现在用微动螺旋细调" if self.clamped.get()
                  else "夹钳已松开 — 指标臂可以自由滑动", "#6fc96f")
        self.redraw()

    def _update_clamp_btn(self):
        self.clamp_btn.configure(
            text="🔒 夹钳: 夹紧 (点此松开)" if self.clamped.get()
            else "🔓 夹钳: 松开 (点此夹紧)")

    def _say(self, text, color="#c9a227", secs=2.5):
        import time
        self._hint = (text, color, time.time() + secs)

    def can_coarse(self):
        return (not self.strict_clamp.get()) or (not self.clamped.get())

    def can_fine(self):
        return (not self.strict_clamp.get()) or self.clamped.get()

    # ---- 读数 ----
    def reading(self):
        try:
            d = self.deg_var.get()
        except Exception:
            d = 0
        try:
            m = self.min_var.get()
        except Exception:
            m = 0.0
        return d + m / 60.0

    def set_reading(self, hs):
        hs = max(0.0, min(120.0, hs))
        d = int(hs)
        m = (hs - d) * 60.0
        if m >= 59.95:
            d += 1
            m = 0.0
        m = round(m, 1)
        # 滑杆 set() 会把值量化到像素, 若让它回写就会把 0.1′ 的微调吃掉
        self._syncing = True
        try:
            self.deg_var.set(d)
            self.min_var.set(m)
            self.coarse.set(min(90, d))
            self.fine.set(m)
        finally:
            self._syncing = False

    def _on_coarse(self, v):
        if getattr(self, "_syncing", False):
            return
        self.deg_var.set(int(float(v)))

    def _on_fine(self, v):
        if getattr(self, "_syncing", False):
            return
        self.min_var.set(round(float(v), 1))

    def _adj(self, delta):
        """统一的读数调整入口, 受夹钳状态约束。"""
        coarse = abs(delta) >= 1.0 - 1e-9
        if coarse and not self.can_coarse():
            self._say("夹钳还夹着 — 先松开夹钳才能转指标臂粗调", "#e08a5a")
            self.redraw()
            return False
        if (not coarse) and not self.can_fine():
            self._say("夹钳松着 — 微动螺旋不咬合齿弧, 先夹紧再细调", "#e08a5a")
            self.redraw()
            return False
        self._auto = None
        self.set_reading(self.reading() + delta)
        self.redraw()
        return True

    def _wheel(self, direction):
        self._adj(direction * 0.1 / 60.0)

    # ==================================================================
    #  模拟正演
    # ==================================================================
    def scene(self):
        lat, lon = self.true_pos()
        utc = self.obs_utc()
        body = self.body_var.get()
        limb = "中心" if is_star(body) else self.limb_var.get()
        pos = EPH.get(body, utc)
        sc = required_reading(pos, lat, lon, utc, limb,
                              self._fnum(self.eye, 2.5), self._fnum(self.ie, 0.0),
                              self._fnum(self.press, 1010), self._fnum(self.temp, 28))
        sc.update(lat=lat, lon=lon, utc=utc, body=body, pos=pos, limb=limb)
        if body == "太阳":
            sc["sun_alt"] = sc["topo"]["alt_app"]
        else:
            try:
                sc["sun_alt"] = topocentric_alt(
                    EPH.get("太阳", utc), lat, lon, utc,
                    self._fnum(self.eye, 2.5), self._fnum(self.press, 1010),
                    self._fnum(self.temp, 28))["alt_app"]
            except Exception:
                sc["sun_alt"] = 30.0
        return sc

    def auto_align(self):
        sc = self.scene()
        hs = sc["hs"]
        if self.noise_var.get():
            import random
            hs += random.gauss(0.0, self._fnum(self.sigma, 0.3)) / 60.0
        self.set_reading(round(hs * 600.0) / 600.0)
        self.redraw()

    # ---- 自动演示 (按真实操作顺序分段) ----
    AUTO_STAGES = [("放下遮光镜", 1.6), ("望远镜对平海平线", 1.0),
                   ("松开夹钳 · 转臂粗调", 2.8), ("夹紧 · 微动螺旋细调", 2.2),
                   ("左右摆动取最低点", 4.0), ("读数记录", 0.6)]

    def auto_demo(self):
        """自动演示: 完整重现一次真实的六分仪测高流程。"""
        import time
        sc = self.scene()
        if sc["topo"]["alt_app"] <= 0:
            messagebox.showinfo("天体在地平线下", "该天体此刻不在地平线上, 换一个天体或时刻。")
            return
        target = sc["hs"]
        if self.noise_var.get():
            import random
            target += random.gauss(0.0, self._fnum(self.sigma, 0.3)) / 60.0
        n_adv, _ = shade_advice(self.body_var.get(), sc["topo"]["alt_app"])
        self.set_shades(0, 0, quiet=True)
        self.clamped.set(True)
        self._update_clamp_btn()
        self.swing.set(False)
        self._swing_t0 = None
        self.set_reading(0.0)
        self._auto = {"stage": 0, "t0": time.time(), "to": target,
                      "n_adv": n_adv, "n_hor": 1 if self.body_var.get() == "太阳" else 0,
                      "coarse_to": max(0.0, target - 0.35),
                      "label": self.AUTO_STAGES[0][0]}
        self.clock.set_paused(True)
        self.pause_btn.configure(text="▶ 继续")

    def _auto_next(self):
        import time
        a = self._auto
        a["stage"] += 1
        a["t0"] = time.time()
        if a["stage"] >= len(self.AUTO_STAGES):
            self.swing.set(False)
            self._auto = None
            self.record()
            self._say("自动演示结束 — 已记录本次观测", "#6fc96f", 4.0)
            return
        a["label"] = self.AUTO_STAGES[a["stage"]][0]

    def _auto_step(self):
        if not self._auto:
            return
        import time
        a = self._auto
        st = a["stage"]
        dur = self.AUTO_STAGES[st][1]
        f = min(1.0, (time.time() - a["t0"]) / dur)
        if st == 0:                                   # 逐片翻下遮光镜
            k = int(f * (a["n_adv"] + a["n_hor"] + 0.001))
            self.set_shades(min(a["n_adv"], k),
                            max(0, min(a["n_hor"], k - a["n_adv"])), quiet=True)
            if f >= 1.0:
                self.set_shades(a["n_adv"], a["n_hor"], quiet=True)
                self._auto_next()
        elif st == 1:                                 # 对平海平线
            if f >= 1.0:
                self.clamped.set(False)
                self._update_clamp_btn()
                self._auto_next()
        elif st == 2:                                 # 粗调 (夹钳松开)
            e = 1 - (1 - f) ** 3
            self.set_reading(a["coarse_to"] * e)
            if f >= 1.0:
                self.set_reading(a["coarse_to"])
                self.clamped.set(True)
                self._update_clamp_btn()
                self._auto_next()
        elif st == 3:                                 # 微动螺旋
            e = 1 - (1 - f) ** 2
            self.set_reading(a["coarse_to"] + (a["to"] - a["coarse_to"]) * e)
            if f >= 1.0:
                self.set_reading(round(a["to"] * 600.0) / 600.0)
                self.swing.set(True)
                self._swing_t0 = time.time()
                self._auto_next()
        elif st == 4:                                 # 摆动
            if f >= 1.0:
                self.swing.set(False)
                self._auto_next()
        else:
            if f >= 1.0:
                self._auto_next()

    # ==================================================================
    #  观测记录
    # ==================================================================
    def make_record(self, body, utc, limb, hs=None, noise=False):
        lat, lon = self.true_pos()
        eye = self._fnum(self.eye, 2.5)
        ie = self._fnum(self.ie, 0.0)
        pr = self._fnum(self.press, 1010)
        tp = self._fnum(self.temp, 28)
        if is_star(body):
            limb = "中心"
        pos = EPH.get(body, utc)
        sc = required_reading(pos, lat, lon, utc, limb, eye, ie, pr, tp)
        if hs is None:
            hs = sc["hs"]
            if noise:
                import random
                hs += random.gauss(0.0, self._fnum(self.sigma, 0.3)) / 60.0
            hs = round(hs * 600.0) / 600.0
        ho, corr = reduce_sight(pos, hs, limb, eye, ie, pr, tp)
        return {"utc": utc, "body": body, "hs": hs, "ho": ho, "pos": pos,
                "limb": limb, "corr": corr, "eye": eye, "ie": ie,
                "press": pr, "temp": tp}

    def add_record(self, rec):
        self.obs.append(rec)
        self.tree.insert("", "end", values=(
            rec["body"].split(" ")[0], rec["utc"].strftime("%m-%d %H:%M:%S"),
            fmt_deg_min(rec["hs"]), fmt_deg_min(rec["ho"]), "—", "—"))
        autosize_tree(self.tree, self.app.mono_font, self.app.ui_font)

    def record(self, quiet=False):
        self.add_record(self.make_record(self.body_var.get(), self.obs_utc(),
                                         self.limb_var.get(), hs=self.reading()))
        if not quiet:
            self.do_fix(silent=True)

    def demo_three(self):
        lat, lon = self.true_pos()
        base = self.obs_utc()
        cand = []
        offsets = [0.0]
        for k in range(1, 19):
            offsets += [k * 0.5, -k * 0.5]
        pool = NAV_BODIES + SEXTANT_STARS
        for off in offsets:
            t = base + dt.timedelta(minutes=int(off * 60))
            for b in pool:
                pos = EPH.get(b, t)
                alt, az = altaz_from_hadec(norm360(pos.gha + lon), pos.dec, lat)
                if alt >= 12.0:
                    cand.append((abs(off), t, b, alt, az))
        cand.sort(key=lambda x: x[0])
        chosen = []
        for c in cand:
            if any(abs(norm180(c[4] - o[4])) < 30.0 for o in chosen):
                continue
            if any(o[2] == c[2] and abs((c[1] - o[1]).total_seconds()) < 3600
                   for o in chosen):
                continue
            chosen.append(c)
            if len(chosen) >= 3:
                break
        for _, t, b, alt, az in chosen:
            limb = "下边缘" if b in ("太阳", "月亮") else "中心"
            self.add_record(self.make_record(b, t, limb,
                                             noise=self.noise_var.get()))
        if len(chosen) < 2:
            messagebox.showinfo("可用观测不足",
                                "前后 9 小时内找不到 2 个方位相差 30° 以上、"
                                "高于 12° 的天体。换个时刻或地点再试。")
        self.do_fix(silent=True)
        self.redraw()

    def del_sel(self):
        for iid in self.tree.selection():
            idx = self.tree.index(iid)
            self.tree.delete(iid)
            if 0 <= idx < len(self.obs):
                self.obs.pop(idx)
        self.do_fix(silent=True)

    def clear_obs(self):
        self.obs.clear()
        for iid in self.tree.get_children():
            self.tree.delete(iid)
        self.last_fix = None
        self._write_out("观测记录已清空。\n")

    # ==================================================================
    #  定位
    # ==================================================================
    def do_fix(self, silent=False):
        if len(self.obs) < 2:
            if not silent:
                messagebox.showinfo("观测不足", "至少需要 2 次不同方位的观测。")
            self._write_out(_T("已记录 %d 次观测, 至少需要 2 次(方位不同)。\n") % len(self.obs))
            return
        lat0 = self._fnum(self.dlat, 0.0)
        lon0 = self._fnum(self.dlon, 100.0)
        lat, lon, info = compute_fix(self.obs, lat0, lon0)
        self.last_fix = (lat, lon)
        tlat, tlon = self.true_pos()
        dlat_nm = (lat - tlat) * 60.0
        dlon_nm = norm180(lon - tlon) * 60.0 * dcos(tlat)
        err = math.hypot(dlat_nm, dlon_nm)
        for i, (o, hc, zn, a) in enumerate(info["rows"]):
            iid = self.tree.get_children()[i]
            self.tree.item(iid, values=(
                o["body"].split(" ")[0], o["utc"].strftime("%m-%d %H:%M:%S"),
                fmt_deg_min(o["hs"]), fmt_deg_min(o["ho"]),
                "%.1f°" % zn, "%+.2f" % a))
        L = []
        A = L.append
        A(_T("【截距法定位】 观测 %d 次   推测位置 DR: %s  %s")
          % (info["n"], deg_dm(lat0, "N", "S"), deg_dm(lon0, "E", "W")))
        A("-" * 60)
        A("天体      LHA        Dec        Hc         Zn      截距a(nm)")
        for o, hc, zn, a in info["rows"]:
            lha = norm360(o["pos"].gha + lon)
            A("%-8s %8.3f°  %+8.3f°  %8.4f°  %6.1f°  %+8.2f %s"
              % (o["body"].split(" ")[0], lha, o["pos"].dec, hc, zn, a,
                 "向" if a > 0 else "背"))
        A("-" * 60)
        if info["warn"]:
            A("⚠ " + info["warn"])
        else:
            A(_T("观测船位  φ = %s    λ = %s") % (deg_dm(lat, "N", "S"),
                                            deg_dm(lon, "E", "W")))
            A(_T("真实位置  φ = %s    λ = %s") % (deg_dm(tlat, "N", "S"),
                                            deg_dm(tlon, "E", "W")))
            A(_T("误差      Δφ = %+.2f′   Δλ = %+.2f′(东西向 %.2f nm)")
              % ((lat - tlat) * 60, norm180(lon - tlon) * 60, dlon_nm))
            A(_T("          总偏差 = %.2f 海里 (%.2f km)   残差 RMS = %.2f′")
              % (err, err * 1.852, info["rms"]))
        o = self.obs[-1]
        c = o["corr"]
        A("")
        A(_T("【最后一次观测的改正明细】%s %s") % (o["body"], o["limb"]))
        A("  Hs %s  −IE %+.2f′  −Dip %+.2f′  = Ha %s"
          % (fmt_deg_min(o["hs"]), -c["IE"], -c["dip"], fmt_deg_min(c["Ha"])))
        A("  −R %+.2f′  ±SD %+.2f′  +PA %+.2f′  = Ho %s"
          % (-c["refr"],
             c["SD"] if o["limb"] == "下边缘" else (-c["SD"] if o["limb"] == "上边缘" else 0.0),
             c["PA"], fmt_deg_min(o["ho"])))
        self._write_out("\n".join(L))

    def _write_out(self, text):
        self.out.configure(state="normal")
        self.out.delete("1.0", "end")
        self.out.insert("1.0", text)
        self.out.configure(state="disabled")

    # ==================================================================
    #  航海历
    # ==================================================================
    def refresh_almanac(self):
        txt, marks = self.almanac_build()
        self.alm.configure(state="normal")
        self.alm.delete("1.0", "end")
        self.alm.insert("1.0", txt)
        self._alm_apply(self.alm, marks)
        self.alm.configure(state="disabled")
        try:
            for row, a, b, tg in marks:
                if tg == "hit":
                    self.alm.see("%d.0" % (row + 1))
                    break
        except Exception:
            pass
        try:
            sc = self.scene()
            self.alm_hdr.configure(
                text=_T("此刻正确读数 Hs = %s   (%s · %s)\n"
                     "真高度 Ho 应为 %s   GHA %.3f°  Dec %+.3f°")
                     % (fmt_deg_min(sc["hs"]), sc["body"], sc["limb"],
                        fmt_deg_min(sc["topo"]["alt_geo"]),
                        sc["pos"].gha, sc["pos"].dec))
        except Exception:
            pass

    def open_almanac(self):
        win = tk.Toplevel(self)
        win.title("航海历 Nautical Almanac · 观测归算全过程")
        win.geometry("1120x780")
        win.configure(bg="#161c22")
        bar = ttk.Frame(win, padding=4)
        bar.pack(fill="x")
        ttk.Label(bar, text="内容由本程序星历实时算出, 格式仿 The Nautical Almanac",
                  foreground="#8fb3d0").pack(side="left")
        txt = tk.Text(win, bg="#0d1117", fg="#d8e0e8", font=self.app.mono_font,
                      relief="flat", wrap="none")
        ysb = ttk.Scrollbar(win, orient="vertical", command=txt.yview)
        xsb = ttk.Scrollbar(win, orient="horizontal", command=txt.xview)
        txt.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)
        ysb.pack(side="right", fill="y")
        xsb.pack(side="bottom", fill="x")
        txt.pack(side="left", fill="both", expand=True)
        content, marks = self.almanac_build()
        txt.insert("1.0", content)
        self._alm_apply(txt, marks)
        txt.configure(state="disabled")
        try:
            for row, a, b, tg in marks:
                if tg == "hit":
                    txt.see("%d.0" % (row + 1))
                    break
        except Exception:
            pass

        def save():
            import os
            path = os.path.abspath("nautical_almanac.txt")
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("已保存", _T("航海历已保存到:\n%s") % path, parent=win)
            except Exception as ex:
                messagebox.showwarning("保存失败", str(ex), parent=win)
        ttk.Button(bar, text="保存为文本", command=save).pack(side="right")
        return win

    # ---- 航海历正文 (带高亮标记) ----
    ALM_TAGS = {
        "hit":  dict(background="#3d3413", foreground="#ffd257"),
        "nxt":  dict(background="#26200c", foreground="#d6b45a"),
        "col":  dict(background="#123544", foreground="#7fe3ff"),
        "hdr":  dict(foreground="#8fb3d0"),
        "eq":   dict(foreground="#9fe0bc"),
        "res":  dict(background="#12321c", foreground="#8fe8a0"),
        "warn": dict(foreground="#e08a5a"),
        "dim":  dict(foreground="#5f7c93"),
    }
    BOLD_TAGS = ("hit", "col", "hdr", "res")

    def almanac_text(self):
        return self.almanac_build()[0]

    def _alm_apply(self, widget, marks):
        for name, cfg in self.ALM_TAGS.items():
            widget.tag_configure(name, font=(self.app.mono_font_b
                                             if name in self.BOLD_TAGS
                                             else self.app.mono_font), **cfg)
        for row, a, b, tag in marks:
            widget.tag_add(tag, "%d.%d" % (row + 1, a), "%d.%d" % (row + 1, b))

    def almanac_build(self):
        """生成航海历正文; 同时返回高亮标记 [(行, 起列, 止列, tag)]。"""
        L, MK = [], []

        def A(s="", tag=None):
            i = len(L)
            L.append(s)
            if tag:
                MK.append((i, 0, len(s), tag))
            return i

        def span(i, a, b, tag):
            MK.append((i, a, b, tag))

        obs = list(self.obs)
        now = self.obs_utc()
        day = (obs[0]["utc"] if obs else now).date()
        base = dt.datetime(day.year, day.month, day.day)
        sc = None
        try:
            sc = self.scene()
        except Exception:
            pass
        cur_body = sc["body"] if sc else self.body_var.get()
        cur_h = now.hour
        A("=" * 118)
        A(_T("        NAUTICAL ALMANAC —— %s (UT)        由本程序的 VSOP87/ELP 星历实时计算")
          % day.strftime(_T("%Y 年 %m 月 %d 日")), "hdr")
        A("=" * 118)
        if sc:
            A()
            A(_T("★ 此刻 (%s UTC) 你选的 %s (%s) 的正确六分仪读数:  Hs = %s")
              % (now.strftime("%H:%M:%S"), sc["body"], sc["limb"],
                 fmt_deg_min(sc["hs"])), "res")
            A(_T("   对应真高度 Ho = %s ;  GHA = %s   Dec = %s")
              % (fmt_deg_min(sc["topo"]["alt_geo"]), fmt_dm(sc["pos"].gha),
                 fmt_dec(sc["pos"].dec)), "res")
            A(_T("   (Hs 已含 眼高俯角 %.2f′ 与 指标差 %.2f′; 你现在的读数是 %s)")
              % (sc["dip"], self._fnum(self.ie, 0.0), fmt_deg_min(self.reading())),
              "dim")
            A("   下面表里: 黄底加粗 = 本次观测所在的整点行, 青底 = 该天体的列, "
              "淡黄 = 下一小时(内插用)。", "dim")
        A()
        A("【第一页】太阳与月亮 (每整点的格林尼治时角 GHA 与赤纬 Dec)", "hdr")
        A("-" * 118)
        hdr = ("  UT  |        SUN  GHA        Dec       "
               "|        MOON  GHA       v      Dec       d      HP")
        i_hdr = A(hdr)
        for h in range(24):
            t = base + dt.timedelta(hours=h)
            su = EPH.get("太阳", t)
            mo = EPH.get("月亮", t)
            vs, ds = hourly_v_d("太阳", t)
            vm, dm = hourly_v_d("月亮", t)
            pre = "  %02dh | " % h
            spart = "%s  %s (d%+5.1f)" % (fmt_dm(su.gha), fmt_dec(su.dec), ds)
            mid = " | "
            mpart = "%s %+5.1f  %s %+5.1f  %4.1f′" % (fmt_dm(mo.gha), vm,
                                                      fmt_dec(mo.dec), dm,
                                                      mo.hp_arcmin)
            i = A(pre + spart + mid + mpart)
            if cur_body in ("太阳", "月亮"):
                if h == cur_h:
                    span(i, 0, len(pre + spart + mid + mpart), "hit")
                elif h == (cur_h + 1) % 24:
                    span(i, 0, len(pre + spart + mid + mpart), "nxt")
            if cur_body in ("太阳", "月亮") and h in (cur_h, (cur_h + 1) % 24):
                if cur_body == "太阳":
                    span(i, len(pre), len(pre + spart), "col")
                    span(i_hdr, len(pre), len(pre + spart), "col")
                else:
                    span(i, len(pre + spart + mid), len(pre + spart + mid + mpart),
                         "col")
                    span(i_hdr, len(pre + spart + mid),
                         len(pre + spart + mid + mpart), "col")
        A("-" * 118)
        A("  注: v = GHA 每小时变化超出标称值的部分 (日/行星标称 15°00.0′/h, "
          "月标称 14°19.0′/h)", "dim")
        A("      d = 赤纬每小时的变化;  HP = 月亮的地平视差", "dim")
        A()
        A("【第二页】白羊宫(春分点)与四颗航海行星", "hdr")
        A("-" * 118)
        PL = ("金星", "火星", "木星", "土星")
        pre2 = "  UT  |  ARIES GHA  |"
        seg2 = ["   VENUS GHA      Dec    |", "    MARS GHA      Dec    |",
                "  JUPITER GHA     Dec    |", "  SATURN GHA      Dec"]
        i_hdr2 = A(pre2 + "".join(seg2))
        cur_even = (cur_h // 2) * 2
        for h in range(0, 24, 2):
            t = base + dt.timedelta(hours=h)
            pre = "  %02dh | %s |" % (h, fmt_dm(gha_aries(t)))
            parts = []
            for b in PL:
                p = EPH.get(b, t)
                parts.append(" %s %s |" % (fmt_dm(p.gha), fmt_dec(p.dec)))
            row = pre + "".join(parts)
            i = A(row[:-1])
            need2 = (cur_body in PL) or is_star(cur_body)
            if need2:
                if h == cur_even:
                    span(i, 0, len(row) - 1, "hit")
                elif h == cur_even + 2:
                    span(i, 0, len(row) - 1, "nxt")
            if is_star(cur_body) and h in (cur_even, cur_even + 2):
                span(i, 8, len(pre) - 1, "col")
                span(i_hdr2, 8, len(pre2) - 1, "col")
            if cur_body in PL and h in (cur_even, cur_even + 2):
                k = PL.index(cur_body)
                a0 = len(pre) + sum(len(x) for x in parts[:k])
                span(i, a0, a0 + len(parts[k]) - 1, "col")
                b0 = len(pre2) + sum(len(x) for x in seg2[:k])
                span(i_hdr2, b0, b0 + len(seg2[k]), "col")
        A("-" * 118)
        A()
        A("【第三页】恒星 (SHA 与赤纬; GHA星 = GHA白羊 + SHA)", "hdr")
        A("-" * 118)
        A("   星名                    SHA          Dec        "
          "|   星名                    SHA          Dec")
        A("-" * 118)
        t0 = base + dt.timedelta(hours=12)
        rows, names = [], []
        for nm, ra0, dec0, mag in BUILTIN_STARS:
            p = EPH.get(nm, t0)
            rows.append("  %-20s %s  %s" % (nm[:20], fmt_dm(norm360(360.0 - p.ra)),
                                            fmt_dec(p.dec)))
            names.append(nm)
        for k in range(0, len(rows), 2):
            line = rows[k] + ("   |" + rows[k + 1] if k + 1 < len(rows) else "")
            i = A(line)
            if names[k] == cur_body:
                span(i, 0, len(rows[k]), "hit")
            if k + 1 < len(rows) and names[k + 1] == cur_body:
                span(i, len(rows[k]) + 4, len(line), "hit")
        A("-" * 118)
        A("  (恒星的 SHA/Dec 一天之内几乎不变, 故航海历只给一天一组)", "dim")
        A()
        # ------------------------------------------------------------------
        self._alm_equation(A, span, sc)
        # ------------------------------------------------------------------
        if not obs:
            A()
            A("(还没有观测记录 —— 对准天体后按「记录本次观测」或「一键多星演练」,")
            A(" 这里就会列出每一次观测从读数 Hs 到经纬度的完整算法。)")
            return "\n".join(L), MK

        lat0 = self._fnum(self.dlat, 0.0)
        lon0 = self._fnum(self.dlon, 100.0)
        A("【第五页】增量与改正 Increments & Corrections", "hdr")
        A("-" * 118)
        for i2, o in enumerate(obs, 1):
            t = o["utc"]
            hh = t.replace(minute=0, second=0, microsecond=0)
            frac = (t - hh).total_seconds() / 3600.0
            star = is_star(o["body"])
            rate = (15.04107 if star else
                    (14.0 + 19.0 / 60.0 if o["body"] == "月亮" else 15.0))
            v, d = (0.0, 0.0) if star else hourly_v_d(o["body"], hh)
            if star:
                p_h_gha = norm360(gha_aries(hh) + norm360(360.0 - o["pos"].ra))
            else:
                p_h_gha = EPH.get(o["body"], hh).gha
            inc = rate * frac
            vcorr = v * frac / 60.0
            gha_calc = norm360(p_h_gha + inc + vcorr)
            A(_T("  观测 %d  %s  %s") % (i2, o["body"], t.strftime("%H:%M:%S")), "hdr")
            A(_T("      整点 GHA(%02dh)      = %s%s")
              % (hh.hour, fmt_dm(p_h_gha), "  (= GHA白羊 + SHA)" if star else ""))
            A(_T("      增量 (%02dm%02ds)      = %s      (%.4f h × %s/h)")
              % (t.minute, t.second, fmt_dm(inc), frac, fmt_dm(rate)))
            if not star:
                A(_T("      v 改正 (v=%+.1f′)    = %+.2f′") % (v, vcorr * 60.0))
            A("      ------------------------------------------")
            A(_T("      GHA                = %s   (直接算得 %s, 差 %.2f″)")
              % (fmt_dm(gha_calc), fmt_dm(o["pos"].gha),
                 abs(norm180(gha_calc - o["pos"].gha)) * 3600.0), "res")
            A()
        A("【第六页】观测归算 Sight Reduction (Marcq St Hilaire 截距法)", "hdr")
        A("=" * 118)
        A(_T("  推测位置 DR:  φ = %s   λ = %s") % (deg_dm(lat0, "N", "S"),
                                             deg_dm(lon0, "E", "W")))
        A()
        for i2, o in enumerate(obs, 1):
            c_ = o["corr"]
            pos = o["pos"]
            lha = norm360(pos.gha + lon0)
            hc, zn = altaz_from_hadec(lha, pos.dec, lat0)
            a = (o["ho"] - hc) * 60.0
            sdsign = {"下边缘": 1.0, "上边缘": -1.0}.get(o["limb"], 0.0)
            A(_T("  ── 观测 %d: %s (%s)  UT %s ──")
              % (i2, o["body"], o["limb"], o["utc"].strftime("%Y-%m-%d %H:%M:%S")),
              "hdr")
            A(_T("   ① Hs = %s   −IE %+.2f′   −Dip %+.2f′ (眼高 %.1f m)  ⇒ Ha = %s")
              % (fmt_deg_min(o["hs"]), -o["ie"], -c_["dip"], o["eye"],
                 fmt_deg_min(c_["Ha"])))
            A("   ② −R %+.2f′ (%.0f hPa %.0f℃)   %s%+.2f′   +PA %+.2f′  ⇒ Ho = %s"
              % (-c_["refr"], o["press"], o["temp"],
                 "SD " if sdsign else "SD ", sdsign * c_["SD"], c_["PA"],
                 fmt_deg_min(o["ho"])))
            A(_T("   ③ 航海历: GHA = %s   Dec = %s   ⇒ LHA = GHA+λ = %s")
              % (fmt_dm(pos.gha), fmt_dec(pos.dec), fmt_dm(lha)))
            A("   ④ sinHc = sinφ·sinDec + cosφ·cosDec·cosLHA ⇒ Hc = %s, Zn = %.1f°"
              % (fmt_deg_min(hc), zn))
            A(_T("   ⑤ 截距 a = Ho − Hc = %+.2f′ = %+.2f 海里 (%s)")
              % (a, a, "向着天体" if a > 0 else "背着天体"), "res")
            A()
        if len(obs) >= 2:
            lat, lon, info = compute_fix(obs, lat0, lon0)
            A("【第七页】位置线交会", "hdr")
            A("-" * 118)
            A("  cos(Zn)·dφ + sin(Zn)·dDep = a   (单位: 海里)", "eq")
            for o, hc, zn, a in info["rows"]:
                A("      %-10s cos(%6.1f°)·dφ + sin(%6.1f°)·dDep = %+7.2f"
                  % (o["body"].split(" ")[0], zn, zn, (o["ho"] - hc) * 60.0), "eq")
            tlat, tlon = self.true_pos()
            dn = (lat - tlat) * 60.0
            de = norm180(lon - tlon) * 60.0 * dcos(tlat)
            A()
            A(_T("  观测船位   φ = %s   λ = %s") % (deg_dm(lat, "N", "S"),
                                              deg_dm(lon, "E", "W")), "res")
            A(_T("  真实位置   φ = %s   λ = %s") % (deg_dm(tlat, "N", "S"),
                                              deg_dm(tlon, "E", "W")))
            A(_T("  偏差 %.2f 海里 (%.2f km);  残差 RMS = %.2f′")
              % (math.hypot(dn, de), math.hypot(dn, de) * 1.852, info["rms"]))
        A()
        A("【原理】天体在地球上的星下点 GP: 纬度 = Dec, 经度 = −GHA。", "hdr")
        A("  观测得到的真高度 Ho 决定你到 GP 的角距 z = 90°−Ho (1′ = 1 海里),")
        A("  于是你必在以 GP 为心、半径 z 的等高圆上; 两个天体的圆相交即船位。")
        A("  经度靠时间: GHA 每 4 分钟走 1°, 钟差 1 秒 ≈ 0.25 海里。")
        return "\n".join(L), MK

    # ---- 定位方程: 由此刻的读数 + 时间 + 改正 解出经纬度 ----
    def _alm_equation(self, A, span, sc):
        A("═" * 118)
        A("【第四页】定位方程 —— 由六分仪读数 Hs + 观测时刻 UT + 误差改正, "
          "解出此刻的纬度 φ 与经度 λ", "hdr")
        A("═" * 118)
        if not sc:
            A("  (参数有误, 暂时无法代入数值)", "warn")
            A()
            return
        hs = self.reading()
        ie = self._fnum(self.ie, 0.0)
        eye = self._fnum(self.eye, 2.5)
        press = self._fnum(self.press, 1010)
        temp = self._fnum(self.temp, 28)
        body, limb = sc["body"], sc["limb"]
        utc = sc["utc"]
        pos = sc["pos"]
        Ho, red = reduce_sight(pos, hs, limb, eye, ie, press, temp)
        Ha = red["Ha"]
        sgn = {"下边缘": 1.0, "上边缘": -1.0}.get(limb, 0.0)
        lat0 = self._fnum(self.dlat, 0.0)
        lon0 = self._fnum(self.dlon, 100.0)
        tlat, tlon = self.true_pos()

        A(" 记号  Hs 六分仪读数 │ IE 指标差 │ Dip 眼高俯角 │ R 蒙气差 │ SD 视半径 │ "
          "PA 视差 │ Ho 真高度(地心)", "dim")
        A()
        A(" ① 读数改正 (仪器与大气的误差矫正)", "hdr")
        A("      Ha = Hs − IE − Dip ,        Dip = 1.758′ × √(眼高 m)", "eq")
        A("      Ho = Ha − R(Ha) + s·SD + PA·cos Ha    s = +1 下缘 / −1 上缘 / 0 中心",
          "eq")
        A(_T("      代入: Hs = %s   IE = %+.2f′   Dip = %.2f′ (眼高 %.2f m)")
          % (fmt_deg_min(hs), ie, red["dip"], eye))
        A("            Ha = %s" % fmt_deg_min(Ha))
        A("            R = %.2f′ (%.0f hPa, %.0f℃)   s·SD = %+.2f′   "
          "PA = %+.2f′" % (red["refr"], press, temp, sgn * red["SD"], red["PA"]))
        i = A(_T("            Ho = %s          ← 天体的真高度") % fmt_deg_min(Ho))
        span(i, 12, 12 + 22, "res")
        A()
        A(" ② 时刻 → 天体的星下点 GP (这一步全靠钟表, 所以钟一定要准)", "hdr")
        A("      GHA = GHA(整点) + 增量(标称速率×Δt) + v·Δt        Dec 同法用 d 内插",
          "eq")
        A("      GP 的纬度 = Dec ,   GP 的经度 = −GHA  (西经为正时取 360−GHA)", "eq")
        hh = utc.replace(minute=0, second=0, microsecond=0)
        frac = (utc - hh).total_seconds() / 3600.0
        star = is_star(body)
        rate = 15.04107 if star else (14.0 + 19.0 / 60.0 if body == "月亮" else 15.0)
        v, d = (0.0, 0.0) if star else hourly_v_d(body, hh)
        A(_T("      代入: UT = %s   Δt = %02dm%02ds = %.5f h")
          % (utc.strftime("%Y-%m-%d %H:%M:%S"), utc.minute, utc.second, frac))
        A(_T("            增量 = %.5f h × %s/h = %s   v = %+.1f′/h → %+.2f′")
          % (frac, fmt_dm(rate), fmt_dm(rate * frac), v, v * frac))
        A("            GHA = %s     Dec = %s" % (fmt_dm(pos.gha), fmt_dec(pos.dec)))
        A("            GP  = ( %s , %s )"
          % (deg_dm(pos.dec, "N", "S"), deg_dm(norm180(-pos.gha), "E", "W")))
        A()
        A(" ③ 等高圆 —— 一次观测能给出的全部信息", "hdr")
        A("      天顶距 z = 90° − Ho ;  1′ = 1 海里", "eq")
        A(_T("      代入: z = 90° − %s = %s = %.1f 海里")
          % (fmt_deg_min(Ho), fmt_deg_min(90.0 - Ho), (90.0 - Ho) * 60.0))
        A(_T("      ⇒ 船位一定在以 GP 为圆心、半径 %.1f 海里的圆上 (一条位置圆)。")
          % ((90.0 - Ho) * 60.0), "dim")
        A()
        A(" ④ 以推测位置 (DR) 算出「应该看到的高度」Hc 与方位 Zn", "hdr")
        A("      LHA = GHA + λ(DR)", "eq")
        A("      sin Hc = sinφ·sinDec + cosφ·cosDec·cos LHA", "eq")
        A("      cos Zn = (sinDec − sinφ·sin Hc) / (cosφ·cos Hc)   "
          "(LHA<180° 时 Zn = 360−Zn)", "eq")
        lha = norm360(pos.gha + lon0)
        hc, zn = altaz_from_hadec(lha, pos.dec, lat0)
        A(_T("      代入: DR φ = %s  λ = %s   ⇒ LHA = %s")
          % (deg_dm(lat0, "N", "S"), deg_dm(lon0, "E", "W"), fmt_dm(lha)))
        A("            Hc = %s     Zn = %.1f°" % (fmt_deg_min(hc), zn))
        A()
        A(" ⑤ 截距 (Marcq St Hilaire)", "hdr")
        A("      a = Ho − Hc     (角分 = 海里;  a>0 向着天体方位 Zn 移动)", "eq")
        a_nm = (Ho - hc) * 60.0
        i = A(_T("      代入: a = %s − %s = %+.2f′ = %+.2f 海里 (%s)")
              % (fmt_deg_min(Ho), fmt_deg_min(hc), a_nm, a_nm,
                 "向着天体" if a_nm > 0 else "背着天体"))
        span(i, 6, 200, "res")
        A()
        A(" ⑥ 位置线方程 (每一次观测给一条直线)", "hdr")
        A("      cos Zn · Δφ  +  sin Zn · Δp  =  a        Δp = Δλ · cos φ (东西距)",
          "eq")
        A(_T("      代入本次: cos(%.1f°)·Δφ + sin(%.1f°)·Δp = %+.2f")
          % (zn, zn, a_nm))
        A("      → 一次观测只能定一条线; 要 2 条以上不同方位的线才交会出点。", "dim")
        A()
        A(" ⑦ 解出经纬度", "hdr")
        A("      φ = φ(DR) + Δφ/60 ,      λ = λ(DR) + Δp/(60·cos φ)", "eq")
        obs = list(self.obs)
        if len(obs) >= 2:
            lat, lon, info = compute_fix(obs, lat0, lon0)
            A(_T("      用已记录的 %d 次观测最小二乘解得:") % len(obs))
            for o, hcx, znx, ax in info["rows"]:
                A("            cos(%6.1f°)·Δφ + sin(%6.1f°)·Δp = %+7.2f   [%s]"
                  % (znx, znx, (o["ho"] - hcx) * 60.0, o["body"]), "eq")
            dphi = (lat - lat0) * 60.0
            dp = norm180(lon - lon0) * 60.0 * dcos(lat0)
            A(_T("            Δφ = %+.2f′    Δp = %+.2f 海里") % (dphi, dp))
            i = A("      ⇒  φ = %s      λ = %s"
                  % (deg_dm(lat, "N", "S"), deg_dm(lon, "E", "W")))
            span(i, 0, 200, "res")
            A(_T("         (真实位置 φ = %s  λ = %s;  偏差 %.2f 海里)")
              % (deg_dm(tlat, "N", "S"), deg_dm(tlon, "E", "W"),
                 math.hypot((lat - tlat) * 60.0,
                            norm180(lon - tlon) * 60.0 * dcos(tlat))))
        else:
            A(_T("      现在只有 %d 次观测 —— 还解不出点。再记录一个方位不同的天体即可。")
              % len(obs), "warn")
            A("      (若此刻天体正过中天, 见下面 ⑧ 可单独定纬度)", "dim")
        A()
        A(" ⑧ 两个特例 (不必解方程组)", "hdr")
        mer = norm180(lha)
        A("      中天测纬:  天体过中天 (LHA = 0° 或 180°) 时", "eq")
        A("            LHA=0°(上中天, 天体在正南/正北):  φ = Dec + (90° − Ho)  "
          "或  Dec − (90° − Ho)", "eq")
        A(_T("            取与推测纬度接近的那个根。本次 LHA = %s (离中天 %.2f°)%s")
          % (fmt_dm(lha), abs(mer),
             "  ← 可以用中天法!" if abs(mer) < 0.5 else ""))
        if abs(mer) < 5.0:
            r1 = pos.dec + (90.0 - Ho)
            r2 = pos.dec - (90.0 - Ho)
            pick = r1 if abs(r1 - lat0) < abs(r2 - lat0) else r2
            i = A(_T("            代入: φ = %s ± %s  ⇒  φ = %s")
                  % (fmt_dec(pos.dec), fmt_deg_min(90.0 - Ho),
                     deg_dm(pick, "N", "S")))
            span(i, 0, 200, "res")
        A("      北极星定纬 (北半球): φ ≈ Ho(北极星) + a0 + a1 + a2  "
          "(三个小改正, 合计 < 1°)", "eq")
        A()
        A(" ⑨ 经度与时间的关系 —— 为什么钟一定要准", "hdr")
        A("      GHA 每小时走 15°, 每 4 分钟走 1°, 每 1 秒走 0.25′", "eq")
        A(_T("      ⇒ 钟慢 1 秒, 经度就错 0.25′ ≈ 0.25 海里 × cos φ ≈ %.0f 米 (本纬度)")
          % (0.25 * 1852.0 * dcos(tlat)), "warn")
        A("      ⇒ 观测瞬间必须同时按秒表: 高度与时刻是成对的, 缺一不可。", "dim")
        A()


    # ==================================================================
    #  绘图
    # ==================================================================
    def _tick(self):
        self.clock.tick()
        if not self.winfo_ismapped():
            self.after(400, self._tick)
            return
        if self._auto:
            self._auto_step()
        try:
            foc = self.focus_get()
        except Exception:
            foc = None
        if foc is not self.utc_ent:
            self.utc_var.set(self.obs_utc().strftime("%Y-%m-%d %H:%M:%S"))
        self.redraw()
        self.after(60 if (self.swing.get() or self._auto) else 250, self._tick)

    def redraw(self):
        c = self.canvas
        c.delete("all")
        W = max(c.winfo_width(), 260)
        H = max(c.winfo_height(), 260)
        try:
            sc = self.scene()
        except Exception as ex:
            c.create_text(W / 2, 40, text=_T("参数有误: %s") % ex, fill="#c96f6f")
            return
        try:
            sh0 = self.shades(sc)
            self.shade_lbl.configure(
                text="D=%.2f  %s" % (sh0["Di"],
                                     {"danger": "⚠ 遮光不足", "bright": "偏亮",
                                      "dark": "偏暗", "ok": "合适"}[sh0["level"]]),
                foreground={"danger": "#ff6b5a", "bright": "#e8a54a",
                            "dark": "#7f9bb3", "ok": "#6fc96f"}[sh0["level"]])
        except Exception:
            pass
        wide = W > 660
        top_h = H * 0.50
        fr = max(44.0, min((top_h - 172) / 2.0, W * 0.155))
        fcx, fcy = (W * 0.22 if wide else W / 2), fr + 68
        self._draw_field(fcx, fcy, fr, sc)
        if wide:
            self._draw_lightpath(W * 0.46, 30, W * 0.52, top_h - 46, sc)
        self._draw_sextant(0, top_h, W, H - top_h, sc)
        self._draw_steps(W, sc)

    # ---- 步骤指引 ----
    def current_step(self, sc, sh=None):
        sh = sh or self.shades(sc)
        dev = abs(self.reading() - sc["hs"]) * 60.0
        if sh["level"] in ("danger", "bright", "dark"):
            return 0
        if dev > 60:
            return 2 if not self.clamped.get() else 2
        if dev > 0.05:
            return 3
        if self.swing.get():
            return 4
        return 5

    def _draw_steps(self, W, sc):
        c = self.canvas
        step = self.current_step(sc)
        fb = self.app.ui_font_b
        right = W - 10
        if self._auto:
            lbl = self._auto.get("label", "自动演示中…")
            c.create_text(W - 10, 12, anchor="e", text="▶ " + lbl,
                          fill="#6fc96f", font=fb)
            right -= text_size(fb, "▶ " + lbl)[0] + 16
        # 一行摆不下 (英文字长) 就从离当前步骤最远的那几步起, 只留圈号 ①②…
        shown = list(self.STEPS)

        def total():
            return 10 + sum(text_size(fb, t)[0] + 14 for t in shown) - 14

        for i in sorted(range(len(shown)), key=lambda k: -abs(k - step)):
            if total() <= right or i == step:
                break
            shown[i] = shown[i].split()[0]
        x = 10
        for i, txt in enumerate(shown):
            on = (i == step)
            done = (i < step)
            c.create_text(x, 12, anchor="w", text=txt,
                          fill="#ffd257" if on else ("#4f7a5c" if done else "#4d6376"),
                          font=self.app.ui_font_b if on else self.app.ui_font)
            x += text_size(fb, txt)[0] + 14
        # 临时提示
        import time
        hint = self._hint
        if hint and hint[2] > time.time():
            c.create_text(W / 2, 30, text=hint[0], fill=hint[1],
                          font=self.app.ui_font_b)
        elif hint:
            self._hint = None

    # ---- 望远镜视场 ----
    SKY_STEPS = [(6.0, "#4e8fd0", "#12405f"),      # 白天
                 (0.0, "#c9743f", "#2c3a4a"),      # 日出日落
                 (-6.0, "#3d5580", "#101c2c"),     # 民用曙暮光
                 (-12.0, "#1b2740", "#0a1220"),    # 航海曙暮光
                 (-90.0, "#080d16", "#04070c")]    # 夜

    def sky_colors(self, sun_alt):
        for a, sky, sea in self.SKY_STEPS:
            if sun_alt >= a:
                return sky, sea
        return self.SKY_STEPS[-1][1], self.SKY_STEPS[-1][2]

    def _vig_arcs(self, cx, cy, r, hy, col_sky, col_sea, split, mir_left):
        """渐晕: 靠近视场边缘逐圈变暗 (真实望远镜的暗角)。"""
        c = self.canvas
        N = 7
        for i in range(N):
            f0 = 0.86 + 0.14 * i / (N - 1.0)
            rr = r * f0
            k = ((f0 - 0.86) / 0.14) ** 1.6 * 0.88
            segs = []
            dy = cy - hy
            if abs(dy) < rr:
                t1 = math.degrees(math.asin(max(-1.0, min(1.0, dy / rr))))
                t2 = 180.0 - t1
                segs = [(t1, 90.0 - t1, "sky", False), (90.0, t2 - 90.0, "sky", True),
                        (t2, 270.0 - t2, "sea", True),
                        (270.0, 360.0 + t1 - 270.0, "sea", False)]
            else:
                nm = "sky" if dy <= -rr else "sea"
                segs = [(90.0, 180.0, nm, True), (270.0, 180.0, nm, False)]
            for st, ex, nm, left in segs:
                if ex <= 0.1:
                    continue
                mir = split and (left == mir_left)
                base = (col_sky[1] if nm == "sky" else col_sea[1]) if mir else \
                       (col_sky[0] if nm == "sky" else col_sea[0])
                c.create_arc(cx - rr, cy - rr, cx + rr, cy + rr, start=st,
                             extent=ex, style="arc", width=max(2, r * 0.14 / N + 1),
                             outline=mix_color(base, "#03050a", k))

    def _draw_field(self, cx, cy, r, sc):
        c = self.canvas
        SCALE = r / 2.1
        horizon_y = cy + r * 0.30
        reading = self.reading()
        pos = sc["pos"]
        sh = self.shades(sc)
        real = self.real_view.get()
        split = real and self.hmirror.get() == "split"
        mir_left = self.mirror_left.get()

        # --- 底色: 直视半 (经地平镜滤片) 与 反射半 (经指标镜滤片) ---
        sky0, sea0 = self.sky_colors(sc.get("sun_alt", 30.0))
        if real:
            ht = HORIZON_SHADES[self.n_hor.get() - 1][2] if self.n_hor.get() else None
            it = INDEX_SHADES[self.n_index.get() - 1][2] if self.n_index.get() else None
            sky_d = shaded_scene_color(sky0, sh["Dh"], ht)
            sea_d = shaded_scene_color(sea0, sh["Dh"], ht)
            sky_m = shaded_scene_color(sky0, sh["Di"], it)
            sea_m = shaded_scene_color(sea0, sh["Di"], it)
        else:
            sky_d = sky_m = "#1b4368"
            sea_d = sea_m = "#071a29"
        xl, xr = cx - r, cx + r
        if split:
            xm = cx
            L = (sky_m, sea_m) if mir_left else (sky_d, sea_d)
            Rr = (sky_d, sea_d) if mir_left else (sky_m, sea_m)
            c.create_rectangle(xl, cy - r, xm, horizon_y, fill=L[0], outline="")
            c.create_rectangle(xl, horizon_y, xm, cy + r, fill=L[1], outline="")
            c.create_rectangle(xm, cy - r, xr, horizon_y, fill=Rr[0], outline="")
            c.create_rectangle(xm, horizon_y, xr, cy + r, fill=Rr[1], outline="")
        else:
            # 全视野地平镜: 两像叠加, 整个视场都带指标滤片的调子
            bg_s = mix_color(sky_d, sky_m, 0.5) if real else sky_d
            bg_e = mix_color(sea_d, sea_m, 0.5) if real else sea_d
            c.create_rectangle(xl, cy - r, xr, horizon_y, fill=bg_s, outline="")
            c.create_rectangle(xl, horizon_y, xr, cy + r, fill=bg_e, outline="")

        # --- 天体在视场中的位置 ---
        off = sc["hs_center"] - reading
        by = horizon_y - off * SCALE
        y_top = horizon_y - (sc["hs_upper"] - reading) * SCALE
        y_bot = horizon_y - (sc["hs_lower"] - reading) * SCALE
        ry = max(1.2, (y_bot - y_top) / 2.0)
        rx = max(1.2, sc["sd"] / 60.0 * SCALE)
        bx = cx if not split else (cx - r * 0.42 if mir_left else cx + r * 0.42)
        swinging = self.swing.get()
        if swinging:
            import time
            if self._swing_t0 is None:
                self._swing_t0 = time.time()
            ph = (time.time() - self._swing_t0) * 2.0 * math.pi / 3.6
            theta = 26.0 * math.sin(ph)
            Rs = 2.6 * r
            ccx, ccy = bx, by - Rs
            arc = []
            for a in range(-30, 31, 2):
                arc += [ccx + Rs * dsin(a), ccy + Rs * dcos(a)]
            c.create_line(arc, fill="#2f4a63", dash=(3, 3))
            bx = ccx + Rs * dsin(theta)
            byn = ccy + Rs * dcos(theta)
            y_top += byn - by
            y_bot += byn - by
            by = byn

        below = sc["topo"]["alt_app"] <= -0.5
        notice = None
        if below:
            notice = (_T("该天体在地平线以下 (h′=%.2f°)") % sc["topo"]["alt_app"],
                      "#c96f6f", cy - r - 34)
        elif abs(by - cy) > r * 1.6:
            arrow = "↑ 天体在视场上方" if by < cy else "↓ 天体在视场下方"
            notice = (_T("%s  %+.2f°  转指标臂到 %s")
                      % (arrow, off, fmt_deg_min(sc["hs"])), "#c9a227", cy - r - 34)
        else:
            self._draw_body_in_field(bx, by, rx, ry, sc, sh, real)

        # --- 直视半盖回去 (半镀银的分界: 反射像只出现在镀银那半) ---
        if split:
            if mir_left:
                c.create_rectangle(cx, cy - r, xr, horizon_y, fill=sky_d, outline="")
                c.create_rectangle(cx, horizon_y, xr, cy + r, fill=sea_d, outline="")
            else:
                c.create_rectangle(xl, cy - r, cx, horizon_y, fill=sky_d, outline="")
                c.create_rectangle(xl, horizon_y, cx, cy + r, fill=sea_d, outline="")

        # --- 海面纹理 ---
        for i in range(1, 6):
            y = horizon_y + i * i * 3
            if y < cy + r:
                c.create_line(xl, y, xr, y, fill=mix_color(sea_d, "#ffffff", 0.06))
        # --- 海平线 ---
        hcol = "#dfe9f2" if not real else mix_color(sky_d, "#ffffff", 0.75)
        if split:
            if mir_left:
                c.create_line(cx, horizon_y, xr, horizon_y, fill=hcol, width=2)
                c.create_line(xl, horizon_y, cx, horizon_y,
                              fill=mix_color(sky_m, "#ffffff", 0.35), width=1)
            else:
                c.create_line(xl, horizon_y, cx, horizon_y, fill=hcol, width=2)
                c.create_line(cx, horizon_y, xr, horizon_y,
                              fill=mix_color(sky_m, "#ffffff", 0.35), width=1)
            # 镀银分界线
            c.create_line(cx, cy - r, cx, cy + r, fill="#8a9aa8", width=2)
            c.create_line(cx + (1 if mir_left else -1), cy - r,
                          cx + (1 if mir_left else -1), cy + r, fill="#39485a")
        else:
            c.create_line(xl, horizon_y, xr, horizon_y, fill=hcol, width=2)
            c.create_line(cx, cy - r, cx, cy + r, fill="#31465a", dash=(4, 4))

        if real:
            self._vig_arcs(cx, cy, r, horizon_y, (sky_d, sky_m), (sea_d, sea_m),
                           split, mir_left)
        self._circle_mask(cx, cy, r, "#0b0f13")
        c.create_oval(cx - r, cy - r, cx + r, cy + r, outline="#2b3742", width=6)
        c.create_oval(cx - r, cy - r, cx + r, cy + r, outline="#55697a", width=2)

        # 视场一栏可用的横向范围 (右边是双反射原理图)
        Wc = max(c.winfo_width(), 260)
        xa, xb = 6.0, (Wc * 0.46 - 8.0) if Wc > 660 else Wc - 6.0
        # --- 半区标注 (每半宽 r; 英文太长就退一号字) ---
        if split:
            mx = cx - r * 0.5 if mir_left else cx + r * 0.5
            dx = cx + r * 0.5 if mir_left else cx - r * 0.5
            lh_b = text_size(self.app.ui_font_b, "Ag")[1]
            for tx, txt in ((mx, "镀银半\n反射像"), (dx, "透明半\n海平线")):
                f = self.app.ui_font
                if text_size(f, txt)[0] > r * 0.92:
                    f = self.f_small
                # 两行字的下沿不许碰到下面那行「偏差 …」
                yc = min(cy + r - 11,
                         cy + r + 14 - lh_b / 2.0 - 2 - text_size(f, txt)[1] / 2.0)
                c.create_text(tx, yc, text=txt, justify="center",
                              fill="#c6d6e4", font=f)
        if notice:
            fit_text(c, cx, notice[2], notice[0], self.app.ui_font_b, xa, xb,
                     alt_fonts=(self.app.ui_font,), fill=notice[1])
        fit_text(c, cx, cy - r - 18,
                 _T("望远镜视场 · 视场高 %.1f° · 1 像素≈%.2f′")
                 % (2 * r / SCALE, 60 / SCALE), self.app.ui_font, xa, xb,
                 alt_fonts=(self.f_small,), fill="#7f9bb3")

        # --- 遮光片状态条 ---
        self._draw_shade_bar(cx, cy + r + 46, r, sc, sh)
        if swinging:
            fit_text(c, cx, cy + r + 30,
                     "左右缓缓摆动六分仪 (rock it slowly): 天体划弧, "
                     "弧的最低点才是真高度", self.app.ui_font, xa, xb,
                     alt_fonts=(self.f_small,), fill="#7f9bb3")
        dev = (reading - sc["hs"]) * 60.0
        if not below:
            if abs(dev) < 0.05:
                txt, col = _T("✔ 已切于海平线   Hs = %s") % fmt_deg_min(reading), "#6fc96f"
            else:
                amt = ("%+.2f′" % dev) if abs(dev) < 60 else ("%+.2f°" % (dev / 60.0))
                txt, col = (_T("偏差 %s (%s)") % (amt, "读数偏大" if dev > 0 else "读数偏小"),
                            "#c9a227")
            fit_text(c, cx, cy + r + 14, txt, self.app.ui_font_b, xa, xb,
                     alt_fonts=(self.app.ui_font,), fill=col)

    def _draw_body_in_field(self, bx, by, rx, ry, sc, sh, real):
        """在镀银半里画反射像, 颜色随遮光片密度变化。"""
        c = self.canvas
        body = sc["body"]
        Di = sh["Di"] if real else 1.9
        if body == "太阳":
            col = sun_disc_color(Di)
            if sh["level"] == "danger" and real:
                for k, f in ((2.6, 0.16), (1.9, 0.3), (1.45, 0.5)):
                    c.create_oval(bx - rx * k, by - ry * k, bx + rx * k, by + ry * k,
                                  fill=mix_color("#0b0f13", "#fffbe8", f), outline="")
                col = "#ffffff"
            elif Di < 2.2:
                c.create_oval(bx - rx * 1.5, by - ry * 1.5, bx + rx * 1.5,
                              by + ry * 1.5,
                              fill=mix_color("#0b0f13", col, 0.30), outline="")
            c.create_oval(bx - rx, by - ry, bx + rx, by + ry, fill=col,
                          outline=mix_color(col, "#000000", 0.35), width=1)
        elif body == "月亮":
            self._draw_moon(bx, by, rx, ry, sc["pos"], dim=(10.0 ** (-0.4 * Di))
                            if real else 1.0)
        elif is_star(body):
            f = max(0.10, 10.0 ** (-0.55 * Di)) if real else 1.0
            for k, col in ((3.6, "#4a5d78"), (2.0, "#eaf2ff")):
                c.create_oval(bx - k, by - k, bx + k, by + k,
                              fill=dim_color(col, f), outline="")
            c.create_line(bx - 10, by, bx + 10, by, fill=dim_color("#9fc0ea", f))
            c.create_line(bx, by - 10, bx, by + 10, fill=dim_color("#9fc0ea", f))
        else:
            f = max(0.10, 10.0 ** (-0.5 * Di)) if real else 1.0
            for k, col in ((3.4, "#4a5d78"), (2.0, "#cfe3ff")):
                c.create_oval(bx - k, by - k, bx + k, by + k,
                              fill=dim_color(col, f), outline="")

    def _draw_shade_bar(self, cx, y, r, sc, sh):
        """遮光片一排小方块 (可点), 以及明暗提示。"""
        c = self.canvas
        self._shade_hits = []
        n_i, n_h = self.n_index.get(), self.n_hor.get()
        w, h, gap = 26, 16, 4
        f = self.app.ui_font
        wl_i = text_size(f, "指标")[0]
        wl_h = text_size(f, "地平")[0]
        total = len(INDEX_SHADES) + len(HORIZON_SHADES)
        # 两组小方块前各有一个标签; 第二个标签前留足它自己的宽度, 免得压住前一组
        row = wl_i + 6 + total * (w + gap) - 2 * gap + 18 + wl_h
        x = cx - row / 2.0 + wl_i + 6
        c.create_text(x - 6, y + h / 2, anchor="e", text="指标", fill="#9fb6c9",
                      font=self.app.ui_font)
        for i, (nm, dv, col) in enumerate(INDEX_SHADES):
            on = i < n_i
            hot = (self._press_key == ("shade", "index", i))
            c.create_rectangle(x, y, x + w, y + h,
                               fill="#ffd257" if hot else (col if on else "#141d25"),
                               outline="#fff0b0" if hot else
                               ("#e8dcae" if on else "#3a4b59"),
                               width=2 if (on or hot) else 1)
            c.create_text(x + w / 2, y + h / 2, text=nm.split()[0],
                          fill="#f0e6c8" if on else "#54697a",
                          font=self.app.ui_font)
            self._shade_hits.append((x, y, x + w, y + h, "index", i))
            x += w + gap
        x += 12 - gap + wl_h + 6
        c.create_text(x - 6, y + h / 2, anchor="e", text="地平", fill="#9fb6c9",
                      font=self.app.ui_font)
        for i, (nm, dv, col) in enumerate(HORIZON_SHADES):
            on = i < n_h
            hot = (self._press_key == ("shade", "hor", i))
            c.create_rectangle(x, y, x + w, y + h,
                               fill="#ffd257" if hot else (col if on else "#141d25"),
                               outline="#fff0b0" if hot else
                               ("#9fe0bc" if on else "#3a4b59"),
                               width=2 if (on or hot) else 1)
            c.create_text(x + w / 2, y + h / 2, text=nm.split()[0],
                          fill="#d8f0e2" if on else "#54697a",
                          font=self.app.ui_font)
            self._shade_hits.append((x, y, x + w, y + h, "hor", i))
            x += w + gap
        msg = {"danger": ("⚠ 危险! 遮光片不足, 真船上这样直视太阳会灼伤眼睛", "#ff6b5a"),
               "bright": ("太亮 — 边缘发糊切不准, 再翻下一片", "#e8a54a"),
               "dark": ("太暗 — 天体看不见了, 翻起一片", "#7f9bb3"),
               "ok": ("遮光合适 — 盘面边缘清晰锐利", "#6fc96f")}[sh["level"]]
        Wc = max(c.winfo_width(), 260)
        xa, xb = 6.0, (Wc * 0.46 - 8.0) if Wc > 660 else Wc - 6.0
        fit_text(c, cx, y + h + 13, msg[0], self.app.ui_font_b, xa, xb,
                 alt_fonts=(self.app.ui_font,), fill=msg[1])
        fit_text(c, cx, y + h + 29,
                 _T("密度 D(指标)=%.2f  D(地平)=%.2f  该天体需要 ≈%.2f")
                 % (sh["Di"], sh["Dh"], max(0.0, sh["need"])), self.app.ui_font,
                 xa, xb, alt_fonts=(self.f_small,), fill="#5f7c93")

    def _draw_moon(self, x, y, rx, ry, pos, dim=1.0):
        c = self.canvas
        dim = max(0.10, min(1.0, dim))
        c.create_oval(x - rx, y - ry, x + rx, y + ry,
                      fill=dim_color("#2a2f36", dim), outline=dim_color("#555c66", dim))
        k = max(0.0, min(1.0, pos.illum))
        bright = 1.0 if (0 < pos.phase < 180) else -1.0
        pts = []
        N = 36
        for i in range(N + 1):
            a = -90 + 180.0 * i / N
            pts += [x + bright * rx * dcos(a), y - ry * dsin(a)]
        term = rx * (1 - 2 * k)
        for i in range(N + 1):
            a = 90 - 180.0 * i / N
            pts += [x + bright * term * dcos(a), y - ry * dsin(a)]
        if len(pts) >= 6:
            c.create_polygon(pts, fill=dim_color("#e8e6df", dim), outline="")
        c.create_oval(x - rx, y - ry, x + rx, y + ry,
                      outline=dim_color("#8c9099", dim))

    def _circle_mask(self, cx, cy, r, color):
        c = self.canvas
        big = r * 4
        pts = [cx - big, cy - big, cx + big, cy - big, cx + big, cy + big,
               cx - big, cy + big, cx - big, cy]
        N = 72
        for i in range(N + 1):
            a = 180.0 - 360.0 * i / N
            pts += [cx + r * dcos(a), cy - r * dsin(a)]
        pts += [cx - big, cy]
        c.create_polygon(pts, fill=color, outline="")

    # ---- 双反射光路 ----
    def _draw_lightpath(self, x0, y0, w, h, sc):
        c = self.canvas
        Hs = max(0.5, min(120.0, self.reading()))
        c.create_rectangle(x0, y0, x0 + w, y0 + h, outline="#28323b", fill="#0d141a")
        fit_text(c, x0 + w / 2, y0 + 14, "双反射原理 (光路随指标臂一起转)",
                 self.app.ui_font_b, x0 + 6, x0 + w - 6,
                 alt_fonts=(self.app.ui_font, self.f_small), fill="#8fb3d0")
        T = (x0 + 0.14 * w, y0 + 0.70 * h)
        HG = (x0 + 0.46 * w, y0 + 0.70 * h)
        IM = (x0 + 0.46 * w, y0 + 0.26 * h)
        din = (-dcos(Hs), dsin(Hs))
        dout = (0.0, 1.0)
        nx, ny = dout[0] - din[0], dout[1] - din[1]
        nl = math.hypot(nx, ny) or 1.0
        nx, ny = nx / nl, ny / nl
        mx, my = -ny, nx
        ML = 0.10 * h + 14
        rl = 0.42 * w
        if din[0] < -1e-6:
            rl = min(rl, (x0 + w - 20 - IM[0]) / -din[0])
        if din[1] > 1e-6:
            rl = min(rl, (IM[1] - y0 - 30) / din[1])
        rl = max(40.0, rl)
        far = (IM[0] - din[0] * rl, IM[1] - din[1] * rl)
        c.create_line(far[0], far[1], IM[0], IM[1], fill="#ffd257", width=2,
                      arrow="last", arrowshape=(9, 11, 4))
        c.create_text(far[0] - 8, far[1] + 12, text="来自天体", anchor="e",
                      fill="#c9a227", font=self.app.ui_font)
        c.create_line(IM[0], IM[1], HG[0], HG[1], fill="#ffd257", width=2,
                      arrow="last", arrowshape=(9, 11, 4))
        c.create_line(x0 + w - 12, HG[1], HG[0], HG[1], fill="#8fd0f0", width=2,
                      arrow="last", arrowshape=(9, 11, 4))
        c.create_text(x0 + w - 14, HG[1] - 12, text="来自海平线", anchor="e",
                      fill="#5f9dc0", font=self.app.ui_font)
        c.create_line(HG[0], HG[1], T[0], T[1], fill="#cfe3ff", width=3,
                      arrow="last", arrowshape=(10, 12, 5))
        c.create_line(IM[0] - mx * ML, IM[1] - my * ML,
                      IM[0] + mx * ML, IM[1] + my * ML, fill="#e8eef4", width=5)
        c.create_text(IM[0] - 14, IM[1] + 6, text="指标镜 (转 Hs/2)", anchor="e",
                      fill="#9fb6c9", font=self.app.ui_font)
        c.create_line(HG[0] - ML * 0.7, HG[1] + ML * 0.7,
                      HG[0] + ML * 0.7, HG[1] - ML * 0.7, fill="#9fb6c9", width=5)
        c.create_line(HG[0], HG[1], HG[0] + ML * 0.7, HG[1] - ML * 0.7,
                      fill="#e8eef4", width=5)
        fit_text(c, HG[0] + 12, HG[1] + 22, "地平镜 (半镀银, 固定)",
                 self.app.ui_font, HG[0] + 12, x0 + w - 6, anchor="w",
                 alt_fonts=(self.f_small,), fill="#9fb6c9")
        c.create_rectangle(T[0] - 34, T[1] - 9, T[0] + 6, T[1] + 9,
                           fill="#243040", outline="#5b7d94")
        c.create_oval(T[0] - 42, T[1] - 7, T[0] - 30, T[1] + 7,
                      fill="#1b2530", outline="#5b7d94")
        c.create_text(T[0] - 36, T[1] + 22, text="望远镜/眼", anchor="w",
                      fill="#9fb6c9", font=self.app.ui_font)
        c.create_arc(IM[0] - 46, IM[1] - 46, IM[0] + 46, IM[1] + 46,
                     start=-90, extent=min(170.0, Hs), style="arc",
                     outline="#c9a227", dash=(2, 2))
        fit_text(c, IM[0] + 52, IM[1] + 34,
                 _T("两束光夹角 = Hs = %s") % fmt_deg_min(self.reading()),
                 self.app.ui_font, IM[0] + 52, x0 + w - 6, anchor="w",
                 alt_fonts=(self.f_small,), fill="#c9a227")
        fit_text(c, x0 + w / 2, y0 + h - 12,
                 "镜面转 θ ⇒ 反射光转 2θ ⇒ 弧上刻度 = 2×臂角 = Hs",
                 self.app.ui_font, x0 + 6, x0 + w - 6,
                 alt_fonts=(self.f_small,), fill="#5f7c93")

    # ---- 真实六分仪 (可拖动) ----
    def _draw_sextant(self, x0, y0, W, H, sc):
        c = self.canvas
        if H < 150:
            return
        reading = self.reading()
        self._btn_hits = []
        # 弧的几何: 圆心(指标镜转轴)在上方, 弧在下方
        px = x0 + W * 0.66
        R = min(W * 0.34, H * 0.68)
        py = y0 + 26
        a0, a1 = -58.0, 58.0                 # 弧张角 (读数 0..120)
        self._arm_geom = (px, py, R, a0, a1)

        def arc_pt(read, rad):
            ang = a0 + (max(0.0, min(120.0, read)) / 120.0) * (a1 - a0)
            return (px + rad * dsin(ang), py + rad * dcos(ang))

        c.create_line(x0 + 8, y0 + 4, x0 + W - 8, y0 + 4, fill="#1d2c38")
        # 框架
        e0 = arc_pt(0, R)
        e1 = arc_pt(120, R)
        c.create_polygon([px, py + 8, e0[0], e0[1], e1[0], e1[1]],
                         fill="#141d25", outline="#3a4b59", width=2)
        for k in (0.30, 0.62):
            q0 = arc_pt(30, R * k)
            q1 = arc_pt(90, R * k)
            c.create_line(px, py + 8, q0[0], q0[1], fill="#2b3a46", width=6)
            c.create_line(px, py + 8, q1[0], q1[1], fill="#2b3a46", width=6)
        # 弧与刻度
        c.create_arc(px - R, py - R, px + R, py + R, start=a0 - 90.0,
                     extent=(a1 - a0), style="arc", outline="#c9b47a", width=8)
        for d in range(0, 121):
            p1 = arc_pt(d, R - (11 if d % 10 == 0 else (7 if d % 5 == 0 else 4)))
            p2 = arc_pt(d, R - 1)
            c.create_line(p1[0], p1[1], p2[0], p2[1],
                          fill="#8a7a4a" if d % 10 else "#e8dcae",
                          width=2 if d % 10 == 0 else 1)
        taken = []                     # 已占的地方: 文字最后统一摆, 不许压这些
        for d in range(0, 121, 10):
            tx, ty = arc_pt(d, R - 26)
            it = c.create_text(tx, ty, text=str(d), fill="#d8cfa8",
                               font=self.app.ui_font)
            taken.append(c.bbox(it))
        for d in range(0, 121, 4):                 # 弧带本身
            ax, ay = arc_pt(d, R - 2)
            taken.append((ax - 6, ay - 6, ax + 6, ay + 6))
        # 指标臂
        ix, iy = arc_pt(reading, R + 17)
        c.create_line(px, py + 8, ix, iy, fill="#c9a227", width=7)
        c.create_line(px, py + 8, ix, iy, fill="#f0d67a", width=3)
        taken += seg_boxes(px, py + 8, ix, iy, pad=5)
        # ---- 夹钳 (index-arm clamp): 骑在弧上, 夹紧后臂锁死 ----
        clamped = self.clamped.get()
        cl_c = "#c94f3d" if clamped else "#5aa07a"
        if self._press_key == ("clamp",):
            cl_c = "#ffd257"
        ux, uy = ix - px, iy - (py + 8)
        ul = math.hypot(ux, uy) or 1.0
        ux, uy = ux / ul, uy / ul
        nxv, nyv = -uy, ux                       # 臂的法向
        cxp, cyp = px + ux * (R + 17), py + 8 + uy * (R + 17)
        quad = [cxp + nxv * 13 - ux * 9, cyp + nyv * 13 - uy * 9,
                cxp - nxv * 13 - ux * 9, cyp - nyv * 13 - uy * 9,
                cxp - nxv * 13 + ux * 13, cyp - nyv * 13 + uy * 13,
                cxp + nxv * 13 + ux * 13, cyp + nyv * 13 + uy * 13]
        c.create_polygon(quad, fill="#26323d", outline=cl_c, width=3)
        # 夹钳的扳把: 夹紧时压向弧, 松开时翘起
        lv = 1.0 if clamped else -1.0
        c.create_line(cxp, cyp, cxp + nxv * 22 * lv + ux * 10,
                      cyp + nyv * 22 * lv + uy * 10, fill=cl_c, width=5)
        c.create_oval(cxp - 4, cyp - 4, cxp + 4, cyp + 4, fill=cl_c, outline="")
        self._clamp_hit = (cxp - 24, cyp - 24, cxp + 24, cyp + 24)
        taken.append((cxp - 18, cyp - 18, cxp + 18, cyp + 18))
        labels = [(((px + ux * (R + 46), py + 8 + uy * (R + 46), "center"),
                    (px + ux * (R + 62), py + 8 + uy * (R + 62), "center"),
                    (px + ux * (R + 80), py + 8 + uy * (R + 80), "center")),
                   "夹钳 锁紧" if clamped else "夹钳 松开", cl_c, self.app.ui_font_b)]
        # 指标镜 (随臂转 reading/2)
        half = reading / 2.0
        mlen = 26
        mang = -half                            # 屏幕上的镜面倾角
        c.create_line(px - mlen * dcos(mang), py + 8 - mlen * dsin(mang),
                      px + mlen * dcos(mang), py + 8 + mlen * dsin(mang),
                      fill="#e8eef4", width=6)
        c.create_oval(px - 9, py - 1, px + 9, py + 17, fill="#c9a227", outline="")
        taken += seg_boxes(px - mlen * dcos(mang), py + 8 - mlen * dsin(mang),
                           px + mlen * dcos(mang), py + 8 + mlen * dsin(mang), pad=5)
        taken.append((px - 10, py - 2, px + 10, py + 18))
        labels.append((((px + 16, py + 2, "w"), (px + 32, py + 2, "w"),
                        (px - 32, py + 2, "e"), (px + 14, py - 10, "sw")),
                       "指标镜", "#9fb6c9", self.app.ui_font))
        # 地平镜 + 望远镜 (固定在框架左边)
        hgx, hgy = arc_pt(10, R * 0.68)
        c.create_line(hgx - 16, hgy + 16, hgx + 16, hgy - 16, fill="#9fb6c9", width=6)
        c.create_line(hgx, hgy, hgx + 16, hgy - 16, fill="#e8eef4", width=6)
        taken.append((hgx - 19, hgy - 19, hgx + 19, hgy + 19))
        tel = (hgx - 46, hgy)
        c.create_rectangle(tel[0] - 26, tel[1] - 9, tel[0] + 16, tel[1] + 9,
                           fill="#243040", outline="#5b7d94")
        c.create_oval(tel[0] - 34, tel[1] - 7, tel[0] - 22, tel[1] + 7,
                      fill="#1b2530", outline="#5b7d94")
        taken.append((tel[0] - 35, tel[1] - 10, tel[0] + 17, tel[1] + 10))
        labels.append((((hgx + 20, hgy - 20, "w"), (hgx - 16, hgy - 22, "se"),
                        (hgx + 20, hgy - 38, "w"), (hgx - 16, hgy - 40, "se")),
                       "地平镜(半镀银)", "#9fb6c9", self.app.ui_font))
        labels.append((((tel[0] - 34, tel[1] + 24, "w"), (tel[0] - 36, tel[1] - 12, "sw"),
                        (tel[0] - 38, tel[1], "e"), (tel[0] - 36, tel[1] - 28, "sw"),
                        (tel[0] - 36, tel[1] + 12, "ne"), (tel[0] - 36, tel[1] - 12, "se"),
                        (tel[0] - 36, tel[1] - 44, "sw")),
                       "望远镜", "#9fb6c9", self.app.ui_font))
        # 遮光镜: 指标镜前一组 (翻下=挡在光路上, 翻起=竖起来靠在框架上)
        sh = self.shades(sc)
        n_i, n_h = self.n_index.get(), self.n_hor.get()
        sx1, sy1 = px + 30, py + 22
        for i, (nm, dv, col) in enumerate(INDEX_SHADES):
            on = i < n_i
            X = sx1 + i * 15
            hot = (self._press_key == ("shade", "index", i))
            if on:      # 翻下: 竖直挡在指标镜前
                c.create_rectangle(X, sy1 + 4, X + 12, sy1 + 30,
                                   fill="#ffd257" if hot else col,
                                   outline="#fff0b0" if hot else "#e8dcae", width=2)
            else:       # 翻起: 平躺
                c.create_rectangle(X, sy1 + 4, X + 12, sy1 + 12,
                                   fill="#ffd257" if hot else dim_color(col, 0.45),
                                   outline="#fff0b0" if hot else "#4a5a68")
            self._shade_hits.append((X, sy1, X + 12, sy1 + 32, "index", i))
        taken.append((sx1 - 2, sy1 + 2, sx1 + 15 * len(INDEX_SHADES), sy1 + 32))
        labels.append((((sx1 + 30, sy1 + 42, "center"), (sx1 - 4, sy1 + 42, "nw"),
                        (sx1 - 4, sy1 + 58, "nw"), (sx1 + 15 * len(INDEX_SHADES) + 6,
                                                     sy1 + 18, "w")),
                       "指标遮光镜 (点击翻下/翻起)", "#c9b47a", self.app.ui_font))
        # 地平镜前的一组
        hx1, hy1 = hgx - 4, hgy + 26
        for i, (nm, dv, col) in enumerate(HORIZON_SHADES):
            on = i < n_h
            X = hx1 + i * 15
            hot = (self._press_key == ("shade", "hor", i))
            if on:
                c.create_rectangle(X, hy1, X + 12, hy1 + 24,
                                   fill="#ffd257" if hot else col,
                                   outline="#fff0b0" if hot else "#9fe0bc", width=2)
            else:
                c.create_rectangle(X, hy1, X + 12, hy1 + 8,
                                   fill="#ffd257" if hot else dim_color(col, 0.45),
                                   outline="#fff0b0" if hot else "#4a5a68")
            self._shade_hits.append((X, hy1 - 2, X + 12, hy1 + 26, "hor", i))
        taken.append((hx1 - 2, hy1 - 2, hx1 + 15 * len(HORIZON_SHADES), hy1 + 26))
        labels.append((((hx1 + 24, hy1 - 6, "w"),
                        (hx1 + 15 * len(HORIZON_SHADES) + 4, hy1 + 12, "w"),
                        (hx1 - 6, hy1 + 12, "e"), (hx1, hy1 + 30, "nw")),
                       "地平遮光镜", "#7fbfa0", self.app.ui_font))
        # 光路 (示意): 天体 -> 指标镜 -> 地平镜 -> 望远镜
        alt_dir = sc["topo"]["alt_app"]
        L2 = R * 0.55
        sun_from = (px + L2 * dcos(alt_dir), py + 8 - L2 * dsin(alt_dir))
        c.create_line(sun_from[0], sun_from[1], px, py + 8, fill="#ffd257",
                      width=2, arrow="last", arrowshape=(8, 10, 4), dash=(6, 3))
        c.create_line(px, py + 8, hgx, hgy, fill="#ffd257", width=2,
                      arrow="last", arrowshape=(8, 10, 4), dash=(6, 3))
        c.create_line(hgx, hgy, tel[0] + 16, tel[1], fill="#cfe3ff", width=2,
                      arrow="last", arrowshape=(8, 10, 4))
        c.create_line(hgx + R * 0.42, hgy, hgx, hgy, fill="#8fd0f0", width=2,
                      arrow="last", arrowshape=(8, 10, 4))
        for a_, b_ in ((sun_from, (px, py + 8)), ((px, py + 8), (hgx, hgy)),
                       ((hgx, hgy), (tel[0] + 16, tel[1])),
                       ((hgx + R * 0.42, hgy), (hgx, hgy))):
            taken += seg_boxes(a_[0], a_[1], b_[0], b_[1], pad=3)
        labels.append((((hgx + R * 0.43, hgy - 12, "w"), (hgx + R * 0.43, hgy + 12, "w"),
                        (hgx + R * 0.42 + 6, hgy, "w")),
                       "海平线", "#5f9dc0", self.app.ui_font))
        # 微动螺旋 (分盘)
        dr = arc_pt(120, R)
        dcx, dcy = dr[0] + 22, dr[1] + 10
        drum_r = 20
        c.create_oval(dcx - drum_r, dcy - drum_r, dcx + drum_r, dcy + drum_r,
                      fill="#243040", outline="#8a9aa8", width=2)
        mm = (reading - int(reading)) * 60.0
        for k in range(0, 60, 5):
            ang = -k * 6.0 + mm * 6.0
            c.create_line(dcx + (drum_r - 6) * dsin(ang), dcy - (drum_r - 6) * dcos(ang),
                          dcx + drum_r * dsin(ang), dcy - drum_r * dcos(ang),
                          fill="#c9d4de")
        c.create_line(dcx, dcy - drum_r - 6, dcx, dcy - drum_r + 2, fill="#ffd257",
                      width=2)
        self._btn(dcx - drum_r - 26, dcy - 11, 22, 22, "◀", -0.1 / 60)
        self._btn(dcx + drum_r + 4, dcy - 11, 22, 22, "▶", 0.1 / 60)
        self._drum_geom = (dcx, dcy, drum_r)
        taken.append((dcx - drum_r - 27, dcy - drum_r - 7, dcx + drum_r + 27, dcy + drum_r + 1))
        labels.append((((dcx, dcy + drum_r + 12, "center"), (dcx, dcy + drum_r + 4, "n"),
                        (dcx + drum_r + 27, dcy + drum_r + 4, "ne"),
                        (dcx - drum_r - 27, dcy + drum_r + 4, "nw")),
                       _T("微动螺旋 %.1f′") % mm, "#9fb6c9", self.app.ui_font))
        # 读数 (左栏: 只许用到六分仪左边那一条空地, 英文太长就退一号字或折行)
        tx0 = x0 + 14
        ty0 = y0 + 46
        inst_left = min(tel[0] - 36, px - R * dsin(58.0) - 10)
        xlim = max(tx0 + 120, inst_left - 10)
        fb, fn = self.app.ui_font_b, self.app.ui_font
        c.create_text(tx0, ty0, anchor="w",
                      text="Hs = %s" % fmt_deg_min(reading),
                      fill="#e8eef4", font=self.app.big_font)
        shift = [0.0]                    # 前面有行折了, 后面各排一起往下挪的量

        def row(y, txt, f, alts, col):
            """一行字: 放得下就原位; 放不下先退字号, 再不行就折行并把下面推开。"""
            y += shift[0]
            for ff in (f,) + tuple(alts):
                if text_size(ff, txt)[0] <= xlim - tx0:
                    c.create_text(tx0, y, anchor="w", text=txt, fill=col, font=ff)
                    return
            ff = alts[-1] if alts else f
            lh = text_size(ff, "Ag")[1]
            it_ = c.create_text(tx0, y - lh / 2.0, anchor="nw", text=txt, fill=col,
                                font=ff, width=xlim - tx0)
            bb_ = c.bbox(it_)
            if bb_:
                shift[0] += max(0.0, (bb_[3] - bb_[1]) - lh - 2)

        row(ty0 + 26, _T("应读 %s  (%s · %s)")
            % (fmt_deg_min(sc["hs"]), sc["body"], sc["limb"]), fb, (fn,), "#9fb6c9")
        topo = sc["topo"]
        row(ty0 + 46, _T("真高度 %.4f°  视高度 %.4f°  方位 %.1f°")
            % (topo["alt_topo"], topo["alt_app"], az_fmt(topo["az"], 1)),
            fn, (self.f_small,), "#7f9bb3")
        row(ty0 + 64, _T("GHA %.3f°  Dec %+.3f°  SD %.2f′  HP %.2f′  蒙气差 %.2f′")
            % (sc["pos"].gha, sc["pos"].dec, sc["sd"], sc["pos"].hp_arcmin, topo["refr"]),
            fn, (self.f_small,), "#5f7c93")
        if not self.strict_clamp.get():
            gtxt, gcol = ("已关严格模拟: 所有按钮都能用", "#7f9bb3")
        elif clamped:
            gtxt, gcol = ("夹钳锁紧中 → 只有 1′ / 0.1′ 微动螺旋能动; "
                          "要 1° 粗调请先点夹钳松开", "#e8a54a")
        else:
            gtxt, gcol = ("夹钳松开中 → 可拖指标臂或按 1° 粗调; "
                          "微动螺旋要夹紧才咬合齿弧", "#6fc96f")
        row(ty0 + 86, gtxt, fb, (fn,), gcol)
        bx, by, bw, bh = tx0, ty0 + 98 + shift[0], 52, 26
        for lbl, dv in (("◀◀ 1°", -1.0), ("◀ 1′", -1.0 / 60), ("▶ 1′", 1.0 / 60),
                        ("▶▶ 1°", 1.0)):
            self._btn(bx, by, bw, bh, lbl, dv)
            bx += bw + 6
        s0 = shift[0]
        row(by + bh + 14 - s0, "键盘: ← → = 0.1′   Shift+← → = 1′   Ctrl 或 ↑↓ = 1°",
            fn, (self.f_small,), "#5f7c93")
        by2 = by + bh + 26 + (shift[0] - s0)
        self._btn(tx0, by2, 60, 24, "◀ 0.1′", -0.1 / 60)
        self._btn(tx0 + 66, by2, 60, 24, "0.1′ ▶", 0.1 / 60)
        c.create_text(tx0 + 134, by2 + 12, anchor="w", text="微动螺旋",
                      fill="#9fb6c9", font=self.app.ui_font)
        # ---- 六分仪上的标注最后统一摆: 先试原位, 压到零件、光路、刻度、
        #      左栏文字或别的标注就换个地方 (字宽按实际显示的语言量) ----
        for it in c.find_all():
            if c.type(it) == "text":
                bb = c.bbox(it)
                if bb and bb[1] >= y0 and bb[0] < inst_left:
                    taken.append(bb)
        Hc = max(c.winfo_height(), 260)
        bounds = (x0 + 2, y0 + 6, x0 + W - 2, Hc - 2)
        for cands, txt, col, fnt in labels:
            place_text(c, cands, txt, fnt, taken, bounds, fill=col)


    def _key_adj(self, sign, e=None):
        """键盘左右 = 0.1′; Shift = 1′; Ctrl = 1°; 上下 = 1°。"""
        st = getattr(e, "state", 0) if e else 0
        big = abs(sign) >= 60
        sign = 1 if sign > 0 else -1
        if big or (st & 0x0004):
            step = 1.0
        elif st & 0x0001:
            step = 1.0 / 60.0
        else:
            step = 0.1 / 60.0
        self._adj(sign * step)
        return "break"

    def _btn(self, x, y, w, h, label, delta, color="#243040"):
        c = self.canvas
        idx = len(self._btn_hits)
        coarse = abs(delta) >= 1.0 - 1e-9
        ok = self.can_coarse() if coarse else self.can_fine()
        pressed = (self._press_key == ("btn", idx))
        if not ok:
            fill, out, fg, wd = "#171f27", "#33414d", "#4b5b68", 1
        elif pressed:
            fill, out, fg, wd = "#f0d67a", "#fff0b0", "#101820", 2
        else:
            fill, out, fg, wd = color, "#5b7d94", "#e8eef4", 1
        c.create_rectangle(x, y, x + w, y + h, fill=fill, outline=out, width=wd)
        c.create_text(x + w / 2, y + h / 2, text=label, fill=fg,
                      font=self.app.ui_font_b)
        if not ok:      # 画一把小锁, 表示被夹钳锁住
            lx, ly = x + w - 7, y + 5
            c.create_rectangle(lx - 3, ly + 2, lx + 3, ly + 7, outline="#7a6a3a")
            c.create_arc(lx - 3, ly - 2, lx + 3, ly + 4, start=0, extent=180,
                         style="arc", outline="#7a6a3a")
        self._btn_hits.append((x, y, x + w, y + h, delta))

    def _btn_repeat(self, key, delta, first):
        """按住不放时连发 (先慢后快), 松手即停。"""
        if self._press_key != key:
            self._repeat_job = None
            return
        if not first:
            if not self._adj(delta):
                self._repeat_job = None
                return
        self._repeat_job = self.after(400 if first else 70,
                                      lambda: self._btn_repeat(key, delta, False))

    # ---- 鼠标: 拖动指标臂 / 微动螺旋 ----
    def _press(self, e):
        self._drag_mode = None
        self.canvas.focus_set()
        self._cancel_repeat()
        for i, (x0, y0, x1, y1, dv) in enumerate(getattr(self, "_btn_hits", [])):
            if x0 <= e.x <= x1 and y0 <= e.y <= y1:
                self._press_key = ("btn", i)
                if self._adj(dv):
                    self._btn_repeat(("btn", i), dv, True)
                else:
                    self.redraw()
                return
        ch = getattr(self, "_clamp_hit", None)
        if ch and ch[0] <= e.x <= ch[2] and ch[1] <= e.y <= ch[3]:
            self._press_key = ("clamp",)
            self.toggle_clamp()
            return
        for x0, y0, x1, y1, kind, k in getattr(self, "_shade_hits", []):
            if x0 <= e.x <= x1 and y0 <= e.y <= y1:
                self._press_key = ("shade", kind, k)
                self._toggle_shade(kind, k)
                return
        g = self._arm_geom
        if g:
            px, py, R, a0, a1 = g
            d = math.hypot(e.x - px, e.y - (py + 8))
            if 0.25 * R < d < R + 26:
                ang = math.degrees(math.atan2(e.x - px, e.y - (py + 8)))
                if a0 - 6 <= ang <= a1 + 6:
                    if not self.can_coarse():
                        self._say("夹钳还夹着 — 指标臂动不了, 先点夹钳松开", "#e08a5a")
                        self.redraw()
                        return
                    self._drag_mode = "arm"
                    self._motion(e)
                    return
        dg = getattr(self, "_drum_geom", None)
        if dg and math.hypot(e.x - dg[0], e.y - dg[1]) < dg[2] + 8:
            if not self.can_fine():
                self._say("夹钳松着 — 微动螺旋空转, 先夹紧", "#e08a5a")
                self.redraw()
                return
            self._drag_mode = "drum"
            self._drum_last = math.degrees(math.atan2(e.x - dg[0], dg[1] - e.y))

    def _motion(self, e):
        if self._drag_mode == "arm":
            px, py, R, a0, a1 = self._arm_geom
            ang = math.degrees(math.atan2(e.x - px, e.y - (py + 8)))
            ang = max(a0, min(a1, ang))
            self._auto = None
            self.set_reading((ang - a0) / (a1 - a0) * 120.0)
            self.redraw()
        elif self._drag_mode == "drum":
            dg = self._drum_geom
            ang = math.degrees(math.atan2(e.x - dg[0], dg[1] - e.y))
            d = norm180(ang - self._drum_last)
            self._drum_last = ang
            self._auto = None
            self.set_reading(self.reading() + d / 6.0 / 60.0)
            self.redraw()

    def _cancel_repeat(self):
        if self._repeat_job is not None:
            try:
                self.after_cancel(self._repeat_job)
            except Exception:
                pass
            self._repeat_job = None

    def _release(self, e):
        self._drag_mode = None
        self._cancel_repeat()
        if self._press_key is not None:
            self._press_key = None
            self.redraw()


def fmt_deg_min(x):
    """十进制度 -> 度°分.分′ (六分仪读数格式)。"""
    sign = "-" if x < 0 else ""
    x = abs(x)
    d = int(x)
    m = (x - d) * 60.0
    if m >= 59.995:
        d += 1
        m = 0.0
    return "%s%d°%05.2f′" % (sign, d, m)


# ===========================================================================
#  星空页: 地平坐标投影 + 月相
# ===========================================================================
class SkyCam:
    """地平坐标的立体投影 (stereographic) 相机 —— 大视场也不会严重变形。"""
    ALT_MIN, ALT_MAX = -25.0, 88.0

    def __init__(self, az=180.0, alt=25.0, fov=75.0):
        self.az = az
        self.alt = alt
        self.fov = fov

    def orbit(self, d_az, d_alt):
        self.az = norm360(self.az + d_az)
        self.alt = max(self.ALT_MIN, min(self.ALT_MAX, self.alt + d_alt))

    def zoom(self, f):
        self.fov = max(0.8, min(140.0, self.fov * f))

    def basis(self):
        f = _enu_from_altaz(self.alt, self.az)
        r = _cross(f, (0.0, 0.0, 1.0))
        n = math.sqrt(_dot(r, r))
        if n < 1e-9:
            r = (1.0, 0.0, 0.0)
        else:
            r = (r[0] / n, r[1] / n, r[2] / n)
        u = _cross(r, f)
        return f, r, u

    def project(self, alt, az, W, H):
        f, r, u = self.basis()
        v = _enu_from_altaz(alt, az)
        c = max(-1.0, min(1.0, _dot(v, f)))
        if c < -0.5:                       # 背后 120° 以外不画
            return None
        a, b = _dot(v, r), _dot(v, u)
        th = math.acos(c)
        rr = 2.0 * math.tan(th / 2.0)
        hyp = math.hypot(a, b)
        if hyp < 1e-12:
            return (W / 2.0, H / 2.0)
        k = (H / 2.0) / (2.0 * math.tan(self.fov / 4.0 * D2R))
        return (W / 2.0 + rr * (a / hyp) * k, H / 2.0 - rr * (b / hyp) * k)


def draw_phase_disc(canvas, x, y, r, k, pa_deg, lit="#e9e7de", dark="#23272e",
                    outline="#7d838c", tag=None):
    """
    画一个月相圆面。
      k      被照亮比例 0..1
      pa_deg 明亮边缘的方位角 (自屏幕上方起顺时针为正)
    """
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=dark, outline=outline)
    k = max(0.0, min(1.0, k))
    if k <= 0.004:
        return
    if k >= 0.996:
        canvas.create_oval(x - r, y - r, x + r, y + r, fill=lit, outline=outline)
        return
    beta = pa_deg - 90.0
    cb, sb = dcos(beta), dsin(beta)
    pts = []
    N = 40
    for i in range(N + 1):                    # 亮侧半圆
        a = -90.0 + 180.0 * i / N
        pts.append((r * dcos(a), -r * dsin(a)))
    t = r * (1.0 - 2.0 * k)                   # 终结线 (半短轴, 可为负)
    for i in range(N + 1):
        a = 90.0 - 180.0 * i / N
        pts.append((t * dcos(a), -r * dsin(a)))
    flat = []
    for px, py in pts:
        flat += [x + px * cb - py * sb, y + px * sb + py * cb]
    canvas.create_polygon(flat, fill=lit, outline="")
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="", outline=outline)


def moon_events(date_local, lat, lon, tzoff):
    """月出 / 中天 / 月落 (当地标准时)。判据: 视高度 = +0.125° (含视差与半径)。"""
    base = dt.datetime(date_local.year, date_local.month, date_local.day)
    start = base - dt.timedelta(hours=tzoff)
    step = dt.timedelta(minutes=10)
    N = 24 * 6

    def alt_at(t):
        p = EPH.get("月亮", t)
        h0 = 0.7275 * p.hp_arcmin / 60.0 - 0.5667
        a, _ = altaz_from_hadec(norm360(p.gha + lon), p.dec, lat)
        return a - h0

    vals = [(start + step * i, alt_at(start + step * i)) for i in range(N + 1)]

    def refine(t0, t1):
        for _ in range(30):
            tm = t0 + (t1 - t0) / 2
            if (alt_at(t0) < 0) == (alt_at(tm) < 0):
                t0 = tm
            else:
                t1 = tm
        return t0 + (t1 - t0) / 2

    rise = sett = None
    for i in range(N):
        if vals[i][1] < 0 <= vals[i + 1][1]:
            rise = refine(vals[i][0], vals[i + 1][0])
        if vals[i][1] >= 0 > vals[i + 1][1]:
            sett = refine(vals[i][0], vals[i + 1][0])
    tr = None
    prev = None
    for t, _a in vals:
        h = norm180(EPH.get("月亮", t).gha + lon)
        if prev is not None and prev[1] < 0 <= h and (h - prev[1]) < 180:
            t0, t1 = prev[0], t
            for _ in range(30):
                tm = t0 + (t1 - t0) / 2
                if norm180(EPH.get("月亮", tm).gha + lon) < 0:
                    t0 = tm
                else:
                    t1 = tm
            tr = t0 + (t1 - t0) / 2
        prev = (t, h)

    def loc(t):
        return None if t is None else t + dt.timedelta(hours=tzoff)
    return loc(rise), loc(tr), loc(sett)


POLAR_GROUP = {"北极星 Polaris", "北极二 Kochab", "十字架二 Acrux",
               "十字架三 Mimosa", "十字架一 Gacrux", "十字架四 Imai",
               "十字架五 εCru"}


class SkyTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master, padding=6)
        self.app = app
        self.clock = TimeEngine()
        self.cam = SkyCam()
        self._lun_cache = {}
        self._strip_cache = {}
        self._mev_cache = {}
        self._oct_cache = {}
        self._hover = {"strip": None, "diag": None, "orbit": None}
        self.stars = []
        self._load_stars()
        self._build()
        self._bind_mouse()
        self.after(200, self._tick)

    # -- 星表 --
    def _load_stars(self):
        import os
        self.stars = list(BUILTIN_STARS)          # 先放内置亮星
        self.star_file = None
        for name in ("stars.csv", "star_catalogue.csv", "星表.csv"):
            for base in (os.path.dirname(os.path.abspath(__file__)), os.getcwd()):
                p = os.path.join(base, name)
                if os.path.exists(p):
                    extra = load_star_catalogue(p)
                    if extra:
                        self.stars = list(BUILTIN_STARS) + extra
                        self.star_file = p
                        return

    # -- 界面 --
    def _build(self):
        scroll = VScrollFrame(self, width=452)
        scroll.pack(side="right", fill="y")
        right = scroll.body
        left = ttk.Frame(self)
        left.pack(side="left", fill="both", expand=True)

        self.info = tk.Text(left, height=9, bg="#0d1117", fg="#d8e0e8",
                            font=self.app.mono_font, relief="flat", wrap="word")
        self.info.pack(side="bottom", fill="x")
        self.info.configure(state="disabled")
        self.canvas = tk.Canvas(left, bg="#05070c", highlightthickness=0,
                                width=560, height=520)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.redraw())

        # ---- 地点 ----
        f1 = ttk.LabelFrame(right, text=" 观测地点 ", padding=6)
        f1.pack(fill="x", pady=(0, 5))
        self.city_var = tk.StringVar(value=CITIES[DEFAULT_CITY][0])
        cb = ttk.Combobox(f1, textvariable=self.city_var, width=28, state="readonly",
                          values=[c[0] for c in CITIES] + ["自定义 Custom"])
        cb.grid(row=0, column=0, columnspan=4, sticky="we")
        cb.bind("<<ComboboxSelected>>", self._on_city)
        self.lat_var = tk.StringVar(value="%.4f" % CITIES[DEFAULT_CITY][1])
        self.lon_var = tk.StringVar(value="%.4f" % CITIES[DEFAULT_CITY][2])
        self.tz_var = tk.StringVar(value="%.2f" % CITIES[DEFAULT_CITY][3])
        ttk.Label(f1, text="纬度 φ").grid(row=1, column=0, sticky="w")
        ttk.Entry(f1, textvariable=self.lat_var, width=11).grid(row=1, column=1)
        ttk.Label(f1, text="经度 λ").grid(row=1, column=2, sticky="w", padx=(6, 0))
        ttk.Entry(f1, textvariable=self.lon_var, width=11).grid(row=1, column=3)
        ttk.Label(f1, text="时区 UTC±").grid(row=2, column=0, sticky="w")
        ttk.Entry(f1, textvariable=self.tz_var, width=11).grid(row=2, column=1)
        ttk.Button(f1, text="按经度取时区", command=self._tz_from_lon).grid(
            row=2, column=2, columnspan=2, sticky="we", padx=(6, 0))

        # ---- 时间 ----
        f2 = ttk.LabelFrame(right, text=" 时间 (默认随真实时间走) ", padding=6)
        f2.pack(fill="x", pady=(0, 5))
        tr = ttk.Frame(f2)
        tr.grid(row=0, column=0, columnspan=4, sticky="we")
        self.pause_btn = ttk.Button(tr, text="⏸ 暂停", width=8,
                                    command=self._toggle_pause)
        self.pause_btn.pack(side="left")
        self.speed_var = tk.StringVar(value=SPEEDS[0][0])
        cbs = ttk.Combobox(tr, textvariable=self.speed_var, width=8, state="readonly",
                           values=[s[0] for s in SPEEDS])
        cbs.pack(side="left", padx=(4, 0))
        cbs.bind("<<ComboboxSelected>>", self._on_speed)
        ttk.Button(tr, text="回到现在", width=8,
                   command=self._go_now).pack(side="left", padx=(4, 0))
        self.date_var = tk.StringVar()
        self.time_var = tk.StringVar()
        ttk.Label(f2, text="日期").grid(row=1, column=0, sticky="w", pady=(4, 0))
        self.date_ent = ttk.Entry(f2, textvariable=self.date_var, width=12)
        self.date_ent.grid(row=1, column=1, sticky="w", pady=(4, 0))
        ttk.Label(f2, text="时刻").grid(row=1, column=2, sticky="w", padx=(6, 0))
        self.time_ent = ttk.Entry(f2, textvariable=self.time_var, width=10)
        self.time_ent.grid(row=1, column=3, sticky="w")
        ttk.Button(f2, text="跳到该时刻", command=self._jump_to).grid(
            row=2, column=0, columnspan=4, sticky="we", pady=3)
        nb2 = ttk.Frame(f2)
        nb2.grid(row=3, column=0, columnspan=4, sticky="we")
        for txt, d in (("−1日", -1440), ("−1时", -60), ("−10分", -10),
                       ("+10分", 10), ("+1时", 60), ("+1日", 1440)):
            ttk.Button(nb2, text=txt, width=6,
                       command=lambda dd=d: self._nudge(dd)).pack(side="left")
        f2.columnconfigure(3, weight=1)

        # ---- 显示 ----
        f3 = ttk.LabelFrame(right, text=" 显示 ", padding=6)
        f3.pack(fill="x", pady=(0, 5))
        self.sh_grid = tk.BooleanVar(value=True)
        self.sh_ecl = tk.BooleanVar(value=True)
        self.sh_label = tk.BooleanVar(value=True)
        self.sh_mag = tk.BooleanVar(value=True)
        self.sh_qiyao = tk.BooleanVar(value=True)     # 七曜: 日月五星
        self.sh_polar = tk.BooleanVar(value=True)     # 北极星 + 南十字
        self.sh_other = tk.BooleanVar(value=False)    # 其余亮星
        ttk.Checkbutton(f3, text="七曜 (日月五星)", variable=self.sh_qiyao,
                        command=self.redraw).grid(row=0, column=0, sticky="w")
        ttk.Checkbutton(f3, text="北极星 · 南十字", variable=self.sh_polar,
                        command=self.redraw).grid(row=0, column=1, sticky="w")
        ttk.Checkbutton(f3, text="其余亮星 (点开才显示)", variable=self.sh_other,
                        command=self.redraw).grid(row=1, column=0, columnspan=2, sticky="w")
        ttk.Separator(f3, orient="horizontal").grid(row=2, column=0, columnspan=2,
                                                    sticky="we", pady=3)
        ttk.Checkbutton(f3, text="地平网格", variable=self.sh_grid).grid(row=3, column=0, sticky="w")
        ttk.Checkbutton(f3, text="黄道", variable=self.sh_ecl).grid(row=3, column=1, sticky="w")
        ttk.Checkbutton(f3, text="名称", variable=self.sh_label).grid(row=4, column=0, sticky="w")
        ttk.Checkbutton(f3, text="放大日月行星(便于看月相)", variable=self.sh_mag).grid(
            row=4, column=1, sticky="w")
        ttk.Button(f3, text="一键回正 (面向北看地面)", command=self._reset_view).grid(
            row=5, column=0, columnspan=2, sticky="we", pady=(4, 0))
        ttk.Button(f3, text="看月亮", command=self._look_moon).grid(row=6, column=0, sticky="we", pady=(3, 0))
        ttk.Button(f3, text="看太阳", command=self._look_sun).grid(row=6, column=1, sticky="we", pady=(3, 0))
        ttk.Label(f3, text="按住左键拖动看天, 松开固定; 滚轮缩放视场; 点天体看资料",
                  foreground="#5f7c93").grid(row=7, column=0, columnspan=2, sticky="w")
        if self.star_file:
            ttk.Label(f3, text=_T("恒星: 内置 %d 颗 + %s 共 %d 颗")
                      % (len(BUILTIN_STARS), self.star_file.split("/")[-1],
                         len(self.stars)),
                      foreground="#7f9bb3").grid(row=8, column=0, columnspan=2, sticky="w")
        else:
            ttk.Label(f3, text=_T("恒星: 内置 %d 颗亮星(含北极星/南十字)。放 stars.csv 可加更多")
                      % len(BUILTIN_STARS),
                      foreground="#5f7c93").grid(row=8, column=0, columnspan=2, sticky="w")
        ttk.Button(f3, text="看北极星", command=lambda: self._look_at("北极星 Polaris")).grid(
            row=9, column=0, sticky="we", pady=(3, 0))
        ttk.Button(f3, text="看南十字", command=lambda: self._look_at("十字架二 Acrux")).grid(
            row=9, column=1, sticky="we", pady=(3, 0))

        # ---- 月相定向 (南北半球月相的明暗方向是反的) ----
        orf = ttk.Frame(right)
        orf.pack(fill="x", pady=(4, 2))
        ttk.Label(orf, text="月相定向:", foreground="#8fb3d0").pack(side="left")
        self.moon_orient = tk.StringVar(value="obs")
        for txt, val in (("观测者所见 (含南北半球翻转)", "obs"),
                         ("天球定向 (北天极朝上)", "cel")):
            ttk.Radiobutton(orf, text=txt, value=val, variable=self.moon_orient,
                            command=self.redraw).pack(side="left", padx=(6, 0))

        # ---- 月相三页 ----
        nbk = ttk.Notebook(right)
        self.nbk = nbk
        nbk.pack(fill="both", expand=True)
        self.p_strip = tk.Canvas(nbk, bg="#05070c", highlightthickness=0, height=330)
        self.p_diag = tk.Canvas(nbk, bg="#071018", highlightthickness=0, height=360)
        self.p_orbit = tk.Canvas(nbk, bg="#071018", highlightthickness=0, height=360)
        self.p_text = tk.Text(nbk, bg="#0d1117", fg="#d8e0e8",
                              font=self.app.mono_font, relief="flat", wrap="word")
        nbk.add(self.p_strip, text=" 本月月相 ")
        nbk.add(self.p_diag, text=" 月相成因 ")
        nbk.add(self.p_orbit, text=" 轨道展开 ")
        nbk.add(self.p_text, text=" 朔望周期 ")
        self.p_text.configure(state="disabled")
        self.p_strip.bind("<Button-1>", self._strip_click)
        for cv, key in ((self.p_strip, "strip"), (self.p_diag, "diag"),
                        (self.p_orbit, "orbit")):
            cv.bind("<Configure>", lambda e: self.redraw())
            cv.bind("<Motion>", lambda e, k=key: self._on_hover(k, e))
            cv.bind("<Leave>", lambda e, k=key: self._on_hover(k, None))
        nbk.bind("<<NotebookTabChanged>>", lambda e: self.redraw())

        t = self.local_time()
        self.date_var.set(t.strftime("%Y-%m-%d"))
        self.time_var.set(t.strftime("%H:%M:%S"))

    def _bind_mouse(self):
        c = self.canvas
        self._drag = None
        self._press_xy = None
        self._moved = 0.0
        self.dragging = False
        self.selected = None
        self._sky_hits = []

        def press(e):
            self.dragging = True
            self._drag = (e.x, e.y)
            self._press_xy = (e.x, e.y)
            self._moved = 0.0

        def drag(e):
            if not self._drag:
                return
            dx, dy = e.x - self._drag[0], e.y - self._drag[1]
            self._moved += abs(dx) + abs(dy)
            self._drag = (e.x, e.y)
            k = self.cam.fov / 700.0
            self.cam.orbit(-dx * k, dy * k)
            self.redraw()

        def rel(e):
            self.dragging = False
            self._drag = None
            if self._moved < 5:                 # 视为"点选"
                self._pick(e.x, e.y)
            self.redraw()

        c.bind("<ButtonPress-1>", press)
        c.bind("<B1-Motion>", drag)
        c.bind("<ButtonRelease-1>", rel)
        c.bind("<MouseWheel>", lambda e: (self.cam.zoom(1 / 1.15 if e.delta > 0 else 1.15),
                                          self.redraw()))
        c.bind("<Button-4>", lambda e: (self.cam.zoom(1 / 1.15), self.redraw()))
        c.bind("<Button-5>", lambda e: (self.cam.zoom(1.15), self.redraw()))

    # -- 参数 --
    def params(self):
        try:
            lat = float(self.lat_var.get())
            lon = float(self.lon_var.get())
            tz = float(self.tz_var.get())
        except ValueError:
            return 3.139, 101.6869, 8.0
        return max(-89.9, min(89.9, lat)), lon, tz

    def local_time(self):
        return self.clock.local(self.params()[2])

    def _on_city(self, *_):
        for c in CITIES:
            if c[0] == self.city_var.get():
                self.lat_var.set("%.4f" % c[1])
                self.lon_var.set("%.4f" % c[2])
                self.tz_var.set("%.2f" % c[3])
                break
        self._lun_cache.clear()
        self._strip_cache.clear()
        self.redraw()

    def _tz_from_lon(self):
        try:
            self.tz_var.set("%.2f" % round(float(self.lon_var.get()) / 15.0))
        except ValueError:
            pass
        self.redraw()

    def _toggle_pause(self):
        paused = self.clock.toggle_pause()
        self.pause_btn.configure(text="▶ 继续" if paused else "⏸ 暂停")
        self.redraw()

    def _on_speed(self, *_):
        for name, val in SPEEDS:
            if name == self.speed_var.get():
                self.clock.speed = val
                break

    def _go_now(self):
        self.clock.now()
        self.clock.speed = 1.0
        self.speed_var.set(SPEEDS[0][0])
        self.redraw()

    def _jump_to(self):
        tz = self.params()[2]
        try:
            d = dt.datetime.strptime(self.date_var.get().strip(), "%Y-%m-%d")
            parts = self.time_var.get().strip().split(":")
            hh = int(parts[0])
            mm = int(parts[1]) if len(parts) > 1 else 0
            ss = float(parts[2]) if len(parts) > 2 else 0.0
            self.clock.set_local(d + dt.timedelta(hours=hh, minutes=mm, seconds=ss), tz)
        except Exception:
            messagebox.showwarning("时刻格式", "日期 2026-08-30, 时刻 21:30:00")
            return
        self.redraw()

    def _nudge(self, minutes):
        self.clock.jump(dt.timedelta(minutes=minutes))
        self.redraw()

    def _look_at(self, body, keep_zoom=False):
        lat, lon, tz = self.params()
        p = EPH.get(body, self.clock.utc())
        alt, az = altaz_from_hadec(norm360(p.gha + lon), p.dec, lat)
        self.cam.az = az
        self.cam.alt = max(self.cam.ALT_MIN, min(self.cam.ALT_MAX, alt))
        if not keep_zoom and self.cam.fov < 40.0:
            self.cam.fov = 50.0            # 放大过头时自动退回看得见的视场
        self.selected = body
        self.redraw()

    def _reset_view(self):
        """一键回正: 面向北、看到地面, 右东左西。"""
        self.cam.az = 0.0
        self.cam.alt = 20.0
        self.cam.fov = 120.0
        self.selected = None
        self.redraw()

    def _look_moon(self):
        self._look_at("月亮")

    def _look_sun(self):
        self._look_at("太阳")

    def _strip_click(self, e):
        """点月相表里的某一天 -> 跳到那一天的同一时刻。"""
        info = getattr(self, "_strip_hit", None)
        if not info:
            return
        for x, y, r, payload in info:
            if (e.x - x) ** 2 + (e.y - y) ** 2 <= (r + 10) ** 2:
                t = payload[1] if isinstance(payload, tuple) else payload
                # 保持一天里的同一时刻, 只换日期
                cur = self.clock.utc()
                t = dt.datetime.combine(t.date(), cur.time())
                self.clock.set_utc(t)
                self.redraw()
                return


    def _pick(self, x, y):
        best, bd = None, 26.0 ** 2
        for hx, hy, name, kind in getattr(self, "_sky_hits", []):
            d = (hx - x) ** 2 + (hy - y) ** 2
            if d < bd:
                bd, best = d, name
        self.selected = best
        self._ev_cache = {}

    def _object_info(self, name, utc, lat, lon, tz):
        """选中天体的详细资料 (Stellarium 式)。"""
        p = EPH.get(name, utc)
        jd_ut = julian_day(utc)
        jd_tt = jd_ut + delta_t_seconds(utc) / 86400.0
        eps = true_obliquity(jd_tt)
        lam, bet = equ_to_ecl(p.ra, p.dec, eps)
        lha = norm360(p.gha + lon)
        alt_geo, az = altaz_from_hadec(lha, p.dec, lat)
        par = (p.hp_arcmin / 60.0) * dcos(alt_geo)
        alt_topo = alt_geo - par
        refr = refraction_true_to_app(alt_topo) if alt_topo > -2 else 0.0
        alt_app = alt_topo + refr / 60.0
        L = []
        A = L.append
        star = (p.kind == "star")
        A(_T("【选中】%s%s      (点空白处取消选择)")
          % (name, "  恒星" if star else ""))
        A(_T("  视赤经 α = %s      视赤纬 δ = %s   (当日真分点)")
          % (hm_from_hours(p.ra / 15.0), deg_dm(p.dec, "N", "S")))
        A(_T("  视黄经 λ = %s      视黄纬 β = %s")
          % (deg_dm(lam, "+", "-"), deg_dm(bet, "N", "S")))
        A(_T("  地平坐标: 高度 %+.4f° (视 %+.4f°, 蒙气差 %.2f′)   方位 %.3f° (%s)")
          % (alt_topo, alt_app, refr, az_fmt(az, 3), _az_name(az)))
        A(_T("  格林时角 GHA %.4f°   地方时角 LHA %.4f° (%+.3f h)")
          % (p.gha, norm180(lha), norm180(lha) / 15.0))
        if star:
            nm, ra0, dec0, mag = STAR_BY_NAME[name]
            lam0, bet0 = equ_to_ecl(ra0, dec0, mean_obliquity(0.0))
            A(_T("  J2000: α=%s δ=%s   λ=%s β=%s   视星等 %.2f")
              % (hm_from_hours(ra0 / 15.0), deg_dm(dec0, "N", "S"),
                 deg_dm(lam0, "+", "-"), deg_dm(bet0, "N", "S"), mag))
            A(_T("  恒星时角 SHA = %.4f°  (航海历用 GHA = GHA白羊 + SHA)")
              % az_fmt(360.0 - p.ra, 4))
        else:
            A(_T("  距离 %.0f km = %.6f AU   视半径 %.3f′   地平视差 %.3f′")
              % (p.dist_km, p.dist_km / AU_KM, p.sd_arcmin, p.hp_arcmin))
            extra = ""
            if name in ("月亮", "水星", "金星", "火星"):
                extra = _T("   相位角 %.2f°  被照亮 %.2f%%") % (p.phase, p.illum * 100.0)
            A("  %s%s" % (("月相: " + phase_name(elongation_deg(utc)))
                          if name == "月亮" else "", extra))
        key = (name, (utc + dt.timedelta(hours=tz)).date(), round(lat, 3),
               round(lon, 3))
        if key not in getattr(self, "_ev_cache", {}):
            self._ev_cache = {key: body_events(name, key[1], lat, lon, tz)}
        r, tr, st = self._ev_cache[key]
        A(_T("  今日: 升 %s   中天 %s   落 %s   (当地标准时)")
          % (fmt_hm(r), fmt_hm(tr), fmt_hm(st)))
        return L


    def octants(self, lun):
        key = lun["new0"] if lun else None
        if key is None:
            return None
        if key not in self._oct_cache:
            self._oct_cache.clear()
            self._oct_cache[key] = lunation_octants(lun)
        return self._oct_cache[key]

    def _on_hover(self, which, e):
        if e is None:
            self._hover[which] = None
        else:
            self._hover[which] = (e.x, e.y)
        self.redraw()

    def _tip(self, canvas, which, hits, lines_fn):
        """在某个画布上按命中区域画提示框。hits: [(x,y,r,payload)]"""
        pos = self._hover.get(which)
        if not pos:
            return
        x, y = pos
        for hx, hy, hr, payload in hits:
            if (x - hx) ** 2 + (y - hy) ** 2 <= (hr + 8) ** 2:
                lines = lines_fn(payload)
                if lines:
                    canvas_tooltip(canvas, x, y, lines, self.app.tip_font,
                                   max(canvas.winfo_width(), 200),
                                   max(canvas.winfo_height(), 200))
                return


    def _octant_lines(self, k, utc, tz):
        idx, total, lun = self.lun_of(utc, tz)
        oct_t = self.octants(lun)
        if not oct_t:
            return None
        t = oct_t[k]
        out = [_T("本轮朔望月的 %s   (视黄经差 %d°)") % (OCTANT_NAMES[k], k * 45)]
        if t is None:
            out.append("(本月内未出现)")
            return out
        loc = t + dt.timedelta(hours=tz)
        pi = moon_phase_info(t)
        out.append(_T("公历 %s   (当地标准时 UTC%+.1f)")
                   % (loc.strftime(_T("%Y年%m月%d日 %H:%M:%S")), tz))
        out.append(_T("世界时 UTC %s") % t.strftime("%Y-%m-%d %H:%M:%S"))
        out.append(_T("此刻被照亮 %.2f%%   农历 %s")
                   % (pi["k"] * 100.0,
                      CN_DAY[min(30, max(1, (loc.date()
                                             - (lun["new0"] + dt.timedelta(hours=tz)).date()).days + 1)) - 1]))
        age = (t - lun["new0"]).total_seconds() / 86400.0
        out.append(_T("距本月朔 %.3f 日 (朔 %s)")
                   % (age, (lun["new0"] + dt.timedelta(hours=tz)).strftime("%m-%d %H:%M")))
        return out

    # -- 主循环 --
    def _tick(self):
        self.clock.tick()
        if not self.winfo_ismapped():          # 不在当前页签就不画
            self.after(400, self._tick)
            return
        try:
            foc = self.focus_get()
        except Exception:
            foc = None
        if foc not in (self.date_ent, self.time_ent):
            t = self.local_time()
            self.date_var.set(t.strftime("%Y-%m-%d"))
            self.time_var.set(t.strftime("%H:%M:%S"))
        self.redraw()
        self.after(250, self._tick)

    # -- 缓存 --
    def lun_of(self, utc, tz):
        key = (utc + dt.timedelta(hours=tz)).date()
        if key not in self._lun_cache:
            self._lun_cache.clear()
            self._lun_cache[key] = lunar_day_index(utc, tz)
        return self._lun_cache[key]

    # ===================================================================
    #  星空绘制
    # ===================================================================
    def redraw(self):
        lat, lon, tz = self.params()
        utc = self.clock.utc()
        c = self.canvas
        c.delete("all")
        W = max(c.winfo_width(), 200)
        H = max(c.winfo_height(), 200)
        sun = EPH.get("太阳", utc)
        sun_alt, _sa = altaz_from_hadec(norm360(sun.gha + lon), sun.dec, lat)

        # 天空底色 (随太阳高度变化)
        if sun_alt > 0:
            sky = "#4b7fb5"
        elif sun_alt > -6:
            sky = "#2c4a70"
        elif sun_alt > -12:
            sky = "#16263c"
        elif sun_alt > -18:
            sky = "#0b1522"
        else:
            sky = "#05070c"
        c.create_rectangle(0, 0, W, H, fill=sky, outline="")

        proj = lambda a, z: self.cam.project(a, z, W, H)

        # 地平网格
        if self.sh_grid.get():
            for alt in (15, 30, 45, 60, 75):
                pts = []
                for az in range(0, 366, 6):
                    p = proj(alt, az % 360)
                    if p:
                        pts += [p[0], p[1]]
                    elif len(pts) >= 4:
                        c.create_line(pts, fill="#1f3346")
                        pts = []
                if len(pts) >= 4:
                    c.create_line(pts, fill="#1f3346")
            for az in range(0, 360, 30):
                pts = []
                for alt in range(0, 89, 3):
                    p = proj(alt, az)
                    if p:
                        pts += [p[0], p[1]]
                if len(pts) >= 4:
                    c.create_line(pts, fill="#1f3346")

        # 黄道
        if self.sh_ecl.get():
            jd_ut = julian_day(utc)
            jd_tt = jd_ut + delta_t_seconds(utc) / 86400.0
            eps = true_obliquity(jd_tt)
            gast = gha_aries(utc)
            pts = []
            for lam in range(0, 366, 3):
                ra = norm360(math.degrees(math.atan2(dsin(lam) * dcos(eps), dcos(lam))))
                de = math.degrees(math.asin(dsin(eps) * dsin(lam)))
                a2, z2 = altaz_from_hadec(norm360(gast - ra + lon), de, lat)
                p = proj(a2, z2)
                if p:
                    pts += [p[0], p[1]]
                elif len(pts) >= 4:
                    c.create_line(pts, fill="#4a3f6b", dash=(4, 3))
                    pts = []
            if len(pts) >= 4:
                c.create_line(pts, fill="#4a3f6b", dash=(4, 3))

        # 地面(地平线以下): 用小四边形铺满 —— 无论抬头低头都不会填反
        GND = "#23595f"                       # 浅青: 一眼看出这是"地下"
        for i in range(6):
            aa0 = -15.0 * i
            aa1 = -15.0 * (i + 1)
            for j in range(0, 360, 12):
                q = [proj(aa0, j), proj(aa0, (j + 12) % 360),
                     proj(aa1, (j + 12) % 360), proj(aa1, j)]
                if any(p is None for p in q):
                    continue
                xs = [p[0] for p in q]
                ys = [p[1] for p in q]
                if (max(xs) - min(xs)) > W * 1.5 or (max(ys) - min(ys)) > H * 1.5:
                    continue
                if max(xs) < -20 or min(xs) > W + 20 or max(ys) < -20 or min(ys) > H + 20:
                    continue
                flat = []
                for p in q:
                    flat += [p[0], p[1]]
                c.create_polygon(flat, fill=GND, outline="")
        # 地下的虚线网格 (画在地面之上才看得见)
        if self.sh_grid.get():
            for alt in (-15, -30, -45, -60, -75):
                pts = []
                for az in range(0, 366, 6):
                    p = proj(alt, az % 360)
                    if p and abs(p[0]) < 6 * W and abs(p[1]) < 6 * H:
                        pts += [p[0], p[1]]
                    elif len(pts) >= 4:
                        c.create_line(pts, fill="#5fc8c8", dash=(3, 4))
                        pts = []
                if len(pts) >= 4:
                    c.create_line(pts, fill="#5fc8c8", dash=(3, 4))
            for az in range(0, 360, 30):
                pts = []
                for alt in range(-88, 1, 4):
                    p = proj(alt, az)
                    if p and abs(p[0]) < 6 * W and abs(p[1]) < 6 * H:
                        pts += [p[0], p[1]]
                if len(pts) >= 4:
                    c.create_line(pts, fill="#4bb0b0", dash=(2, 5))
        # 地平线 (青色加粗)
        seg = []
        segs = []
        for az in range(0, 363, 2):
            p = proj(0.0, az % 360)
            if p is None or abs(p[0]) > 6 * W or abs(p[1]) > 6 * H:
                if len(seg) > 2:
                    segs.append(seg)
                seg = []
            else:
                if seg and abs(p[0] - seg[-1][0]) > W:
                    if len(seg) > 2:
                        segs.append(seg)
                    seg = []
                seg.append(p)
        if len(seg) > 2:
            segs.append(seg)
        for sg in segs:
            line = []
            for x, y in sg:
                line += [x, y]
            c.create_line(line, fill="#00e5e5", width=3)

        # 方位标记
        for az, lbl, main in ((0, "北 N", 1), (45, "东北 NE", 0), (90, "东 E", 1),
                              (135, "东南 SE", 0), (180, "南 S", 1),
                              (225, "西南 SW", 0), (270, "西 W", 1),
                              (315, "西北 NW", 0)):
            p = proj(1.2, az)
            if p and -60 < p[0] < W + 60 and -60 < p[1] < H + 60:
                c.create_text(p[0] + 1, p[1] + 1, text=lbl, fill="#04202a",
                              font=self.app.dir_font)
                c.create_text(p[0], p[1], text=lbl,
                              fill="#ffd257" if main else "#5ff0f0",
                              font=self.app.dir_font)

        # 恒星 (分组: 北极星/南十字 与 其余亮星)
        self._sky_hits = []
        if self.stars and (self.sh_polar.get() or self.sh_other.get()):
            jd_tt = julian_day(utc) + delta_t_seconds(utc) / 86400.0
            gast = gha_aries(utc)
            for nm, ra0, de0, mag in self.stars:
                if mag > 5.0:
                    continue
                grp = POLAR_GROUP if nm in POLAR_GROUP else None
                if grp:
                    if not self.sh_polar.get():
                        continue
                elif not self.sh_other.get():
                    continue
                ra, de = precess_j2000(ra0, de0, jd_tt)
                a2, z2 = altaz_from_hadec(norm360(gast - ra + lon), de, lat)
                if a2 < -1:
                    continue
                p = proj(a2, z2)
                if not p or not (0 < p[0] < W and 0 < p[1] < H):
                    continue
                rr = max(0.8, 3.4 - 0.55 * mag)
                c.create_oval(p[0] - rr, p[1] - rr, p[0] + rr, p[1] + rr,
                              fill="#e8eef8", outline="")
                if nm:
                    self._sky_hits.append((p[0], p[1], nm, "star"))
                if self.sh_label.get() and (mag < 2.2 or nm in STAR_BY_NAME) and nm:
                    c.create_text(p[0] + 8, p[1] - 6, text=nm.split(" ")[0],
                                  anchor="w", fill="#8fa9bf", font=self.app.ui_font)

        # 日月行星
        # 放大到一定程度就按真实视直径画 (像 Stellarium 那样)
        mag_k = 3.0 if (self.sh_mag.get() and self.cam.fov > 25) else 1.0
        scale = (H / 2.0) / (2.0 * math.tan(self.cam.fov / 4.0 * D2R))
        for body in (SKY_BODIES if self.sh_qiyao.get() else []):
            p = EPH.get(body, utc)
            a2, z2 = altaz_from_hadec(norm360(p.gha + lon), p.dec, lat)
            refr = refraction_true_to_app(a2) / 60.0 if a2 > -2 else 0.0
            a2 += refr
            q = proj(a2, z2)
            if not q:
                continue
            rr = p.sd_arcmin / 60.0 * D2R * scale * mag_k
            col = BODY_COLOR.get(body, "#ffffff")
            if body == "月亮":
                info = moon_phase_info(utc)
                pa = self._limb_screen_pa(p, info["chi"], lat, lon, q, proj)
                rr = max(9.0, rr)
                draw_phase_disc(c, q[0], q[1], rr, info["k"], pa,
                                lit="#efeee6", dark="#1b1f26", outline="#6a707a")
            else:
                rr = max(2.0 if body != "太阳" else 6.0, rr)
                if body == "太阳":
                    c.create_oval(q[0] - rr * 1.6, q[1] - rr * 1.6,
                                  q[0] + rr * 1.6, q[1] + rr * 1.6,
                                  fill="", outline="#ffe9a8")
                c.create_oval(q[0] - rr, q[1] - rr, q[0] + rr, q[1] + rr,
                              fill=col, outline="")
            self._sky_hits.append((q[0], q[1], body, "body"))
            if self.sh_label.get():
                c.create_text(q[0] + rr + 6, q[1] - rr - 4, text=body, anchor="w",
                              fill=col, font=self.app.ui_font)

        # 选中标记
        if self.selected:
            for hx, hy, nm, kd in self._sky_hits:
                if nm == self.selected:
                    c.create_oval(hx - 16, hy - 16, hx + 16, hy + 16,
                                  outline="#ffd257", width=2)
                    for a in (0, 90, 180, 270):
                        c.create_line(hx + 20 * dsin(a), hy - 20 * dcos(a),
                                      hx + 28 * dsin(a), hy - 28 * dcos(a),
                                      fill="#ffd257")
                    break

        # HUD
        state = "拖动中…" if self.dragging else "已固定"
        c.create_text(10, 12, anchor="w", font=self.app.ui_font_b, fill="#8fb3d0",
                      text=_T("视线 %s: 方位 %.1f° (%s)   高度 %+.1f°   视场 %.0f°")
                           % (state, self.cam.az, _az_name(self.cam.az),
                              self.cam.alt, self.cam.fov))
        c.create_text(10, 30, anchor="w", font=self.app.ui_font, fill="#5f7c93",
                      text="按住左键拖动改变视角, 松开即固定; 滚轮缩放视场")
        lt = self.local_time()
        c.create_text(W - 10, 12, anchor="e", font=self.app.ui_font_b, fill="#8fb3d0",
                      text="%s  (UTC%+.1f)  φ=%s λ=%s"
                           % (lt.strftime("%Y-%m-%d %H:%M:%S"), tz,
                              deg_dm(lat, "N", "S"), deg_dm(lon, "E", "W")))

        self._update_info(utc, lat, lon, tz)
        self._draw_strip(utc, tz)
        self._draw_diagram(utc, tz)


    def _limb_screen_pa(self, pos, chi, lat, lon, q0, proj):
        """
        把"明亮边缘方位角 χ"(自天北极经天东量) 换算成屏幕上的方位角
        (自屏幕上方顺时针)。做法: 把天球的北向与东向分别投影到屏幕再合成,
        这样无论投影是否镜像、视差角多少, 结果都自动正确。
        """
        d = 0.4
        lha0 = norm360(pos.gha + lon)
        an, zn = altaz_from_hadec(lha0, min(89.5, pos.dec + d), lat)
        pn = proj(an, zn)
        # 天东 = 赤经增大的方向 => 地方时角减小
        ae, ze = altaz_from_hadec(norm360(lha0 - d / max(0.02, dcos(pos.dec))),
                                  pos.dec, lat)
        pe = proj(ae, ze)
        if not pn or not pe:
            return 0.0
        nx, ny = pn[0] - q0[0], pn[1] - q0[1]
        ex, ey = pe[0] - q0[0], pe[1] - q0[1]
        ln = math.hypot(nx, ny) or 1.0
        le = math.hypot(ex, ey) or 1.0
        nx, ny = nx / ln, ny / ln
        ex, ey = ex / le, ey / le
        dx = dcos(chi) * nx + dsin(chi) * ex
        dy = dcos(chi) * ny + dsin(chi) * ey
        return math.degrees(math.atan2(dx, -dy))

    # ===================================================================
    #  左下角信息
    # ===================================================================
    def _update_info(self, utc, lat, lon, tz):
        if self.selected:
            try:
                L = self._object_info(self.selected, utc, lat, lon, tz)
            except Exception as ex:
                L = [_T("选中 %s 时出错: %s") % (self.selected, ex)]
            self.info.configure(state="normal")
            self.info.delete("1.0", "end")
            self.info.insert("1.0", "\n".join(L))
            self.info.configure(state="disabled")
            return
        info = moon_phase_info(utc)
        m = info["moon"]
        idx, total, lun = self.lun_of(utc, tz)
        lha = norm360(m.gha + lon)
        alt, az = altaz_from_hadec(lha, m.dec, lat)
        L = []
        A = L.append
        A(_T("【月亮】视赤经 %s  视赤纬 %s   地平: 高度 %+.3f°  方位 %.2f°")
          % (hm_from_hours(m.ra / 15.0), deg_dm(m.dec, "N", "S"), alt, az_fmt(az, 2)))
        A(_T("        月地距离 %.0f km   视半径 %.2f′   地平视差 %.2f′")
          % (m.dist_km, m.sd_arcmin, m.hp_arcmin))
        A(_T("【月相】视黄经差(月−日) %.3f°   相位角 %.2f°   被照亮 %.1f%%   %s")
          % (info["elong"], info["i"], info["k"] * 100.0, phase_name(info["elong"])))
        A(_T("        明亮边缘方位角 χ = %.1f° (自天北极向东) —— 决定月牙朝哪边") % info["chi"])
        if idx:
            A(_T("【农历】本朔望月第 %d 天 = %s   (本月共 %d 天)")
              % (idx, CN_DAY[min(idx, 30) - 1], total))
        su = info["sun"]
        salt, saz = altaz_from_hadec(norm360(su.gha + lon), su.dec, lat)
        A(_T("【太阳】高度 %+.3f°  方位 %.2f°   %s")
          % (salt, az_fmt(saz, 2), "白天" if salt > -0.833 else
             ("民用晨昏蒙影" if salt > -6 else
              ("航海晨昏蒙影" if salt > -12 else
               ("天文晨昏蒙影" if salt > -18 else "天文夜")))))
        self.info.configure(state="normal")
        self.info.delete("1.0", "end")
        self.info.insert("1.0", "\n".join(L))
        self.info.configure(state="disabled")

    # ===================================================================
    #  本月月相表 (图一)
    # ===================================================================
    def _draw_strip(self, utc, tz):
        c = self.p_strip
        c.delete("all")
        W = max(c.winfo_width(), 260)
        H = max(c.winfo_height(), 220)
        idx, total, lun = self.lun_of(utc, tz)
        if not lun:
            return
        key = (lun["new0"].date(), round(tz, 2))
        if key not in self._strip_cache:
            self._strip_cache.clear()
            days = []
            d0 = (lun["new0"] + dt.timedelta(hours=tz)).date()
            lat_s, lon_s, _tz_s = self.params()
            for i in range(total):
                loc_noon = dt.datetime(d0.year, d0.month, d0.day) + \
                    dt.timedelta(days=i, hours=12)
                t = loc_noon - dt.timedelta(hours=tz)
                pi = moon_phase_info(t)
                mo = pi["moon"]
                q = parallactic_angle(norm360(mo.gha + lon_s), mo.dec, lat_s)
                days.append((i + 1, t, pi["k"], pi["chi"], pi["elong"], q))
            self._strip_cache[key] = days
        days = self._strip_cache[key]

        cols = 6
        rows = (len(days) + cols - 1) // cols
        cw = W / cols
        ch = min(52.0, (H - 42) / max(1, rows))
        r = min(cw * 0.30, ch * 0.36)
        c.create_text(W / 2, 12, text=_T("本朔望月全套月相 (共 %d 天, 各日当地正午)") % total,
                      fill="#8fb3d0", font=self.app.ui_font_b)
        obs = (self.moon_orient.get() == "obs")
        lat_s = self.params()[0]
        c.create_text(W / 2, 27, fill="#5f7c93", font=self.app.ui_font,
                      text=(_T("观测者定向 (%s, 天顶朝上): 各日当地正午时你抬头看到的样子; "
                            "点任一天可跳到那天")
                            % ("南半球" if lat_s < 0 else "北半球")) if obs
                      else "天球定向: 北天极朝上, 天东在左; 点任一天可跳到那天")
        hits = []
        for i, (day, t, k, chi, elong, qq) in enumerate(days):
            cx = cw * (i % cols) + cw / 2
            cy = 44 + ch * (i // cols) + ch / 2
            cur = (day == idx)
            if cur:
                c.create_rectangle(cx - cw / 2 + 2, cy - ch / 2 + 1,
                                   cx + cw / 2 - 2, cy + ch / 2 - 1,
                                   outline="#c9a227", width=2)
            pa_s = -(chi - qq) if obs else -chi
            draw_phase_disc(c, cx, cy - ch * 0.13, r, k, pa_s,
                            lit="#e9e7de", dark="#1a1e24", outline="#565d66")
            c.create_text(cx, cy + ch * 0.30, text=CN_DAY[min(day, 30) - 1],
                          fill="#c9a227" if cur else "#8fa9bf",
                          font=self.app.ui_font)
            hits.append((cx, cy - ch * 0.13, r, (day, t, k, elong, qq, chi)))
        self._strip_hit = hits
        oct_t = self.octants(lun)

        def strip_lines(payload):
            day, t, k, elong, qq, chi = payload
            loc = t + dt.timedelta(hours=tz)
            out = [_T("%s   公历 %s") % (CN_DAY[min(day, 30) - 1],
                                   loc.strftime("%Y-%m-%d")),
                   _T("当日正午: 照亮 %.1f%%   视黄经差 %.1f°   %s")
                   % (k * 100.0, elong, phase_name(elong)),
                   _T("月龄 %.2f 日") % ((t - lun["new0"]).total_seconds() / 86400.0),
                   _T("明亮边缘 χ %.1f° (自天北极向东量)   视差角 q %.1f°") % (chi, qq),
                   _T("屏幕上明亮边缘朝向 %.1f° (自上方顺时针) —— %s")
                   % (az_fmt(-(chi - qq), 1),
                      "亮在右" if dsin(-(chi - qq)) > 0.15 else
                      ("亮在左" if dsin(-(chi - qq)) < -0.15 else "亮在上/下"))]
            if oct_t:
                same = []
                cur_i, cur_t, nxt = None, None, None
                for i, ot in enumerate(oct_t):
                    if ot is None:
                        continue
                    olo = ot + dt.timedelta(hours=tz)
                    if olo.date() == loc.date():
                        same.append(_T("★ 本日 %s 进入 %s")
                                    % (olo.strftime("%H:%M:%S"), OCTANT_NAMES[i]))
                    if olo <= loc:
                        cur_i, cur_t = i, olo
                    elif nxt is None:
                        nxt = (i, olo)
                if cur_i is None:            # 还没到本月第一个相位
                    cur_i, cur_t = 0, lun["new0"] + dt.timedelta(hours=tz)
                out.append(_T("现处相位: %s   自 %s 起")
                           % (OCTANT_NAMES[cur_i],
                              cur_t.strftime("%Y-%m-%d %H:%M:%S")))
                if nxt:
                    out.append(_T("下一相位: %s   %s")
                               % (OCTANT_NAMES[nxt[0]],
                                  nxt[1].strftime("%Y-%m-%d %H:%M:%S")))
                out += same
            return out
        self._tip(c, "strip", hits, strip_lines)

    # ===================================================================
    #  月相成因图 (图三 + 图二)
    # ===================================================================
    def _draw_diagram(self, utc, tz):
        c = self.p_diag
        c.delete("all")
        W = max(c.winfo_width(), 260)
        H = max(c.winfo_height(), 220)
        info = moon_phase_info(utc)
        elong = info["elong"]

        top_h = H
        cx, cy = W * 0.42, top_h / 2 + 14
        R = min(W * 0.24, (top_h - 70) * 0.30)

        # 太阳光 (自右向左)
        for i in range(7):                      # 阳光箭头自三行说明之下起
            y = 58 + i * (top_h - 84) / 6.0
            c.create_line(W - 4, y, W * 0.845, y, fill="#c9a227", arrow="last",
                          arrowshape=(8, 10, 4))
        # 「← 太阳光」原在第二行说明的右端; 说明太长会撞上, 就挪到第一支箭头底下
        sun_w = text_size(self.app.ui_font_b, "← 太阳光")[0]
        line2 = (_T("内圈 = 从北极上方看的真实明暗;  外圈 = 在%s看到的样子 "
                    "(鼠标指向可看时刻)")
                 % ("南半球" if self.params()[0] < 0 else "北半球"))
        sun_y = (30 if 8 + text_size(self.app.ui_font, line2)[0] < W - 14 - sun_w
                 else 58 + (top_h - 84) / 12.0)        # 挪到头两支箭头之间
        c.create_text(W - 6, sun_y, text="← 太阳光", anchor="e",
                      fill="#e8c56a", font=self.app.ui_font_b)

        # 地球
        c.create_oval(cx - 13, cy - 13, cx + 13, cy + 13, fill="#2b6ea8",
                      outline="#8fb3d0")
        c.create_arc(cx - 13, cy - 13, cx + 13, cy + 13, start=-90, extent=180,
                     fill="#183d5e", outline="")
        c.create_text(cx, cy + 24, text="地球", fill="#8fb3d0",
                      font=self.app.ui_font)
        c.create_oval(cx - R, cy - R, cx + R, cy + R, outline="#3a4d5c", dash=(3, 3))

        names = ["朔·新月", "娥眉月", "上弦月", "盈凸月", "望·满月",
                 "亏凸月", "下弦月", "残月"]
        south = (self.params()[0] < 0)
        hits = []
        for i in range(8):
            e = i * 45.0
            mx = cx + R * dcos(e)
            my = cy - R * dsin(e)
            # 内圈: 从"上方"看的真实明暗 —— 永远朝太阳(右)的一半亮
            c.create_oval(mx - 8, my - 8, mx + 8, my + 8, fill="#20242b",
                          outline="#5a626c")
            c.create_arc(mx - 8, my - 8, mx + 8, my + 8, start=-90, extent=180,
                         fill="#e9e7de", outline="")
            # 外圈: 地球上看到的月相
            ox = cx + (R + 46) * dcos(e)
            oy = cy - (R + 46) * dsin(e)
            k = (1 - dcos(e)) / 2.0
            pa = 90.0 if (dsin(e) >= 0) != south else 270.0
            draw_phase_disc(c, ox, oy, 15, k, pa, lit="#f2f0e8", dark="#12161c",
                            outline="#6a707a")
            c.create_text(ox, oy + 24, text=names[i], fill="#7fbf7f",
                          font=self.app.ui_font)
            hits.append((ox, oy, 17, i))
            hits.append((mx, my, 10, i))
        # 当前位置
        mx = cx + R * dcos(elong)
        my = cy - R * dsin(elong)
        c.create_oval(mx - 12, my - 12, mx + 12, my + 12, outline="#c9a227", width=2)
        c.create_line(cx, cy, mx, my, fill="#c9a227", dash=(3, 3))
        if getattr(self, "_f_small", None) is None:
            self._f_small = _pick_font(self.app.root, CJK_FONTS, 8)
        xr = W - 8 if sun_y != 30 else W - 14 - sun_w
        fit_text(c, 8, 12, "月绕地公转 → 日月夹角变化 → 月相", self.app.ui_font_b,
                 8, W - 8, anchor="w", alt_fonts=(self.app.ui_font,), fill="#8fb3d0")
        fit_text(c, 8, 28, line2, self.app.ui_font, 8, xr, anchor="w",
                 alt_fonts=(self._f_small,), fill="#5f7c93")
        fit_text(c, 8, 44, ("南半球: 盈月亮在「左」, 亏月亮在「右」—— 与北半球正好"
                            "颠倒 (观测者头下脚上地面对同一个月亮)。" if south else
                            "北半球: 盈月亮在「右」, 亏月亮在「左」。到了南半球"
                            "整个明暗方向会左右颠倒。"), self.app.ui_font,
                 8, W - 8, anchor="w", alt_fonts=(self._f_small,), fill="#7fbf7f")
        self._tip(c, "diag", hits, lambda k: self._octant_lines(k, utc, tz))

        self._draw_orbit(utc, tz)

        # ---- 朔望周期文字页 ----
        self._update_cycle_text(utc, tz)


    def _draw_orbit(self, utc, tz):
        """图二式: 沿公转轨道展开 —— 阳光自上方来, 下方是地球上看到的月相。"""
        c = self.p_orbit
        c.delete("all")
        W = max(c.winfo_width(), 260)
        H = max(c.winfo_height(), 260)
        info = moon_phase_info(utc)
        elong = info["elong"]
        names2 = ["朔 · 新月", "娥眉月", "上弦月", "盈凸月",
                  "望 · 满月", "亏凸月", "下弦月", "残月"]
        if getattr(self, "_f_small", None) is None:
            self._f_small = _pick_font(self.app.root, CJK_FONTS, 8)
        fit_text(c, W / 2, 12, "沿公转轨道展开: 阳光一律自上方射来", self.app.ui_font_b,
                 6, W - 6, alt_fonts=(self.app.ui_font, self._f_small), fill="#8fb3d0")
        south = (self.params()[0] < 0)
        fit_text(c, W / 2, 28, _T("上排 = 地月系统 (红圈为月亮轨道), 下方 = 在%s看到的月相")
                 % ("南半球" if south else "北半球"), self.app.ui_font, 6, W - 6,
                 alt_fonts=(self._f_small,), fill="#5f7c93")
        cols, rows = 4, 2
        cw = W / cols
        chh = (H - 52) / rows
        hits = []
        for i in range(8):
            col, row = i % cols, i // cols
            ex = cw * col + cw / 2
            top = 44 + chh * row
            e = i * 45.0
            cur = abs(norm180(elong - e)) < 22.5
            if cur:
                c.create_rectangle(ex - cw / 2 + 3, top - 4, ex + cw / 2 - 3,
                                   top + chh - 6, outline="#c9a227")
            for j in range(3):                      # 阳光
                xx = ex - 14 + j * 14
                c.create_line(xx, top + 2, xx, top + 14, fill="#c9a227",
                              arrow="last", arrowshape=(6, 7, 3))
            rr = min(cw * 0.26, chh * 0.20)
            ey = top + 20 + rr
            c.create_oval(ex - rr, ey - rr, ex + rr, ey + rr, outline="#7a4a4a",
                          dash=(2, 2))
            c.create_oval(ex - 6, ey - 6, ex + 6, ey + 6, fill="#2b6ea8",
                          outline="#8fb3d0")            # 地球
            mx = ex + rr * dsin(e)                     # 朔时月亮朝太阳(上)
            my = ey - rr * dcos(e)
            c.create_oval(mx - 5, my - 5, mx + 5, my + 5, fill="#20242b",
                          outline="#5a626c")
            c.create_arc(mx - 5, my - 5, mx + 5, my + 5, start=0, extent=180,
                         fill="#e9e7de", outline="")   # 朝上(向阳)的一半亮
            k = (1 - dcos(e)) / 2.0
            pa = 90.0 if (dsin(e) >= 0) != south else 270.0
            dr = min(15.0, chh * 0.16)
            dy = ey + rr + dr + 8
            draw_phase_disc(c, ex, dy, dr, k, pa, lit="#f2f0e8",
                            dark="#12161c", outline="#6a707a")
            c.create_text(ex, dy + dr + 10, text=names2[i],
                          fill="#c9a227" if cur else "#7fbf7f",
                          font=self.app.ui_font)
            hits.append((ex, dy, dr + 4, i))
            hits.append((ex, ey, rr, i))
        fit_text(c, W / 2, H - 22,
                 "月绕地一圈 = 一个朔望月 ≈ 29.53 日 (比恒星月 27.32 日长, 因地球同时在绕日走)",
                 self.app.ui_font, 6, W - 6, alt_fonts=(self._f_small,), fill="#7f9bb3")
        fit_text(c, W / 2, H - 8, _T("金框 = 此刻所处的位置 (%s) · 鼠标指向某相位可看它的公历时刻")
                 % phase_name(elong), self.app.ui_font, 6, W - 6,
                 alt_fonts=(self._f_small,), fill="#c9a227")
        self._tip(c, "orbit", hits, lambda k: self._octant_lines(k, utc, tz))

    def _update_cycle_text(self, utc, tz):
        lat, lon, _tz = self.params()
        idx, total, lun = self.lun_of(utc, tz)
        info = moon_phase_info(utc)
        L = []
        A = L.append

        def loc(t):
            return "—" if t is None else (t + dt.timedelta(hours=tz)).strftime(
                "%Y-%m-%d %H:%M:%S")
        A(_T("【本朔望月 (当地标准时 UTC%+.1f)】") % tz)
        if lun:
            A(_T("  朔 (新月)   %s      ← 定为初一") % loc(lun["new0"]))
            A(_T("  上弦        %s") % loc(lun["first"]))
            A(_T("  望 (满月)   %s") % loc(lun["full"]))
            A(_T("  下弦        %s") % loc(lun["last"]))
            A(_T("  下次朔      %s") % loc(lun["new1"]))
            A(_T("  本月长度    %.4f 日  (朔望月平均 29.530589 日)") % lun["length"])
            age = (utc - lun["new0"]).total_seconds() / 86400.0
            A("")
            A("【此刻】")
            A(_T("  月龄        %.3f 日") % age)
            A(_T("  农历日      第 %d 天 = %s   (本月共 %d 天)")
              % (idx, CN_DAY[min(idx, 30) - 1], total))
        A(_T("  月相        %s") % phase_name(info["elong"]))
        A(_T("  视黄经差    %.4f°   相位角 %.3f°   被照亮 %.2f%%")
          % (info["elong"], info["i"], info["k"] * 100.0))
        A(_T("  月地距离    %.1f km   视半径 %.3f′") % (info["moon"].dist_km,
                                                info["moon"].sd_arcmin))
        A("")
        A("【今日月出中天月落 (当地)】")
        try:
            key = ((utc + dt.timedelta(hours=tz)).date(), round(lat, 3),
                   round(lon, 3), round(tz, 2))
            if key not in self._mev_cache:
                self._mev_cache.clear()
                self._mev_cache[key] = moon_events(key[0], lat, lon, tz)
            r, tr, s = self._mev_cache[key]
            A(_T("  月出 %s   中天 %s   月落 %s") % (fmt_hm(r), fmt_hm(tr), fmt_hm(s)))
        except Exception:
            A("  (计算失败)")
        A("")
        A("【说明】")
        A("  月相只取决于日月的黄经差 (elongation):")
        A("     0°   = 朔, 月在日地之间, 背光面朝我们")
        A("     90°  = 上弦, 日落前后过中天, 上半夜可见, 亮面朝西(向太阳)")
        A("     180° = 望, 日落月出, 通宵可见")
        A("     270° = 下弦, 后半夜升起, 日出前后过中天, 亮面朝东")
        A("  月亮每天东移约 12.19°, 故每天迟约 50 分钟升起。")
        A("  「明亮边缘方位角 χ」加上视差角 q 之后, 才是你在天上真正看到的")
        A("  月牙倾斜方向 —— 左边星空图里的月亮就是按 χ−q 画的。")
        self.p_text.configure(state="normal")
        self.p_text.delete("1.0", "end")
        self.p_text.insert("1.0", "\n".join(L))
        self.p_text.configure(state="disabled")


def _az_name(az):
    names = ["北", "东北", "东", "东南", "南", "西南", "西", "西北"]
    return names[int((norm360(az) + 22.5) // 45) % 8]


# ===========================================================================
#  主窗口
# ===========================================================================
def _pick_font(root, candidates, size, bold=False):
    import tkinter.font as tkfont
    fams = set(tkfont.families(root))
    for name in candidates:
        if name in fams:
            return tkfont.Font(root=root, family=name, size=size,
                               weight="bold" if bold else "normal")
    return tkfont.Font(root=root, size=size,
                       weight="bold" if bold else "normal")


CJK_FONTS = ["Microsoft YaHei", "PingFang SC", "Noto Sans CJK SC",
             "Source Han Sans SC", "WenQuanYi Micro Hei", "SimHei",
             "Heiti SC", "Arial Unicode MS", "DejaVu Sans"]
MONO_FONTS = ["Sarasa Mono SC", "Noto Sans Mono CJK SC", "Consolas", "Menlo",
              "DejaVu Sans Mono", "Courier New"]


# ===========================================================================
#  第四页: 太阳周日视运动 · 24 节气轨迹
#  固定视角: 观测者站在天穹中心朝「西」看 —— 东在下(面向自己), 西在上(远方),
#  南在左, 北在右, 天顶在正上方。地平面画成浅青色椭圆(正交投影的水平圆)。
# ===========================================================================

# 24 节气 (名称, 太阳视黄经°)  —— 按立春起的传统顺序排列
SOLAR_TERMS = [
    ("立春", 315), ("雨水", 330), ("惊蛰", 345), ("春分", 0),
    ("清明", 15),  ("谷雨", 30),  ("立夏", 45),  ("小满", 60),
    ("芒种", 75),  ("夏至", 90),  ("小暑", 105), ("大暑", 120),
    ("立秋", 135), ("处暑", 150), ("白露", 165), ("秋分", 180),
    ("寒露", 195), ("霜降", 210), ("立冬", 225), ("小雪", 240),
    ("大雪", 255), ("冬至", 270), ("小寒", 285), ("大寒", 300),
]

# 本页专用地点表 (名称, 纬度 N+, 经度 E+, 标准时区)
TRACK_PLACES = [
    ("吉隆坡 Kuala Lumpur",        3.1390, 101.6869,  8.0),
    ("新加坡 Singapore",           1.3521, 103.8198,  8.0),
    ("槟城 George Town",           5.4141, 100.3288,  8.0),
    ("哥打京那巴鲁 Kota Kinabalu",  5.9804, 116.0735,  8.0),
    ("郑州 Zhengzhou",            34.7466, 113.6254,  8.0),
    ("登封·告成 周公测景台",        34.4067, 113.1367,  8.0),
    ("洛阳 Luoyang",              34.6197, 112.4540,  8.0),
    ("安阳 Anyang",               36.0997, 114.3931,  8.0),
    ("曲阜 Qufu",                 35.5967, 116.9925,  8.0),
    ("西安 Xi'an",                34.3416, 108.9398,  8.0),
    ("北京 Beijing",              39.9042, 116.4074,  8.0),
    ("天津 Tianjin",              39.3434, 117.3616,  8.0),
    ("济南 Jinan",                36.6512, 117.1201,  8.0),
    ("青岛 Qingdao",              36.0671, 120.3826,  8.0),
    ("南京 Nanjing",              32.0603, 118.7969,  8.0),
    ("上海 Shanghai",             31.2304, 121.4737,  8.0),
    ("武汉 Wuhan",                30.5928, 114.3055,  8.0),
    ("成都 Chengdu",              30.5728, 104.0668,  8.0),
    ("重庆 Chongqing",            29.5630, 106.5516,  8.0),
    ("昆明 Kunming",              25.0389, 102.7183,  8.0),
    ("广州 Guangzhou",            23.1291, 113.2644,  8.0),
    ("香港 Hong Kong",            22.3193, 114.1694,  8.0),
    ("台北 Taipei",               25.0330, 121.5654,  8.0),
    ("沈阳 Shenyang",             41.8057, 123.4315,  8.0),
    ("哈尔滨 Harbin",             45.8038, 126.5350,  8.0),
    ("乌鲁木齐 Urumqi",           43.8256,  87.6168,  8.0),
    ("拉萨 Lhasa",                29.6520,  91.1721,  8.0),
    ("东京 Tokyo",                35.6762, 139.6503,  9.0),
    ("雅加达 Jakarta",            -6.2088, 106.8456,  7.0),
    ("悉尼 Sydney",              -33.8688, 151.2093, 10.0),
    ("伦敦 London",               51.5074,  -0.1278,  0.0),
    ("纽约 New York",             40.7128, -74.0060, -5.0),
    ("北极圈 66.5°N",             66.5000, 113.6254,  8.0),
]
TRACK_DEFAULT = 0                     # 预设: 吉隆坡


def _term_color(lam):
    """按太阳黄经给节气配色: 冬至一带偏蓝, 夏至一带偏红, 上下半年分走两侧色相。"""
    import colorsys
    lam = lam % 360.0
    if 270.0 <= lam or lam <= 90.0:            # 冬至→春分→夏至 (太阳北行)
        f = ((lam - 270.0) % 360.0) / 180.0
        hue = 205.0 * (1.0 - f)                # 蓝→青→绿→黄→红
        sat, val = 0.78, 0.98
    else:                                       # 夏至→秋分→冬至 (太阳南行)
        f = (lam - 90.0) / 180.0
        hue = (360.0 - 155.0 * f) % 360.0      # 红→粉→紫→蓝
        sat, val = 0.62, 0.96
    r, g, b = colorsys.hsv_to_rgb(hue / 360.0, sat, val)
    return "#%02x%02x%02x" % (int(r * 255), int(g * 255), int(b * 255))


TERM_COLORS = [_term_color(l) for _, l in SOLAR_TERMS]


# ---------------------------------------------------------------------------
#  节气时刻: 解 太阳视黄经 = 目标值
# ---------------------------------------------------------------------------
def sun_apparent_lambda(utc):
    """太阳视黄经 (度, 含章动与光行差) —— 节气的定义量。"""
    p = EPH.get("太阳", utc)
    jd_ut = julian_day(utc)
    jd_tt = jd_ut + delta_t_seconds(utc) / 86400.0
    lam, _ = equ_to_ecl(p.ra, p.dec, true_obliquity(jd_tt))
    return lam


_TERM_CACHE = {}


def solar_term_utc(year, lam_target):
    """求某公历年内 太阳视黄经首次到达 lam_target 的 UTC 时刻。"""
    key = (year, round(lam_target, 6))
    if key in _TERM_CACHE:
        return _TERM_CACHE[key]
    t = dt.datetime(year, 1, 1)
    lam0 = sun_apparent_lambda(t)
    t = t + dt.timedelta(days=norm360(lam_target - lam0) / 0.98565)
    for _ in range(10):
        err = norm180(sun_apparent_lambda(t) - lam_target)
        if abs(err) < 1e-7:
            break
        t = t - dt.timedelta(days=err / 0.98565)
    _TERM_CACHE[key] = t
    return t


# ---------------------------------------------------------------------------
#  一日之内太阳位置的快速插值器
#  一天里 赤纬 与 (GHA - 15°×时) 都极其平滑, 取 13 个样点线性插值即可,
#  精度优于 0.001°, 而后续任意细的采样都不再需要动星历。
# ---------------------------------------------------------------------------
class DaySun:
    def __init__(self, t_ref_utc, x0=-3.0, x1=29.0, n=13):
        self.t0 = t_ref_utc               # x = 自 t_ref 起算的小时数
        self.x0, self.x1, self.n = x0, x1, n
        self.xs = [x0 + (x1 - x0) * i / (n - 1) for i in range(n)]
        self.dec, self.res = [], []
        self.sd = 0.267
        prev = None
        for i, xx in enumerate(self.xs):
            p = EPH.get("太阳", t_ref_utc + dt.timedelta(seconds=xx * 3600.0))
            self.dec.append(p.dec)
            r = p.gha - 15.0 * xx
            if prev is not None:
                r = prev + norm180(r - prev)
            prev = r
            self.res.append(r)
            if i == (n - 1) // 2:
                self.sd = p.sd_arcmin / 60.0
        self.step = (x1 - x0) / (n - 1)

    def _lerp(self, arr, x):
        f = (x - self.x0) / self.step
        i = int(math.floor(f))
        i = max(0, min(self.n - 2, i))
        u = f - i
        return arr[i] + (arr[i + 1] - arr[i]) * u

    def dec_at(self, x):
        return self._lerp(self.dec, x)

    def gha_at(self, x):
        return self._lerp(self.res, x) + 15.0 * x

    def altaz(self, x, lat, lon):
        return altaz_from_hadec(norm360(self.gha_at(x) + lon),
                                self._lerp(self.dec, x), lat)

    def hour_angle(self, x, lon):
        """地方时角 (度, 西正, −180..180)。"""
        return norm180(self.gha_at(x) + lon)

    def tst(self, x, lon):
        """真太阳时 (小时, 0..24)。"""
        return (12.0 + self.hour_angle(x, lon) / 15.0) % 24.0

    def eot_min(self, x, lon):
        """均时差 = 真太阳时 − 地方平太阳时 (分钟)。"""
        lmt = (self.t0 + dt.timedelta(seconds=x * 3600.0)
               + dt.timedelta(hours=lon / 15.0))
        lmt_h = lmt.hour + lmt.minute / 60.0 + lmt.second / 3600.0
        return norm180((self.tst(x, lon) - lmt_h) * 15.0) * 4.0


def _hm(h):
    """小时(浮点) -> 'HH:MM'"""
    h = h % 24.0
    m = int(round(h * 60.0))
    if m >= 1440:
        m -= 1440
    return "%02d:%02d" % (m // 60, m % 60)


def _hms(h):
    h = h % 24.0
    s = int(round(h * 3600.0))
    if s >= 86400:
        s -= 86400
    return "%02d:%02d:%02d" % (s // 3600, (s // 60) % 60, s % 60)


def _dm_str(x):
    """十进制度 -> 度分 (如 73°30′)"""
    sign = "-" if x < 0 else ""
    x = abs(x)
    d = int(x)
    m = (x - d) * 60.0
    if m >= 59.95:
        d += 1
        m = 0.0
    return "%s%d°%02d′" % (sign, d, int(round(m)))


class SunTrackTab(ttk.Frame):
    """太阳周日视运动模型 (固定视角, 只可缩放平移)。"""

    GROUND = "#a9dcd6"          # 地面: 浅青
    GROUND_EDGE = "#5fb3ab"
    SKY_BG = "#0b1016"

    def __init__(self, master, app):
        super().__init__(master, padding=6)
        self.app = app
        self.zoom = 1.0
        self.pan = [0.0, 0.0]
        self._drag = None
        self._day_cache = {}
        self._rows = []
        self.f_tick = _pick_font(app.root, MONO_FONTS, 7)
        self.f_tick_b = _pick_font(app.root, MONO_FONTS, 8, bold=True)
        self.f_lab = _pick_font(app.root, CJK_FONTS, 9)
        self.f_lab_b = _pick_font(app.root, CJK_FONTS, 9, bold=True)
        self.f_dir = _pick_font(app.root, CJK_FONTS, 15, bold=True)
        self._build()
        self.after(120, self._first_draw)

    def _first_draw(self):
        self._refresh_term_labels()
        self.redraw()

    # ==================== 界面 =============================================
    def _build(self):
        scroll = VScrollFrame(self, width=452)
        scroll.pack(side="right", fill="y")
        right = scroll.body
        left = ttk.Frame(self)
        left.pack(side="left", fill="both", expand=True)

        self.canvas = tk.Canvas(left, bg=self.SKY_BG, highlightthickness=0,
                                width=640, height=640)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.redraw())
        self.canvas.bind("<MouseWheel>", self._on_wheel)
        self.canvas.bind("<Button-4>", lambda e: self._on_wheel(e, +1))
        self.canvas.bind("<Button-5>", lambda e: self._on_wheel(e, -1))
        self.canvas.bind("<ButtonPress-1>", self._on_press)
        self.canvas.bind("<B1-Motion>", self._on_move)
        self.canvas.bind("<ButtonRelease-1>", lambda e: setattr(self, "_drag", None))
        self.canvas.bind("<Double-Button-1>", lambda e: self._reset_view())

        # ---------------- 地点 ----------------
        loc = ttk.LabelFrame(right, text=" 观测地点 ", padding=6)
        loc.pack(fill="x", pady=(0, 5))
        self.city_var = tk.StringVar(value=TRACK_PLACES[TRACK_DEFAULT][0])
        cb = ttk.Combobox(loc, textvariable=self.city_var, width=30, state="readonly",
                          values=[p[0] for p in TRACK_PLACES] + ["自定义 Custom"])
        cb.grid(row=0, column=0, columnspan=4, sticky="we", pady=(0, 3))
        cb.bind("<<ComboboxSelected>>", self._on_city)
        self.lat_var = tk.StringVar(value="%.4f" % TRACK_PLACES[TRACK_DEFAULT][1])
        self.lon_var = tk.StringVar(value="%.4f" % TRACK_PLACES[TRACK_DEFAULT][2])
        self.tz_var = tk.StringVar(value="%.2f" % TRACK_PLACES[TRACK_DEFAULT][3])
        ttk.Label(loc, text="纬度 φ (N+)").grid(row=1, column=0, sticky="w")
        ttk.Entry(loc, textvariable=self.lat_var, width=11).grid(row=1, column=1, sticky="w")
        ttk.Label(loc, text="经度 λ (E+)").grid(row=1, column=2, sticky="w", padx=(8, 0))
        ttk.Entry(loc, textvariable=self.lon_var, width=11).grid(row=1, column=3, sticky="w")
        ttk.Label(loc, text="时区 UTC±").grid(row=2, column=0, sticky="w")
        ttk.Entry(loc, textvariable=self.tz_var, width=11).grid(row=2, column=1, sticky="w")
        ttk.Button(loc, text="按经度取时区", width=15,
                   command=self._tz_from_lon).grid(row=2, column=2, columnspan=2,
                                                   sticky="we", padx=(8, 0))
        for v in (self.lat_var, self.lon_var, self.tz_var):
            v.trace_add("write", lambda *a: self._invalidate())

        # ---------------- 日期时间 ----------------
        tm = ttk.LabelFrame(right, text=" 日期 · 时刻 ", padding=6)
        tm.pack(fill="x", pady=(0, 5))
        now = utcnow() + dt.timedelta(hours=TRACK_PLACES[TRACK_DEFAULT][3])
        self.y_var = tk.StringVar(value=str(now.year))
        self.mo_var = tk.StringVar(value=str(now.month))
        self.d_var = tk.StringVar(value=str(now.day))
        self.h_var = tk.StringVar(value=str(now.hour))
        self.mi_var = tk.StringVar(value="%02d" % now.minute)
        row = ttk.Frame(tm)
        row.pack(fill="x")
        for txt, var, w in (("年", self.y_var, 5), ("月", self.mo_var, 3),
                            ("日", self.d_var, 3), ("时", self.h_var, 3),
                            ("分", self.mi_var, 3)):
            ttk.Label(row, text=txt).pack(side="left", padx=(0, 1))
            e = ttk.Entry(row, textvariable=var, width=w)
            e.pack(side="left", padx=(0, 6))
        for v in (self.y_var, self.mo_var, self.d_var, self.h_var, self.mi_var):
            v.trace_add("write", lambda *a: self._invalidate())
        row2 = ttk.Frame(tm)
        row2.pack(fill="x", pady=(4, 0))
        ttk.Button(row2, text="此刻", width=7, command=self._set_now).pack(side="left")
        ttk.Button(row2, text="−1 时", width=7,
                   command=lambda: self._bump_hour(-1)).pack(side="left", padx=3)
        ttk.Button(row2, text="+1 时", width=7,
                   command=lambda: self._bump_hour(+1)).pack(side="left")
        ttk.Button(row2, text="正午", width=7,
                   command=lambda: self._set_hm(12, 0)).pack(side="left", padx=3)
        self.follow_date = tk.BooleanVar(value=True)
        ttk.Checkbutton(tm, text="也画出「所选日期」当天的轨迹 (白色)",
                        variable=self.follow_date,
                        command=self.redraw).pack(anchor="w", pady=(4, 0))

        # ---------------- 时制 ----------------
        ts = ttk.LabelFrame(right, text=" 时间制 (输入与图上标注都按此) ", padding=6)
        ts.pack(fill="x", pady=(0, 5))
        self.tmode = tk.StringVar(value="zone")
        for txt, val, tip in (("标准时 (按时区)", "zone", "手表时间"),
                              ("地方平太阳时", "lmt", "按本地经度, 不含均时差"),
                              ("真太阳时 (日晷)", "tst", "太阳中天即 12:00")):
            ttk.Radiobutton(ts, text="%s —— %s" % (txt, tip), value=val,
                            variable=self.tmode,
                            command=self.redraw).pack(anchor="w")
        self.tconv = ttk.Label(ts, text="", foreground="#8fd0c6",
                               font=self.app.mono_font, justify="left")
        self.tconv.pack(anchor="w", pady=(4, 0))

        # ---------------- 24 节气 ----------------
        jq = ttk.LabelFrame(right, text=" 24 节气 (勾选即画该日轨迹, 可多选) ", padding=6)
        jq.pack(fill="x", pady=(0, 5))
        st = ttk.Style()
        self.term_vars = []
        self.term_btns = []
        grid = ttk.Frame(jq)
        grid.pack(fill="x")
        for i, (name, lam) in enumerate(SOLAR_TERMS):
            var = tk.BooleanVar(value=False)
            sname = "Jq%d.TCheckbutton" % i
            st.configure(sname, background="#161c22", foreground=TERM_COLORS[i])
            st.map(sname, foreground=[("active", "#ffffff")],
                   background=[("active", "#1d252d")])
            b = ttk.Checkbutton(grid, text=name, variable=var, style=sname,
                                command=self.redraw)
            b.grid(row=i // 4, column=i % 4, sticky="w", padx=(0, 4))
            self.term_vars.append(var)
            self.term_btns.append(b)
        qb = ttk.Frame(jq)
        qb.pack(fill="x", pady=(6, 0))
        ttk.Button(qb, text="二分二至", width=9,
                   command=lambda: self._preset(["春分", "夏至", "秋分", "冬至"])
                   ).pack(side="left")
        ttk.Button(qb, text="四立八节", width=9,
                   command=lambda: self._preset(["立春", "春分", "立夏", "夏至",
                                                 "立秋", "秋分", "立冬", "冬至"])
                   ).pack(side="left", padx=3)
        ttk.Button(qb, text="全选 24", width=8,
                   command=lambda: self._preset([n for n, _ in SOLAR_TERMS])
                   ).pack(side="left")
        ttk.Button(qb, text="一键清空", width=9,
                   command=self.clear_all).pack(side="right")

        # ---------------- 显示与视图 ----------------
        vw = ttk.LabelFrame(right, text=" 显示 · 视图 ", padding=6)
        vw.pack(fill="x", pady=(0, 5))
        self.opt_grid = tk.BooleanVar(value=True)
        self.opt_ticks = tk.BooleanVar(value=True)
        self.opt_hours = tk.BooleanVar(value=True)
        self.opt_sun = tk.BooleanVar(value=True)
        self.opt_events = tk.BooleanVar(value=True)
        self.opt_below = tk.BooleanVar(value=True)
        self.opt_legend = tk.BooleanVar(value=True)
        opts = [("地平坐标网格", self.opt_grid), ("周边刻度", self.opt_ticks),
                ("整点时刻", self.opt_hours), ("此刻太阳位置", self.opt_sun),
                ("日出/日落/中天标注", self.opt_events),
                ("地平线下轨迹(虚线)", self.opt_below),
                ("图例", self.opt_legend)]
        for i, (txt, var) in enumerate(opts):
            ttk.Checkbutton(vw, text=txt, variable=var,
                            command=self.redraw).grid(row=i // 2, column=i % 2,
                                                      sticky="w", padx=(0, 8))
        zb = ttk.Frame(vw)
        zb.grid(row=4, column=0, columnspan=2, sticky="we", pady=(6, 0))
        ttk.Button(zb, text="放大 +", width=8,
                   command=lambda: self._zoom_by(1.25)).pack(side="left")
        ttk.Button(zb, text="缩小 −", width=8,
                   command=lambda: self._zoom_by(0.8)).pack(side="left", padx=3)
        ttk.Button(zb, text="复位视图", width=10,
                   command=self._reset_view).pack(side="left")
        self.zoom_lab = ttk.Label(zb, text="1.00×", foreground="#8fb3d0")
        self.zoom_lab.pack(side="right")
        el = ttk.Frame(vw)
        el.grid(row=5, column=0, columnspan=2, sticky="we", pady=(4, 0))
        ttk.Label(el, text="视线俯角").pack(side="left")
        self.cam_el = tk.DoubleVar(value=24.0)
        ttk.Scale(el, from_=8.0, to=85.0, variable=self.cam_el, orient="horizontal",
                  command=lambda _v: self.redraw()).pack(side="left", fill="x",
                                                         expand=True, padx=6)
        self.el_lab = ttk.Label(el, text="24°", width=5, foreground="#8fb3d0")
        self.el_lab.pack(side="right")

        # ---------------- 数据表 ----------------
        tb = ttk.LabelFrame(right, text=" 各条轨迹的日出 / 中天 / 日落 ", padding=4)
        tb.pack(fill="both", expand=True)
        cols = ("term", "date", "rise", "noon", "set", "len", "alt", "azr")
        heads = ("节气", "日期", "日出", "中天", "日落", "昼长", "午高度", "日出方位")
        wid = (46, 62, 50, 50, 50, 50, 56, 58)
        self.tree = ttk.Treeview(tb, columns=cols, show="headings", height=11)
        for c, h, w in zip(cols, heads, wid):
            self.tree.heading(c, text=h)
            self.tree.column(c, width=w, anchor="center", stretch=False)
        self.tree.pack(fill="both", expand=True)
        tree_hscroll(self.tree, tb)
        self.note = ttk.Label(right, foreground="#7f9bb3", font=self.f_lab,
                              justify="left", wraplength=430,
                              text="鼠标滚轮缩放(以光标为定点) · 按住左键拖动平移 · "
                                   "双击复位。视角固定为「东在近前、南左北右」, 只缩放"
                                   "不旋转。低纬度(如吉隆坡)太阳近天顶, 把「视线俯角」"
                                   "拉到 50°~80° 可把各条轨迹拉开看清。")
        self.note.pack(fill="x", pady=(4, 0))

    # ==================== 小工具 ===========================================
    def _fnum(self, var, default=0.0):
        try:
            return float(str(var.get()).strip())
        except Exception:
            return default

    def _inum(self, var, default=1):
        try:
            return int(float(str(var.get()).strip()))
        except Exception:
            return default

    def site(self):
        return (self._fnum(self.lat_var, 3.139),
                self._fnum(self.lon_var, 101.6869),
                self._fnum(self.tz_var, 8.0))

    def _on_city(self, _e=None):
        name = self.city_var.get()
        for n, la, lo, tz in TRACK_PLACES:
            if n == name:
                self.lat_var.set("%.4f" % la)
                self.lon_var.set("%.4f" % lo)
                self.tz_var.set("%.2f" % tz)
                break
        self._invalidate()

    def _tz_from_lon(self):
        lon = self._fnum(self.lon_var, 0.0)
        self.tz_var.set("%.2f" % (round(lon / 15.0)))

    def _set_now(self):
        _, _, tz = self.site()
        t = utcnow() + dt.timedelta(hours=tz)
        self.y_var.set(str(t.year))
        self.mo_var.set(str(t.month))
        self.d_var.set(str(t.day))
        self.h_var.set(str(t.hour))
        self.mi_var.set("%02d" % t.minute)

    def _set_hm(self, h, m):
        self.h_var.set(str(h))
        self.mi_var.set("%02d" % m)

    def _bump_hour(self, d):
        h = self._inum(self.h_var, 12) + d
        if h < 0:
            h += 24
        if h > 23:
            h -= 24
        self.h_var.set(str(h))

    def _preset(self, names):
        for i, (n, _l) in enumerate(SOLAR_TERMS):
            if n in names:
                self.term_vars[i].set(True)
        self.redraw()

    def clear_all(self):
        for v in self.term_vars:
            v.set(False)
        self.redraw()

    def _invalidate(self):
        self._day_cache.clear()
        self._refresh_term_labels()
        self.redraw()

    def _zoom_by(self, f):
        self.zoom = max(0.35, min(60.0, self.zoom * f))
        self.redraw()

    def _reset_view(self):
        self.zoom = 1.0
        self.pan = [0.0, 0.0]
        self.redraw()

    def _on_wheel(self, e, direction=None):
        if direction is None:
            direction = 1 if e.delta > 0 else -1
        f = 1.18 if direction > 0 else 1 / 1.18
        old = self.zoom
        self.zoom = max(0.35, min(80.0, self.zoom * f))
        k = self.zoom / old
        # 以光标为定点缩放:  O' = P + k·(O − P)
        ox, oy, R, yc = self.ox, self.oy, self.R, self._yc
        ox2 = e.x + k * (ox - e.x)
        oy2 = e.y + k * (oy - e.y)
        self.pan[0] = ox2 - self.W / 2.0
        self.pan[1] = oy2 - self.H / 2.0 - R * k * yc
        self.redraw()

    def _on_press(self, e):
        self._drag = (e.x, e.y, self.pan[0], self.pan[1])

    def _on_move(self, e):
        if not self._drag:
            return
        x0, y0, p0, p1 = self._drag
        self.pan = [p0 + (e.x - x0), p1 + (e.y - y0)]
        self.redraw()

    # ==================== 天文 =============================================
    def _term_date(self, idx):
        """该节气在本页所选年份、所选时区下的本地日期与精确时刻。"""
        year = self._inum(self.y_var, utcnow().year)
        _, _, tz = self.site()
        t_utc = solar_term_utc(year, SOLAR_TERMS[idx][1])
        loc = t_utc + dt.timedelta(hours=tz)
        return loc.date(), loc, t_utc

    def _refresh_term_labels(self):
        try:
            for i in range(24):
                d, loc, _ = self._term_date(i)
                self.term_btns[i].configure(
                    text="%s %d/%d" % (SOLAR_TERMS[i][0], d.month, d.day))
        except Exception:
            pass

    def _daysun(self, date_local):
        """取某本地日期的太阳插值器 (t0 = 该地本时区 00:00 对应的 UTC)。"""
        _, _, tz = self.site()
        key = (date_local, round(tz, 4))
        ds = self._day_cache.get(key)
        if ds is None:
            t0 = (dt.datetime(date_local.year, date_local.month, date_local.day)
                  - dt.timedelta(hours=tz))
            ds = DaySun(t0)
            self._day_cache[key] = ds
        return ds

    def disp_hours(self, ds, x):
        """把 x(自本地 00:00 起的小时) 换算成当前时制的显示小时。"""
        _, lon, tz = self.site()
        m = self.tmode.get()
        if m == "zone":
            return x % 24.0
        if m == "lmt":
            return (x - tz + lon / 15.0) % 24.0
        return ds.tst(x, lon)

    def x_of_disp(self, ds, h):
        """把当前时制的钟点 h 换算成 x。"""
        _, lon, tz = self.site()
        m = self.tmode.get()
        if m == "zone":
            return h
        if m == "lmt":
            return h + tz - lon / 15.0
        x = h + tz - lon / 15.0
        for _ in range(4):
            d = norm180((h - ds.tst(x, lon)) * 15.0) / 15.0
            x += d
            if abs(d) < 1e-6:
                break
        return x

    def day_info(self, date_local):
        """日出/中天/日落 (x 值) 与极昼极夜判断。"""
        lat, lon, _ = self.site()
        ds = self._daysun(date_local)
        step = 1.0 / 6.0
        xs = [i * step for i in range(int(24 / step) + 1)]
        alts = [ds.altaz(x, lat, lon)[0] for x in xs]
        tgt = -0.833

        def refine(a, b):
            for _ in range(50):
                m = (a + b) / 2.0
                if (ds.altaz(a, lat, lon)[0] - tgt) * (ds.altaz(m, lat, lon)[0] - tgt) <= 0:
                    b = m
                else:
                    a = m
            return (a + b) / 2.0

        rise = sett = None
        for i in range(len(xs) - 1):
            if alts[i] < tgt <= alts[i + 1]:
                rise = refine(xs[i], xs[i + 1])
            if alts[i] >= tgt > alts[i + 1]:
                sett = refine(xs[i], xs[i + 1])
        # 中天: 时角过零
        noon = None
        for i in range(len(xs) - 1):
            h0 = ds.hour_angle(xs[i], lon)
            h1 = ds.hour_angle(xs[i + 1], lon)
            if h0 < 0 <= h1:
                a, b = xs[i], xs[i + 1]
                for _ in range(50):
                    m = (a + b) / 2.0
                    if ds.hour_angle(m, lon) < 0:
                        a = m
                    else:
                        b = m
                noon = (a + b) / 2.0
                break
        polar = None
        if rise is None and sett is None:
            polar = "极昼" if max(alts) > tgt else "极夜"
        return {"ds": ds, "rise": rise, "noon": noon, "set": sett,
                "polar": polar, "alts": alts}

    # ==================== 投影 =============================================
    def _setup_view(self):
        W = max(60, self.canvas.winfo_width())
        H = max(60, self.canvas.winfo_height())
        el = max(6.0, min(86.0, float(self.cam_el.get())))
        self.el_lab.configure(text="%.0f°" % el)
        self.zoom_lab.configure(text="%.2f×" % self.zoom)
        se, ce = dsin(el), dcos(el)
        # 正交投影下, 整个天球(含地平线下的短虚线)恰好落在半径 1 的圆内;
        # 再留出周边刻度与文字的边。视图因此与纬度、节气无关, 始终「固定」。
        y_top, y_bot = 1.06, -1.10
        R0 = min(W / 2.46, H / (y_top - y_bot))
        self.R = R0 * self.zoom
        self._yc = (y_top + y_bot) / 2.0
        self.ox = W / 2.0 + self.pan[0]
        self.oy = H / 2.0 + self.R * self._yc + self.pan[1]
        self._se, self._ce = se, ce
        self.W, self.H = W, H

    def P(self, alt, az, r=1.0):
        """(高度角, 方位角 北起顺时针, 半径) -> 画布坐标。"""
        ca = dcos(alt) * r
        E = ca * dsin(az)
        N = ca * dcos(az)
        U = dsin(alt) * r
        sx = N
        sy = -self._se * E + self._ce * U
        return (self.ox + sx * self.R, self.oy - sy * self.R)

    def PG(self, rho, az):
        """地平面上 (半径 rho, 方位 az) 的点。"""
        E = rho * dsin(az)
        N = rho * dcos(az)
        return (self.ox + N * self.R, self.oy + self._se * E * self.R)

    # ==================== 绘制 =============================================
    # ---- 带避让的文字标注 --------------------------------------------------
    @staticmethod
    def _ovl(a, b):
        return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])

    def _lab(self, x, y, text, fill, font, cands=None, reserve_only=False):
        w, h = text_size(font, text)            # 按实际显示的语言与字体量
        h = max(13.0, h - 4.0)
        if cands is None:
            k = w / 2 + 13
            cands = [(0, -15), (0, 15), (k, 0), (-k, 0), (0, -30), (0, 30),
                     (k, -17), (-k, -17), (k, 17), (-k, 17),
                     (0, -45), (0, 45), (k, -34), (-k, -34)]
        pick = None
        for dx, dy in cands:
            cx, cy = x + dx, y + dy
            box = (cx - w / 2 - 2, cy - h / 2 - 1, cx + w / 2 + 2, cy + h / 2 + 1)
            if not any(self._ovl(box, b) for b in self._boxes):
                pick = (cx, cy, box)
                break
        if pick is None:
            cx, cy = x + cands[0][0], y + cands[0][1]
            pick = (cx, cy, (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2))
        self._boxes.append(pick[2])
        if not reserve_only:
            self.canvas.create_text(pick[0], pick[1], text=text, fill=fill,
                                    font=font)
        return pick[0], pick[1]

    def redraw(self):
        c = self.canvas
        c.delete("all")
        self._boxes = []
        self._setup_view()
        try:
            self._draw_all()
        except Exception as ex:                       # 输入还没填完时不要炸
            c.create_text(self.W / 2, self.H / 2, text=_T("等待输入…  (%s)") % ex,
                          fill="#6b7a88", font=self.f_lab)

    def _draw_all(self):
        c = self.canvas
        lat, lon, tz = self.site()
        self._draw_ground()
        rows = []

        # ---- 要画的日子: 各勾选节气 + (可选)所选日期 ----
        jobs = []
        for i, v in enumerate(self.term_vars):
            if v.get():
                d, loc, _ = self._term_date(i)
                jobs.append({"name": SOLAR_TERMS[i][0], "color": TERM_COLORS[i],
                             "date": d, "exact": loc, "kind": "term"})
        if self.follow_date.get():
            d = self._sel_date()
            if d and all(j["date"] != d for j in jobs):
                jobs.append({"name": "所选日", "color": "#f2f6fa", "date": d,
                             "exact": None, "kind": "day"})

        # ---- 图例先占位 (免得曲线标注压到它) ----
        self._jobs = jobs
        if self.opt_legend.get() and jobs:
            lw = self._legend_w(jobs, self._legend_head(),
                                self._legend_texts(jobs, sample=True))
            self._boxes.append((4, 4, 4 + lw + 6,
                                26 + (15 if len(jobs) <= 14 else 13) * len(jobs)))

        # ---- 地平线下的轨迹先画 (画在地面之上, 虚线) ----
        if self.opt_below.get():
            for j in jobs:
                self._draw_path(j, below=True)
        self._draw_horizon()
        if self.opt_grid.get():
            self._draw_grid()
        if self.opt_ticks.get():
            self._draw_az_ticks()
            self._draw_alt_ticks()
        self._draw_cardinals()

        # ---- 地平线上的轨迹 (先全部画线, 再统一放标注, 避免被压) ----
        for j in jobs:
            info = self._draw_path(j, below=False)
            if info:
                rows.append(info)
        for r in rows:
            self._annotate(r)
        self._draw_legend(rows)
        self._fill_table(rows)
        self._update_conv()

    def _sel_date(self):
        try:
            return dt.date(self._inum(self.y_var), self._inum(self.mo_var),
                           self._inum(self.d_var))
        except Exception:
            return None

    # ---- 地面 -------------------------------------------------------------
    def _draw_ground(self):
        c = self.canvas
        pts = []
        for k in range(721):
            pts.extend(self.PG(1.0, k * 0.5))
        c.create_polygon(pts, fill=self.GROUND, outline="")
        # 地面的方位辅助线
        for az in range(0, 360, 15):
            a, b = self.PG(0.0, az), self.PG(1.0, az)
            c.create_line(a[0], a[1], b[0], b[1],
                          fill="#8ccbc4" if az % 45 else "#63b3ab",
                          width=1 if az % 45 else 2)
        for rho in (0.25, 0.5, 0.75):
            pts = []
            for k in range(121):
                pts.extend(self.PG(rho, k * 3))
            c.create_polygon(pts, fill="", outline="#8ccbc4", width=1)
        c.create_text(*self.PG(0.13, 225), text="地 平 面", fill="#2f6b66",
                      font=self.f_lab_b)

    def _draw_horizon(self):
        c = self.canvas
        pts = []
        for k in range(721):
            pts.extend(self.PG(1.0, k * 0.5))
        c.create_polygon(pts, fill="", outline=self.GROUND_EDGE, width=2)

    # ---- 网格 -------------------------------------------------------------
    def _draw_grid(self):
        c = self.canvas
        for alt in range(10, 90, 10):
            pts = []
            for k in range(121):
                pts.extend(self.P(alt, k * 3))
            c.create_polygon(pts, fill="", outline="#22323f",
                             width=2 if alt == 30 or alt == 60 else 1)
        for az in range(0, 360, 15):
            pts = []
            for a in range(0, 91, 3):
                pts.extend(self.P(a, az))
            c.create_line(pts, fill="#22323f", width=2 if az % 45 == 0 else 1)
        zx, zy = self.P(90, 0)
        c.create_line(zx - 7, zy, zx + 7, zy, fill="#4d6d80")
        c.create_line(zx, zy - 7, zx, zy + 7, fill="#4d6d80")
        c.create_text(zx + 14, zy - 8, text="天顶 Z", fill="#6d8fa3",
                      font=self.f_lab, anchor="w")

    # ---- 方位刻度 ---------------------------------------------------------
    def _draw_az_ticks(self):
        c = self.canvas
        px_per_deg = self.R * math.pi / 180.0
        if px_per_deg > 26:
            minor, medium, label = 1, 5, 1
        elif px_per_deg > 7:
            minor, medium, label = 1, 5, 5
        elif px_per_deg > 2.4:
            minor, medium, label = 1, 5, 10
        elif px_per_deg > 0.9:
            minor, medium, label = 5, 10, 30
        else:
            minor, medium, label = 10, 30, 90
        for az in range(0, 360, minor):
            big = (az % medium == 0)
            r1 = 1.055 if (az % (medium * 2) == 0) else (1.035 if big else 1.018)
            a = self.PG(1.0, az)
            b = self.PG(r1, az)
            c.create_line(a[0], a[1], b[0], b[1],
                          fill="#7fd8d0" if big else "#4e8b86",
                          width=2 if az % 90 == 0 else 1)
            if az % label == 0 and az % 90 != 0:
                t = self.PG(1.115, az)
                c.create_text(t[0], t[1], text="%d°" % az, fill="#63b3ab",
                              font=self.f_tick)
                self._boxes.append((t[0] - 13, t[1] - 6, t[0] + 13, t[1] + 6))

    # ---- 高度刻度 (南、北子午圈) ------------------------------------------
    def _draw_alt_ticks(self):
        c = self.canvas
        px = self.R * math.pi / 180.0
        if px > 7:
            minor, medium, label = 1, 5, 5
        elif px > 2.4:
            minor, medium, label = 1, 5, 10
        else:
            minor, medium, label = 5, 10, 30
        for az, anchor, dx in ((180, "e", -1), (0, "w", 1)):
            for alt in range(0, 91, minor):
                big = (alt % medium == 0)
                r1 = 1.045 if alt % (medium * 2) == 0 else (1.03 if big else 1.015)
                a = self.P(alt, az)
                b = self.P(alt, az, r1)
                c.create_line(a[0], a[1], b[0], b[1],
                              fill="#5d7f93" if big else "#39505f",
                              width=2 if alt % 30 == 0 else 1)
                if alt % label == 0 and alt != 0:
                    t = self.P(alt, az, 1.075)
                    c.create_text(t[0], t[1], text="%d°" % alt, fill="#6d8fa3",
                                  font=self.f_tick, anchor=anchor)
                    self._boxes.append((t[0] - 22, t[1] - 6, t[0] + 22, t[1] + 6))

    def _draw_cardinals(self):
        c = self.canvas
        for az, name, dxy in ((0, "北 N", (34, 0)), (90, "东 E", (0, 30)),
                              (180, "南 S", (-34, 0)), (270, "西 W", (0, -28))):
            x, y = self.PG(1.0, az)
            c.create_text(x + dxy[0], y + dxy[1], text=name, fill="#e8c56a",
                          font=self.f_dir)
            self._boxes.append((x + dxy[0] - 28, y + dxy[1] - 12,
                                x + dxy[0] + 28, y + dxy[1] + 12))
        for az, name in ((45, "东北"), (135, "东南"), (225, "西南"), (315, "西北")):
            x, y = self.PG(1.175, az)
            c.create_text(x, y, text=name, fill="#8a7a4e", font=self.f_lab)
            self._boxes.append((x - 20, y - 8, x + 20, y + 8))

    # ---- 一条日轨 ---------------------------------------------------------
    def _draw_path(self, job, below=False):
        c = self.canvas
        lat, lon, tz = self.site()
        info = self.day_info(job["date"])
        ds = info["ds"]
        col = job["color"]

        # 采样整天
        N = 24 * 20
        pts = []
        for i in range(N + 1):
            x = 24.0 * i / N
            alt, az = ds.altaz(x, lat, lon)
            pts.append((x, alt, az))

        if below:                       # 地平线以下: 只画到 −12° (民用昏影终)
            seg = []
            for x, alt, az in pts:
                if -12.0 <= alt < -0.833:
                    seg.append(self.P(alt, az))
                else:
                    if len(seg) > 1:
                        c.create_line([v for p in seg for v in p], fill=col,
                                      width=1, dash=(3, 5), smooth=True)
                    seg = []
            if len(seg) > 1:
                c.create_line([v for p in seg for v in p], fill=col, width=1,
                              dash=(3, 5), smooth=True)
            return None

        # --- 地平线以上的主曲线 ---
        seg = []
        for x, alt, az in pts:
            if alt >= -0.833:
                seg.append(self.P(alt, az))
            else:
                if len(seg) > 1:
                    c.create_line([v for p in seg for v in p], fill=col,
                                  width=3, smooth=True, capstyle="round")
                seg = []
        if len(seg) > 1:
            c.create_line([v for p in seg for v in p], fill=col, width=3,
                          smooth=True, capstyle="round")

        # --- 行进方向箭头 ---
        if info["rise"] is not None and info["set"] is not None:
            xm = info["rise"] + (info["set"] - info["rise"]) * 0.62
            a1, z1 = ds.altaz(xm - 0.12, lat, lon)
            a2, z2 = ds.altaz(xm + 0.12, lat, lon)
            p1, p2 = self.P(a1, z1), self.P(a2, z2)
            c.create_line(p1[0], p1[1], p2[0], p2[1], fill=col, width=3,
                          arrow="last", arrowshape=(12, 15, 5))

        # --- 整点 ---
        nsel = len(self._jobs)
        if self.opt_hours.get() and info["rise"] is not None:
            hstep = 1 if (self.zoom > 1.4 or nsel <= 4) else 2
            for hh in range(0, 24, hstep):
                x = self.x_of_disp(ds, float(hh))
                if not (0.0 <= x <= 24.0):
                    continue
                alt, az = ds.altaz(x, lat, lon)
                if alt < 0.5:
                    continue
                px, py = self.P(alt, az)
                c.create_oval(px - 2.5, py - 2.5, px + 2.5, py + 2.5,
                              fill=col, outline="")
                if self.zoom > 1.15 or nsel <= 5:
                    c.create_text(px, py - 10, text="%d" % hh, fill=col,
                                  font=self.f_tick_b)

        # --- 日出 / 日落 / 中天 / 此刻 (先算, 标注留到最后统一放) ---
        rise_h = set_h = noon_h = None
        maxalt = az_noon = None
        az_rise = az_set = None
        if info["rise"] is not None:
            rise_h = self.disp_hours(ds, info["rise"])
            _, az_rise = ds.altaz(info["rise"], lat, lon)
        if info["set"] is not None:
            set_h = self.disp_hours(ds, info["set"])
            _, az_set = ds.altaz(info["set"], lat, lon)
        if info["noon"] is not None:
            noon_h = self.disp_hours(ds, info["noon"])
            maxalt, az_noon = ds.altaz(info["noon"], lat, lon)

        sun = None
        if self.opt_sun.get():
            h = self._input_hours()
            x = self.x_of_disp(ds, h)
            alt, az = ds.altaz(x, lat, lon)
            sun = {"h": h, "alt": alt, "az": az}
            if alt >= -0.9:
                px, py = self.P(alt, az)
                r = 9
                for k in range(12):
                    a = k * 30
                    c.create_line(px + r * 1.15 * dcos(a), py + r * 1.15 * dsin(a),
                                  px + r * 1.80 * dcos(a), py + r * 1.80 * dsin(a),
                                  fill=col, width=2)
                c.create_oval(px - r, py - r, px + r, py + r, fill="#e2453f",
                              outline=col, width=2)
                self._boxes.append((px - r - 14, py - r - 14,
                                    px + r + 14, py + r + 14))

        return {"name": job["name"], "date": job["date"], "color": col,
                "rise": rise_h, "noon": noon_h, "set": set_h,
                "maxalt": maxalt, "az_noon": az_noon,
                "az_rise": az_rise, "az_set": az_set,
                "polar": info["polar"],
                "daylen": (None if (info["rise"] is None or info["set"] is None)
                           else (info["set"] - info["rise"])),
                "exact": job["exact"], "sun": sun}

    def _annotate(self, r):
        """日出/日落/中天/此刻太阳 的文字标注 (带避让)。"""
        col = r["color"]
        n = len(self._jobs)
        if self.opt_events.get():
            if r["az_rise"] is not None:
                x, y = self.P(0.0, r["az_rise"])
                self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill=col,
                                        outline="#0b1016")
                lx, ly = self.P(0.0, r["az_rise"], 1.16)
                self._lab(lx, ly, _T("日出 %s") % _hm(r["rise"]), col, self.f_lab_b,
                          cands=[(dx, dy) for dy in (12, 26, 40, 54, 68, 82, -14)
                                 for dx in (0, 62, -62, 124, -124)])
            if r["az_set"] is not None:
                x, y = self.P(0.0, r["az_set"])
                self.canvas.create_oval(x - 4, y - 4, x + 4, y + 4, fill=col,
                                        outline="#0b1016")
                lx, ly = self.P(0.0, r["az_set"], 1.16)
                self._lab(lx, ly, _T("日落 %s") % _hm(r["set"]), col, self.f_lab_b,
                          cands=[(dx, dy) for dy in (-13, -27, -41, -55, -69, 13)
                                 for dx in (0, 62, -62, 124, -124)])
            if r["maxalt"] is not None and r["maxalt"] > 0 and n <= 10:
                x, y = self.P(r["maxalt"], r["az_noon"])
                self._lab(x, y, _T("%s 中天 %s") % (_dm_str(r["maxalt"]),
                                               _hm(r["noon"])),
                          col, self.f_lab_b,
                          cands=[(dx, dy) for dy in (-16, -30, 16, 30, -44, 44)
                                 for dx in (0, 78, -78, 156, -156)])
        s = r["sun"]
        if s and s["alt"] >= -0.9 and n <= 12:
            px, py = self.P(s["alt"], s["az"])
            self._lab(px, py, "%s %s h=%s" % (r["name"], _hm(s["h"]),
                                              _dm_str(s["alt"])),
                      "#ffd9a0", self.f_lab_b,
                      cands=[(dx, dy) for dy in (26, -26, 40, -40, 54, -54)
                             for dx in (0, 90, -90, 180, -180)])

    def _input_hours(self):
        return (self._inum(self.h_var, 12) % 24) + self._inum(self.mi_var, 0) / 60.0

    # ---- 图例 -------------------------------------------------------------
    def _legend_w(self, rows, head=None, lines=()):
        """图例框宽: 至少 352 (中文原样); 英文字长就按实际显示宽度放宽。"""
        w = 352
        if head:
            w = max(w, text_size(self.f_lab, head)[0] + 16)
        for t in lines:
            w = max(w, text_size(self.f_tick_b, t)[0] + 32 + 10)
        return w

    def _legend_head(self):
        mode = {"zone": "标准时", "lmt": "地方平太阳时",
                "tst": "真太阳时"}[self.tmode.get()]
        lat, lon, tz = self.site()
        return (_T("%s  φ=%s  λ=%s\n%s (UTC%+.2f) · %s年 · ↑日出 ☉中天 ↓日落")
                % (self.city_var.get().split()[0], deg_dm(lat, "N", "S"),
                   deg_dm(lon, "E", "W"), mode, tz, self.y_var.get()))

    def _legend_texts(self, rows, sample=False):
        """图例各行。节气名补齐到同宽, 后面各栏才对得齐 (英文名长短不一, 按译名最长者补);
        sample=True 时用占位时刻, 只为事先量宽度。"""
        pad = 4 if LANG != "en" else max(len(tr(r["name"])) for r in rows)
        tpl = _T("%-4s %02d-%02d  ↑%s  ☉%s  ↓%s  昼%5.2fh  高%s").replace("%-4s", "%-*s")
        texts = []
        for r in rows:
            nm = r["name"] if LANG != "en" else tr(r["name"])
            mo, dd = r["date"].month, r["date"].day
            if sample:
                texts.append(tpl % (pad, nm, mo, dd, "00:00", "00:00", "00:00",
                                    12.0, "00°00′"))
            elif r["polar"]:
                texts.append("%-*s %02d-%02d  %s" % (pad, nm, mo, dd, r["polar"]))
            else:
                texts.append(tpl % (pad, nm, mo, dd, _hm(r["rise"]), _hm(r["noon"]),
                                    _hm(r["set"]), r["daylen"], _dm_str(r["maxalt"])))
        return texts

    def _draw_legend(self, rows):
        if not self.opt_legend.get() or not rows:
            return
        c = self.canvas
        head = self._legend_head()
        x0, y0 = 8, 8
        texts = self._legend_texts(rows)
        w = self._legend_w(rows, head, texts)
        dy = 15 if len(rows) <= 14 else 13
        h = 34 + dy * len(rows)
        c.create_rectangle(x0, y0, x0 + w, y0 + h, fill="#0e161d",
                           outline="#2c3742")
        c.create_text(x0 + 8, y0 + 16, text=head, anchor="w",
                      fill="#8fb3d0", font=self.f_lab)
        for i, (r, txt) in enumerate(zip(rows, texts)):
            yy = y0 + 40 + dy * i
            c.create_line(x0 + 8, yy, x0 + 26, yy, fill=r["color"], width=3)
            c.create_text(x0 + 32, yy, text=txt, anchor="w", fill="#d8e0e8",
                          font=self.f_tick_b)

    # ---- 右侧表格与时制换算 ------------------------------------------------
    def _fill_table(self, rows):
        self.tree.delete(*self.tree.get_children())
        for r in rows:
            if r["polar"]:
                self.tree.insert("", "end", values=(
                    r["name"], "%02d-%02d" % (r["date"].month, r["date"].day),
                    r["polar"], "—", "—", "—",
                    "—" if r["maxalt"] is None else _dm_str(r["maxalt"]), "—"))
            else:
                self.tree.insert("", "end", values=(
                    r["name"], "%02d-%02d" % (r["date"].month, r["date"].day),
                    _hm(r["rise"]), _hm(r["noon"]), _hm(r["set"]),
                    "%.2f h" % r["daylen"], _dm_str(r["maxalt"]),
                    "%.1f°" % r["az_rise"]))
        autosize_tree(self.tree, self.app.mono_font, self.app.ui_font)

    def _update_conv(self):
        lat, lon, tz = self.site()
        d = self._sel_date()
        if d is None:
            self.tconv.configure(text="日期无效")
            return
        ds = self._daysun(d)
        h = self._input_hours()
        x = self.x_of_disp(ds, h)
        zone = x % 24.0
        lmt = (x - tz + lon / 15.0) % 24.0
        tst = ds.tst(x, lon)
        eot = ds.eot_min(x, lon)
        alt, az = ds.altaz(x, lat, lon)
        half = "上午" if tst < 12 else "下午"
        hh = tst % 12
        if hh < 1e-9:
            hh = 12
        self.tconv.configure(
            text=(_T("标准时 %s   地方平时 %s   真太阳时 %s\n"
                  "均时差 %+.1f 分   经度时差 %+.1f 分   此刻属 %s %.1f 时\n"
                  "太阳 高度 %s   方位 %.2f° (%s)")
                  % (_hms(zone), _hms(lmt), _hms(tst), eot,
                     (lon / 15.0 - tz) * 60.0, half, hh,
                     _dm_str(alt), az_fmt(az, 2), _az_name(az))))




# ===========================================================================
#  历法工具 (纯儒略日, 不受 datetime 1..9999 年限制) —— 供日月食千年推算
#  1582-10-15 之前按儒略历显示 (与国际日月食典同一惯例)
#  天文年号: 0 年 = 公元前 1 年, -1 年 = 公元前 2 年 …
# ===========================================================================
def jd_to_cal(jd):
    """儒略日 -> (年, 月, 日, 时, 分, 秒)。年可为 0 或负 (天文年号)。"""
    jd = jd + 0.5
    z = math.floor(jd)
    f = jd - z
    if z >= 2299161:
        al = math.floor((z - 1867216.25) / 36524.25)
        a = z + 1 + al - math.floor(al / 4)
    else:
        a = z
    b = a + 1524
    c = math.floor((b - 122.1) / 365.25)
    d = math.floor(365.25 * c)
    e = math.floor((b - d) / 30.6001)
    day = b - d - math.floor(30.6001 * e) + f
    month = e - 1 if e < 14 else e - 13
    year = c - 4716 if month > 2 else c - 4715
    di = int(math.floor(day))
    fr = (day - di) * 24.0
    hh = int(fr)
    mf = (fr - hh) * 60.0
    mm = int(mf)
    ss = (mf - mm) * 60.0
    if ss >= 59.9995:
        ss = 0.0
        mm += 1
    if mm >= 60:
        mm -= 60
        hh += 1
    if hh >= 24:                      # 极罕见的进位, 退回用整日重算
        return jd_to_cal(jd - 0.5 + 1e-9)
    return int(year), int(month), di, hh, mm, ss


def cal_to_jd(y, m, d, hh=0, mm=0, ss=0.0):
    """(年,月,日,时,分,秒) -> 儒略日。1582-10-15 前按儒略历解释。"""
    dd = d + (hh + mm / 60.0 + ss / 3600.0) / 24.0
    yy, mo = y, m
    if mo <= 2:
        yy -= 1
        mo += 12
    if (y, m, d) < (1582, 10, 15):
        b = 0
    else:
        a = math.floor(yy / 100.0)
        b = 2 - a + math.floor(a / 4)
    return (math.floor(365.25 * (yy + 4716)) + math.floor(30.6001 * (mo + 1))
            + dd + b - 1524.5)


def jd_year(jd):
    """儒略日 -> 小数年 (供 ΔT)。"""
    y, m = jd_to_cal(jd)[0], jd_to_cal(jd)[1]
    return y + (m - 0.5) / 12.0


def delta_t_jd(jd):
    return delta_t_year(jd_year(jd))


def cn_year(y):
    return _T("公元前%d年") % (1 - y) if y <= 0 else _T("%d年") % y


def fmt_jd(jd, tz=0.0, sec=True):
    """儒略日 -> 中文日期串 (tz 为要加的时区小时)。"""
    y, mo, d, hh, mm, ss = jd_to_cal(jd + tz / 24.0)
    t = "%02d:%02d:%02d" % (hh, mm, int(ss)) if sec else "%02d:%02d" % (hh, mm)
    if y <= 0:
        return _T("公元前 %d 年 %02d-%02d %s") % (1 - y, mo, d, t)
    return "%04d-%02d-%02d %s" % (y, mo, d, t)


def fmt_jd_short(jd, tz=0.0):
    y, mo, d, hh, mm, ss = jd_to_cal(jd + tz / 24.0)
    pre = "-%d" % (1 - y) if y <= 0 else "%04d" % y
    return "%s-%02d-%02d %02d:%02d" % (pre, mo, d, hh, mm)


def dur_str(days):
    """时长 (日) -> 'Xm YYs' / 'Xh YYm'"""
    s = days * 86400.0
    if s < 0:
        return "—"
    if s < 3600:
        return _T("%d分%02d秒") % (int(s) // 60, int(round(s)) % 60)
    return _T("%d时%02d分%02d秒") % (int(s) // 3600, (int(s) // 60) % 60,
                                int(round(s)) % 60)


# ===========================================================================
#  日月食 —— 几何内核
#  日月位置一律取「地心视位置」(含光行差与光行时): 地面在 t 时刻所见的影,
#  正是由 太阳(t-8.3分) 与 月亮(t-1.3秒) 的几何位置决定的, 与视位置一致。
#  月半径按 NASA/Espenak 惯例取两个值:
#     外切 (半影, C1/C4/P1/P4)  k = 0.2725076
#     内切 (本影, C2/C3)        k = 0.272281
# ===========================================================================
ECL_A = 6378.137                       # 地球赤道半径 km (WGS84)
ECL_F = 1.0 / 298.257223563            # 扁率
ECL_BA = 1.0 - ECL_F                   # b/a
ECL_RSUN = 696000.0                    # 太阳半径 km
ECL_RMOON_P = 0.2725076 * ECL_A        # 1738.09 km  外切用
ECL_RMOON_U = 0.272281 * ECL_A         # 1736.65 km  内切用


def eph_sun_moon_jd(jd_ut):
    """按儒略日取 (太阳, 月亮) 地心视位置。支持公元前 (绕开 datetime)。"""
    if EPH.use_skyfield and EPH._sf:
        try:
            return _sf_sun_moon_jd(jd_ut)
        except Exception:
            pass
    jd_tt = jd_ut + delta_t_jd(jd_ut) / 86400.0
    return sun_apparent(jd_tt, jd_ut), moon_apparent(jd_tt, jd_ut)


def _sf_sun_moon_jd(jd_ut):
    sf = EPH._sf
    ts, eph = sf["ts"], sf["eph"]
    t = ts.ut1_jd(jd_ut)
    earth = eph['earth']
    out = []
    ap = {}
    for name, key, rad in (("太阳", 'sun', 695700.0), ("月亮", 'moon', 1737.4)):
        a = earth.at(t).observe(eph[key]).apparent()
        ap[name] = a
        ra_o, dec_o, dist = a.radec('date')
        dk = dist.km
        out.append(BodyPos(name, norm360(ra_o._degrees), dec_o.degrees,
                           norm360(t.gast * 15.0 - norm360(ra_o._degrees)), dk,
                           math.degrees(math.asin(rad / dk)) * 60.0,
                           math.degrees(math.asin(EARTH_RADIUS_KM / dk)) * 60.0))
    sep = ap["月亮"].separation_from(ap["太阳"]).degrees
    out[1].phase = sep
    out[1].illum = (1 - dcos(sep)) / 2.0
    return out[0], out[1]


def _body_rect(p):
    """地心赤道直角坐标 (km)。"""
    return (p.dist_km * dcos(p.dec) * dcos(p.ra),
            p.dist_km * dcos(p.dec) * dsin(p.ra),
            p.dist_km * dsin(p.dec))


def _vlen(v):
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])


def _vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _vang(a, b):
    d = _dot(a, b) / (_vlen(a) * _vlen(b))
    return math.degrees(math.acos(max(-1.0, min(1.0, d))))


def gast_jd(jd_ut):
    """格林尼治真恒星时 (度)。"""
    T = (jd_ut + delta_t_jd(jd_ut) / 86400.0 - 2451545.0) / 36525.0
    dpsi, deps, _om = nutation(T)
    return norm360(gmst_deg(jd_ut) + dpsi * dcos(mean_obliquity(T) + deps))


def _stretch(v):
    """把椭球拉成单位球的坐标 (单位: 赤道半径)。"""
    return (v[0] / ECL_A, v[1] / ECL_A, v[2] / (ECL_A * ECL_BA))


def _unstretch_latlon(P, jd_ut):
    """单位球上的点 -> (大地纬度, 经度 E+)。"""
    phis = math.degrees(math.atan2(P[2], math.hypot(P[0], P[1])))
    lat = math.degrees(math.atan(dtan(phis) / ECL_BA))
    lon = norm180(math.degrees(math.atan2(P[1], P[0])) - gast_jd(jd_ut))
    return lat, lon


def solar_geom(jd_ut, sm=None):
    """
    某时刻的日食几何。返回 dict:
      gamma    影轴到地心的最小距离 / 赤道半径 (有正负: + = 轴过地心之北)
      gamma_e  同一距离但在「椭球拉伸空间」中量 (< 1 即为中心食)
      r_pen/r_umb  基本平面上半影/本影半径 (km, r_umb<0 表示锥顶已在其前)
      pierce   中心食时影轴与地面的交点 (纬度, 经度), 否则 None
    """
    s, m = sm if sm else eph_sun_moon_jd(jd_ut)
    Sx, Mx = _body_rect(s), _body_rect(m)
    D = _vlen(_vsub(Sx, Mx))
    u = [(Mx[i] - Sx[i]) / D for i in range(3)]
    t0 = -(Mx[0] * u[0] + Mx[1] * u[1] + Mx[2] * u[2])
    C = [Mx[i] + t0 * u[i] for i in range(3)]
    sep_km = _vlen(C)
    tan_f1 = (ECL_RSUN + ECL_RMOON_P) / D
    tan_f2 = (ECL_RSUN - ECL_RMOON_U) / D
    r_pen = ECL_RMOON_P + t0 * tan_f1
    r_umb = ECL_RMOON_U - t0 * tan_f2
    # γ 的正负: C 在基本平面上朝北为正
    yv = [-u[2] * u[0], -u[2] * u[1], 1.0 - u[2] * u[2]]
    ny = _vlen(yv) or 1.0
    sgn = 1.0 if sum(C[i] * yv[i] for i in range(3)) / ny >= 0 else -1.0
    # 椭球拉伸空间: 判轴是否击中地球
    Ms, Ss = _stretch(Mx), _stretch(Sx)
    Ds = _vlen(_vsub(Ms, Ss))
    us = [(Ms[i] - Ss[i]) / Ds for i in range(3)]
    bb = sum(Ms[i] * us[i] for i in range(3))
    cc = sum(v * v for v in Ms) - 1.0
    disc = bb * bb - cc
    gamma_e = math.sqrt(max(0.0, cc + 1.0 - bb * bb))
    pierce = None
    t_near = None
    if disc > 0:
        tn = -bb - math.sqrt(disc)
        P = [Ms[i] + tn * us[i] for i in range(3)]
        pierce = _unstretch_latlon(P, jd_ut)
        Pk = (P[0] * ECL_A, P[1] * ECL_A, P[2] * ECL_A * ECL_BA)
        t_near = _vlen(_vsub(Pk, Mx))
    else:                                # 非中心: 最接近影轴的地面点
        n = math.sqrt(sum(v * v for v in (Ms[i] - bb * us[i] for i in range(3))))
        Cv = [Ms[i] - bb * us[i] for i in range(3)]
        n = _vlen(Cv) or 1.0
        pierce = _unstretch_latlon([v / n for v in Cv], jd_ut)
    return {"jd": jd_ut, "sun": s, "moon": m, "Sx": Sx, "Mx": Mx, "u": u,
            "D": D, "t0": t0, "C": C, "sep_km": sep_km,
            "gamma": sgn * sep_km / ECL_A, "gamma_e": gamma_e,
            "r_pen": r_pen, "r_umb": r_umb, "tan_f2": tan_f2,
            "central": disc > 0, "pierce": pierce, "t_near": t_near}


def solar_kind(g):
    """中心食分类: 全食 / 环食 / 全环食 (混合食)。非中心返回 '偏食'/'无'。"""
    if not g["central"]:
        return "偏食"
    r_near = ECL_RMOON_U - g["t_near"] * g["tan_f2"]
    r_t0 = ECL_RMOON_U - g["t0"] * g["tan_f2"]
    if (r_near > 0) != (r_t0 > 0):
        return "全环食"
    return "全食" if r_near > 0 else "环食"


def solar_path_width(g):
    """最大食处的本影带宽度 (km)。非中心食返回 None。"""
    if not g["central"]:
        return None
    lat, lon = g["pierce"]
    th = gast_jd(g["jd"]) + lon
    nrm = (dcos(lat) * dcos(th), dcos(lat) * dsin(th), dsin(lat))
    cosi = abs(sum(nrm[i] * g["u"][i] for i in range(3)))
    r = ECL_RMOON_U - g["t_near"] * g["tan_f2"]
    return 2.0 * abs(r) / max(0.05, cosi)


def _parab_min(f, t0, half, rounds=3):
    """抛物线迭代求 f 的极小点 (t 单位 = 日)。"""
    t, h = t0, half
    for _ in range(rounds):
        a, b, c = f(t - h), f(t), f(t + h)
        den = a - 2.0 * b + c
        if abs(den) < 1e-13:
            break
        d = 0.5 * h * (a - c) / den
        t += max(-2.0 * h, min(2.0 * h, d))
        h = max(h * 0.25, 0.5 / 86400.0)
    return t


def _bisect(f, ta, tb, n=42):
    """f(ta) 与 f(tb) 异号时求根。"""
    fa = f(ta)
    for _ in range(n):
        tm = 0.5 * (ta + tb)
        if (f(tm) < 0) == (fa < 0):
            ta = tm
        else:
            tb = tm
    return 0.5 * (ta + tb)


# ---------------------------------------------------------------------------
#  站心 (局地) 情况 —— 严格含周日视差
# ---------------------------------------------------------------------------
def observer_xyz(lat, lon, jd_ut, h_m=0.0):
    """观测者的地心赤道直角坐标 (km)。"""
    u = math.degrees(math.atan(ECL_BA * dtan(lat)))
    hk = h_m / 1000.0 / ECL_A
    rc = dcos(u) + hk * dcos(lat)
    rs = ECL_BA * dsin(u) + hk * dsin(lat)
    th = gast_jd(jd_ut) + lon
    return (ECL_A * rc * dcos(th), ECL_A * rc * dsin(th), ECL_A * rs)


def local_solar(jd_ut, lat, lon, h_m=0.0, g=None):
    """
    站心所见的日月关系。返回 dict:
      sep  日月中心视角距 (度)   sd_s 日视半径   sd_m1 月外切半径  sd_m2 月内切半径
      alt  太阳几何高度 (度, 未加折射)   az 太阳方位角
      pa   月心相对日心的位置角 (自天北极起向东量, 度)
    """
    g = g or solar_geom(jd_ut)
    O = observer_xyz(lat, lon, jd_ut, h_m)
    ds = _vsub(g["Sx"], O)
    dm = _vsub(g["Mx"], O)
    Ls, Lm = _vlen(ds), _vlen(dm)
    sd_s = math.degrees(math.asin(ECL_RSUN / Ls))
    sd_m1 = math.degrees(math.asin(ECL_RMOON_P / Lm))
    sd_m2 = math.degrees(math.asin(ECL_RMOON_U / Lm))
    sep = _vang(ds, dm)
    alt = 90.0 - _vang(O, ds)
    ra_s = norm360(math.degrees(math.atan2(ds[1], ds[0])))
    dec_s = math.degrees(math.asin(max(-1.0, min(1.0, ds[2] / Ls))))
    ra_m = norm360(math.degrees(math.atan2(dm[1], dm[0])))
    dec_m = math.degrees(math.asin(max(-1.0, min(1.0, dm[2] / Lm))))
    pa = norm360(math.degrees(math.atan2(
        dcos(dec_m) * dsin(ra_m - ra_s),
        dsin(dec_m) * dcos(dec_s) - dcos(dec_m) * dsin(dec_s) * dcos(ra_m - ra_s))))
    lha = norm360(gast_jd(jd_ut) + lon - ra_s)
    az = altaz_from_hadec(lha, dec_s, lat)[1]
    return {"sep": sep, "sd_s": sd_s, "sd_m1": sd_m1, "sd_m2": sd_m2,
            "alt": alt, "az": az, "pa": pa, "ra_s": ra_s, "dec_s": dec_s,
            "ra_m": ra_m, "dec_m": dec_m, "dist_s": Ls, "dist_m": Lm,
            "lha": lha}


def eclipse_obscuration(sep, R, r):
    """被遮面积比 (R = 日视半径, r = 月视半径)。"""
    if sep >= R + r:
        return 0.0
    if sep <= abs(R - r):
        return min(1.0, (r * r) / (R * R))
    c1 = max(-1.0, min(1.0, (sep * sep + r * r - R * R) / (2 * sep * r)))
    c2 = max(-1.0, min(1.0, (sep * sep + R * R - r * r) / (2 * sep * R)))
    tri = 0.5 * math.sqrt(max(0.0, (-sep + r + R) * (sep + r - R)
                              * (sep - r + R) * (sep + r + R)))
    return (r * r * math.acos(c1) + R * R * math.acos(c2) - tri) / (math.pi * R * R)


def local_solar_contacts(jd_hint, lat, lon, h_m=0.0, wide=False):
    """
    某地的日食全过程。wide=True 时先粗扫 ±5.5 小时再收敛 (用于「本地可见」检索)。
    返回 dict: t_max/mag/obsc/kind/c1..c4/alt/az/sun_up
    """
    def sepf(t):
        return local_solar(t, lat, lon, h_m)["sep"]
    t0 = jd_hint
    if wide:
        best, bt = 1e9, jd_hint
        for i in range(-6, 7):
            t = jd_hint + i * (55.0 / 1440.0)
            v = sepf(t)
            if v < best:
                best, bt = v, t
        t0 = bt
    t_max = _parab_min(sepf, t0, 24.0 / 1440.0)
    L = local_solar(t_max, lat, lon, h_m)
    sep, ss, sm1, sm2 = L["sep"], L["sd_s"], L["sd_m1"], L["sd_m2"]
    out = {"t_max": t_max, "sep": sep, "sd_s": ss, "sd_m": sm2, "alt": L["alt"],
           "az": L["az"], "mag": 0.0, "obsc": 0.0, "kind": "无",
           "c1": None, "c2": None, "c3": None, "c4": None}
    if sep >= ss + sm1:
        return out
    central = sep < abs(ss - sm2)
    out["mag"] = (sm2 / ss) if central else (ss + sm1 - sep) / (2.0 * ss)
    out["obsc"] = eclipse_obscuration(sep, ss, sm2 if central else sm1)
    g1 = lambda t: (lambda q: q["sep"] - (q["sd_s"] + q["sd_m1"]))(
        local_solar(t, lat, lon, h_m))
    out["c1"] = _bisect(g1, t_max - 0.22, t_max)
    out["c4"] = _bisect(g1, t_max + 0.22, t_max)
    if central:
        out["kind"] = "全食" if sm2 >= ss else "环食"
        g2 = lambda t: (lambda q: q["sep"] - abs(q["sd_s"] - q["sd_m2"]))(
            local_solar(t, lat, lon, h_m))
        out["c2"] = _bisect(g2, t_max - 0.10, t_max)
        out["c3"] = _bisect(g2, t_max + 0.10, t_max)
    else:
        out["kind"] = "偏食"
    return out


# ---------------------------------------------------------------------------
#  月食 (地心现象, 各地所见相同; 只看月亮在不在地平线上)
#  影半径用经典的 1/50 放大 (Chauvenet), 与国际月食典同一约定
# ---------------------------------------------------------------------------
def lunar_geom(jd_ut, sm=None):
    s, m = sm if sm else eph_sun_moon_jd(jd_ut)
    ra_a, dec_a = norm360(s.ra + 180.0), -s.dec
    cs = (dsin(dec_a) * dsin(m.dec)
          + dcos(dec_a) * dcos(m.dec) * dcos(ra_a - m.ra))
    sep = math.degrees(math.acos(max(-1.0, min(1.0, cs))))
    pi_m = m.hp_arcmin / 60.0
    pi_s = s.hp_arcmin / 60.0
    s_s = s.sd_arcmin / 60.0
    s_m = m.sd_arcmin / 60.0
    # 影半径的大气放大: 用 Danjon 规则 (把地球半径加大 1/85), 与 NASA
    # 《五千年月食典》同一约定; 旧的 Chauvenet「影放大 2%」会大出约 9″。
    pm = 0.998340 * pi_m * (1.0 + 1.0 / 85.0)
    rho_u = pm + pi_s - s_s
    rho_p = pm + pi_s + s_s
    # 月心相对影心的位置角 (自天北极向东)
    pa = norm360(math.degrees(math.atan2(
        dcos(m.dec) * dsin(m.ra - ra_a),
        dsin(m.dec) * dcos(dec_a) - dcos(m.dec) * dsin(dec_a) * dcos(m.ra - ra_a))))
    return {"jd": jd_ut, "sep": sep, "rho_u": rho_u, "rho_p": rho_p,
            "s_m": s_m, "sun": s, "moon": m, "pa": pa,
            "ra_a": ra_a, "dec_a": dec_a,
            "mag_u": (rho_u + s_m - sep) / (2.0 * s_m),
            "mag_p": (rho_p + s_m - sep) / (2.0 * s_m)}


def lunar_contacts(jd_hint):
    f = lambda t: lunar_geom(t)["sep"]
    t_max = _parab_min(f, jd_hint, 40.0 / 1440.0)
    g = lunar_geom(t_max)
    out = {"t_max": t_max, "mag_u": g["mag_u"], "mag_p": g["mag_p"],
           "kind": "无", "p1": None, "u1": None, "u2": None, "u3": None,
           "u4": None, "p4": None, "geom": g}
    if g["mag_p"] <= 0:
        return out
    fp = lambda t: (lambda q: q["sep"] - (q["rho_p"] + q["s_m"]))(lunar_geom(t))
    out["p1"] = _bisect(fp, t_max - 0.30, t_max)
    out["p4"] = _bisect(fp, t_max + 0.30, t_max)
    out["kind"] = "半影月食"
    if g["mag_u"] > 0:
        fu = lambda t: (lambda q: q["sep"] - (q["rho_u"] + q["s_m"]))(lunar_geom(t))
        out["u1"] = _bisect(fu, t_max - 0.26, t_max)
        out["u4"] = _bisect(fu, t_max + 0.26, t_max)
        out["kind"] = "月偏食"
    if g["mag_u"] >= 1.0:
        ft = lambda t: (lambda q: q["sep"] - (q["rho_u"] - q["s_m"]))(lunar_geom(t))
        out["u2"] = _bisect(ft, t_max - 0.16, t_max)
        out["u3"] = _bisect(ft, t_max + 0.16, t_max)
        out["kind"] = "月全食"
    return out


def moon_topo_altaz(jd_ut, lat, lon, m=None):
    """月亮的站心视高度/方位 (含视差与折射)。"""
    if m is None:
        m = eph_sun_moon_jd(jd_ut)[1]
    lha = norm360(gast_jd(jd_ut) - m.ra + lon)
    a, az = altaz_from_hadec(lha, m.dec, lat)
    a -= (m.hp_arcmin / 60.0) * dcos(a)
    return a + refraction_true_to_app(a) / 60.0, az


# ---------------------------------------------------------------------------
#  Meeus 第 49 章: 平朔望 + 主要周期项 (只作为搜索起点, 误差 < 1 分钟)
# ---------------------------------------------------------------------------
def phase_jde(k):
    """k 为整数 = 朔, k+0.5 = 望。返回 (JDE(TT), F)。"""
    T = k / 1236.85
    jde = (2451550.09766 + 29.530588861 * k + 0.00015437 * T * T
           - 0.000000150 * T ** 3 + 0.00000000073 * T ** 4)
    E = 1 - 0.002516 * T - 0.0000074 * T * T
    M = 2.5534 + 29.10535670 * k - 0.0000014 * T * T - 0.00000011 * T ** 3
    Mp = (201.5643 + 385.81693528 * k + 0.0107582 * T * T
          + 0.00001238 * T ** 3 - 0.000000058 * T ** 4)
    F = (160.7108 + 390.67050284 * k - 0.0016118 * T * T
         - 0.00000227 * T ** 3 + 0.000000011 * T ** 4)
    Om = 124.7746 - 1.56375588 * k + 0.0020672 * T * T + 0.00000215 * T ** 3
    full = abs(k - math.floor(k) - 0.5) < 0.25
    c0, c1, c2, c3 = ((-0.40614, 0.17302, 0.01614, 0.01043) if full
                      else (-0.40720, 0.17241, 0.01608, 0.01039))
    jde += (c0 * dsin(Mp) + c1 * E * dsin(M) + c2 * dsin(2 * Mp)
            + c3 * dsin(2 * F)
            + 0.00734 * E * dsin(Mp - M) - 0.00515 * E * dsin(Mp + M)
            + 0.00209 * E * E * dsin(2 * M) - 0.00111 * dsin(Mp - 2 * F)
            - 0.00057 * dsin(Mp + 2 * F) + 0.00056 * E * dsin(2 * Mp + M)
            - 0.00042 * dsin(3 * Mp) + 0.00042 * E * dsin(M + 2 * F)
            + 0.00038 * E * dsin(M - 2 * F) - 0.00024 * E * dsin(2 * Mp - M)
            - 0.00017 * dsin(Om))
    return jde, F


def k_range_for_years(y0, y1):
    k0 = int(math.floor((y0 - 2000.0) * 12.3685)) - 3
    k1 = int(math.ceil((y1 + 1 - 2000.0) * 12.3685)) + 3
    return k0, k1


ECL_KIND_COLOR = {"全食": "#ff6b6b", "环食": "#ffd166", "全环食": "#ff9f45",
                  "偏食": "#8fb3d0", "月全食": "#e05c5c", "月偏食": "#e0a05c",
                  "半影月食": "#8fa9bf"}


def scan_solar_eclipses(y0, y1, progress=None, stop=None, site=None):
    """
    扫描 [y0, y1] 内的全部日食。site=(lat,lon) 时只保留该地可见者并附局地情况。
    progress(done, total) 回调; stop() 返回 True 即中止。
    返回 list of dict。
    """
    k0, k1 = k_range_for_years(y0, y1)
    total = k1 - k0 + 1
    out = []
    for idx, k in enumerate(range(k0, k1 + 1)):
        if stop and stop():
            break
        if progress and (idx % 64 == 0):
            progress(idx, total)
        jde, F = phase_jde(k)
        if abs(dsin(F)) > 0.37:                 # Meeus 判据: 绝无可能
            continue
        jd = jde - delta_t_jd(jde) / 86400.0
        t = _parab_min(lambda x: solar_geom(x)["sep_km"], jd, 0.03)
        g = solar_geom(t)
        if g["gamma_e"] >= 1.0 + g["r_pen"] / ECL_A:
            continue
        y = jd_to_cal(t)[0]
        if y < y0 or y > y1:
            continue
        lat, lon = g["pierce"]
        kind = solar_kind(g)
        c = local_solar_contacts(t, lat, lon)
        rec = {"jd": t, "kind": kind, "gamma": g["gamma"],
               "mag": c["mag"], "lat": lat, "lon": lon,
               "dur": (c["c3"] - c["c2"]) if (c["c2"] and c["c3"]) else 0.0,
               "width": solar_path_width(g), "central": g["central"],
               "sun_dist": g["sun"].dist_km, "moon_dist": g["moon"].dist_km}
        if site:
            lc = local_solar_contacts(t, site[0], site[1], wide=True)
            if lc["mag"] <= 0.0:
                continue
            # 太阳在食甚时可能已落, 但「带食而出/带食而没」仍算看得见
            ups = [lc["alt"]]
            for kk in ("c1", "c4"):
                if lc[kk]:
                    ups.append(local_solar(lc[kk], site[0], site[1])["alt"])
            if max(ups) < -0.9:
                continue
            lc["vis"] = ("全程可见" if min(ups) > -0.9 else
                         ("食甚可见·带食出没" if lc["alt"] > -0.9 else "带食出/入"))
            rec["local"] = lc
        out.append(rec)
    if progress:
        progress(total, total)
    return out


def scan_lunar_eclipses(y0, y1, progress=None, stop=None, site=None):
    """扫描 [y0, y1] 内的全部月食。site 时要求月亮在食甚前后确曾升起。"""
    k0, k1 = k_range_for_years(y0, y1)
    total = k1 - k0 + 1
    out = []
    for idx, k in enumerate(range(k0, k1 + 1)):
        if stop and stop():
            break
        if progress and (idx % 64 == 0):
            progress(idx, total)
        jde, F = phase_jde(k + 0.5)
        if abs(dsin(F)) > 0.37:
            continue
        jd = jde - delta_t_jd(jde) / 86400.0
        t = _parab_min(lambda x: lunar_geom(x)["sep"], jd, 0.03)
        g = lunar_geom(t)
        if g["mag_p"] <= 0.0:
            continue
        y = jd_to_cal(t)[0]
        if y < y0 or y > y1:
            continue
        c = lunar_contacts(t)
        if c["kind"] == "无":
            continue
        rec = {"jd": c["t_max"], "kind": c["kind"], "mag_u": c["mag_u"],
               "mag_p": c["mag_p"], "c": c,
               "dur_u": (c["u4"] - c["u1"]) if c["u1"] else 0.0,
               "dur_t": (c["u3"] - c["u2"]) if c["u2"] else 0.0,
               "dur_p": (c["p4"] - c["p1"]) if c["p1"] else 0.0}
        # 影心的地面正下点 (该处月亮正当头, 全程可见)
        ra_a, dec_a = g["ra_a"], g["dec_a"]
        rec["lat"] = dec_a
        rec["lon"] = norm180(ra_a - gast_jd(c["t_max"]))
        if site:
            a0 = moon_topo_altaz(c["t_max"], site[0], site[1])[0]
            t1 = c["u1"] or c["p1"]
            t2 = c["u4"] or c["p4"]
            a1 = moon_topo_altaz(t1, site[0], site[1])[0]
            a2 = moon_topo_altaz(t2, site[0], site[1])[0]
            if max(a0, a1, a2) < -0.5:
                continue
            rec["alt_max"] = a0
            rec["vis"] = ("全程可见" if min(a0, a1, a2) > -0.5
                          else ("食甚可见" if a0 > -0.5 else "带食出/入"))
        out.append(rec)
    if progress:
        progress(total, total)
    return out


def circle_lens(c1, r1, c2, r2, n=48):
    """两圆交集 (透镜形) 的多边形顶点; 无交集返回 []。用于画月食的影内部分。"""
    dx, dy = c2[0] - c1[0], c2[1] - c1[1]
    d = math.hypot(dx, dy)
    if d >= r1 + r2:
        return []
    if d <= abs(r1 - r2):
        cc, rr = (c1, r1) if r1 <= r2 else (c2, r2)
        return [(cc[0] + rr * math.cos(2 * math.pi * i / n),
                 cc[1] + rr * math.sin(2 * math.pi * i / n)) for i in range(n)]
    if d < 1e-12:
        return []
    th = math.atan2(dy, dx)
    a = (d * d + r1 * r1 - r2 * r2) / (2 * d)
    b = d - a
    a1 = math.acos(max(-1.0, min(1.0, a / r1)))
    a2 = math.acos(max(-1.0, min(1.0, b / r2)))
    pts = []
    for i in range(n + 1):
        w = th - a1 + 2 * a1 * i / n
        pts.append((c1[0] + r1 * math.cos(w), c1[1] + r1 * math.sin(w)))
    th2 = th + math.pi
    for i in range(n + 1):
        w = th2 - a2 + 2 * a2 * i / n
        pts.append((c2[0] + r2 * math.cos(w), c2[1] + r2 * math.sin(w)))
    return pts


# ===========================================================================
#  土圭 (圭表) —— 表(垂直标杆) + 圭(南北向的水平量天尺)
#  「立竿见影, 度影知时」: 正午影长随太阳赤纬变化, 是二十四节气的原始测法。
# ===========================================================================
OBLIQ_NOM = 23.4393                  # 名义黄赤交角 (仅用于「所需圭长」估算)

#  预设规格: (名称, 表高cm, 历史圭长cm或None, 默认尺长cm, 说明)
GUI_PRESETS = [
    ("小 · 桌面手搓 (20 cm 表)", 20.0, None, 0.0,
     "自己动手就能做: 3 mm 亚克力板或硬卡纸做圭, 一根 20 cm 铝条/竹签做表。\n"
     "圭面刻度用 A4 纸打印后贴上 (毫米即可读到 0.3% 的影长精度)。\n"
     "关键是表必须真正铅垂 (吊铅锤) 且圭面水平 (水平仪或注水槽), 圭必须\n"
     "严格指向真北 —— 不是磁北。用「等影法」定北: 上午与下午影长相等的两点连线\n"
     "取中垂线即是子午线。"),
    ("中 · 传统八尺表 (周公测景台)", 196.0, 300.0, 24.5,
     "《周髀算经》「周髀长八尺」。唐开元十一年 (723) 南宫说在告成立石表, 表高\n"
     "八尺 ≈ 1.96 m, 石圭长约 3 m —— 今河南登封「周公测景台」即此。\n"
     "八尺表是中国二千年间的标准器: 夏至影一尺五寸、冬至影一丈三尺 (洛阳一带),\n"
     "《周髀》《后汉书·律历志》的影长表都以此为准。"),
    ("大 · 登封观星台 (郭守敬 1276)", 946.0, 3119.0, 24.525,
     "元至元十三年郭守敬所建, 现存河南登封告成镇。台身高 9.46 m, 台顶横梁即「表」,\n"
     "较传统八尺表高出五倍, 影长随之放大五倍, 读数精度大增。\n"
     "台北的石圭俗称「量天尺」, 长 31.19 m、宽 0.53 m, 由 36 方青石接成, 两侧凿\n"
     "水槽以校水平。郭守敬另创「景符」—— 一块开小孔的铜片, 在圭上移动, 让横梁与\n"
     "太阳同时在孔后成像, 把模糊的半影边缘变成清晰的细线, 读数可到「分」(≈2.5 mm)。\n"
     "《授时历》回归年 365.2425 日即由此台测得。"),
    ("自定义", 100.0, None, 0.0, "自行填写表高与圭长。"),
]

CHI_PRESETS = [("只用公制 (cm)", 0.0), ("汉尺 23.1 cm", 23.1),
               ("唐尺 24.5 cm", 24.5), ("元尺 24.525 cm", 24.525),
               ("清营造尺 32.0 cm", 32.0), ("今市尺 33.333 cm", 33.3333)]


def gui_required_arms(H, lat):
    """
    全年正午影所需的圭长 (与表高同单位)。返回 (北臂, 南臂, 说明)。
    正午太阳高度 h = 90 - |φ - δ|, δ ∈ [-ε, +ε]。
    δ < φ 时影朝北, δ > φ 时影朝南。
    """
    eps = OBLIQ_NOM

    def arm(h):
        if h <= 0.4:
            return None                    # 太阳不升 / 影趋于无限长
        return H / dtan(h)

    north = south = 0.0
    note = []
    if lat > -eps:                         # 存在 δ < φ 的日子
        north = arm(90.0 - (lat + eps))
        if north is None:
            note.append("该纬度冬季正午太阳不升, 北臂影长无限")
    if lat < eps:                          # 存在 δ > φ 的日子
        south = arm(90.0 - (eps - lat))
        if south is None:
            note.append("该纬度夏季正午太阳不升, 南臂影长无限")
    if abs(lat) < eps:
        note.append("回归线之间: 一年有两天太阳过天顶 (正午无影), 影会南北易向, "
                    "故圭须南北双向")
    return north, south, "; ".join(note)


_GUI_SEASON_CACHE = {}


def _sun_dec_crossings(t0, t1, target, cuts=()):
    """
    太阳视赤纬 δ(t) 穿过 target 的时刻 (UTC), 二分到 30 秒以内。
    cuts 取两至时刻: δ 在两至之间单调, 每段最多穿过一次, 故不会漏根。
    返回 [(utc, +1 上升穿过 / -1 下降穿过), ...]
    """
    def f(t):
        return EPH.get("太阳", t).dec - target
    pts = [t0] + sorted(c for c in cuts if t0 < c < t1) + [t1]
    out = []
    for a, b in zip(pts[:-1], pts[1:]):
        fa, fb = f(a), f(b)
        if (fa < 0.0) == (fb < 0.0):
            continue
        lo, hi, flo = a, b, fa
        while hi - lo > dt.timedelta(seconds=30):
            mid = lo + (hi - lo) / 2
            fm = f(mid)
            if (fm < 0.0) == (flo < 0.0):
                lo, flo = mid, fm
            else:
                hi = mid
        out.append((lo + (hi - lo) / 2, 1 if fb > fa else -1))
    return out


def gui_noon_seasons(year, lat, lon, tz):
    """
    这一年里正午影朝哪边 (当地日历年)。
      zen  : 太阳过天顶 (δ = φ, 正午无影) —— 只在两回归线之间才有。
             每项 dict(utc=穿过时刻, dir=+1/-1, noon=最贴近天顶的那个当地真正午
             (UTC), zd=该正午的天顶距 |φ−δ|°)。
             dir=+1 (δ 上升穿过 φ) 之后太阳在天顶以北 → 正午影朝南;
             dir=-1 之后 → 正午影朝北。
      dark : 正午太阳中心恰在地平线的时刻 (只在极圈内), [(utc, dir), ...]
      south0: 当地 1 月 1 日 0 时正午影是否朝南 (δ > φ)
    """
    key = (year, round(lat, 4), round(lon, 4), round(tz, 3), EPH.use_skyfield)
    if key in _GUI_SEASON_CACHE:
        return _GUI_SEASON_CACHE[key]
    t0 = dt.datetime(year, 1, 1) - dt.timedelta(hours=tz)
    t1 = dt.datetime(year + 1, 1, 1) - dt.timedelta(hours=tz)
    cuts = []
    for y in (year - 1, year, year + 1):
        for lam in (90.0, 270.0):
            try:
                cuts.append(solar_term_utc(y, lam))
            except Exception:
                pass
    eps = OBLIQ_NOM
    zen = []
    if abs(lat) < eps + 0.05:
        for t, sgn in _sun_dec_crossings(t0, t1, lat, cuts):
            loc = t + dt.timedelta(hours=tz)
            best = None
            for dd in (-1, 0, 1):
                d0 = loc + dt.timedelta(days=dd)
                nn = local_apparent_noon(d0.year, d0.month, d0.day, lat, lon, tz)
                zd = abs(EPH.get("太阳", nn).dec - lat)
                if best is None or zd < best[1]:
                    best = (nn, zd)
            zen.append({"utc": t, "dir": sgn, "noon": best[0], "zd": best[1]})
    dark = []
    if lat > 90.0 - eps - 0.05:
        dark = _sun_dec_crossings(t0, t1, lat - 90.0, cuts)
    elif lat < -(90.0 - eps - 0.05):
        dark = _sun_dec_crossings(t0, t1, lat + 90.0, cuts)
    res = {"zen": zen, "dark": dark,
           "south0": EPH.get("太阳", t0).dec > lat}
    if len(_GUI_SEASON_CACHE) > 64:
        _GUI_SEASON_CACHE.clear()
    _GUI_SEASON_CACHE[key] = res
    return res


def gui_season_spans(year, lat, lon, tz):
    """
    把 gui_noon_seasons 的穿越点整理成本年内的区间 (当地日期):
      返回 (south_spans, dark_spans), 各为 [(起, 止), ...] (当地 datetime),
      south_spans = 正午影朝南的日子; 其余日子正午影朝北 (或无影)。
    """
    ss = gui_noon_seasons(year, lat, lon, tz)
    t0 = dt.datetime(year, 1, 1)
    t1 = dt.datetime(year + 1, 1, 1)

    def spans(events, start_on):
        out, cur = [], (t0 if start_on else None)
        for t, on in events:
            if on and cur is None:
                cur = t
            elif (not on) and cur is not None:
                out.append((cur, t))
                cur = None
        if cur is not None:
            out.append((cur, t1))
        return out

    loc = lambda u: u + dt.timedelta(hours=tz)
    if abs(lat) >= OBLIQ_NOM + 0.05:
        south = [(t0, t1)] if lat < 0 else []
    else:
        ev = sorted((loc(z["noon"]), z["dir"] > 0) for z in ss["zen"])
        south = spans(ev, ss["south0"])
    dark = []
    if ss["dark"]:
        # 北极圈内: δ 下降穿过 (φ−90) 起正午不升; 南极圈内: δ 上升穿过 (φ+90) 起
        start_dir = -1 if lat > 0 else 1
        d0 = (EPH.get("太阳", t0 - dt.timedelta(hours=tz)).dec
              < lat - 90.0) if lat > 0 else (
             EPH.get("太阳", t0 - dt.timedelta(hours=tz)).dec > lat + 90.0)
        ev = sorted((loc(t), d == start_dir) for t, d in ss["dark"])
        dark = spans(ev, d0)
    return south, dark


def gui_biao_side(lat):
    """
    表身放在零点的哪一侧, 才不会挡住正午影:
      "S"  北回归线以北 —— 影恒朝北, 表身在零点以南, 读数自表北面起 (登封即此)
      "N"  南回归线以南 —— 影恒朝南, 表身在零点以北, 读数自表南面起
      "C"  两回归线之间 —— 影南北都有, 表用细杆立在零点上, 读数自表心起
    """
    if lat >= OBLIQ_NOM:
        return "S"
    if lat <= -OBLIQ_NOM:
        return "N"
    return "C"


def gnomon_shadow(H, alt):
    """垂直表在水平面上的影长; 太阳在地平下或极低时返回 None。"""
    if alt is None or alt <= 0.05:
        return None
    return H / dtan(alt)


def gnomon_tip_en(H, alt, az):
    """影端在地平坐标 (东, 北) 的位置。"""
    L = gnomon_shadow(H, alt)
    if L is None:
        return None
    return (-L * dsin(az), -L * dcos(az))


def gnomon_penumbra(H, alt, sd_deg):
    """
    (本影端, 几何影端, 半影端) 的距离。太阳有 ~0.53° 的圆面, 影端必然是一段
    渐变的模糊带 —— 这正是郭守敬要发明「景符」的原因。
    """
    g = gnomon_shadow(H, alt)
    if g is None:
        return None
    u = gnomon_shadow(H, alt + sd_deg)
    p = gnomon_shadow(H, alt - sd_deg)
    return (u if u else 0.0, g, p if p else g * 8.0)


def local_apparent_noon(y, mo, d, lat, lon, tz):
    """当地真太阳时正午 (太阳上中天) 的 UTC 时刻。"""
    t = dt.datetime(y, mo, d, 12) - dt.timedelta(hours=tz)
    for _ in range(5):
        p = EPH.get("太阳", t)
        h = norm180(p.gha + lon)              # 地方时角, 西为正
        t -= dt.timedelta(seconds=h / 15.0 * 3600.0)
    return t


def gui_sun_at(utc, lat, lon):
    """返回 (视高度, 方位角, 真高度, 视半径°, 赤纬)。"""
    p = EPH.get("太阳", utc)
    tp = topocentric_alt(p, lat, lon, utc)
    return (tp["alt_app"], tp["az"], tp["alt_topo"], p.sd_arcmin / 60.0, p.dec)


def gui_term_rows(year, lat, lon, tz, H):
    """
    该年 24 节气当天正午的影长表。返回 list of dict:
      name/lam/date/noon_local/alt/len/dir/reading
    reading: 圭上读数, 北为正 (cm 或与 H 同单位)。
    """
    rows = []
    for name, lam in SOLAR_TERMS:
        t_term = solar_term_utc(year, lam)
        loc = t_term + dt.timedelta(hours=tz)
        noon = local_apparent_noon(loc.year, loc.month, loc.day, lat, lon, tz)
        alt, az, alt_t, sd, dec = gui_sun_at(noon, lat, lon)
        L = gnomon_shadow(H, alt)
        if L is None:
            reading, dirn = None, "无影 (太阳未升)"
        else:
            reading = -L * dcos(az)              # 北为正
            dirn = "北" if reading > 0 else ("南" if reading < 0 else "—")
        rows.append({"name": name, "lam": lam, "term_utc": t_term,
                     "date": loc.date(), "noon": noon + dt.timedelta(hours=tz),
                     "alt": alt, "dec": dec, "len": L, "reading": reading,
                     "dir": dirn, "sd": sd})
    return rows


def fmt_chi(cm, chi_cm):
    """把厘米数写成 尺寸分厘 (chi_cm <= 0 时返回空串)。"""
    if chi_cm <= 0 or cm is None:
        return ""
    sign = "-" if cm < 0 else ""
    v = abs(cm) / chi_cm                       # 单位: 尺
    chi = int(v)
    cun = int((v - chi) * 10)
    fen = int(round(((v - chi) * 10 - cun) * 10))
    if fen >= 10:
        fen = 0
        cun += 1
    if cun >= 10:
        cun = 0
        chi += 1
    if chi:
        return _T("%s%d尺%d寸%d分") % (sign, chi, cun, fen)
    if cun:
        return _T("%s%d寸%d分") % (sign, cun, fen)
    return _T("%s%d分") % (sign, fen)


def fmt_len_cm(cm):
    if cm is None:
        return "—"
    if abs(cm) >= 100:
        return "%.3f m" % (cm / 100.0)
    return "%.2f cm" % cm


def nice_step(span, want):
    """选一个「好看」的刻度步长, 使 span/step 接近 want。"""
    if span <= 0:
        return 1.0
    raw = span / max(1.0, want)
    e = math.floor(math.log10(raw))
    for m in (1.0, 2.0, 2.5, 5.0, 10.0):
        s = m * (10.0 ** e)
        if s >= raw:
            return s
    return 10.0 ** (e + 1)


class GuiBiaoTab(ttk.Frame):
    """土圭 (圭表) 三维模型 —— 任一经纬度、任一时刻的日影。"""

    SKY = "#0a0f14"

    def __init__(self, master, app):
        super().__init__(master, padding=6)
        self.app = app
        self.cam = Camera3D(az=12.0, el=26.0, dist=5.3, fov=42.0,
                            target=(0, 0, 0.3))
        self._term_cache = {}
        self._panned = False
        self.f_tick = _pick_font(app.root, MONO_FONTS, 7)
        self.f_tick_b = _pick_font(app.root, MONO_FONTS, 8, bold=True)
        self.f_lab = _pick_font(app.root, CJK_FONTS, 9)
        self.f_lab_b = _pick_font(app.root, CJK_FONTS, 10, bold=True)
        self._build()
        self.after(150, self._first)

    def _first(self):
        self._apply_preset(init=True)
        self.redraw()

    # ================== 界面 ==================
    def _build(self):
        scroll = VScrollFrame(self, width=468)
        scroll.pack(side="right", fill="y")
        R = scroll.body
        left = ttk.Frame(self)
        left.pack(side="left", fill="both", expand=True)
        self.canvas = tk.Canvas(left, bg=self.SKY, highlightthickness=0,
                                width=660, height=680)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.redraw())
        self.mouse = OrbitMouse(self.canvas, self.cam, self.redraw)
        self.mouse.on_pan = lambda: setattr(self, "_panned", True)
        self.canvas.bind("<Double-Button-1>", lambda e: self._reset_view())

        # ---- 地点 ----
        loc = ttk.LabelFrame(R, text=" 观测地点 (任一经纬度) ", padding=6)
        loc.pack(fill="x", pady=(0, 5))
        self.city_var = tk.StringVar(value=TRACK_PLACES[0][0])
        cb = ttk.Combobox(loc, textvariable=self.city_var, width=32,
                          state="readonly",
                          values=[p[0] for p in TRACK_PLACES] + ["自定义 Custom"])
        cb.grid(row=0, column=0, columnspan=4, sticky="we", pady=(0, 3))
        cb.bind("<<ComboboxSelected>>", self._on_city)
        self.lat_var = tk.StringVar(value="%.4f" % TRACK_PLACES[0][1])
        self.lon_var = tk.StringVar(value="%.4f" % TRACK_PLACES[0][2])
        self.tz_var = tk.StringVar(value="%.2f" % TRACK_PLACES[0][3])
        ttk.Label(loc, text="纬度 φ (N+)").grid(row=1, column=0, sticky="w")
        ttk.Entry(loc, textvariable=self.lat_var, width=11).grid(row=1, column=1)
        ttk.Label(loc, text="经度 λ (E+)").grid(row=1, column=2, sticky="w",
                                               padx=(8, 0))
        ttk.Entry(loc, textvariable=self.lon_var, width=11).grid(row=1, column=3)
        ttk.Label(loc, text="时区 UTC±").grid(row=2, column=0, sticky="w")
        ttk.Entry(loc, textvariable=self.tz_var, width=11).grid(row=2, column=1)
        ttk.Button(loc, text="按经度取时区", width=15,
                   command=self._tz_from_lon).grid(row=2, column=2, columnspan=2,
                                                   sticky="we", padx=(8, 0))
        for v in (self.lat_var, self.lon_var, self.tz_var):
            v.trace_add("write", lambda *a: self._invalidate())

        # ---- 规格 ----
        sp = ttk.LabelFrame(R, text=" 圭表规格 ", padding=6)
        sp.pack(fill="x", pady=(0, 5))
        self.size_var = tk.StringVar(value=GUI_PRESETS[0][0])
        rf = ttk.Frame(sp)                     # 英文名字长, 改排一列
        rf.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="w")
        ncol = 1 if LANG == "en" else 2
        for i, p in enumerate(GUI_PRESETS):
            ttk.Radiobutton(rf, text=p[0], value=p[0], variable=self.size_var,
                            command=self._apply_preset).grid(row=i // ncol,
                                                             column=i % ncol,
                                                             sticky="w")
        g = ttk.Frame(sp)
        g.grid(row=2, column=0, columnspan=2, sticky="we", pady=(5, 0))
        self.h_var = tk.StringVar(value="20.0")
        self.an_var = tk.StringVar(value="12.0")
        self.as_var = tk.StringVar(value="10.0")
        ttk.Label(g, text="表高 (cm)").grid(row=0, column=0, sticky="w")
        ttk.Entry(g, textvariable=self.h_var, width=10).grid(row=0, column=1)
        ttk.Label(g, text="圭·北臂").grid(row=0, column=2, sticky="w", padx=(8, 0))
        ttk.Entry(g, textvariable=self.an_var, width=9).grid(row=0, column=3)
        ttk.Label(g, text="圭·南臂").grid(row=1, column=2, sticky="w", padx=(8, 0))
        ttk.Entry(g, textvariable=self.as_var, width=9).grid(row=1, column=3)
        ttk.Button(g, text="按纬度自动定圭长", width=17,
                   command=self._auto_arms).grid(row=1, column=0, columnspan=2,
                                                 sticky="we", pady=(3, 0))
        for v in (self.h_var, self.an_var, self.as_var):
            v.trace_add("write", lambda *a: self._invalidate())
        cr = ttk.Frame(sp)
        cr.grid(row=3, column=0, columnspan=2, sticky="we", pady=(4, 0))
        ttk.Label(cr, text="尺长").pack(side="left")
        self.chi_var = tk.StringVar(value=CHI_PRESETS[0][0])
        ccb = ttk.Combobox(cr, textvariable=self.chi_var, width=18,
                           state="readonly", values=[c[0] for c in CHI_PRESETS])
        ccb.pack(side="left", padx=4)
        ccb.bind("<<ComboboxSelected>>", lambda e: self.redraw())
        self.obs_shape = tk.BooleanVar(value=False)
        ttk.Checkbutton(cr, text="画成观星台形制", variable=self.obs_shape,
                        command=self.redraw).pack(side="left", padx=(6, 0))
        self.spec_lab = ttk.Label(sp, text="", foreground="#8fd0c6",
                                  font=self.app.mono_font, justify="left",
                                  wraplength=440)
        self.spec_lab.grid(row=4, column=0, columnspan=2, sticky="w", pady=(4, 0))

        # ---- 圭的方位 ----
        azf = ttk.LabelFrame(R, text=" 圭的方位 (按此纬度) ", padding=6)
        azf.pack(fill="x", pady=(0, 5))
        self.az_lab = ttk.Label(azf, text="", foreground="#e8d9a8",
                                font=self.app.mono_font, justify="left",
                                wraplength=444)
        self.az_lab.pack(anchor="w")

        # ---- 时间 ----
        tm = ttk.LabelFrame(R, text=" 日期 · 时刻 (当地标准时) ", padding=6)
        tm.pack(fill="x", pady=(0, 5))
        now = utcnow() + dt.timedelta(hours=TRACK_PLACES[0][3])
        self.y_var = tk.StringVar(value=str(now.year))
        self.mo_var = tk.StringVar(value=str(now.month))
        self.d_var = tk.StringVar(value=str(now.day))
        self.h2_var = tk.StringVar(value=str(now.hour))
        self.mi_var = tk.StringVar(value="%02d" % now.minute)
        row = ttk.Frame(tm)
        row.pack(fill="x")
        for txt, var, w in (("年", self.y_var, 5), ("月", self.mo_var, 3),
                            ("日", self.d_var, 3), ("时", self.h2_var, 3),
                            ("分", self.mi_var, 3)):
            ttk.Label(row, text=txt).pack(side="left", padx=(0, 1))
            ttk.Entry(row, textvariable=var, width=w).pack(side="left", padx=(0, 6))
        self._prog = False                  # 程序自己在改日期/时刻 (不算用户手改)
        self.lock_noon = tk.BooleanVar(value=True)
        for v in (self.y_var, self.mo_var, self.d_var, self.h2_var, self.mi_var):
            v.trace_add("write", lambda *a: self._invalidate())
        for v in (self.h2_var, self.mi_var):           # 手改时/分 = 不要正午了
            v.trace_add("write", lambda *a: self._on_hm_edit())
        lk = ttk.Frame(tm)
        lk.pack(fill="x", pady=(4, 0))
        ttk.Checkbutton(lk, text="锁定当日真正午 —— 影子恒落在圭上 (预设; 改时/分即解锁)",
                        variable=self.lock_noon,
                        command=self._on_lock).pack(anchor="w")
        self.noon_lab = ttk.Label(tm, text="", foreground="#e8c56a",
                                  font=self.app.mono_font, justify="left",
                                  wraplength=444)
        self.noon_lab.pack(anchor="w", pady=(2, 0))
        r2 = ttk.Frame(tm)
        r2.pack(fill="x", pady=(4, 0))
        ttk.Button(r2, text="此刻", width=6,
                   command=self._set_now).pack(side="left")
        ttk.Button(r2, text="真正午", width=7,
                   command=self._set_noon).pack(side="left", padx=3)
        for lbl, dh in (("−1时", -1), ("+1时", 1)):
            ttk.Button(r2, text=lbl, width=6,
                       command=lambda d=dh: self._bump(hours=d)).pack(side="left",
                                                                      padx=(0, 3))
        for lbl, dd in (("−1日", -1), ("+1日", 1)):
            ttk.Button(r2, text=lbl, width=6,
                       command=lambda d=dd: self._bump(days=d)).pack(side="left",
                                                                     padx=(0, 3))

        # ---- 24 节气 ----
        jq = ttk.LabelFrame(R, text=" 24 节气快捷 (点一下 = 跳到该日真正午) ",
                            padding=6)
        jq.pack(fill="x", pady=(0, 5))
        st = ttk.Style()
        grid = ttk.Frame(jq)
        grid.pack(fill="x")
        for i, (name, lam) in enumerate(SOLAR_TERMS):
            sname = "Gq%d.TButton" % i
            st.configure(sname, background="#1d252d", foreground=TERM_COLORS[i],
                         font=self.f_lab, padding=(2, 2))
            st.map(sname, background=[("active", "#31445c")])
            ttk.Button(grid, text=name, width=5, style=sname,
                       command=lambda n=name: self._goto_term(n)
                       ).grid(row=i // 6, column=i % 6, padx=1, pady=1)
        self.mark_terms = tk.BooleanVar(value=True)
        ttk.Checkbutton(jq, text="在圭面上标出全年 24 节气的正午影端",
                        variable=self.mark_terms,
                        command=self.redraw).pack(anchor="w", pady=(5, 0))

        # ---- 显示 ----
        vw = ttk.LabelFrame(R, text=" 显示 · 视图 ", padding=6)
        vw.pack(fill="x", pady=(0, 5))
        self.o_scale = tk.BooleanVar(value=True)
        self.o_pen = tk.BooleanVar(value=True)
        self.o_track = tk.BooleanVar(value=True)
        self.o_sun = tk.BooleanVar(value=True)
        self.o_grid = tk.BooleanVar(value=True)
        self.o_chi = tk.BooleanVar(value=True)
        for i, (txt, var) in enumerate([("圭面刻度", self.o_scale),
                                        ("半影 (模糊带)", self.o_pen),
                                        ("当日影端轨迹", self.o_track),
                                        ("太阳与光线", self.o_sun),
                                        ("地面方位网格", self.o_grid),
                                        ("尺寸分刻度", self.o_chi)]):
            ttk.Checkbutton(vw, text=txt, variable=var,
                            command=self.redraw).grid(row=i // 2, column=i % 2,
                                                      sticky="w", padx=(0, 8))
        zb = ttk.Frame(vw)
        zb.grid(row=3, column=0, columnspan=2, sticky="we", pady=(6, 0))
        ttk.Button(zb, text="放大 +", width=7,
                   command=lambda: self._zoom(1 / 1.35)).pack(side="left")
        ttk.Button(zb, text="缩小 −", width=7,
                   command=lambda: self._zoom(1.35)).pack(side="left", padx=3)
        ttk.Button(zb, text="复位", width=6,
                   command=self._reset_view).pack(side="left")
        ttk.Button(zb, text="自北看", width=7,
                   command=lambda: self._view(4, 14)).pack(side="left", padx=3)
        ttk.Button(zb, text="自南看", width=7,
                   command=lambda: self._view(184, 16)).pack(side="left")
        ttk.Button(zb, text="俯视", width=6,
                   command=lambda: self._view(6, 84)).pack(side="left", padx=3)
        self.zoom_lab = ttk.Label(zb, text="1.0×", foreground="#8fb3d0")
        self.zoom_lab.pack(side="right")

        # ---- 读数 ----
        info = ttk.LabelFrame(R, text=" 此刻读数 ", padding=5)
        info.pack(fill="x", pady=(0, 5))
        self.info = ttk.Label(info, text="", justify="left",
                              font=self.app.mono_font, foreground="#d8e0e8")
        self.info.pack(anchor="w")

        # ---- 节气影长表 ----
        tb = ttk.LabelFrame(R, text=" 该年 24 节气正午影长 (点一行可跳过去) ",
                            padding=4)
        tb.pack(fill="both", expand=True)
        cols = ("t", "date", "alt", "len", "chi", "dir")
        heads = ("节气", "日期", "正午高度", "影长", "尺寸分", "向")
        wid = (48, 66, 62, 74, 88, 30)
        self.tree = ttk.Treeview(tb, columns=cols, show="headings", height=13)
        for c, h, w in zip(cols, heads, wid):
            self.tree.heading(c, text=h)
            self.tree.column(c, width=w, anchor="center", stretch=False)
        self.tree.pack(fill="both", expand=True)
        tree_hscroll(self.tree, tb)
        self.tree.bind("<<TreeviewSelect>>", self._on_pick_term)
        self.note = ttk.Label(R, foreground="#7f9bb3", font=self.f_lab,
                              justify="left", wraplength=448, text=(
            "左键拖动转视角 · 右键拖动平移 · 滚轮缩放 (改视场角, 可放到极大) · "
            "双击复位。圭面读数以表的投影边为 0 (北回归线以北 = 表北面, 南回归线以南 = 表南面, "
            "两回归线之间 = 表心), 北为正、南为负。"))
        self.note.pack(fill="x", pady=(4, 0))

    # ================== 小工具 ==================
    def _f(self, var, d=0.0):
        try:
            return float(str(var.get()).strip())
        except Exception:
            return d

    def _i(self, var, d=1):
        try:
            return int(float(str(var.get()).strip()))
        except Exception:
            return d

    def params(self):
        return self._f(self.lat_var, 3.139), self._f(self.lon_var, 101.6869), \
            self._f(self.tz_var, 8.0)

    def spec(self):
        H = max(0.5, self._f(self.h_var, 20.0))
        an = max(0.0, self._f(self.an_var, H))
        asr = max(0.0, self._f(self.as_var, 0.0))
        return H, an, asr

    def chi_cm(self):
        for n, v in CHI_PRESETS:
            if n == self.chi_var.get():
                return v
        return 0.0

    def local_dt(self):
        y = max(1, min(9998, self._i(self.y_var, 2026)))
        mo = max(1, min(12, self._i(self.mo_var, 1)))
        d = max(1, min(31, self._i(self.d_var, 1)))
        while d > 1:
            try:
                base = dt.datetime(y, mo, d)
                break
            except ValueError:
                d -= 1
        else:
            base = dt.datetime(y, mo, 1)
        return base + dt.timedelta(hours=self._i(self.h2_var, 12),
                                   minutes=self._i(self.mi_var, 0))

    def noon_utc(self):
        """当前日期在此经度的当地真正午 (太阳上中天) 的 UTC 时刻, 精确到秒以下。"""
        lat, lon, tz = self.params()
        L = self.local_dt()
        return local_apparent_noon(L.year, L.month, L.day, lat, lon, tz)

    def utc(self):
        if self.lock_noon.get():
            try:
                return self.noon_utc()
            except Exception:
                pass
        return self.local_dt() - dt.timedelta(hours=self._f(self.tz_var, 8.0))

    def _on_hm_edit(self):
        if not self._prog and self.lock_noon.get():
            self.lock_noon.set(False)          # 用户自己改了时/分 → 不再锁正午

    def _on_lock(self):
        if self.lock_noon.get():
            self._show_noon_in_entries()
        self.redraw()

    def _show_noon_in_entries(self):
        """锁定时把时/分输入框也改成正午 (四舍五入到分钟, 真正用的是精确时刻)。"""
        try:
            t = self.noon_utc() + dt.timedelta(hours=self._f(self.tz_var, 8.0))
        except Exception:
            return
        t = t + dt.timedelta(seconds=30)
        self._prog = True
        try:
            if self.h2_var.get() != str(t.hour):
                self.h2_var.set(str(t.hour))
            if self.mi_var.get() != "%02d" % t.minute:
                self.mi_var.set("%02d" % t.minute)
        finally:
            self._prog = False

    def _invalidate(self):
        if getattr(self, "_prog", False):        # 程序成批改日期时, 改完再统一重画
            return
        self._term_cache.clear()
        self.redraw()

    def _on_city(self, _e=None):
        for n, la, lo, tz in TRACK_PLACES:
            if n == self.city_var.get():
                self.lat_var.set("%.4f" % la)
                self.lon_var.set("%.4f" % lo)
                self.tz_var.set("%.2f" % tz)
                break

    def _tz_from_lon(self):
        self.tz_var.set("%.2f" % (round(self._f(self.lon_var) / 15.0)))

    def _apply_preset(self, init=False):
        for name, H, hist, chi, _txt in GUI_PRESETS:
            if name != self.size_var.get():
                continue
            if name.startswith("自定义"):
                break
            self.h_var.set("%.1f" % H)
            self.obs_shape.set(name.startswith("大"))
            for cn, cv in CHI_PRESETS:
                if abs(cv - chi) < 1e-6:
                    self.chi_var.set(cn)
                    break
            else:
                self.chi_var.set(CHI_PRESETS[0][0])
            self._auto_arms(hist)
            break
        self.redraw()

    def _auto_arms(self, hist=None):
        lat = self._f(self.lat_var, 3.139)
        H = max(0.5, self._f(self.h_var, 20.0))
        n, s, _note = gui_required_arms(H, lat)
        cap = H * 20.0                      # 极圈内影长趋于无限, 只好截断
        n = cap if n is None else min(n, cap)
        s = cap if s is None else min(s, cap)
        n = max(n * 1.12, H * 0.15)         # 留 12% 余量
        s = max(s * 1.15, H * 0.12)
        if hist:                       # 历史器物: 取历史圭长与需求的较大者
            if lat >= 0:               # 北半球影朝北: 加在北臂 (登封的量天尺在台北)
                n = max(n, hist)
            else:                      # 南半球影朝南: 镜像, 加在南臂
                s = max(s, hist)
        self.an_var.set("%.1f" % n)
        self.as_var.set("%.1f" % s)

    def _set_now(self):
        self.lock_noon.set(False)
        t = utcnow() + dt.timedelta(hours=self._f(self.tz_var, 8.0))
        self._set_dt(t)

    def _set_dt(self, t):
        self._prog = True
        try:
            self.y_var.set(str(t.year))
            self.mo_var.set(str(t.month))
            self.d_var.set(str(t.day))
            self.h2_var.set(str(t.hour))
            self.mi_var.set("%02d" % t.minute)
        finally:
            self._prog = False
        self._term_cache.clear()
        self.redraw()

    def _set_noon(self):
        self.lock_noon.set(True)
        self._show_noon_in_entries()
        self.redraw()

    def _bump(self, hours=0, days=0):
        if hours:
            self.lock_noon.set(False)          # 改钟点 = 不要正午了
        self._set_dt(self.local_dt() + dt.timedelta(hours=hours, days=days))
        if self.lock_noon.get():
            self._show_noon_in_entries()

    def _goto_term(self, name):
        lat, lon, tz = self.params()
        yr = self._i(self.y_var, 2026)
        for n, lam in SOLAR_TERMS:
            if n != name:
                continue
            t = solar_term_utc(yr, lam) + dt.timedelta(hours=tz)
            noon = local_apparent_noon(t.year, t.month, t.day, lat, lon, tz)
            self.lock_noon.set(True)               # 节气快捷 = 该日真正午
            self._set_dt(noon + dt.timedelta(hours=tz, seconds=30))
            break

    def _on_pick_term(self, _e=None):
        sel = self.tree.selection()
        if sel:
            self._goto_term(self.tree.item(sel[0], "values")[0])

    def _zoom(self, f):
        self.cam.zoom(f)
        self.redraw()

    def _view(self, az, el):
        self.cam.az, self.cam.el = az, el
        self.redraw()

    def _reset_view(self):
        self.cam.az, self.cam.el, self.cam.fov = 12.0, 26.0, 42.0
        self.cam.dist = 5.3
        self._panned = False
        self.redraw()

    def terms(self):
        lat, lon, tz = self.params()
        H, _an, _as = self.spec()
        key = (self._i(self.y_var, 2026), round(lat, 4), round(lon, 4),
               round(tz, 3), round(H, 4))
        if key not in self._term_cache:
            self._term_cache.clear()
            try:
                self._term_cache[key] = gui_term_rows(key[0], lat, lon, tz, H)
            except Exception:
                self._term_cache[key] = []
        return self._term_cache[key]

    # ================== 绘制 ==================
    def redraw(self):
        try:
            self._draw()
        except Exception as ex:
            self.canvas.delete("all")
            self.canvas.create_text(20, 20, anchor="nw", fill="#e08a8a",
                                    text=_T("绘制出错: %s") % ex,
                                    font=self.app.mono_font)

    def _draw(self):
        c = self.canvas
        c.delete("all")
        W = max(c.winfo_width(), 320)
        Hc = max(c.winfo_height(), 260)
        lat, lon, tz = self.params()
        H, an, asr = self.spec()
        utc = self.utc()
        alt, az, alt_t, sd, dec = gui_sun_at(utc, lat, lon)

        span = max(an + asr, H * 1.4, 1e-6)
        SC = 3.2 / span                      # 厘米 -> 世界单位
        Hw = H * SC
        anw, asw = an * SC, asr * SC
        Wg = max(0.055 * 3.2, min(0.42 * 3.2, (H * 0.30) * SC))   # 圭宽
        Tg = Wg * 0.22                                            # 圭厚

        if not self._panned:
            self.cam.target[0] = 0.0
            self.cam.target[1] = (anw - asw) * 0.42
            self.cam.target[2] = Hw * 0.30
        pt = Painter3D(c, self.cam, W, Hc)
        mag = self.cam.mag()

        # ---------- 地面 ----------
        GR = max(anw, asw, Hw) * 1.55 + 0.4
        if self.o_grid.get():
            ring = [(GR * dsin(a), GR * dcos(a), -Tg) for a in range(0, 360, 5)]
            pt.poly(ring, bias=180.0, fill="#0d151c", outline="#16232e")
            for rr in (GR * 0.35, GR * 0.65, GR * 0.92):
                pt.polyline([(rr * dsin(a), rr * dcos(a), -Tg + 0.002)
                             for a in range(0, 361, 6)], bias=178.0,
                            fill="#182835")
            for a in range(0, 360, 15):
                pt.line((0.0, 0.0, -Tg + 0.002),
                        (GR * dsin(a), GR * dcos(a), -Tg + 0.002), bias=178.0,
                        fill="#203546" if a % 45 == 0 else "#16242f")
            for lbl, a, col in (("北 N 子 0°", 0, "#8fd0c6"), ("东 E 卯 90°", 90, "#5f7c93"),
                                ("南 S 午 180°", 180, "#e8c56a"), ("西 W 酉 270°", 270, "#5f7c93")):
                pt.text(((GR + 0.22) * dsin(a), (GR + 0.22) * dcos(a), -Tg + 0.05),
                        lbl, fill=col, font=self.f_lab_b, dodge=True)
            for a in range(30, 360, 30):          # 地面方位角刻度 (自北顺时针)
                if a % 90:
                    pt.text(((GR + 0.16) * dsin(a), (GR + 0.16) * dcos(a),
                             -Tg + 0.04), "%d°" % a, fill="#3f5a6e",
                            font=self.f_tick)

        # ---------- 圭 (量天尺) ----------
        y0, y1 = -asw, anw
        top = [(-Wg / 2, y0, 0.0), (Wg / 2, y0, 0.0), (Wg / 2, y1, 0.0),
               (-Wg / 2, y1, 0.0)]
        pt.poly(top, bias=2.0, fill="#3d4b57", outline="#7d8e9c", width=1)
        for xs in (-Wg / 2, Wg / 2):
            pt.poly([(xs, y0, 0.0), (xs, y1, 0.0), (xs, y1, -Tg), (xs, y0, -Tg)],
                    bias=2.5, fill="#2a353f", outline="#55636f")
        pt.poly([(-Wg / 2, y1, 0.0), (Wg / 2, y1, 0.0), (Wg / 2, y1, -Tg),
                 (-Wg / 2, y1, -Tg)], bias=2.5, fill="#222c34", outline="#55636f")
        # 两侧水槽 (校水平用)
        for xs in (-Wg * 0.40, Wg * 0.40):
            pt.poly([(xs - Wg * 0.05, y0, 0.001), (xs + Wg * 0.05, y0, 0.001),
                     (xs + Wg * 0.05, y1, 0.001), (xs - Wg * 0.05, y1, 0.001)],
                    bias=1.6, fill="#22303c", outline="")
        # 子午线
        pt.line((0, y0, 0.002), (0, y1, 0.002), bias=1.2, fill="#c9a227", width=2)
        pt.text((0, y1 + 0.13, 0.05), "子 · 北 0°", fill="#8fd0c6", font=self.f_lab_b,
                dodge=True)
        pt.text((0, y0 - 0.13, 0.05), "午 · 南 180°", fill="#e8c56a", font=self.f_lab_b,
                dodge=True)

        # ---------- 刻度 ----------
        if self.o_scale.get():
            self._ticks(pt, SC, y0, y1, Wg, mag, an, asr)

        # ---------- 表 ----------
        self._draw_biao(pt, Hw, Wg, SC, H, gui_biao_side(lat))

        # ---------- 节气标记 ----------
        rows = self.terms() if self.mark_terms.get() else []
        if rows:
            self._draw_terms(pt, rows, SC, Wg, an, asr)

        # ---------- 当日影端轨迹 ----------
        if self.o_track.get():
            self._draw_track(pt, SC, lat, lon, tz, H)

        # ---------- 影子 ----------
        pen = gnomon_penumbra(H, alt, sd)
        tip_en = gnomon_tip_en(H, alt, az)
        if tip_en and pen:
            self._draw_shadow(pt, SC, Wg, alt, az, pen, Hw)

        # ---------- 太阳 ----------
        if self.o_sun.get() and alt > 0:
            s = _enu_from_altaz(alt, az)
            d = max(anw, asw, Hw) * 1.9 + 0.6
            sp = (s[0] * d, s[1] * d, s[2] * d + Hw)
            pt.line((0.0, 0.0, Hw), sp, bias=-3.0, fill="#8a7326", width=1)
            pt.dot(sp, max(4.0, 7.0 * min(3.0, mag)), bias=-6.0,
                   fill="#ffd66b", outline="#ffeaa0")

        pt.flush()
        self._wg_cm = Wg / SC
        self._overlay(c, W, Hc, lat, lon, tz, utc, alt, az, alt_t, sd, dec,
                      H, an, asr, pen, tip_en)
        self.zoom_lab.configure(text="%.1f×" % mag)
        self._fill_tree()

    # ---- 表 ----
    def _draw_biao(self, pt, Hw, Wg, SC, H_cm, side="S"):
        if self.obs_shape.get():
            self._draw_observatory(pt, Hw, Wg, k=(-1.0 if side == "N" else 1.0))
            return
        # 表身: 北半球北面贴在 y=0 (身在南), 南半球南面贴在 y=0 (身在北),
        # 回归线之间用细杆立在零点正中 —— 影长一律自 y=0 起算
        if side == "C":
            w = max(Wg * 0.07, Hw * 0.012)
            xs = [-w / 2, w / 2]
            ys = [-w / 2, w / 2]
        else:
            w = max(Wg * 0.26, Hw * 0.035)
            xs = [-w / 2, w / 2]
            ys = [-w, 0.0] if side == "S" else [0.0, w]
        faces = [
            [(xs[0], ys[1], 0), (xs[1], ys[1], 0), (xs[1], ys[1], Hw), (xs[0], ys[1], Hw)],
            [(xs[0], ys[0], 0), (xs[1], ys[0], 0), (xs[1], ys[0], Hw), (xs[0], ys[0], Hw)],
            [(xs[0], ys[0], 0), (xs[0], ys[1], 0), (xs[0], ys[1], Hw), (xs[0], ys[0], Hw)],
            [(xs[1], ys[0], 0), (xs[1], ys[1], 0), (xs[1], ys[1], Hw), (xs[1], ys[0], Hw)],
            [(xs[0], ys[0], Hw), (xs[1], ys[0], Hw), (xs[1], ys[1], Hw), (xs[0], ys[1], Hw)],
        ]
        cols = ["#5a6a78", "#3b4854", "#46545f", "#46545f", "#8a9aa8"]
        for f, cl in zip(faces, cols):
            pt.poly(f, fill=cl, outline="#96a6b4", width=1)
        pt.avoid_pts([pp for fc in faces for pp in fc])     # 标注别躲到表身后面
        pt.dot((0.0, 0.0, Hw), 3.0, bias=-1.0, fill="#ffd66b", outline="#c9a227")
        pt.text((0.0, (w * 2.2 + 0.08) * (1.0 if side == "N" else -1.0), Hw * 0.55),
                _T("表 %g cm") % round(H_cm, 2), fill="#c9d6e2", font=self.f_lab_b,
                bias=-50.0, dodge=True)

    def _draw_observatory(self, pt, Hw, Wg, k=1.0):
        """
        登封观星台形制: 梯形台身 + 中央凹槽 + 顶部横梁 (梁即「表」)。
        k=+1 台身在横梁以南 (北半球, 影朝北); k=−1 镜像到横梁以北 (南半球)。
        """
        bw, tw = Wg * 4.6, Wg * 2.3          # 台底/台顶 半宽
        bd, td = -k * Wg * 4.6, -k * Wg * 2.3  # 台身进深 (带方向)
        sl = Wg * 0.32                        # 凹槽半宽
        base = "#4a4038"
        face = "#5c5148"
        topc = "#6d6157"
        for sgn in (-1, 1):
            x0b, x1b = sgn * sl, sgn * bw
            x0t, x1t = sgn * sl, sgn * tw
            # 迎影的立面 (梯形)
            pt.poly([(x0b, 0.0, 0.0), (x1b, 0.0, 0.0),
                     (x1t, 0.0, Hw), (x0t, 0.0, Hw)],
                    fill=face, outline="#8b7f73", width=1)
            # 外侧面
            pt.poly([(x1b, 0.0, 0.0), (x1b, bd, 0.0),
                     (x1t, td, Hw), (x1t, 0.0, Hw)],
                    fill=base, outline="#7a6f64")
            # 凹槽内壁
            pt.poly([(x0b, 0.0, 0.0), (x0b, bd * 0.55, 0.0),
                     (x0t, td * 0.55, Hw), (x0t, 0.0, Hw)],
                    fill="#3a322c", outline="#6b6058")
            # 台顶
            pt.poly([(x0t, 0.0, Hw), (x1t, 0.0, Hw),
                     (x1t, td, Hw), (x0t, td, Hw)],
                    fill=topc, outline="#95887a")
            # 背影的立面
            pt.poly([(x0b, bd, 0.0), (x1b, bd, 0.0),
                     (x1t, td, Hw), (x0t, td, Hw)],
                    fill="#413830", outline="#6b6058")
        # 横梁 = 表
        bh = Hw * 0.022
        pt.poly([(-sl, 0.0, Hw), (sl, 0.0, Hw), (sl, 0.0, Hw - bh),
                 (-sl, 0.0, Hw - bh)], bias=-0.5, fill="#c9a227",
                outline="#ffdf7a", width=1)
        pt.poly([(-sl, 0.0, Hw), (sl, 0.0, Hw), (sl, -k * bh, Hw),
                 (-sl, -k * bh, Hw)],
                bias=-0.6, fill="#e8c56a", outline="#ffdf7a")
        pt.text((0.0, td * 1.15, Hw * 1.10), "横梁 (表)", fill="#ffdf7a",
                font=self.f_lab_b)

    # ---- 刻度 ----
    def _ticks(self, pt, SC, y0w, y1w, Wg, mag, an_cm, as_cm):
        """圭面刻度: 东侧公制, 西侧尺寸分。按整数倍数取值, 保证大刻正好落在整数上。"""
        span_cm = an_cm + as_cm
        step = nice_step(span_cm / max(1.0, mag), 12.0)     # 大刻 (带标注)
        fine = step / 10.0                                   # 小刻
        show_fine = (span_cm / fine / max(1.0, mag)) < 90
        i0 = int(math.ceil(-as_cm / fine - 1e-9))
        i1 = int(math.floor(an_cm / fine + 1e-9))
        if i1 - i0 > 1200:
            i0, i1 = 0, 0
        n_lab = 0
        for k in range(i0, i1 + 1):
            v = k * fine
            yw = v * SC
            if k % 10 == 0:
                ln, col, wdt = Wg * 0.36, "#e6eff7", 2
            elif k % 2 == 0:
                ln, col, wdt = Wg * 0.22, "#9db2c4", 1
            elif show_fine:
                ln, col, wdt = Wg * 0.11, "#65788a", 1
            else:
                continue
            pt.line((Wg / 2, yw, 0.003), (Wg / 2 - ln, yw, 0.003), bias=1.0,
                    fill=col, width=wdt)
            if k % 10 == 0 and n_lab < 46:
                n_lab += 1
                pt.text((Wg / 2 + Wg * 0.24, yw, 0.02),
                        ("%g" % round(v, 6)), bias=1.0, fill="#c4d3e0",
                        font=self.f_tick)
        pt.text((Wg / 2 + Wg * 0.34, y1w * 0.30, 0.06), "cm  (公制)",
                bias=1.0, fill="#8fb3d0", font=self.f_tick_b)

        chi = self.chi_cm()
        if not (self.o_chi.get() and chi > 0):
            return
        fen = chi / 100.0                       # 1 分 = 1/100 尺
        show_fen = (span_cm / fen / max(1.0, mag)) < 120
        j0 = int(math.ceil(-as_cm / fen - 1e-9))
        j1 = int(math.floor(an_cm / fen + 1e-9))
        if j1 - j0 > 1600:
            show_fen = False
        n_lab = 0
        for k in range(j0, j1 + 1):
            if not show_fen and k % 10:
                continue
            v = k * fen
            yw = v * SC
            if k % 100 == 0:
                ln, col, wdt = Wg * 0.36, "#e8c56a", 2
            elif k % 10 == 0:
                ln, col, wdt = Wg * 0.21, "#b79a52", 1
            elif show_fen:
                ln, col, wdt = Wg * 0.10, "#7d6c3c", 1
            else:
                continue
            pt.line((-Wg / 2, yw, 0.003), (-Wg / 2 + ln, yw, 0.003), bias=1.0,
                    fill=col, width=wdt)
            if k % 100 == 0 and n_lab < 42:
                n_lab += 1
                ci = k // 100
                txt = (_T("%s尺") % CN_NUM10(ci)) if 0 <= ci < 100 else _T("%d尺") % ci
                if ci < 0:
                    txt = _T("南%s尺") % (CN_NUM10(-ci) if -ci < 100 else -ci)
                pt.text((-Wg / 2 - Wg * 0.28, yw, 0.02), txt, bias=1.0,
                        fill="#e8c56a", font=self.f_tick)
        pt.text((-Wg / 2 - Wg * 0.40, y1w * 0.30, 0.06), _T("尺 (1尺=%g cm)") % chi,
                bias=1.0, fill="#e8c56a", font=self.f_tick_b)

    # ---- 节气标记 ----
    def _draw_terms(self, pt, rows, SC, Wg, an_cm, as_cm):
        # 低纬度时 24 个影端可能挤在几厘米内 —— 按屏幕间距决定标不标名字
        lab_gap = (an_cm + as_cm) * SC / max(1.0, 17.0 * self.cam.mag())
        last = [None, 0]
        idx = {n: i for i, (n, _l) in enumerate(SOLAR_TERMS)}
        rows = sorted(rows, key=lambda r: (r["reading"] if r["reading"]
                                           is not None else -9e9))
        for r in rows:
            i = idx.get(r["name"], 0)
            if r["reading"] is None:
                continue
            v = r["reading"]
            if v > an_cm or v < -as_cm:
                continue
            yw = v * SC
            col = TERM_COLORS[i % len(TERM_COLORS)]
            pt.line((-Wg * 0.30, yw, 0.006), (Wg * 0.30, yw, 0.006), bias=0.6,
                    fill=col, width=2)
            pt.dot((0.0, yw, 0.008), 2.6, bias=0.4, fill=col, outline="")
            if last[0] is None or abs(yw - last[0]) >= lab_gap:
                last[0] = yw
                side = 1 if (last[1] % 2 == 0) else -1
                last[1] += 1
                pl = (Wg * (0.56 if side > 0 else -0.56), yw, 0.03)
                q1, q0 = pt.project(pl), pt.project((0.0, yw, 0.03))
                anc = "center"
                if q1 is not None and q0 is not None:   # 字往圭外侧伸, 不压到圭面
                    anc = "w" if q1[0] >= q0[0] else "e"
                pt.text(pl, r["name"], bias=0.4, fill=col, font=self.f_lab,
                        anchor=anc, dodge=True)

    # ---- 当日影端轨迹 ----
    def _draw_track(self, pt, SC, lat, lon, tz, H_cm):
        L = self.local_dt()
        base = dt.datetime(L.year, L.month, L.day) - dt.timedelta(hours=tz)
        pts = []
        for i in range(0, 97):
            t = base + dt.timedelta(minutes=15 * i)
            a, az_, _at, _sd, _d = gui_sun_at(t, lat, lon)
            if a is None or a <= 1.2:
                if pts:
                    pt.polyline(pts, bias=0.9, fill="#3f6b8c")
                    pts = []
                continue
            e, n = gnomon_tip_en(H_cm, a, az_)
            if math.hypot(e, n) > H_cm * 26:
                continue
            pts.append((e * SC, n * SC, 0.004))
        if pts:
            pt.polyline(pts, bias=0.9, fill="#3f6b8c")
        # 整点标记
        for hh in range(5, 20):
            t = base + dt.timedelta(hours=hh)
            a, az_, _at, _sd, _d = gui_sun_at(t, lat, lon)
            if a <= 2.0:
                continue
            e, n = gnomon_tip_en(H_cm, a, az_)
            if math.hypot(e, n) > H_cm * 26:
                continue
            pt.dot((e * SC, n * SC, 0.005), 2.0, bias=0.8, fill="#5f9ec0",
                   outline="")
            pt.text((e * SC, n * SC - 0.06, 0.03), "%d" % hh, bias=0.8,
                    fill="#4d7d9c", font=self.f_tick)

    # ---- 影子 ----
    def _draw_shadow(self, pt, SC, Wg, alt, az, pen, Hw):
        u_len, g_len, p_len = pen
        dx, dy = -dsin(az), -dcos(az)
        hw = Wg * 0.085
        px, py = -dy, dx                       # 影的横向
        def quad(L0, L1, col, bias):
            a = (dx * L0 * SC, dy * L0 * SC, 0.004)
            b = (dx * L1 * SC, dy * L1 * SC, 0.004)
            w0 = hw * 0.55
            w1 = hw * (0.55 + 0.6 * (L1 / max(g_len, 1e-6)))
            pt.poly([(a[0] + px * w0, a[1] + py * w0, a[2]),
                     (a[0] - px * w0, a[1] - py * w0, a[2]),
                     (b[0] - px * w1, b[1] - py * w1, b[2]),
                     (b[0] + px * w1, b[1] + py * w1, b[2])],
                    bias=bias, fill=col, outline="")
        if self.o_pen.get() and p_len > u_len:
            quad(0.0, p_len, "#243039", 0.30)          # 半影 (外)
        quad(0.0, u_len, "#070a0e", 0.20)              # 本影
        pt.line((0, 0, 0.006),
                (dx * g_len * SC, dy * g_len * SC, 0.006), bias=0.1,
                fill="#ff9f45", width=2)               # 几何影长 (景符所得)
        pt.dot((dx * g_len * SC, dy * g_len * SC, 0.008), 3.4, bias=0.0,
               fill="#ff9f45", outline="#ffd0a0")
        pt.text((dx * g_len * SC, dy * g_len * SC - 0.09, 0.06),
                _T("此刻影 %.1f° · %s") % (az_fmt(az + 180.0, 1), fmt_len_cm(g_len)),
                bias=-0.2, fill="#ffb877", font=self.f_tick_b, dodge=True)

    # ---- 文字层 ----
    def _overlay(self, c, W, Hc, lat, lon, tz, utc, alt, az, alt_t, sd, dec,
                 H, an, asr, pen, tip):
        chi = self.chi_cm()
        loc = utc + dt.timedelta(hours=tz)
        L = []
        A = L.append
        A("%s  UTC%+g   φ %s  λ %s"
          % (loc.strftime("%Y-%m-%d %H:%M:%S"), tz,
             deg_dm(lat, "N", "S"), deg_dm(lon, "E", "W")))
        A(_T("太阳: 视高度 %.4f°  真高度 %.4f°  方位 %.3f° (%s)  赤纬 %+.4f°")
          % (alt, alt_t, az_fmt(az, 3), _az_name(az), dec))
        if pen is None or tip is None:
            A("太阳在地平线下 (或过低), 无日影。")
        else:
            u_len, g_len, p_len = pen
            e, n = tip
            A(_T("影长 (自%s起): %s     圭上读数 %s %s")
              % ({"S": _en("表北面", "the gnomon's north face"),
                  "N": _en("表南面", "the gnomon's south face"),
                  "C": _en("表心", "the gnomon's axis")}[gui_biao_side(lat)],
                 fmt_len_cm(g_len), fmt_len_cm(abs(n)),
                 "北" if n > 0 else ("南" if n < 0 else "")))
            if chi > 0:
                A(_T("           尺寸分: %s     圭上读数 %s")
                  % (fmt_chi(g_len, chi), fmt_chi(n, chi)))
            A(_T("影端方位 %.2f° (%s)   偏离子午线 %s")
              % (az_fmt(az + 180.0, 2), _az_name(norm360(az + 180.0)),
                 fmt_len_cm(abs(e))))
            A(_T("半影模糊带: %s ~ %s  (宽 %s) —— 郭守敬「景符」正为消此模糊")
              % (fmt_len_cm(u_len), fmt_len_cm(p_len), fmt_len_cm(p_len - u_len)))
            A(_T("影长 / 表高 = %.5f     tan(90°−h) = %.5f") % (g_len / H, g_len / H))
        need_n, need_s, note = gui_required_arms(H, lat)
        short = []
        if need_n and an < need_n:
            short.append(_T("北臂需 ≥ %s") % fmt_len_cm(need_n))
        if need_s and asr < need_s:
            short.append(_T("南臂需 ≥ %s") % fmt_len_cm(need_s))
        A(_T("圭: 北 %s / 南 %s    此纬度全年所需 北 %s / 南 %s%s")
          % (fmt_len_cm(an), fmt_len_cm(asr),
             fmt_len_cm(need_n) if need_n else "极长", fmt_len_cm(need_s) if need_s else "0",
             ("   ⚠ " + "、".join(short)) if short else "   ✓ 够长"))
        self.info.configure(text="\n".join(L))
        if self.lock_noon.get():
            self._show_noon_in_entries()
        try:
            self.noon_lab.configure(text=self._noon_text(lat, lon, tz, utc))
        except Exception as ex:
            self.noon_lab.configure(text="(%s)" % ex)
        try:
            self.az_lab.configure(text=self._azimuth_text(
                lat, lon, tz, utc, alt, az, H, an, asr, tip))
        except Exception as ex:                       # 不让说明栏拖垮画面
            self.az_lab.configure(text=_T("(方位说明计算出错: %s)") % ex)
        for name, _h, _hist, _c, txt in GUI_PRESETS:
            if name == self.size_var.get():
                self.spec_lab.configure(text=txt)
                break
        c.create_text(10, 10, anchor="nw", fill="#7f9bb3", font=self.f_lab,
                      text=_T("土圭 · 圭表 —— 表高 %s, 圭长 %s (北) + %s (南)"
                           "   · 圭轴 = 子午线: 北臂 0° / 南臂 180°")
                           % (fmt_len_cm(H), fmt_len_cm(an), fmt_len_cm(asr)))
        c.create_text(10, Hc - 12, anchor="sw", fill="#5f7c93", font=self.f_lab,
                      text=_T("放大 %.1f×  ·  视角 方位 %.0f° 仰角 %.0f°")
                           % (self.cam.mag(), self.cam.az, self.cam.el))

    def _noon_text(self, lat, lon, tz, utc):
        """影子何时落在圭上: 当地真正午 = 12:00 − 均时差 + 经度改正 (标准时)。"""
        nn = self.noon_utc()
        loc = nn + dt.timedelta(hours=tz)
        noon_min = loc.hour * 60 + loc.minute + loc.second / 60.0 + loc.microsecond / 6e7
        lon_corr = (tz * 15.0 - lon) * 4.0                 # 分钟
        eot = 12 * 60 + lon_corr - noon_min               # 均时差 (真太阳时 − 平太阳时)
        L = [_T("影落圭上的时刻 = 当地真正午 %s (UTC%+g)")
             % (loc.strftime("%H:%M:%S"), tz),
             _T("  = 12:00 − 均时差 %+.1f 分 + 经度改正 %+.1f 分 (时区子午线 %g° − 经度 %.3f°)")
             % (eot, lon_corr, tz * 15.0, lon)]
        if not self.lock_noon.get():
            dm = (utc - nn).total_seconds() / 60.0
            L.append(_T("  此刻离正午 %+.1f 分 —— 影子%s") %
                     (dm, _en("就在圭上", "on the scale") if abs(dm) < 0.5
                      else _en("斜出圭外", "off the scale")))
        return "\n".join(L)

    def _azimuth_text(self, lat, lon, tz, utc, alt, az, H, an, asr, tip):
        """「圭的方位」栏: 圭轴方位、各臂朝向与所需长度、全年影向、日中无影日。"""
        eps = OBLIQ_NOM
        L = []
        A = L.append
        if abs(lat) >= 89.9:
            A(_T("φ %s: 极点没有子午线 —— 四面八方都是南 (或都是北),") % deg_dm(lat, "N", "S"))
            A("太阳一天里高度几乎不变, 没有「正午影」, 圭表在此不能用。")
            return "\n".join(L)
        A("圭轴方位 = 当地子午线 (真南北线), 与纬度无关:")
        A("  北臂 → 方位   0° (真北)     南臂 → 方位 180° (真南)")
        A("  表一律铅垂。随纬度倾斜的是日晷的晷针 (仰角 |φ|), 不是土圭。")
        A("  要对准真北, 不是磁北 (罗盘须改正磁偏角); 最稳用「等影法」定子午线。")
        need_n, need_s, _note = gui_required_arms(H, lat)
        if lat >= eps:
            band = "北回归线以北 → 全年正午影朝北, 只需北臂"
        elif lat <= -eps:
            band = "南回归线以南 → 全年正午影朝南, 只需南臂"
        else:
            band = "两回归线之间 → 正午影一年两度南北易向, 圭须双臂"
        A("φ %s: %s" % (deg_dm(lat, "N", "S"), band))
        if lat > -eps:
            A(_T("  北臂 →   0°  需 %s  (冬至·12 月正午 h %.2f°)")
              % (fmt_len_cm(need_n) if need_n else "∞ (正午太阳不升)",
                 90.0 - (lat + eps)))
        if lat < eps:
            A(_T("  南臂 → 180°  需 %s  (夏至·6 月正午 h %.2f°)")
              % (fmt_len_cm(need_s) if need_s else "∞ (正午太阳不升)",
                 90.0 - (eps - lat)))
        if lat >= eps:
            A(_T("  夏至正午影最短 %s (仍朝北)") % fmt_len_cm(H * dtan(lat - eps)))
        elif lat <= -eps:
            A(_T("  冬至正午影最短 %s (仍朝南)") % fmt_len_cm(H * dtan(-lat - eps)))
        yr = self._i(self.y_var, 2026)
        south, dark = gui_season_spans(yr, lat, lon, tz)
        md = lambda t: t.strftime("%m-%d")
        y0, y1 = dt.datetime(yr, 1, 1), dt.datetime(yr + 1, 1, 1)

        def wrap(spans):
            """跨年的两段 (… → 12-31 与 01-01 → …) 合成一段「→ 次年」。"""
            sp = list(spans)
            if len(sp) >= 2 and sp[0][0] == y0 and sp[-1][1] == y1:
                sp = sp[1:-1] + [(sp[-1][0], sp[0][1], True)]
            out = []
            for it in sp:
                a, b = it[0], it[1]
                nxt = len(it) > 2
                out.append("%s → %s%s" % (md(a), "次年 " if nxt else "",
                                          md(b) if b != y1 else "12-31"))
            return out
        if -eps < lat < eps:
            parts = wrap(south)
            A(_T("  %d 年 影朝南 (用南臂 180°): %s; 其余日子影朝北 (用北臂 0°)")
              % (yr, "、".join(parts) if parts else "无"))
            zen = gui_noon_seasons(yr, lat, lon, tz)["zen"]
            if zen:
                zz = sorted(zen, key=lambda z: z["noon"])
                A(_T("  日中无影 (太阳过天顶): %s   残影 ≤ %s")
                  % (" · ".join((z["noon"] + dt.timedelta(hours=tz)).strftime("%m-%d %H:%M")
                                for z in zz),
                     fmt_len_cm(H * dtan(max(z["zd"] for z in zz)))))
        for txt in wrap(dark):
            A(_T("  %d 年 正午太阳不升 (极夜, 无影): %s") % (yr, txt))
        side = gui_biao_side(lat)
        if side == "C":
            A("  表用细杆立在圭的零点正中 (南北两臂都要接影); 若用方柱,")
            A("  北臂零点在柱北面、南臂零点在柱南面。")
            if self.obs_shape.get():
                A("  ⚠ 观星台形制的台身在横梁一侧, 会挡住另一臂的正午影 —— 回归线之间不宜。")
        elif side == "N":
            A("  南半球: 表立在圭的北端, 读数自表南面起 (与登封镜像)。")
        # 今日正午
        loc = utc + dt.timedelta(hours=tz)
        nn = local_apparent_noon(loc.year, loc.month, loc.day, lat, lon, tz)
        na, naz, _x, _s, _d = gui_sun_at(nn, lat, lon)
        nl = gnomon_shadow(H, na)
        noon_s = (nn + dt.timedelta(hours=tz)).strftime("%H:%M:%S")
        if nl is None:
            A(_T("今日真正午 %s  太阳不升, 无影") % noon_s)
        elif nl < 0.005:
            A(_T("今日真正午 %s  日中无影 (h %.2f°)") % (noon_s, na))
        else:
            r = -nl * dcos(naz)
            A(_T("今日真正午 %s  影朝%s → %s  %s  (h %.2f°)")
              % (noon_s, "北" if r > 0 else "南", "0°" if r > 0 else "180°",
                 fmt_len_cm(nl), na))
        # 此刻
        if tip is None:
            A(_T("此刻 %s 太阳在地平线下, 无影") % loc.strftime("%H:%M"))
        else:
            e, n = tip
            gl = math.hypot(e, n)
            saz = norm360(az + 180.0)
            half = getattr(self, "_wg_cm", H * 0.3) / 2.0
            on = abs(e) <= half and -asr <= n <= an
            A(_T("此刻 %s 影 → %.2f° (%s)  %s, %s")
              % (loc.strftime("%H:%M"), az_fmt(saz, 2), _az_name(saz), fmt_len_cm(gl),
                 "落在圭上" if on else _T("偏离圭轴 %s —— 不在圭上") % fmt_len_cm(abs(e))))
            if not on:
                A("  (圭只接正午影; 其余时刻影本来就斜出圭外)")
        return "\n".join(L)

    def _fill_tree(self):
        rows = self.terms()
        cur = [self.tree.item(i, "values")[0] for i in self.tree.get_children()]
        if cur == [r["name"] for r in rows] and cur:
            return
        self.tree.delete(*self.tree.get_children())
        chi = self.chi_cm()
        for r in rows:
            self.tree.insert("", "end", values=(
                r["name"], r["date"].strftime("%m-%d"),
                "%.3f°" % r["alt"],
                fmt_len_cm(r["len"]) if r["len"] else "—",
                fmt_chi(r["reading"], chi) if chi > 0 else "—",
                r["dir"][:1]))
        autosize_tree(self.tree, self.app.mono_font, self.app.ui_font)


def CN_NUM10(k):
    """0..99 的中文数字 (刻度标签用); 英文模式下就用阿拉伯数字。"""
    if LANG == "en":
        return str(k)
    d = "零一二三四五六七八九"
    if k < 10:
        return d[k]
    if k < 20:
        return "十" + (d[k % 10] if k % 10 else "")
    return d[k // 10] + "十" + (d[k % 10] if k % 10 else "")


# ===========================================================================
#  日月食页 —— 任一经纬度、任意时刻的日月位置; 千年尺度的食检索; 类星图的
#  望远镜视场与全过程动画。
# ===========================================================================
import threading as _threading
import queue as _queue


ECL_SPEEDS = [("暂停", 0.0), ("1×", 1.0), ("10×", 10.0), ("60×", 60.0),
              ("300×", 300.0), ("1200×", 1200.0)]

ECL_RANGES = [("±50 年", 50), ("±100 年", 100), ("±500 年", 500),
              ("±1000 年", 1000), ("±3000 年", 3000)]


def ecl_accuracy_note(y0, y1):
    """按年代给出诚实的精度说明。"""
    lim = max(abs(y0 - 2000), abs(y1 - 2000))
    if lim <= 150:
        return ("ΔT 已由实测定出, 时刻可信到 ~1 秒, 食延时可信到 ~1 秒。", "#7fbf7f")
    if lim <= 500:
        return ("ΔT 外推, 时刻不确定度约 ±10 秒~±1 分; 经度随之有 ±0.05° 量级偏差。",
                "#c9d67a")
    if lim <= 1500:
        return ("ΔT 长期抛物线外推, 时刻不确定度可达 ±5~15 分钟; "
                "最大食点经度可差 ±3°。类型/食分仍可靠。", "#e8c56a")
    return ("远古/远未来: ΔT 抛物线的不确定度可达 ±30 分钟以上 (公元前尤甚), "
            "时刻与经度仅供参考; 但食的「有无·类型·食分·纬度」依然可靠。", "#e08a8a")


class EclipseTab(ttk.Frame):
    SKY = "#05080c"

    def __init__(self, master, app):
        super().__init__(master, padding=6)
        self.app = app
        self.jd = julian_day(utcnow())
        self.event = None            # 当前载入的食
        self.mode = "none"           # none / solar / lunar
        self.fov = 1.6               # 视场角 (度)
        self.playing = False
        self.speed = 60.0
        self._rows = []
        self._q = _queue.Queue()
        self._worker = None
        self._stop = False
        self._sync = False
        self.f_tick = _pick_font(app.root, MONO_FONTS, 7)
        self.f_lab = _pick_font(app.root, CJK_FONTS, 9)
        self.f_lab_b = _pick_font(app.root, CJK_FONTS, 10, bold=True)
        self.f_big = _pick_font(app.root, MONO_FONTS, 13, bold=True)
        self._build()
        self.after(200, self._tick)

    # ==================== 界面 ====================
    def _build(self):
        scroll = VScrollFrame(self, width=520)
        scroll.pack(side="right", fill="y")
        R = scroll.body
        left = ttk.Frame(self)
        left.pack(side="left", fill="both", expand=True)
        self.canvas = tk.Canvas(left, bg=self.SKY, highlightthickness=0,
                                width=660, height=680)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.redraw())
        self.canvas.bind("<MouseWheel>",
                         lambda e: self._zoom(1 / 1.2 if e.delta > 0 else 1.2))
        self.canvas.bind("<Button-4>", lambda e: self._zoom(1 / 1.2))
        self.canvas.bind("<Button-5>", lambda e: self._zoom(1.2))
        self.canvas.bind("<Double-Button-1>", lambda e: self._fit())

        # ---- 地点 ----
        loc = ttk.LabelFrame(R, text=" 观测地点 (任一经纬度) ", padding=6)
        loc.pack(fill="x", pady=(0, 5))
        self.city_var = tk.StringVar(value=TRACK_PLACES[0][0])
        cb = ttk.Combobox(loc, textvariable=self.city_var, width=34,
                          state="readonly",
                          values=[p[0] for p in TRACK_PLACES] + ["自定义 Custom"])
        cb.grid(row=0, column=0, columnspan=4, sticky="we", pady=(0, 3))
        cb.bind("<<ComboboxSelected>>", self._on_city)
        self.lat_var = tk.StringVar(value="%.4f" % TRACK_PLACES[0][1])
        self.lon_var = tk.StringVar(value="%.4f" % TRACK_PLACES[0][2])
        self.tz_var = tk.StringVar(value="%.2f" % TRACK_PLACES[0][3])
        ttk.Label(loc, text="纬度 φ (N+)").grid(row=1, column=0, sticky="w")
        ttk.Entry(loc, textvariable=self.lat_var, width=11).grid(row=1, column=1)
        ttk.Label(loc, text="经度 λ (E+)").grid(row=1, column=2, sticky="w",
                                               padx=(8, 0))
        ttk.Entry(loc, textvariable=self.lon_var, width=11).grid(row=1, column=3)
        ttk.Label(loc, text="时区 UTC±").grid(row=2, column=0, sticky="w")
        ttk.Entry(loc, textvariable=self.tz_var, width=11).grid(row=2, column=1)
        ttk.Button(loc, text="按经度取时区", width=15,
                   command=lambda: self.tz_var.set(
                       "%.2f" % round(self._f(self.lon_var) / 15.0))
                   ).grid(row=2, column=2, columnspan=2, sticky="we", padx=(8, 0))
        for v in (self.lat_var, self.lon_var, self.tz_var):
            v.trace_add("write", lambda *a: self.redraw())

        # ---- 时刻 ----
        tm = ttk.LabelFrame(R, text=" 时刻 (当地标准时) ", padding=6)
        tm.pack(fill="x", pady=(0, 5))
        now = utcnow() + dt.timedelta(hours=TRACK_PLACES[0][3])
        self.tv = {}
        row = ttk.Frame(tm)
        row.pack(fill="x")
        for key, txt, val, w in (("y", "年", now.year, 6), ("mo", "月", now.month, 3),
                                 ("d", "日", now.day, 3), ("h", "时", now.hour, 3),
                                 ("mi", "分", now.minute, 3),
                                 ("s", "秒", now.second, 3)):
            ttk.Label(row, text=txt).pack(side="left", padx=(0, 1))
            v = tk.StringVar(value=str(val))
            self.tv[key] = v
            ttk.Entry(row, textvariable=v, width=w).pack(side="left", padx=(0, 5))
            v.trace_add("write", lambda *a: self._time_from_entry())
        r2 = ttk.Frame(tm)
        r2.pack(fill="x", pady=(4, 0))
        ttk.Button(r2, text="此刻", width=6,
                   command=self._set_now).pack(side="left")
        for lbl, dv in (("−1日", -1.0), ("−1时", -1 / 24.0), ("−1分", -1 / 1440.0),
                        ("+1分", 1 / 1440.0), ("+1时", 1 / 24.0), ("+1日", 1.0)):
            ttk.Button(r2, text=lbl, width=6,
                       command=lambda d=dv: self._jump(d)).pack(side="left", padx=1)

        # ---- 位置读数 ----
        pos = ttk.LabelFrame(R, text=" 此刻 日 / 月 位置 ", padding=5)
        pos.pack(fill="x", pady=(0, 5))
        self.pos_lab = ttk.Label(pos, text="", justify="left",
                                 font=self.app.mono_font, foreground="#d8e0e8")
        self.pos_lab.pack(anchor="w")

        # ---- 检索 ----
        se = ttk.LabelFrame(R, text=" 日月食检索 ", padding=6)
        se.pack(fill="x", pady=(0, 5))
        self.kind_var = tk.StringVar(value="solar_local")
        kinds = [("全球日食 (列出最大食点经纬度)", "solar"),
                 ("全球月食", "lunar"),
                 ("本地可见的日食", "solar_local"),
                 ("本地可见的月食", "lunar_local")]
        for i, (txt, val) in enumerate(kinds):
            ttk.Radiobutton(se, text=txt, value=val, variable=self.kind_var
                            ).grid(row=i // 2, column=i % 2, sticky="w")
        yr = ttk.Frame(se)
        yr.grid(row=2, column=0, columnspan=2, sticky="we", pady=(5, 0))
        cy = utcnow().year
        self.y0_var = tk.StringVar(value=str(cy - 50))
        self.y1_var = tk.StringVar(value=str(cy + 50))
        ttk.Label(yr, text="年份 自").pack(side="left")
        ttk.Entry(yr, textvariable=self.y0_var, width=7).pack(side="left", padx=2)
        ttk.Label(yr, text="至").pack(side="left")
        ttk.Entry(yr, textvariable=self.y1_var, width=7).pack(side="left", padx=2)
        ttk.Label(yr, text="(负数=公元前)", foreground="#5f7c93").pack(side="left")
        pr = ttk.Frame(se)
        pr.grid(row=3, column=0, columnspan=2, sticky="we", pady=(3, 0))
        for txt, n in ECL_RANGES:
            ttk.Button(pr, text=txt, width=8,
                       command=lambda k=n: self._set_range(k)).pack(side="left",
                                                                    padx=1)
        bt = ttk.Frame(se)
        bt.grid(row=4, column=0, columnspan=2, sticky="we", pady=(5, 0))
        self.go_btn = ttk.Button(bt, text="开始检索", width=11,
                                 command=self._start_search)
        self.go_btn.pack(side="left")
        ttk.Button(bt, text="停止", width=7,
                   command=self._stop_search).pack(side="left", padx=3)
        self.prog = ttk.Progressbar(bt, mode="determinate", length=210)
        self.prog.pack(side="left", padx=6, fill="x", expand=True)
        self.cnt_lab = ttk.Label(bt, text="", foreground="#8fb3d0", width=9)
        self.cnt_lab.pack(side="right")
        self.acc_lab = ttk.Label(se, text="", foreground="#c9d67a",
                                 font=self.f_lab, wraplength=480, justify="left")
        self.acc_lab.grid(row=5, column=0, columnspan=2, sticky="w", pady=(4, 0))

        # ---- 结果表 ----
        tb = ttk.LabelFrame(R, text=" 检索结果 (双击一行 = 载入并可动画) ",
                            padding=4)
        tb.pack(fill="both", expand=True, pady=(0, 5))
        self.cols = ("a", "b", "c", "d", "e", "f", "g", "h")
        self.tree = ttk.Treeview(tb, columns=self.cols, show="headings", height=14)
        for cc in self.cols:
            self.tree.column(cc, width=60, anchor="center", stretch=False)
        vs = ttk.Scrollbar(tb, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vs.set)
        vs.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True)
        tree_hscroll(self.tree, tb)
        self.tree.bind("<Double-Button-1>", self._load_sel)
        self.tree.bind("<Return>", self._load_sel)
        lb = ttk.Frame(tb)
        lb.pack(fill="x", pady=(3, 0))
        ttk.Button(lb, text="载入选中的食", command=self._load_sel).pack(
            side="left", fill="x", expand=True)
        self.auto_move = tk.BooleanVar(value=True)
        ttk.Checkbutton(lb, text="全球检索时自动把观测点移到最大食点",
                        variable=self.auto_move).pack(side="left", padx=(6, 0))

        # ---- 动画 ----
        an = ttk.LabelFrame(R, text=" 全过程动画 ", padding=6)
        an.pack(fill="x", pady=(0, 5))
        self.tl = tk.DoubleVar(value=0.0)
        self.scale = ttk.Scale(an, from_=0.0, to=1.0, variable=self.tl,
                               orient="horizontal", command=self._on_slide)
        self.scale.pack(fill="x")
        cr = ttk.Frame(an)
        cr.pack(fill="x", pady=(4, 0))
        self.play_btn = ttk.Button(cr, text="▶ 播放", width=8,
                                   command=self._toggle_play)
        self.play_btn.pack(side="left")
        self.spd_var = tk.StringVar(value="60×")
        sc = ttk.Combobox(cr, textvariable=self.spd_var, width=7, state="readonly",
                          values=[s[0] for s in ECL_SPEEDS])
        sc.pack(side="left", padx=4)
        sc.bind("<<ComboboxSelected>>", self._on_speed)
        self.jump_bar = ttk.Frame(an)
        self.jump_bar.pack(fill="x", pady=(4, 0))
        self.contact_lab = ttk.Label(an, text="", justify="left",
                                     font=self.app.mono_font,
                                     foreground="#8fd0c6")
        self.contact_lab.pack(anchor="w", pady=(4, 0))

        # ---- 视图 ----
        vw = ttk.LabelFrame(R, text=" 视图 ", padding=6)
        vw.pack(fill="x")
        zb = ttk.Frame(vw)
        zb.pack(fill="x")
        ttk.Button(zb, text="放大 +", width=7,
                   command=lambda: self._zoom(1 / 1.5)).pack(side="left")
        ttk.Button(zb, text="缩小 −", width=7,
                   command=lambda: self._zoom(1.5)).pack(side="left", padx=3)
        ttk.Button(zb, text="适配", width=6, command=self._fit).pack(side="left")
        self.fov_lab = ttk.Label(zb, text="", foreground="#8fb3d0")
        self.fov_lab.pack(side="right")
        self.orient = tk.StringVar(value="zenith")
        ob = ttk.Frame(vw)
        ob.pack(fill="x", pady=(4, 0))
        for txt, val in (("天顶朝上 (实际所见)", "zenith"),
                         ("天北极朝上", "celestial")):
            ttk.Radiobutton(ob, text=txt, value=val, variable=self.orient,
                            command=self.redraw).pack(side="left", padx=(0, 8))
        self.o_corona = tk.BooleanVar(value=True)
        self.o_path = tk.BooleanVar(value=True)
        self.o_horizon = tk.BooleanVar(value=True)
        ob2 = ttk.Frame(vw)
        ob2.pack(fill="x", pady=(2, 0))
        for txt, var in (("日冕/贝利珠", self.o_corona), ("轨迹", self.o_path),
                         ("地平小图", self.o_horizon)):
            ttk.Checkbutton(ob2, text=txt, variable=var,
                            command=self.redraw).pack(side="left", padx=(0, 8))
        self.note = ttk.Label(R, foreground="#7f9bb3", font=self.f_lab,
                              justify="left", wraplength=500, text=(
            "滚轮缩放 (可放到 0.01° 视场, 看清食既/生光的接触点) · 双击适配。"
            "未载入食时, 画面按真实角距同时显示日与月。"))
        self.note.pack(fill="x", pady=(4, 0))

    # ==================== 小工具 ====================
    def _f(self, var, d=0.0):
        try:
            return float(str(var.get()).strip())
        except Exception:
            return d

    def _i(self, v, d=0):
        try:
            return int(float(str(v.get()).strip()))
        except Exception:
            return d

    def site(self):
        return self._f(self.lat_var, 3.139), self._f(self.lon_var, 101.6869)

    def tz(self):
        return self._f(self.tz_var, 8.0)

    def _on_city(self, _e=None):
        for n, la, lo, tz in TRACK_PLACES:
            if n == self.city_var.get():
                self.lat_var.set("%.4f" % la)
                self.lon_var.set("%.4f" % lo)
                self.tz_var.set("%.2f" % tz)
                break

    def _set_range(self, n):
        cy = utcnow().year
        self.y0_var.set(str(cy - n))
        self.y1_var.set(str(cy + n))
        y0, y1 = self._i(self.y0_var, cy), self._i(self.y1_var, cy)
        txt, col = ecl_accuracy_note(y0, y1)
        self.acc_lab.configure(text=txt, foreground=col)

    def _set_now(self):
        self.jd = julian_day(utcnow())
        self._sync_entries()
        self.redraw()

    def _jump(self, d):
        self.jd += d
        self._sync_entries()
        self.redraw()

    def _sync_entries(self):
        y, mo, d, hh, mi, ss = jd_to_cal(self.jd + self.tz() / 24.0)
        self._sync = True
        try:
            self.tv["y"].set(str(y))
            self.tv["mo"].set(str(mo))
            self.tv["d"].set(str(d))
            self.tv["h"].set(str(hh))
            self.tv["mi"].set("%02d" % mi)
            self.tv["s"].set("%02d" % int(ss))
        finally:
            self._sync = False

    def _time_from_entry(self):
        if self._sync:
            return
        try:
            self.jd = cal_to_jd(self._i(self.tv["y"], 2026),
                                max(1, min(12, self._i(self.tv["mo"], 1))),
                                max(1, min(31, self._i(self.tv["d"], 1))),
                                self._i(self.tv["h"], 0),
                                self._i(self.tv["mi"], 0),
                                self._i(self.tv["s"], 0)) - self.tz() / 24.0
        except Exception:
            return
        self.redraw()

    def _zoom(self, f):
        self.fov = max(0.01, min(180.0, self.fov * f))
        self.redraw()

    def _fit(self):
        try:
            L = local_solar(self.jd, *self.site())
            if self.mode == "lunar" and self.event:
                g = lunar_geom(self.jd)
                self.fov = max(2.0, 2.4 * (g["rho_p"] + g["s_m"]))
            elif self.mode == "solar" and self.event:
                self.fov = max(0.9, 3.0 * (L["sd_s"] + L["sd_m1"]))
            else:
                self.fov = max(1.2, min(160.0, L["sep"] * 1.7))
        except Exception:
            self.fov = 1.6
        self.redraw()

    def _on_speed(self, _e=None):
        for t, v in ECL_SPEEDS:
            if t == self.spd_var.get():
                self.speed = v
                break

    def _toggle_play(self):
        self.playing = not self.playing
        self.play_btn.configure(text="⏸ 暂停" if self.playing else "▶ 播放")

    def _on_slide(self, _v=None):
        if not self.event:
            return
        t0, t1 = self.event["span"]
        self.jd = t0 + (t1 - t0) * float(self.tl.get())
        self._sync_entries()
        self.redraw()

    def _set_tl(self):
        if not self.event:
            return
        t0, t1 = self.event["span"]
        f = 0.0 if t1 <= t0 else max(0.0, min(1.0, (self.jd - t0) / (t1 - t0)))
        self._slide_lock = True
        self.tl.set(f)
        self._slide_lock = False

    def _tick(self):
        if self.playing and self.event:
            self.jd += self.speed / 86400.0 * 0.045
            t0, t1 = self.event["span"]
            if self.jd > t1:
                self.jd = t0
            self._sync_entries()
            self._set_tl()
            self.redraw()
        self._drain()
        self.after(45, self._tick)

    # ==================== 检索 (后台线程) ====================
    def _stop_search(self):
        self._stop = True

    def _start_search(self):
        if self._worker and self._worker.is_alive():
            messagebox.showinfo("检索中", "已有检索在跑, 请先停止。")
            return
        y0, y1 = self._i(self.y0_var, 2000), self._i(self.y1_var, 2050)
        if y1 < y0:
            y0, y1 = y1, y0
        if y1 - y0 > 6200:
            messagebox.showwarning("范围过大",
                                   "单次最多 6200 年 (约 76000 个朔望月)。")
            return
        txt, col = ecl_accuracy_note(y0, y1)
        self.acc_lab.configure(text=txt, foreground=col)
        kind = self.kind_var.get()
        site = self.site() if kind.endswith("_local") else None
        self._rows = []
        self.tree.delete(*self.tree.get_children())
        self._setup_cols(kind)
        self._stop = False
        self.prog.configure(value=0, maximum=100)
        self.go_btn.configure(text="检索中…")

        q = self._q

        def prog(done, total):
            q.put(("p", 100.0 * done / max(1, total)))

        def run():
            try:
                fn = (scan_solar_eclipses if kind.startswith("solar")
                      else scan_lunar_eclipses)
                res = fn(y0, y1, progress=prog, stop=lambda: self._stop,
                         site=site)
                q.put(("r", res))
            except Exception as ex:
                q.put(("e", "%s: %s" % (type(ex).__name__, ex)))

        self._worker = _threading.Thread(target=run, daemon=True)
        self._worker.start()

    def _drain(self):
        try:
            while True:
                tag, payload = self._q.get_nowait()
                if tag == "p":
                    self.prog.configure(value=payload)
                elif tag == "r":
                    self._rows = payload
                    self._fill_rows()
                    self.go_btn.configure(text="开始检索")
                    self.prog.configure(value=100)
                    self.cnt_lab.configure(text=_T("%d 次") % len(payload))
                elif tag == "e":
                    self.go_btn.configure(text="开始检索")
                    messagebox.showerror("检索出错", payload)
        except _queue.Empty:
            pass

    def _setup_cols(self, kind):
        if kind == "solar":
            heads = ("日期时刻 UT", "类型", "γ", "食分", "最大食 纬度",
                     "最大食 经度", "中心食时长", "本影带宽")
            wid = (132, 46, 56, 54, 74, 76, 74, 66)
        elif kind == "lunar":
            heads = ("日期时刻 UT", "类型", "本影食分", "半影食分", "全食时长",
                     "偏食时长", "半影时长", "月天顶点纬度")
            wid = (132, 58, 62, 62, 74, 74, 74, 78)
        elif kind == "solar_local":
            heads = ("当地日期时刻", "本地所见", "食分", "遮蔽", "太阳高度",
                     "初亏 C1", "复圆 C4", "全/环食时长")
            wid = (132, 58, 54, 54, 62, 62, 62, 76)
        else:
            heads = ("当地日期时刻", "类型", "本影食分", "月亮高度", "可见性",
                     "全食时长", "偏食时长", "半影时长")
            wid = (132, 58, 62, 62, 68, 70, 70, 70)
        for cc, h, w in zip(self.cols, heads, wid):
            self.tree.heading(cc, text=h)
            self.tree.column(cc, width=w, anchor="center", stretch=False)

    def _fill_rows(self):
        kind = self.kind_var.get()
        tz = self.tz()
        self.tree.delete(*self.tree.get_children())
        for i, r in enumerate(self._rows):
            if kind == "solar":
                v = (fmt_jd_short(r["jd"]), r["kind"], "%+.4f" % r["gamma"],
                     "%.4f" % r["mag"], deg_dm(r["lat"], "N", "S"),
                     deg_dm(r["lon"], "E", "W"),
                     dur_str(r["dur"]) if r["dur"] else "—",
                     ("%.0f km" % r["width"]) if r["width"] else "—")
            elif kind == "lunar":
                v = (fmt_jd_short(r["jd"]), r["kind"],
                     "%.4f" % r["mag_u"] if r["mag_u"] > 0 else "—",
                     "%.4f" % r["mag_p"], dur_str(r["dur_t"]) if r["dur_t"] else "—",
                     dur_str(r["dur_u"]) if r["dur_u"] else "—",
                     dur_str(r["dur_p"]), deg_dm(r["lat"], "N", "S"))
            elif kind == "solar_local":
                lc = r["local"]
                v = (fmt_jd_short(lc["t_max"], tz),
                     lc["kind"] + ("" if lc.get("vis", "").startswith("全程")
                                   else "·带食"),
                     "%.4f" % lc["mag"], "%.1f%%" % (lc["obsc"] * 100.0),
                     "%.1f°" % lc["alt"],
                     fmt_jd(lc["c1"], tz)[-8:-3] if lc["c1"] else "—",
                     fmt_jd(lc["c4"], tz)[-8:-3] if lc["c4"] else "—",
                     dur_str(lc["c3"] - lc["c2"]) if lc["c2"] else "—")
            else:
                v = (fmt_jd_short(r["jd"], tz), r["kind"],
                     "%.4f" % r["mag_u"] if r["mag_u"] > 0 else "—",
                     "%.1f°" % r.get("alt_max", 0.0), r.get("vis", "—"),
                     dur_str(r["dur_t"]) if r["dur_t"] else "—",
                     dur_str(r["dur_u"]) if r["dur_u"] else "—",
                     dur_str(r["dur_p"]))
            self.tree.insert("", "end", iid=str(i), values=v)
        autosize_tree(self.tree, self.app.mono_font, self.app.ui_font)

    def _load_sel(self, _e=None):
        sel = self.tree.selection()
        if not sel:
            return
        try:
            r = self._rows[int(sel[0])]
        except Exception:
            return
        kind = self.kind_var.get()
        if kind.startswith("solar"):
            self._load_solar(r)
        else:
            self._load_lunar(r)

    def _load_solar(self, r):
        lat, lon = self.site()
        lc = r.get("local")
        self._moved = ""
        if lc is None:                       # 来自「全球」检索
            lc = local_solar_contacts(r["jd"], lat, lon, wide=True)
            ups = [lc["alt"]] + [local_solar(lc[k], lat, lon)["alt"]
                                 for k in ("c1", "c4") if lc[k]]
            weak = (lc["mag"] <= 0.02 or max(ups) < -0.9)
            if self.auto_move.get() or weak:
                lat, lon = r["lat"], r["lon"]
                self.lat_var.set("%.4f" % lat)
                self.lon_var.set("%.4f" % lon)
                self.tz_var.set("%.2f" % round(lon / 15.0))
                self.city_var.set("自定义 Custom")
                lc = local_solar_contacts(r["jd"], lat, lon, wide=True)
                self._moved = (_T("※ 已把观测地点移到「最大食点」%s %s%s")
                               % (deg_dm(r["lat"], "N", "S"),
                                  deg_dm(r["lon"], "E", "W"),
                                  " (原地点看不到这次食)" if weak else
                                  " —— 取消上面的勾选可留在原地点"))
                self._moved += _T(" · 时区已按该地经度改为 UTC%+g") % round(lon / 15.0)
        t0 = lc["c1"] or (lc["t_max"] - 0.08)
        t1 = lc["c4"] or (lc["t_max"] + 0.08)
        pad = (t1 - t0) * 0.05
        self.mode = "solar"
        self.event = {"rec": r, "lc": lc, "span": (t0 - pad, t1 + pad)}
        self.jd = lc["t_max"]
        self._build_jumps([("初亏 C1", lc["c1"]), ("食既 C2", lc["c2"]),
                           ("食甚", lc["t_max"]), ("生光 C3", lc["c3"]),
                           ("复圆 C4", lc["c4"])])
        self._sync_entries()
        self._set_tl()
        self._fit()

    def _load_lunar(self, r):
        c = r.get("c") or lunar_contacts(r["jd"])
        self._moved = ""
        lat, lon = self.site()
        if r.get("c") is None:               # 来自「全球」检索
            ts = [t for t in (c["p1"], c["t_max"], c["p4"]) if t]
            if (self.auto_move.get()
                    or max(moon_topo_altaz(t, lat, lon)[0] for t in ts) < -0.5):
                self.lat_var.set("%.4f" % r["lat"])
                self.lon_var.set("%.4f" % r["lon"])
                self.tz_var.set("%.2f" % round(r["lon"] / 15.0))
                self.city_var.set("自定义 Custom")
                self._moved = (_T("※ 已把观测地点移到食甚时月亮的天顶点 %s %s "
                               "(该处全程可见)")
                               % (deg_dm(r["lat"], "N", "S"),
                                  deg_dm(r["lon"], "E", "W")))
        t0 = c["p1"] or (c["t_max"] - 0.12)
        t1 = c["p4"] or (c["t_max"] + 0.12)
        pad = (t1 - t0) * 0.04
        self.mode = "lunar"
        self.event = {"rec": r, "c": c, "span": (t0 - pad, t1 + pad)}
        self.jd = c["t_max"]
        self._build_jumps([("半影始 P1", c["p1"]), ("初亏 U1", c["u1"]),
                           ("食既 U2", c["u2"]), ("食甚", c["t_max"]),
                           ("生光 U3", c["u3"]), ("复圆 U4", c["u4"]),
                           ("半影终 P4", c["p4"])])
        self._sync_entries()
        self._set_tl()
        self._fit()

    def _build_jumps(self, items):
        for w in self.jump_bar.winfo_children():
            w.destroy()
        for txt, t in items:
            if t is None:
                continue
            b = ttk.Button(self.jump_bar, text=txt, width=8,
                           command=lambda tt=t: self._goto(tt))
            b.pack(side="left", padx=1)
        VScrollFrame.refit(self.jump_bar)

    def _goto(self, t):
        self.jd = t
        self._sync_entries()
        self._set_tl()
        self.redraw()

    # ==================== 绘制 ====================
    def redraw(self):
        try:
            self._draw()
        except Exception as ex:
            self.canvas.delete("all")
            self.canvas.create_text(16, 16, anchor="nw", fill="#e08a8a",
                                    font=self.app.mono_font,
                                    text=_T("绘制出错: %s: %s") % (type(ex).__name__, ex))

    def _screen_off(self, sep, pa, q, scale):
        """角距+位置角 -> 画布位移 (像素)。"""
        p = pa - (q if self.orient.get() == "zenith" else 0.0)
        return (-sep * dsin(p) * scale, -sep * dcos(p) * scale)

    def _draw(self):
        c = self.canvas
        c.delete("all")
        W = max(c.winfo_width(), 320)
        H = max(c.winfo_height(), 260)
        lat, lon = self.site()
        tz = self.tz()
        scale = (min(W, H) * 0.44) / max(1e-6, self.fov / 2.0)
        cx, cy = W * 0.5, H * 0.46
        if self.mode == "lunar" and self.event:
            self._draw_lunar(c, W, H, cx, cy, scale, lat, lon, tz)
        else:
            self._draw_solar(c, W, H, cx, cy, scale, lat, lon, tz)
        self.fov_lab.configure(text=_T("视场 %s") % (
            "%.3f′" % (self.fov * 60) if self.fov < 0.2 else "%.2f°" % self.fov))
        self._update_pos(lat, lon, tz)
        if self.o_horizon.get():
            self._draw_horizon(c, W, H, lat, lon)

    # ---- 日食 / 日月同框 ----
    def _draw_solar(self, c, W, H, cx, cy, scale, lat, lon, tz):
        L = local_solar(self.jd, lat, lon)
        q = parallactic_angle(L["lha"], L["dec_s"], lat)
        rs = L["sd_s"] * scale
        rm = L["sd_m2"] * scale
        dx, dy = self._screen_off(L["sep"], L["pa"], q, scale)
        sep, ss, sm = L["sep"], L["sd_s"], L["sd_m2"]
        total = sep < (sm - ss)
        annular = sep < (ss - sm)
        partial = (not total) and (not annular) and sep < ss + L["sd_m1"]
        night = L["alt"] < -0.85

        # 背景: 食甚附近天色变暗
        if partial or total or annular:
            obsc = eclipse_obscuration(sep, ss, sm)
        else:
            obsc = 0.0
        bg = "#05080c" if (night or total) else mix_color(
            "#0a1622", "#04070a", min(1.0, obsc ** 3))
        c.create_rectangle(0, 0, W, H, fill=bg, outline="")

        # 轨迹
        if self.o_path.get() and self.event and self.mode == "solar":
            t0, t1 = self.event["span"]
            pts = []
            for i in range(61):
                t = t0 + (t1 - t0) * i / 60.0
                Q = local_solar(t, lat, lon)
                qq = parallactic_angle(Q["lha"], Q["dec_s"], lat)
                ox, oy = self._screen_off(Q["sep"], Q["pa"], qq, scale)
                pts += [cx + ox, cy + oy]
            if len(pts) >= 4:
                c.create_line(pts, fill="#22323f", dash=(3, 4))

        # 日冕 (全食时)
        if total and self.o_corona.get():
            self._corona(c, cx, cy, rs, rm)
        # 太阳 (带临边昏暗)
        n = 16
        for i in range(n, 0, -1):
            f = i / float(n)
            r = rs * f
            col = mix_color("#fff6d8", "#ff9d3a", (1 - f) ** 1.4)
            if night:
                col = dim_color(col, 0.45)
            c.create_oval(cx - r, cy - r, cx + r, cy + r, fill=col, outline="")
        c.create_oval(cx - rs, cy - rs, cx + rs, cy + rs, outline="#ffcf7a")
        # 月亮
        mx, my = cx + dx, cy + dy
        if sep < ss + L["sd_m1"] + 0.02:
            if total and self.o_corona.get():
                # 色球环
                c.create_oval(mx - rm * 1.012, my - rm * 1.012,
                              mx + rm * 1.012, my + rm * 1.012,
                              fill="#7a1e1e", outline="")
            c.create_oval(mx - rm, my - rm, mx + rm, my + rm,
                          fill="#0a0d11", outline="#2b3440")
            if self.o_corona.get():
                self._beads(c, cx, cy, rs, mx, my, rm)
        else:
            c.create_oval(mx - rm, my - rm, mx + rm, my + rm,
                          fill="#8e9299", outline="#c8ccd2")
        # 标注
        self._legend(c, W, H, scale)
        st = ("全食" if total else "环食" if annular
              else "偏食" if partial else "未食")
        L2 = [_T("%s   (当地 UTC%+g)") % (fmt_jd(self.jd, tz), tz),
              "UT %s" % fmt_jd(self.jd),
              _T("状态 %s   食分 %.4f   遮蔽 %.2f%%")
              % (st,
                 (sm / ss) if (total or annular) else
                 max(0.0, (ss + L["sd_m1"] - sep) / (2 * ss)),
                 obsc * 100.0),
              _T("日月中心角距 %.4f′   日视半径 %.4f′   月视半径 %.4f′")
              % (sep * 60, ss * 60, sm * 60),
              _T("太阳 高度 %+.3f°  方位 %.2f° (%s)%s")
              % (L["alt"], az_fmt(L["az"], 2), _az_name(L["az"]),
                 "   ← 在地平线下" if night else "")]
        self._head(c, W, L2, "#ffd66b" if not night else "#7f9bb3")
        self._contact_text(tz)

    def _corona(self, c, cx, cy, rs, rm):
        """日冕: 内冕用逐像素同心圈叠出平滑光晕, 外面再叠冕流与极区羽状结构。"""
        R = max(rs, rm)
        r = R * 1.004
        r_out = min(R * 3.0, 2400.0)
        step = max(1.0, R / 260.0)
        while r < r_out:
            f = (r / R - 1.0) / 2.0
            c.create_oval(cx - r, cy - r, cx + r, cy + r,
                          outline=dim_color("#eef4fd",
                                            max(0.012, 0.62 * math.exp(-f * 5.4))))
            r += step
        for k in range(240):
            a = k * (360.0 / 240.0) + 0.7
            w = ((0.5 + 0.5 * math.sin(a * 2.7 * D2R + 0.4))
                 * (0.5 + 0.5 * math.cos(a * 5.3 * D2R + 2.1))
                 * (0.6 + 0.4 * math.sin(a * 1.3 * D2R)))
            ln = 0.42 + 1.45 * (w ** 0.85)
            if abs(dsin(a)) > 0.72:                 # 极区: 短而直的羽状物
                ln *= 0.40
            segs = 8
            for i2 in range(segs):
                f0, f1 = i2 / segs, (i2 + 1) / segs
                r0, r1 = R * (1.0 + ln * f0), R * (1.0 + ln * f1)
                col = dim_color("#f4f8ff", 0.62 * (1.0 - f0) ** 1.35)
                c.create_line(cx + r0 * dsin(a), cy - r0 * dcos(a),
                              cx + r1 * dsin(a), cy - r1 * dcos(a), fill=col)

    def _beads(self, c, cx, cy, rs, mx, my, rm):
        """食既/生光前后的贝利珠与钻石环。"""
        d = math.hypot(mx - cx, my - cy)
        if rm <= rs:
            return
        gap = rm - rs - d          # >0 = 已全食且尚有余量; <0 = 尚未食既
        if abs(gap) > rs * 0.03:   # 只在食既/生光前后极短的一瞬出现
            return
        th = math.atan2(cy - my, mx - cx)      # 太阳心相对月心的方向
        for k in range(-4, 5):
            a = th + k * 0.055
            px = mx + rm * math.cos(a)
            py = my - rm * math.sin(a)
            r = 1.6 + 2.6 * math.exp(-abs(k) * 0.55)
            c.create_oval(px - r, py - r, px + r, py + r, fill="#fff3c4",
                          outline="")
        r = 3.0 + 4.5 * max(0.0, 1.0 + gap / max(rs * 0.02, 1e-6))
        c.create_oval(mx + rm * math.cos(th) - r, my - rm * math.sin(th) - r,
                      mx + rm * math.cos(th) + r, my - rm * math.sin(th) + r,
                      fill="#fffbe8", outline="")

    # ---- 月食 ----
    def _draw_lunar(self, c, W, H, cx, cy, scale, lat, lon, tz):
        g = lunar_geom(self.jd)
        m = g["moon"]
        lha = norm360(gast_jd(self.jd) - m.ra + lon)
        q = parallactic_angle(lha, m.dec, lat)
        alt, az = moon_topo_altaz(self.jd, lat, lon, m)
        Rp, Ru, rm = g["rho_p"] * scale, g["rho_u"] * scale, g["s_m"] * scale
        dx, dy = self._screen_off(g["sep"], g["pa"], q, scale)
        mx, my = cx + dx, cy + dy
        c.create_rectangle(0, 0, W, H, fill="#05080c", outline="")
        # 半影 / 本影
        c.create_oval(cx - Rp, cy - Rp, cx + Rp, cy + Rp, fill="#0d1117",
                      outline="#2b3440", dash=(4, 4))
        c.create_oval(cx - Ru, cy - Ru, cx + Ru, cy + Ru, fill="#14090a",
                      outline="#5c2a2a")
        c.create_text(cx, cy - Rp - 10, text=_T("地球半影 %.3f°") % g["rho_p"],
                      fill="#5f7c93", font=self.f_lab)
        c.create_text(cx, cy - Ru - 10, text=_T("地球本影 %.3f°") % g["rho_u"],
                      fill="#a05c5c", font=self.f_lab)
        c.create_line(cx - 6, cy, cx + 6, cy, fill="#5c2a2a")
        c.create_line(cx, cy - 6, cx, cy + 6, fill="#5c2a2a")
        # 轨迹
        if self.o_path.get() and self.event:
            t0, t1 = self.event["span"]
            pts = []
            for i in range(61):
                t = t0 + (t1 - t0) * i / 60.0
                G = lunar_geom(t)
                mm = G["moon"]
                lh = norm360(gast_jd(t) - mm.ra + lon)
                qq = parallactic_angle(lh, mm.dec, lat)
                ox, oy = self._screen_off(G["sep"], G["pa"], qq, scale)
                pts += [cx + ox, cy + oy]
            if len(pts) >= 4:
                c.create_line(pts, fill="#2b3a46", dash=(3, 4))
        # 月面
        c.create_oval(mx - rm, my - rm, mx + rm, my + rm, fill="#ded9cc",
                      outline="#f2eee2")
        # 半影: 由外向内逐层变暗 (真实半影是渐变的, 不是一刀切)
        N = 14
        for i2 in range(N):
            f = 1.0 - i2 / float(N)
            lens = circle_lens((mx, my), rm, (cx, cy), Rp * f + Ru * (1 - f), 40)
            if len(lens) >= 3:
                flat = []
                for p in lens:
                    flat += [p[0], p[1]]
                c.create_polygon(flat, outline="",
                                 fill=mix_color("#d8d3c6", "#8a8478",
                                                (i2 / (N - 1.0)) ** 0.8))
        # 本影: 边缘偏橙, 越靠影心越暗红 —— 地球大气折射进来的红光
        N = 16
        for i2 in range(N):
            f = 1.0 - i2 / float(N)
            lens = circle_lens((mx, my), rm, (cx, cy), Ru * f, 40)
            if len(lens) >= 3:
                flat = []
                for p in lens:
                    flat += [p[0], p[1]]
                c.create_polygon(flat, outline="",
                                 fill=mix_color("#a8563c", "#3a0c06",
                                                (i2 / (N - 1.0)) ** 0.75))
        c.create_oval(mx - rm, my - rm, mx + rm, my + rm, fill="", outline="#f2eee2")
        self._legend(c, W, H, scale)
        L2 = [_T("%s   (当地 UTC%+g)") % (fmt_jd(self.jd, tz), tz),
              "UT %s" % fmt_jd(self.jd),
              _T("本影食分 %s   半影食分 %.4f   月心距影心 %.4f°")
              % ("%.4f" % g["mag_u"] if g["mag_u"] > 0 else "—",
                 g["mag_p"], g["sep"]),
              _T("月亮 视高度 %+.3f°  方位 %.2f° (%s)%s")
              % (alt, az_fmt(az, 2), _az_name(az),
                 "   ← 在地平线下, 此地看不到" if alt < -0.5 else "")]
        self._head(c, W, L2, "#e0a05c")
        self._contact_text(tz)

    # ---- 公共装饰 ----
    def _legend(self, c, W, H, scale):
        """右下角比例尺。"""
        want = W * 0.16
        deg = want / scale
        for u, nm in ((1.0, "1°"), (0.5, "30′"), (1 / 6.0, "10′"),
                      (1 / 60.0, "1′"), (1 / 600.0, "6″"), (1 / 3600.0, "1″")):
            if deg >= u:
                px = u * scale
                x1, y1 = W - 18, H - 22
                c.create_line(x1 - px, y1, x1, y1, fill="#8fb3d0", width=2)
                c.create_line(x1 - px, y1 - 4, x1 - px, y1 + 4, fill="#8fb3d0")
                c.create_line(x1, y1 - 4, x1, y1 + 4, fill="#8fb3d0")
                c.create_text(x1 - px / 2, y1 - 9, text=nm, fill="#8fb3d0",
                              font=self.f_lab)
                break
        up = "天顶" if self.orient.get() == "zenith" else "天北极"
        c.create_text(W - 18, 16, anchor="ne", text="↑ %s" % up,
                      fill="#5f7c93", font=self.f_lab)

    def _head(self, c, W, lines, col):
        y = 12
        for i, t in enumerate(lines):
            c.create_text(12, y, anchor="nw", text=t,
                          fill=col if i == 2 else "#c9d6e2",
                          font=self.f_big if i == 2 else self.app.mono_font)
            y += 21 if i == 2 else 15

    def _draw_horizon(self, c, W, H, lat, lon):
        """左下角地平小图: 日与月此刻在天上的位置。"""
        r = 62
        ox, oy = 16 + r, H - 16 - r
        c.create_oval(ox - r, oy - r, ox + r, oy + r, fill="#080d13",
                      outline="#243343")
        c.create_oval(ox - r * 0.5, oy - r * 0.5, ox + r * 0.5, oy + r * 0.5,
                      outline="#182635")
        for lbl, a in (("N", 0), ("E", 90), ("S", 180), ("W", 270)):
            c.create_text(ox + (r + 8) * dsin(a), oy - (r + 8) * dcos(a),
                          text=lbl, fill="#4d6d82", font=self.f_lab)
        try:
            s, m = eph_sun_moon_jd(self.jd)
        except Exception:
            return
        for pos, col, nm in ((s, "#ffd66b", "☉"), (m, "#dcd8cc", "☾")):
            lha = norm360(gast_jd(self.jd) - pos.ra + lon)
            a, az = altaz_from_hadec(lha, pos.dec, lat)
            if pos.name == "月亮":
                a -= (pos.hp_arcmin / 60.0) * dcos(a)
            rr = r * (1.0 - max(-0.12, min(1.0, a / 90.0)))
            x = ox + rr * dsin(az)
            y = oy - rr * dcos(az)
            fill = col if a > -0.85 else dim_color(col, 0.35)
            c.create_oval(x - 5, y - 5, x + 5, y + 5, fill=fill, outline="")
            c.create_text(x, y - 11, text="%s %+.0f°" % (nm, a), fill=fill,
                          font=self.f_lab)

    def _contact_text(self, tz):
        if not self.event:
            self.contact_lab.configure(text="尚未载入任何食 —— 检索后双击一行载入。")
            return
        L = []
        if self.mode == "solar":
            lc = self.event["lc"]
            r = self.event["rec"]
            L.append(_T("全球: %s   γ %+.4f   最大食点 %s %s")
                     % (r["kind"], r["gamma"], deg_dm(r["lat"], "N", "S"),
                        deg_dm(r["lon"], "E", "W")))
            if r.get("width"):
                L.append(_T("       本影带宽 %.0f km   中心食最长 %s")
                         % (r["width"], dur_str(r["dur"])))
            L.append(_T("本地: %s  食分 %.4f  遮蔽 %.2f%%  食甚太阳高度 %.2f°")
                     % (lc["kind"], lc["mag"], lc["obsc"] * 100.0, lc["alt"]))
            for nm, k in (("初亏 C1", "c1"), ("食既 C2", "c2"),
                          ("生光 C3", "c3"), ("复圆 C4", "c4")):
                if lc[k]:
                    L.append("  %s  %s" % (nm, fmt_jd(lc[k], tz)))
            L.append(_T("  食甚      %s") % fmt_jd(lc["t_max"], tz))
            if lc["c2"] and lc["c3"]:
                L.append(_T("  %s持续 %s") % (lc["kind"], dur_str(lc["c3"] - lc["c2"])))
            if lc["c1"] and lc["c4"]:
                L.append(_T("  全过程 %s") % dur_str(lc["c4"] - lc["c1"]))
            if not lc["c2"]:
                L.append("  (本地只见偏食 —— 想看全/环食请把观测点移到中心食带内)")
        else:
            cc = self.event["c"]
            L.append(_T("%s   本影食分 %s   半影食分 %.4f")
                     % (cc["kind"],
                        "%.4f" % cc["mag_u"] if cc["mag_u"] > 0 else "— (未入本影)",
                        cc["mag_p"]))
            for nm, k in (("半影始 P1", "p1"), ("初亏 U1", "u1"),
                          ("食既 U2", "u2"), ("生光 U3", "u3"),
                          ("复圆 U4", "u4"), ("半影终 P4", "p4")):
                if cc[k]:
                    L.append("  %s  %s" % (nm, fmt_jd(cc[k], tz)))
            L.append(_T("  食甚       %s") % fmt_jd(cc["t_max"], tz))
            if cc["u2"]:
                L.append(_T("  全食持续 %s") % dur_str(cc["u3"] - cc["u2"]))
            if cc["u1"]:
                L.append(_T("  偏食持续 %s") % dur_str(cc["u4"] - cc["u1"]))
        if getattr(self, "_moved", ""):
            L.append(self._moved)
        self.contact_lab.configure(text="\n".join(L))

    def _update_pos(self, lat, lon, tz):
        try:
            s, m = eph_sun_moon_jd(self.jd)
        except Exception as ex:
            self.pos_lab.configure(text=_T("星历出错: %s") % ex)
            return
        L = []
        for p, nm in ((s, "太阳"), (m, "月亮")):
            lha = norm360(gast_jd(self.jd) - p.ra + lon)
            a, az = altaz_from_hadec(lha, p.dec, lat)
            geo = a
            if nm == "月亮":
                a -= (p.hp_arcmin / 60.0) * dcos(a)
            app = a + refraction_true_to_app(a) / 60.0
            L.append(_T("%s  α %s   δ %s   高度 %+7.3f°(视)  方位 %7.3f° %s")
                     % (nm, _ra_hms(p.ra), fmt_dec(p.dec), app, az_fmt(az, 3),
                        _az_name(az)))
            L.append(_T("      距离 %12.1f km   视半径 %.4f′   地平视差 %.4f′")
                     % (p.dist_km, p.sd_arcmin, p.hp_arcmin))
        jd_tt = self.jd + delta_t_jd(self.jd) / 86400.0
        eps = true_obliquity(jd_tt)
        ls = equ_to_ecl(s.ra, s.dec, eps)[0]
        lm = equ_to_ecl(m.ra, m.dec, eps)[0]
        el = norm360(lm - ls)
        L.append(_T("日月视黄经差 %.4f°   角距 %.4f°   月面被照亮 %.2f%%   %s")
                 % (el, _vang(_body_rect(s), _body_rect(m)), m.illum * 100.0,
                    phase_name(el)))
        self.pos_lab.configure(text="\n".join(L))


def _ra_hms(ra_deg):
    h = ra_deg / 15.0
    hh = int(h)
    mm = (h - hh) * 60.0
    return "%02dh%04.1fm" % (hh, mm)


# ===========================================================================
#  第七页: 轨 道  Orbits
#  ---------------------------------------------------------------------
#  三种画法, 都是平面/正投影, 不给自由三维 (角度写死, 只能缩放平移):
#    A 实际距离平面图 —— 上下左右各 11 AU (共 22 AU), 从黄北极看下来。
#      轨道用 VSOP87 逐点采样画出, 该偏心就偏心, 该椭圆就椭圆;
#      每颗星按「自 key in 的日期起算的一个恒星周期」画满一圈。
#    B 等距示意平面图 —— 轨道画成等间距同心圆, 只看相对方位, 不看距离。
#    C 侧面图 —— 以「当时的太阳—地球连线」为水平轴, 从黄道面内看过去,
#      竖轴 = 日心黄道 z, 一眼看出谁在日地连线之上、谁在之下。
#      横轴仍是真实的 22 AU; 竖轴因真实值只有 0.0x AU, 另给放大倍数。
#  只画 日 月 五大行星 (+ 地球)。全部可动画, 预设 电脑 1 秒 = 星图 1 日。
# ===========================================================================

import time as _time
import random as _random

# 恒星周期 (日) —— 用来决定「一周期」画多长
ORB_PERIOD = {"水星": 87.96926, "金星": 224.70080, "地球": 365.25636,
              "火星": 686.97985, "木星": 4332.589, "土星": 10759.22}
# 轨道半长径 (AU) —— 只用于等距示意图的排序与标注
ORB_A = {"水星": 0.38710, "金星": 0.72333, "地球": 1.00000,
         "火星": 1.52371, "木星": 5.20260, "土星": 9.55491}
ORB_PLANETS = ["水星", "金星", "地球", "火星", "木星", "土星"]

# 画图用配色 (仿参考图: 深底 + 浅灰轨道线)
ORB_COLOR = {"太阳": "#ffe07a", "月亮": "#d7d9dd", "水星": "#b08a76",
             "金星": "#d4a63c", "地球": "#4fa3dd", "火星": "#e8654a",
             "木星": "#ef8a68", "土星": "#ddd39c"}
ORB_ORBIT_COLOR = {"水星": "#7a6558", "金星": "#8e7434", "地球": "#3a6f92",
                   "火星": "#95483a", "木星": "#9a5c47", "土星": "#8f8a68"}
# 画面上的圆点半径 (像素, 与真实大小无关, 只求看得见)
ORB_DOTR = {"太阳": 15.0, "水星": 4.0, "金星": 6.0, "地球": 6.5, "月亮": 3.0,
            "火星": 5.0, "木星": 11.0, "土星": 10.0}
ORB_SYMBOL = {"太阳": "☉", "月亮": "☽", "水星": "☿", "金星": "♀", "地球": "⊕",
              "火星": "♂", "木星": "♃", "土星": "♄"}
# 侧面图里标注文字的错位量 (像素 dx, dy; dy 正 = 摆在星体下方)
# —— 缩到全幅时内行星全挤在中间一小团, 得把标注拉开并画引线
# 行星名的摆放次序 (先摆的先占好位置): 地球、月亮最要紧, 外行星最后
ORB_LABEL_PRI = {"地球": 0, "金星": 2, "水星": 3, "火星": 4, "木星": 5, "土星": 6}
ORB_SIDE_LAB = {"水星": (-64.0, -62.0), "金星": (-60.0, 30.0),
                "地球": (46.0, -44.0), "火星": (-26.0, 54.0),
                "木星": (34.0, -28.0), "土星": (26.0, 26.0)}

# 十二宫: 以 太阳视黄经 300° (大寒 = 水瓶座 0°) 为 子宫 0°, 之后每 30° 一宫。
# 顺序按十二辰 (太阳黄经递增 → 地支递减): 子 亥 戌 酉 申 未 午 巳 辰 卯 寅 丑。
ORB_GONG = ["子", "亥", "戌", "酉", "申", "未", "午", "巳", "辰", "卯",
            "寅", "丑"]
ORB_GONG_EN = {"子": "Zi", "丑": "Chou", "寅": "Yin", "卯": "Mao", "辰": "Chen",
               "巳": "Si", "午": "Wu", "未": "Wei", "申": "Shen", "酉": "You",
               "戌": "Xu", "亥": "Hai"}
ORB_GONG_TERM = ["大寒", "雨水", "春分", "谷雨", "小满", "夏至", "大暑",
                 "处暑", "秋分", "霜降", "小雪", "冬至"]
# 动画速度预设: (显示名, 星图日 / 真实秒)
ORB_SPEEDS = [("1 日/秒 (预设)", 1.0), ("2×", 2.0), ("5×", 5.0), ("10×", 10.0),
              ("30×", 30.0), ("100×", 100.0), ("365×", 365.0),
              ("1000×", 1000.0), ("3650×", 3650.0), ("0.2× (慢)", 0.2)]


def orb_gong_of(lam):
    """由黄经 (度) 求 (宫名, 宫内度数, 节气名)。子宫 0° = 黄经 300° = 大寒。"""
    x = (lam - 300.0) % 360.0
    i = int(x // 30.0)
    return ORB_GONG[i], x - i * 30.0, ORB_GONG_TERM[i]


def orb_lref(mode, L_earth_now):
    """
    轨道图的参考黄经 (图面正下方对应的日心黄经)。屏幕角 a = L − Lref,
    自正下方起逆时针。两种定盘, 子 0° 都恒在正下方:
      earth (预设) 日地恒定: 地球恒在正下方 = 子 0°, 日地虚线永远对准子 0°,
                   太阳、地球不动, 其余行星按 (日心黄经 − 地球日心黄经) 绕着走
      term         大寒定盘: 子宫 0° = 大寒 = 水瓶 0° (地球日心黄经 120°) 在正下方,
                   大寒那天地球在子宫 0°, 之后地球照常绕太阳 360°
    """
    if mode == "term":
        return 120.0
    return norm360(L_earth_now)


def orb_rel_pos(name, jd_tt):
    """
    日地恒定盘上的位置: (相对角, 黄道面上的日心距 AU)。
    相对角 = 该星日心黄经 − 地球日心黄经 (逆时针为正); 0° = 与地球同一方向
    (外行星 = 冲, 内行星 = 下合), 180° = 在太阳背后 (合 / 上合)。
    """
    _v, L, B, R = orb_helio_xyz(name, jd_tt)
    Le = orb_helio_xyz("地球", jd_tt)[1]
    return norm360(L - Le), R * dcos(B)


# 会合周期 (日) = 1 / |1/P − 1/P地| —— 日地恒定盘上转回原相对位置所需的时间
ORB_SYNODIC = {p: 1.0 / abs(1.0 / ORB_PERIOD[p] - 1.0 / ORB_PERIOD["地球"])
               for p in ORB_PLANETS if p != "地球"}
# 相对轨迹的取样间隔 (日): 让每段的相对角约 1.2~1.6°, 画出来是光滑曲线
ORB_REL_STEP = {"水星": 0.5, "金星": 2.0, "火星": 3.0, "木星": 1.5, "土星": 1.5}


def orb_helio_xyz(name, jd_tt):
    """日心黄道直角坐标 (AU, 当日平黄道分点)。"""
    if name == "地球":
        L, B, R = helio_ecl("earth", jd_tt)
    else:
        L, B, R = planet_helio(name, jd_tt)
    return _rect(L, B, R), L, B, R


class OrbitTab(ttk.Frame):
    BG = "#22252a"                     # 参考图那种深灰底
    HALF_AU = 11.0                     # 半幅 11 AU → 全幅 22 AU

    def __init__(self, master, app):
        super().__init__(master, padding=6)
        self.app = app
        self.view = "true"             # true / equal / side
        self.jd0 = julian_day(utcnow())      # key in 的起始日 (UT 儒略日)
        self.jd = self.jd0
        self.playing = False
        self.day_per_sec = 1.0
        self._last_wall = None
        self.zoom = 1.0                # 1.0 = 半幅正好 11 AU
        self.pan = [0.0, 0.0]
        self._drag = None
        self._orbit_cache = {}
        self._rel_cache = {}           # 日地恒定盘的相对轨迹 (逐段续算)
        self._sync = False
        self._stars = None
        self.f_lab = _pick_font(app.root, CJK_FONTS, 9)
        self.f_lab_b = _pick_font(app.root, CJK_FONTS, 10, bold=True)
        self.f_sml = _pick_font(app.root, CJK_FONTS, 8)
        self.f_num = _pick_font(app.root, MONO_FONTS, 8)
        self._build()
        self._sync_entries()
        self.after(120, self._tick)

    # ==================== 界面 ====================
    def _build(self):
        scroll = VScrollFrame(self, width=470)
        scroll.pack(side="right", fill="y")
        R = scroll.body
        left = ttk.Frame(self)
        left.pack(side="left", fill="both", expand=True)
        self.canvas = tk.Canvas(left, bg=self.BG, highlightthickness=0,
                                width=760, height=760)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", lambda e: self.redraw())
        self.canvas.bind("<MouseWheel>",
                         lambda e: self._zoom(1.15 if e.delta > 0 else 1 / 1.15))
        self.canvas.bind("<Button-4>", lambda e: self._zoom(1.15))
        self.canvas.bind("<Button-5>", lambda e: self._zoom(1 / 1.15))
        self.canvas.bind("<ButtonPress-1>", self._drag_start)
        self.canvas.bind("<B1-Motion>", self._drag_move)
        self.canvas.bind("<ButtonRelease-1>", lambda e: setattr(self, "_drag", None))
        self.canvas.bind("<Double-Button-1>", lambda e: self._fit())

        # ---- 画法 ----
        vw = ttk.LabelFrame(R, text=" 画 法 (三选一, 都是平面图, 不给自由三维) ",
                            padding=6)
        vw.pack(fill="x", pady=(0, 5))
        self.view_var = tk.StringVar(value="true")
        for txt, val in (("① 实际距离  上下左右各 11 AU (共 22 AU)", "true"),
                         ("② 等距示意  轨道等间距, 只看相对方位", "equal"),
                         ("③ 侧 面 图  以当时日地连线为水平轴", "side")):
            ttk.Radiobutton(vw, text=txt, value=val, variable=self.view_var,
                            command=self._on_view).pack(anchor="w")
        self.view_note = ttk.Label(vw, text="", foreground="#7f9bb3",
                                   font=self.f_sml, wraplength=430,
                                   justify="left")
        self.view_note.pack(anchor="w", pady=(3, 0))

        # ---- 日期 ----
        tm = ttk.LabelFrame(R, text=" 起始日期 (当地标准时) —— 输入后画面静止, "
                                    "按 ▶ 才走 ", padding=6)
        tm.pack(fill="x", pady=(0, 5))
        self.tz_var = tk.StringVar(value="8")
        self.tv = {}
        r1 = ttk.Frame(tm)
        r1.pack(fill="x")
        now = utcnow() + dt.timedelta(hours=8)
        for key, txt, val, w in (("y", "年", now.year, 6), ("mo", "月", now.month, 3),
                                 ("d", "日", now.day, 3), ("h", "时", now.hour, 3),
                                 ("mi", "分", now.minute, 3)):
            ttk.Label(r1, text=txt).pack(side="left", padx=(0, 1))
            v = tk.StringVar(value=str(val))
            self.tv[key] = v
            en = ttk.Entry(r1, textvariable=v, width=w)
            en.pack(side="left", padx=(0, 5))
            en.bind("<Return>", lambda e: self._apply_date())
        ttk.Label(r1, text="UTC±").pack(side="left")
        ez = ttk.Entry(r1, textvariable=self.tz_var, width=5)
        ez.pack(side="left")
        ez.bind("<Return>", lambda e: self._apply_date())
        r2 = ttk.Frame(tm)
        r2.pack(fill="x", pady=(4, 0))
        ttk.Button(r2, text="设为起始日 (并停住)", width=20,
                   command=self._apply_date).pack(side="left")
        ttk.Button(r2, text="此刻", width=6,
                   command=self._set_now).pack(side="left", padx=3)
        ttk.Button(r2, text="⟲ 回到起始日", width=13,
                   command=self._rewind).pack(side="left")
        self.date_lab = ttk.Label(tm, text="", foreground="#c9d67a",
                                  font=self.app.mono_font, justify="left")
        self.date_lab.pack(anchor="w", pady=(4, 0))

        # ---- 动画 ----
        an = ttk.LabelFrame(R, text=" 动 画 ", padding=6)
        an.pack(fill="x", pady=(0, 5))
        cr = ttk.Frame(an)
        cr.pack(fill="x")
        self.play_btn = ttk.Button(cr, text="▶ 播放", width=9,
                                   command=self._toggle_play)
        self.play_btn.pack(side="left")
        ttk.Button(cr, text="⏹ 停并归零", width=11,
                   command=self._rewind).pack(side="left", padx=3)
        ttk.Label(cr, text="速度").pack(side="left", padx=(8, 2))
        self.spd_var = tk.StringVar(value=ORB_SPEEDS[0][0])
        cb = ttk.Combobox(cr, textvariable=self.spd_var, width=14,
                          state="readonly", values=[s[0] for s in ORB_SPEEDS])
        cb.pack(side="left")
        cb.bind("<<ComboboxSelected>>", self._on_speed)
        cr2 = ttk.Frame(an)
        cr2.pack(fill="x", pady=(4, 0))
        ttk.Label(cr2, text="自定义: 真实 1 秒 =").pack(side="left")
        self.cust_var = tk.StringVar(value="1")
        ttk.Entry(cr2, textvariable=self.cust_var, width=9).pack(side="left", padx=3)
        ttk.Label(cr2, text="星图日").pack(side="left")
        ttk.Button(cr2, text="套用", width=6,
                   command=self._apply_custom).pack(side="left", padx=6)
        self.loop_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(an, text="地球走满一周期 (365.2564 日) 自动回到起始日",
                        variable=self.loop_var).pack(anchor="w", pady=(3, 0))
        self.clock_lab = ttk.Label(an, text="", foreground="#8fd0c6",
                                   font=self.app.mono_font, justify="left")
        self.clock_lab.pack(anchor="w", pady=(3, 0))

        # ---- 定盘 ----
        fr = ttk.LabelFrame(R, text=" 定 盘 (子 0° 恒在正下方) ", padding=6)
        fr.pack(fill="x", pady=(0, 5))
        self.frame_var = tk.StringVar(value="earth")
        for txt, val, note in (
                ("日地恒定 (预设)", "earth",
                 "太阳、地球不动, 地球恒在子 0° (正下方), 日地虚线永远对准子 0°; "
                 "其余行星绕着走, 看它们相对日地的运动。"),
                ("大寒定盘", "term",
                 "子宫 0° / 大寒 / 水瓶 0° 固定在正下方; 大寒那天地球在子宫 0°, "
                 "之后地球照常绕太阳 360°。")):
            ttk.Radiobutton(fr, text=txt, value=val, variable=self.frame_var,
                            command=self.redraw).pack(anchor="w")
            ttk.Label(fr, text=note, foreground="#b9c7d3", wraplength=410,
                      justify="left").pack(anchor="w", padx=(22, 0), pady=(0, 3))
        ttk.Label(fr, text="日地恒定盘的十二辰环以日地连线为子 0°, 环上角度 = 该星日心黄经 "
                           "− 地球日心黄经: 外行星到子 0° = 冲, 到午 0° = 合; 内行星到子 0° "
                           "= 下合, 到午 0° = 上合。大寒定盘的环标的是「地球走到这个方位时, "
                           "太阳在哪一宫、哪个节气」。两种盘的角度都自正下方起沿逆时针 "
                           "(= 行星实际公转方向) 递增。",
                  foreground="#7f9bb3", font=self.f_sml, wraplength=430,
                  justify="left").pack(anchor="w", pady=(3, 0))

        # ---- 显示 ----
        op = ttk.LabelFrame(R, text=" 显 示 ", padding=6)
        op.pack(fill="x", pady=(0, 5))
        self.o_orbit = tk.BooleanVar(value=True)
        self.o_name = tk.BooleanVar(value=True)
        self.o_moon = tk.BooleanVar(value=True)
        self.o_gong = tk.BooleanVar(value=True)
        self.o_grid = tk.BooleanVar(value=True)
        self.o_arc = tk.BooleanVar(value=True)
        self.o_ray = tk.BooleanVar(value=True)
        items = [("轨道线 (一整周期)", self.o_orbit), ("行星名标注", self.o_name),
                 ("月亮 (示意放大)", self.o_moon), ("十二宫 / 24 节气环", self.o_gong),
                 ("AU 网格圈", self.o_grid), ("已走过的弧", self.o_arc),
                 ("日地连线", self.o_ray)]
        for i, (txt, var) in enumerate(items):
            ttk.Checkbutton(op, text=txt, variable=var, command=self.redraw
                            ).grid(row=i // 2, column=i % 2, sticky="w")
        sr = ttk.Frame(op)
        sr.grid(row=4, column=0, columnspan=2, sticky="we", pady=(5, 0))
        ttk.Label(sr, text="侧面图 竖向放大").pack(side="left")
        self.vex = tk.DoubleVar(value=10.0)
        ttk.Scale(sr, from_=1.0, to=120.0, variable=self.vex,
                  orient="horizontal",
                  command=lambda *a: self.redraw()).pack(side="left", fill="x",
                                                         expand=True, padx=5)
        self.vex_lab = ttk.Label(sr, text="30×", width=6, foreground="#8fb3d0")
        self.vex_lab.pack(side="left")

        # ---- 缩放 ----
        zw = ttk.LabelFrame(R, text=" 缩 放 (滚轮 / 拖动平移 / 双击适配) ", padding=6)
        zw.pack(fill="x", pady=(0, 5))
        zb = ttk.Frame(zw)
        zb.pack(fill="x")
        ttk.Button(zb, text="放大 +", width=7,
                   command=lambda: self._zoom(1.4)).pack(side="left")
        ttk.Button(zb, text="缩小 −", width=7,
                   command=lambda: self._zoom(1 / 1.4)).pack(side="left", padx=3)
        ttk.Button(zb, text="适配 22 AU", width=11,
                   command=self._fit).pack(side="left")
        ttk.Button(zb, text="1 AU = 1 cm", width=11,
                   command=self._real_size).pack(side="left", padx=3)
        self.zoom_lab = ttk.Label(zw, text="", foreground="#8fb3d0",
                                  font=self.f_num)
        self.zoom_lab.pack(anchor="w", pady=(3, 0))

        # ---- 读数 ----
        rd = ttk.LabelFrame(R, text=" 此刻各星位置 ", padding=5)
        rd.pack(fill="both", expand=True)
        self.read_lab = ttk.Label(rd, text="", justify="left",
                                  font=self.app.mono_font, foreground="#d8e0e8")
        self.read_lab.pack(anchor="w")
        self._on_view()

    # ==================== 小工具 ====================
    def _f(self, var, d=0.0):
        try:
            return float(str(var.get()).strip())
        except Exception:
            return d

    def _i(self, var, d=0):
        try:
            return int(float(str(var.get()).strip()))
        except Exception:
            return d

    def tz(self):
        return self._f(self.tz_var, 8.0)

    def _on_view(self, *_):
        self.view = self.view_var.get()
        notes = {
            "true": "真实比例: 土星远日点 10.1 AU, 正好塞得进 ±11 AU。"
                    "轨道由 VSOP87 逐点采样画出, 偏心率、椭圆长短轴都是真的。",
            "equal": "等距示意: 半径只表示「第几条轨道」, 不代表距离; "
                     "行星的方位角仍是真的。",
            "side": "侧面图: 横轴 = 当时的日地连线方向 (真实比例, 全宽 22 AU), "
                    "竖轴 = 日心黄道 z。真实 z 最大也才 0.4 AU (土星), "
                    "所以竖向另给放大倍数, 括号里是真值。",
        }
        self.view_note.configure(text=notes[self.view])
        self.redraw()

    def _zoom(self, f):
        self.zoom = max(0.12, min(200.0, self.zoom * f))
        self.redraw()

    def _fit(self):
        self.zoom = 1.0
        self.pan = [0.0, 0.0]
        self.redraw()

    def _real_size(self):
        """按屏幕实测尺寸把 1 AU 定成 1 cm (即 22 AU = 22 cm)。"""
        try:
            mm_per_px = (self.winfo_screenmmwidth()
                         / float(self.winfo_screenwidth()))
        except Exception:
            mm_per_px = 0.2769
        want_px_per_au = 10.0 / mm_per_px           # 1 cm = 10 mm
        base = self._base_scale()
        if base > 0:
            self.zoom = want_px_per_au / base
        self.pan = [0.0, 0.0]
        self.redraw()

    def _drag_start(self, e):
        self._drag = (e.x, e.y, self.pan[0], self.pan[1])

    def _drag_move(self, e):
        if not self._drag:
            return
        x0, y0, p0, p1 = self._drag
        self.pan = [p0 + (e.x - x0), p1 + (e.y - y0)]
        self.redraw()

    # ==================== 时间 ====================
    def _apply_date(self):
        y, mo, d = self._i(self.tv["y"], 2026), self._i(self.tv["mo"], 1), \
            self._i(self.tv["d"], 1)
        h, mi = self._i(self.tv["h"], 0), self._i(self.tv["mi"], 0)
        try:
            loc = dt.datetime(y, max(1, min(12, mo)), max(1, min(31, d)),
                              max(0, min(23, h)), max(0, min(59, mi)))
        except ValueError:
            messagebox.showwarning("日期无效", "请检查年月日时分。")
            return
        self.jd0 = julian_day(loc - dt.timedelta(hours=self.tz()))
        self.jd = self.jd0
        self._orbit_cache.clear()
        self.playing = False
        self.play_btn.configure(text="▶ 播放")
        self.redraw()

    def _set_now(self):
        now = utcnow() + dt.timedelta(hours=self.tz())
        for k, v in (("y", now.year), ("mo", now.month), ("d", now.day),
                     ("h", now.hour), ("mi", now.minute)):
            self.tv[k].set(str(v))
        self._apply_date()

    def _rewind(self):
        self.jd = self.jd0
        self.playing = False
        self.play_btn.configure(text="▶ 播放")
        self.redraw()

    def _sync_entries(self):
        loc = jd_to_datetime(self.jd0) + dt.timedelta(hours=self.tz())
        for k, v in (("y", loc.year), ("mo", loc.month), ("d", loc.day),
                     ("h", loc.hour), ("mi", loc.minute)):
            self.tv[k].set(str(v))

    def _toggle_play(self):
        self.playing = not self.playing
        self._last_wall = _time.monotonic()
        self.play_btn.configure(text="⏸ 暂停" if self.playing else "▶ 播放")

    def _on_speed(self, *_):
        for t, v in ORB_SPEEDS:
            if t == self.spd_var.get():
                self.day_per_sec = v
                self.cust_var.set(("%g" % v))
                break

    def _apply_custom(self):
        v = self._f(self.cust_var, 1.0)
        if v <= 0:
            messagebox.showwarning("速度无效", "请填大于 0 的数 (星图日 / 真实秒)。")
            return
        self.day_per_sec = v
        self.spd_var.set(_T("自定义 %g×") % v)

    def _tick(self):
        if self.playing and not self.winfo_ismapped():
            self._last_wall = None            # 切到别的页签就别空转
        elif self.playing:
            now = _time.monotonic()
            if self._last_wall is None:
                self._last_wall = now
            dtr = max(0.0, min(0.5, now - self._last_wall))
            self._last_wall = now
            self.jd += dtr * self.day_per_sec
            if self.loop_var.get() and self.jd - self.jd0 >= ORB_PERIOD["地球"]:
                self.jd = self.jd0 + (self.jd - self.jd0) % ORB_PERIOD["地球"]
            self.redraw()
        else:
            self._last_wall = None
        self.after(40, self._tick)

    # ==================== 星历 ====================
    def _jdtt(self, jd_ut):
        return jd_ut + delta_t_seconds(jd_to_datetime(jd_ut)) / 86400.0

    def _orbit_pts(self, name):
        """一整个恒星周期的日心轨道采样 (自起始日算起)。"""
        key = (name, round(self.jd0, 5))
        if key in self._orbit_cache:
            return self._orbit_cache[key]
        per = ORB_PERIOD[name]
        n = 360
        out = []
        for i in range(n + 1):
            jd = self.jd0 + per * i / n
            vec, L, B, Rr = orb_helio_xyz(name, self._jdtt(jd))
            out.append((vec, L, B, Rr))
        self._orbit_cache[key] = out
        return out

    def _state(self):
        """当前时刻全部天体的日心黄道向量。"""
        jt = self._jdtt(self.jd)
        st = {}
        for p in ORB_PLANETS:
            vec, L, B, Rr = orb_helio_xyz(p, jt)
            st[p] = {"vec": vec, "L": L, "B": B, "R": Rr}
        st["太阳"] = {"vec": (0.0, 0.0, 0.0), "L": 0.0, "B": 0.0, "R": 0.0}
        # 月亮: 由地心视位置转黄道, 再加地球日心向量 → 月亮的日心向量
        try:
            utc = jd_to_datetime(self.jd)
            m = EPH.get("月亮", utc)
            eps = true_obliquity(jt)
            lam, bet = equ_to_ecl(m.ra, m.dec, eps)
            rm = m.dist_km / AU_KM
            gvec = _rect(lam, bet, rm)
            ev = st["地球"]["vec"]
            st["月亮"] = {"vec": tuple(a + b for a, b in zip(ev, gvec)),
                          "L": lam, "B": bet, "R": rm, "geo": True}
        except Exception:
            pass
        return st

    def _lref(self, st):
        """
        参考黄经 (图面正下方对应的日心黄经), 子 0° 恒在正下方:
          earth (预设) 日地恒定: = 此刻地球的日心黄经 —— 地球、日地虚线恒对子 0°
          term         大寒定盘: = 120° (子宫 0° = 大寒 = 日 λ300° = 地球 L120°)
        """
        return orb_lref(self.frame_var.get(), st["地球"]["L"])

    def _rel_trail(self, p):
        """
        日地恒定盘上 p 的相对轨迹 [(相对角, 日心距), …]: 自起始日起每 ORB_REL_STEP 日
        一点, 只留最近一个会合周期 (再长就绕回原处叠在一起)。按需续算、缓存。
        """
        step = ORB_REL_STEP[p]
        ent = self._rel_cache.get(p)
        if ent is None or ent["jd0"] != self.jd0:
            ent = {"jd0": self.jd0, "base": 0, "pts": []}
            self._rel_cache[p] = ent
        span = self.jd - self.jd0
        if span <= 0:
            return []
        n = int(span / step)                       # 需要第 0..n 点
        keep = int(math.ceil(ORB_SYNODIC[p] / step))
        lo = max(0, n + 1 - keep)
        if lo > ent["base"] + len(ent["pts"]) or lo < ent["base"]:
            ent["base"], ent["pts"] = lo, []       # 跳得太远 (或倒回去), 重起
        pts = ent["pts"]
        while ent["base"] + len(pts) <= n:
            j = ent["base"] + len(pts)
            pts.append(orb_rel_pos(p, self._jdtt(self.jd0 + step * j)))
        if lo - ent["base"] > keep:                # 丢掉窗口以外的旧点
            del pts[:lo - ent["base"]]
            ent["base"] = lo
        return pts[lo - ent["base"]:n + 1 - ent["base"]]

    # ==================== 画图 ====================
    def _base_scale(self):
        W = max(60, self.canvas.winfo_width())
        H = max(60, self.canvas.winfo_height())
        return min(W, H) * 0.47 / self.HALF_AU     # 像素 / AU (zoom = 1)

    def _plan_xy(self, cx, cy, s, Lref, L, R):
        a = norm360(L - Lref)
        return cx + s * R * dsin(a), cy + s * R * dcos(a)

    def redraw(self, *_):
        c = self.canvas
        c.delete("all")
        W, H = c.winfo_width(), c.winfo_height()
        if W < 60 or H < 60:
            return
        self.vex_lab.configure(text="%.0f×" % self.vex.get())
        st = self._state()
        Lref = self._lref(st)
        cx = W * 0.5 + self.pan[0]
        cy = H * 0.5 + self.pan[1]
        t1, t2 = self._head_texts(st)            # 顶上两行标题占的地方 (环上的字要让开)
        self._hdr_box = (0, 0, 10 + max(text_size(self.f_lab_b, t1)[0],
                                        text_size(self.f_sml, t2)[0]) + 8, 40)
        if self.view == "true":
            self._draw_true(c, W, H, cx, cy, st, Lref)
        elif self.view == "equal":
            self._draw_equal(c, W, H, cx, cy, st, Lref)
        else:
            self._draw_side(c, W, H, cx, cy, st, Lref)
        self._head(c, W, st, Lref)
        self._readout(st, Lref)

    # ---------- ① 实际距离 ----------
    def _draw_true(self, c, W, H, cx, cy, st, Lref):
        s = self._base_scale() * self.zoom
        self.zoom_lab.configure(
            text=_T("1 AU = %.1f px   全幅 22 AU = %.0f px   缩放 %.2f×")
                 % (s, 22 * s, self.zoom))
        if self.o_grid.get():
            self._au_grid(c, cx, cy, s, W, H)
        if self.o_gong.get():
            self._gong_ring(c, cx, cy, s * self.HALF_AU * 0.985, Lref)
        # 轨道
        if self.o_orbit.get():
            for p in ORB_PLANETS:
                pts = []
                for vec, L, B, Rr in self._orbit_pts(p):
                    x, y = self._plan_xy(cx, cy, s, Lref, L, Rr * dcos(B))
                    pts += [x, y]
                c.create_line(*pts, fill=ORB_ORBIT_COLOR[p], width=1,
                              smooth=True)
        # 已走过的弧
        if self.o_arc.get():
            self._walked_arc(c, cx, cy, s, Lref, st)
        # 日地连线 (再淡淡地延到十二辰环: 日地恒定盘上正好对准子 0°)
        if self.o_ray.get():
            ex, ey = self._plan_xy(cx, cy, s, Lref, st["地球"]["L"],
                                   st["地球"]["R"])
            c.create_line(cx, cy, ex, ey, fill="#5d7f96", dash=(4, 3))
            if self.o_gong.get():
                self._ray_to_ring(c, cx, cy, ex, ey,
                                  st["地球"]["L"] - Lref, s * self.HALF_AU * 0.985)
        # 星体 (先画完所有星体, 名字最后统一摆, 互相让开)
        rs = max(5.0, min(22.0, s * 0.22))
        self._sun(c, cx, cy, rs, label=False)
        labels = [("太阳", "#ffe07a", self.f_lab, cx, cy, rs, 225.0, -1)]  # 先试左上
        obst = [(cx - rs, cy - rs, cx + rs, cy + rs)]
        order = sorted(ORB_PLANETS, key=lambda p: -ORB_A[p])
        for p in order:
            x, y = self._plan_xy(cx, cy, s, Lref, st[p]["L"],
                                 st[p]["R"] * dcos(st[p]["B"]))
            r = ORB_DOTR[p]
            self._body(c, p, x, y, r)
            obst.append((x - r, y - r, x + r, y + r))
            labels.append(("%s %s" % (p, ORB_SYMBOL[p]), ORB_COLOR[p], self.f_lab,
                           x, y, r, norm360(st[p]["L"] - Lref), ORB_LABEL_PRI[p]))
            if p == "地球" and self.o_moon.get() and "月亮" in st:
                m = self._moon_near(c, cx, cy, s, Lref, st, x, y)
                obst.append((m[0] - 3.2, m[1] - 3.2, m[0] + 3.2, m[1] + 3.2))
                labels.append((_en("月", "Moon"), "#c9ced4", self.f_sml,
                               m[0], m[1], 3.2, m[2], 1))
        self._scalebar(c, W, H, s, "AU")
        if self.o_name.get():
            self._place_labels(c, W, H, labels, obst)

    def _ray_to_ring(self, c, cx, cy, ex, ey, a, Rg):
        """日地虚线从地球再延到十二辰环 (淡一些), 一眼看出它对准环上的哪一度。"""
        d = math.hypot(ex - cx, ey - cy)
        if Rg <= d + 4:
            return
        c.create_line(ex, ey, cx + Rg * dsin(a), cy + Rg * dcos(a),
                      fill="#3f5868", dash=(2, 5))

    def _place_labels(self, c, W, H, labels, obst):
        """
        行星名互相让开: 先试「离太阳更远的那一侧」, 不行再绕着星体转着试 8 个方位,
        距离按字的实际宽高算 (中英文同一套)。都不行就挑重叠最少的那个。
        labels: (文字, 颜色, 字体, x, y, 星体半径, 外指方位°, 优先级)
        obst  : 不许压住的框 (星体圆点、太阳)
        """
        placed = []
        hdr = (0, 0, W, 40)                       # 顶上两行标题
        top = list(obst) + [hdr]
        for it in c.find_all():                   # 已画上的字 (AU 圈、十二辰环、太阳、比例尺)
            if c.type(it) == "text":
                bb = c.bbox(it)
                if bb:
                    top.append(bb)

        def ov(a, b):
            w = min(a[2], b[2]) - max(a[0], b[0])
            h = min(a[3], b[3]) - max(a[1], b[1])
            return w * h if w > 0 and h > 0 else 0.0

        for text, col, font, x, y, r, ang, _pri in sorted(labels, key=lambda t: t[7]):
            tw = font.measure(tr(text))           # 量的是实际显示的那一种语言
            th = font.metrics("linespace")
            best = None
            for k, da in enumerate((0, 45, -45, 90, -90, 135, -135, 180)):
                a = ang + da
                dx, dy = dsin(a), dcos(a)
                ext = abs(dx) * tw / 2.0 + abs(dy) * th / 2.0
                px, py = x + dx * (r + 4 + ext), y + dy * (r + 4 + ext)
                box = (px - tw / 2.0, py - th / 2.0, px + tw / 2.0, py + th / 2.0)
                bad = sum(ov(box, o) for o in top) + sum(ov(box, o) for o in placed)
                if box[0] < 0 or box[2] > W or box[3] > H:
                    bad += tw * th * 0.5
                score = bad * 100.0 + k
                if best is None or score < best[0]:
                    best = (score, px, py, box)
                if bad == 0:
                    break
            _sc, px, py, box = best
            placed.append(box)
            c.create_text(px, py, text=text, fill=col, font=font)

    def _walked(self, p):
        """自起始日到此刻实际走过的那一段轨道采样 (直接切缓存, 不再算星历)。"""
        span = self.jd - self.jd0
        pts = self._orbit_pts(p)
        if span <= 0:
            return []
        k = int(min(1.0, span / ORB_PERIOD[p]) * (len(pts) - 1))
        return pts[:k + 1]

    def _walked_arc(self, c, cx, cy, s, Lref, cur):
        """
        自起始日到此刻, 各星走过的那一段 (加粗高亮)。
          大寒定盘: 盘不动, 就是轨道上实际走过的弧
          日地恒定: 盘跟着地球转, 画的是「相对日地」的轨迹 —— 每一点都按当时的
                    (日心黄经 − 地球日心黄经) 摆, 留最近一个会合周期; 地球自己不动, 不画
        """
        rel = self.frame_var.get() == "earth"
        for p in ORB_PLANETS:
            pts = []
            if rel:
                if p == "地球":
                    continue
                for a, rr in self._rel_trail(p):
                    pts += [cx + s * rr * dsin(a), cy + s * rr * dcos(a)]
            else:
                seg = self._walked(p)
                if len(seg) < 2:
                    continue
                for vec, L, B, Rr in seg:
                    x, y = self._plan_xy(cx, cy, s, Lref, L, Rr * dcos(B))
                    pts += [x, y]
            if not pts:
                continue
            d = cur[p]
            x, y = self._plan_xy(cx, cy, s, Lref, d["L"], d["R"] * dcos(d["B"]))
            pts += [x, y]
            if len(pts) >= 4:
                c.create_line(*pts, fill=ORB_COLOR[p], width=2, smooth=True)

    # ---------- ② 等距示意 ----------
    def _draw_equal(self, c, W, H, cx, cy, st, Lref):
        Rmax = min(W, H) * 0.42 * self.zoom
        step = Rmax / 6.5
        self.zoom_lab.configure(text=_T("等距示意图 · 轨道间距 %.0f px · 缩放 %.2f×")
                                     % (step, self.zoom))
        rad = {p: step * (i + 1.5) for i, p in enumerate(ORB_PLANETS)}
        # 外圈星尘 (仿参考图)
        self._starband(c, cx, cy, Rmax * 1.10, Rmax * 1.24)
        for p in ORB_PLANETS:
            r = rad[p]
            c.create_oval(cx - r, cy - r, cx + r, cy + r, outline="#cfd3d6",
                          width=1)
        if self.o_gong.get():
            self._gong_ring(c, cx, cy, Rmax * 1.03, Lref, faint=True)
        if self.o_ray.get():
            a = norm360(st["地球"]["L"] - Lref)
            ex, ey = cx + rad["地球"] * dsin(a), cy + rad["地球"] * dcos(a)
            c.create_line(cx, cy, ex, ey, fill="#5d7f96", dash=(4, 3))
            if self.o_gong.get():
                self._ray_to_ring(c, cx, cy, ex, ey, a, Rmax * 1.03)
        rsun = step * 0.72
        self._sun(c, cx, cy, rsun)
        obst = [(cx - rsun, cy - rsun, cx + rsun, cy + rsun)]
        names, moon = [], None
        for p in sorted(ORB_PLANETS, key=lambda q: -ORB_A[q]):
            a = norm360(st[p]["L"] - Lref)
            x, y = cx + rad[p] * dsin(a), cy + rad[p] * dcos(a)
            # 圆点随轨道间距放大, 但不许大过轨道间距 (土星连环一起算)
            rr = ORB_DOTR[p] * max(0.85, min(2.2, step / 26.0))
            rr = min(rr, step * (0.20 if p == "土星" else 0.30))
            self._body(c, p, x, y, rr)
            ext = rr * (2.05 if p == "土星" else 1.0)          # 土星连环
            obst.append((x - ext, y - ext, x + ext, y + ext))
            names.append((ORB_LABEL_PRI[p], p, rad[p], a, rr))
            if p == "地球" and self.o_moon.get() and "月亮" in st:
                da = norm360(st["月亮"]["L"] - Lref)
                off = rr + 11
                mx, my = x + off * dsin(da), y + off * dcos(da)
                self._body(c, "月亮", mx, my, 3.2)
                obst.append((mx - 3.2, my - 3.2, mx + 3.2, my + 3.2))
                moon = (mx, my, da)
        if self.o_name.get():
            placed = self._curved_names(c, cx, cy, sorted(names), obst)
            if moon:
                self._place_labels(c, W, H, [(_en("月", "Moon"), "#c9ced4", self.f_sml,
                                              moon[0], moon[1], 3.2, moon[2], 1)],
                                   obst + placed)

    def _starband(self, c, cx, cy, r0, r1):
        if self._stars is None:
            rng = _random.Random(20260907)
            self._stars = [(rng.random() * 360.0,
                            rng.random(), 0.7 + rng.random() * 0.9)
                           for _ in range(1400)]
        for a, f, sz in self._stars:
            r = r0 + (r1 - r0) * f
            x, y = cx + r * dsin(a), cy + r * dcos(a)
            c.create_oval(x - sz, y - sz, x + sz, y + sz, fill="#8d9298",
                          outline="")

    @staticmethod
    def _ov(a, b):
        w = min(a[2], b[2]) - max(a[0], b[0])
        h = min(a[3], b[3]) - max(a[1], b[1])
        return w * h if w > 0 and h > 0 else 0.0

    def _curved_names(self, c, cx, cy, items, obst):
        """
        等距示意图的行星名: 沿轨道切线摆 (仿参考图的弧形标注)。先试星体逆时针一侧,
        压到别的星、别的字就改摆顺时针一侧; 沿弧让开的距离按字的实际宽度算
        (中英文同一套)。返回已占的框, 供月亮的名字让开。
        items: (优先级, 星名, 轨道半径, 方位°, 圆点半径)
        """
        top = list(obst)
        for it in c.find_all():                   # 十二辰环上的字等
            if c.type(it) == "text":
                bb = c.bbox(it)
                if bb:
                    top.append(bb)
        placed = []
        th = self.f_lab.metrics("linespace")
        for _pri, p, r, a, rr in items:
            tw = self.f_lab.measure(tr(p))
            best = None
            for k, sg in enumerate((1.0, -1.0)):
                ext = rr * (2.05 if p == "土星" else 1.0)
                a2 = a + sg * math.degrees((ext + 5.0 + tw / 2.0) / max(1.0, r))
                x, y = cx + r * dsin(a2), cy + r * dcos(a2)
                ang = norm180(a2)                 # 切线方向; tkinter 角度逆时针为正
                if ang > 90 or ang < -90:         # 免得字倒过来
                    ang += 180
                ang = norm180(ang)
                hx = abs(tw / 2.0 * dcos(ang)) + abs(th / 2.0 * dsin(ang))
                hy = abs(tw / 2.0 * dsin(ang)) + abs(th / 2.0 * dcos(ang))
                box = (x - hx, y - hy, x + hx, y + hy)
                bad = (sum(self._ov(box, o) for o in top)
                       + sum(self._ov(box, o) for o in placed))
                if best is None or bad * 100.0 + k < best[0]:
                    best = (bad * 100.0 + k, x, y, ang, box)
                if bad == 0:
                    break
            _sc, x, y, ang, box = best
            placed.append(box)
            try:
                c.create_text(x, y, text=p, fill=ORB_COLOR[p], font=self.f_lab,
                              angle=ang)
            except Exception:
                c.create_text(x, y, text=p, fill=ORB_COLOR[p], font=self.f_lab)
        return placed

    # ---------- ③ 侧面图 ----------
    def _draw_side(self, c, W, H, cx, cy, st, Lref):
        s = self._base_scale() * self.zoom
        ve = self.vex.get()
        Le = st["地球"]["L"]
        cu, su = dcos(Le), dsin(Le)
        self.zoom_lab.configure(
            text=_T("1 AU = %.1f px (横)   全幅 22 AU = %.0f px   竖向 %.0f× 放大")
                 % (s, 22 * s, ve))

        def proj(vec):
            x, y, z = vec
            return cx + s * (x * cu + y * su), cy - s * ve * z

        # 黄道面 = 日地连线 所在的水平线
        c.create_line(0, cy, W, cy, fill="#4a5a68")
        c.create_text(6, cy - 8, text="黄道面 · 太阳—地球连线 (z = 0)",
                      anchor="w", fill="#7f9bb3", font=self.f_sml)
        c.create_text(W - 6, cy - 8, text="↑ 高过日地线", anchor="e",
                      fill="#8fd0c6", font=self.f_sml)
        c.create_text(W - 6, cy + 14, text="↓ 低过日地线", anchor="e",
                      fill="#d08f8f", font=self.f_sml)
        # 横向 AU 刻度
        if self.o_grid.get():
            k = 1
            while k * s > 26 and k <= 11:
                for sg in (-1, 1):
                    x = cx + sg * k * s
                    if 0 < x < W:
                        c.create_line(x, cy - 4, x, cy + 4, fill="#5d7f96")
                        c.create_text(x, cy + 15, text="%d" % k,
                                      fill="#6d8798", font=self.f_num)
                k += 1 if s * 1 > 60 else 2
        # 竖向 z 刻度 (整幅横线, 数字靠左边缘, 免得压住中间的星)
        for zz in (0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0):
            dy = s * ve * zz
            if 26 < dy < H * 0.55:
                for sg in (-1, 1):
                    yy = cy - sg * dy
                    c.create_line(0, yy, W, yy, fill="#333e48", dash=(2, 6))
                    c.create_text(6, yy - 7, text="z = %+.2f AU" % (sg * zz),
                                  anchor="w", fill="#5d7f96", font=self.f_num)
        # 轨道 (侧看 = 一条扁扁的斜线, 与 z=0 的两个交点就是升降交点)
        if self.o_orbit.get():
            for p in ORB_PLANETS:
                pts = []
                for vec, L, B, Rr in self._orbit_pts(p):
                    x, y = proj(vec)
                    pts += [x, y]
                c.create_line(*pts, fill=ORB_ORBIT_COLOR[p], width=1)
        if self.o_arc.get():
            for p in ORB_PLANETS:
                seg = self._walked(p)
                if len(seg) < 2:
                    continue
                pts = []
                for vec, L, B, Rr in seg:
                    x, y = proj(vec)
                    pts += [x, y]
                pts += list(proj(st[p]["vec"]))
                c.create_line(*pts, fill=ORB_COLOR[p], width=2)
        ex, ey = proj(st["地球"]["vec"])
        if self.o_ray.get():
            c.create_line(cx, cy, ex, ey, fill="#5d7f96", dash=(4, 3))
            c.create_line(ex, 0, ex, H, fill="#33454f", dash=(1, 5))
        rsun = max(5.0, min(22.0, s * 0.22))
        self._sun(c, cx, cy, rsun)
        obst = [(cx - rsun, cy - rsun, cx + rsun, cy + rsun)]
        side_lab = []
        for p in sorted(ORB_PLANETS, key=lambda q: -ORB_A[q]):
            x, y = proj(st[p]["vec"])
            self._body(c, p, x, y, ORB_DOTR[p])
            ext = ORB_DOTR[p] * (2.05 if p == "土星" else 1.0)
            obst.append((x - ext, y - ext, x + ext, y + ext))
            side_lab.append((ORB_LABEL_PRI[p], p, x, y))
            if p == "地球" and self.o_moon.get() and "月亮" in st:
                mx, my = proj(st["月亮"]["vec"])
                dx, dy = mx - x, my - y
                d = math.hypot(dx, dy)
                if d < 1e-9:
                    dx, dy, d = 1.0, 0.0, 1.0
                off = ORB_DOTR["地球"] + 11
                self._body(c, "月亮", x + dx / d * off, y + dy / d * off, 3.2)
        self._scalebar(c, W, H, s, "AU (横向真实比例)")
        if self.o_name.get():
            self._side_labels(c, W, H, sorted(side_lab), st, obst)

    def _side_labels(self, c, W, H, items, st, obst):
        """
        侧面图的标注: 缩到全幅时内行星挤成一团, 标注错开摆、拉细引线回星体。
        先试预设的错位, 压到别的星或字就换方向、再拉远; 字宽按实际显示的语言量。
        """
        top = list(obst) + [(0, 0, W, 40)]
        for it in c.find_all():                   # 刻度数字、z 标尺、文字说明
            if c.type(it) == "text":
                bb = c.bbox(it)
                if bb:
                    top.append(bb)
        placed = []
        th = self.f_sml.metrics("linespace")
        for _pri, p, x, y in items:
            text = "%s z=%+.4f" % (p, st[p]["vec"][2])
            tw = self.f_sml.measure(tr(text))
            ox0, oy0 = ORB_SIDE_LAB[p]
            best = None
            k = 0
            for f in (1.0, 1.6, 2.3):
                for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                    ox, oy = ox0 * sx * f, oy0 * sy * f
                    tx, ty = x + ox, y + oy
                    anc = "w" if ox > 20 else ("e" if ox < -20 else
                                               ("n" if oy > 0 else "s"))
                    px = tx + (3 if anc == "w" else -3 if anc == "e" else 0)
                    py = ty + (4 if anc == "n" else -4 if anc == "s" else 0)
                    if anc == "w":
                        box = (px, py - th / 2.0, px + tw, py + th / 2.0)
                    elif anc == "e":
                        box = (px - tw, py - th / 2.0, px, py + th / 2.0)
                    elif anc == "n":
                        box = (px - tw / 2.0, py, px + tw / 2.0, py + th)
                    else:
                        box = (px - tw / 2.0, py - th, px + tw / 2.0, py)
                    bad = (sum(self._ov(box, o) for o in top)
                           + sum(self._ov(box, o) for o in placed))
                    if box[0] < 0 or box[2] > W or box[1] < 0 or box[3] > H:
                        bad += tw * th
                    if best is None or bad * 100.0 + k < best[0]:
                        best = (bad * 100.0 + k, tx, ty, px, py, anc, oy, box)
                    k += 1
                    if bad == 0:
                        break
                if best[0] < 100.0:
                    break
            _sc, tx, ty, px, py, anc, oy, box = best
            placed.append(box)
            r = ORB_DOTR[p]
            c.create_line(x, y + (r if oy > 0 else -r), tx, ty,
                          fill=dim_color(ORB_COLOR[p], 0.55))
            c.create_text(px, py, text=text, anchor=anc, fill=ORB_COLOR[p],
                          font=self.f_sml)

    # ---------- 公用绘制 ----------
    def _sun(self, c, cx, cy, r, label=True):
        r = max(6.0, min(90.0, r))
        n = max(6, int(r * 0.7))                 # 一圈渐隐的光晕 (向底色过渡)
        for k in range(n):
            f = (k + 1) / float(n)
            rr = r * (1.0 + 0.45 * f)
            c.create_oval(cx - rr, cy - rr, cx + rr, cy + rr,
                          outline=mix_color(self.BG, "#ffe07a",
                                            0.42 * (1.0 - f) ** 1.6))
        c.create_oval(cx - r, cy - r, cx + r, cy + r, fill="#ffe07a",
                      outline="#ffd257")
        if label and self.o_name.get():
            c.create_text(cx - r - 5, cy - r - 5, text="太阳", anchor="se",
                          fill="#ffe07a", font=self.f_lab)

    def _body(self, c, p, x, y, r):
        col = ORB_COLOR[p]
        if p == "土星":
            self._ring(c, x, y, r * 2.05, r * 0.62, "#c9b98a", back=True)
            c.create_oval(x - r, y - r, x + r, y + r, fill=col, outline="#efe6bd")
            self._ring(c, x, y, r * 2.05, r * 0.62, "#e3d6a8", back=False)
            return
        c.create_oval(x - r, y - r, x + r, y + r, fill=col,
                      outline=dim_color(col, 1.35))
        if p == "木星" and r > 5:
            for f in (-0.55, -0.22, 0.12, 0.45):
                dy = f * r
                hw = math.sqrt(max(0.0, r * r - dy * dy)) * 0.95
                c.create_line(x - hw, y + dy, x + hw, y + dy,
                              fill="#f7cdb4" if f < 0 else "#d96f52",
                              width=max(1, int(r * 0.28)))
        elif p == "地球" and r > 4:
            c.create_oval(x - r * 0.55, y - r * 0.45, x + r * 0.05,
                          y + r * 0.25, fill="#5fbf7a", outline="")
            c.create_oval(x + r * 0.12, y - r * 0.05, x + r * 0.62,
                          y + r * 0.62, fill="#5fbf7a", outline="")
        elif p == "火星" and r > 4:
            c.create_oval(x - r * 0.5, y - r * 0.75, x + r * 0.1, y - r * 0.25,
                          fill="#f3b49a", outline="")

    def _ring(self, c, x, y, ra, rb, col, back=True, tilt=-18.0):
        """土星环: 用采样折线画一个倾斜的椭圆, 分前后两半。"""
        pts = []
        a0, a1 = (180, 360) if back else (0, 180)
        for i in range(a0, a1 + 1, 6):
            px, py = ra * dcos(i), rb * dsin(i)
            rx = px * dcos(tilt) - py * dsin(tilt)
            ry = px * dsin(tilt) + py * dcos(tilt)
            pts += [x + rx, y + ry]
        if len(pts) >= 4:
            c.create_line(*pts, fill=col, width=max(1, int(rb * 0.55)),
                          smooth=True)

    def _moon_near(self, c, cx, cy, s, Lref, st, ex, ey):
        """月亮: 真实距离 0.0026 AU 看不见, 故按真方向、固定像素距离示意画出。"""
        # 以地球为原点的方向 = 月亮的地心黄经方向
        a = norm360(st["月亮"]["L"] - Lref)
        off = ORB_DOTR["地球"] + 12
        mx, my = ex + off * dsin(a), ey + off * dcos(a)
        c.create_line(ex, ey, mx, my, fill="#5a6874")
        self._body(c, "月亮", mx, my, 3.2)
        return mx, my, a                          # 名字由 _place_labels 统一摆

    def _au_grid(self, c, cx, cy, s, W, H):
        for au in (1, 2, 3, 5, 10, 11):
            r = au * s
            if r < 8 or r > max(W, H) * 1.6:
                continue
            col = "#3d4a55" if au != 11 else "#55707f"
            c.create_oval(cx - r, cy - r, cx + r, cy + r, outline=col,
                          dash=() if au == 11 else (2, 4))
            c.create_text(cx + r * 0.7071, cy - r * 0.7071,
                          text="%d AU" % au, fill="#5d7080", font=self.f_num)
        c.create_line(cx - 9, cy, cx + 9, cy, fill="#55707f")
        c.create_line(cx, cy - 9, cx, cy + 9, fill="#55707f")

    def _gong_ring(self, c, cx, cy, R, Lref, faint=False):
        """
        十二辰环, 子 0° 恒在正下方。
          大寒定盘: 标「地球走到这个方位时, 太阳在哪一宫、哪个节气」(子·大寒 在正下方)
          日地恒定: 以日地连线为子 0°, 每 30° 一宫 (子 0°、亥 0°、戌 0° …), 环不转;
                    环上角度 = 该星日心黄经 − 地球日心黄经
        """
        if R < 40:
            return
        col = "#4f6272" if faint else "#5f7a8c"
        c.create_oval(cx - R, cy - R, cx + R, cy + R, outline=col)
        Ri = R * 0.965
        if self.frame_var.get() == "earth":
            for k in range(24):
                a = 15.0 * k
                major = (k % 2 == 0)
                zi = (k == 0)
                r0 = Ri * (0.94 if zi else (0.965 if major else 0.982))
                c.create_line(cx + r0 * dsin(a), cy + r0 * dcos(a),
                              cx + R * dsin(a), cy + R * dcos(a),
                              fill="#e8c56a" if zi else
                              ("#7f9bb3" if major else "#4f6272"),
                              width=2 if zi else 1)
                if major:
                    self._ring_label(c, cx, cy, R, a, "%s 0°" % ORB_GONG[k // 2],
                                     "#e8c56a" if zi else "#93aec4",
                                     self.f_lab_b if zi else self.f_sml)
            return
        for name, lam in SOLAR_TERMS:                 # lam = 太阳视黄经
            L = norm360(lam + 180.0)                  # → 地球日心黄经
            a = norm360(L - Lref)
            major = (lam % 30 == 0)
            r0 = Ri * (0.965 if major else 0.982)
            c.create_line(cx + r0 * dsin(a), cy + r0 * dcos(a),
                          cx + R * dsin(a), cy + R * dcos(a),
                          fill="#7f9bb3" if major else "#4f6272")
            if major:
                g, _d, _t = orb_gong_of(lam + 0.001)
                self._ring_label(c, cx, cy, R, a, "%s·%s" % (g, name), "#93aec4",
                                 self.f_sml)

    def _ring_label(self, c, cx, cy, R, a, text, col, font):
        """环外标字; 若会压到顶上两行标题, 就改标在环内侧。"""
        w, h = text_size(font, text)
        rt = R * 1.032
        x, y = cx + rt * dsin(a), cy + rt * dcos(a)
        hdr = self._hdr_box if getattr(self, "_hdr_box", None) else (0, 0, 0, 0)
        if box_ov(anchor_box(x, y, "center", w, h), hdr) > 0:
            rt = R * 0.965 - h * 0.9
            x, y = cx + rt * dsin(a), cy + rt * dcos(a)
        c.create_text(x, y, text=text, fill=col, font=font)

    def _scalebar(self, c, W, H, s, unit):
        au = 1.0
        for cand in (0.5, 1, 2, 5, 10):
            if cand * s <= W * 0.28:
                au = cand
        L = au * s
        x0, y0 = 18, H - 22
        c.create_line(x0, y0, x0 + L, y0, fill="#93aec4", width=2)
        for xx in (x0, x0 + L):
            c.create_line(xx, y0 - 5, xx, y0 + 5, fill="#93aec4")
        c.create_text(x0 + L / 2, y0 - 10, text="%g %s" % (au, unit),
                      fill="#93aec4", font=self.f_sml)

    def _head_texts(self, st):
        loc = jd_to_datetime(self.jd) + dt.timedelta(hours=self.tz())
        span = self.jd - self.jd0
        txt = (_T("%04d-%02d-%02d %02d:%02d  (UTC%+g)    自起始日 %+.3f 日 "
               "(%.3f 地球年)") % (loc.year, loc.month, loc.day, loc.hour,
                                loc.minute, self.tz(), span,
                                span / ORB_PERIOD["地球"]))
        Le = st["地球"]["L"]
        g, d, t = orb_gong_of(norm360(Le + 180.0))
        if self.view == "side":
            info = (_T("侧面图 · 横轴 = 此刻日地连线 (地球在右) · 此刻太阳在 %s宫 %.2f° (%s后)")
                    % (g, d, t))
        elif self.frame_var.get() == "earth":
            info = (_T("日地恒定 · 地球恒在正下方 = 子 0° (地球日心黄经 %.2f°) · "
                       "此刻太阳在 %s宫 %.2f° (%s后)") % (az_fmt(Le, 2), g, d, t))
        else:
            info = (_T("大寒定盘 · 正下方 = 子宫 0° = 大寒 (地球日心黄经 120°) · "
                       "地球在逆时针 %.2f° · 此刻太阳在 %s宫 %.2f° (%s后)")
                    % (az_fmt(Le - 120.0, 2), g, d, t))
        return txt, info

    def _head(self, c, W, st, Lref):
        txt, info = self._head_texts(st)
        span = self.jd - self.jd0
        c.create_text(10, 12, text=txt, anchor="w", fill="#e8c56a",
                      font=self.f_lab_b)
        c.create_text(10, 30, anchor="w", fill="#8fb3d0", font=self.f_sml, text=info)
        self.clock_lab.configure(
            text=_T("真实 1 秒 = 星图 %g 日   |   地球一圈需 %.1f 真实秒\n"
                 "已走 %.3f 日 = %.4f 地球年") % (
                     self.day_per_sec, ORB_PERIOD["地球"] / self.day_per_sec,
                     span, span / ORB_PERIOD["地球"]))
        self.date_lab.configure(
            text=_T("起始日 UT %s") % jd_to_datetime(self.jd0).strftime(
                "%Y-%m-%d %H:%M"))

    def _readout(self, st, Lref):
        """
        右栏读数: 拆成「日心」「地心」两张窄表, 右栏宽度放得下, 不必横向卷动。
        英文模式下星名、宫名先译好再按最长者补齐, 各栏才对得齐。
        """
        ev = st["地球"]["vec"]
        en = (LANG == "en")
        seq = ["太阳", "月亮", "水星", "金星", "地球", "火星", "木星", "土星"]
        nm = {q: (tr(q) if en else q) for q in seq}
        pad = max(len(nm[q]) for q in seq) if en else 4
        if en:
            ha = "%-*s %9s %8s %8s  %8s %8s" % (pad, "Body", "Hel.lon", "Screen",
                                                "r AU", "Hel.lat", "z AU")
            hb = "%-*s %9s %-12s %8s" % (pad, "Body", "Geo.lon", "Palace", "Dist AU")
        else:
            ha = "天体  日心黄经  屏幕角  日心距AU   黄纬     z AU"
            hb = "天体  地心黄经  宫 度       距地AU"
        A = [ha, "-" * (len(ha) if en else 53)]
        B = [hb, "-" * (len(hb) if en else 35)]
        for p in seq:
            if p not in st:
                continue
            d = st[p]
            vec = d["vec"]
            dx, dy, dz = (vec[0] - ev[0], vec[1] - ev[1], vec[2] - ev[2])
            dist = math.sqrt(dx * dx + dy * dy + dz * dz)
            # 一律由日心向量现算, 免得月亮那一行混进地心量
            Rh = math.sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)
            Lh = norm360(math.degrees(math.atan2(vec[1], vec[0])))
            Bh = math.degrees(math.asin(vec[2] / Rh)) if Rh > 1e-12 else 0.0
            if p == "太阳":
                A.append("%-*s %9s %8s %8.5f  %8s %8.5f"
                         % (pad, nm[p], "——", "——", 0.0, "——", 0.0))
            else:
                A.append("%-*s %8.3f° %7.2f° %8.5f  %+7.4f° %+8.5f"
                         % (pad, nm[p], Lh, az_fmt(Lh - Lref, 2), Rh, Bh, vec[2]))
            if p == "地球":
                B.append("%-*s  %s" % (pad, nm[p], _en("——— 观测点 ———",
                                                       "——— observer ———")))
                continue
            glam = norm360(math.degrees(math.atan2(dy, dx)))
            g, gd, _t = orb_gong_of(glam)
            if en:
                B.append("%-*s %8.3f° %-12s %8.5f"
                         % (pad, nm[p], glam, "%s %06.3f°" % (ORB_GONG_EN[g], gd), dist))
            else:
                B.append("%-4s %8.3f° %s%06.3f° %8.5f" % (p, glam, g, gd, dist))
        lines = A + [""] + B
        g, gd, t = orb_gong_of(norm360(st["地球"]["L"] + 180.0))
        lines.append("")
        lines.append(_T("太阳视黄经 %.3f° → %s宫 %.3f°  (本宫自「%s」起)")
                     % (az_fmt(st["地球"]["L"] + 180.0, 3), g, gd, t))
        lines.append("屏幕角: 自图面正下方起, 逆时针。 z > 0 = 高过日地线"
                     "(黄道面), z < 0 = 低过。")
        if self.frame_var.get() == "earth":
            lines.append("日地恒定: 屏幕角 = 日心黄经 − 地球日心黄经; "
                         "0° = 冲 / 下合, 180° = 合 / 上合。")
        lines.append("宫度按 我定的 子宫 0° = 太阳黄经 300° = 大寒 = 水瓶 0°,"
                     " 十二辰 子亥戌酉申未午巳辰卯寅丑。")
        self.read_lab.configure(text="\n".join(lines))


class App(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding=4)
        self.root = root
        self.ui_font = _pick_font(root, CJK_FONTS, 9)
        self.ui_font_b = _pick_font(root, CJK_FONTS, 10, bold=True)
        self.mono_font = _pick_font(root, MONO_FONTS, 9)
        self.mono_font_b = _pick_font(root, MONO_FONTS, 9, bold=True)
        self.big_font = _pick_font(root, MONO_FONTS, 16, bold=True)
        self.dir_font = _pick_font(root, CJK_FONTS, 13, bold=True)
        self.tip_font = _pick_font(root, CJK_FONTS, 10)
        self.pack(fill="both", expand=True)
        self._style()
        self._build()

    def _style(self):
        st = ttk.Style()
        try:
            st.theme_use("clam")
        except tk.TclError:
            pass
        bg, fg = "#161c22", "#d8e0e8"
        st.configure(".", background=bg, foreground=fg, font=self.ui_font)
        st.configure("TFrame", background=bg)
        st.configure("TLabelframe", background=bg, foreground="#8fb3d0",
                     bordercolor="#2c3742")
        st.configure("TLabelframe.Label", background=bg, foreground="#8fb3d0",
                     font=self.ui_font_b)
        st.configure("TLabel", background=bg, foreground=fg)
        st.configure("TCheckbutton", background=bg, foreground=fg)
        st.configure("TRadiobutton", background=bg, foreground=fg)
        st.configure("TButton", background="#243040", foreground=fg,
                     bordercolor="#33414d", focuscolor=bg)
        st.map("TButton", background=[("active", "#31445c")])
        st.configure("TNotebook", background=bg, bordercolor="#2c3742")
        st.configure("TNotebook.Tab", background="#1d252d", foreground="#9fb6c9",
                     padding=(18, 7), font=self.ui_font_b)
        st.map("TNotebook.Tab", background=[("selected", "#2b3b4d")],
               foreground=[("selected", "#eaf2f8")])
        st.configure("Treeview", background="#0d1117", fieldbackground="#0d1117",
                     foreground=fg, font=self.mono_font, bordercolor="#2c3742")
        st.configure("Treeview.Heading", background="#243040", foreground="#9fb6c9",
                     font=self.ui_font)
        st.configure("TEntry", fieldbackground="#0d1117", foreground=fg,
                     insertcolor=fg, bordercolor="#33414d")
        st.configure("TSpinbox", fieldbackground="#0d1117", foreground=fg,
                     insertcolor=fg, arrowcolor=fg)
        st.configure("TCombobox", fieldbackground="#0d1117", foreground=fg,
                     background="#243040", arrowcolor=fg,
                     selectbackground="#0d1117", selectforeground=fg)
        st.map("TCombobox",
               fieldbackground=[("readonly", "#0d1117"), ("disabled", "#161c22")],
               foreground=[("readonly", fg), ("disabled", "#6b7a88")],
               selectbackground=[("readonly", "#0d1117")],
               selectforeground=[("readonly", fg)],
               background=[("readonly", "#243040"), ("active", "#31445c")])
        st.map("TEntry", fieldbackground=[("disabled", "#161c22")],
               foreground=[("disabled", "#6b7a88")])
        st.configure("TScale", background=bg, troughcolor="#0d1117")
        st.configure("Vertical.TScrollbar", background="#243040",
                     troughcolor="#0d1117", arrowcolor=fg, bordercolor="#2c3742")
        # 下拉列表 (非 ttk 部件, 只能用 option database)
        self.root.option_add("*TCombobox*Listbox.background", "#0d1117")
        self.root.option_add("*TCombobox*Listbox.foreground", fg)
        self.root.option_add("*TCombobox*Listbox.selectBackground", "#31445c")
        self.root.option_add("*TCombobox*Listbox.selectForeground", "#ffffff")
        self.root.option_add("*TCombobox*Listbox.font", self.ui_font)
        self.root.configure(bg=bg)

    def _build(self):
        bar = ttk.Frame(self)
        bar.pack(fill="x", pady=(0, 4))
        ttk.Label(bar, text="日晷 · 六分仪 · 星空月相 · 太阳视运动 · 土圭 · 日月食 · 轨道",
                  font=self.ui_font_b,
                  foreground="#e8c56a").pack(side="left")
        # ---- 界面语言 (居中): 预设中英参杂; 切到 English 即整个界面重建为全英文 ----
        #      先于右侧的星历状态栏打包, 窗口窄时被截短的是状态栏而不是它
        lf = ttk.Frame(bar)
        lf.pack(side="left", expand=True)
        ttk.Label(lf, text="界面语言 Language:", foreground="#8fb3d0").pack(side="left")
        self.lang_var = tk.StringVar(value=LANG)
        for txt, val in (("中英文 (预设)", "zh"), ("English", "en")):
            ttk.Radiobutton(lf, text=txt, value=val, variable=self.lang_var,
                            command=self._set_lang).pack(side="left", padx=(6, 0))
        self.eph_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(bar, text="使用 Skyfield/JPL 高精度星历",
                        variable=self.eph_var,
                        command=self._toggle_eph).pack(side="right")
        self.status = ttk.Label(bar, text=EPH.status, foreground="#7f9bb3")
        self.status.pack(side="right", padx=10)
        self._status_full = EPH.status
        self._tip = None
        bar.bind("<Configure>", self._fit_status, add="+")
        self.status.bind("<Enter>", self._status_tip_show)
        self.status.bind("<Leave>", self._status_tip_hide)
        # 预设就用 JPL 星历: 本机已有 de421.bsp 就直接启用 (不联网)
        ok_sf, msg_sf = EPH.try_skyfield(allow_download=False)
        self.eph_var.set(bool(ok_sf))
        self._set_status(EPH.status if ok_sf else (EPH.status + " · " + msg_sf))
        self.after(300, self._fit_status)

        nb = ttk.Notebook(self)
        nb.pack(fill="both", expand=True)
        self.nb = nb
        self.sundial = SundialTab(nb, self)
        self.sextant = SextantTab(nb, self)
        self.sky = SkyTab(nb, self)
        self.track = SunTrackTab(nb, self)
        self.gui = GuiBiaoTab(nb, self)
        self.ecl = EclipseTab(nb, self)
        self.orb = OrbitTab(nb, self)
        nb.add(self.sundial, text="  日 晷  Sundial  ")
        nb.add(self.sextant, text="  六分仪  Sextant  ")
        nb.add(self.sky, text="  星空 · 月相  Sky  ")
        nb.add(self.track, text="  太阳视运动 · 24节气  Sun Track  ")
        nb.add(self.gui, text="  土 圭 · 圭表  Gnomon  ")
        nb.add(self.ecl, text="  日食 · 月食  Eclipse  ")
        nb.add(self.orb, text="  轨 道  Orbits  ")

    def _set_lang(self):
        """切换界面语言: 记下当前页签, 停掉各页的定时器, 整个界面按新语言重建。"""
        global LANG
        new = self.lang_var.get()
        if new == LANG:
            return
        try:
            cur = self.nb.index(self.nb.select())
        except Exception:
            cur = 0
        if new == "en":
            _install_i18n()
        root = self.root
        for job in root.tk.splitlist(root.tk.call("after", "info")):
            try:                         # 只取消排程; 命令留给 destroy() 去删
                root.tk.call("after", "cancel", job)
            except Exception:
                pass
        LANG = new
        _TR_CACHE.clear()
        _EN_REV.clear()
        self.destroy()
        app = App(root)
        try:
            app.nb.select(cur)
        except Exception:
            pass
        root.title(APP_TITLE)               # 标题经钩子按当前语言显示

    def _toggle_eph(self):
        if self.eph_var.get():
            if not messagebox.askyesno(
                    "启用 JPL 星历?",
                    "将尝试载入 skyfield 与 de421.bsp。\n"
                    "若本机尚无该星历文件, skyfield 会从网上下载约 17 MB,\n"
                    "下载期间界面会暂时无响应。是否继续?\n\n"
                    "(内置算法已达 太阳<0.4″ 月亮<0.2″ 金星<3″, 通常无需切换)"):
                self.eph_var.set(False)
                return
            ok, msg = EPH.try_skyfield()
            if not ok:
                self.eph_var.set(False)
                messagebox.showwarning(
                    "无法启用高精度星历",
                    _T("%s\n\n将继续使用内置算法。\n"
                    "内置算法与 IAU SOFA/ERFA 比对的视位置误差:\n"
                    "  太阳 < 0.4″   月亮 < 0.2″   金星 < 3″\n"
                    "对六分仪(读数分辨率 0.1′ = 6″)已绰绰有余。") % msg)
            else:
                messagebox.showinfo("星历", msg)
        else:
            EPH.disable_skyfield()
        self._set_status(EPH.status)

    # ---- 顶栏星历状态: 放不下就中间省略 (留头尾, 尾巴常是文件名), 鼠标移上去看全文 ----
    def _set_status(self, text):
        self._status_full = text
        self._fit_status()

    def _fit_status(self, _e=None):
        full = tr(self._status_full)
        bar = self.status.master
        try:
            bw = bar.winfo_width()
            used = sum(ch.winfo_reqwidth() for ch in bar.winfo_children()
                       if ch is not self.status)
        except Exception:
            return
        avail = bw - used - 40
        f = self.ui_font
        shown = full
        if bw > 1 and avail < 80 and f.measure(full) > avail:
            shown = "ⓘ"                      # 实在没地方: 只留个记号, 鼠标移上去看全文
        elif bw > 1 and f.measure(full) > avail:
            tail = full[-min(len(full) // 3, 26):]
            head = full[:len(full) - len(tail)]
            while head and f.measure(head + "…" + tail) > avail:
                head = head[:-1]
            shown = (head.rstrip() + "…" + tail) if head else ("…" + tail)
        self._status_shown = shown
        if self.status.cget("text") != shown:
            self.status.configure(text=shown)

    def _status_tip_show(self, _e=None):
        full = tr(self._status_full)
        if getattr(self, "_status_shown", full) == full or self._tip is not None:
            return
        tw = tk.Toplevel(self)
        tw.wm_overrideredirect(True)
        tk.Label(tw, text=full, bg="#243040", fg="#d8e0e8", font=self.ui_font,
                 padx=6, pady=3, justify="left").pack()
        tw.update_idletasks()
        x = min(self.status.winfo_rootx(),
                self.winfo_screenwidth() - tw.winfo_reqwidth() - 4)
        y = self.status.winfo_rooty() + self.status.winfo_height() + 2
        tw.wm_geometry("+%d+%d" % (max(0, x), y))
        self._tip = tw

    def _status_tip_hide(self, _e=None):
        if self._tip is not None:
            try:
                self._tip.destroy()
            except Exception:
                pass
            self._tip = None


# ===========================================================================
#  自检 (python sundial_sextant.py --selftest)
# ===========================================================================
def selftest():
    import random
    ok_all = True

    def report(name, ok, detail):
        nonlocal ok_all
        ok_all = ok_all and ok
        print("  [%s] %-34s %s" % ("通过" if ok else "失败", name, detail))

    print("=" * 74)
    print("日晷 / 六分仪 模拟器 —— 数值自检")
    print("星历: %s" % EPH.status)
    print("=" * 74)

    # 1. 六分仪正演/反演闭合
    print("\n1) 六分仪改正链闭合 (Hs→Ho 应还原地心真高度)")
    worst = 0.0
    for body in BODIES:
        for limb in ["下边缘", "上边缘", "中心"]:
            for hh in range(0, 24, 3):
                utc = dt.datetime(2026, 8, 30, hh, 20)
                pos = EPH.get(body, utc)
                sc = required_reading(pos, 3.139, 101.6869, utc, limb,
                                      2.5, -1.2, 1008.0, 29.0)
                if sc["topo"]["alt_app"] < 5:
                    continue
                ho, _ = reduce_sight(pos, sc["hs"], limb, 2.5, -1.2, 1008.0, 29.0)
                worst = max(worst, abs(ho - sc["topo"]["alt_geo"]) * 3600.0)
    report("改正链闭合", worst < 0.01, "最大残差 %.6f″" % worst)

    # 2. 日晷时线 vs 经典公式
    print("\n2) 日晷时线几何")
    worst = 0.0
    for phi in (3.139, 51.5, -33.9, 23.44, 70.0, -5.0):
        for H in range(-165, 180, 15):
            d = style_shadow_on_plane(phi, H, (0, 0, 1.0), (1.0, 0, 0), (0, 1.0, 0))
            th = math.degrees(math.atan2(d[0], d[1]))
            ref = math.degrees(math.atan2(dsin(phi) * dsin(H), dcos(H)))
            if phi < 0:
                ref = norm180(180 - math.degrees(
                    math.atan2(dsin(-phi) * dsin(H), dcos(H))))
            worst = max(worst, abs(norm180(th - ref)))
    report("水平晷 tanθ=sinφ·tanH", worst < 1e-9, "最大偏差 %.3e°" % worst)

    # 3. 均时差极值 (公认: 约 −14.2 分(2月中) / +16.4 分(11月初))
    print("\n3) 均时差年内极值")
    eots = []
    for day in range(0, 365, 1):
        utc = dt.datetime(2026, 1, 1) + dt.timedelta(days=day)
        sun = EPH.get("太阳", utc)
        eots.append((norm180((sun.gha + 180.0) - 0.0) * 4.0, utc))
    lo, hi = min(eots), max(eots)
    ok = (-14.6 < lo[0] < -13.8) and (16.0 < hi[0] < 16.8)
    report("EoT 极值", ok, "最小 %+.2f 分 (%s), 最大 %+.2f 分 (%s)"
           % (lo[0], lo[1].strftime("%m-%d"), hi[0], hi[1].strftime("%m-%d")))

    # 4. 完美观测定位闭合
    print("\n4) 截距法定位闭合 (无误差观测, DR 偏离 1.5°)")
    cases = [(3.139, 101.6869, dt.datetime(2026, 8, 30, 11, 10)),
             (51.4779, 0.0, dt.datetime(2026, 3, 21, 6, 30)),
             (-33.8688, 151.2093, dt.datetime(2026, 12, 21, 19, 0)),
             (35.0, -40.0, dt.datetime(2027, 7, 4, 2, 0)),
             (-5.0, -160.0, dt.datetime(2026, 11, 2, 20, 0))]
    worst = 0.0
    for tlat, tlon, when in cases:
        cand = []
        offs = [0.0] + [s * k * 0.5 for k in range(1, 19) for s in (1, -1)]
        for off in offs:
            t = when + dt.timedelta(minutes=int(off * 60))
            for b in BODIES:
                pos = EPH.get(b, t)
                alt, az = altaz_from_hadec(norm360(pos.gha + tlon), pos.dec, tlat)
                if alt >= 12:
                    cand.append((abs(off), t, b, alt, az))
        cand.sort(key=lambda x: x[0])
        ch = []
        for c in cand:
            if any(abs(norm180(c[4] - o[4])) < 30 for o in ch):
                continue
            if any(o[2] == c[2] and abs((c[1] - o[1]).total_seconds()) < 3600
                   for o in ch):
                continue
            ch.append(c)
            if len(ch) >= 3:
                break
        obs = []
        for _, t, b, alt, az in ch:
            pos = EPH.get(b, t)
            limb = "下边缘" if b != "金星" else "中心"
            sc = required_reading(pos, tlat, tlon, t, limb, 2.5, -1.2, 1008, 29)
            ho, _ = reduce_sight(pos, sc["hs"], limb, 2.5, -1.2, 1008, 29)
            obs.append({"utc": t, "body": b, "hs": sc["hs"], "ho": ho,
                        "pos": pos, "limb": limb})
        flat, flon, info = compute_fix(obs, tlat + 1.5, tlon - 1.5)
        dn = (flat - tlat) * 60.0
        de = norm180(flon - tlon) * 60.0 * dcos(tlat)
        err = math.hypot(dn, de) * 1852.0
        worst = max(worst, err)
        print("     φ=%+8.3f λ=%+9.3f  %d 次观测 -> 误差 %.3f m"
              % (tlat, tlon, len(obs), err))
    report("定位闭合", worst < 1.0, "最大误差 %.3f 米" % worst)

    # 5. 含随机误差的散布
    print("\n5) 含 σ=0.3′ 随机观测误差 (吉隆坡, 200 次)")
    random.seed(20260830)
    errs = []
    tlat, tlon = 3.139, 101.6869
    base = dt.datetime(2026, 8, 30, 11, 10)
    triple = []
    for off, b in ((0, "金星"), (-2.5, "金星"), (3.0, "月亮")):
        t = base + dt.timedelta(minutes=int(off * 60))
        triple.append((t, b))
    for _ in range(200):
        obs = []
        for t, b in triple:
            pos = EPH.get(b, t)
            limb = "下边缘" if b == "月亮" else "中心"
            sc = required_reading(pos, tlat, tlon, t, limb, 2.5, 0.0, 1010, 28)
            hs = sc["hs"] + random.gauss(0, 0.3) / 60.0
            ho, _ = reduce_sight(pos, hs, limb, 2.5, 0.0, 1010, 28)
            obs.append({"utc": t, "body": b, "hs": hs, "ho": ho,
                        "pos": pos, "limb": limb})
        flat, flon, info = compute_fix(obs, tlat + 1.5, tlon - 1.5)
        errs.append(math.hypot((flat - tlat) * 60.0,
                               norm180(flon - tlon) * 60.0 * dcos(tlat)))
    errs.sort()
    report("误差传播", errs[len(errs) // 2] < 2.0,
           "中位 %.2f nm, 90%% %.2f nm, 最大 %.2f nm"
           % (errs[100], errs[180], errs[-1]))

    # 6. 日出日落 (吉隆坡)
    print("\n6) 吉隆坡日出/中天/日落 (UTC+8)")
    for d in (dt.date(2026, 3, 21), dt.date(2026, 6, 21), dt.date(2026, 12, 21)):
        r, n, s, p = solar_events(d, 3.139, 101.6869, 8.0)
        print("     %s  日出 %s  中天 %s  日落 %s" % (d, fmt_hm(r), fmt_hm(n), fmt_hm(s)))

    # 7. 朔弦望求解
    print("\n7) 朔弦望时刻 (求解视黄经差 = 0/90/180/270)")
    t = dt.datetime(2026, 1, 5)
    lens = []
    worst_e = 0.0
    worst_k = 0.0
    for _ in range(13):
        lun = lunation(t)
        if not lun:
            break
        for key, tgt in (("new0", 0.0), ("first", 90.0), ("full", 180.0),
                         ("last", 270.0)):
            worst_e = max(worst_e, abs(norm180(elongation_deg(lun[key]) - tgt)))
        lens.append(lun["length"])
        t = lun["new1"] + dt.timedelta(days=2)
    report("相位时刻求根", worst_e < 1e-4, "视黄经差残差 < %.2e°" % worst_e)
    report("朔望月长度", 29.2 < min(lens) and max(lens) < 29.9,
           "最短 %.4f 最长 %.4f 平均 %.4f 日 (理论平均 29.530589)"
           % (min(lens), max(lens), sum(lens) / len(lens)))

    # 8. 月相几何
    print("\n8) 月相几何 (被照亮比例 k 与视黄经差的一致性)")
    for i in range(0, 30):
        utc = dt.datetime(2026, 8, 13, 6, 0) + dt.timedelta(days=i)
        info = moon_phase_info(utc)
        k_approx = (1 - dcos(info["elong"])) / 2.0
        worst_k = max(worst_k, abs(info["k"] - k_approx))
    report("k 与 elongation 自洽", worst_k < 0.02,
           "最大差 %.4f (月亮黄纬与相位角几何造成, 属正常)" % worst_k)

    # 9b. 24 节气与日轨插值
    print("\n9) 24 节气时刻 / 日轨插值 / 时制换算")
    worst = 0.0
    for name, lam in SOLAR_TERMS:
        t = solar_term_utc(2026, lam)
        worst = max(worst, abs(norm180(sun_apparent_lambda(t) - lam)))
    report("节气求根 (视黄经)", worst < 1e-6, "最大残差 %.2e°" % worst)
    for y, mth, dd, nm in ((2026, 3, 20, "春分"), (2026, 6, 21, "夏至"),
                           (2026, 12, 22, "冬至")):
        tt = solar_term_utc(y, dict(SOLAR_TERMS)[nm]) + dt.timedelta(hours=8)
        print("     %s %s (北京时)" % (nm, tt.strftime("%Y-%m-%d %H:%M:%S")))
    wd = wg = 0.0
    for d in (dt.date(2026, 3, 20), dt.date(2026, 6, 21), dt.date(2026, 12, 22)):
        t0 = dt.datetime(d.year, d.month, d.day) - dt.timedelta(hours=8)
        ds = DaySun(t0)
        for i in range(0, 241):
            x = i * 0.1
            pp = EPH.get("太阳", t0 + dt.timedelta(seconds=x * 3600))
            wd = max(wd, abs(pp.dec - ds.dec_at(x)))
            wg = max(wg, abs(norm180(pp.gha - ds.gha_at(x))))
    report("日轨插值", wd < 1e-3 and wg < 1e-3,
           "赤纬 %.6f°  时角 %.6f°" % (wd, wg))
    # 郑州 春分: 正午高度 应为 90−φ+δ
    lat, lon, tz = 34.7466, 113.6254, 8.0
    d = dt.date(2026, 3, 20)
    ds = DaySun(dt.datetime(d.year, d.month, d.day) - dt.timedelta(hours=tz))
    a, b = 11.0, 14.0
    for _ in range(60):
        mmid = (a + b) / 2
        if ds.hour_angle(mmid, lon) < 0:
            a = mmid
        else:
            b = mmid
    xn = (a + b) / 2
    alt, az = ds.altaz(xn, lat, lon)
    ref = 90.0 - lat + ds.dec_at(xn)
    report("郑州春分正午高度", abs(alt - ref) < 1e-6,
           "%.4f° (理论 90−φ+δ = %.4f°)" % (alt, ref))
    report("中天即真太阳时 12:00", abs(ds.tst(xn, lon) - 12.0) < 1e-6,
           "真太阳时 %s" % _hms(ds.tst(xn, lon)))

    # 10. 三维相机
    print("\n10) 三维相机与投影")
    cam = Camera3D(az=137.0, el=31.0, dist=6.0)
    vaz, vel = cam.look_dir()
    ok = abs(norm180(vaz - (137.0 + 180.0))) < 1e-6 and abs(vel + 31.0) < 1e-6
    report("视线方向", ok, "相机方位 137° 仰角 31° → 视线方位 %.3f° 俯仰 %+.3f°"
           % (vaz, vel))
    cam.orbit(0, -90)
    lo = cam.el
    cam.orbit(0, +200)
    report("仰角限位", abs(lo - Camera3D.EL_MIN) < 1e-9
           and abs(cam.el - Camera3D.EL_MAX) < 1e-9,
           "下限 %.1f° 上限 %.1f° (不会转到晷面底下)" % (lo, cam.el))

    # 11. 历法 (纯儒略日, 支持公元前)
    print("\n11) 儒略日历法 (公元前也要对)")
    worst = 0
    for (y, mo, d, hh, mi, ss, jd) in [
            (2000, 1, 1, 12, 0, 0, 2451545.0), (1987, 1, 27, 0, 0, 0, 2446822.5),
            (1957, 10, 4, 19, 26, 24, 2436116.31), (837, 4, 10, 7, 12, 0, 2026871.8),
            (-1000, 7, 12, 12, 0, 0, 1356001.0), (-1001, 8, 17, 21, 36, 0, 1355671.4),
            (-4712, 1, 1, 12, 0, 0, 0.0)]:
        v = cal_to_jd(y, mo, d, hh, mi, ss)
        worst = max(worst, abs(v - jd))
    report("Meeus 历表 7 例", worst < 1e-6, "最大偏差 %.2e 日" % worst)
    bad = 0
    for k in range(0, 3000):
        j = 900000.0 + k * 987.6543
        y, mo, d, hh, mi, ss = jd_to_cal(j)
        if abs(cal_to_jd(y, mo, d, hh, mi, ss) - j) > 2e-5:
            bad += 1
    report("JD↔历 往返 3000 次", bad == 0, "失败 %d 次 (跨越公元前 3000 年至今)" % bad)

    # 12. 日食: 与 NASA/Espenak 食典比对
    print("\n12) 日食几何 (对比 NASA 五千年日食典)")

    def solar_at(y, mo, d):
        jd0 = cal_to_jd(y, mo, d, 12, 0, 0)
        k = round((y + (mo - 1) / 12.0 - 2000) * 12.3685)
        best = None
        for kk in range(k - 2, k + 3):
            jde, _F = phase_jde(kk)
            j = jde - delta_t_jd(jde) / 86400.0
            if abs(j - jd0) < 2.0:
                best = j
        t = _parab_min(lambda x: solar_geom(x)["sep_km"], best, 0.03)
        return t, solar_geom(t)

    # (日期, γ, 最大食点纬度, 经度, 类型, 本影带宽 km, 食分, 中心食时长 s)
    SOL_REF = [
        ((2017, 8, 21), 0.4367, 36.97, -87.65, "全食", 115.0, 1.0306, 160.2),
        ((2024, 4, 8), 0.3431, 25.30, -104.13, "全食", 197.5, 1.0566, 268.1),
        ((2009, 7, 22), 0.0698, 24.22, 144.13, "全食", 258.4, 1.0799, 398.8),
        ((2019, 7, 2), -0.6466, -17.42, -108.97, "全食", 200.6, 1.0459, 273.4),
        ((2023, 10, 14), 0.3753, 11.36, -83.12, "环食", 187.8, 0.9520, 317.0),
        ((2023, 4, 20), -0.3952, -9.62, 125.80, "全环食", 49.0, 1.0132, 76.0),
        ((1999, 8, 11), 0.5062, 45.10, 24.30, "全食", 112.4, 1.0286, 143.0),
    ]
    wt, wg, wp, wm, wd, kind_ok = 0.0, 0.0, 0.0, 0.0, 0.0, True
    for (ymd, ga, la, lo, kd, wid, mg, du) in SOL_REF:
        t, g = solar_at(*ymd)
        wg = max(wg, abs(g["gamma"] - ga))
        wp = max(wp, abs(g["pierce"][0] - la), abs(norm180(g["pierce"][1] - lo)))
        kind_ok = kind_ok and (solar_kind(g) == kd)
        wd = max(wd, abs(solar_path_width(g) - wid) / wid)
        c = local_solar_contacts(t, la, lo)
        wm = max(wm, abs(c["mag"] - mg))
        if c["c2"] and c["c3"]:
            wt = max(wt, abs((c["c3"] - c["c2"]) * 86400.0 - du))
    report("γ (影轴到地心距)", wg < 0.001, "最大偏差 %.5f 地球半径" % wg)
    report("最大食点经纬度", wp < 0.05, "最大偏差 %.4f° (≈%.1f km)" % (wp, wp * 111.2))
    report("食类型 (含全环食)", kind_ok, "7 例全部判对 (全食/环食/全环食)")
    report("本影带宽", wd < 0.02, "最大相对偏差 %.2f%%" % (wd * 100))
    report("食分 (最大食点)", wm < 0.001, "最大偏差 %.5f" % wm)
    report("中心食持续时间", wt < 2.0, "最大偏差 %.2f 秒" % wt)

    # 全环食判据
    hyb = [((2013, 11, 3), "全环食"), ((2005, 4, 8), "全环食"),
           ((2031, 11, 14), "全环食"), ((2020, 6, 21), "环食"),
           ((2027, 8, 2), "全食"), ((2026, 2, 17), "环食")]
    ok = all(solar_kind(solar_at(*d)[1]) == k for d, k in hyb)
    report("全环食(混合食)判据", ok, "另 6 例 (2013/2005/2031/2020/2027/2026) 全对")

    # 13. 月食
    print("\n13) 月食 (Danjon 1/85 影放大, 对比 NASA 五千年月食典)")

    def lunar_at(y, mo, d):
        jd0 = cal_to_jd(y, mo, d, 12, 0, 0)
        k = round((y + (mo - 1) / 12.0 - 2000) * 12.3685)
        best = None
        for kk in range(k - 2, k + 3):
            jde, _F = phase_jde(kk + 0.5)
            j = jde - delta_t_jd(jde) / 86400.0
            if abs(j - jd0) < 2.0:
                best = j
        return lunar_contacts(best)

    LUN_REF = [((2025, 9, 7), "月全食", 1.3619, 82.0), ((2022, 11, 8), "月全食", 1.3589, 84.9),
               ((2021, 5, 26), "月全食", 1.0095, 14.5), ((2026, 3, 3), "月全食", 1.1512, 58.2),
               ((2019, 7, 16), "月偏食", 0.6531, None), ((2023, 10, 28), "月偏食", 0.1220, None)]
    wm = wt = 0.0
    kok = True
    for ymd, kd, mg, tot in LUN_REF:
        c = lunar_at(*ymd)
        kok = kok and (c["kind"] == kd)
        wm = max(wm, abs(c["mag_u"] - mg))
        if tot:
            wt = max(wt, abs((c["u3"] - c["u2"]) * 1440.0 - tot))
    report("月食类型", kok, "6 例全对")
    report("本影食分", wm < 0.001, "最大偏差 %.5f" % wm)
    report("全食持续时间", wt < 0.3, "最大偏差 %.2f 分钟" % wt)

    # 14. 圭表 (土圭)
    print("\n14) 圭表 (土圭) 几何")
    H = 196.0
    worst = 0.0
    for lat in (-40.0, -3.0, 0.0, 3.139, 23.0, 34.4067, 52.0):
        for mth in (1, 3, 6, 9, 12):
            t = local_apparent_noon(2026, mth, 15, lat, 101.6869, 8.0)
            alt, az, _at, _sd, dec = gui_sun_at(t, lat, 101.6869)
            if alt <= 3:
                continue
            L = gnomon_shadow(H, alt)
            worst = max(worst, abs(L - H / dtan(alt)))
            # 正午时影必落在子午线上 (方位 0° 或 180°)
            worst = max(worst, min(abs(norm180(az)), abs(norm180(az - 180.0))) * 1e-4)
    report("影长 = 表高/tan(h)", worst < 1e-6, "最大残差 %.2e cm; 正午影严格在子午线上" % worst)

    # 所需圭长: 与逐日暴力扫描比对
    for lat in (3.139, 34.4067, -33.87):
        n_req, s_req, _note = gui_required_arms(H, lat)
        bn = bs = 0.0
        for doy in range(0, 366, 3):
            d0 = dt.datetime(2026, 1, 1) + dt.timedelta(days=doy)
            t = local_apparent_noon(d0.year, d0.month, d0.day, lat, 101.6869, 8.0)
            alt, az, _a, _s, _d = gui_sun_at(t, lat, 101.6869)
            L = gnomon_shadow(H, alt)
            if L is None:
                continue
            r = -L * dcos(az)
            bn = max(bn, r)
            bs = max(bs, -r)
        okn = (n_req is None) or abs(bn - n_req) / max(1.0, n_req) < 0.03
        oks = abs(bs - (s_req or 0.0)) < max(2.0, 0.05 * H)
        report("φ=%+.2f° 圭长需求" % lat, okn and oks,
               "公式 北 %.1f/南 %.1f cm ; 逐日扫描 北 %.1f/南 %.1f cm"
               % (-1.0 if n_req is None else n_req,
                  -1.0 if s_req is None else s_req, bn, bs))

    # 低纬度: 一年之中影会南北易向
    rows = gui_term_rows(2026, 3.139, 101.6869, 8.0, 20.0)
    dirs = set(r["dir"] for r in rows if r["reading"] is not None)
    report("吉隆坡影向南北互易", {"北", "南"} <= dirs,
           "24 节气正午影向: %s (回归线内的必然现象)" % "/".join(sorted(dirs)))

    # 半影模糊带
    u, gm, p = gnomon_penumbra(946.0, 32.18, 0.2724)
    exp = 946.0 * (1.0 / dtan(32.18 - 0.2724) - 1.0 / dtan(32.18 + 0.2724))
    report("半影模糊带", p > gm > u > 0 and abs((p - u) - exp) < 1e-6,
           "登封冬至: 本影 %.1f / 几何 %.1f / 半影 %.1f cm, 模糊带宽 %.2f cm "
           "—— 郭守敬「景符」正为消此" % (u, gm, p, p - u))

    # 15. 月相定向 (南半球是反的)
    print("\n15) 月相明暗方向 (南北半球相反)")

    def _u(v):
        n = math.sqrt(_dot(v, v))
        return tuple(x / n for x in v)

    worst = 0.0
    random.seed(20260903)
    for _ in range(3000):
        lat = random.uniform(-85, 85)
        lha = random.uniform(-179, 179)
        dec = random.uniform(-70, 70)
        chi = random.uniform(0, 360)
        alt, az = altaz_from_hadec(norm360(lha), dec, lat)
        if alt < 3:
            continue
        um = (dsin(az) * dcos(alt), dcos(az) * dcos(alt), dsin(alt))
        P = (0.0, dcos(lat), dsin(lat))
        nh = _u([P[i] - _dot(P, um) * um[i] for i in range(3)])
        eh = _cross(nh, um)
        a2, z2 = altaz_from_hadec(norm360(lha - 0.01 / max(0.05, dcos(dec))), dec, lat)
        u2 = (dsin(z2) * dcos(a2), dcos(z2) * dcos(a2), dsin(a2))
        if _dot(_u([u2[i] - um[i] for i in range(3)]), eh) < 0:
            eh = tuple(-x for x in eh)
        limb = [dcos(chi) * nh[i] + dsin(chi) * eh[i] for i in range(3)]
        up = _u([(0.0, 0.0, 1.0)[i] - um[i] * um[2] for i in range(3)])
        right = _cross(um, up)
        pa_true = math.degrees(math.atan2(_dot(limb, right), _dot(limb, up)))
        pa_f = -(chi - parallactic_angle(lha, dec, lat))
        worst = max(worst, abs(norm180(pa_true - pa_f)))
    report("屏幕明暗方位 = −(χ−q)", worst < 1e-6,
           "3000 组随机 (纬度 ±85°) 最大偏差 %.2e°" % worst)
    # 上弦月: 北半球亮在右, 南半球亮在左
    chi_fq = 270.0                     # 上弦: 亮边朝西
    pn = norm360(-(chi_fq - parallactic_angle(0.0, 0.0, 40.0)))
    ps = norm360(-(chi_fq - parallactic_angle(0.0, 0.0, -40.0)))
    report("上弦月南北半球翻转", dsin(pn) > 0.9 and dsin(ps) < -0.9,
           "北纬40° 亮边屏幕方位 %.0f°(右) / 南纬40° %.0f°(左)" % (pn, ps))

    # 16. 圆交集 (月食阴影)
    print("\n16) 圆交集多边形 (月食本影遮月的形状)")
    worst = 0.0
    for r1, r2, d in ((1.0, 1.0, 1.0), (1.0, 2.0, 1.5), (0.5, 3.0, 2.6),
                      (1.0, 1.3, 0.4), (2.0, 1.0, 2.5)):
        pts = circle_lens((0, 0), r1, (d, 0), r2, 400)
        a = 0.0
        for i in range(len(pts)):
            x0, y0 = pts[i]
            x1, y1 = pts[(i + 1) % len(pts)]
            a += x0 * y1 - x1 * y0
        a = abs(a) / 2.0
        c1 = max(-1.0, min(1.0, (d * d + r1 * r1 - r2 * r2) / (2 * d * r1)))
        c2 = max(-1.0, min(1.0, (d * d + r2 * r2 - r1 * r1) / (2 * d * r2)))
        tri = 0.5 * math.sqrt(max(0.0, (-d + r1 + r2) * (d + r1 - r2)
                                  * (d - r1 + r2) * (d + r1 + r2)))
        exact = r1 * r1 * math.acos(c1) + r2 * r2 * math.acos(c2) - tri
        worst = max(worst, abs(a - exact) / exact)
    report("透镜面积", worst < 2e-4, "对比解析解, 最大相对偏差 %.2e" % worst)

    # 17. 轨道页
    print("\n17) 轨道页 (日心位置 / 一周期 / 定盘 / 十二宫)")
    # (a) 一个恒星周期后回到原处
    jd0 = julian_day(dt.datetime(2026, 1, 20, 4, 0))
    res = []
    for p in ORB_PLANETS:
        v0, L0, B0, R0 = orb_helio_xyz(p, jd0)
        v1, L1, B1, R1 = orb_helio_xyz(p, jd0 + ORB_PERIOD[p])
        res.append((p, abs(norm180(L1 - L0))))
    worst = max(r[1] for r in res)
    # 大行星互相摄动, 实际周期本就不严格等于平均恒星周期 (土星受木星摄动最甚),
    # 故容差取 1.5°, 只用来抓「周期表填错」这类粗错。
    report("恒星周期闭合", worst < 1.5,
           "走满一周期后日心黄经残差 " + " ".join("%s%.2f°" % r for r in res))
    # (b) 日心距落在近远日点之间 (±1.5%: 近远日距本身受摄动逐圈变动)
    bounds = {"水星": (0.3075, 0.4667), "金星": (0.7184, 0.7282),
              "地球": (0.9833, 1.0167), "火星": (1.3814, 1.6660),
              "木星": (4.9501, 5.4570), "土星": (9.0412, 10.1238)}
    bad = []
    for p in ORB_PLANETS:
        lo, hi = 9e9, -9e9
        for i in range(0, 241):
            _v, _L, _B, R = orb_helio_xyz(p, jd0 + ORB_PERIOD[p] * i / 240.0)
            lo, hi = min(lo, R), max(hi, R)
        b = bounds[p]
        if lo < b[0] * 0.985 or hi > b[1] * 1.015:
            bad.append("%s %.4f~%.4f (册 %.4f~%.4f)" % (p, lo, hi, b[0], b[1]))
    report("近/远日距在册", not bad,
           "6 星一周期内日心距皆在已知近远日点 ±1.5% 内"
           if not bad else ";".join(bad))
    # (c) 大寒 = 太阳黄经 300° = 地球日心黄经 120° = 子宫 0°
    t_dh = solar_term_utc(2026, 300.0)
    jt = julian_day(t_dh) + delta_t_seconds(t_dh) / 86400.0
    Le, Be, Re = helio_ecl("earth", jt)
    g, gd, gt = orb_gong_of(300.0)
    ok = (abs(norm180(Le - 120.0)) < 0.02 and g == "子" and gd < 1e-9
          and gt == "大寒")
    report("大寒锚点", ok,
           "%s(UT) 地球日心黄经 %.4f° (应 120°, 差 %.1f″ = 光行差), "
           "此点定为 %s宫 %.3f° / %s"
           % (t_dh.strftime("%Y-%m-%d %H:%M"), Le,
              abs(norm180(Le - 120.0)) * 3600.0, g, gd, gt))
    # (d) 定盘 —— 子 0° 恒在正下方:
    #     日地恒定 (预设): 不论哪天, 地球与日地虚线都在正下方 (= 子 0°), 别的星在
    #                      (日心黄经 − 地球日心黄经) 处;
    #     大寒定盘: 子宫 0° (地球 L120°) 在正下方, 大寒日地球在正下方, 平日照常绕行
    def _scr(L, Lref):
        a = norm360(L - Lref)
        return dsin(a), dcos(a)                  # (右, 下)
    ok_d = True
    for L_now in (9.88, 120.0, 250.0, 359.99):   # 不同日期的地球位置
        x, y = _scr(L_now, orb_lref("earth", L_now))
        ok_d = ok_d and abs(x) < 1e-12 and abs(y - 1.0) < 1e-12
        a_mars = norm360(76.8 + L_now - orb_lref("earth", L_now))
        ok_d = ok_d and abs(a_mars - 76.8) < 1e-9
        x, y = _scr(120.0, orb_lref("term", L_now))
        ok_d = ok_d and abs(x) < 1e-12 and abs(y - 1.0) < 1e-12
    xe, ye = _scr(Le, orb_lref("term", Le))      # 大寒日的地球
    ok_d = ok_d and abs(xe) < 4e-4 and ye > 0.9999
    a_oct = norm360(9.88 - orb_lref("term", 9.88))
    ok_d = ok_d and abs(a_oct - 249.88) < 1e-9
    report("子 0° 定盘", ok_d,
           "日地恒定: 地球/日地虚线恒在正下方 (子 0°), 他星在 L−L地; "
           "大寒定盘: 子宫 0° 恒在正下方, 大寒日地球在正下方, 10-03 地球在 %.2f°"
           % a_oct)
    # (d2) 日地恒定盘上 相对角 0° = 冲 / 下合: 对照公布的日期 (UT)
    ev_ok, ev_txt = True, []
    for nm, day, kind in (("木星", dt.datetime(2026, 1, 10), "冲"),
                          ("土星", dt.datetime(2026, 10, 4), "冲"),
                          ("金星", dt.datetime(2026, 10, 24), "下合")):
        def _rel(jd, nm=nm):
            return norm180(orb_rel_pos(nm, jd + delta_t_seconds(
                jd_to_datetime(jd)) / 86400.0)[0])
        a, b = julian_day(day) - 6.0, julian_day(day) + 6.0
        fa = _rel(a)
        for _ in range(50):
            mid = 0.5 * (a + b)
            fm = _rel(mid)
            if (fa < 0) == (fm < 0):
                a, fa = mid, fm
            else:
                b = mid
        hit = jd_to_datetime(0.5 * (a + b))
        dd = (hit - day).total_seconds() / 86400.0
        ev_ok = ev_ok and -0.01 <= dd < 1.01           # 落在公布的那一天 (UT) 之内
        ev_txt.append("%s%s %s" % (nm, kind, hit.strftime("%m-%d %H:%M")))
    report("日地恒定 子 0° = 冲/下合", ev_ok,
           " · ".join(ev_txt) + " (公布: 木星冲 01-10, 土星冲 10-04, 金星下合 10-24)")
    # (d3) 相对轨迹: 走满一个平均会合周期, 相对角转回原处 (偏心率使实际会合周期
    #      有出入, 水星最大, 故只取外行星与金星严查)
    jt0 = julian_day(dt.datetime(2026, 1, 1))
    res = []
    for nm in ("金星", "火星", "木星", "土星"):
        a0 = orb_rel_pos(nm, jt0)[0]
        a1 = orb_rel_pos(nm, jt0 + ORB_SYNODIC[nm])[0]
        res.append((nm, abs(norm180(a1 - a0))))
    report("会合周期闭合", max(r[1] for r in res) < 12.0,
           "一个平均会合周期后相对角残差 " + " ".join("%s%.1f°" % r for r in res))
    # (e) 十二宫环: 每宫 30°, 首宫起于大寒
    seq_ok = all(orb_gong_of(300.0 + 30.0 * k)[0] == ORB_GONG[k]
                 for k in range(12))
    span_ok = all(abs(orb_gong_of(300.0 + 30.0 * k + 29.999)[1] - 29.999) < 1e-6
                  for k in range(12))
    report("十二宫分度", seq_ok and span_ok,
           "子亥戌酉申未午巳辰卯寅丑, 每宫 30°, 子宫 0° = 黄经 300°")
    # (f) 月亮: 日心向量 = 地球日心向量 + 地心向量, 地月距合理
    utc = dt.datetime(2026, 3, 5, 0, 0)
    jd_ut = julian_day(utc)
    jt = jd_ut + delta_t_seconds(utc) / 86400.0
    m = EPH.get("月亮", utc)
    lam, bet = equ_to_ecl(m.ra, m.dec, true_obliquity(jt))
    gv = _rect(lam, bet, m.dist_km / AU_KM)
    ev = _rect(*helio_ecl("earth", jt))
    hv = tuple(a2 + b2 for a2, b2 in zip(ev, gv))
    dmoon = math.sqrt(sum((hv[i] - ev[i]) ** 2 for i in range(3)))
    report("月亮日心向量", 0.00238 < dmoon < 0.00272,
           "地月距 %.6f AU = %.0f km (合 356400~406700 km)"
           % (dmoon, dmoon * AU_KM))

    # 18. 日晷: 三维晷面上的影子方向必须与时线一致 (赤道晷秋分→春分照南面)
    print("\n18) 晷面投影影向 (赤道晷两面 / 水平晷 / 垂直晷)")
    worst, cases, bad = 0.0, 0, 0
    for kind in ("赤道晷 Equatorial", "水平晷 Horizontal", "垂直朝南晷 Vertical South"):
        for lat in (-45.0, -20.0, -3.0, 3.139, 20.0, 40.0, 60.0):
            geo = dial_geom3d(kind, lat)
            ctr, nrm, rv, uv = geo["center"], geo["n"], geo["r"], geo["u"]
            for dec in (-23.0, -10.0, -3.9, 3.9, 10.0, 23.0):
                for Hh in range(-170, 171, 10):
                    alt, az = altaz_from_hadec(norm360(Hh), dec, lat)
                    if alt <= 1:
                        continue
                    sv = _enu_from_altaz(alt, az)
                    sn = _dot(sv, nrm)
                    if abs(sn) < 1e-3:
                        continue
                    tip = style_tip_on_lit_side(geo, sn)
                    if tip is None:
                        continue
                    t = _dot(tuple(tip[i] - ctr[i] for i in range(3)), nrm) / sn
                    tS = tuple(tip[i] - sv[i] * t for i in range(3))
                    v = tuple(tS[i] - geo["root"][i] for i in range(3))
                    dx, dy = _dot(v, rv), _dot(v, uv)
                    ln = math.hypot(dx, dy)
                    want = style_shadow_on_plane(lat, Hh, nrm, rv, uv)
                    if ln < 1e-9 or want is None:
                        continue
                    ang = math.degrees(math.acos(max(-1.0, min(1.0, (dx * want[0] + dy * want[1]) / ln))))
                    cases += 1
                    worst = max(worst, ang)
                    bad += ang > 0.01
    report("投影影向 = 时线方向", bad == 0,
           "%d 组 (3 种晷 × 7 纬度 × 6 赤纬 × 时角), 最大偏差 %.1e°" % (cases, worst))
    # 平面图 (2D) 赤道晷的左右手性: 正对受照面、正午影线朝下, 上午影在哪一侧
    bad2 = 0
    for lat in (40.0, 3.139, -3.139, -33.87):
        for dec in (20.0, -20.0):
            gax = polar_axis(lat)
            alt, az = altaz_from_hadec(norm360(-45.0), dec, lat)
            sv = _enu_from_altaz(alt, az)
            nl = gax if _dot(sv, gax) > 0 else tuple(-x for x in gax)

            def sh(Hx):
                a2, z2 = altaz_from_hadec(norm360(Hx), dec, lat)
                s2 = _enu_from_altaz(a2, z2)
                sp = tuple(s2[i] - _dot(s2, nl) * nl[i] for i in range(3))
                m_ = math.sqrt(_dot(sp, sp))
                return tuple(-x / m_ for x in sp)
            up = tuple(-x for x in sh(0.0))
            right = _cross(up, nl)
            phys_right = _dot(sh(-45.0), right) > 0              # 上午影在右?
            code_right = -dsin(eq2d_sign(dec) * -45.0) > 0
            bad2 += phys_right != code_right
    report("平面图赤道晷左右", bad2 == 0,
           "南北半球 × 上下两面共 8 组: 正对受照面看, 上午影所在侧与实物一致"
           if bad2 == 0 else "%d 组左右颠倒" % bad2)
    # 垂直晷朝向赤道: 南半球冬夏正午都有影, 晷针在受照一侧, 影线朝下
    okv = True
    for lat in (-45.0, -33.87, 33.87, 45.0):
        geo = dial_geom3d("垂直", lat)
        for dec in (-20.0, 0.0, 20.0):
            alt, az = altaz_from_hadec(0.0, dec, lat)
            sv = _enu_from_altaz(alt, az)
            sn = _dot(sv, geo["n"])
            tip = style_tip_on_lit_side(geo, sn) if sn > 1e-6 else None
            d = style_shadow_on_plane(lat, 0.0, geo["n"], geo["r"], geo["u"])
            okv = okv and tip is not None and d is not None and d[1] < -0.99
    report("垂直晷朝向赤道", okv,
           "φ=±33.87°/±45°, 冬至/春分/夏至正午: 墙面受光、晷针在受光侧、正午线竖直向下")
    okb = (gui_biao_side(34.62) == "S" and gui_biao_side(-33.87) == "N"
           and gui_biao_side(3.139) == "C" and gui_biao_side(0.0) == "C"
           and gui_biao_side(-23.0) == "C")
    report("土圭表身位置", okb, "北回归线以北表身在南, 南回归线以南表身在北, 其间用细杆居中")
    worst = 0.0
    for kind, f in (("水平晷", lambda la, H: math.degrees(math.atan2(dsin(abs(la)) * dsin(H), dcos(H)))),
                    ("赤道晷", lambda la, H: H),
                    ("垂直", lambda la, H: math.degrees(math.atan2(dcos(la) * dsin(H), dcos(H))))):
        for lat in (-60.0, -33.87, -10.0, 10.0, 34.62, 60.0):
            geo = dial_geom3d(kind, lat)
            for H in range(-135, 136, 15):
                th = hour_line_angle(geo, lat, float(H))
                if th is not None:
                    worst = max(worst, abs(norm180(th - f(lat, float(H)))))
    report("规格表时线角", worst < 1e-6,
           "三种晷 × 南北 6 个纬度: 与 tanθ=sinφtanH / θ=H / tanθ=cosφtanH 最大差 %.1e°"
           % worst)

    # 19. 土圭: 圭轴恒为子午线; 影朝南/朝北的日期段与逐日正午读数一致
    print("\n19) 土圭方位 (子午线 / 影向季节 / 日中无影)")
    worst = 0.0
    for lat in (-60.0, -33.87, -23.0, -10.0, 0.0, 3.139, 10.0, 23.0, 34.4067, 60.0):
        for mth in range(1, 13):
            t = local_apparent_noon(2026, mth, 10, lat, 101.6869, 8.0)
            alt, az, _a, _s, _d = gui_sun_at(t, lat, 101.6869)
            if alt > 2:
                worst = max(worst, min(abs(norm180(az)), abs(norm180(az - 180.0))))
    report("正午影方位 ∈ {0°, 180°}", worst < 0.01,
           "10 个纬度 × 12 个月, 正午太阳方位偏离子午线最大 %.4f°" % worst)
    mism = 0
    tot = 0
    for lat in (-23.0, -10.0, 0.0, 3.139, 10.0, 23.0):
        south, _dark = gui_season_spans(2026, lat, 101.6869, 8.0)
        for doy in range(0, 365, 2):
            d0 = dt.datetime(2026, 1, 1) + dt.timedelta(days=doy)
            t = local_apparent_noon(d0.year, d0.month, d0.day, lat, 101.6869, 8.0)
            alt, az, _a, _s, dec = gui_sun_at(t, lat, 101.6869)
            if abs(dec - lat) < 0.45:            # 过天顶前后一两天, 方向本来就模糊
                continue
            is_south = abs(norm180(az)) < 90.0     # 太阳在北 → 影朝南
            in_span = any(a <= d0 + dt.timedelta(hours=12) < b for a, b in south)
            tot += 1
            mism += (is_south != in_span)
    report("影朝南/朝北日期段", mism == 0,
           "回归线内 6 个纬度逐 2 日核对 %d 天, 不符 %d 天" % (tot, mism))
    ss = gui_noon_seasons(2026, 3.139, 101.6869, 8.0)
    zz = sorted(ss["zen"], key=lambda z: z["noon"])
    ok = len(zz) == 2 and all(z["zd"] < 0.25 for z in zz)
    report("吉隆坡日中无影", ok,
           "%s (那天正午天顶距 %s)"
           % (" · ".join((z["noon"] + dt.timedelta(hours=8)).strftime("%m-%d %H:%M") for z in zz),
              " / ".join("%.3f°" % z["zd"] for z in zz)))
    cases = [(359.9996, 2, "0.00"), (-1e-12, 3, "0.000"), (359.96, 1, "0.0"),
             (180.0 - 1e-9, 2, "180.00"), (359.994, 2, "359.99"), (720.25, 2, "0.25")]
    got = [("%%.%df" % nd) % az_fmt(a, nd) for a, nd, _ in cases]
    ok = got == [w for _, _, w in cases]
    report("方位显示不出 360", ok,
           "正午影方位 359.9996° 印作 %s° (不是 360.00°); 其余 %s"
           % (got[0], ", ".join(got[1:])))

    # 20. 全英文界面: 对照表完整、模板占位符一致、中英模式不受影响
    print("\n20) 全英文界面 (对照表)")
    global LANG
    import ast as _ast
    spec = _re.compile(r"%(?:\([^)]*\))?[#0\- +]*(?:\*|\d+)?(?:\.(?:\*|\d+))?[hlL]?[diouxXeEfFgGcrsa%]")
    bad_spec = [k for k, v in _EN.items() if spec.findall(k) and spec.findall(k) != spec.findall(v)
                and "%" in k and _re.search(r"%[^%]", k)]
    import os as _os
    src_path = _os.path.abspath(__file__) if "__file__" in globals() else sys.argv[0]
    tree = _ast.parse(open(src_path, encoding="utf-8").read())
    lits = set()
    for node in _ast.walk(tree):
        if isinstance(node, _ast.Call) and isinstance(node.func, _ast.Name) and node.func.id == "_T":
            for a in node.args:
                if isinstance(a, _ast.Constant) and isinstance(a.value, str):
                    lits.add(a.value)
    # 真实的轨道页表头模板, 代入中文的宫名、节气名后整句应无中文残留
    head = ("日地恒定 · 地球恒在正下方 = 子 0° (地球日心黄经 %.2f°) · "
            "此刻太阳在 %s宫 %.2f° (%s后)")
    vals = (9.88, "辰", 9.88, "秋分")
    old = LANG
    try:
        LANG = "en"
        _TR_CACHE.clear()
        untranslated = [x for x in lits if _CJK_RE.search(tr(_T(x)))]
        sample = tr(_T(head) % vals)
    finally:
        LANG = old
        _TR_CACHE.clear()
    zh_same = (tr("太阳") == "太阳" and _T(head) == head
               and tr(head % vals) == head % vals)
    report("对照表 / 模板", not bad_spec and not untranslated,
           "%d 条对照, %d 个 _T 模板全部有英文且占位符一致" % (len(_EN), len(lits))
           if not (bad_spec or untranslated) else
           "占位符不一致 %d, 未译模板 %d: %r" % (len(bad_spec), len(untranslated),
                                            (bad_spec + untranslated)[:3]))
    report("英文拼句 / 中英模式原样", zh_same and not _CJK_RE.search(sample),
           "例: %s" % sample)

    print("\n" + "=" * 74)
    print("总计: %s" % ("全部通过" if ok_all else "有项目未通过"))
    print("=" * 74)
    return 0 if ok_all else 1


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry("1400x960")
    root.minsize(1050, 700)
    App(root)
    root.mainloop()


# ===========================================================================
#  全英文界面的对照表: 中文原文 -> 英文 (格式模板的占位符与次序和原文一致)
# ===========================================================================
_EN_DATA = {
    '丑': 'Chou',
    '东': 'E',
    '亥': 'Hai',
    '分': 'min',
    '北': 'N',
    '十': '10',
    '午': 'Wu',
    '南': 'S',
    '卯': 'Mao',
    '向': 'Toward',
    '大': 'Large',
    '子': 'Zi',
    '宫': 'palace',
    '寅': 'Yin',
    '巳': 'Si',
    '年': 'yr',
    '度': 'deg',
    '快': 'ahead of',
    '慢': 'behind',
    '戌': 'Xu',
    '无': 'none',
    '日': 'd',
    '时': 'h',
    '月': 'mo',
    '未': 'Wei',
    '申': 'Shen',
    '秒': 's',
    '背': 'Away',
    '至': 'to',
    '西': 'W',
    '辰': 'Chen',
    '酉': 'You',
    '三十': '30th',
    '上午': 'morning',
    '上海': 'Shanghai',
    '下午': 'afternoon',
    '丑宫': 'Chou palace',
    '丑时': 'Chou hour',
    '东京': 'Tokyo',
    '东北': 'NE',
    '东南': 'SE',
    '两者': 'Both',
    '中天': 'Transit',
    '中心': 'Centre',
    '二十': '20th',
    '亥宫': 'Hai palace',
    '亥时': 'Hai hour',
    '传统': 'Traditional',
    '伦敦': 'London',
    '俯视': 'Top view',
    '偏亮': 'Rather bright',
    '偏暗': 'Rather dark',
    '偏食': 'Partial',
    '停止': 'Stop',
    '全程': 'Full',
    '全食': 'Total',
    '冬至': 'Winter Solstice',
    '切点': 'Limb',
    '初一': '1st',
    '初七': '7th',
    '初三': '3rd',
    '初九': '9th',
    '初二': '2nd',
    '初五': '5th',
    '初八': '8th',
    '初六': '6th',
    '初十': '10th',
    '初四': '4th',
    '刷新': 'Refresh',
    '刻度': 'Scale',
    '北京': 'Beijing',
    '十一': '11th',
    '十七': '17th',
    '十三': '13th',
    '十九': '19th',
    '十二': '12th',
    '十五': '15th',
    '十八': '18th',
    '十六': '16th',
    '十四': '14th',
    '午宫': 'Wu palace',
    '午时': 'Wu hour',
    '南京': 'Nanjing',
    '卯宫': 'Mao palace',
    '卯时': 'Mao hour',
    '台北': 'Taipei',
    '合适': 'Good',
    '名称': 'Names',
    '图例': 'Legend',
    '土星': 'Saturn',
    '地平': 'Horizon',
    '地球': 'Earth',
    '垂直': 'Vertical',
    '处暑': 'Heat Ends',
    '复位': 'Reset',
    '夏至': 'Summer Solstice',
    '大寒': 'Major Cold',
    '大暑': 'Major Heat',
    '大雪': 'Major Snow',
    '天体': 'Body',
    '天津': 'Tianjin',
    '天顶': 'Zenith',
    '太阳': 'Sun',
    '套用': 'Apply',
    '子宫': 'Zi palace',
    '子时': 'Zi hour',
    '安阳': 'Anyang',
    '寅宫': 'Yin palace',
    '寅时': 'Yin hour',
    '寒露': 'Cold Dew',
    '小寒': 'Minor Cold',
    '小暑': 'Minor Heat',
    '小满': 'Grain Buds',
    '小雪': 'Minor Snow',
    '尺长': 'Chi length',
    '巳宫': 'Si palace',
    '巳时': 'Si hour',
    '广州': 'Guangzhou',
    '廿一': '21st',
    '廿七': '27th',
    '廿三': '23rd',
    '廿九': '29th',
    '廿二': '22nd',
    '廿五': '25th',
    '廿八': '28th',
    '廿六': '26th',
    '廿四': '24th',
    '影长': 'Shadow length',
    '悉尼': 'Sydney',
    '惊蛰': 'Insects Awaken',
    '戌宫': 'Xu palace',
    '戌时': 'Xu hour',
    '成都': 'Chengdu',
    '拉萨': 'Lhasa',
    '指标': 'Index',
    '放大': 'Zoom in',
    '日出': 'Sunrise',
    '日期': 'Date',
    '日落': 'Sunset',
    '时制': 'Hour system',
    '时刻': 'Time',
    '时辰': 'Shichen',
    '昆明': 'Kunming',
    '星历': 'Ephemeris',
    '星名': 'star name',
    '星等': 'mag',
    '春分': 'Spring Equinox',
    '昼长': 'Daylight',
    '暂停': 'Pause',
    '曲阜': 'Qufu',
    '月亮': 'Moon',
    '木星': 'Jupiter',
    '未宫': 'Wei palace',
    '未时': 'Wei hour',
    '未食': 'No eclipse',
    '极夜': 'Polar night',
    '极昼': 'Polar day',
    '极长': 'very long',
    '槟城': 'George Town',
    '正午': 'Noon',
    '此刻': 'Now',
    '武汉': 'Wuhan',
    '残月': 'Waning Crescent',
    '水平': 'Horizontal',
    '水星': 'Mercury',
    '沈阳': 'Shenyang',
    '洛阳': 'Luoyang',
    '济南': 'Jinan',
    '清明': 'Clear & Bright',
    '清空': 'Clear all',
    '火星': 'Mars',
    '环食': 'Annular',
    '珠影': 'Nodus shadow',
    '申宫': 'Shen palace',
    '申时': 'Shen hour',
    '白天': 'Daytime',
    '白露': 'White Dew',
    '秋分': 'Autumn Equinox',
    '立冬': 'Winter Begins',
    '立夏': 'Summer Begins',
    '立春': 'Spring Begins',
    '立秋': 'Autumn Begins',
    '类型': 'Type',
    '纽约': 'New York',
    '缩小': 'Zoom out',
    '节气': 'Term',
    '芒种': 'Grain in Ear',
    '西北': 'NW',
    '西南': 'SW',
    '西安': "Xi'an",
    '视图': 'View',
    '谷雨': 'Grain Rain',
    '赤纬': 'Dec',
    '赤经': 'RA',
    '赤道': 'Equatorial',
    '跳转': 'Go',
    '轨迹': 'Path',
    '辰宫': 'Chen palace',
    '辰时': 'Chen hour',
    '适配': 'Fit',
    '速度': 'Speed',
    '遮蔽': 'Obscur.',
    '郑州': 'Zhengzhou',
    '酉宫': 'You palace',
    '酉时': 'You hour',
    '重庆': 'Chongqing',
    '金星': 'Venus',
    '雨水': 'Rain Water',
    '霜降': 'Frost Descends',
    '青岛': 'Qingdao',
    '食分': 'Mag.',
    '食甚': 'Maximum',
    '香港': 'Hong Kong',
    '黄道': 'Ecliptic',
    '%d尺': '%d chi',
    '%d年': '%d CE',
    '%s尺': '%s chi',
    '+1分': '+1 min',
    '+1日': '+1 d',
    '+1时': '+1 h',
    '·带食': '·at rise/set',
    '−1分': '−1 min',
    '−1日': '−1 d',
    '−1时': '−1 h',
    '上弦月': 'First Quarter',
    '上边缘': 'Upper limb',
    '下弦月': 'Last Quarter',
    '下边缘': 'Lower limb',
    '东 E': 'E',
    '亏凸月': 'Waning Gibbous',
    '亮在右': 'lit on right',
    '亮在左': 'lit on left',
    '全环食': 'Hybrid',
    '北 N': 'N',
    '北半球': 'Northern Hemisphere',
    '北极圈': '66.5°N',
    '午高度': 'Noon Alt',
    '南 S': 'S',
    '南半球': 'Southern Hemisphere',
    '可见性': 'Visibility',
    '吉隆坡': 'Kuala Lumpur',
    '哈尔滨': 'Harbin',
    '地平镜': 'Horizon mirror',
    '大窗口': 'Pop out',
    '天北极': 'North celestial pole',
    '天文夜': 'Astronomical night',
    '娥眉月': 'Waxing Crescent',
    '尺寸分': 'Chi-cun-fen',
    '已保存': 'Saved',
    '已固定': 'fixed',
    '截距′': 'Int.′',
    '所选日': 'Selected',
    '指标镜': 'Index mirror',
    '新加坡': 'Singapore',
    '星图日': 'simulated days',
    '月偏食': 'Partial',
    '月全食': 'Total',
    '望远镜': 'Telescope',
    '标准时': 'Standard time',
    '检索中': 'Searching',
    '次年 ': 'next year ',
    '水平晷': 'Horizontal dial',
    '海平线': 'Sea horizon',
    '盈凸月': 'Waxing Gibbous',
    '看太阳': 'Look at Sun',
    '看月亮': 'Look at Moon',
    '真正午': 'Noon (apparent)',
    '自北看': 'From north',
    '自南看': 'From south',
    '自定义': 'Custom',
    '西 W': 'W',
    '规格表': 'Specs',
    '赤道晷': 'Equatorial dial',
    '雅加达': 'Jakarta',
    '  恒星': '  (star)',
    ' ←现在': ' ← now',
    ' 定位 ': ' Fix ',
    ' 显示 ': ' Display ',
    ' 观测 ': ' Observation ',
    ' 视图 ': ' View ',
    '#1 浅': '#1 light',
    '#2 中': '#2 medium',
    '#3 深': '#3 dark',
    '%d 次': '%d found',
    '+1 时': '+1 h',
    '+10分': '+10 min',
    '1日/秒': '1 day/s',
    'H1 浅': 'H1 light',
    'H2 中': 'H2 medium',
    'H3 深': 'H3 dark',
    '−1 时': '−1 h',
    '−10分': '−10 min',
    '⏸ 暂停': '⏸ Pause',
    '▶ 播放': '▶ Play',
    '▶ 继续': '▶ Resume',
    '【时间】': '[Time]',
    '【此刻】': '[Now]',
    '【说明】': '[Notes]',
    '一键清空': 'Clear all',
    '严格模拟': 'Strict simulation',
    '中天起午': 'Wu begins at transit',
    '乌鲁木齐': 'Urumqi',
    '二分二至': 'Eq. & Sol.',
    '保存失败': 'Save failed',
    '偏食时长': 'Partial dur.',
    '全球月食': 'Global lunar eclipses',
    '全程可见': 'Fully visible',
    '全部翻起': 'Raise all',
    '全食时长': 'Total dur.',
    '删除选中': 'Delete selected',
    '半影时长': 'Pen. dur.',
    '半影月食': 'Penumbral',
    '半影食分': 'Pen. mag.',
    '南%s尺': 'S %s chi',
    '向着天体': 'toward the body',
    '周边刻度': 'Edge scales',
    '四立八节': '8 major',
    '回到现在': 'Back to now',
    '圭·北臂': 'Scale · north arm',
    '圭·南臂': 'Scale · south arm',
    '圭面刻度': 'Scale graduations',
    '地平小图': 'Horizon inset',
    '地平网格': 'Alt-az grid',
    '地球恒钉': 'Earth pinned',
    '复位视图': 'Reset view',
    '天顶 Z': 'Zenith Z',
    '太阳高度': 'Sun alt.',
    '年份 自': 'Years from',
    '建议滤片': 'Advised shades',
    '开始检索': 'Search',
    '微动螺旋': 'Micrometer drum',
    '手表时间': 'clock time',
    '拖动中…': 'dragging…',
    '放大 +': 'Zoom in +',
    '整点时刻': 'Hour marks',
    '方位 θ': 'Direction θ',
    '日出方位': 'Rise Az',
    '日地连线': 'Sun-Earth line',
    '日期无效': 'Invalid date',
    '时刻格式': 'Time format',
    '显示时线': 'Show hour lines',
    '月亮高度': 'Moon alt.',
    '月相: ': 'Moon phase: ',
    '朔·新月': 'New Moon',
    '望·满月': 'Full Moon',
    '本地所见': 'Seen here',
    '本影带宽': 'Path width',
    '本影食分': 'Umbral mag.',
    '来自天体': 'From the body',
    '格林尼治': 'Greenwich',
    '检索中…': 'Searching…',
    '检索出错': 'Search error',
    '正午高度': 'Noon Alt',
    '正对晷面': 'Face-on',
    '气温 ℃': 'Temperature ℃',
    '看北极星': 'Look at Polaris',
    '看南十字': 'Look at Southern Cross',
    '真太阳时': 'Apparent solar time',
    '眼高 m': 'Height of eye m',
    '立即对准': 'Align now',
    '纬度 φ': 'Latitude φ',
    '经度 λ': 'Longitude λ',
    '缩小 −': 'Zoom out −',
    '背着天体': 'away from the body',
    '范围过大': 'Range too large',
    '落在圭上': 'falls on the scale',
    '观测不足': 'Too few sights',
    '视线俯角': 'Look-down angle',
    '计算船位': 'Compute fix',
    '读数偏大': 'reading too high',
    '读数偏小': 'reading too low',
    '读数记录': 'Read and record',
    '速度无效': 'Invalid speed',
    '重置视角': 'Reset view',
    '食甚可见': 'Max visible',
    ' 动 画 ': ' Animation ',
    ' 显 示 ': ' Display ',
    ' 航海历 ': ' Nautical Almanac ',
    '#4 最深': '#4 darkest',
    '%s%d分': '%s%d fen',
    '12 时辰': '12 shichen',
    '1× 实时': '1× real time',
    '24 小时': '24-hour',
    '2D 平面': '2D',
    '3D 立体': '3D',
    '±50 年': '±50 yr',
    '← 太阳光': '← Sunlight',
    '上(北)面': 'upper (north) face',
    '下(南)面': 'lower (south) face',
    '东北 NE': 'NE',
    '东南 SE': 'SE',
    '中心食时长': 'Central dur.',
    '亮在上/下': 'lit top/bottom',
    '保存为文本': 'Save as text',
    '全选 24': 'All 24',
    '初亏 C1': 'C1',
    '初亏 U1': 'U1',
    '北面/上面': 'north/upper face',
    '南面/下面': 'south/lower face',
    '地 平 面': 'Horizon plane',
    '地平遮光镜': 'Horizon shades',
    '地平镜滤片': 'Horizon shades',
    '垂直朝南晷': 'Vertical south dial',
    '复圆 C4': 'C4',
    '复圆 U4': 'U4',
    '天北极朝上': 'North celestial pole up',
    '太阳与光线': 'Sun and ray',
    '夹钳 松开': 'Clamp released',
    '夹钳 锁紧': 'Clamp locked',
    '尺寸分刻度': 'Chi-cun-fen scale',
    '已走过的弧': 'Arc travelled',
    '带食出/入': 'Eclipsed at rise/set',
    '指标差 ′': 'Index error ′',
    '指标镜滤片': 'Index shades',
    '放下遮光镜': 'Lower the shades',
    '日出 %s': 'Rise %s',
    '日落 %s': 'Set %s',
    '月相定向:': 'Phase orientation:',
    '望远镜/眼': 'Telescope/eye',
    '来自海平线': 'From the sea horizon',
    '生光 C3': 'C3',
    '生光 U3': 'U3',
    '行星名标注': 'Planet labels',
    '西北 NW': 'NW',
    '西南 SW': 'SW',
    '视场 %s': 'FOV %s',
    '起始日锁定': 'Start-date lock',
    '跳到该时刻': 'Go to time',
    '食既 C2': 'C2',
    '食既 U2': 'U2',
    ' 圭表规格 ': ' Gnomon & scale dimensions ',
    ' 月相成因 ': ' Phases ',
    ' 朔望周期 ': ' Cycle ',
    ' 本月月相 ': ' This month ',
    ' 此刻读数 ': ' Current readings ',
    ' 观测地点 ': ' Location ',
    ' 观测记录 ': ' Sight log ',
    ' 计算结果 ': ' Results ',
    ' 轨道展开 ': ' Orbit ',
    'AU 网格圈': 'AU grid circles',
    '±100 年': '±100 yr',
    '±500 年': '±500 yr',
    '⏹ 停并归零': '⏹ Stop & reset',
    '⚠ 遮光不足': '⚠ Not enough shade',
    '【太阳位置】': '[Sun position]',
    '【日晷读数】': '[Sundial reading]',
    '【星历】%s': '[Ephemeris] %s',
    '【晷面公式】': '[Dial formulas]',
    '一键多星演练': 'Auto multi-body drill',
    '全/环食时长': 'Tot./ann. dur.',
    '公元前%d年': '%d BCE',
    '半影始 P1': 'P1',
    '半影终 P4': 'P4',
    '可用观测不足': 'Not enough usable sights',
    '哥打京那巴鲁': 'Kota Kinabalu',
    '地平坐标网格': 'Alt-az grid',
    '地方平太阳时': 'Local mean time',
    '地面方位网格': 'Ground azimuth grid',
    '天文晨昏蒙影': 'astronomical twilight',
    '当地日期时刻': 'Local date & time',
    '当日影端轨迹': "Day's shadow-tip path",
    '按经度取时区': 'TZ from longitude',
    '日冕/贝利珠': "Corona/Baily's beads",
    '星表.csv': 'star_catalogue.csv',
    '最大食 纬度': 'Lat. at max',
    '最大食 经度': 'Long. at max',
    '月天顶点纬度': 'Sub-lunar lat.',
    '朔 (新月)': 'New Moon',
    '朔 · 新月': 'New Moon',
    '望 (满月)': 'Full Moon',
    '望 · 满月': 'Full Moon',
    '横梁 (表)': 'Crossbar (gnomon)',
    '此刻太阳位置': 'Sun position now',
    '民用晨昏蒙影': 'Civil twilight',
    '气压 hPa': 'Pressure hPa',
    '真实目镜视场': 'Real eyepiece view',
    '自动测量演示': 'Auto sight demo',
    '自动演示中…': 'Auto demo running…',
    '航海晨昏蒙影': 'Nautical twilight',
    '记录本次观测': 'Record sight',
    '载入选中的食': 'Load selected eclipse',
    '   ✓ 够长': '   ✓ long enough',
    ' 全过程动画 ': ' Whole-eclipse animation ',
    ' 日月食检索 ': ' Eclipse search ',
    ' 晷面与视图 ': ' Dial & view ',
    '±1000 年': '±1000 yr',
    '±3000 年': '±3000 yr',
    '↑ 高过日地线': '↑ above the Sun-Earth line',
    '↓ 低过日地线': '↓ below the Sun-Earth line',
    '① 放下遮光镜': '① Lower the shades',
    '⑥ 读数并记录': '⑥ Read and record',
    '⟲ 回到起始日': '⟲ Back to start date',
    '天体在地平线下': 'Body below the horizon',
    '娥眉月 (盈)': 'Waxing Crescent',
    '子 0° 定盘': 'Zi 0° fixed',
    '日期时刻 UT': 'Date & time UT',
    '时区 UTC±': 'Time zone UTC±',
    '晷面半径 cm': 'Dial radius cm',
    '曲阜 Qufu': 'Qufu',
    '本地可见的日食': 'Solar eclipses visible here',
    '本地可见的月食': 'Lunar eclipses visible here',
    '画成观星台形制': 'Draw as the Observatory',
    '自定义 %g×': 'Custom %g×',
    '表 %g cm': 'Gnomon %g cm',
    '表高 (cm)': 'Gnomon height (cm)',
    '透明半\n海平线': 'Clear half\n(horizon)',
    '镀银半\n反射像': 'Silvered half\n(reflection)',
    '随机误差 σ=': 'Random error σ=',
    '  (计算失败)': '  (calculation failed)',
    '  全过程 %s': '  Whole eclipse lasts %s',
    ' ⑦ 解出经纬度': ' ⑦ Solve for latitude and longitude',
    ' 此刻各星位置 ': ' Body positions now ',
    '%d分%02d秒': '%dm %02ds',
    '%s 中天 %s': '%s, transit %s',
    '%s%d寸%d分': '%s%d cun %d fen',
    '(本月内未出现)': '(does not occur in this lunation)',
    '(负数=公元前)': '(negative = BCE)',
    '0.2× (慢)': '0.2× (slow)',
    'DR ← 真位置': 'DR ← true position',
    'cm  (公制)': 'cm  (metric)',
    '— (未入本影)': '— (not in umbra)',
    '丑时 01–03': 'Chou hour 01–03',
    '东京 Tokyo': 'Tokyo',
    '中英文 (预设)': 'Chinese–English (default)',
    '亥时 21–23': 'Hai hour 21–23',
    '传统(午含中天)': 'Traditional (Wu contains transit)',
    '侧面图 竖向放大': 'Side view vertical exaggeration',
    '北 N 子 0°': 'N Zi 0°',
    '北臂需 ≥ %s': 'North arm needs ≥ %s',
    '午时 11–13': 'Wu hour 11–13',
    '半影 (模糊带)': 'Penumbra (blur band)',
    '南臂需 ≥ %s': 'South arm needs ≥ %s',
    '卯时 05–07': 'Mao hour 05–07',
    '参数有误: %s': 'Invalid parameters: %s',
    '地平镜(半镀银)': 'Horizon mirror (half-silvered)',
    '子 · 北 0°': 'Zi · N 0°',
    '子时 23–01': 'Zi hour 23–01',
    '寅时 03–05': 'Yin hour 03–05',
    '左右摆动取最低点': 'Rock for the lowest point',
    '巳时 09–11': 'Si hour 09–11',
    '常用 30 cm': 'Typical 30 cm',
    '庭园 60 cm': 'Garden 60 cm',
    '戌时 19–21': 'Xu hour 19–21',
    '拉萨 Lhasa': 'Lhasa',
    '按纬度自动定圭长': 'Fit arms to latitude',
    '按纬度自动选晷面': 'Auto-pick dial by latitude',
    '星历出错: %s': 'Ephemeris error: %s',
    '显示太阳日行轨迹': "Show Sun's daily path",
    '望远镜对平海平线': 'Aim telescope at sea horizon',
    '未时 13–15': 'Wei hour 13–15',
    '桌面 15 cm': 'Desk 15 cm',
    '武汉 Wuhan': 'Wuhan',
    '残月 (亏娥眉)': 'Waning Crescent',
    '残月 (蛾眉月)': 'Waning Crescent',
    '济南 Jinan': 'Jinan',
    '申时 15–17': 'Shen hour 15–17',
    '织女一 Vega': 'Vega',
    '绘制出错: %s': 'Drawing error: %s',
    '袖珍 10 cm': 'Pocket 10 cm',
    "西安 Xi'an": "Xi'an",
    '观测时刻 UTC': 'Sight time UTC',
    '辰时 07–09': 'Chen hour 07–09',
    '适配 22 AU': 'Fit 22 AU',
    '酉时 17–19': 'You hour 17–19',
    '镜面在左(反装)': 'Mirror on left (reversed)',
    '  %s持续 %s': '  %s phase lasts %s',
    '  偏食持续 %s': '  Partial phase lasts %s',
    '  全食持续 %s': '  Total phase lasts %s',
    '  当地钟表 %s': '  Local clock %s',
    '  真太阳时 %s': '  Apparent solar time %s',
    ' 日期 · 时刻 ': ' Date · Time ',
    ' 显示 · 视图 ': ' Display · view ',
    '↑ 天体在视场上方': '↑ Above the field',
    '↓ 天体在视场下方': '↓ Below the field',
    '七曜 (日月五星)': 'Sun, Moon & 5 planets',
    '东 E 卯 90°': 'E Mao 90°',
    '伦敦 London': 'London',
    '北极星 · 南十字': 'Polaris · Southern Cross',
    '十字架五 εCru': 'εCru',
    '十字架四 Imai': 'Imai',
    '参宿七 Rigel': 'Rigel',
    '只用公制 (cm)': 'Metric only (cm)',
    '台北 Taipei': 'Taipei',
    '天津四 Deneb': 'Deneb',
    '天狼 Sirius': 'Sirius',
    '娥眉月 (蛾眉月)': 'Waxing Crescent',
    '安阳 Anyang': 'Anyang',
    '广场 150 cm': 'Plaza 150 cm',
    '悉尼 Sydney': 'Sydney',
    '无影 (太阳未升)': '— no shadow (Sun not up)',
    '无法启用高精度星历': 'Cannot enable the high-precision ephemeris',
    '月亮 (示意放大)': 'Moon (schematic, enlarged)',
    '月龄 %.2f 日': 'Moon age %.2f d',
    '标准时 (按时区)': 'Standard time (by time zone)',
    '残月 (亏娥眉月)': 'Waning Crescent',
    '真太阳时 (日晷)': 'Apparent solar time (sundial)',
    '纬度 φ (N+)': 'Latitude φ (N+)',
    '经度 λ (E+)': 'Longitude λ (E+)',
    '观测记录已清空。\n': 'Sight log cleared.\n',
    '角宿一 Spica': 'Spica',
    '请检查年月日时分。': 'Please check the year, month, day, hour and minute.',
    '赤道·东经101°': 'Equator · 101°E',
    '起始日 UT %s': 'Start date UT %s',
    '食甚可见·带食出没': 'Max visible · eclipsed at rise/set',
    '马腹一 Hadar': 'Hadar',
    '   ← 在地平线下': '   ← below the horizon',
    '  八刻的钟表时刻:': '  Clock times of the 8 ke:',
    '%s   公历 %s': '%s   Gregorian %s',
    '1 日/秒 (预设)': '1 day/s (default)',
    '∞ (正午太阳不升)': '∞ (Sun not up at noon)',
    '② 望远镜对平海平线': '② Aim telescope at sea horizon',
    '⑤ 左右摆动取最低点': '⑤ Rock for the lowest point',
    '【刻】真太阳时 %s': '[Ke] apparent solar time %s',
    '【第七页】位置线交会': '[Page 7] Intersection of the lines of position',
    '世界时 UTC %s': 'UTC %s',
    '偏差 %s (%s)': 'Off by %s (%s)',
    '北京 Beijing': 'Beijing',
    '北极二 Kochab': 'Kochab',
    '北极圈 66.5°N': 'Arctic Circle 66.5°N',
    '北河三 Pollux': 'Pollux',
    '十字架二 Acrux': 'Acrux',
    '午 · 南 180°': 'Wu · S 180°',
    '南 S 午 180°': 'S Wu 180°',
    '南京 Nanjing': 'Nanjing',
    '启用 JPL 星历?': 'Enable JPL ephemeris?',
    '哈尔滨 Harbin': 'Harbin',
    '唐尺 24.5 cm': 'Tang chi 24.5 cm',
    '地平线下轨迹(虚线)': 'Tracks below horizon (dashed)',
    '地球半影 %.3f°': "Earth's penumbra %.3f°",
    '地球本影 %.3f°': "Earth's umbra %.3f°",
    '天津 Tianjin': 'Tianjin',
    '微动螺旋 %.1f′': 'Micrometer drum\n%.1f′',
    '成都 Chengdu': 'Chengdu',
    '推测位置 DR  φ': 'DR position  φ',
    '日出/日落/中天标注': 'Rise/set/transit labels',
    '昆明 Kunming': 'Kunming',
    '汉尺 23.1 cm': 'Han chi 23.1 cm',
    '河鼓二 Altair': 'Altair',
    '洛阳 Luoyang': 'Luoyang',
    '老人 Canopus': 'Canopus',
    '自定义 Custom': 'Custom location',
    '自行填写表高与圭长。': 'Enter the gnomon height and scale lengths yourself.',
    '西 W 酉 270°': 'W You 270°',
    '轨道线 (一整周期)': 'Orbit lines (one full period)',
    '零一二三四五六七八九': '0123456789',
    '青岛 Qingdao': 'Qingdao',
    '    第%d刻 %s': '    Ke %d  %s',
    '  ← 可以用中天法!': '  ← meridian method can be used!',
    '  对应真太阳时 %s': '  Corresponds to apparent solar time %s',
    '%s%d尺%d寸%d分': '%s%d chi %d cun %d fen',
    'AU (横向真实比例)': 'AU (horizontal, true scale)',
    '【%s时】起算: %s': '[%s shichen] reckoning: %s',
    '【晷面与晷针实际尺寸】': '[Actual size of dial and style]',
    '上海 Shanghai': 'Shanghai',
    '中天起午 (你的用法)': 'Wu begins at transit (your convention)',
    '乌鲁木齐 Urumqi': 'Urumqi',
    '五车二 Capella': 'Capella',
    '北极星 Polaris': 'Polaris',
    '十字架一 Gacrux': 'Gacrux',
    '十字架三 Mimosa': 'Mimosa',
    '南河三 Procyon': 'Procyon',
    '大角 Arcturus': 'Arcturus',
    '天顶朝上 (实际所见)': 'Zenith up (as seen)',
    '太阳中天即 12:00': "12:00 at the Sun's transit",
    '夹紧 · 微动螺旋细调': 'Clamp · fine-tune with micrometer drum',
    '心宿二 Antares': 'Antares',
    '显示珠影(nodus)': 'Show nodus shadow',
    '松开夹钳 · 转臂粗调': 'Unclamp · swing arm (coarse)',
    '沈阳 Shenyang': 'Shenyang',
    '登封·告成 周公测景台': "Gaocheng, Dengfeng – Duke of Zhou's Shadow Platform",
    '等待输入…  (%s)': 'Waiting for input…  (%s)',
    '纽约 New York': 'New York',
    '航海历已保存到:\n%s': 'Nautical Almanac saved to:\n%s',
    '设为起始日 (并停住)': 'Set as start date (and stop)',
    '雅加达 Jakarta': 'Jakarta',
    '  中天高度 %.3f°': '  Transit altitude %.3f°',
    '  昼长 %.3f 小时': '  Day length %.3f h',
    '  视赤纬 δ = %s': '  Apparent Dec δ       = %s',
    '  视赤经 α = %s': '  Apparent RA α        = %s',
    '  食甚      %s': '  Max %s',
    ' (原地点看不到这次食)': ' (this eclipse is not visible from the original site)',
    ' 时刻 (当地标准时) ': ' Time (local standard time) ',
    '【时辰】起算方式: %s': '[Shichen] reckoning: %s',
    '元尺 24.525 cm': 'Yuan chi 24.525 cm',
    '其余亮星 (点开才显示)': 'Other bright stars (shown only when ticked)',
    '十二宫 / 24 节气环': 'Twelve palaces / 24 solar terms ring',
    '天球定向 (北天极朝上)': 'Celestial (north up)',
    '尺 (1尺=%g cm)': 'chi (1 chi = %g cm)',
    '广州 Guangzhou': 'Guangzhou',
    '指标镜 (转 Hs/2)': 'Index mirror (turns Hs/2)',
    '按本地经度, 不含均时差': 'from local longitude, without the equation of time',
    '摆动演示 (swing)': 'Rocking demo (swing)',
    '水委一 Achernar': 'Achernar',
    '清营造尺 32.0 cm': "Qing builder's chi 32.0 cm",
    '绘制出错: %s: %s': 'Drawing error: %s: %s',
    '轩辕十四 Regulus': 'Regulus',
    '郑州 Zhengzhou': 'Zhengzhou',
    '重庆 Chongqing': 'Chongqing',
    '香港 Hong Kong': 'Hong Kong',
    '  下次朔      %s': '  Next New Moon  %s',
    '  世界时 UTC  %s': '  UTC                  %s',
    '  望 (满月)   %s': '  Full Moon      %s',
    '  杆影长/杆高 = %s': '  Rod shadow/height    = %s',
    '  食甚       %s': '  Max %s',
    ' 圭的方位 (按此纬度) ': ' Scale orientation (for this latitude) ',
    ' 此刻 日 / 月 位置 ': ' Sun / Moon positions now ',
    '%d时%02d分%02d秒': '%dh %02dm %02ds',
    '★ 本日 %s 进入 %s': '★ At %s this day the Moon enters %s',
    '【真太阳时刻度】%s:00': '[Apparent solar time mark] %s:00',
    '一键回正 (面向北看地面)': 'Reset view (face north, ground in view)',
    '下一相位: %s   %s': 'Next phase: %s   %s',
    '今市尺 33.333 cm': 'Modern market chi 33.333 cm',
    '地平镜 (半镀银, 固定)': 'Horizon mirror (half-silvered, fixed)',
    '已有检索在跑, 请先停止。': 'A search is already running; please stop it first.',
    '已翻下 %d 片指标遮光镜': '%d index shade(s) lowered',
    '放大日月行星(便于看月相)': 'Enlarge Sun, Moon & planets',
    '新加坡 Singapore': 'Singapore',
    '毕宿五 Aldebaran': 'Aldebaran',
    '自定义: 真实 1 秒 =': 'Custom: 1 real second =',
    '赤道晷自动转到有影子的一面': 'Equatorial dial: auto-turn to the face with the shadow',
    '选中 %s 时出错: %s': 'Error while selecting %s: %s',
    '  上弦        %s': '  First Quarter  %s',
    '  下弦        %s': '  Last Quarter   %s',
    '  属 %s时 第 %d 刻': '  In %s shichen, ke %d',
    '  晷面形状      %s': '  Plate shape     %s',
    '  月相        %s': '  Phase          %s',
    ' 观测地点 (任一经纬度) ': ' Location (any latitude/longitude) ',
    '%Y 年 %m 月 %d 日': '%Y-%m-%d',
    '(方位说明计算出错: %s)': '(Error computing the orientation notes: %s)',
    '北落师门 Fomalhaut': 'Fomalhaut',
    '南门二 Rigil Kent': 'Rigil Kent',
    '参宿四 Betelgeuse': 'Betelgeuse',
    '圆盘, 直径 %.1f cm': 'disc, diameter %.1f cm',
    '按「刷新」生成本日航海历。\n': 'Press "Refresh" to generate the Nautical Almanac for this day.\n',
    '格林尼治 Greenwich': 'Greenwich',
    '槟城 George Town': 'George Town',
    '此刻影 %.1f° · %s': 'Shadow now %.1f° · %s',
    '水平晷 Horizontal': 'Horizontal dial',
    '界面语言 Language:': 'Language:',
    '赤道晷 Equatorial': 'Equatorial dial',
    '  儒略日 JD   %.6f': '  Julian Day (JD)      %.6f',
    '  观测 %d  %s  %s': '  Sight %d  %s  %s',
    '  轨 道  Orbits  ': '  Orbits  ',
    ' 时间 (默认随真实时间走) ': ' Time (follows real time by default) ',
    '【今日月出中天月落 (当地)】': "[Today's moonrise, transit and moonset (local)]",
    '两束光夹角 = Hs = %s': 'Angle between the rays = Hs = %s',
    '偏离圭轴 %s —— 不在圭上': 'off the scale axis by %s — not on the scale',
    '太阳在地平线以下 —— 无日影': 'Sun below the horizon — no shadow',
    '已关严格模拟: 所有按钮都能用': 'Strict simulation off: all buttons available',
    '指标遮光镜 (点击翻下/翻起)': 'Index shades (click to flip)',
    '观测者所见 (含南北半球翻转)': 'As seen (hemisphere flip)',
    '遮光合适 — 盘面边缘清晰锐利': 'Shading OK — the limb is crisp and sharp',
    '🔒 夹钳: 夹紧 (点此松开)': '🔒 Clamp: locked (click to release)',
    '🔓 夹钳: 松开 (点此夹紧)': '🔓 Clamp: released (click to lock)',
    '  六分仪  Sextant  ': '  Sextant  ',
    '  日 晷  Sundial  ': '  Sundial  ',
    '  星空 · 月相  Sky  ': '  Sky · Moon Phase  ',
    ' ⑧ 两个特例 (不必解方程组)': ' ⑧ Two special cases (no simultaneous equations needed)',
    '%s   (当地 UTC%+g)': '%s   (local UTC%+g)',
    '④ 夹紧 · 微动螺旋切于海平线': '④ Clamp · fine-tune limb onto horizon',
    '【当日太阳时刻 · 当地标准时】': "[Today's Sun times · local standard time]",
    '全球日食 (列出最大食点经纬度)': 'Global solar eclipses (lists lat/long of greatest eclipse)',
    '吉隆坡 Kuala Lumpur': 'Kuala Lumpur',
    '垂直朝南晷面 (自南向北看墙面)': 'Vertical south dial (looking north at the wall)',
    '应读 %s  (%s · %s)': 'Should read %s  (%s · %s)',
    '晷面制作规格 Dial Spec': 'Dial construction spec',
    '自动演示结束 — 已记录本次观测': 'Auto demo finished — sight recorded',
    '至少需要 2 次不同方位的观测。': 'At least 2 sights at different azimuths are needed.',
    '   ← 在地平线下, 此地看不到': '   ← below the horizon, not visible here',
    '  (= GHA白羊 + SHA)': '  (= GHA Aries + SHA)',
    '  真高度 h  = %+.4f°': '  True altitude h      = %+.4f°',
    ' —— 取消上面的勾选可留在原地点': ' — untick the option above to stay at the original site',
    ' 日期 · 时刻 (当地标准时) ': ' Date · time (local standard time) ',
    ' 观测者真实位置 (模拟视场用) ': " Observer's true position (for simulating the view) ",
    '③ 松开夹钳 · 转臂把天体带下来': '③ Unclamp · swing arm to bring body down',
    '【钟表刻度】当地标准时 %s:00': '[Clock mark] local standard time %s:00',
    '中 · 传统八尺表 (周公测景台)': "Medium · Traditional 8-chi gnomon (Duke of Zhou's platform)",
    '传统 (午时含中天, 子时跨半夜)': 'Traditional (Wu contains transit, Zi spans midnight)',
    '全球检索时自动把观测点移到最大食点': 'On global search, move the observer to greatest eclipse',
    '双反射原理 (光路随指标臂一起转)': 'Double reflection: the light path turns with the index arm',
    '太暗 — 天体看不见了, 翻起一片': 'Too dark — body invisible, raise one shade',
    '夹钳已夹紧 — 现在用微动螺旋细调': 'Clamp locked — now fine-tune with the micrometer drum',
    '夹钳已松开 — 指标臂可以自由滑动': 'Clamp released — the index arm slides freely',
    '左=东(上午)   右=西(下午)': 'Left = E (morning)   Right = W (afternoon)',
    '此刻 %s 太阳在地平线下, 无影': 'Now %s: Sun below the horizon, no shadow',
    '现处相位: %s   自 %s 起': 'Current phase: %s   since %s',
    '蓝 = 真太阳时 (晷面固有刻度)': "Blue = apparent solar time (the dial's own scale)",
    '  (参数有误, 暂时无法代入数值)': '  (Invalid parameters; values cannot be substituted for now)',
    '  冬至正午影最短 %s (仍朝南)': '  Shortest noon shadow (Winter Solstice): %s (still pointing south)',
    '  地方真太阳时(晷面读数)  %s': '  Local apparent time (dial reading)  %s',
    '  夏至正午影最短 %s (仍朝北)': '  Shortest noon shadow (Summer Solstice): %s (still pointing north)',
    '  斜边(晷针)长  %.2f cm': '  Hypotenuse      %.2f cm  (= the style)',
    '  晷针垂直晷面伸出 %.2f cm': '  Style projects %.2f cm perpendicular to the plate',
    '  月龄        %.3f 日': '  Moon age       %.3f d',
    '  格林时角 GHA = %.4f°': '  GHA                  = %.4f°',
    ' 时间制 (输入与图上标注都按此) ': ' Time system (used for inputs and chart labels) ',
    '%Y年%m月%d日 %H:%M:%S': '%Y-%m-%d %H:%M:%S',
    '✔ 已切于海平线   Hs = %s': '✔ Touching the horizon   Hs = %s',
    '【最后一次观测的改正明细】%s %s': '[Correction details for the last sight] %s %s',
    '今日真正午 %s  太阳不升, 无影': "Today's apparent noon %s  Sun not up, no shadow",
    '夹钳松着 — 微动螺旋空转, 先夹紧': 'Clamp released — the micrometer drum spins freely; lock the clamp first',
    '小 · 桌面手搓 (20 cm 表)': 'Small · Desktop DIY (20 cm gnomon)',
    '无法载入 de421.bsp: %s': 'Cannot load de421.bsp: %s',
    '沿公转轨道展开: 阳光一律自上方射来': 'Laid out along the orbit: sunlight always from the top',
    '距本月朔 %.3f 日 (朔 %s)': "%.3f d after this lunation's New Moon (%s)",
    ' 各条轨迹的日出 / 中天 / 日落 ': ' Sunrise / transit / sunset of each track ',
    '也画出「所选日期」当天的轨迹 (白色)': 'Also draw the track of the "selected date" (white)',
    '在圭面上标出全年 24 节气的正午影端': 'Mark the noon shadow tips of all 24 solar terms on the scale',
    '太亮 — 边缘发糊切不准, 再翻下一片': 'Too bright — limb blurred, lower one more shade',
    '太阳 h=%.1f° Az=%.1f°': 'Sun h=%.1f° Az=%.1f°',
    '太阳在地平线下 (或过低), 无日影。': 'Sun below the horizon (or too low): no shadow.',
    '显示刻 (15 分一刻, 一时辰八刻)': 'Show ke (1 ke = 15 min, 8 ke per shichen)',
    '月绕地公转 → 日月夹角变化 → 月相': 'Moon orbits Earth → Sun–Moon angle changes → phase',
    '画满 24 时线 (极地/极昼时有用)': 'Draw all 24 hour lines (useful near the poles / in polar day)',
    '该纬度冬季正午太阳不升, 北臂影长无限': 'At this latitude the noon Sun stays below the horizon in northern winter; the north-arm shadow is infinite',
    '该纬度夏季正午太阳不升, 南臂影长无限': 'At this latitude the noon Sun stays below the horizon in northern summer; the south-arm shadow is infinite',
    '  土 圭 · 圭表  Gnomon  ': '  Gnomon (Tugui)  ',
    '  均时差 EoT  = %+.2f 分': '  Equation of time (EoT) = %+.2f min',
    '  日食 · 月食  Eclipse  ': '  Solar & Lunar Eclipses  ',
    '  晷针仰角 = |φ| = %.4f°': '  Style elevation = |φ| = %.4f°',
    ' · 时区已按该地经度改为 UTC%+g': " · time zone set to UTC%+g from the site's longitude",
    ' ① 读数改正 (仪器与大气的误差矫正)': ' ① Reading corrections (instrument and atmospheric errors)',
    '%s  %+.2f°  转指标臂到 %s': '%s  %+.2f°  → set the arm to %s',
    '③ 侧 面 图  以当时日地连线为水平轴': '③ Side view  current Sun-Earth line as horizontal axis',
    '【第二页】白羊宫(春分点)与四颗航海行星': '[Page 2] Aries (vernal equinox) and the four navigational planets',
    '哥打京那巴鲁 Kota Kinabalu': 'Kota Kinabalu',
    '垂直朝南晷 Vertical South': 'Vertical south dial',
    '大 · 登封观星台 (郭守敬 1276)': 'Large · Dengfeng Observatory (Guo Shoujing, 1276)',
    '此刻被照亮 %.2f%%   农历 %s': 'Illuminated %.2f%% at that moment   lunar date %s',
    '该天体在地平线以下 (h′=%.2f°)': 'This body is below the horizon (h′=%.2f°)',
    '  杆长          %.2f cm': '  Rod length      %.2f cm',
    ' ⑥ 位置线方程 (每一次观测给一条直线)': ' ⑥ Line-of-position equation (each sight gives one straight line)',
    '② 等距示意  轨道等间距, 只看相对方位': '② Equal spacing  orbits evenly spaced, relative directions only',
    '使用 Skyfield/JPL 高精度星历': 'Use Skyfield/JPL high-precision ephemeris',
    '公元前 %d 年 %02d-%02d %s': '%d BCE %02d-%02d %s',
    '夹钳还夹着 — 先松开夹钳才能转指标臂粗调': 'Clamp still locked — release it before swinging the index arm (coarse)',
    '尚未载入任何食 —— 检索后双击一行载入。': 'No eclipse loaded yet — run a search, then double-click a row to load one.',
    '接近二分点: 阳光近乎平行盘面, 影线消失': 'Near an equinox: sunlight almost parallel to the plate, shadow line vanishes',
    '黄道面 · 太阳—地球连线 (z = 0)': 'Ecliptic plane · Sun—Earth line (z = 0)',
    '  (橙色刻度按今日均时差画, 每天会略移)': "  (orange marks follow today's EoT and shift slightly each day)",
    '  (点一下钉住/取消; 空白处点一下取消)': '  (click to pin/unpin; click empty space to clear)',
    '  地方平太阳时            %s': '  Local mean time                     %s',
    ' ③ 等高圆 —— 一次观测能给出的全部信息': ' ③ Circle of equal altitude — all the information a single sight can give',
    ' 时间 (当地标准时, 默认随真实时间走) ': ' Time (local standard time; follows real time by default) ',
    ' 检索结果 (双击一行 = 载入并可动画) ': ' Results (double-click a row = load and animate) ',
    '北回归线以北 → 全年正午影朝北, 只需北臂': 'North of the Tropic of Cancer → the noon shadow points north all year; only the north arm is needed',
    '南回归线以南 → 全年正午影朝南, 只需南臂': 'South of the Tropic of Capricorn → the noon shadow points south all year; only the south arm is needed',
    '夹钳还夹着 — 指标臂动不了, 先点夹钳松开': "Clamp still locked — the index arm can't move; click the clamp to release it first",
    '晷针与墙面夹角 = %.2f° (指向天极)': 'Style-to-wall angle = %.2f° (pointing at the celestial pole)',
    '本轮朔望月的 %s   (视黄经差 %d°)': '%s of this lunation   (elongation %d°)',
    '真实位置  φ = %s    λ = %s': 'True pos. φ = %s    λ = %s',
    '观测船位  φ = %s    λ = %s': 'Fix       φ = %s    λ = %s',
    '该天体此刻不在地平线上, 换一个天体或时刻。': 'This body is not above the horizon at the moment; choose another body or time.',
    '请填大于 0 的数 (星图日 / 真实秒)。': 'Please enter a number greater than 0 (simulated days per real second).',
    '  当地标准时  %s  (UTC%+.2f)': '  Local standard time  %s  (UTC%+.2f)',
    '  日出 %s   中天 %s   日落 %s': '  Sunrise %s   Transit %s   Sunset %s',
    '  月出 %s   中天 %s   月落 %s': '  Moonrise %s   transit %s   moonset %s',
    ' 24 节气 (勾选即画该日轨迹, 可多选) ': " 24 solar terms (tick to draw that day's track; multiple allowed) ",
    ' ⑨ 经度与时间的关系 —— 为什么钟一定要准': ' ⑨ Longitude and time — why the clock must be accurate',
    '※ 已把观测地点移到「最大食点」%s %s%s': '※ Observer moved to the "greatest eclipse" point %s %s%s',
    '【本朔望月 (当地标准时 UTC%+.1f)】': '[This lunation (local standard time UTC%+.1f)]',
    '恒星: 内置 %d 颗 + %s 共 %d 颗': 'Stars: %d built-in + %s = %d in total',
    '此刻太阳赤纬 δ=%+.2f° → 光照 %s': "Sun's declination now δ=%+.2f° → lights the %s",
    '此刻阳光照不到朝南墙面 (太阳在北侧或已落下)': 'Sunlight does not reach the south-facing wall now (Sun is to the north or has set)',
    '   相位角 %.2f°  被照亮 %.2f%%': '   Phase angle %.2f°  illuminated %.2f%%',
    '  (圭只接正午影; 其余时刻影本来就斜出圭外)': '  (The scale only catches the noon shadow; at other times the shadow naturally slants off the scale)',
    '  公式: tanθ = cosφ · tanH': '  Formula: tanθ = cosφ · tanH',
    '  真实位置   φ = %s   λ = %s': '  True pos.  φ = %s   λ = %s',
    '  观测船位   φ = %s   λ = %s': '  Fix        φ = %s   λ = %s',
    ' ⑤ 截距 (Marcq St Hilaire)': ' ⑤ Intercept (Marcq St Hilaire)',
    ' 缩 放 (滚轮 / 拖动平移 / 双击适配) ': ' Zoom (mouse wheel / drag to pan / double-click to fit) ',
    ' 该年 24 节气正午影长 (点一行可跳过去) ': ' Noon shadow on the 24 solar terms (click a row to jump there) ',
    '%s   本影食分 %s   半影食分 %.4f': '%s   umbral mag. %s   penumbral mag. %.4f',
    '【选中】%s%s      (点空白处取消选择)': '[Selected] %s%s      (click empty sky to deselect)',
    '今日真正午 %s  日中无影 (h %.2f°)': "Today's apparent noon %s  shadowless noon (h %.2f°)",
    '公历 %s   (当地标准时 UTC%+.1f)': 'Gregorian %s   (local standard time UTC%+.1f)',
    '各天体方位太接近, 位置线近乎平行, 无法定位。': 'Azimuths of the bodies are too close: lines of position nearly parallel, no fix possible.',
    '夹钳松着 — 微动螺旋不咬合齿弧, 先夹紧再细调': 'Clamp released — the micrometer drum does not engage the rack; lock it first, then fine-tune',
    '      用已记录的 %d 次观测最小二乘解得:': '      Least-squares solution from the %d recorded sights:',
    '     180° = 望, 日落月出, 通宵可见': '     180° = Full Moon: rises at sunset, visible all night',
    '  垂直朝南晷: tanθ = cosφ·tanH': '  Vertical south dial: tanθ = cosφ·tanH',
    '  方位角 Az = %.3f°  (北起顺时针)': '  Azimuth Az           = %.3f°  (from N, clockwise)',
    '  朔 (新月)   %s      ← 定为初一': '  New Moon       %s   ← counted as lunar day 1',
    '  水平晷时线: tanθ = sinφ·tanH': '  Horizontal dial hour lines: tanθ = sinφ·tanH',
    ' 24 节气快捷 (点一下 = 跳到该日真正午) ': " 24 solar terms (click = jump to that day's apparent noon) ",
    ' 六分仪读数 Hs (也可直接拖动左边的指标臂) ': ' Sextant reading Hs (or drag the index arm on the left) ',
    ' 定 盘 (子 0° 在哪里 = 我的观测视角) ': ' Chart orientation (where Zi 0° sits = my viewpoint) ',
    '已启用 Skyfield / DE421 (%s)': 'Skyfield / DE421 enabled (%s)',
    '按住左键拖动改变视角, 松开即固定; 滚轮缩放视场': 'Left-drag to change the view, release to fix it; mouse wheel zooms the field of view',
    '本朔望月全套月相 (共 %d 天, 各日当地正午)': "This lunation's phases (%d days, each at local noon)",
    '橙 = 当地标准时 (按今日均时差画, 每天略移)': "Orange = local standard time (drawn with today's EoT; shifts slightly each day)",
    '矩形, 宽 %.1f cm × 高 %.1f cm': 'rectangle, width %.1f cm × height %.1f cm',
    '  %d 年 正午太阳不升 (极夜, 无影): %s': '  In %d the Sun does not rise at noon (polar night, no shadow): %s',
    '  晷针形状      直角三角形 (指北的三角板)': '  Style shape     right triangle (a triangular plate pointing north)',
    ' 画 法 (三选一, 都是平面图, 不给自由三维) ': ' View mode (pick one of three; all flat 2-D, no free 3-D) ',
    '两回归线之间 → 正午影一年两度南北易向, 圭须双臂': 'Between the tropics → the noon shadow swaps between north and south twice a year; the scale needs both arms',
    '已启用 Skyfield / DE421 高精度星历': 'Skyfield / DE421 high-precision ephemeris enabled',
    '影端方位 %.2f° (%s)   偏离子午线 %s': 'Shadow-tip azimuth %.2f° (%s)   off the meridian by %s',
    '日期 2026-08-30, 时刻 21:30:00': 'Enter date as 2026-08-30 and time as 21:30:00',
    '  今日 12 时辰 ↔ 当地标准时 (钟表) 对照:': "  Today's 12 shichen ↔ local standard time (clock):",
    '  太阳视运动 · 24节气  Sun Track  ': '  Sun Track · 24 Solar Terms  ',
    '  当地钟表 %s   ← 晷影指到这条线时手表的读数': '  Local clock %s   ← what a watch reads when the shadow is on this line',
    '  推测位置 DR:  φ = %s   λ = %s': '  DR position:  φ = %s   λ = %s',
    '  时线角度表 (θ 自子午线量起, 正值向下午一侧)': '  Hour-line angle table (θ measured from the meridian, positive toward the afternoon side)',
    '  晷针形状      自墙面伸出的斜杆 (指向天极)': '  Style shape     slanted rod projecting from the wall (pointing at the celestial pole)',
    '  此刻 %s时 第 %d 刻   (真太阳时 %s)': '  Now: %s shichen, ke %d   (apparent solar time %s)',
    '  此刻晷面无影 (太阳在地平下, 或阳光照在另一面)': '  No shadow on the dial now (Sun below the horizon, or lighting the other face)',
    '  赤道晷时线: θ = H (每小时 15° 均匀)': '  Equatorial dial hour lines: θ = H (uniform, 15° per hour)',
    '⚠ 危险! 遮光片不足, 真船上这样直视太阳会灼伤眼睛': '⚠ Danger! Too few shades — on a real ship this would burn your eyes',
    '单次最多 6200 年 (约 76000 个朔望月)。': 'At most 6200 years per search (about 76000 lunations).',
    '圭轴方位 = 当地子午线 (真南北线), 与纬度无关:': 'Scale axis azimuth = local meridian (true north-south line), independent of latitude:',
    '状态 %s   食分 %.4f   遮蔽 %.2f%%': 'Status: %s   magnitude %.4f   obscuration %.2f%%',
    '     270° = 下弦, 后半夜升起, 清晨在正南': '     270° = Last Quarter: rises ~midnight, S at dawn',
    '  日中无影 (太阳过天顶): %s   残影 ≤ %s': '  Shadowless noon (Sun at zenith): %s   residual shadow ≤ %s',
    '  晷面半径 %.1f cm      推荐晷面: %s': '  Dial radius %.1f cm      Recommended: %s',
    '  月相只取决于日月的黄经差 (elongation):': '  The phase depends only on the elongation (Moon−Sun Δλ):',
    '  杆与墙面夹角  %.4f°  = 90° − |φ|': '  Rod-wall angle  %.4f°  = 90° − |φ|',
    '  视黄经 λ = %s      视黄纬 β = %s': '  Apparent ecliptic longitude λ = %s      latitude β = %s',
    ' 遮光镜 Shades · 夹钳 Clamp · 目镜 ': ' Shades · Clamp · Eyepiece ',
    '【太阳】高度 %+.3f°  方位 %.2f°   %s': '[Sun]   Alt %+.3f°  Az %.2f°   %s',
    '中天起午 (太阳中天=午时之始, 底天=子时之始/日始)': "Wu begins at transit (Sun's transit = start of Wu, lower transit = start of Zi / start of the day)",
    '地球走满一周期 (365.2564 日) 自动回到起始日': 'Return to start date automatically after one full Earth period (365.2564 d)',
    '天球定向: 北天极朝上, 天东在左; 点任一天可跳到那天': 'Celestial: north up, east left; click a day to jump to it',
    '已记录 %d 次观测, 至少需要 2 次(方位不同)。\n': '%d sight(s) recorded; at least 2 are needed (at different azimuths).\n',
    '此刻 %s 影 → %.2f° (%s)  %s, %s': 'Now %s: shadow → %.2f° (%s)  %s, %s',
    '请用 2026-08-30 08:20:00 这样的格式': 'Please use a format like 2026-08-30 08:20:00',
    '     0°   = 朔, 月在日地之间, 背光面朝我们': '     0°   = New Moon: Moon between Sun & Earth, unlit side to us',
    '  ── 观测 %d: %s (%s)  UT %s ──': '  ── Sight %d: %s (%s)  UT %s ──',
    '  三角形高      %.2f cm  (北端垂直立起)': '  Triangle height %.2f cm  (vertical edge at the north end)',
    '  晷针仰角      %.4f°  = 当地纬度 |φ|': '  Style angle     %.4f°  = local latitude |φ|',
    '  月地距离    %.1f km   视半径 %.3f′': '  Distance       %.1f km   SD %.3f′',
    '  杆长          每面露出 %.2f cm 即可': '  Rod length      %.2f cm protruding from each face is enough',
    'Skyfield + JPL DE421 星历 (角秒级)': 'Skyfield + JPL DE421 ephemeris (arcsecond accuracy)',
    '① 实际距离  上下左右各 11 AU (共 22 AU)': '① True distances  11 AU each way (22 AU across)',
    '中纬度 |φ|=%.1f°: 水平晷时线张得开, 也最常见': "Mid-latitude |φ|=%.1f°: a horizontal dial's hour lines spread out well, and it is the most common type",
    '全球: %s   γ %+.4f   最大食点 %s %s': 'Global: %s   γ %+.4f   greatest eclipse %s %s',
    '地球恒钉: 地球永远停在 θ 处, 其余星体与盘每天绕着转': 'Earth pinned at θ; the chart turns around it every day',
    '太阳 高度 %+.3f°  方位 %.2f° (%s)%s': 'Sun: Alt %+.3f°  Az %.2f° (%s)%s',
    '影长 (自表北面起): %s     圭上读数 %s %s': 'Shadow length (N face): %s     scale reading %s %s',
    '           尺寸分: %s     圭上读数 %s': '           chi-cun-fen: %s     scale reading %s',
    '       本影带宽 %.0f km   中心食最长 %s': '       path width %.0f km   max central duration %s',
    '  地方时角 LHA = %+.4f°  (%+.3f h)': '  LHA                  = %+.4f°  (%+.3f h)',
    '  当地钟表  %s → %s   ← 实际进出该时辰的时刻': '  Local clock  %s → %s   ← when this shichen actually begins and ends',
    '  晷针形状      垂直穿过盘心的细杆 (两面都要露出)': '  Style shape     thin rod through the plate centre, perpendicular to it (must protrude from both faces)',
    '  视半径 SD = %.2f′   日地距 %.6f AU': '  Semidiameter SD      = %.2f′   distance %.6f AU',
    ' 这里就会列出每一次观测从读数 Hs 到经纬度的完整算法。)': ' and every sight will be worked here in full, from the reading Hs to latitude and longitude.)',
    '(自受照面俯视: 正午影线朝下, 上午在右侧, 下午在左侧)': '(Looking down on the lit face: noon shadow points down, morning on the right, afternoon on the left)',
    '太阳一天里高度几乎不变, 没有「正午影」, 圭表在此不能用。': 'the Sun\'s altitude barely changes during the day, there is no "noon shadow", and the gnomon & scale cannot be used here.',
    '屏幕上明亮边缘朝向 %.1f° (自上方顺时针) —— %s': 'Bright limb on screen: %.1f° clockwise from top — %s',
    '按住左键拖动看天, 松开固定; 滚轮缩放视场; 点天体看资料': 'Drag to look around, release to fix; wheel zooms; click for info',
    '日期请用 2026-08-30, 时刻请用 16:20:00': 'Enter the date as 2026-08-30 and the time as 16:20:00',
    '月亮 视高度 %+.3f°  方位 %.2f° (%s)%s': 'Moon: apparent alt %+.3f°  Az %.2f° (%s)%s',
    '望远镜视场 · 视场高 %.1f° · 1 像素≈%.2f′': 'Telescope field · field height %.1f° · 1 px ≈ %.2f′',
    '此刻阳光照在晷面背后 (没有晷针的那一面) —— 晷面上无影': 'Sunlight is now on the back of the dial (the side without the style) — no shadow on the dial',
    '真高度 %.4f°  视高度 %.4f°  方位 %.1f°': 'True alt %.4f°  apparent alt %.4f°  Az %.1f°',
    '航海历 Nautical Almanac · 观测归算全过程': 'Nautical Almanac · Full sight reduction',
    '      (若此刻天体正过中天, 见下面 ⑧ 可单独定纬度)': '      (If the body is on the meridian right now, see ⑧ below: latitude can be found on its own)',
    '      整点 GHA(%02dh)      = %s%s': '      GHA at %02dh         = %s%s',
    '  真太阳时  %02d:00:00 → %02d:00:00': '  Apparent solar time  %02d:00:00 → %02d:00:00',
    '  经度改正    = %+.2f 分  (λ−15°×tz)': '  Longitude correction   = %+.2f min  (λ−15°×tz)',
    '  视高度 h′ = %+.4f°   (蒙气差 %.2f′)': '  Apparent altitude h′ = %+.4f°   (refraction %.2f′)',
    'Skyfield + JPL DE421 (角秒级) · %s': 'Skyfield + JPL DE421 (arcsecond accuracy) · %s',
    '上=度 粗调  下=分 微动螺旋 (画布上滚轮 = 0.1′)': 'Top = degrees, coarse   Bottom = minutes, micrometer drum   (mouse wheel on canvas = 0.1′)',
    '低纬度(|φ|=%.1f°)水平晷时线极密集, 建议改用赤道晷': 'Low latitude (|φ|=%.1f°): horizontal dial hour lines are very dense — equatorial dial recommended',
    '等距示意图 · 轨道间距 %.0f px · 缩放 %.2f×': 'Equal-spacing diagram · orbit spacing %.0f px · zoom %.2f×',
    '  (本地只见偏食 —— 想看全/环食请把观测点移到中心食带内)': '  (Only partial here — to see the total/annular phase, move the observer into the central path)',
    '  三角形底边    %.2f cm  (沿子午线由中心向北量)': '  Triangle base   %.2f cm  (measured along the meridian from the centre northward)',
    '  月亮每天东移约 12.19°, 故每天迟约 50 分钟升起。': '  Moving ~12.19° east a day, the Moon rises ~50 min later daily.',
    '  月牙倾斜方向 —— 左边星空图里的月亮就是按 χ−q 画的。': '  gives the crescent tilt you actually see; the sky view uses χ−q.',
    '  此刻晷针影长 %.2f cm   影长/晷针高 = %.3f': '  Style shadow now %.2f cm   Shadow/style height = %.3f',
    '  珠(nodus)高 %.2f cm  珠影长 %.2f cm': '  Nodus height %.2f cm  Nodus shadow %.2f cm',
    'φ %s: 极点没有子午线 —— 四面八方都是南 (或都是北),': 'φ %s: there is no meridian at the pole — every direction is south (or north),',
    '【农历】本朔望月第 %d 天 = %s   (本月共 %d 天)': '[Lunar calendar] Day %d of this lunation = %s   (%d days this month)',
    '低纬度(|φ|=%.1f°)水平晷时线极度密集, 建议改用赤道晷': 'Low latitude (|φ|=%.1f°): horizontal dial hour lines are extremely dense — equatorial dial recommended',
    '极区 |φ|=%.1f°: 太阳可整日不落, 赤道晷绕一圈都均匀': 'Polar region |φ|=%.1f°: the Sun may stay up all day; an equatorial dial is uniform all the way round',
    '阳光几乎平行于晷面 —— 影线消失 (赤道晷在二分点前后会这样)': 'Sunlight almost parallel to the dial — shadow line vanishes (an equatorial dial does this around the equinoxes)',
    '      d = 赤纬每小时的变化;  HP = 月亮的地平视差': "      d = hourly change in declination;  HP = the Moon's horizontal parallax",
    '      v 改正 (v=%+.1f′)    = %+.2f′': '      v corr. (v=%+.1f′)  = %+.2f′',
    ' 起始日期 (当地标准时) —— 输入后画面静止, 按 ▶ 才走 ': ' Start date (local time) — chart stays still until ▶ Play ',
    '【截距法定位】 观测 %d 次   推测位置 DR: %s  %s': '[Fix by intercept method]  %d sights   DR position: %s  %s',
    '当日正午: 照亮 %.1f%%   视黄经差 %.1f°   %s': 'Local noon: illuminated %.1f%%   elongation %.1f°   %s',
    '放大 %.1f×  ·  视角 方位 %.0f° 仰角 %.0f°': 'Zoom %.1f×  ·  view azimuth %.0f°, elevation %.0f°',
    '本影食分 %s   半影食分 %.4f   月心距影心 %.4f°': 'Umbral mag. %s   penumbral mag. %.4f   Moon to shadow centre %.4f°',
    '本机没有 de421.bsp (勾选开关可联网下载约 17 MB)': 'No de421.bsp on this computer (tick the checkbox to download about 17 MB)',
    '至少需要 2 个不同方位的天体(或同一天体不同时刻)才能定出船位。': 'A fix needs at least 2 bodies at different azimuths (or the same body at different times).',
    '赤道晷 · 盘面倾角 = 余纬 %.2f°, 晷针垂直盘面指向天极': 'Equatorial dial · plate tilt = colatitude %.2f°, style perpendicular to the plate, pointing at the celestial pole',
    '起始日锁定: 起始日把地球摆到 θ 处, 之后盘不动, 地球自己走': 'Start-date lock: Earth at θ on the start date, chart then fixed',
    '高纬度 |φ|=%.1f°: 太阳终日偏低, 垂直朝南面受光角度好': 'High latitude |φ|=%.1f°: the Sun stays low all day; a vertical south-facing dial catches the light at a good angle',
    ' ④ 以推测位置 (DR) 算出「应该看到的高度」Hc 与方位 Zn': ' ④ From the DR position, compute the "altitude you should see" Hc and the azimuth Zn',
    '※ 已把观测地点移到食甚时月亮的天顶点 %s %s (该处全程可见)': '※ Observer moved to the sub-lunar point at maximum %s %s (whole eclipse visible there)',
    '上排 = 地月系统 (红圈为月亮轨道), 下方 = 在%s看到的月相': "Top: Earth–Moon (red ring = Moon's orbit) · bottom: %s view",
    '今日真正午 %s  影朝%s → %s  %s  (h %.2f°)': "Today's apparent noon %s  shadow points %s → %s  %s  (h %.2f°)",
    '镜面转 θ ⇒ 反射光转 2θ ⇒ 弧上刻度 = 2×臂角 = Hs': 'Mirror turns θ ⇒ reflected ray turns 2θ ⇒ arc scale = 2×arm angle = Hs',
    '      天顶距 z = 90° − Ho ;  1′ = 1 海里': '      Zenith distance z = 90° − Ho ;  1′ = 1 nm',
    '  今日 (%s) 12 时辰的钟表时刻 —— 逐个求根解出, 非近似': '  Today (%s): clock times of the 12 shichen — each solved by root-finding, not approximated',
    '  今日: 升 %s   中天 %s   落 %s   (当地标准时)': '  Today: rise %s   transit %s   set %s   (local standard time)',
    '  农历日      第 %d 天 = %s   (本月共 %d 天)': '  Lunar day      no. %d = %s   (%d days this month)',
    'ΔT 已由实测定出, 时刻可信到 ~1 秒, 食延时可信到 ~1 秒。': 'ΔT is fixed by observation: times reliable to ~1 s, eclipse durations to ~1 s.',
    '【第一页】太阳与月亮 (每整点的格林尼治时角 GHA 与赤纬 Dec)': '[Page 1] Sun and Moon (Greenwich hour angle GHA and declination Dec at each whole hour)',
    '【第五页】增量与改正 Increments & Corrections': '[Page 5] Increments & Corrections',
    '太阳视黄经 %.3f° → %s宫 %.3f°  (本宫自「%s」起)': 'Sun apparent longitude %.3f° → %s palace %.3f°  (this palace starts at "%s")',
    '夹钳松开中 → 可拖指标臂或按 1° 粗调; 微动螺旋要夹紧才咬合齿弧': 'Clamp released → drag the arm or use 1° steps; the drum engages only when clamped',
    '未安装 skyfield (pip install skyfield)': 'skyfield not installed (pip install skyfield)',
    '金框 = 此刻所处的位置 (%s) · 鼠标指向某相位可看它的公历时刻': 'Gold frame = now (%s) · hover over a phase for its date and time',
    '  (恒星的 SHA/Dec 一天之内几乎不变, 故航海历只给一天一组)': "  (A star's SHA/Dec barely changes within a day, so the Nautical Almanac gives one set per day)",
    '  「明亮边缘方位角 χ」加上视差角 q 之后, 才是你在天上真正看到的': '  "Bright-limb position angle χ" corrected for parallactic angle q',
    '  晷针(style)长 %.2f cm   晷针与晷面夹角 %.2f°': '  Style length %.2f cm   Style–plate angle %.2f°',
    '  表一律铅垂。随纬度倾斜的是日晷的晷针 (仰角 |φ|), 不是土圭。': "  The gnomon is always plumb. What tilts with latitude is a sundial's style (elevation |φ|), not the tugui.",
    ' ② 时刻 → 天体的星下点 GP (这一步全靠钟表, 所以钟一定要准)': " ② Time → the body's geographical position GP (this step rests entirely on the clock, so the clock must be accurate)",
    '(还没有观测记录 —— 对准天体后按「记录本次观测」或「一键多星演练」,': '(No sights recorded yet — align on a body, then press "Record sight" or "Auto multi-body drill",',
    '影长 / 表高 = %.5f     tan(90°−h) = %.5f': 'Shadow length / gnomon height = %.5f     tan(90°−h) = %.5f',
    '明亮边缘 χ %.1f° (自天北极向东量)   视差角 q %.1f°': 'Bright limb χ %.1f° (N through E)   parallactic angle q %.1f°',
    '此刻阳光照在晷面的另一面 (%s) —— 拖动视角转到那一面才看得到影子': 'Sunlight is now on the other face of the dial (%s) — drag the view round to that face to see the shadow',
    '            Ho = %s          ← 天体的真高度': '            Ho = %s          ← true altitude of the body',
    '      ⇒ 观测瞬间必须同时按秒表: 高度与时刻是成对的, 缺一不可。': '      ⇒ Press the stopwatch at the very instant of the sight: altitude and time come as a pair, and neither is any use without the other.',
    '      代入: z = 90° − %s = %s = %.1f 海里': '      Calc: z = 90° − %s = %s = %.1f nm',
    '  南臂 → 180°  需 %s  (夏至·6 月正午 h %.2f°)': '  South arm → 180°  needs %s  (Summer Solstice · June noon h %.2f°)',
    '  安装          墙面正南, 杆根在盘面上缘中点, 斜向下方伸出': "  Mounting        wall facing due south; rod root at the midpoint of the plate's top edge, slanting downward",
    '  安装          底边压在子午线上, 直角在北端, 斜边朝北天极': '  Mounting        base on the meridian line, right angle at the north end, hypotenuse toward the north celestial pole',
    '  本月长度    %.4f 日  (朔望月平均 29.530589 日)': '  Month length   %.4f d  (mean lunation 29.530589 d)',
    '【第三页】恒星 (SHA 与赤纬; GHA星 = GHA白羊 + SHA)': '[Page 3] Stars (SHA and declination; GHA star = GHA Aries + SHA)',
    '            代入: φ = %s ± %s  ⇒  φ = %s': '            Calc: φ = %s ± %s  ⇒  φ = %s',
    '      中天测纬:  天体过中天 (LHA = 0° 或 180°) 时': '      Latitude by meridian altitude:  when the body transits (LHA = 0° or 180°)',
    '  北臂 →   0°  需 %s  (冬至·12 月正午 h %.2f°)': '  North arm →   0°  needs %s  (Winter Solstice · December noon h %.2f°)',
    '  晷面读数 − 钟表 = %+.2f 分   ← 晷面永远比钟表%s这么多': '  Dial reading − clock   = %+.2f min   ← the dial is always this much %s the clock',
    '  视赤经 α = %s      视赤纬 δ = %s   (当日真分点)': '  Apparent RA α = %s      Dec δ = %s   (true equinox of date)',
    '内容由本程序星历实时算出, 格式仿 The Nautical Almanac': "Computed live from this program's ephemeris; layout modelled on The Nautical Almanac",
    '密度 D(指标)=%.2f  D(地平)=%.2f  该天体需要 ≈%.2f': 'Density D(index)=%.2f  D(horizon)=%.2f  this body needs ≈%.2f',
    '日月中心角距 %.4f′   日视半径 %.4f′   月视半径 %.4f′': 'Sun-Moon centre separation %.4f′   Sun SD %.4f′   Moon SD %.4f′',
    '等距示意: 半径只表示「第几条轨道」, 不代表距离; 行星的方位角仍是真的。': 'Equal spacing: the radius only says "which orbit", not distance; the planets\' angular positions are still true.',
    '      → 一次观测只能定一条线; 要 2 条以上不同方位的线才交会出点。': '      → One sight gives only a line; 2 or more lines at different azimuths are needed to intersect in a point.',
    '   对应真高度 Ho = %s ;  GHA = %s   Dec = %s': '   Corresponding true altitude Ho = %s;  GHA = %s   Dec = %s',
    '  于是你必在以 GP 为心、半径 z 的等高圆上; 两个天体的圆相交即船位。': '  so you must lie on the circle of equal altitude centred on the GP with radius z; where the circles of two bodies cross is the fix.',
    '  偏差 %.2f 海里 (%.2f km);  残差 RMS = %.2f′': '  Error %.2f nm (%.2f km);  residual RMS = %.2f′',
    '  要对准真北, 不是磁北 (罗盘须改正磁偏角); 最稳用「等影法」定子午线。': '  Align with true north, not magnetic north (correct a compass for magnetic declination); the most reliable way to find the meridian is the equal-shadow method.',
    '【原理】天体在地球上的星下点 GP: 纬度 = Dec, 经度 = −GHA。': "[Principle] A body's geographical position on Earth, GP: latitude = Dec, longitude = −GHA.",
    '北半球: 盈月亮在「右」, 亏月亮在「左」。到了南半球整个明暗方向会左右颠倒。': 'North: waxing Moon lit on the right, waning on the left (mirrored in the south).',
    '半影模糊带: %s ~ %s  (宽 %s) —— 郭守敬「景符」正为消此模糊': "Penumbral blur: %s ~ %s  (width %s) — Guo Shoujing's shadow sharpener (jingfu) was made to remove exactly this blur",
    '圭: 北 %s / 南 %s    此纬度全年所需 北 %s / 南 %s%s': 'Scale: N %s / S %s    needed year-round at this latitude: N %s / S %s%s',
    '日晷 · 六分仪 · 星空月相 · 太阳视运动 · 土圭 · 日月食 · 轨道': 'Sundial · Sextant · Sky & Moon Phase · Sun Track · Gnomon · Eclipses · Orbits',
    '            Δφ = %+.2f′    Δp = %+.2f 海里': '            Δφ = %+.2f′    Δp = %+.2f nm',
    '      代入: DR φ = %s  λ = %s   ⇒ LHA = %s': '      Calc: DR φ = %s  λ = %s   ⇒ LHA = %s',
    '     90°  = 上弦, 日落时在正南, 上半夜可见, 亮面朝西(向太阳)': '     90°  = First Quarter: S at sunset, sets ~midnight, lit side W',
    '  盘面倾角      %.4f°  = 90° − |φ| (盘面平行天赤道)': '  Plate tilt      %.4f°  = 90° − |φ| (plate parallel to the celestial equator)',
    '  视黄经差    %.4f°   相位角 %.3f°   被照亮 %.2f%%': '  Elongation     %.4f°   phase angle %.3f°   illum. %.2f%%',
    '恒星: 内置 %d 颗亮星(含北极星/南十字)。放 stars.csv 可加更多': 'Stars: %d built-in (incl. Polaris, Southern Cross); add stars.csv for more',
    '本地: %s  食分 %.4f  遮蔽 %.2f%%  食甚太阳高度 %.2f°': 'Local: %s  mag. %.4f  obscuration %.2f%%  Sun alt. at max %.2f°',
    '    %s  真太阳时 %02d:00–%02d:00   钟表 %s – %s': '    %s  solar %02d:00–%02d:00   clock %s – %s',
    '    %s  真太阳时 %02d:00–%02d:00   钟表 %s–%s%s': '    %s  solar %02d:00–%02d:00   clock %s–%s%s',
    '  %s  制作规格   纬度 φ = %s   晷面半径 R = %.1f cm': '  %s  construction specs   latitude φ = %s   dial radius R = %.1f cm',
    '  J2000: α=%s δ=%s   λ=%s β=%s   视星等 %.2f': '  J2000: α=%s δ=%s   λ=%s β=%s   apparent mag %.2f',
    '  北臂 → 方位   0° (真北)     南臂 → 方位 180° (真南)': '  North arm → Az   0° (true N)     South arm → Az 180° (true S)',
    '  注: 时线只与纬度有关, 与日期无关; 刻 = 15 分 = 时角 3.75°': '  Note: hour lines depend only on latitude, not on the date; 1 ke = 15 min = 3.75° of hour angle',
    '回归线之间: 一年有两天太阳过天顶 (正午无影), 影会南北易向, 故圭须南北双向': 'Between the tropics: the Sun passes the zenith on two days a year (shadowless noon) and the shadow swaps between north and south, so the scale needs both a north and a south arm',
    '      现在只有 %d 次观测 —— 还解不出点。再记录一个方位不同的天体即可。': '      Only %d sight(s) so far — no fix yet. Record one more body at a different azimuth.',
    '  cos(Zn)·dφ + sin(Zn)·dDep = a   (单位: 海里)': '  cos(Zn)·dφ + sin(Zn)·dDep = a   (units: nm)',
    '  安装          杆指向天极, 盘心在杆上; 春分后看上面, 秋分后看下面': '  Mounting        rod points at the celestial pole, plate centre on the rod; after the Spring Equinox read the upper face, after the Autumn Equinox the lower face',
    '  经度靠时间: GHA 每 4 分钟走 1°, 钟差 1 秒 ≈ 0.25 海里。': '  Longitude comes from time: GHA advances 1° every 4 minutes, so a clock error of 1 s ≈ 0.25 nm.',
    '         (真实位置 φ = %s  λ = %s;  偏差 %.2f 海里)': '         (true position φ = %s  λ = %s;  error %.2f nm)',
    '      距离 %12.1f km   视半径 %.4f′   地平视差 %.4f′': '      distance %12.1f km   SD %.4f′   HP %.4f′',
    '  %d 年 影朝南 (用南臂 180°): %s; 其余日子影朝北 (用北臂 0°)': '  In %d the shadow points south (south arm, 180°): %s; on all other days it points north (north arm, 0°)',
    '  格林时角 GHA %.4f°   地方时角 LHA %.4f° (%+.3f h)': '  GHA %.4f°   LHA %.4f° (%+.3f h)',
    '%-4s %02d-%02d  ↑%s  ☉%s  ↓%s  昼%5.2fh  高%s': '%-4s %02d-%02d  ↑%s  ☉%s  ↓%s  day %5.2fh  alt %s',
    '内圈 = 从北极上方看的真实明暗;  外圈 = 在%s看到的样子 (鼠标指向可看时刻)': 'Inner: above the N. Pole · outer: %s view (hover = times)',
    '夹钳锁紧中 → 只有 1′ / 0.1′ 微动螺旋能动; 要 1° 粗调请先点夹钳松开': 'Clamp locked → only the 1′ / 0.1′ drum works; unclamp for 1° steps',
    '日月视黄经差 %.4f°   角距 %.4f°   月面被照亮 %.2f%%   %s': 'Moon-Sun apparent Δλ %.4f°   separation %.4f°   illuminated %.2f%%   %s',
    '视线 %s: 方位 %.1f° (%s)   高度 %+.1f°   视场 %.0f°': 'View (%s): Az %.1f° (%s)   Alt %+.1f°   FOV %.0f°',
    '      GHA 每小时走 15°, 每 4 分钟走 1°, 每 1 秒走 0.25′': '      GHA moves 15° per hour, 1° every 4 minutes, 0.25′ every second',
    '      ⇒ 船位一定在以 GP 为圆心、半径 %.1f 海里的圆上 (一条位置圆)。': '      ⇒ The ship must lie on the circle centred on the GP with radius %.1f nm (a circle of position).',
    '      代入: UT = %s   Δt = %02dm%02ds = %.5f h': '      Calc: UT = %s   Δt = %02dm%02ds = %.5f h',
    '   ⑤ 截距 a = Ho − Hc = %+.2f′ = %+.2f 海里 (%s)': '   ⑤ Intercept a = Ho − Hc = %+.2f′ = %+.2f nm (%s)',
    '  恒星时角 SHA = %.4f°  (航海历用 GHA = GHA白羊 + SHA)': '  SHA = %.4f°  (Nautical Almanac: GHA = GHA Aries + SHA)',
    '★ 此刻 (%s UTC) 你选的 %s (%s) 的正确六分仪读数:  Hs = %s': '★ Now (%s UTC), the correct sextant reading for your selected %s (%s):  Hs = %s',
    '【月亮】视赤经 %s  视赤纬 %s   地平: 高度 %+.3f°  方位 %.2f°': '[Moon]  Apparent RA %s  Dec %s   Horizontal: Alt %+.3f°  Az %.2f°',
    '左右缓缓摆动六分仪 (rock it slowly): 天体划弧, 弧的最低点才是真高度': 'Rock the sextant slowly: the body swings in an arc; its lowest point is the true altitude',
    '观测者定向 (%s, 天顶朝上): 各日当地正午时你抬头看到的样子; 点任一天可跳到那天': 'Observer (%s): zenith up, local noon; click a day to jump to it',
    '        明亮边缘方位角 χ = %.1f° (自天北极向东) —— 决定月牙朝哪边': '        Bright-limb position angle χ = %.1f° (N through E) — sets which way the crescent faces',
    '        月地距离 %.0f km   视半径 %.2f′   地平视差 %.2f′': '        Distance %.0f km   SD %.2f′   HP %.2f′',
    '   (Hs 已含 眼高俯角 %.2f′ 与 指标差 %.2f′; 你现在的读数是 %s)': '   (Hs already includes dip %.2f′ and index error %.2f′; your current reading is %s)',
    '  公式: θ = H                   (每小时正好 15°, 均匀)': '  Formula: θ = H                   (exactly 15° per hour, uniform)',
    '%s  α %s   δ %s   高度 %+7.3f°(视)  方位 %7.3f° %s': '%s  α %s   δ %s   apparent alt %+7.3f°  Az %7.3f° %s',
    'ΔT 外推, 时刻不确定度约 ±10 秒~±1 分; 经度随之有 ±0.05° 量级偏差。': 'ΔT extrapolated: times uncertain by about ±10 s to ±1 min, giving longitude errors of order ±0.05°.',
    '内置星历 VSOP87/ELP (对比 ERFA: 日<0.4″ 月<0.2″ 金<3″)': 'Built-in ephemeris VSOP87/ELP (vs ERFA: Sun<0.4″ Moon<0.2″ Venus<3″)',
    '      代入: a = %s − %s = %+.2f′ = %+.2f 海里 (%s)': '      Calc: a = %s − %s = %+.2f′ = %+.2f nm (%s)',
    '   真太阳时    时角 H        θ (度)      每刻 (15分) 的 θ': '   Solar time  H (HA)       θ (deg)   θ at each ke (15 min)',
    '1 AU = %.1f px   全幅 22 AU = %.0f px   缩放 %.2f×': '1 AU = %.1f px   full width 22 AU = %.0f px   zoom %.2f×',
    '每次观测给出一条位置线; 2 条以上交会出船位。\n详细解算过程见左下「计算结果」与航海历页。': 'Each sight gives one line of position; 2 or more lines intersect at the fix.\nFor the full working see "Results" (lower left) and the Nautical Almanac tab.',
    '误差      Δφ = %+.2f′   Δλ = %+.2f′(东西向 %.2f nm)': 'Error     Δφ = %+.2f′   Δλ = %+.2f′ (E-W %.2f nm)',
    '  距离 %.0f km = %.6f AU   视半径 %.3f′   地平视差 %.3f′': '  Distance %.0f km = %.6f AU   SD %.3f′   HP %.3f′',
    '低纬度 |φ|=%.1f°: 水平晷的时线挤成一束几乎读不出, 赤道晷每小时正好 15° 均匀': "Low latitude |φ|=%.1f°: a horizontal dial's hour lines crowd together and are almost unreadable; an equatorial dial is uniform at exactly 15° per hour",
    '%s  φ=%s  λ=%s\n%s (UTC%+.2f) · %s年 · ↑日出 ☉中天 ↓日落': '%s  φ=%s  λ=%s\n%s (UTC%+.2f) · %s · ↑rise ☉transit ↓set',
    '【第六页】观测归算 Sight Reduction (Marcq St Hilaire 截距法)': '[Page 6] Sight Reduction (Marcq St Hilaire intercept method)',
    '前后 9 小时内找不到 2 个方位相差 30° 以上、高于 12° 的天体。换个时刻或地点再试。': 'Could not find 2 bodies higher than 12° with azimuths at least 30° apart within 9 hours either side. Try another time or location.',
    '键盘: ← → = 0.1′   Shift+← → = 1′   Ctrl 或 ↑↓ = 1°': 'Keys: ← → = 0.1′   Shift+← → = 1′   Ctrl or ↑↓ = 1°',
    '      代入本次: cos(%.1f°)·Δφ + sin(%.1f°)·Δp = %+.2f': '      This sight: cos(%.1f°)·Δφ + sin(%.1f°)·Δp = %+.2f',
    '  观测得到的真高度 Ho 决定你到 GP 的角距 z = 90°−Ho (1′ = 1 海里),': '  The observed true altitude Ho fixes your angular distance from the GP, z = 90°−Ho (1′ = 1 nm),',
    '【月相】视黄经差(月−日) %.3f°   相位角 %.2f°   被照亮 %.1f%%   %s': '[Phase] Elongation (Moon−Sun) %.3f°   phase angle %.2f°   illuminated %.1f%%   %s',
    '            取与推测纬度接近的那个根。本次 LHA = %s (离中天 %.2f°)%s': '            Take the root closer to the DR latitude. This sight: LHA = %s (%.2f° from transit)%s',
    '          总偏差 = %.2f 海里 (%.2f km)   残差 RMS = %.2f′': '          Total error = %.2f nm (%.2f km)   residual RMS = %.2f′',
    '      GHA                = %s   (直接算得 %s, 差 %.2f″)': '      GHA                = %s   (computed directly %s, diff %.2f″)',
    '      a = Ho − Hc     (角分 = 海里;  a>0 向着天体方位 Zn 移动)': '      a = Ho − Hc     (arcminutes = nm;  a>0: move toward the body, along azimuth Zn)',
    '   ③ 航海历: GHA = %s   Dec = %s   ⇒ LHA = GHA+λ = %s': '   ③ Nautical Almanac: GHA = %s   Dec = %s   ⇒ LHA = GHA+λ = %s',
    '太阳: 视高度 %.4f°  真高度 %.4f°  方位 %.3f° (%s)  赤纬 %+.4f°': 'Sun: apparent alt %.4f°  true alt %.4f°  Az %.3f° (%s)  Dec %+.4f°',
    '屏幕角: 自图面正下方起, 逆时针。 z > 0 = 高过日地线(黄道面), z < 0 = 低过。': 'Screen angle: measured from straight down on the chart, anticlockwise. z > 0 = above the Sun-Earth line (ecliptic plane), z < 0 = below.',
    '月绕地一圈 = 一个朔望月 ≈ 29.53 日 (比恒星月 27.32 日长, 因地球同时在绕日走)': 'One lap = one lunation ≈ 29.53 d (> sidereal 27.32 d; Earth orbits the Sun too)',
    '  三角晷针: 底边 %.2f cm   尖端高 %.2f cm   仰角 = |φ| = %.3f°': '  Triangular gnomon: base %.2f cm   tip height %.2f cm   elevation = |φ| = %.3f°',
    '南半球: 盈月亮在「左」, 亏月亮在「右」—— 与北半球正好颠倒 (观测者头下脚上地面对同一个月亮)。': 'South: waxing Moon lit on the left, waning on the right (the north mirrored).',
    '      增量 (%02dm%02ds)      = %s      (%.4f h × %s/h)': '      Increment (%02dm%02ds) = %s      (%.4f h × %s/h)',
    'GHA %.3f°  Dec %+.3f°  SD %.2f′  HP %.2f′  蒙气差 %.2f′': 'GHA %.3f°  Dec %+.3f°  SD %.2f′  HP %.2f′  refraction %.2f′',
    '1 AU = %.1f px (横)   全幅 22 AU = %.0f px   竖向 %.0f× 放大': '1 AU = %.1f px (horizontal)   full width 22 AU = %.0f px   vertical exaggeration %.0f×',
    'ΔT 长期抛物线外推, 时刻不确定度可达 ±5~15 分钟; 最大食点经度可差 ±3°。类型/食分仍可靠。': 'ΔT from long-term parabolic extrapolation: times may be off by ±5–15 min; longitude of greatest eclipse by up to ±3°. Type and magnitude remain reliable.',
    '夹紧时只能用微动螺旋(细调); 松开后指标臂可沿弧自由滑动(粗调)。\n画布上直接点遮光片或夹钳也可以操作。': 'Clamped: micrometer drum only (fine). Unclamped: index arm slides freely along the arc (coarse).\nShades and clamp can also be clicked directly on the canvas.',
    '      GP 的纬度 = Dec ,   GP 的经度 = −GHA  (西经为正时取 360−GHA)': '      GP latitude = Dec ,   GP longitude = −GHA  (as a positive east longitude: 360−GHA)',
    '%-4s %8.3f° %7.2f° %8.5f  %+7.4f° %+8.5f   ——— 观测点 ———': '%-4s %8.3f° %7.2f° %8.5f  %+7.4f° %+8.5f   ——— observer ———',
    '   下面表里: 黄底加粗 = 本次观测所在的整点行, 青底 = 该天体的列, 淡黄 = 下一小时(内插用)。': "   In the tables below: bold on yellow = the whole-hour row of this sight, cyan = this body's column, pale yellow = the next hour (for interpolation).",
    '  地平坐标: 高度 %+.4f° (视 %+.4f°, 蒙气差 %.2f′)   方位 %.3f° (%s)': '  Horizontal: Alt %+.4f° (apparent %+.4f°, refraction %.2f′)   Az %.3f° (%s)',
    '      Ha = Hs − IE − Dip ,        Dip = 1.758′ × √(眼高 m)': '      Ha = Hs − IE − Dip ,        Dip = 1.758′ × √(height of eye in m)',
    '  公式: tanθ = sinφ · tanH      (H = 时角 = (真太阳时 − 12)×15°)': '  Formula: tanθ = sinφ · tanH      (H = hour angle = (apparent solar time − 12)×15°)',
    '【第四页】定位方程 —— 由六分仪读数 Hs + 观测时刻 UT + 误差改正, 解出此刻的纬度 φ 与经度 λ': '[Page 4] Fix equations — from sextant reading Hs + time of sight UT + error corrections, solve for the current latitude φ and longitude λ',
    '天体      LHA        Dec        Hc         Zn      截距a(nm)': 'Body      LHA        Dec        Hc         Zn      Intercept a (nm)',
    '      代入: Hs = %s   IE = %+.2f′   Dip = %.2f′ (眼高 %.2f m)': '      Calc: Hs = %s   IE = %+.2f′   Dip = %.2f′ (height of eye %.2f m)',
    '宫度按 我定的 子宫 0° = 太阳黄经 300° = 大寒 = 水瓶 0°, 十二辰 子亥戌酉申未午巳辰卯寅丑。': 'Palace degrees use my own definition: Zi palace 0° = solar longitude 300° = Major Cold = Aquarius 0°; the twelve branches run Zi Hai Xu You Shen Wei Wu Si Chen Mao Yin Chou.',
    '定盘 %s · θ=%.1f° · 正下方 = 日心黄经 %.2f° · 此刻太阳在 %s宫 %.2f° (%s后)': 'Orientation: %s · θ=%.1f° · straight down = heliocentric longitude %.2f° · Sun now at %s palace %.2f° (after %s)',
    '真实 1 秒 = 星图 %g 日   |   地球一圈需 %.1f 真实秒\n已走 %.3f 日 = %.4f 地球年': '1 real second = %g simulated days   |   one Earth orbit takes %.1f real seconds\nElapsed %.3f days = %.4f Earth years',
    '            增量 = %.5f h × %s/h = %s   v = %+.1f′/h → %+.2f′': '            Increment = %.5f h × %s/h = %s   v = %+.1f′/h → %+.2f′',
    '      ⇒ 钟慢 1 秒, 经度就错 0.25′ ≈ 0.25 海里 × cos φ ≈ %.0f 米 (本纬度)': '      ⇒ A clock 1 s slow puts longitude out by 0.25′ ≈ 0.25 nm × cos φ ≈ %.0f m (at this latitude)',
    '天体  日心黄经  屏幕角  日心距AU   黄纬     z AU     地心黄经  宫 度       距地AU': 'Body   Hel.lon   Screen     r AU   Hel.lat     z AU    Geo.lon Palace deg    Δ AU',
    '      GHA = GHA(整点) + 增量(标称速率×Δt) + v·Δt        Dec 同法用 d 内插': '      GHA = GHA(whole hour) + increment(nominal rate×Δt) + v·Δt        Dec likewise, interpolated with d',
    '子 0° 定盘 (预设): 子宫 0° / 大寒 / 水瓶 0° 固定在 θ 处 (θ=0 即正下方), 地球按日期绕行': 'Zi 0° fixed (default): Zi palace 0° at θ (θ=0 = bottom); Earth moves by date',
    '%04d-%02d-%02d %02d:%02d  (UTC%+g)    自起始日 %+.3f 日 (%.3f 地球年)': '%04d-%02d-%02d %02d:%02d  (UTC%+g)    %+.3f days from start date (%.3f Earth years)',
    '   ① Hs = %s   −IE %+.2f′   −Dip %+.2f′ (眼高 %.1f m)  ⇒ Ha = %s': '   ① Hs = %s   −IE %+.2f′   −Dip %+.2f′ (height of eye %.1f m)  ⇒ Ha = %s',
    '  注: v = GHA 每小时变化超出标称值的部分 (日/行星标称 15°00.0′/h, 月标称 14°19.0′/h)': '  Note: v = excess of the hourly change in GHA over the nominal rate (Sun/planets nominal 15°00.0′/h, Moon nominal 14°19.0′/h)',
    '滚轮缩放 (可放到 0.01° 视场, 看清食既/生光的接触点) · 双击适配。未载入食时, 画面按真实角距同时显示日与月。': 'Mouse wheel zooms (down to a 0.01° field of view, to see second/third contact (C2/C3) closely) · double-click to fit. With no eclipse loaded, the view shows the Sun and Moon together at their true angular separation.',
    '      北极星定纬 (北半球): φ ≈ Ho(北极星) + a0 + a1 + a2  (三个小改正, 合计 < 1°)': '      Latitude by Polaris (northern hemisphere): φ ≈ Ho(Polaris) + a0 + a1 + a2  (three small corrections, total < 1°)',
    '此刻正确读数 Hs = %s   (%s · %s)\n真高度 Ho 应为 %s   GHA %.3f°  Dec %+.3f°': 'Correct reading now: Hs = %s   (%s · %s)\nTrue altitude Ho should be %s   GHA %.3f°  Dec %+.3f°',
    '        NAUTICAL ALMANAC —— %s (UT)        由本程序的 VSOP87/ELP 星历实时计算': "        NAUTICAL ALMANAC — %s (UT)        computed live from this program's VSOP87/ELP ephemeris",
    '土圭 · 圭表 —— 表高 %s, 圭长 %s (北) + %s (南)   · 圭轴 = 子午线: 北臂 0° / 南臂 180°': 'Tugui · gnomon & scale — gnomon height %s, scale length %s (N) + %s (S)   · scale axis = meridian: north arm 0° / south arm 180°',
    '左键拖动转视角(松开即固定) · 右键拖动平移 · 滚轮/「放大」可放到 %.0f× (低纬度看时线要用) · 仰角限 %d°~%d°': 'Left-drag to turn the view (fixed on release) · right-drag to pan · mouse wheel / "Zoom in" magnifies up to %.0f× (needed for hour lines at low latitudes) · elevation limits %d°~%d°',
    '真实比例: 土星远日点 10.1 AU, 正好塞得进 ±11 AU。轨道由 VSOP87 逐点采样画出, 偏心率、椭圆长短轴都是真的。': "True scale: Saturn's aphelion is 10.1 AU, so it just fits inside ±11 AU. Orbits are sampled point by point from VSOP87; eccentricities and the ellipses' major and minor axes are all real.",
    '      Ho = Ha − R(Ha) + s·SD + PA·cos Ha    s = +1 下缘 / −1 上缘 / 0 中心': '      Ho = Ha − R(Ha) + s·SD + PA·cos Ha    s = +1 lower limb / −1 upper limb / 0 centre',
    '      cos Zn · Δφ  +  sin Zn · Δp  =  a        Δp = Δλ · cos φ (东西距)': '      cos Zn · Δφ  +  sin Zn · Δp  =  a        Δp = Δλ · cos φ (departure)',
    '左键拖动转视角 · 右键拖动平移 · 滚轮缩放 (改视场角, 可放到极大) · 双击复位。圭面读数以「表」的北面为 0, 北为正、南为负。': "Left-drag rotates the view · right-drag pans · mouse wheel zooms (changes the field of view; can magnify enormously) · double-click resets. Scale readings are zero at the gnomon's north face, positive to the north and negative to the south.",
    ' 记号  Hs 六分仪读数 │ IE 指标差 │ Dip 眼高俯角 │ R 蒙气差 │ SD 视半径 │ PA 视差 │ Ho 真高度(地心)': ' Notation  Hs sextant reading │ IE index error │ Dip dip of the horizon │ R refraction │ SD semidiameter │ PA parallax in altitude │ Ho true altitude (geocentric)',
    '远古/远未来: ΔT 抛物线的不确定度可达 ±30 分钟以上 (公元前尤甚), 时刻与经度仅供参考; 但食的「有无·类型·食分·纬度」依然可靠。': 'Remote past/future: the ΔT parabola can be uncertain by more than ±30 min (worse still BCE), so times and longitudes are indicative only; but an eclipse\'s "occurrence · type · magnitude · latitude" remain reliable.',
    '视角 %s: 视线方位 %.1f°  俯仰 %+.1f°   (相机在方位 %.1f°, 仰角 %.1f°)   放大 %.1f×  视场 %.1f°': 'View (%s): line of sight Az %.1f°  pitch %+.1f°   (camera at Az %.1f°, elevation %.1f°)   zoom %.1f×  FOV %.1f°',
    '            LHA=0°(上中天, 天体在正南/正北):  φ = Dec + (90° − Ho)  或  Dec − (90° − Ho)': '            LHA=0° (upper transit, body due south/north):  φ = Dec + (90° − Ho)  or  Dec − (90° − Ho)',
    '      cos Zn = (sinDec − sinφ·sin Hc) / (cosφ·cos Hc)   (LHA<180° 时 Zn = 360−Zn)': '      cos Zn = (sinDec − sinφ·sin Hc) / (cosφ·cos Hc)   (if LHA<180°, Zn = 360−Zn)',
    '把星表放成同目录下的 stars.csv 即可显示恒星\n列名支持: name/名称, ra 或 ra_deg 或 ra_h, dec/dec_deg, mag/星等': 'Put a star catalogue named stars.csv in the program folder to show stars\nSupported columns: name, ra or ra_deg or ra_h, dec/dec_deg, mag',
    '   星名                    SHA          Dec        |   星名                    SHA          Dec': '   Star                    SHA          Dec        |   Star                    SHA          Dec',
    '侧面图: 横轴 = 当时的日地连线方向 (真实比例, 全宽 22 AU), 竖轴 = 日心黄道 z。真实 z 最大也才 0.4 AU (土星), 所以竖向另给放大倍数, 括号里是真值。': 'Side view: horizontal axis = direction of the Sun-Earth line at that moment (true scale, 22 AU full width); vertical axis = heliocentric ecliptic z. Real z is at most about 0.4 AU (Saturn), so the vertical axis gets its own exaggeration factor; values in brackets are true values.',
    '标准时 %s   地方平时 %s   真太阳时 %s\n均时差 %+.1f 分   经度时差 %+.1f 分   此刻属 %s %.1f 时\n太阳 高度 %s   方位 %.2f° (%s)': 'Standard %s   LMT %s   Apparent %s\nEoT %+.1f min   Long. offset %+.1f min   now: %s, %.1f h\nSun altitude %s   azimuth %.2f° (%s)',
    '日晷 · 六分仪 · 星空月相 · 太阳视运动 · 土圭 · 日月食 · 轨道  模拟器  ·  Sundial / Sextant / Sky / Gnomon / Eclipse Simulator': 'Sundial · Sextant · Sky & Moon Phase · Sun Track · Gnomon · Eclipses · Orbits — Simulator',
    '鼠标滚轮缩放(以光标为定点) · 按住左键拖动平移 · 双击复位。视角固定为「东在近前、南左北右」, 只缩放不旋转。低纬度(如吉隆坡)太阳近天顶, 把「视线俯角」拉到 50°~80° 可把各条轨迹拉开看清。': 'Mouse wheel zooms (about the cursor) · hold the left button and drag to pan · double-click resets. The view is fixed with east nearest you, south on the left and north on the right; it zooms but does not rotate. At low latitudes (e.g. Kuala Lumpur) the Sun passes near the zenith: raise the "Look-down angle" to 50°~80° to spread the tracks apart.',
    'θ = 0° 即轨道图正下方。预设定盘下 θ 是 子宫 0° (大寒 / 水瓶 0°) 的方位, 所以预设子 0° 就在正下方; 另两种定盘下 θ 是地球的方位。角度沿逆时针 (= 行星实际公转方向) 递增。': "θ = 0° is straight down on the orbit chart. In the default orientation θ is the direction of Zi palace 0° (Major Cold / Aquarius 0°), so by default Zi 0° is straight down; in the other two orientations θ is the direction of Earth. Angles increase anticlockwise (= the planets' actual direction of revolution).",
    '%s\n\n将继续使用内置算法。\n内置算法与 IAU SOFA/ERFA 比对的视位置误差:\n  太阳 < 0.4″   月亮 < 0.2″   金星 < 3″\n对六分仪(读数分辨率 0.1′ = 6″)已绰绰有余。': '%s\n\nContinuing with the built-in algorithms.\nApparent-position errors of the built-in algorithms against IAU SOFA/ERFA:\n  Sun < 0.4″   Moon < 0.2″   Venus < 3″\nMore than enough for the sextant (reading resolution 0.1′ = 6″).',
    '将尝试载入 skyfield 与 de421.bsp。\n若本机尚无该星历文件, skyfield 会从网上下载约 17 MB,\n下载期间界面会暂时无响应。是否继续?\n\n(内置算法已达 太阳<0.4″ 月亮<0.2″ 金星<3″, 通常无需切换)': 'Will try to load skyfield and de421.bsp.\nIf this ephemeris file is not on this computer yet, skyfield will download about 17 MB from the internet,\nand the window will not respond during the download. Continue?\n\n(The built-in algorithms already achieve Sun <0.4″, Moon <0.2″, Venus <3″; switching is usually unnecessary.)',
    '《周髀算经》「周髀长八尺」。唐开元十一年 (723) 南宫说在告成立石表, 表高\n八尺 ≈ 1.96 m, 石圭长约 3 m —— 今河南登封「周公测景台」即此。\n八尺表是中国二千年间的标准器: 夏至影一尺五寸、冬至影一丈三尺 (洛阳一带),\n《周髀》《后汉书·律历志》的影长表都以此为准。': 'Zhoubi Suanjing: "the gnomon of Zhou is eight chi long". In 723 (Kaiyuan 11, Tang) Nangong Yue erected a stone gnomon at Gaocheng,\neight chi ≈ 1.96 m tall, with a stone scale about 3 m long — it survives today as the Duke of Zhou\'s Shadow Platform at Dengfeng, Henan.\nThe eight-chi gnomon was China\'s standard instrument for two thousand years: summer-solstice shadow 1 chi 5 cun, winter-solstice shadow 13 chi (around Luoyang);\nthe shadow-length tables of the Zhoubi and of the Treatise on Pitch-pipes and Calendar in the Book of the Later Han are all based on it.',
    '自己动手就能做: 3 mm 亚克力板或硬卡纸做圭, 一根 20 cm 铝条/竹签做表。\n圭面刻度用 A4 纸打印后贴上 (毫米即可读到 0.3% 的影长精度)。\n关键是表必须真正铅垂 (吊铅锤) 且圭面水平 (水平仪或注水槽), 圭必须\n严格指向真北 —— 不是磁北。用「等影法」定北: 上午与下午影长相等的两点连线\n取中垂线即是子午线。': 'Easy to make yourself: a 3 mm acrylic sheet or stiff card for the scale, a 20 cm aluminium strip or bamboo skewer for the gnomon.\nPrint the graduations on A4 paper and stick them on (reading to 1 mm already gives 0.3% shadow-length precision).\nThe key: the gnomon must be truly plumb (hang a plumb bob), the scale level (spirit level or water channel),\nand the scale aligned exactly with true north — not magnetic north. Find north by the equal-shadow method:\njoin the morning and afternoon shadow tips of equal length; the perpendicular bisector of that line is the meridian.',
    '元至元十三年郭守敬所建, 现存河南登封告成镇。台身高 9.46 m, 台顶横梁即「表」,\n较传统八尺表高出五倍, 影长随之放大五倍, 读数精度大增。\n台北的石圭俗称「量天尺」, 长 31.19 m、宽 0.53 m, 由 36 方青石接成, 两侧凿\n水槽以校水平。郭守敬另创「景符」—— 一块开小孔的铜片, 在圭上移动, 让横梁与\n太阳同时在孔后成像, 把模糊的半影边缘变成清晰的细线, 读数可到「分」(≈2.5 mm)。\n《授时历》回归年 365.2425 日即由此台测得。': "Built by Guo Shoujing in 1276 (Zhiyuan 13, Yuan dynasty); it still stands at Gaocheng, Dengfeng, Henan.\nThe platform is 9.46 m high and the crossbar on top is the gnomon: five times the traditional eight-chi height, so the shadow is five times longer and readings are far more precise.\nThe stone scale north of the platform, the Sky-Measuring Scale, is 31.19 m long and 0.53 m wide, made of 36 bluestone blocks, with water channels cut along both sides for levelling.\nGuo Shoujing also invented the shadow sharpener (jingfu): a copper plate with a pinhole that slides along the scale so that the crossbar and the Sun are imaged together behind the hole,\nturning the blurred penumbral edge into a sharp thin line; readings reach one fen (≈2.5 mm).\nThe Shoushi calendar's tropical year of 365.2425 days was measured at this observatory.",
    '六分仪操作 (与真船上一样):\n  ① 先把遮光镜翻下来 —— 测太阳必须遮光, 否则灼伤眼睛。\n     按「建议滤片」会按太阳高度自动选深浅; 也可以直接点画面上的滤片。\n  ② 望远镜对平海平线 —— 本模拟里海平线永远在视场正中。\n  ③ 松开夹钳(点画面上红色的夹钳), 拖动金色指标臂把天体带下来。\n  ④ 夹紧夹钳, 用微动螺旋(分盘/箭头/键盘←→)把下边缘正好切在海平线上。\n  ⑤ 左右缓缓摆动六分仪(勾「摆动演示」), 天体划弧, 弧的最低点才是真高度。\n  ⑥ 记下 Hs 与秒表时刻 → 按「记录本次观测」。\n  ⑦ 记 2~3 个方位不同的天体, 到「定位」页按「计算船位」。\n  「自动测量演示」会把①~⑥整套动作演一遍。\n': 'Using the sextant (just as on a real ship):\n  ① First lower the shades — never observe the Sun unshaded, or it will burn your eyes.\n     "Advised shades" picks the density from the Sun\'s altitude; you can also click the shades on the canvas.\n  ② Aim the telescope at the sea horizon — in this simulation the horizon always stays mid-field.\n  ③ Unclamp (click the red clamp on the canvas) and drag the gold index arm to bring the body down.\n  ④ Clamp, then use the micrometer drum (drag the drum, click its arrows or press ←→) to set the lower limb exactly on the horizon.\n  ⑤ Rock the sextant slowly from side to side (tick "Rocking demo"): the body swings in an arc; only its lowest point gives the correct altitude.\n  ⑥ Note Hs and the stopwatch time → press "Record sight".\n  ⑦ Take 2–3 bodies at different azimuths, then press "Compute fix" on the "Fix" tab.\n  "Auto sight demo" runs through the whole of ①–⑥.\n',
    '北面': 'north face',
    '南面': 'south face',
    '上面': 'upper face',
    '下面': 'lower face',
    '东面': 'east face',
    '西面': 'west face',
    '垂直朝北晷': 'vertical north dial',
    '高纬度 |φ|=%.1f°: 太阳终日偏低, %s面受光角度好': 'High latitude |φ|=%.1f°: the Sun stays low all day, so %s face catches the light best',
    '垂直朝南': 'a vertical south-facing',
    '垂直朝北 (南半球)': 'a vertical north-facing (southern hemisphere)',
    '  晷针形状      直角三角形 (指%s的三角板)': '  Style shape   right triangle (a set square pointing %s)',
    '  三角形底边    %.2f cm  (沿子午线由中心向%s量)': '  Triangle base %.2f cm  (measured from the centre toward the %s along the meridian)',
    '  三角形高      %.2f cm  (%s端垂直立起)': '  Triangle height %.2f cm  (raised vertically at the %s end)',
    '  安装          底边压在子午线上, 直角在%s端, 斜边朝%s天极': '  Mounting      base on the meridian, right angle at the %s end, hypotenuse toward the %s celestial pole',
    '  安装          杆指向天极, 盘心在杆上; 春分后看%s面, 秋分后看%s面': '  Mounting      rod aimed at the celestial pole, plate centred on it; after the March equinox read the %s face, after the September equinox the %s face',
    '上': 'upper',
    '下': 'lower',
    '右': 'right',
    '左': 'left',
    '  安装          墙面正%s, 杆根在盘面上缘中点, 斜向下方伸出 (指向%s天极)': "  Mounting      wall facing due %s, rod rooted at the middle of the plate's top edge, sloping down and out (toward the %s celestial pole)",
    '垂直朝北晷 Vertical North': 'Vertical north dial',
    '(正对受照的%s看: 正午影线朝下, 上午在%s侧, 下午在%s侧)': '(facing the sunlit %s: noon line points down, morning on the %s, afternoon on the %s)',
    '上(北)面': 'upper (north) face',
    '下(北)面': 'lower (north) face',
    '上(南)面': 'upper (south) face',
    '下(南)面': 'lower (south) face',
    '垂直朝北晷面 (自北向南看墙面, 南半球)': 'Vertical north-facing dial (wall seen from the north; southern hemisphere)',
    '左=西 (上午影)   右=东 (下午影)': 'left = west (morning shadows)   right = east (afternoon shadows)',
    '左=东 (下午影)   右=西 (上午影)': 'left = east (afternoon shadows)   right = west (morning shadows)',
    '此刻阳光照不到朝北墙面 (太阳在南侧或已落下)': 'No sunlight on the north-facing wall now (the Sun is to the south or has set)',
    '     90°  = 上弦, 日落前后过中天, 上半夜可见, 亮面朝西(向太阳)': '     90°  = First Quarter: transits around sunset, visible in the evening, lit side west (toward the Sun)',
    '     270° = 下弦, 后半夜升起, 日出前后过中天, 亮面朝东': '     270° = Last Quarter: rises after midnight, transits around sunrise, lit side east',
    '锁定当日真正午 —— 影子恒落在圭上 (预设; 改时/分即解锁)': 'Lock to apparent noon — shadow always on the scale (default; editing h/min unlocks)',
    '左键拖动转视角 · 右键拖动平移 · 滚轮缩放 (改视场角, 可放到极大) · 双击复位。圭面读数以表的投影边为 0 (北回归线以北 = 表北面, 南回归线以南 = 表南面, 两回归线之间 = 表心), 北为正、南为负。': "Left-drag rotates the view · right-drag pans · mouse wheel zooms (changes the field of view; can magnify enormously) · double-click resets. Scale readings are zero at the edge that casts the shadow (north of the Tropic of Cancer: the gnomon's north face; south of the Tropic of Capricorn: its south face; between the tropics: its axis), positive to the north and negative to the south.",
    '影长 (自%s起): %s     圭上读数 %s %s': 'Shadow length (from %s): %s     scale reading %s %s',
    '表北面': "the gnomon's north face",
    '表南面': "the gnomon's south face",
    '表心': "the gnomon's axis",
    '影落圭上的时刻 = 当地真正午 %s (UTC%+g)': 'Shadow lies on the scale at local apparent noon %s (UTC%+g)',
    '  = 12:00 − 均时差 %+.1f 分 + 经度改正 %+.1f 分 (时区子午线 %g° − 经度 %.3f°)': '  = 12:00 − EoT %+.1f min + longitude correction %+.1f min (zone meridian %g° − longitude %.3f°)',
    '  此刻离正午 %+.1f 分 —— 影子%s': '  Now %+.1f min from noon — shadow %s',
    '就在圭上': 'on the scale',
    '斜出圭外': 'off the scale',
    '  表用细杆立在圭的零点正中 (南北两臂都要接影); 若用方柱,': "  Use a thin rod standing exactly on the scale's zero (both arms catch shadows); with a square post,",
    '  北臂零点在柱北面、南臂零点在柱南面。': "  the north arm's zero is at the post's north face and the south arm's zero at its south face.",
    '  ⚠ 观星台形制的台身在横梁一侧, 会挡住另一臂的正午影 —— 回归线之间不宜。': "  ⚠ The observatory body stands on one side of the crossbar and blocks the other arm's noon shadow — unsuitable between the tropics.",
    '  南半球: 表立在圭的北端, 读数自表南面起 (与登封镜像)。': '  Southern hemisphere: the gnomon stands at the north end of the scale; readings start at its south face (mirror image of Dengfeng).',
    # ---- 轨道页: 两种定盘 (日地恒定 / 大寒定盘) ----
    ' 定 盘 (子 0° 恒在正下方) ': ' Chart frame (Zi 0° always straight down) ',
    '日地恒定 (预设)': 'Sun–Earth fixed (default)',
    '太阳、地球不动, 地球恒在子 0° (正下方), 日地虚线永远对准子 0°; 其余行星绕着走, 看它们相对日地的运动。': 'Sun and Earth stay put: Earth always sits at Zi 0° (straight down) and the dashed Sun–Earth line always aims at Zi 0°; the other planets move around them, showing their motion relative to the Sun and Earth.',
    '大寒定盘': 'Major Cold frame',
    '子宫 0° / 大寒 / 水瓶 0° 固定在正下方; 大寒那天地球在子宫 0°, 之后地球照常绕太阳 360°。': 'Zi palace 0° / Major Cold / Aquarius 0° fixed straight down; at Major Cold Earth is at Zi palace 0°, after which it goes round the Sun through 360° as usual.',
    '日地恒定盘的十二辰环以日地连线为子 0°, 环上角度 = 该星日心黄经 − 地球日心黄经: 外行星到子 0° = 冲, 到午 0° = 合; 内行星到子 0° = 下合, 到午 0° = 上合。大寒定盘的环标的是「地球走到这个方位时, 太阳在哪一宫、哪个节气」。两种盘的角度都自正下方起沿逆时针 (= 行星实际公转方向) 递增。': "In the Sun–Earth-fixed frame the twelve-branch ring takes the Sun–Earth line as Zi 0°, and a planet's angle on the ring = its heliocentric longitude − Earth's: an outer planet at Zi 0° is at opposition, at Wu 0° at conjunction; an inner planet at Zi 0° is at inferior conjunction, at Wu 0° at superior conjunction. In the Major Cold frame the ring shows which palace and solar term the Sun is in when Earth reaches that direction. In both frames angles increase anticlockwise from straight down (= the planets' actual direction of revolution).",
    '日地恒定 · 地球恒在正下方 = 子 0° (地球日心黄经 %.2f°) · 此刻太阳在 %s宫 %.2f° (%s后)': 'Sun–Earth fixed · Earth always straight down = Zi 0° (Earth heliocentric longitude %.2f°) · Sun now at %s palace %.2f° (after %s)',
    '侧面图 · 横轴 = 此刻日地连线 (地球在右) · 此刻太阳在 %s宫 %.2f° (%s后)': 'Side view · horizontal axis = current Sun–Earth line (Earth on the right) · Sun now at %s palace %.2f° (after %s)',
    '大寒定盘 · 正下方 = 子宫 0° = 大寒 (地球日心黄经 120°) · 地球在逆时针 %.2f° · 此刻太阳在 %s宫 %.2f° (%s后)': 'Major Cold frame · straight down = Zi palace 0° = Major Cold (Earth heliocentric longitude 120°) · Earth at %.2f° anticlockwise · Sun now at %s palace %.2f° (after %s)',
    '日地恒定: 屏幕角 = 日心黄经 − 地球日心黄经; 0° = 冲 / 下合, 180° = 合 / 上合。': "Sun–Earth fixed: screen angle = heliocentric longitude − Earth's; 0° = opposition / inferior conjunction, 180° = conjunction / superior conjunction.",
}
_EN.update(_EN_DATA)


def _en_add_bilingual(names):
    """「中文 English」式的名字 (地点、星名): 单独出现的中文部分也译成英文部分。"""
    for nm in names:
        m = _re.match(r"^(\S*[%s]\S*)\s+([^%s]+)$" % (_CJK_CHARS, _CJK_CHARS), nm)
        if m:
            _EN.setdefault(m.group(1), m.group(2).strip())


_en_add_bilingual([row[0] for row in CITIES] + [row[0] for row in TRACK_PLACES]
                  + [row[0] for row in _STAR_RAW] + list(SEXTANT_STARS))


if __name__ == "__main__":
    main()
