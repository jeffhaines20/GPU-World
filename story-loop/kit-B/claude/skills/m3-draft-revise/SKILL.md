---
name: m3-draft-revise
description: Runs milestone M3 — the first complete draft, then revision rounds against the critics and the blind comparisons, with the revert rule and the stop conditions. Use once G2 is signed.
---

# M3 — Draft and revise

**The first draft.** Spawn `story-writer` with the spine, the bible, the brief, and the length target.
It writes the whole story to `story/drafts/draft-01.md` before anything is revised. Then run
`python3 checks/run_all_checks.py --milestone 3`.

**Each round, in this order.**

0. Reset the per-round caps in `STATE.md` (comparisons) to Used 0.
1. **Calibrate.** `make calibrate` builds this round's planted-defect pair from the current draft (one
   of: the ending flattened to a summary; a scene replaced by exposition; a tic pass applied) and runs
   the round's judges on it. A judge that prefers the weakened copy, or calls it equal, does not count
   this round. Record it; `check_comparisons.py` enforces it.
2. **Compare.** Four different exemplars drawn to cover the set over rounds, one rubric dimension per
   pair, both orders, two judges (`craft-critic-a` and `craft-critic-b`, a fresh context each, and those
   exact names in both the pairs and the calibration verdicts), written into
   `reviews/comparisons/round-NN.json` — **the shape is `reviews/comparisons/RECORD_SHAPE.md`, which is
   the whole contract; read it before you write your first record.**

   **Repeat one dimension against a second exemplar.** Three of the four pairs take a different rubric
   dimension; the fourth repeats the dimension that was the largest gap in the last round (at round 1,
   the heaviest-weighted one). The bar's rule about a dimension the draft loses on needs that dimension
   tried against two different exemplars before it can fire — one lost pairing is the story losing to a
   better story on one thing — so a round of four dimensions tried once each can never trigger it, and
   the weakness the rule exists to find stays invisible.

   The draft-against-draft round is not written here: it belongs to step 6, after this round's revision
   exists, and carries this round's number.
3. **Critique.** Fresh contexts, each getting the draft and its own brief only: `flow-critic`,
   `depth-critic`, `adversarial-critic` (its own history included). Every third round also
   `fresh-reader` and `originality-critic`. Never let a critic see another's current report.
4. **Revise.** Decide which findings this revision will answer, and spawn `story-writer` fresh with the
   draft and those findings only — severities, not the critics' reasoning. It writes the next numbered
   draft. The findings you do not pass on are not lost; step 5 records each one and why.
5. **Close.** `close-review` writes a disposition for every review of this round. It runs **after** the
   revision, not before, because a disposition of FIXED names the draft that fixed it and that draft does
   not exist until step 4 has run. Close before revising and every row is REJECTED or DEFERRED by
   construction, and the register that is supposed to record what got better records nothing.
6. **Judge the revision.** Compare the new draft against the one it replaced, and — once the human has
   signed G3 — against the draft they signed, as a `baseline_signed` block in the same record
   (`RECORD_SHAPE.md` gives it). The second pairing is the one that matters: against its immediate
   predecessor a story sanded a little flatter each round wins every time, because every single round is
   an improvement, and only a baseline far enough back shows the accumulation. Same mechanism as step 2, calibrated the same way, into
   `round-NN-revision.json` with this round's number, each judge told it is a revision pair so that it
   answers the sixth question in its brief: what did the newer draft lose. Revert
   when the judge names something lost and the pair does not go to the newer draft: write the older text
   out as the next numbered draft with a note saying what it restores, raise "Reverted revisions in a
   row" in `STATE.md`'s process signals, and record the changed approach in `LEDGER.md`. Otherwise set
   that counter back to 0. `check_state.py` reads it from M3 and fails at three; at three, stop and write
   to `INBOX.md`. Nothing is deleted: a revert is a new draft, never a removed one.
7. **Ledger and digest.** One `LEDGER.md` row (round, draft, largest gap, approach, the review file).
   Then three lines into `INBOX.md` under "Since you last looked": findings by severity per critic;
   whether the new findings are in text the last revision changed; the comparison result and how it moved.
8. **Check the stop conditions** in `LOOP_DESIGN.md` §9 and say in the ledger which one you checked.

**G3** is called when the first complete draft exists and the checks pass — not when the story is
finished. The human reads it once, without notes, and their reaction is evidence no critic can produce.
Revision rounds continue after G3 until the stop conditions fire.

**Where this fails.** Revising before the draft is complete; letting the writer see the critics'
reports; skipping calibration because the judges "were fine last round"; counting a comparison whose
two orders disagreed as a win; carrying on past the revision cap because the story is nearly there.

**The shape of a draft file.** Every file in `story/drafts/` is `draft-NN.md` and opens with exactly this
front matter, keys in lower case, before a blank line and the story:

```
---
draft: 4
date: 2026-04-19
---
```

`draft:` must match the number in the file name, and the keys are lower case because that is what
`check_manuscript.py` reads — `Draft:` is not found and the check fails on a file that looks right.
