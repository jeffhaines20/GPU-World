#!/usr/bin/env python3
"""Orchestrator convenience for M1: write a judge's batch file holding only the named cards (and their probes,
where a probe file exists), so that a premise-judge sees its batch and nothing else of PREMISES.md.
Usage: make_batch.py <PREMISES.md> <outfile> <probes-dir-or-'-'> P-03 P-17 ...
Cards are written in the order given (the orchestrator shuffles). Each card's "Closest published" and
"Status" lines are kept; nothing else is added."""
import re, sys
from pathlib import Path
src, out, probes, *ids = sys.argv[1:]
text = Path(src).read_text(encoding="utf-8")
cards = {m.group(1): m.group(0) for m in re.finditer(r"^### (P-\d\d) — cell \d — .*?(?=^### P-\d\d — |\Z)", text, re.M | re.S)}
parts = []
for i in ids:
    if i not in cards:
        sys.exit(f"no card {i}")
    card = cards[i].strip()
    if probes != "-":
        pf = Path(probes) / f"{i}.md"
        if pf.exists():
            card += "\n\nProbe passage (250-350 words of the hardest passage, written from the card):\n\n" + pf.read_text(encoding="utf-8").strip()
    parts.append(card)
Path(out).write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
print(f"{out}: {len(ids)} cards, {len(Path(out).read_text().split())} words")
