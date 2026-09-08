#!/usr/bin/env python3
"""Builds this round's calibration pair: a mechanically weakened copy of the current draft that a judge
with taste must prefer the original to. The defects are planted by program, not by an agent's judgment,
so the pair is reproducible and nobody has to decide how bad to make it: filter words and adverbs
inserted, the rhythm flattened, and the ending cut back to a summary sentence. It writes the weakened
text alone, with no header naming it, because the judge is not told which pairs are calibration pairs and
a file that announces itself is not a test. It prints the defects that actually landed and the hash to
record; a defect that could not be planted (an ending already one sentence long, say) is not claimed.
The orchestrator then runs the round's judges on (original, weakened) in both orders, anonymized, and
records `caught` for each judge that chose the original both times, in the round's JSON under
`calibration`, with the pair file's name and hash. check_comparisons.py refuses a round whose judges did
not catch it, whose verdicts are empty, or whose pair file is missing or altered.
What this cannot do: make a judge have taste. It catches a judge that approves anything; a judge whose
preferences are merely ordinary passes this and is caught by nothing here.
Usage: calibrate.py"""
import random
import re
import sys
from pathlib import Path
from common import ROOT, current_draft, sentences, sha256_text, split_front_matter

FILLER = ["somehow ", "suddenly ", "quite ", "rather ", "actually "]
FILTERS = [("saw", "could see that"), ("heard", "could hear that"), ("knew", "somehow knew that"),
           ("was", "seemed to be"), ("stood", "began to stand"), ("looked", "started to look")]


def weaken(body, seed=7):
    """(text, [defects that landed])."""
    rng = random.Random(seed)
    paras = [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]
    landed, tics, rhythm = [], 0, 0
    out = []
    for para in paras:
        new = []
        for j, s in enumerate(sentences(para)):
            t = s
            for a, b in FILTERS:
                t2 = re.sub(rf"\b{a}\b", b, t, count=1)
                tics += t2 != t
                t = t2
            if j % 2 == 0 and len(t) > 30:
                t = rng.choice(FILLER).capitalize() + t[0].lower() + t[1:]
                tics += 1
            new.append(t)
        joined = " ".join(new)
        flat = re.sub(r"(\w), (and|but|so) ", r"\1 \2 ", joined)
        rhythm += flat != joined
        out.append(flat)
    if tics:
        landed.append("tic-pass")
    if rhythm:
        landed.append("flattened-rhythm")
    if out:
        # Cut the ending back to a summary sentence. When the last paragraph is already one sentence —
        # the shape this kit's own agent briefs push toward — cut into the paragraph before it instead,
        # so that the defect is planted rather than merely claimed.
        target = -1 if len(sentences(out[-1])) > 1 else (-2 if len(out) > 1 and len(sentences(out[-2])) > 1 else None)
        if target is not None:
            out[target] = sentences(out[target])[0]
            if target == -2:
                out = out[:-1]
            landed.append("ending-cut-to-summary")
    return "\n\n".join(out), landed


def main(root=ROOT):
    path = current_draft(root)
    if not path:
        print("  FAIL: no draft to calibrate against; the first calibration is run after the first draft")
        return 1
    _, body = split_front_matter(path.read_text(encoding="utf-8"))
    text, landed = weaken(body)
    out = Path(root) / "reviews" / "comparisons" / f"calibration-{path.stem}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    if not landed:
        print("  FAIL: no defect could be planted in this draft; calibration cannot be run on it, and a "
              "round with no calibration does not count. Tell the human.")
        return 1
    print(f"calibration pair written: reviews/comparisons/{out.name}")
    print(f"  original: story/drafts/{path.name}")
    print(f"  planted:  {', '.join(landed)}")
    print(f"  draft_sha256:  {sha256_text(body)}")
    print("     ^ the record's draft_sha256. It is the sha256 of the draft's body — everything after the")
    print("       front matter, exactly as the file has it — and this is the value check_comparisons.py")
    print("       recomputes, so copy it rather than hashing the file yourself.")
    print(f"  pair_sha256: {sha256_text(out.read_text(encoding='utf-8'))}")
    print("The file holds the weakened text and nothing else: no header, no label. Show the judges the two")
    print("texts as Story A and Story B, both orders, anonymized, and do not tell them it is a calibration.")
    print("A judge that chooses the weakened copy either way, or calls the pair equal, does not count this")
    print("round. Record in the round's JSON, per reviews/comparisons/RECORD_SHAPE.md:")
    print(f'  "calibration": {{"planted": "{", ".join(landed)}", "pair_file": "{out.name}",')
    print('                   "pair_sha256": "<the hash above>",')
    print('                   "verdicts": {"<judge>": "caught"}, "passed": true}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
