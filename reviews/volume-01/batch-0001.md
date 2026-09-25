# Review — Batch 0001, Volume 01, Chapters 1–10

Reviewed phase: `batch-0001` (commit `989b1df`). Source log: `logs/batch-0001.review.log` (gitignored, hence this file).

**Verdict as received:** the batch is strong — ten complete scenes, no outline padding, no duplicate paragraphs, POV plan matched, the six-name cap respected, and **exactly two Gatehouse lines** (Ch 4 and Ch 8), verified. Exactly one next-batch prompt exists, so the dispatch guard holds. The defects are concentrated in **date and provenance bookkeeping**, and most of them sit in the state files the next writer is told to read first.

## Disposition summary

| # | Severity | Finding | Where fixed | Status |
| --- | --- | --- | --- | --- |
| 1 | P1 | "Twenty-four days ago … YR 302" contradicts itself in one line | `chapter-0007.md` | Fixed |
| 2 | P1 | Bell identity unresolved and load-bearing — one bell in two places | `chapter-0007.md`, `state/continuity.md` 37, `state/open-threads.md` 12, prompt | Fixed |
| 3 | P1 | Three different numbers for one court ruling | `chapter-0010.md`, `state/batch-summaries.md`, `state/continuity.md` 43, prompt | Fixed |
| 4 | P1 | Batch summary restates the seizure as "on or about the twenty-first" | `state/batch-summaries.md` | Fixed |
| 5 | P1 | Four marks change owners at the handoff | `workspace/volume-01/batch-0002/PROMPT.md` (Ch 11, Ch 20) | Fixed |
| 6 | P1 | Date arithmetic in the handoff ("four days to the second of Greenmonth") | `state/open-threads.md`, `state/batch-summaries.md`, `state/current.md`, prompt | Fixed |
| 7 | P1 | Ch 9 misattributes the fever figure to the gallery woman | `chapter-0009.md` | Fixed |
| 8 | P2 | Ch 15's pull restates the ninth-of-Greenmonth summons | `workspace/volume-01/batch-0002/PROMPT.md` | Fixed |
| 9 | P3 | Word count wrong in two places (36,600 vs 39,561) | `state/current.md`, `state/batch-summaries.md` | Fixed |
| 10 | P3 | Ch 10 is 1.75× the pack median and its last third sags | `chapter-0010.md` | Fixed by removal of duplication — see below |
| 11 | P3 | Uniform dialogue tags | — | No change — see below |
| 12 | P3 | Ch 2 hands the surety to the clerk instead of to Aren | `chapter-0002.md` | Fixed |
| 13 | P3 | Ch 9's factor has no want and no decision | `chapter-0009.md` | Fixed, cap-compliant |

## Detail

**1. Ch 7 date.** The bell went on a Crown clearance roll in **YR 302** and came off the block at Merefen on the first of Mudmonth, YR 312, so "twenty-four days ago" was wrong and self-contradicting inside a single sentence. Replaced with the year arithmetic the chapter's own dates support: *ten years ago, and one year after the writ.* The reviewer noted that a marked lie would be better material than a slip, given the Quen lecture that follows about knowing who else is selling you the truth. **A lie was rejected** — it would contradict the sworn account Aren's files in Ch 10 and the third of the bench's terms. The contradiction is instead resolved inside the same speech, which is what finding 2 needed anyway.

**2. Bell identity.** This is the volume's hinge and it now says so on the page, in Aren's own flat sentence to the bench: nine stone, split lip to shoulder, the founder's mark on the shoulder is the Bellweather founder's mark and he read it in a Merefen scrap yard before he came up the north steps; the same bell is under a tarred cloth in Bellweather's yard **and** was on an iron cradle in Merefen, and he rang it in Merefen, and both are true and he cannot make them agree. The Crown's own Merefen entry reads *unclassified salvage*, no city, no river, **YR 302** — which is the proof that the north has had the bell and cannot say where from. This reads as an anchor in two places, not as a plot hole, and continuity item 37 now states it as **settled fact rather than open mystery** so a later writer cannot "fix" it into a twin, a copy, or a time-diverge.

**3 and 4. The seizure's numbers.** One figure: **three days**, from the sixteenth (the day on the paper) to the morning of the nineteenth (the bell off the abutment). That is the damning number, because it means the whole seizure was executed in three days off a document that predates the storm. **Eight** is how long the cradle stood empty when Aren returned on the twenty-seventh; **nine** is how long he was gone. The prose, the batch summary, continuity item 43, the current-state file, and the Batch 0002 prompt now all say three days, and each says explicitly which figures not to use.

**5. The four marks.** Ch 9 gives them to Tovan twice; Ch 10 restates it from Aren's side; the Ch 20 card already said Tovan has the money and will not be asked. Only the Ch 11 card had them with Aren, and it had them in the sentence that opens the batch. Corrected there, and the Ch 20 card's resistance was also broken because **Aren had one and a quarter and had to pay four** with no stated source. It now points at the two ways Chapter 19's ending already set up and requires the batch to be clear about which one pays before the glass is cut. Aren's actual position (a shilling a day, eleven days of unpaid wages, about a mark and a quarter) is recorded once in continuity item 48 and in the prompt's standing facts.

**6. Date arithmetic.** Ch 11 opens on the **first** of Greenmonth, so the renewal on the second is a day after tomorrow, not four days out, and the hearing of the fourth is three days from the opening. Fixed in both state files. While fixing it, an unstated fact surfaced: **Mudmonth's length is fixed nowhere in the bible or the outlines**, so any count running forward from the twenty-seventh can be off by one. The Ch 18 card's "Eleven days now, since the twenty-seventh" was re-anchored to the renewal ("five days after the renewal"), and Ch 20's pull was de-numbered. Both now say why.

**7. Fever figure.** In Ch 5 the number two hundred and eleven comes from **the ferryman on the bank**; the gallery woman's contribution is *How would you know?*; and the woman who keeps her shutters shut lives on Ferry Lane. Three women. Ch 9 gave the number to the gallery woman and the batch summary merged her with the Ferry Lane woman, so a single fever had been spread across two errors. All three are now named separately in the prose, in continuity item 36, in `open-threads.md`, and in the Batch 0002 prompt.

**8. Ch 15's pull.** The card ended the hearing on the clerk reading the ninth-of-Greenmonth summons — which Ch 10 already put on a magistrate's table **in full, in front of Mara, six days earlier**. The card's own genuinely new material is Bram Ottery's unsought statement naming the man who was told the bell was the fever's. That is now the chapter's landing, with the summons demoted to a note by the clerk, and the watch-sergeant set up early in Rell's hearing so the room can turn at the end. The midpoint paragraph was corrected to match, since the batch's discovery is the *hole under* two already-public summonses, not the summonses.

**10. Ch 10's length — partially fixed, deliberately.** The reviewer offered two remedies: split at the clamp beat, or move the eleven-marks ledger page into Ch 11's cold open. **Both were rejected as plot changes.** Renumbering would break the ten-chapter plan, the day map, `chapter-summaries.md`, and the one-prompt-per-batch guard. Moving the ledger out of Ch 10 would gut a beat that is load-bearing twice: it is the moral argument of the whole batch (a record is not an argument) and it is continuity item 40, which the volume's climax builds on.

Reading the sag closely showed it had a specific and fixable cause: **the exhibit-goes-under-the-account beat appears three times** — as a rule in Lysa's speech, as a restatement in the following paragraph, and as the dramatised act of her physically putting the sheet at the bottom of the stack. The hearing date is stated three times. The clause "a document is slower than a man and lasts longer" appears twice in adjacent paragraphs. A miscount ("I am going to tell you two things" followed by three numbered items, the second of them also labelled "Two") compounded it. The restatement paragraph was cut to the one thing in it that is genuinely new — the renewal's date and what it does to the file's weight — and the numbering fixed to three. Prose preserved; nothing cut that was doing work.

**11. Dialogue tags — no change.** The review's own measurement does not support the finding: it counted 292 `said + Capital` across ~40,000 words, and found **zero** instances of the `", said` construction and zero of the `rather than said` tic. "Said" is not on the filler list in `AGENTS.md`, and 292 across ten chapters is not a pattern a reader will notice. Tagging was measured and deliberately left alone.

**12. Ch 2's surety.** The clerk now stops at "Six marks" and Aren supplies the tool-chest before the sentence is finished, with a line that registers the decision as already made rather than newly taken. The reasoning, previously arriving half a beat later at :105, now has the gesture to sit on. The clerk's "that'll be three and a half and half of it is rust" and everything after is untouched.

**13. Ch 9's factor.** He now does the sum where he stands, has a want that has nothing to do with a bell or a road (to be a man who has not eaten the loss), and takes a decision (cut new stock at the western end so the stone becomes somebody else's problem for a season, carrying the difference out of a year instead of a quarter). He still says he will come back on the first and ask again — Ch 17's card has him asking — and he is still **addressed by office**, so the six-name cap is untouched. The batch's strongest minor character now recurs across two batches with something of his own.

## Not changed, on purpose

- **No plot moved.** No chapter was renumbered, split, or removed; no planned beat was cut; the ending outline and `outline/volume-01.md` were not touched; no final enemy was introduced.
- **`state/phase-ledger.json` was not edited.** It is controller-owned, stale by design, and not what dispatch reads.
- **`workspace/volume-01/batch-0001/PROMPT.md` was not edited.** It is the record of the phase that already ran.
- **No second prompt was created.** `workspace/volume-01/batch-0002/PROMPT.md` remains the only Chapters 11–20 prompt.
