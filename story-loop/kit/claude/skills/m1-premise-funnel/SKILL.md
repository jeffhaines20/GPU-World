---
name: m1-premise-funnel
description: Runs milestone M1 — frames the premise space, generates twenty-four premises in isolation, compresses them to cards, probes the strongest six with real prose, judges them blind, and puts three in front of the human. Use once G0 is signed.
---

# M1 — The premise funnel

Refuses to run before G0 is signed (`check_state.py` holds the milestone line).

1. **Frame before generating.** Write the six cells into `design/PARTITIONS.md` with the narrowing the
   brief implies. This file is written and committed *before* any premise exists; a premise generated
   before the partition table is a premise that chose its own cell.
2. **Generate.** Spawn six `premise-writer` agents, one per cell, each in a fresh context, each given
   only its cell, the register, the taste brief, and the length target. Four cards each. Collect them
   into `design/PREMISES.md` with IDs P-01 to P-24 and `Status: generated`. Never show a writer another
   writer's cards.
3. **Strike the known stories.** Spawn `originality-critic` on all twenty-four cards at once. Any card
   it calls derivative is struck on the page with the named story and the reason. This happens *before*
   probing, because a probe of a known story is six hundred words spent proving it reads well.
4. **Judge the cards.** Two `premise-judge` agents, fresh contexts, batches of at most six, shuffled per
   batch, neither seeing the other's scores nor the writers' identities. Keep two rankings: one by the
   scores shrunk toward the pool median, so that one enthusiastic judge cannot carry a card, and one by
   each card's **highest single-judge score**. Where the two judges differ by two points or more on a
   card, mark it disputed.
5. **Choose six to probe.** Take five from the shrunk ranking, no more than two from one cell, and give
   the sixth slot to the highest card on the second ranking that the shrunk ranking did not take —
   usually the disputed one. The shrinkage exists to stop a fluke carrying a card; the reserved slot
   exists because the card two good judges argue about is the strange one, and shrinking is exactly
   what removes it. Mark all six `Status: probed`.
6. **Probe.** Spawn `probe-writer` on each of the six, naming the hardest passage for that premise.
   250-350 words each, saved beside the card. Then run step 4 again over cards-plus-probes.
7. **Offer three.** Two finalists from the shrunk ranking, and the third slot to the most disputed
   surviving card if one is disputed. Write to `INBOX.md`: each finalist with its card, its probe, its
   originality note, and the dispute stated as a dispute — "one judge called this the best of the
   twenty-four and the other called it the weakest, and here is what each said". Say which the judges
   preferred, say that the choice is the human's, and stop. Never resolve a dispute with a third judge:
   the disagreement is the information.
8. **The human picks**, recording it with `make decide TYPE=pick`. If they send a cell back, regenerate that cell only: the writer and premise
   caps carry one spare cell for exactly this, and a second regeneration needs the human's caps decision. Then G1 through the gate skill.

**Where this fails.** Generating before framing; probing before the originality pass; handing the human
one option with two decoys; resolving a judge disagreement instead of showing it.
