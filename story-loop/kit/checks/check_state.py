#!/usr/bin/env python3
"""STATE.md is a sound register: the milestone line parses, every cap has a name and a number, no Used is
blank from M1 on, no cap has been overspent, the process signals are
readable and the revert counter has not reached three, and the live table matches the caps the human accepted at
intake (checks/caps.approved.json) row for row, with no value above the accepted one.
Bypass attempts this check refuses: a cap raised above the accepted value; a spent cap drawn on again, or rescued by raising it; a Value that is not a number; a cap row deleted, renamed, or added without a new acceptance;
a milestone line advanced past a gate that has no sign-off.
What it does not check: that the Used figures are honest. They are the orchestrator's estimate, labelled
one, and the harness's own spending limit is the wall. It also cannot check who wrote caps.approved.json:
this kit does not depend on git, so the human's protection there is that they commit it themselves at
intake and can read `git log` at any gate where the project is in git.
Usage: check_state.py [--milestone N] | --accept-caps INTAKE|DEC-NNN"""
import json
import re
import sys
from pathlib import Path
from common import ROOT, Report, cell, read_json, read_text, register_rows

ACCEPTED = "checks/caps.approved.json"


def parse_number(s):
    s = (s or "").strip().replace(",", "")
    m = re.fullmatch(r"(\d+(?:\.\d+)?)\s*([KMkm]?)", s)
    if not m:
        return None
    return float(m.group(1)) * {"": 1, "k": 1e3, "K": 1e3, "m": 1e6, "M": 1e6}[m.group(2)]


def gate_signed(root, n):
    return bool(re.search(rf"^###\s+G{n}\b", read_text(Path(root) / "DECISIONS.md"), re.M))


def caps_row(root, dec):
    """The human's own caps decision, or None. A cap is the only hard limit on what this loop spends, and
    an agent may never raise one — so the row that re-opens the budget is checked the way check_gate.py
    checks a gate-amend row and plant_faults.py checks a fault-suite row: it has to exist, be of the right
    type, and be the human's. Without this, one string on a command line raises every cap at once."""
    rows, problems = register_rows(Path(root) / "DECISIONS.md", "ID", others=("Author", "Type"))
    if problems:
        return None
    for r in rows:
        if cell(r, "ID") == dec and cell(r, "Author").lower() == "human" and cell(r, "Type").lower() == "caps":
            return r
    return None


def accept_caps(root, accepted):
    p = Path(root) / ACCEPTED
    if accepted == "INTAKE" and p.exists():
        print(f"  FAIL: {ACCEPTED} exists; INTAKE is the first acceptance only — a later change is a caps "
              f"decision the human writes, then --accept-caps DEC-NNN")
        return 1
    if accepted != "INTAKE":
        if not re.fullmatch(r"DEC-\d+", accepted):
            print(f"  FAIL: {accepted!r} is not INTAKE or a decision row ID; a re-acceptance names the "
                  f"human's caps row, as `--accept-caps DEC-012`")
            return 1
        if caps_row(root, accepted) is None:
            print(f"  FAIL: DECISIONS.md has no row {accepted} with Author `human` and Type `caps`. The "
                  f"caps are the human's only hard limit on what this loop spends and an agent may never "
                  f"raise one, so re-accepting them needs their own row: `make decide TYPE=caps` prints "
                  f"it, the human writes it, and then this command names it")
            return 1
    rows, problems = register_rows(Path(root) / "STATE.md", "Cap")
    for pr in problems:
        print(f"  FAIL: {pr}")
    if problems:
        return 1
    entries = []
    for r in rows:
        name, val = cell(r, "Cap"), cell(r, "Value")
        if not name or parse_number(val) is None:
            print(f"  FAIL: STATE.md line {r['_line']}: a cap with no name or a Value that is not a "
                  f"number ({val!r}); fix the table before accepting")
            return 1
        entries.append({"name": name, "value": val})
    p.write_text(json.dumps({"accepted": accepted, "caps": entries}, indent=1) + "\n", encoding="utf-8")
    print(f"caps accepted under {accepted}: {len(entries)} caps written to {ACCEPTED}")
    print("The human now commits this file together with BRIEF.md (make intake prints the command).")
    return 0


def main(root=ROOT, milestone=None, complete=False):
    rep = Report("state")
    state = Path(root) / "STATE.md"
    m = re.search(r"\*\*Milestone:\*\*\s*M(\d)", read_text(state))
    if not m:
        rep.fail("STATE.md has no '**Milestone:** M<n>' line; every check that keys on the milestone reads it here")
        return rep.finish()
    declared = int(m.group(1))
    if milestone is not None and milestone > declared:
        rep.fail(f"asked for milestone {milestone}, but STATE.md says M{declared}; the gate skill is the "
                 f"only thing that advances this line")
    for n in range(0, declared):
        if not gate_signed(root, n):
            rep.fail(f"STATE.md says M{declared}, but DECISIONS.md carries no '### G{n}' sign-off; a "
                     f"milestone is not advanced past a gate the human has not signed")
    rows, problems = register_rows(state, "Cap")
    for pr in problems:
        rep.fail(pr)
    live = {}
    for r in rows:
        name, val, used = cell(r, "Cap"), cell(r, "Value"), cell(r, "Used")
        v = parse_number(val)
        if not name:
            rep.fail(f"STATE.md line {r['_line']}: a cap row with no name")
            continue
        if v is None:
            rep.fail(f"{name}: Value {val!r} is not a number; a cap the checks cannot read is not a cap")
            continue
        live[name] = v
        if declared >= 1 and not used:
            rep.fail(f"{name}: Used is blank; the orchestrator writes it every turn, labelled an estimate")
            continue
        u = parse_number(used)
        if u is None and used:
            rep.fail(f"{name}: Used {used!r} is not a number")
        elif u is not None and v > 0 and u > v:
            rep.fail(f"{name}: Used {used} is over the cap {val}; the loop drew on a row that was spent, "
                     f"which is the one thing a cap forbids")
        elif u is not None and v > 0 and u == v:
            rep.note(f"{name}: spent ({used} of {val}); nothing further may be drawn on this row without the "
                     f"human's caps decision, and the next draw is a failing check")
    signals, sig_problems = register_rows(state, "Signal", others=("Value", "Written by"))
    if declared >= 3:
        for pr in sig_problems:
            rep.fail(pr)
        by_name = {cell(r, "Signal").lower(): cell(r, "Value") for r in signals}
        reverts = next((v for k, v in by_name.items() if k.startswith("reverted revisions")), None)
        if reverts is None:
            rep.fail("STATE.md's process signals carry no 'Reverted revisions in a row' row; the revert rule "
                     "in LOOP_DESIGN.md section 9 has no reader without it")
        else:
            n = parse_number(reverts)
            if n is None:
                rep.fail(f"the reverted-revisions signal reads {reverts!r}, which is not a number")
            elif n >= 3:
                rep.fail(f"{int(n)} revisions in a row have been reverted; the story is being sanded - stop "
                         f"and write to INBOX.md, as LOOP_DESIGN.md section 9 says")
    p = Path(root) / ACCEPTED
    if not p.exists():
        if declared >= 1:
            rep.fail(f"{ACCEPTED} missing: the caps were never accepted (at the end of intake, "
                     f"check_state.py --accept-caps INTAKE, committed by the human with BRIEF.md)")
    else:
        acc = read_json(p)
        approved = {e["name"]: parse_number(e["value"]) for e in acc.get("caps", [])}
        for name, v in live.items():
            if name not in approved:
                rep.fail(f"{name}: a cap not in the accepted set; a new cap is the human's caps decision "
                         f"and a re-acceptance under it")
            elif approved[name] is not None and v > approved[name]:
                rep.fail(f"{name}: Value {v:g} is above the accepted {approved[name]:g}; an agent may lower "
                         f"a cap, never raise it")
        for name in approved:
            if name not in live:
                rep.fail(f"the accepted cap {name!r} is gone from STATE.md; dropping a cap is the human's "
                         f"caps decision and a re-acceptance under it")
        rep.note(f"{len(live)} caps, accepted under {acc.get('accepted')}")
    return rep.finish()


if __name__ == "__main__":
    if "--accept-caps" in sys.argv:
        sys.exit(accept_caps(ROOT, sys.argv[sys.argv.index("--accept-caps") + 1]))
    ms = int(sys.argv[sys.argv.index("--milestone") + 1]) if "--milestone" in sys.argv else None
    sys.exit(main(milestone=ms, complete="--complete" in sys.argv))
