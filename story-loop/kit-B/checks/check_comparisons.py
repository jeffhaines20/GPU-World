#!/usr/bin/env python3
"""The blind comparisons are admissible evidence. A round is a file reviews/comparisons/round-NN.json in
the shape reviews/comparisons/RECORD_SHAPE.md gives. This check holds it to that shape: the round names
the draft it judged and its hash; every pair was judged in both orders; the calibration names a pair file
that exists, unchanged, and every judge that voted appears there as having caught the planted defect; and
at a gate the round covers enough different exemplars, enough of them against supplied text, wins enough
pairings outright, and is not mostly order-disagreements. At a gate a revision round
(round-NN-revision.json) must also exist for the current draft, judged against the draft before it, every
verdict carrying what the newer draft lost.
Bypass attempts this check refuses: a round with no calibration, an empty verdicts list, a judge that
voted and was never calibrated, or a calibration whose pair file is missing or altered; a pair judged in
one order only; a gate met on four dimensions against one exemplar, or on comparisons made only from
memory; a gate met on order-disagreements counted as wins; a gate with no draft-against-draft round; a
losing round re-run until it wins, since every round judged on the current draft must meet the bar and the
count is printed. A round whose calibration failed is already refused, so a round re-run because its judges
were not calibrated is not the same thing as a re-roll.
What it does not check: whether the judges have taste; whether a judge was really given nothing but the
two texts (that is the fresh context and CLAUDE.md rule 2, not a check); or whether the verdicts were
made at all rather than typed. Calibration catches a judge that cannot tell a flattened ending from the
real one; it does not catch a judge whose preferences are merely ordinary, and nothing here can. That is
what the human's reading at G3 and the read-aloud at G4 are for.
Usage: check_comparisons.py [--milestone N] [--gate N]"""
import json
import re
import sys
from pathlib import Path
from common import (ROOT, Report, cell, current_draft, drafts, read_json, register_rows, sha256_text,
                    split_front_matter, thresholds)

WINNER = {"AB": "A", "BA": "B"}          # the loop's draft is A when it was shown first


def rounds(root, suffix=""):
    d = Path(root) / "reviews" / "comparisons"
    pat = re.compile(rf"round-(\d+){re.escape(suffix)}\.json")
    out = [(int(pat.fullmatch(p.name).group(1)), p) for p in d.glob("round-*.json")
           if pat.fullmatch(p.name)] if d.exists() else []
    return [p for _, p in sorted(out)]


def tally(pairs, rep=None, name=""):
    """(wins, ties, losses, orders-seen) over (exemplar, dimension) pairs.

    A pair is one exemplar on one dimension. Where two judges both vote on it — which §7.3 mandates and
    the record shape names (`craft-critic-a`, `craft-critic-b`) — the pair is counted once, and the two
    judges have to agree in both orders for it to be a win. A flat disagreement between two calibrated
    judges is the most informative thing a round can produce, and it is a tie, for the same reason an
    order-disagreement is: the evidence does not point one way.

    Keying only on (exemplar, dimension, order) made the last judge in the JSON array overwrite the
    first, so the same eight verdicts gave a different result depending on how the array was sorted, and
    half of them vanished without a line of output.
    """
    by_judge, orders = {}, {}
    for p in pairs:
        key = (p.get("exemplar"), p.get("dimension"))
        jkey = (key, p.get("judge"), p.get("order"))
        if jkey in by_judge and rep is not None:
            rep.fail(f"{name}: {p.get('exemplar')} on '{p.get('dimension')}' has two verdicts from "
                     f"{p.get('judge')!r} in order {p.get('order')}; one judge votes once per order")
        by_judge[jkey] = p.get("choice")
        orders.setdefault(key, set()).add(p.get("order"))
    votes = {}
    for (key, judge, order), choice in by_judge.items():
        votes.setdefault(key, {}).setdefault(judge, {})[order] = choice
    w = t = l = 0
    for key, judges in votes.items():
        verdicts = []
        for judge, picks in judges.items():
            if len(picks) < 2:
                continue
            won = [picks.get(o) == WINNER[o] for o in ("AB", "BA")]
            verdicts.append(True if all(won) else (False if not any(won) else None))
        if not verdicts:
            continue
        if all(v is True for v in verdicts):
            w += 1
        elif all(v is False for v in verdicts):
            l += 1
        else:
            t += 1                                   # judges disagreed, or one flipped on order
    return w, t, l, orders


def signed_draft(root):
    """The draft the human signed at G3, from the sign-off's own record, or None before they have.

    A revision is judged against its immediate predecessor and against this. The first pairing catches a
    revision that went backwards; only the second catches a story that has been getting one degree
    smoother, and duller, every round.
    """
    m = re.search(r"^###\s+G3\b[^\n]*\n(.*?)(?=^###\s+G|\Z)",
                  (Path(root) / "DECISIONS.md").read_text(encoding="utf-8"), re.S | re.M)
    if not m:
        return None
    at = re.search(r"\bdraft-(\d+)\b", m.group(1))
    if at:
        return f"draft-{at.group(1)}"
    ds = drafts(root)                               # the sign-off named no draft: the newest at G3 time
    return ds[0][1].stem if ds else None


def body_of(path):
    return split_front_matter(Path(path).read_text(encoding="utf-8"))[1]


def check_record(rep, root, rec, path, gate, th, expect_draft, revision=False):
    if rec.get("draft") != expect_draft.stem:
        # Between step 4 of an M3 round (which writes the next draft) and step 2 of the next one, the
        # newest exemplar round necessarily names the previous draft. Failing on that mid-round left the
        # suite red for most of every round, and CLAUDE.md rule 3 makes a failing check the next piece —
        # so the round's own normal state read as an instruction to abandon it. At a gate it is a real
        # failure: a gate rests on a round judged on the draft being signed.
        msg = (f"{path.name} judged {rec.get('draft')!r}, but the current draft is {expect_draft.stem}; "
               f"a round is evidence about the draft it read")
        if gate is not None:
            rep.fail(msg)
        else:
            rep.note(msg + " — expected between a revision and the next round's comparison")
        return
    if rec.get("draft_sha256") != sha256_text(body_of(expect_draft)):
        msg = (f"{path.name}: the draft changed since this round was judged (hash differs); re-run the "
               f"comparisons against the draft as it now is")
        rep.fail(msg) if gate is not None else rep.note(msg + " — expected mid-round. If the record was "
                                                        "written by hand, the draft_sha256 this check "
                                                        "computes is the one `make calibrate` prints")
    pairs = rec.get("pairs") or []
    if not pairs:
        rep.fail(f"{path.name}: no pairs")
        return
    voters = {p.get("judge") for p in pairs if p.get("judge")}
    if True:
        cal = rec.get("calibration") or {}
        if not cal:
            rep.fail(f"{path.name}: no calibration; judges are run on a planted-defect pair before their "
                     f"verdicts count (make calibrate)")
        else:
            verdicts = cal.get("verdicts") or {}
            if not verdicts:
                rep.fail(f"{path.name}: the calibration records no verdicts; an empty list is not a pass")
            if not cal.get("planted"):
                rep.fail(f"{path.name}: the calibration names no planted defect")
            pf = cal.get("pair_file")
            fp = Path(root) / "reviews" / "comparisons" / (pf or "")
            if not pf or not fp.exists():
                rep.fail(f"{path.name}: the calibration names no pair file that exists ({pf!r}); "
                         f"make calibrate writes it and prints its name and hash")
            elif cal.get("pair_sha256") != sha256_text(fp.read_text(encoding="utf-8")):
                rep.fail(f"{path.name}: the calibration pair {pf} has changed since the round was judged")
            missed = sorted(j for j, v in verdicts.items() if v != "caught")
            if missed:
                rep.fail(f"{path.name}: judge(s) {', '.join(missed)} did not catch the planted "
                         f"{cal.get('planted')}; their verdicts do not count this round")
            uncalibrated = sorted(v for v in voters if v not in verdicts)
            if uncalibrated:
                rep.fail(f"{path.name}: judge(s) {', '.join(uncalibrated)} voted on pairs and appear in no "
                         f"calibration verdict; every judge that votes is calibrated first")
            if cal.get("passed") is not True and not rec.get("superseded_by"):
                rep.fail(f"{path.name}: calibration is not marked passed. Rule 10 says a judge that misses "
                         f"the planted defect does not count that round, and rule 4 says nothing is "
                         f"deleted — so the way to close this round is to run another one with calibrated "
                         f"judges and add `\"superseded_by\": \"round-NN.json\"` here, naming it. The "
                         f"failed round stays on disk as the record that it happened")
    w, t, l, seen = tally(pairs, rep, path.name)
    for (ex, dim), orders in sorted(seen.items()):
        if set(orders) != {"AB", "BA"}:
            rep.fail(f"{path.name}: {ex} on '{dim}' was judged in order(s) {sorted(orders)}; every pair is "
                     f"judged both ways, because a judge that flips on order is reporting position, not quality")
    if revision:
        if len({(p.get("exemplar"), p.get("dimension")) for p in pairs}) < th["min_revision_pairs"]:
            rep.fail(f"{path.name}: a revision round of fewer than {th['min_revision_pairs']} pairs; one "
                     f"verdict is not evidence about a whole draft")
        for p in pairs:
            if not str(p.get("lost", "")).strip():
                rep.fail(f"{path.name}: a verdict with no 'lost' answer; a revision round exists to ask what "
                         f"the newer draft lost, and 'nothing lost' is an answer that must be written")
    slugs, problems = register_rows(root / "design" / "RUBRIC.md", "Dimension", others=("Slug",))
    for pr in problems:
        rep.fail(pr)
    known = {cell(r, "Slug").strip("` ").lower() for r in slugs if cell(r, "Slug")}
    if pairs and not known:
        rep.fail("design/RUBRIC.md gives no dimension slugs, so nothing here can tell one dimension from "
                 "another spelling of it. The Slug column is what a record's 'dimension' field must match; "
                 "without it two spellings of one dimension count as two dimensions and the round looks "
                 "broader than it was. Restore the column before judging a round")
    for p in pairs:                                  # 'ending' and 'The ending' are two dimensions to the
        dim = str(p.get("dimension", "")).strip()    # grouping below, and a round written with both looks
        if known and dim.lower() not in known:  # 'known' empty is failed above, not skipped       # like eight tried once instead of four tried twice
            rep.fail(f"{path.name}: the pair {p.get('exemplar')!r} names the dimension {dim!r}, which is "
                     f"not one of the rubric's slugs ({', '.join(sorted(known))}). The slug is the exact "
                     f"string design/RUBRIC.md gives each dimension; two spellings of one dimension are "
                     f"two dimensions to this check")
    for p in pairs:
        for field, why in (("evidence", "the phrase or moment in each text the judge is pointing at"),
                           ("needs", "what the weaker text would have to do to win this dimension")):
            if not str(p.get(field, "")).strip():
                rep.fail(f"{path.name}: the pair {p.get('exemplar')!r} on '{p.get('dimension')}' has no "
                         f"'{field}' — {why}. The craft critic produces five things and the record holds "
                         f"all five; a choice with no evidence is a preference, not a comparison, and "
                         f"'needs' is the one field the writer acts on")
    for p in pairs:                                  # a missing or misspelled field must not read as "supplied
        if not isinstance(p.get("from_memory"), bool):  # text": that is the number the gate rests on, and a
            rep.fail(f"{path.name}: the pair {p.get('exemplar')!r} on '{p.get('dimension')}' has no boolean "
                     f"'from_memory'; the field says whether the judge held the exemplar's text or worked "
                     f"from memory, a gate rests on how many pairs are on supplied text, and a field that is "
                     f"absent or misspelled would otherwise be counted as supplied text")
    full_pairs = len({(p["exemplar"], p["dimension"]) for p in pairs
                      if p.get("from_memory") is False})
    exemplars = len({p.get("exemplar") for p in pairs})
    rep.note(f"{path.name}: {len(seen)} pairs over {exemplars} exemplar(s), {full_pairs} on supplied text; "
             f"{w} win, {t} tie (the orders or the two judges disagreed), {l} loss")
    if gate is None or revision:
        return
    total = w + t + l
    if exemplars < th["exemplars_per_round"]:
        rep.fail(f"{path.name}: {exemplars} different exemplar(s); a gate needs {th['exemplars_per_round']}, "
                 f"and four dimensions against one story is one comparison, not four")
    if full_pairs < th["min_full_text_pairs_at_gate"]:
        rep.fail(f"{path.name}: {full_pairs} pair(s) judged against a supplied exemplar text; a gate needs "
                 f"{th['min_full_text_pairs_at_gate']}, since a comparison nobody re-read is weaker evidence")
    if total and w / total < th["min_win_share_at_gate"]:
        rep.fail(f"{path.name}: the draft wins {w} of {total} pairings outright ({w / total:.0%}), under the "
                 f"bar of {th['min_win_share_at_gate']:.0%}; a tie is an order-disagreement and is not a win")
    if total and t / total > th["max_tie_share_at_gate"]:
        rep.fail(f"{path.name}: {t} of {total} pairings are order-disagreements ({t / total:.0%}, over "
                 f"{th['max_tie_share_at_gate']:.0%}); a round this noisy is not evidence — re-run it")
    by_dim = {}
    for p in pairs:
        by_dim.setdefault(p.get("dimension"), []).append(p)
    # A dimension the draft is weak on shows up as losing against exemplar after exemplar. Against a
    # single exemplar it is one verdict, and one lost verdict is not a weakness — it is the story losing
    # to a better story on one thing, which the win share already prices in. So this rule needs the
    # dimension to have been tried against enough different exemplars to mean anything; below that the
    # loss is printed and the round is not failed for it.
    need = th["min_pairings_for_dimension_rule"]
    for dim, ps in sorted(by_dim.items()):
        if not ps or any(p.get("choice") == WINNER.get(p.get("order")) for p in ps):
            continue
        tried = len({p.get("exemplar") for p in ps})
        if tried >= need:
            rep.fail(f"{path.name}: the draft loses every pairing on '{dim}', against {tried} different "
                     f"exemplars; a dimension it loses on this consistently is the round's finding")
        else:
            rep.note(f"{path.name}: the draft lost on '{dim}', but against only {tried} exemplar(s); this "
                     f"is not failed, because a dimension has to be tried against {need} before losing "
                     f"every pairing on it means anything. If '{dim}' is the gap, put it against another "
                     f"exemplar next round rather than reading one loss as a verdict")


def main(root=ROOT, milestone=None, gate=None):
    rep = Report("comparisons")
    th = thresholds(root)["comparisons"]
    files, revfiles = rounds(root), rounds(root, "-revision")
    path = current_draft(root)
    if not files:
        if gate is not None:
            rep.fail("no comparison round in reviews/comparisons/; a gate rests on one "
                     "(reviews/comparisons/RECORD_SHAPE.md gives the shape)")
        elif milestone is not None and milestone >= 3 and path:
            rep.note("no comparison round yet; the first one is judged after the first draft")
        else:
            rep.note("no comparison round yet, which is right before M3")
        return rep.finish()
    if not path:
        rep.fail("a comparison round exists and story/drafts/ has no draft")
        return rep.finish()
    on_this_draft = []
    for f in files:
        try:
            r = read_json(f)
        except json.JSONDecodeError as e:
            rep.fail(f"{f.name}: not valid JSON ({e})")
            return rep.finish()
        if r.get("draft") == path.stem:
            on_this_draft.append((f, r))
    if not on_this_draft:
        check_record(rep, root, read_json(files[-1]), files[-1], gate, th, path)
        return rep.finish()
    if len(on_this_draft) > 1:
        rep.note(f"{len(on_this_draft)} rounds were judged on {path.stem}: "
                 f"{', '.join(f.name for f, _ in on_this_draft)}. A gate is met only if every one of them "
                 f"met the bar, so that re-running a round cannot turn a loss into a win.")
    names = {f.name for f, _ in on_this_draft}
    for f, r in on_this_draft:
        sup = r.get("superseded_by")
        if sup:
            # A round whose judges failed calibration is not evidence, and rule 4 forbids deleting it.
            # Superseding it says so on the record: the round that replaces it must exist, name this
            # draft, and have passed its own calibration — checked below like any other.
            if sup not in names:
                rep.fail(f"{f.name}: superseded_by names {sup!r}, which is not a round on {path.stem}")
            elif r.get("calibration", {}).get("passed") is True:
                rep.fail(f"{f.name}: superseded_by names {sup!r}, but this round's calibration passed; a "
                         f"round is superseded because its judges failed calibration, not because its "
                         f"result was unwelcome")
            else:
                rep.note(f"{f.name}: superseded by {sup} — its judges failed calibration, so it does not "
                         f"count toward the bar and is kept only as the record that it happened")
            continue
        check_record(rep, root, r, f, gate, th, path)
    if gate is not None and len(drafts(root)) > 1:
        if not revfiles:
            rep.fail("no revision round (reviews/comparisons/round-NN-revision.json); at a gate the draft is "
                     "also judged against the draft before it, which is what catches a story being sanded flat")
        else:
            try:
                rrec = read_json(revfiles[-1])
            except json.JSONDecodeError as e:
                rep.fail(f"{revfiles[-1].name}: not valid JSON ({e})")
                return rep.finish()
            prev = drafts(root)[-2][1].stem
            if rrec.get("previous") != prev:
                rep.fail(f"{revfiles[-1].name}: judged against {rrec.get('previous')!r}, but the draft before "
                         f"the current one is {prev}")
            # Draft N against N-1 cannot see sanding: a story flattened one degree a round beats its own
            # immediate predecessor every time. The pairing that can see it is against the draft the human
            # last signed, which is why it is required from the moment one exists. Until this, that pairing
            # lived in two sentences of prose with no field, no threshold and no check.
            signed = signed_draft(root)
            if signed:
                base = rrec.get("baseline_signed")
                if not base:
                    rep.fail(f"{revfiles[-1].name}: no 'baseline_signed'. Once the human has signed a draft "
                             f"at G3, the revision round pairs draft N against that draft as well as "
                             f"against N-1: against its immediate predecessor a story sanded a little "
                             f"flatter each round wins every time, and only the signed draft is far enough "
                             f"back for the flattening to be visible. Add the block "
                             f"(reviews/comparisons/RECORD_SHAPE.md gives the shape)")
                else:
                    if base.get("draft") != signed:
                        rep.fail(f"{revfiles[-1].name}: baseline_signed names {base.get('draft')!r}; the "
                                 f"draft the human signed at G3 is {signed}")
                    bpairs = base.get("pairs") or []
                    if len({(q.get("exemplar"), q.get("dimension")) for q in bpairs}) < th["min_revision_pairs"]:
                        rep.fail(f"{revfiles[-1].name}: baseline_signed carries fewer than "
                                 f"{th['min_revision_pairs']} pairs; one verdict is not evidence about a "
                                 f"whole draft")
                    for q in bpairs:
                        if not str(q.get("lost", "")).strip():
                            rep.fail(f"{revfiles[-1].name}: a baseline_signed verdict with no 'lost' answer; "
                                     f"this is the pairing that exists to ask what the story has lost since "
                                     f"the human last saw it, and 'nothing lost' is an answer that must be "
                                     f"written")
            check_record(rep, root, rrec, revfiles[-1], gate, th, path, revision=True)
    return rep.finish()


if __name__ == "__main__":
    ms = int(sys.argv[sys.argv.index("--milestone") + 1]) if "--milestone" in sys.argv else None
    g = int(sys.argv[sys.argv.index("--gate") + 1]) if "--gate" in sys.argv else None
    sys.exit(main(milestone=ms, gate=g))
