#!/usr/bin/env python3
"""Tests the checks, not the story. Builds a fixture project in a scratch directory that passes every
check at milestone 4 with gate 4, then plants one known fault at a time and expects the matching check to
fail on each, and runs positive controls that must pass. When every fault is caught and every control
passes it writes checks/faults.lock.json, which carries a hash of every file in checks/ from that run, so
that run_all_checks.py can refuse to report success after a check has been edited without re-running this.
A check nobody has seen fail is not a check.
Usage: plant_faults.py"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import split_front_matter

HERE = Path(__file__).resolve().parent
KIT = HERE.parent
PY = sys.executable
STORY = (HERE / "_fixture_story.txt").read_text(encoding="utf-8")


def run(root, script, *args):
    return subprocess.run([PY, str(Path(root) / "checks" / script), *args], cwd=root,
                          capture_output=True, text=True)


def put(root, rel, text):
    p = Path(root) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def edit(root, rel, old, new, count=1):
    p = Path(root) / rel
    t = p.read_text(encoding="utf-8")
    assert old in t, f"{rel}: anchor not found: {old[:60]!r}"
    p.write_text(t.replace(old, new, count), encoding="utf-8")


def sha256_body(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


DRAFT_1 = "\n\n".join(STORY.strip().split("\n\n")[:-1])
DRAFT_2 = STORY.strip()


def build_fixture(root):
    shutil.copytree(KIT, root, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    for gone in ("checks/faults.lock.json", "checks/caps.approved.json", "checks/gates.seen.json"):
        (Path(root) / gone).unlink(missing_ok=True)
    put(root, "STATE.md", """# State

**Milestone:** M4 — Final · **Updated:** 2026-09-07 · **Current draft:** draft-02

## Caps

| Cap | Value | Used | What kind of number |
|---|---|---|---|
| Premise-writer calls (one per partition cell) | 7 | 6 | budget for M1 |
| Premises generated | 28 | 24 | budget for M1 |
| Probe passages | 6 | 6 | budget for M1 |
| Premise-judge calls | 12 | 10 | budget for M1 |
| Revision rounds in M3 | 12 | 2 | budget for M3 |
| Comparison verdicts per round | 20 | 12 | resets when a round starts; 4 calibration, 8 exemplar, 4 revision |
| Rounds one finding may survive before it goes to the human | 3 | 1 | live count, per finding |
| Fresh-reader calls | 5 | 1 | budget for M3 and M4 |
| Tokens, whole project | 8M | 2M | the human's allowance |

## Process signals

| Signal | Value | Written by |
|---|---|---|
| Reverted revisions in a row | 0 | the m3 skill |
| Rounds since a finding was accepted | 0 | the m3 skill |
| Last comparison result (wins-ties-losses, full-text share) | 4-0-0, 3 of 4 pairs on supplied text | the m3 skill |
| Judges calibrated this round | yes | make calibrate |
""")
    put(root, "DECISIONS.md", """# Decisions

One row per decision. Agents write rows with author `agent`.

| ID | Date | Author | Type | Decision | Why | Alternative not taken |
|---|---|---|---|---|---|---|
| DEC-001 | 2026-09-05 | agent | routing | sub-agent tool, one file per agent | the harness has one | separate sessions |
| DEC-002 | 2026-09-05 | human | taste | weights as in RUBRIC.md | the ending matters most to me | flat weights |
| DEC-003 | 2026-09-05 | human | pick | premise P-11, the listening station | the only one I kept thinking about | P-04, P-19 |
| DEC-004 | 2026-09-06 | agent | other | draft-02 supersedes draft-01 after round 1 | the ending was explained | keep draft-01 |
| DEC-005 | 2026-09-07 | human | title | "A Record of Nothing" | it is the line the story turns on | "Kettle", "The Long Ferry" |
| DEC-006 | 2026-09-07 | human | taste | the measuring in the middle stays | it is what she has instead of company | cut it |

## Gate sign-offs

### G0 - 2026-09-05

I read the brief back and it is what I asked for. The exemplar list is mine and I could supply three of
the texts. I want the quiet kind, not the adventure kind, and the brief says so. It goes through.

### G1 - 2026-09-05

I read the three cards and the three sample passages. The listening station is the one I kept thinking
about an hour later, and the other two I had already forgotten. I would like the ending to stay open.
Go ahead with that one.

### G2 - 2026-09-06

The spine is the story I wanted from the card. The turn is real and I can see what it costs her. I am
slightly worried the middle is only arithmetic, so watch that. It goes through.

### G3 - 2026-09-06

I read it once without stopping. The middle sagged where I thought it would and the last page did not.
The ending explained itself in the last paragraph and I would rather it did not. Send it back for that.

### G4 - 2026-09-07

I read the whole thing aloud and it held. The place where I stumbled before is gone and the ending now
leaves me with the image rather than the explanation. This is what I wanted and it goes through.
""")
    put(root, "LEDGER.md", """# Ledger

| Round | Draft | Largest gap | Approach | Evidence (the review file) |
|---|---|---|---|---|
| 1 | draft-01 | the ending explains itself | cut the last paragraph to its image | reviews/REV-01.md |
| 2 | draft-02 | the middle is arithmetic | give her something to do while she counts | reviews/REV-02.md |
""")
    put(root, "design/EXEMPLARS.md", """# The exemplar set

| # | Title | Author | Year | Text supplied | Why the human named it |
|---|---|---|---|---|---|
| 1 | The Salt Gardeners | A. Fixture | 1974 | yes | the ending lands without explaining |
| 2 | Nine Kinds of Weather | B. Fixture | 1981 | yes | a person, not a lecture |
| 3 | The Cartographer's Wife | C. Fixture | 1996 | yes | the idea is used, not described |
| 4 | Hollow Season | D. Fixture | 2003 | no | I remember the last line |
| 5 | Interior, With Snow | E. Fixture | 2008 | no | quiet and strange |
| 6 | The Second Ocean | F. Fixture | 2011 | no | the turn is real |
| 7 | Wintering | G. Fixture | 2013 | no | I read it twice |
| 8 | The Glass Orchard | H. Fixture | 2015 | no | it earns its idea |
| 9 | Small Hours | I. Fixture | 2017 | no | the sentences |
| 10 | The Long Ferry Home | J. Fixture | 2019 | no | the aftertaste |
""")
    for slug, title in (("salt-gardeners", "The Salt Gardeners"), ("nine-kinds", "Nine Kinds of Weather"),
                        ("cartographers-wife", "The Cartographer's Wife")):
        put(root, f"design/exemplars/{slug}.txt",
            f"{title}\n\nA fixture stands in for the human's own copy of a published story. Nothing in this\n"
            f"file is any real author's work; the real project holds the texts the human supplied, and the\n"
            f"comparison judges read those.\n")
    put(root, "design/PARTITIONS.md", """# The premise space, cut before anything is generated

| Cell | Source of strangeness | Narrowing from the brief | Writer |
|---|---|---|---|
| C1 | a technology and what it costs | quiet register, one hard idea | premise-writer 1 |
| C2 | a biology | quiet register | premise-writer 2 |
| C3 | a cosmology | quiet register | premise-writer 3 |
| C4 | a social arrangement | quiet register | premise-writer 4 |
| C5 | physics or time | quiet register | premise-writer 5 |
| C6 | an alteration of mind | quiet register | premise-writer 6 |
""")
    put(root, "design/PREMISES.md", """# Premise cards

### P-11 - C1 - the listening station
Conceit: a station has been calling into an ocean for eighty-eight years with its transmitter switched off.
Who: the keeper, who took the post for the quiet.
Obstacle: the record says the board was switched off on purpose, and the person who did it is long gone.
Turn: she turns it on, and something answers after a delay too long to be distance.
Last image: the keeper standing in the room, letting the station speak.
Question: what is owed to a thing you have made wait.
Not the obvious version: the obvious version is first contact; this one is about the pause before an answer.
Closest published: a great many first-contact stories; none I know turns on the transmitter being off.
Status: chosen
""")
    spine = """# The spine

**Point of view and tense:** third limited, past, close on the keeper, because the story is the size of
one person's attention.
**Who:** the keeper. She wants a room with one window. She is wrong that she wants nothing to happen.
**Obstacle:** the record is complete and says the silence is correct.
**The turn:** she turns the board on, and after that the silence cannot be read as emptiness again.
**Ending image:** the keeper standing in the middle of the room with her hands at her sides.
**The question:** what is owed to a thing that has been made to wait, and the story does not answer it.
**Length target:** about 1,100 words.

## Beats

1. The hum changes and she writes it down.
2. She goes down the shaft and finds the draw.
3. The log says a keeper switched the board off in the second year.
4. She turns it on and the buffer holds a return.
5. She does the arithmetic and the number is not a distance.

## What this story must not become

A first-contact story with a revelation in the last line, or a story about a machine rather than about
the keeper.
"""
    put(root, "story/SPINE.md", spine)
    put(root, "story/BIBLE.md", """# Story bible

## Names

| Name | What it is | Spelling notes |
|---|---|---|
| Ada | the keeper | never Ada's full name |
| Mir | the person who taught her the discipline | one syllable |
| Kettle | the station | capitalised, no article |
| Oyelaran | the keeper who switched the board off | as spelled here |

## Invented terms

| Term | Meaning | First appears |
|---|---|---|
| lattice | the array sunk through the ice | paragraph 7 |
| hydrophones | the listening elements of the lattice | paragraph 7 |

## Motifs

| Word | Why it repeats |
|---|---|
| nothing | the story turns on a record of nothing being a record |

## Word that is not a drift

| Word that is not a drift | Why both are meant to be there |
|---|---|

## Rules of the conceit

The lattice can transmit and receive. The delay is eighty-five minutes and is not a distance.

## Timeline

Built ninety years ago. The board switched off in year two. Ada arrives in year eighty-eight.

## Physical details that must not drift

The lamp above the hatch is amber. The ice is grey and pitted. Three kilometres of it from the window.
""")
    put(root, "story/drafts/draft-01.md", f"draft: 01\ndate: 2026-09-06\n\n{DRAFT_1}\n")
    put(root, "story/drafts/draft-02.md", f"draft: 02\ndate: 2026-09-07\n\n{DRAFT_2}\n")
    put(root, "reviews/REV-01.md", """# REV-01 - adversarial critic, round 1 (draft-01)

## Findings

F1: MAJOR - the last paragraph explains what the image has already shown; a reader who has followed the
arithmetic does not need the sentence that tells them what it means, and being told is the feeling of an
unearned ending.
F2: MINOR - the middle is a sequence of measurements and the keeper does nothing but measure.

## What survived

The opening earns the page. The turn is a turn.
""")
    put(root, "reviews/REV-01-disposition.md", """# Disposition for REV-01 (adversarial critic, round 1)

| Finding | Disposition | Detail |
|---|---|---|
| F1 | FIXED | draft-02 - the last paragraph is cut to its image |
| F2 | REJECTED | the measuring is what she has instead of company; REV-03 read it the same way, and the human kept it in DEC-006 |
""")
    put(root, "reviews/REV-02.md", """# REV-02 - flow critic, round 2 (draft-02)

## Findings

F1: MINOR - "It happened at 11:06." I re-read this to find what "it" was, because the paragraph before
ends on a different subject.
""")
    put(root, "reviews/REV-02-disposition.md", """# Disposition for REV-02 (flow critic, round 2)

| Finding | Disposition | Detail |
|---|---|---|
| F1 | FIXED | draft-02 - the antecedent is named in the sentence |
""")
    _, body2 = split_front_matter((Path(root) / "story/drafts/draft-02.md").read_text(encoding="utf-8"))
    weak = (Path(root) / "reviews/comparisons/calibration-draft-02.md")
    weak.parent.mkdir(parents=True, exist_ok=True)
    weak.write_text("A weakened copy, written by checks/calibrate.py: the text alone, with no header.\n",
                    encoding="utf-8")
    cal = {"planted": "tic-pass, flattened-rhythm, ending-cut-to-summary",
           "pair_file": "calibration-draft-02.md",
           "pair_sha256": sha256_body(weak.read_text(encoding="utf-8")),
           "verdicts": {"craft-critic-a": "caught", "craft-critic-b": "caught"}, "passed": True}
    put(root, "reviews/REV-03.md", """# REV-03 - depth critic, round 1 (draft-01)

## Findings

F1: MINOR - the measuring in the middle is what she has instead of company, and it earns its place; I
read it the same way the adversarial critic did and would not cut it.
""")
    put(root, "reviews/REV-03-disposition.md", """# Disposition for REV-03 (depth critic, round 1)

| Finding | Disposition | Detail |
|---|---|---|
| F1 | REJECTED | nothing to change; the finding agrees with the draft as it stands |
""")
    pairs = []
    # 'ending' is tried against two different exemplars on purpose: the rule that fails a round for losing
    # every pairing on one dimension needs a dimension to recur before it can fire, so a fixture in which
    # every dimension appears once could not exercise it at all.
    for ex, dim, memory, judge in (("salt-gardeners", "ending", False, "craft-critic-a"),
                                   ("nine-kinds", "character", False, "craft-critic-b"),
                                   ("cartographers-wife", "ending", False, "craft-critic-a"),
                                   ("hollow-season", "aftertaste", True, "craft-critic-b")):
        for order, ours in (("AB", "A"), ("BA", "B")):
            pairs.append({"exemplar": ex, "dimension": dim, "order": order, "choice": ours,
                          "from_memory": memory, "judge": judge, "confidence": 4,
                          "reason": "the ending leaves the image rather than the explanation",
                          "evidence": "ours closes on the salt drying white; theirs closes on a paragraph of explanation",
                          "needs": "the weaker one would have to cut its last paragraph and trust the image"})
    put(root, "reviews/comparisons/round-01.json", json.dumps({
        "round": 1, "draft": "draft-02", "draft_sha256": sha256_body(body2),
        "calibration": cal, "pairs": pairs}, indent=1) + "\n")
    rev_pairs = []
    for dim in ("ending", "sentences"):
        for order, ours in (("AB", "A"), ("BA", "B")):
            rev_pairs.append({"exemplar": "draft-01", "dimension": dim, "order": order, "choice": ours,
                              "from_memory": False, "judge": "craft-critic-a", "confidence": 4,
                              "reason": "the cut ending is stronger",
                              "evidence": "the newer draft ends on the image the older one explained",
                              "needs": "the older one would have to lose its last paragraph",
                              "lost": "nothing lost; the older draft's last paragraph said what the image says"})
    # Once G3 is signed the revision round also pairs against the draft the human signed, which in this
    # fixture is draft-01: the pairing that can see a story being sanded flat, which N-against-N-1 cannot.
    base_pairs = []
    for dim in ("ending", "sentences"):
        for order, ours in (("AB", "A"), ("BA", "B")):
            base_pairs.append({"exemplar": "draft-01", "dimension": dim, "order": order, "choice": ours,
                               "from_memory": False, "judge": "craft-critic-a", "confidence": 4,
                               "reason": "the current draft is closer to what the human asked for",
                               "evidence": "the signed draft explained its ending; this one shows it",
                               "needs": "the signed draft would have to cut its last paragraph",
                               "lost": "nothing lost since the human last read it"})
    put(root, "reviews/comparisons/round-01-revision.json", json.dumps({
        "round": 1, "draft": "draft-02", "previous": "draft-01",
        "draft_sha256": sha256_body(body2), "calibration": cal, "pairs": rev_pairs,
        "baseline_signed": {"draft": "draft-01", "pairs": base_pairs}}, indent=1) + "\n")
    r = run(root, "check_state.py", "--accept-caps", "INTAKE")
    assert r.returncode == 0, r.stdout
    r = run(root, "check_gate.py", "--record")
    assert r.returncode == 0, r.stdout
    write_lock(Path(root) / "checks", len(FAULTS), len(CONTROLS), root)   # the lock a real project has after its first run


# ---------------------------------------------------------------- the faults
def f_draft_too_long(r):
    p = Path(r) / "story/drafts/draft-02.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n\n" + ("The ice went on. " * 1400), encoding="utf-8")


def f_todo_left_in(r):
    edit(r, "story/drafts/draft-02.md", "She wrote the time down.", "She wrote the time down. TODO")


def f_stage_direction(r):
    edit(r, "story/drafts/draft-02.md", "She turned it on.", "[scene: describe the switch here]")


def f_draft_numbering_gap(r):
    (Path(r) / "story/drafts/draft-02.md").rename(Path(r) / "story/drafts/draft-03.md")
    edit(r, "story/drafts/draft-03.md", "draft: 02", "draft: 03")


def f_front_matter_mismatch(r):
    edit(r, "story/drafts/draft-02.md", "draft: 02", "draft: 04")


def f_no_date_line(r):
    edit(r, "story/drafts/draft-02.md", "date: 2026-09-07\n", "")


def f_adverbs_over_the_extreme(r):
    p = Path(r) / "story/drafts/draft-02.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n\n" + " ".join(
        f"She moved {w} and waited." for w in
        ["slowly", "quietly", "carefully", "quickly", "softly", "gently", "sharply", "warily",
         "steadily", "grimly", "coldly", "wearily", "patiently", "silently", "stiffly", "calmly",
         "briskly", "faintly", "dimly", "loosely", "tightly", "evenly", "roughly", "keenly", "plainly"]
    ) + "\n", encoding="utf-8")


def f_filter_words_over_the_extreme(r):
    p = Path(r) / "story/drafts/draft-02.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n\n" + " ".join(
        ["She felt the cold.", "She saw that the lamp burned.", "She heard the hum.",
         "She noticed the ice.", "She realized the time.", "She seemed to wait.",
         "She began to count.", "She started to write.", "She tried to sleep.",
         "She could see the shaft.", "She could hear the water.", "She could feel the floor.",
         "Somehow the board was warm.", "Suddenly the light changed.", "She felt the wall.",
         "She saw that the log was old.", "She heard the ferry.", "She noticed the note.",
         "She realized the number.", "She seemed to know."]) + "\n", encoding="utf-8")


def f_same_opener_run(r):
    p = Path(r) / "story/drafts/draft-02.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n\n" + "\n\n".join(
        ["Later the hum returned and she wrote it down again.",
         "Later the lamp went out and came back on its own.",
         "Later the buffer filled and she did not read it.",
         "Later the ferry was still two hundred days out."]) + "\n", encoding="utf-8")


def f_paragraph_too_long(r):
    p = Path(r) / "story/drafts/draft-02.md"
    meta, body = split_front_matter(p.read_text(encoding="utf-8"))
    p.write_text("draft: 02\ndate: 2026-09-07\n\n" + re.sub(r"\n\s*\n", " ", body).strip() + "\n",
                 encoding="utf-8")


def f_sentences_all_one_length(r):
    flat = " ".join(f"{w} came down across the ice again now." for w in
                    ["Snow", "Rain", "Light", "Dark", "Wind", "Cold", "Frost", "Dust", "Steam", "Salt",
                     "Smoke", "Ash", "Hail", "Sleet", "Fog", "Grit", "Rime", "Spray", "Foam", "Grey"])
    put(r, "story/drafts/draft-02.md", f"draft: 02\ndate: 2026-09-07\n\n{flat}\n")


def f_undeclared_repeated_word(r):
    edit(r, "story/BIBLE.md", "| nothing | the story turns on a record of nothing being a record |\n", "")


def f_name_respelled(r):
    edit(r, "story/drafts/draft-02.md", "She traced the draw for three days.",
         "She traced the draw through Kettel for three days.")


def f_bible_term_never_used(r):
    edit(r, "story/BIBLE.md", "| Oyelaran | the keeper who switched the board off | as spelled here |",
         "| Oyelaran | the keeper who switched the board off | as spelled here |\n| Quorl | a thing cut in revision | as spelled here |")


def f_review_without_disposition(r):
    (Path(r) / "reviews/REV-01-disposition.md").unlink()


def f_disposition_missing_a_row(r):
    edit(r, "reviews/REV-01-disposition.md",
         "| F2 | REJECTED | the measuring is what she has instead of company; REV-03 read it the same way, and the human kept it in DEC-006 |\n", "")


def f_disposition_blank_finding_cell(r):
    p = Path(r) / "reviews/REV-01-disposition.md"
    p.write_text(p.read_text(encoding="utf-8").rstrip("\n") + "\n|  | DEFERRED | owner: nobody |\n", encoding="utf-8")


def f_fixed_names_missing_draft(r):
    edit(r, "reviews/REV-01-disposition.md", "draft-02 - the last paragraph", "draft-09 - the last paragraph")


def f_fixed_names_no_draft(r):
    edit(r, "reviews/REV-02-disposition.md", "draft-02 - the antecedent is named in the sentence",
         "the antecedent is named in the sentence")


def f_finding_outside_the_section(r):
    edit(r, "reviews/REV-01.md", "## What survived", "## What survived\n\nF3: the title is weak.\n")


def f_second_findings_heading(r):
    p = Path(r) / "reviews/REV-01.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n## Findings\n\nF4: and another thing.\n", encoding="utf-8")


def f_disposition_row_outside_the_table(r):
    p = Path(r) / "reviews/REV-01-disposition.md"
    p.write_text(p.read_text(encoding="utf-8") + "\nA closing note.\n\n| F9 | FIXED | draft-02 - smuggled in |\n",
                 encoding="utf-8")


def f_cap_raised_above_accepted(r):
    edit(r, "STATE.md", "| Revision rounds in M3 | 12 | 2 |", "| Revision rounds in M3 | 20 | 2 |")


def f_used_blank(r):
    edit(r, "STATE.md", "| Fresh-reader calls | 5 | 1 |", "| Fresh-reader calls | 5 |  |")


def f_cap_overspent(r):
    edit(r, "STATE.md", "| Fresh-reader calls | 5 | 1 |", "| Fresh-reader calls | 5 | 6 |")


def f_milestone_past_an_unsigned_gate(r):
    p = Path(r) / "DECISIONS.md"
    t = p.read_text(encoding="utf-8")
    i, j = t.index("### G3"), t.index("### G4")
    p.write_text(t[:i] + t[j:], encoding="utf-8")


def f_cap_dropped(r):
    edit(r, "STATE.md", "| Probe passages | 6 | 6 | budget for M1 |\n", "")


def f_gate_signoff_too_short(r):
    edit(r, "DECISIONS.md", "I read the whole thing aloud and it held.", "Fine.")
    edit(r, "DECISIONS.md", " The place where I stumbled before is gone and the ending now\nleaves me with the image rather than the explanation. This is what I wanted and it goes through.", "")


def f_gate_signoff_in_the_agents_voice(r):
    p = Path(r) / "DECISIONS.md"
    t = p.read_text(encoding="utf-8")
    i = t.index("### G4")
    p.write_text(t[:i] + "### G4 - 2026-09-07\n\nThis milestone is excellent and the story meets all the "
                 "criteria set out in the brief. No further changes are needed at this time. The work "
                 "should go through immediately.\n", encoding="utf-8")


def f_past_signoff_reworded(r):
    edit(r, "DECISIONS.md", "The spine is the story I wanted from the card.",
         "The spine is roughly the story I had in mind.")


def f_past_signoff_deleted(r):
    p = Path(r) / "DECISIONS.md"
    t = p.read_text(encoding="utf-8")
    i, j = t.index("### G1"), t.index("### G2")
    p.write_text(t[:i] + t[j:], encoding="utf-8")


def f_doc_names_a_missing_check(r):
    p = Path(r) / "CLAUDE.md"
    p.write_text(p.read_text(encoding="utf-8") + "\nThe voice is held by `check_voice.py` every round.\n",
                 encoding="utf-8")


def f_skill_names_a_missing_agent(r):
    p = Path(r) / "claude/skills/m3-draft-revise/SKILL.md"
    p.write_text(p.read_text(encoding="utf-8") + "\nAlso spawn `ghost-critic` each round.\n", encoding="utf-8")


def f_doc_names_a_missing_make_target(r):
    p = Path(r) / "READ_ME_FIRST.md"
    p.write_text(p.read_text(encoding="utf-8") + "\nRun `make polish` when you are ready.\n", encoding="utf-8")


def f_doc_names_a_missing_path(r):
    p = Path(r) / "CLAUDE.md"
    p.write_text(p.read_text(encoding="utf-8") + "\nThe voice sheet lives at `design/VOICE.md`.\n",
                 encoding="utf-8")


def _cmp(r, fn):
    p = Path(r) / "reviews/comparisons/round-01.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    fn(d)
    p.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")


def f_pair_judged_one_order(r):
    _cmp(r, lambda d: d.__setitem__("pairs", [p for p in d["pairs"]
                                              if not (p["exemplar"] == "nine-kinds" and p["order"] == "BA")]))


def f_no_calibration(r):
    _cmp(r, lambda d: d.pop("calibration"))


def f_judge_missed_the_planted_defect(r):
    _cmp(r, lambda d: d["calibration"]["verdicts"].__setitem__("craft-critic-b", "missed"))


def f_stale_draft_hash(r):
    _cmp(r, lambda d: d.__setitem__("draft_sha256", "0" * 64))


def f_gate_on_memory_only(r):
    _cmp(r, lambda d: [p.__setitem__("from_memory", True) for p in d["pairs"]])


def f_caps_accepted_under_a_row_that_does_not_exist(r):
    """An agent raises a cap, then re-accepts the caps under a decision row nobody wrote. The acceptance
    must be refused, so the raised cap is still caught on the next run."""
    edit(r, "STATE.md", "| Revision rounds in M3 | 12 |", "| Revision rounds in M3 | 40 |")
    run(r, "check_state.py", "--accept-caps", "DEC-777")


def f_not_a_drift_declared_with_no_reason(r):
    f_name_respelled(r)
    edit(r, "story/BIBLE.md", "| Word that is not a drift | Why both are meant to be there |\n|---|---|",
         "| Word that is not a drift | Why both are meant to be there |\n|---|---|\n| Kettel |  |")


def f_two_verdicts_from_one_judge_in_one_order(r):
    def dup(d):
        first = [q for q in d["pairs"] if q["exemplar"] == "nine-kinds" and q["order"] == "AB"][0]
        d["pairs"].append(dict(first))
    _cmp(r, dup)


def f_rubric_without_slugs(r):
    lines = (Path(r) / "design/RUBRIC.md").read_text(encoding="utf-8").splitlines(True)
    out = []
    for line in lines:
        if line.startswith("| ") and "`" in line:      # strip the Slug cell from every dimension row
            cells = line.split("|")
            del cells[2]
            line = "|".join(cells)
        elif line.startswith("| Dimension |") or line.startswith("|---|---|---|---|"):
            cells = line.split("|")
            del cells[2]
            line = "|".join(cells)
        out.append(line)
    (Path(r) / "design/RUBRIC.md").write_text("".join(out), encoding="utf-8")


def f_major_rejected_citing_only_a_sibling_review(r):
    edit(r, "reviews/REV-01.md", "F2: MINOR - the middle is a sequence", "F2: MAJOR - the middle is a sequence")
    edit(r, "reviews/REV-01-disposition.md",
         "| F2 | REJECTED | the measuring is what she has instead of company; REV-03 read it the same way, and the human kept it in DEC-006 |",
         "| F2 | REJECTED | the measuring is what she has instead of company; REV-03 read it the same way |")


def f_revision_round_without_the_signed_baseline(r):
    _rev(r, lambda d: d.pop("baseline_signed", None))


def f_loses_every_pairing_on_a_dimension(r):
    def flip(d):                                     # both exemplars tried on 'ending', so the dimension
        for p in d["pairs"]:                         # recurs and the rule is allowed to fire
            if p["dimension"] == "ending":
                p["choice"] = "B" if p["order"] == "AB" else "A"
    _cmp(r, flip)


def f_pair_without_from_memory(r):
    _cmp(r, lambda d: [p.pop("from_memory") for p in d["pairs"] if p["exemplar"] == "nine-kinds"])


def f_pair_with_misspelled_from_memory(r):
    def rename(d):
        for p in d["pairs"]:
            if p["exemplar"] == "nine-kinds":
                p["fromMemory"] = p.pop("from_memory")
    _cmp(r, rename)


def f_pair_with_a_dimension_off_the_rubric(r):
    _cmp(r, lambda d: [p.__setitem__("dimension", "The ending") for p in d["pairs"]
                       if p["exemplar"] == "salt-gardeners"])


def f_pair_without_evidence(r):
    _cmp(r, lambda d: [p.__setitem__("evidence", "") for p in d["pairs"]
                       if p["exemplar"] == "hollow-season"])


def f_pair_without_needs(r):
    _cmp(r, lambda d: [p.pop("needs") for p in d["pairs"] if p["exemplar"] == "hollow-season"])


def f_calibration_verdicts_empty(r):
    _cmp(r, lambda d: d["calibration"].__setitem__("verdicts", {}))


def f_uncalibrated_judge_voted(r):
    _cmp(r, lambda d: d["calibration"]["verdicts"].pop("craft-critic-b"))


def f_calibration_pair_missing(r):
    (Path(r) / "reviews/comparisons/calibration-draft-02.md").unlink()


def f_calibration_pair_altered(r):
    p = Path(r) / "reviews/comparisons/calibration-draft-02.md"
    p.write_text(p.read_text(encoding="utf-8") + "and a sentence added after the judging.\n", encoding="utf-8")


def f_one_exemplar_four_dimensions(r):
    _cmp(r, lambda d: [p.__setitem__("exemplar", "salt-gardeners") for p in d["pairs"]])


def f_ties_counted_as_wins(r):
    _cmp(r, lambda d: [p.__setitem__("choice", "A") for p in d["pairs"]])


def f_no_revision_round(r):
    (Path(r) / "reviews/comparisons/round-01-revision.json").unlink()


def f_revision_verdict_without_lost(r):
    p = Path(r) / "reviews/comparisons/round-01-revision.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    d["pairs"][0].pop("lost")
    p.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")


def f_major_rejected_on_the_agents_say_so(r):
    edit(r, "reviews/REV-01-disposition.md",
         "| F2 | REJECTED | the measuring is what she has instead of company; REV-03 read it the same way, and the human kept it in DEC-006 |",
         "| F2 | REJECTED | the measuring is what she has instead of company |")
    edit(r, "reviews/REV-01.md", "F2: MINOR - the middle is a sequence", "F2: MAJOR - the middle is a sequence")


def f_major_deferred_at_a_gate(r):
    edit(r, "reviews/REV-01-disposition.md", "| F1 | FIXED | draft-02 - the last paragraph is cut to its image |",
         "| F1 | DEFERRED | trigger: a later pass; owner: the writer |")


def f_finding_without_a_severity(r):
    edit(r, "reviews/REV-02.md", 'F1: MINOR - "It happened at 11:06."', 'F1: "It happened at 11:06."')


def f_motif_declared_without_a_reason(r):
    edit(r, "story/BIBLE.md", "| nothing | the story turns on a record of nothing being a record |",
         "| nothing |  |")


def f_three_reverts_in_a_row(r):
    edit(r, "STATE.md", "| Reverted revisions in a row | 0 | the m3 skill |",
         "| Reverted revisions in a row | 3 | the m3 skill |")


def f_repeat_beyond_the_top_five(r):
    """A tic outside the five most frequent words, with five honest motifs above it in the count."""
    edit(r, "story/BIBLE.md", "| nothing | the story turns on a record of nothing being a record |",
         "| nothing | the story turns on a record of nothing being a record |\n"
         "| eighty | the years the station waited |\n| station | the place is the other character |\n"
         "| kilometres | distance is what she measures |\n| something | what she cannot name |")
    p = Path(r) / "story/drafts/draft-02.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n\n" + " ".join(
        ["The console held its light.", "She read the console again.", "A console is a promise.",
         "The console said nothing new.", "She left the console on.", "The console, then.",
         "Morning, and the console.", "The console."]) + "\n", encoding="utf-8")


def f_losing_round_rerun_until_it_wins(r):
    p = Path(r) / "reviews/comparisons/round-01.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    lost = json.loads(json.dumps(d))
    for pair in lost["pairs"]:
        pair["choice"] = "B" if pair["order"] == "AB" else "A"
    put(r, "reviews/comparisons/round-01.json", json.dumps(lost, indent=1) + "\n")
    d["round"] = 2
    put(r, "reviews/comparisons/round-02.json", json.dumps(d, indent=1) + "\n")


def f_second_change_under_a_spent_amend_row(r):
    c_human_amends_their_own_signoff(r)
    res = run(r, "check_gate.py", "--record")
    assert res.returncode == 0, res.stdout          # the first change is authorised and spends the row
    t = (Path(r) / "DECISIONS.md").read_text(encoding="utf-8")
    i = t.index("### G2"); j = t.index("### G3")
    put(r, "DECISIONS.md", t[:i] + "### G2 - 2026-09-06\n\nThe spine is exactly right and I have no "
        "reservations at all about any part of it. Everything here is what I asked for. It goes through "
        "without changes of any kind.\n\n" + t[j:])


def f_major_rejected_citing_its_own_review(r):
    edit(r, "reviews/REV-01.md", "F2: MINOR - the middle is a sequence", "F2: MAJOR - the middle is a sequence")
    edit(r, "reviews/REV-01-disposition.md",
         "| F2 | REJECTED | the measuring is what she has instead of company; REV-03 read it the same way, and the human kept it in DEC-006 |",
         "| F2 | REJECTED | the measuring is the point, as REV-01 itself concedes two lines later |")


def f_major_rejected_citing_a_review_that_does_not_exist(r):
    edit(r, "reviews/REV-01.md", "F2: MINOR - the middle is a sequence", "F2: MAJOR - the middle is a sequence")
    edit(r, "reviews/REV-01-disposition.md",
         "| F2 | REJECTED | the measuring is what she has instead of company; REV-03 read it the same way, and the human kept it in DEC-006 |",
         "| F2 | REJECTED | the measuring is the point; REV-99 agreed and the human said so in DEC-999 |")


def f_disposition_word_not_one_of_the_three(r):
    edit(r, "reviews/REV-01.md", "F2: MINOR - the middle is a sequence", "F2: MAJOR - the middle is a sequence")
    edit(r, "reviews/REV-01-disposition.md",
         "| F2 | REJECTED | the measuring is what she has instead of company; REV-03 read it the same way, and the human kept it in DEC-006 |",
         "| F2 | Rejected (see below) | the measuring is the point |")


def _rev(r, fn):
    p = Path(r) / "reviews/comparisons/round-01-revision.json"
    d = json.loads(p.read_text(encoding="utf-8"))
    fn(d)
    p.write_text(json.dumps(d, indent=1) + "\n", encoding="utf-8")


def f_revision_round_without_calibration(r):
    _rev(r, lambda d: d.pop("calibration"))


def f_revision_round_of_one_pair(r):
    _rev(r, lambda d: d.__setitem__("pairs", [p for p in d["pairs"] if p["dimension"] == "ending"]))


def f_check_changed_without_rerunning(r):
    p = Path(r) / "checks/check_tics.py"
    p.write_text(p.read_text(encoding="utf-8") + "\n# an innocent comment\n", encoding="utf-8")


FAULTS = [
    ("a draft over the length the human set", f_draft_too_long, ["check_manuscript.py", "--milestone", "4", "--complete"], "outside the range"),
    ("a TODO left in the manuscript", f_todo_left_in, ["check_manuscript.py"], "TODO"),
    ("a bracketed stage direction standing in for a scene", f_stage_direction, ["check_manuscript.py"], "stage direction"),
    ("a gap in the draft numbering", f_draft_numbering_gap, ["check_manuscript.py"], "numbered"),
    ("front matter whose draft number is not the file's", f_front_matter_mismatch, ["check_manuscript.py"], "front matter says draft"),
    ("a draft with no date line", f_no_date_line, ["check_manuscript.py"], "no 'date:' line"),
    ("adverbs past the extreme", f_adverbs_over_the_extreme, ["check_tics.py"], "-ly adverbs at"),
    ("filter words past the extreme", f_filter_words_over_the_extreme, ["check_tics.py"], "filter words at"),
    ("four paragraphs in a row opening on one word", f_same_opener_run, ["check_tics.py"], "in a row open with"),
    ("a paragraph over the maximum", f_paragraph_too_long, ["check_tics.py"], "over the maximum of"),
    ("every sentence the same length", f_sentences_all_one_length, ["check_tics.py"], "sentence lengths vary by"),
    ("a repeated word not declared as a motif", f_undeclared_repeated_word, ["check_tics.py"], "declare it in BIBLE.md"),
    ("a name respelled halfway through", f_name_respelled, ["check_continuity.py"], "one character from the bible's"),
    ("a bible entry the story never uses", f_bible_term_never_used, ["check_continuity.py"], "never appears in"),
    ("a review with findings and no disposition", f_review_without_disposition, ["check_reviews.py"], "no REV-01-disposition.md"),
    ("a disposition missing a finding's row", f_disposition_missing_a_row, ["check_reviews.py"], "no row for F2"),
    ("a disposition row with a blank Finding cell", f_disposition_blank_finding_cell, ["check_reviews.py"], "blank Finding cell"),
    ("FIXED naming a draft that does not exist", f_fixed_names_missing_draft, ["check_reviews.py"], "not in story/drafts/"),
    ("FIXED naming no draft at all", f_fixed_names_no_draft, ["check_reviews.py"], "FIXED naming nothing that changed"),
    ("a numbered finding outside the Findings section", f_finding_outside_the_section, ["check_reviews.py"], "outside the '## Findings' heading"),
    ("a second Findings heading", f_second_findings_heading, ["check_reviews.py"], "two '## Findings' headings"),
    ("a disposition row that lost its table", f_disposition_row_outside_the_table, ["check_reviews.py"], "a table row outside any table"),
    ("a cap raised above the accepted value", f_cap_raised_above_accepted, ["check_state.py", "--milestone", "4"], "above the accepted"),
    ("a cap's Used left blank", f_used_blank, ["check_state.py", "--milestone", "4"], "Used is blank"),
    ("a cap drawn on after it was spent", f_cap_overspent, ["check_state.py", "--milestone", "4"], "is over the cap"),
    ("a milestone advanced past an unsigned gate", f_milestone_past_an_unsigned_gate, ["check_state.py", "--milestone", "4"], "carries no '### G3' sign-off"),
    ("an accepted cap dropped from the table", f_cap_dropped, ["check_state.py", "--milestone", "4"], "is gone from STATE.md"),
    ("a gate sign-off of one line", f_gate_signoff_too_short, ["check_gate.py", "--gate", "4"], "words; the human writes"),
    ("a gate sign-off in the agent's voice", f_gate_signoff_in_the_agents_voice, ["check_gate.py", "--gate", "4"], "how an agent writes a sign-off"),
    ("a past sign-off reworded after the fact", f_past_signoff_reworded, ["check_gate.py", "--record"], "not the paragraph first recorded"),
    ("a past sign-off deleted after the loop moved on", f_past_signoff_deleted, ["check_gate.py", "--record"], "once written, is gone"),
    ("a document naming a check that does not exist", f_doc_names_a_missing_check, ["check_claims.py"], "which is not in checks/"),
    ("a skill spawning an agent with no brief", f_skill_names_a_missing_agent, ["check_claims.py"], "no brief in claude/agents/"),
    ("a document naming a make target that does not exist", f_doc_names_a_missing_make_target, ["check_claims.py"], "the Makefile does not define"),
    ("a document naming a path that is not in the kit", f_doc_names_a_missing_path, ["check_claims.py"], "neither in the kit nor beside it"),
    ("a pair judged in one order only", f_pair_judged_one_order, ["check_comparisons.py", "--milestone", "4"], "is judged both ways"),
    ("a comparison round with no calibration", f_no_calibration, ["check_comparisons.py", "--milestone", "4"], "no calibration"),
    ("a judge that missed the planted defect", f_judge_missed_the_planted_defect, ["check_comparisons.py", "--milestone", "4"], "did not catch the planted"),
    ("a comparison round judged on an older draft, at a gate", f_stale_draft_hash, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "changed since this round was judged"),
    ("a gate met on comparisons made only from memory", f_gate_on_memory_only, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "judged against a supplied exemplar text"),
    ("a draft losing every pairing on one dimension", f_loses_every_pairing_on_a_dimension, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "loses every pairing on"),
    ("a pair with no from_memory field, which would count as supplied text", f_pair_without_from_memory, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "has no boolean 'from_memory'"),
    ("a pair whose from_memory field is misspelled", f_pair_with_misspelled_from_memory, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "has no boolean 'from_memory'"),
    ("a pair naming a dimension that is not a rubric slug", f_pair_with_a_dimension_off_the_rubric, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "not one of the rubric's slugs"),
    ("a verdict with a choice and no evidence", f_pair_without_evidence, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "has no 'evidence'"),
    ("a verdict that does not say what the weaker text needs", f_pair_without_needs, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "has no 'needs'"),
    ("caps re-accepted under a decision row nobody wrote", f_caps_accepted_under_a_row_that_does_not_exist, ["check_state.py", "--milestone", "4"], "is above the accepted"),
    ("a drift declared not-a-drift with no reason", f_not_a_drift_declared_with_no_reason, ["check_continuity.py"], "declared not a drift with no reason"),
    ("two verdicts from one judge in one order", f_two_verdicts_from_one_judge_in_one_order, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "one judge votes once per order"),
    ("a rubric with no dimension slugs, which would switch off slug validation", f_rubric_without_slugs, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "no dimension slugs"),
    ("a MAJOR rejected by citing a sibling review that never agreed", f_major_rejected_citing_only_a_sibling_review, ["check_reviews.py", "--gate", "4"], "without the human's say-so"),
    ("a revision round with no signed-draft baseline", f_revision_round_without_the_signed_baseline, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "no 'baseline_signed'"),
    ("a calibration recording no verdicts at all", f_calibration_verdicts_empty, ["check_comparisons.py", "--milestone", "4"], "records no verdicts"),
    ("a judge that voted and was never calibrated", f_uncalibrated_judge_voted, ["check_comparisons.py", "--milestone", "4"], "appear in no calibration verdict"),
    ("a calibration whose pair file is gone", f_calibration_pair_missing, ["check_comparisons.py", "--milestone", "4"], "no pair file that exists"),
    ("a calibration pair altered after the judging", f_calibration_pair_altered, ["check_comparisons.py", "--milestone", "4"], "has changed since the round was judged"),
    ("a gate met on four dimensions against one exemplar", f_one_exemplar_four_dimensions, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "different exemplar(s); a gate needs"),
    ("a judge with pure position bias, its ties counted as wins", f_ties_counted_as_wins, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "order-disagreements"),
    ("a gate with no draft-against-draft round", f_no_revision_round, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "no revision round"),
    ("a revision verdict that does not say what was lost", f_revision_verdict_without_lost, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "no 'lost' answer"),
    ("a MAJOR rejected on the orchestrator's own say-so", f_major_rejected_on_the_agents_say_so, ["check_reviews.py"], "without the human's say-so"),
    ("a MAJOR left deferred at a gate", f_major_deferred_at_a_gate, ["check_reviews.py", "--gate", "4"], "deferred at G4"),
    ("a finding written with no severity", f_finding_without_a_severity, ["check_reviews.py"], "no severity"),
    ("a motif declared with no reason", f_motif_declared_without_a_reason, ["check_tics.py"], "declared with no reason"),
    ("three revisions reverted in a row", f_three_reverts_in_a_row, ["check_state.py", "--milestone", "4"], "being sanded"),
    ("a tic outside the five most repeated words", f_repeat_beyond_the_top_five, ["check_tics.py"], "appears 8 times"),
    ("a losing round re-run until it wins", f_losing_round_rerun_until_it_wins, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "rounds were judged on draft-02"),
    ("a second change to a sign-off under one spent gate-amend row", f_second_change_under_a_spent_amend_row, ["check_gate.py", "--record"], "not the paragraph first recorded"),
    ("a MAJOR rejected by citing the review it is dispositioning", f_major_rejected_citing_its_own_review, ["check_reviews.py"], "without the human's say-so"),
    ("a MAJOR rejected by citing a review and a row that do not exist", f_major_rejected_citing_a_review_that_does_not_exist, ["check_reviews.py"], "without the human's say-so"),
    ("a disposition word that is not one of the three", f_disposition_word_not_one_of_the_three, ["check_reviews.py"], "exactly FIXED, REJECTED, or DEFERRED"),
    ("a revision round with no calibration", f_revision_round_without_calibration, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "no calibration"),
    ("a revision round of a single pair", f_revision_round_of_one_pair, ["check_comparisons.py", "--milestone", "4", "--gate", "4"], "fewer than 2 pairs"),
    ("a check changed without re-running the fault suite", f_check_changed_without_rerunning, ["run_all_checks.py", "--milestone", "4"], "has changed since the fault suite last passed"),
]


# ------------------------------------------------------------- the controls
def c_new_draft_in_sequence(r):
    src = (Path(r) / "story/drafts/draft-02.md").read_text(encoding="utf-8")
    put(r, "story/drafts/draft-03.md", src.replace("draft: 02", "draft: 03").replace("2026-09-07", "2026-09-08"))


def c_motif_declared(r):
    p = Path(r) / "story/drafts/draft-02.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n\n" + " ".join(
        ["The ferry was late.", "The ferry was always late.", "She thought about the ferry.",
         "A ferry is a promise.", "The ferry would come.", "The ferry, then, was the whole of it.",
         "She stopped counting days and counted ferry weeks instead."]) + "\n", encoding="utf-8")
    edit(r, "story/BIBLE.md", "| nothing | the story turns on a record of nothing being a record |",
         "| nothing | the story turns on a record of nothing being a record |\n| ferry | the only thing that arrives, and it is what she measures time in |")


def c_cap_lowered_by_an_agent(r):
    edit(r, "STATE.md", "| Revision rounds in M3 | 12 | 2 |", "| Revision rounds in M3 | 8 | 2 |")


def c_bible_term_added_and_used(r):
    edit(r, "story/BIBLE.md", "| hydrophones | the listening elements of the lattice | paragraph 7 |",
         "| hydrophones | the listening elements of the lattice | paragraph 7 |\n| ferry | the vessel that swaps the keeper | paragraph 4 |")


def c_review_closed_properly(r):
    put(r, "reviews/REV-03.md", "# REV-03 - depth critic, round 2 (draft-02)\n\n## Findings\n\n"
        "F1: MINOR - the question is real, but the middle answers it once out loud where it does not need to.\n")
    put(r, "reviews/REV-03-disposition.md", "# Disposition for REV-03 (depth critic, round 2)\n\n"
        "| Finding | Disposition | Detail |\n|---|---|---|\n"
        "| F1 | FIXED | draft-02 - the sentence that said it out loud is gone |\n")


def c_decision_row_after_the_gates(r):
    edit(r, "DECISIONS.md",
         "| DEC-005 | 2026-09-07 | human | title | \"A Record of Nothing\" | it is the line the story turns on | \"Kettle\", \"The Long Ferry\" |",
         "| DEC-005 | 2026-09-07 | human | title | \"A Record of Nothing\" | it is the line the story turns on | \"Kettle\", \"The Long Ferry\" |\n"
         "| DEC-006 | 2026-09-07 | human | caps | one more fresh-reader call | I want a second opinion on the ending | stop here |")


def c_comparison_round_for_a_new_draft(r):
    """The next round, on the next draft: a new numbered record beside the old one, nothing overwritten."""
    c_new_draft_in_sequence(r)
    _, body = split_front_matter((Path(r) / "story/drafts/draft-03.md").read_text(encoding="utf-8"))
    for name, new in (("round-01.json", "round-02.json"), ("round-01-revision.json", "round-02-revision.json")):
        d = json.loads((Path(r) / "reviews/comparisons" / name).read_text(encoding="utf-8"))
        d["round"], d["draft"], d["draft_sha256"] = 2, "draft-03", sha256_body(body)
        if "previous" in d:
            d["previous"] = "draft-02"
            for pair in d["pairs"]:
                pair["exemplar"] = "draft-02"
        put(r, f"reviews/comparisons/{new}", json.dumps(d, indent=1) + "\n")


def c_deliberate_roughness(r):
    p = Path(r) / "story/drafts/draft-02.md"
    p.write_text(p.read_text(encoding="utf-8") +
                 "\n\nNo answer.\n\nShe waited - the way you wait for a door - and the door did not open.\n",
                 encoding="utf-8")


def c_protagonist_named_often(r):
    """A third-person story says its protagonist's name. Fifteen times in eleven hundred words is ordinary."""
    edit(r, "story/BIBLE.md", "| Ada | the keeper | never Ada's full name |",
         "| Miriam | the keeper | never her full name |")
    p = Path(r) / "story/drafts/draft-02.md"
    body = p.read_text(encoding="utf-8").replace("Ada ", "Miriam ").replace("Ada,", "Miriam,")
    extra = " ".join(["Miriam counted again.", "The lamp held, and Miriam wrote it down.",
                      "Miriam slept badly.", "In the morning Miriam checked the buffer.",
                      "Miriam did the arithmetic twice.", "Nobody had told Miriam about the board.",
                      "Miriam sat with it.", "The ice, Miriam thought, was the same ice.",
                      "Miriam turned the lamp off.", "Miriam waited."])
    p.write_text(body.rstrip("\n") + "\n\n" + extra + "\n", encoding="utf-8")


def c_name_that_neighbours_an_ordinary_word(r):
    """A character called Wren, in a story where the word "when" appears: not a drifted name."""
    edit(r, "story/BIBLE.md", "| Mir | the person who taught her the discipline | one syllable |",
         "| Wren | the person who taught her the discipline | one syllable |")
    p = Path(r) / "story/drafts/draft-02.md"
    p.write_text(p.read_text(encoding="utf-8").replace("Mir ", "Wren ").replace("Mir,", "Wren,"),
                 encoding="utf-8")


def c_human_amends_their_own_signoff(r):
    edit(r, "DECISIONS.md", "| DEC-006 | 2026-09-07 | human | taste |",
         "| DEC-007 | 2026-09-07 | human | gate-amend | I reworded my own G2 paragraph | it said less than I meant | leave it |\n| DEC-006 | 2026-09-07 | human | taste |")
    edit(r, "DECISIONS.md", "The spine is the story I wanted from the card.",
         "The spine is exactly the story I wanted from the card.")


def c_plural_of_an_invented_term(r):
    """Two lattices is not a drifted lattice."""
    edit(r, "story/drafts/draft-02.md", "She traced the draw for three days.",
         "She traced the draw for three days. Two lattices, in fact, had been sunk here, and only one still ran.")


def c_declared_near_neighbour(r):
    """Mara and Mars in one story: a writer's choice a program cannot tell from a typo, so the bible says so."""
    edit(r, "story/BIBLE.md", "| Ada | the keeper | never Ada's full name |",
         "| Ada | the keeper | never Ada's full name |\n| Mara | the keeper before her | as spelled here |")
    edit(r, "story/BIBLE.md", "| Word that is not a drift | Why both are meant to be there |\n|---|---|",
         "| Word that is not a drift | Why both are meant to be there |\n|---|---|\n| Mars | the planet, and Mara the keeper; both are meant |")
    edit(r, "story/drafts/draft-02.md", "She wrote the time down.",
         "She wrote the time down, the way Mara had, in the years the relay still spoke to Mars.")


def c_major_rejected_with_real_corroboration(r):
    """A MAJOR closed as REJECTED under a decision row the human actually wrote — the only thing that
    closes one, since every review in a round was commissioned by the orchestrator."""
    edit(r, "reviews/REV-01.md", "F2: MINOR - the middle is a sequence", "F2: MAJOR - the middle is a sequence")


def c_one_lost_pairing_on_a_dimension_tried_once(r):
    """A dimension tried against a single exemplar and lost. Four exemplars over eight rubric dimensions
    means most dimensions are tried once a round, so failing the round for one clean loss would make the
    real bar 'never lose a single pairing' — much stricter than the bar §7.1 states. It is printed, not
    failed, and the win share still carries the round."""
    def flip(d):
        for p in d["pairs"]:
            if p["exemplar"] == "hollow-season":     # 'aftertaste', the one dimension tried once
                p["choice"] = "B" if p["order"] == "AB" else "A"
    _cmp(r, flip)


def c_pristine_kit_with_no_drafts_folder(r):
    """Day one: the kit as deployed, before the first draft has created story/drafts/. Git keeps no empty
    folder, so a fresh copy has none, and four documents name it. The fixture writes drafts into that
    folder before any check runs, so this is the one state the suite never reached, and the one the
    handoff prompt's first command runs in."""
    shutil.rmtree(Path(r) / "story/drafts")


CONTROLS = [
    ("the day-one claims check on a pristine kit with no drafts folder", c_pristine_kit_with_no_drafts_folder, ["check_claims.py"]),
    ("a new draft added in sequence", c_new_draft_in_sequence, ["check_manuscript.py", "--milestone", "4", "--complete"]),
    ("a repeated word declared as a motif", c_motif_declared, ["check_tics.py"]),
    ("a cap lowered by an agent", c_cap_lowered_by_an_agent, ["check_state.py", "--milestone", "4"]),
    ("a bible term added and used in the draft", c_bible_term_added_and_used, ["check_continuity.py"]),
    ("a review closed with a complete disposition", c_review_closed_properly, ["check_reviews.py"]),
    ("a decision row added after the gates", c_decision_row_after_the_gates, ["check_gate.py", "--record"]),
    ("a comparison round for a new draft", c_comparison_round_for_a_new_draft, ["check_comparisons.py", "--milestone", "4", "--gate", "4"]),
    ("deliberate roughness: a fragment and a dash", c_deliberate_roughness, ["check_tics.py"]),
    ("a protagonist named fifteen times in eleven hundred words", c_protagonist_named_often, ["check_tics.py"]),
    ("a character called Wren in a story containing the word when", c_name_that_neighbours_an_ordinary_word, ["check_continuity.py"]),
    ("the human amending their own sign-off under a gate-amend row", c_human_amends_their_own_signoff, ["check_gate.py", "--record"]),
    ("the plural of an invented term", c_plural_of_an_invented_term, ["check_continuity.py"]),
    ("a near neighbour the bible declares on purpose", c_declared_near_neighbour, ["check_continuity.py"]),
    ("a MAJOR rejected by naming a review and a human row that exist", c_major_rejected_with_real_corroboration, ["check_reviews.py", "--gate", "4"]),
    ("a dimension tried against one exemplar and lost", c_one_lost_pairing_on_a_dimension_tried_once, ["check_comparisons.py", "--milestone", "4", "--gate", "4"]),
]


def write_lock(checks_dir, faults, controls, root):
    lock = Path(checks_dir) / "faults.lock.json"
    if lock.exists():
        old = json.loads(lock.read_text(encoding="utf-8"))
        smaller = faults < old.get("faults", 0) or controls < old.get("controls", 0)
        allowed = re.search(r"\|\s*human\s*\|\s*fault-suite\s*\|", (Path(root) / "DECISIONS.md").read_text(encoding="utf-8"))
        if smaller and not allowed:
            print(f"REFUSED: the suite has shrunk ({old.get('faults')}→{faults} faults, "
                  f"{old.get('controls')}→{controls} controls) and DECISIONS.md carries no human row of "
                  f"type fault-suite permitting it; a fault removed quietly is a check nobody tests")
            return False
    data = {"faults": faults, "controls": controls, "checks": {}}
    for p in sorted(Path(checks_dir).iterdir()):
        if p.is_file() and p.name not in ("faults.lock.json", "caps.approved.json", "gates.seen.json"):
            data["checks"][p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
    lock.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return True


def main():
    base = Path(tempfile.mkdtemp(prefix="story-loop-faults-"))
    fixture = base / "fixture"
    build_fixture(fixture)
    r = run(fixture, "run_all_checks.py", "--milestone", "4", "--complete", "--gate", "4")
    if r.returncode != 0:
        print(r.stdout)
        print("FIXTURE DOES NOT PASS; fix the fixture or the checks before planting faults")
        return 1
    print("fixture passes every check at milestone 4 with gate 4")
    missed = 0
    for i, (name, mutate, cmd, expect) in enumerate(FAULTS, 1):
        scratch = base / f"fault-{i:02d}"
        shutil.copytree(fixture, scratch)
        mutate(scratch)
        res = run(scratch, cmd[0], *cmd[1:])
        caught = res.returncode != 0 and expect in res.stdout
        missed += 0 if caught else 1
        print(f"{'CAUGHT' if caught else 'MISSED'}  {i:02d} {name}  [{cmd[0]}]")
        if not caught:
            if res.returncode != 0:
                print(f"  failed, but not on the words this fault targets ({expect!r})")
            print(res.stdout)
    failed = 0
    for i, (name, setup, cmd) in enumerate(CONTROLS, 1):
        scratch = base / f"control-{i:02d}"
        shutil.copytree(fixture, scratch)
        try:
            setup(scratch)
            res = run(scratch, cmd[0], *cmd[1:])
            ok = res.returncode == 0
        except AssertionError as e:
            ok, res = False, None
            print(f"  assertion: {e}")
        failed += 0 if ok else 1
        print(f"{'PASSES' if ok else 'BLOCKED'} control {i:02d} {name}  [{cmd[0]}]")
        if not ok and res is not None:
            print(res.stdout)
    locked = False
    if not missed and not failed:
        locked = write_lock(HERE, len(FAULTS), len(CONTROLS), fixture)
        if locked:
            print("checks/faults.lock.json written: every check is bound to this passing run")
    print(f"\n{len(FAULTS) - missed}/{len(FAULTS)} faults caught; {len(CONTROLS) - failed}/{len(CONTROLS)} "
          f"positive controls pass" + ("" if not (missed or failed) else " — the checks are not trustworthy yet"))
    shutil.rmtree(base, ignore_errors=True)
    return 0 if not missed and not failed and locked else 1


if __name__ == "__main__":
    sys.exit(main())
