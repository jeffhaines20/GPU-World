# Read me first

**Project:** GPU World story · **Milestone:** M0 — Intake · **Updated:** 2026-09-08

This is your copy of what the agents are doing. You write in two files and no others: `INBOX.md`, where the agents write what they need from you and where you answer, and `DECISIONS.md`, where your gate sign-offs go. (`BRIEF.md` at intake and `design/RUBRIC.md` are worth a look when this page points you at them; everything else in the folder is the agents'.)

## What is being made

One science-fiction short story, between 1,000 and 5,000 words: about four to twenty minutes of reading.
A team of AI agents writes it. Some of them write; the others only criticize, and never see who wrote
what, because an agent that grades its own work grades it kindly.

## What the loop asks of you

Two to two and a half hours in total, in five sittings: forty minutes, then twenty, ten, fifteen to twenty-five, and thirty to forty.
Each one is a **gate**: the agents stop, write what they need into `INBOX.md`, and wait for you.

**Two honest caveats about that number.** It is the total if you say yes at every gate. Each time you send
something back, add a sitting — what each refusal costs you is written into the five items below, so you
can see the price before you decide. And it does not include the homework in step 1 of `README.md`:
assembling your ten to fifteen stories and finding out which ones you own as text is an evening's work,
and it is the thing the whole bar rests on.

**How long in calendar time.** Expect two to four weeks between the first sitting and the last: the agents
work in units of about a day per round, and there are usually eight to twelve rounds between the spine and
the finished story. Your sittings are short; the waits between them are not.

1. **Intake (about forty minutes).** You answer questions about what you like: the kind of science
   fiction you want, three to five short stories you love and one sentence on why each, two or three
   things you never want to read, whether an unhappy ending is allowed. Then you name ten to fifteen
   published stories that stand for the quality you want. That set is the bar the story is measured
   against, so choose stories you would be glad to be compared to. **Aim to have at least four of them as
   plain text you can hand over.** Three is the floor — below that the agents are told to stop at intake and
   say so rather than proceed quietly — and four or more is what lets the comparisons vary from round to
   round instead of using the same three every time. Any readable form works: a `.txt` or `.md` file, text
   pasted out of an ebook reader, a PDF you can select text in. A scan you cannot select text in does not
   count, and the file name does not matter. Put them in `design/exemplars/`, one file per story. Where you
   cannot supply one, the comparison is made from the judges' knowledge of that story, which is weaker
   evidence, and they will tell you which is which.
2. **Choosing the idea (about twenty minutes).** You get three premises, each with a card and a sample
   passage of about 300 words. You pick one, or send one back — and sending one back does not swap in a single replacement: the agents generate four fresh premises from that whole idea-category and probe and judge them again, which costs about a day of their time and nothing of yours. At this sitting you write two short things: one line saying which premise you chose (`make decide TYPE=pick` prints it), and the three-to-five-sentence gate paragraph below. Every other gate is the paragraph alone.
3. **The spine (about ten minutes).** One page — who the story is about, what they want, what turns, how
   it ends, and the question underneath — and a short passage written from it, so you can hear the voice
   before there is a draft. Cheaper to change now than later. If you say no, the spine is rewritten
   against what you said and comes back to you, which costs the agents about a day and you one more
   ten-minute sitting; and if the trouble is the premise rather than the spine, the loop goes back to
   M1's runner-up premises rather than drafting on.
4. **The first full draft (fifteen to twenty-five minutes, depending on how long the story ran).** You read
   it once, straight through, without taking notes, and then say what you felt and what must change. Your
   first reading is evidence nobody else in this loop can produce, and it is spent the moment you read the
   draft twice. **You are not signing the story off here** — revision rounds continue either way, and there
   is no yes or no to give. Whatever you say becomes findings the revisions have to answer, so say what you
   felt even where you cannot say why.
5. **The finished story (thirty to forty minutes, depending on how long the story ended up).** You read it
   **aloud** — a 3,500-word story takes a little over twenty minutes to say out loud and a 5,000-word one
   takes half an hour, and then you owe three to five sentences. Prose that looks fine on a screen and falls
   apart in the mouth is the commonest failure of a story written by machine, and reading it aloud is the
   only test that catches it. **This is the one gate where you say yes or no**, and here is what no costs:
   the agents take your paragraph as findings, run one to three more revision rounds — a few days — and
   bring the story back for another reading aloud. That is a sixth sitting of the same length, and a second
   refusal a seventh. Say no anyway if the story is not right; that is what this gate is for, and it is the
   only point in the project where anyone can say so. But you should know the price before you pay it.

## How you sign a gate

Run `make gate N=1` (the number changes per gate). It prints the heading to paste into `DECISIONS.md` and
the question that gate is asking. You type three to five sentences in your own words — what you saw, what
you liked, what must change, whether it goes through — and save them. At G3 the question is different
(what the draft did to you, with no yes or no to give) and `make gate N=3` prints that instead. The agents never write this for you. No check can tell who typed a paragraph, so what protects it is
this: no agent may write or edit one, and once you have saved a sign-off, any later change to it fails
every run until you say, in a decision row of your own, that you made the change. If an agent ever offers to write your sign-off, that is a bug; say no.

If you want to change the wording of a sign-off you already wrote, you can: add a decision row of type
`gate-amend` naming that gate (`make decide TYPE=gate-amend`), and then edit your paragraph. One row covers one change to one gate: if you are tidying two sign-offs at one sitting, write two rows. The check
refuses a changed sign-off without that row, because a changed sign-off with nobody's name on it is how a
record stops meaning anything.

## What you can trust and what you cannot

The agents can check some things by program: the length, that names and invented terms stay consistent,
that every criticism got an answer, and that every comparison was run in both orders by a judge that was
tested that day on a rigged pair — the story's own text against a deliberately worsened copy of it. A
judge that cannot tell those apart does not get a vote that round. They cannot check whether the story is good. That is what your five sittings
are for, and the last one, reading it aloud, is the one that matters most.

They also cannot prove the story is original. They will name the published stories closest to it and say
what is different, and they will tell you what they did not look at.

## If something looks wrong

Say so in plain words, in chat or in `INBOX.md`. "This is boring in the middle" is a usable finding.
You are never expected to say why, or to suggest a fix.
