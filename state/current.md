# Current State

Current phase: batch writing (Volume 01, Batch 0001 complete; Chapters 11–20 are next)

Current volume: 1

Current batch: 1 complete; next batch is 2 (Chapters 11–20)

Last completed chapter: `chapters/volume-01/chapter-0010.md`

Last batch summary: the **Batch 0001 — Volume 01, Chapters 1–10, "The Nineteenth of Mudmonth"** entry in `state/batch-summaries.md`. Read that entry first; it carries the canon the batch invented and the question Chapter 11 opens on.

File convention: chapter files are `chapters/volume-01/chapter-0001.md` through `chapter-0010.md`, four digits, matching the `### Chapter 0001` card labels in `outline/batches/volume-01-batch-0001.md`. Batch 0002 continues the same convention at `chapter-0011.md` through `chapter-0020.md`.

Canon status: the bible, series outline, ending outline, `outline/volume-01.md` (Chapters 1–50), and `outline/batches/volume-01-batch-0001.md` are all established. **Chapters 1–10 exist as finished prose**, ten complete scenes, roughly 36,600 words, POVs Aren ×8 / Mara ×1 / Tovan ×1, with exactly two Gatehouse lines in the whole batch. Per-chapter summaries are in `state/chapter-summaries.md`; the canon the batch established is `state/continuity.md` items 32–42; the new threads are in `state/open-threads.md`.

Active threats:

- **Captain Rell and the watch**, holding a bell under a Crown seal in a storehouse by the fish weir, on an order dated the sixteenth of Mudmonth, before the storm and before the anniversary. A second letter, dated the twenty-ninth, again names Aren road-keeper of Merefen and summons him to the provincial town on the ninth of Greenmonth. Lysa Fenn's hearing on the seizure is set for the **fourth of Greenmonth**; the province's renewal is the **second**.
- **The private-keeper clause**, applied twice to Aren in documents nobody can source, and Lysa has searched three registers for the office and found nothing.
- **Bellweather-Living's own problems**, running without him: a moving crack in the outer ring of the second pier, a new cutwater nine months long that the debt forbids, forty-one toll-houses three of which want the northern trade reopened badly enough to be arguing with a stranger, and a register page offered to him in exchange for one in a year.
- **The path continues without Aren.** He has promised the bench to return and has no way to, and at Stage 1 he has no way to send or receive a word.

Active promises:

- The Bellweather Sundering's official account is false, and Edric Hunn signed the fatal cull order. In Volume 01's midpoint, the toll-house outgoing writ register names him. The counterfoil that proves a writ was sent, sealed, dated, and unsigned on the stub is now in the Archive.
- The Gatehouse preserves living continuations and cannot reset them while conscious life exists.
- Aren's mother Ilyra crossed a sealed path to save him; her exact fate is intentionally unresolved and untouched except as the verse whose pitch he has lost.
- Aren and Mara Vey's slow-burn relationship begins as hostile cooperation over custody of the evidence, and the undated promise is the shape of it.
- The final resolution is a distributed Charter of Many Roads, not a single ruler's perfect world.

Current relationship pressure: Aren and Mara have a filed exhibit, a broken undated promise, and a working disagreement about what may share a page. Tovan has stated the volume's refusal — he will mend the bridge, he will not hold the road, will not keep the secret, and will not be the man holding the span — and the refusal has not been answered. Aren's relation to Edric is unexamined devotion that has begun to sour without Edric appearing in person.

Current power state: **Stage 0 with a roadmark, still unqualified.** The first crossing paid the roadmark, the lost verse-pitch, nine days of the main-world calendar against a saying of three, a crossed scar on the Old Toll sill, and three days of fever that broke on the thirtieth. One carryover exists: the motion of a narrow Mend, which came back in his fingers unbidden and cannot be reproduced without a stone, a narrow bound, and a teacher, and which he does not have. **No return stitch is prepared and none can be until the sill is mended with anchor-glass — two Steppe discs, four marks, money before cutting.** Stage 1 needs a second crossing plus an informed local consent, and is reached at the volume's climax (Chapters 41–47) and not before.

Fixed story frame: **YR 312, Mudmonth to Fallowmonth**, in Merefen at flood stage. The eleventh anniversary of the Sundering fell on the **nineteenth of Mudmonth**, in the storm. Volume 01 runs from the sixth of Mudmonth to the last week of Fallowmonth, about five months of main-world time, with three crossings whose longest path interval is six months and twenty days.

Day map so far, main world, Mudmonth YR 312: Ch 1 the sixth · Ch 2 the eleventh · Ch 3 the twelfth · Ch 4 the night of the eighteenth into the nineteenth · Ch 5–7 path time, no main-world clock · Ch 8 the twenty-seventh · Ch 9 the twenty-seventh to the thirtieth · Ch 10 the thirtieth. Markets in Mudmonth fall on the fourth, ninth, fourteenth, nineteenth, twenty-fourth and twenty-ninth; the market of the nineteenth was lost to the storm and the twenty-fourth was lost to the shut road, and the twenty-fourth was put off to the twenty-seventh. **Block 2 runs from the thirtieth of Mudmonth to the fourth of Greenmonth**, with the province's renewal on the second.

Next planned phase: `workspace/volume-01/batch-0002/PROMPT.md` — Chapters 11–20 as finished prose, Block 2, "What the fever cost everyone else." **Exactly one prompt may exist per batch.** The Batch 0001 prompt directory stays on disk as the record of the phase that ran; do not rewrite it, and do not create a second prompt for Chapters 11–20 anywhere else.

Standing pipeline guard: `state/phase-ledger.json` is controller-owned, is never written by the writer, is stale by design, and is not what dispatch reads — dispatch reads the sorted `workspace/**/PROMPT.md` files. `AGENTS.md` says to update the ledger and the writer agent's rule forbids it, and the runner's restore list does not include the ledger, so nothing will undo a careless edit. Leave it alone.

Last change: Batch 0001. Ten chapters written to `chapters/volume-01/`, then the batch summary, chapter summaries, continuity items 32–42, the relationship state, and the open-threads file were updated, and one next-phase prompt was created for Chapters 11–20. The Batch 0001 prompt directory was left in place as the record of the completed phase. No controller file was edited.
