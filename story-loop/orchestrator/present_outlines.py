#!/usr/bin/env python3
"""Outline pass: assemble the ranking offered to the human after round 2.
Usage: present_outlines.py <revised-dir> <scores-round1.json> <scores-round2.json> <critiques-round2.md> <review-round2 files...>
Ranking A as in rank_outlines.py (seven axes of 35; each reviewer's total pulled halfway toward that reviewer's median,
then the mean); ties broken by the reviewers' read-to-the-end picks, then question plus surprise (FRAME.md). Prints
markdown: the final ranking with round-1 positions, the round-2 verdicts, then every revised outline in full with both
round-2 critiques and the reviser's note of what changed."""
import re, sys, json, statistics
from pathlib import Path
rdir, s1_f, s2_f, crit_f, *reviews = sys.argv[1:]
s1, s2 = json.load(open(s1_f)), json.load(open(s2_f))
def rankA(scores):
    judges = list(scores)
    totals = {j: {c: sum(a.values()) for c, a in scores[j].items()} for j in judges}
    med = {j: statistics.median(totals[j].values()) for j in judges}
    ids = sorted({c for j in judges for c in scores[j]})
    return {c: statistics.mean((totals[j][c] + med[j]) / 2 for j in judges if c in totals[j]) for c in ids}, totals, med
A1, _, _ = rankA(s1); A2, T2, med2 = rankA(s2)
judges = list(s2)
verdicts, read_end = [], {}
for f in reviews:
    t = Path(f).read_text(encoding="utf-8"); name = "reviewer " + re.search(r"review-(?:round\d-)?([ab])", Path(f).name).group(1)
    for kind in ("READ TO THE END", "MOST SURPRISING", "DOES NOT SURVIVE"):
        m = re.search(rf"^{kind}:\s*(.+)$", t, re.M)
        if m:
            verdicts.append((name, kind, m.group(1).strip()))
            if kind == "READ TO THE END":
                q = re.search(r"O-\d", m.group(1))
                if q: read_end[q.group(0)] = read_end.get(q.group(0), 0) + 1
qs = {c: sum(s2[j][c]["question"] + s2[j][c]["surprise"] for j in judges if c in s2[j]) for c in A2}
order = sorted(A2, key=lambda c: (-A2[c], -read_end.get(c, 0), -qs[c]))
r1order = sorted(A1, key=lambda c: -A1[c])
cards, titles, notes = {}, {}, {}
for f in sorted(Path(rdir).glob("O-*.md")):
    t = f.read_text(encoding="utf-8"); parts = re.split(r"^## What changed\s*$", t, flags=re.M)
    cards[f.stem] = parts[0].strip(); notes[f.stem] = parts[1].strip() if len(parts) > 1 else "(no note)"
    titles[f.stem] = re.match(r"^### O-\d — (.+)$", t.splitlines()[0]).group(1)
crit = {m.group(1): m.group(2).strip() for m in re.finditer(r"^## (O-\d)\n(.*?)(?=^## O-\d\n|\Z)", Path(crit_f).read_text(encoding="utf-8"), re.M|re.S)}
print("## The final ranking (round 2, revised outlines)\n")
print("| Rank | Outline | Ranking A (of 35) | Raw totals | Round-1 rank | Round-1 A |")
print("|---|---|---|---|---|---|")
for i, c in enumerate(order, 1):
    ts = [T2[j][c] for j in judges if c in T2[j]]
    d = " (disputed)" if len(ts) > 1 and max(ts) - min(ts) >= 7 else ""
    print(f"| {i} | {c} {titles.get(c, '')} | {A2[c]:.1f}{d} | {', '.join(str(int(t)) for t in ts)} | {r1order.index(c) + 1} | {A1[c]:.1f} |")
print(f"\nReviewer pool medians in round 2: " + ", ".join(f"{j} {med2[j]:g}" for j in judges) + ".\n")
print("## The round-2 verdicts\n")
for name, kind, v in verdicts:
    print(f"- {name}, {kind.lower()}: {v}")
print("\n## The five revised outlines, in ranked order\n")
for c in order:
    print(cards[c] + "\n")
    print(f"**Round-2 reviewers on {c}.**\n")
    print(crit.get(c, "(no critique parsed)") + "\n")
    print(f"**What the reviser changed.** {notes[c]}\n")
    print("---\n")
