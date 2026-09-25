# The rubric

The craft dimensions every comparison and every critic works from. The human weights them at intake (1 to 3). The weight decides how
often a dimension is the one a comparison round tests: a 3 comes up in most rounds, a 2 in about half, a 1
in some. Everything is still checked at the final round; the weights say what the story is mostly judged
on along the way. A weight of 0 removes a dimension, and needs a decision row saying why.
A comparison judges **one** dimension at a time, because a judge asked for an overall verdict gives
whichever dimension it happened to notice.

The **Slug** column is the exact string a comparison record's `dimension` field takes — lower case, one word, no article. `check_comparisons.py` groups pairs by that string, so `ending` and `The ending` are two different dimensions to it, and a round written with both looks like eight dimensions tried once instead of four tried twice. Use the slug in the record and the full name in prose.

| Dimension | Slug | The question a judge is asked | Weight |
|---|---|---|---|
| Opening | `opening` | Which story earns the next page faster, and how? | 2 |
| Character | `character` | In which story does a person want something, and pay for it? | 2 |
| The idea | `idea` | Which story's science-fictional idea is stranger and better used — not which idea is cleverer, but which is more *used*? | 2 |
| Scene | `scene` | Which story puts you in a place with people doing things, rather than telling you about it? | 2 |
| Sentences | `sentences` | Which story's prose would you rather read for an hour? | 2 |
| The turn | `turn` | In which story does something change that cannot change back? | 2 |
| The ending | `ending` | Which ending is both surprising and inevitable? Which one earns its last image? | 2 |
| Aftertaste | `aftertaste` | A day later, which one would you still be thinking about, and about what? | 2 |

**How a judge answers.** A forced choice (A or B, no ties offered), one sentence of reason, at most one
sentence quoted from each as evidence, and a confidence from 1 to 5. Ties are produced by the
mechanism, not by the judge: a pair whose two orders disagree is recorded as a tie.

**What the rubric is not.** It is not a score to maximize. No agent ever computes a total. The
dimensions exist so that a comparison is about something, and so that a story losing every pairing on
one dimension is visible.
