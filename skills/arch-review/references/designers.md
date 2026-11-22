# Blind designers and the compare step

Designers solve the problem **without seeing the proposal**. If one lands where the proposal
landed, that is independent evidence the proposal is sound. If they all land somewhere else,
that is the strongest 🔴 signal this skill produces.

Count comes from `<pack>/confirmed.md`: light 0 · normal 2 · heavy 3. At 0, skip this file.

## Information rule

A designer may read:

- `<pack>/problem-brief.md` and `<pack>/map.md` (today's system, no proposed changes),
- `<pack>/sheet.md` (headlines only),
- any repo at its **default branch** via `glab api --method GET` with `ref=HEAD`, or a local
  clone only if it is already on its default branch (never fetch, checkout, or pull).

A designer may **not** read `<pack>/proposal.md`, `<pack>/proposal-delta.md`, `diff.patch`,
`discussions.json`, the MR, its branch, its thread, or its tickets. It must not search GitLab
or Jira for the ticket key or MR number.

Give designers file paths only for what they may read. Do not tell them what to ignore; just
never give them the rest.

## Claim step (one at a time, in order)

Each claim is a small agent (`sonnet`). Dispatch designer 1, wait, rule, then designer 2 with
the updated sheet, and so on.

> You are designer N. Read `<pack>/problem-brief.md`, `<pack>/map.md`, `<pack>/sheet.md`, and
> the lens list in `<skill>/references/lenses.md`. Pick one broad approach you believe could
> solve the problem well. Use the lenses to steer, not a stance. Choose an approach that is
> not already on the sheet. Reply with one line: `<where the fix lives> — <main tool or
> mechanism> — <why this is worth trying>`. Do not design it yet.

**The main session rules on overlap**, not the designer. Two headlines are the **same** when
the fix lives in the same place **and** uses the same main tool. Same → send it back once with
"that is taken by designer K; pick another." If the second try also overlaps, keep it and note
the overlap. Then append the headline to `<pack>/sheet.md`.

The real proposal is **never** on the sheet. So a designer may land on it by itself. That is
the point, not a bug.

## Build step (all designers in parallel)

Dispatch all build agents (`sonnet`) in **one message**. Each gets its own headline and the
sheet (headlines only, never another designer's details).

> You are designer N. Your approach: `<headline>`. Design it properly for the problem in
> `<pack>/problem-brief.md`, inside today's system in `<pack>/map.md`. Read code at each repo's
> default branch as needed. Write `<pack-root>/designers/designer-N.md` with exactly these
> sections:
>
> 1. **Components** — what exists after, and which service each piece lives in.
> 2. **Edges** — who calls whom, sync or async, with what timeout or retry.
> 3. **Data owner** — the source of truth for each piece of data, and who else reads it.
> 4. **Contracts** — APIs, tables, events, or files that change or appear.
> 5. **Rollout** — the order things reach prod, and how to back out.
> 6. **Trade-offs** — what this gives up, named on axes (risk, cost, reversibility, fit).
> 7. **Rough cost** — engineer-weeks, plus any new infra or third-party spend.
> 8. **Confidence** — high / medium / low, and the one fact that would change your mind.
>
> Prose and boxes-and-arrows only. **No code, no pseudo-code, no class or method names you
> invented.** "There is no real alternative to the obvious fix here" is an allowed answer; say
> why in section 6.
>
> Read-only. Do not edit anything except your own file. Do not spawn agents or invoke skills.
> Return one line: your approach and your confidence.

## Compare (main session)

Read each `designer-N.md` next to `<pack>/proposal-delta.md`. Two designs **match** when the
fix lives in the same place and uses the same main mechanism. Details may differ.

| What happened | Candidate |
|---|---|
| A designer matches the proposal | 🟢 Holds, with the designer as evidence |
| A designer matches the core but diverges on one part | 🟢 for the core, plus a 🟡 on that part |
| A designer diverges | 🟡 Decide, proposal vs that design |
| Every designer diverges, the same way | 🔴 Risk |
| Every designer diverges, in different ways | 🟡 Decide per divergence. No 🔴 from compare alone |

**Design-preference filter.** Each 🟡 must name the axis where the alternative is **better**:
risk, cost, reversibility, or fit. Different but not better on a named axis → drop it, or keep
it as a one-line aside. Log every drop in `<pack-root>/compare.md` so it can show up under
Dismissed findings.

Write `<pack-root>/compare.md`: one row per designer, match or diverge, the axis, and the
candidate verdict. These candidates go to the lens reviewers and the judge like any other
finding, with IDs `DES-1`, `DES-2`, ….
