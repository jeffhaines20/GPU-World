#!/usr/bin/env python3
"""Questions funnel, round 2: compile the revisers' cards into one file that make_batch.py can cut.
Usage: compile_revised.py <revised-dir> <cells.json> <out REVISED.md> <out CHANGES.md>
Each revised/Q-NN.md holds the card (heading '### Q-NN — <title>', eight fields, 'Status: revised') and then a
'## What changed' section. The card part is copied verbatim, with the cell put back into the heading
('### Q-NN — cell X — <title>') so that make_batch.py finds it and strips it again for the reviewers. The
'What changed' notes go to a separate file the reviewers never see. Prints a check line per card: the fields
present, the card's word count, and whether the reviser's note says the card survives."""
import re, sys, json
from pathlib import Path
rdir, cells_f, out_cards, out_changes = sys.argv[1:]
cells = json.load(open(cells_f))
FIELDS = ["Implication:", "Follows from:", "For an ordinary person:", "The strongest objection:", "Either side:",
          "Not the obvious version:", "Who it lands on:", "Status:"]
cards, changes = [], []
for f in sorted(Path(rdir).glob("Q-*.md")):
    text = f.read_text(encoding="utf-8").strip()
    m = re.match(r"^### (Q-\d\d) — (.+)$", text.splitlines()[0])
    if not m:
        sys.exit(f"{f.name}: first line is not a card heading: {text.splitlines()[0]!r}")
    qid, title = m.group(1), m.group(2)
    if qid != f.stem:
        sys.exit(f"{f.name}: heading says {qid}")
    if title.startswith("cell "):   # a reviser kept the cell in; strip it so the reviewers do not see it
        title = re.sub(r"^cell [A-Za-z0-9]+ — ", "", title)
    parts = re.split(r"^## What changed\s*$", text, flags=re.M)
    card = parts[0].strip()
    note = parts[1].strip() if len(parts) > 1 else ""
    body = "\n".join(card.splitlines()[1:])
    missing = [x for x in FIELDS if not re.search(r"^" + re.escape(x), body, re.M)]
    status = re.search(r"^Status:\s*(.+)$", body, re.M)
    words = len(body.split())
    survives = "not survive" not in note.lower() and "does not survive" not in card.lower()
    print(f"{qid}: cell {cells[qid]} · {words} words · missing {missing or 'none'} · status {status.group(1) if status else '?'} · note {len(note.split())} words · reviser says {'survives' if survives else 'DOES NOT SURVIVE'}")
    cards.append(f"### {qid} — cell {cells[qid]} — {title}\n{body}")
    changes.append(f"## {qid} — {title}\n\n{note}\n")
Path(out_cards).write_text("\n\n".join(cards) + "\n", encoding="utf-8")
Path(out_changes).write_text("# What the revisers changed (round 2 reviewers do not see this)\n\n" + "\n".join(changes), encoding="utf-8")
print(f"{out_cards}: {len(cards)} cards, {len(Path(out_cards).read_text().split())} words")
