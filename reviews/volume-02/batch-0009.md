# Review of Volume 02 Batch 0009 — Chapters 81–90, "The Nine Months"

**A partly reconstructed record, and the honest reason for that is in finding 8.**

The review ran against the writer phase's commit (`novel: save writer work batch-0009`) and did its work in
`logs/batch-0009.review.log`, which is gitignored. **The session was cut off by a rejected tool call while it
was still gathering its own measurements, and it never returned a written list of findings.** What follows is
what that session had already established and verified, plus the checks run afterwards to close the list, and
the disposition of every one of them. **This is therefore closer to a disposition record with its evidence than
to a findings list, and it should be read as the second kind of file the ones marked *gap record* in
`reviews/README.md` are — the reasoning is here because it was reconstructed while it was still recoverable,
and it will not be next time unless the review phase writes its file before it ends.**

## What the review had established when it stopped

Nine findings. Every one applied, in one pass, none requiring a story change.

| # | Finding | Disposition |
| --- | --- | --- |
| 1 | **Meta-language in the prose, thirty-three instances.** Chapters 81–90 carried *this volume* thirty-three times across the ten files, plus *the volume's argument*, *the whole of the volume*, *this chapter* and *the chapter*. Two passages stepped furthest outside the fiction: **Ch 82 line 5** addressed the reader about "the following forty pages" and about "a character", and **Ch 83 line 5** addressed the reader about "waiting eleven months for a man to die". | **Applied.** All thirty-three rewritten into the room. No plot beat, fact, figure or date moved with them. |
| 2 | **The density was the finding, not the vocabulary.** Batch 0008 carries 46 such references across thirty chapters; Volume 01 about a dozen across fifty; Batch 0009 carried 32 across ten. The batch roughly doubled a rate the manuscript had been holding down for ninety chapters. | **Applied as a rule, not a cleanup.** Recorded in continuity item 234 and in the Batch 0010 prompt: the narrator may not use *this volume*, *this chapter*, *the reader*, *the author* or *this book*; **a notebook entry in Aren's hand may say *this book*, because the notebook is a physical object in his bag** — two of the three survivors are exactly that, and the third is a private book in a counting house in another country. |
| 3 | **A main-world month name had leaked into a path-time chapter.** Ch 88 said the line opened "on the fourth of Hearthmonth"; its own next paragraph said "the fourth day of the first month of the year". The County of Ash has no Hearthmonth and the batch says so twice in its own voice, and continuity item 226 uses the county's form. | **Applied.** Both paragraphs now use the county's frame and agree with each other. The guardrail that no real-world month is spoken in Chapters 81–90 is true of the prose again. **The one month left in the batch, Fallowmonth in Ch 90, is correct and was left alone: it is Mara Vey's own earlier entry in a main-world day-book, four hundred miles off.** |
| 4 | **The batch's word count was wrong in two state files, in the total and in Chapter 90.** The writer phase recorded 40,778 and a Chapter 90 of 5,827. The files gave 40,798 and 5,847, and **5,827 is Batch 0004's Chapter 39 copied across**. | **Applied, and re-measured after the repair.** The batch is **40,772**, Chapter 90 is **5,847**, the per-chapter column is 3,779 / 3,757 / 3,955 / 4,678 / 3,277 / 3,628 / 3,667 / 4,144 / 4,040 / 5,847, and the four-batch column is **151,365**. All three foot. |
| 5 | **A state file asserted a next-phase prompt that did not exist.** `state/current.md` claimed in three places that the writer phase had created `workspace/volume-02/batch-0010/PROMPT.md`. **It had not been created at all, so Chapters 91–100 had no prompt anywhere in `workspace/` and dispatch would have fallen through to the generic continuation.** | **Applied.** The prompt now exists with ten cards, the binding guardrails, the closed day map and the cast cap of two names and four unfilled slots. It is the only prompt for that block. |
| 6 | **The outline's Chapter 100 card carries a figure this batch's prose supersedes.** `outline/volume-02.md` §8 says four hundred and fifty-six tiles are going to be ground back into clay, "in Hearthmonth". On the page the number is **two hundred and fifty-four**, and the 456 is a floor of a surplus that has not been divided, multiplied, worked back from or entered on any slate, and the county has no Hearthmonth. | **Applied in the prompt and in continuity item 234. The outline was not edited** — the same handling the two hundred and fifty leagues got at the end of the Batch 0008 repair, where the error was corrected in the next-phase prompt and in state rather than in the outline, so that the outline's own record of its plan survives. |
| 7 | **The review's own findings existed only in a gitignored log.** That is the exact failure `reviews/README.md` was written to prevent, and this file is the fix. | **Applied.** This file, plus a line in `reviews/README.md`. |
| 8 | **The review session was cut off mid-measurement by a rejected tool call** — it was running the meta-language count across the earlier batches to establish whether the rate was a regression when it stopped, and never returned a findings list. | **Recorded rather than repaired.** The measurement it was running is the one in finding 2 and it was finished in the repair pass. **The process defect is the finding: the review phase must write its findings and their dispositions to `reviews/` before it ends, not leave them in a log that is deleted.** |
| 9 | **The state file's own summary of the batch inherited the same wrong figures** as the batch entry, in three places, which is how a single bad number reaches a prompt. | **Applied.** `state/current.md`'s canon line, its last-change line and the Batch 0009 entry's landed paragraph now carry the measured figures and say on their face that they were corrected. |
| 10 | **Two unpaired bold openers, found while checking the markup of the edited passages: Chapters 84 and 86 each open `**` inside an italic notebook entry and never close it**, so the emphasis runs away to the next `**` in the file and the rest of the entry renders as literal asterisks in a strict renderer. Pre-existing from the writer phase, not introduced by this pass. | **Applied.** Each opener is closed immediately before the entry's own closing `*`, which is where the author put it. **No word was added or removed and no line moved** — the batch is still 40,772 words and the per-chapter column is unchanged. |

## Measured and found sound, so that a later review does not re-open it

- **No duplicated paragraph** anywhere in the batch (paragraph-level comparison across all ten files: zero
  groups). **No sentence of sixteen words or more appears twice**, in one file or across two.
- **The ban list is clean.** No *Gatehouse*, no *Culling Order*, no *custodian*, no *Bind*, no melody cost, in
  any of the ten chapters. No System display, no gate, no revelation, no mechanism explained.
- **The money foots.** The un-firing's column is 325 + 270 = **595 pence = twelve marks one shilling and seven
  pence**, at forty-eight pence to the mark and twelve to the shilling: thirteen men at five pence for five
  days, and nine cords at thirty. Chapter 89's three lines and its total are all consistent, and the
  twenty-six words the repair removed came out of narration and not out of a column.
- **The two eighth ruled lines do not appear in the batch at all**, and no character refers to either. **No two
  of the volume's five blanks are in one room, in one chapter or in one sentence**, and no character says any
  two are the same.
- **Nobody dies, nobody is killed, no arch goes down, no glass breaks.** The catastrophe is a man of fifty-eight
  who is alive.
- **The standing house convention about weekdays and market days is unchanged** and is inherited by Block 5:
  a chapter may state both and may not reconcile them. The manuscript already does this at the fourth of
  Hearthmonth, a Friday and a market day, and at the ninth of Frostmonth, a Monday and a market day.

## Declined

**A proposal to bring the whole batch's narrator into Aren's tighter register.** Declined: the register is the
manuscript's own, ninety chapters use it, the chapters are otherwise finished prose, and a repair pass is not a
rewrite. The register did not change in this pass and should not change in the next one.

## What this pass did not touch

The plot, the chapter numbers, the cards, the twelve recorded Batch 0009 deviations, the day map, the cast
ledger, the four carried corrections from the Volume 01 close, the drift figures, the ending, and every
controller file — `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`,
`REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` and `state/phase-ledger.json` are all untouched, and the
ledger is controller-owned and stale by design.
