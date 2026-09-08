# Inbox

What is waiting on you, and what has happened since you last looked. The orchestrator writes the three
sections it owns; **"From you" is yours**, and no agent ever edits or deletes anything in it — the same
rule that protects your gate sign-offs. Answer here or in chat, whichever you prefer.

## From you

_(anything you want to say, at any time. "This is boring in the middle" is a usable finding; you are never
expected to say why, or to suggest a fix. The orchestrator reads this section every turn and answers under
"Since you last looked", leaving what you wrote where it is.)_

## Waiting on you

**Gate G0, about ten minutes.** Intake is recorded. Read these back and correct anything that is not what you
said: `BRIEF.md` (your answers, verbatim where they were yours, marked "the default" where you took it),
`design/EXEMPLARS.md` (the set that resulted: nine texts fetched, all obtainable online), `DECISIONS.md` rows
DEC-006 to DEC-010 (your words) and DEC-001 to DEC-005 (how this harness runs the loop), and the caps table in
`STATE.md` (tokens 10M, revision rounds 3, the rest as the kit ships them).

Two one-word questions first, because only you can answer them:

1. **Omelas.** You named it as loved and it was on the proposed list, but no text is obtainable. Keep it in the set
   judged from the judges' memory, which the design counts as weaker evidence, or drop it? *keep* or *drop*.
2. **The Yellow Wallpaper.** You named it as loved. It is public domain and fetched, but it was not on the list you
   accepted, so it is not in the set until you say so. It is not science fiction. *add* or *leave out*.

Then the sign-off. Write three to five sentences in your own words: what you saw, what you liked, what must change,
whether it goes through. Say them in chat; they are pasted under a heading `### G0 — 2026-09-08 (dictated in chat)`
in `DECISIONS.md` without a word changed, and no agent ever edits them afterwards.

**Findings we decided not to act on:** none; no critic has run yet.

**A deviation to know about.** The kit has you commit the brief and the caps yourself (`make intake`). You have no
shell here, so the orchestrator committed them at your standing instruction to commit and push, in the commit named
"Intake". DEC-005 records this.

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
| 2026-09-08 | Intake: the BRIEF.md questions with defaults, the exemplar set (12 proposed), the token cap | 2026-09-08, in chat: defaults, Jeff, three loved stories, use every text obtainable online, cap raised to 10M |
| 2026-09-08 | G0: Omelas keep or drop; Yellow Wallpaper add or leave out; the sign-off paragraph | |
