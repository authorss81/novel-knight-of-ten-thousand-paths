# Continuity State

Bootstrap canon is established in `bible/`, `outline/series.md`, and `outline/ending.md`. No chapter prose exists yet.

## Hard canon

- World: Neyra, a late-medieval river-and-road world. Years count from the **Quiet Reckoning**; the story opens in **YR 312, Mudmonth**.
- Protagonist: Sir Aren Kest, thirty-two, a former Lantern Guard captain and current bridge repairer in Merefen. Estranged from Tovan; still idealizes Edric.
- Starting mystery: the Bellweather Sundering, **YR 301, Mudmonth**, erased Bellweather and seven villages. The story opens on the eleventh anniversary, in the same season. The Crown blames Aren’s failed bridge defense.
- The seven villages: Alder Cross, Saltbrim, Wrenlow, Cobbett, Nine Elms, Stonebarrow, Hushwater.
- Deeper answer: Marshal Edric Hunn and the Lantern Council ordered a forced cull to contain the Unwritten Wound; the order sacrificed a living city.
- Gatehouse rule: a living path cannot be reset or forcibly closed while conscious life exists inside it. Closing a route removes Aren’s access, not the world.
- **Local custody rule (added in bootstrap):** roads are opened by named local custodians, not by Aren. Two consenting custodians with paired anchors can open a road without him, and path communities can open roads to each other without the main world. Aren is a translator and temporary common anchor, never a necessary mechanism. The ending must show roads working without him.
- Path capacity: one at Stage 0/First Stitch, then two, three, five, seven, and ten at later stages. The final Unowned Road stage removes exclusive personal access.
- Path costs: roadmarks, memory loss, path bleed, lost time, failed workings, social obligations, and permanent local consequences. No path is a disposable map.
- Crossing budget: about three attempted crossings per season at any stage; three days of fever after a return at Stage 1, growing to a month at Stage 6. A return stitch is consumed by use.
- Final enemy: Edric Hunn, using the established First Witness protocol to activate the One Road. No new final enemy is planned.

## Canon clarifications recorded in this phase

1. **Name change.** The Culling Order field warden was renamed **Sera Dain → Sabin Dain** to remove a collision with Sera Quen. Use Sabin Dain in all prose and state.
2. **Name change.** The Lantern Council chancellor was renamed **Veyra Senn → Iselde Senn** to remove a collision with Mara Vey.
3. **Cast discipline.** At most six new named characters per batch. Every recurring character needs one want unrelated to Aren. No supporting character is killed for shock.
4. **The bell has provenance.** Crown salvage, sold at a Merefen clearance for two pence, bought by Aren as scrap bronze in the opening Mudmonth. It is a damaged anchor, not a key or a summons.
5. **Mara’s archive is the main-world Bellweather Claims Archive** in Merefen’s salt-loft rooms. It is not the living archive inside Bellweather-Living, which is run by Hollis Dree and refuses to surrender copies.
6. **Relationship policy is decided:** one slow-burn relationship, Aren and Mara Vey. No harem.
7. **Aren’s age arithmetic.** Aren is 32 at the opening and was **21** at the Sundering (born YR 280, apprenticed at twelve, Guard at seventeen, commissioned by brevet at twenty-one). This is deliberate: he was the youngest captain in the Guard, which is why Edric chose him, why the Crown can blame a boy, and why Aren believed his own defence for three years. Do not rewrite the Sundering as a child being made to do it alone. He held a real command and really failed it.
8. **The Rusk families are separated.** Jos Rusk, the Hushwater ferryman, survives and lives in Merefen; his claim is the first one Mara Vey personally refutes, and he is wrong about the cause. His wife **Anwen Rusk** (37, who kept the Hushwater ferry’s crossing book) and daughter **Bryn Rusk** (11) are among the erased and are now named outright instead of being left as “the wife and daughter.” The recurring Merefen ferryman formerly called Pei Rusk is **Pei Tarrow** (52, Hushwater survivor’s son, freight boats on the Old Toll channel). He is no relation to Jos Rusk. Do not stage the two men together, and do not let a bystander call Pei a Rusk.
9. **Hanna Vey and Mara Vey are not related.** The shared surname is deliberate common naming from the Sable river country, not a plot relation, not a mistake, and not a reason to rename either of them later. Let Mara notice the coincidence once, early and coldly, and never return to it. No scene may imply kinship.
10. **Toll figures are locked.** Bellweather city: about **four thousand**. The seven villages: about **seven hundred and twenty** (Alder Cross 200, Saltbrim 90, Wrenlow 60, Cobbett 140, Nine Elms 110, Stonebarrow 40, Hushwater 80). The Crown quotes the city figure alone and folds the villages into it; the Archive keeps the two numbers apart on every page and never prints a combined total. In a book whose moral weight rests on exact arithmetic, a character arguing about the dead must use the number actually being argued about.
11. **Dispatch reality, for the record.** The runner selects the first `workspace/**/PROMPT.md` in sorted order that has no `.done` or `.blocked` marker. `state/phase-ledger.json` and `PHASE_SYSTEM.md` are controller-owned, are never written by the writer, and the ledger is not what dispatch reads — so the only protection against a repeated batch is the prompt files themselves. Consequence: **exactly one prompt may exist per batch.** The duplicate `workspace/phase-002-batch-plan/` prompt, which also asked for Chapters 1–10, was deleted during the phase-000 fix pass. `workspace/volume-01/batch-0001/PROMPT.md` is the single prompt for the first batch and pairs with `outline/batches/volume-01-batch-0001.md`. The `.wip-conflict` marker in `workspace/phase-000-bootstrap/` only gates WIP-branch resume and is cleared by the runner on completion; leave it alone.
12. **The named dead are records, not cast.** Ferris Oat, Hanna Vey, Corin Slate, Bess Alder, Anwen Rusk, and Bryn Rusk are read aloud, quoted, filed, and argued over; they do not act on the page and do not count against the six-new-named-characters-per-batch limit. That limit applies to characters who speak, decide, or obstruct. A survivor or claimant who acts is a character and does count: Jos Rusk and Pei Tarrow are both cast, not records.

## Relationship starting point

Aren has not met Mara Vey before the opening batch. He is estranged from Tovan Kest and carries a mixed memory of Edric’s mentorship. Mara’s first appearance should establish her as an exacting archive keeper who questions the ethics of path evidence.

## Ending constraints

The ending must preserve Bellweather-Living as a living sovereign community, contain but not magically cure the Unwritten Wound, ratify the Charter of Many Roads, keep Aren and Mara’s relationship voluntary and independent, and leave Edric alive for public judgment.

## Knowledge control

`outline/series.md` contains a per-volume table of who knows what. Do not reveal a fact to any character before the volume listed there. This is the primary tool for protecting the central mystery across 900 chapters.
