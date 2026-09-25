---
name: m0-intake
description: Runs milestone M0 — one sitting with the human that turns "write a good science-fiction story" into a taste brief, an exemplar set that is the bar, a weighted rubric, and accepted caps. Use at the very start, or whenever BRIEF.md has a blank answer.
---

# M0 — Intake

1. **Ask for the working title and folder name first**, write the title into `READ_ME_FIRST.md`'s
   Project line, then ask, in one message, every blank row of `BRIEF.md` with its default beside it, so
   that "the defaults are fine" is a complete answer. Ask for the human's name for sign-offs.
2. **The exemplar set.** Ask for ten to fifteen published short stories, and for each one whether they
   can supply the text. Put supplied texts in `design/exemplars/` under `<slug>.txt`, and record every
   entry in `design/EXEMPLARS.md` with `Text supplied: yes|no`. If the human offers fewer than eight, say what that costs: a thin bar makes every later comparison weaker. If fewer than three texts can be supplied, stop and put it to the human before M1: either they find three, or they accept in a decision row that the gate condition drops to the number they have and the comparisons rest more on the judges' memory. Never lower it yourself. Never add a story to the set yourself; you may *propose* candidates in `INBOX.md` for
   the human to accept or reject, marked as proposals.
3. **The rubric.** Walk the eight dimensions in `design/RUBRIC.md` and ask the human to weight each 1 to
   3. Their weights, in their words, become a `DECISIONS.md` row of type taste.
4. **Routing rows** (author agent): how this harness spawns a fresh-context agent; where you read your
   own token use; whether the originality critic has web search, and if not, a row saying its verdict
   rests on knowledge alone.
5. **Caps.** Read the table in `STATE.md` aloud to the human, with the token cap converted to their
   plan's money figure if they know it. Accept or change each. Then `python3 checks/check_state.py
   --accept-caps INTAKE`, which snapshots the table to `checks/caps.approved.json`.
6. **Stage everything except `BRIEF.md` by name.** The human commits `BRIEF.md` and the accepted caps
   themselves: run `make intake`, which prints the two commands, and wait. Never run them yourself.
7. Then `python3 checks/run_all_checks.py --milestone 0 --complete`, print it in full, and run the gate
   skill for G0.

**Where this fails.** Accepting a one-flavour exemplar set (all New Wave, all hard sf), which produces a
pastiche; asking the taste questions as a list the human skims rather than a conversation; writing an
answer on the human's behalf because they were vague — a vague answer recorded as vague is worth more
than a precise one you invented.
