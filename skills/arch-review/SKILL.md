---
name: arch-review
description: Use when the question about a GitLab merge request or a design proposal is whether the design is sound and fits the surrounding systems — "architecture review", "arch review", "is this design sound", "does this fit the system", "review this proposal", "/arch-review". Also for an idea with no written proposal yet. NOT for line-level bugs, style, or test gaps (use pr-review), and NOT for a health check of an existing area with no change proposed.
---

# Architecture Review

Review the **shape** of a change, not its lines. Two questions: is the plan sound, and does it
fit the systems around it? Think of a building inspector reading the floor plan: where the load
goes, what happens in a fire, how hard it is to move a wall later.

Its signature move: **blind designers** solve the same problem without seeing the proposal. If
they land where the proposal did, it holds. If they all land somewhere else, that is a 🔴.

## Inputs

- A GitLab MR (URL or `!iid` + repo).
- A design proposal: a doc, a ticket, a Confluence page, a file.
- An idea with nothing written. First write **"Your proposal as I understand it"**, get it
  confirmed, then review that.

## Prerequisites

- `glab`, authenticated. Credentials come from the user's environment; this skill holds none.
- The Agent tool (for designers, reviewers, adversaries, judge). Without it, see Degradation in
  `references/adversaries-judge.md`.
- Optional: Jira/Confluence connectors for tickets and docs; a read-only DB tool and a metrics
  tool for the real-numbers step.

`<skill>` below means this skill's base directory. `<scratchpad>` means the session's scratch
directory.

## What counts as architecture

A finding must pass one test. **Rewrite:** it stays true if every line is rewritten into the
same boxes and arrows. **Map:** its fix changes a component, edge, data owner, contract,
runtime property, or rollout step, or it is a one-way door. Tie-breaker: would another team,
service, or on-call notice? Everything else is one "run /pr-review" line. Full text in
`references/lenses.md`.

## The flow

Track the phases as a todo list if a todo tool exists, otherwise as a checklist in chat. Two stops (the 🚧 gate and the 🛑 checkpoint), plus an ask before any live query.

| # | Phase | Who | Reference |
|---|---|---|---|
| 0 | 🚧 **Decision gate**: who could own this, have they framed it, who reads downstream | main | below |
| 1 | **Gather** the evidence pack, once | main | `map.md` |
| 2 | **Map** today's neighborhood, write the delta and the problem brief, suggest tier + lenses | main | `map.md` |
| 3 | 🛑 **Checkpoint**: map, scope, tier, lenses (core + picks), problem brief leak check, designer count | main | `checkpoint.md` |
| 4 | **Blind designers**: claim one at a time, then build in parallel | sonnet × 0/2/3 | `designers.md` |
| 5 | **Compare** designs to the proposal → `DES-` candidates | main | `designers.md` |
| 6 | **Lens reviewers**: Fit, Failure, Time | sonnet × 3 (light: inline) | `reviewers.md` |
| 7 | **Adversaries**: straw-man pre-mortem (normal+), steel-man (heavy) | sonnet | `adversaries-judge.md` |
| 8 | **Real numbers**, only if a verdict hinges on one, only after a yes | main | `adversaries-judge.md` |
| 9 | **Cold judge**: verify, merge, rule on alternatives | opus | `adversaries-judge.md` |
| 10 | **Report** + short verdict in chat | main | `report.md` |
| 11 | **Memory**: offer to save lasting system facts | main | below |

Every agent gets the pack **by path**, writes its report to its own file, and returns one line.
Read reports from disk, not from return values. That keeps the main window small.

## Decision gate

A hard stop before phase 1. Nothing is read until it clears. Answer four questions in chat:

> 1. Which systems could own this?
> 2. Who owns each one? (name the owning team, not a single person)
> 3. Has each owner helped frame the problem?
> 4. Who reads this data downstream?

Answer from what is already known. "Don't know" is a valid answer; it becomes an open question
in the report.

Then rule:

- **Every candidate system is ours, or every outside owner has helped frame it** → clear. Carry
  the answers into the map (phase 2) and C1.
- **Another team's system is a candidate and its owner has not helped frame it** → stop. Say
  which owner to bring in, and wait. Clear only if the user explicitly says to go ahead without
  them, and say so in the report.

Why it runs first: in one real review, blind designers and a cold judge ruled one way. The call flipped once the other system's owner joined, because the owner held
downstream facts no review could reach. Blind designers fix anchoring on the proposal. They do
not fix a missing person in the room.

## Core lenses (always on)

- **C1 System fit** — right service, fits its neighbors, not already built elsewhere.
- **C2 Blast radius & failure unit** — when it fails, what fails with it, and is that the
  intended unit.
- **C3 Premises measured** — which data facts it assumes, whether prod was measured, the
  tripwire when one breaks, and which decisions are still unmade.
- **C4 Cost of being wrong** — if the *design* is wrong in six months: what piles up, flat or
  compounding exit cost, the cheapest hedge today.

The 19-lens catalog is in `references/lenses.md`. The map step picks from it by signal.

## Hard rules

1. **Read-only.** Never write to GitLab, Jira, Confluence, a database, or any external system.
2. **`glab api --method GET` only**, params in the URL. Never `-f`/`-F`: glab silently switches
   to POST when fields are added, and the token may be able to write.
3. **Designers never see the proposal.** Only the problem brief, today's map, and the sheet.
4. **One checkpoint after the gate.** Do not stop between phases 4 and 10 except to ask before a live query.
5. **Every finding needs evidence** (`file:line`, a contract, a ticket, a number) and **another
   path with its rough cost**. No evidence or no alternative → it is an open question, not a
   finding.
6. **🟢 names what it rests on** ("holds while …"). **🔴/🟡 carry a door tag** (one-way /
   two-way). **Unmade decisions are 🟡 with an owner.**
7. **Different is not better.** An alternative must win on a named axis (risk, cost,
   reversibility, fit) or it is dropped as a design preference, and shown as dismissed.
8. **No PII** in any report or chat message. Live data: counts and totals only, never rows.
9. **Say it out loud** whenever a step degrades.

## Memory

After the report, offer to save **lasting system facts** the review learned (a timeout
contract, a capacity limit, who owns a table). One fact at a time, only with the user's yes, in
the user's memory system. Never per-MR trivia, never PII, never a growing map file: a map file
goes stale silently, and the next run re-reads `CLAUDE.md` and memory anyway.

## Common mistakes

Seen in a no-skill baseline review of a real MR:

| Mistake | What it looks like | The fix in this skill |
|---|---|---|
| **Anchoring on the proposal** | "Right layer," then every later question judged from inside the proposal's frame. The fix-it-at-the-source option is never priced. | Blind designers run before anyone grades. C1 asks "does this belong here" as its own question, with an alternative and a cost. |
| **Judging like a merge gate** | Every finding sorted into "blocker / not a blocker." Design questions get parked as "settle before prod." | Verdicts are 🔴 Risk / 🟡 Decide / 🟢 Holds, about the design, not the merge. A real open choice is 🟡 with an owner, even if merging is safe. |
| **Tuning instead of asking whose promise it is** | Deep analysis of a timeout value or a range boundary, never "which team owns this, and did they promise it?" | #3 Cross-service calls and #19 Bets on things we don't control ask ownership directly. |
| **Mixing in line-level notes** | Javadoc wording, metric tags, a missing test stub, given the same space as architecture. | The rewrite/map tests. Anything that fails both is one "run /pr-review" line. |
