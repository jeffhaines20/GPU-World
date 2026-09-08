#!/usr/bin/env python3
"""Orchestrator convenience: write an anonymized A/B pair for a judge.
Usage: make_pair.py <text-for-A> <text-for-B> <outdir> <label>
Strips a draft's front matter (the key: value lines between --- fences) and any leading markdown title
line, so that neither file carries a name, a byline, a draft number, or a path that says where it came from.
Writes <outdir>/<label>-A.txt and <outdir>/<label>-B.txt and prints their word counts."""
import re, sys
from pathlib import Path

def clean(path):
    t = Path(path).read_text(encoding="utf-8")
    m = re.match(r"\A(?:---\n)?((?:[a-z_]+:.*\n)+)(?:---\n)?", t)
    if m:
        t = t[m.end():]
    t = t.lstrip("\n")
    lines = t.split("\n")
    if lines and lines[0].startswith("#"):
        t = "\n".join(lines[1:]).lstrip("\n")
    return t.strip() + "\n"

a, b, out, label = sys.argv[1:5]
Path(out).mkdir(parents=True, exist_ok=True)
for letter, src in (("A", a), ("B", b)):
    text = clean(src)
    p = Path(out) / f"{label}-{letter}.txt"
    p.write_text(text, encoding="utf-8")
    print(f"{p}: {len(text.split())} words")
