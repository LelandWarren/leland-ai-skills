---
name: write-ticket
description: Use when someone wants a Jira ticket written from their own notes, requirements, meeting notes, a Slack thread, a bug report or data — "make a ticket", "turn this into a ticket", "write this up as a story/bug/spike/epic", "/write-ticket". Also when a pile of asks needs to become an epic with children.
---

# Write a ticket from notes

## Overview

The team's ticket shape lives in `TEMPLATE.md`, next to this file. Read it first. It sets the sections, the type modules and the rules for "Done when" lines.

This skill adds one thing on top: **every line traces to a source, or it is an ask.** The requester must be able to see which lines are facts and which are guesses.

## Sources

Every sentence in the ticket comes from one of three places:
1. **The input.** The requester's notes, data or thread.
2. **Something you read.** A Jira ticket or doc. Cite its key or link.
3. **An ask.** Written as `[ask: …]`, or as an open question.

A detail you would like to add but cannot source becomes an ask. This covers a reason, a date, an owner, a criterion, an outcome measure or a judging criterion.

When a "Done when", Behaviour or Outcome line depends on an open question, it says "as decided in Q1". It never states the answer you guessed. If the check method also depends on the question, write `check: as decided in Q1`.

**What counts as sourced:**
- The template's own defaults count as sourced. For example, a spike's output is a decision note.
- The order of work counts too. Writing "needed by: before start" is your call, not a fact you need from anyone.
- Facts from Jira go in **Context**, cited by key, but only when they change what gets built, checked or decided. A contradiction, a dependency's status and a "to confirm" all qualify. Renames, history and details of tickets this one doesn't touch do not. If a Jira fact contradicts the input, it also goes first in the Summary.
- **What "contradicts" means:** both can't be true at once. "No email is sent" against "the gateway emails a link" contradicts. So does a known limit against a promise the input makes ("can miss live tokens" against "ends their sign-in right away"). A status that lags is not a contradiction: "In Review" for work the input calls merged is a dependency's status, in Context.
- **Jira doesn't mention what the input assumes:** write it in Context as "to confirm", citing the key you read. If the work can't start until it is confirmed, write "to confirm before start".

**Who an ask is for.** Ask only for what the requester knows and the work can't find out:
- Their reason.
- A deadline.
- A choice between options.

Anything the work itself will find out is part of the work, not an ask. Put it in the spike's question, in Context as "to confirm", or in a Done-when line. "Which code is duplicated?" is the spike's job. An unknown owner is `owner: —`, not an ask.

A gap you spot while reading Jira is part of the work too. For example, a dependency can fail, but the input never says what the screen shows then. Make it a Done-when line, not an ask. End the line with `(gap: <key>)`, naming the ticket that shows the gap, so the requester can see you added it. If no ticket shows the gap, leave the line out.

## Steps

1. **List the facts in the input.** Do this in your head. Keep the input's own words for dates and amounts. "End of month" stays "end of month".
2. **Search Jira, if the Jira tools are available.** First read every ticket key the input names, even one cited for a single objective. Check the whole ticket against the input, not just the cited part. Then look in the team's project for unresolved tickets and epics that match the input's main nouns. Read the top matches.
   - A likely duplicate goes in the Summary.
   - Facts from a ticket you read are cited by key.
   - A clear parent epic is linked. Otherwise the parent is `[ask: parent epic]`.
   - Without Jira access, say so in the Summary.
3. **Pick the type.** Assume Epic, Story, Task, Bug and Subtask unless the project's own type list differs.
   - A spike is a **Task** whose title starts with `Spike:`.
   - If the input holds several separate results, or more than about a week of work, make it an **Epic**. List the children as one-line titles under Children. Do not draft each child in full.
   - **An existing ticket covers a child:** list it by key under Children. Put any conflict with the input in the Summary.
   - **The work may belong under an existing epic:** add that as an open question. Still draft the new one.
   - **A timebox given as a range:** use the top of the range. "2-3 days" becomes 3 days. Say so in the ticket.
   - **A spike's fixed lines:** keep them. You may add "(criteria as decided in Q1)" to D2.
   - **A bug's title:** name the fixed state. It must never contradict the input.
4. **Draft the ticket from `TEMPLATE.md`.** If the input has a change log, keep each entry in the template's Change log.
5. **Check the draft against the input:**
   - Is the input already a ticket, with a Why, criteria or steps? Then the draft should be no more than about 1.5× its length. If it is longer, cut Context first.
   - Does the title say the same thing as the input, in the same direction? For example, "included" and "left out" are opposites.
   - Does every sentence pass the Sources rule?
   - Does every "Done when" line follow the template rules?

## Handback shape

Reply in this order:

1. **Summary**, 5 lines at most:
   - The type and the title.
   - For an epic, the child titles.
   - Any duplicates or related tickets found.
   - How many asks there are, and anything marked "to confirm before start" (it fails the ready check).
2. **Check before filing.** At most 5 bullets, the most blocking first:
   - Each bullet is one `[ask: …]` or open question, naming the section it belongs to.
   - If there are more, end with "plus N smaller asks, marked inline".
3. **The ticket.** The full description in a markdown block. For an epic, the epic only.
4. **One closing line.**
   - For an Epic: "Say *file it* to create this in Jira, or *draft the children* for the child tickets."
   - For any other type: "Say *file it* to create this in Jira."

If the requester says "don't ask me questions", still deliver the full draft in this shape. Don't stop to ask first. The asks stay in the draft and the list.

## Filing

Create Jira issues only when the requester says yes. Then link the parent and any related keys, and reply with the new keys.

## Common mistakes

| Mistake | Fix |
|---|---|
| A believable reason added to Why ("they retype it by hand") | Use the input's reason, or write `[ask: why]` |
| "Maybe" in the input turned into a Done-when line | Make it an open question. The Done-when line says "as decided in Q1" |
| Issue type "Spike" | Task, with a title starting `Spike:` |
| "Parent: none" written without searching | Search, or write `[ask: parent epic]` |
| Six full tickets for one request | Draft the epic, list the children, offer to draft them |
| Asking the requester what the work will find out ("which code is duplicated?") | Make it part of the work: the spike question, Context "to confirm", or a Done-when line |
| `owner: [ask]` and `needed by: [ask]` on every question | `owner: —`, and pick "before start" or "before merge" yourself |
