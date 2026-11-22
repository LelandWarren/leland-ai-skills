# Skills

Claude Code skills for reviewing designs and code, thinking through decisions, and writing
clearly. Each folder under `skills/` is one skill: a `SKILL.md` plus any references or scripts it
reads.

## Install

Copy (or symlink) the skills you want into `~/.claude/skills/`:

```bash
git clone <this repo> ~/src/skills
ln -s ~/src/skills/skills/eli5 ~/.claude/skills/eli5
```

Most skills are explicit-invocation lenses: type `/<name>` or use one of the trigger phrases in its
description.

## The skills

### Review and judgment
| Skill | What it does |
|---|---|
| `pr-review` | End-to-end GitLab MR review: triage, teach-back, a lens catalog, parallel blind reviewers, steel-man/straw-man, a cold judge, and kind draft comments. |
| `arch-review` | Architecture review of an MR or proposal: blind designers solve the problem first, then lens reviewers, adversaries and a cold judge rule. |
| `adversarial` | Puts one claim on trial: a prosecutor, a defender, then a judge with a binary verdict. |
| `double-check` | Fact-checks claims against receipts. Includes an optional PreToolUse gate hook (`scripts/gate.py`) that pauses before outward posts and plans. |
| `understanding-before-building` | Grounds an assigned ticket in its real context and contracts before any design. |

### Design and decisions
| Skill | What it does |
|---|---|
| `architect-buddy` | A calm principal architect: four questions first, use what exists, always says what it cut. |
| `analogues` | Names the classic problem under yours and checks your solution against how others solved it. |
| `macro-system-architect` | A five-vector lens for amorphous, stalled or organizational problems. |
| `least-regret` | Judges a hard choice from six months out, with a pre-mortem and a recorded prediction. |
| `write-ticket` | Turns notes into a Jira ticket where every line is sourced or marked as an ask. |

### Explaining and writing
| Skill | What it does |
|---|---|
| `eli5` | Explains from zero without talking down. |
| `slow-teach` | Teaches one tiny piece per turn, with a quick check each time. |
| `worked-example` | Explains through one tiny example that changes a step at a time. |
| `draw` | Turns the last explanation into a diagram, walked through box by box. |
| `writing-plainly` | Base clarity lens for MR descriptions, docs and messages. |
| `grade6` | Rewrites prose to a 6th-grade reading level without changing meaning. |
| `warmer` | Makes a draft shorter and kinder without softening the verdict. |
| `unslop` | Strips the tells that make text read as machine-written. |

The writing lenses stack: content first (`writing-plainly`, `eli5`, `grade6`), tone last
(`warmer`, `unslop`).

## Plugin

`plugins/token-meter` shows how full the context window is in the status line. Its type stubs are
written by Claude Code when it loads the plugin, so they are not checked in.

## Notes

- Some skills mention GitLab (`glab`), Jira or Slack because that is where they were built. The
  methods carry over to GitHub and other trackers with small edits.
- Tests: `python3 -m unittest skills/double-check/scripts/test_gate.py`.

## License

Public domain, under the Unlicense. See `LICENSE`.
