#!/usr/bin/env python3
"""M4: assemble story/STORY.md, the generated final file: the title, the story (the named draft with its front matter
stripped), and the colophon for the human — word count, the exemplar set the story was measured against, the comparison
records with their results, the count of full-text against from-memory verdicts, and what is unfinished.
Usage: make_story.py <kit> <draft-NN> "<title>" [--title-status "<how the title was chosen>"] [--unfinished "<text>"]"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]) / "checks"))
from common import split_front_matter, word_count
args = sys.argv[1:]
def opt(name):
    if name in args:
        i = args.index(name); v = args[i + 1]; del args[i:i + 2]; return v
    return ""
title_status = opt("--title-status"); unfinished = opt("--unfinished")
kit, draft, title = args[0], args[1], args[2]
K = Path(kit)
_, body = split_front_matter((K / "story/drafts" / f"{draft}.md").read_text(encoding="utf-8"))
body = body.strip("\n")
n = word_count(body)
rows, full, mem, exemplars = [], 0, 0, set()
for f in sorted((K / "reviews/comparisons").glob("round-*.json")):
    r = json.loads(f.read_text(encoding="utf-8"))
    pairs = r["pairs"] + (r.get("baseline_signed") or {}).get("pairs", [])   # the signed-draft baseline counts too
    for e in pairs:
        if e.get("from_memory"): mem += 1
        else: full += 1
    kind = ("revision, against the draft before it and against the draft the human signed" if r.get("baseline_signed") else "revision") if "previous" in r else "exemplar"
    by = {}
    for e in pairs:
        won = (e["order"] == "AB" and e["choice"] == "A") or (e["order"] == "BA" and e["choice"] == "B")
        by.setdefault((e["exemplar"], e["dimension"]), []).append(won)
        if kind == "exemplar": exemplars.add(e["exemplar"])
    parts = []
    for (ex, dim), v in by.items():
        res = "won" if all(v) else "lost" if not any(v) else "tie"
        parts.append(f"{dim} against {ex}: {res} ({sum(v)} of {len(v)} verdicts)")
    cal = r.get("calibration", {})
    rows.append(f"- `{f.name}` on {r['draft']} ({kind}; judges {', '.join(sorted(cal.get('verdicts', {}).keys()))}, calibration {'passed' if cal.get('passed') else 'failed'}): " + "; ".join(parts))
colophon = [
    "", "---", "", "## Colophon", "",
    "For the human, not for a reader of the story.", "",
    f"- Word count: {n} (the draft is `story/drafts/{draft}.md`).",
    f"- Title: {title_status or 'as given above'}.",
    "- Exemplar set it was measured against, all supplied as full text: " + ", ".join(sorted(exemplars)) + ".",
    "- Comparison records (`reviews/comparisons/`):",
] + ["  " + r for r in rows] + [
    f"- Verdicts on supplied text: {full}; from memory: {mem}.",
]
if unfinished:
    colophon += ["- Unfinished: " + unfinished]
out = f"# {title}\n\n{body}\n" + "\n".join(colophon) + "\n"
(K / "story/STORY.md").write_text(out, encoding="utf-8")
print(f"{K/'story/STORY.md'}: {n} words of story; {full} full-text and {mem} from-memory verdicts over {len(rows)} records")
