# Phase 3: CMO Memory System Implementation

**Location:** `/Users/donovan/PROMAN_OS/CMO/memories/`

---

## Memory → Agent/Skill Promotion Pipeline

Memories are **workflow candidates**. Track usage, and promote to agents/skills when validated.

```
Document workflow → Use 5+ times → 80%+ success → Promote
```

### Tracking Fields (in every memory file)

```markdown
**Content type:** [Free/Paid/LinkedIn/Notes]
**Last used:** [Date]
**Use count:** [N] ← increment each use
**Success rate:** [High/Medium/Low]
**Promotion status:** Memory | Candidate | Promoted to @agent-name
```

### CMO Promotion Examples

| Memory | After 5+ uses, promote to |
|--------|---------------------------|
| `free-post-patterns.md` | `@newsletter-drafter` agent |
| `newsletter-to-linkedin.md` | Already: `@linkedin-post-expander` |
| `hook-formulas.md` | `skill:hook-generator` |
| `engagement-patterns.md` | `@content-analyst` agent |

### Monthly Review

Check `memories/` for promotion candidates:
```bash
grep -r "Use count:" memories/ | sort -t: -k2 -rn
```

---

## Directory Structure to Create

```
CMO/memories/
├── README.md
├── content-creation/
│   ├── free-post-patterns.md
│   ├── paid-blueprint-patterns.md
│   └── hook-formulas.md
├── repurposing/
│   ├── newsletter-to-linkedin.md
│   └── substack-notes.md
├── performance/
│   ├── engagement-patterns.md
│   └── pillar-balance.md
└── pipeline/
    └── coo-to-content.md
```

---

## Files to Create

### 1. `CMO/memories/README.md`

```markdown
# CMO Workflow Memory

Search here FIRST before any content task.

## Quick Index

| Content Type | Search First |
|--------------|--------------|
| Free tier post | `content-creation/free-post-patterns.md` |
| Paid guide | `content-creation/paid-blueprint-patterns.md` |
| Strong hook | `content-creation/hook-formulas.md` |
| LinkedIn post | `repurposing/newsletter-to-linkedin.md` |
| Substack Note | `repurposing/substack-notes.md` |
| Low engagement fix | `performance/engagement-patterns.md` |
| Pillar balance | `performance/pillar-balance.md` |
| Content ideas | `pipeline/coo-to-content.md` |

## ALWAYS Check First

**Before ANY content task:**
```bash
# Check for COO-sourced content opportunities
cat ../memories/domain-handoffs/content-opportunities.md

# Then search CMO memories
grep -ri "[keyword]" memories/
```

## How to Search

```bash
# All CMO memories
grep -ri "[keyword]" memories/

# By category
grep -ri "[keyword]" memories/content-creation/
grep -ri "[keyword]" memories/repurposing/
grep -ri "[keyword]" memories/performance/
grep -ri "[keyword]" memories/pipeline/
```

## Execution Loop (CMO)

1. **CHECK FLYWHEEL** - Search `../memories/domain-handoffs/content-opportunities.md`
2. **SEARCH** - Check this folder for relevant patterns
3. **DECIDE** - Use existing pattern OR plan new
4. **EXECUTE** - Follow steps, maintain voice
5. **CAPTURE** - Update memory with engagement data
6. **TRACK** - Log to `../memories/flywheel/complete-cycles.md` if from COO

## Related Resources

- Agents: @linkedin-post-expander, @substack-notes-generator
- Commands: /newsletter-post, /free-post-outline, /newsletter-to-linkedin
- Voice guide: `.claude/output-styles/ai-pm-voice`
```

---

### 2. `CMO/memories/content-creation/free-post-patterns.md`

```markdown
# Free Tier Post Patterns

**Content type:** Free (What + Why insights)
**Engagement target:** 3.5%+
**Last used:** [Date]

---

## Purpose

Free tier posts build awareness and demonstrate expertise. They provide valuable insights WITHOUT step-by-step implementation (save that for paid).

**Goal:** Demonstrate expertise, create curiosity for paid tier.

---

## Prerequisites

- [ ] Topic from pipeline (check `../pipeline/coo-to-content.md`)
- [ ] Topic saturation checked (not overdone)
- [ ] Pillar assigned (AI Workflow 44% / Tool 22% / Thinking 33%)
- [ ] Unique angle identified

---

## Steps

### 1. Source the Insight (15 min)

**First, check flywheel:**
```bash
cat ../../memories/domain-handoffs/content-opportunities.md
```

If COO insight available → Use it (higher engagement historically)
If not → Use `pipeline/coo-to-content.md` or `/topic-saturation-check`

### 2. Structure (MANDATORY FORMAT)

```
HOOK (100-150 words)
├── Near-miss story, surprising stat, or bold claim
├── Create curiosity
└── Promise value

FAILURE PATTERN (200-300 words)
├── Why current approach fails
├── Relatable struggle
└── Build problem awareness

FRAMEWORK (400-500 words)
├── The insight or principle (What + Why)
├── NOT step-by-step How (save for paid)
└── Actionable concept they can apply

IMPLEMENTATION TEASE (100-150 words)
├── Hint at how to build
├── Create desire for paid content
└── Show what's possible

CTA (50-100 words)
├── Subscribe for paid tier
├── Or link to related free content
└── Clear next action
```

### 3. Draft (60-90 min)

**Command:** `/free-post-outline` for structure
**Voice:** Check `../.claude/output-styles/ai-pm-voice`

Key voice elements:
- **Practical:** No theory without application
- **Specific:** "Saved R47K" not "saved money"
- **Honest:** Share failures and near-misses
- **Energetic:** Short sentences, active voice

### 4. Edit (30-45 min)

**Commands:**
- `/analyze-draft` - Structure check
- `/engagement-hooks` - Hook alternatives
- `/generate-hook-variants` - A/B options

**Checklist:**
- [ ] Hook creates curiosity (would I keep reading?)
- [ ] Structure followed exactly
- [ ] Voice matches AI PM
- [ ] Real numbers included
- [ ] CTA clear

### 5. Publish

- Move to `newsletter-archive/`
- Publish to Substack
- Update status in content-opportunities.md if COO-sourced

---

## High-Performing Examples

### 4.2% Engagement
**Title:** "The R47,000 Mistake I Almost Made (And How AI Caught It First)"
**Pillar:** AI Workflow Mastery
**COO source:** Budget variance alert from Arowana
**What worked:** Real number (R47K), near-miss story, clear AI application

### 4.0% Engagement
**Title:** "Why Your PM Tool Isn't the Problem (Your Workflow Is)"
**Pillar:** Thinking Mastery
**What worked:** Challenged common belief, framework for evaluation

### 2.8% Engagement (Lower)
**Title:** "The Future of AI in Construction PM"
**Pillar:** Tool Mastery
**What didn't work:** Too broad, no specific story, vague predictions
**Lesson:** Specific > general, story > trend

---

## Tools/References

- **Commands:** /free-post-outline, /newsletter-post, /analyze-draft
- **Agent:** @newsletter-competitive-analyst
- **Voice:** `.claude/output-styles/ai-pm-voice`

---

## Lessons Learned

**Real numbers drive engagement:** "R47K" >> "significant amount"

**Near-miss > success story:** Vulnerability builds trust

**COO-sourced content performs better:** 3.8% avg vs 3.3% for other sources

**Specific > general:** One deep example beats five shallow ones
```

---

### 3. `CMO/memories/content-creation/paid-blueprint-patterns.md`

```markdown
# Paid Tier Blueprint Patterns

**Content type:** Paid (How to Build guides)
**Engagement target:** 4%+ (higher for paid audience)
**Last used:** [Date]

---

## Purpose

Paid tier delivers implementation details. Readers pay for the "how" after free tier showed the "what" and "why".

**Goal:** Deliver actionable, step-by-step guides that justify subscription.

---

## Prerequisites

- [ ] Free post published that teased this guide
- [ ] Complete workflow tested and documented
- [ ] Screenshots/code examples ready
- [ ] Time estimate for reader implementation

---

## Steps

### 1. Validate Demand

Check:
- Free post engagement on this topic
- Comments/questions received
- CTA click-through rate

### 2. Structure (BLUEPRINT FORMAT)

```
CONTEXT (200-300 words)
├── Quick reminder of the What/Why (link to free post)
├── What reader will build
└── Time estimate and prerequisites

STEP-BY-STEP BUILD (1000-1500 words)
├── Numbered steps
├── Screenshots/code at each step
├── Common pitfalls highlighted
└── "Checkpoint" after each major section

CUSTOMIZATION (200-300 words)
├── How to adapt for their situation
├── Variables to adjust
└── Advanced options

TROUBLESHOOTING (200-300 words)
├── Common errors and fixes
├── FAQ from beta testers/comments
└── Where to get help

NEXT STEPS (100-150 words)
├── What to build next
├── Related guides
└── Community discussion link
```

### 3. Draft (2-3 hours)

**Command:** `/paid-post-blueprint`

Key elements:
- Every step tested and verified
- Screenshots at decision points
- Copy-paste code/commands where applicable
- "Why" brief explanation for each step

### 4. Edit (45-60 min)

**Checklist:**
- [ ] Can reader follow without prior knowledge?
- [ ] Every step has expected outcome
- [ ] Screenshots current and clear
- [ ] No assumed knowledge unexplained
- [ ] Time estimate accurate

### 5. Publish

- Schedule for premium tier
- Send notification to paid subscribers
- Add to guide index

---

## High-Performing Examples

### Budget Watchdog Guide
**Title:** "Building a Budget Watchdog with Claude Code: 30-Minute Implementation"
**Free post:** "The R47,000 Mistake..."
**What worked:** Clear time estimate, real tool output, troubleshooting section

### LOI Automation Guide
**Title:** "Automating LOIs: From Request to Signed in Under 10 Minutes"
**Free post:** "Why Manual LOIs Cost You More Than Time"
**What worked:** Before/after comparison, actual template included

---

## Tools/References

- **Commands:** /paid-post-blueprint
- **Voice:** `.claude/output-styles/ai-pm-voice`

---

## Lessons Learned

**Time estimates matter:** "30 minutes" more compelling than "quick"

**Include troubleshooting:** Readers will hit issues, anticipate them

**Link to free post:** Reinforces value chain, helps SEO
```

---

### 4. `CMO/memories/content-creation/hook-formulas.md`

```markdown
# Hook Formulas

**When to use:** Opening any content piece
**Last used:** [Date]

---

## High-Performing Hook Types

### 1. Near-Miss Story
```
"Last Tuesday, I almost [disaster]. Here's what saved me..."
"I was seconds away from [mistake] when [intervention]..."
```
**Engagement:** 4.0%+ average
**Why it works:** Vulnerability, suspense, relatability

### 2. Specific Number
```
"R47,000. That's how much [outcome]..."
"3 minutes. That's all it took to [result]..."
```
**Engagement:** 3.8%+ average
**Why it works:** Concrete, credible, attention-grabbing

### 3. Contrarian Claim
```
"Your [common tool] isn't the problem. Your [workflow] is."
"Stop trying to [common advice]. Do [opposite] instead."
```
**Engagement:** 3.7%+ average
**Why it works:** Challenges beliefs, creates curiosity

### 4. Before/After
```
"Last month: [painful state]. This week: [transformed state]."
"6 months ago I [old way]. Now I [new way]. Here's what changed..."
```
**Engagement:** 3.5%+ average
**Why it works:** Demonstrates transformation, shows possibility

### 5. Question Hook
```
"What would you do with 10 extra hours per week?"
"Why do 90% of [group] struggle with [task]?"
```
**Engagement:** 3.3%+ average
**Why it works:** Engages reader directly, creates reflection

---

## Hook Testing Process

1. Write 3 variants using different formulas
2. Use `/generate-hook-variants` for more options
3. Pick strongest for main post
4. Save others for LinkedIn/Notes versions

---

## Common Mistakes

**Too vague:** "I learned something important" → "I lost R47K learning this"
**Too long:** Hook should be 2-3 sentences max
**No stakes:** What does reader lose by not reading?
**Clickbait without payoff:** Hook must match content delivery

---

## Lessons Learned

**Numbers beat adjectives:** "R47K" > "significant amount"
**Near-miss beats success:** Failures more relatable than wins
**Specificity builds trust:** "Last Tuesday" > "Recently"
```

---

### 5. `CMO/memories/repurposing/newsletter-to-linkedin.md`

```markdown
# Newsletter to LinkedIn Workflow

**When to use:** After publishing newsletter, repurpose for LinkedIn
**Last used:** [Date]
**Success rate:** High

---

## Prerequisites

- [ ] Newsletter published
- [ ] Engagement data available (optional but helpful)
- [ ] LinkedIn posting window identified (Tue-Thu, 8-10am ideal)

---

## Steps

### 1. Extract Core Insight (10 min)

From newsletter, identify:
- One key takeaway
- Most quotable line
- Real result/number

### 2. Reformat (15-20 min)

**Command:** `/newsletter-to-linkedin [post-title]`
**Agent:** @linkedin-post-expander

**LinkedIn Format:**
```
[Hook - 1-2 lines, create curiosity]

[Blank line]

[Problem statement - 2-3 lines]

[Blank line]

[Solution/insight - bullet points or numbered list]

[Blank line]

[Result or proof point]

[Blank line]

[CTA - question or invitation to comment]

[Blank line]

#relevanthashtags (3-5 max)
```

### 3. Optimize for LinkedIn

**Key differences from newsletter:**
- Shorter paragraphs (1-2 sentences)
- More white space
- Bullet points preferred
- Question at end (drives comments)
- No external links in post (kills reach)

### 4. Schedule

- Best times: Tuesday-Thursday, 8-10am local
- Use scheduling tool or post directly
- Link to newsletter in first comment (not post body)

### 5. Engage

- Respond to every comment within 2 hours
- Like comments within 1 hour
- Ask follow-up questions

---

## LinkedIn-Specific Hooks

```
"Unpopular opinion: [contrarian take]"
"I spent [time] on [thing]. Here's what I learned:"
"The best [advice] I ever got: [advice]. Here's why:"
"Stop [common action]. Start [better action]. Here's the difference:"
```

---

## Hashtag Strategy

**Always include:**
- #projectmanagement
- #AI or #artificialintelligence

**Rotate based on content:**
- #construction (for COO-sourced)
- #productivity
- #leadership
- #automation

**Avoid:**
- More than 5 hashtags
- Overly generic (#business, #success)

---

## Tools/References

- **Command:** /newsletter-to-linkedin
- **Agent:** @linkedin-post-expander

---

## Lessons Learned

**No links in post body:** LinkedIn suppresses posts with external links. Put in comments.

**Engagement window critical:** First 2 hours determine reach. Be available to respond.

**Questions drive comments:** End with genuine question, not rhetorical.
```

---

### 6. `CMO/memories/repurposing/substack-notes.md`

```markdown
# Substack Notes Workflow

**When to use:** Creating bite-sized content for Substack Notes
**Last used:** [Date]
**Success rate:** Medium-High

---

## Prerequisites

- [ ] Source content identified (newsletter or standalone)
- [ ] Core insight extracted
- [ ] Visual element ready (optional but helps)

---

## Steps

### 1. Identify Note-Worthy Content

From newsletters, extract:
- Surprising stat
- Quotable insight
- Useful tip
- Behind-the-scenes moment

### 2. Format for Notes (5-10 min)

**Agent:** @substack-notes-generator

**Note Format:**
```
[Hook - 1 sentence]

[Insight - 2-3 sentences max]

[Optional: Image or screenshot]

[Question or CTA]
```

**Character limit:** ~280 characters for best engagement

### 3. Types of Notes

**Insight Note:**
Quick takeaway from longer content
```
The most expensive tool in your stack isn't software.
It's the 20 minutes you spend deciding which tool to use for each task.
Automate the decision, not just the task.
```

**Behind-the-Scenes:**
Show process or work-in-progress
```
Writing tomorrow's newsletter on budget automation.
Current outline has 4 sections. Will probably cut to 3.
What's one thing you'd want to know about automating budget tracking?
```

**Quick Tip:**
Actionable in one sentence
```
Before any client call, write down the ONE decision you need from them.
Everything else is context.
```

### 4. Timing

- Post 2-3 Notes between newsletters
- Don't post same day as newsletter
- Engage with other Notes in your niche

---

## Tools/References

- **Agent:** @substack-notes-generator

---

## Lessons Learned

**Shorter = better:** Notes that try to say too much underperform.

**Questions drive replies:** End with genuine question.

**Consistency matters:** Regular Notes build algorithmic favor.
```

---

### 7. `CMO/memories/performance/engagement-patterns.md`

```markdown
# Engagement Patterns

**When to use:** Analyzing what drives engagement, fixing underperforming content
**Last used:** [Date]

---

## Engagement Targets

| Content Type | Target | Current Avg |
|--------------|--------|-------------|
| Free newsletter | 3.5%+ | 3.8% |
| Paid newsletter | 4.0%+ | TBD |
| LinkedIn | 2.0%+ | TBD |
| Substack Notes | 1.5%+ | TBD |

---

## High Engagement Drivers

### 1. Real Numbers
- "R47K" not "significant savings"
- "30 minutes" not "quickly"
- "15% reduction" not "improved efficiency"

### 2. Near-Miss Stories
- "I almost..."
- "We nearly..."
- Vulnerability builds trust

### 3. COO-Sourced Content
- Average 3.8% vs 3.3% for other sources
- Real operational context resonates
- Flywheel content outperforms

### 4. Specific > General
- One deep example beats five shallow
- Named tools/methods beat generic "AI"
- Actual screenshots beat descriptions

### 5. Strong Hook
- Near-miss hooks: 4.0%+ avg
- Specific number hooks: 3.8%+ avg
- See `../content-creation/hook-formulas.md`

---

## Low Engagement Warning Signs

| Pattern | Problem | Fix |
|---------|---------|-----|
| Opens low | Weak hook | Test 3 hook variants |
| Drops mid-article | Structure issue | Check flow, add subheads |
| Low CTA clicks | Unclear value | Strengthen CTA, add urgency |
| Few shares | Not quotable | Add tweetable one-liner |
| Low comments | No question | End with genuine question |

---

## Fixing Underperforming Content

### Step 1: Diagnose
- Where do readers drop off?
- What's the engagement pattern vs high performers?
- Is hook weak or content weak?

### Step 2: Test
- New hook (quickest fix)
- Restructure (medium effort)
- Add examples/numbers (requires new content)

### Step 3: Repurpose
- Turn into LinkedIn with stronger hook
- Extract best part for Note
- Save and retry topic later with better angle

---

## Tools/References

- **Command:** /performance-analysis

---

## Lessons Learned

**Hook is 80% of the battle:** Great content with weak hook fails.

**Track what works:** Keep examples of high performers for reference.

**Iterate, don't abandon:** Underperforming topics often just need better angle.
```

---

### 8. `CMO/memories/performance/pillar-balance.md`

```markdown
# Pillar Balance Tracking

**When to use:** Content planning, ensuring balanced coverage
**Last used:** [Date]

---

## Target Distribution

| Pillar | Target | Description |
|--------|--------|-------------|
| AI Workflow Mastery | 44% | Building compounding systems |
| Tool Mastery | 22% | Deep dives on specific tools |
| Thinking Mastery | 33% | Cognitive frameworks |

---

## Why These Ratios

**AI Workflow (44%):** Core differentiator. Practical implementation drives subscriptions.

**Tool Mastery (22%):** Necessary but commoditized. Too much = generic tech blog.

**Thinking Mastery (33%):** Builds authority and loyalty. Abstract but high-value.

---

## Current Balance

| Pillar | Posts | Actual % | vs Target |
|--------|-------|----------|-----------|
| AI Workflow | [N] | [X]% | [+/-]% |
| Tool | [N] | [X]% | [+/-]% |
| Thinking | [N] | [X]% | [+/-]% |

*Update monthly*

---

## Pillar Assignment

**AI Workflow Mastery:**
- Automation case studies
- System-building guides
- Workflow optimization
- Claude Code implementations
- Integration tutorials

**Tool Mastery:**
- Tool reviews
- Feature deep-dives
- Comparison posts
- Setup guides
- Tips and tricks

**Thinking Mastery:**
- Decision frameworks
- Mental models
- Strategy posts
- Leadership insights
- Mindset shifts

---

## Rebalancing Actions

**If AI Workflow under:**
- Check `../../memories/domain-handoffs/content-opportunities.md` for COO insights
- Focus next 2-3 posts on implementations

**If Tool over:**
- Pause tool reviews
- Convert tool posts to workflow posts (tool as part of system)

**If Thinking under:**
- Extract frameworks from workflow posts
- Add strategy layer to implementation posts

---

## Lessons Learned

**Workflow posts drive subscriptions:** Don't neglect core pillar.

**Tool posts have short shelf-life:** Tools change, principles don't.

**Thinking posts build loyalty:** Readers return for unique perspective.
```

---

### 9. `CMO/memories/pipeline/coo-to-content.md`

```markdown
# COO to Content Pipeline

**When to use:** Generating content ideas from operations
**Last used:** [Date]

---

## Primary Source: content-opportunities.md

**ALWAYS check first:**
```bash
cat ../../memories/domain-handoffs/content-opportunities.md
```

COO-sourced content performs 15% better on average (3.8% vs 3.3% engagement).

---

## How to Convert COO to Content

### Step 1: Identify the Story

From COO workflow, extract:
- What problem was solved?
- What was the "before" state?
- What was the "after" result?
- What made this challenging?
- What would reader gain?

### Step 2: Choose Angle

| COO Element | Free Tier Angle | Paid Tier Angle |
|-------------|-----------------|-----------------|
| Problem solved | Why this matters | How to solve it |
| Tool used | What it enables | How to set it up |
| Time saved | The principle | The implementation |
| Money saved | The insight | The calculation |

### Step 3: Fill in Gaps

COO memories have operational detail. Add:
- Story arc (beginning, middle, end)
- Reader relatability (they face this too)
- Broader principle (beyond this specific case)
- Actionable takeaway

---

## Content Mining Questions

Ask COO work:
1. What took longer than expected? (Process improvement content)
2. What almost went wrong? (Near-miss story)
3. What did client appreciate most? (Value proposition content)
4. What would you do differently? (Lessons learned content)
5. What did AI make possible? (Automation content)

---

## Pipeline Workflow

```
COO completes workflow
        ↓
Logs to content-opportunities.md (if content-worthy)
        ↓
CMO reviews weekly
        ↓
Selects for content calendar
        ↓
Drafts using CMO memories
        ↓
Publishes
        ↓
Tracks in flywheel/complete-cycles.md
```

---

## When COO Insights Run Low

Alternative sources:
1. Client questions (what do they ask repeatedly?)
2. Industry trends (what's changing?)
3. Tool updates (what's new?)
4. Comments/feedback (what do readers want?)
5. Competitor gaps (what aren't others covering?)

---

## Lessons Learned

**Operational context = credibility:** "I built this for a real project" beats theory.

**Numbers from COO work are gold:** Real metrics drive engagement.

**Flywheel is the advantage:** Competitors can't fake operational experience.
```

---

## CMO/CLAUDE.md Modification

**File:** `/Users/donovan/PROMAN_OS/CMO/CLAUDE.md`

**Insert after "Quick Start" section (~line 18):**

```markdown
---

## Workflow Memory System

**Before content tasks:**
1. **FIRST:** Check `../memories/domain-handoffs/content-opportunities.md` for COO insights
2. Search `memories/README.md` for relevant workflow
3. If found → Follow documented steps exactly

**Content Type → Category mapping:**
| Content Type | Search First |
|--------------|--------------|
| Free tier post | `memories/content-creation/free-post-patterns.md` |
| Paid guide | `memories/content-creation/paid-blueprint-patterns.md` |
| Strong hook | `memories/content-creation/hook-formulas.md` |
| LinkedIn post | `memories/repurposing/newsletter-to-linkedin.md` |
| Substack Note | `memories/repurposing/substack-notes.md` |
| Low engagement fix | `memories/performance/engagement-patterns.md` |
| Pillar balance | `memories/performance/pillar-balance.md` |
| Content ideas | `memories/pipeline/coo-to-content.md` |

**After content tasks:**
- Update memory with engagement data and lessons
- Track flywheel in `../memories/flywheel/complete-cycles.md`

---
```

---

## Implementation Checklist

- [ ] Create `CMO/memories/` directory
- [ ] Create `CMO/memories/content-creation/` directory
- [ ] Create `CMO/memories/repurposing/` directory
- [ ] Create `CMO/memories/performance/` directory
- [ ] Create `CMO/memories/pipeline/` directory
- [ ] Create `CMO/memories/README.md`
- [ ] Create `CMO/memories/content-creation/free-post-patterns.md`
- [ ] Create `CMO/memories/content-creation/paid-blueprint-patterns.md`
- [ ] Create `CMO/memories/content-creation/hook-formulas.md`
- [ ] Create `CMO/memories/repurposing/newsletter-to-linkedin.md`
- [ ] Create `CMO/memories/repurposing/substack-notes.md`
- [ ] Create `CMO/memories/performance/engagement-patterns.md`
- [ ] Create `CMO/memories/performance/pillar-balance.md`
- [ ] Create `CMO/memories/pipeline/coo-to-content.md`
- [ ] Modify `CMO/CLAUDE.md` with Workflow Memory System section
