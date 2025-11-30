# Newsletter Creation Workflow
> Last updated: 2025-11-30

## Overview

Weekly newsletter for "The AI PM" Substack - practical AI for construction PMs and knowledge workers.

## Pre-Flight Checks

1. Check `CMO/brain-dump/` for raw content ideas
2. Review `CMO/content-strategy-playbook.md` for current themes
3. Check pipeline in `CMO/new-post-ideas/` for scheduled topics

## Steps

### 1. Content Selection
- Pick topic from pipeline or brain-dump
- Ensure it fits one of three pillars:
  - AI Workflow Mastery (44%)
  - Tool Mastery (22%)
  - Thinking Mastery (33%)

### 2. Drafting
- Create draft in `CMO/newsletter-drafts/`
- Follow structure: Hook -> Failure Patterns -> Framework -> Implementation -> CTA
- Use `/newsletter-post` command for guided creation

### 3. Voice & Style
- Check `CMO/.claude/output-styles/ai-pm-voice` for brand voice
- Keep paragraphs short (3-4 sentences max)
- Include one "operational insight" from real work

### 4. Review
- Apply formatting from `CMO/newsletter-archive/` examples
- Verify CTA is present and compelling
- Check free vs paid tier appropriateness

### 5. Repurposing Pipeline
After publishing:
- Use `/newsletter-to-linkedin` for LinkedIn post
- Use `/generate-notes` for 3-5 Substack Notes
- Consider Twitter thread if topic warrants

## Tools Used

| Tool | Purpose |
|------|---------|
| `/newsletter-post` | Guided creation |
| `/free-post-outline` | Structure free tier |
| `/paid-post-blueprint` | Premium guides |
| `/newsletter-to-linkedin` | Repurpose |

## Common Pitfalls

- Don't forget CTA at end
- Keep paragraphs short
- Always include operational insight
- Don't mix free insights with paid blueprints in same post

## Related

- `decisions/content-strategy.md` - Why we structure content this way
- `gotchas/common-errors.md` - Publishing mistakes to avoid
