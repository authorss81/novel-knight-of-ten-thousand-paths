# Volume 13, Batch 0003 — Chapters 621 to 630, the review of a verification pass

**The reviewed artifact.** Commit `b2500e2` *"novel: save writer work batch-0003"*, which is a **verification-and-repair pass over a block that was already written on disk** and not a writing pass. It was handed `workspace/volume-13/batch-0003/PROMPT.md`, correctly refused to draft Chapters 621 to 630 because the two `ls` commands in the prompt's own first line returned forty files and `chapter-0640.md`, repaired two meta-frame sentences, and rewrote only the state records. The review is `logs/batch-0003.review.log`, which is gitignored, and **this file is the disposition, written by the repair pass before the next dispatch overwrites the log.** It is the second review artifact Volume 13 has and the sixth time in this project that a review's findings have survived only by being copied out of a log.

**Disposition in one line. Three findings and one minor note: two applied, one recorded with an owner, one checked and declined with reasons. One sentence of prose changed, in one file. Six record locations corrected. No plot beat, no dateline, no weekday, no money figure, no name, no outline requirement and no ending moved. No chapter was restarted, no chapter was written, no prompt was created, and no controller file was touched.**

---

## What the review verified correct, and it is left standing

- **The refusal to write was right, and the review confirmed the reasoning rather than taking it on trust.** Forty chapter files ending at `chapter-0640.md`, Batch 0004 complete behind Batch 0003, `workspace/volume-13/batch-0005/PROMPT.md` already standing at ninety lines and correctly scoped to Chapters 641 to 650. Not duplicating that prompt was correct and remains correct.
- **Every headline figure reproduced exactly on an independent recount**, file by file and concatenated: manuscript 1,777,743 in 640 chapters at the time of the review, Volumes 01 to 12 1,681,701, Batches 0001 to 0004 at 20,333 / 24,843 / 26,847 / 23,719, Volume 13 at 95,742, and `chapter-0628.md` at 2,582 before the repair and 2,585 after it.
- **All ten per-chapter counts in the new chapter summaries matched the files.** Bold parity, curly-quote parity and the dash and semicolon counts were clean, and no chapter file was missing its trailing newline.
- **The three false DEFECTS the reviewed pass recorded about its own instruments were real and the write-up is accurate.** A prefix glob of `chapter-062*.md` matches 0620 to 0629 and pulls in a neighbouring batch; the coda's figure lists cannot be split on commas because a list separator and a number join are the same three letters; a leftmost-match regex starts at the wrong `and`. Each produced a false finding against a correct page.
- **`state/phase-ledger.json` was untouched** and still reads `phase-000-bootstrap`, `planned`, which is the standing defect this directory records at `volume-13/batch-0002.md` item 10 and which is controller-owned.

---

## Finding 1 — HIGH — a meta frame was missed inside the very block being verified. **Applied.**

`chapters/volume-13/chapter-0629.md` line 59 read:

> Then the badge-man said the last thing of that morning and it is the thing **Block 0004 stands on**…

This prints the production unit's own numbered label in scene prose, and it is blunter than either instance the reviewed pass repaired, because those two at least said *block* while this one says *Block 0004*. **Chapter 0629 is inside Batch 0003 and the new summaries certify it "2,804 words, unchanged."**

**Repaired to `and it is the thing the thirty-one years stand on`, nine words for eight.** The choice is not cosmetic. The badge-man's speech begins two paragraphs below and ends *this is the first of the three in thirty-one years that anybody has done anything about*, so the repaired clause now tells the reader what to listen for, which the original could not do without leaving the world. **One sentence in one file, and nothing else in 0629 was touched**: not the dateline, not the copyist's refusal of the good news, not Hester Vane's single naming of herself, not the man of about thirty-four writing *Three* in words because a figure in a column would have been a number by Friday.

**The finding's larger half is the completeness claim it falsifies, and the state files carried that claim forward as fact.** `state/continuity.md` 1506 said a successor *should* repair two instances; `state/open-threads.md` 505 said **Two remain**, both in closed Batch 0002. A manuscript-wide sweep finds **at least five, spanning three volumes**, and the sweep carried by this repair finds **eight, in four**. The four the review did not report are `volume-12/chapter-0570.md` line 39, `volume-12/chapter-0578.md` line 17, `volume-05/chapter-0240.md` line 37 and `volume-01/chapter-0047.md` lines 55 and 181. **Every one was read in context and every one was checked against this book's heavy masonry vocabulary**, in which a dressed block, a block of ground and block-wood are ordinary and correct, so that the word alone proves nothing and the referent decides. Both corrected claims are now marked falsified in place rather than deleted, and the full inventory is at `state/open-threads.md` 511.

## Finding 2 — HIGH — three stale figures sat in operative hand-off positions with no supersession marker. **Applied at all three.**

The reviewed pass corrected `state/current.md` line 3 and declared 26,844 and 1,777,440 SUPERSEDED. Three passages still asserted the old figures in the present tense:

- `state/current.md` line 16, under *Where the manuscript is*.
- `state/open-threads.md` 502, which sits under the heading *Threads Volume 13 Batch 0004 hands to Volume 13 Batch 0005* and **directly above item 503, the binding list of what Batch 0005 must not do** — that is, the next writer's operative brief.
- `state/continuity.md` 1503, directly above the corrected item 1504.

**All three now carry the corrected figures and a marker in the sentence itself**, and the figures have moved again as a result of Finding 1: Batch 0003 is 26,848, Volume 13 is 95,743 and the manuscript is 1,777,744. **The repository has an established convention these three skipped** — item 1494 → *PARTIALLY SUPERSEDED BY 1495*, open-threads 483 → *SUPERSEDED BY 488* — and the rule the convention serves is its own: *do not print a figure from any record in this repository without counting it off the page*. **A successor reading item 502 on its own inherited three wrong numbers with no signal that they had moved, and 502 is the paragraph immediately above the one that tells the next writer what it may not do.**

## Finding 3 — MEDIUM — the two known defects were stranded with no owner. **Recorded with an owner, and the owner is not Batch 0005.**

`chapter-0617.md` line 37 and `chapter-0620.md` line 61 are genuine and were correctly identified by the reviewed pass, which correctly declined them on scope. **Recording a defect without an owner means it will not be repaired, and the review is right about that.**

**The remedy taken is ownership, recorded at `state/open-threads.md` 511, and the two remedies the review offered were the two available ones.** A carve-out in Batch 0005 was not written, because `workspace/volume-13/batch-0005/PROMPT.md` line 19 says *Do not write 601 to 640* and item 503 says do not repair closed prose on a hunch, and **`volume-04/batch-0002.md` in this directory records why that matters in one sentence: a wrong number is caught by the next person who adds the column; a wrong prohibition is obeyed.** So neither bar was touched and neither was argued with. **The owner is a dedicated repair dispatch with the whole manuscript open, minimum scope the two Volume 13 instances because Volume 13 is the volume now in progress and will be read as a unit, with the three closed-volume instances taken in the same pass, and with an instruction to re-derive the inventory rather than inherit it, because two passes have now inherited this list from each other and both have got it wrong.**

## The minor note — genuine-looking `chapter` and `scene` hits in closed volumes. **Checked, two declined, one half applied.**

- `volume-01/chapter-0038.md` line 99, *he wrote a draft of two thousand words and destroyed it*: **not a defect.** A character writes a draft and the act is on the page.
- `volume-02/chapter-0092.md` line 69, *the thing that made it a breach instead of a scene*: **not a defect.** A breach is this book's own word for a road opened without authority and a scene is a scene.
- **The useful half of the note is the instrument half and it is applied**, at `state/open-threads.md` 513: a manuscript-wide count of the word *chapter* returns 638 files out of 640, and almost all of it is each file's own `# Chapter NNNN` title line, so **a sweep of that word must exclude line 1 or it will report a clean volume as a defect.**

---

## Finding 5 — raised by this repair, not by the review, and it is about a measurement's own record. **Applied to the records; no prose moved.**

**The reviewed pass corrected a record that did not reproduce, and the correction does not reproduce either.** It recorded the block's longest run against the six hundred and twenty prior chapters as **36 words** and corrected an earlier record's *label* for it, saying the run is scene prose at `chapter-0625.md` against `chapter-0620.md` and is **not** in a cost coda.

**Re-run on the basis that item names — a plain whitespace split with the title line included, an eight-word window slid one token at a time, all six hundred and twenty prior chapters — the maximum is FORTY-THREE words, and it is the cost coda's recited frame, at `chapter-0624.md`.** The per-chapter series is 29 / 29 / 31 / 43 / 36 / 27 / 29 / 30 / 32 / 27. A second basis, words rather than whitespace tokens with the title line dropped and the emphasis marks stripped, moves only 0623, from 31 to 34. **So thirty-six and forty-three are two bases and not one wrong number, and both are wrong to quote without the basis.** The run text at 0624 was read to be sure: it is *a fourth course not laid a hired room over a saddler's and about four hundred paces of lane are thirteen figures of distance and of count and not one of them is a price*, running on into the coda's persons list, which is `outline/volume-13.md` §7's own recited device and not a lift.

**The advice survives and is unchanged, which is the part that matters: the run the reviewed pass warns against is still scene prose, still a deliberate recurrence, and must still not be repaired.** The 32-word run at 0629 is a third instance of the same method and not a defect either, being Hester Vane's *it is the crossings that are open and the weeks the road is shut* against the woman of about forty-three's *What we keep is the crossings that are open and the weeks the road is shut* at `chapter-0619.md` line 71. **What does not survive is the confidence that the label was wrong.** `state/continuity.md` 1508 and `state/open-threads.md` 507 are marked at 1512 and 513, and the standing is the one this directory has now stated four times: **a figure about a sweep must carry the basis it was measured on, and the correction of such a figure is subject to the same rule as the figure.**

---

## Recorded and not applied

**4. The numeric coda is a publishability risk, and it is the outline's design.** Unchanged from `volume-13/batch-0002.md` item 8 and not re-argued: `outline/volume-13.md` §7 and §10 design a footed money column per chapter plus a coda listing every figure in the chapter that is not in it, and Chapter 0629's coda is 616 of 2,805 words at 21.96 per cent. **Not repaired, because repairing it is a change to the volume's designed mechanic across fifty chapters and would be a plot-level decision, not a repair.** The share still falls as the body lengthens, which is the direction the standing asks for.

**6. One pre-existing bold-parity oddity in a closed batch, found while checking this pass's own work and not repaired.** `volume-13/chapter-0639.md` line 25 reads *the woman of about thirty-six said, **“**and you were right then as well.**”* — a fragment opened bold and closed in the wrong place. **It is the only odd line in six hundred and forty files, it is in closed Batch 0004, it was not among the review's findings, and no reader sees it.** Recorded at `state/open-threads.md` 513 and not repaired, because a repair pass that widens its own scope on a hunch is the failure `reviews/volume-13/batch-0002.md` item 3 and this directory's own standing both warn against.

**7. `state/phase-ledger.json` reads `phase-000-bootstrap`, `planned`, against 640 chapters.** **Controller-owned, not written, and recorded here rather than acted on,** as at `volume-13/batch-0002.md` item 10.

---

## What this review adds to the pattern

**The fifteenth data point found the same three classes — continuity, arithmetic, voice — found no plot defect in the delivered prose, and found one new thing, which is that the *correction* of a measurement is itself a measurement and is subject to the same rule.** Two reviews running now, one on each side of a single sentence: the reviewed pass corrected a run-length record's label and was wrong on its own stated basis; this review could have inherited that correction and did not, because it re-ran the instrument.

Three things here are new.

**One: the pass that verifies a block does not read the block.** It swept a class, repaired two instances, wrote down that two remained, and missed a third in the same ten chapters that it had just certified *unchanged* with a word count. **A completeness claim about a sweep is itself a claim about the sweep's basis, and the word that gave it away — `Block 0004`, with the number in it — was not in the list of patterns the sweep searched for.** This is `volume-11/batch-0005.md`'s standing point arriving for the third time: **a rule about register is not a rule about vocabulary, and a sweep that names its patterns keeps finding the one it named.**

**Two: two passes inherited one defect list from each other and both got it wrong, in the same direction.** The reviewed pass wrote *two remain*; this review found six; this repair found eight. **The cost was not that the list was short but that nobody owned it**, and a defect with no owner is a defect with no deadline.

**Three, and it is the same shape as Finding 2: the operative brief is where a wrong number does the most damage.** Item 502 is the paragraph immediately above the list of what Batch 0005 must not do. **A figure that is wrong in an archive is a nuisance and a figure that is wrong one paragraph above a prohibition is inherited as fact by the next writer, who has no way to know it was ever in doubt.**
