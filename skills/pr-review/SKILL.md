---
name: pr-review
description: Review a GitLab merge request end-to-end — triage its blast radius, load the diff and linked Jira context, teach back the real intent, auto-select review lenses from a ~30-lens catalog (you confirm), grade against them with file:line evidence at a scrutiny tier, run an adversarial challenge round, filter findings for author-autonomy, draft kind, postable comments, and — on a pass, only after you confirm — post a per-lens "why it passed" summary to the MR. Use when the user shares a GitLab MR URL or asks to review an MR, PR, or merge request.
---

# PR Review

Turn a GitLab merge request into a structured, evidence-based review. Two goals:
the reviewer *understands* the change's real intent, and the MR ends up solid and
understandable. Human stays in the loop; this reaches the useful dialogue faster.

## Prerequisites

- `glab` (GitLab CLI) — authenticated.
- Atlassian Jira MCP — for the ticket chain. Degrade gracefully if absent.
- The Claude Code memory dir — for repo recall/persist.

## Session model + effort

The main session does the judgment work at every tier: triage, teach-back, lens choice,
the final filter, and the comments the author reads. At light tier it also does all the
grading, since no agents run. So it needs a strong model at every tier. Wave agents
already have their models pinned in phase 5, and this section does not change them.

| Tier | Recommend | Why |
|---|---|---|
| Light | Opus high | Grades every lens inline. Do not drop to medium. |
| Normal | Opus high | Runs the wave and writes the final comments. |
| Heavy | Opus high | Same work, more of it. |
| Heavy + money math or prod data | Opus max | Correctness beats cost. |

The skill cannot switch the session's model. It only recommends one:
- **At the start**, if the session is below Opus high (e.g. Sonnet, or Opus medium), say
  so in one line before phase 1: "Reviews want Opus high. This session is on <X>. Switch
  in the model picker, or I'll carry on." Then carry on. Do not stop the review over it.
- **At Checkpoint 1**, once the tier is set, name the combo for it from the table. Flag
  it only when it differs from what the session is on.

## How to run

Eight phases. Three **hard checkpoints (🛑)** — stop and wait for the user. Track phases
as a todo list. Lens selection and scrutiny come from `references/lenses.md`; how the
lenses are run across agents comes from `references/waves.md`.

### 1. Load the artifact
- `glab mr view <id> --repo <path>` and `glab mr diff <id> --repo <path>`.
- Fetch discussions: `glab api "projects/<enc>/merge_requests/<id>/discussions"`.
- Establish the **real files changed** from the diff. This is the source of truth.
- **Build the evidence pack once** — write `mr-view.md`, `diff.patch`, `discussions.json`,
  and `changed-files.txt` to `<scratchpad>/pr-review-<id>/pack/` (layout in
  `references/waves.md` → **Evidence pack**). No later phase re-fetches the MR; a push
  landing mid-review must not give different agents different diffs. Report the pack path.
  The pack lives in the session scratchpad and holds the raw diff, which may contain PII —
  it is never persisted to memory. It lives only for this session's scratchpad and is
  not carried between sessions — a new session starts a new pack.

### 2. Load context
- Walk the ticket chain via the Jira MCP: subtask → task → epic → dependency.
- Read the repo `CLAUDE.md`. Recall memory facts tagged to this repo (re-verify each
  against the current diff before relying on it).
- Write the ticket chain, the `CLAUDE.md` notes, and the recalled memory facts to
  `<pack>/context.md`. This is the only **session** context wave agents get — no
  conversation history; the link walker still leaves the pack and follows outward links as
  part of its job.

### 3. Triage & set scrutiny
- Read the MR's **shape** from the diff: size/file count, what it touches, one-way vs
  two-way door.
- Apply `references/lenses.md` → **Triage table** + **Always-core** to build a **candidate
  lens set**, and the **Tier rule** to set a **scrutiny tier** (light / normal / heavy).
- The tier also sets **wave depth** — `references/waves.md` → **Wave depth**. Light = 0
  agents (grade inline). Normal = wave 1 + judge (5). Heavy = wave 1 + wave 2 + judge (7).
- Pull in the **decision lenses** only if the change is load-bearing (heavy, or sets a
  pattern others copy) or the user asked for the principal/director hat.

### 4. Teach it back (ELI5) + propose lenses
- Explain what the change is *for* in plain terms.
- Voice the step-back (problem-fit): "the ticket says X; what we're **really** doing is Y."
- Present the lens set in **two clearly separated groups — always name both**:
  1. **The 6 always-core lenses** (problem-fit · spec/acceptance fit · correctness ·
     test honesty · readability · MR-as-communication). State explicitly that these run on
     **every** MR. Never present only the triggered lenses — the always-core block is
     shown in full every time, even when triggered lenses dominate.
  2. **The triggered lenses** this MR's shape woke, each with the signal that woke it
     (e.g. "migration & rollback — because there's a Liquibase change").
- Then the **tier + why**: "at *heavy* scrutiny, because it's a migration."
- Then the **wave depth** the tier implies, stated plainly: "that's *heavy*, so I'd run
  seven agents — four blind reviewers, a steel-man and straw-man, then a cold judge."
- Then the **session combo** for that tier, from **Session model + effort** above. Name it
  only if it differs from the current session: "heavy and it touches money totals, so
  Opus max is the better fit — this session is on Opus high."
- 🛑 **Checkpoint 1:** "Here's my understanding + the 6 always-core lenses (always on) +
  the triggered lenses, tier, and wave depth I'd grade against — correct/add/drop anything
  (including a one-off lens for this MR), bump the tier, or change the wave depth?"
  Silence = the proposed set runs.
  Wave depth is a closed set — 0, 5, or 7. A request for anything else ("run six",
  "skip the judge") is confirmed back to the nearest of the three (ties round up), and the
  user is told which one that is.
- **On confirmation**, write the agreed lens set, tier, and wave depth to
  `<pack>/confirmed.md`. Every wave agent reads it; an agent's lens list is the
  intersection of its brief and this file. Any lens in `confirmed.md` that no brief claims
  goes to the reviewer whose evidence it needs — the main session decides and names it in
  that agent's dispatch — except knowledge sharing / mentorship, which always stays in the
  main session. If no reviewer can see the evidence that lens needs, the main
  session runs it inline and says so.

### 5. Grade in waves (depth scaled by the confirmed wave depth)
- **Self-contained identity — no delegation to other review skills** (`code-review`,
  `adversarial`). The lens reasoning is always this skill's own. It may run
  that reasoning across its own wave agents — see `references/waves.md`.
- Branch on the **wave depth recorded in `<pack>/confirmed.md`**, not on the tier directly.
  The tier only supplies that depth's default (light → 0, normal → 5, heavy → 7); the user
  may have overridden the depth at Checkpoint 1 independently of the tier, and the override
  is what runs.
- **Depth 0 (usually light): no agents.** Grade every selected lens inline, as one careful
  read. Skip to phase 6.
- **5a — Wave 1 (Depth 5 and Depth 7, usually normal and heavy).** Dispatch the four
  reviewers from `references/waves.md` → **Wave 1 briefs** in **one message** so they run
  concurrently and none sees another's output. Model `sonnet`. Each writes its report to
  `<pack-root>/wave1/` and returns one line.
- **5b — Wave 2 (Depth 7 only, usually heavy).** Dispatch the steel-man and straw-man in
  **one message**. Model `sonnet`. Reports to `<pack-root>/wave2/`.
- **5c — Wave 3 (Depth 5 and Depth 7, usually normal and heavy).** Dispatch the judge.
  Model `opus`. It gets the pack and the wave reports (wave 2's, if they exist) **and
  nothing from this conversation** — its independence is the point. Report to
  `<pack-root>/wave3/judge.md`.
- Read the reports **from disk**, not from agent return values. That is what keeps this
  window small.
- Every verdict cites `file:line`. **Reconcile every human/bot summary claim against the
  actual diff** (summaries can be stale/wrong) — the link walker does this, but check it.
- Tier controls how hard each agent looks (see **Scrutiny tiers** below).
- At **heavy** tier only, offer: "Check out the branch and run build/tests/coverage to
  verify the claims?" This stays in the main session — it is evidence-gathering, not lens
  work. If the branch won't build (e.g. needs a dependency MR), skip and note it.

### 6. Challenge round
- **If a judge ran** (depth 5 or 7): present the judge's **Confirmed findings**
  steel-manned (best case for the current code first), severity-ranked, split **blocking
  vs nice-to-know**. Then **show what died** — summarize the judge's **Rulings** table:
  how many findings were downgraded or dismissed, and name each dismissed one in a line
  with the reason. A dismissed finding is *visible*, not silently absent — that is how the
  user audits the machine, and how a wrong dismissal gets caught. (If the judge failed and
  you judged in the main session, use this branch and say the cold-judge independence was
  lost.)
- **If the review ran inline** (depth 0, or the Agent tool was unavailable): present
  your own findings steel-manned, same ranking and same split. Name anything you
  considered and rejected, for the same audit reason, and say plainly that this was one
  reader in one pass.
- If **wave 2 did not run** (depth 5, or a wave-2 failure at depth 7), say so: no steel-man
  challenged these findings, so a false positive is likelier this run.
- 🛑 **Checkpoint 2:** "Poke holes before I finalize." Concede or defend with evidence.
  Reviving a dismissed finding here is normal and expected. Also surface any steel-man
  "Noted, out of scope" notes so the user sees what it flagged in passing but didn't rule on.

### 7. Autonomy filter → distill & draft
- **Autonomy filter first:** pour every surviving finding through "real code-health issue
  vs my preference among equally valid approaches?" Keep only what *definitely improves
  code health*; drop or demote the rest to a one-line non-blocking aside. Emit a visible
  ledger: "Kept N. Dropped M as preference-only: …".
- **Re-apply the judge's lens-reconciliation rule** (`references/waves.md` → **Wave 3
  brief**) to the lens-verdict table now that Checkpoint 2 (a revived finding) and
  the autonomy filter (a dropped or demoted finding) may have changed the finding set: a
  lens with no surviving ⚠️/❌ finding becomes ✅; a revived or demoted finding sets its
  lens row to its current severity. Do this before the scorecard is presented.
- **Present the verdict scorecard** (see below) covering **every lens that ran** — the 6
  always-core plus the chosen ones.
- Surviving findings → comments using `references/comment-style.md`. Draft only — never post.
- Persist reusable repo learnings to memory (see below).

### 8. Post the pass summary (explicit confirm only)
- **Runs only when the MR passes** — no surviving **❌ blocking** finding. (⚠️ caveats are
  fine; a pass-with-notes is still a pass — call the notes out as non-blocking.)
- Compose a **pass-summary comment** for the MR: a per-lens rundown of what was graded and
  **why it passed**, in the kind tone of `references/comment-style.md`. It mirrors the
  verdict scorecard but reads as a message to the author. **Keep all PII out** — no
  destination street address or recipient name (postal code, city, region/state, country,
  PO-box flag are fine).
- 🛑 **Checkpoint 3:** Show the **exact comment text**, then ask: "Post this to MR !<id> as a general
  comment? I won't post without your yes."
- **On an explicit yes:** `glab mr note create <id> -m "<text>" --repo <path>`. Report the
  note URL so it's confirmed posted.
- **On no / silence:** leave it as a draft and stop. Never auto-post.
- **If the MR did NOT pass** (any surviving ❌ blocking finding): skip this step. Say the
  pass-summary is withheld because N blocking issue(s) remain; the drafted findings stand.

## Scrutiny tiers

The tier scales **how hard you look**, not how many lenses run.

- **Light** (screen door: small, local, two-way): one read-through; flag only clear
  problems; no branch checkout.
- **Normal:** read every line; reconcile every summary claim; reason edge cases.
- **Heavy** (vault door: one-way): all of normal + deliberately construct failure
  scenarios + read migration/contract diffs twice + pull in the decision lenses + offer
  the branch checkout & test/coverage run.

## Autonomy filter

Author autonomy is a **filter, not a finding**. Bar (Google's standard): keep a finding
only if it *definitely improves code health, even if not perfect*. Preference among
equally valid approaches → drop, or demote to a one-line non-blocking teaching aside —
never worded as a request. Always emit the kept/dropped ledger so it's honest and
reversible.

## Verdict scorecard

The closing artifact of every review (phase 7), covering **every lens that ran** — the 6
always-core lenses **plus** every chosen/triggered lens. Two parts, in this order:

**1. Detail — a short paragraph per lens-section** (group by altitude: Decision /
Execution / Future / Meta; skip a group with no lenses that ran). Each paragraph says what
this section's lenses found, in plain terms, with `file:line` where it matters.

**2. The at-a-glance table** — one row per lens:

| Lens | | Verdict |
|---|---|---|
| Correctness | ✅ | Handles null + empty; no concurrent path touched. |
| Migration & rollback | ⚠️ | Forward migration fine; no down-migration — see `db/….xml:12`. |
| Domain invariants | ❌ | Writes `tenant_id=''` not NULL — breaks partner-level match (`Repo.java:88`). |

Legend: **✅ clean · ⚠️ non-blocking finding / caveat · ❌ blocking problem.** Every ⚠️/❌
row's one-liner names the concrete issue (and `file:line` when it has one); a ✅ row says in
a few words *why* it's clean, so the pass is legible, not just a wall of green. Always-core
lenses appear even when ✅ — that is how the reader sees they were actually judged.

## Hard rules
1. Diff is source of truth — verify every summary claim against it.
2. Every finding cites `file:line` + a concrete failure scenario, or drop it.
3. Steel-man before flagging; keep only findings that survive.
4. Never post without your explicit per-MR yes. Findings comments are **draft-only**; only
   the pass-summary (phase 8) may be posted, only on a pass, and only after you confirm.
5. Separate blocking from teaching explicitly.
6. Run the autonomy filter before drafting any comment.
7. Anything posted to the MR carries **no PII** (no destination street address or recipient
   name; postal code, city, region/state, country, PO-box flag are fine).
8. Every wave agent returns `file:line` evidence **and** a per-lens verdict. An agent that
   returns findings without verdicts has not finished its job — re-run it once; only if it
   fails again, cover that lens set inline and say so. The scorecard must show every lens
   that ran.

## Memory
- **Recall** (Phase 2): load repo-tagged facts; re-verify against the current diff before
  relying on them.
- **Persist** (Phase 7): save durable repo conventions/gotchas as `reference`-type
  memories (one fact per file + MEMORY.md pointer). Never PII, never per-MR trivia.

## Graceful degradation
- No Jira MCP auth → review with diff + CLAUDE.md only; say so.
- Branch won't build → skip the run step; fall back to static reasoning; note it.
- Bad/unreachable MR URL → stop early with a clear message; don't guess.
- **Huge diff** (won't fit / too many files) → don't choke: flag reviewability as a
  finding, then grade the highest-tier files first and say what you sampled.
- **Posting fails** (glab auth / no permission / network) → report the error, keep the
  pass-summary as a draft, don't retry blindly.
- **A wave agent fails or returns nothing** → run that reviewer's lenses inline and **say
  so**. A lens set never silently disappears from the scorecard.
- **The judge fails** → judge in the main session, and say plainly that the cold-judge
  independence was lost on this run.
- **The Agent tool is unavailable** → fall back to inline grading at the real tier, and
  tell the user the review was single-pass. Full list in `references/waves.md` →
  **Degradation**.
