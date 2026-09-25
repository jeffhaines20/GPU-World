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

## Revision: eleven revisers, one card each

Each reviser saw only its packet (`revise/Q-NN-packet.md`: the card and the two critiques) and wrote `revised/Q-NN.md`
(the card in the fixed shape, then "What changed", at most 150 words). All eleven reported that their card survives;
nine said "narrowed". Word counts 588 to 605 (Q-21 five over the 600 asked; left as written). Q-12 dropped leasing and
now argues from guardianship, which the premise's silence on who directs a ward's share allows. Cost: 1,023,886 tokens
over eleven calls (default type), about twice what FRAME.md budgeted for this step. The notes are compiled in
`round2/CHANGES.md`; the cards, with their cells put back for the batch tool, in `round2/REVISED.md`.

## Round 2: the eleven revised cards, two fresh reviewers, four batches

Batches in `round2/batches.json`, six and five per reviewer, shuffled by `random.Random(seed).shuffle` over the eleven in
round-1 rank order, seeds a = 20260918, b = 20260919 (recorded before the reviewers ran). Reviewer a on the session's
default model, reviewer b on opus, both read-only Explore agents with the round-1 prompt unchanged (they were not told
it was a second round). Replies verbatim in `round2/review-a-1.md`, `review-a-2.md`, `review-b-1.md`, `review-b-2.md`;
scores in `round2/scores-round2.json`, critiques by card in `round2/critiques-round2.md`. Both pool medians 22 of 25
(21 in round 1). Cost: 141,288 tokens over four calls.

| Rank | Card | Cell | Ranking A | Raw totals (of 25) | Note |
|---|---|---|---|---|---|
| 1 | Q-06 Practicing on People | B | 22.8 | 24, 23 |  |
| 2 | Q-11 The Ghost Estate | C | 22.2 | 22, 23 |  |
| 3 | Q-12 The Ward's Share | C | 22.2 | 23, 22 |  |
| 4 | Q-14 The Rights Run | D | 22.2 | 23, 22 |  |
| 5 | Q-27 Nothing said is evidence | G | 22.2 | 22, 23 |  |
| 6 | Q-05 The Unasked Question | B | 22.0 | 20, 24 |  |
| 7 | Q-08 The Promise Against the Forecast | B | 22.0 | 22, 22 |  |
| 8 | Q-26 The lucid remainder | G | 21.5 | 21, 21 |  |
| 9 | Q-15 No Cognition Without a Person | D | 21.2 | 20, 21 |  |
| 10 | Q-25 Solitude becomes a verb | G | 21.2 | 20, 21 |  |
| 11 | Q-21 The Competence Marriage | F | 20.8 | 21, 18 |  |

Ranking B (highest single): Q-05 and Q-06 at 24; Q-11, Q-12, Q-14, Q-27 at 23; Q-08 at 22. **Disputed:** none (the
widest gap is Q-05, 20 against 24; Q-21, disputed in round 1, is now 21 against 18).

The reviewers' batch verdicts (verbatim in the review files):

- reviewer a-1, most important: Q-14, because it turns universal counsel into a solvency test of every guarantee a state has underwritten with its citizens' incapacity, and forces a choice no polity can make quietly.
- reviewer a-1, most novel: Q-06, because it recasts the exhausted "AI makes us dumb" worry as a consent problem — self-cultivation as an unpriced risk run on other people who can now audit the bill.
- reviewer a-1, does not survive: Q-15, because its own flagged step (5) is contradicted by the Milgram evidence it cites and its independence claim fails to the briefing objection — the state writes the facts the counsel reasons from, so the "counsel the state did not pick" is not the check the card needs.
- reviewer a-2, most important: Q-12, because it locates the one place the premise's equality is a fiction and makes a life's continuation a line item in a household's income.
- reviewer a-2, most novel: Q-12, because dependents turning from costs into assets and guardianship into compute custody is a reading no commentary on AI access has produced.
- reviewer a-2, does not survive: none — Q-05 is the weakest, since its own concession that the model holds only what she has told it makes the change one of speed that the card must inflate into a change of kind, but the "ignorance becomes an act" turn still earns its place.
- reviewer b-1, most important: Q-14, because it puts the constitutional guarantee itself on the table and shows a state forced to say aloud what it has always rationed in silence.
- reviewer b-1, most novel: Q-11, because inherited context as an estate whose upkeep is the heir's own allotted mind is a reading of the premise no follower of this subject will have seen.
- reviewer b-1, does not survive: Q-15, because its central move needs the soldier's share to know the fact the briefing withheld, and once the counsel is only as good as the state's own account, "I did not ask" collapses back into "I could not know."
- reviewer b-2, most important: Q-06, because a permanently frozen ceiling makes the right to cultivate judgment past it a question about whether human practical wisdom continues at all, and it lands on an ordinary parent.
- reviewer b-2, most novel: Q-12, because dependents becoming net assets and equality leaking into de facto family pooling is a structural consequence no one in this discourse has named.
- reviewer b-2, does not survive: Q-21, because its central step — that a known-false need can no longer dress a bid for attention — is contradicted by how couples actually use pretexts, and its "crisis" is a mood with no event, no deadline and nobody paying.

**Offered to the human: the top five on ranking A**, Q-06, Q-11, Q-12, Q-14, Q-27. Q-06 leads alone; the other four
tie at 22.2 and are exactly the four places left, so no tie-break was needed. Q-05 and Q-08 sit just below at 22.0
(Q-05 was first in round 1 and has the highest single score, 24 from reviewer b, against 20 from reviewer a). Named as not
surviving by a reviewer this round: Q-15 (both reviewers, batch 1: the soldier's counsel reasons only from the state's
briefing) and Q-21 (reviewer b: a known-false need can still dress a bid; no event, no price). No reviser said its card
does not survive. Cells in the five: B, C (twice), D, G; cells A (philosophical) and E (religious) had no card in the
eleven, and F's only card, Q-21, fell.

**Are the round-2 objections new, or the round-1 ones surviving?** For four of the five, the weakest step named in
round 2 lies in text the reviser changed: Q-06 (round 1: deferring builds only deferring, and "worse expected outcome";
round 2: that judgment needs live cases, and that counsel's presence makes a departure an imposition), Q-11 (round 1:
the scale leap to "worth more than a house"; round 2: the continuity premium the reviser itself named, and "one day to
give"), Q-12 (round 1: leasing; round 2: why a legislature would not ring-fence ward-engines), Q-27 (round 1: the record
is better evidence, the cost is not zero; round 2: the boards' own shares could learn to read coaching). For Q-14 the
same step, (4), the size of the information-priced fraction, is named by both reviewers in both rounds; the reviser
called it "an empirical bet" it could not fix from the premise. That is the kit's "same largest gap under the same
approach for two rounds" pattern, and it is said to the human rather than sent to a third reviser.

**Movement from round 1 to round 2** (rank on A): Q-06 2nd to 1st; Q-11 9th to 2nd; Q-12 3rd to 3rd; Q-14 4th to 4th;
Q-27 10th to 5th; Q-05 1st to 6th; Q-08 7th to 7th; Q-26 6th to 8th; Q-15 8th to 9th; Q-25 5th to 10th; Q-21 disputed
to 11th.

**Cost of the whole funnel:** about 2.2M tokens (seven thinkers, ten reviews, eleven revisions, four re-reviews),
against the 1.6M FRAME.md estimated; the revisers were the overrun. Project total about 7.2M of 10M.

**Waiting on the human:** their choice of question, in their words; a caps row for the third premise pass (the
premise-writer cap is spent at 13 of 13; probes 4 and judge calls 6 remain); and whether the token cap is raised,
since 2.8M does not reach a revision round at the measured costs.
