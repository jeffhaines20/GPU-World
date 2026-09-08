#!/usr/bin/env python3
"""Every promise these documents make names something that exists. Each `check_*.py`, `make <target>`,
agent name, skill name, and kit-relative path named in the design, the kit's documents, the skills, or
the agent briefs must resolve: to a file in checks/, a target in the Makefile, a file under
.claude/agents/ or .claude/skills/, or a path in the kit — unless it is listed here as created at
runtime.
Bypass attempts this check refuses: a document that says a thing is checked by a check that does not
exist; a skill that spawns an agent with no brief; a `make` target named in a document and missing from
the Makefile; a path cited in a document that is nowhere in the kit.
What it does not check: whether the check that exists does what the sentence says it does. That is the
fault suite's job for the checks, and a reviewer's for the prose.
Usage: check_claims.py"""
import re
import sys
from pathlib import Path
from common import ROOT, Report, read_text

RUNTIME = {
    "checks/caps.approved.json", "checks/gates.seen.json", "checks/faults.lock.json",
    "story/STORY.md", "design/exemplars/", "story/drafts/draft-01.md", "reviews/comparisons/",
}
# A path carrying NN or <> is a template for a file the loop creates, not a file the kit ships.
# A review file is created at runtime too (CLAUDE.md rule 5 numbers them as the reports arrive), so a
# document naming one by number is naming a file that will exist, not one that ships. Resolving these
# against the folder beside the kit made this check pass in the design repository — where the reviews of
# the design itself happen to sit — and fail in every deployment, which is a folder holding kit/ and
# LOOP_DESIGN.md and no reviews yet. That is the first command the handoff prompt gives.
REVIEW_FILE = re.compile(r"\Areviews/REV-\d+(-disposition)?\.md\Z")


def docs(root):
    out = [Path(root) / n for n in ("CLAUDE.md", "READ_ME_FIRST.md", "BRIEF.md", "STATE.md",
                                    "DECISIONS.md", "INBOX.md", "LEDGER.md")]
    out += sorted((Path(root) / ".claude").rglob("*.md"))
    out += sorted((Path(root) / "design").glob("*.md")) + sorted((Path(root) / "story").glob("*.md"))
    # RECORD_SHAPE.md is what the m3 skill calls the whole contract, and README.md and HANDOFF_PROMPT.md
    # are the two documents a human reads before anything runs. A broken identifier in any of the three
    # was invisible to this check.
    out += sorted((Path(root) / "reviews" / "comparisons").glob("*.md"))
    for beside in ("LOOP_DESIGN.md", "README.md", "HANDOFF_PROMPT.md"):
        p = Path(root).parent / beside
        if p.exists():
            out.append(p)
    return [p for p in out if p.exists()]


def main(root=ROOT):
    rep = Report("claims")
    root = Path(root)
    checks = {p.name for p in (root / "checks").glob("*.py")}
    agents = {p.stem for p in (root / ".claude" / "agents").glob("*.md")}
    skills = {p.parent.name for p in (root / ".claude" / "skills").glob("*/SKILL.md")}
    makefile = read_text(root / "Makefile")
    targets = set(re.findall(r"^([a-z][a-z0-9-]*):", makefile, re.M))
    seen = 0
    for doc in docs(root):
        text = read_text(doc)
        rel = doc.name if doc.parent == root else str(doc.relative_to(root.parent))
        for name in set(re.findall(r"`?\b(check_[a-z_]+\.py|run_all_checks\.py|plant_faults\.py|calibrate\.py)\b`?", text)):
            seen += 1
            if name not in checks:
                rep.fail(f"{rel} names {name}, which is not in checks/")
        for t in set(re.findall(r"`make ([a-z-]+)", text)):
            seen += 1
            if t not in targets:
                rep.fail(f"{rel} names `make {t}`, which the Makefile does not define")
        for a in set(re.findall(r"`([a-z]+-(?:critic|writer|judge|reader|editor|architect))`", text)):
            seen += 1
            if a not in agents:
                rep.fail(f"{rel} names the agent `{a}`, which has no brief in .claude/agents/")
        for s in set(re.findall(r"`(m[0-4]-[a-z-]+|close-review|gate)` skill", text)):
            seen += 1
            if s not in skills:
                rep.fail(f"{rel} names the `{s}` skill, which is not in .claude/skills/")
        for path in set(re.findall(r"`((?:checks|design|story|reviews)/[A-Za-z0-9_./<>-]+)`", text)):
            seen += 1
            clean = path.rstrip("/")
            if (path in RUNTIME or clean + "/" in RUNTIME or "<" in path or "NN" in path
                    or REVIEW_FILE.match(clean)):
                continue
            if not ((root / clean).exists() or (root.parent / clean).exists()):
                rep.fail(f"{rel} names `{path}`, which is neither in the kit nor beside it, and is not "
                         f"listed as created at runtime")
    rep.note(f"{seen} claim(s) checked across {len(docs(root))} document(s)")
    return rep.finish()


if __name__ == "__main__":
    sys.exit(main())
