#!/usr/bin/env python3
"""M3: assemble reviews/comparisons/round-NN.json (or round-NN-revision.json) from saved judge replies.
Usage: assemble_round.py <kit> <round NN> <draft-NN> <draft_sha256> <planted> <cal_pair_file> <cal_sha256> <replies-dir> [--revision previous-draft [--signed signed-draft]]
With --signed, the replies whose manifest exemplar is the signed draft go into the record's baseline_signed block (RECORD_SHAPE.md),
the pairing against the draft the human signed at G3 that check_comparisons.py requires once a G3 sign-off exists; the replies whose
exemplar is the previous draft stay in pairs. Each verdict's exemplar is read from the manifest, never from the flag.
Reply files are named <label>--<judge>.md (e.g. exhalation-AB--craft-critic-a.md), parsed with parse_verdict.py. The
calibration verdicts (labels cal-AB, cal-BA) decide "caught" per judge: the true draft is A in cal-AB and B in cal-BA."""
import sys, json, subprocess
from pathlib import Path
kit, rnd, draft, dsha, planted, calfile, calsha, rdir = sys.argv[1:9]
revision = sys.argv[sys.argv.index("--revision") + 1] if "--revision" in sys.argv else None
signed = sys.argv[sys.argv.index("--signed") + 1] if "--signed" in sys.argv else None
if signed and not revision: sys.exit("--signed needs --revision")
R = Path(rdir); pv = Path(__file__).with_name("parse_verdict.py")
manifest = {m["label"]: m for m in json.loads((R / "manifest.json").read_text(encoding="utf-8"))}
pairs, base_pairs, verdicts = [], [], {}
for f in sorted(R.glob("*--*.md")):
    label, judge = f.stem.split("--")
    m = manifest[label]
    if label.startswith("cal-"):
        r = subprocess.run([sys.executable, str(pv), str(f), "calibration", m["dimension"], m["order"], judge], capture_output=True, text=True)
        if r.returncode: sys.exit(r.stdout + r.stderr)
        e = json.loads(r.stdout); won = (m["order"] == "AB" and e["choice"] == "A") or (m["order"] == "BA" and e["choice"] == "B")
        verdicts.setdefault(judge, []).append(won); continue
    r = subprocess.run([sys.executable, str(pv), str(f), m["exemplar"], m["dimension"], m["order"], judge], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stdout + r.stderr)
    e = json.loads(r.stdout)
    if revision and "lost" not in e: sys.exit(f"{f}: revision verdict without LOST")
    if revision and m["exemplar"] not in (revision, signed): sys.exit(f"{f}: a revision round reply paired against {m['exemplar']}, which is neither the previous draft nor the signed one")
    (base_pairs if signed and m["exemplar"] == signed else pairs).append(e)
cal = {j: ("caught" if len(v) == 2 and all(v) else "missed") for j, v in verdicts.items()}
rec = {"round": int(rnd), "draft": draft, "draft_sha256": dsha,
       "calibration": {"planted": planted, "pair_file": Path(calfile).name, "pair_sha256": calsha, "verdicts": cal, "passed": bool(cal) and all(x == "caught" for x in cal.values())},
       "pairs": pairs}
if revision: rec["previous"] = revision
if signed:
    if not base_pairs: sys.exit(f"--signed {signed} given and no reply is paired against it")
    rec["baseline_signed"] = {"draft": signed, "pairs": base_pairs}
out = Path(kit, "reviews/comparisons", f"round-{int(rnd):02d}{'-revision' if revision else ''}.json")
out.write_text(json.dumps(rec, indent=1, ensure_ascii=False), encoding="utf-8")
print(out, "pairs:", len(pairs), "baseline_signed pairs:", len(base_pairs), "calibration:", cal)
