#!/usr/bin/env python3
"""Shared readers for every check in this kit. Two ideas carry most of the weight.

`register_rows` reads a markdown table as a register: it finds the one table whose header carries the
named column, and fails when there is no such table, when there is more than one, or when a row has lost
its table — a row after a blank line, or under a heading with no header row, which is how a row gets
hidden from a reader that only counts. A file may hold several tables; a table is one that has a header
delimiter row under its first line, and a group of rows without one is a fragment, not a table. A reader
that only counts must fail when it cannot find what it counts, because an empty result looks like a clean one.

`Report` collects failures and prints them under the check's name, so a run of the suite reads as a
list of checks rather than a wall of text.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Report:
    def __init__(self, name):
        self.name, self.problems, self.notes = name, [], []

    def fail(self, msg):
        self.problems.append(msg)

    def note(self, msg):
        self.notes.append(msg)

    def finish(self):
        for n in self.notes:
            print(f"  note: {n}")
        for p in self.problems:
            print(f"  FAIL: {p}")
        print(f"[{self.name}] {'FAILED' if self.problems else 'passed'}")
        return 1 if self.problems else 0


def read_text(path):
    p = Path(path)
    return p.read_text(encoding="utf-8") if p.exists() else ""


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def register_rows(path, key_header, others=()):
    """([rows], [problems]) — the one table in `path` whose header carries `key_header` (case-insensitive),
    as dicts keyed by the header cells with `_line` added. Fails on no such table, more than one, or a row
    outside it."""
    p = Path(path)
    if not p.exists():
        return [], [f"{p.name} is missing"]
    lines = p.read_text(encoding="utf-8").splitlines()
    wanted = [key_header.lower()] + [o.lower() for o in others]
    tables, cur, problems = [], None, []
    for i, line in enumerate(lines, 1):
        s = line.strip()
        is_row = s.startswith("|") and s.endswith("|") and len(s) > 1
        if is_row:
            cells = [c.strip() for c in s.strip("|").split("|")]
            if cur is None:
                cur = {"header": cells, "rows": [], "start": i, "delim": False}
            elif not cur["rows"] and not cur["delim"] and set("".join(cells)) <= set("-: "):
                cur["delim"] = True          # the delimiter row under a header makes this a real table
            else:
                cur["rows"].append((i, cells))
        elif cur is not None:
            tables.append(cur)
            cur = None
    if cur is not None:
        tables.append(cur)
    for t in tables:
        if not t["delim"]:                   # a group with no header delimiter is rows that lost their table
            for line_no, _ in [(t["start"], t["header"])] + t["rows"]:
                problems.append(f"{p.name} line {line_no}: a table row outside any table (after a blank line, "
                                f"or under a heading with no header row); move it into its table or remove it")
    tables = [t for t in tables if t["delim"]]
    matching = [t for t in tables
                if any(h.lower() == key_header.lower() for h in t["header"])
                and all(any(h.lower() == w for h in t["header"]) for w in wanted)]
    if not matching:
        return [], [f"{p.name}: no table with a '{key_header}' column; the register a check counts must be findable"]
    if len(matching) > 1:
        return [], [f"{p.name}: {len(matching)} tables carry a '{key_header}' column (lines "
                    f"{', '.join(str(t['start']) for t in matching)}); a register is one table"]
    t = matching[0]
    header = [h.strip() for h in t["header"]]
    rows = []
    for line_no, cells in t["rows"]:
        row = {header[i]: (cells[i] if i < len(cells) else "") for i in range(len(header))}
        row["_line"] = line_no
        rows.append(row)
    return rows, problems


def cell(row, name):
    for k, v in row.items():
        if k != "_line" and k.strip().lower() == name.strip().lower():
            return str(v).strip()
    return ""


FRONT_MATTER = re.compile(r"\A(?:---\n)?((?:[a-z_]+:.*\n)+)(?:---\n)?", re.M)


def split_front_matter(text):
    """({key: value}, body) — the `key: value` lines a draft opens with, and everything after them."""
    m = FRONT_MATTER.match(text)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def word_count(body):
    return len([w for w in re.split(r"\s+", re.sub(r"[#*_>`\[\]]", " ", body)) if w.strip()])


def drafts(root=ROOT):
    """[(number, Path)] for story/drafts/draft-NN.md, lowest first."""
    d = Path(root) / "story" / "drafts"
    out = []
    for p in sorted(d.glob("draft-*.md")) if d.exists() else []:
        m = re.fullmatch(r"draft-(\d+)", p.stem)
        if m:
            out.append((int(m.group(1)), p))
    return sorted(out)


def current_draft(root=ROOT):
    ds = drafts(root)
    return ds[-1][1] if ds else None


def sentences(body):
    text = re.sub(r"\s+", " ", body)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[\"'A-Z])", text) if s.strip()]


COMMON_WORDS = set("""the a an and or but if then than that this these those of to in on at by for with from
as is are was were be been being it its he she they them him her his hers their there here you your i me
my we us our not no nor so too very can could would should will shall may might must do does did done
have has had having what when where who whom which how why all any both each few more most other some
such only own same just now up down out off over under again further once about into through during
before after above below between while because though although until since upon among against toward
across behind beside beyond within without near far still yet even also ever never always often
sometimes soon later once twice back away down round about like unlike into onto off""".split())


def proper_nouns(body):
    """Words capitalised mid-sentence: the words in a story that are names rather than sentence openings."""
    out, start_of_sentence = set(), True
    for tok in re.finditer(r"[A-Za-z][A-Za-z'-]*|[.!?]+|\n\s*\n", body):
        s = tok.group(0)
        if s[0].isalpha():
            if not start_of_sentence and s[0].isupper():
                out.add(s)
            start_of_sentence = False
        else:
            start_of_sentence = True
    return out


def thresholds(root=ROOT):
    return read_json(Path(root) / "checks" / "thresholds.json")


def milestone(root=ROOT):
    m = re.search(r"\*\*Milestone:\*\*\s*M(\d)", read_text(Path(root) / "STATE.md"))
    return int(m.group(1)) if m else None
