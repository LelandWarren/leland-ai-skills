---
name: double-check
description: Use when the user says /double-check, "double-check that" or "fact-check that"; when the double-check gate hook blocks a post or plan; before asking the user to decide something that rests on facts; before building a design, plan or recommendation on a code or system fact; or before stating from memory how an outside system (API, auth, cookies, cloud, Claude Code) behaves.
---

# double-check

Every fact starts **wrong**. It becomes VERIFIED only with a **receipt**: a quote or value from a
source opened during this check, plus where it lives (`file:line`, command and output, URL, ticket
key and field).

## Modes

| Mode | When | Claims | Output |
|---|---|---|---|
| full | `/double-check`, "double-check that", "fact-check that" | up to 10 | full report |
| quiet | the gate hook blocked a call, or you self-started | up to 5 | all pass: `Checked N facts, all have receipts.` Otherwise the full report, top line counting every claim |

Full-mode target: the last assistant message that states facts (default), given text, a file path,
or `helper` (the last helper report). `--fresh` hands steps 2–4 to one helper (below).

## Steps

1. **Claims.** Quote each checkable fact word for word, one per line. A sentence holding two facts
   becomes two claims. Facts are names, numbers, dates, states, and what code, files, tickets or
   systems say or do. List opinions, plans, predictions and reasoning as "out of scope (try
   /adversarial)". Over the cap: check the claims the message leans on most and list the rest as
   "not checked".
2. **Falsifier.** For each claim, write where the truth lives and what you would see there if the
   claim were wrong. In full mode, print the claim list with its falsifiers before the first
   source is opened.
3. **Receipt.** Open that source with read-only tools. Each check opens its own sources.
   - Our code and config: read the lines themselves. A file name, file type or hit count is a
     pointer, not a receipt.
   - Tickets, MRs, Slack, counts, CI: fetch now.
   - Outside systems: the official docs page, or a small local test (curl, a short script). When a
     fetch tool summarizes the page, ask it for verbatim quotes; a quote is a receipt, a
     paraphrase is a lead. Blogs and forums are leads.
   - A claim about change over time ("now", "since", "used to"): check the current state. If it
     holds but no source dates the change, the verdict is VERIFIED with the time word dropped.
   - "Not found" is a receipt only when the whole source was searched (a grep, a full read). A
     partial read that finds nothing leaves the claim at CAN'T VERIFY.
   - Memory, training, earlier chat and the message under check are the claim's origin, never its
     receipt.
4. **Verdict.** VERIFIED · WRONG (give the true fact and its receipt) · PARTLY WRONG (say which
   part) · CAN'T VERIFY. No receipt means CAN'T VERIFY.
5. **Report.**
   - Top line: `X of Y verified · Z wrong · P partly wrong · W can't verify`.
   - Table: Claim | Verdict | Receipt.
   - For each WRONG: "I was wrong about …", then the corrected statement.
   - The out-of-scope and not-checked lists.

The skill reports. Fixes are offered to the user, never made by this skill.

**After a gate block:** all pass → retry the identical call. A WRONG claim → replace it with the
true fact from its receipt. A CAN'T VERIFY claim → tag it "(unchecked)" or cut it. Tell the user
what changed, then retry. Changed text is gated once more, and the quiet check is quick the second
time. The gate adds a check; the user's own approval rules for sends and posts still apply.

## Your own claims

The claim under check is usually one you made, and you will want it to be right. A claim you
remember making with confidence still needs a receipt. "I'm fairly sure the docs say…" is CAN'T
VERIFY until the docs are open.

## --fresh

Write the step-1 claim list, claims only, to `double-check-claims.md` in the scratchpad. Dispatch
one helper (Sonnet, effort medium) with that path and this file's path; it runs steps 2–4 and
returns the table. If its answer looks thin, rerun it on the parent model and say so.

## Gate hook

`scripts/gate.py` (PreToolUse) blocks once before outward posts (Slack, Jira, Confluence, GitLab,
Gmail, and `glab`/`gh` commands that create or comment on MRs, PRs and issues), `ExitPlanMode`,
and the first `Write` of a design, spec or plan file per session.
Off switch: `touch ~/.claude/double-check/off`. Tests: `scripts/test_gate.py`.
