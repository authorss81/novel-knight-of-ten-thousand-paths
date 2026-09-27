# State Archive

**Four ledgers were put on a rolling window during the review of Volume 07 Batch 0004, because between them they had grown to about 4.8 MB and were being carried whole into every phase, which is the opposite of what AGENTS.md asks a rolling summary to be.** The files in this directory are the parts that were moved out. **They are not deleted, not summarised and not renumbered, and each is a byte-for-byte copy of exactly the text that was cut from the live file.**

| Archive file | Cut from | Holds | Items/sections |
| --- | --- | --- | --- |
| `continuity-volumes-01-06.md` | `state/continuity.md` | Volume 01 to Volume 06, batch by batch, every volume close, and the six review-repair sections | continuity items 1 to 859 |
| `open-threads-volumes-01-06.md` | `state/open-threads.md` | the initial threads, the outline-phase answers, and the per-batch thread sections for Volumes 01 to 06 | all sections before *Threads Volume 07 Batch 0001 carries into Batch 0002* |
| `batch-summaries-volumes-01-06.md` | `state/batch-summaries.md` | one entry per batch for Volumes 01 to 06, including all five volume closes and every review-repair entry | all sections before *Volume 07 — Batch 0001* |
| `chapter-summaries-volumes-01-06.md` | `state/chapter-summaries.md` | the Volume 01 index and one section per batch for Volumes 01 to 06 | Chapters 1 to 300 |

**Four rules govern the window, and a phase that breaks one has broken canon rather than tidied it.**

1. **Numbers are never renumbered.** A continuity item number means the same thing here as in the live file, and so does a thread, chapter or batch number. Item 412 is findable either way.
2. **Nothing is deleted, only moved.** Reconstruct any earlier state of any of the four ledgers by concatenating the archive back onto the live file at the cut point.
3. **A volume is never archived while it is being read.** The window moves forward at a volume close, after the close has audited the volume it is closing, and never in the middle of one.
4. **Global material is never archived.** Sections that bind the whole project rather than one volume stay in the live file whatever their byte offset. That is why `## Hard canon`, `## Ending constraints` and `## Knowledge control` are live in `state/continuity.md`, and `## Initial story threads`, `## Answers to the questions the outline phase had to settle` and `## Final-volume questions` are live in `state/open-threads.md`, even though each of them sits at a byte offset that would have swept them into an archive. **They are also still in the archives, because the archives are copies, and a global section appearing in both places is harmless and a global section appearing in neither is not.**

**The window does not move again until the Volume 07 close.** Volume 07 is live in all four files and a close audits the volume it is closing, so the close is where the cut for Volumes 01 to 07 is made, and it is made after that close has read the volume and not before.
