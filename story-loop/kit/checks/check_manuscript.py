#!/usr/bin/env python3
"""The current draft is a manuscript: it exists, opens with its front matter (draft number and date),
its word count is inside the range the human set in checks/thresholds.json, it carries no placeholder
text, and the drafts are numbered without a gap so that nothing was written over.
Bypass attempts this check refuses: a draft left at TODO or TK; a bracketed stage direction standing in
for a scene; a draft file numbered out of sequence so an earlier one is shadowed; front matter whose
draft number disagrees with its file name.
What it does not check: whether the words are any good, which is what every critic and both gates are for.
Usage: check_manuscript.py [--milestone N] [--complete]"""
import re
import sys
from common import ROOT, Report, current_draft, drafts, split_front_matter, thresholds, word_count

PLACEHOLDERS = [
    (re.compile(r"\bTODO\b"), "TODO"),
    (re.compile(r"\bTK\b"), "TK"),
    (re.compile(r"\bXXX\b"), "XXX"),
    (re.compile(r"\blorem ipsum\b", re.I), "lorem ipsum"),
    (re.compile(r"\[[^\]\n]{0,80}(scene|describe|expand|fix|insert|write)[^\]\n]{0,80}\]", re.I), "a bracketed stage direction"),
    (re.compile(r"<[^>\n]{0,60}(placeholder|to be written)[^>\n]{0,60}>", re.I), "a placeholder"),
]


def main(root=ROOT, milestone=None, complete=False):
    rep = Report("manuscript")
    ds = drafts(root)
    if milestone is not None and milestone < 3:
        if not ds:
            rep.note("no draft yet, which is right before M3")
            return rep.finish()
    if not ds:
        rep.fail("story/drafts/ has no draft-NN.md; M3 begins by writing the whole draft")
        return rep.finish()
    numbers = [n for n, _ in ds]
    expected = list(range(1, len(numbers) + 1))
    if numbers != expected:
        rep.fail(f"the drafts are numbered {numbers}, not {expected}; a gap or a repeat means a draft was "
                 f"written over, and no draft is ever deleted or replaced")
    path = current_draft(root)
    meta, body = split_front_matter(path.read_text(encoding="utf-8"))
    if "draft" not in meta:
        rep.fail(f"{path.name}: no 'draft:' line in the front matter")
    elif meta["draft"].zfill(2) != path.stem.split("-")[1]:
        rep.fail(f"{path.name}: front matter says draft {meta['draft']}, the file name says "
                 f"{path.stem.split('-')[1]}")
    if "date" not in meta:
        rep.fail(f"{path.name}: no 'date:' line in the front matter")
    for pat, name in PLACEHOLDERS:
        m = pat.search(body)
        if m:
            line = body[:m.start()].count("\n") + 1
            rep.fail(f"{path.name} line {line}: {name} — a placeholder in the manuscript ({m.group(0)[:40]!r})")
    n = word_count(body)
    lo, hi = thresholds(root)["length"]["min_words"], thresholds(root)["length"]["max_words"]
    if complete or (milestone is not None and milestone >= 4):
        if not (lo <= n <= hi):
            rep.fail(f"{path.name}: {n} words, outside the range the human set ({lo}–{hi})")
    elif n > hi:
        rep.fail(f"{path.name}: {n} words, over the maximum the human set ({hi})")
    elif n < lo:
        rep.note(f"{path.name}: {n} words, under {lo}; the range is enforced when the draft is called complete")
    rep.note(f"{len(ds)} draft(s); current {path.name}, {n} words")
    return rep.finish()


if __name__ == "__main__":
    ms = int(sys.argv[sys.argv.index("--milestone") + 1]) if "--milestone" in sys.argv else None
    sys.exit(main(milestone=ms, complete="--complete" in sys.argv))
