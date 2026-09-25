---
name: close-review
description: Closes a review round — one disposition row per finding, FIXED with the draft that fixed it, REJECTED with the reason, DEFERRED with the trigger; then runs the check. Use after every review and after that round's revision has been written, and always before the next review is commissioned.
---

# Closing a review

**When.** After the round's revision exists, not before. A FIXED row names the draft that fixed the
finding, so closing a review before that draft is written leaves REJECTED and DEFERRED as the only rows
you can honestly put — and the register whose job is to record what got better records nothing. In M3
that is step 5 of `m3-draft-revise`, after step 4 has produced the new draft.

For each review file from the round:

1. Read every finding. A finding is a numbered item under the review's `## Findings` heading.
2. Write `reviews/<REV-NN>-disposition.md` from `reviews/disposition_template.md`: one row per finding,
   each named exactly once, no extra rows and no blank rows.
   - **FIXED** names the draft number that fixed it (`draft-06`), and says in a few words what changed.
     A FIXED row that names no draft is not a disposition. **At M1 and M2 there are no drafts**, and a
     finding about a premise or a spine is fixed by changing the premise or the spine — so before the
     first draft exists a FIXED row names the artefact instead: `SPINE.md`, `PREMISES.md`, or the card
     by ID (`P-14`).
   - **REJECTED** gives the reason in the review's own terms. "The flatness is the point of the scene"
     is a reason; "disagree" is not. A **MAJOR** may only be rejected under a decision row the human
     wrote, named by ID (`DEC-012`): they are the only reader who can overrule a critic's MAJOR. Another
     critic's report does not close one — every review in the round was commissioned by you, and a
     sibling that happens to exist has not agreed to anything. If you think a MAJOR is wrong, put it to
     the human in `INBOX.md` and let them write the row; otherwise fix it.
   - **DEFERRED** names the trigger that reopens it and who owns it.
3. Run `python3 checks/check_reviews.py`. It fails on: a review with findings and no disposition; a
   disposition that does not name every finding once; a blank Finding cell; a Disposition cell that is not
   exactly FIXED, REJECTED, or DEFERRED (no "Deferred to M4", no "Fixed in draft-06"); a FIXED row naming
   no draft or a draft that does not exist; a finding with no severity in its own text; a MAJOR rejected
   without naming a decision row the human wrote; and, at G4, a MAJOR left DEFERRED. (Not at G3: that
   gate is the human's first reading, not an approval, and open MAJORs are the expected state there.)
4. Add the `LEDGER.md` row for the round.

Never close a review by rewriting the review. Never disposition a finding as FIXED before the draft that
fixes it exists — which is why this skill runs after the revision and not before it.
