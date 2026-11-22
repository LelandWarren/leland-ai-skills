"""Run: python3 -m unittest ~/.claude/skills/double-check/scripts/test_gate.py"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

GATE = Path(__file__).with_name("gate.py")


def run(tool, inp, home, sid="s1"):
    out = subprocess.run(
        [sys.executable, str(GATE)],
        input=json.dumps({"tool_name": tool, "tool_input": inp, "session_id": sid}),
        capture_output=True, text=True, env={**os.environ, "DOUBLE_CHECK_DIR": home},
    )
    assert out.returncode == 0, out.stderr
    return json.loads(out.stdout)["hookSpecificOutput"]["permissionDecision"] if out.stdout.strip() else "allow"


class GateTest(unittest.TestCase):
    def setUp(self):
        self.home = tempfile.mkdtemp()

    def test_post_blocked_once_then_passes(self):
        inp = {"channel_id": "C1", "message": "PROJ-1 is closed"}
        tool = "mcp__28747af6__slack_send_message_draft"
        self.assertEqual(run(tool, inp, self.home), "deny")
        self.assertEqual(run(tool, inp, self.home), "allow")

    def test_changed_text_gated_again(self):
        tool = "mcp__abc__addCommentToJiraIssue"
        self.assertEqual(run(tool, {"body": "a"}, self.home), "deny")
        self.assertEqual(run(tool, {"body": "b"}, self.home), "deny")

    def test_new_session_gated_again(self):
        tool = "mcp__abc__save_note"
        self.assertEqual(run(tool, {"body": "a"}, self.home, "s1"), "deny")
        self.assertEqual(run(tool, {"body": "a"}, self.home, "s2"), "deny")

    def test_gmail_and_gitlab_and_confluence(self):
        for t in ["mcp__5b82__send_message", "mcp__5b82__create_draft", "mcp__f7d9__save_merge_request",
                  "mcp__dc40__updateConfluencePage"]:
            self.assertEqual(run(t, {"x": 1}, self.home), "deny", t)

    def test_not_gated(self):
        for t in ["mcp__ccd_session_mgmt__send_message", "mcp__28747af6__slack_read_channel",
                  "mcp__dc40__getJiraIssue", "Edit", "TodoWrite"]:
            self.assertEqual(run(t, {"x": 1}, self.home), "allow", t)

    def test_bash_posts(self):
        for c in ['glab mr note 12 -m "PROJ-1 is closed"', 'cd repo && glab mr create --fill',
                  'glab mr update 5 --description x', 'gh pr comment 3 -b hi', 'gh issue create -t t']:
            self.assertEqual(run("Bash", {"command": c}, self.home), "deny", c)
            self.assertEqual(run("Bash", {"command": c}, self.home), "allow", c)

    def test_bash_not_gated(self):
        for c in ["glab mr view 12", "git log --oneline", "gh pr list", "ls -la"]:
            self.assertEqual(run("Bash", {"command": c}, self.home), "allow", c)

    def test_bash_mention_is_gated_on_purpose(self):
        # Text match, not a shell parse: a command that only mentions "glab mr note" is gated
        # once too. Rare, and costs one block, so simplicity wins.
        self.assertEqual(run("Bash", {"command": "git commit -m 'run glab mr note'"}, self.home), "deny")

    def test_design_files(self):
        for p in ["/w/double-check-design.md", "/w/docs/specs/thing.md", "/w/PLAN.md",
                  "/w/2026-11-21-gap-spec.md", "/w/plans/x.md"]:
            self.assertEqual(run("Write", {"file_path": p, "content": "c"}, self.home), "deny", p)
            self.assertEqual(run("Write", {"file_path": p, "content": "changed"}, self.home), "allow", p)

    def test_non_design_files(self):
        for p in ["/w/explanation.md", "/w/planning-notes.txt", "/w/README.md", "/w/spec.py",
                  "/u/.claude/projects/x/memory/plan.md"]:
            self.assertEqual(run("Write", {"file_path": p, "content": "c"}, self.home), "allow", p)

    def test_exit_plan_mode(self):
        self.assertEqual(run("ExitPlanMode", {"plan": "p"}, self.home), "deny")
        self.assertEqual(run("ExitPlanMode", {"plan": "p"}, self.home), "allow")

    def test_off_switch(self):
        Path(self.home, "off").touch()
        self.assertEqual(run("ExitPlanMode", {"plan": "p"}, self.home), "allow")

    def test_bad_input_fails_open(self):
        out = subprocess.run([sys.executable, str(GATE)], input="not json", capture_output=True,
                             text=True, env={**os.environ, "DOUBLE_CHECK_DIR": self.home})
        self.assertEqual((out.returncode, out.stdout), (0, ""))


if __name__ == "__main__":
    unittest.main()
