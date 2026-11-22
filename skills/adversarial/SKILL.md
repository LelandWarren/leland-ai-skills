---
name: adversarial
description: Use when the user asks to stress-test a claim, output, plan, or document by arguing both sides — "adversarial review that", "/adversarial", "put that on trial", "argue both sides of this", "tear that apart and defend it", "steelman and attack this". A prosecutor argues it is completely wrong, a defender argues it is completely right, then a neutral judge rules. Works on the conversation itself or on an external file. Explicit invocation only.
---

# Put It On Trial (adversarial)

## Overview

Stage a courtroom over one proposition. A prosecutor is totally convinced it is wrong and argues
only that. A defender is totally convinced it is right and argues only that. They go two rounds.
Then a neutral judge rules for one side, states its confidence, and lists which accusations
stuck.

**Core principle:** a single reviewer trying to be balanced produces mush — "mostly fine, though
you might consider…". Two committed opponents produce specifics, because each one has to go find
something. The balance comes at the end, from the judge, not from either advocate.

## When to use

- The user asks for it: "adversarial review that", "/adversarial", "put that on trial", "argue
  both sides", "tear that apart", "attack and defend this".
- Two ways it gets pointed at:
  - **The conversation** — a claim, conclusion, recommendation, or plan from this session,
    including something you just said.
  - **An artifact** — a file, doc, or spec named by path.
- Skip it when the user wants a full multi-perspective review of a merge request or design
  doc — use a dedicated review skill (`pr-review`, `arch-review`) for that. This skill fetches
  nothing and argues one proposition.
- Skip it when the user wants a straight answer. This is deliberately not that.

## The method

### 1. Parse the invocation

| Form | Meaning |
|---|---|
| `/adversarial` alone | Target is the last substantive assistant output |
| `/adversarial <text>` | Explicit target or proposition |
| `/adversarial <path>` | Target is that file |
| A bare number, e.g. `4` | Round count N. Default `2` |
| `--deep` | Prosecutor and defender run as subagents with tool access |

Arguments combine in any order: `/adversarial 4 --deep "the batch fix is safe"`.

**"Last substantive output"** is the most recent assistant message containing a claim,
conclusion, recommendation, plan, or code. Skip acknowledgments, tool narration, and clarifying
questions.

### 2. Set the charge — exactly one proposition

A debate about "this document" produces nothing. Narrow to the single load-bearing claim.

- **Bare `/adversarial`** — draft the proposition, show it to the user, and **wait** for a yes or
  an edit before round 1.
- **Anything explicit** — do not ask. State the charge at the top of round 1 and begin.

If the target is a long document, say which claim you picked and why it is the load-bearing one.

### 3. Run the debate

Read the role contracts and follow them exactly:

- `references/prosecutor.md`
- `references/defender.md`

Each side must obey its own evidence rule. Do not soften either contract, and do not let the
prosecutor go easy because the target is something you wrote — that is the single most likely
way this skill fails.

Round order, for N rounds (default 2):

1. **Prosecutor opens.** It has not seen any defense.
2. **Defender responds** to the target and the prosecution.
3. **Round 2+: prosecutor rebuts** the defender's last message specifically.
4. **Round 2+: defender rebuts** the prosecutor's last message specifically.

#### `--deep`: real subagents with tool access

By default you play all three roles yourself. This is cheap and sees the whole conversation for
free, but it is one model arguing with itself — and prosecuting your *own* output is the softest
spot in the design. `--deep` fixes that structurally.

With `--deep`, each round dispatches the prosecutor and defender as **separate subagents**:

- Give each subagent the charge, the target, and the transcript so far — and **nothing
  about your own reasoning**. The point is that they did not inherit your framing.
- **Dispatch the two in sequence, never in parallel.** The prosecutor goes first. Append its
  argument to the transcript you hand the defender — the defender is contractually required to
  quote and answer the prosecution's actual words, and a defender dispatched in parallel
  receives nothing to rebut and gets scored as restatement.
- Instruct each to read its contract by path before arguing:
  `~/.claude/skills/adversarial/references/prosecutor.md` or `.../defender.md`.
- They have tool access. Tell them explicitly to go **gather** evidence — grep, read the files,
  check the history — rather than argue from what they were told.
- **When the target is the conversation**, a subagent cannot see the chat. Write a briefing
  dossier named `adversarial-dossier.md` to the session scratchpad — the charge, the exact text
  on trial, and any context it depends on — and pass the file path.

The **judge stays in-context**. It needs the full picture, and it is the role that speaks to the
user.

Run the full N. There is no early exit — a weak round 1 often sharpens in round 2, and
predictable cost is worth more than the tokens saved. `N = 1` is legal: openings only.

Render each side's output under its own heading so the transcript is readable as a transcript.

### 4. Rule

Read `references/judge.md` and follow it exactly. Read the original target before the transcript.
Discard `[UNSUPPORTED]` arguments, bad anchors, and restatements, and list what you discarded.
The verdict is binary.

## Guards

- **Never auto-trigger.** Explicit invocation only, like `eli5` and `grade6`.
- **Never fetch an MR, doc page, or ticket.** Argue what is in front of you.
- **Never let a side pad.** A prosecutor out of real charges says so and stops. Running out is
  itself a finding, and the judge treats it as one.
- **Never soften the verdict.** "Both sides make good points" is the failure this skill exists to
  escape. If it is close, that is `CONFIDENCE: low`, and the judge recommends more rounds.
- **Never post the verdict anywhere.** No MR comments, no ticket updates, no Slack. The output is
  for the user to read and decide on.

## Composing with other skills

This is a **content** lens. House convention is content first, tone last — so `/warmer` or
`/grade6` over the verdict afterward is fine and expected. It does not stack with itself except
by explicit re-invocation, which is exactly what a low-confidence ruling recommends.
