# Inbox

What is waiting on you, and what has happened since you last looked. The orchestrator writes the three
sections it owns; **"From you" is yours**, and no agent ever edits or deletes anything in it — the same
rule that protects your gate sign-offs. Answer here or in chat, whichever you prefer.

## From you

_(anything you want to say, at any time. "This is boring in the middle" is a usable finding; you are never
expected to say why, or to suggest a fix. The orchestrator reads this section every turn and answers under
"Since you last looked", leaving what you wrote where it is.)_

## Waiting on you

**Intake (G0), about forty minutes.** The full set of questions, each with its default beside it, is in the
chat message of 2026-09-08 headed "Intake". "The defaults are fine" answers everything except two questions
that are your taste and have no default: the three to five stories you love, and the exemplar set (ten to
fifteen published short stories, with, for each, whether you can supply the text — aim for at least four,
three is the floor). Twelve exemplars are *proposed* there for you to accept or reject; none is added
unless you say so. One more decision is yours before anything runs: the token cap. You named 2M in the
handoff; the dry run measured what a round costs in this harness, and the chat message gives the
arithmetic and three options. Answer in chat; your words are copied in verbatim and marked as having come
that way.

## Since you last looked

- **Day-one checks.** `run_all_checks.py` failed on the pristine kit: `check_claims.py` refused four documents
  for naming `story/drafts/`, a folder the first draft creates and git does not keep while empty. The fault
  suite had not seen it because its fixture writes drafts into that folder first. Fixed by listing the folder
  as created at runtime and adding a control that runs the claims check on a kit with no drafts folder. Suite:
  74 faults caught, 16 controls pass. Committed.
- **Dry run** in a scratch copy, since deleted: a 450-word throwaway by a story-writer, `make calibrate`, two
  judges in both orders on the calibration pair (both caught it) and on one exemplar pair (Wells, "The Star",
  public domain; the throwaway won on "ending" both orders, both judges), the record in the RECORD_SHAPE
  contract (passed at round strictness, failed at gate strictness on exactly the two rules a one-pair round
  cannot meet), one depth-critic report (1 MAJOR, 4 MINOR, 2 NIT), a revision, and a disposition the check
  accepted. Lessons are in `../orchestrator/RUNBOOK.md`; the one that matters for you is cost: every agent
  costs about 19–29K tokens before it reads a word, so a revision round with two judges is 1.1–1.7M tokens,
  and 1.35M has already been spent. The 2M you named will not reach a story.

## The request log

_(every request made of the human, kept after it is answered)_

| Date | Request | Answered |
|---|---|---|
| 2026-09-08 | Intake: the BRIEF.md questions with defaults, the exemplar set (12 proposed), the token cap | |
