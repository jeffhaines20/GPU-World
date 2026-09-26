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

## The originality critic (REV-03)

One Explore agent on opus with web search (ten searches, one page fetch), reading `OUTLINES.md` only; report saved
verbatim as `reviews/REV-03.md`; disposition in `reviews/REV-03-disposition.md`. Findings: F1 MAJOR, O-1 and O-3 are one
story twice (a father's yearly books scored overnight by a grown child leaving by boat, a kitchen-table ending); F2 MINOR,
O-4 a third telling of the child-audits-father premise; F3 MINOR, O-2 and O-5 share their confrontation scene; F4 MINOR,
all five end on a withheld verdict and share four prose reflexes; F5 to F7 MINOR, wrong "closest published" lines on O-3,
O-5 and O-2; F8 to F10 NIT. Nothing lifted. Cost: 159,019 tokens.

**Routing.** F1 to a rebuild of O-1 (both reviewers called it the card's own scenario with a ledger added; reviewer b
said O-3 uses the shared frame more freshly); O-3 keeps its frame. F3 to a rebuild of O-5's confrontation; O-2 keeps its
scene. F2 to O-4 (drop the card's phrase and reconsider the theft). F4 to every reviser by name. The packets
(`revise/O-N-packet.md`) therefore carry, beyond the outline and the critiques the frame promised, a short routing note
from the orchestrator (`revise/notes/O-N.md`); that is the one addition to the frame's "nothing else", made because a
MAJOR must be dispositioned and two revisers moving away from each other blind could converge again.

## The revision: five fresh revisers

Explore agents on opus, each reading only its packet. The first launch was cut short by the account's usage limit: O-2's
reviser had handed back before the cut; the four others produced nothing and were relaunched with the same packets.
Replies saved verbatim to `revised/O-N.md`. All five report that the outline survives.

| Outline | Revised title | Words before the passage | Passage | What changed, in brief |
|---|---|---|---|---|
| O-1 | He Has It With Him | 996 | 272 | rebuilt: the auditor is the Tolliver boy, now Wade's trainee, on one night shift; no child scores the books, no one leaves by water, no kitchen table; "He has it with him" is the turn; the ending places a new bet |
| O-2 | Working Height | 982 | 296 | Marga's kitchen confession cut; the 02:14 thesis line replaced by "No" and "Let me", the review inferring the want from the record; Noor's father as the want's source; Gawande and Bohjalian named; "Again" kept |
| O-3 | Undispensed | 967 | 313 | a live case added (the daughter's sertraline script in his drawer); she reads the last book first; the ending is the drawer, not the blank line; Nell is Thora; Ishiguro and Alexander named |
| O-4 | Eleven Fathers | 1,003 | 314 | the theft and the Co-op call gone; Kit's case is caused by overhearing the audit and reaches Rob because Tess lets it; the card's phrase gone; a new last image (Kit's ear) |
| O-5 | Breast Law | 1,029 | 316 | the father given a face and a claim; Counsel names what Aalin sees, so she departs on weight alone; she never meets the boy; the mother audits the judge, not the judgment; McEwan and Caine named; the herring emblem and the Act's exposition cut |

Reported cost of the four relaunched revisers and O-4: 560,780 tokens; O-2's reviser and the four interrupted attempts
reported no usage (their transcripts total 3.5MB) and are carried as an estimated 0.5M. Two of the five notes run over the
150-word cap (O-1 and O-2 at 165; O-5 at 156); left as written.

**Round 2** uses the seeds recorded in `batches.json` before any writer ran: reviewer a reads O-3, O-1, O-5, O-4, O-2;
reviewer b reads O-2, O-1, O-4, O-3, O-5 (`batch-round2-a.md`, `batch-round2-b.md`, 6,512 words each).

## Round 2: the five revised outlines, two fresh reviewers

Replies verbatim in `review-round2-a.md` and `review-round2-b.md`; scores in `scores-round2.json`; critiques by outline in
`critiques-round2.md`; the offer assembled in `OFFER.md`. Pool medians: a 30, b 27 (31 and 30 in round 1). Cost: 223,081
tokens over two calls.

| Rank | Outline | Ranking A (of 35) | Raw totals | Round-1 rank | Round-1 A |
|---|---|---|---|---|---|
| 1 | O-4 Eleven Fathers | 31.0 | 33, 34 | 2 | 30.8 |
| 2 | O-2 Working Height | 30.2 | 31, 33 | 1 | 31.8 |
| 3 | O-3 Undispensed | 28.5 | 30, 27 | 4 | 29.2 |
| 4 | O-5 Breast Law | 27.5 | 28, 25 | 3 | 30.5 |
| 5 | O-1 He Has It With Him | 27.0 | 26, 25 | 5 | 28.8 |

Ranking B (highest single): O-4 34, O-2 33, O-3 30, O-5 28, O-1 26. Disputed (gap of seven or more): none; the widest
gaps are O-5 and O-3 at three.

Verdicts. Read to the end: O-4 (a), O-2 (b). Most surprising: O-5 (a), O-4 (b). Does not survive: O-1 (a: its central
charge is a cover-up with a known victim, Dubus's "A Father's Story" in a dispatch room, and its turn a withheld night
released on cue) and O-5 (b: the judge's childhood in the litigant's phrase is a stock courtroom reveal the reader makes
first; close to The Children Act; the departure reads as plain bias). No reviser said its outline does not survive.

**Are the round-2 objections new, or the round-1 ones surviving?** O-4: round 1's gap (the theft coincidence) is gone; the
new gaps are in the new mechanism (it opens on analytics; the inference that waiting till five was Tess's own practice
on Kit must reach the page). O-2: both round-1 gaps (the confession, the thesis line) are gone; new: after the birth Noor
has nothing at stake, the Gawande claim is argued in the note and dramatized in no scene, and "Again" may read as pardon.
O-1: rebuilt, so every objection is new, and it is one objection from both reviewers: the founding departure (a ten-year-old
serving a season for the son's alarm, logged "Cost: not mine") is knowing wrongdoing, so the reader condemns Wade before
the question opens. O-3: the same largest gap in both rounds under a changed approach (the sertraline drawer was added, and
both reviewers find the price still too mild, an emergency supply being a phone call away). O-5: the same largest gap in
both rounds under a changed approach (round 1: her case was too thin, so the reader convicts her; round 2: the added
childhood-affinity reveal makes the departure read as bias, so the reader convicts her earlier). By the kit's ledger rule
the O-3 and O-5 gaps have now survived two rounds; a third attempt needs a changed approach written down first, or the
human's decision, and this is the human's decision.

**Movement, round 1 to round 2** (rank, ranking A): O-4 2nd to 1st (30.8 to 31.0; raw 31, 31 to 33, 34); O-2 1st to 2nd
(31.8 to 30.2); O-3 4th to 3rd (29.2 to 28.5); O-5 3rd to 4th (30.5 to 27.5); O-1 5th to 5th (28.8 to 27.0). The reviewers
were fresh each round, so the numbers are not strictly comparable, but only O-4 gained raw points; the other four lost
some. Nothing is deleted: both versions of every outline are on file (`outlines/` and `revised/`), and the human may pick
either version of any of them.

**Cost of the pass.** Reported: writers 648,829; round-1 reviewers 210,241; originality critic 159,019; revisers 560,780
(five reported calls); round-2 reviewers 223,081: 1,801,950. Unreported: five reviser calls cut short by the account's
usage limit, carried as an estimated 0.5M. With the orchestrator's own share, about 2.7M against the 1.1M the frame
estimated. Project total about 9.9M of the 10M cap. Nothing further runs without the human's caps row.

**Carried to M2 and M3.** The originality critic's F4 (four prose reflexes: the cut from a hard line to an ambient sound;
a line said flatly "the way" a job reads things; someone who "did not remember" a small act of the hand; someone who
looked "at the window, where") is to be given to the draft's critics by name. Whichever outline is chosen, the
story-architect inherits that outline's round-2 critiques and its REV-03 reading.

## Waiting on the human (G1, third time)

The pick, or a send-back, in their words; the G1 sign-off paragraph; and the token cap, since the spine cannot start
inside what is left.

## M2: the spines (both kits), 2026-09-25 to 2026-09-26

G1 was signed on 2026-09-25 for two outlines (DEC-020): story A, O-4 Eleven Fathers, in `kit/`; story B, O-2 Working Height,
in `kit-B/`. Each story-architect (default type, Fable 5.1, DEC-021) read only its M2 packet (`story/M2-PACKET.md`: the
revised outline, the Q-06 card, the originality critic's reading and findings, two readers' largest gaps without scores,
the length target), `BRIEF.md`, and the two templates, and rewrote `story/SPINE.md` and `story/BIBLE.md`. The architects'
reports, verbatim:

**Story A, first architect** (114,916 tokens): "Decisions the outline left open: close third on Tess, past tense (she must
not conclude; Rob and Kit stay behind the wall). The bud and bowl kept; buds answer only their owner, hear only the hall
from the bowl, never replay anything: the audit runs on Tess's telling alone. "Counsel" and "model" dropped from the
manuscript: people say "mine", "yours", "it"; Rob names a bud only by its owner. The mother left in April 2029, unnamed,
and the bowl began that week, no cause given. A third entry (the party at nine) added so Rob is plainly wrong once. On
Friday Tess leaves her own bud in the bowl and takes only Kit's. Week fixed: 17–22 September 2040. Gaps: Reader b
answered: one plain sentence at four on Thursday that she is waiting to see what her father does, not for Kit's sake,
with her bud's "You could still go in" beside it. Reader a, half: no numbers on page one, and the curve's steadiness made
the audit's own blindness (the bud says the shape is built in). Refused the other half: the premise was chosen at G1;
the surprise owed is the plot's, not the setup's. Least sure: whether that one plain Thursday sentence makes the second
defendant too legible and tips into thesis."

**Story B, first architect** (132,323 tokens): "Decisions the outline left open: close third on Noor, past tense (the sound
must be heard and lost with her; Sanne stays opaque). The baby unnamed. Sanne sends the complaint and asks for Noor the
same morning; Noor chooses to go. The counsel's landing recommendation is "listen through three more"; her figure moves
to 96.9 at 02:14. Marga's 0.4 is six departures, one cord, five for nothing; she refuses to listen to the recording. The
review is written to Sanne as "you" and Noor reads it in that form. Three plays; the third at Sanne's ear, out of Noor's
hearing. Oosterschelde under the bridge, distinct from the father's Westerschelde. Gaps: Reader a answered: complaint
stands, no pardon line, Sanne's own counsel says nothing is there and she listens anyway; Bohjalian's shape kept, its
trial banned. Reader b answered in part: the complaint is priced (live cases suspended, simulator hours, sign-off deferred
past Marga to a stranger reading the record) in one message and one simulator scene; refused the implication that the
back half needs more plot, because the weight belongs on the quiet scene. Least sure: whether rules alone can keep the
last image (mother, baby, phone at ear) from reading as a pardon; the writer's temperature decides it."

**First critic round** (two Explore critics on opus per kit, reading the spine, the outline's passage and the brief):
story A, REV-04 (depth) 1 MAJOR 7 MINOR 1 NIT and REV-05 (adversarial) 2 MAJOR 6 MINOR 1 NIT, NEEDS CHANGES; story B,
REV-04 0/6/1 and REV-05 1 MAJOR 6 MINOR 3 NIT, NEEDS CHANGES. Costs: 137,684 + 136,774 (A); 134,834 + 147,957 (B).
Both spines went to fresh architects with the findings lists only (`story/M2-FINDINGS.md`). The first launch of both
revisions was cut short by the account's usage limit (Fable calls, tokens unreported); story B's half-written spine was
restored from the last commit and both were relaunched on 2026-09-26.

**Story B, revising architect** (175,618 tokens): "MAJOR (REV-05 F1): the archive exists and has already been tried. "The
misses", the registry's recordings of births a counsel heard nothing wrong in, were played blind to every midwife in
2033 and to every second-year since, and everyone scores at chance: Marga in 2033, Noor in 2038. It is a clause of the
Obstacle, a line in beat 5 beside her hundred on the simulator, one sentence in the Who, and in the bible a term, a rule
and two timeline entries. So Noor asked "Let me" knowing no recording holds an ear; the fading is evidence for neither
side, and a live birth is truly the only test. Addressed: REV-04 F1 ("Keep that" cut; the obstetrician says "loose";
Marga silent), F2 (the cord concrete in beat 2, "Left side" in beat 1, the birth books in beat 5), F3 and REV-05 F2 ("Your
call" is logged as Marga's seventh departure, 99.6 to 99.5; she checks it once at Goes; the review names her; January is
her reason; Sanne's "All right" at 02:16 is quoted, so her listening is her second departure), F4 (she has had the
recording since Wednesday, unplayed; Joost's line), F5 and REV-05 F6 (the five words replaced by the box), F6 and REV-05 F3
(fading told once, in the passage), F7; REV-05 F4 (Noor wants to hear it, through Sanne, and counts to the second: vanity
in the last image, chosen), F5, F7, F8, F9 (four contractions). Refused: REV-05 F10 for the passage; "gallop" stays as
written there and appears nowhere else. Least sure: whether "the misses" reads as a fact of the world or as the story
explaining itself." The spine grew from 1,964 to 2,101 words against the instruction not to grow; left as written.
Dispositions: `kit-B/reviews/REV-04-disposition.md`, `REV-05-disposition.md` (F10 REJECTED with the reason). Second
critic round on the revised spine: REV-06 (depth, fresh) and REV-07 (adversarial, with its first report and the
dispositions).

