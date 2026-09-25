#!/usr/bin/env python3
"""Outline pass: write a reviewer's batch file holding the named outlines in the order given (the orchestrator shuffles).
Usage: make_outline_batch.py <outlines-dir> <outfile> O-4 O-1 ...
Each outline is copied verbatim from <outlines-dir>/O-N.md up to (not including) any '## What changed' note."""
import re, sys
from pathlib import Path
d, out, *ids = sys.argv[1:]
parts = []
for i in ids:
    t = (Path(d) / f"{i}.md").read_text(encoding="utf-8")
    t = re.split(r"^## What changed\s*$", t, flags=re.M)[0].strip()
    if not t.startswith(f"### {i} — "):
        sys.exit(f"{i}: file does not start with its heading")
    parts.append(t)
Path(out).write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
print(f"{out}: {len(ids)} outlines, {len(Path(out).read_text().split())} words")
