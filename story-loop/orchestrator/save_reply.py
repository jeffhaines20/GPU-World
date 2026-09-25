#!/usr/bin/env python3
"""Orchestrator convenience: copy an agent's final reply, verbatim, out of its JSONL transcript into a file.
Usage: save_reply.py <transcript.output> <dest> [<must-contain>]
Takes the last assistant text block in the transcript, or the last SubagentHandback message (optionally the last one
containing <must-contain>). The text is copied unchanged."""
import json, sys
from pathlib import Path
src, dest = sys.argv[1], sys.argv[2]
must = sys.argv[3] if len(sys.argv) > 3 else None
found = None
def texts(o):
    if isinstance(o, dict):
        if o.get("type") == "text" and isinstance(o.get("text"), str):
            yield o["text"]
        # an agent that hands its report back through the harness's SubagentHandback call puts the text in the call's input
        if o.get("type") == "tool_use" and o.get("name") == "SubagentHandback" and isinstance(o.get("input"), dict) \
                and isinstance(o["input"].get("message"), str):
            yield o["input"]["message"]
        for v in o.values():
            yield from texts(v)
    elif isinstance(o, list):
        for v in o:
            yield from texts(v)
for line in Path(src).read_text(encoding="utf-8").splitlines():
    try:
        obj = json.loads(line)
    except Exception:
        continue
    for t in texts(obj):
        if must is None or must in t:
            found = t
if not found:
    sys.exit("no reply text found")
Path(dest).write_text(found.strip() + "\n", encoding="utf-8")
print(f"{dest}: {len(found.split())} words")
