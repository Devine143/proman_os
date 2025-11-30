# Troubleshooting Guide

**Last Updated:** 2025-11-30

---

## System-Wide Issues

### Hooks Not Running

**Symptoms:** Scripts exist but don't execute

**Diagnosis:**
1. Check scripts are executable: `ls -la .claude/hooks/`
2. Validate settings.json syntax: `cat .claude/settings.json | python3 -m json.tool`
3. Check hook logs in `.claude/logs/`

**Fixes:**
```bash
# Make executable
chmod +x .claude/hooks/*.sh

# Validate JSON
cat .claude/settings.json | python3 -m json.tool

# Increase timeout in settings.json
"timeout": 10000  # 10 seconds
```

---

### Agents Not Routing Correctly

**Symptoms:** Agent invocation fails or wrong agent responds

**Diagnosis:**
1. Check agent file exists: `ls .claude/agents/`
2. Verify filename matches invocation
3. Check agent has valid YAML frontmatter

**Fixes:**
```bash
# List all agents
ls .claude/agents/*.md

# Verify frontmatter
head -10 .claude/agents/your-agent.md
```

**Try explicit invocation:** `@agent-name`

---

### Backups Not Created

**Symptoms:** Files edited but no backup in `backups/` directory

**Diagnosis:**
1. Check if file matches critical patterns
2. Verify `pre-tool-backup.sh` is executable
3. Review `.claude/logs/operations.log` for errors

**Critical patterns:**
- `*/projects/*/*.csv`
- `*/05-procurement/*`
- `*/02-planning/*`
- `*_budget*`, `*_cost_model*`, `*_risk_register*`

---

### Logs Growing Too Large

**Symptoms:** Log files exceeding 1MB

**Fixes:**
```bash
# Check sizes
ls -lh .claude/logs/

# Manual rotation
mv .claude/logs/operations.log .claude/logs/operations.log.old
touch .claude/logs/operations.log

# Or truncate
> .claude/logs/operations.log
```

---

## COO Domain Issues

### Files Not Following Naming Standards

**Problem:** Incorrectly named files in project folders

**Standard format:** `[Company_Name]_[Document_Type]_[Date_YYYYMMDD].[ext]`

**Examples:**
```
Correct:
- Weideman_Architects_Drawing_Package_20251128.pdf
- BHR_Quote_HVAC_System_20251120.pdf

Incorrect:
- Drawing Package Nov 28.pdf
- quote.pdf
- BHR Pty Ltd quote.pdf
```

---

### Project Files in Wrong Location

**Problem:** Documents not filed to correct PMP folder

**Rule:** Don't leave files in `00-inbox/` for >24 hours

**Project structure:**
```
00-inbox/       -> Incoming, unprocessed
01-initiation/  -> Feasibility, requirements
02-planning/    -> Fee proposals, program, PM plan
03-design/      -> Design submissions, drawings
04-consultants/ -> Engineer reports
05-procurement/ -> Orders, quotations, LOIs
06-compliance/  -> Approvals, safety, regulations
07-execution/   -> Construction phase docs
08-handover/    -> Completion, snag lists
09-meetings/    -> Minutes, agendas
```

---

## CMO Domain Issues

### Low Engagement on Posts

**Symptoms:** Engagement rate <2% for multiple posts

**Diagnosis:**
1. Run `/performance-analysis` to identify trend
2. Check saturation with `/topic-saturation-check`
3. Review hooks with `/engagement-hooks`

**Fixes:**
1. Return to proven pillars (NotebookLM, MCP, workflows)
2. Increase personal stories
3. Test new hooks with `/generate-hook-variants`
4. Shift learning path mix

---

### Content Pipeline Empty

**Symptoms:** No ideas in `new-post-ideas/`

**Fixes:**
1. Run `/idea-generator` for batch ideation
2. Use `/trend-analysis` for emerging topics
3. Review COO operational learnings for content opportunities
4. Check `brain-dump/` for raw notes

---

### Repurposed Content Not Converting

**Symptoms:** LinkedIn/Notes get views but no Substack traffic

**Fixes:**
1. Strengthen cliffhangers in repurposed content
2. Add clear CTAs to full post
3. Test different hook formats per platform
4. Use `/content-repurpose` with explicit linking strategy

---

## Context Engineering Failure Modes

### Wrong Agent/Skill Invoked

**Symptoms:**
- Output doesn't match request
- Agent uses wrong templates
- Skill applies to different domain

**Root Causes:**
- Ambiguous trigger words
- Missing clarification step
- Overlapping skill descriptions

**Recovery:**
1. Stop current execution
2. Explicitly name correct tool: "Use the `docx` skill specifically"
3. If persistent, check skill YAML headers for conflicting triggers

**Prevention:**
- Use explicit tool names for critical tasks
- Review disambiguation matrix in architecture.md

---

### Context Pollution (Token Overflow)

**Symptoms:**
- Claude "forgets" earlier instructions
- Responses become slower
- Mixing up details between tasks/projects
- Re-reading files already loaded

**Root Causes:**
- Session too long without context pruning
- Loading full files when summaries would suffice
- Not offloading state properly

**Recovery:**
1. Save current state to TodoWrite
2. Explicitly state: "Clearing context. Active task: [X]"
3. Start fresh with minimal context reload

**Prevention:**
- Follow Context Hygiene protocol (see architecture.md)
- Use progressive disclosure - don't load full docs upfront
- Summarize completed work, don't preserve full history

---

### Skill Execution Drift

**Symptoms:**
- Output deviates from template
- Steps skipped or reordered
- Custom additions not requested

**Root Causes:**
- Skill SKILL.md too vague
- Missing concrete examples in skill
- Context from other tasks bleeding in

**Recovery:**
1. Re-invoke skill explicitly
2. Reference specific template: "Use exactly the format in templates/loi-template.docx"
3. If persistent, skill needs refinement

**Prevention:**
- Keep skills focused (one job, done well)
- Include concrete examples in skill knowledge/
- Test skills in isolation before production use

---

### Cross-Domain Confusion

**Symptoms:**
- COO output in CMO style (or vice versa)
- Filing to wrong domain folders
- Using wrong naming conventions

**Root Causes:**
- Ambiguous request didn't specify domain
- Task genuinely spans both domains
- Previous task context bleeding over

**Recovery:**
1. Clarify domain: "This is COO operations work"
2. Re-file any misplaced outputs
3. If cross-domain, explicitly hand off: "COO portion complete. Switching to CMO."

**Prevention:**
- Always confirm domain for ambiguous requests
- Use domain-specific triggers ("AI LOI" for COO, "newsletter" for CMO)
- Clear context between domain switches

---

### Stale Context (Outdated Information)

**Symptoms:**
- Decisions based on old data
- Missing recent updates
- Contradicting current state

**Root Causes:**
- Relying on loaded context instead of re-reading
- Not re-reading files before acting
- Carrying old state in context

**Recovery:**
1. Re-read current state files: PROJECT_STATUS.md, relevant project files
2. Check file modification dates
3. Refresh context with fresh data

**Prevention:**
- Re-read relevant files at session start
- Check modification dates on critical files
- Don't trust context older than 24 hours for operational data

---

## Maintenance Tasks

### Weekly
- Review `logs/operations.log` for errors
- Check backup disk usage: `du -sh .claude/backups/`

### Monthly
- Archive old logs
- Review subagent-activity.log for patterns
- Clean up old state snapshots if needed
- Audit backup retention

### Quarterly
- Review and update agent documentation
- Optimize hook performance
- Archive session-history.log
- Update CLAUDE.md files with new learnings

---

## Escalation Path

1. **Domain issues** -> Domain CLAUDE.md
2. **Cross-domain issues** -> Root CLAUDE.md
3. **Technical issues** -> Claude Code documentation
4. **Business decisions** -> CEO (Donovan)

---

## Log Locations

| Log | Purpose |
|-----|---------|
| `.claude/logs/operations.log` | All tool usage |
| `.claude/logs/subagent-activity.log` | Agent executions |
| `.claude/logs/session-history.log` | Session lifecycle |
| `COO/logs/[session-id]/` | COO session logs |
