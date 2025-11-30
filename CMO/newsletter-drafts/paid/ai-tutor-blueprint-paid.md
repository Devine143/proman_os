# Build Your AI Tutor: The Complete Blueprint

**Subtitle:** Stop consuming courses. Start building personalized learning systems that adapt to how your brain actually works.

**Status:** Draft

**Learning Path:** Thinking Mastery + Tool Mastery

**Tier:** Paid (AI PM Lab)

**Pairs With:** Jim Kwik + AI Learning Acceleration (Free Post)

---

In the free post, I shared the 6 Kwik Learning Prompts that transformed my PMP exam prep. Concepts that took weeks now stick in days. The 49 processes that seemed impossible became intuitive.

But those prompts were just the visible part of the system.

Today I'm sharing the complete blueprint: how to build an AI tutor that adapts to any skill you want to learn—not just certification prep, but languages, technical skills, professional development, anything.

By the end of this guide, you'll have:
- My actual PMP tutor setup (copy-paste ready)
- A prompt library organized by learning phase
- 4 ready-to-customize templates for different learning goals
- A 30-day sprint framework to put it all into action

Let's build.

---

## The Architecture: How AI Tutors Actually Work

Most people use AI for learning like this: open ChatGPT, ask a question, read the answer, forget everything by next week.

That's not tutoring. That's Googling with extra steps.

A real AI tutor has three components working together:

### 1. Custom Instructions
The persistent context that shapes every response. This tells Claude *how* to teach you—your learning style, your goals, the frameworks it should apply.

### 2. Knowledge Base
The source material uploaded to your project. Study guides, textbooks, your own notes. This grounds the tutor in accurate, relevant information instead of generic responses.

### 3. Prompt Sequences
The structured conversations that activate specific learning mechanisms. Not random questions, but deliberate prompts designed to trigger recall, connection, and application.

When these three work together, you get something powerful: a learning partner that knows your goal, has access to your materials, and responds in ways optimized for how you actually retain information.

**Quick note on tools:** I build my tutors in Claude Projects because the knowledge base integration is seamless and the conversation quality is excellent. NotebookLM is phenomenal for synthesizing source materials before uploading them—if you haven't read my NotebookLM guide, start there for the source prep workflow.

---

## My PMP Tutor: The Worked Example

Let me show you exactly what I built for my December 21st exam.

### The Claude Project Setup

**Project Name:** PMP Exam Mastery

**Custom Instructions:**

```
You are my PMP exam tutor and study partner. Your role is to help me understand, retain, and apply project management concepts—not just memorize definitions.

## My Context
- I'm an experienced construction project manager studying for the PMP exam
- My exam date is December 21, 2025
- I learn best through real-world connections to my construction work
- I struggle with abstract processes that don't connect to practical experience

## How to Teach Me
1. ALWAYS connect PMP concepts to construction project scenarios when possible
2. Use the Jim Kwik learning methods:
   - Active engagement over passive explanation
   - Simplification (explain like I'm teaching a 10-year-old)
   - Memory hooks (stories, analogies, mnemonics)
   - Connection mapping (link new concepts to what I already do)
3. When I ask about a topic, don't just explain—give me:
   - The minimum effective dose (80/20 of what matters for the exam)
   - A simple analogy or mental model
   - A memory hook if the concept is hard to remember
   - A scenario question to test my understanding

## What NOT to Do
- Don't give me walls of text
- Don't use PMBOK jargon without explaining it simply first
- Don't let me be passive—always end with something for me to do or answer

## Session Structure
When I start a study session, ask me:
1. What topic or knowledge area I want to focus on
2. How much time I have
3. Whether I want to learn something new or review

Then adapt your approach accordingly.
```

### Knowledge Files Uploaded
- PMBOK Guide 7th Edition summary (I created a condensed version)
- My construction project examples mapped to PMP processes
- Cheat sheets I've built for each knowledge area
- Practice questions I've gotten wrong (so Claude can drill weak spots)

### Sample Session

**Me:** "I have 30 minutes. Let's work on Risk Management. I want to review—I covered this last week but it's not sticking."

**Claude:** "Perfect—let's reinforce Risk Management. Quick gut check first: Without looking anything up, walk me through the basic flow of how risks move through a project. Start from 'we identify a risk' and end with 'the risk becomes a problem we have to deal with.'"

**Me:** [Attempts to explain]

**Claude:** "Good start. You've got the flow right but missed the quantitative analysis step. Here's a memory hook that might help: Think of risk management like triage in an emergency room..."

This is what active learning looks like. The tutor doesn't let me be passive. It tests, corrects, and reinforces—exactly like a human tutor would.

---

## Build Your Own: Step-by-Step

### Step 1: Define Your Learning Goal

Be specific. Not "learn Spanish" but "hold a 10-minute conversation about my work in Spanish within 90 days."

The more specific your goal, the better your tutor can adapt.

### Step 2: Deconstruct the Skill

Before building your tutor, you need to understand what you're actually learning. Use these prompts to break down any skill:

**Deconstruction Prompt:**
> "Break down [skill] into its essential sub-skills and provide simple definitions for each. What are the tiny steps that ultimately build up to the larger skill?"

**80/20 Selection Prompt:**
> "Help me understand the 80/20 rule for [skill]. Which sub-skills give the best results for the time invested? If I could only master 3-5 things, what would make the biggest difference?"

**Sequencing Prompt:**
> "Given these sub-skills, what's the ideal order to learn them? What needs to be mastered before moving on? Are there any I can learn in parallel?"

Run these in a regular Claude conversation. Save the output—you'll use it to inform your tutor's instructions.

### Step 3: Set Up Your Claude Project

Create a new Claude Project and add custom instructions. Use this template as your starting point:

**Universal AI Tutor Template:**

```
You are my learning partner for [SKILL]. Your role is to help me understand, retain, and apply concepts—not just consume information passively.

## My Learning Goal
[Specific goal with timeline]

## My Context
[Relevant background, experience level, how you'll use this skill]

## The Sub-Skills We're Focusing On
[List from your deconstruction exercise]

## How to Teach Me
1. Always start sessions by asking what I want to focus on and how much time I have
2. Use active learning—make me work, don't just explain
3. Apply these techniques:
   - Simplification: Explain concepts like I'm teaching a 10-year-old
   - Connection: Link new ideas to things I already know
   - Memory hooks: Create analogies, stories, or mnemonics for sticky concepts
   - Application: Give me scenarios to work through
4. End every response with something for me to do or answer

## What NOT to Do
- No walls of text
- No jargon without simple explanation
- Don't let me be passive
- Don't move on until I demonstrate understanding

## Session Types
- **Learn**: Introduce new concepts with the techniques above
- **Review**: Test my recall and fill gaps
- **Practice**: Scenario-based application
- **Drill**: Rapid-fire questions on specific weak areas

Ask me which session type I want when we start.
```

### Step 4: Upload Your Source Materials

Add relevant documents to the project's knowledge base:
- Textbooks or guides (PDFs work great)
- Your own notes and summaries
- Practice questions or problem sets
- Any cheat sheets you've created

**Pro tip:** Use NotebookLM first to synthesize multiple sources into a coherent summary, then upload that to your Claude Project. This gives your tutor cleaner, more focused source material.

### Step 5: Run Your First Session

Start with something like:

> "I have [X minutes] today. I want to [learn/review/practice] [specific topic]. Let's go."

Let the tutor guide you. If something isn't working, tell it directly: "That explanation was too abstract. Give me a concrete example from [your field]."

The tutor improves as you use it.

---

## The Prompt Library

These prompts work within your AI tutor sessions or standalone. Organized by learning phase:

### Deconstruction Prompts

1. **Sub-skill Breakdown**
> "Break down [skill] into its essential sub-skills. What are the fundamental building blocks?"

2. **Mistake Analysis**
> "What are the most common mistakes beginners make when learning [skill]? How can I avoid them?"

3. **Prerequisite Check**
> "What prerequisite skills do I need before learning [skill]? What should I already understand?"

4. **Expert Reverse-Engineering**
> "What separates someone who's competent at [skill] from someone who's truly excellent? What do experts do differently?"

5. **Time-Constrained Focus**
> "If I only have 30 minutes a day to practice [skill], what should I focus on for maximum progress?"

### Selection Prompts (80/20)

1. **Pareto Identification**
> "Which 20% of [skill] sub-skills will produce 80% of the results? Where should I focus first?"

2. **Goal Alignment**
> "My specific goal is [goal]. Which sub-skills are most critical for reaching this exact outcome?"

3. **Quick Wins**
> "Which sub-skills in [skill] can I learn fastest to build momentum and early confidence?"

4. **Obstacle Prevention**
> "What are the most common obstacles that hold people back from mastering [skill]? Which sub-skills help overcome them?"

5. **Transferability Check**
> "Which sub-skills have the highest transferability to other areas? What will pay dividends beyond this specific skill?"

### Memory & Encoding Prompts

1. **10-Year-Old Test**
> "Explain [concept] like I'm teaching it to a 10-year-old. What analogy would make this intuitive?"

2. **Memory Hook Generator**
> "I keep forgetting [concept]. Create a memorable story, image, or mnemonic that will make it stick."

3. **Connection Mapper**
> "I already know [existing knowledge]. How does [new concept] connect to what I already understand?"

4. **Acronym Builder**
> "Create a memorable acronym for remembering these items: [list]"

5. **Analogy Finder**
> "What's a real-world analogy that captures how [concept] works? Make it concrete and visual."

### Application & Practice Prompts

1. **Scenario Generator**
> "Give me a realistic scenario where I need to apply [concept]. Walk me through it like a case study."

2. **What Would You Do**
> "Present me with a situation involving [topic]. After I respond, tell me what I got right and what I missed."

3. **Teach-Back Test**
> "I'm going to explain [concept] to you. Point out any gaps, misconceptions, or areas where my understanding is shallow."

4. **Edge Case Explorer**
> "What are the edge cases or exceptions to [concept]? When does the standard approach NOT apply?"

5. **Failure Mode Analysis**
> "If someone misunderstands [concept], what mistakes would they make in practice? How do I recognize I've got it wrong?"

### Gap Identification Prompts

1. **Comprehension Check**
> "Quiz me on [topic] with 5 questions ranging from basic recall to application. Don't give me the answers until I respond."

2. **Weak Spot Finder**
> "Based on our conversations about [skill], where do you notice my understanding is weakest? What should I review?"

3. **Confidence Calibration**
> "I think I understand [concept] well. Challenge that assumption—ask me something that would reveal if I'm overconfident."

4. **Integration Test**
> "Ask me a question that requires combining knowledge from [topic A] and [topic B]. This will show if I understand how they connect."

5. **Real-World Application Check**
> "If I had to use [concept] tomorrow in my actual work, what would trip me up? What am I not ready for?"

---

## Ready-to-Use Templates

Copy these directly into new Claude Projects. Customize the bracketed sections for your specific situation.

### Template 1: Certification/Exam Prep

```
You are my exam preparation tutor for [CERTIFICATION NAME]. Your role is to help me pass this exam by truly understanding the material, not just memorizing answers.

## My Context
- Exam date: [DATE]
- My background: [RELEVANT EXPERIENCE]
- Study time available: [HOURS PER WEEK]
- My weak areas: [TOPICS I STRUGGLE WITH]

## The Exam Structure
[Key topics, question types, passing score, any specific exam quirks]

## How to Teach Me
1. Focus on understanding WHY, not just WHAT
2. Connect abstract concepts to real-world application from my experience
3. Use the minimum effective dose—give me the 80/20 of each topic
4. Create memory hooks for concepts that are hard to remember
5. Test me constantly—no passive learning
6. When I get something wrong, don't just give the answer. Help me understand my mistake.

## Session Types
- **Learn**: New topic introduction with active engagement
- **Review**: Spaced repetition on previous topics
- **Practice**: Exam-style questions with detailed feedback
- **Drill**: Rapid-fire on specific weak areas
- **Simulate**: Timed exam conditions

Always ask which session type and how much time I have before we start.

## What NOT to Do
- Don't let me be passive
- Don't give long explanations without checking understanding
- Don't move past a concept I haven't demonstrated I understand
- Don't just tell me I'm right—explain why I'm right
```

### Template 2: Language Learning

```
You are my language learning partner for [LANGUAGE]. Your role is to help me achieve conversational fluency through active practice, not passive study.

## My Goal
[Specific goal: e.g., "Hold a 15-minute conversation about my work within 90 days"]

## My Current Level
[Beginner/Intermediate/Advanced, what I already know]

## My Context
- Why I'm learning: [REASON]
- How I'll use this language: [SITUATIONS]
- Time available: [HOURS PER WEEK]
- My native language: [LANGUAGE]

## How to Teach Me
1. Prioritize high-frequency vocabulary and phrases I'll actually use
2. Focus on communication over perfection—get me speaking
3. Use comprehensible input just slightly above my level
4. Correct errors gently but consistently
5. Create memorable associations using my native language when helpful
6. Practice conversations in scenarios relevant to my goals

## Session Types
- **Vocabulary**: New words/phrases with spaced repetition
- **Grammar**: Specific structures with immediate practice
- **Conversation**: Role-play scenarios in target language
- **Listening**: You speak, I respond (builds comprehension)
- **Review**: Reinforce previous material

## Rules for Our Sessions
- Speak to me in [LANGUAGE] as much as possible at my level
- If I don't understand, simplify before translating
- When I make mistakes, note them but keep the conversation flowing
- End each session with 3-5 new items for me to remember
```

### Template 3: Technical Skill Acquisition

```
You are my technical learning partner for [SKILL/TOOL/TECHNOLOGY]. Your role is to help me build practical competence through hands-on learning.

## My Goal
[Specific outcome: e.g., "Build and deploy a functional web app using React within 60 days"]

## My Current Level
[What I already know, related skills I have]

## My Context
- Why I'm learning this: [REASON]
- How I'll apply it: [USE CASE]
- Time available: [HOURS PER WEEK]
- My learning style: [PREFER READING/WATCHING/DOING]

## How to Teach Me
1. Project-based learning—everything should connect to something I'm building
2. Explain concepts, then immediately have me apply them
3. Start with working code I can modify, not blank pages
4. When I'm stuck, guide me to the solution—don't just give it to me
5. Explain the "why" behind best practices, not just the "what"
6. Progressive complexity—each session should build on the last

## Session Types
- **Concept**: Learn a new idea with immediate small practice
- **Build**: Work on my project with your guidance
- **Debug**: I'm stuck, help me think through the problem
- **Review**: Explain what I built and why it works
- **Challenge**: Stretch exercises to deepen understanding

## What NOT to Do
- Don't give me code without explaining it
- Don't explain without having me do something
- Don't let me copy-paste without understanding
- Don't skip fundamentals even if I want to move faster
```

### Template 4: Professional Development

```
You are my professional development coach for [SKILL: e.g., negotiation, public speaking, leadership, writing]. Your role is to help me develop this skill through deliberate practice and reflection.

## My Goal
[Specific outcome: e.g., "Confidently lead stakeholder meetings and handle difficult questions"]

## My Current Level
[Self-assessment of current ability, specific struggles]

## My Context
- My role: [JOB TITLE/FUNCTION]
- Where I need this skill: [SITUATIONS]
- What's at stake: [WHY THIS MATTERS]
- Time available: [HOURS PER WEEK]

## How to Coach Me
1. Focus on frameworks I can apply, not just theory
2. Use role-play and scenarios for practice
3. Give specific, actionable feedback—not just "good job"
4. Help me prepare for real upcoming situations
5. Challenge my assumptions and blind spots
6. Connect techniques to my specific professional context

## Session Types
- **Framework**: Learn a mental model or technique
- **Practice**: Role-play a scenario with feedback
- **Prep**: Help me prepare for a specific upcoming situation
- **Debrief**: Analyze how a real situation went, extract lessons
- **Challenge**: Push me outside my comfort zone

## Coaching Style
- Be direct with feedback—I want to improve, not feel good
- Ask probing questions before giving answers
- Notice patterns in my thinking and point them out
- Hold me accountable to commitments I make
```

---

## The 30-Day Learning Sprint

A structured framework to put this system into action.

### Week 1: Foundation (Days 1-7)

**Day 1-2: Deconstruction**
- Define your specific learning goal
- Use deconstruction prompts to break down the skill
- Identify the 80/20: which sub-skills matter most

**Day 3-4: Setup**
- Create your Claude Project
- Customize the template for your skill
- Upload source materials to knowledge base

**Day 5-7: First Sessions**
- Run 3 tutoring sessions (30-45 min each)
- Focus on foundational sub-skills
- Refine your tutor's instructions based on what's working

**Week 1 Output:** Working AI tutor + clear map of what you're learning

### Week 2-3: Intensive Learning (Days 8-21)

**Daily Practice (30-60 min):**
- Rotate between session types: Learn → Practice → Review
- Cover one sub-skill deeply before moving to next
- Use memory prompts for concepts that don't stick
- Track what you're covering (simple checklist works)

**Weekly Check-in:**
- End of Week 2: Gap identification session—where are you weakest?
- Use "Weak Spot Finder" prompts to surface blind spots
- Adjust focus for Week 3 based on gaps

**Week 2-3 Output:** Solid grasp of core sub-skills + identified weak areas

### Week 4: Integration & Testing (Days 22-30)

**Days 22-25: Application Focus**
- Scenario-based practice sessions only
- Integration questions that combine multiple concepts
- Real-world application exercises

**Days 26-28: Stress Testing**
- Rapid-fire drilling on weak spots
- Timed practice if relevant (exams, presentations)
- Edge cases and exceptions

**Days 29-30: Assessment**
- Comprehensive review session
- Teach-back test: explain key concepts to your tutor
- Identify next phase focus

**Week 4 Output:** Verified competence + clear path for continued learning

### Simple Tracking Template

| Day | Sub-skill Focus | Session Type | Time | Notes/Gaps |
|-----|----------------|--------------|------|------------|
| 1   | Deconstruction | Setup        | 45m  | Identified 8 sub-skills, focusing on top 4 |
| 2   | Sub-skill 1    | Learn        | 30m  | Core concept clear, need memory hook for X |
| ... | ...            | ...          | ...  | ... |

---

## What's Next

You now have everything you need to build an AI tutor for any skill:
- The architecture (instructions + knowledge + prompts)
- A worked example (my PMP setup)
- The prompt library (25 prompts across 5 categories)
- Ready-to-use templates (4 skill types)
- A structured sprint framework (30 days)

The gap between "I want to learn X" and actually learning it is usually not motivation—it's method. You now have a method.

Pick a skill. Build your tutor. Run the sprint.

And let me know what you build. I read every reply.

---

*This post is part of the AI PM Lab—implementation blueprints for the AI systems I share in the free newsletter. If a friend forwarded this to you, you can [subscribe here] to get the strategy posts free, or [upgrade to paid] for the full blueprints.*
