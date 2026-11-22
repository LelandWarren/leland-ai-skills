# The report

The main session writes it from `judge.md` (or its own judging, if the judge failed). Agents
write dense, formal prose. Treat theirs as a rough draft and rewrite it plainly.

Save to `<pack-root>/report.md`. If writing it is refused, put the full report in the reply instead and say so. Then, in chat: the **Verdict** section only, the file path,
and two offers: copy the report somewhere kept, and draw a Mermaid diagram of the map with the
findings pinned on it.

## Template

Fill every section in this order. A section with nothing in it says "None."

```markdown
# Architecture review: <title> (<MR link or doc>)

## Verdict
<Two or three sentences. Is the design sound? The one thing to act on first.>
🔴 <n> · 🟡 <n> · 🟢 <n> (finding items, not scorecard rows) · Tier: <tier> · Designers: <n> (<how many matched the proposal>)

## Findings

### 🔴 <claim in one line> · <one-way | two-way> door
- **What goes wrong:** <given this state or load, this component does X, so who sees Y>
- **Evidence:** <file:line, contract, ticket, or number>
- **Other path:** <alternative> — <rough cost>
- **Downside of the recommended path:** <what it costs or risks>
- **Found by:** <IDs, e.g. FAIL-2 + DES-1 (2 of 3 designers)>

### 🟡 <claim> · <door>
<same fields, plus>
- **Owner:** <who decides> (unmade decisions only)

### 🟢 <what holds>
- **Holds while:** <the assumption it rests on>
- **Watch:** <sensitive spot> (optional)

## Cost of being wrong
<From C4: exit cost at ~6 months (low / medium / high) · flat or compounding · the cheapest
hedge today and its cost.>

## Lens scorecard
| Lens | | Why |
|---|---|---|
<every lens that ran, 🟢 rows included, from the judge's merged table>

## Open questions
<What could not be verified, and what would settle it. Kept apart from verdicts.>

## Dismissed findings
| ID | Claim | Why it died |
|---|---|---|
<every dismissed finding, including design-preference drops from compare.md, and
"Not judged (over cap)" rows. A finding split by the judge gets a row for its dismissed half,
e.g. "FAIL-2 (shutdown half)".>

Downgraded to a 🟢 Watch: <IDs, and which 🟢 item each folded into>.

## Out of scope
<One line: "N line-level notes came up — run /pr-review." Omit the line if N is 0.>

## How this ran
<Tier · designers · which agents ran · anything that degraded, and what that means for trust.>
```

## Rules for the text

- Findings order: 🔴, then 🟡, then 🟢. Within a verdict, one-way doors first.
- Each finding's claim is about components and flows. `file:line` is evidence only.
- **No PII.** Counts and field names only. Never a street address, recipient name, or phone.
- Plain language: short sentences, one idea each, every term used as the reader would say it.
