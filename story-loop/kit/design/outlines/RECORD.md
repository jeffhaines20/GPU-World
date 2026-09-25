# Record of the outline pass (DEC-016, DEC-017)

## The five outlines

Five writers (read-only Explore agents on opus, DEC-018), one cell each, in isolation, each reading only `Q-06.md` and its
brief (`writer-prompt.md`). Replies saved verbatim to `outlines/O-N.md`; compiled in `OUTLINES.md` (6,716 words).

| Outline | Title | Cell | Words before the passage (cap 1,000) | Passage |
|---|---|---|---|---|
| O-1 | Right, Late | the parent | 1,079 | 316 |
| O-2 | Working Height | the apprentice | 1,001 | 281 |
| O-3 | Undispensed | the one who never departed | 1,037 | 326 |
| O-4 | Eleven Fathers | the audited | 996 | 319 |
| O-5 | The Herring's Backbone | the rule | 1,000 | 337 |

Three overran the pre-passage cap (O-1 by 79 words, O-3 by 37, O-2 by 1); left as written, since the orchestrator edits
nothing. Cost: 648,829 tokens over five calls (about 130K each, against the 40K the frame estimated: the writers drafted
at length inside their own contexts before replying).

## Round 1: two reviewers, one batch of five each

Batches from `batches.json` (seeds recorded before the writers ran): reviewer a read O-4, O-1, O-5, O-2, O-3; reviewer b
read O-2, O-3, O-4, O-5, O-1. Reviewer a on the session default model, b on opus, both with `reviewer-prompt.md`. Replies
verbatim in `review-round1-a.md` and `review-round1-b.md`; scores in `scores-round1.json`; critiques by outline in
`critiques-round1.md`. Pool medians: a 31, b 30 (of 35). Cost: 210,241 tokens over two calls.

| Rank | Outline | Ranking A | Raw totals (of 35) |
|---|---|---|---|
| 1 | O-2 Working Height | 31.8 | 34, 32 |
| 2 | O-4 Eleven Fathers | 30.8 | 31, 31 |
| 3 | O-5 The Herring's Backbone | 30.5 | 31, 30 |
| 4 | O-3 Undispensed | 29.2 | 26, 30 |
| 5 | O-1 Right, Late | 28.8 | 27, 27 |

Ranking B (highest single): O-2 34, O-4 31, O-5 31, O-3 30, O-1 27. Disputed (gap of seven or more): none; the widest
gap is O-3, 26 against 30.

Verdicts. Read to the end: O-2 (both). Most surprising: O-5 (a), O-3 (b). Does not survive: O-3 (a: predictable from its
first beat, stakes are acts never taken, and it repeats O-1's shape) and O-1 (b: restages the card's own example almost
beat for beat, while O-3 uses the same frame more freshly).

The largest gaps named, by outline: O-1, it is the card's own scenario with a ledger added (both), its best ideas (the
Tolliver boy, "He has it with him") buried, a middle of entries read aloud. O-2, the kitchen confession in beat 8 is a
stock mentor reveal in an over-full plan (a); the 02:14 line states the story's thesis in a frightened character's mouth
(b). O-3, almost nothing is risked on the page; the practising is on paper (both). O-4, Kit's theft in Tess's last week, in
the shape of her own, makes the hinge feel arranged (both). O-5, Aalin's case for keeping the boy is too thin against a
mother, a dying grandmother and the boy's stated wish, and the other party has no face (both); too much institution for
5,000 words (both).
