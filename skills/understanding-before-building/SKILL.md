---
name: understanding-before-building
description: Use when you pick up an assigned unit of work — a ticket, issue, or request — and its full scope or rationale isn't self-evident from the item alone, before designing or coding. Applies whether or not there's an epic, design doc, or in-repo spec, and especially when the work depends on other items or on a contract (types, enums, endpoints, schema) defined elsewhere.
---

# Understanding Before Building

> **Status: draft — not yet baseline-tested.** Harden it with the RED scenarios at the bottom before relying on it as a discipline skill.

## Overview

Turn an assigned unit of work — plus whatever context happens to surround it — into a grounded, teach-backable mental model with explicit scope, **before** designing or coding. This is the research/scoping phase that feeds `superpowers:brainstorming`; do not design the solution here.

**Core principle:** Discover the context that actually exists (don't assume a shape), verify contracts against code (not prose), and state what's in and out of scope — before proposing anything.

## When to use

- You're handed a ticket / issue / request whose scope or "why" isn't obvious from the item text.
- It links to an epic, a design doc, an in-repo spec, other tickets, or a contract defined elsewhere (another service, package, schema).
- Even with almost no context (a bare ticket) — the method reconstructs intent from the code plus one clarifying round.

Skip for trivial, self-contained changes whose scope is already obvious.

## The method

### 1. Discover the context — follow pointers, don't assume a reading list
Start from what you're handed and follow every pointer outward until you stop learning new things. Gather whatever exists from this taxonomy; the absence of any one is fine:

| Source | Usually holds |
|---|---|
| Work item + its comments/history | the literal ask, recent pivots |
| Parent epic / initiative, siblings | the "why", the bigger goal |
| blocks / blocked-by / relates-to items | dependencies, sequencing |
| Narrative docs (Confluence, Google Doc, **in-repo spec/ADR/README**, PRD) | intent, decisions, constraints |
| The code — the feature today + the contracts it touches (types, enums, endpoints, schema, migrations), across repos/packages | the actual shape |
| People (reporter, domain owner) | intent you can't derive |

Read the **comments and dependency items** — that is where pivots and re-scopes hide.

### 2. Establish source of truth per fact type
- **Intent / behavior / "why"** → humans + narrative docs (newest wins; if docs disagree, ask).
- **Contract / exact shape** (names, enums, endpoints, schema) → the code that will actually run (merged/deployed), fetched fresh.
- **Conflict between them → surface it, don't silently pick.**

### 3. Build the model and teach it back
Explain it in plain language, as if to a smart non-expert. If you can't, you don't understand it yet — return to step 1.

### 4. Locate the feature in the code
Explore from a few named, distinct perspectives (e.g. data layer, UI, tests, the contract it depends on). Ground every claim in `file:line`. Parallel read-only agents work well when breadth is large.

### 5. Scope it
- **Objectives — SHOULD and SHOULDN'T.** Naming what's out of scope prevents creep and makes deferrals defensible.
- **Buildable now vs. blocked on a dependency.** What can ship behind a flag/stub vs. what must wait — and what safety invariant keeps the not-yet-live part invisible.
- **Open questions for humans.** Anything side-effectful or ambiguous.

### 6. Pressure-test, then hand off
Check the plan against the design's *spirit* and a future maintainer's eyes; enumerate the **whole value space** of any predicate/enum (unknown / other / not-yet-live). Decide **how you'll actually verify it working** (if the app is gated or hard to run, plan a stub) — then hand off to `superpowers:brainstorming` → `writing-plans`.

## Hard rules (don't skip under pressure)

| Rationalization | Reality |
|---|---|
| "The doc says the field/enum is X, I'll model that." | Docs state intent; **code defines the contract.** Verify names against merged/deployed code before modeling. |
| "The field isn't there, so it doesn't exist." | Your checkout may be stale. `git fetch` / check the deployed contract before concluding absence. |
| "I'll just handle the happy-path value." | Enumerate the whole value space — unknown, other, not-yet-live — or it breaks in review or prod. |
| "I'll assume what they meant for this side-effectful bit." | Side-effectful or ambiguous = an open question for a human, not a guess. |
| "There's no epic/doc, so there's nothing to research." | Reconstruct intent from the code it touches + one clarifying round. |

## Red flags — you skipped the grounding
- Building a shared type/enum from a name you only read in prose.
- Concluding "no such field/endpoint" without a fresh fetch.
- No SHOULD/SHOULDN'T list before designing.
- You can't explain the work simply.
- You didn't read the dependency items' comments.

## Common mistakes
- Treating the design doc as the contract (it's intent, not shape).
- Deferring "how will I see this work?" to the end — decide it during scoping.
- Guessing a side-effectful decision instead of listing it as an open question.
- Re-deriving facts already established; capture deferred work durably (a follow-up ticket) instead of holding it in your head.

## Hardening (run before relying on this)
Per `superpowers:writing-skills`, validate with RED baselines. Give a fresh agent, WITHOUT this skill:
1. A ticket whose **design doc uses a different enum/field name than the backend code** — confirm it models the doc name (the failure).
2. A ticket with a **scope pivot buried in a dependency ticket's comments** — confirm it misses the pivot (the failure).

Then verify this skill flips both. Add any new rationalizations it surfaces to the table above. These two failures are drawn from real sessions (an enum name mismatch shipped and caught late; a mid-stream design pivot that lived only in comments).
