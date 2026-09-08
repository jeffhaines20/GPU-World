# The brief

The human's answers. The orchestrator asks; the human answers; after gate G0 no agent edits this file.

## The story

| Question | Your answer | Default if you have none |
|---|---|---|
| The kind of science fiction you want (literary, hard sf, adventure, absurdist, quiet and strange) | | quiet and strange, with one hard idea |
| Three to five short stories you love, and one sentence each on why | | |
| Two or three things you never want to read in this story | | a twist ending that cancels the story; a lecture in dialogue |
| Subjects to avoid entirely | | none |
| Length target inside 1,000–5,000 words | | about 3,500 |
| Is an unhappy or unresolved ending acceptable? | | yes |
| Is the story for you, or for a particular reader? | | for you |
| Anything the story must contain (an image, a place, an obsession) | | nothing |

## The bar

These three are the questions only you can answer, so two of them have no default. The story is measured
against the set you name here and against nothing else.

**About the weights.** Every comparison asks a judge about **one** craft dimension at a time, because a
judge asked for an overall verdict answers about whichever dimension it happened to notice. The weight
decides how often a dimension is the one being tested: a 3 comes up in most rounds, a 2 in about half, a 1
in some. All eight are tested in the final round whatever the weights, so a 1 is *tested less often*, not
*ignored*. All 2s is a perfectly good answer and means "no strong feelings, test them evenly". A 0 removes
a dimension entirely and needs a decision row saying why; that is rare and you do not need it.

| Question | Your answer | Default |
|---|---|---|
| Ten to fifteen published short stories that stand for the quality you want | | none — only you can name your bar |
| For each: can you supply the text? Aim for at least four; three is the floor. (yes → put the file in `design/exemplars/`, any readable form, one file per story; no → the judges work from their knowledge of it, which is weaker and is recorded as such) | | none — only you know what you own |
| The eight craft dimensions in `design/RUBRIC.md` — opening, character, the idea, scene, sentences, the turn, the ending, aftertaste — weighted 1 to 3 each. See "About the weights" above | | all 2s, unless you feel strongly, in which case raise two or three of them to 3 |

## Practical

| Question | Your answer | Default |
|---|---|---|
| How much of your time, in total | | two to two and a half hours over five sittings: 40 minutes at intake, then 20, 10, 15–25 and 30–40. That is the all-yes path; each time you send something back, add a sitting. It does not include the evening of homework before intake |
| Your name for the sign-offs | | — (there is no sensible default; it is your name) |
| The token budget for the whole project. A token is about three quarters of a word of everything the agents read and write; nothing here is charged to you by this loop, but your provider may charge for the run | | 8M, which covers a full run — the funnel, a first draft, and twelve revision rounds with their critics — with room to spare |
| Any paid service the agents may call (an image or search API) | | none |
| Where the finished story goes | | `story/STORY.md`, nowhere else |

## Routing

Rows the orchestrator fills in, each with a `DECISIONS.md` row: how this harness spawns a fresh-context
agent; where the orchestrator reads its own token use; whether web search is available to the
originality critic, and if not, that its verdict rests on the critics' knowledge alone.
