# Gather and map

Both run in the main session, before the checkpoint. Everything lands in the evidence pack.
No later agent re-fetches the proposal. That way every agent reviews the same bytes, even if
someone pushes mid-review.

## Pack layout

`<pack-root>` = `<scratchpad>/arch-review-<slug>/` (slug = MR iid, ticket key, or a short name).
`<pack>` = `<pack-root>/pack/`.

```
<pack-root>/
  pack/
    proposal.md          # MR description + title, or the doc, or the confirmed restatement
    diff.patch           # MRs only
    discussions.json     # MRs only
    context.md           # tickets, repo CLAUDE.md facts, recalled memory facts
    map.md               # today's neighborhood, NO proposed changes (designers read this)
    proposal-delta.md    # what the proposal changes on the map (designers never read this)
    problem-brief.md     # the problem, no solution (designers read this)
    confirmed.md         # written after the checkpoint
    sheet.md             # designer headlines
  designers/  reviewers/  adversaries/
  compare.md  numbers.md  judge.md  report.md
```

## Gather

- **MR:** `glab api --method GET "projects/<enc>/merge_requests/<iid>"`, `.../diffs?per_page=100`
  (page until empty), `.../discussions?per_page=100`. `<enc>` is the URL-encoded project path.
- **Doc or ticket:** read it with whatever connector reaches it (Confluence, Jira, a file).
  If none can, ask the user to paste it.
- **Idea only:** write `proposal.md` as **"Your proposal as I understand it"**: the problem,
  the approach, what changes where, what is out of scope. Show it. Wait for the user to
  confirm or fix it. Review only the confirmed version.
- **Context:** walk linked tickets (story → epic → blockers). Read the repo `CLAUDE.md`.
  Recall memory facts about the services involved. Re-check any fact that names a file, flag,
  or function before relying on it.

## Map

Draw the neighborhood the change touches, **as it stands today**.

- **What goes on it:** services and repos, the tables and queues they own, the calls between
  them (sync or async, timeout, retry), contracts (APIs, events, files, shared tables), who
  consumes each, and the deploy and rollout model.
- **Where facts come from:** read standing system facts at run time from the repo's
  `CLAUDE.md` and the user's memory (capacity, timeouts, monitors, deploy gates, known
  traps). Nothing is shipped with this skill, so nothing here goes stale.
- **Cross-repo reads:** default branch only, `ref=HEAD`. Never assume the literal name
  `master`. Read another branch only when the user names it. The repo under review is read on
  the MR branch for `proposal-delta.md` and at `ref=HEAD` for `map.md`.
  - File: `glab api --method GET "projects/<enc>/repository/files/<enc-path>/raw?ref=HEAD"`
  - Tree: `glab api --method GET "projects/<enc>/repository/tree?ref=HEAD&path=<dir>&per_page=100"`
  - Code search: `glab api --method GET "groups/<group>/search?scope=blobs&search=<term>"`.
    Always scope to the group. Global search is denied.
- **Local clones are off limits for git.** Never `fetch`, `checkout`, or `pull` in a local
  clone: it belongs to the user and may hold their work. Read local files only when the clone
  is on the branch you need. Otherwise read through `glab` with `ref=<branch>` (the MR's
  `source_branch` for the delta, `ref=HEAD` for today).
- **Dated facts about another team's system go stale.** When a memory fact about another
  service drives a finding (an index exists or not, a timeout value, a limit), re-check it on
  that repo's default branch before putting it on the map.
- **Unmerged work:** if the design leans on another open MR, mark it `(unmerged: !NNN)` on
  the map. Findings that rest on it must say so.
- A wide neighborhood may go to one `Explore` agent (read-only) for the cross-repo sweep. The
  main session still writes `map.md`.

Then write:

- `map.md` — today's system. Plain boxes-and-arrows text. Keep it to what the change touches
  plus one hop out.
- `proposal-delta.md` — what the proposal adds, removes, or rewires on that map.
- `problem-brief.md` — the problem in the user's and the system's terms: who hurts, what is
  slow or wrong, the constraints (deadline, team size, SLAs), and what "solved" looks like.
  **No approach, no mechanism, no component the proposal introduces.** Test: could a designer
  guess the proposal from this brief alone? If yes, rewrite it.

## Depth tier

Suggest one from the map. The user confirms at the checkpoint.

| Tier | When | Designers | Agents |
|---|---|---|---|
| Light | one service, no contract or data-owner change, two-way door | 0 | none, main session inline |
| Normal | a contract, a shared resource, or a second service touched | 2 | designers + 3 reviewers + straw-man + judge |
| Heavy | a one-way door, stored data others read, several services, or money customers see | 3 | designers + 3 reviewers + steel-man + straw-man + judge |

## Lens picks

The 4 core lenses always run. Pick catalog lenses from their **"Pick it when"** signals in
`lenses.md`, and write down the signal that woke each one. #15 (Problem fit and scope) is
always picked for design proposals and ideas. For an MR, pick it by its signals (vague
description, scope much bigger than the ticket).
