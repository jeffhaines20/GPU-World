#!/usr/bin/env python3
"""Questions funnel: assemble the offer to the human from a round's scores.
Usage: present_top.py <REVISED.md> <scores.json> <cells.json> <critiques.md> <CHANGES.md> <N> <review files...>
Ranking A as in rank_questions.py (each reviewer's total pulled halfway toward that reviewer's pool median, then the
mean); ties on A broken as FRAME.md declares: cell coverage (a cell not yet in the offer wins), then the reviewers'
MOST IMPORTANT picks, then importance plus novelty. Prints markdown: the ranking of every card, the batch verdicts,
then the top N cards in full with both reviewers' scores and weakest steps and the reviser's note of what changed."""
import re, sys, json, statistics
from pathlib import Path
revised, scores_f, cells_f, crit_f, changes_f, n, *reviews = sys.argv[1:]
n = int(n)
scores = json.load(open(scores_f)); cells = json.load(open(cells_f))
text = Path(revised).read_text(encoding="utf-8")
cards = {m.group(1): m.group(0).strip() for m in re.finditer(r"^### (Q-\d\d) — cell [A-Za-z0-9]+ — .*?(?=^### Q-\d\d — |\Z)", text, re.M | re.S)}
titles = {m.group(1): m.group(2) for m in re.finditer(r"^### (Q-\d\d) — cell [A-Za-z0-9]+ — (.+)$", text, re.M)}
crit = {}
for m in re.finditer(r"^## (Q-\d\d)\n(.*?)(?=^## Q-\d\d\n|\Z)", Path(crit_f).read_text(encoding="utf-8"), re.M | re.S):
    crit[m.group(1)] = m.group(2).strip()
changes = {m.group(1): m.group(2).strip() for m in re.finditer(r"^## (Q-\d\d) — .*?\n(.*?)(?=^## Q-\d\d — |\Z)", Path(changes_f).read_text(encoding="utf-8"), re.M | re.S)}
verdicts, most_imp = [], {}
for f in reviews:
    t = Path(f).read_text(encoding="utf-8")
    name = Path(f).stem.replace("review-", "reviewer ")
    for kind in ("MOST IMPORTANT", "MOST NOVEL", "DOES NOT SURVIVE"):
        m = re.search(rf"^{kind}:\s*(.+)$", t, re.M)
        if m:
            verdicts.append((name, kind, m.group(1).strip()))
            if kind == "MOST IMPORTANT":
                q = re.search(r"Q-\d\d", m.group(1))
                if q: most_imp[q.group(0)] = most_imp.get(q.group(0), 0) + 1
judges = list(scores)
totals = {j: {c: sum(a.values()) for c, a in scores[j].items()} for j in judges}
medians = {j: statistics.median(totals[j].values()) for j in judges}
ids = sorted({c for j in judges for c in scores[j]})
rankA = {c: statistics.mean((totals[j][c] + medians[j]) / 2 for j in judges if c in totals[j]) for c in ids}
impnov = {c: sum(scores[j][c]["importance"] + scores[j][c]["novelty"] for j in judges if c in scores[j]) for c in ids}
# selection with the declared tie-breaks
chosen = []
remaining = sorted(ids, key=lambda c: -rankA[c])
while len(chosen) < n and remaining:
    top = rankA[remaining[0]]
    tied = [c for c in remaining if abs(rankA[c] - top) < 1e-9]
    if len(tied) > 1 and len(chosen) + len(tied) > n:
        covered = {cells[c] for c in chosen}
        tied.sort(key=lambda c: (cells[c] in covered, -most_imp.get(c, 0), -impnov[c]))
        print(f"<!-- tie at {top:.1f} among {', '.join(tied)}: broken by cell coverage, most-important picks, importance+novelty -->")
    for c in tied:
        if len(chosen) < n:
            chosen.append(c); remaining.remove(c)
print("## Ranking of the eleven revised cards (round 2)\n")
print("| Rank | Card | Cell | Ranking A | Raw totals (of 25) | Note |")
print("|---|---|---|---|---|---|")
order = chosen + [c for c in remaining]
for i, c in enumerate(order, 1):
    ts = [totals[j][c] for j in judges if c in totals[j]]
    d = "disputed" if len(ts) > 1 and max(ts) - min(ts) >= 5 else ""
    print(f"| {i} | {c} {titles.get(c, '')} | {cells[c]} | {rankA[c]:.1f} | {', '.join(str(t) for t in ts)} | {d} |")
print(f"\nReviewer pool medians: " + ", ".join(f"{j} {medians[j]:g}" for j in judges) + ".\n")
print("## The reviewers' batch verdicts\n")
for name, kind, v in verdicts:
    print(f"- {name}, {kind.lower()}: {v}")
print(f"\n## The top {n}, in full\n")
for c in chosen:
    print(cards[c] + "\n")
    print(f"**Round-2 reviewers on {c}.**\n")
    print(crit.get(c, "(no critique parsed)") + "\n")
    print(f"**What the reviser changed.** {changes.get(c, '(no note)')}\n")
    print("---\n")
