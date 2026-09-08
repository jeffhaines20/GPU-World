# The brief

The human's answers. The orchestrator asks; the human answers; after gate G0 no agent edits this file.

## The story

| Question | Your answer | Default if you have none |
|---|---|---|
| The kind of science fiction you want (literary, hard sf, adventure, absurdist, quiet and strange) | the default ("Defaults are fine", in chat, 2026-09-08) | quiet and strange, with one hard idea |
| Three to five short stories you love, and one sentence each on why | "I quite liked the Yellow Wallpaper, the Death of Ivan Ilyich, and the One who Walk Away from Omelas, although please don't let these constrain you. I quite like philosophical fiction that is well written and makes you think differently about something you had assumed." (verbatim, in chat) | |
| Two or three things you never want to read in this story | the default | a twist ending that cancels the story; a lecture in dialogue |
| Subjects to avoid entirely | the default: none | none |
| Length target inside 1,000–5,000 words | the default: about 3,500 | about 3,500 |
| Is an unhappy or unresolved ending acceptable? | the default: yes | yes |
| Is the story for you, or for a particular reader? | the default: for you. (The story is also an entry for the GPU World contest, whose judges are Neal Stephenson, Gwern Branwen and Matt Huang; the human left the default.) | for you |
| Anything the story must contain (an image, a place, an obsession) | the default, which here is the contest premise: frontier AI progress stops on 1 September 2026; by 2040 every human has around-the-clock access to the equivalent of a frontier model; business as usual, neither a simple utopia nor a simple nightmare. Nothing else. | nothing |

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
| Ten to fifteen published short stories that stand for the quality you want | "I cannot provide any, unless you happen to think it will be especially useful and worth my putting in the effort. So use all of the ones that you can get online either by fetching or because they are in the public domain as the exemplar set, including any in the reserve list you can get." (verbatim, in chat.) The resulting set is in `design/EXEMPLARS.md`. | none — only you can name your bar |
| For each: can you supply the text? Aim for at least four; three is the floor. (yes → put the file in `design/exemplars/`, any readable form, one file per story; no → the judges work from their knowledge of it, which is weaker and is recorded as such) | none from the human's own copies; every text in the set was fetched by the orchestrator from a public-domain edition or the publisher's own free page, at the human's instruction above, and `design/EXEMPLARS.md` records the source of each | none — only you know what you own |
| The eight craft dimensions in `design/RUBRIC.md` — opening, character, the idea, scene, sentences, the turn, the ending, aftertaste — weighted 1 to 3 each. See "About the weights" above | the default: all 2s | all 2s, unless you feel strongly, in which case raise two or three of them to 3 |

## Practical

| Question | Your answer | Default |
|---|---|---|
| How much of your time, in total | the default | two to two and a half hours over five sittings: 40 minutes at intake, then 20, 10, 15–25 and 30–40. That is the all-yes path; each time you send something back, add a sitting. It does not include the evening of homework before intake |
| Your name for the sign-offs | Jeff | — (there is no sensible default; it is your name) |
| The token budget for the whole project. A token is about three quarters of a word of everything the agents read and write; nothing here is charged to you by this loop, but your provider may charge for the run | "Raise the cap to 10M." (in chat, after the dry run's cost arithmetic; the handoff had said 2M) | 8M, which covers a full run — the funnel, a first draft, and twelve revision rounds with their critics — with room to spare |
| Any paid service the agents may call (an image or search API) | the default: none | none |
| Where the finished story goes | the default: `story/STORY.md`, nowhere else | `story/STORY.md`, nowhere else |

## Routing

Rows the orchestrator fills in, each with a `DECISIONS.md` row: how this harness spawns a fresh-context
agent; where the orchestrator reads its own token use; whether web search is available to the
originality critic, and if not, that its verdict rests on the critics' knowledge alone.

| Question | Answer | Decision row |
|---|---|---|
| How this harness spawns a fresh-context agent | Claude Code's Agent tool, one fresh context per call, the brief file named or inlined as the prompt; judges and critics as read-only Explore agents, builders as the default type; judges see anonymized A/B copies only | DEC-001 |
| Where the orchestrator reads its own token use | the session's remaining-token counter, plus each sub-agent's reported total from its completion notice; Used in STATE.md is the sum and is labelled an estimate | DEC-002 |
| Web search for the originality critic | available (WebSearch and WebFetch); when a search fails the report says so | DEC-003 |
| Which models | builders and judge a on the session's default model, judge b on opus, flow-critic and fresh-reader on sonnet | DEC-004 |
| The human's channel | chat only: every human row and sign-off is dictated in chat and copied in unchanged, and commits the kit asks the human to make are made by the orchestrator at their standing instruction | DEC-005 |
