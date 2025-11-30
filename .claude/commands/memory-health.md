Run a health check on the memory system (WORKING.md task files and docs/learnings/).

Execute: `uv run .claude/hooks/utils/memory_health.py`

Report findings to me and suggest fixes for any issues found.

If there are [UNINDEXED] files, offer to update docs/learnings/README.md.
If there are [STALE] tasks, ask if I want to review and update them.
If there are [MISSING] files, offer to run with --fix flag.
