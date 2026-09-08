#!/usr/bin/env python3
"""Orchestrator convenience for M1: the two rankings PARTITIONS.md declares, from a scores file.
Input: a JSON file {"judge-a": {"P-01": {"idea":4,"person":3,"turn":5,"prose":null,"aftertaste":4}, ...}, "judge-b": {...}}
A card's total per judge is the sum of scored axes scaled to 25 (an unscored axis, e.g. prose with no probe,
is left out and the rest scaled up). Ranking A: each judge's total pulled halfway toward that judge's pool
median, then the mean over judges. Ranking B: the highest single-judge total. Disputed: totals differ by 5+.
Usage: rank_premises.py scores.json [cells.json]   (cells.json maps P-NN -> cell number, for the two-per-cell rule)"""
import json, statistics, sys
scores = json.load(open(sys.argv[1]))
cells = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
judges = list(scores)
def total(axes):
    vals = [v for v in axes.values() if isinstance(v, (int, float))]
    return 25.0 * sum(vals) / (5 * len(vals)) if vals else None
totals = {j: {c: total(a) for c, a in scores[j].items()} for j in judges}
medians = {j: statistics.median([t for t in totals[j].values() if t is not None]) for j in judges}
cards = sorted({c for j in judges for c in scores[j]})
rows = []
for c in cards:
    ts = [totals[j].get(c) for j in judges]
    ts = [t for t in ts if t is not None]
    shrunk = [(t + medians[j]) / 2 for j, t in zip(judges, ts)]
    a = statistics.mean(shrunk); b = max(ts)
    disputed = (max(ts) - min(ts) >= 5) if len(ts) > 1 else False
    rows.append((c, a, b, ts, disputed))
print("Ranking A (shrunk toward each judge's median):")
for c, a, b, ts, d in sorted(rows, key=lambda r: -r[1]):
    print(f"  {c} cell {cells.get(c,'?')}: {a:5.1f}   raw {', '.join(f'{t:.1f}' for t in ts)}{'   DISPUTED' if d else ''}")
print("Ranking B (highest single-judge total):")
for c, a, b, ts, d in sorted(rows, key=lambda r: -r[2]):
    print(f"  {c} cell {cells.get(c,'?')}: {b:5.1f}")
print("Judge medians:", {j: round(m, 1) for j, m in medians.items()})
