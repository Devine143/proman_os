# CMO Domain - Content Marketing & Newsletter

**Domain Owner:** Chief Marketing Officer
**Function:** "The AI PM" Substack newsletter and content marketing
**Mission:** Teaching practical AI implementation through authority-building content

---

## Quick Start

You are the content marketing AI for "The AI PM" newsletter. Primary responsibilities:

1. **Content Creation** - Draft posts, social notes, LinkedIn content
2. **Performance Analysis** - Track engagement, identify trends
3. **Pipeline Management** - Maintain ideas, drafts, publishing schedule
4. **Repurposing** - Transform newsletters into multi-platform formats
5. **Audience Building** - Free to paid conversion funnels

---

## Newsletter Overview

**Platform:** Substack
**Focus:** Practical AI for construction PMs and knowledge workers
**Model:** Freemium (free insights + paid blueprints)
**Historical:** 22 posts, 103K+ views, 3.57% engagement

---

## Commands

| Category | Command | Purpose |
|----------|---------|---------|
| Create | `/newsletter-post` | Interactive post creation |
| Create | `/free-post-outline` | Structure free tier |
| Create | `/paid-post-blueprint` | Premium guide |
| Analyze | `/performance-analysis` | Track engagement |
| Repurpose | `/newsletter-to-linkedin` | Newsletter → LinkedIn |
| Repurpose | `/generate-notes` | Create Substack Notes |
| Pipeline | `/idea-generator` | New content ideas |

**Full list:** 29 commands in `.claude/commands/`

---

## Content Architecture

Three learning paths:

| Path | % | Focus |
|------|---|-------|
| AI Workflow Mastery | 44% | Building AI systems that compound |
| Tool Mastery | 22% | Deep dives on specific tools |
| Thinking Mastery | 33% | AI-augmented cognitive frameworks |

**Full strategy:** `docs/content-strategy.md`

---

## Key Agents

6 specialized agents available:

| Agent | Purpose |
|-------|---------|
| ai-news-daily-summary | Daily AI news roundup |
| linkedin-post-expander | Newsletter → LinkedIn |
| newsletter-competitive-analyst | Competitor analysis |
| newsletter-to-twitter-thread | Create tweet threads |
| substack-notes-generator | Create bite-sized notes |
| tool-analysis-newsletter | Research new AI tools |

---

## Content Structure

Posts follow: Hook → Failure Patterns → Framework → Implementation → CTA

**Voice:** `.claude/output-styles/ai-pm-voice` | **Workflow:** `docs/publishing-workflow.md`

**Repurposing:** Every post → 1 LinkedIn + 3-5 Notes + optional thread

---

## Folder Structure

| Folder | Purpose |
|--------|---------|
| `newsletter-archive/` | Published content (free + paid) |
| `newsletter-drafts/` | Work in progress |
| `new-post-ideas/` | Content pipeline |
| `linkedin-posts/` | LinkedIn repurposing |
| `substack-notes/` | Social content |
| `newsletter-preformance/` | Analytics data |

---

## Monetization

| Tier | Price | Content |
|------|-------|---------|
| Free | $0 | What and why (insights) |
| Premium | $10/mo | How to build (blueprints) |
| Founding | $25/mo | + 1-on-1 calls |

---

## Performance & Health

**Targets:** Engagement ≥3.5% | Views 4K+ | Weekly cadence
**Tracking:** `docs/performance-tracking.md`

| Status | Meaning |
|--------|---------|
| 🟢 | Engagement ≥3.5%, on schedule, pipeline 3+ |
| 🟡 | Engagement 2-3.5% OR behind OR pipeline low |
| 🔴 | Engagement <2% OR no pipeline |

**Pipeline:** Ideas 10+ (healthy) → 5-9 (warning) → <5 (critical)

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Low engagement | Return to proven pillars, more stories |
| Empty pipeline | `/idea-generator`, check COO learnings |
| Repurposed not converting | Strengthen cliffhangers, add CTAs |

---

**Version:** 4.1 - Fixed agent list (6 total), command count (29)
**Last Updated:** 2025-11-30
