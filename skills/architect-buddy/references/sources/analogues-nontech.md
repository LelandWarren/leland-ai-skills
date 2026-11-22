# Non-tech analogues for a simplicity-first architect skill

Tags: measured = read from a source this session; derived = arithmetic on measured; model; guess. "secondary" = book/press/summary. "(unchecked)" = from memory, not read this session.
Reading limits: nejm.org, pubmed, iso.org and lockheedmartin.com blocked fetches (403/cookie wall). Primary pages were NOT read directly; numbers below come from the Harvard Gazette (secondary, press office of the study's authors), search snippets, and Wikipedia. Each is flagged.

## Worth-it note
This is background evidence for a design choice (encode taste as a skill), not a build costing. No build is costed here.

## 1. WHO Surgical Safety Checklist (2008-09) -- family 1: write down expert judgment
- Who/when: WHO "Safe Surgery Saves Lives" expert panel led by Atul Gawande; pilot Oct 2007-Sep 2008; Haynes et al., NEJM 2009.
- Problem: Surgical outcomes varied by team; experts' habits (confirm patient, site, antibiotics, instrument counts) were not applied consistently.
- What they did: one-page checklist used at three pauses: before anesthesia, before incision, before patient leaves the OR. Items are short and every team runs the same ones.
- Outcome:
  - 8 hospitals in 8 cities (Seattle, Toronto, London, Auckland, Amman, New Delhi, Manila, Ifakara) [measured, secondary: Harvard Gazette]
  - 7,688 patients: 3,733 before, 3,955 after [measured, secondary]
  - Major complications 11% -> 7% [measured, secondary] (relative drop ~36% [derived])
  - Inpatient deaths after major operations 1.5% -> 0.8% [measured, secondary] (relative drop ~47% [derived])
  - Gawande team's US savings estimate $15-25 billion a year [model, secondary; not our concern]
- Where it breaks for us:
  - Their checklist is binary, closed-ended, and run by a whole team at fixed pauses. Our skill is open-ended advice: "is this simple enough" has no yes/no item.
  - Their gain was measured against patient outcomes. We have no outcome metric for "advice felt simpler".
  - The study was before-and-after with no control group, so the gain is partly confounded (unchecked, from memory of the paper's stated limitation).
  - Lesson that transfers: short, run at set decision points (before design, before build), not a long essay.
- Sources: https://news.harvard.edu/gazette/story/2009/01/surgical-safety-checklist-drops-deaths-and-complications-by-more-than-one-third/ (secondary, read) ; https://pubmed.ncbi.nlm.nih.gov/19144931/ (primary, blocked, not read; NEJM DOI 10.1056/NEJMsa0810119)

## 2. Shipping container standard, ISO 668 (1968) -- family 2: standard interface so parts fit later
- Who/when: Malcolm McLean (Ideal-X, 1956); ISO series 1 sizes in the 1960s; ISO 668 first published 1968.
- Problem: Each port, line and railroad had its own box; cargo was loaded piece by piece and could not move between ships, trucks and trains.
- What they did: Fixed the corner fittings, widths and length classes so any box fits any compatible ship, crane, truck or rail car. ISO 668 gives only the external dimensions and ratings; the detailed internals live in a separate standard, ISO 1496. The standard has since been amended, not replaced: 45-foot boxes added 2005; max gross mass raised to 36,000 kg for all sizes except 10-foot in 2016 [measured, Wikipedia citing ISO amendments].
- Outcome:
  - ISO 668 first published 1968; 7th edition January 2020 [measured, ANSI blog/ISO listing]
  - Loading cost for conventional cargo about $5.83 per ton vs about 15.8 cents per ton for the 1956 Ideal-X loading [measured, secondary: Levinson, "The Box", as relayed in search results; baselines vary by source, $5+ to ~$8 per ton] (about 97% lower [derived])
  - Note: that cost fall came from containerization, not from the ISO standard alone; the standard's own outcome is that the 1968 interface still governs 50+ years later [derived from 1968 and 2020 dates].
- Where it breaks for us:
  - Their standard fixes physical interfaces among many independent parties who never meet. We are one person plus an agent; there is no second party to interoperate with, so the cost of a wrong interface is our own refactor, not a global recall.
  - The standard fights fragmentation by consensus among shipping lines (a political process); ours is a taste file.
  - Lesson that transfers: freeze the small interface, let the insides vary, and extend by amendment rather than break old pieces.
- Sources: https://blog.ansi.org/ansi/series-1-freight-containers-iso-668-2020/ (secondary, from search) ; https://en.wikipedia.org/wiki/ISO_668 (secondary, read) ; https://www.iso.org/standard/76912.html (primary, blocked, not read) ; Levinson, The Box (2006), via https://pubsonline.informs.org/do/10.1287/orms.2006.04.08/full/ (blocked; figures only seen in search results)
- LEGO 1958 patent not researched: no primary patent text was read, so it is not claimed here.

## 3. Lockheed Skunk Works, Kelly Johnson's 14 rules (1943, formalized early 1950s) -- family 3: complexity creep
- Who/when: Kelly Johnson, Lockheed; rules begun on the XP-80 in 1943, formalized early 1950s [secondary summary of Lockheed text].
- Problem: Large programs grew in headcount, paperwork and approvals; aircraft schedules and costs slipped.
- What they did: 14 rules that cap size and process: one manager with near-total control (rule 1); a small group of highly capable people (3); a simple drawing and release system that still handles changes (4); minimal reports but thorough records of important work (5); monthly cost reviews so there are no overrun surprises (6); no duplicated inspections (8); reward not tied to number of people supervised (14).
- Outcome:
  - U-2: Johnson promised first flight in 8 months; the first aircraft was delivered for test July 29, 1955, 9 months after contract [measured, Lockheed history page via search result; page itself blocked]
  - Team of 26 in the special projects engineering group after the Dec 9, 1954 go-ahead [measured, CIA article via search result]
  - Small-staff rule: "10% to 25% of the size of a normal program" [measured, secondary summary; exact wording varies by source]
  - No independent measure of cost or quality vs comparable programs was found. Outcome evidence is mostly Lockheed's own account (self-reported).
- Where it breaks for us:
  - Johnson's rules work through authority and secrecy (one boss, walled-off team, customer trust). We have one person and an agent, so "small team" is already true and does not constrain anything.
  - The rules attack headcount and reports, not design shape. Our habits are about code design; the rules only transfer in spirit (cut process, keep records short).
  - Self-reported, survivorship: we hear about the programs that worked.
  - Lesson that transfers: rules were few (14), plain, and each named a thing to NOT add.
- Sources: https://lib.fo.am/skunkworks (secondary, read; paraphrases Lockheed text) ; https://www.lockheedmartin.com/en-us/news/features/history/u2.html (primary, blocked; seen via search snippet) ; https://www.cia.gov/stories/story/ask-molly-what-really-went-on-at-area-51/ (CIA, seen via search snippet only)

## What this says for the skill (measured facts only)
- The two best-evidenced analogues (checklist, container) both won by being short and fixed at the interface or pause point, not by encoding all of the experts' judgment.
- Only the checklist has a published before/after outcome with counts; none of the three tests "advice quality" the way we would need.
- Not found: any non-tech case measuring consistency of open-ended design advice. The closest (Alexander's Pattern Language, 1977) was not researched and has no outcome measure known to me (unchecked).

## Decisions for the user
- Whether to treat these as support or as color only. Recommendation: color only; none are tested on a one-person plus AI setup.
- Whether to chase primary sources (NEJM full text via a different route, ISO 668 text, Lockheed page) before citing numbers outside this note. Recommendation: yes, if numbers go into the skill itself.
