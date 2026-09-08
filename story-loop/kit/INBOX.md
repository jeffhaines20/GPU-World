# Inbox

What is waiting on you, and what has happened since you last looked. The orchestrator writes the three
sections it owns; **"From you" is yours**, and no agent ever edits or deletes anything in it — the same
rule that protects your gate sign-offs. Answer here or in chat, whichever you prefer.

## From you

_(anything you want to say, at any time. "This is boring in the middle" is a usable finding; you are never
expected to say why, or to suggest a fix. The orchestrator reads this section every turn and answers under
"Since you last looked", leaving what you wrote where it is.)_

## Waiting on you

_(nothing: the funnel is running. Next stop is G1, three premises to choose from.)_

## Since you last looked

- **G0 is signed.** Your paragraph of 2026-09-08 is in `DECISIONS.md` under a G0 heading marked as dictated in
  chat, unchanged. I read it as GO (DEC-011); correct me if that is wrong. The milestone line is now M1.

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
| 2026-09-08 | G0: Omelas keep or drop; Yellow Wallpaper add or leave out; the sign-off paragraph | 2026-09-08, in chat: "1. Keep. 2. Add."; the G0 paragraph came in chat the same day and is pasted in DECISIONS.md |
