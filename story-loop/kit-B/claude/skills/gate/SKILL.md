---
name: gate
description: Prepares a human gate and finishes it — regenerates READ_ME_FIRST.md, runs the milestone's checks, writes the INBOX request, then after the human's own sign-off verifies it and advances the state. Use at the end of every milestone.
---

# The gate

**Before the human.**

1. Regenerate `READ_ME_FIRST.md`'s header (project, milestone, date) and check that everything it
   promises still exists.
2. `python3 checks/run_all_checks.py --milestone <N> --complete --pregate <N>`. Print it in full. A
   failing check is not a gate; fix it first.

   `--pregate <N>` runs every check `--gate <N>` runs, at the same strictness, with one exception: the
   sign-off check, which cannot pass before the human has signed and which no agent may ever make pass.
   Everything else — the comparison bar, the open MAJORs, the caps, the manuscript — is held to the full
   gate standard here, deliberately. The human's first reading of a draft is spent once and cannot be
   spent again, so a gate that passes a lenient pre-check, takes that reading, and then fails its own
   post-sign-off check has wasted the one thing this loop cannot regenerate. At G3 this usually means the
   round's comparison must be judged **before** the human is asked to read, not after.
3. Write the `INBOX.md` request: what to read, how long it should take, what question is being asked,
   and the exact command. List, in one short block, every MAJOR finding that was answered with REJECTED
   since the last gate, with the reason given, under the heading "Findings we decided not to act on".
   **"Since the last gate" means:** every review named in a `LEDGER.md` row below the last row whose Gate
   cell is filled — and every review, if no row carries one yet. The ledger is the boundary because it is
   the only register that has a row per round and a mark per gate; do not date-match, and do not guess
   from REV numbers.
   The human is the only reader who can overrule that, and they cannot overrule what they never see. Then: "run `make gate N=<N>`, write three to five sentences in your own words
   — what you saw, what you liked, what must change, whether it goes through — and save them."
4. **Stop.** Never write the sign-off. If the human dictates it in chat, write it verbatim, attribute it
   in the heading, and say in `INBOX.md` that this gate's words came through chat.

**After the human's sign-off exists.**

5. `python3 checks/run_all_checks.py --milestone <N> --complete --gate <N>` passes — the same command as
   step 2, now with the sign-off in place. If the paragraph says something must change, that is a finding:
   open a review round on it before advancing.
6. Record the outcome (GO, BACK, STOP) as a `DECISIONS.md` row (author agent), and write which outcome
   you read into `INBOX.md` beside the human's paragraph so they can correct you.
7. Advance the milestone line in `STATE.md`. This skill is the only place that line changes. Write this
   gate into the Gate cell of `LEDGER.md`'s most recent row, which is what makes "since the last gate"
   answerable at the next gate. At G0 and G1 there is usually no row yet — the ledger holds one row per
   critic round and the first is M2's — and then there is nothing to write: skip this step, and step 3's
   "every review, if no row carries a gate yet" covers it.

A sign-off, once written, is never edited by anyone. What the human wants to add later is a new row.
