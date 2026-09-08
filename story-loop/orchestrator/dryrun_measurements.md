# Dry-run verdicts as they arrive (order: judge / pair / order / choice / conf)
a / cal / AB / A / 5   -> true draft chosen (A was the draft)   tokens 40923
b / cal / AB / A / 5   -> true draft chosen                     tokens 40590
b / cal / BA / B / 5   -> true draft chosen (B was the draft)   tokens 40751
a / cal / BA / B / 5   -> true draft chosen                     tokens 41846
CALIBRATION: both judges caught in both orders.
writer: 80372 tokens, 8 tool uses, 396 s; said 446 words, check_manuscript counts 480.

## Re-run on the FINAL text (446 words), draft body sha 6cf5a9a4..., pair sha 3b4edcd3...
INLINE (0 tool uses): a/cal/AB/A/5 38254 tok 4.9s ; a/cal/BA/B/5 38661 tok ; b/cal/AB/A/5 38250 ; b/cal/BA/B/5 38243
=> calibration: both judges caught, both orders. Fixed per-call overhead ~35-38K tokens even with no reads.
LESSON: sub-agent fixed context ~35K tokens; 3-read judge ~41-50K; inline ~38K. No cheap path. Budget per round with 2 judges: 28-36 verdicts x ~45K = 1.3-1.6M + critics + writer ~= 1.7-2.0M.
ONE-FILE judges (1 tool use) on the exemplar pair: a/ex/AB/A/4 48724 ; a/ex/BA/B/4 48763 ; b/ex/AB/A/4 47259 ; b/ex/BA/B/4 47283
=> draft WINS 'ending' vs The Star outright (both orders, both judges). Cost ~same as 3-read (~50K). Fixed overhead dominates.
round-01.json: passes at --milestone 3; at --gate 3 fails on (1) exemplars 1 < 4, (2) supplied-text pairs 1 < 3. Check works as designed.
Observation: all four verdicts quote the same two sentences and give near-identical reasons; two models, one taste. The design's 'same judge' worry (§11.4) is live even with model rotation.
OVERHEAD PROBES (trivial prompt, haiku): Explore type = 18864 tokens floor.
general-purpose floor = 29113; claude floor = 29243. subagent_tokens counts NEW tokens per agent (base context once + reads + output), not re-reads.
Cost model: verdict ~ base(29K default / 19K Explore) + texts (~10K) + output(~0.5K). 
Spent so far (approx): orchestrator ~290K (15M counter), sub-agents ~870K + critic pending => ~1.2M incl. setup + dry run.
EXPLORE-type judge on ex-AB one-file prompt: choice A, conf 4, same quotes, sound reasoning; 34538 tokens (vs 47-49K default type). => use Explore type for judges (~28% cheaper); critics likewise, returning the report in the reply for the orchestrator to save verbatim (Explore cannot Write).
depth-critic: 66802 tokens, 3 tool uses, 404 s; 1 MAJOR 4 MINOR 2 NIT; report shape correct; check_reviews demands disposition. Passed F1,F5,F6,F7 to the writer; F2,F3,F4 to be DEFERRED.
