# Review: phase-001-outline, fix pass

**Phase:** `phase-001-outline` — Volume 01 outline and Batch 0001 chapter cards.
**Reviewed commit:** `5342184` ("novel: save writer work phase-001-outline").
**Reviewer output:** `logs/phase-001-outline.review.log` (gitignored; persisted here so the quality gate has a record).
**Disposition:** all 21 findings and four meta/wording artifacts applied, in two passes. A verification pass over the first round found six defects, five introduced by the fix itself, and all six are corrected below. No plot beat moved, no chapter card removed, no controller file edited.

## Blocking contradictions in the delivered outline

| # | Finding | Fix |
| ---: | --- | --- |
| 1 | The guild's removal notice was dated the eleventh but reached Aren on the seventh. | Chapter 2 moved to the **eleventh**, the day the notice arrives and the day it is dated. The card's "eight days before the anniversary" now computes correctly. A day map was added to the batch header so the shift cannot be half-applied. |
| 2 | "Eleven days ago" for the bell purchase; the first of Mudmonth to the sixth is five. | Corrected to **five days** in the batch's starting condition, the Chapter 1 card, and `state/continuity.md` item 15. |
| 3 | Chapter 3's pull counted thirteen days to the anniversary from the eighth. | Chapter 3 moved to the **twelfth**; the pull now reads **seven days**, and the count is no longer copied forward from Chapter 1. |
| 4 | The fever was three, four, and five days in three cards. | One number, propagated: **three days, the twenty-seventh to the twenty-ninth, breaking on the thirtieth**, which is the day Chapter 10 opens. Fixed in the batch header, the Chapter 8, 9 and 10 cards, the volume time budget, and `state/continuity.md` item 25. The crossing budget in `state/continuity.md` was also corrected: three days is the figure at Stage 0 as well as Stage 1, since the first crossing is a Stage 0 crossing. |
| 5 | The empty cradle was "still empty in Chapter 50" while the volume's final image has the bell back on it. | `state/continuity.md` item 22 corrected: the empty cradle is the Chapter 8 plant; the bell returns to the bridge during the Block 5 resolution, banded and re-sealed, and never returns to Aren. A matching bullet was added to the volume's concrete resolution so the return has a reason on the page. |
| 6 | Ferris Oat's brine weights were spent as a payoff in Chapter 3, Chapter 10, and Chapter 48–50. | Kept as a **cited authority** in Volume 01 — the extract Mara trades in Chapter 3 — and removed as a filed exhibit from Chapter 10 and from the Ch 48–50 resolution, which now files the writ register page instead. The named roll of the dead built out of the weights stays reserved for **Chapter 892**. |
| 7 | The third crossing's drift was three weeks against a ledger that allowed three to ten days. | The **series ledger** was widened rather than the plot changed: Volume 01 now allows three days to three weeks of uncertainty at return, and the volume outline states that three weeks is the ceiling at this scale. `state/continuity.md` item 29. |

## Rule and world consistency

| # | Finding | Fix |
| ---: | --- | --- |
| 8 | "Eleven fingers" was applied to a survey gauge in Chapter 1. | Recast as the argument it should be: a ferryman's folk reading, a three-day-old written gauge board, and Aren believing the man with the boat. `bible/terminology.md` now states that fingers are folk measure, that a surveyor never quotes them, and that a written table never reads in fingers. The Chapter 5 card is marked as the deliberate echo of that same lesson, learned from strangers. |
| 9 | "The guild" named two institutions in consecutive chapters. | The main-world body is named and bounded: the **Merefen bridge guild**, the town's craft body holding the Old Toll crossing in municipal trust. Added to the volume's faction list, to the batch header, and to `state/continuity.md` item 27. Both guilds now also carry their full name the first time they appear inside a card — the Merefen guild in Chapters 1 and 2, the Bellweather Bridge Guild in Chapters 5 and 6 — so the reader is never left to infer which one a scene means. A third variant, "the Bellweather-Living bell guild," was removed from `state/current.md`. |
| 10 | Hushwater Reach had about eighty living souls and Hushwater had exactly eighty erased. | Decoupled. The cooperative counts **ferry hands and hearths, not souls**, so the hamlet's nearest estimate is **near sixty**, and `bible`-locked figures stay untouched. Updated in the volume outline, `state/continuity.md` item 24, `state/open-threads.md` thread 10, and the Chapter 7 card, with an instruction that no character notices the gap. |
| 11 | Chapter 10 invented a salvage claim and dated it eleven days ago. | `bible/characters.md` already establishes that a Merefen magistrate filed Aren's salvage claim after the Sundering; the eleven years and the YR 301 date are now recorded in that entry, and the filing is separated from the bell in the Chapter 10 card and in `state/open-threads.md` thread 7. **The contents of the filing are not stated anywhere.** A phrase in an earlier draft of the card — that he came back "with what the inquiry left him" — was cut in verification because it gestures at the contents the same fix promises never to name. |
| 12 | "Two and a half hundredweight" is not a Neyra measure; "four timber-equivalent masses" is unclear diction. | `bible/terminology.md` now forbids hundredweight, fixes the bell at **nine stone**, and explains that a bell is lifted by its headstock, never by its body — which the Chapter 4 card uses. The Chapter 5 line is now "one four-bay timber bridge that he is reading the way he reads Sedge Reach at home." |

## Structure the writer would have hit

| # | Finding | Fix |
| ---: | --- | --- |
| 13 | Ten unaccounted days between Chapter 3 and Chapter 4. | A "days the cards do not cover" section states all three cuts, what may happen in them, and what may not. The thirteenth to the eighteenth is an interval with no visitor, no document, and no bell sound. The volume time budget now lists the same days. **The first round of this fix also introduced a hole here** — a one-week hold signed in Chapter 1 would have lapsed on the thirteenth, inside the declared empty cut, with nothing to say why the bell was still on the cradle. The hold now runs to the guild's next sitting on the twenty-fourth, which is after the storm, so the bell's presence needs no explanation and the paper the watch overrides becomes a fact worth having. |
| 14 | The promise to Mara was worded two ways, which decided whether Chapter 4 was a betrayal. | The **open-ended** wording is locked: she refuses to date the promise, and Chapter 4 is a broken promise rather than a technicality. Fixed in the Chapter 3 card, `state/continuity.md` item 28, and `state/open-threads.md`. The euphoria in Chapter 4 now costs him something. |
| 15 | Chapter 10 counted one lie of omission; Chapter 2 was a second. | Chapter 2 now states the **principled choice** — six marks buy nothing, a bond puts the bell in his name, and he would rather be answerable than be free — and the batch owns both omissions, which he files himself in Chapter 10. |
| 16 | Two forward leaks. | Chapter 1's pull no longer announces a bond that does not exist until Chapter 2. Chapter 2's pull no longer reports a visitor waiting at his door; Mara now finds him the way the outline says she does, by asking the ferrymen who signed the sill. |

## Meta artifacts and wording removed from canon files

- "(planned name)" deleted from Alis Merrow, and the reserve slots turned into a stated rule: a batch may name fewer than six, and a slot is never filled to fill it.
- **Aldis Fenn** is declared as Lysa's elder sister and reeve of Merefen, per `bible/characters.md`, so the volume has three known family-name threads and one accidental-looking Fenn collision fewer.
- The cast table's "new named characters" column is now "named in prose," with a note that all six Batch 0001 names already exist in the bible; `state/continuity.md` item 19 was corrected to match.
- Mara is no longer described as "a keeper with a stalled claim" or as an "archive keeper," either in the batch card or in the relationship starting point, because the volume's corrupted term is *keeper* and the Archive should not be described with it.

## Repository and pipeline

| # | Finding | Fix |
| ---: | --- | --- |
| 17 | No chapter file path was specified anywhere the writer reads. | Recorded in `state/current.md`: `chapters/volume-01/chapter-0001.md`, four digits, matching the card labels, with `PHASE_SYSTEM.md` named as the controller-owned authority. `state/continuity.md` item 30. |
| 18 | Batch summaries had no home. | `state/batch-summaries.md` created with the rules for an entry, and `state/current.md`'s "Last batch summary" field now points into it. |
| 19 | Review artifacts were never persisted. | This file. `reviews/README.md` updated. |
| 20 | The phase ledger is permanently stale and two controller docs disagree about it. | Not editable by the writer, so it is now labelled rather than changed: `state/current.md` and `state/continuity.md` item 31 both state that the ledger is controller-owned, stale by design, and not what dispatch reads, and that `AGENTS.md`'s update instruction is superseded. A future writer must not "fix" it. |
| 21 | Dispatch order was correct but undocumented, and no prompt guarded against a duplicate batch prompt. | `state/current.md` now describes the two-step dispatch honestly: this fix pass closes the phase, then the batch prompt runs. The one-prompt-per-batch rule is stated in `state/current.md` and `state/continuity.md` item 31, and a guard line was added to `workspace/phase-001-outline/PROMPT.md`. |

## Defects the fix pass itself introduced, and their correction

A verification pass over the first round of fixes found these. All are corrected in the files as they now stand; they are recorded because a later reader comparing against `logs/phase-001-outline.review.log` will not otherwise know they existed.

1. The one-week hold problem described under finding 13. The hold now runs to the guild's next sitting on the twenty-fourth, and a correction to a second bad arithmetic claim about it is recorded below.
2. The batch's undisclosed facts were counted as two in four places while three were named. Now stated consistently as **two omissions holding three facts** — to Mara, the undated promise and the night he has chosen; to Tovan, the reason for the bond — with both omissions filed in Chapter 10.
3. The volume's final image already said "a new crack sealed with dull red oathlight," which implied the bell breaks a second time with nothing to cause it. Both the image and the new resolution bullet now say **the old split**, and the resolution states that nothing in the bell breaks again in this volume.
4. The claim that the runner "reverts controller files on commit" was wrong in a way that mattered: `restore_controller_files` does not list `state/phase-ledger.json`, so a careless ledger edit would not be undone. The guard in `state/current.md` and `state/continuity.md` item 31 now says so plainly.
5. A new cross-reference cited `outline/ending.md` for the three-day fever. The ending outline states no fever length, and item 25 now says so instead of citing it.
6. The crossing budget priced the three-day fever at Stage 1 while Volume 01's first crossing is a Stage 0 crossing. The budget now reads as a Stage 0 and Stage 1 figure alike.
7. A second verification pass then found four more. `state/continuity.md` item 15 claimed the watch's order overrode the hold "six days before anyone sits" — the sitting is the twenty-fourth and the seizure the twenty-seventh, so the order replaces the town's process three days *after* it, and nothing happens on the twenty-fourth because a bench cannot act against a man who is not in front of it. The hold term is now also stated in `outline/volume-01.md`, which is where the empty cut is declared. Chapter 7 still used bare "the guild" throughout, and the batch header's chapter list named chapters that no longer use the word; both corrected. The Chapter 10 card had been cleaned of "with what the inquiry left him" but the same phrase was still in `bible/characters.md`, which is the canon file a writer reads first; it is gone. And the cards' phrase "the fourth day" for the thirtieth collided with the state file's instruction never to write a fourth day of fever — the thirtieth is now "the day the fever breaks" everywhere.

7. A latent conflict, pre-existing rather than introduced: `bible/characters.md` and `state/continuity.md` both made **Bram Ottery** the man who carries out the bell seizure, but the seizure is in Chapters 8–10 and Bram is a Batch 0002 name. Both now say the seizure is Rell's watch and its sergeant is addressed by office and left unnamed, with Bram entering by name in Volume 02 — which is also when somebody has to answer in writing. Nothing in the cards forced the collision; it would have been written into canon by the first draft of Chapter 8.

## What was checked and left alone

Village toll figures still sum to 720. The "four thousand and seven hundred and twenty are never on one page" rule holds, and the one sentence that made the two numbers ambiguous in Chapter 10 was rewritten to name them separately. Stage 0 holds throughout, with Stage 1 withheld to Chapters 41–47. The POV split is unchanged. The two Gatehouse lines stay one per threshold. The midpoint reveal stays in the toll-house counting room. The batch's midpoint and climax sit where the pacing rules want them. The planned ending was not touched: the ending outline still reserves the brine weights, the named roll, and the silent bell for Chapters 892 and 900.
