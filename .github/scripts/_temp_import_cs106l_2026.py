#!/usr/bin/env python3
import hashlib, shutil, urllib.request
from pathlib import Path
import fitz

BASE = Path("materials/cs106l/2026-spring")
FILES = {
    "2026Spring-05-Containers.pdf": {
        "urls":[
            "https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-05-Containers.pdf",
            "https://web.stanford.edu/class/cs106l/lectures/2026Spring-05-Containers.pdf",
        ],
        "bytes":16146632,
        "pages":68,
        "sha256":"1dad3333f05915e63e395854d027c52eac3575ee6e00a08371091e067140bc46",
    },
    "2026Spring-11-LambdasAndFunctors.pdf": {
        "urls":[
            "https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-11-LambdasAndFunctors.pdf",
            "https://web.stanford.edu/class/cs106l/lectures/2026Spring-11-LambdasAndFunctors.pdf",
        ],
        "bytes":9299906,
        "pages":137,
        "sha256":"4c40b1349fc366f05d76c1de044b3043d8644e7dc2f15ce8abcc83e15b76dd62",
    },
}
VISUAL11 = [1,14,25,26,29,35,36,37,38,39,40,41,47,52,62,67,69,70,77,78,80,83,87,88,94,102,104,114,115,126,137]

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()

def download_verified(name, meta):
    dst=BASE/name
    dst.parent.mkdir(parents=True, exist_ok=True)
    errors=[]
    for url in meta["urls"]:
        try:
            req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=180) as r, open(dst,"wb") as f:
                shutil.copyfileobj(r,f)
            size=dst.stat().st_size
            digest=sha256(dst)
            doc=fitz.open(dst)
            pages=len(doc)
            doc.close()
            if (size,digest,pages)!=(meta["bytes"],meta["sha256"],meta["pages"]):
                errors.append(f"{url}: verification mismatch size={size} sha256={digest} pages={pages}")
                continue
            print(f"verified {name} from {url}: {size} bytes, {pages} pages, {digest}")
            return
        except Exception as e:
            errors.append(f"{url}: {type(e).__name__}: {e}")
    raise SystemExit("all download candidates failed for "+name+"\n" + "\n".join(errors))

def render(pdf_name, out_dir, page_numbers):
    doc=fitz.open(BASE/pdf_name)
    out=BASE/out_dir
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    for n in page_numbers:
        p=doc[n-1]
        scale=2000/max(p.rect.width,p.rect.height)
        pix=p.get_pixmap(matrix=fitz.Matrix(scale,scale), alpha=False)
        pix.save(out/f"page-{n:03d}.jpg", jpg_quality=88)
    doc.close()
    got=sorted(int(p.stem.split("-")[1]) for p in out.glob("page-*.jpg"))
    if got!=list(page_numbers):
        raise SystemExit(f"render coverage mismatch for {out_dir}")
    print(f"rendered {len(got)} pages to {out_dir}")

BASE.mkdir(parents=True, exist_ok=True)
for name,meta in FILES.items():
    download_verified(name,meta)
render("2026Spring-05-Containers.pdf","lecture-05-pages",range(1,69))
render("2026Spring-11-LambdasAndFunctors.pdf","lecture-11-pages",VISUAL11)
