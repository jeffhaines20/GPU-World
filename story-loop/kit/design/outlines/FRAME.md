# The outline pass (DEC-016, DEC-017), framed before any writer runs

**What this is.** The human chose Q-06, Practicing on People, and asked for "say, five outlines of stories that would both
convey the rich philosophical complexities of the idea and also be gripping, excellent sci-fi short stories, then again have
reviewers critique and iterate, and then present me with a ranking of the Q-06 story ideas." This pass is the third premise
pass, in a new shape: outlines rather than cards with separate probes. Like the questions funnel it is outside the kit's
skills; no check reads its outputs; its rules are declared here before any agent runs and its records stay in this folder.
The output is a ranking of five outlines, revised once against critique, for the human to pick from at G1.

**The question.** `Q-06.md` in this folder is the revised card, without the reviser's note; every writer reads it and
nothing else.

**The cut.** Five cells, one writer each, in isolation, one outline each, O-1 to O-5. The cells partition who departs from
the counsel, on whom it lands, and who audits:

| Cell | Name | Narrowing |
|---|---|---|
| O-1 | The parent | The card's own crisis: a parent who raised a child without asking the model, wanting to be the one who knew the child, and the audit when the child is grown. This is the version the card itself gives, so it is the hardest cell: a reader who has read the card will predict the list at nineteen. Find the form in which the audit does not go as the card says, or the parent is not who the card expects, or the bill is presented by someone the card did not name. The question must stay whether the parent was entitled to find out, given who paid and who can check. |
| O-2 | The apprentice | A young person in work where departing from the counsel lands on strangers' bodies or lives: a midwife, a nurse, a teacher, a pilot, a social worker, an interpreter at a border, a vet, a line cook with allergies on the ticket. Every stranger has the same model and can check the bill. The want: to become someone whose judgment is their own. The price: paid by someone who never agreed and can now read exactly what it cost. |
| O-3 | The one who never departed | A person who always followed the counsel and was, by every audit, right: flawless, and at fifty asked for the one judgment the counsel cannot give, or audited by their own child and found clean and empty. The capped-wisdom side of the question, from inside: what it is to have a life no one can fault and no judgment of one's own. Both sides must stay live: the story must not conclude that they wasted their life, nor that they did not. |
| O-4 | The audited | Told from the side of the one practiced on: the child with the list, the patient, the shamed worker, the pupil. They can run the years back through their own model and read every place the counsel would have done better. The story is the audit itself: whether to present the bill, what it costs to have been someone's practice, and whether the one practiced on would have chosen the script if asked. The question from the creditor's side. |
| O-5 | The rule | A place where departing is governed: a hospital or a guild that forbids departure in the first years; a court where the model is the standard of care, so that departure is negligence in itself; a religious order, a village, a school for judges, a union, a family with a written rule. Someone who must break the rule to become a judge of anything, and the ones who made the rule because they once paid for somebody else's growth. The political and legal version of the question, carried by one person in one place. |

**The writers' brief**, identical but for the cell, is kept verbatim in `writer-prompt.md`. It gives the contest, the
project's reading of the premise, the human's taste in their words, the exemplar titles for register, the M1 premise-writer
rules (a person first, a turn that cannot change back, a last image, the obvious version named and not written, the closest
published story named honestly or "none", no moral) and the outline shape below. Writers reply with the outline; the
orchestrator saves the reply verbatim to `outlines/O-N.md`.

**The outline shape**, fixed: the M1 card fields (Conceit, Who, Obstacle, Turn, Last image, Question, Not the obvious
version, Closest published), plus three the human's advice asks for (What the reader assumed and no longer does; Why it
cannot be predicted, and why it is earned; Beats: six to ten scenes, what changes in each), plus The passage: 250 to 350
words of the hardest scene, so that "gripping" and "excellent" can be judged on prose and not on promise. At most 1,000
words before the passage.

**The review.** Two reviewers, fresh contexts, each reading all five in one batch (the cap is six), order shuffled with
recorded seeds (`batches.json`, written before the writers ran), neither seeing the other. Reviewer a runs on the session's
default model, reviewer b on opus. Seven axes, 1 to 5 each: **question** (both sides live, dramatized, not settled),
**surprise** (not predictable; the turn earned), **insight** (the reader thinks differently about something assumed),
**grip** (want, price, pressure, a scene one cannot leave), **person** (particular, placed, embodied), **ending** (the last
image earned and open), **prose** (from the passage, against the best published SF). One sentence each, plus one sentence
naming the largest gap. Per batch: which they would read to the end, which is most surprising, which does not survive. The
prompt is kept verbatim in `reviewer-prompt.md`. Alongside, one **originality critic** in the kit's shape (the closest
published works, Derivative MAJOR / In conversation / Familiar furniture / Unfamiliar, what it did not check) reads all
five; its report is saved verbatim as `reviews/REV-03.md` so that `check_reviews.py` counts its findings, and gets a
disposition after the revision.

**The ranking, declared now.** A total is the sum of seven axes, out of 35. Ranking A pulls each reviewer's total halfway
toward that reviewer's pool median and takes the mean; ranking B is the highest single-reviewer total; an outline is
disputed at a gap of seven or more (a fifth of the scale, as five of twenty-five was). Ties on A are broken by the
reviewers' read-to-the-end picks, then by question plus surprise. Cell coverage does not apply: one outline per cell.

**The iteration.** All five go to fresh revisers (the human asked for a ranking of the five, not a cut), each with its
outline, both reviewers' critiques of it and the originality critic's note on it, and nothing else. The reviser strengthens,
narrows or reports that the outline does not survive, and rewrites it in the same shape with `Status: revised`, then a
"What changed" note of at most 150 words that the round-2 reviewers never see. Two fresh reviewers score the revised five
with the same prompt and seeds recorded in advance; the final ranking is that round's ranking A. The human receives all
five revised outlines in full, both rounds' scores, the verdicts, the originality report and the movement from round 1;
an outline a reviser or reviewer says does not survive is named as such and stays in the ranking.

**Routing (DEC-018).** Writers, revisers and the originality critic run as read-only Explore agents on opus (the
premise-writer and originality-critic briefs name opus); reviewers a and b on the session default and opus. Each replies
with its text and the orchestrator saves the reply verbatim with `orchestrator/save_reply.py`; nothing is edited. Rule 1
holds: a fresh context per call, the brief as the prompt, no agent grading its own work.

**Caps.** Five premise-writer calls (13 to 18, DEC-017) and five premises (52 to 57). Reviewers and the originality critic
draw on the six premise-judge calls unspent: 2 + 1 in round 1, 2 in round 2, one left. No probe row is drawn on: the passage
is part of the outline.

**Cost, estimated.** Writers 5 × about 40K, reviewers 2 × 45K, originality about 60K, revisers 5 × 60K, re-review 2 × 45K,
the orchestrator about 0.3M: about 1.1M in all, leaving about 1.7M of the 10M. That does not reach the spine and a first
draft (about 0.3M and 1.1 to 1.7M); the token cap is put to the human again with the ranking.
