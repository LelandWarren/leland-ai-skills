# Adversaries and the cold judge

## Adversaries

Run after the reviewers. **Normal:** straw-man only. **Heavy:** straw-man first, then the
steel-man once the straw-man is done, so every finding (including `STRAW-`) gets a defense
before the judge. Both run on `sonnet` and read the whole pack, `compare.md`, `designers/`,
`reviewers/`, and (steel-man only) `adversaries/straw-man.md`.

The two are asymmetric on purpose. The steel-man attacks the **findings**. The straw-man
attacks the **design**. If both attacked the design, false positives would live on, and
killing false positives is half the reason this step exists.

### Steel-man — `adversaries/steel-man.md`

> Defend the proposal. For every `DES-`, `FIT-`, `FAIL-`, `TIME-`, and `STRAW-` finding, argue as hard
> as the evidence allows that the proposal is right. You may use constraints the blind
> designers never had: history in `context.md`, deadlines, team size, what the neighbors
> already do, what a past incident taught.
>
> For each finding write **stands / weakened / falls**, with evidence for the verdict itself.
> "Falls" needs positive evidence the proposal is right, not just a missing proof that it is
> wrong. For each `DES-` alternative, say whether it is truly cheaper or safer once those
> constraints are counted.
>
> Raise no new findings. Anything new goes in one line under "Noted, out of scope."
>
> Read-only, no delegation, `glab api --method GET` only. Return one line: stands / weakened /
> falls counts.

### Straw-man — `adversaries/straw-man.md`

> Assume every reviewer was too polite and too narrow. Run a **pre-mortem**: *it is six months
> later and this design failed. Write the most likely story of why*, in five to ten plain
> sentences. Then turn each distinct cause in the story into a finding, unless it is already on
> the list.
>
> Look hardest where the reviewers are structurally weak: the seams between two lenses; what
> is true of the design as a whole but of no one file; the second run (retry, replay,
> redeploy, rollback); the day an upstream team changes something they never promised; wild
> success (10× volume, other teams copying it).
>
> Same evidence bar and return contract as the reviewers (`<skill>/references/reviewers.md`),
> IDs prefixed `STRAW-`, no Lens verdicts table. Put the pre-mortem story at the top.
>
> Read-only, no delegation, `glab api --method GET` only. Return one line: finding counts.

## Before the judge: the cap

Count findings after grouping obvious duplicates (same component, same failure). If more than
~15 groups remain, the main session keeps every 🔴 and the strongest 🟡 up to ~15. The cut
groups go to the report as **"Not judged (over cap)"**, one line each, so nothing vanishes
silently. The judge gets the kept findings as **raw IDs** plus the suggested groups, and does
the real merge itself.

## Real numbers (between the adversaries and the judge)

Only if some report lists **Needs a number**, and only if the answer could change a verdict.

1. Collect the questions. Drop any whose answer would not move a verdict.
2. Ask the user once, listing each query in plain words (what it counts, where). Wait for a
   yes.
3. Run read-only tools the user has (a guarded DB-read tool, a metrics tool). **Counts and
   totals only, never rows.** Keep queries narrow and `EXPLAIN` anything broad: production
   databases may be small and busy.
4. Write `<pack-root>/numbers.md`: question, query in words, result, which finding it touches.

No yes, or no tools → those premises go to **Open questions**. Say so.

## Cold judge — `judge.md`

Runs on **`opus`**. It has not seen the conversation, the checkpoint dialogue, or anything the
user said. That coldness is the point: nothing said earlier can anchor it. Never paste
conversation history into its prompt.

> You are judging an architecture review. Read `<pack>/`, `<pack-root>/compare.md`,
> `designers/`, `reviewers/`, `adversaries/` if present, and `numbers.md` if present. The
> lens definitions and the **What counts as architecture** tests are in
> `<skill>/references/lenses.md`.
>
> **Rule on every finding** (`DES-`, `FIT-`, `FAIL-`, `TIME-`, `STRAW-`). Verify each at the
> source (the file, the contract, the number). Do not take a reviewer's word for it. Where
> the steel-man says a finding falls, check its evidence yourself; it is an advocate, not an
> authority.
>
> - **confirmed** — real. Give the final verdict (🔴 Risk / 🟡 Decide) and the door tag.
> - **downgraded** — real but smaller. 🔴 → 🟡, or 🟡 → a 🟢 with a Watch note. Say why.
> - **dismissed** — not real, not architectural (fails both tests), or only a preference.
>   Say what disproves it.
>
> For every alternative path: is it **really cheaper or safer** on a named axis (risk, cost,
> reversibility, fit), or just different? Just different → the finding is dismissed as a
> design preference.
>
> **Merge duplicates.** Two sources reaching the same problem from different evidence is a
> stronger finding, not two. Keep every contributing ID.
>
> **Merge the lens verdicts** from all reviewer tables into one table covering every lens
> that ran. Where two disagree, take the worse and keep both reasons. Keep every 🟢 row with
> its "holds while …". Then reconcile: a lens whose only findings were dismissed becomes 🟢; a
> confirmed finding with no lens row sets that row. The findings and the table must not
> contradict each other.
>
> Write `<pack-root>/judge.md` with four sections:
>
> 1. **Rulings** — `ID | claim | ruling | reason`. Every input ID appears, dismissed included.
> 2. **Confirmed findings** — deduplicated, 🔴 before 🟡, each in the reviewer return-contract
>    shape with its final verdict and door tag.
> 3. **Merged lens verdicts** — every lens that ran, 🟢 rows included.
> 4. **Open questions** — what no one could verify, and what would settle it.
>
> Read-only, no delegation, `glab api --method GET` only. PII by location, never by value.
> Return one line: confirmed / downgraded / dismissed counts.

## Degradation

- **An agent fails or returns nothing** → the main session runs that role itself and **says
  so out loud**. A lens never silently disappears from the report.
- **A reviewer returns findings but no Lens verdicts table** → re-run it once, then fill the
  table inline and note it.
- **The judge fails** → the main session judges and states that cold-judge independence was
  lost on this run.
- **Normal tier (no steel-man)** → say in the report that nothing defended the proposal
  against the findings, so false positives are likelier.
- **No Agent tool** → the main session runs every step inline at the confirmed tier's depth,
  skips the blind designers (it has seen the proposal, so it cannot be blind), and says so.
