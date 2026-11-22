# Simplicity canon: research notes (2026-11-21)
Scorecard: 7 guesses right, 2 half right, 0 wrong.
Source note: pages were read through a summarizing fetch tool, so wording is the tool's paraphrase unless in quotes. Three PDFs (Brooks, Parnas x2) came back as binary and could not be read directly; I used HTML copies instead. No numbers below are measured unless tagged.

## Q1 Hickey, Simple Made Easy (2011): GUESS RIGHT
Source (talk transcript): https://github.com/matthiasn/talk-transcripts/blob/master/Hickey_Rich/SimpleMadeEasy.md
- Simple = "sim" + "plex", one fold/braid/twist: no interleaving of concerns. Complex = folded/braided together.
- Easy = near at hand: obtainable/installable, familiar, within our capabilities. Relative: easy or hard "for someone".
- Simplicity is objective (you can inspect a system for interleaving); ease is relative.
- Complect = archaic word he revives: interleave, entwine, braid. Complecting is the source of complexity.
- Quote: "simplicity is a choice"

## Q2 Ousterhout, A Philosophy of Software Design: GUESS RIGHT
Sources: author's CS190 lecture page https://web.stanford.edu/~ouster/cgi-bin/cs190-winter18/lecture.php?topic=complexity ; Talks at Google transcript https://rosetta.to/u/talksatgoogle/a-philosophy-of-software-design-john-ousterhout-talks-at-google (transcript site, secondary host of his talk); book page https://web.stanford.edu/~ouster/cgi-bin/book.php (only describes 2nd-edition changes, e.g. Ch.6 "General-Purpose Modules are Deeper").
- Complexity = anything about a system's structure that makes it hard to develop (other summaries: "understand and modify"). What matters is "apparent complexity", what a developer experiences, not size.
- Causes: dependencies and obscurity. Symptoms: change amplification, cognitive load, unknown unknowns.
- Deep module = simple interface, lots of functionality beneath (his favorite: UNIX file I/O, five core calls). Shallow = interface nearly as big as the work done; "class-itis" of many tiny classes.
- Tactical = get the feature working fast, small shortcuts that pile up. Strategic = good design is the goal; invest about 10-20% of dev time in design (guess: he says he has no hard data).
- Define errors out of existence = redefine the operation so the error case is not an error. Examples: Tcl unset of a missing variable, UNIX delete of an open file, Java substring returning the overlap.

## Q3 DRY (Hunt & Thomas): GUESS RIGHT
Sources: https://pragprog.com/tips/ (Tip 15, p.31) ; https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/ ; Changelog interview, https://changelog.com/podcast/352 (via search snippet only, not opened).
- Wording: "single, unambiguous, authoritative representation within a system" (Tip 15).
- 20th-anniversary book blurb: "Avoid the trap of duplicating knowledge"; section titled "DRY: The Evils of Duplication".
- Per the Changelog snippet, Dave Thomas says DRY came to mean "don't cut and paste" but the original was about knowledge, not code. (Interview not opened: unchecked beyond snippet.)

## Q4 Sandi Metz, The Wrong Abstraction: GUESS RIGHT
Source: https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction
- "duplication is far cheaper than the wrong abstraction".
- Decay path: extract duplication; new need almost fits; add parameter + conditional; repeat until tangled. Sunk-cost thinking keeps people preserving it.
- Recovery: inline the shared code back into each caller, keep only the branch each caller uses, delete the rest. Re-extract later from real current needs.

## Q5 Gall's Law: GUESS RIGHT (second half unverified in this run)
Source: https://en.wikipedia.org/wiki/Gall%27s_law (secondary; book is Systemantics, 1975 as General Systemantics, retitled 1977, p.71 cited)
- Wording: "A complex system that works is invariably found to have evolved from a simple system that worked."
- The "designed from scratch never works" clause is the usual second sentence of the law; the fetch returned only the first sentence (unchecked here).

## Q6 KISS, YAGNI, Rule of Three: HALF RIGHT
- KISS: credited to Kelly Johnson, Lockheed Skunk Works. Story: he gave engineers a basic tool kit and required the jet be field-repairable by an average mechanic with only those tools. Source (secondary): https://en.wikipedia.org/wiki/KISS_principle . Note: "Keep it Short and Simple" appears in a 1938 newspaper.
- YAGNI: HALF WRONG on attribution. Fowler credits Kent Beck and Chet Hendrickson on the C3 project (Beck answering "you aren't going to need it" to each listed capability); his page does not mention Jeffries. Source: https://martinfowler.com/bliki/Yagni.html . Jeffries wrote it up on his site: "Always implement things when you actually need them." https://ronjeffries.com/xprog/articles/practices/pracnotneed/
- Fowler's four costs of building ahead: build, delay, carry (extra complexity), repair (when the guess was wrong).
- Rule of Three: popularized by Fowler in Refactoring, attributed to Don Roberts: first time just do it; third time you refactor. Only secondary sources found (Wikipedia, Goodreads note); the "three strikes" baseball phrasing is a popular paraphrase, not confirmed in the book. https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)

## Q7 Brooks: GUESS RIGHT
Sources: No Silver Bullet HTML copy https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet ; second-system via search snippets of Wisconsin quotes page https://pages.cs.wisc.edu/~param/quotes/man-month.html (not opened).
- Essence = difficulties inherent in software's conceptual structure; accidents = difficulties of today's production, not inherent. Complexity is essential: parts rarely repeat, elements interact nonlinearly, so complexity grows faster than size.
- Quote: "The complexity of software is an essential property, not an accidental one."
- Second system: "most dangerous system a man ever designs"; tendency to over-design with all the frills sidetracked on the first. Example: IBM 709 after the 704, about half its operations regularly used.

## Q8 Anti-patterns: GUESS RIGHT
- Spolsky, Architecture Astronauts (2001): https://www.joelonsoftware.com/2001/04/21/dont-let-architecture-astronauts-scare-you/ . Thinkers who abstract until the idea loses practical meaning; Napster's value was search, not P2P design. Quote: "you run out of oxygen".
- McKinley, Choose Boring Technology: https://boringtechnology.club/ . Roughly three innovation tokens early in a company's life (his rough estimate, a guess-level figure). Spend them on what differentiates the business; boring tech keeps tokens free; new tools carry ongoing operational cost.

## Q9 Unix philosophy and Parnas
- McIlroy foreword (BSTJ 1978): HALF RIGHT. Maxims: "Make each program do one thing well." and expect each program's output to become another program's input. The foreword does NOT use the phrase "text streams"; it warns against stringently columnar or binary input formats. Source: https://archive.org/stream/bstj57-6-1899/bstj57-6-1899_djvu.txt . (Foreword co-authored by McIlroy, Pinson, Tague.) "Text streams" is a later paraphrase.
- Parnas 1972: RIGHT. Modules should hide design decisions likely to change; decomposing by flowchart steps is "almost always incorrect". Hidden-decision modules may cost extra cross-module calls. Source read: Morning Paper summary quoting the paper, https://blog.acolyer.org/2016/09/05/on-the-criteria-to-be-used-in-decomposing-systems-into-modules/ (secondary). Primary PDFs (cse.sc.edu, wstomv.win.tue.nl) could not be text-extracted.

## Gaps
- Primary text not read directly: Parnas, Brooks PDF, Gall's second sentence, Fowler's Rule of Three, Jeffries tie to Beck, Dave Thomas interview.
