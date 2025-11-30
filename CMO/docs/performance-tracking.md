# Performance Tracking

**Last Updated:** 2025-11-29

---

## Key Metrics

**Data Location:** `newsletter-preformance/` and `content-strategy-playbook.md`

| Metric | Target | Historical |
|--------|--------|------------|
| Engagement Rate | ≥3.5% | 3.57% |
| Average Views | 4,000+ | 4,937 |
| Conversion Rate | 3-5% | TBD |
| Publishing Cadence | Weekly | Variable |

---

## Historical Performance

**Posts Published:** 22
**Total Views:** 103K+
**Top Performer:** 15,942 views (NotebookLM content)

---

## Performance Analysis Process

### After Each Publish (Wait 7 Days)

1. **Record Metrics:**
   - Total views
   - Likes count
   - Comments count
   - Shares count
   - Time to first 100 views

2. **Calculate Engagement Rate:**
   ```
   Engagement Rate = (Likes + Comments + Shares) / Views × 100
   ```

3. **Run Analysis:**
   - `/update-performance-stats` - Add new data
   - `/performance-analysis` - Identify trends

4. **Update Domain Status:**
   - `/refresh-domain-status`

---

## Pattern Identification

Questions to answer:

- Which learning path performs best?
- What topics drive highest engagement?
- What post length is optimal?
- Which hooks convert best?
- What day/time performs best?

---

## Status Indicators

### Domain Health

- **Green:** Engagement ≥3.5%, publishing on schedule, pipeline has 3+ ideas
- **Yellow:** Engagement 2-3.5% OR pipeline <3 ideas OR behind schedule
- **Red:** Engagement <2% OR significant decline OR no content in pipeline

### Warning Signals

- Engagement rate declining below 3%
- Consecutive posts below 2,000 views
- Comment rate below 0.5%
- Publishing gaps >10 days

---

## Content Performance by Learning Path

Track engagement by category:

| Learning Path | % of Content | Avg Engagement |
|--------------|--------------|----------------|
| AI Workflow Mastery | 44% | Track |
| Tool Mastery | 22% | Track |
| Thinking Mastery | 33% | Track |

---

## Top Performing Content

### Proven Topics

1. **NotebookLM** - Highest view counts
2. **MCP/Claude Integration** - High engagement
3. **Vibe Coding** - Strong interest

### Proven Formats

1. Personal story + framework
2. Step-by-step guides
3. Tool deep dives
4. "How I built..." posts

---

## Optimization Strategies

### When Engagement Drops

1. Return to proven pillars (NotebookLM, MCP, workflows)
2. Increase personal story ratio
3. Test new hooks with `/generate-hook-variants`
4. Shift learning path mix

### When Views Drop

1. Check if topic is saturated
2. Analyze hook quality
3. Compare to high performers
4. Consider timing changes

### When Conversion Drops

1. Strengthen cliffhangers
2. Improve CTAs
3. Test different hook formats
4. Verify links are working

---

## Competitive Benchmarking

### Tracking Process

1. Run `/newsletter-competitive-analyst` monthly
2. Document in `new-post-ideas/competitive-newsletter-analysis/`
3. Identify content gaps
4. Find differentiation opportunities

### Competitors to Monitor

- AI-focused newsletters in productivity space
- Project management content creators
- AI tool reviewers and educators

---

## Reporting

### To CEO Dashboard

Metrics flow to `/daily-briefing` and `/weekly-review`:

- Recent content performance
- Publishing deadlines
- Pipeline status
- Engagement trends

### Domain Status File

`CMO/DOMAIN-STATUS.md` contains:

| Metric | Source | Update Frequency |
|--------|--------|------------------|
| Total Posts | Performance stats | After each publish |
| Total Views | Performance stats | Weekly |
| Average Engagement | Calculated | Weekly |
| Pipeline Depth | File counts | Daily |
| Content Health | Multi-factor | Weekly |

---

## Troubleshooting

### Low Engagement (Multiple Posts)

**Diagnosis:**
1. `/performance-analysis` - Check trends
2. `/topic-saturation-check` - Check overuse
3. `/engagement-hooks` - Review hook quality
4. Compare to high performers

**Fixes:**
1. Return to proven content pillars
2. More personal stories
3. Test new hooks
4. Shift learning path mix

### Domain Status Not Updating

**Fixes:**
1. Run `/refresh-domain-status`
2. Check performance stats are current
3. Verify file permissions
4. Review command execution logs
