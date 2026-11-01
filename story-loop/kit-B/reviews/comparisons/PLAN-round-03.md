# Round 3 plan, story B — the final comparison round, declared before any round-3 verdict exists (2026-11-01)

Draft judged: draft-08, the text the human will read at G4: draft-07 (the second line edit) with the four touches the
human chose on 2026-11-01 (DEC-035: the opening's tags, the knot sentence, what came of the recording, the Apgar line).
No verdict is spent until draft-08 exists and `make calibrate` has built its planted-defect pair from it.

The repeated dimension is `idea`, the largest gap of round 2 (lost 0 of 4 against the-machine-stops) and of round 1
(lost against exhalation and lena), tried here against a fourth exemplar whose strength it is. The three others are the
two dimensions story B has never been tried on, `opening` and `aftertaste`, and `sentences`, where the record moved most
(lost 0 of 4 against yellow-wallpaper on draft-01; lost 1 of 4 to draft-02 in the draft-03 revision pair; two line edits
since), each put against the exemplar whose strength it is, so that the bar is a real one. Exemplars are drawn to cover
the set over rounds: the-star and cat-pictures-please have not yet been read against story B; the other two are repeats
chosen for the dimension, not for the result they gave before. All four are supplied as text (4 of 4; the bar needs 3).

- idea × cat-pictures-please (text) — the repeated dimension; an AI premise used all the way down
- opening × yellow-wallpaper (text)
- sentences × exhalation (text)
- aftertaste × the-star (text)

The revision round (round-03-revision.json), per LOOP_DESIGN.md §7.2: draft-08 against draft-07, the draft before it,
and against draft-02, the draft the human signed at G3, on `idea` and `sentences`, the two dimensions every earlier
revision pair was judged on, so that the record reads across rounds; each judge told it is a revision pair and asked
what the newer draft lost.

Calibration: `make calibrate` on draft-08 (calibration-draft-08.md); both judges, both orders; a judge counts only if it
chose the true draft in both orders. One calibration serves the exemplar pairs and the revision pairs, which are judged
on the same draft in the same round. Judges as in rounds 1 and 2: craft-critic-a = Explore on the session default,
craft-critic-b = Explore on opus; a fresh context per verdict; anonymized A/B files from orchestrator/build_round.py; the
A/B assignment per order recorded in the round JSON.

Verdicts this round: 4 calibration + 16 exemplar (4 pairs × 2 orders × 2 judges) + 16 revision (2 baselines × 2
dimensions × 2 orders × 2 judges) = 36. The per-round cap stands at 32 (DEC-027), so the round waits on the human's
caps row; the G4 hand-over's figure of "about 1.3M" for this round counted 20 verdicts and was wrong by the second judge
on the exemplar pairs and by the signed baseline; at about 66K tokens a verdict the round costs about 2.4M.
