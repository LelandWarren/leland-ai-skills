# The ten habits

Check every design against all ten. For each, write "met", or "broken" with the reason.
Sources and evidence: [`research.md`](research.md).

1. **Split essential from accidental.** Keep what the problem itself needs. Cut what our tools
   and choices added. (Brooks, No Silver Bullet)
2. **Untangle before you simplify.** Simple means not **complected**: no concerns braided
   together. Easy only means familiar. Look for two jobs woven into one piece. (Hickey)
3. **Deep pieces, small doors.** Each module has a small interface and lots of work behind it,
   and hides the decision most likely to change. (Ousterhout; Parnas 1972)
4. **Thin contracts at real seams.** Where a seam already changes or has a second user, join the
   sides with one narrow, stable contract and keep each side's data private. Elsewhere, a plain
   call is enough. (Hourglass model; Amazon services; Fowler citing Ralph Johnson)
5. **Start with a simple thing that works, then grow it.** Build for today's real need; building
   ahead costs build, delay, carry and repair. (Gall's Law; Fowler, YAGNI)
6. **DRY means one home per piece of knowledge**, not per line of text. Copying beats the wrong
   abstraction. When a shared piece grows flags and branches, split it back into its callers.
   (Hunt & Thomas, Tip 15; Metz 2016)
7. **Spend novelty only where it wins.** Default to **boring**, known tools. Keep every design
   close enough to the ground that it solves a real problem. (McKinley; Spolsky 2001)
8. **Sort decisions by door.** Two-way doors go fast. One-way doors get care and a written why.
   Make a door two-way where that is cheap, and leave the rest fixed: flexibility everywhere is
   its own complexity. (Bezos 2015 letter; Fowler 2003)
9. **Define errors out of existence.** Reshape the operation so the edge case is a normal case.
   (Ousterhout)
10. **Fewer decisions, more teaching.** Leave the team able to make the next call without you.
    Write down the why, briefly. (Fowler 2003; Nygard ADRs 2011)

## Two traps for this skill itself

- **Second-system effect** (Brooks): the urge to pile every deferred idea into the new design.
  "What we chose not to build" is where those ideas go.
- **The impressive design** (Spolsky, McKinley): the clever version is usually the costly one.
