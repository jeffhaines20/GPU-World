# Decisions

One row per decision. Agents write rows with author `agent`. A row with author `human` records a choice
the human made in their own words: the premise pick, the title, the caps, a subject ruled out. Written with `make decide TYPE=<pick|caps|title|taste|routing|gate-amend|fault-suite|other>` and saved by
the human themselves. Two of those types exist to unlock something the checks otherwise refuse:
`gate-amend`, naming a gate (G2, say), which lets you change the wording of a sign-off you already wrote —
an agent may never do this, and without your row the check treats a changed sign-off as tampering; and
`fault-suite`, which permits the agents' own self-test suite to lose a test.

| ID | Date | Author | Type | Decision | Why | Alternative not taken |
|---|---|---|---|---|---|---|

## Gate sign-offs

Written by the human, in their own words, after reading. One section per gate (`### G0` … `### G4`),
three to five sentences. A section, once written, is never edited: what you want to add later is a new
row above.
