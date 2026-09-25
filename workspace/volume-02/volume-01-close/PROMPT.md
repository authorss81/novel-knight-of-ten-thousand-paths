# Volume 01 close — handing *The Bellweather-Living Road* to Volume 02

**This is the only prompt for this phase.** Volume 01 is complete: Chapters 1–50 exist as finished prose in `chapters/volume-01/chapter-0001.md` through `chapter-0050.md`, four digits, **270,562 words** by `wc -w`, title lines included. This phase writes **no chapter prose.** It produces a **volume-close record** and a **Volume 02 outline**, and nothing else. Do not create a Chapters 51–60 prompt anywhere in `workspace/`, do not recreate or edit the Batch 0001–0005 prompt directories (`workspace/volume-01/batch-000*/PROMPT.md`), which are the record of the phases that ran, and do not create a second volume-close prompt.

Guard: this phase writes fiction-plan and manuscript-state files only. Never edit `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, or `state/phase-ledger.json`. `state/phase-ledger.json` is controller-owned, is stale by design, and is not what dispatch reads — leave it alone. The five earlier batch prompt directories keep their prompts and gain a `.done` marker from the controller, not from you.

---

## What this phase is for

**You are closing a volume and opening the next one.** `outline/ending.md` fixes the ending of the whole book; **nothing in it may be moved.** Volume 01's own resolution is fixed in `outline/volume-01.md` under *Concrete resolution (Chapters 48–50)* and it has now been delivered on the page. Your job is to read the fifty chapters as a whole, state what the volume actually turned out to be, check every promise against what is on the page, and write a Volume 02 outline that is the honest sequel to a finished book rather than a sequel to a plan.

## Read all of it, in this order

1. `outline/series.md` — **in full**, especially the time continuity ledger, the knowledge-control table, and the antagonist ladder. **The Volume 02 row of the time ledger is binding: seven months of main-world elapsed, and a longest path interval of nine months in the County of Ash.** Do not widen the drift beyond the ledger.
2. `outline/ending.md` — **in full**, and do not summarise it from memory. The setup-to-payoff table at the end names the setups planted in Volumes 1–17, and the Volume 01 rows of it are the seven plants this volume just made good: the bell bought for two pence, the brine weights, the accepted fever account, the anniversary storm, the missing-anchor ledger, the cut on a forged witness, and the path community that kept its painful memories. **The book's whole question, stated once, is* a man who can cross and cannot stop crossing* — Volume 01's answer was that he has to be one of the things other people can hold, and Volume 02 has to take that answer seriously enough to count the people.**
3. `outline/volume-01.md` — the whole of it, and especially *Block 5*, *Volume climax*, *Concrete resolution*, *Cast plan*, *Continuity traps*, *Time budget*, and *Power and cost ledger*.
4. All **fifty chapters**. They are not long: 270,562 words total. Read them. Do not work from the summaries for anything that a later volume will depend on.
5. `state/current.md` — last, for the day map, the weekday chain, and the power state.
6. `state/continuity.md` — **all 125 numbered items, and the relationship state at the end of every block.** Items 111–112 are the Batch 0005 pre-write calendar resolutions, 113–125 are the canon that batch invented, and the section headed **Relationship state at the end of Chapter 50** is where the volume leaves every character — **read it before the Chapter 40 one, not after it, and do not treat the Chapter 40 section as the latest state.** All three are load-bearing and none may be re-derived.
7. `state/open-threads.md` — **threads 1–58**, and in particular **49–58**, which were opened by the last ten chapters and are what the next volume inherits.
8. `state/batch-summaries.md` — all five entries, including their repair passes.
9. `state/chapter-summaries.md` — the per-chapter record.
10. `bible/characters.md`, `bible/terminology.md`, `bible/world.md` if present, and `NOVEL_SPEC.md`.

## What to produce

### 1. `outline/volumes/volume-01-close.md` — the volume-close record

A substantial, honest, single-volume document. It is the thing the next three volumes will be written against. It must contain:

- **What the volume was about**, in one paragraph, said without the marketing voice the prose does not use.
- **The volume's argument, as it landed.** The thesis the book has been pressing since Chapter 4 is *a man who can cross believes that makes him the person who should decide*, and the volume's answer is that he is one of the things other people can hold. Say where that is proved, where it is not, and what it cost.
- **A state-of-the-world ledger at the end of Chapter 50**, in the same spirit as the state block at the end of Batch 0001 in `state/batch-summaries.md`, covering: the Old Toll crossing and its trust; Sedge Reach; the bridge guild, the reeve and the watch; the Bellweather Claims Archive and its four places and its writ; the Crown's instruments and the county file two hundred miles off; the Old Toll bell; the road itself; Aren; Mara; Tovan; Lysa and Aldis Fenn; Rell; Millward; the salt merchant; Sarn Oyelaran; the salt-loft lease; the market board; and the yard.
- **A promise-by-promise audit.** Take every promise in `outline/volume-01.md`, `outline/ending.md`'s Volume 1 setups, and `state/open-threads.md`, and for each write: **delivered on the page / delivered on the page but not as planned / deliberately deferred and where it now lives.** Include the Ferris Oat brine weights (deliberately deferred to Chapter 892, and the two lines four lines apart in the day-book are the thread), the missing-anchor ledger, the YR 302 out-of-place clearance entry, the eleven-year-old 301 salvage filing, the roadmark and why he can cross, the private-keeper clause, the two hundred and eleven, the two Hushwater figures, the eleven-year-old silence, the verse, and the two Fenn sisters.
- **The four corrections Volume 02 must not undo**, which are the ones a reader would notice: the **two-disc seat is gone and there is no third**; the **road is a line and two hands, not a piece of glass**; **Bellweather-Living's two stewards are Sera Quen and the man with the mallet, and Aren is neither**; and **the name is on a separate sheet under a separate number.**
- **The three hooks**, in the order `outline/volume-01.md` gives them, each stated as a document with a date and an owner.
- **A short honest paragraph on what Volume 01 did badly**, and which of those defects Volume 02 should inherit on purpose and which should be corrected.

### 2. `outline/volume-02.md` — the Volume 02 outline

The real deliverable. It must be the same species of document as `outline/volume-01.md`: volume identity, dominant pressure, the volume's central question, the starting state of every load-bearing character, the starting power state, major locations and factions, the mechanics it runs on, a **five-block escalation sequence (Chapters 51–100)**, the volume's climax, the concrete resolution, the next-volume question, a power-and-cost ledger, a six-name-per-batch cast plan for Batches 0006–0010, a knowledge-control table, continuity traps, and a time budget that matches the series ledger exactly.

Requirements on the substance:

- **The County of Ash** is the Volume 02 path, the longest path interval in the series so far at nine months, and it must be a **different kind of community from Bellweather-Living** — not a city that refused to be rescued with a creditor in it. Read the series outline's Volume 02 row and the antagonist ladder's second rung (**Halven**, who trades the missing-anchor ledger to the Council after Edric offers him a legal shield, and who in Volume 11 testifies against Iselde Senn and is later permanently barred from office) and build the volume so that **Halven's trade lands inside it.**
- **Edric's office has stopped asking Aren to stop and has started asking who else he has told** (Ch 50). That is the volume's political engine, and the answer is a form with a column headed *Keeper* in an office that now has a woman's name in a provincial file. **Name the office and the form, not the people in it.** Volume 02 is where the provincial office becomes a character.
- **The second severance authorization in the same hand, four years later, in an unnamed county** is now visible to four people in two countries. Decide who goes to look, what it costs, and which of the four of them goes, and make it a person with a want that is not Aren.
- **The claimant's form about the eastern-counties fever with its list of names to be removed from the public roll** is the first thing to reach the Archive on somebody else's initiative in eleven years. It is not the Archive's war, and the volume must be about that fact.
- **Aren's power state at the start of Volume 02 is Stage 1, by qualification, and Volume 02 is the volume in which somebody counts the four people he has.** He has a copying post at three shillings a week, a guild roll and an election in Frostmonth, eleven marks and fourpence owed by a trust in abeyance, and a roadmark. He is on the guild roll as a **road warden elected in this room in Frostmonth** — write that scene.
- **Volume 02's second severance cannot be another arch.** The volume's failure must be a failure of a different kind: an administrative one, an archival one, or a labour one. `outline/series.md` gives the antagonist's second rung as a registrar who trades records for a shield. Build the volume's engine on **records being bought and sold**, not on a structure failing.
- **The drift is now three weeks at Volume 01 and the series ledger allows it to widen with each volume, and the nine-month Ash interval must be costed in main-world days and in lost main-world days, with a number.** Volume 01's drift is stated on the page in Chapter 47's notebook and must not be contradicted.
- **Do not introduce a new final enemy.** Edric Hunn is the antagonist of the whole book. Sabin Dain enters in Volume 02 as a named person with a want unrelated to Aren, is not a Gatehouse Order member yet, and the phrase "Culling Order" is already spent for Volume 01 and may appear once more, in a document or a claimant's mouth, with no member attached to it.
- **Name no more than six new characters per fifty-chapter volume, and give every one of them a want in their own voice.** The Volume 01 total across five batches was **no new name in Batch 0005, and four of the six-name cap unfilled on the final block**; Volume 02 may be more generous and should be, because a new path needs new faces, but it must be deliberate. **Do not record Edric Hunn as a Batch 0005 name.** He is first named in `chapter-0026.md` and is a signature on the Crown's letter from Chapter 38; what the last batch gave him is his first page and his first room, in which he was refused in ninety seconds. **Five places asserted "one new name in Batch 0005" and the assertion was false** — `state/continuity.md` item 124, `state/batch-summaries.md`, `state/chapter-summaries.md`, `state/current.md` and this line — **and all five are now corrected. Do not let it back in.** **Volume 01 added no character who was not already named in `bible/characters.md`; the man with the mallet, the salt merchant, the sett-cutter and the toll-clerk on the north steps are all addressed by trade, and the two men hurt in Chapter 47 are unnamed on the page by design.**

### 3. State updates

- Append a **`## Canon established by the Volume 01 close`** heading to `state/continuity.md` with the numbered items the close establishes: the volume-02 ledger figures, the County of Ash's shape, the provincial office and its form, the eastern-counties claimant's form, the Ash nine-month cost, the Guild's Frostmonth election, the Halven trade's landing, and any correction the close makes to an earlier item.
- Update `state/current.md`: current phase becomes **volume close complete / Volume 02 outlined**, next planned phase is the Volume 02 Batch 0006 prompt, and the volume-02 day map and power state go in.
- Update `state/open-threads.md` with a short **"Threads the Volume 01 close carries into Volume 02"** list, and cross-reference it to the close document.
- Append a **Batch/phase record** to `state/batch-summaries.md` for this close, in the same shape as the five batch entries, saying what the close changed, what it corrected, and the question Chapter 51 opens on.
- Append per-chapter or per-block notes to `state/chapter-summaries.md` **only if the close changes a chapter's meaning**; do not rewrite the fifty entries.

## Hard requirements for the close

- **Do not write chapter prose.** No scene, no dialogue, no narrative. This is a planning phase. If you find yourself writing a sentence somebody would read aloud, put it in quotation marks inside a *document* the outline says exists, and stop.
- **Do not move the ending.** `outline/ending.md` is fixed. Every Volume 02 plan must be checkable against it.
- **Do not re-derive the calendar.** Continuity items 93, 111 and 112 own the weekday chain and the fever pattern, and the series ledger owns the drift. If a chapter appears to contradict one of them, **the chapter is wrong and the close records the correction**; it does not move the chain.
- **Do not total the four thousand with the seven villages, anywhere, in any file.** Four thousand is the Crown's figure. The seven villages are seven hundred and twenty by name, in the county's spelling, with `sum not stated` in the total line, and an eighth ruled line that is the city's and is still empty. Hushwater Reach in the path is near sixty and Hushwater in the main world is eighty, and the two are never printed together.
- **Do not explain the mechanism.** Nobody in Volume 01 learned why he can cross. Nobody may learn it in Volume 02 either — `outline/series.md` puts Ilyra's route at Volume 04's answer and the private-keeper clause at Volume 03's plant, and the identity of Ilyra's route at Volume 09. Volume 02 may deepen the wound and may name the wound's name in an office's hand. It may not answer it.
- **Preserve the four carried corrections** listed above, and say so in both output files.
- **A volume close that praises the volume is a bad volume close.** The audit has to find things, and the "did badly" paragraph has to be specific and has to be about the prose and the structure, not about the reviewer.

## Deliverables, in one place

- `outline/volumes/volume-01-close.md` — the close record.
- `outline/volume-02.md` — the Volume 02 outline, Chapters 51–100.
- Updated `state/continuity.md`, `state/current.md`, `state/open-threads.md`, `state/batch-summaries.md`, and `state/chapter-summaries.md`.

**Exactly one prompt exists for this phase: this one.** When it is done, the next phase is the Volume 02 Batch 0006 prompt, and that phase creates it, not you.
