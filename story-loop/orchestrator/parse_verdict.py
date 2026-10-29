#!/usr/bin/env python3
"""M3: turn a craft-critic's reply (the shape the orchestrator's judge prompt asks for) into one entry of a comparison
record. Usage: parse_verdict.py <reply.md> <exemplar> <dimension> <order AB|BA> <judge> [from_memory]
Prints the JSON entry; the orchestrator assembles the round file. Fails if any required field is missing."""
import re, sys, json
from pathlib import Path
reply, exemplar, dimension, order, judge, *rest = sys.argv[1:]
t = Path(reply).read_text(encoding="utf-8")
def f(k, required=True):
    m = re.search(rf"^{k}:\s*(.+)$", t, re.M)
    if not m and required: sys.exit(f"{reply}: missing {k}")
    return m.group(1).strip() if m else None
choice = f("CHOICE").strip("* ").upper()[:1]
if choice not in ("A", "B"): sys.exit(f"{reply}: choice is {choice!r}")
e = {"exemplar": exemplar, "dimension": dimension, "order": order, "choice": choice,
     "from_memory": bool(rest and rest[0] == "from_memory"), "judge": judge,
     "confidence": int(re.search(r"\d", f("CONFIDENCE")).group(0)),
     "reason": f("REASON"), "evidence": "A: " + f("EVIDENCE A") + " | B: " + f("EVIDENCE B"), "needs": f("NEEDS")}
lost = f("LOST", required=False)
if lost: e["lost"] = lost
for k in ("reason", "evidence", "needs"):
    if not e[k].strip(): sys.exit(f"{reply}: empty {k}")
print(json.dumps(e, ensure_ascii=False, indent=1))
