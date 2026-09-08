# The Story Loop: a build loop for one excellent science-fiction short story

*Version 0.4 · 2026-09-08 · a design specification, not yet a tested deployment. 0.4 answers review round 3 (`reviews/REV-07.md` adversarial, `REV-08.md` cold orchestrator check, `REV-09.md` cold human read): 21 MAJOR, 25 MINOR, 10 NIT across the three, on top of round 2's 16 MAJOR and round 1's 20. All dispositioned in `reviews/`; `README.md`'s "Review status" section is the running account.*

A loop for agents to write one science-fiction short story of 1,000 to 5,000 words that a good editor would place beside the acclaimed short fiction of the field. It is built on the loop-engineering material at the root of this repository, and on the postmortem of the first loop built from it (`POSTMORTEM-dungeon-crawler-loop.md`), whose central lesson is written into this design: **a claim in these documents that nothing performs is a defect, and late in a review a promise is closed by narrowing it, not by building machinery.**

---

## 1. The design card

**Objective.** One finished science-fiction short story, 1,000 to 5,000 words, in English, written to be read once and remembered.

**Bar.** A set of ten to fifteen published stories the human names at intake — the exemplar set. The story is at the bar when fresh judges, comparing it blind and in both orders against those stories, place it at or above the middle of that set on the craft dimensions in `design/RUBRIC.md`, and no critic has a MAJOR finding open. The bar is a set of real stories rather than a score, because a score is a thing agents optimize and a story is not.

**Verification, in order of authority.**

1. **Mechanical** (a program decides): length in range; the manuscript has no placeholder text; invented names, terms, and facts are used consistently with the story bible; every review has a disposition naming what changed; every blind comparison was run in both orders by a judge that passed calibration that round.
2. **Measured** (a program reports; a person or a critic reads the report): prose tics and their density, sentence-length variance, paragraph outliers, repeated openers and repeated distinctive words. These are printed, not gated, except at the extremes stated in `checks/thresholds.json`, because prose that optimizes a tic count is worse prose.
3. **Blind comparison** (a fresh judge, order-swapped, anonymized): the story against exemplars, and the current draft against the previous draft.
4. **Judgment** (fresh critics with the artifact and the bar only): craft, flow, depth, originality, and one general reader.

The tiers are ordered by how hard each is to fool. Nothing in tier 4 gates anything until the judges have been calibrated that round against a planted defect (§7.3).

---

## 2. The shape

Five milestones, five human gates, one story.

| Milestone | What comes out of it | Gate |
|---|---|---|
| M0 Intake | the human's taste brief, the exemplar set, the caps, the rubric | G0: the human reads the brief back and signs |
| M1 Premise funnel | twenty-four premises generated in isolation, compressed to cards, probed, judged, three offered | G1: the human picks the premise |
| M2 Spine | the premise as a spine (character, want, obstacle, turn, ending image, the question), a 300-word probe passage, the story bible | G2: the human reads the spine and the probe |
| M3 Draft and revise | the draft, revised in rounds against the critics until the stop conditions fire | G3: the human reads the first complete draft |
| M4 Final | line edit, title, the read-aloud pass, the finished story | G4: the human reads it aloud and signs |

The human's total time is two to two and a half hours across five sittings: forty minutes at intake (G0), twenty choosing the premise (G1), ten on the spine (G2), fifteen to twenty-five on the first full draft (G3), thirty to forty on the finished story read aloud (G4) — the last two vary with how long the story ran, and a read-aloud is slower than a read. That total is the path where they say yes at every gate; each send-back adds a sitting, and §8 says what each one costs them. It also excludes the evening before intake in which they assemble the exemplar set, which is the largest single thing this design asks of a person. Every gate is a stop: the loop writes what it needs into `INBOX.md` and waits. No gate is signed by an agent.

**Why a funnel before a loop.** Which premise to write has no cheap evaluator: nothing can test a premise the way a check tests a word count. The handoff document's answer is a funnel — generate wide and in isolation, compress, buy information before judging, then let the human choose from a shortlist. Everything after M1 does have evaluators, so everything after M1 is a loop.

---

## 3. What the loop may not do

- Publish, submit, post, or send the story anywhere.
- Spend money, or call a paid service that is not named in `BRIEF.md`.
- Reproduce more than a quoted phrase from any exemplar or any other copyrighted text in the manuscript, the reviews, or the notes. Comparisons quote at most one sentence, for evidence.
- Delete a draft, a review, or a comparison record. Every draft is kept in `story/drafts/`.
- Write, edit, or paraphrase the human's gate sign-off.
- Pass off text written by another author as the story's own, in whole or in part.
- Continue past a cap in `STATE.md` without the human's decision.

---

## 4. The milestones

### M0 — Intake

**Purpose.** Turn "write a good science-fiction story" into a bar an agent can inspect and boundaries it cannot cross.

**What happens.** One sitting with the human, about forty minutes, in one message and then a few exchanges. The orchestrator asks every blank row in `BRIEF.md`: the register (literary, pulp adventure, hard sf, absurdist, quiet); three to five stories the human loves with one sentence each on why; two or three things they never want to read; whether there are subjects to avoid; the length target inside 1,000 to 5,000; whether a downbeat ending is acceptable; and the exemplar set.

**The exemplar set is the bar and needs care.** The human names ten to fifteen published short stories. For each one, the orchestrator asks whether the human can supply the text (a file they own). Where the text is supplied, comparisons are made against the words. Where it is not, comparisons are made against the judge's knowledge of that story and are recorded as `from_memory`, and the gate at M3 requires at least three of a round's four pairs to be judged against supplied text, because a judgment about a text nobody re-read is weaker evidence and the design says so rather than hiding it.

**Outputs.** `BRIEF.md` complete; `design/EXEMPLARS.md` with the set and its provenance; `design/RUBRIC.md` (the craft dimensions, weighted by the human); caps in `STATE.md`; the first `DECISIONS.md` rows.

**Where it fails.** Skipping the taste questions, which produces a competent story the human does not like; or accepting an exemplar set of one kind, which produces a pastiche of that kind.

### M1 — The premise funnel

**Purpose.** Find the one premise worth five thousand words, and know why it beat twenty-three others.

**What happens, in the handoff document's order.**

1. **Frame before generating.** The orchestrator writes `design/PARTITIONS.md`: the axes the premise space is cut along, and the cells. The default partition is the *source of strangeness* (a technology, a biology, a cosmology, a social arrangement, an alteration of physics, an alteration of mind) crossed with the *emotional register* the human chose. Written before any premise exists, so the generators cannot all drift to the same corner.
2. **Generate wide, in isolation.** Six `premise-writer` agents, each in a fresh context, each given one cell, the taste brief, and nothing else — not the other cells, not each other's output. Four premises each: twenty-four.
3. **Compress to cards.** Each premise becomes a card in `design/PREMISES.md` with a fixed shape: the conceit in one sentence; who the story is about and what they want; the obstacle; the turn; the last image; the question the story leaves; why this is not the obvious version of this idea; and the closest published story the writer knows of, with what differs.
4. **Strike the known stories.** The `originality-critic` reads all twenty-four cards and marks any that are a published story wearing a hat; those are struck with the name of the story, before anything is spent probing them.
5. **Judge the cards.** Two `premise-judge` agents, fresh, score the survivors against the rubric in batches of at most six, order shuffled per batch, never seeing who wrote what or each other's scores. Two rankings are kept: one on scores shrunk toward the pool median, so a single enthusiastic score does not carry a premise, and one on each card's highest single-judge score.
6. **Probe six.** Five from the shrunk ranking, no more than two from one cell, and the sixth slot reserved for the highest card on the second ranking that the first did not take — usually the one the judges disagree about. A `probe-writer` writes 250 to 350 words of the single hardest passage for each. This is the funnel's "buy information": prose reveals in a page what a card cannot. Then step 5 runs again over cards-and-probes.
7. **Select.** Three finalists to the human in `INBOX.md`, each with its card, its probe, the originality note, and any disagreement between the judges stated as a disagreement; the third slot is reserved for the most disputed surviving card. The human picks one, or asks for another cell to be regenerated. The M1 caps — writer calls, premises, probe passages and judge calls alike — are each sized for exactly one regeneration, so the first send-back costs them nothing and needs no decision row; a second one does.

**Done when** no critic holds a MAJOR objection against the chosen premise and the human's pick is recorded as a decision row.

**Where it fails.** Generating before framing (every premise lands in the same cell); judging cards without probes (the card that reads well and has no prose in it); the human handed one option instead of three.

### M2 — The spine

**Purpose.** Make the expensive mistakes cheap. A spine is a page; a draft is a week.

**What happens.** The `story-architect` turns the premise into `story/SPINE.md`: the point-of-view and tense with one sentence on why; the character, their want, and the thing they are wrong about; the obstacle; the turn, in one sentence; the ending image and what it costs; the philosophical or psychological question the story is actually about, and the answer it refuses to give; four to six beats; the target length inside the human's range. It writes `story/BIBLE.md` at the same time: names, invented terms and their spellings, the rules of the conceit, the timeline, the physical details that must stay consistent.

The `depth-critic` and the `adversarial-critic` read the spine and the M1 probe. A MAJOR here (the turn is not a turn; the question is a slogan; the ending is the premise restated) is fixed on the spine, not in the draft.

**Where it fails.** A spine that is a summary rather than a structure; an ending chosen because it is neat.

### M3 — Draft and revise

**Purpose.** The story.

**Order of work.** The `story-writer` writes the whole draft to `story/drafts/draft-01.md` before anything is revised, because a story revised paragraph by paragraph never learns its own shape. Then rounds, each one:

1. The mechanical and measured checks run (`run_all_checks.py --milestone 3`).
2. The critics run in fresh contexts, each given the draft and the bar and nothing else — never the writer's notes, never each other's reports, never the revision history: `craft-critic` (blind comparison against exemplars), `flow-critic`, `depth-critic`, `adversarial-critic` (persistent, keeps its history), and every third round `fresh-reader` and `originality-critic`.
3. `close-review` writes a disposition for every review: FIXED with what changed, REJECTED with the reason, DEFERRED with the trigger.
4. The `story-writer`, in a fresh context, revises against the findings only.
5. The new draft is compared against the previous draft (§7.2). A revision that loses more than it gains is reverted and the ledger records a changed approach.
6. A row in `LEDGER.md`: round, the largest gap, the approach taken.

**Done when** the stop conditions in §9 fire and the human has signed G3 on a complete draft.

**Where it fails.** Revising before the draft is complete; the same finding surviving two rounds under the same approach, with no changed approach written down before a third (the spinning rule); a revision that flattens the story's one distinctive thing.

### M4 — Final

**Purpose.** Turn a finished draft into a finished story.

**What happens.** A line edit pass by the `line-editor` against the flow critic's marks; the title (three candidates, the human picks); the read-aloud pass, in which the `flow-critic` reads the story sentence by sentence and marks every place a reader would stumble, and the human reads it aloud at the gate; the fresh reader, the adversarial critic, and the originality critic on the text the human will sign — the fresh reader's question, whether there is one thing worth remembering tomorrow, is the question closest to the objective and is asked here rather than four drafts back; a final full comparison round, calibrated, with its draft-against-draft round; the finished file at `story/STORY.md` with a word count and the exemplar set it was measured against.

---

## 5. The roles

| Agent | Kind | Gets | Never gets | Produces |
|---|---|---|---|---|
| `premise-writer` | builder (×6, one per cell) | the taste brief, one partition cell | other cells, other premises | four premise cards |
| `probe-writer` | builder | one card, the taste brief | the judges' criteria | 250–350 words of the hardest passage |
| `premise-judge` | critic (×2) | cards and probes, the rubric | who wrote what, the other judge | scores with one reason each |
| `story-architect` | builder | the chosen premise, the brief | the other premises | `SPINE.md`, `BIBLE.md` |
| `story-writer` | builder | the spine, the bible, the findings to address | the critics' reasoning, the comparisons | a draft |
| `craft-critic` | critic | two anonymized stories, the rubric dimension | which is the loop's, the prior verdicts | a forced choice, a reason, what the weaker needs |
| `flow-critic` | critic | the draft | the spine, the intent | every stumble, by line, with the reason |
| `depth-critic` | critic | the draft (or the spine, at M2) | the writer's statement of theme | whether the question is real and the psychology is true |
| `originality-critic` | critic | the cards, or the draft | the writer's claim of originality | the closest published works, what differs, and what it cannot rule out |
| `fresh-reader` | critic | the draft only | everything else | where attention dropped, what confused, whether the ending landed |
| `adversarial-critic` | critic, persistent | the draft, its own history | the other critics' current reports | the story's load-bearing weakness, ranked findings, the sharpest question |
| `line-editor` | builder | the draft, the flow marks | the critics' judgments | a line-edited draft |

**The firewall.** A critic receives the artifact and the bar, and its claim is in its prompt. It never receives the builder's reasoning, the disposition history, or another critic's current report. The handoff document is explicit that hiding files is not a firewall when the work product carries its own history; here the work product is a story, which does not, so the firewall holds if the critic is given the manuscript and the rubric and nothing else. The one exception is the adversarial critic, which keeps its own history on purpose.

---

## 6. What each check does, and what it cannot prove

| Check | Refuses | Cannot prove |
|---|---|---|
| `check_manuscript.py` | a draft outside the length range (below it only when the draft is called complete); placeholder text (TODO, TK, XXX, lorem, bracketed stage directions); a missing front-matter field; drafts numbered with a gap or a repeat, so an earlier draft is shadowed | that the words are good |
| `check_tics.py` | only the extremes in `thresholds.json`: adverb and filter-word density, sentence-length variance below a floor, four paragraphs opening on one word, a paragraph past the maximum, and a distinctive word repeated past the limit without a reason in the bible's Motifs table. Names and invented terms are never counted as repeats. Everything else is printed | that prose free of tics is alive |
| `check_continuity.py` | a name or invented term in the manuscript one character from the bible's spelling; a bible entry the story never uses. It reads the Names and Invented-terms tables only: the Rules, Timeline, and Physical-details sections are prose no program parses, and it prints the capitalised words the bible does not list so that a name nobody declared is visible | that the conceit makes sense, or that the timeline is possible |
| `check_reviews.py` | a review with findings and no disposition; a disposition that does not name every finding once, or with a blank Finding cell; a Disposition cell that is not exactly FIXED, REJECTED, or DEFERRED; a FIXED row naming no draft, or a draft that does not exist; a finding with no severity; a MAJOR rejected without naming a review that exists and is not the one being dispositioned, or a decision row the human wrote; at a gate, a MAJOR left deferred | that the fix was any good |
| `check_comparisons.py` | a round with no calibration, an empty verdict list, a judge that voted and was never calibrated, or a calibration whose pair file is missing or altered; a pair judged in one order only; a round whose draft hash is not the current draft's (at a gate); at a gate, too few different exemplars, too few pairs on supplied text, ties counted as wins, a round mostly ties, a dimension the draft lost against every one of two or more different exemplars, or an earlier round on the same draft that did not meet the bar. The draft-against-draft round is held to the same calibration as any other, must carry a minimum number of pairs, and every one of its verdicts must answer what the revision lost; a gate with no such round fails | that the judges have taste, or that a judge was given nothing but the two texts — the firewall is the fresh context and rule 2, not this check |
| `check_state.py` | a cap with a blank Used, or overspent past its value, or above the value the human accepted, or added or dropped without a new acceptance; a milestone advanced past a gate with no sign-off; from M3, a missing or unreadable revert counter, or three reverts in a row | that the numbers are honest, since Used is the orchestrator's estimate |
| `check_gate.py` | a gate sign-off that changed after it was saved, unless the human wrote a `gate-amend` decision row naming that gate — and each such row is spent on one change, so a second edit needs a second row; a `DECISIONS.md` gate section that no longer matches the record | that the human, rather than the orchestrator, typed the words. Nothing can check that. What protects a sign-off is that no agent may write one and that any later change to it fails every run until the human says in their own row that they made it |
| `run_all_checks.py` | runs the above in order and refuses if the fault suite has not been run since a check changed | — |

Every check prints what it does not stop. The postmortem's largest single class of defect was a document claiming a verifier that did not exist; `check_claims.py` is the mechanical half of the answer: every `check_*.py`, `make` target, agent name, skill name, and kit path named anywhere in these documents must resolve to something that exists, and it fails on any that does not. It matches identifiers, not sentences, so a claim written without naming a check — "the flow is verified at every round" — is invisible to it, and catching that is a reviewer's job.

---

## 7. The three evaluators that carry the weight

### 7.1 Blind comparison against the exemplars

A round of comparisons is: the current draft, stripped of title and byline, against four exemplars drawn to cover the set over time. Each pair is judged twice, in both orders, by a fresh judge that receives the two texts, one rubric dimension, and no other context. The judge returns a forced choice, one reason, one sentence of evidence quoted from each, and a confidence. A pair whose two orders disagree is recorded as a tie and counted as noise, not as a win. The record is `reviews/comparisons/round-NN.json`, numbered so that two rounds in one day are two records and nothing is overwritten; its shape is `reviews/comparisons/RECORD_SHAPE.md`, which is the contract the orchestrator writes to. It carries the pairs, the orders, the verdicts, the judge, the draft's hash (a short string computed from the text, which changes if a single word changes, so a record cannot be quietly re-pointed at a later draft), and whether each exemplar was full text or from memory.

**The bar at G3 and G4**, and this is what §1's "at or above the middle of the set" means in practice, counted **within the one round that the gate rests on** rather than added up over the project: the round covers at least four different exemplars; at least three of its four pairs were judged against text the human supplied; the draft wins outright — both orders agreeing — at least half the pairs; no more than a third of the pairs are order-disagreements, since a round that noisy is not evidence; and there is no rubric dimension it loses on against every one of two or more different exemplars. That last rule needs the two: with four exemplars spread across eight dimensions a dimension is usually tried once, and one lost pairing is the story losing to a better story on one thing, which the win share already counts. Failing the round for it would make the real bar “never cleanly lose a single pairing”, which is not the bar stated here. A single loss is printed instead, with the suggestion to try that dimension against a second exemplar next round. A pair whose orders disagree is a tie: it is not a loss and it is not a win, and it never counts toward the bar.

### 7.2 The draft against the draft before it

The same mechanism, applied to draft N against **two** baselines: draft N−1, and — from the moment the human has signed a draft at G3 — the draft they signed. Both go in `reviews/comparisons/round-NN-revision.json` (the shape is in `reviews/comparisons/RECORD_SHAPE.md`, which gives the `baseline_signed` block), with one extra question the craft critic is told to answer only for a revision pair, and which is question 6 of its brief: *what did the newer one lose?* The second baseline is the one that matters and it is worth saying why. A story sanded one degree flatter every round beats its own immediate predecessor every single time — each individual revision really is a small improvement — so a pairing against N−1 is structurally blind to the failure this section is named for. Only a baseline far enough back shows the accumulation, and the last draft a person actually read and signed is the right distance. `check_comparisons.py` requires the block at a gate once a G3 sign-off exists. Every verdict in that record carries the answer, and "nothing lost" is an answer that has to be written; `check_comparisons.py` requires the record at any gate once more than one draft exists and refuses one whose verdicts do not carry it. This is the answer to the failure mode that ends most revision loops, in which each round makes the story more correct and less alive. If the judge names something lost and the pair does not go to the newer draft, the revision is reverted: the orchestrator writes the older text out as the next numbered draft with a note, raises the revert counter in `STATE.md`'s process signals, and records a changed approach in `LEDGER.md`. The decision is the orchestrator's and the record is the evidence for it; `check_state.py` reads the counter and stops the loop at three reverts in a row.

### 7.3 Calibrating the judges before they gate

Soft judges are the whole tier-4 apparatus, and a soft judge that approves anything is worse than no judge. A judge in this loop is one spawned critic, and the round's judges are named in the record (`craft-critic-a`, `craft-critic-b`) so that a verdict can be traced to the judge that gave it. Before any comparison round counts, those same judges are run on a control pair built for that round by `make calibrate`: the current draft against a deliberately weakened copy of itself, in which one defect has been planted — the ending flattened to a summary, a scene replaced by exposition, or a tic pass applied. A judge that prefers the weakened copy, or that calls the pair equal, is not calibrated that round and its verdicts are discarded. `check_comparisons.py` enforces the whole of this: the record names the pair file and its hash and the check re-hashes it, an empty verdict list is not a pass, and a judge that voted on a pair and appears in no verdict fails the round. The weakened copy is written with no header naming it, so a judge cannot tell a calibration pair from a comparison, and `make calibrate` reports only the defects it actually managed to plant.

This is the fiction analogue of a fault suite: it tests the evaluator rather than the artifact, and it is the one mechanism in this design that makes a soft verdict admissible.

---

## 8. The human's part

| Gate | What they do | About |
|---|---|---|
| G0 | read the brief back, correct it, sign | 40 min with intake |
| G1 | read three premise cards and three probes; pick one, or send one back — which regenerates that whole idea-category, four fresh premises probed and judged again, about a day of the agents' time and none of theirs; a second regeneration needs a caps decision row. Two things to save: the pick as a decision row (`make decide TYPE=pick`), and the paragraph as the gate sign-off (`make gate N=1`). The row is which story; the paragraph is what you thought | 20 min |
| G2 | read the spine and the probe passage; say whether this is the story they want. If not, the spine is rewritten and comes back to you; if the premise itself is wrong, the loop returns to M1's runner-up premises rather than drafting | 10 min |
| G3 | read the first complete draft, once, without notes; say what they felt and what must change. Whatever you say becomes findings the revision rounds must answer; you are not signing the story off here, only saying what it did to you, so `make gate N=3` prints a different question and does not ask whether it goes through | 15–25 min, with the length of the draft |
| G4 | read the finished story aloud; sign, or send it back. Sending it back takes the paragraph as findings, runs one to three more revision rounds — a few days — and returns the story for another reading aloud: a sixth sitting of the same length, and a second refusal a seventh. Say this to them at the gate, in `INBOX.md`, before they decide; a gate that describes only the yes is not asking a question | 30–40 min, with the length of the story |

Signing is a paragraph in `DECISIONS.md`, three to five sentences, in the human's words: what they saw, what they liked, what must change, whether it goes through. `make gate N=<n>` prints the heading to paste and the question that gate asks; the human runs it and writes underneath. At G4 the read-aloud is not decoration: it is the one test in this design that catches prose which scans on the page and collapses in the mouth, and it is the backstop for everything the checks cannot prove.

---

## 9. Stop conditions, declared before the run

- **Success.** No MAJOR open from any critic on one draft; the comparison bar in §7.1 met on that draft; `run_all_checks.py --milestone 4 --complete` passes; the human signs G4.
- **Diminishing returns.** Two consecutive revision rounds in which no finding is accepted, or in which the comparison result does not move.
- **Budget.** Twelve revision rounds in M3, or the token cap in `STATE.md`. On reaching it: stop, hand over the best draft by comparison record, and say what is unfinished.
- **Spinning.** The same largest gap survives two rounds under the same approach; a changed approach goes in `LEDGER.md` before a third, or the piece escalates to the human.
- **Regression.** Three reverted revisions in a row: stop and escalate; the story is being sanded.
- **Too thin a bar.** Fewer than three exemplars can be supplied as text: say so at intake, before M1, and ask the human either to find three (a library, a copy they own, a public-domain story) or to accept in a decision row that the comparisons will be weaker and the gate condition lowered to the number they can supply. Never lower it silently; a bar nobody can read is not a bar.
- **Infeasibility.** The premise cannot be made to work at this length: report it with the evidence and the options, and offer the runner-up premise. Never quietly lower the bar.

**Severity, declared before the run.** **MAJOR**: a good reader would stop reading, misread the story, or feel the ending was unearned; or the premise or its execution is close enough to a named published story that a reader would call it derivative; or the conceit contradicts itself in a way that breaks the spell. **MINOR**: a passage that works but sits below the story's own best level; a line that stumbles; a beat that is doing too little. **NIT**: word choice, punctuation, taste. A critic that cannot say what a reader loses is reporting a MINOR.

---

## 10. Caps

| Cap | Value | Kind |
|---|---|---|
| Premise-writer calls | 7 | one per cell, and one spare for the regeneration G1 offers |
| Premises generated | 28 | twenty-four, and one regenerated cell |
| Probe passages | 6 | M1 |
| Premise-judge calls | 12 | M1: two judges over four batches of cards is eight, and two more over the six probes is ten; the rest is headroom |
| Revision rounds | 12 | M3 |
| Comparison verdicts per round | 20 | every verdict a round spends: 4 calibration, 8 exemplar, 4 revision — 8 once the revision round also pairs against the draft the human signed at G3 |
| Rounds one finding may survive before it goes to the human | 3 | the spinning rule: the approach changes before the third |
| Tokens, whole project | 8M | the human's allowance |
| Fresh-reader calls | 5 | M3 and M4 |

Agents may lower a cap and never raise it. A raise is the human's decision row. A row spent to its value is a stop rather than a failure: `check_state.py` notes it, and the next draw on that row fails.

---

## 11. Failure modes and what catches each

1. **Premises all from one corner of the space** → the partition table, written before generation.
2. **A premise that is a known story in a hat** → the originality critic reads all cards before the probes are written.
3. **A card that reads better than it writes** → the probe passage, before judging.
4. **The judges agreeing because they are the same judge** → two judges, fresh contexts, shuffled batches, scores shrunk toward the median.
5. **The ending chosen because it is neat** → the spine gate; the depth critic's standing question; MAJOR by the severity rule.
6. **The story workshopped flat** → the revision round's `baseline_signed` block, which pairs the current draft against the last draft a person read and signed rather than against its immediate predecessor; the revert rule; the revision-round cap. The N-against-N−1 pairing catches a revision that went backwards and cannot catch this one, because every individual round is an improvement.
7. **The critics drifting to a house style** → the exemplar set is the bar; judges are fresh each round; models rotate where the harness allows.
8. **A soft judge that approves anything** → calibration against a planted defect, every round, enforced by a check.
9. **A comparison won by position bias** → both orders, every pair; disagreement recorded as a tie.
10. **The conceit contradicting itself** → the bible and `check_continuity.py`.
11. **Prose optimized for a tic count** → the tic check reports and does not gate, except at the extremes.
12. **Reproducing an exemplar's sentences** → the forbidden list; the originality critic; the one-sentence quoting limit.
13. **A claim in these documents that nothing performs** → `check_claims.py`.
14. **A revision round that loses the story's one distinctive thing** → the adversarial critic's standing question, "what is the one thing only this story does?", asked every round; the revision record's *lost* answer, which is question 6 of the craft critic's brief and is required in both the N−1 pairing and the `baseline_signed` one; the revert rule and its counter.
15. **A judge with pure position bias** (choosing whichever text is shown first) → both orders on every pair, a disagreement recorded as a tie rather than a win, and a round refused when more than a third of its pairs are ties.
16. **A calibration that never happened** → the record names the pair file and its hash, the check re-hashes it, an empty verdict list is not a pass, and a judge that voted and was never calibrated fails the round.
17. **A MAJOR closed by the orchestrator rejecting it** → a rejected MAJOR names the review or the human decision that agreed, the adversarial critic re-reads its own rejected findings every round, and every rejected MAJOR is listed for the human at the next gate.
18. **The funnel selecting the safe card** → the shrunk ranking is kept beside a highest-single-score ranking, and one probe slot and one finalist slot are reserved for the card the judges disagree about.
19. **A character's name read as a tic, or an ordinary word read as a drifted name** → names and invented terms are never counted as repeats, and a near-miss is only ever a capitalised word against a capitalised term, or a non-common word against a lower-case one.

---

## 12. What this design cannot do

- It cannot prove originality. It can name the closest published work its critics know, and search where the harness allows, and say what it did not look at. A story can resemble something none of the critics has read.
- It cannot verify that an exemplar comparison made from memory is faithful to the exemplar. That is why the full-text count is a gate condition and the memory flag is recorded.
- It cannot make a judge have taste. Calibration catches a judge that approves a planted defect; it does not catch a judge whose preferences are merely ordinary.
- It cannot tell whether the human will love the story. That is what the gates are for, and the read-aloud at G4 is the last of them.
