# Common Errors & Fixes
> Last updated: 2025-11-30

## Claude Code Errors

### PostToolUse:Read Hook Error
**Symptom:** Hook fails silently or throws error on file read
**Cause:** Usually path issues or missing session directory
**Fix:** Check `logs/` directory exists, verify session_id extraction

### rm -rf Blocked Unexpectedly
**Symptom:** Legitimate deletion blocked by pre_tool_use hook
**Cause:** Path not in ALLOWED_RM_DIRECTORIES
**Fix:** Add directory to whitelist in `pre_tool_use.py` or use manual deletion

### Subagent Not Finding Files
**Symptom:** Task agent can't locate files that exist
**Cause:** Working directory context not passed correctly
**Fix:** Use absolute paths in agent prompts, or specify cwd explicitly

## Documentation Errors

### CLAUDE.md References Non-Existent Paths
**Symptom:** Docs mention folders/files that don't exist
**Cause:** Structure changed without updating docs
**Fix:** Run docs-auditor skill: "audit documentation"

### Agent Count Mismatch
**Symptom:** CLAUDE.md says "5 agents" but different number exists
**Cause:** Agents added/removed without doc update
**Fix:** Count actual `.md` files in `.claude/agents/` and update docs

## Publishing Errors

### Newsletter Missing CTA
**Symptom:** Low conversion from free readers
**Cause:** Forgot call-to-action at end of post
**Fix:** Always end with clear next step for reader

### LinkedIn Post Too Long
**Symptom:** Post truncated or engagement drops
**Cause:** Direct copy from newsletter without adaptation
**Fix:** Use `/newsletter-to-linkedin` which reformats appropriately

## Project Management Errors

### Sensitive Info in Client Report
**Symptom:** Internal notes visible to client
**Cause:** Copy-paste from internal docs
**Fix:** Always use "Draft first, CEO review before send" rule

### Budget Numbers Don't Match
**Symptom:** Report shows different figures than source docs
**Cause:** Stale data or calculation errors
**Fix:** Always pull from single source of truth, verify before finalizing

## Prevention Checklist

- [ ] Run docs-auditor after major structural changes
- [ ] CEO review on all client-facing output
- [ ] Use absolute paths in agent prompts
- [ ] Test hooks after settings.json changes
