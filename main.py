import argparse,html,os
from pathlib import Path

def build(originals,restored):
    pairs=[]
    for p in sorted(originals.iterdir()):
        if p.suffix.lower() not in {".png",".jpg",".jpeg",".webp"}:continue
        q=restored/p.name
        if q.exists():pairs.append((p,q))
    if not pairs:raise ValueError("No matching image filenames")
    return pairs

def main():
    p=argparse.ArgumentParser();p.add_argument("originals");p.add_argument("restored");p.add_argument("output");a=p.parse_args()
    out=Path(a.output).resolve();pairs=build(Path(a.originals),Path(a.restored))
    rows=[]
    for before,after in pairs:
        b=html.escape(Path(os.path.relpath(before,out.parent)).as_posix(),quote=True)
        c=html.escape(Path(os.path.relpath(after,out.parent)).as_posix(),quote=True)
        rows.append(f'<section><h2>{html.escape(before.name)}</h2><img src="{b}" alt="Original"><img src="{c}" alt="Restored"></section>')
    out.write_text('<!doctype html><meta charset="utf-8"><title>Restoration Gallery</title><style>img{max-width:45%;margin:1%}section{border-bottom:1px solid #aaa}</style>'+''.join(rows),encoding="utf-8")
if __name__=="__main__":main()
