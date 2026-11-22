# Ticket template (lean modular, draft v0.2)

Every ticket has one shared core. Each ticket type adds a small module. Optional pieces go in only when they help.

Draft for the team to review. The reasons behind each part are in the "Where each part comes from" table at the bottom.

---

## 1. Title

`<area>: <the result, in plain words>`

Examples: `web-ui: success green matches the brand palette`, `pricing-service: accept a WEEK rebate period`.

Name the result, not the code change.

---

## 2. The core (every ticket)

Always in this order, so readers know where to look.

```markdown
## Why
<Up to 5 sentences. What is wrong or missing, who feels it,
and what happens if we leave it.>

## Done when
- D1. <one result someone else can see> — check: <test | query | stage | review>
- D2. ...

## Not in scope
- <at least one line. If truly none, write "None known.">

## Links
- Parent: <epic key, or why there is none>
- Blocks / blocked by: <keys>
- Docs: <design doc, ADR, meeting notes>
```

### Rules for "Done when" lines

1. **One result per line.** If a line has "and", think about splitting it.
2. **Someone other than the author can check it, once this ticket is done.** If a line can only pass after other tickets ship, name them in the check: `check: stage, after PROJ-123`.
3. **No fuzzy words.** Avoid "intuitive", "clean", "neatly", "robust", "fast", "easy" and "properly". Use a number, or something a person can see.
4. **State the result, not the code steps.** Code notes go in Context. A call to another ticket's code counts as a result when making that call is this ticket's job. For example: "the screen sends `app: 'customer-portal'`".
5. **Every line names its check method.** There are four. They are NASA's four verification methods, renamed for software:

| Check | Means | NASA method |
|---|---|---|
| `test` | An automated test passes. Name the test or the case. | Test |
| `query` | A SQL query, log search or metric shows it. Put the query in the ticket or link to it. | Analysis |
| `stage` | Seen working on stage or in a demo. | Demonstration |
| `review` | Someone reads the code, config or doc and confirms it. | Inspection |

The IDs (D1, D2…) let the MR, the tests and the close-out point at one line.

---

## 3. Optional pieces (add only when they help)

Put them between **Why** and **Done when**.

```markdown
## Context
<What exists today. Where the code lives. Earlier tickets.>

## Behaviour
<How it should work, seen from outside, as numbered steps.
Not the implementation.>

## Open questions
- Q1. <question> — owner: <name>, needed by: <date or "before start">
```

A ticket is **not ready** while an open question says "needed by: before start", or Context says "to confirm before start".

One more optional piece goes last, after **Links**:

```markdown
## Change log
- <date>: <what changed, and why>. Source: <doc, ticket or person>.
```

Add a line when a decision changes the ticket after it is filed.

---

## 4. Type modules

Each type adds its module right after **Why**.

### Story or Task: no extra module

- Use **Story** when someone outside the team will see the change.
- Use **Task** for everything else.
- Both use the core only.

### Bug

```markdown
## Seen
<What happens. Include the number, the error, or a query that shows it.>

## Expected
<What should happen instead.>

## Reproduce
1. <steps, or the query that finds affected rows>

## Impact
<Who is hit, how many, and how much money if known.>
```

"Done when" must include a line like this: `D?. A test that fails before the fix and passes after — check: test`.

### Spike

Many Jira projects have no Spike issue type. File a spike as a **Task** whose title starts with `Spike:`.

```markdown
## Question
<One question, ending in "?".>

## Timebox
<N days. At the timebox, stop and write up what is known.>

## Output
<What the answer will look like: a decision note, a recommendation,
or follow-up tickets.>
```

A spike's "Done when" is always the same three lines:

```markdown
- D1. The question is answered, or the timebox is reached with what is known written down — check: review
- D2. The output names the options, how they were judged, and the pick — check: review
- D3. Follow-up tickets exist, or the note says none are needed — check: review
```

### Epic

```markdown
## Outcome
<The change we want, as something we can measure. How we will measure it,
and roughly when.>

## Children
- <KEY> — <one line>
- planned: <idea with no ticket yet>
```

Epic rules:
- **Children cover the outcome. No more, no less.** Every child is needed for the outcome, and together they are enough.
- **"Done when" includes the outcome check.**
- **Leftovers become a punch list.** Any children not done are listed by name, each one moved to a new home or dropped on purpose.

---

## 5. Ready check (before moving to In Progress)

Four yes/no questions. A "no" means fix the ticket first.

1. Could someone else tell when it is done, from "Done when" alone?
2. Is there nothing marked "before start", in Open questions or in Context?
3. Is it about a week of work or less? If not, split it. The team should set the real limit.
4. Is the parent linked, or does the ticket say why there is none?

---

## 6. Close-out (one comment when moving to Done)

```markdown
**Close-out**
- D1 ✓ <link to test, query result, or stage screenshot>
- D2 ✓ ...
- Changed from plan: <what changed and why, or "nothing">
- Left over: <items moved to new tickets, by key, or "nothing">
```

---

## Where each part comes from

| Part | Software source | Outside software |
|---|---|---|
| Why, up to 5 sentences | Connextra's "so that"; Shape Up's problem statement | Army commander's intent: "normally does not exceed five sentences" (FM 5-0, 2005) |
| Results, not code steps | Linear issues; Cucumber declarative scenarios | Army mission orders; NASA "what, not how" |
| Done when, with IDs | Acceptance criteria; Jeffries' Confirmation | NASA verification matrix (unique ID, success criterion) |
| Check method per line | BDD (tests as criteria) | NASA's four methods: test, analysis, demonstration, inspection |
| No fuzzy words | INVEST's "Testable" | NASA's good-requirement traits; INCOSE's characteristics of a good requirement |
| Not in scope | Shape Up no-gos; design-doc non-goals | PMI WBS 100% rule ("no extra work") |
| Open questions with owner | Example Mapping red cards | Construction RFIs, answered in writing within a time limit |
| Spike: question, timebox, output | XP spike; Shape Up appetite | NASA trade study and decision report |
| Epic: children cover the outcome | Story mapping; story splitting | PMI WBS 100% rule |
| Epic leftovers as a list | none found | AIA punch list at substantial completion |
| Ready check | Definition of Ready (a team convention, not in the Scrum Guide) | Last Planner quality criteria: definition, soundness, size |
| Close-out from Done when | Scrum Definition of Done | Army after-action review; pre-registration's "transparent changes" |
| Change log | Team practice | Pre-registration's "transparent changes" |
