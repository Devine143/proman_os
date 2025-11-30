<!-- IMAGE: Hero image - top of post
PROMPT: A professional in business casual attire working at a modern desk with two monitors - one showing a terminal/code interface, the other showing construction project documents and Gantt charts. Clean minimalist office with warm natural lighting through large windows. Cape Town cityscape visible in background. Editorial illustration style, muted earth tones with subtle teal accents. Professional but approachable atmosphere.
-->

# How I Use Claude Code as My Business Partner

**When I first heard about "Claude Code"—a tool marketed to software engineers—I almost scrolled past. I'm a construction project manager, not a developer. But something made me curious: what if "code" wasn't the point?**

_By Donovan • [Date]_

My days are filled with risk registers, stakeholder matrices, project charters, and work breakdown structures. I coordinate consultants, manage client expectations, and keep multi-million rand developments from falling apart.

The promise of Claude Code wasn't "write code faster." It was "an AI that works alongside you in your actual environment." An AI that reads your files, understands your context, and executes complex tasks while you think.

Three months later, Claude Code has become my silent business partner. Not for coding—for everything else.

---

## Why a "coding tool" works for project management

Here's what makes Claude Code different from ChatGPT or regular Claude:

**Regular AI chat:**

- Lives in a browser tab
- You upload or copy-paste documents one at a time
- AI gives suggestions you manually implement
- Context disappears when you close the window
- Every new conversation starts from zero

**Claude Code:**

- Lives in your actual file system
- Reads entire project folders—dozens of documents at once—without manual uploads
- Creates and edits documents directly in your folders
- Remembers your project structure and preferences via configuration files
- Builds on previous work automatically

Think of it like this: Regular AI is a consultant you visit in their office, handing over one document at a time. Claude Code is a colleague who sits at the desk next to you, has access to your entire filing cabinet, and can actually draft documents while you're talking.

<!-- IMAGE: Comparison diagram - section break
PROMPT: Split-screen comparison illustration. Left side: person walking to separate office building carrying single document, labeled "Regular AI". Right side: two people sitting side-by-side at same desk, one pointing at shared filing cabinet, labeled "Claude Code". Clean flat design, muted blue and warm grey palette, minimal detail, conceptual diagram style.
-->

For project management, this means I can say:

> "Read the tender documents in my current project folder, analyze the scope, and create a preliminary risk register based on what you find."

And Claude Code actually does it—reading my real files (all 47 pages across multiple documents), understanding the project context, and producing a document I can use.

**Important caveat:** This requires some comfort with command-line interfaces. If you've never opened a terminal before, there's a learning curve. I'll share resources at the end for complete beginners—but be honest with yourself about whether you're willing to invest a few hours learning something new.

**Why not simpler alternatives?** Fair question. I tried Claude Projects (browser-based with file uploads) but hit limits when dealing with large tender packages—uploading 47 documents manually gets tedious fast. I looked at Notion AI and ClickUp Brain, but they're optimized for their own ecosystems rather than my existing document workflows. Claude Code won because it works with my files directly, doesn't lock me into a platform, and handles the volume of documentation that construction projects generate. Is the setup more complex? Yes. But for managing multiple concurrent projects, that upfront investment pays off repeatedly.

---

## My actual PM workflows with Claude Code

Enough theory. Let me show you exactly how this plays out in construction project management—including where it works brilliantly and where it's burned me.

### 1. Risk assessment with broader coverage

Last month I was preparing for a new commercial development. The client sent over 47 pages of tender documentation, site reports, and consultant proposals.

**The old way:** Spend half a day reading everything, manually identifying risks, categorizing by probability and impact, and building a register in Excel.

**The Claude Code way:**

> "Read all the documents in the /Tender folder. Identify potential project risks across these categories: site conditions, regulatory compliance, stakeholder conflicts, budget constraints, and timeline dependencies. Create a risk register with probability ratings, impact assessments, and recommended mitigation strategies. Format it for my standard template."

Fifteen minutes later, I had a comprehensive draft risk register that surfaced items for my review more systematically than a quick read-through would have.

Here's what made this valuable: buried on page 38 of the geotechnical report was a note about soil contamination testing requirements that would trigger additional municipal approvals. I might have caught this eventually, but Claude flagged it immediately as a regulatory compliance risk. I verified it was legitimate, added it to our project timeline, and we avoided what could have been a two-month delay.

**The key word is "draft."** I still review everything with my professional judgment. Claude surfaces potential risks—I validate which ones are real and appropriately categorized for this specific project.

### 2. Stakeholder analysis with depth

Construction projects live or die by stakeholder management. Developers, architects, engineers, contractors, municipal officials, neighbours—each with different interests, influence levels, and communication needs.

I now point Claude Code at my project documentation and ask:

> "Based on the project charter and meeting notes in this folder, create a stakeholder analysis matrix. Identify each stakeholder's interests, level of influence, potential concerns, and recommended engagement strategy. Flag any relationships that might create conflicts."

What comes back isn't generic template filler. It's analysis based on my actual project context—synthesizing information about specific consultants, historical patterns from meeting notes, and relationship dynamics I've documented.

**But here's where I learned to be careful:** Claude once flagged a contractor as "high risk for conflict" based on meeting notes where I'd documented a scope disagreement. What Claude didn't understand was that we'd resolved that issue months ago and now had an excellent working relationship. The AI reads patterns in text; it doesn't understand relationship nuance the way a human does.

I now treat stakeholder outputs as a first draft that captures documented information—not as a substitute for my actual relationships with these people.

### 3. Project charters that capture documented information

Project charters used to take me a full day. Gathering information from emails, meetings, and documents. Synthesizing it into a coherent scope statement. Defining objectives, constraints, assumptions, and success criteria.

Now my workflow is:

> "I'm initiating a new project. Read my meeting notes from the client kick-off, the initial proposal, and the site assessment report. Draft a project charter including: project purpose and justification, measurable objectives, high-level scope, key deliverables, constraints and assumptions, preliminary milestone schedule, and success criteria. Follow PMBOK guidelines."

Claude Code produces a first draft that captures the documented information comprehensively. I then spend my time on what actually matters: refining the strategic elements, ensuring alignment with client expectations, and adding the professional judgment that comes from experience.

**A note on professional responsibility:** These remain my documents. I review, validate, and sign off on everything. Claude is a drafting tool, not a replacement for professional judgment. My SACPCMP registration means I'm accountable for the quality and accuracy of project documentation—AI assistance doesn't change that responsibility.

### 4. Work breakdown structures from scope documents

WBS development is where projects get real. Breaking down deliverables into manageable work packages that can be assigned, tracked, and controlled.

For a recent residential development, I used Claude Code like this:

> "Based on the approved project scope in scope-statement.md, create a work breakdown structure for this residential development. Break down to level 3 for major phases and level 4 for critical path activities. Include: design development, regulatory approvals, site establishment, structural works, building envelope, internal finishes, external works, and handover. Format as both an outline and a visual hierarchy."

The output gave me a structured WBS following standard construction sequencing logic. It organized deliverables in a logical flow based on typical construction phases from its training data.

**What it doesn't do:** understand your specific site constraints, local subcontractor availability, or Cape Town's particular approval timelines. I always adjust the AI-generated structure based on project-specific realities. The value is in having a comprehensive starting framework rather than a blank page.

**A failure that taught me to double-check:** Claude once generated a WBS for a heritage building renovation that completely omitted the Heritage Western Cape approval phase. It treated the project like new construction rather than a protected structure. I caught it during my review—but only because I have a mental checklist of required phases for different project types. I added the missing phase, adjusted the dependencies, and made a note in my CLAUDE.md to always specify when projects involve heritage buildings. The lesson: Claude doesn't know what it doesn't know, so your expertise needs to fill those gaps.

### 5. Meeting preparation and follow-up

Before every significant meeting, I ask Claude Code to:

> "Read the previous meeting minutes, my notes on outstanding issues, and the current project status report. Prepare a meeting agenda that addresses open items, identifies decisions needed, and includes talking points for the budget discussion with the client."

After meetings, I dictate rough notes and have Claude Code transform them:

> "Convert these meeting notes into formal minutes with action items, responsible parties, and due dates. Update the project issues log with any new items raised."

The administrative burden that used to consume my evenings now takes minutes.

---

## The setup that makes this work

Those workflows only happen because I've structured my environment to support them. Here's what that looks like in practice:

### Project folder structure

Every project follows the same structure:

```
Project-Name/
├── 01-Initiation/
│   ├── project-charter.md
│   ├── stakeholder-register.md
│   └── feasibility-notes.md
├── 02-Planning/
│   ├── scope-statement.md
│   ├── wbs.md
│   ├── risk-register.md
│   └── schedule-baseline.md
├── 03-Execution/
│   ├── meeting-minutes/
│   ├── progress-reports/
│   └── change-requests/
├── 04-Monitoring/
│   ├── issues-log.md
│   └── variance-reports/
└── CLAUDE.md
```

Yes, this means I've moved my core project documentation to markdown files. But here's what makes this practical for client-facing work:

### The document skills game-changer

Anthropic released official "document skills" for Claude Code that solve the "my clients expect Word documents" problem. These skills let Claude Code create professional Word (.docx), Excel (.xlsx), PowerPoint (.pptx), and PDF files directly.

I was skeptical at first—how good could AI-generated Word documents really be? So I tested it on a real project charter last month. The result: a properly formatted .docx file with headers, a table of contents, styled tables for the milestone schedule, and consistent formatting throughout. My client couldn't tell it wasn't manually created in Word.

My workflow now looks like this:

1. **Work in markdown** for speed and AI collaboration
2. **Export to client formats** when needed using the docx skill

For example, after drafting a project charter in markdown, I ask:

> "Use the docx skill to convert project-charter.md into a professional Word document with proper formatting, headers, and our standard cover page."

Claude Code generates a polished .docx file ready for client review. Last week I used the xlsx skill to generate a formatted risk register with conditional formatting for high-priority items—something that would have taken me 30 minutes of Excel fiddling happened in seconds.

**To install the document skills:**

```bash
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
```

This means you get the best of both worlds: the speed of working in plain text with AI, plus the professional output formats your clients expect.

**The reality check:** The document skills handle 80-90% of formatting automatically. For important client documents, I still do a quick review—adjusting margins, tweaking table widths, ensuring page breaks fall in sensible places. But that's 5 minutes of polish versus 30 minutes of manual conversion.

### The CLAUDE.md file

This is the secret weapon. Every project folder has a `CLAUDE.md` file that tells Claude Code about the project context:

```markdown
# Project Context

## Project Overview
Commercial office development in Cape Town CBD
Client: [Developer Name]
Value: R85 million
Duration: 18 months

## Key Stakeholders
- Client PM: [Name] - decision maker, prefers weekly updates
- Architect: [Firm] - design lead, watch for scope creep
- Structural Engineer: [Firm] - reliable, conservative on timelines

## Current Phase
Planning - WBS development and schedule baseline

## Document Standards
- Use PMBOK terminology
- Risk ratings: 1-5 scale for probability and impact
- Currency: South African Rand (ZAR)
- Date format: DD Month YYYY

## My Preferences
- Be direct and practical, not theoretical
- Flag items that need my decision vs. items you can handle
- When uncertain, ask rather than assume
```

When Claude Code reads this file, every response is contextually aware. It knows the project, the stakeholders, my preferences, and the current phase.

**The maintenance reality:** I update CLAUDE.md when projects move between phases or when stakeholder dynamics change significantly. It's maybe 5 minutes per week per active project. For me, that's worth the dramatically better AI outputs.

---

## What this actually costs

Let me be transparent about the investment:

**Financial cost:**

- Claude Code requires a Claude subscription. Here are the tiers:
  - **Pro:** R360/month (or R306/month with annual billing) — includes Claude Code access
  - **Max 5x:** R1,800/month — 5x more usage than Pro
  - **Max 20x:** R3,600/month — 20x more usage than Pro

I'm currently on the Pro plan at R360/month. For most project managers, this is sufficient—you get Claude Code access plus generous usage limits. The Max plans are for power users running heavy workflows daily.

**Time investment:**

- Initial setup: 2-3 hours (installing Node.js, Claude Code, getting API access)
- Learning effective prompting: About a week of experimentation
- Per-project setup: 30-60 minutes to create folder structure and CLAUDE.md
- Ongoing: 5-10 minutes per project per week maintaining context files

**Technical requirements:**

- Comfort with command-line basics (or willingness to learn)
- Node.js installed on your computer
- Anthropic API account with credits

For me, the ROI is clear—I estimate I save 8-10 hours per week on administrative documentation. But I was already somewhat technical before starting. Your mileage may vary.

---

## What this actually feels like

Numbers are one thing. Here's the honest experience after three months:

**The good:**

- Complex documents that took hours now take minutes to draft
- I surface potential risks and issues more systematically
- My thinking time increased because admin time decreased
- I can take on more projects without drowning in paperwork

**The learning curve:**

- It took a week to figure out how to structure prompts effectively
- "Generate a risk register" produces generic garbage
- "Read these specific files and create a risk register based on this project's actual conditions" produces useful drafts
- The quality of your output directly reflects the quality of your direction

**The honest limitations:**

- Claude sometimes misunderstands construction terminology or local context
- It can be overconfident—I once had Claude rate a risk as "low probability" that anyone familiar with Cape Town municipal approvals would know is actually high probability
- Complex regulatory requirements need human expertise
- It's a tool that amplifies your professional judgment, not a replacement for it
- The outputs are drafts, not finished products—always review with professional skepticism

---

## Who this is actually for

Before you invest time setting this up, let me be direct about fit:

**This approach works if you:**

- Create documents as a core part of your work (reports, analyses, registers, charters)
- Work with complex information that needs synthesis
- Have repeatable workflows that follow patterns
- Are comfortable with command-line interfaces OR willing to invest time learning
- Value your strategic thinking time over administrative time
- Understand that AI outputs require professional review and validation

**This might not be for you if:**

- You need AI that "just works" without setup or learning curve
- Your work is primarily relationship-based rather than document-based
- You're not willing to learn command-line basics
- You don't have clear workflows to optimize
- You expect AI to replace professional judgment rather than support it

---

## Your next move

If you're curious, here's the realistic path:

### For complete beginners (never used a terminal):

1. **Learn command-line basics first.** Search "terminal basics for beginners" on YouTube—spend 30 minutes understanding what a terminal is and how to navigate folders.
2. **Install Node.js** from nodejs.org (it's a free download with a normal installer).
3. **Then come back to Claude Code** once you're comfortable typing commands.

### For those comfortable with basic terminal commands:

**Step 1: Install Claude Code**

```bash
npm install -g @anthropic-ai/claude-code
```

**Step 2: Set up Anthropic API access**
Visit console.anthropic.com, create an account, and add credits.

**Step 3: Navigate to a project folder**

```bash
cd /path/to/your/project
claude
```

**Step 4: Start with analysis, not creation**

Your first prompt should be exploratory:

> "Read the documents in this folder and summarize what you understand about this project. What are the key deliverables, stakeholders, and potential challenges you can identify?"

This lets you see how Claude Code interprets your files before asking it to create anything.

**Step 5: Build your CLAUDE.md**

Create a simple context file:

```markdown
# Project Context
[Brief project description]

## My Role
[What you do on this project]

## Document Preferences
[How you like things formatted]
```

Watch how responses improve with context.

---

## The real transformation

Here's what changed for me:

I used to think of AI as a research assistant—good for answering questions, limited for real work. Claude Code shifted that completely.

Now I think of AI as a junior team member who can handle document drafting, initial analysis, and administrative tasks while I focus on the work that actually requires my expertise: strategic decisions, stakeholder relationships, and professional judgment.

The projects didn't get easier. But the ratio of strategic thinking to administrative burden shifted dramatically in favor of the work that matters.

That's not a coding skill. That's a capability expansion for any knowledge worker who creates documents, analyzes information, and manages complexity.

**The outputs still need my professional review. The accountability still rests with me. But the hours spent on first drafts? Those I've reclaimed for higher-value work.**

So here's my question for you: What would you build if the administrative burden wasn't your bottleneck?

Not hypothetically. Actually think about it. That risk register you've been putting off. The project charter sitting half-finished. The stakeholder analysis you know you should update but never find time for.

Pick one. Try Claude Code on it this week. See what happens.

---

_I'm building a detailed guide on using Claude Code for project management—including templates, prompts, and troubleshooting for common issues. If you try this approach, hit reply and tell me what worked, what confused you, and what you wish it could do. Your real experiences will shape what I create next._
