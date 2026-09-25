# The shape of a comparison record

One file per comparison round, `reviews/comparisons/round-NN.json`, numbered from 01, written by the orchestrator after the
round's judging. `check_comparisons.py` reads the newest of these and refuses a round that does not have
this shape. Nothing else in the kit writes this file, so it is written by hand from what the judges
returned, and the shape below is the whole contract.

```json
{
  "round": 3,
  "draft": "draft-04",
  "draft_sha256": "<sha256 of the draft's body, the text after the front matter>",
  "calibration": {
    "planted": "tic-pass, flattened-rhythm, ending-cut-to-summary",
    "pair_file": "calibration-draft-04.md",
    "pair_sha256": "<sha256 of that file, which make calibrate prints>",
    "verdicts": {"craft-critic-a": "caught", "craft-critic-b": "caught"},
    "passed": true
  },
  "pairs": [
    {
      "exemplar": "salt-gardeners",
      "dimension": "ending",
      "order": "AB",
      "choice": "A",
      "from_memory": false,
      "judge": "craft-critic-a",
      "confidence": 4,
      "reason": "one sentence, in the judge's words",
      "evidence": "the phrase or moment in each text the judge is pointing at",
      "needs": "what the weaker text would have to do to win this dimension"
    }
  ]
}
```

**Field by field.**

- `draft` — the stem of the draft judged, `draft-NN`, and `draft_sha256` is the sha256 of that file's
  body, the text after the front-matter lines. `python3 -c "..."` is not needed: `checks/calibrate.py`
  prints it, and `check_comparisons.py` recomputes it and fails when the draft has moved on.
- `calibration` — this round's planted-defect result. `planted` names the defects `make calibrate` says
  actually landed; `pair_file` and `pair_sha256` are the weakened copy it wrote and the hash it printed,
  and the check opens that file and re-hashes it. `verdicts` gives one entry per judge that voted this
  round, `"caught"` when that judge chose the true draft over the weakened copy in **both** orders,
  `"missed"` otherwise; `passed` is true only when every judge caught it. An empty `verdicts` is not a
  pass, a judge that appears on a pair and not in `verdicts` fails the round, and so does a `missed`.
- `pairs` — one entry per verdict, so a pair judged in both orders is **two** entries with the same
  `exemplar` and `dimension` and different `order`.
- `order` — `"AB"` when the loop's draft was shown first, `"BA"` when the exemplar was. `choice` is the
  letter the judge picked. So the loop's draft won that verdict when `order` is `AB` and `choice` is `A`,
  or `order` is `BA` and `choice` is `B`; the check does this arithmetic, you do not.
- `from_memory` — true when the exemplar's text was not supplied and the judge worked from its knowledge
  of the story. A gate needs at least the number of full-text verdicts in `checks/thresholds.json`.
- `judge` — the agent, and where two judges ran, a name that distinguishes them (`craft-critic-a`), so
  that the calibration verdicts can be matched to the judges that voted. Whatever name you use here is
  the name that must appear in `calibration.verdicts`: the check matches the two verbatim, so a judge
  called `craft-critic-a` there and `craft-critic` here reads as a judge that voted and was never
  calibrated, and fails the round. The example above uses the suffixed form in both places for that reason.
- `reason`, `evidence`, `needs` — the craft critic produces five things and the record holds all five.
  `reason` is why the winner won, in one sentence; `evidence` is the phrase or the moment in each text
  the judge is pointing at, which is what makes a soft verdict checkable by a reader who was not there;
  `needs` is what the weaker text would have to do to win this dimension, and it is the one field the
  writer acts on. All three must be non-empty. A verdict with a choice and no evidence is a preference,
  not a comparison.

**The signed-draft baseline.** Once the human has signed a draft at G3, the revision record carries a
second block beside `pairs`, judged the same way, against the draft they signed:

```json
  "baseline_signed": {
    "draft": "draft-04",
    "pairs": [
      { "exemplar": "draft-04", "dimension": "sentences", "order": "AB", "choice": "A",
        "from_memory": false, "judge": "craft-critic-a", "confidence": 3,
        "reason": "...", "evidence": "...", "needs": "...",
        "lost": "the older draft's third paragraph had a joke this one has smoothed away" }
    ]
  }
```

It exists because draft N against draft N−1 cannot see the failure it is named for. A story sanded one
degree flatter every round beats its own immediate predecessor every single time — each revision is a
small improvement — and only a pairing far enough back shows the accumulation. Same rules as the rest of
the record: both orders, calibrated judges, `min_revision_pairs` at a gate, and every verdict answers
what was lost.

**A round whose judges failed calibration** is not evidence, and nothing is ever deleted — so it stays on
disk carrying `"superseded_by": "round-03.json"`, naming the round that was run in its place with
calibrated judges. The named round must exist and be judged on the same draft, and a round whose own
calibration passed may not be superseded: this is the record of a calibration failure, not a way to
retire a result you did not like.

**A revision round** — draft N against the draft it replaced, and against the draft the human last signed —
is recorded the same way in `reviews/comparisons/round-NN-revision.json`, carrying the number of the round
whose revision produced draft N. It is written once, at the end of the round, not alongside the exemplar
round. It carries `"previous": "draft-03"` beside `draft`, sets each entry's `exemplar` to that older
draft's stem, carries a `calibration` block like any other round — and note that this is **not** the block from step 2
of the same round: that one was calibrated on draft N−1, and the revision round is judged on draft N. Run
`make calibrate` again once the new draft exists, on the draft the record names. (At M4 the two coincide,
because both rounds are judged on the final draft; everywhere else they do not.) Every entry carries one
extra field, `lost`, holding the
judge's answer to "what did the newer one lose" — `"nothing lost"` is an answer and must be written.
`check_comparisons.py` requires a revision round at any gate once more than one draft exists, and refuses
one whose entries do not carry `lost`. Whether to revert is the orchestrator's call under the m3 skill;
this record is the evidence for it, and what the human reads at the gate.

**Numbering.** Rounds are `round-01.json`, `round-02.json`, and so on. The check reads the highest-
numbered file, so a round is never overwritten and two rounds can happen in one day. Nothing here is ever
deleted.
