---
name: analogues
description: Use when the user wants a problem or solution checked against how others solved the same kind of problem — "/analogues", "this is a classic X problem", "who else has solved this", "prior art for this". Names the classic problem family, gathers tech-company and non-tech solutions to it, then judges our solution against them and against doing nothing. Uses primary sources and tags every number.
---

# Analogues

Find the **classic problem** under our problem, see how others solved it, and judge our solution against theirs.

An **analogue** is someone else's case of the same classic problem. Every analogue matches ours only up to a point. The spot where it stops matching is where it **breaks**. Each analogue's break is the most important thing to record, because an analogue with an unstated break looks more convincing than it is.

Source and number rules: primary sources (official docs, source code, specs, first-party data), every claim cited, every number tagged **measured** (read from a source), **derived** (arithmetic on measured numbers), **model** (rests on assumptions) or **guess**. This skill adds one tier for non-tech analogues: books, HBR case studies and journalism may be used, tagged **secondary** beside the claim.

## Steps

### 1. Frame

Take the problem from the arguments if given. Otherwise infer it from the session (the MR, plan or design under discussion).

Show the user:
- **Our problem**, in 1–2 lines.
- **Our solution**, in 1 line (or "none yet").
- **The artifact**: the diff, code paths or design doc that hold our solution (or "none"). Step 3 checks against this, not the 1-line summary.
- **Our stack**: the category our solution lives in (for example "Postgres-backed job queue"), so the tech helper can find same-stack cousins.
- **2–3 classic problem families** it belongs to, each as "a classic _X_ problem" with one line on why.

Done when the user has OK'd the framing and the families. Wait for that OK before any helper starts; the families decide everything downstream.

### 2. Gather

Dispatch two helpers in parallel with the Agent tool, `model: sonnet`, `effort: medium`. One covers tech companies, one covers non-tech organizations (hospitals, airlines, governments, retailers, militaries, utilities, and so on). Give each the brief in [Helper brief](#helper-brief), filled in.

Caps across all families: **3–5 tech analogues**, **2–4 non-tech analogues**, plus **1–2 same-stack cousins** on top (tools in our own stack that solve the same problem, such as other Postgres job queues). Cousins are the closest fit and often carry the cheapest fixes. Prefer fewer, well-sourced analogues over many thin ones.

Done when both helpers have returned. Read each result. If one is thin (under the cap, missing sources, or vague on outcomes or breaks), rerun that one task on the parent model (leave `model` unset) and tell the user you did.

### 3. Compare

Score every analogue on four lines:

1. **Fit**: how close it is to our problem, and where it **breaks**.
2. **Evidence**: did it work? Measured results, or only claims? Carry the source tags through.
3. **Cost to adopt**: what doing the same would take for us.
4. **Lesson**: the one thing it says about our solution.

When there is an artifact, read it and check every lesson against it. Each place our solution falls short of a lesson is a **gap**: record it with `file:line` (or the doc section), the analogue behind it, and the cheapest fix. Also record **complements**: cheap additions the analogues pair with their main mechanism that we lack.

Then reach a **verdict** on our solution: **keep**, **change** (say what), or **drop**. Weigh it against the **do-nothing baseline** and the cheapest option. A secondary source can inform the verdict but never carry it alone.

Done when every analogue has all four lines, every lesson has been checked against the artifact (if any), and the verdict names which analogues and gaps drive it.

### 4. Write

Write one Markdown file where the repo already keeps such notes (match the convention; if none, pick a sensible spot and say where). Order:

1. **Verdict**: keep / change / drop, the why, and the analogues behind it.
2. **Gaps and complements**: each with `file:line`, the analogue behind it, and the cheapest fix.
3. **Comparison table**: one row per analogue (who, family, fit and break, evidence, cost to adopt, lesson).
4. **Framing**: our problem, our solution, the artifact, the families.
5. **Tech analogues**: detail per analogue.
6. **Non-tech analogues**: detail per analogue.
7. **Sources**.

Then give the user a short chat summary: the verdict, the top gaps, the 2–3 analogues that drive it, and the file path.

## Helper brief

Fill in the brackets.

```
Goal: find how [tech companies | non-tech organizations] solved [classic problem
families, one line each]. Our problem, for context: [1–2 lines]. Our solution:
[1 line].

Find [3–5 tech | 2–4 non-tech] analogues in total across the families. Choose the
ones with the best evidence of outcomes. [Tech only: also find 1–2 same-stack
cousins: tools in [our stack] that solve this problem. Record their defaults and
any cheap extras they pair with the main mechanism.]

Source rules: use primary sources, cite every claim, and tag every number
measured, derived, model or guess. [Non-tech only: start with regulations and standards (CFR,
OSHA, ICAO, safety-board rules): they are primary sources and their pages load
reliably. Books, HBR cases and journalism are allowed; tag each such claim
"secondary".]

Return, for each analogue:
- Who, and when.
- Which family it belongs to.
- Their problem, in 1–2 lines.
- What they did.
- The outcome, with every number tagged and a source link.
- Where it breaks: how their situation differs from ours.
- Source links.

Done when every analogue has a source link, a tagged outcome (or "no outcome
published"), and a break. Read-only: do not edit any files.
```
