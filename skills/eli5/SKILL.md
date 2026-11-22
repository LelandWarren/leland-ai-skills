---
name: eli5
description: Use when the user explicitly asks to have something explained as if they're new to it — "explain like I'm five", "like I'm a junior", "over-explain this", "I don't know what I don't know", "walk me through it from zero", "pretend I've never seen this". Works for code, a technical mechanism, a domain term, a process, or a doc. Anchors on what the reader already knows, defines every term, gives only the core, and reassures without talking down.
---

# Explain Like I'm New (ELI5)

## Overview

Explain something to someone who doesn't yet know the vocabulary — and may not even know which
questions to ask — so they come away genuinely understanding it and feeling it was never as scary
as it looked.

**Core principle:** explain the *thing*, never explain *down*. The reader is smart; they just
aren't in this context yet. Difficulty here is almost always a simple idea wearing a lot of
vocabulary — so name the vocabulary and expose the simple idea.

## When to use

- The user explicitly asks: "explain like I'm five / a junior", "over-explain it", "I don't know
  what I don't know", "walk me through from zero", "pretend I've never seen this".
- Works on anything: code, a technical mechanism, a domain term, a process, a design doc.
- Skip it when the user wants a terse expert answer — this is the deliberate opposite of that.

## The method

Work in this order:

1. **Anchor on what they already know.** Open with one thing the reader owns or has seen: their MR,
   their ticket, a tool they use daily ("!123 is your hosting MR. It sets up hosting for the
   web app's pages."). Build outward from that anchor. Assume no vocabulary beyond it.
2. **Build in dependency order.** Define A before you use A to explain B. Lay the foundation, then
   build on it.
3. **Define every term on first use.** A one-line plain gloss in parentheses or after a dash. No
   unglossed jargon, ever.
4. **Name the vocabulary they don't know they're missing.** "Here are the words that'll show up, so
   they stop being scary." This is what actually helps someone who doesn't know what to ask.
5. **For an engineer, real code is the analogy.** Show a 2–5 line snippet, or a before/after pair,
   of the actual thing. Reach for an everyday analogy (a receipt, a labeled drawer) only when the
   reader isn't technical or no code fits. One good analogy beats three strained ones.
6. **Reassure honestly.** Name that the thing is smaller than it looks, and *why* — usually because
   a simple idea is carrying a pile of names.
7. **Close with a one-breath summary.** Restate the whole thing in plain English, as if to a friend.
8. **Give the core, then stop.** The core is the 2–3 ideas the whole thing rests on, and the reply
   fits on one screen. Everything else is a next layer: name it in one line ("The 3 parts we kept
   are a detail on top. Want that next?") and let them pull it.

## Reassure without belittling (the line that matters most)

Reassuring makes the reader feel capable. Belittling makes them feel dumb for not already knowing.
The difference is concrete:

- **Do:** "This is smaller than it looks — really one idea with a lot of names attached." / "Nothing
  here is over your head; you've now seen every term." / "The scary-sounding word just means X."
- **Don't:** "This is easy." / "Obviously…" / "Simply do X." / "As everyone knows…" — each of these
  quietly says *you should have known this already*.

Drop "just", "simply", "obviously", "trivially". Explain the thing, not the person.

## Composing with other skills

This is a **content lens** — invoke it alongside others and stack them:

- **Order:** content/clarity first, tone last. This skill and `writing-plainly` are both content
  lenses; a tone pass like `warmer` runs *after*.
- **On conflict, the more specific skill wins.** This skill deliberately **overrides**
  `writing-plainly`'s "don't over-explain / don't belabor the obvious" — here, over-explaining and
  defining the obvious *is* the point. It keeps plainly's DNA (plain words, non-condescending, no
  jargon walls) and its brevity: every term gets defined, but only the core gets explained.

## Red flags — you've drifted

- A term went undefined.
- You assumed context the reader said they don't have.
- A wall of text with no foundation laid first.
- "Easy / simple / obvious / just" crept in.
- You dumped every layer instead of offering the next one.
- More than 3 ideas, or more than one screen, before the first offer.
- You opened on a metaphor while the reader's own MR or code was right there to anchor on.
- The analogy is doing more harm than good — they'd now believe something false.

## Quick check before you send

Could someone who'd never seen this topic follow it top to bottom, know every term by the end, and
feel it was more approachable than they feared — without ever feeling talked down to? If not,
revise.
