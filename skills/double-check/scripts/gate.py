#!/usr/bin/env python3
"""PreToolUse gate for the double-check skill.

Blocks an outward post (Slack, Jira, Confluence, GitLab, Gmail, glab/gh MR/PR/issue writes) or a design moment
(ExitPlanMode, first Write of a design/spec/plan file this session) once, so Claude checks
the facts first. The same content passes on retry; changed content is gated once more.

Off switch: touch ~/.claude/double-check/off
Fails open: any error lets the tool call through.
"""
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

HOME = Path(os.environ.get("DOUBLE_CHECK_DIR", str(Path.home() / ".claude" / "double-check")))

POST = re.compile(
    r"^mcp__(?!ccd_).+__("
    r"slack_send_message|slack_send_message_draft|slack_schedule_message|"
    r"slack_create_canvas|slack_update_canvas|"
    r"addCommentToJiraIssue|createJiraIssue|editJiraIssue|"
    r"createConfluencePage|updateConfluencePage|"
    r"createConfluenceFooterComment|createConfluenceInlineComment|"
    r"save_note|save_merge_request|save_merge_request_review|save_work_item|"
    r"send_message|create_draft|update_draft|reply|forward"
    r")$"
)
BASH_POST = re.compile(
    r"\b(glab\s+(mr|issue)\s+(create|note|update|comment)"
    r"|gh\s+(pr|issue)\s+(create|comment|edit|review))\b"
)
DESIGN_NAME = re.compile(r"(^|[-_.\s])(designs?|specs?|plans?)([-_.\s]|$)", re.I)
DESIGN_DIR = re.compile(r"/(specs|plans|designs)/", re.I)
SKIP_DIR = re.compile(r"/(memory|\.git|node_modules)/")

POST_REASON = (
    "double-check gate: this text is about to leave the building. Run the double-check skill "
    "in quiet mode on the facts in it (up to 5). If every fact has a receipt, retry this exact "
    "call unchanged and it will go through. If a fact is wrong or can't be verified, fix or "
    "tag the text, tell the user, then retry (changed text is gated once more)."
)
DESIGN_REASON = (
    "double-check gate: a plan or design is about to go to the user. Run the double-check skill "
    "in quiet mode on the facts it rests on (code, tickets, system behavior; up to 5). Then "
    "retry the same call and it will go through. Fix the design first if a fact is wrong."
)


def classify(tool, inp):
    """Return (key, reason) when this call is gated, else None."""
    if tool == "ExitPlanMode":
        return "plan:" + digest(inp), DESIGN_REASON
    if tool == "Write":
        path = str(inp.get("file_path", ""))
        if SKIP_DIR.search(path) or not path.endswith(".md"):
            return None
        stem = os.path.basename(path)[:-3]
        if DESIGN_NAME.search(stem) or DESIGN_DIR.search(path):
            return "file:" + path, DESIGN_REASON
        return None
    if tool == "Bash":
        if BASH_POST.search(str(inp.get("command", ""))):
            return "post:bash:" + digest(inp), POST_REASON
        return None
    if POST.match(tool):
        return "post:" + tool + ":" + digest(inp), POST_REASON
    return None


def digest(inp):
    return hashlib.sha256(json.dumps(inp, sort_keys=True).encode()).hexdigest()[:20]


def main():
    if (HOME / "off").exists():
        return
    event = json.load(sys.stdin)
    gated = classify(event.get("tool_name", ""), event.get("tool_input") or {})
    if not gated:
        return
    key, reason = gated
    state_dir = HOME / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    sid = re.sub(r"[^A-Za-z0-9_-]", "", str(event.get("session_id") or "none")) or "none"
    state = state_dir / sid
    seen = state.read_text().splitlines() if state.exists() else []
    if key in seen:
        return
    with state.open("a") as f:
        f.write(key + "\n")
    cutoff = time.time() - 7 * 86400
    for old in state_dir.iterdir():
        if old.stat().st_mtime < cutoff:
            old.unlink()
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
