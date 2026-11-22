# Comment Style

Tone: empathetic, down-to-earth, non-condescending, non-verbose. Assume the author is
probably right. Mark optional things **optional** and say *why*. Always include a
`file:line` anchor. Prefer one clear ask per comment.

**Before these templates apply, the autonomy filter has already run** (SKILL.md phase 7):
a preference-only observation never reaches a template — it was dropped or demoted to a
one-line non-blocking aside. So every comment produced here is, by construction, a real
code-health issue or an explicitly-optional teaching note.

## Template: optional-hardening

For a safe, cheap improvement that is NOT a correctness bug.

> **Optional — take it or leave it, not a correctness issue.** <one line: why the code
> is already safe>. The only wrinkle: <the edge/cost>. <The cheap change> would <benefit>.
> <Reassure about any downside>. Totally fine to leave as-is; just flagging the cheap version.

## Template: informational

For a "the label doesn't match the box" heads-up; assume the author is right.

> Small heads-up, probably nothing on your end — <the observation, e.g. summary claims X
> but the diff shows Y>. I'm guessing <benign explanation>, which makes sense given <context>.
> Just confirming <the thing> is intentional so nobody <bad outcome>. No change needed if so.

## Template: rationale-request

For capturing the "why" of a magic number / decision.

> Could we link <ticket> here (or a one-liner) on why <the value/decision>? Mainly so
> future-us reads it as <the real reason> rather than a magic number — and knows <the
> important scoping caveat>. Non-blocking, just for the paper trail.

## Anchoring

Give the exact `file:line` for inline comments; use a general MR comment for anything
about the MR as a whole (e.g. a stale summary). Provide an anchor table when there are
several.
