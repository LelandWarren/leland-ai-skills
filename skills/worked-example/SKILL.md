---
name: worked-example
description: Use when the user asks to see something explained through a concrete, step-by-step example — "/worked-example", "show me with numbers", "walk me through an example", "give me a worked example", "show me a concrete example", "I need a concrete example". Works for math (money, rates, totals), data moving through code (one record traced stop by stop), and choices between options (the same example run through each one). Builds one tiny example and changes it one visible step at a time, with a state table after each step. NOT for defining terms from zero (use eli5).
---

# Worked Example

## Overview

Explain something by building one tiny example and changing it one step at a time. The reader
watches the numbers or the record change, step by step, until the idea is obvious.

**Core principle:** made-up numbers are fine. Made-up behavior is not. The values can be invented
and small. Each step must match what the code or math really does.

## When to use

- The user asks for an example, a walkthrough with numbers, or "show me".
- A design choice is abstract and its failure is indirect: dedupe, claims, double billing,
  ordering. An example makes the failure visible.
- Skip it for a one-line factual answer. Never fire on your own just because you're explaining.

## Pick the mode

| Mode | Use when | Shape |
|---|---|---|
| **Math** | There's a calculation: money, rates, weights, totals | Small numbers, worked step by step |
| **Data flow** | A record moves through code or a system | One tiny record, traced stop by stop, with a flow strip |
| **Options** | Comparing choices | One shared setup, a short run per option, a comparison table at the end |

## The method

1. **Check the mechanics first.** If the example is about real code or a real system, read the
   code path (or run the math) before you write a step. Pure math or a general idea skips this.
   If you can't check a step, mark it ⚠️ and say what you assumed. Never guess silently.
2. **Choose tiny, made-up values.** Use 2–4 items and round-ish numbers (10, 12, 8 dollars). Use real
   data only when the user asks for it. Real rows can carry PII (street address, recipient name),
   and prod databases are busy.
3. **Write the Setup line.** One bold line, no emoji: what we start with.
4. **Walk 3–7 steps.** Each step is one line: what happened, plus the tiny calculation or the
   rule that fired. Then show the updated state table. If it needs more than 7 steps, split it
   into parts ("Part 1: ingest", "Part 2: invoice").
5. **Mark the aha.** Put 👉 on the one step where the surprise happens: where the double charge
   comes from, or why option B is safer.
6. **Close with the result.** One ✅ line saying what the example shows.

Show all the steps at once. Don't wait for "next". The user can ask you to slow down at a step.

## Visual markers (fixed legend)

Use these every time, so the reader's eye learns them once:

| Marker | Meaning |
|---|---|
| **Setup:** | The starting state (bold label, no emoji) |
| 1️⃣ 2️⃣ 3️⃣ … | Step numbers |
| 🆕 + **bold** | The cell or value that just changed |
| 👉 | The aha step |
| ⚠️ | A step not checked against code, or a failure in an options table |
| ✅ | The result, or the good outcome in an options table |

Topic emojis (📦 shipment, 💵 money, 📄 file, 🗄️ database, 🧩 mapper) are fine where they help
the eye. Keep it to about 6 marker types per example: it should feel like a map, not confetti.

**Data-flow strip.** Put the whole trip on one line at the top. Then bold the current stop at each
step:

```
📄 file → 🧩 mapper → 🔍 enrich → 🗄️ DB
📄 file → **🧩 mapper** → 🔍 enrich → 🗄️ DB   ← you are here
```

## Template: math

> **Setup:** 3 shipments, cost 10 · 12 · 8 dollars. Markup is 15%.
>
> **1️⃣ Find each markup** → 10 × 15% = **1.50**
>
> | 📦 | Cost 💵 | Markup | Sell |
> |---|---|---|---|
> | A | 10.00 | **1.50** 🆕 | — |
> | B | 12.00 | **1.80** 🆕 | — |
> | C | 8.00 | **1.20** 🆕 | — |
>
> **2️⃣ Add it to the cost** → 10.00 + 1.50 = **11.50**
>
> | 📦 | Cost 💵 | Markup | Sell |
> |---|---|---|---|
> | A | 10.00 | 1.50 | **11.50** 🆕 |
> | B | 12.00 | 1.80 | **13.80** 🆕 |
> | C | 8.00 | 1.20 | **9.20** 🆕 |
>
> 👉 **The aha:** markup is a percent, so the bigger shipment earns more (1.80 vs 1.20).
>
> ✅ **Result:** 30.00 of cost becomes 34.50 to bill.

In real output, write money the normal way, with a dollar sign. This file writes amounts without
one only because of the loader trap noted at the bottom.

## Template: options

Use one shared setup. Then give each option its own short run (2–4 steps, same markers). End with
one comparison table:

> | | Option A | Option B |
> |---|---|---|
> | Billed 💵 | 50 ⚠️ double | 25 ✅ |
> | Why | resend inserts a second row | resend matches the first row and is skipped |

## Composing with other skills

- **Order:** `eli5` defines the words first → this skill runs the example → `grade6` or `warmer`
  polish last.
- With `grilling` or a decision brief: use the options mode inside a question whose failure is
  indirect, so the user can see the failure before choosing.
- If the user wants to learn an area deeply, with practice and recall, suggest a longer tutoring
  session (or `slow-teach`) instead.

## Red flags — you've drifted

- A step describes behavior you didn't check, and it has no ⚠️.
- The numbers got big or messy (1,247.83) when 10 would do.
- More than 7 steps in one part.
- A step changed two things at once.
- No 👉, or 👉 on more than one step.
- The table repeats without a 🆕 showing what changed.
- Emoji confetti: more than about 6 marker types.

## Quick check before you send

Could someone follow every step, see exactly what changed each time, and point at the aha
without reading any prose? Does each step match what the real code does? If not, revise.

## Maintainer note: no dollar sign before a digit in this file

The skill loader treats a dollar sign followed by a number as an argument slot, like a shell
script does. When the skill is called with arguments, each such amount gets swapped for an argument
word: "ten dollars" written the usual way came back as "surcharge" in the first test (2026-10-19).
Write amounts here as plain numbers, and keep the dollar sign away from digits.
