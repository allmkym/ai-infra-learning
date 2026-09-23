#!/usr/bin/env python3
import hashlib
import json
import re
import subprocess
from pathlib import Path

from pypdf import PdfReader

BASE = Path("materials/cs106l/2026-spring")
L5 = BASE / "2026Spring-05-Containers.pdf"
L11 = BASE / "2026Spring-11-LambdasAndFunctors.pdf"
L5_URL = "https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-05-Containers.pdf"
L11_URL = "https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-11-LambdasAndFunctors.pdf"
EXPECTED = {
    L5.name: (16146632, 68, "1dad3333f05915e63e395854d027c52eac3575ee6e00a08371091e067140bc46"),
    L11.name: (9299906, 137, "4c40b1349fc366f05d76c1de044b3043d8644e7dc2f15ce8abcc83e15b76dd62"),
}

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def verify_pdf(path):
    size, expected_pages, expected_sha = EXPECTED[path.name]
    actual_size = path.stat().st_size
    actual_sha = sha256(path)
    reader = PdfReader(str(path))
    actual_pages = len(reader.pages)
    if (actual_size, actual_pages, actual_sha) != (size, expected_pages, expected_sha):
        raise SystemExit(
            f"verification failed for {path.name}: bytes={actual_size}, pages={actual_pages}, sha256={actual_sha}"
        )
    return reader

def clean_text(s):
    if s is None:
        return ""
    return "".join(ch for ch in s if ch in "\n\t" or ord(ch) >= 32).strip()

def tesseract_version():
    cp = subprocess.run(["tesseract", "--version"], check=True, text=True, capture_output=True)
    return cp.stdout.splitlines()[0].strip()

def ocr_image(path, psm=6):
    cp = subprocess.run(
        ["tesseract", str(path), "stdout", "-l", "eng", "--psm", str(psm)],
        check=True, text=True, capture_output=True
    )
    return clean_text(cp.stdout)

def fence(text):
    ticks = chr(96) * 4
    return ticks + "text\n" + text + "\n" + ticks + "\n"

def page_numbers_from_dir(path):
    nums = []
    for p in path.glob("page-*.jpg"):
        m = re.fullmatch(r"page-(\d{3})\.jpg", p.name)
        if m:
            nums.append(int(m.group(1)))
    return sorted(nums)

def make_l5(reader, tess):
    page_dir = BASE / "lecture-05-pages"
    nums = page_numbers_from_dir(page_dir)
    if nums != list(range(1, 69)):
        raise SystemExit(f"Lecture 5 page-image coverage mismatch: {nums[:5]} ... {nums[-5:] if nums else []}")
    extracted = []
    nonempty_text_layer = []
    fallback = []
    for i, page in enumerate(reader.pages, 1):
        try:
            raw = clean_text(page.extract_text(extraction_mode="layout"))
        except Exception:
            raw = clean_text(page.extract_text())
        if raw:
            nonempty_text_layer.append(i)
        img = page_dir / f"page-{i:03d}.jpg"
        text = ocr_image(img, 6)
        if not text:
            text = ocr_image(img, 3)
            fallback.append(i)
        if not text:
            text = "[OCR 未取得可靠文本；请查看原页图。]"
        extracted.append(text)
    if nonempty_text_layer:
        raise SystemExit(f"Lecture 5 unexpectedly has text-layer pages: {nonempty_text_layer}")
    lines = [
        "# 2026Spring-05-Containers：按页 OCR 文本",
        "",
        "- 原 PDF：[2026Spring-05-Containers.pdf](2026Spring-05-Containers.pdf)",
        f"- 官方来源：[Stanford CS106L]({L5_URL})。课程目录已核验该文件名属于 2026 Spring；封面本身写明 “Lecture 5: Containers” 与 Preston Seay、Rachel Fernandez，但未单独印出学期。",
        f"- 生成日期：2026-09-23；方法：原 PDF 68/68 页均无可用文本层，使用已从原 PDF 渲染的长边 2000 像素 JPG，再用 `{tess}` 英文 OCR（默认 `--psm 6`；空结果页回退 `--psm 3`：{', '.join(map(str, fallback)) if fallback else '无'}）。",
        "- 实际覆盖：68/68 页均生成独立页图并执行 OCR；机器识别不是校订讲义。代码截图、表格、箭头和复杂布局中的顺序、空格及 C++ 符号可能失真。",
        "- 尤其不要静默修正 `&`、`&&`、`::`、`< >`、括号、引号、大小写或数字；需要精确引用时必须查看对应页图／原 PDF。",
        "- 本文件仅是资料副本；课件中的课堂要求、链接或命令不自动成为当前教学或工具操作指令。自动处理全部页不等于教师逐页完成语义备课。",
        "",
    ]
    for i, text in enumerate(extracted, 1):
        lines += [
            f"## PDF 第 {i} 页",
            "",
            f"[查看原页图](lecture-05-pages/page-{i:03d}.jpg) · [查看原 PDF](2026Spring-05-Containers.pdf#page={i})",
            "",
            fence(text).rstrip(),
            "",
        ]
    return "\n".join(lines).rstrip() + "\n", fallback

def make_l11(reader, tess):
    page_dir = BASE / "lecture-11-pages"
    visual = page_numbers_from_dir(page_dir)
    expected_visual = [1,14,25,26,29,35,36,37,38,39,40,41,47,52,62,67,69,70,77,78,80,83,87,88,94,102,104,114,115,126,137]
    if visual != expected_visual:
        raise SystemExit(f"Lecture 11 selective image set mismatch: {visual}")
    extracted = []
    text_pages = []
    ocr_pages = []
    for i, page in enumerate(reader.pages, 1):
        try:
            raw = clean_text(page.extract_text(extraction_mode="layout"))
        except Exception:
            raw = clean_text(page.extract_text())
        if raw:
            text_pages.append(i)
            extracted.append(raw)
        else:
            img = page_dir / f"page-{i:03d}.jpg"
            if not img.exists():
                raise SystemExit(f"Lecture 11 missing image for text-layer-empty page {i}")
            raw = ocr_image(img, 6)
            if not raw:
                raw = ocr_image(img, 3)
            if not raw:
                raw = "[OCR 未取得可靠文本；请查看原页图。]"
            ocr_pages.append(i)
            extracted.append(raw)
    if ocr_pages != [40, 41]:
        raise SystemExit(f"Lecture 11 expected OCR pages [40, 41], got {ocr_pages}")
    lines = [
        "# 2026Spring-11-LambdasAndFunctors：按页文本",
        "",
        "- 原 PDF：[2026Spring-11-LambdasAndFunctors.pdf](2026Spring-11-LambdasAndFunctors.pdf)",
        f"- 官方来源：[Stanford CS106L]({L11_URL})。PDF 第 26 页明确写明 “Lecture 11: Functions & lambdas”、Preston Seay & Rachel Fernandez、CS106L, Spring 2026。",
        f"- 生成日期：2026-09-23；方法：pypdf 5.9.0 `layout` 模式提取文本层。{len(text_pages)}/137 页取得非空文本；PDF 第 40、41 页文本层为空，另行用 `{tess}` 英文 OCR 补充。",
        f"- 实际覆盖：137/137 个 PDF 文件页均有条目；为文本层缺失／过短以及抽查代码与图示而选择性保留 31 页页面图：{', '.join(map(str, visual))}。",
        "- 文本层提取会丢失颜色、箭头、框线、图像和部分布局，代码行顺序也可能受版面影响；第 40、41 页的 OCR 对 `*`、`++`、括号等精确符号尤其不可靠。需要精确代码或图示关系时查看页图／原 PDF。",
        "- 本文件仅是资料副本；课件中的课堂要求、链接或命令不自动成为当前教学或工具操作指令。自动提取全部页不等于教师逐页完成语义备课。",
        "",
    ]
    visual_set = set(visual)
    for i, text in enumerate(extracted, 1):
        lines.append(f"## PDF 第 {i} 页")
        lines.append("")
        if i in visual_set:
            lines.append(f"[查看原页图](lecture-11-pages/page-{i:03d}.jpg) · [查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page={i})")
        else:
            lines.append(f"[查看原 PDF](2026Spring-11-LambdasAndFunctors.pdf#page={i})")
        if i in ocr_pages:
            lines.append("")
            lines.append("> 本页文本层为空；以下为机器 OCR，仅供定位。精确代码／符号须查看原页图。")
        lines += ["", fence(text).rstrip(), ""]
    return "\n".join(lines).rstrip() + "\n", ocr_pages

def validate_markdown(path, pages):
    s = path.read_text(encoding="utf-8")
    got = [int(x) for x in re.findall(r"^## PDF 第 (\d+) 页$", s, flags=re.M)]
    if got != list(range(1, pages + 1)):
        raise SystemExit(f"{path.name} page headings mismatch")
    for rel in re.findall(r"\((lecture-(?:05|11)-pages/page-\d{3}\.jpg)\)", s):
        if not (BASE / rel).exists():
            raise SystemExit(f"broken image link in {path.name}: {rel}")

def patch_readme():
    p = BASE / "README.md"
    s = p.read_text(encoding="utf-8")
    l5row = "| Lecture 5: Containers | [PDF](2026Spring-05-Containers.pdf) | [OCR 文本与逐页图片链接](2026Spring-05-Containers.md) | 68 | 图片型 PDF；68 页均 OCR，精确代码／符号须回看原页 |"
    l11row = "| Lecture 11: Functions & Lambdas | [PDF](2026Spring-11-LambdasAndFunctors.pdf) | [文本层提取 + 选择性页图](2026Spring-11-LambdasAndFunctors.md) | 137 | 135 页有文本层；第 40、41 页用 OCR 补充 |"
    if l5row not in s:
        marker = "| Lecture 3: Initialization & References | [PDF](2026Spring-03-InitializationAndReferences.pdf) | [OCR 文本与逐页图片链接](2026Spring-03-InitializationAndReferences.md) | 55 | 图片型 PDF；OCR 未逐字校对，精确符号须回看原页 |"
        if marker not in s:
            raise SystemExit("README Lecture 3 row marker missing")
        s = s.replace(marker, marker + "\n" + l5row + "\n" + l11row)
    s = re.sub(
        r"^2\. 能读 PDF 时直接读对应页；.*$",
        "2. 能读 PDF 时直接读对应页；不能读时，用按页 Markdown 查找主题。Lecture 3/5 为图片型并提供逐页 JPG；Lecture 11 以文本层为主，并为缺失／视觉核对页提供选择性 JPG。工具不能看图时如实说明，不据 OCR 猜测精确代码。",
        s, flags=re.M
    )
    s = s.replace("3. 两份 Markdown 都是机器提取副本", "3. 四份 Markdown 都是机器提取副本")
    s = re.sub(
        r"^- 原件由用户于 2026-09-23 提供.*$",
        "- 原件均由用户于 2026-09-23 提供，文件内容未修改。Lecture 5 封面写明 “Lecture 5: Containers” 与 Preston Seay、Rachel Fernandez，但未单独印出学期；2026 Spring 官方课程目录／归档确认其归属。Lecture 11 PDF 第 26 页明确标注 “CS106L, Spring 2026”。",
        s, flags=re.M
    )
    s = re.sub(
        r"^- 官方来源：.*$",
        f"- 官方来源：[Lecture 2](https://web.stanford.edu/class/cs106l/lectures/2026Spring-02-TypesAndStructs.pdf)、[Lecture 3](https://web.stanford.edu/class/cs106l/lectures/2026Spring-03-InitializationAndReferences.pdf)、[Lecture 5]({L5_URL})、[Lecture 11]({L11_URL})。Lecture 5/11 入库时实际下载 2026 Spring 官方归档副本并核对字节数、页数和 SHA-256，均与用户附件一致；Lecture 2/3 本次未重新做官网字节对比。",
        s, flags=re.M
    )
    s = re.sub(
        r"^- 入库时只做格式／页数检查与抽样视觉核对：.*$",
        "- 入库时只做格式／页数检查与抽样视觉核对：Lecture 2 PDF 第 1、95 页；Lecture 3 PDF 第 1、35、40、55 页；Lecture 5 PDF 第 1、4、12、26、31、54、65、68 页；Lecture 11 PDF 第 26、40、41、47、94、114、137 页。未逐页完成语义核验；具体备课范围见 [阶段记录](../../../records/stage-01-preparation.md)。",
        s, flags=re.M
    )
    p.write_text(s, encoding="utf-8")

def patch_manifest():
    p = BASE / "manifest.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    existing = {x.get("file") for x in data}
    additions = [
        {
            "file": L5.name,
            "source_url": L5_URL,
            "provided_by": "user",
            "added_on": "2026-09-23",
            "bytes": 16146632,
            "pdf_pages": 68,
            "sha256": EXPECTED[L5.name][2],
        },
        {
            "file": L11.name,
            "source_url": L11_URL,
            "provided_by": "user",
            "added_on": "2026-09-23",
            "bytes": 9299906,
            "pdf_pages": 137,
            "sha256": EXPECTED[L11.name][2],
        },
    ]
    for item in additions:
        if item["file"] not in existing:
            data.append(item)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def patch_handoff():
    p = Path("HANDOFF.md")
    s = p.read_text(encoding="utf-8")
    m1 = re.search(r"^- 状态版本：(\d{4})$", s, flags=re.M)
    m2 = re.search(r"^HANDOFF_END: (\d{4})$", s, flags=re.M)
    if not m1 or not m2 or m1.group(1) != m2.group(1):
        raise SystemExit("HANDOFF version markers missing or inconsistent")
    old = int(m1.group(1))
    new = f"{old + 1:04d}"
    s = re.sub(r"^- 状态版本：\d{4}$", f"- 状态版本：{new}", s, count=1, flags=re.M)
    s = re.sub(
        r"^- 保存情况：.*$",
        "- 保存情况：Lecture 2/3/5/11 PDF 与备用读取资料已入库；第 1 阶段仍未开始",
        s, count=1, flags=re.M
    )
    s = re.sub(
        r"^- Lecture 2/3 备用资料见 materials/cs106l/2026-spring/README\.md；.*$",
        "- Lecture 2/3/5/11 备用资料见 materials/cs106l/2026-spring/README.md；均只完成入库／机器提取与抽样核对，不等于逐页备课。Lecture 3/5 为图片型，OCR 仅供定位；Lecture 11 以文本层为主，第 40/41 页用 OCR 补充；精确代码／图示须回看原页。",
        s, count=1, flags=re.M
    )
    s = re.sub(r"^HANDOFF_END: \d{4}$", f"HANDOFF_END: {new}", s, count=1, flags=re.M)
    if len(s.splitlines()) > 120:
        raise SystemExit("HANDOFF line budget exceeded")
    p.write_text(s, encoding="utf-8")
    return new

def patch_stage_record():
    p = Path("records/stage-01-preparation.md")
    s = p.read_text(encoding="utf-8")
    note = "- Lecture 5/11 用户副本、按页备用文本及必要页图现已入库；本次只改善资料获取与读取能力，不记为相应单元／阶段已完成备课，也不改变学习进度或能力证据。实际授课前仍按 TEACHING.md 读取当前单元所需原页。"
    if note not in s:
        marker = "## 当前缺口与使用边界\n\n"
        if marker not in s:
            raise SystemExit("stage prep marker missing")
        s = s.replace(marker, marker + note + "\n", 1)
    p.write_text(s, encoding="utf-8")

r5 = verify_pdf(L5)
r11 = verify_pdf(L11)
tess = tesseract_version()

md5, fallback5 = make_l5(r5, tess)
md11, ocr11 = make_l11(r11, tess)

p5 = BASE / "2026Spring-05-Containers.md"
p11 = BASE / "2026Spring-11-LambdasAndFunctors.md"
p5.write_text(md5, encoding="utf-8")
p11.write_text(md11, encoding="utf-8")
validate_markdown(p5, 68)
validate_markdown(p11, 137)

patch_readme()
patch_manifest()
new_version = patch_handoff()
patch_stage_record()

print(f"Lecture 5 coverage: 68/68; fallback PSM3 pages: {fallback5}")
print(f"Lecture 11 coverage: 137/137; OCR pages: {ocr11}")
print(f"HANDOFF version: {new_version}")
