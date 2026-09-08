# The exemplar set

The bar. Ten to fifteen published short stories the human named at intake. The story is measured
against these and against nothing else.

**Provenance matters and is recorded.** Where the human supplied the text, it sits in
`design/exemplars/` and comparisons are made against the words. Where they could not, the comparison is
made against the judge's knowledge of the story, is recorded with `from_memory: true`, and counts less:
the gate at M3 and M4 requires at least **three of a round's four pairs** to be judged against text the
human supplied (`checks/thresholds.json`, `min_full_text_pairs_at_gate`). A **pair** is one exemplar on
one dimension, judged in both orders — so a round of four pairs is eight verdicts, and "three pairs on
supplied text" means three of the round's four exemplars, not three verdicts.

Below three supplied texts in the whole set the loop cannot meet that at all, and `LOOP_DESIGN.md` §11
tells the orchestrator to stop at intake and say so rather than proceed quietly. Four or more is what
makes a round's exemplars vary from round to round instead of repeating the same three.

**Copyright.** These texts are the human's copies, used here to judge one story against them. Nothing
from an exemplar is reproduced in the manuscript, and a comparison quotes at most one sentence from each
side as evidence.

| # | Title | Author | Year | Text supplied | Why the human named it |
|---|---|---|---|---|---|
| 1 | The Machine Stops | E. M. Forster | 1909 | yes — `the-machine-stops.txt`, 12,155 words, public domain (Project Gutenberg #72890, *The Eternal Moment and Other Stories*) | proposed by the orchestrator as the ancestor of the premise, a machine serving every need; accepted in chat with the instruction to use every text obtainable online |
| 2 | The Star | H. G. Wells | 1897 | yes — `the-star.txt`, 4,429 words, public domain (Gutenberg #11870) | proposed: one global event through many small lives; accepted as above |
| 3 | The Country of the Blind | H. G. Wells | 1904 | yes — `country-of-the-blind.txt`, 11,269 words, public domain (Gutenberg #11870) | proposed: a social arrangement that is right from inside; accepted as above |
| 4 | As Easy as A.B.C. | Rudyard Kipling | 1912 | yes — `as-easy-as-abc.txt`, 10,205 words, public domain (Gutenberg #13085, *A Diversity of Creatures*) | proposed: a working technocratic future told as ordinary; accepted as above |
| 5 | Exhalation | Ted Chiang | 2008 | yes — `exhalation.txt`, 6,505 words, fetched from the publisher's free page (lightspeedmagazine.com/fiction/exhalation/); under copyright, not committed, re-fetch on resume | proposed: a hard idea carried by feeling; accepted as above |
| 6 | Cat Pictures Please | Naomi Kritzer | 2015 | yes — `cat-pictures-please.txt`, 3,420 words, fetched from the publisher's free page (clarkesworldmagazine.com/kritzer_01_15/); not committed | proposed: a benevolent AI's own view, humane and funny; accepted as above |
| 7 | Lena | qntm | 2021 | yes — `lena.txt`, about 1,950 words, fetched from the author's page (qntm.org/mmacevedo); not committed | proposed: the form is the idea; accepted as above |
| 8 | STET | Sarah Gailey | 2018 | yes — `stet.txt`, 1,772 words, fetched from the publisher's free page (firesidefiction.com/stet); not committed | reserve list: form-driven, an autonomous-car story told in footnotes; accepted as above |
| 9 | Welcome to Your Authentic Indian Experience™ | Rebecca Roanhorse | 2017 | yes — `welcome-to-your-authentic-indian-experience.txt`, 3,596 words, fetched from the publisher's free page (apexbookcompany.com/blogs/apex-magazine/welcome-to-your-authentic-indian-experience); not committed | reserve list: a technology of experience lived with; accepted as above |
| 10 | The Ones Who Walk Away from Omelas | Ursula K. Le Guin | 1973 | no — not obtainable as text; judged from the judges' knowledge of it, recorded `from_memory: true` ("Keep", in chat, 2026-09-08) | one of the three stories the human named as loved |
| 11 | The Yellow Wallpaper | Charlotte Perkins Gilman | 1892 | yes — `yellow-wallpaper.txt`, 6,078 words, public domain (Gutenberg #1952) ("Add", in chat, 2026-09-08) | one of the three stories the human named as loved; not science fiction |

**Not obtainable, therefore not in the set:** The Truth of Fact, the Truth of Feeling (Ted Chiang, 2013): the
publisher's page is gone and the archive copy is blocked from this environment. Bloodchild, Speech Sounds, There Will Come Soft Rains, The Nine Billion Names of God, When It Changed, The Last
Question, Burning Chrome: under copyright and not posted free by their publishers; the human supplies no copies.

**Rotation.** A round draws four different exemplars. Over rounds the draw covers the set: the two long Wells and
Forster texts cost a judge more to read, so they are drawn no more than one per round.
