# Lens Catalog

A **lens (modality)** is one honest question you ask the MR that the other lenses are
blind to. A good set is one where no two lenses collapse into each other.

**0 leads; derive-and-tune per PR — never apply blindly.** Acceptance criteria only matter
if we're solving the right problem. The skill auto-selects a subset (see Triage); the user
confirms/edits it at Checkpoint 1.

Each finding lens below is written as: **Name** — *Question* · catches (that others miss) ·
**fires when**.

## The two controls (NOT findings — they change how the finding lenses are used)

- **Reversibility / blast radius** — a scrutiny *dial*. One-way door (migration, public
  contract, backfill) → push every other lens harder. Two-way door → go light. Sets the
  tier (see Tier rule). Never itself a `file:line` finding.
- **Author autonomy** — a finding *filter*. Before drafting, drop findings that are mere
  preference among equally valid approaches; keep only what "definitely improves code
  health." The counterweight to over-blocking. Applied in SKILL.md phase 7.

## Altitude 1 — should this exist? (the decision)

- **Problem-fit** — *Are we solving the real problem, or the ticket's literal words?* ·
  catches correct code that ships the wrong thing · **fires: always-core.**
- **Build / buy / delete / do-nothing** — *Should any code exist for this?* · catches
  work whose cheapest form is not writing it · **fires: load-bearing changes only (heavy
  tier or user asks).**
- **Opportunity cost** — *Is this the best use of two engineers this week?* · catches the
  flawless MR that should never have been built · **fires: load-bearing only.**
- **Strategic / roadmap fit** — *Serves where we're going, or a clever detour?* · catches
  hardening a soon-deprecated component · **fires: load-bearing only.**
- **Road not taken** — *Was there a simpler/more correct path, judged against the author's
  REAL constraints?* · catches an unreasoned tradeoff (not reviewer taste) · **fires:
  load-bearing only; teaching output, never blocking, no `file:line`.**

## Altitude 2 — is it built right? (the execution)

- **Spec / acceptance fit** — *Does it do what was actually asked?* · the only lens judging
  against external intent · **fires: always-core.**
- **Correctness** — *Right result on every input — null, edge, error, concurrent?* · the
  unhandled null / swallowed exception / race · **fires: always-core.**
- **Domain invariants** — *Does it uphold the repo's business rules the type system can't
  express?* · locally-valid-but-globally-illegal writes (NULL tenant, NOT NULL surrogate) ·
  **fires: touches a known-invariant area (CLAUDE.md/memory) or PII columns.**
- **Security** — *What can a hostile caller do — input, authz, secrets, injection?* · the
  only adversarial lens · **fires: auth/secrets/input-parsing/PII touched.**
- **Data integrity / idempotency** — *On retry or replay, does it stay consistent?* · the
  double-write / non-idempotent job · **fires: migration, batch/ingestion, backfill,
  at-least-once path.**
- **Test honesty** — *Will the tests actually fail when the code breaks?* · coverage
  theater (asserts nothing, mocks the subject, tests the DTO not the DB) · **fires:
  always-core.**
- **Design / architecture fit** — *Does this logic even belong here?* · a change that
  passes every other lens but sits in the wrong place · **fires: new class/service/module
  or a new abstraction.**
- **Interface / API contract quality** — *Is the new public surface itself good?* · a
  clumsy signature future callers inherit · **fires: new/changed public API, client
  schema, endpoint.**
- **Migration & rollback safety** — *Can it roll out AND roll back; do old+new coexist
  mid-deploy?* · the un-revertable migration, the expand-without-contract · **fires:
  migration / Liquibase / schema change.**
- **Performance / operational safety** — *At prod scale + concurrency, any N+1, unbounded
  query, lock, or heap surprise?* · behavior under load, not on the unit test's small
  input · **fires: batch/scale/query/lock change, large tables, big IN-lists.**

## Altitude 3 — will it age well? (the future & the system)

- **Over-engineering** — *Built for a future that may never come?* · speculative
  generality nobody needs · **fires: new abstraction / generic framework.**
- **Under-engineering** — *Too thin for cases that exist today?* · the missing edge/branch
  the current inputs already hit · **fires: new abstraction / non-trivial logic.**
- **Tech debt** — *A knowing shortcut — acknowledged, or silent and reckless?* · debt taken
  without a paper trail · **fires: any shortcut, TODO, or "temporary" path in the diff.**
- **Codebase-grain fit** — *Goes with the grain of the code, or fights it?* · a second
  bespoke pattern beside an established one · **fires: new abstraction, or diverges from a
  documented convention.**
- **Precedent-setting** — *Do we want the next person to copy this?* · fine once, toxic
  replicated · **fires: introduces a pattern others will copy (heavy/load-bearing).**
- **Coupling / new failure modes / new deps** — *What does this newly bind us to, and how
  can it now break?* · a new network hop, shared singleton, deploy-ordering assumption ·
  **fires: adds a dependency, singleton, shared state, or cross-service call.**
- **Chesterton's Fence** — *Do we understand why the thing we're deleting was there?* · a
  "cleanup" that removes a load-bearing guard · **fires: deletes code, a check, or a
  defensive branch.**
- **Observability / operability** — *Once live, can we see it work — and see it fail?* ·
  silent failure, unmonitored WARN, a renamed log string that disables a log-based
  monitor · **fires: new job/path/metric/log, or removes/renames a log line.**
- **Total cost of ownership** — *Who carries this for years?* · cheap to write, expensive
  to keep · **fires: new subsystem, new dependency, bespoke tooling.**
- **Bus factor** — *Does approving this deepen a single point of failure?* · a correct MR
  only its author understands · **fires: complex/novel area, single-author domain.**
- **Readability** — *Can the next reader grok it fast?* covers simplicity (YAGNI), naming,
  comments (why not what), consistency · **fires: always-core.**

## Cross-cutting (meta)

- **MR as communication** — *Does the description carry the why? Small enough to review?
  Good paper trail?* · a diff with no recoverable rationale · **fires: always-core.**
- **Delivery-flow health** — *Does this help or clog throughput / review queue / WIP?* ·
  the 2,000-line PR that stalls the pipeline · **fires: big diff / many files.**
- **Knowledge sharing / mentorship** — *Does the review grow the team, or only gate it?* ·
  a missed teaching moment · **fires: user asks, or a teachable pattern appears.**
- **Compliance / regulatory** — *PII, licensing, audit obligations no line of the diff
  shows?* · address/recipient-name exposure, an incompatible licence · **fires: touches
  PII columns, adds a dependency with a licence, or an audited path.**
- **Scope discipline / reviewability** — *One clean change, or a grab-bag — revertable as a
  unit?* · a mix of concerns that can't be reviewed or reverted cleanly · **fires: big diff
  / many files, or several concerns in one MR.**

## Always-core (every MR, no trigger)

problem-fit · spec/acceptance fit · correctness · test honesty · readability ·
MR-as-communication.

## Triage table (signal in the diff → lenses woken; contribution to the tier)

| Signal | Lenses woken | Tier push |
|---|---|---|
| Migration / Liquibase / schema change | migration & rollback · data integrity · reversibility | heavy |
| New/changed public API, client schema, endpoint | interface contract · migration & rollback · reversibility | heavy |
| Touches PII columns (address, recipient name) | compliance · domain invariants · security | heavy |
| Backfill / first-run / one-time job | operability · ops safety · reversibility | heavy |
| New singleton / shared state / multi-instance | coupling · ops safety · correctness (concurrency) | heavy |
| Security-sensitive (auth, secrets, input parsing) | security · data integrity | heavy |
| New abstraction / generic framework | over-eng · under-eng · precedent · codebase-grain fit · design fit | normal |
| Deletes code / removes a guard | Chesterton's Fence | normal |
| Adds a dependency | coupling/failure modes · TCO · compliance | normal |
| Batch / scale / query / lock change | performance/ops · operability | normal |
| Big diff / many files | scope discipline · delivery-flow health | (flags reviewability) |

**Decision lenses** (build/buy/delete · opportunity cost · strategic fit · road-not-taken)
have no clean code signal. Fire them **only** when the change is load-bearing (heavy tier,
or sets a pattern others copy) or the user asks for the principal/director hat. Always
teaching output — never blocking on their own.

## Tier rule

`light` by default → `normal` if any normal trigger fires → `heavy` if any heavy trigger
fires. The user may override at Checkpoint 1.

## Non-collapse seams (keep these distinct)

- over- vs under- vs debt = built-for-nobody / too-thin-for-today / right-sized-but-shortcut.
- codebase-grain fit vs Chesterton's Fence = adding *with* the grain vs not *removing*
  load-bearing structure.
- tech debt vs TCO = a chosen repayable shortcut vs the unavoidable lifetime carry of even
  clean code.
- precedent-setting vs codebase-grain fit = forward-looking (who copies next) vs present
  (matches what's here).
- reversibility vs operability = undo-ability vs detectability.
- design/architecture fit vs codebase-grain fit = does it belong *here* (placement) vs does
  it match how we build (pattern reuse).
