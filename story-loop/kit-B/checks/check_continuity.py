#!/usr/bin/env python3
"""The story bible and the manuscript agree. Every name and invented term the bible lists appears in the
draft spelled as the bible spells it; nothing in the draft is a near-miss of a bible term (one character
away, which is how a name drifts across a revision); and no bible entry goes unused, because an entry the
story never uses is either a cut the bible did not hear about or a detail the writer forgot to place.
Bypass attempts this check refuses: a character renamed halfway through; an invented term respelled; a
bible entry left behind after a scene was cut. A plural is never a drift, and a word the bible's
"Word that is not a drift" table declares is left alone — Mara and Mars in one story, or two
characters called Mara and Mira, are things writers do and a program cannot tell them from a typo.
What it does not check: whether the rules of the conceit make sense, or whether the timeline is possible;
and it reads only the Names and Invented-terms tables, so the bible's Rules, Timeline, and Physical-details
sections are prose no program parses. A name the architect never listed is invisible to drift-detection, so
the check prints the capitalised words the bible does not know about, as a note for the orchestrator to act on.
That is the depth critic's question and the adversarial critic's sweep.
Usage: check_continuity.py"""
import re
import sys
from common import COMMON_WORDS, ROOT, Report, cell, current_draft, proper_nouns, register_rows, split_front_matter


def plural_of(term, word):
    """True when `word` is the term's plural or the term is the word's: the commonest thing done to a noun."""
    a, b = term.lower(), word.lower()
    return b in (a + "s", a + "es") or a in (b + "s", b + "es")


def near_miss(term, word):
    """True when `word` is one edit from `term` and not equal — a substitution, an insertion, a deletion, or a
    transposition of two adjacent letters: the four shapes a name takes when it drifts across a revision."""
    if word.lower() == term.lower() or abs(len(word) - len(term)) > 1 or len(term) < 4:
        return False
    if plural_of(term, word):
        return False
    a, b = term.lower(), word.lower()
    if a[0] != b[0]:
        return False
    if len(a) == len(b):
        diff = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
        if len(diff) == 1:
            return True
        if len(diff) == 2 and diff[1] == diff[0] + 1:          # a transposition, the commonest way a name drifts
            i = diff[0]
            return a[i] == b[i + 1] and a[i + 1] == b[i]
        return False
    short, long = (a, b) if len(a) < len(b) else (b, a)
    for i in range(len(long)):
        if long[:i] + long[i + 1:] == short:
            return True
    return False


def unlisted_note(rep, path, body, proper, known):
    """Capitalised words the bible does not list, which are therefore outside drift-detection. This runs
    before every early return: an empty bible is exactly the state in which a name nobody declared is most
    likely, and returning early on it switched off the one safeguard the design promises for that case.
    COMMON_WORDS is filtered so that first-person narration does not report 'I' as an undeclared name."""
    unlisted = sorted({w for w in proper
                       if w.lower() not in known and w.lower() not in COMMON_WORDS
                       and len(re.findall(r"\b" + re.escape(w) + r"\b", body)) >= 3})
    if unlisted:
        rep.note("capitalised words used three times or more that the bible does not list, and which are "
                 "therefore outside drift-detection: " + ", ".join(unlisted[:8]))


def main(root=ROOT, milestone=None):
    rep = Report("continuity")
    path = current_draft(root)
    if not path:
        rep.note("no draft yet; nothing to hold the bible to")
        return rep.finish()
    _, body = split_front_matter(path.read_text(encoding="utf-8"))
    all_words = set(re.findall(r"[A-Za-z][A-Za-z'-]+", body))
    proper = proper_nouns(body)
    terms = []
    for table, key in (("Names", "Name"), ("Invented terms", "Term")):
        rows, problems = register_rows(root / "story" / "BIBLE.md", key)
        for pr in problems:
            rep.fail(pr)
        for r in rows:
            t = cell(r, key)
            if t:
                terms.append((t, key, r["_line"]))
    allowed = set()
    rows, problems = register_rows(root / "story" / "BIBLE.md", "Word that is not a drift",
                                   others=("Why both are meant to be there",))
    for pr in problems:
        rep.fail(pr)
    if not problems:
        for r in rows:
            w = cell(r, "Word that is not a drift")
            if w and not cell(r, "Why both are meant to be there"):
                rep.fail(f"BIBLE.md line {r['_line']}: {w!r} is declared not a drift with no reason given. "
                         f"This table switches off the check that catches a renamed character, so a row "
                         f"without a reason is an off-switch nobody has to justify — the Motifs table asks "
                         f"the same of a declared motif. Say why both words are meant to be there")
        allowed = {cell(r, "Word that is not a drift").lower() for r in rows
                   if cell(r, "Word that is not a drift")}
        if allowed:
            rep.note("words the bible says are not drift: " + ", ".join(sorted(allowed)))
    unlisted_note(rep, path, body, proper, {p.lower() for tm, _, _ in terms for p in tm.split()})
    if not terms:
        rep.note("the bible lists no names or terms yet, so drift-detection is entirely off: nothing in "
                 "the draft can be compared to a spelling the bible does not have. The capitalised words "
                 "above are the whole cast as far as this check can see")
        return rep.finish()
    known_terms = {p.lower() for tm, _, _ in terms for p in tm.split()}
    for term, kind, line in terms:
        pattern = r"\b" + re.escape(term) + r"\b"
        if not re.search(pattern, body):
            rep.fail(f"BIBLE.md line {line}: {kind.lower()} {term!r} never appears in {path.name}; either "
                     f"the story cut it and the bible has not heard, or the writer forgot to place it")
            continue
        head = term.split()[0]
        # A capitalised term is only ever confused with another capitalised word used as a name; a
        # lower-case term is never confused with ordinary English. Without both rules, a character
        # called Wren collides with the word "when".
        candidates = (proper if head[:1].isupper() else
                      {w for w in all_words if w.lower() not in COMMON_WORDS and w[:1].islower()})
        for w in candidates:
            if w.lower() in allowed:
                continue
            # Two bible entries one character apart — Mara and Mira, a pair of siblings — are a thing a
            # writer does on purpose, and both are declared here already. Reading one as a drift of the
            # other made the bible fight itself and needed a not-a-drift row in each direction.
            if w.lower() in known_terms and w.lower() != term.lower():
                continue
            if near_miss(head, w):
                rep.fail(f"{path.name}: {w!r} is one character from the bible's {term!r} — a name that "
                         f"drifted, or a term respelled. If the two words are both meant to be there, put "
                         f"{w!r} in the bible's \"Word that is not a drift\" table and this check will leave "
                         f"it alone; the bible's spelling is otherwise the story's")
    rep.note(f"{len(terms)} bible entries held against {path.name}")
    return rep.finish()


if __name__ == "__main__":
    ms = int(sys.argv[sys.argv.index("--milestone") + 1]) if "--milestone" in sys.argv else None
    sys.exit(main(milestone=ms))
