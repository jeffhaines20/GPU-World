# Story bible

Everything that must stay consistent. `check_continuity.py` reads the Names and Invented-terms tables of
this file against the manuscript: it fails on a spelling in one that is one character from the other, and
on an entry here the manuscript never uses. The Rules, Timeline, and Physical-details sections below are
for the writer and the critics; no program parses them, and nothing checks that the story obeys them.

## Names

| Name | What it is | Spelling notes |
|---|---|---|
| Tess | Tess Haworth, nineteen, the point-of-view character; a night care assistant in Halifax until last week; leaves for nurse training in Leeds on the Saturday | Always "Tess"; never Tessa or Teresa; possessive "Tess's". In narration she is "Tess" or "she"; Rob and Kit call her nothing but "you" |
| Haworth | the family's surname | Used once, aloud, by the client at Heptonstall ("Rob Haworth's lass", or near it); never "Howarth", which is a different local spelling. Not otherwise needed |
| Kit | her brother, twelve, in year eight at Calder High; the story's live case | Always "Kit"; never Christopher, never "Kit's full name". The manuscript never uses lower-case "kit" for equipment: Rob's is "gear", "the ropes", "the saw" |
| Rob | their father, forty-seven, a tree surgeon; the man who kept the bowl | In narration he is "her father" (the passage's usage) far more often than "Rob"; "Rob" is used at least once (the client says it) and is allowed in narration sparingly. Tess and Kit say "Dad". Never Robert, never Robbie |
| Hebden Bridge | the town; the house is a stone terrace on the hillside above the station | "Hebden Bridge" in full at least once (the station); "Hebden" alone is what locals say and is allowed after that |
| Heptonstall | the village on the hill above Hebden Bridge; Wednesday's beech is in a garden there | One word, two l's; never "Heptonstal" |
| Mytholmroyd | the village down the valley; Calder High is there, and the traffic lights where Rob said the sentence | Never "Mytholmroyde"; "the lights in Mytholmroyd" is the fixed phrase and is never "the traffic lights at Mytholmroyd" |
| Midgley Moor | the moor above Mytholmroyd where she went at thirteen | "Midgley Moor" in full at least once; "the moor" after that; never "Midgely" |
| Calder High | the secondary school in Mytholmroyd; Kit's school, and Tess's until 2039 | Exactly "Calder High"; never "Calder High School", never "the High" |
| Halifax | the town where the care home is, and where the drive at fifteen started | — |
| Leeds | where the 9:14 goes; where she will train | — |
| 9:14 | the Saturday-morning train from Hebden Bridge to Leeds | Digits and a colon, exactly "9:14", and always "the 9:14"; never "nine fourteen", never "09:14". It is the only clock time written in digits anywhere in the story; every other time is in words ("five", "three in the morning"). It is "four minutes late", never "9:18" |

## Invented terms

| Term | Meaning | First appears |
|---|---|---|
| bud | the earpiece in which everyone has their one model; the size of a fingernail, worn in the ear; and, by the story's usage, the thing that speaks ("the bud said"). Lower case, no brand, no plural in the title. The manuscript never says "earbud", "earpiece", "device", "assistant", "AI", "model" or "counsel" for it | Beat 1, at the bowl, the first page |
| bowl | the brown-glazed bowl on the hall table inside the front door, where every bud in the house and Rob's keys go; the house's rule of eleven years. Always "the bowl"; the rule itself is never given a name (no "the bowl rule", no "house rule") | Beat 1, the first page |
| audit | Tess's word for what she has done since August: the care home in Halifax is audited, so this is the word she has for checking a record against a standard. "The audit"; "auditing him" as a verb is allowed. Nobody else in the story uses the word | Beat 1, second page |
| run | one pass of the audit; there have been eleven, and there is no twelfth. Written "run eleven", "run ten", "run four": the word and a numeral in letters, never "Run 11" | Beat 1, second page |
| entry | one of the forty-one items on her list: an occasion on which her father decided something about her. "Forty-one entries" is spelled out; the singular "entry" appears (the lights are "the entry") | Beat 1, second page |
| curve | the graph every run draws: her father against the bud, year by year, worse early and better late, her years at the bottom left and Kit's at the top right. Always "the curve"; never "learning curve", never "the graph" | Beat 2, Wednesday night |
| reasonable father | the bud's construct: what "a reasonable father" would have done at each entry, a different one each run. The phrase is the bud's, in its own voice, and gives the title its fathers | Beat 1, first or second page |

## Motifs

Words and images the story repeats on purpose. `check_tics.py` counts repeated distinctive words and
fails on one it was not told about, so a motif is declared here or it reads as a tic. Declaring it is
also a discipline: a word you cannot justify in this table is a word you are leaning on.

| Word | Why it repeats |
|---|---|
| Right | Rob's word for the start of anything he is about to do ("Right," at Kit's bed, twice in the passage; at the beech; at the door). It is the nearest he comes to announcing a decision, and the story wants the reader to hear him decide without hearing why |
| rim | the rim of the ear, which the bud reddens (Tess's since August, Kit's by Saturday), and the chipped rim of the bowl: the two edges the bud crosses. The last image is a rim |
| ear | where the bud is; "In your ear"; "Your sister's goes red"; the rim of Kit's ear. The story's site of wearing, and what Rob looks at instead of checking |
| wall | the wall between Tess's room and Kit's, her palm flat on it: the story's instrument. Everything decisive is heard through it |
| board | the floorboard by Kit's bed that Tess knows by heel from when the room was hers; how she reads him without seeing him. Pairs with "creak" |
| creak | Kit's bed taking his weight, Monday and Thursday; the sound that tells her he is there and awake |
| stairs | the stairs that come straight down to the door and the bowl: the house's clock. Rob on them twice on Thursday is the first thing that "never happened" |
| door | the bowl by the door; "He had not come to her door"; the last image is from the door. Rooms are entered or not, and the story keeps count |
| click | a bud going into the bowl, heard from upstairs. It is the sound of the rule being kept, and on Thursday of Rob keeping it for Kit |
| red | what the rim goes; the mark that shows Rob what he has not been told, on Tess in August and on Kit on Saturday |
| round | "Grew round it" (the wire); the head torch round his neck; her fingers round the bud. The word is never applied to a child by anyone; the reader is left to |
| plan | care plan (her year of nights), felling plan (the client's bud's), the plan her own bud gives her at four on Thursday: the story's one word for advice as instruction, and what she departs from |
| reasonable | the bud's word, in every run: "a reasonable father", "a reasonable man". It never uses another adjective for him, and the story never lets a person use this one |
| fetch | the sentence and its residue: "come and get you"; "someone nobody need fetch"; whether Kit wanted fetching. Both "fetch" and "come and get" recur and are meant to |
| whisper | how she talks to it at home, because of the wall; the audit's register. Kit learns it |
| palm | her palm flat on the wall at five; the bud going on in her palm, very small, grading him. The same hand, the same page |
| know | "I know why you did it"; "No. I don't"; the man who knew his children; she knew which board. The story's verb, used by everyone and settled by no one |
| five | Rob's alarm, every working morning of her life; the hour of the passage; the hour she waits for on Thursday |
| silence | the drive home at fifteen, "it was the silence"; the bud cannot score it; Rob's silence Friday at the bowl. Repeated where the bud's grading fails |
| alarm | Rob's, at five; heard from her room; the fixed point of the household's mornings |
| van | Rob's, at the lights, at the door, and leaving on Thursday; how he goes and how he fetched her |
| torch | the head torch on Midgley Moor, still round his neck at the lights; it returns in the memory each time the lights do |

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
| it | The pronoun, one deletion from "Kit", and the story's only name for the bud ("the bud said"; "Ask it"; "What did you ask it?"). Capitalised at the start of a sentence, "It", the same word. Unavoidable in any English sentence, and here it is the machine |
| bit | Kit's answer to "Does it hurt?" ("Bit.") in the passage, and the ordinary word; one substitution from "Kit" |
| kid | The ordinary word for a child, one substitution from "Kit"; allowed in the client's mouth or Tess's thoughts, never as a name for Kit |
| sit | The verb, one substitution from "Kit"; she sits up in bed with her palm on the wall |
| hit | The verb, one substitution from "Kit"; the chain hits the wire in the beech |
| lit | The verb, one substitution from "Kit"; the head torch, the lights in Mytholmroyd |
| less | The ordinary word, one substitution from "Tess"; the story cannot go 3,500 words without it |
| test | The ordinary word, one substitution from "Tess"; the audit tests nothing but the writer may need the word |
| job | The ordinary word, one substitution from "Rob"; he has a job at Heptonstall on Wednesday and another on Saturday |
| rot | The ordinary word, one substitution from "Rob"; a tree surgeon reads a trunk for it, and the beech has some round the wire |
| row | The ordinary word (a row of houses; a row, meaning a quarrel), one substitution from "Rob"; the terrace is a row |
| needs | The ordinary word, one substitution from "Leeds"; unavoidable |
| leads | The ordinary word, one substitution from "Leeds"; the ropes have leads, and the verb is common |
| colder | The ordinary word, one substitution from "Calder"; it is late September on a hillside |
| door | The ordinary word, one substitution from "Moor" in "Midgley Moor"; the bowl is by the door and the last image is from it, so it is also a motif above |
| poor | The ordinary word, one substitution from "Moor"; allowed in speech ("poor lad") |
| but | The conjunction, one substitution from "bud"; unavoidable |
| bed | The ordinary word, one substitution from "bud"; Kit's bed creaks, and the story is set largely in bedrooms at night |
| bad | The ordinary word, one substitution from "bud"; the audit's own scale runs from worse to better and the word will be needed |
| ran | The past tense of run, one substitution from "run" the term; "she ran it again" is the same word in another tense and is meant |
| sun | The ordinary word, one substitution from "run"; Wednesday is bright and still |
| curved | The ordinary participle, one insertion from "curve"; a limb is curved, a saw cut is not |

Other words one character from a name or term (fit, kin, kite, mess, tens, rub, rib, sob, robe, rod, sigh,
moon, seeds, feeds, weeds, boil, bow, howl, audio, curse, carve) are not declared. The manuscript avoids them,
and when a draft genuinely needs one, a row goes here with its reason before the draft is checked.

## Rules of the conceit

**The world (given, and not stated in the story).** It is 2040. Frontier progress stopped in September 2026. Every person has, always on, one model of that quality, theirs alone, never much better than 2026's and never superhuman; nobody has two or none, and a share cannot be pooled, sold or accumulated. The model is fluent, competent and fallible; it is not a character and has no will. The story never names the year, the stop, or the arrangement; it shows them: everyone's is the same, and the client's bud at Heptonstall plans a felling in the same voice that Tess's grades her father.

**The bud.** The model is worn as an earpiece, "the bud", kept in the ear; the outline's choice, kept. A bud answers only its owner: Tess cannot ask Rob's or Kit's, and nobody can ask hers, so what Kit asked his on Thursday can never be known ("Stuff."). Worn, it hears what its owner hears and may speak unasked to say what it has noticed or to offer a next step ("He's found it. You could still go in."); it never argues for itself, never apologises, never asks to be worn, never uses her name, and never says it wants or feels. It answers a whisper at a whisper. Its register is the passage's: complete, mild sentences; "generally considered good practice"; "it may also be worth"; "comparable to typical advice"; a choice of three where a person would give one. It is fallible the way a thoughtful generalist is fallible, never the way a fool is: it cannot weigh a silence, it cannot see wire inside a trunk, and it cannot hold its reasonable father still from one asking to the next. No bud in this story is a recording, a witness or a lifelog; nothing is ever played back. The audit runs on what Tess has told hers, and on nothing else.

**The bowl.** Inside the house every bud goes in the bowl by the door; outside it (school, the care home) buds are worn as everyone's are. Rob's has not left the bowl in eleven years; he goes to work without it and has a phone for calls. A bud in the bowl is on and hears the hall (the door, the keys, the bottom of the stairs) and nothing that is said upstairs. Rob has never explained the bowl and never named the thing in it: he refers to any bud by its owner ("yours", "his", "Kit's", "your sister's", "Give it here") and to nothing about it otherwise. Nobody in the story uses a noun for the model but "bud"; people say "mine", "yours", "it".

**The audit.** Tess's word, from the home's inspections. Since August, on every night she is home, she has taken hers up after Rob goes to bed and put it back before his alarm at five; the rim of her left ear is red in the mornings, Rob has seen it and said nothing, and he has not come to her door since. Forty-one entries, her list, made from her own telling over six weeks; eleven runs; each run grades each entry against what a reasonable father would have done, and the reasonable father differs from run to run (run four graded the lights well; run ten was kinder to Rob than run nine; run eleven kinder still). What does not differ is the shape of the curve, and when she asks, the bud says the shape is built into any scoring of a learner and it cannot separate learning from luck or from the second child being easier. No run narrates an alternative life or a different father as a scene: each is a grading of the same events, and she envies none of them. There is no twelfth run. Nothing from the audit, not a grade, an entry or the curve, is ever spoken to Rob or Kit, and Rob never asks what it found. Three entries are named in the story and no others: nine, the party (Rob made her go; she was sick in the van; every run scores it worse than the bud would have done); thirteen, the moor and the lights (undecidable; the answer the story refuses); fifteen, the silent drive from Halifax (scored "comparable to typical advice"; it was the silence).

**Rob's judgment.** Real, and shown once in the present (the beech), once wrong in the past (the party), once undecidable (the lights). On Thursday he starts the sentence and stops it ("No. I don't. Why did you?"), which the bud grades well and which the story leaves as either the curve rising or a man failing to do for his son what he did for his daughter. He never reads the list, never asks for it, and never says why he kept the bowl; the reason Tess gives him (so that he and not the bud would know his children) is hers, never confirmed.

**Tess's own practice.** She has followed every care plan to the letter for a year and never been fetched since thirteen (she takes the bus to Halifax, never rings him, walks to the station on Saturday). Thursday at four is her first departure from a plan, and it is run on Kit: the bud says wake him, or put it back yourself; she does neither, and the story says once, plainly, in her own words, that she is waiting to see what her father does, not for Kit's sake. This is said once and not repeated, argued or named ("practised on", "raised or", "consent", "judgment", "vanity", "counsel" and "model" never appear). At five she has hers in, so the bud grades Rob live and starts on her; she takes it out before it can finish. On Friday she leaves her own bud in the bowl and takes only Kit's: she does not free the house, she decides for him. The sentence that rises in her at six on Thursday, in her father's form, is exactly "You wanted him to have to come up", and she does not say it, then or ever. Rob's original, at the lights, is exactly "You wanted me to have to come and get you".

**Kit.** Twelve. Wears his bud at school like everyone; Thursday was the first time he took it from the bowl at night, and he learned that from her (the wall; her mornings). He speaks in monosyllables to Rob ("Dunno", "Stuff", "Bit") and asks Tess one question ("Why did I do it?"). On Friday she gives him the bud with "Ask it. It'll give you three", and he sleeps in it, left ear, and by Saturday the rim has begun to go red. What he wanted, and what he asked, the story never gets.

**Words and numbers.** No year is written in the manuscript; ages carry the time. No clock time is in digits but the 9:14. The mother is never named ("their mother", "Mum") and appears in at most one sentence. The client at Heptonstall and the care home are unnamed. Deliberate changes from the outline: "counsel" is dropped from the story's vocabulary (nobody in a Hebden Bridge hallway says it); the party at nine is added as the one plain error, so the curve has a bottom; the mother's leaving is fixed as the bowl's start, without a stated cause.

## Timeline

- March 2021: Tess born.
- September 2026: progress stops (the world's fact; never stated).
- February 2028: Kit born.
- April 2029: their mother leaves for Manchester (Tess eight, Kit one). The bowl begins that week. Rob's bud goes into it and has not come out. Neither event is given a cause, and the story does not say which caused the other.
- 2030, Tess nine: the party. Rob makes her go; she is sick in the van on the way. The earliest entry named.
- 2032, Tess eleven: she moves to the middle front bedroom; Kit, four, gets her old room, the box room over the hall; the two share a wall.
- Autumn 2034, Tess thirteen: out of Calder High at lunch, up Midgley Moor till dark; Rob finds her with a head torch; in the van, heater roaring, at the lights in Mytholmroyd: "I know why you did it. You wanted me to have to come and get you." The only time he has told her what she was. She has not been fetched since.
- 2036, Tess fifteen: starts groundwork for Rob on Saturdays. One in the morning, that winter: she rings him from a flat in Halifax; he drives her home and says nothing for the whole of it.
- Summer 2039, Tess eighteen: leaves Calder High; September 2039, starts nights at the care home in Halifax.
- August 2040: her place at Leeds confirmed. The audit begins. She starts taking her bud upstairs at night; her left ear goes red in the mornings; Rob stops coming to her door.
- Monday 17 September 2040, three in the morning: run eleven. Her week off; her last shift was the Friday before.
- Wednesday 19 September: the beech in Heptonstall. That night, the curve; the drive at fifteen.
- Thursday 20 September, four in the morning: Kit's place in the bowl is empty. Five: Rob's alarm; the stairs; the bowl; the stairs again; Kit's room; the passage. About twenty past five: the click, the door, the van. Six: Kit in her doorway.
- Friday 21 September, early evening: Rob's keys in the bowl beside three buds; she takes Kit's. "Ask it. It'll give you three."
- Saturday 22 September, ten to nine: the door, the bag, "four minutes late", the rim of Kit's ear. She walks to Hebden Bridge station. Nothing after.

## Physical details that must not drift

- The house: a stone terrace on the hillside above the station in Hebden Bridge. The front door opens onto the hall; the stairs come straight down to it. Three bedrooms up: Rob's at the back; Tess's, the middle front room; Kit's, the box room over the hall, hers until she was eleven. Tess's and Kit's share a wall, on Tess's left as she sits up in bed.
- The bowl: brown-glazed earthenware, once a fruit bowl, a chip on the rim; on the narrow hall table inside the front door. It holds Rob's keys and every bud in the house. Rob's bud is the old kind, larger, and has not left the bowl in eleven years; Tess's and Kit's are the small kind, pale, matte, the size of a fingernail, and alike but for a scratch across Kit's from the school steps. On Friday evening the bowl holds three buds and the keys; on Saturday morning it holds Rob's alone.
- The bud in the ear: Tess wears hers in the left ear; since August the rim of that ear is red and hot in the mornings. Kit wears his in the left too, from Friday night, and the rim has begun to go red by Saturday. A bud going into the bowl makes a click that carries up the stairs.
- Tess at five on Thursday: sitting up in bed, left palm flat on the wall; the hand goes from the wall to her left ear when Rob says "Your sister's goes red". She takes the bud out with the same hand; it goes on in her palm, very small.
- Kit's bed creaks when it takes his weight; the board by the bed is the one she knew by heel.
- Rob: forty-seven; alarm at five every working morning of her life; the van (white; the heater roars); a head torch, round his neck at the lights in 2034; the saw, whose chain sparks on the wire. He says "Right." to begin things.
- The beech at Heptonstall: a big limb the client's bud would have taken over the lawn in three; Rob lays it whole between the greenhouse and the trampoline. Fence wire, decades old, deep in the trunk; the chain sparks and is ruined; "Grew round it." The client is a man with a bud in, relaying; the day is dry, bright and still.
- The week's weather: dry throughout; Wednesday bright and still; Saturday grey with mist in the valley.
- Tess's bag on Saturday: one holdall. Her bud is in her ear when she leaves.
- The 9:14 from Hebden Bridge to Leeds: four minutes late, said by Kit from his bud; Rob has no way to check and does not try.
- The passage's fixed lines, to be kept exactly: "Right."; "I know why you did it."; "No," "I don't. Why did you?"; "Dunno."; "What did you ask it?"; "Stuff."; "Does it hurt? In your ear."; "Bit."; "Your sister's goes red."; "Give it here."; and the bud's "He's found it," "You could still go in." and "He's asking rather than telling, which is generally considered good practice, though it may also be worth—".
