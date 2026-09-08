# Orchestrator runbook

Working notes for whoever orchestrates this loop next, so that "continue" loses minutes, not a round.
Not part of the kit: nothing in `kit/` names this folder, and no check reads it. The kit's own state is in
`kit/STATE.md`, `kit/INBOX.md`, `kit/DECISIONS.md`, `kit/LEDGER.md`; read those first, then this.

## What the dry run taught (2026-09-08, scratch copy, deleted afterwards)

1. **Wait for the writer's completion notice before touching its file.** The file appears about a minute
   before the agent finishes and keeps changing. Calibrating on the early text produced a record whose
   hash would have failed `check_comparisons.py`. Re-hash right before writing any record.
2. **`make calibrate` is deterministic** (seed 7): the revision round and the next round's exemplar round
   can share `calibration-draft-NN.md`; re-running it does not invalidate an earlier record's hash.
3. **Judges get neutral copies.** A path like `story/drafts/draft-03.md` or `calibration-draft-03.md`
   reveals provenance. `make_pair.py A B outdir label` writes `label-A.txt` / `label-B.txt` with front
   matter and any title line stripped. Build both orders as separate pairs.
4. **Every agent costs ~19K tokens (Explore type) or ~29K (default type) before it reads a word.** A
   verdict is 32–50K, a critic 60–70K, a writer 70–80K for 500 words. Judges and critics run as Explore
   agents (read-only): same verdict quality, ~28% cheaper; a critic returns its report in the reply and the
   orchestrator saves it verbatim to `reviews/REV-NN.md`. Writers, the architect and the line editor need
   Write and run as the default type. `subagent_tokens` in the completion notice is the figure to add to
   STATE.md's Used; the orchestrator's own use is 15,000,000 minus the session counter.
5. **Per-round cost with two judges**: 4 calibration + 16 exemplar + 8 revision verdicts (16 after G3)
   ≈ 1.1–1.7M tokens with critics and the writer. The kit's 8M default assumed a cheaper harness.
6. **Judge agreement is near-total across models** (9 of 9 verdicts quoted the same two sentences). Model
   rotation does not produce a second taste; the two-judge rule guards against noise, not against shared
   preference. The calibration pair is coarse and catches only a judge that approves anything.
7. **The checks did what the design says.** `round-01.json` passed at round strictness and failed at
   `--gate 3` on exactly the two rules a one-pair round cannot meet; `check_reviews.py` refused the review
   until its disposition existed and passed once every finding had one row.
8. **Not exercised in the dry run**: the revision comparison round (`round-NN-revision.json` with `lost`
   and `baseline_signed`), the gate flow (`--pregate`, sign-off, `--gate`), and `check_state.py` past M0.
   Expect to learn those on the real run's first round.

## Procedure per M3 round (the m3 skill, with the mechanics filled in)

0. STATE.md: comparison verdicts Used ← 0.
1. `make calibrate` (in `kit/`); copy the two hashes it prints. Build cal pairs both orders with make_pair.py.
2. Spawn craft-critic-a (default model) and craft-critic-b (opus), each in a fresh Explore context, one pair
   per call, one dimension per call; record `caught` only if the true draft won both orders.
3. Exemplar pairs: four exemplars, three dimensions + one repeated (last round's largest gap; round 1 the
   heaviest weight), both orders, both judges = 16 calls. Write `round-NN.json` per RECORD_SHAPE.md.
   `python3 checks/check_comparisons.py --milestone 3` and, to see what the gate will demand, `--gate 3`.
4. Critics (Explore, fresh): flow, depth, adversarial (+ its own history); every third round fresh-reader and
   originality-critic. Save each reply verbatim as `reviews/REV-NN.md`.
5. Writer (default type) revises against findings only (severities, no reasoning) → next draft. Wait for
   the completion notice.
6. Dispositions, `check_reviews.py`, then the revision round: `make calibrate` on the new draft, new pairs,
   2 pairs × 2 judges × 2 orders against N−1 (+ the same against the G3-signed draft once one exists),
   each judge told it is a revision pair; every verdict carries `lost`. Revert rule per LOOP_DESIGN §7.2.
7. LEDGER row; three lines in INBOX.md "Since you last looked"; stop conditions checked and named.
