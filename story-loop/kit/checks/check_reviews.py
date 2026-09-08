#!/usr/bin/env python3
"""Every review with findings has a disposition that names each finding exactly once, and every FIXED row
names a draft that exists. A finding is a line under the review's '## Findings' heading that starts with
F<number>; a numbered finding outside that heading fails, because the count is taken there.
Bypass attempts this check refuses: a review with findings and no disposition; a disposition with a row
for a finding the review does not have, or two rows for one finding, or a blank Finding cell; a FIXED row
naming a draft that was never written; a finding written below the Findings section where the count
cannot see it; a finding with no severity; a MAJOR rejected on the orchestrator's own say-so rather than
by naming the review or the human decision that agreed; and, at a gate, a MAJOR left deferred.
What it does not check: whether the fix was any good. That is the next round's critics, and the
adversarial critic opens every FIXED row of its own last report.
Usage: check_reviews.py [--gate N]"""
import re
import sys
from pathlib import Path
from common import ROOT, Report, cell, drafts, read_text, register_rows


def disp_name(_disp, review):
    return review.stem + "-disposition.md"

FINDING = re.compile(r"^\s*(?:[-*]\s*)?(?:\d+[.)]\s*)?(?:[-*]\s*)?(?:#+\s*)?\**F(\d+)\**[:.)\s]", re.M)


def findings_section(text):
    """The text under the one '## Findings' heading, code fences stripped, up to the next heading of the
    same level. A second Findings heading is a failure the caller reports."""
    stripped = re.sub(r"```.*?```", "", text, flags=re.S)
    parts = re.split(r"^##\s+Findings\s*$", stripped, flags=re.M | re.I)
    if len(parts) < 2:
        return ""
    return re.split(r"^##\s+(?!Findings)", parts[1], flags=re.M)[0]


def human_decisions(root):
    """The IDs of decision rows the human wrote: the only rows that can overrule a critic's MAJOR."""
    rows, problems = register_rows(Path(root) / "DECISIONS.md", "ID", others=("Author",))
    return set() if problems else {cell(r, "ID") for r in rows if cell(r, "Author").lower() == "human"}


def severities(section, numbers):
    """{finding number: severity} read from the finding's own text, which every critic brief requires."""
    marks, out = list(FINDING.finditer(section)), {}
    for i, m in enumerate(marks):
        text = section[m.start():marks[i + 1].start() if i + 1 < len(marks) else len(section)]
        sev = re.search(r"\b(MAJOR|MINOR|NIT)\b", text)
        out[int(m.group(1))] = sev.group(1) if sev else None
    return out


def main(root=ROOT, gate=None):
    rep = Report("reviews")
    rdir = Path(root) / "reviews"
    draft_names = {p.stem for _, p in drafts(root)}
    for review in sorted(rdir.glob("REV-*.md")):
        if review.name.endswith("-disposition.md"):
            continue
        text = read_text(review)
        if len(re.findall(r"^##\s+Findings\s*$", re.sub(r"```.*?```", "", text, flags=re.S), re.M | re.I)) > 1:
            rep.fail(f"{review.name}: two '## Findings' headings; the count is taken under one")
            continue
        section = findings_section(text)
        numbers = {int(n) for n in FINDING.findall(section)}
        sev = severities(section, numbers)
        outside = {int(n) for n in FINDING.findall(re.sub(r"```.*?```", "", text, flags=re.S))} - numbers
        if outside:
            rep.fail(f"{review.name}: finding(s) F{', F'.join(str(n) for n in sorted(outside))} outside the "
                     f"'## Findings' heading; every finding goes under it, and a reconfirmed earlier finding "
                     f"is written as that review's ID and number (REV-04 F2)")
        if not numbers:
            continue
        disp = review.with_name(review.stem + "-disposition.md")
        if not disp.exists():
            rep.fail(f"{review.name}: {len(numbers)} finding(s) and no {disp.name}")
            continue
        rows, problems = register_rows(disp, "Finding")
        for pr in problems:
            rep.fail(pr)
        for r in rows:
            if not cell(r, "Finding"):
                rep.fail(f"{disp.name} line {r['_line']}: a disposition row with a blank Finding cell; "
                         f"a row the register holds is never skipped")
        labels = [cell(r, "Finding").upper().replace(" ", "") for r in rows if cell(r, "Finding")]
        wanted = {f"F{n}" for n in numbers}
        missing, extra = sorted(wanted - set(labels)), sorted(set(labels) - wanted)
        dup = sorted({l for l in labels if labels.count(l) > 1})
        if missing or extra or dup:
            rep.fail(f"{disp.name}: the rows do not name the findings one each"
                     + (f"; no row for {', '.join(missing)}" if missing else "")
                     + (f"; rows for {', '.join(extra)}, which {review.name} does not have" if extra else "")
                     + (f"; {', '.join(dup)} named twice" if dup else ""))
        for r in rows:
            label = cell(r, "Finding").upper().replace(" ", "")
            n = int(label[1:]) if re.fullmatch(r"F\d+", label) else None
            this = sev.get(n)
            if this is None and n in numbers:
                rep.fail(f"{review.name} F{n}: no severity; every finding carries MAJOR, MINOR, or NIT, "
                         f"because the stop conditions are written in those words")
            verdict = cell(r, "Disposition").upper()
            if verdict not in ("FIXED", "REJECTED", "DEFERRED"):
                rep.fail(f"{disp.name} line {r['_line']}: the Disposition cell reads "
                         f"{cell(r, 'Disposition')!r}; it is exactly FIXED, REJECTED, or DEFERRED, because "
                         f"the severity rules read this cell and anything else slips past all three")
                continue
            if this == "MAJOR" and verdict == "REJECTED":
                # Requiring only that a citation resolve let any sibling report close any MAJOR: in a real
                # round three to five exist, all commissioned by the orchestrator, and none of them has to
                # have said anything about this finding. The human is the only reader who can overrule a
                # critic's MAJOR, so their row is what it takes.
                cited = re.findall(r"\b(DEC-\d+)\b", cell(r, "Detail"))
                real = [c for c in cited if c in human_decisions(root)]
                if not real:
                    rep.fail(f"{disp.name} line {r['_line']}: a MAJOR rejected without the human's say-so. "
                             f"A MAJOR is closed as REJECTED only under a decision row the human wrote "
                             f"(`make decide TYPE=taste` prints one) and that this row names by ID. Another "
                             f"critic's report does not close it: every review in a round was commissioned "
                             f"by you, and a sibling that happens to exist has not agreed to anything. Fix "
                             f"it, or put it to the human. "
                             f"{'Cited: ' + ', '.join(cited) if cited else 'Nothing cited.'}")
            # G3 is the human's first reading, not an approval: it is called after round 1, when open
            # MAJORs are the expected state, and the design says plainly that nothing goes through there.
            # The no-MAJOR condition is the success stop, so this rule belongs to G4.
            if gate is not None and gate >= 4 and this == "MAJOR" and verdict == "DEFERRED":
                rep.fail(f"{disp.name} line {r['_line']}: a MAJOR deferred at G{gate}; the stop conditions "
                         f"say no MAJOR is open when the story goes through, and G4 is where it does")
            if verdict != "FIXED":
                continue
            detail = cell(r, "Detail")
            named = re.findall(r"draft-\d+", detail)
            # Before M3 there are no drafts, and a review of the premises or the spine is fixed by
            # changing the premise card or the spine. Requiring a draft name there made every M1 and M2
            # review impossible to close by any of the three dispositions.
            artefact = re.search(r"\b(SPINE\.md|PREMISES\.md|BIBLE\.md|P-\d+)\b", detail)
            if not named and not (not draft_names and artefact):
                rep.fail(f"{disp.name} line {r['_line']}: FIXED naming nothing that changed. A FIXED row "
                         f"names the draft that fixed it (`draft-06`); before the first draft exists it "
                         f"names the artefact instead — `SPINE.md`, `PREMISES.md`, or the card by ID "
                         f"(`P-14`) — because at M1 and M2 that is what a fix changes")
            for d in named:
                if d not in draft_names:
                    rep.fail(f"{disp.name} line {r['_line']}: FIXED names {d}, which is not in story/drafts/")
    rep.note(f"{len(list(rdir.glob('REV-*.md')))} file(s) in reviews/")
    return rep.finish()


if __name__ == "__main__":
    g = int(sys.argv[sys.argv.index("--gate") + 1]) if "--gate" in sys.argv else None
    sys.exit(main(gate=g))
