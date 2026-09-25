# Current State

Current phase: outline (Volume 01 and Batch 0001 planning)

Current volume: 1

Current batch: 1

Last completed chapter: none

Last batch summary: none yet. Completed batch summaries are appended to `state/batch-summaries.md`, and this field names the most recent entry.

File convention, for the next phase: write `chapters/volume-01/chapter-0001.md` through `chapters/volume-01/chapter-0010.md` for this batch — four digits, matching the `### Chapter 0001` card labels in `outline/batches/volume-01-batch-0001.md`. `PHASE_SYSTEM.md` is the authority and is controller-owned; do not edit it, and do not improvise a different path.

Canon status: The bible, series outline, and ending outline are established. `outline/volume-01.md` (Chapters 1–50) and `outline/batches/volume-01-batch-0001.md` (chapter cards for Chapters 1–10) are written, mutually consistent, and carry a reviewed fix pass. No chapter prose has been generated.

Active threats:

- **Merefen watch captain Rell**, holding a sealed emergency order from Marshal Edric Hunn's office, written and sealed *before* the anniversary. He believes the cracked bell caused the fever recorded after Bellweather. In the plan, Rell seizes the bell during Aren's first absence and delivers the seizure in Chapters 8–10.
- **The private-keeper clause**, applied to Aren in provincial correspondence for reasons no character can explain. Nobody in Volume 01 learns why he can cross.
- **The Bellweather Bridge Guild's debt**, the toll houses' push to reopen the northern trade, and the outer arch's moving crack: the path's own problems, which are not waiting for Aren.
- **The path continues without him.** The longest quiet stretch in Volume 01 is deliberate.

Active promises:

- The Bellweather Sundering's official account is false, and Edric Hunn signed the fatal cull order. In Volume 01's midpoint, the toll-house outgoing writ register names him.
- The Gatehouse preserves living continuations and cannot reset them while conscious life exists.
- Aren's mother Ilyra crossed a sealed path to save him; her exact fate remains intentionally unresolved and is not touched in Volume 01.
- Aren and Mara Vey's slow-burn relationship begins as hostile cooperation over custody of the evidence.
- The final resolution is a distributed Charter of Many Roads, not a single ruler's perfect world.

Current relationship pressure: Aren and Mara have a custody fight, not a romance. Tovan has stated the volume's refusal — he will mend the bridge, he will not hold the road. Aren's relation to Edric is unexamined devotion that Volume 01 begins to sour without resolving.

Current power state: Stage 0 at the opening, and still Stage 0 at the end of Chapter 10. The first crossing pays the roadmark and the lost verse-pitch immediately, nine days of main-world calendar against a warning of three, and **three days of fever, the twenty-seventh to the twenty-ninth, breaking on the thirtieth**. Stage 1 requires a second crossing plus an informed local consent, so it is reached at Volume 01's climax (Chapters 41–47) and not before.

Fixed story frame for Chapter 1: **YR 312, Mudmonth, the sixth day**, in Merefen at flood stage. The eleventh anniversary of the Sundering falls on the **nineteenth of Mudmonth**, in the storm that night. Volume 01 runs from the sixth of Mudmonth to the last week of Fallowmonth, about five months of main-world time, with three crossings whose longest path interval is six months and twenty days.

Batch 0001 day map, which the chapter cards now share: Ch 1 the sixth · Ch 2 the eleventh · Ch 3 the twelfth · Ch 4 the night of the eighteenth into the nineteenth · Ch 5–7 path time, no main-world clock · Ch 8 the twenty-seventh · Ch 9 the twenty-seventh to the thirtieth · Ch 10 the thirtieth. The thirteenth to the eighteenth is a stated cut with nothing in it.

Next planned phase: this fix pass closes `phase-001-outline`; the runner marks the phase done, and the next dispatch in sorted order is `workspace/volume-01/batch-0001/PROMPT.md` — Chapters 1–10 as finished prose. **Exactly one prompt may exist per batch.** Do not create a second Chapters 1–10 prompt, and do not recreate `workspace/phase-002-batch-plan/`, which was deleted for exactly that reason.

Standing pipeline guard: `state/phase-ledger.json` is controller-owned, is never written by the writer, is stale by design, and is not what dispatch reads — dispatch reads the sorted `workspace/**/PROMPT.md` files. `AGENTS.md` says to update the ledger and the writer agent's rule forbids it, and the runner's restore list does not include the ledger, so nothing will undo a careless edit. Leave it alone.

Last change: the outline phase, plus a reviewer fix pass on it. `outline/volume-01.md` and `outline/batches/volume-01-batch-0001.md` were filled in from their structured templates; the fix pass then corrected the batch's date arithmetic, the fever's length, the brine-weight double spend, the empty-cradle contradiction, the Hushwater headcount, the two-guild collision, and the units, and recorded the decisions in `state/continuity.md` items 15, 22, and 24–31. The reviewer's findings and their dispositions are persisted at `reviews/volume-01/outline-phase-0001.md`. No prose, no volume plot change, and no controller file was edited.
