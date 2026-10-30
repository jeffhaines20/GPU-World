#!/usr/bin/env python3
"""M3: build every anonymized pair file for one comparison round and print the manifest the orchestrator spawns judges
from. Usage: build_round.py <kit> <draft-NN> <round NN> <cal-pair-file> <outdir> <plan: exemplar:dimension,...>
(a plan entry draft-NN:dimension pairs the current draft against that older draft, for the revision round)
Writes, under <outdir>: cal-AB-A.txt/-B.txt and cal-BA-A.txt/-B.txt (the true draft against the weakened copy in both
orders) and, per plan entry, <exemplar>-AB-{A,B}.txt and <exemplar>-BA-{A,B}.txt (the draft first in AB, the exemplar
first in BA). Prints one manifest line per verdict needed: label, exemplar, dimension, order, A path, B path, A words,
B words; the judges (a and b) each take every line. Uses orchestrator/make_pair.py for the stripping."""
import sys, subprocess, json
from pathlib import Path
kit, draft, rnd, cal, out, plan = sys.argv[1:]
K = Path(kit); O = Path(out); O.mkdir(parents=True, exist_ok=True)
dpath = K / "story/drafts" / f"{draft}.md"
mp = Path(__file__).with_name("make_pair.py")
def pair(a, b, label):
    r = subprocess.run([sys.executable, str(mp), str(a), str(b), str(O), label], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr or r.stdout)
    wa = len((O / f"{label}-A.txt").read_text(encoding="utf-8").split()); wb = len((O / f"{label}-B.txt").read_text(encoding="utf-8").split())
    return wa, wb
rows = []
for order, (a, b) in (("AB", (dpath, Path(cal))), ("BA", (Path(cal), dpath))):
    wa, wb = pair(a, b, f"cal-{order}")
    rows.append({"label": f"cal-{order}", "exemplar": "calibration", "dimension": "sentences", "order": order,
                 "A": str(O / f"cal-{order}-A.txt"), "B": str(O / f"cal-{order}-B.txt"), "wa": wa, "wb": wb})
for item in plan.split(","):
    ex, dim = item.split(":")
    # a plan entry named draft-NN is a revision pair: the older draft stands where the exemplar would
    epath = (K / "story/drafts" / f"{ex}.md") if ex.startswith("draft-") else (K / "design/exemplars" / f"{ex}.txt")
    if not epath.exists(): sys.exit(f"no exemplar text {epath}")
    stem = f"{ex}-{dim}" if ex.startswith("draft-") else ex   # a revision pairs one older draft on several dimensions
    for order, (a, b) in (("AB", (dpath, epath)), ("BA", (epath, dpath))):
        wa, wb = pair(a, b, f"{stem}-{order}")
        rows.append({"label": f"{stem}-{order}", "exemplar": ex, "dimension": dim, "order": order,
                     "A": str(O / f"{stem}-{order}-A.txt"), "B": str(O / f"{stem}-{order}-B.txt"), "wa": wa, "wb": wb})
(O / "manifest.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
for r in rows: print(f"{r['label']:34s} {r['dimension']:10s} A={r['wa']:5d}w  B={r['wb']:5d}w")
print(f"{len(rows)} pair files; x2 judges = {2*len(rows)} verdicts; manifest {O/'manifest.json'}")
