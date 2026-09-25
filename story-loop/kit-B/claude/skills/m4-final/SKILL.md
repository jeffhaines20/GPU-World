---
name: m4-final
description: Runs milestone M4 — the line edit, the title, the read-aloud pass, the final comparison round, and the finished file. Use once the M3 stop conditions have fired.
---

# M4 — Final

1. **Line edit.** Spawn `line-editor` with the final draft and the flow critic's marks. It changes
   sentences, never structure, and reports every change with its reason. Changes nobody can justify are
   reverted.
2. **Title.** Three candidates with one line each on what each promises the reader. The human picks;
   `make decide TYPE=title`. Never title it yourself.
3. **The read-aloud pass.** Spawn `flow-critic` on the line-edited draft with the instruction to read
   sentence by sentence and mark every place a reader's mouth would stumble. Fix those; nothing else.
4. **The last judgments on the text the human signs.** Spawn `fresh-reader` on the line-edited draft —
   its question, "one thing you will remember tomorrow, and if there is nothing that is a MAJOR", is the
   question closest to the objective and must be asked of the final text, not of a draft four revisions
   back. Spawn `adversarial-critic` for its last round, and `originality-critic` if the story has changed
   materially since its last pass. Disposition all three before the gate. Then **the final comparison
   round**, the full mechanism: calibration, four exemplars, both orders, at least three pairs on supplied text,
   and the revision round against the previous draft. The bar in `LOOP_DESIGN.md` §7.1 must be met on
   this draft.
5. **Write `story/STORY.md`**: the title, the story, and at the end a short colophon — word count, the
   exemplar set it was measured against, the comparison record, and the count of full-text versus
   from-memory comparisons. The colophon is for the human, not for a reader of the story.
6. **G4.** Write the `INBOX.md` request: read it aloud, all of it, and sign. Say that reading aloud is
   the test, not a formality. Stop. After the human signs, `python3 checks/run_all_checks.py --milestone
   4 --complete --gate 4` must pass, and the loop is done.

**Where this fails.** A line edit that raises the register until the story sounds like everything else;
titling it for the agents rather than the reader; skipping the final comparison because the story "has
not changed much".
