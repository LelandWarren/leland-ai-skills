---
name: grade6
description: Use when the user asks to make a text readable at a 6th-grade level — "make that grade6", "/grade6", "at a sixth-grade reading level", "rewrite this so a 6th grader gets it", "draft the MR grade6". A pure reading-level lens: same meaning, simpler prose. Works on a text they point at OR a text they're asking you to produce. Does NOT explain, define, or add anything — pair with eli5 for that.
---

# Rewrite to a 6th-Grade Reading Level (grade6)

## Overview

Rewrite text so the same meaning lands at a 6th-grade reading level — short sentences, common
words, simple structure. Nothing is added. Nothing is explained. The *only* thing that changes is
how hard the writing is to read.

**Core principle:** keep the meaning exactly; lower the reading level, not the content. The reader
is capable — they just want it to go down easy. Grade 6 is a hard target, not a knob: there's no
"make it grade 4" here.

## When to use

- The user asks for it: "make that grade6", "/grade6", "at a sixth-grade level", "so a 6th grader
  gets it", "keep it simple, grade-six".
- Two ways it gets pointed at, both handled the same way:
  - **Transform** — an existing text. "Make that last comment grade6." → rewrite that text.
  - **Generate-into** — a text that doesn't exist yet. "Draft the MRs grade6." → write the new text
    at grade 6 from the start.
- Skip it when the reader needs a term *explained*, not just simplified — that's `eli5`. Skip it
  when the user wants an expert-terse answer.

## The method

Rules do the heavy lifting. Apply them in this order:

1. **One idea per sentence.** Split any sentence carrying two. If it has a "which/that/because/so
   that" tail doing real work, it's probably two sentences.
2. **Keep sentences short.** Aim ~12–15 words. A long sentence is the single biggest thing that
   pushes reading level up.
3. **Plain words over formal ones.** Prefer 1–2 syllable, everyday words. "use" not "utilize",
   "so" not "consequently", "enough" not "sufficient", "about" not "regarding".
4. **Active voice, concrete subject.** Someone does something. "The job retries the file" beats
   "the file is subjected to a retry."
5. **Cut nominalizations and filler.** "perform a reconciliation" → "match the bills";
   "make a determination" → "decide". Drop hedges and throat-clearing.

### Two guards that keep it honest

- **Fidelity guard — keep the real terms.** Some words have no plain-English twin: `reconciliation`,
  `idempotent`, `Flesch-Kincaid`, product names, people's names, identifiers. Keep them exactly.
  Simplify everything *around* them so the sentence still reads at grade 6. Do **not** define them —
  that's `eli5`'s job when the two are paired. Never trade correctness for a smaller word.
- **Structure guard — rewrite prose only.** Preserve headings, bullets, lists, and layout. Leave
  code blocks, commands, and identifiers untouched. You're lowering the reading level of the
  sentences, not reformatting the document.

## The hard-target check

Grade 6 is a hard target, so check it — don't just aim.

After you draft, do a **silent self-check pass**: read back over the result, estimate its
Flesch-Kincaid Grade Level, and rewrite any sentence that reads above grade 6 (usually because it's
still too long or still leans on a formal word). Then show the final text.

Be honest about what this is: the estimate is your own read, not a calculator — there's no script
and no tool. It's a checked, best-effort target, not a measured one. Keep the check silent; don't
narrate the grade or show the estimate unless the user asks.

## Composing with other skills

This is a **content lens** — stack it with others, don't merge them:

- **Order:** content/clarity first, tone last. `grade6` runs before a tone pass like `warmer`.
- **Distinct from its siblings, on purpose:**
  - `eli5` *adds* explanation and defines every term. `grade6` never explains — it only lowers
    reading level. Pair them when a reader needs a term both simplified *and* explained.
  - `writing-plainly` makes writing clear for a smart outsider but isn't locked to a grade.
    `grade6` locks to grade 6 and changes reading level only.

## Red flags — you've drifted

- You explained or defined a term. (That's `eli5`. Here, keep the term and simplify around it.)
- The meaning shifted, or a nuance got dropped, to fit a smaller word.
- A sentence still runs long or still leans on a formal/latinate word.
- You touched a code block, command, or identifier.
- You reformatted the document instead of just rewriting its prose.

## Quick check before you send

Same meaning, grade-6 prose, nothing added — would a 6th grader read this top to bottom without
stumbling? If not, revise.
