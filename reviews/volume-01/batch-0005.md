# Review — Batch 0005, Volume 01, Chapters 41–50, "The Oath and the Two Bridges"

Reviewed phase: `batch-0005` (commit `56ec6c7`, "novel: save writer work batch-0005"). Source log: `logs/batch-0005.review.log` (gitignored, hence this file). Repair pass applied in the same commit sequence that produced `56ec6c7`'s successor.

**This file records one review of this phase.** A later pass reviewed the result of the repair and returned no further findings against the prose; the only residual items were the stale per-chapter word figures and the review-record gap, both closed here.

## Verdict as received

Structurally the batch is sound. All ten chapters are finished prose, all ten change the situation, the batch midpoint (Ch 46) and the climax (Ch 47) both land, no character acts for plot convenience, and the volume closes where `outline/volume-01.md` said it would. The findings below are all in the **state layer and the formatting layer**; not one required a story change.

## Verified sound (no action)

- **Word counts are exact.** `wc -w` on `chapters/volume-01/*.md` = **270,562**, and the per-batch split in `state/current.md` reproduces exactly: 40,128 / 57,708 / 54,375 / 64,632 / 53,719.
- **State record counts check out.** `state/continuity.md` had 124 numbered items; `state/open-threads.md` threads reach 58; `state/chapter-summaries.md` has a Batch 0005 entry covering all ten chapters with the claimed POV split (Aren ×5 / Mara ×4 / Tovan ×1).
- **Discipline constraints held.** "Culling Order" and "Sabin Dain": 0 occurrences in Ch 41–50. Chapters are genuinely finished prose, not outlines — Ch 45 and Ch 50 both land on closed, resonant beats.
- **Dispatch hygiene is correct.** Exactly one `PROMPT.md` per phase directory; `.done` markers on the six completed phases; `batch-0005/.done` correctly absent while the phase is in review. The Volume 02 close prompt correctly forbids creating a Chapters 51–60 prompt.
- **`state/phase-ledger.json` staleness is already correctly documented** at `state/current.md` as controller-owned and not read by dispatch. No action needed.

## Disposition summary — all applied

Findings **1–5** are the reviewer's, verbatim in substance. Findings **6–7** were raised by the repair pass itself while measuring finding 1's neighbours, and are marked as such so that the provenance of every line below is unambiguous.

| # | Severity | Finding | Where fixed | Status |
| --- | --- | --- | --- | --- |
| 1 | P1 | `state/continuity.md` had no **Chapter 50 relationship state**; the file's newest relationship section described the world ten chapters back, and it sat *after* items 121–124, so the newest baseline a reader would reach for was Chapter 40 | `state/continuity.md` — new section appended; the Ch 40 section moved back to sit directly under the Batch 0004 canon so the file's established `canon → relationship state` order is restored | Fixed |
| 2 | P1 | **"One new name in the batch: Edric Hunn" is false and was propagating into the next phase.** Edric is first named in `chapter-0026.md` and is a signature from Ch 38; the batch-0005 prompt itself calls him established | `state/continuity.md` item 124; `state/batch-summaries.md` (Landed line and card-error note 4); `state/chapter-summaries.md` Batch 0005 header; `state/current.md`; `workspace/volume-02/volume-01-close/PROMPT.md` lines 20 and 54 | Fixed — five files |
| 3 | P2 | **Markdown bold far above house style — 132 bold lines in the batch** against 0 in Batch 0001 and 1 / 7 / 12 in the only earlier instances (Chs 19, 35, 40). Mostly emphasis, plus **8 bolded proper names in plain narration** against 1 in Chapters 1–40. Renders as shouting text | `chapters/volume-01/chapter-0041.md` – `chapter-0050.md`, all ten. **132 → 11**, at the strongest single beat per chapter. No word, sentence, paragraph or beat changed; `wc -w` is byte-identical before and after (270,562) because the markers were not attached to whitespace | Fixed |
| 4 | P2 | **`reviews/volume-01/` had no durable record for batch-0002 or batch-0003**, both of which have `.done` markers, and the README enumerated three files and never mentioned them — the gap was undocumented rather than unnoticed | `reviews/volume-01/batch-0002.md` and `batch-0003.md` created as explicit **gap records that point at the surviving disposition** in `state/batch-summaries.md` rather than inventing a findings list; `reviews/README.md` rewritten to enumerate every reviewed phase and to name the gap | Fixed |
| 5 | P3 | **"Zero Gatehouse lines" is imprecise.** `chapter-0047.md:193` does contain the word, giving the Order's own figure for a held road as a standard of measurement. The substantive constraint holds (no member named, no third Order line spent) but the close phase will audit the language | `state/continuity.md` item 124 and `state/chapter-summaries.md` Batch 0005 header now read *zero Gatehouse Order lines* and name the single appearance as a measurement and not an appearance | Fixed |
| 6 | P2 | *(repair pass)* **Stale per-chapter word figures** in the Batch 0005 summary, summing to 53,713 against the real 53,719, and wrong on six of ten chapters. Same class as the stale figures the Batch 0004 verification pass caught | `state/batch-summaries.md` — now 5,583 / 3,612 / 5,111 / 6,363 / 3,570 / 3,921 / 8,090 / 5,344 / 5,329 / 6,796, measured | Fixed |
| 7 | P3 | *(repair pass)* **The Chapter 50 coda had no canon entry.** Item 125 added: the fourth warmth on the twenty-ninth of Fallowmonth, the note and the answer inside a second and a half, the nine people in the lane, the two hands on the bell, and the verse's second hole with Ilyra's ending note | `state/continuity.md` 125 | Fixed |

## Notes on the judgment calls

**On finding 2.** The correction is a claim about *cast discipline*, not a retcon. Nothing in the prose changes: Edric Hunn was already in the volume and already named. What the batch gave him is his first page and his first room, and the corrected records say exactly that. All five files that carried the false figure now carry the true one, and the Volume 02 close prompt — which had been instructed to write the false figure into the close record as cast-discipline canon — now carries the correction *and* an instruction not to let the false version back in.

**On finding 3.** The batch's real problem was not that bold was wrong but that it was everywhere, so the fix had to be even-handed rather than selective. All eleven remaining instances are load-bearing single beats: the thesis of Ch 41 (*a line and two hands*), the price of the cutwater in Ch 42, the hole in the magistrate's finding in Ch 44, the tolls line in Ch 45, how the arch failed in Ch 47, the two strongest beats in Ch 48, the scar and *I am not the mechanism* in Ch 49, and the brine weights and the empty eighth line in Ch 50. Bolded proper names, bolded role labels in the Ch 50 steward list, and bolded dialogue were all removed, since the emphasis was doing work the sentence already did. **The one System display in the batch — the ferrywright's four-line slate in Ch 49 — was already set in italics and is untouched.**

**On finding 1.** The section is written from the prose of Chapters 41–50, not from the Chapter 40 section it follows, and it is the second half of the batch's movement: the palm-up disclosure of the twenty-second of Fallowmonth entered as *his statement and not her observation*, Toban's book read out loud in daylight with no question asked, Rell carrying the bell out himself, and the marshal refused in ninety seconds with the request for a list of names refused in the same minute. **The Ch 40 section was moved rather than rewritten** — no line of it changed — because the defect was its position in the file, not its content.

## Deliberately not changed

- **The drift.** Three weeks out, three weeks back, stated on the page in Ch 47's notebook as a warning that was wrong and not a surprise, with the correction *the three weeks is on this side and not on mine*. Correct, inside the series ledger, and load-bearing. `47:193–199`
- **The failure in Ch 47.** The Bind does exactly what a Bind does: it puts the load where the load path says it goes, and the second pier was standing on a shelf of gravel. The protagonist's fault is that it was *his* working, not that the magic misfired. **Do not "fix" this in Volume 02 by softening the mechanism.**
- **The three shortest chapters (42, 45, 46 at 3,612 / 3,570 / 3,921 words).** Measured, not padded. Ch 42 does a great deal in little because it is a room with a book in it; Ch 45 ends on a question rather than a turn, which is the card's shape and is paid off in Ch 47's notebook.
- **The unnamed wounded in Ch 47.** A hull-hand addressed by trade and a stranger named in a book in another world. Deliberate, and the reason the batch spent no name.

## One observation, not a defect

`outline/batches/` holds only `volume-01-batch-0001.md`; the cards for batches 2–5 live solely inside the `workspace/` prompts. The batch-0005 prompt acknowledges this explicitly and the close prompt mitigates it by requiring all fifty chapters be read, so nothing is lost — worth knowing that the card record for 40 chapters has no home outside `workspace/`, which is a workspace directory.
