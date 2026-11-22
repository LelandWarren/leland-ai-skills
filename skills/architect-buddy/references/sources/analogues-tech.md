# Tech analogues: encoding simplicity taste (5 analogues + 2 same-stack cousins)

Number tags: measured (read from source), derived, model, guess. All pages read 2026-11-21 via WebFetch (summaries by a small model, not raw text; quotes not verified verbatim).
Honest headline: none of the five publishes a controlled outcome for "same advice every time". The best evidence is Google readability (an internal study, no figures) and Etsy's one 20x anecdote.

## Bottom line (measured facts only)
- Every analogue is a written rule plus a forcing mechanism (a token budget, a time box, a certified reviewer, a ring placement, an interface-only rule). The written rule alone is never the mechanism.
- Only Google reports a measured direction (certified authors' changes review and submit faster), and no figures are given.
- All five rely on an org: a reviewer, a board, a team. Ours is one person plus an AI agent, so only the forcing mechanisms transfer, not the social enforcement.

## Analogue 1. Etsy, "Choose Boring Technology" (Dan McKinley, 2015-03-30)
- Family: 3, complexity creep.
- Problem: teams adopt new tech too readily; each new tool adds operational burden and unknown failure modes.
- What they did: a budget of about 3 "innovation tokens" (model; McKinley's stated heuristic, not a measurement). Each unproven choice spends one. Before adding tech, write down why the current stack can't do it. Adoption is a team-wide conversation with a migration plan for overlapping old tools.
- Outcome: Etsy's activity feeds on PHP/MySQL/Memcached/Gearman scaled about 20x with no targeted work (measured as stated by the author; anecdote, no data shown). Early-years unnecessary Python work and ~2 minute p90 search latency (measured as stated; no data shown). No broader data published. Author says "boring" is a bias, not a rule (Etsy adopted Solr).
- Where it breaks: it spends a shared company budget of operational burden. A solo dev has no on-call rotation to protect; the cost is their own attention and the agent's context. The token count is a model, so use "a small fixed budget", not "3".
- Source: https://mcfunley.com/choose-boring-technology

## Analogue 2. Basecamp/37signals, Shape Up "appetite" (Ryan Singer, book; undated page, copyright 1999-2026)
- Family: 3, complexity creep.
- Problem: estimates start from a design and grow; scope creeps.
- What they did: set the time you are willing to spend first (appetite), then shape the design to fit. Fixed time, variable scope. Default is cancel, not extend (circuit breaker, per glossary). Big batch = 6 weeks (measured, defined by the book); small batch = 1-2 weeks (measured, defined); team of 1 designer + 1-2 programmers (measured, defined).
- Outcome: no aggregate outcome published. Only case stories: the archive warning replaced a permissions system as a one-day change (measured as stated); Files 2.0 was split and its two parts shipped (qualitative).
- Where it breaks: appetite works because a betting table says "no" to ideas. With one person plus an agent there is no one to cancel the project, and the agent does not feel time pressure. The transferable part is "state the appetite as the first question, before design".
- Source: https://basecamp.com/shapeup/1.2-chapter-03

## Analogue 3. Google, readability certification (Software Engineering at Google, ch. 3, Knowledge Sharing)
- Family: 1, write down an expert's judgment.
- Problem: spread language best practices and taste across a huge codebase consistently.
- What they did: mandatory code review; each change needs approval from someone certified in the language (readability). Certification is earned when an author's changes draw consistently fewer comments. Style guides and static analysis hold the checkable rules. About 1-2% of engineers are reviewers (measured); about 20% of engineers participate at any time (measured). Canonical docs need named owners.
- Outcome: internal research team found certified authors' changes take statistically significantly less time to review and submit (measured; no effect size published). Certified engineers self-report higher satisfaction with code quality (measured, self-reported). Costs the book names: heavyweight, scales linearly with headcount, some call it bureaucracy. Short-lived code is exempt.
- Where it breaks: the mechanism is people who earn and award a stamp. We have one reviewer (the user) and a prompt. The cheap transfer: put checkable rules in a checker or a list, and keep the judgment part short. Exempt throwaway code explicitly.
- Source: https://abseil.io/resources/swe-book/html/ch03.html

## Analogue 4. Thoughtworks Technology Radar (Technology Advisory Board, since about 2010)
- Family: 1, write down an expert's judgment.
- Problem: tell many teams what the senior group currently thinks of techniques and tools, without a rigid approved list.
- What they did: about 18 senior people (measured) meet twice a year (measured), debate nominations from client projects, place each as Adopt / Trial / Assess / Caution across 4 quadrants. A champion writes each entry. Entries expire after one edition unless they move. Trial requires production experience.
- Outcome: no outcome published; no adoption data. The FAQ says it is not an approved list, not comprehensive, and archived entries go stale. Volume 35 is current (measured), so it has run for years.
- Where it breaks: it is advice with an expiry, produced by a panel. Ours must be applied automatically by an agent. Transferable: a ring or status label per rule, a date, and a note that old advice goes stale. The evidence is that the format survived, not that it worked.
- Source: https://www.thoughtworks.com/radar/faq

## Analogue 5. Amazon, services behind interfaces only (1998 manifesto; Vogels 2022 write-up; Vogels/Gray 2006 interview)
- Family: 2, standard interface so parts fit later.
- Problem: applications reached the database directly, so a schema change meant app changes. Shared databases bottlenecked innovation.
- What they did: three tiers; clients reach data only through defined service interfaces that hide data model and location. The design target was 10x order volume (model/target, not a result).
- Outcome: no measured outcome in the manifesto. The 2022 article says Amazon moved from monolith to services to microservices over about two decades (stated, qualitative). The 2006 interview page returned 403, so I did not verify its numbers. The popular "API mandate" email is a secondary account and I did not use it.
- Where it breaks: interface-only rules protect many teams from each other. One person owns every piece. A narrow contract pays only where a second consumer or a later change is real (YAGNI). Use contracts at the seams that already change, not everywhere.
- Source: https://www.allthingsdistributed.com/2022/11/amazon-1998-distributed-computing-manifesto.html ; interview (unread, 403): https://queue.acm.org/detail.cfm?id=1142065

## Supporting note: Software Engineering at Google, ch. 15 (Deprecation)
Code is a liability, not an asset (stated claim). No quantitative results in the chapter (measured: none). Advisory deprecation "slightly fewer new uses"; compulsory needs a deadline and owner. Source: https://abseil.io/resources/swe-book/html/ch15.html
Not read: GitLab "boring solutions" value (page text was too long and the section was not reached), so it is not used.

## Same-stack cousins (AI-agent prompts)

### Cousin A. Anthropic `code-simplifier` agent (claude-plugins-official, plugin code-simplifier)
- Defaults: model opus; no tools listed in the frontmatter; scope is recently modified code only; runs autonomously and proactively.
- Mechanism: 5 principles (preserve functionality; apply CLAUDE.md project standards; enhance clarity; maintain balance, no over-simplifying; focus scope) and a 6-step process ending in "verify simplicity" and "document significant changes".
- Extras: a "don't" list (no clever code, no merged concerns, no removing helpful abstractions, no dense one-liners/nested ternaries). No forced questions. No rubric.
- Outcome: no outcome published.
- Source: https://github.com/anthropics/claude-plugins-official/blob/main/plugins/code-simplifier/agents/code-simplifier.md
- Contrast: it cleans after the fact on existing code. Ours advises before building. It has no "what not to build" list and no ask-first step.

### Cousin B. Anthropic `code-architect` agent (feature-dev plugin)
- Defaults: model sonnet; read/search tools only (Glob, Grep, LS, Read, NotebookRead, WebFetch, TodoWrite, WebSearch, KillShell, BashOutput); "pick one approach and commit".
- Mechanism: 3 steps (find existing patterns with file:line, design, blueprint) and 7 fixed output sections (patterns found, decision with trade-offs, components, implementation map, data flow, build sequence, critical details).
- Extras: fixed output template; no explicit simplicity guidance, no forced questions, no rubric. (I could not read the feature-dev command, so I do not know whether it asks clarifying questions upstream.)
- Outcome: no outcome published.
- Source: https://github.com/anthropics/claude-plugins-official/blob/main/plugins/feature-dev/agents/code-architect.md
- Contrast: it optimizes for completeness ("every file") and decisiveness, the opposite of "build less". A fixed output template is the cheap extra worth borrowing for same-advice-every-time, plus a "do not build" section.

## Cheap extras the analogues pair with the main mechanism (borrow list)
1. A budget stated first (Etsy tokens, Shape Up appetite).
2. A "write down why the current thing can't do it" gate (Etsy).
3. A default of cancel/no (Shape Up circuit breaker).
4. Checkable rules in a checker, judgment in prose (Google).
5. Status ring plus date, so advice expires (Thoughtworks).
6. A fixed output template (code-architect) and a don't list (code-simplifier).

## Ask a human
- Does the user want pre-build advice only, or also a post-build simplify pass (cousin A's lane)? Who: the user.

## Decisions for the user
- Which extras to add on top of the 10 habits. Recommendation: items 1, 2 and 6 (budget question first, "why can't the current thing do it" gate, fixed output with a "do not build" section); skip the ring/expiry for now.
- Worth-it gate: this is a personal skill, so the frequency and saving per group are unknown. Nothing here measures them. Cheapest option is a short skill with 3 questions and a template; do-nothing is a valid answer.
