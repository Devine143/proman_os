# .claude/ Directory - System Configuration

Core configuration for PROMAN_OS automation and agents.

---

## Directory Structure

```
.claude/
├── agents/           # 5 cross-domain agents
├── skills/           # Shared skills (2: meta-skill, docs-auditor)
├── hooks/            # Automation scripts (10)
├── settings.json     # Main configuration
└── settings.local.json
```

---

## Agents

| Agent | Purpose |
|-------|---------|
| codebase-documenter | Auto-document codebases |
| meta-agent | Generate new agent configs |
| project-curator | Reorganize project structure |
| trend-researcher | Market research |
| workflow-optimizer | Process improvement |

---

## Skills

| Skill | Purpose | Triggers |
|-------|---------|----------|
| meta-skill | Template for creating new skills | "create skill", "new skill template" |
| docs-auditor | Audit docs against actual structure | "audit documentation", "check docs accuracy", "sync docs" |

---

## Hooks

| Hook File | Trigger | Purpose |
|-----------|---------|---------|
| pre_tool_use.py | Before Write/Edit | Backup critical files |
| post_tool_use.py | After any tool | Audit trail |
| subagent_stop.py | Agent completes | Track performance |
| session_end.py | SessionEnd | Clean temp files |
| pre_compact.py | PreCompact | Preserve state |
| notification.py | Various | Event notifications |
| user_prompt_submit.py | User submits | Prompt handling |
| send_event.py | Various | Send custom events |
| stop.py | Stop event | Handle stop signals |
| test_hitl.py | Testing | Human-in-the-loop testing |

---

## Configuration

**Main config:** `settings.json`
**Local overrides:** `settings.local.json`

---

## Full Documentation

- System architecture: `../docs/architecture.md`
- Troubleshooting: `../docs/troubleshooting.md`

---

**Version:** 3.3 - Removed non-existent folders and commands from docs
**Last Updated:** 2025-11-30
