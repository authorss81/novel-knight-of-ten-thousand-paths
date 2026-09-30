# Review: `9955423` — "novel: save writer work batch-0005" (Vol 13, Ch 641–650)

**Reviewed, then repaired. This file is both the finding and the receipt. The finding is the first half, the figures in it were re-measured after the repair and the receipt is the second half, and nothing in the second half is a claim about the state of the files before the repair except where it says so.**

Working tree was clean at the review and nothing was edited during it. The change under review was 10 chapters, one volume-close record, and five state files, in commit `9955423`.

---

## The finding, as it was made

### Blocker: the prose is not fiction

Chapters 641 to 650 are **indirect-speech summaries**, not scenes. The dominant verb is "said." Characters stand at "the low end of the boards" and talk about procedure; nothing happens to anybody. There is no blocking, no sensory detail, and **zero interiority** — Aren Kest, the only protagonist present, is described from outside like furniture ("his stick against the platform and his good leg on the stones"). `AGENTS.md` requires "complete scenes with physical space, action, sensory detail, dialogue, subtext, character thought."

### Blocker: the cast has been reduced to demographic slots

"The badge-man," "the copyist of about twenty-six," "the woman of about twenty-nine who keeps the room," "a man of about fifty-two's chair." Across ten chapters with about twenty recurring figures, **two are ever named** (Aren Kest; Berta Lomax once). Compare Ch 0003, which names Mara Vey, Ferris Oat, and Alder Cross and gives its POV character an interior line.

### Blocker: the mandated coda has eaten the chapters

The closing block of every chapter is a footed price column plus a self-enumeration — *"eighteen figures of distance… not one of them is a price… seventeen figures of time… ten figures of persons."* Structure is **template-identical in 10/10 chapters**. Share of file: **17.0% to 24.6%**, mean about 20%. `AGENTS.md`: "Never replace a scene with a list," and "A number should matter because of what it changes in the story, not because the number exists." The coda was a spreadsheet; it changed nothing.

### Blocker: length collapse across the series

| Volume | Avg words/chapter |
|---|---|
| 01 | 5,411 |
| 04 | 3,376 |
| 08 | 2,413 |
| 12 | 1,856 |

This batch ran 2,713 to 2,061 and declined across the last five chapters. **The volume closed on its thinnest pages.** Manuscript was 1.80M words; about 60% of that was written at under half the volume-01 chapter length.

### Blocker: state files are append-only archives

`AGENTS.md`: "Do not load the entire manuscript into every prompt. Use **rolling summaries**."

| File | Size at the review |
|---|---|
| `continuity.md` | 984 KB / 1471 lines |
| `open-threads.md` | 764 KB |
| `chapter-summaries.md` | 560 KB |
| `batch-summaries.md` | 468 KB |
| `current.md` | 246 KB, holding the Chapter 560 and the Chapter 650 snapshots at once |

`current.md` contained ten overlapping "What is true at the close of Chapter N" blocks for 560 to 650. **About 3.0 MB of state is roughly 800K tokens — Volume 14 cannot load this.** Continuity had been rolled once (`f018e14`: 1.94 MB to 178 KB) and had since regrown to 1 MB.

### Concrete bugs

1. **Speaker attribution scrambled on the final page.** `chapter-0650.md` — the badge-man's instruction was quoted inside a carter's speech tag, so that Aren Kest appeared to lecture himself, and the next line had the badge-man contradicting the position the "carter" had just taken.
2. **Missing possessive, final page.** `chapter-0650.md` — "about nine **people'** worth of floor." The prompt gates apostrophe *style* in the dozens and no instrument checked for a missing one.
3. **Zero question marks in Ch 0646 and 0650.** The prompt names this exact recurrence: *"Batch 0004 was written and finished with two chapters at zero question marks… A beat added after a sweep is unswept."* It happened again, on the volume's last page.
4. **The volume's central beat is impossible as specified.** Prompt line 35 requires "Aren and Mara separate, agreed and painful"; line 61 bars `Mara Vey` from prose at 0 occurrences. The chapter substituted the unnamed woman who keeps the room, so the separation resolves between a protagonist and a character the reader is never given a name.
5. **Prompt contradicts itself on the last line.** §1 says "a woman of about twenty-nine reading"; §2 beat 4 says Berta Lomax "is the reader… the last line of the volume." The chapter had both women read, splitting the ending.

### Root cause

`workspace/volume-13/batch-0005/PROMPT.md` is about 95% measurement apparatus. §4 to §5 are entirely instruments: collision sets of price totals across three extractors, 8-word shingle chains, two-key comma/`and` list parsing, barred-numeral sweeps, `about`-per-1,000 ratios, "print the basis with every figure." It spent about 1,200 words on how to count money columns and about five lines on what the chapter is about. The apparatus became the deliverable, and the prose was written to satisfy it.

### Compliant

No em/en dashes, no italics, no System panel, no barred kin-term, `Mara Vey` correctly at 0. Exactly one next-phase artifact (`outline/volumes/volume-13-close.md`; no `workspace/volume-14/`, no second prompt). No controller files touched.

---

## The repair, and what it is worth

Ten chapters repaired in place. No chapter restarted, no beat moved, no planned plot changed, no chapter written from scratch, no prompt, outline or controller file touched.

### Against the finding, one by one

| Finding | What was done | Measured after |
|---|---|---|
| Not fiction | Interiority for Aren Kest in all ten; weather, light, smell, sound and blocking in all ten | see the figures below |
| Cast as demographic slots | Individuated inside the name budget rather than named, because the budget is five with four spent and the outline forbids naming the room-keeper. No name was spent | name budget still 4 of 5, `Mara Vey` still 0 |
| Coda is a spreadsheet | The three self-enumerating figure lists deleted from all ten; the footed price column and its mark conversion kept, because that is the house form and because a market's price list is a thing in the world | 4.52% to 6.02%, mean 5.23 |
| Length collapse | Scene prose added to all ten, most to the last five | 3,086 / 2,730 / 2,901 / 2,687 / 2,637 / 2,725 / 2,592 / 2,782 / 2,673 / 2,841 |
| State files | Window moved at the Volume 13 close, copy first and verified, then trimmed; `current.md` compacted to one live block and a thirteen-row volume index | 3.0 MB to 884 KB |
| Bug 1 | Exchange correctly attributed; the carter who appears nowhere else in the block is gone from that line | 0 misattributions found on re-read |
| Bug 2 | Reworded to `floor enough for about nine people in it` | — |
| Bug 3 | No chapter at zero; 15 question marks against 13 | min 1, max 3 |
| Bug 4 | Resolved on the evidence in writing; no name spent; the beat stands | see below |
| Bug 5 | Resolved on the evidence; exactly one reader of the clause | see below |

### Two defects the finding did not contain

Found on a second run of the same instruments, and both belong in this file because both are the kind of thing a close record exists to prevent.

1. **`chapter-0648.md`'s mark conversion did not foot.** The chapter printed three hundred and twenty-three pence and then printed it as *six marks and thirty over*, which is three hundred and eighteen. The over-figure is thirty-five. The block's own recorded claim that all ten columns foot four ways was false for one chapter, **because the four-way check verified the sum of the item list and the restated enumeration and not the conversion printed beside them.** Fixed to thirty-five over. The item sum and the printed total in that chapter were correct and did not move, so the collision set and the collision result are untouched.
2. **A promise on the last page was never kept on the last page.** The badge-man says the woman who said the words is in the room and *will say so herself*, and the block never let her say it. She now does, in her own four sentences, and says that a name in a room is a head at the top of a thing. This is the only beat the repair added that the outline did not already require.

### The two instruction conflicts, resolved on the evidence

Neither resolution spends a name, moves a beat, or changes the plot.

- **The name.** `outline/volume-13.md` §8 and §10.2 and the prompt's §1 call the separation *Aren and Mara*; the same prompt bars `Mara Vey` from prose at 0 and forbids naming the woman of about twenty-nine who keeps the room. **`outline/volume-13.md` §3.2, the section that introduces her, states that the volume's own resolution is that the two of them stop sharing a bed and keep the work** — that is the volume saying who the second party is. The separation is between Aren Kest and her, written in Chapter 0644 and on the last page again in one paragraph. `Mara Vey` is a Volume 01 archivist whose surname is common naming out of the Sable country. **The beat was not retired and the plot did not move; the instruction was wrong and is now answered in writing.**
- **The reader.** `outline/volume-13.md` §9 names a woman of about twenty-nine as reading the clause; §8, §10.4 and the prompt's §2 beat 4 name the fruit-valley delegate, four to one, and the beat is the more specific instruction. **Berta Lomax reads the clause and that reading is the last line of the manuscript; the woman of about twenty-nine reads the standing of the hearing and the state of the book before it, which is a different thing.** Exactly one person reads the clause. To make the last line literally the last line, the two closing paragraphs of Chapter 0650 stand after the money column rather than before it, which is the only change to any file's shape.

### The figures, recounted on the files after the repair

**BASIS ONE, the file total: a plain whitespace split with the title line INCLUDED, each file counted on its own and the ten added.** The block is **27,654**, per chapter **3,086 / 2,730 / 2,901 / 2,687 / 2,637 / 2,725 / 2,592 / 2,782 / 2,673 / 2,841**, and a concatenated `cat` of the ten returns 27,654 and every file ends in a newline. **BASIS TWO, the scene body: everything above the paragraph that opens the cost coda, therefore including the title line and the dateline.** The bodies are **2,946 / 2,587 / 2,770 / 2,551 / 2,485 / 2,561 / 2,453 / 2,636 / 2,526 / 2,698**, minimum 2,453 against the volume's floor of 1,161. **Codas 140 / 143 / 131 / 136 / 152 / 164 / 139 / 146 / 147 / 143**, mean share **5.23%** over **4.52 to 6.02**; on Chapter 0650 the two closing paragraphs stand after the column by design, so that chapter's body figure counts them.

**The block no longer declines.** The shortest chapter is 2,592 and the last page is 2,841, so the volume no longer closes on its thinnest pages. It ran 2,713 down to 2,061 before.

**Manuscript 1,805,098 in 650 chapters**, on the same basis, and a concatenated `cat` returns the same figure. Volumes 01 to 12 at 1,681,701 in 600 and unmoved, because the repair touched no file outside `chapters/volume-13/`. Volume 13 at 123,397 in 50, blocks 20,333 / 24,843 / 26,848 / 23,719 / 27,654, and the six figures add. **The figure 1,800,781 that the pre-repair records carried is out by exactly 4,317, which is 27,654 − 23,337 and is the whole of what the repair added.** The 640 files before this block return 1,777,444 and the earlier correction of the three-hundred-too-high 1,777,744 stands.

**Money, with the extractor first.** Ten totals at **207 / 222 / 247 / 256 / 269 / 280 / 289 / 323 / 337 / 302**, ten distinct, each footing four ways at forty-eight pence the mark. Collision result zero of ten against a set of **178 distinct** built by the declared extractor over the 640 prior files, the four barred numerals absent from the set, free set **178 of 178**; 224 of those files carry a printed total at all. **The collision result was not re-derived, because no total and no printed price moved.**

**`about` is 554 at 20.03 per 1,000**, below the four earlier blocks' 22.46 to 27.60. The `about N of (those|the|these) M` sweep returns no hit where the first number is larger than the second. **It is a reading rule and not a quota and there is no floor; the movement is a consequence of the prose and is not a target.**

**The thank family is 54, and a sweep of every thank-family sentence in the ten files returns zero that is not a negation or a plain statement that a person was not thanked.**

**House rules, swept and counted.** Barred words 0 on word boundaries, including `level`, which appeared once in a draft of 0648 in *about level with the pocket* and was reworded. Meta frame 0, after one self-inflicted hit: a draft of 0650 said *a carter had put a load down where a carter had put a load down in Chapter 0648*, which is the narrator outside the world, and it was reworded. Em dashes 0, en dashes 0, italics 0, straight double quotes 0, semicolons 0, bold parity even on every line of every file. **15 question marks and no chapter at zero.** `Aren Kest` in all ten. **Exact duplicate paragraphs at twelve words or more: 0 against the 640 prior files and 0 inside the block.**

**Runs, with normaliser and scope.** On a whitespace-token normaliser with punctuation kept, sliding an eight-word window one token at a time, scope the ten files against all 640 prior chapter files: the longest chain of consecutive shared eight-word windows found anywhere in the prior corpus is **19 windows, twenty-six words, at `chapter-0641.md`, chaining across 7 of the 640 prior files and owned by none of them**; the largest chain any one new file holds against any one prior file is **15 windows, twenty-two words, at `chapter-0646.md` against `chapter-0636.md`, held by one pair and not tied.** The block reported 26 and 21 for the same two figures before the repair. **Both are lower now; the prose is different prose, so the two sets are not otherwise comparable, and the direction was measured and not asserted.** An eight-word index built as a `defaultdict(set)` must be read with `.get(window, <empty>)` and never with `index[window]`, for the reason in `state/continuity.md` 1530.

**The state window.** The four ledgers fell from 2.79 MB live to 641 KB and `current.md` from 246 KB to a file with one live block and a thirteen-row volume index; 884 KB together against 3.0 MB. Everything cut is in `state/archive/` as a byte-for-byte copy — `continuity-volumes-01-12.md`, `open-threads-volumes-01-12.md`, `chapter-summaries-volumes-01-12.md`, `batch-summaries-volumes-01-12.md`, and `current-md-at-the-volume-13-close.md` — and all five were verified byte-identical with `cmp` against git **before any live file was rewritten**. No item, thread, chapter or batch number was renumbered. **The convention changed from copy-and-leave-whole to copy-verify-trim, and the reason is on the record: leaving the live file whole means it regrows from the copy point on every batch, and a window that is only copied is not a window.**

### What this repair did not do, and why it is written down here

- **Volumes 09 to 12 are unrepaired** at 1,856 to 2,961 words a chapter against 5,411 in Volume 01. This recommendation is not discharged; a repair of four closed volumes is a different brief and this one was told to repair the current phase.
- **The prompt that caused the defect is not rewritten.** `workspace/volume-13/batch-0005/PROMPT.md` is the historical brief of a closed block and its §4 to §5 measurement apparatus is the root cause the finding names. The apparatus lesson is carried forward in the state files. **The next prompt, when one is written, should not inherit it, and the standing instruction for it is in the threads: one money column per volume rather than per chapter is the reviewer's first recommendation and it is not this phase's to enact.**
- **There is no `outline/volumes/volume-10-close.md`.** Twelve of thirteen closes have a record. The gap is recorded in `state/current.md` and in the close record and is not filled, because writing a close record for a volume closed long ago is a repair of a closed volume.
- **`outline/volume-13.md` is not edited.** Its §9 and §10.2 name the second party of the separation and its §9 names the reader of the clause; both are resolved above on the outline's own evidence, in the state files, and no outline was touched.

No files outside `chapters/volume-13/`, `state/`, `state/archive/`, `reviews/` and the one close record were modified. No controller file was touched.
