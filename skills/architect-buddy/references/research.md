# What a canonical principal architect is like (research, 2026-11-21)

Purpose: input to a new principal-architect helper skill. Its job is to see a problem and make it
"smarter, not harder": simple, lego-like pieces, KISS and DRY, no overengineering, still robust.

Helper reports (full text, sources, quotes): `sources/simplicity-canon.md` and
`sources/principal-role.md`. Several pages were read through a summarizing fetch tool,
so wording outside quotes is paraphrase.

## Bottom line

The sources agree on one picture. A principal architect removes complexity. They do not add
cleverness. Ten habits come out of the canon, each with an owner:

1. **Split essential from accidental complexity.** Keep what the problem itself needs. Cut what our
   tools and choices added. (Brooks, No Silver Bullet)
2. **Untangle before you simplify.** Simple means "not braided together", which you can check.
   Easy means "familiar", which is relative. Look for concerns woven into each other. (Hickey)
3. **Deep pieces, small doors.** A good module has a small interface and lots of work behind it.
   Hide the decisions most likely to change. This is what makes lego pieces. (Ousterhout; Parnas 1972)
4. **One narrow, stable contract between parts.** A thin shared waist lets both sides change on
   their own. Never reach into another part's data. (Hourglass model, Beck 2019; Bezos API mandate,
   secondary)
5. **Start with a simple thing that works, then grow it.** Big designs from scratch fail. Don't
   build ahead: building early costs build, delay, carry and repair. (Gall's Law; Fowler, YAGNI)
6. **DRY means one home per piece of knowledge, not per line of text.** Copying is cheaper than the
   wrong abstraction. When a shared piece grows flags and branches, split it back out. (Hunt &
   Thomas, Tip 15; Metz 2016)
7. **Spend novelty only where it wins.** Default to boring, known tools. Beware the architect who
   abstracts until nothing real is left. (McKinley; Spolsky 2001)
8. **Sort decisions by door.** Reversible ones go fast. Irreversible ones get care. Make things
   reversible where it is cheap, but not everything: making all of it flexible makes it complex.
   (Bezos 2015 letter; Fowler 2003, citing Ralph Johnson)
9. **Define errors out of existence.** Reshape the operation so the edge case is not an error.
   (Ousterhout)
10. **Fewer decisions, more teaching.** An architect's value is inverse to the number of decisions
    they make. They raise the team so they are not the bottleneck. They write down *why*, briefly.
    (Fowler 2003, "Architectus Oryzus"; Nygard ADRs 2011)

Amazon's Principal Engineering tenets point the same way by name: "Balanced and pragmatic",
"Respect what came before", "Illuminate and clarify". The page lists names only, so their meanings
are unread.

Two warnings for the skill itself:
- **Second-system effect** (Brooks): the designer of a second system piles in every deferred idea.
  A skill that "improves" designs can do exactly this.
- **Impressive is a smell.** Spolsky's astronaut and McKinley's innovation tokens both say the
  clever design is usually the costly one.

## Facts found

| # | Question | Answer (short) | Source | Tag | My guess |
|---|---|---|---|---|---|
| F1 | Do existing skills already do this? | `arch-review` grades a proposal (fit, failure, time) with blind designers. `macro-system-architect` frames org and project problems (Johnson, Rickover, Marshall, von Neumann). Neither *generates* the simplest design. | `~/.claude/skills/arch-review/SKILL.md`, `~/.claude/skills/macro-system-architect/SKILL.md` | measured | Right |
| F2 | Hickey: simple vs easy, complect | Simple = one braid, objective. Easy = near at hand, relative. Complect = braid concerns together. | talk transcript | measured | Right |
| F3 | Ousterhout: complexity, deep modules | Complexity = what makes a system hard to work on. Causes: dependencies, obscurity. Deep = small interface, much function. Strategic beats tactical. | Stanford CS190 page; Google talk | measured | Right |
| F4 | DRY: code or knowledge? | Knowledge. "single, unambiguous, authoritative representation". | pragprog.com Tip 15 | measured | Right |
| F5 | Metz, wrong abstraction | Duplication is cheaper. Recover by inlining back to callers. | sandimetz.com 2016 | measured | Right |
| F6 | Gall's Law | Working complex systems evolve from simple working ones. Second sentence not read. | Wikipedia (secondary) | secondary | Right |
| F7 | KISS, YAGNI, Rule of Three | KISS: Kelly Johnson. YAGNI: Fowler credits Beck and Hendrickson, not Jeffries. Rule of Three: Don Roberts via Fowler (secondary only). | martinfowler.com/bliki/Yagni | measured / secondary | Half right |
| F8 | Brooks: essence vs accident, second system | As guessed. | No Silver Bullet copy | measured | Right |
| F9 | Spolsky, McKinley | Astronauts lose touch with real problems. About 3 innovation tokens early on (McKinley's own rough figure, **guess**). | joelonsoftware.com; boringtechnology.club | measured | Right |
| F10 | McIlroy, Parnas | "Do one thing well", output feeds the next program. No "text streams" in the 1978 foreword. Parnas: hide decisions likely to change. | BSTJ 1978 on archive.org; Parnas via Morning Paper (secondary) | measured / secondary | Half right |
| F11 | Amazon PE tenets | Nine, not eight. I missed "Lead with empathy". Names only on the page. | atoz.amazon tenets page | measured | Half right |
| F12 | Larson archetypes | Tech Lead, Architect, Solver, Right Hand. Architect owns direction and quality of a critical area. | staffeng.com | measured | Right |
| F13 | Fowler, Who Needs an Architect | Architecture = "the important stuff, whatever that is". Second definition: things perceived hard to change. Key job: remove irreversibility. Value inverse to decisions made. | martinfowler.com PDF (full text) | measured | Half right |
| F14 | Bezos doors, Nygard ADRs | Type 1 / Type 2 as guessed. ADR = title, context, decision, status, consequences. | SEC copy of 2015 letter; cognitect.com 2011 | measured | Right |
| F15 | Reilly | Three parts: big picture, execution, leveling up. "Being Glue" is a separate career-risk talk. | noidea.dog | measured | Right |
| F16 | Narrow waist, API mandate | Hourglass: thin spanning layer. Mandate: service interfaces only. Mandate text from a repost. | arXiv 1607.07183; gist repost (secondary) | measured / secondary | Right |
| F17 | Ladders on simplicity | GitLab Principal page has no "boring" wording. "Boring solutions" is in the Distinguished family. Nearest Principal line: break complex needs into small deliverables. | handbook.gitlab.com | measured | Wrong |

Score: 11 right, 5 half right, 1 wrong. No miss moves the bottom line.

Not read at the primary source: Parnas and Brooks PDFs, Gall's second sentence, Rule of Three
wording, Yegge's original post, Amazon tenet descriptions.

## Ask a human

- **H1. Who is your real exemplar?** Is there a person whose designs you
  want this skill to sound like? Ask: The user. No source knows their taste.
- **H2. When will you reach for it?** Shaping a fresh solution, simplifying an existing design, or
  pre-review before `arch-review`? And roughly how often a week? Ask: The user. This sets whether it
  is worth building (see D1).
- **H3. Our boring defaults.** Which tools count as "boring" here (Postgres, SQS, Spring
  Boot, Terraform…)? Ask: The user or the platform team. Needed so "choose boring" points at
  real defaults. (unchecked)

## Decisions for the user

- **D1. New skill, or extend one?** Options: (a) new generative skill that hands off to
  `arch-review` for grading; (b) add a "simplify mode" to `arch-review`; (c) don't build, keep this
  note as a checklist. Recommend (a). `arch-review` judges a design. This skill would make one.
  ⚠️ Rests on: H2 (how often you'd use it), unchecked. Ask the user. Run the worth-it gate before
  designing.
- **D2. Name.** Avoid `simplify`: a built-in skill already uses it. Recommend `principal` or
  `kiss-architect`.
- **D3. Output shape.** Options: a fixed checklist of the 10 habits, or questions it asks first,
  then a proposed shape. Recommend questions first, then one simple design plus "what we chose
  not to build".
