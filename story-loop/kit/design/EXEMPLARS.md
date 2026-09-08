# The exemplar set

The bar. Ten to fifteen published short stories the human named at intake. The story is measured
against these and against nothing else.

**Provenance matters and is recorded.** Where the human supplied the text, it sits in
`design/exemplars/` and comparisons are made against the words. Where they could not, the comparison is
made against the judge's knowledge of the story, is recorded with `from_memory: true`, and counts less:
the gate at M3 and M4 requires at least **three of a round's four pairs** to be judged against text the
human supplied (`checks/thresholds.json`, `min_full_text_pairs_at_gate`). A **pair** is one exemplar on
one dimension, judged in both orders — so a round of four pairs is eight verdicts, and "three pairs on
supplied text" means three of the round's four exemplars, not three verdicts.

Below three supplied texts in the whole set the loop cannot meet that at all, and `LOOP_DESIGN.md` §11
tells the orchestrator to stop at intake and say so rather than proceed quietly. Four or more is what
makes a round's exemplars vary from round to round instead of repeating the same three.

**Copyright.** These texts are the human's copies, used here to judge one story against them. Nothing
from an exemplar is reproduced in the manuscript, and a comparison quotes at most one sentence from each
side as evidence.

| # | Title | Author | Year | Text supplied | Why the human named it |
|---|---|---|---|---|---|
