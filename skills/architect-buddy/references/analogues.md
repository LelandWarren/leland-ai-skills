# Principal-architect skill: analogues (2026-11-21)

Builds on `research.md`. Helper reports with full sources:
`sources/analogues-tech.md`, `sources/analogues-nontech.md`.

## 1. Verdict: change

Keep the 10 habits, but **not as the skill's main mechanism**. Every analogue pairs its written
rules with a *forcing step*: a budget stated first, a fixed pause, a template, a default of "no".
A list of 10 good habits with no forcing step is the one shape no analogue used.

So the skill should be:
- **3–4 forced questions at fixed pauses**, asked before any design. (Checklist, Shape Up, Etsy)
- **One fixed output template** that always ends with "what we chose not to build". (code-architect
  template, code-simplifier don't-list, Skunk Works rules that name what not to add)
- **A default answer of "don't build" or "use what we have".** (Shape Up circuit breaker, Etsy gate)
- **The 10 habits as a reference file** the skill checks its design against, not a lecture.

Do-nothing baseline: keep the research note as a personal checklist. Cheapest option: a short
skill with the forced questions and the template, about 1 page. The analogues favor the cheap
option. Nothing here says a big multi-agent skill would do better.

Driven by: Shape Up appetite, Etsy boring tech, WHO surgical checklist, Anthropic's two agent
prompts.

Evidence warning: no analogue measured "consistent design advice". Only the surgical checklist
has before/after counts, and those came through a secondary source. Treat the verdict as
pattern-matching across cases, not proof.

## 2. Gaps and complements

No skill exists yet, so gaps are checked against the planned design in the research note.

| # | Gap in our plan | Where | Analogue behind it | Cheapest fix |
|---|---|---|---|---|
| G1 | Habits list has no forcing step | research note, Bottom line | All 8 (rule + mechanism every time) | Open the skill with fixed questions, asked every time |
| G2 | 10 habits is long for the moment of use | research note, Bottom line | WHO checklist (short, at pauses); Skunk Works (few plain rules) | 3–4 questions in the skill body; habits move to `references/` |
| G3 | Habit 4 ("narrow contract between parts") can be over-applied | research note, habit 4 | Amazon services (contracts pay with many teams); Fowler/Johnson caution | Reword: add a contract only at a seam that already changes or has a second user |
| G4 | No budget asked up front | research note, D3 | Shape Up appetite; Etsy innovation tokens | First question: "How much is this worth? Hours, days, a week?" |
| G5 | No "why can't what we have do it?" gate | research note, D3 | Etsy (write down why the current stack can't) | Second question, before any new piece is proposed |

Complements (cheap extras analogues pair with the main idea):
- **One-way or two-way door?** as the third question. Already in habit 8, just promote it. (Bezos)
- **Extend, don't break.** Add to an interface by amendment, keep old pieces fitting. (ISO 668,
  changed by amendment since 1968)
- **Exempt throwaway work.** Spikes and one-off scripts skip the ritual. (Google readability
  exempts short-lived code)

Skipped on purpose: Thoughtworks-style status rings with expiry dates, and Google-style checkers.
Both need an org or tooling. Revisit if the skill grows.

## 3. Comparison table

| Who | Family | Fit, and where it breaks | Evidence | Cost to adopt | Lesson |
|---|---|---|---|---|---|
| Etsy, Choose Boring Technology (2015) | Complexity creep | Close. Breaks: it guards a shared on-call budget; we guard one person's attention | One author anecdote (20x scale, no data) | Tiny: one question | Make every new piece justify itself in writing |
| Basecamp, Shape Up appetite | Complexity creep | Close. Breaks: needs a betting table to say no; an agent feels no time pressure | No outcome published, case stories only | Tiny: one question | State the budget before the design |
| Google, readability (SWE at Google ch. 3) | Write down judgment | Medium. Breaks: needs certified human reviewers | Internal study: faster review, no effect size | High for full copy; low for "rules in a list, judgment short" | Checkable rules go in a list; keep judgment brief |
| Thoughtworks Tech Radar | Write down judgment | Medium. Breaks: a panel twice a year, not an agent per task | Survived 35 volumes; no outcome data | Medium | Advice goes stale; date it (skipped for now) |
| Amazon services behind interfaces (1998) | Standard interface | Medium. Breaks: protects many teams; we own every piece | No measured outcome in the source | Low as a wording fix | Contracts only at seams that really change |
| Anthropic `code-simplifier` agent (cousin) | Same stack | Close stack, other lane: cleans code after it is written | None published | Low: borrow its don't-list | A short "don't" list keeps an agent from clever code |
| Anthropic `code-architect` agent (cousin) | Same stack | Close stack, opposite goal: aims for complete blueprints | None published | Low: borrow its fixed template | A fixed output template makes the advice repeatable |
| WHO Surgical Safety Checklist (2009) | Write down judgment | Medium. Breaks: yes/no items; "simple enough?" is not yes/no | Complications 11%→7%, deaths 1.5%→0.8% (measured, secondary; no control group) | Low | Short, fixed pause points beat long guidance |
| ISO 668 shipping container (1968) | Standard interface | Loose. Breaks: many parties who never meet; we are one | Interface still in force 50+ years on (derived); cost fall is containerization overall (secondary) | Nil | Freeze the small interface, let insides vary, extend by amendment |
| Skunk Works 14 rules (1943–50s) | Complexity creep | Loose. Breaks: works through authority on teams, not design shape | Lockheed's own account (U-2 in about 9 months) | Nil | Few plain rules, each naming what not to add |

## 4. Framing

- **Our problem:** turn the user's "smarter, not harder" taste into a skill that gives the same
  simplicity-first advice every time.
- **Our solution:** a principal-architect skill built on the 10 habits.
- **Artifact:** none yet. Checked against the planned design in the research note.
- **Our stack:** a Claude Code skill (a Markdown prompt an AI agent follows).
- **Families:** write down an expert's judgment; standard interface so parts fit later;
  complexity creep.

## 5–6. Analogue detail

Full detail per analogue (who, when, what they did, outcome, break, sources) is in
`sources/analogues-tech.md` and `sources/analogues-nontech.md`.

Non-tech source note: nejm.org, pubmed, iso.org and lockheedmartin.com blocked the helper. All
non-tech numbers are tagged secondary. I did not rerun on a stronger model: the blocks are on the
sites, so a rerun would hit the same walls. The LEGO brick patent was not researched.

## 7. Sources

- https://mcfunley.com/choose-boring-technology
- https://basecamp.com/shapeup/1.2-chapter-03
- https://abseil.io/resources/swe-book/html/ch03.html
- https://www.thoughtworks.com/radar/faq
- https://www.allthingsdistributed.com/2022/11/amazon-1998-distributed-computing-manifesto.html
- https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-simplifier/agents/code-simplifier.md
- https://github.com/anthropics/claude-plugins-official/blob/main/plugins/feature-dev/agents/code-architect.md
- https://news.harvard.edu/gazette/story/2009/01/surgical-safety-checklist-drops-deaths-and-complications-by-more-than-one-third/ (secondary)
- https://en.wikipedia.org/wiki/ISO_668 (secondary)
- https://lib.fo.am/skunkworks (secondary)
