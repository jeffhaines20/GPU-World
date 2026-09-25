# Story bible

Everything that must stay consistent. `check_continuity.py` reads the Names and Invented-terms tables of
this file against the manuscript: it fails on a spelling in one that is one character from the other, and
on an entry here the manuscript never uses. The Rules, Timeline, and Physical-details sections below are
for the writer and the critics; no program parses them, and nothing checks that the story obeys them.

## Names

| Name | What it is | Spelling notes |
|---|---|---|

## Invented terms

| Term | Meaning | First appears |
|---|---|---|

## Motifs

Words and images the story repeats on purpose. `check_tics.py` counts repeated distinctive words and
fails on one it was not told about, so a motif is declared here or it reads as a tic. Declaring it is
also a discipline: a word you cannot justify in this table is a word you are leaning on.

| Word | Why it repeats |
|---|---|

## Word that is not a drift

Words in the story that sit one character from a name or term above and are meant to. `check_continuity.py`
reads one character's difference as a name that drifted across a revision, which is usually right; when it
is not — Mara in a story that mentions Mars — the word that is *not* a bible entry goes here, one row per
word, and the check leaves it alone. Two names that are both in the bible (Mara and Mira, say) need no row
at all: the check knows they are both meant to be there. A plural never needs declaring.

Every row needs its reason. This table switches off the check that catches a character renamed halfway
through a revision, so a row with a blank reason is an off-switch nobody has to justify; the check refuses
one, exactly as it refuses a motif declared with no reason.

| Word that is not a drift | Why both are meant to be there |
|---|---|

## Rules of the conceit

_(what the strangeness can and cannot do; the limits the story must respect)_

## Timeline

_(what happens when, including what happened before the story starts)_

## Physical details that must not drift

_(the colour of a thing, which hand, how many, the weather)_
