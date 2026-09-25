#!/usr/bin/env python3
"""Parse the outline-pass review files into a scores JSON and a per-outline critique file.
Usage: parse_outline_reviews.py <out-scores.json> <out-critiques.md> <review files...>
A review file holds lines 'O-N | question=N | surprise=N | insight=N | grip=N | person=N | ending=N | prose=N' followed
by eight reason lines (seven axes and 'largest gap'). The reviewer name is taken from the file name (review-a-*, review-b-*)."""
import re, sys, json
from pathlib import Path
AX = ("question","surprise","insight","grip","person","ending","prose")
out_scores, out_crit, *files = sys.argv[1:]
scores, crit = {}, {}
pat = r"^(O-\d) \| " + r" \| ".join(f"{a}=(\d)" for a in AX)
for f in files:
    judge = "reviewer-" + re.search(r"review-(?:round\d-)?([ab])", Path(f).name).group(1)
    lines = Path(f).read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        m = re.match(pat, lines[i].strip())
        if m:
            c = m.group(1)
            scores.setdefault(judge, {})[c] = {k: int(v) for k, v in zip(AX, m.groups()[1:])}
            block, j = [], i + 1
            while j < len(lines) and not re.match(r"^(O-\d) \| |^READ TO|^MOST |^DOES NOT", lines[j].strip()):
                if lines[j].strip(): block.append(lines[j].strip())
                j += 1
            crit.setdefault(c, {})[judge] = "\n".join(block)
            i = j
        else:
            i += 1
json.dump(scores, open(out_scores, "w"), indent=1)
with open(out_crit, "w") as fh:
    for c in sorted(crit):
        fh.write(f"## {c}\n\n")
        for judge in sorted(crit[c]):
            s = scores[judge][c]
            fh.write(f"### {judge} — " + ", ".join(f"{a} {s[a]}" for a in AX) + f" (total {sum(s.values())} of 35)\n\n{crit[c][judge]}\n\n")
print({j: len(v) for j, v in scores.items()}, "outlines with critiques:", len(crit))
