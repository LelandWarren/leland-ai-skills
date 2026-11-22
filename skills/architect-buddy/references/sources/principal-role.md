# Principal / staff / architect role: first-party findings (2026-11-21)

Scorecard: 7 guesses. Right 4 (Q2, Q4, Q5, Q6), half 2 (Q1, Q3), wrong/unsupported 1 (Q7).
Method note: Fowler PDF was read in full text locally (extracted from the PDF); other pages via fetch summaries (a small model summarised them, so quotes outside Fowler's PDF are paraphrase-level).

## Q1 Amazon PE Community tenets: HALF RIGHT (list missing one)
- Primary source (Amazon's own tenets page, redirected to atoz.amazon): https://atoz.amazon/en-us/jobs/principal-engineering-community/tenets (also amazon.jobs/en/landing_pages/pe-community-tenets). Lists NINE names, no descriptions on that page.
- Nine tenets (measured, from the page): Exemplary practitioner; Technically fearless; **Lead with empathy**; Balanced and pragmatic; Illuminate and clarify; Flexible in approach; Respect what came before; Learn, educate, and advocate; Have resounding impact.
- Your guess had 8 of 9, correct wording. Missing: "Lead with empathy" (third in order).
- Descriptions of each tenet were not on the page. Fetch the "Learn more" link before quoting a meaning. Worth the effort: "Balanced and pragmatic", "Respect what came before", and "Illuminate and clarify" are the ones closest to "simple, no overengineering".
- Amazon's Well-Architected page describes PEs as "pragmatic visionaries" (https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.pec.en.html).

## Q2 Staff archetypes (Will Larson): RIGHT
- Source: https://staffeng.com/guides/staff-archetypes/
- Four: Tech Lead (guides approach and execution of one team or a cluster), Architect, Solver (digs into hard problems until resolved), Right Hand (extends an exec's attention and authority).
- Architect is "responsible for the direction, quality, and approach within a critical area" (the page's wording, from the fetch summary). Typically a major, complex domain such as API design, storage or cloud infrastructure.
- Effective Architects stay close to business goals, user needs and technical constraints, and use authority earned through consistently good judgment to advocate sound approaches.
- Note: it is a domain-owner role, not a "draws the big diagrams" role.

## Q3 Fowler, "Who Needs an Architect?" (IEEE Software, July/Aug 2003): HALF RIGHT
- Primary: https://martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf (read in full text).
- Definition: architecture is the expert developers' **shared understanding** of the system design (via Ralph Johnson), so it is a social construct: "Architecture is about the important stuff. Whatever that is." Your guess had that part right.
- "Hard to change" is real but it is the second definition: "things that people perceive as hard to change". Also "the decisions that you wish you could get right early".
- On irreversibility, guess is right and sharper than expected: "one of an architect's most important tasks is to remove architecture by finding ways to eliminate irreversibility" (paraphrase, verbatim in the PDF). The example: a DBA made schema changes easy, so the schema stopped being architectural.
- Not in your guess but the most useful for the skill:
  - Two kinds of architect. "Architectus Reloadus" makes all the important decisions (a single mind for conceptual integrity). "Architectus Oryzus" collaborates closely, spots issues early, and mentors.
  - Rule of thumb: an architect's value is inversely proportional to the number of decisions he or she makes. The key activity is mentoring to raise the team's level, so the architect is not a bottleneck.
  - Alternative name: "guide", as in mountaineering.
  - Johnson caution: making everything easy to change makes the whole system very complex. So you pick which things to make flexible.

## Q4 Bezos one-way/two-way doors and Nygard ADRs: RIGHT
- Bezos 2015 shareholder letter. The aboutamazon.com URL 404'd; I used the SEC-hosted exhibit: https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm
  - Type 1: consequential, nearly irreversible, need deliberate, consultative decisions. Type 2: reversible, "made quickly by high judgment individuals or small groups".
  - Extra point: big orgs apply the heavy Type 1 process to Type 2 decisions too, which brings slowness, risk aversion and less invention. (Note: the letter's names are "Type 1" and "Type 2"; "one-way/two-way door" is the letter's metaphor for them.)
- Nygard, 2011: https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions (fetched OK).
  - Sections: Title, Context (forces at play, neutral wording), Decision (active voice), Status (proposed/accepted/deprecated/superseded), Consequences (positive, negative, neutral).
  - Core argument: keep small, versioned decision records so later people avoid blind acceptance and blind reversal. That is also "respect what came before".

## Q5 Reilly, Staff Engineer's Path / Being Glue: RIGHT, with a split
- Book (three parts): big picture, execution, leveling up. Source: https://noidea.dog/staff (author's site; summary says it describes the book's structure rather than a time breakdown). Part I covers chs 1-3, II chs 4-6, III chs 7-9 (O'Reilly TOC via search, secondary).
  - Big picture: org context, vision/strategy, decisions that unblock others. Execution: large ambiguous cross-team projects, plus managing time, energy, influence. Leveling up: mentoring, sponsoring, coaching, delegating, reviews, modelling good practice.
- "Being Glue" is a different claim: https://noidea.dog/glue. Glue work (unblocking, design review, onboarding, standards, alignment) is technical leadership, is often unrewarded, and "if you only do glue, you will only get better at glue" (paraphrase of the page). Its theme is career risk, not the three pillars. Don't merge the two.

## Q6 Narrow waist and the API mandate: RIGHT (one source is secondary)
- Hourglass: Micah Beck, "On the Hourglass Model", CACM 62(7) 2019, arXiv https://www.arxiv.org/abs/1607.07183. The thin waist is a restricted "spanning layer" (IP on the Internet); large bells above and below are the many apps and many lower layers. Correction: sole author is Beck. Not the three-author paper I'd guessed to look for. Reached via search snippets only.
- Bezos mandate (~2002), via Yegge's rant. Secondary repost: https://gist.github.com/chitchcock/1281611 (a copy of the post; I did not reach Yegge's own original).
  - Teams expose data and function through service interfaces only; interaction only through those interfaces; no direct linking, no reading another team's data store, no shared memory; any tech choice per team; interfaces designed to be externalizable; (the post says) non-compliance gets you fired.
  - Reading: a small stable shared contract lets both sides change independently. It is the same idea as Fowler's "remove irreversibility", applied at team boundaries. (Inference, model.)

## Q7 Engineering ladders on simplicity / saying no: WRONG for Principal, partly right for the value
- GitLab Engineering Career Framework, Principal: https://handbook.gitlab.com/handbook/engineering/careers/matrix/principal/ (full page fetched with curl and searched for "boring", "simpl", "complex").
  - No "boring" or "simplicity" wording in the Principal framework. It says: recognize good solutions to complex problems across domains and explain their merits; act as DRI and coach in the Architecture Design Process; "decompose [cross-team complex requirements] into a proposal of small deliverables" (paraphrase); unblock across teams; plan with a roughly 6-month view.
- "Boring solutions" does appear one level up in GitLab's Distinguished Engineer job family: "able to distill complex problems down to actionable items with boring solutions". https://handbook.gitlab.com/job-families/engineering/development/management/distinguished
  - Search snippets also placed "boring solutions" in senior-level and staff-level pages. I did not verify those on the page text (unchecked).
- I did not find Dropbox or Shopify ladder text. Not searched further. Unverified.
- Verdict: GUESS wrong as stated (Principal page lacks it). The value is real but is cited at Distinguished. "Decompose into small deliverables" is the nearest Principal-level match for composability.

## What this means for the skill (design attributes, with the source behind each)
- Remove irreversibility where cheap; accept it where the cost is high (Fowler, Johnson caution).
- Sort every decision into one-way vs two-way before spending effort (Bezos).
- Write down why, briefly (Nygard).
- Own direction and quality of one critical area; stay near the business (Larson).
- Raise the team so you are not the bottleneck; value is inverse to decisions you make (Fowler).
- Narrow, stable interfaces between pieces; hide data stores behind them (hourglass, API mandate).
- Pragmatic, respect what came before, make things clear (Amazon tenets by name only; descriptions not read).
