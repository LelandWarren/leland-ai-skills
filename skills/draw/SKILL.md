---
name: draw
description: Use when the user says "/draw", "draw that", "picture it" or "diagram this" about something Claude just explained (an architecture, a process, a data path, a decision), or says yes to a "Want a picture?" offer.
---

# draw

Turn the last explanation into a picture inline in chat, walked through the way `eli5` explains:
anchored on what the user knows, every box given its what and why. The chat is the canvas. An
Artifact is a separate ask.

1. **Load the guide.** Call `mcp__visualize__read_me` with modules `["diagram"]`, silently. Its
   rules govern every box, color and size. This skill adds only what it leaves out.
2. **Pick the type** from what the explanation does:

   | The explanation...                                   | Draw                                                      |
   | ---------------------------------------------------- | --------------------------------------------------------- |
   | moves one thing through steps (a file, a request)    | flow                                                      |
   | says what lives inside what (services, buckets)      | structure                                                 |
   | weighs two options, or before against after          | compare: two columns, same rows, the difference in color  |

3. **Boil it down.** List the nouns the reader must hold. Each one is a box. The budget is 6 boxes
   per drawing, side notes included, and read_me's 4–5 is the sweet spot. Over budget: draw an
   overview first (one box per part, the main arrow only), then one drawing per part.
4. **Label and color.**
   - Label with names of systems, carriers, paths and states, in the short words the user already
     uses. Stand in a role ("customer", "ops contact") for any person, customer name, email,
     address or account number.
   - Color what's new: parts that exist today are gray, the new or changed part gets one color
     ramp. When nothing is new, color by owner (one ramp per team, gray for storage). Add a
     one-line legend.
5. **Draw** with `mcp__visualize__show_widget`, then walk the drawing right under it, in about 150
   words:
   1. **Anchor:** one line on what the user already knows and what this drawing adds.
   2. **Each box, one line:** what it does, and why it's there when the explanation or the code
      says why.
   3. **How**, only where the mechanism is the point (a status code, a one-step save).
   4. **Words you'll see:** a short gloss for new terms in the labels. Skip terms already
      explained this session.

   After the last drawing, give a one-breath summary, then offer the next layer in one line.
   A box with no sourced why keeps its what alone. Guessed whys go in one "Open whys" line after
   the summary, tagged "(unchecked)". Each drawing carries its own legend. `/draw` is an ask to
   explain, so the reply-size cap lifts. Each drawing's walkthrough stays on one screen.
6. **Offer to publish when others will read it.** If the user names a reader, a channel or a doc,
   end with one line: "Publish this as an Artifact?" Publish only on their yes.

If `show_widget` is missing from the session, write the SVG to the scratchpad and send it with
`SendUserFile`, `display: "render"`.
