#!/usr/bin/env python3
"""Prose measures, printed rather than graded. Adverb and filter-word density, sentence-length variation,
runs of paragraphs opening the same way, over-long paragraphs, and distinctive words used too often.
Everything is printed every run; only the extremes in checks/thresholds.json fail, because prose written
to lower a tic count is worse prose and a check that grades style teaches an agent to write for the check.
Repetition is the one measure that cannot be judged from the outside — a word repeated eleven times is a
tic or a motif and the count cannot tell — so a repeated word is failed only when the bible's Motifs table
has not declared it. That turns an unjudgeable measure into a declaration the writer has to make.
Bypass attempts this check refuses: a draft where every sentence is the same length; adverb or filter-word
density past the extreme; a paragraph longer than the maximum; the same opening word four paragraphs running; a distinctive word repeated past the limit and not declared
as a motif in the bible; a motif declared with no reason given. Names and invented terms from the bible are
not counted as repeats at all: a third-person story says its protagonist's name, and that is not a tic.
What it does not check: whether any of these numbers means the prose is good. A story can pass every
measure and be dead on the page; that is the flow critic's finding and the human's read-aloud at G4.
Usage: check_tics.py"""
import re
import statistics
import sys
from collections import Counter
from common import (COMMON_WORDS, ROOT, Report, cell, current_draft, register_rows, sentences,
                    split_front_matter, thresholds, word_count)

FILTERS = ["seemed to", "seemed", "felt", "saw that", "heard", "noticed", "realized", "realised",
           "watched as", "began to", "started to", "tried to", "could see", "could hear", "could feel",
           "somehow", "suddenly", "found himself", "found herself", "found itself", "found themselves"]
NOT_ADVERBS = {"family", "reply", "supply", "apply", "ally", "rally", "holy", "ugly", "only", "early",
               "likely", "unlikely", "lonely", "lovely", "silly", "jolly", "daily", "weekly", "monthly",
               "yearly", "friendly", "deadly", "costly", "elderly", "orderly", "july", "italy", "belly",
               "fly", "sly", "ply", "imply", "multiply", "assembly", "anomaly", "melancholy", "chilly"}
COMMON = COMMON_WORDS


def main(root=ROOT, milestone=None):
    rep = Report("tics")
    path = current_draft(root)
    if not path:
        rep.note("no draft yet; nothing to measure")
        return rep.finish()
    th = thresholds(root)["tics"]
    _, body = split_front_matter(path.read_text(encoding="utf-8"))
    words = re.findall(r"[A-Za-z']+", body)
    n = max(len(words), 1)
    lower = [w.lower() for w in words]
    ly = [w for w in lower if w.endswith("ly") and len(w) > 4 and w not in NOT_ADVERBS]
    ly_rate = 1000 * len(ly) / n
    filt = sum(len(re.findall(r"\b" + re.escape(f) + r"\b", body, re.I)) for f in FILTERS)
    filt_rate = 1000 * filt / n
    sents = sentences(body)
    lengths = [len(re.findall(r"[A-Za-z']+", s)) for s in sents] or [0]
    stdev = statistics.pstdev(lengths) if len(lengths) > 1 else 0.0
    paras = [p for p in re.split(r"\n\s*\n", body) if p.strip()]
    para_words = [word_count(p) for p in paras]
    openers = [(re.findall(r"[A-Za-z']+", p) or [""])[0].lower() for p in paras]
    run, worst_run, worst_word = 1, 1, openers[0] if openers else ""
    for i in range(1, len(openers)):
        run = run + 1 if openers[i] == openers[i - 1] and openers[i] else 1
        if run > worst_run:
            worst_run, worst_word = run, openers[i]
    distinctive = Counter(w for w in lower if w not in COMMON and len(w) > 5)
    top = distinctive.most_common(5)

    rep.note(f"{len(sents)} sentences, mean {statistics.mean(lengths):.1f} words, spread {stdev:.1f}")
    rep.note(f"-ly adverbs {len(ly)} ({ly_rate:.1f} per 1000 words); filter words {filt} ({filt_rate:.1f} per 1000)")
    rep.note(f"{len(paras)} paragraphs, longest {max(para_words) if para_words else 0} words; "
             f"longest run of paragraphs opening on one word: {worst_run} ({worst_word!r})")


    if ly_rate > th["ly_adverbs_per_1000_max"]:
        rep.fail(f"-ly adverbs at {ly_rate:.1f} per 1000 words, over the extreme of {th['ly_adverbs_per_1000_max']}")
    if filt_rate > th["filter_words_per_1000_max"]:
        rep.fail(f"filter words at {filt_rate:.1f} per 1000 words, over the extreme of "
                 f"{th['filter_words_per_1000_max']} (the reader is being told about the seeing rather than shown it)")
    if len(lengths) > 4 and stdev < th["sentence_length_stdev_min"]:
        rep.fail(f"sentence lengths vary by {stdev:.1f} words, under the floor of {th['sentence_length_stdev_min']}; "
                 f"prose at one length has one rhythm")
    if worst_run > th["same_opener_run_max"]:
        rep.fail(f"{worst_run} paragraphs in a row open with {worst_word!r} (limit {th['same_opener_run_max']})")
    if para_words and max(para_words) > th["paragraph_words_max"]:
        rep.fail(f"a paragraph of {max(para_words)} words, over the maximum of {th['paragraph_words_max']}")
    motifs, names = set(), set()
    rows, problems = register_rows(root / "story" / "BIBLE.md", "Word", others=("Why it repeats",))
    for pr in problems:
        rep.fail(pr)
    if not problems:
        for r in rows:
            w = cell(r, "Word")
            if not w:
                continue
            if not cell(r, "Why it repeats"):
                rep.fail(f"BIBLE.md line {r['_line']}: the motif {w!r} is declared with no reason; a word you "
                         f"cannot say why you repeat is a word you are leaning on")
            motifs.add(w.lower())
        if motifs:
            rep.note("declared motifs: " + ", ".join(sorted(motifs)))
    for key in ("Name", "Term"):
        rows, problems = register_rows(root / "story" / "BIBLE.md", key)
        if not problems:
            for r in rows:
                for part in cell(r, key).split():
                    names.add(part.lower())
    if names:
        rep.note("names and terms, which repeat by necessity and are not counted: " + ", ".join(sorted(names)))
    shown = [(w, c) for w, c in distinctive.most_common() if w not in names][:5]
    rep.note("most repeated distinctive words: " + (", ".join(f"{w}\u00d7{c}" for w, c in shown) or "none"))
    for w, c in distinctive.most_common():          # every word over the limit, not a fixed window: a
        if c <= th["distinctive_word_repeats_max"]:  # declared motif must not blind the check to the next word
            break
        if w in names or w in motifs:
            continue
        rep.fail(f"{w!r} appears {c} times (limit {th['distinctive_word_repeats_max']}); either it is a "
                 f"tic the reader will start to see, or it is a motif — declare it in BIBLE.md's Motifs "
                 f"table with the reason, and this check will leave it alone")
    return rep.finish()


if __name__ == "__main__":
    ms = int(sys.argv[sys.argv.index("--milestone") + 1]) if "--milestone" in sys.argv else None
    sys.exit(main(milestone=ms))
