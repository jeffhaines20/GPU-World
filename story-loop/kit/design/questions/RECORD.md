# Record of the questions-first funnel

## Round 1: twenty-eight cards, two reviewers, ten batches

Scores in `scores-round1.json` (fifty-six lines, verbatim replies in `review-a-*.md` and `review-b-*.md`); the
critiques by card in `critiques-round1.md`. Both reviewers' pool medians were 21 of 25.
Batches in `batches.json`: the twenty-eight IDs in order, shuffled by `random.Random(seed).shuffle`, cut 6, 6, 6, 5, 5;
seeds a = 20260916, b = 20260917 (not written down at the time; checked on 2026-09-14 to reproduce the file exactly).

Ranking A (shrunk): Q-05 22.2 · Q-06 22.2 · Q-12 22.0 · Q-14 21.8 · Q-25 21.8 · Q-26 21.8 · Q-08 21.5 · Q-15 21.5 ·
Q-11 21.2 · Q-27 21.2 · then Q-16 and Q-23 at 21.0, Q-01, Q-02, Q-17, Q-19 and Q-21 at 20.8, and the rest down to 19.8.
Ranking B: Q-05, Q-06, Q-12 at 24; Q-14, Q-21, Q-25, Q-26, Q-27 at 23. **Disputed:** Q-21 (23 against 18).

The reviewers' batch verdicts. Most important: Q-14 (twice), Q-05, Q-15 (twice), Q-12, Q-13, Q-04, Q-01, Q-25.
Most novel: Q-27, Q-11 (twice), Q-19, Q-21, Q-06, Q-02, Q-26, Q-18, Q-20. Does not survive: Q-24, Q-09 (twice),
Q-20, Q-12 (reviewer a: its engine is leasing, which the granted premise forbids), Q-03, Q-28, Q-07, Q-21 (reviewer b),
and one "none, though Q-02 is closest".

**To revision (eleven):** the top ten on ranking A, Q-05, Q-06, Q-12, Q-14, Q-25, Q-26, Q-08, Q-15, Q-11, Q-27, plus
the disputed Q-21. Cells A (philosophical) and E (religious) have no card in the eleven: their best, Q-01, Q-02, Q-17
and Q-19, sit at 20.8, though Q-19, Q-02 and Q-18 were each named most novel by a reviewer. Each reviser receives
the card and the two critiques of that card only (`revise/Q-NN-packet.md`) and writes `revised/Q-NN.md`.
