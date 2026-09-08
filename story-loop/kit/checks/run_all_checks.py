#!/usr/bin/env python3
"""Runs every check in order and prints one line per check. With no --milestone it reads the milestone
from STATE.md, so that the bare command in the handoff prompt is the right command on day one. Refuses to report success when the fault suite
has not been re-run since a check changed: checks/faults.lock.json carries a hash of every check file
from the last passing run of plant_faults.py, and a check edited without re-running the suite is a check
nobody has seen fail.
Usage: run_all_checks.py [--milestone N] [--complete] [--gate N | --pregate N]
  --gate N     everything a gate rests on, including the human's sign-off. Run after they sign.
  --pregate N  the same schedule with the sign-off check left out, for the run before they sign — the
               sign-off cannot exist yet and no agent may write one, so --gate N cannot pass there."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import milestone as milestone_from_state

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
PY = sys.executable
ALWAYS = ["check_state.py", "check_claims.py", "check_reviews.py", "check_manuscript.py"]
FROM_M3 = ["check_tics.py", "check_continuity.py", "check_comparisons.py"]
# Only the checks that actually branch on the flag are given it. A check that takes a flag it never reads
# is a promise its own usage line does not keep, and the next person to change it cannot tell whether the
# flag matters. check_tics and check_continuity measure the same things at every milestone; check_state
# and check_comparisons key on the milestone but not on whether the draft is called complete.
TAKES_MILESTONE = {"check_state.py", "check_manuscript.py", "check_comparisons.py"}
TAKES_COMPLETE = {"check_manuscript.py"}
NOT_CHECKS = {"faults.lock.json", "caps.approved.json", "gates.seen.json"}   # records the loop writes, not checks



def freshness():
    lock = HERE / "faults.lock.json"
    if not lock.exists():
        return ["checks/faults.lock.json missing: run python3 checks/plant_faults.py, which writes it when "
                "every planted fault is caught"]
    data = json.loads(lock.read_text(encoding="utf-8"))
    problems = []
    for p in sorted(HERE.iterdir()):
        if not p.is_file() or p.name in NOT_CHECKS:
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()
        if data.get("checks", {}).get(p.name) != h:
            problems.append(f"{p.name} has changed since the fault suite last passed; every changed check "
                            f"ships with a planted fault it catches and a control it passes — re-run "
                            f"python3 checks/plant_faults.py and commit the lock with the change")
    for name in data.get("checks", {}):
        if not (HERE / name).exists():
            problems.append(f"{name} is in the lock and gone from checks/")
    return problems


def flags(script, ms, complete):
    return (([] if ms is None or script not in TAKES_MILESTONE else ["--milestone", str(ms)])
            + (["--complete"] if complete and script in TAKES_COMPLETE else []))


def schedule(ms, complete, gate, pregate=False):
    scripts = [(s, flags(s, ms, complete)) for s in ALWAYS]
    if ms is not None and ms >= 3:
        scripts += [(s, flags(s, ms, complete)) for s in FROM_M3]
    scripts.append(("check_gate.py", ["--record"]))
    if gate is not None:
        # --pregate runs everything a gate rests on EXCEPT the sign-off check, because the sign-off does
        # not exist yet and the one thing the orchestrator may never do is write it. Ordering the full
        # --gate command before the human signs made every gate unpassable: the check failed, the skill
        # said fix it first, and the only fix was forbidden.
        if not pregate:
            scripts.append(("check_gate.py", ["--gate", str(gate)]))
        scripts[scripts.index(("check_reviews.py", []))] = ("check_reviews.py", ["--gate", str(gate)])
        cmp_flags = flags("check_comparisons.py", ms, complete)
        if ("check_comparisons.py", cmp_flags) in scripts:
            scripts[scripts.index(("check_comparisons.py", cmp_flags))] = (
                "check_comparisons.py", cmp_flags + ["--gate", str(gate)])
    return scripts


def main():
    given = int(sys.argv[sys.argv.index("--milestone") + 1]) if "--milestone" in sys.argv else None
    ms = given if given is not None else milestone_from_state()
    gate = int(sys.argv[sys.argv.index("--gate") + 1]) if "--gate" in sys.argv else None
    pregate = "--pregate" in sys.argv
    if pregate:
        gate = int(sys.argv[sys.argv.index("--pregate") + 1])
    complete = "--complete" in sys.argv
    print(f"milestone {ms if ms is not None else 'unknown: STATE.md has no milestone line'}"
          f"{'' if given is not None else ' (from STATE.md)'}")
    failed = []
    print("== fault suite freshness")
    stale = freshness()
    for pr in stale:
        print(f"  FAIL: {pr}")
    if stale:
        failed.append("faults.lock")
    else:
        lock = json.loads((HERE / "faults.lock.json").read_text(encoding="utf-8"))
        print(f"  every check matches the suite's last passing run: {lock.get('faults')} faults, "
              f"{lock.get('controls')} controls")
    for script, args in schedule(ms, complete, gate, pregate):
        print(f"== {script} {' '.join(args)}".rstrip())
        r = subprocess.run([PY, str(HERE / script)] + args, cwd=ROOT, capture_output=True, text=True)
        print(r.stdout.rstrip())
        if r.stderr.strip():
            print(r.stderr.rstrip())
        if r.returncode != 0:
            failed.append(script)
    print()
    print("ALL CHECKS PASSED" if not failed else f"CHECKS FAILED: {', '.join(sorted(set(failed)))}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
