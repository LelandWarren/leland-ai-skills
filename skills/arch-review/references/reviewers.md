# Lens reviewers

Three reviewers, split by the **question they ask**, not one agent per lens. This spreads
evidence, not opinions: each one looks at the change from a different side, and they never see
each other's work.

Each reviewer runs only its lenses that appear in `<pack>/confirmed.md`. The core lenses are
spread so no reviewer is idle.

| Reviewer | Prefix | Asks | Lenses it owns |
|---|---|---|---|
| **Fit** | `FIT-` | Is this the right thing, in the right place? | C1 System fit · #1 One path, one choke point · #5 Data ownership and identity · #13 Abstraction earns its keep · #15 Problem fit and scope · #17 Ownership and lifetime cost · #18 Load-bearing removals |
| **Failure** | `FAIL-` | What happens when it breaks or gets busy? | C2 Blast radius & failure unit · #3 Cross-service calls · #4 Shared capacity and load shape · #7 Replay and idempotency · #9 Detection · #11 Unknown-input policy · #12 Real-infra guarantees · #14 Tradeoff points |
| **Time** | `TIME-` | What does this look like in six months, and to whom? | C3 Premises measured · C4 Cost of being wrong · #2 Contracts and intermediaries · #6 Downstream consumers and history · #8 Rollout order · #10 Trust boundary and PII · #16 Second-order effects · #19 Bets on things we don't control |

At **light** tier the main session runs every confirmed lens inline, using the same return
contract as its own checklist. At normal and heavy, dispatch all three (`sonnet`) in **one
message**.

## Brief (same for all three, with the row filled in)

> You are the **<Reviewer>** reviewer in an architecture review. Your question: *<Asks>*.
>
> Read the whole pack at `<pack>/` (proposal, delta, map, context, diff if present,
> discussions if present), `<pack-root>/compare.md`, and `<pack-root>/designers/*.md` if they
> exist. Read code anywhere you need: the repo under review on the MR branch, other repos at
> `ref=HEAD` via `glab api --method GET`.
>
> Run these lenses from `<skill>/references/lenses.md`: <owned lenses that are in
> confirmed.md>. Apply its **What counts as architecture** tests to every finding. A finding
> that passes neither test goes under **Line-level notes** as one line, with no verdict.
>
> Weigh the designer candidates (`DES-n`) that touch your lenses: agree, sharpen, or argue
> against, with evidence. Do not re-issue them under your own prefix.
>
> Write `<pack-root>/reviewers/<reviewer>.md` using the return contract below, IDs prefixed
> `<PREFIX>`. Return one line: counts of 🔴 / 🟡 / 🟢.

## Return contract

Every reviewer returns **all four parts**. Part 2 is the one agents forget: without it a
clean review comes back empty, and the report cannot show that a 🟢 was actually judged.

```markdown
# <Reviewer> report

## 1. Findings

### <PREFIX>-1: <one-line claim about components or flows>
- **Lens:** <exact lens name>
- **Candidate:** 🔴 Risk | 🟡 Decide
- **Door:** one-way | two-way
- **Architecture test:** rewrite | map (<what on the map changes>)
- **Evidence:** `path/File.java:88`, a contract, a ticket, or a memory/CLAUDE.md fact
- **What goes wrong:** Given <state or load>, <component> does <X>, so <who notices> sees <Y>.
- **Other path:** <alternative> — rough cost <engineer-days/weeks, infra>
- **Downside of the path you'd recommend:** <what it costs or risks>
- **Owner** (unmade decisions only): <team or role who must pick>

(Repeat. If none, write "None.")

## 2. Lens verdicts

| Lens | Verdict | Why |
|---|---|---|
| C2 Blast radius & failure unit | 🟢 | Holds while the tracking client keeps its 30s timeout; a failure stays inside one batch run. Watch: pool size. |
| #4 Shared capacity | 🔴 | See FAIL-1. |

One row per owned lens that ran. A 🟢 row must say **"holds while …"** and name the assumption.
It may add a **Watch:** note for a sensitive spot.

## 3. Needs a number

Premises only a live count can settle. One line each: the question, where the answer lives
(table, metric), and which finding it would change. Never run the query yourself.

## 4. Line-level notes

One line each. These collapse into the report's "Out of scope — run /pr-review" line.
```

## Rules binding on every reviewer

- **Claims about components and flows.** `file:line` may be evidence, never the claim.
- **Evidence or drop it.** No location, contract, or fact behind it → not a finding.
- **PII:** cite by location. Never quote a street address, recipient name, or phone number.
  Postal code, city, region/state, country, and PO-box flag are fine.
- **Read-only.** Write only your own report. `glab api --method GET` only, params in the URL,
  never `-f`/`-F` (glab silently turns those into a POST). No DB or metrics queries.
- **No delegation.** Do not invoke skills or spawn agents.
