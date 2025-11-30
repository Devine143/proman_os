# Hooks & Automation

**Event-triggered automation for PROMAN_OS**

---

## Hook Overview

| Hook | Trigger | Purpose |
|------|---------|---------|
| PreToolUse | Before Write/Edit | Backup critical files |
| PostToolUse | After any tool | Log operations |
| SubagentStop | Agent completes | Track performance |
| Stop | Session closes | Archive logs, clean temp files |
| PreCompact | Before compression | Save state for recovery |

---

## Configuration

Hooks are configured in `settings.json` files:

| Scope | File |
|-------|------|
| Root (CEO) | `/.claude/settings.json` |
| COO Domain | `/COO/.claude/settings.json` |
| CMO Domain | `/CMO/.claude/settings.json` |

**Important:** Claude Code does NOT inherit settings from parent directories. Each domain needs its own `settings.json`.

---

## Hook Technology: Python + uv

All hooks use Python with uv for consistency:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["python-dotenv"]
# ///
```

**Why Python/uv over Bash:**
- Complex logic handled naturally
- Robust error handling with try/except
- Native JSON parsing (hooks receive JSON input)
- Inline dependency declaration
- Easier to maintain

---

## Hook Script Template

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import json
import sys
from pathlib import Path

def main():
    try:
        input_data = json.loads(sys.stdin.read())
        # Hook logic here
        sys.exit(0)
    except Exception:
        sys.exit(0)  # Fail silently to not block Claude

if __name__ == '__main__':
    main()
```

**Shared Utilities:** `/.claude/hooks/utils/`

---

## Adding Hooks to New Domains

1. Create `.claude/hooks/` directory in the domain
2. Copy hook templates from COO or root
3. Configure `settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit|MultiEdit",
      "hooks": [{
        "type": "command",
        "command": "uv run $CLAUDE_PROJECT_DIR/.claude/hooks/pre_tool_use.py"
      }]
    }]
  }
}
```

**Key hooks to implement:**
- `pre_tool_use.py` - Backup critical files before edits
- `pre_compact.py` - Save state before context compression

---

**Version:** 2.0 - Removed Working Memory Integration
**Last Updated:** 2025-11-30
