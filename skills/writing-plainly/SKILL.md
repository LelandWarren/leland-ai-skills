---
name: writing-plainly
description: Use when writing something a reader needs to understand quickly — a PR/MR description, a doc or spec summary, a ticket or Slack comment — or when asked to explain or summarize something clearly, plainly, or in simple terms. Applies whenever the audience may be outside the weeds of the work.
---

# Writing Plainly

## Overview

Write so a smart reader who isn't in the weeds gets it fast: plain words, honest about what's done and not done and the trade-offs, any unavoidable term defined, and never talking down.

**Core principle:** Lead with the plain answer, then the depth. Say what you did *and* what you didn't. Respect the reader's intelligence without assuming their context.

This is a recipe, not a rulebook — aim for output that *looks like* the shapes below.

## When to use
- Writing a PR/MR description, a doc/spec summary, or a ticket/Slack comment.
- Asked to "explain this clearly / plainly / in simple terms," or to summarize work.
- Any time the reader may not share your context.

Skip it for writing aimed at people already deep in the same weeds (a terse note to a co-implementer), where shared jargon is faster.

## Voice (always)
- **Plain words over jargon.** Prefer the everyday equivalent.
- **Short sentences, skimmable structure** — tight sections, short bullets.
- **Answer first, detail after.** Don't make the reader dig for the point.
- **Non-condescending.** Explain the *thing*, don't explain *down*. Assume a competent reader who simply isn't in this context. Drop "simply / just / obviously." Don't belabor the obvious.

## Substance (the honesty moves — this is what makes it trustworthy)
- **Did AND didn't.** State what you did, then explicitly what you didn't do or left out of scope.
- **Name the alternatives.** Mention the options/trade-offs you considered, not only the chosen path.
- **Own the limits plainly.** What isn't working yet, what you assumed, known caveats — stated, not hedged or buried.
- **Tag numbers by how solid they are.** Mark each as measured, derived, model or guess. Only measured or derived numbers go in a headline, a summary, bold text or a summary table. A model shows as a range with its inputs. A label in small print loses to a bold number, so the format must match the label. Asked for a number you can't measure? Say so, and name what would measure it.

## Jargon and terms
- Reach for a plain equivalent first.
- If a domain term is genuinely unavoidable, **gloss it on first use** — a one-line inline definition in parentheses or a dash.
- If a doc leans on several such terms, add a short **glossary** block near the top.

## Per-artifact recipes

**PR / MR description** — sections in this order:
1. **The problem** — what was wrong or missing, plainly.
2. **What we did** — the change, in a few bullets.
3. **What we didn't** — scope boundaries; what other tickets own.
4. **Why this solves it** — the reasoning tying change to problem.
5. **Notes / future work** — caveats, follow-ups, anything deferred.
6. **Testing** — what you verified and how; what's still unverified.

**Doc / spec summary:** a plain one-paragraph "what this is and why" up top, then the details.

**Chat "explain clearly":** no template — voice + substance only. Give the plain answer first, then the depth if wanted. A one-sentence analogy is fine when it genuinely helps; skip it if the topic is sensitive or the analogy would distort.

## Composing with other skills

This is the base **content/clarity lens** — invoke it alongside others and stack them:

- **Order:** content/clarity first, tone last. This skill runs before a tone pass like `warmer`.
- **On conflict, the more specific skill wins.** `eli5` deliberately **overrides** this skill's
  "don't over-explain / don't belabor the obvious" when the reader is new to the topic and wants
  every term defined. That's expected — reach for `eli5` instead of this skill when the goal is to
  teach from zero rather than to compress for a smart outsider.

## Red flags — you've drifted
- A wall of jargon with nothing defined.
- Only the happy path — no "what we didn't do."
- Caveats hedged into vagueness or buried at the bottom.
- "Simply / just / obviously," or over-explaining things the reader plainly knows.
- The reader would have to already understand the work to understand the writing.

## Quick check before you post
Would someone one step removed from this work — a teammate on another feature, a reviewer, a PM — get the point on one read, know what you did and didn't do, and trust that you named the limits? If not, revise.
