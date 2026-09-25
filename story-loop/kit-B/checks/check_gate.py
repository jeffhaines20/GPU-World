#!/usr/bin/env python3
"""The gate sign-off exists and is a human's paragraph: a '### G<n>' section in DECISIONS.md with at least
the words and sentences the threshold file asks for, and not one of the phrases an agent reaches for when
it writes a sign-off on the human's behalf. With --record (run every turn) every sign-off that ever
existed is still present and unchanged, held against a copy taken when it was first seen, so a past gate
cannot be quietly reworded once the loop has moved on.
Bypass attempts this check refuses: a missing or one-line sign-off; a sign-off in the agent's voice; a
past gate's paragraph shortened, reworded, or deleted after the fact, unless the human says in a
decision row of type gate-amend that they changed their own words — and each such row authorises exactly one
change and is then spent, so a gate amended once is not left unguarded afterwards.
What it does not check: that the human, rather than the orchestrator, typed the words. This kit does not
depend on git, so that rests on the orchestrator's instructions (rule 8) and on the human reading their
own paragraph back at the next gate, which the gate skill asks them to do.
Usage: check_gate.py --gate N | --record"""
import json
import re
import sys
from pathlib import Path
from common import ROOT, Report, cell, read_text, register_rows, sha256_text, thresholds


def amend_rows(root, n):
    """The IDs of human gate-amend rows naming this gate: the human's own statement that they, not an agent,
    changed their own paragraph. Each row authorises one change and is then spent, so a gate that was
    legitimately amended once does not have its tamper detection switched off for good."""
    rows, problems = register_rows(Path(root) / "DECISIONS.md", "ID", others=("Author", "Type", "Decision"))
    if problems:
        return []
    return [cell(r, "ID") for r in rows
            if cell(r, "Author").lower() == "human" and cell(r, "Type").lower() == "gate-amend"
            and re.search(rf"\bG{n}\b", cell(r, "Decision") + " " + cell(r, "Why"))]

RECORD = "checks/gates.seen.json"
AGENT_VOICE = [r"\bthis milestone (?:is|was) (?:excellent|complete)\b", r"\bshould (?:go through|proceed) "
               r"(?:immediately|without)\b", r"\bas the orchestrator\b", r"\bI have reviewed the\b",
               r"\bmeets all (?:the )?criteria\b", r"\bno (?:further )?changes (?:are )?(?:required|needed)\b"]


def sections(text):
    out = {}
    for m in re.finditer(r"^###\s+G(\d)\b[^\n]*\n(.*?)(?=^###\s+G\d\b|\Z)", text, re.M | re.S):
        out[int(m.group(1))] = m.group(2).strip()
    return out


def main(root=ROOT, gate=None, record=False):
    rep = Report("gate-record" if record else f"gate-{gate}")
    text = read_text(Path(root) / "DECISIONS.md")
    secs = sections(text)
    th = thresholds(root)["gate"]
    if record:
        p = Path(root) / RECORD
        raw = json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}
        seen = {k: v for k, v in raw.items() if k != "_spent"}
        spent = set(raw.get("_spent", []))
        amended = []
        for n, body in sorted(secs.items()):
            h = sha256_text("\n".join(l.rstrip() for l in body.splitlines() if l.strip()))
            if str(n) not in seen:
                seen[str(n)] = h
            elif seen[str(n)] != h:
                unspent = [r for r in amend_rows(root, n) if r not in spent]
                if unspent:
                    seen[str(n)] = h          # the human said, in their own row, that they changed their own words
                    spent.add(unspent[0])     # and that row is now spent: the next change needs a new one
                    # Held back until the write succeeds. The write runs only when nothing failed, so a run
                    # in which another gate failed persisted nothing while still printing that this row was
                    # spent — a note describing a state that was not saved, identical on the next run.
                    amended.append(f"the G{n} sign-off was amended by the human under {unspent[0]}; the record "
                                   f"now holds the new paragraph, and {unspent[0]} is spent")
                else:
                    rep.fail(f"the G{n} sign-off is not the paragraph first recorded (lines lost, added, or "
                             f"reworded). If an agent changed it, restore it. If you are the human and you "
                             f"meant to change your own words, add a decision row of type gate-amend naming "
                             f"G{n} (make decide TYPE=gate-amend) and this check will re-seal the record.")
        for n in sorted(k for k in seen if k != "_spent"):
            if int(n) not in secs:
                rep.fail(f"the G{n} sign-off, once written, is gone from DECISIONS.md")
        if not rep.problems:
            seen["_spent"] = sorted(spent)
            p.write_text(json.dumps(seen, indent=1, sort_keys=True) + "\n", encoding="utf-8")
            for note in amended:
                rep.note(note)
        elif amended:
            rep.note(f"{len(amended)} amendment(s) were NOT recorded, because this run failed and the "
                     f"record is only rewritten by a clean run. Fix the failures above and run again; the "
                     f"gate-amend row(s) are not spent yet")
        rep.note(f"{len(secs)} gate sign-off(s) on record" if secs else "no gate signed yet")
        return rep.finish()
    if gate not in secs:
        rep.fail(f"DECISIONS.md has no '### G{gate}' sign-off; the human writes it themselves "
                 f"(make gate N={gate} prints how), and no agent writes it for them")
        return rep.finish()
    body = secs[gate]
    words = len(body.split())
    sents = len([s for s in re.split(r"(?<=[.!?])\s+", body) if s.strip()])
    if words < th["min_words"]:
        rep.fail(f"the G{gate} sign-off is {words} words; the human writes three to five sentences about "
                 f"what they saw, at least {th['min_words']} words")
    if sents < th["min_sentences"]:
        rep.fail(f"the G{gate} sign-off is {sents} sentence(s); at least {th['min_sentences']} are asked for")
    for pat in AGENT_VOICE:
        if re.search(pat, body, re.I):
            rep.fail(f"the G{gate} sign-off contains {re.search(pat, body, re.I).group(0)!r}, which is how an "
                     f"agent writes a sign-off; this paragraph is the human's or it is nothing")
            break
    rep.note(f"G{gate}: {words} words, {sents} sentences")
    return rep.finish()


if __name__ == "__main__":
    if "--record" in sys.argv:
        sys.exit(main(record=True))
    g = int(sys.argv[sys.argv.index("--gate") + 1]) if "--gate" in sys.argv else 0
    sys.exit(main(gate=g))
