# Manuscript completion declaration — Chapters 1 to 900, eighteen years, and no work remains

## 1. What this phase is, in one sentence

**THE MANUSCRIPT IS COMPLETE AND THIS PHASE DECLARES THE COMPLETION AND WRITES NOTHING.** There are nine hundred chapter files on disk across eighteen years, `NOVEL_SPEC.md` plans approximately nine hundred chapters across eighteen, `outline/series.md` numbers eighteen and stops, and `outline/ending.md` gives Chapter 900 a title and an image. **There is no Chapter 901 in any outline in this project, there is no nineteenth year, there is no next part to write, and no phase may write one.**

**THIS PROMPT DELIBERATELY CARRIES TWO STRINGS THAT `scripts/novel_runner.sh` ACTUALLY MATCHES, being `THIS PHASE DECLARES THE COMPLETION` in this section and `THE MANUSCRIPT IS COMPLETE` in this section, and it relies on a third, being `Write nothing.` in §3. Do not shorten them to `declare the completion` or to lower-case `manuscript is complete` without re-reading `declare_completion_from_prompt`, because the runner's first pattern is `this phase (verifies|records|declares)|the runner recognises the declaration|declare (the )?completion|write nothing` and its second is `manuscript (is|has) (finished|complete)|novel is (finished|complete)|book is (finished|complete)`, and it is the phrases as they stand that satisfy them, and `The runner recognises the declaration` in §1 satisfies the first pattern a second time.** A phase asked to write when there is nothing to write returns an empty result, which the runner cannot tell apart from a failure, and it burns every attempt until it blocks itself. The controller has a path for exactly this case and this prompt uses it: `declare_completion_from_prompt` is called at `novel_runner.sh:372`, before the model loop, and it writes `state/complete.md`, touches this directory's `.done` and stops dispatching.

**AND THIS PHASE IS REACHED ONLY AFTER `workspace/continuation/next-0011/` RECEIVES ITS `.done` MARKER, which the runner writes at `novel_runner.sh:480` on the success path of the phase that was running when this file was written.** That is expected and not a fault. The selection loop takes the first prompt in sorted order that has no `.done`, so a declaration must sit one place behind the live phase. `ensure_next_phase`, called at line 479 immediately before that marker is written, finds this directory already present as another incomplete phase and therefore creates no further prompt, so nothing loops and nothing competes for selection. **If this phase is ever dispatched while `next-0011` is still unmarked, that is the anomaly to report, and it is not a reason to write anything.**

## 2. What is on disk, re-derived, so that the declaration is a measurement and not a belief

- **900 chapter files**, `chapters/volume-01/chapter-0001.md` through `chapters/volume-18/chapter-0900.md`, fifty per year, no gaps in the numbering.
- **2,641,013 words**, on a whitespace-delimited token count over the file whole, being `cat` over each year's fifty files piped to `wc -w`. All eighteen per-year figures reproduce the figures already printed in `state/current.md` and in each year's own close record, to the word.
- **The last page is `chapters/volume-18/chapter-0900.md`**, dated the twenty-fifth of Frostmonth YR 325, a Tuesday and not a market morning, being day 3690, which derives from the single anchor of day 2310 being a Monday with Mudmonth at sixty days and every other month at thirty and the year turning at the first of Thawmonth.
- **All nineteen setup-to-payoff rows in `outline/ending.md` are paid on a page**, and none was left for a later year.
- **All five questions the plan says stay open are still open at the end of the year**, and none of them implies a new enemy.
- **Eighteen years, seventeen close records, one records gap** at `state/open-threads.md` item 539, being that Year 10 has none. The gap is recorded and not filled and this declaration does not fill it.
- **The series-level record is `outline/series-close.md`** and is on disk.

## 3. What this phase must not do

1. **Write nothing.** Not a chapter, not a page of prose, not an outline, not a card, not a summary, not a state line, not a marker. The only thing this phase produces is the runner's own `state/complete.md`, which the runner writes by itself.
2. **Do not create a Volume 19, a Chapter 901, a new antagonist, a sequel, a prequel or an epilogue.** The plan of record ends at Chapter 900 and `outline/ending.md` is fixed.
3. **Do not resolve any of the five open questions**, do not cure the bleed, the engine damage or the scar, do not mend the join in the founding paper, do not answer the written request sent up the ordinary post, and do not conduct the trial that is ordered and not held. **The plan puts that trial inside Chapters 891 to 895 and the pages order it and do not hold it, and that gap is a finding and not something to close.**
4. **Do not open any file under `chapters/`.** All nine hundred pages belong to completed phases.
5. **Do not touch** `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or `state/phase-ledger.json`. **That last one is still `phase-000-bootstrap`, status `planned`, attempts 0, against nine hundred chapters on disk; the count of phases that have reported it is twenty-two and that count is carried from `outline/volumes/volume-18-close.md`, which prints twenty-one. It is controller-owned and this phase reports the finding and does not touch the file.**
6. **Do not thank anybody.**

## 4. If the runner calls a model for this phase anyway

**Write nothing and say nothing.** If a model is invoked, the correct output is no file changes at all, because the declaration has already been recorded by the runner before the call. Do not attempt to reconstruct `outline/series-close.md`, do not re-verify anything, do not produce a summary of the manuscript, and do not treat the empty result as a failure to be retried. The empty result **is** the correct output.

**One order dependence is worth naming.** `retire_obsolete_phases` runs at `novel_runner.sh:106` and calls `scripts/rescue_overscoped.py`, which prepends a header instructing a writer to *write the chapters*, whereas `declare_completion_from_prompt` runs at line 372. `rescue_overscoped.py` only walks directories containing a `.blocked` marker, and this directory does not and must not, so the two cannot collide. **If a `.blocked` marker ever appears here the declaration path becomes unreachable, and that is the finding to report rather than a licence to write a chapter.**

## 5. The one line that is the whole of this file

**The Knight of Ten Thousand Paths is finished at nine hundred chapters and 2,641,013 words, and the last thing a man does in it is stand four paces off a toll bridge at dawn with his tool bag at his feet while three other people open a road, and it answers across the water for about four hundred people who are not there, and nobody thanks anybody, and he goes home.**