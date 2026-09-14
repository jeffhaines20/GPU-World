#!/usr/bin/env python3
"""Ranking for the questions-first funnel (design/questions/FRAME.md). Same shape as rank_premises.py, five axes:
importance, rigour, novelty, arguability, story. Usage: rank_questions.py scores.json cells.json"""
import json, statistics, sys
scores = json.load(open(sys.argv[1])); cells = json.load(open(sys.argv[2]))
judges = list(scores)
totals = {j: {c: float(sum(a.values())) for c, a in scores[j].items()} for j in judges}
medians = {j: statistics.median(totals[j].values()) for j in judges}
cards = sorted({c for j in judges for c in scores[j]})
rows = []
for c in cards:
    ts = [totals[j][c] for j in judges if c in totals[j]]
    shrunk = [(t + medians[j]) / 2 for j, t in zip(judges, ts)]
    rows.append((c, statistics.mean(shrunk), max(ts), ts, (max(ts) - min(ts) >= 5) if len(ts) > 1 else False))
print("Ranking A (shrunk):")
for c, a, b, ts, d in sorted(rows, key=lambda r: -r[1]):
    print(f"  {c} cell {cells.get(c,'?')}: {a:5.1f}   raw {', '.join(f'{t:.0f}' for t in ts)}{'   DISPUTED' if d else ''}")
print("Ranking B (highest single):")
for c, a, b, ts, d in sorted(rows, key=lambda r: -r[2])[:12]:
    print(f"  {c}: {b:.0f}")
print("medians", {j: medians[j] for j in judges})
