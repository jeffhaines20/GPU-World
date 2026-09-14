#!/usr/bin/env python3
"""Parse the questions-funnel review files into a scores JSON and a per-card critique file.
Usage: parse_reviews.py <out-scores.json> <out-critiques.md> <review files...>
A review file holds lines 'Q-NN | importance=N | rigour=N | novelty=N | arguability=N | story=N' followed by six
reason lines (five axes and 'weakest step'). The reviewer name is taken from the file name (review-a-*, review-b-*)."""
import re, sys, json
from pathlib import Path
out_scores, out_crit, *files = sys.argv[1:]
scores, crit = {}, {}
for f in files:
    judge = "reviewer-" + re.search(r"review-([ab])", Path(f).name).group(1)
    lines = Path(f).read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^(Q-\d\d) \| importance=(\d) \| rigour=(\d) \| novelty=(\d) \| arguability=(\d) \| story=(\d)", lines[i].strip())
        if m:
            c = m.group(1)
            scores.setdefault(judge, {})[c] = {k: int(v) for k, v in zip(("importance","rigour","novelty","arguability","story"), m.groups()[1:])}
            block = []
            j = i + 1
            while j < len(lines) and not re.match(r"^(Q-\d\d) \| |^MOST |^DOES NOT", lines[j].strip()):
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
            fh.write(f"### {judge} — importance {s['importance']}, rigour {s['rigour']}, novelty {s['novelty']}, arguability {s['arguability']}, story {s['story']}\n\n{crit[c][judge]}\n\n")
print({j: len(v) for j, v in scores.items()}, "cards with critiques:", len(crit))
