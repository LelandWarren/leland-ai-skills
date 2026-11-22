---
name: slow-teach
description: Use when the user asks to be taught a topic slowly, over many turns, one small piece at a time — "teach me slowly", "one piece at a time", "one tiny piece at a time", "I get lost when too much comes at once", "slow teach", "/slow-teach". Works for any topic: a design idea, a system, a domain concept, a plan. NOT for a one-shot explanation from zero (use eli5), or a single example with numbers (use worked-example).
---

# Slow Teach

## Overview

Teach one tiny idea per turn. The learner's answers set the pace.

**Core principle:** plan the whole ladder privately, and show one rung at a time. The learner only
ever sees the piece they are on. Too much at once is the failure this skill exists to prevent.

Teaching only. During the lesson, build, edit, and decide nothing.

## Before turn 1: build the ladder (private)

1. **List 5–10 pieces** in dependency order. Each piece is one idea you could say in one sentence.
   The last piece is always "what this means for you" or "the first small step."
2. **Pick one anchor picture**: an everyday scene that can carry most of the pieces (a house-sitter
   reading a fridge note, a store receipt).
3. **Run the picture check.** Act the scene out in your head. If the real scene does something the
   idea doesn't, pick another scene. (A coat check hands the coat back, so it's a poor picture for
   "skip the repeat.")

Never show the ladder. Saying how many pieces there are is fine.

## Turn 1

Open with: "We'll go one tiny piece at a time. Stop me anytime, or say 'faster' or 'skip.'"
Then teach Piece 1 in the turn shape below.

## The turn shape (every teaching turn)

1. **Header:** `**Piece N of M: <name>**`. Use sub-parts when a piece needs more than one turn:
   `**Piece 3, part 2: silver**`.
2. **Body:** 5–8 short sentences, sixth-grade words, one idea.
3. **One picture.** Reuse the anchor. Add a new picture only for an idea the anchor can't carry.
4. **No tables.** Lists of 4 items or fewer.
5. **Last line:** `**Quick check:**` and one question that applies the idea to a real case from
   the learner's own world.

Quick check, good: "A partner resends `orders-0915.csv` with the same order numbers. What happens to
row 1?" Quick check, weak: "What is an idempotency key?" The good one asks them to use the idea.
The weak one asks them to recite it.

## Replying to an answer

1. **First line grades it**, in a few words: "Exactly." / "Close. One fix: gold is one person, not
   many." / "Not quite. The system can't see names at all. Let's try a different picture." When
   it's off, name the miss in one short clause.
2. **Reuse their good phrases.** If they coin a phrase that fits, say so and use it from then on.
3. **Right or close:** add at most one refinement. Then teach the next piece in the same turn,
   under its own header.
4. **Shaky or wrong:** re-teach the same piece with a new picture, under `**Piece N, again: <name>**`.
   Fix the first idea before adding a second. End with a fresh quick check.
5. **"faster":** fold the next two pieces into one turn. **"skip":** go straight to the next piece.

## The last piece

Recap every piece in one line, like "1 the problem → 2 a claim → 3 trust steps → …". Then ask one
yes/no question about what to do next. Do nothing on it without a yes.

## Fits with

- A Mentor or ADHD style: the quick check is the turn's one next action, so it stays the last line.
- `eli5` explains from zero in one go. `worked-example` traces one example with numbers. This skill
  is the slow, many-turn version, and can borrow either inside a single piece.

## Red flags: you've drifted

- Two pieces, or the ladder, showed up in one turn.
- A turn has no `Piece N of M` header.
- The quick check asks for a definition from memory.
- The grade isn't the first line of the reply.
- A shaky answer got a second new idea instead of a new picture.
- The picture's real-world behavior fights the idea.
