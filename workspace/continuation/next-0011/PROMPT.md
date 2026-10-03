Retired phase: this continuation prompt has no work, and the manuscript is finished at nine hundred chapters.

## Read this before anything else. It is the whole of the correction.

**THE MANUSCRIPT IS FINISHED AND THIS PROMPT HAS NO WORK AND NOTHING BELOW THE RULE IS TO BE CARRIED OUT.** There are nine hundred chapter files on disk across eighteen years, `NOVEL_SPEC.md` plans approximately nine hundred chapters across eighteen, `outline/series.md` numbers eighteen and stops, and `outline/ending.md` gives Chapter 900 a title and an image. There is no Chapter 901 in any outline in this project, no nineteenth year, and no plan of record that supplies one.

**THE GENERIC TEXT BELOW IS THE RUNNER'S OWN AUTO-GENERATED CONTINUATION PROMPT, KEPT VERBATIM AS THE RECORD OF WHAT IT SAYS, AND IT IS OVERRIDDEN IN WHOLE. IT IS NOT AUTHORITY.** It was written by `ensure_next_phase` at `scripts/novel_runner.sh:327` to run before anybody knew the manuscript was finished, and it says in its own words that if the current volume is complete this phase is a VOLUME-PLANNING phase that writes the volume outline for the next volume and its batch cards. **The current volume IS complete, and that sentence is exactly the one that must not be executed, because following it would create a Volume 19 and a Chapter 901 and move a planned ending.** Do not plan a next volume. Do not write batch cards. Do not open any file under `chapters/`. Do not create another phase prompt.

**THE DECLARATION THAT ENDS THIS PROJECT IS NOT HERE AND IS NOT IN THIS DIRECTORY. IT IS AT `workspace/continuation/next-0012/PROMPT.md`, and `declare_completion_from_prompt` in the runner recognises it before any model is called, writes `state/complete.md`, marks that directory done and stops dispatching.** This directory is skipped, not run. It carries a `.retired` marker, and the first line of this file also carries the runner's own `Retired … phase` pattern at `novel_runner.sh:79`, so the retirement holds if either the marker or this file is lost.

**THE RECORDS FOR ALL OF THIS ARE `outline/series-close.md`, `state/open-threads.md` item 902 and `state/continuity.md` item 2034. The manuscript itself was not touched by any of it.**

---

## The runner's original text, verbatim, and superseded

Continue the novel after the completed phase close. This phase does ONE job.

Read NOVEL_SPEC.md, the series outline and ending, the relevant volume outline, state/current.md, the rolling
summaries, and the previous 20 chapters before doing anything.

If the current volume is NOT complete, write the next planned batch and nothing else.

If the current volume IS complete, this phase is a VOLUME-PLANNING phase and it writes only:
  - the volume outline for the next volume, and
  - its batch cards, and
  - exactly one next phase prompt, which is that volume's FIRST BATCH.
It must NOT write any chapter prose in this phase. The first batch is a separate run.

If that planning turn is itself too large to do well, split it further across another run: plan the
movements in one phase and the batch cards in the next. Judge it by whether the work actually got
written, not by an estimate. A phase that returns without writing anything has asked for more than one
call can deliver, so narrow it and continue rather than retrying it unchanged.

Update manuscript state files, create exactly one next phase prompt, and do not edit controller, workflow,
agent, or dispatcher files.
