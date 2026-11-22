# Wave Review

How `pr-review` phase 5 runs its lenses across agents. The lens *content* lives in
`lenses.md`; this file is only about **who runs which lenses, on what evidence, in what
order**.

The organizing idea: **this parallelizes evidence, not opinions.** Four wave-1 reviewers
see four different things. That is why they are worth running, and why they must not talk
to each other.

## Wave depth

**SKILL.md phase 5 branches on the wave depth recorded in `<pack>/confirmed.md`, not on the
tier directly.** The tier only supplies that depth's default; the user may override the
depth at Checkpoint 1 independently of the tier, and the override is what phase 5 runs.

| Tier (default source) | Depth | What runs |
|---|---|---|
| Light | 0 | Main session grades inline, exactly as before waves existed |
| Normal | 5 | Wave 1 + wave 3 judge |
| Heavy | 7 | Wave 1 + wave 2 + wave 3 judge |

Changing the tier moves the depth with it unless the user overrides the depth separately.

Wave depth is a closed set — 0, 5, or 7. Anything else the user asks for is confirmed
back to the nearest of the three (ties round up).

**Models:** the six reviewers run on `sonnet`. The judge runs on `opus`.

## Evidence pack

Built **once**, by the main session, in phase 1–2. No agent re-fetches the MR.

Why once: four agents each running `glab mr diff` is four copies of the same bytes, and a
push landing mid-review would hand different agents different diffs. One pack keeps hard
rule 1 — *diff is source of truth* — literally true across all seven agents.

`<pack-root>` is `<scratchpad>/pr-review-<id>/`; `<pack>` is `<pack-root>/pack/`.

### Layout

```
<scratchpad>/pr-review-<id>/
  pack/
    mr-view.md            # glab mr view <id>
    diff.patch            # glab mr diff <id>
    discussions.json      # glab api .../discussions
    changed-files.txt     # the real file list, derived from diff.patch
    context.md            # Jira chain, repo CLAUDE.md notes, recalled memory facts
    confirmed.md          # written after Checkpoint 1: lens set, tier, wave depth
  wave1/
    spec-reader.md
    diff-reader.md
    second-question.md
    link-walker.md
  wave2/
    steel-man.md
    straw-man.md
  wave3/
    judge.md
```

Every agent is given the pack **by path** and writes its report to its own file above. It
returns only a one-line summary to the main session. Reports are read from disk, not from
agent return values — that is what keeps the main window small.

`changed-files.txt` is the authoritative file list. An agent that finds a filename in a
description but not in `changed-files.txt` reports that as drift, not as a change.

## Return contract

Every reviewer and adversary returns **two** things. Part 2 is easy to forget and is not
optional: phase 7's scorecard covers *every lens that ran*, and phase 8's pass-summary is
a per-lens "why it passed" rundown. If an agent returns only problems, a clean review
comes back empty and neither artifact can be built.

```markdown
# <role> report

## Findings

### <PREFIX>-1: <one-line claim>
- **Lens:** <exact lens name from lenses.md>
- **Severity:** blocking | non-blocking
- **Evidence:** `path/to/File.java:88`
- **Failure scenario:** Given <input/state>, the code does <X>, which breaks <Y>.

(Repeat per finding. If there are none, write "None.")

## Lens verdicts

| Lens | Verdict | Why |
|---|---|---|
| Correctness | ✅ | Handles null and empty; no concurrent path touched |
| Test honesty | ⚠️ | `FooTest.java:41` asserts on the DTO, not the persisted row |
```

Rules binding on every agent:

- **Finding-ID prefixes**, so the judge can reference findings unambiguously:
  `SPEC-` · `DIFF-` · `SQ-` · `LINK-` · `STRAW-`. The steel-man issues no new IDs.
- **One row per lens you own**, including ✅ rows. A ✅ row says in a few words *why* it is
  clean. Legend: ✅ clean · ⚠️ non-blocking finding/caveat · ❌ blocking problem.
- **`file:line` or drop it.** A finding with no location and no concrete failure scenario
  is not a finding.
- **PII:** cite `file:line`, never quote a PII value (street address, recipient name,
  phone). Postal code, city, region/state, country, and PO-box flag are fine.
- **Read-only.** Do not edit, write, or create any file except your own report. Never post
  to the MR. Never run `glab mr note`, `glab mr approve`, or any write command.
- **No delegation.** Do not invoke other skills or spawn further agents.

## Wave 1 briefs

All four dispatch **in a single message** so they run concurrently. Independence is
structural — none can observe another's output because none has finished when the others
start. Do not tell them to "ignore" each other; just never give them each other's files.

The six always-core lenses spread across all four, so no reviewer is idle even on a small
MR: problem-fit + spec fit (spec reader), correctness + test honesty (diff reader),
readability (second question), MR-as-communication (link walker).

Any lens in `confirmed.md` that no brief claims goes to the reviewer whose evidence it
needs — the main session decides and names it in that agent's dispatch — except
knowledge sharing / mentorship, which always stays in the main session. If no reviewer
can see the evidence that lens needs, the main session runs it inline and says so.

### 1. Spec reader — `wave1/spec-reader.md`

> You are reviewing a merge request's **intent**, not its code. You may read
> `<pack>/mr-view.md`, `<pack>/context.md`, `<pack>/discussions.json`, `<pack>/confirmed.md`,
> and the linked Jira tickets. **You may NOT open `diff.patch` or any source file.** That
> restriction is the point: a reviewer holding the code rationalizes the code.
>
> Run these lenses from `lenses.md`: **problem-fit** and **spec / acceptance fit**. If
> `confirmed.md` lists any of the decision lenses — build / buy / delete / do-nothing,
> opportunity cost, strategic / roadmap fit, road not taken — run them. (The main session
> selects them when the change is load-bearing: heavy tier, or it sets a pattern others
> copy, or the user asked for the principal/director hat.) All four are teaching output,
> never blocking, and carry no `file:line`.
>
> Judge whether the ticket's stated need and the MR's stated change are the same thing.
> Name what the ticket asked for, what the MR says it does, and where those diverge. Cite
> ticket keys and `mr-view.md` quotes as evidence in place of `file:line`.
>
> Write your report to `<pack-root>/wave1/spec-reader.md` using the Return contract, with
> finding IDs prefixed `SPEC-`. Return one line: how many findings and their severities.

### 2. Diff reader — `wave1/diff-reader.md`

> You are reviewing the code itself. Read `<pack>/diff.patch`,
> `<pack>/changed-files.txt`, `<pack>/context.md`, and the repo as needed for surrounding
> code.
>
> Run these lenses from `lenses.md`, filtered to the set in `<pack>/confirmed.md`:
> **correctness**, **domain invariants**, **security**, **data integrity / idempotency**,
> **test honesty**, **design / architecture fit**, **interface / API contract quality**,
> **migration & rollback safety**, **performance / operational safety**, and
> **compliance / regulatory**.
>
> Compliance is yours rather than the link walker's because its trigger — *touches PII
> columns* — is a diff-visible signal. On **interface / API contract quality** judge the
> signature itself: is this a good surface for future callers? Whether the *docs* still
> match it is the link walker's half; do not duplicate it.
>
> Scrutiny depth is set by the tier in `<pack>/confirmed.md`. At **heavy**, deliberately construct
> failure scenarios and read migration and contract diffs twice.
>
> Write your report to `<pack-root>/wave1/diff-reader.md` using the Return contract, with
> finding IDs prefixed `DIFF-`. Return one line: how many findings and their severities.

### 3. Second question — `wave1/second-question.md`

> You are reading the same code as another reviewer, but you are asking a different
> question. They ask *is it correct*. You ask **will it age well**. Read
> `<pack>/diff.patch`, `<pack>/changed-files.txt`, `<pack>/context.md`, and the repo.
>
> You have not been told what the other reviewer found, and you should not try to guess.
> Findings you both reach are merged later; that duplication is expected and cheap.
>
> Run these lenses from `lenses.md`, filtered to the set in `<pack>/confirmed.md`:
> **over-engineering**, **under-engineering**, **tech debt**, **codebase-grain fit**,
> **precedent-setting**, **coupling / new failure modes / new deps**, **Chesterton's
> Fence**, **observability / operability**, **total cost of ownership**, **bus factor**,
> and **readability**.
>
> Two of these are high-yield and routinely skipped. **Chesterton's Fence:** for every
> deletion in the diff, find why the deleted thing existed before judging its removal
> safe. **Observability:** a renamed or removed log string can silently disable a
> log-based monitor — check for that specifically.
>
> Write your report to `<pack-root>/wave1/second-question.md` using the Return contract,
> with finding IDs prefixed `SQ-`. Return one line: how many findings and their severities.

### 4. Link walker — `wave1/link-walker.md`

> You are the reviewer who **leaves the diff**. Historically this role produces the single
> best finding of a review, because it sees what no diff-reader can.
>
> You need `glab` and the Jira MCP to follow links out of the pack. If either is
> unavailable, report which links you could not reach instead of staying silent about them.
>
> Start from `<pack>/mr-view.md`, `<pack>/context.md`, and `<pack>/discussions.json`.
> Follow every outward link and check each one:
>
> 1. **Linked MRs** in other repos — is each still open, merged, or closed? Does its
>    description depend on an MR that has since been closed or rescoped? A cross-repo
>    dependency chain with a dead link in it is a blocking finding.
> 2. **Jira siblings** — other subtasks under the same epic. Does this MR contradict or
>    duplicate one? Does it claim to complete something a sibling owns?
> 3. **Docs drift** — OpenAPI specs, Javadoc, README, in-repo design docs. Does prose
>    still describe the *old* behavior? Compare against `<pack>/diff.patch` and
>    `<pack>/changed-files.txt`.
> 4. **Discussion drift** — does any human or bot summary in `discussions.json` claim
>    something the diff does not do?
>
> Run these lenses from `lenses.md`, filtered to the set in `<pack>/confirmed.md`:
> **MR as communication**, **delivery-flow health**, and **scope discipline / reviewability**.
> Report docs drift under **interface / API contract quality**, and say in the finding that
> it is the documentation half of that lens.
>
> You may open the diff to confirm drift, but your findings must be ones a diff-only
> reviewer could not reach. A finding whose whole evidence is inside `diff.patch` belongs
> to another reviewer, not you.
>
> Write your report to `<pack-root>/wave1/link-walker.md` using the Return contract, with
> finding IDs prefixed `LINK-`. Return one line: how many findings and their severities.

## Wave 2 briefs

**Depth 7 only.** Dispatch both **in a single message** after wave 1 completes. Both
get the pack and all four wave-1 reports.

The two roles are asymmetric on purpose. The steel-man attacks **findings**; the straw-man
attacks **the code**. A pair that both attacked the code would leave false positives
alive — and killing a false positive is half of why wave 2 exists.

### 5. Steel-man — `wave2/steel-man.md`

> Your job is to **defend the code**. For each finding in `<pack-root>/wave1/*.md`, argue
> as strongly as the evidence allows that the code is actually fine — the reviewer
> misread a branch, the case is unreachable, a guard upstream already handles it, the test
> does assert the right thing.
>
> This role is the false-positive killer. A review that never dismisses anything is not
> being careful; it is being agreeable.
>
> You may **not** raise new findings. If you notice something new, say so in one line
> under "Noted, out of scope" and move on.
>
> For every finding write a verdict: **stands** / **weakened** / **falls**, with
> `file:line` evidence for the verdict itself. "Falls" requires positive evidence the code
> is correct — not merely the absence of proof that it is wrong.
>
> Write your report to `<pack-root>/wave2/steel-man.md`. Use the Findings section shape of
> the Return contract, one entry per wave-1 finding ID you assessed, and skip the Lens
> verdicts table — you own no lenses. Return one line: how many stand, weaken, fall.

### 6. Straw-man — `wave2/straw-man.md`

> Assume all four wave-1 reviewers were too polite and too narrow. **What did every one of
> them miss?** Read the pack and all four wave-1 reports.
>
> You may **not** restate an existing finding. Your value is only in what is not already
> on the list. Places the four are structurally weakest:
>
> - Seams **between** reviewers — the code is fine and the ticket is fine, but together
>   they mean something nobody checked.
> - Things true of the change as a whole rather than of any one line.
> - The hostile caller. Only **security** is adversarial by design; on a non-security MR
>   nobody is thinking about an attacker.
> - What happens on the **second** run — retry, replay, redeploy, rollback.
>
> Same evidence bar as everyone else: `file:line` plus a concrete failure scenario, or
> drop it. Do not pad.
>
> Write your report to `<pack-root>/wave2/straw-man.md` using the Return contract, with
> finding IDs prefixed `STRAW-`, and skip the Lens verdicts table — you own no lenses.
> Return one line: how many findings and their severities.

## Wave 3 brief

### 7. Judge — `wave3/judge.md`

Runs on **opus**. Runs at depth 5 and depth 7. It has **not** seen the user's
conversation, the teach-back, or the Checkpoint 1 dialogue. That coldness is the point: it
cannot be anchored by anything said earlier in the session. Do not paste conversation
history into its prompt.

> The Return contract's binding rules apply to you too: `file:line` or drop it; cite PII by
> location, never quote a PII value; read-only — do not edit any file but your report, and
> never run `glab mr note`, `glab mr approve`, or any write command; no delegation to other
> skills or agents.
>
> You are judging a merge-request review. Read the evidence pack at `<pack-root>/pack/`,
> the four reports in `<pack-root>/wave1/`, and — if present — the two in
> `<pack-root>/wave2/`.
>
> **Rule on every finding** from wave 1 and the straw-man. Verify each against the actual
> diff and repo; do not take a reviewer's word for it. For each, return:
>
> - **confirmed** — real, with the evidence you verified.
> - **downgraded** — real but less severe than claimed; say the new severity and why.
> - **dismissed** — not a real problem; say what disproves it.
>
> Where the steel-man says a finding **falls**, check its evidence yourself before
> dismissing. The steel-man is an advocate, not an authority.
>
> **Merge duplicates.** Two reviewers reaching the same problem from different evidence is
> a *strengthened* finding, not two findings. Keep every contributing ID in the merged
> entry.
>
> **Merge the lens verdicts.** Collect the verdict tables from all four wave-1 reports into
> one table covering every lens that ran. Where two reviewers verdict the same lens, take
> the worse verdict and keep both reasons. Do not drop ✅ rows — a clean lens must still
> appear, with its reason, or the pass cannot be shown to be a real pass.
>
> Then reconcile the merged table against your own Rulings. A lens whose only ⚠️/❌
> findings were all dismissed becomes ✅, with your reason. A downgraded finding moves its
> lens ❌→⚠️. A confirmed finding with no lens row — a straw-man finding, for instance —
> sets that lens's row to match its severity. Your **Confirmed findings** section and your
> **Merged lens verdicts** table must not contradict each other: a reader must not be able
> to find a blocking finding on a lens you marked ✅, or a ❌ lens with no surviving finding
> behind it.
>
> Write your report to `<pack-root>/wave3/judge.md` with three sections:
>
> 1. **Rulings** — a table: `ID | claim | ruling | reason`. Every input ID appears,
>    including dismissed ones.
> 2. **Confirmed findings** — the surviving set, deduplicated, severity-ranked, each with
>    `file:line` and its failure scenario.
> 3. **Merged lens verdicts** — the combined table, every lens that ran, ✅ rows included.
>
> Return one line: confirmed / downgraded / dismissed counts.

## Merging

After the judge returns, the main session reads `wave3/judge.md` and continues with
`SKILL.md` phase 6. Three things stay in the main session and are never delegated:

- **The autonomy filter** (phase 7) and its visible kept/dropped ledger.
- **The verdict scorecard**, assembled from the judge's merged lens verdicts.
- **The plain-prose rewrite.** Agents return dense, formal writing. It is a rough draft for
  the main session, never final copy for the user.

The **knowledge sharing / mentorship** lens also stays here. It judges the review's output,
not the change, so no agent can run it.

The main session mentions any steel-man "Noted, out of scope" notes at Checkpoint 2 — they
are written to disk and otherwise read by nobody.

## Degradation

- **An agent fails or returns nothing** → the main session runs that reviewer's lenses
  itself and **says so out loud**. A lens set never silently disappears from the
  scorecard.
- **An agent returns findings but no Lens verdicts table** → re-run that agent once. If it
  fails again, fill the verdicts inline in the main session and note it.
- **The judge fails** → the main session judges, and states plainly that the cold-judge
  independence was lost on this run.
- **Wave 2 is skipped** (depth 5, or a wave-2 failure at depth 7) → the judge still runs.
  Say in phase 6 that no steel-man challenged the findings, so false positives are likelier
  this run.
- **The Agent tool is unavailable** → fall back to inline grading at the real tier's depth
  of scrutiny, not light-tier scrutiny, and tell the user the review was single-pass.
