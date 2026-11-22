# The one checkpoint

The only stop before the report, except the ask before real numbers. Show all of this in one
message, then wait.

1. **The map** — `map.md` in short form, plus the proposal's delta in one or two lines.
2. **Scope** — what this review covers and what it leaves out. Name any unmerged MR the design
   leans on.
3. **Tier and why** — "normal, because it adds a call to another service and holds a DB
   connection longer."
4. **Lenses in two groups. Always show both:**
   - the 4 core lenses (always on): System fit · Blast radius & failure unit · Premises
     measured · Cost of being wrong,
   - the catalog picks, each with the signal that woke it.
5. **The problem brief**, in full.
6. **Designer count** (from the tier, overridable).

Then ask, in one line:

> Change anything? And check the problem brief and the map together: do they hint at the
> answer? Facts about today's system (what is slow, what it costs) are allowed. The
> proposal's mechanism, or a component it introduces, is a leak.

## After the answer

- Apply every change the user makes.
- If they flag a leak, rewrite the brief and show only the new brief again.
- Silence or "go" means the shown setup runs.
- Write `<pack>/confirmed.md`: tier, designer count, the full lens list with owners (which
  reviewer runs it, see the table in `reviewers.md`), and the final problem brief's path.

No other stop follows until the real-numbers ask (only if a finding needs a number) and the
report.
