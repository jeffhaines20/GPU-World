# The handoff prompt

Paste this to the agent that will run the loop, in a folder holding a copy of `kit/` and `LOOP_DESIGN.md`.
The only thing you have to change is `<8M>` near the end. Everything else can stand as written; the **Filling it in** table below says what that number is and what to put there.

---

> **Objective.** Write one science-fiction short story of 1,000 to 5,000 words, good enough to sit beside
> the published stories I will name at intake. Everything you need is in this folder: read
> `LOOP_DESIGN.md` once, then `kit/CLAUDE.md`, then work from the skills in `kit/.claude/skills/`. You are
> the orchestrator: you write nothing yourself and grade nothing you wrote.
>
> **Before you start anything.** From inside `kit/`, run `python3 checks/run_all_checks.py` and then
> `python3 checks/plant_faults.py`. The first must print ALL CHECKS PASSED and the second must catch every
> planted fault and pass every control. If either does not, stop and tell me; a kit whose own checks are
> broken cannot judge a story: diagnose it and fix it before intake, and say what was wrong.
> Then do a dry run, in a **scratch copy of the kit outside this
> folder** so that nothing you write there lands in the project's own drafts, reviews, or records: take
> one throwaway premise of your own, write four hundred words, and walk them through one comparison round
> end to end — `make calibrate`, two judges, both orders, the record in the shape
> `reviews/comparisons/RECORD_SHAPE.md` gives, one critic report, one disposition. Then delete the scratch
> copy and tell me what the dry run taught you. The point is that the machinery has been exercised once
> before it matters; the four hundred words are not the story and never enter the project.
>
> **Then intake.** Run the `m0-intake` skill. Ask me everything in `kit/BRIEF.md` in one message with the
> defaults beside each question, so that "the defaults are fine" answers everything except the two questions
> that are my taste and nothing else: the stories I love, and the exemplar set. Those have no defaults
> because only I can answer them. Ask me for the exemplar set — ten to fifteen published short stories — and
> for each one whether I can supply the text, telling me to aim for at least four as text and that three is
> the floor. Do not add stories to that set yourself; propose them and let me accept or reject.
>
> **Then the funnel, then the story.** `m1-premise-funnel` (twenty-four premises in isolation, six
> probed, three offered to me), `m2-spine`, `m3-draft-revise`, `m4-final`. Stop at every gate and wait.
> Never write my sign-off, never pick the premise, never answer a brief question on my behalf.
>
> **Severity.** MAJOR: a good reader would stop reading, misread the story, or feel the ending was
> unearned; or the premise or its execution is close enough to a named published story that a reader
> would call it derivative; or the conceit contradicts itself in a way that breaks the spell. MINOR: a
> passage below the story's own best level. NIT: word choice. A critic that cannot say what a reader
> loses is reporting a MINOR.
>
> **Stop.** Stop when no MAJOR is open, the comparison bar in `LOOP_DESIGN.md` §7.1 is met on one draft,
> and I have signed G4. Also stop and tell me if: two revision rounds pass with no finding accepted; three
> revisions in a row are reverted; the same largest gap survives two rounds under one approach; you reach
> twelve revision rounds or <8M> tokens. On any of these, hand me the best draft by the comparison record
> and say what is unfinished. Never lower the bar quietly; an unreachable bar is a result, reported with
> the evidence.
>
> **Report to me after every critic round, three lines**: findings by severity per critic; whether the new
> findings are in text the last revision changed; the comparison result and how it moved. Put them in
> `kit/INBOX.md` under "Since you last looked" and say them in chat.
>
> **Keep a resumable state.** If you are interrupted, I want to be able to say "continue" and lose
> minutes, not a round.
>
> **Two things I care about more than speed.** First, I would rather have a strange story with a flaw
> than a smooth one with nothing in it: if a revision would make the story safer, say so and ask.
> Second, when a document in the kit promises something no check or agent actually does, tell me — I
> would rather narrow the promise than build more machinery.

---

## If the day-one checks fail

You are not expected to understand the failure. Tell the agent to diagnose and fix it before intake, and
do not let it start the story on a kit whose own checks fail — a kit that cannot catch its own planted
faults cannot judge a story. You are allowed to insist on that, and it is the right call.

## Filling it in

| Bracket | What to put there |
|---|---|
| `<8M>` | The token budget for the whole project. A token is about three quarters of a word of everything the agents read and write. 8M is the kit's default and covers a full run — the funnel, a first draft, and twelve revision rounds with their critics — with room to spare. This loop never spends money itself; whether the run costs you anything is between you and whoever provides the agents. Leave it at 8M unless you have a reason. |

You will also need, at intake: your ten to fifteen exemplar stories and which of them you can supply as
text (aim for at least four, three is the floor), three to five stories you love with one sentence each
on why, and two or three things you never want to read. Assembling that list is an evening's work and is
worth doing before you paste this.
