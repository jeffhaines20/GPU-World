# Story bible

Everything that must stay consistent. `check_continuity.py` reads the Names and Invented-terms tables of
this file against the manuscript: it fails on a spelling in one that is one character from the other, and
on an entry here the manuscript never uses. The Rules, Timeline, and Physical-details sections below are
for the writer and the critics; no program parses them, and nothing checks that the story obeys them.

## Names

| Name | What it is | Spelling notes |
|---|---|---|
| Noor Brouwer | The trainee midwife, 24, born 2016, in the last month of her training; concordance 97.1 on the night, the lowest in Zeeland; 96.9 from 02:14 | "Noor" in narration and speech; the full "Noor Brouwer" once, in the review, which names her in full. Never Nora or Noora. The English words door and nor sit one character away and are declared below; do not use poor, moor, noon or Noord. |
| Marga Dekker | The supervising midwife, 65, trained from 1998, concordance 99.6 over nine years of scoring; retires 31 January 2041 | "Marga" in narration and speech; "Marga Dekker" once, in the review. Never Margo or Marge. |
| Sanne | The mother; a dike inspector for the water board; first baby; hers is the birth that is spent | No surname anywhere: her counsel writes the review to her as "you", and the story never needs one. Do not use sane, Sanna or Anne. |
| Joost | Sanne's partner; keeps the bed on its blocks because it is easier for the stitches | No surname. Do not use joist or roost. |
| Zierikzee | The town on the island where the practice and Sanne's house are; the island is not named | One word, two z's, ending -zee. |
| Zeeland | The province; Noor's 97.1 is its lowest | Dutch spelling; never Zealand. |
| Zeelandbrug | The five-kilometre bridge over the Oosterschelde; the transfer's road to Goes | One word; "the Zeelandbrug" at first use, "the bridge" after. |
| Oosterschelde | The water under the Zeelandbrug: black, under white lamps | Not the Westerschelde. Two different waters; the story keeps them apart. |
| Westerschelde | The estuary her father pilots ships up | Her father's water only; never the bridge's. |
| Goes | The town with the hospital where the section is done | Capital G. The English verb goes and its neighbour does are declared below. |

## Invented terms

| Term | Meaning | First appears |
|---|---|---|
| counsel | The model everyone carries, worn at the collar. Always lowercase, always "it" in narration; it says "I" when it speaks. "The counsel", "her counsel", "Sanne's counsel", "mine" (Sanne's word). Fluent, competent, fallible, without a will. | Beat 1, first paragraph |
| concordance | The share of a midwife's scored decisions that agreed with her counsel's recommendation at the time. Scored from the record, published on the registry, shown at the edge of her counsel's display. It measures agreement, not outcomes: a departure that turns out right still lowers it. Noor 97.1, then 96.9; Marga 99.6. | Beat 1 |
| departure | The registry's word for a decision that did not follow the counsel's recommendation. Each is logged with its time and lowers concordance whatever comes of it. Noor: seven this year before the night, all small; the transfer is the eighth. Marga: six in nine years. | Beat 1 |
| record | Everything a counsel hears, says and logs. A woman's counsel may read the professional records of her care. The record holds what was said, done and wanted, never what was heard. | Beat 1 |
| recording | The stretch of the record that is sound: the contraction at 02:10 and the heart after it, the doppler through Noor's collar with Sanne's breath under it, played from Noor's phone. | Beat 5 as a noun; the sound itself is beat 1 |
| review | The document Sanne's counsel wrote to her, in the second person, on day two, when she asked it to read her care; sent to the practice the same day as notice; the complaint is drafted from it. | Beat 4 |
| simulator | The counsel's training cases: births it writes, voices through the doppler and scores. It has never made a heart it could not hear. | Beat 5; may be named as the obstacle in beat 2 |
| training decision | The review's phrase for what the departure was "consistent with": a decision made in order to learn. Quoted, never paraphrased, except by Sanne ("It says I was probably a training decision"). | Beat 4 |
| ten past two | The story's name for the recording after the night. | Beat 5; the clock time 02:10 is beat 1 |
| working height | The height the hired blocks bring a bed to, where a midwife works standing. The title; the bed's height in beat 1; where Sanne lies on day eight. | Beat 1 |

## Motifs

Words and images the story repeats on purpose. `check_tics.py` counts repeated distinctive words and
fails on one it was not told about, so a motif is declared here or it reads as a tic. Declaring it is
also a discipline: a word you cannot justify in this table is a word you are leaning on.

| Word | Why it repeats |
|---|---|
| heart | The fetal heart on the doppler is the story's object; the heart her father sends is its cheap double. Every scene has one. |
| hear | The verb of the question: what Noor did or did not do; what the counsel "hears nothing wrong" with. Hearing is the result. |
| heard | Past form of the same: "What did you hear?" is answered by what she heard; Marga "didn't hear it". |
| listen | The act, which the record can log (who listened, when) but not the result of. |
| listened | Past form: Marga listened through a contraction; Noor "had listened to ten past two perhaps four hundred times". |
| listening | The story's last verb: Noor watches Sanne listening. |
| counsel | The invented term; on every page. |
| concordance | The invented term; the pace she checks. |
| departure | The invented term; what is logged at 02:14. |
| departures | Its plural: the review's list of seven. |
| record | The invented term; what the review reads. |
| recording | The invented term; what Noor plays. The story is about what a record holds and what it does not. |
| review | The invented term; the back half's document. |
| simulator | The invented term; where she is sent. |
| fair | The story's word for the counsel and the review, always meant, never ironic in the narration: "It was very fair." |
| fairly | The adverb, for the counsel's last act: it "told her, fairly, that nothing is there". |
| patient | The counsel's manner, adjective only; Sanne is never "the patient". |
| patiently | How the counsel gives the same answer each time. |
| patience | The reason she stops asking: "the patience was worse". |
| height | The bed on its blocks; the title; the last image ("the height Noor would have worked at"). |
| working | Only in "working height": the title, and the blocks bringing the bed to it in beat 1. |
| blocks | The hired bed blocks, there in beat 1 and still there on day eight; the physical fact that ties the first scene to the last. |
| late | "A fraction late" is the thing heard; the review's "no late deceleration" is the same word in the counsel's mouth. |
| nothing | The counsel's finding at 02:10, Marga's second departure ("and nothing"), the counsel's last word ("nothing is there"), Noor's hands ("nothing to do with her hands"): the story's word for what a record can hold. |
| again | The turn; the word Sanne says; the replays. |
| gallop | The doppler's sound, "a horse going hard on sand"; used only in the recording scenes. |
| knot | The true knot: the evidence that is not evidence. |
| bridge | The Zeelandbrug and "a birth on the bridge": the risk the counsel priced, in beats 2, 3 and 4. |
| contraction | The unit of the night; listening happens after one. |
| contractions | Its plural; the simulator has its own. |
| centimetres | "Eight centimetres" is where labour is at 02:10 and where it stops at Goes. British spelling. |
| section | The caesarean; the review's word; the father's statistics. |
| phone | Noor's; where the recording and the photograph live; at Sanne's ear at the end. |
| want | What the review reads off the record; the noun is the review's before it is Noor's. |
| wanting | The review's gerund: "the student's wanting". |
| five | "Three in five" is the price; "one time in five" is Noor's hearing by Friday; "five kilometres" is the bridge. The echo is meant. |
| two | "Ten past two" and "fourteen minutes past two" are the story's two timestamps. |
| call | "Your call" is Marga's line; "the call" is a decision; Joost calls the ambulance. Three senses on purpose. |
| collar | Where the counsel is worn; "on every collar" is the world in three words. |
| January | Marga's retirement; what Noor "thinks of" on the landing; the board's deadline. |
| daughter | Sanne's; she is never named, so "her daughter" is the only way to say her. |

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
| goes | The English verb ("the heart goes", "the gallop goes on"); the town is Goes. Both are meant. |
| does | The English verb; one character from the town Goes. |
| door | The bedroom door and the landing outside it; one character from Noor. |
| nor | The conjunction; one character from Noor. |

## Rules of the conceit

- The year is 2040. Frontier AI progress stopped in September 2026. Every person has one model of that quality, always on, theirs alone: never much better than 2026's, never superhuman; no one has two, no one has none, and a share cannot be pooled, sold or accumulated. It is fluent, competent and fallible. It is not a character and has no will; the story never gives it a wish, a mood or a plan.
- It is called the counsel and worn at the collar: a flat clip the size of a two-euro coin, matte, on the left collar. It speaks low and close, pitched for its wearer, in short sentences, and can be asked to write instead. It hears everything its wearer hears. Noor's doppler is paired to her counsel, so at 02:10 it heard the same sound she did, through the same instrument, and found nothing wrong.
- The counsel never says more than four sentences at once, never lies, never hedges to seem wise, never raises a thing it has not been asked unless it is a risk. What it cannot do is hear what it cannot hear, and the story never has it pretend otherwise. Its patience is real; "the patience was worse" is Noor's, not the story's.
- The record is everything a counsel hears, says and logs, timed to the second. Professional records of a person's care are open to that person; their counsel may read them. A midwife's departures and her concordance are on the public registry. So Sanne's counsel could read Noor's record of the night, Marga's, and Sanne's own; the review is built from all three.
- Concordance scoring of midwives began in the Netherlands in 2031. The counsel identifies each decision in the record where it gave a recommendation, and scores it followed or not. Small agreements count, which is why the figures are so high; a departure that turns out right still counts against. The figure is scored at the moment of the decision: Noor's moved at 02:14, before the ambulance came.
- The simulator is the counsel's. It writes each case, voices the doppler, scores the trainee, and cannot present a heart it could not itself hear, because it does not know one. So the only place to learn whether one can outhear it is a real woman.
- A review is any person's counsel reading their care back to them when asked. It gives likelihoods, recommendations, quotations from the record with their times, and, fairly, what the record supports about the practitioner's motive. It cannot report a hearing that left no trace, and says so in its own words. It drafts a complaint if asked and sends nothing without being told.
- A complaint from a review goes to the practice and the training board. On notice of a possible complaint about a trainee's departure with harm, the board suspends her live cases until the complaint is resolved or withdrawn, moves her remaining hours to the simulator, and defers her sign-off. The board's review of a complaint can take up to eight weeks from the day it is received. Nobody's registration is at stake; a trainee's sign-off, and who signs it, is.
- Home birth is still ordinary in Zeeland in 2040, with a handheld doppler, a bed on hired blocks, and an ambulance transfer over the Zeelandbrug to Goes when the midwife says so. Nothing in the medicine is beyond 2026; the counsel does not change what a midwife can do at a bed, only what it costs to do it without it.

## Timeline

- 1 September 2026: frontier AI progress stops. Every later model is of that quality and no better.
- 1998: Marga Dekker begins her midwifery training. She has had the practice in Zierikzee for most of her working life.
- 2016: Noor Brouwer is born.
- 2029: the last time Noor's father overrules his counsel, piloting on the Westerschelde. He says so at birthdays, as a good thing, and it is.
- 2031: concordance scoring of midwives begins. Marga's 99.6 covers nine years: six departures, one a cord twice round the neck (right), five women moved for nothing. Noor has been at two of the six: the cord, and one of the five.
- Autumn 2038 to November 2040: Noor's scored placements. Concordance 97.1 by the night; seven departures this year before it, all small (which side to lie on; when to examine; whether to call the maternity nurse yet).
- Monday 12 November 2040, evening: Sanne's labour, at home under the dike in Zierikzee. Marga and Noor attend. The bed is on its four hired blocks.
- Tuesday 13 November, 02:00: eight centimetres, all normal, contractions about two minutes apart.
- 02:10: after a contraction, Noor hears the heart come back a fraction late. Her counsel: baseline one-forty, variability normal, no deceleration. She has Marga listen at once; Marga hears the tail of that return and the whole of the contraction at 02:12, and shakes her head.
- 02:13 to 02:14, the landing: the counsel's four sentences (no indication; transfer at eight centimetres in a first labour carries a risk of birth on the bridge, under one in twenty; it recommends listening through three more contractions and reassessing; can she say what she heard?). "No." Marga: "I didn't hear it." "Let me." "Your call." The departure is logged at 02:14 and her figure moves to 96.9.
- 02:16: Noor tells Sanne and Joost. Their counsels say what hers says. "Why?" "I can't tell you." Sanne agrees. 02:19: Joost calls the ambulance. 02:33: it arrives. Marga follows in her own car; Joost rides in front.
- 02:40: on the Zeelandbrug. Sanne on all fours on the stretcher. The counsel's odds of a birth on the bridge fall as the contractions space out. Noor checks her figure once: 96.9.
- About 03:05: Goes. Labour stops at eight centimetres and does not restart with augmentation.
- 07:40: caesarean section. The obstetrician lifts the cord: a true knot, loose. 07:50: Noor photographs it with his leave. A girl; Apgar nine at one minute, ten at five.
- Tuesday 13 November, night ("the first night"): Noor plays ten past two and hears it after every contraction.
- Wednesday 14 November, day two: Sanne asks her counsel to review her care. The review reaches the practice the same morning as notice. Noor reads it there.
- Thursday 15 November, day three: the board's message through Noor's counsel: live cases suspended; remaining hours on the simulator; sign-off deferred. Her father's message: a heart, and Goes's section statistics.
- Friday 16 November, day four: the simulator in the practice's back room; Marga packing; Noor hears it one time in five.
- Sunday 18 November, day six: from this night she does not hear it at all. She stops asking the counsel.
- Tuesday 20 November, day eight, morning: Sanne sends the complaint, and the same morning asks the practice for Noor to come. Marga tells Noor she need not go.
- Tuesday 20 November, afternoon: the house under the dike; the bed still on its blocks; the passage; the last image. The story ends there.
- 31 January 2041: Marga retires. A review that runs its eight weeks from 20 November ends about 15 January; if it runs long, the sign-off falls to her successor, who joins in January and has never seen Noor at a bed.

## Physical details that must not drift

- The house: under the dike in Zierikzee, on the dike side of the town, the bedroom upstairs with a landing outside its door. No window is looked at.
- The bed: on four hired grey plastic blocks from the home-care shop, which raise it by a hand's length to working height. Still on them on day eight; Joost's reason is that it is easier for the stitches, getting up.
- The counsel: a flat matte clip at the left collar. Noor's is on her tunic on the night and on her coat on day eight; Sanne's is on her cardigan on day eight. It is never an earpiece.
- The doppler: handheld, in Noor's right hand, her left hand flat on Sanne's belly. It is paired to her counsel. The recording is the doppler and the room through her collar, about two minutes long, spanning the contraction at 02:10 and the heart after it.
- The heart at 02:10: about one-forty; the return after the contraction that Noor hears as a fraction late, "like someone answering to her name a moment after it was called". Through the phone's speaker it is "fast and soft, a horse going hard on sand"; the gallop slows under the contraction and comes back.
- The night: dry, cold, still; no rain. The Zeelandbrug's lamps are white; the Oosterschelde under them is black.
- The ambulance: Sanne on all fours on the stretcher; Noor in the back with her; Joost in the front; Marga following in her own car.
- Goes: the hospital's delivery room, then theatre. The obstetrician is a man and is never named. The cord is lifted in his gloved hands; the knot is a single loose overhand, not tightened.
- The photograph: on Noor's phone, taken 07:50, behind the recording. It is never offered to Sanne. The review gives it a paragraph and calls it "not evidence that transfer was needed".
- The baby: a girl, born 13 November 2040 at 07:40, never named in the story. On day eight she sleeps face down on Sanne's chest, one fist under her cheek; Sanne's hand lies flat on the small back and rises when it rises.
- Sanne on day eight: on the bed on its blocks, at the height Noor would have worked at; stitches from the section; eyes on her daughter's head, not on the phone, through the first two plays. On the third she holds Noor's phone at her ear, and Noor hears nothing of it.
- Noor on day eight: stands beside the bed "with nothing to do with her hands"; sets the phone on the duvet for the first play; reaches for it when it ends. She has played ten past two "perhaps four hundred times".
- Noor's phone: where the record is read; the recording and the photograph on it; her figure at the edge of her counsel's display.
- The father: never named; a Westerschelde pilot; appears only as one message, a heart and Goes's section statistics, "which are good". No call, no scene.
- The practice: Marga's, in Zierikzee, unnamed; a back room where the simulator runs on Noor's counsel with the doppler paired; boxes for January.
- The board, the academy, the water board, the home-care shop, the hospital, the island: none named.
- The review's fixed phrases: "probably avoidable"; "about three in five"; a recommendation that every future birth be planned in hospital; "not evidence that transfer was needed"; "Let me" and "Your call" quoted with 02:14; the recording at 02:10 "reanalysed", "no late deceleration"; the seven departures listed; "consistent with a training decision". It is written to Sanne as "you".
- Lines that stay as written: "I didn't hear it." "Let me." "Your call." "Why?" "I can't tell you." "Keep that." "I sent it this morning. Mine drafted it. It was very fair." "I read it." "'Let me.' Fourteen minutes past two. That's you. You asked her." "It says I was probably a training decision." "What did you hear?" "Again."
- Marga's line in beat 5, when she will not listen to the recording, is the writer's, five words or fewer, and explains nothing.
- The counsel's last words in the story are Sanne's counsel giving her the second to listen at and saying, fairly, that nothing is there. After that no counsel speaks.
