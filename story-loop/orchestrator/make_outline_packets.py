#!/usr/bin/env python3
"""Outline pass: build one revision packet per outline: the outline as it stands, both reviewers' critiques of it, and the
originality critic's reading of it and any finding naming it. Nothing else goes in.
Usage: make_outline_packets.py <outlines-dir> <critiques.md> <REV-03.md> <out-dir> O-1 O-2 ..."""
import re, sys
from pathlib import Path
d, crit_f, rev_f, out, *ids = sys.argv[1:]
crit = {m.group(1): m.group(2).strip() for m in re.finditer(r"^## (O-\d)\n(.*?)(?=^## O-\d\n|\Z)", Path(crit_f).read_text(encoding="utf-8"), re.M|re.S)}
rev = Path(rev_f).read_text(encoding="utf-8")
reading = {m.group(1): m.group(0).strip() for m in re.finditer(r"^\*\*(O-\d) [^*]*\*\*.*?(?=^\*\*O-\d |^\*\*Between|^## |\Z)", rev, re.M|re.S)}
between = re.search(r"^\*\*Between the outlines\.\*\*.*?(?=^## |\Z)", rev, re.M|re.S)
findings = re.findall(r"^(F\d+: .*)$", rev, re.M)
Path(out).mkdir(exist_ok=True)
for i in ids:
    o = re.split(r"^## What changed\s*$", (Path(d)/f"{i}.md").read_text(encoding="utf-8"), flags=re.M)[0].strip()
    fs = [f for f in findings if i in f]
    body = [f"# Revision packet for {i}", "", "## The outline as it stands", "", o, "", "## The two reviewers' critiques of this outline", "",
            crit.get(i, "(no critique parsed)"), "", "## The originality critic on this outline", "", reading.get(i, "(no reading found)")]
    if between: body += ["", between.group(0).strip()]
    body += ["", "Findings naming this outline:"] + ([f"- {f}" for f in fs] or ["- none"])
    Path(out, f"{i}-packet.md").write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"{i}: packet {len(' '.join(body).split())} words, {len(fs)} finding(s)")
