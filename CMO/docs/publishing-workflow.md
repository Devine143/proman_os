# Publishing Workflow

**Last Updated:** 2025-11-29

---

## Content Pipeline Overview

```
Ideation → Outlining → Drafting → Editing → Publishing → Repurposing → Tracking
```

---

## Step 1: Ideation

**Commands:**
- `/idea-generator` - Batch generate new topics
- `/trend-analysis` - Identify emerging AI trends
- `/angle-generator` - Find unique content angles

**Storage:**
- `new-post-ideas/free-post-ideas/` - Free tier ideas
- `new-post-ideas/paid-post-ideas/` - Premium ideas

**Best Practices:**
- Maintain 10+ ideas in pipeline at all times
- Batch ideation sessions weekly
- Categorize by learning path (Workflow/Tool/Thinking)
- Check COO domain for operational content opportunities

---

## Step 2: Outlining

**Commands:**
- `/free-post-outline` - Structure free tier post
- `/paid-post-blueprint` - Create premium guide outline

**Validation:**
- `/topic-saturation-check` - Ensure topic isn't overused
- `/perspective-analysis` - Confirm unique angle

**Structure:**
1. Hook
2. Failure Patterns
3. Framework
4. Implementation
5. Next Steps

---

## Step 3: Drafting

**Location:** `newsletter-drafts/free/` or `newsletter-drafts/paid/`

**Process:**
1. Create draft in appropriate folder
2. Follow structure patterns
3. Embed image prompts using HTML comments
4. Read voice guidelines: `.claude/output-styles/ai-pm-voice`

**Image Prompt Format:**
```markdown
<!-- IMAGE: [description of where image goes]
PROMPT: [Full prompt for Gemini Nano Banana]
-->
```

**Image Locations:**
- Hero image (opening)
- Section breaks
- Concept illustrations
- Call-to-action visual

---

## Step 4: Editing

**Commands:**
- `/analyze-draft` - Comprehensive review
- `/quick-edit` - Minor polish
- `/engagement-hooks` - Check hook quality
- `/generate-hook-variants` - Create A/B test options

**Quality Checklist:**
- [ ] Hook is compelling
- [ ] Follows structure pattern
- [ ] Voice matches guidelines
- [ ] Images embedded properly
- [ ] CTA is clear
- [ ] No topic saturation issues

---

## Step 5: SEO & Optimization

**Commands:**
- `/seo-optimize` - Improve discoverability
- `/social-preview` - Generate sharing preview

**Pre-Publish Checks:**
- Title optimized for search
- Meta description compelling
- Internal links to related content
- External links where valuable

---

## Step 6: Publishing

**Actions:**
1. Move from `newsletter-drafts/` to `newsletter-archive/`
2. Publish to Substack
3. Generate supporting content

**Post-Publish Commands:**
- `/newsletter-to-linkedin` - Create LinkedIn post
- `/generate-notes` - Create Substack Notes
- `/newsletter-to-twitter-thread` - Create Twitter thread (optional)

**Output Locations:**
- LinkedIn: `linkedin-posts/daily-linkedin-posts/`
- Notes: `substack-notes/daily-notes-generation/`
- Threads: `twitter-threads/`

---

## Step 7: Performance Tracking

**Timeline:** Wait 7 days for metrics to stabilize

**Commands:**
- `/update-performance-stats` - Record new metrics
- `/performance-analysis` - Identify trends
- `/refresh-domain-status` - Update DOMAIN-STATUS.md

**Metrics to Record:**
- Total views
- Likes count
- Comments count
- Shares count
- Time to first 100 views

**Engagement Rate:**
```
(Likes + Comments + Shares) / Views × 100
```

---

## File Naming Conventions

### Newsletter Archive
Format: Descriptive, hyphenated names
```
ai-environment.md
vibe-coding-guide.md
atomic-habit-ai-system.md
```

### LinkedIn Posts
Format: `linkedin-post-YYYY-MM-DD-HHMM.md`
```
linkedin-post-2025-11-28-0930.md
```

### Substack Notes
Format: `substack-notes-YYYY-MM-DD.md`
```
substack-notes-2025-11-28.md
```

---

## Pipeline Health Indicators

| Indicator | Healthy | Warning | Critical |
|-----------|---------|---------|----------|
| Ideas in Pipeline | 10+ | 5-9 | <5 |
| Drafts in Progress | 2-3 | 1 | 0 |
| Publishing Cadence | Weekly | Bi-weekly | >14 days |
| Completion Rate | >80% | 60-79% | <60% |

---

## Content Repurposing Rules

1. **Every newsletter should generate:**
   - 1 LinkedIn post
   - 3-5 Substack Notes
   - Optional Twitter thread for high performers

2. **Platform Optimization:**
   - Don't just copy-paste
   - Maintain consistent voice
   - Optimize for each platform's algorithm

3. **Linking Strategy:**
   - Always link back to original Substack post
   - Use cliffhangers to drive traffic
   - Clear CTAs in repurposed content

---

## Command Quick Reference

### Creation
| Command | Purpose |
|---------|---------|
| `/newsletter-post` | Interactive post creation |
| `/free-post-outline` | Free tier structure |
| `/paid-post-blueprint` | Premium guide outline |
| `/quick-note-to-post` | Rapid development |

### Analysis
| Command | Purpose |
|---------|---------|
| `/analyze-draft` | Comprehensive review |
| `/topic-saturation-check` | Overuse detection |
| `/performance-analysis` | Trend identification |

### Repurposing
| Command | Purpose |
|---------|---------|
| `/newsletter-to-linkedin` | LinkedIn conversion |
| `/generate-notes` | Substack Notes |
| `/newsletter-to-twitter-thread` | Twitter threads |
