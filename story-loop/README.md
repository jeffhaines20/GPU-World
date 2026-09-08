# The Story Loop

A loop for AI agents to write one science-fiction short story of 1,000 to 5,000 words, good enough to sit
beside the short fiction its owner admires. Built from the loop-engineering material at the root of this
repository and from the postmortem of the first loop built with it.

## What is here

- **`LOOP_DESIGN.md`** — the design: the bar, the five milestones, the critics, the three evaluators that
  carry the weight, the stop conditions, and what the design cannot do. This is the engineering
  specification and it is long; if you are the human in the loop rather than the person maintaining the
  loop, read `kit/READ_ME_FIRST.md` instead, and the four sections of this one named in step 1 below.
- **`HANDOFF_PROMPT.md`** — the message to paste to the agent that will run the loop, with the numbers
  filled in.
- **`kit/`** — everything the agents run from: the orchestrator's rules, twelve agent briefs and seven
  skills (in `kit/claude/`, deliberately with no leading dot, so that no file manager hides them and no
  upload drops them), ten checks with a suite of seventy-four planted faults and fifteen positive
  controls, and the templates the loop fills in.

## How to use it

All three steps below are yours to start; step 2 is the one where you hand over and the agents take it.

1. **Homework, before anything starts.** Two pieces, and the second is the real one.
   - Read `LOOP_DESIGN.md` sections 1 (the bar), 2 (the shape), 8 (your part), and 9 (when it stops).
     About fifteen minutes.
   - Choose ten to fifteen published short stories that stand for the quality you want, and find out
     which of them you have as plain text. **Budget an evening**: this is the bar the whole loop measures
     against, and hunting down which stories you actually own is slower than picking them. Aim to have at
     least four as text. Bring the list to intake — you will be asked to type it there, not to invent it
     there.

   Neither piece is part of the time in step 3; that is the sittings only.
2. **Handing over.** Copy `kit/` **and `LOOP_DESIGN.md`** into a folder for the story — the agent reads
   the design from beside the kit, and copying the kit alone makes its first instruction fail. Paste
   `HANDOFF_PROMPT.md` to the agent and let it run the day-one checks
   (`python3 checks/run_all_checks.py`, then `python3 checks/plant_faults.py`). If either fails, the
   agent should diagnose and fix it before intake: a kit whose own checks are broken cannot judge a
   story, and you are allowed to insist on that.
3. **Yours, five sittings, two to two and a half hours in all.** Intake (40 min); pick the premise from
   three (20); read the spine (10); read the first full draft once without notes (15–25); read the
   finished story aloud (30–40). The last two vary with how long the story ran. That total assumes you
   say yes at every gate — each send-back adds a sitting, and `kit/READ_ME_FIRST.md` says what each one
   costs before you decide. `kit/READ_ME_FIRST.md` is the document written for you and repeats all of this.

## What the design leans on

Three things do most of the work, and each is the answer to a way a writing loop usually fails.

- **A bar made of real stories, not a score.** The story is judged by blind comparison against the
  exemplars the owner named, one craft dimension at a time, in both orders, by judges that do not know
  which text is the loop's. A score would be optimized; ten stories cannot be.
- **Judges calibrated against a planted defect, every round.** Before any comparison counts, the round's
  judges are shown the draft against a mechanically weakened copy of itself. A judge that cannot tell
  them apart does not vote that round. This is the only thing that makes a soft verdict admissible.
- **A revision that loses more than it gains is reverted.** Every draft is kept, and each new one is
  compared against the one before it with the question "what did this lose?". Most revision loops end
  with a story that is more correct and less alive; this one can see that happening.

## Review status

Version 0.4. **Not yet signed off; not yet run on a real story.**

Round 1 (three critics on v0.1): the adversarial critic found 14 MAJOR, 3 MINOR and 1 NIT (`REV-01.md`:
the comparison record and its calibration were keys an agent typed, with nothing bound to them; ties
counted as wins; a gate could be met on one exemplar; the revert rule had no record, no check and no
reader; a character's name read as a tic and an ordinary word as a drifted name), the cold human read
said it could run the loop with 6 MINOR and 1 NIT (`REV-02.md`), and the cold orchestrator check found
6 MAJOR and 5 others (`REV-03.md`: the bare day-one command failed on a pristine kit; the one file
format every round depends on was taught nowhere). All 36 dispositioned in `reviews/`, all FIXED in
v0.2, which added 13 planted faults and 3 positive controls — 55 faults and 11 controls in all.

Round 2 (the same three on v0.2): the adversarial critic found 8 MAJOR, 5 MINOR and 1 NIT (`REV-04.md`:
every round-1 fix had a hole reachable by good-faith input — a plural read as a drifted name, a declared
motif blinding the repeat check to the next word, numbered rounds turning into best-of-N, one gate-amend
row unlocking a sign-off forever, a MAJOR rejected by citing its own review, and the draft-against-draft
round exempt from calibration and every floor). The cold orchestrator check found 8 MAJOR and 5 MINOR
(`REV-05.md`: closing a review before revising made a FIXED disposition unreachable by construction; a
missing `from_memory` field counted as supplied text; two round-1 findings whose dispositions claimed more
than they fixed). The cold human read found 5 MINOR and 1 NIT (`REV-06.md`) and said it could run the loop.
All 33 dispositioned, all FIXED in v0.3, which added 13 faults and 4 controls — **68 faults and 15
controls in all**.

The two round-1 findings that came back are the reason the round-2 dispositions were re-verified against
the tree one at a time rather than trusted: three more rows turned out to describe fixes in wording the
code did not use, and were corrected before this version was cut.

Round 3 (the same three on v0.3): the adversarial critic found 13 MAJOR, 6 MINOR and 2 NIT (`REV-07.md`),
the cold orchestrator check 7 MAJOR, 5 MINOR and 3 NIT (`REV-08.md`), and the cold human read 1 MAJOR,
14 MINOR and 5 NIT (`REV-09.md`, verdict "I could run this"). All 51 dispositioned, all FIXED in v0.4,
which added 6 faults — **74 faults and 15 controls**.

**The round-3 finding that matters most is about the process, not the kit.** The adversarial critic
counted its own thirteen: nine were *the cost of a round-2 fix*, two were findings dispositioned FIXED
whose fix was never built, one was a partial fix with its hole still open, and one was fresh ground. The
cold orchestrator check found the same independently — three of its seven were earlier findings returning
through their own fixes, including the day-one command failing in a deployment folder because the round-2
fix repaired it only in the repository where the design is written. Each round's repairs are the next
round's defects. MAJOR counts across the three rounds went 20, 16, 21: this review is not converging, and
the reason is visible in the numbers rather than hidden behind them.

**Stopping rule, declared before the first review:** the design closes when all three reviewers report
nothing above MINOR on one version. MAJOR means a mechanism fails on good-faith input, lets a defect
ship silently, or is a promise these documents make that nothing performs; MINOR means a reader could
proceed but had to guess; NIT is wording. Budget: three rounds.
