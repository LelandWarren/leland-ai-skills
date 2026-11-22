# Lenses

The questions reviewers ask. `SKILL.md` says who runs which lens and when.

**Source tags** in the "From" notes: **F** = published frameworks (ATAM, AWS Well-Architected,
C4/arc42, design-doc practice, ADRs, Bezos doors) · **T** = existing review tools · **H** = a
class of real past failure. The H notes are examples to calibrate against, not a checklist.

## What counts as architecture

Two tests. A finding has to pass at least one.

1. **Rewrite test.** Say a good engineer rewrote every line but kept the same boxes and arrows.
   The finding is architectural if it would still be true. (T)
2. **Map test.** The finding is architectural if the fix changes something on the neighborhood
   map: a component, an edge, a data owner, a contract, a runtime property (failure, capacity,
   security, cost), or a rollout step. It is also architectural if the change is hard to undo
   (a one-way door). (F: SEI "externally visible properties", Fowler "hard to change", Nygard
   and arc42 significance lists. T: pr-review map-shaped fixes.)

**Tie-breaker:** "Would another team, another service, or on-call notice if this were done
differently?" (F)

**Rules that follow from the tests:**
- Evidence may cite `file:line`. The claim has to be about components and flows.
- Mixed lenses run only their system-level half.
- Line-level notes go in one "out of scope, run /pr-review" line with no verdict.

## Core lenses (always on)

### C1. System fit
- **Question:** Does this sit in the right service? Does it fit the neighbors that already
  exist? Does the capability already exist somewhere else?
- **Evidence:** the map (who calls whom, who owns what), the service's stated purpose, sibling
  implementations across repos.
- **From:** F System Fit, Conceptual Integrity · T Responsibility placement, Build/reuse/skip ·
  H parallel implementations drift.

### C2. Blast radius and failure unit
- **Question:** When this fails, what fails with it? What is the unit of failure (field, line,
  file, record, tenant run, batch run)? Is that the intended unit?
- **Evidence:** callers and callees on the map, shared resources, exception classes against the
  catch sites, retry policy against whether the failure is permanent or transient.
- **From:** F Blast Radius (AWS REL10 bulkheads) · T Failure domains · H error-handling
  granularity (one unchecked exception aborts the whole batch run).

### C3. Premises measured
- **Question:** Which data facts does the design assume (field is populated, coverage %,
  cardinality, join key, uniqueness)? Has each one been measured in prod for the target
  customer? Which key decisions are still unmade? **Tripwire:** what is the earliest signal that
  a premise broke later, and who sees it?
- **Evidence:** memory/CLAUDE.md facts first (free). A premise that needs a live count goes on
  the report's **Needs a number** list. Reviewers never query. The main session asks the user
  first (see the real-numbers step), and fetches counts and totals only, never rows.
- **From:** H, the largest history class. It is invisible in a diff (a feature built on a field
  prod never fills; two data sets assumed to join that barely overlap). F ATAM: unmade decisions and
  unexamined assumptions count as risks.

### C4. How fucked are we if we're wrong *(report label "Cost of being wrong")*
- **Question:** Six months from now we learn the design was wrong: an unknown unknown, a premise
  broke, or it needs a refactor. How bad is it to live with, and how bad is it to get out?
- **Sub-questions:**
  - **What piles up while we live with it?** Data stored in its shape, consumers built on its
    contract, copies, customer-visible outputs (issued bills, sent emails), code that copied the pattern.
  - **Does the exit cost stay flat or compound?** A flag you flip stays cheap. A table other
    services read gets more expensive every week.
  - **What does the exit look like?** Delete it, migrate off it, or run both side by side. Is
    deleting the whole thing even possible?
  - **Who else pays?** Other teams, finance, customers.
  - **Is there a cheap hedge today?** A seam, a new column instead of an overwrite, a flag, or
    keeping raw inputs so we can re-derive later.
- **Output:** exit cost at ~6 months (low / medium / high) + flat or compounding + the cheapest
  hedge and its cost.
- **Pairs with C2:** C2 asks how bad it is when the *code* breaks today. C4 asks how bad it is
  when the *design* turns out wrong later.
- **Absorbs:** the one-way / two-way door half of catalog #8. The door tag in `report.md` comes from here.
- **From:** F Bezos Type 1/Type 2 doors, Fowler "remove irreversibility", AWS "review
  early to avoid one-way doors" · H (history you can't redo: frozen records, `ON CONFLICT DO
  NOTHING`).

## Catalog (the map step picks)

Each lens: the question, and the signals that wake it.

| # | Lens | Question | Pick it when | From |
|---|---|---|---|---|
| 1 | **One path, one choke point** | Is the rule enforced where every caller passes? Does this add a second way to compute something? If it reuses a shared path, do all callers really need the same thing? | new optional params, a fix to one caller of a shared service, a new mapper/enricher/pricing path, a shared helper stretched to a new caller | H (a rule enforced in one caller but not another), T House-pattern fit |
| 2 | **Contracts and intermediaries** | Who consumes each changed contract? Can old and new coexist? What rewrites the contract in between (gateway, generated client, codegen types, EDI pipe)? | DTOs, `@Schema`, client jars, events, enums that cross services, file/CSV layouts, gateway routes | F Contract Compatibility · T Contracts · H (a gateway silently strips a new field; a client library never republished) |
| 3 | **Cross-service calls** | For each synchronous call: whose timeout fires first? What does a timeout look like to the user and to monitoring? Who owns the endpoint, and who else calls it? | new or changed calls to another service, retries, timeouts, workarounds for a slow upstream | F Dependency Failure Handling (AWS REL05) · H (an upstream timeout shorter than ours) |
| 4 | **Shared capacity and load shape** | Which shared resource does this load? Who else is on it, and when? How does it act at the largest partner and at peak? | queries on big tables, longer connection holds, new workers/schedulers, fan-out, in-memory sizing by input, per-pod concurrency | F Capacity (AWS "stop guessing capacity") · T Scale · H (a small shared DB writer with no statement timeout) |
| 5 | **Data ownership and identity** | Who is the source of truth? Is the store right for the access pattern? What identifies one row, and can two real things share that key? | new tables/columns, copies of data owned elsewhere, new unique keys, cross-source merges | F Data Ownership · T Data model durability · H (two real records sharing one key, so one was billed twice) |
| 6 | **Downstream consumers and history** | Who reads this after it's written (bills, exports, a ledger, the UI)? Is the value frozen or recomputed? If it's wrong, can we fix it, and from what? | writes to stored data others read, backfills, re-derive/re-stamp jobs, anything touching issued bills | H (frozen line-detail rows, an hourly export, `ON CONFLICT DO NOTHING` can't correct history) |
| 7 | **Replay and idempotency** | On retry, replay, redeploy, or reprocess, does the system end up in one correct state? | queue consumers, batch jobs, reprocess endpoints, schedulers, retryable mutations | F (AWS REL04) · T Replay · H gap (no incident yet, likely real) |
| 8 | **Rollout order** | In what order must migrations, regions, dependent MRs, clients, and flags reach prod? Is the mixed-version window safe both ways? Can deploy day be rolled back? (The long-term "one-way door" question lives in C4.) | migrations, enum changes, multi-repo work, flags, manual deploy gates | F Deploy & Rollback (AWS OPS06) · T Rollout, Cross-repo sequencing · H |
| 9 | **Detection** | If this goes wrong silently in prod, how do we find out, and how fast? Which monitor, ticket automation, or dashboard keys on what this emits or stops emitting? | new failure modes, swallowed errors, new async paths, changed log text, "wrong numbers" failures | F Observability · T Operability · H (monitors keyed on log text; an error metric that opens support tickets) |
| 10 | **Trust boundary and PII** | Does this widen who can reach data or actions? Is the rule enforced where the write lands, not in a layer that can be bypassed? Does PII move somewhere new? | new endpoints, authz/tenancy logic, exports, new sinks (logs, S3, lake), PII fields | F Security · T Trust boundaries · H (a sensitive write guarded by a too-broad role) |
| 11 | **Unknown-input policy** | When input is outside what the design handles (unit, currency, config field, vocabulary), does it fail loud, skip with a reason, or quietly default? | parsers, mappers, config readers, new enum values, unit conversion | H (an unexpected unit, an unexpected currency, unsupported config fields silently ignored) |
| 12 | **Real-infra guarantees** | Which guarantees come only from the real DB, index, planner, or upstream? Does verification touch the real thing or a mock? | NOT NULL/unique constraints, query-plan-dependent designs, "tests pass" as the safety argument | H (a P1 incident despite 100% test coverage) |
| 13 | **Abstraction earns its keep** | Is each new framework or seam deep, with a real second user? When the next likely change arrives, does it bend or break? | new frameworks, extension points, "general" machinery built for one case, hard-coded per-customer branches | T Seam depth, Over-engineering · F Evolution Path (ATAM growth scenarios) |
| 14 | **Tradeoff points** | Which qualities does this trade against each other? Is it the right trade? Who picks the dial? | caching, batching thresholds, async vs sync, pool sizes, a claimed quality benefit | F ATAM sensitivity/tradeoff points |
| 15 | **Problem fit and scope** | Does it solve the real problem, not just the ticket's words? Are the non-goals stated? Is it the best use of ~2 engineers? | design proposals (always), vague MRs, scope much bigger than the ticket | T Problem fit, Strategic fit · F Goals/Non-goals |
| 16 | **Second-order effects** | If this works perfectly, what breaks next? Where does the load or bottleneck move? What if it wildly succeeds: 10× use, or other teams copy it? | workarounds, caches, new upstream traffic, behavior that will be copied | T Second-order effects |
| 17 | **Ownership and lifetime cost** | Who carries this for years? Is that carry (people, infra, third-party spend, one-person knowledge) worth it? What does a new engineer inherit once the builders are gone? | new infra, new vendors, paid per-call APIs, subsystems only one person understands | T Ownership · F Cost & Efficiency |
| 18 | **Load-bearing removals** | For each thing the change removes or replaces, do we know why it existed? | deletes of components, flows, guards, monitors, or disabled processors | T Chesterton's Fence |
| 19 | **Bets on things we don't control** | What does this bet stays true that another team, vendor, or carrier owns (query bounds, what a gateway strips, a file layout, a rate limit)? What happens the day they change it, and would we notice? | reliance on upstream behavior that isn't a written contract, workarounds around another service, carrier/vendor formats, dedupe or ordering that depends on an upstream | Spark from C4 · H (a dedupe that rests on an upstream's inclusive query bounds) |

**Not a lens, a mechanism:** "Alternatives considered" (F Google/arc42/Nygard, T Road not taken)
is what the blind designers do (`designers.md`). So it is not in the catalog.
