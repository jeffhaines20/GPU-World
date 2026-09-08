# State

**Milestone:** M1 — Premise funnel · **Updated:** 2026-09-08 · **Current draft:** none

## Caps

The Value column is the loop's own budget, sized by this design and accepted by the human at intake as one block (`checks/caps.approved.json`). Only the token budget is asked of them by name in `BRIEF.md`; the rest are the agents' working numbers, which they may lower and may never raise. An agent may lower a value, never raise it; a
raise, a new cap, or a dropped cap is a `DECISIONS.md` row of type caps that the human writes. Used is
the orchestrator's estimate, written every turn. A row spent to its Value is a stop: the next draw on it
is a failing check.

| Cap | Value | Used | What kind of number |
|---|---|---|---|
| Premise-writer calls (one per partition cell) | 7 | 6 | budget for M1: six cells, and one spare so that the human sending a cell back at G1 does not need a caps decision. Every M1 row below is sized the same way — one regeneration and no more; a second needs the human's caps row |
| Premises generated | 28 | 0 | budget for M1: twenty-four, and four more for one regenerated cell |
| Probe passages | 10 | 0 | budget for M1: six probes for the six cards chosen at step 6, and four more so that one regenerated cell can be probed too. Sized for the send-back G1 offers the human |
| Premise-judge calls | 16 | 0 | budget for M1: two judges over four batches of six cards is eight calls, two more over the probed six is ten; four more so that a regenerated cell's cards can be judged and then re-judged with their probe. Sized for the send-back G1 offers the human |
| Revision rounds in M3 | 3 | 0 | budget for M3; resets never. Lowered from the kit's 12 to the 3 the human named in the handoff; a raise is their caps row |
| Comparison verdicts per round | 20 | 0 | resets when a round starts, and counts **every** verdict the round spends, not only the exemplar round's: calibration is 2 judges × 2 orders = 4; the exemplar round is 4 pairs × 2 orders = 8; the revision round is at least 2 pairs × 2 orders = 4, and 8 once a G3 sign-off exists and draft N is also paired against the draft the human signed. The old value of 8 counted the middle set only and no M3 round could be run inside it |
| Rounds one finding may survive before it goes to the human | 3 | 0 | live count, per finding; the approach changes before the third round, and the human hears about it at the third |
| Fresh-reader calls | 5 | 0 | budget for M3 and M4 |
| Tokens, whole project | 10M | 1.45M | the human's allowance: 2M in the handoff, raised to 10M in chat at intake (DEC-008) after the dry run measured what a round costs here. Used is an estimate: the orchestrator's own context plus every sub-agent's reported tokens; 1.4M was spent on the day-one fix, the dry run and intake |

## Process signals

| Signal | Value | Written by |
|---|---|---|
| Reverted revisions in a row | 0 | the m3 skill, after each draft-against-draft comparison |
| Rounds since a finding was accepted | 0 | the m3 skill |
| Last comparison result (wins–ties–losses, full-text share) | none | the m3 skill |
| Judges calibrated this round | not yet | `make calibrate` |
