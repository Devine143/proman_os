# How I Automated My Daily Chase List and Reclaimed 30 Minutes Every Morning

*Draft Status: Second Draft*
*Tier: Free*
*Learning Path: AI Workflow Mastery*

---

## The Morning That Broke Me

I caught myself re-reading the same contractor email for the third time because I kept losing focus. Twenty tasks. Two projects. Zero momentum.

That's when it hit me: I wasn't managing my tasks. My tasks were managing me.

I manage construction projects for a living. Contractors waiting on approvals. Consultants needing decisions. Suppliers chasing payment confirmations. And somewhere buried in all of that—my own actual work.

Here's what my mornings used to look like:

Open laptop. Open OmniFocus. Stare at the list. Pick a task. Try to remember the context. Pull up the email thread. Draft a follow-up. Send it. Back to the list. Pick another task. Repeat.

By 9:30am, I'd sent maybe eight follow-up messages. I'd context-switched a dozen times. And I was already mentally exhausted—before doing any of the thinking work that actually moves projects forward.

---

## The Hidden Cost of "Just Following Up"

Here's what nobody tells you about task management: the list isn't the problem. The friction is.

Every follow-up requires the same invisible work:
- **Context retrieval**: Who is this person? What's the history? What did I last say?
- **Priority assessment**: How urgent is this really? What's the consequence of waiting?
- **Message composition**: How do I phrase this professionally without sounding pushy?
- **Channel selection**: Email or WhatsApp? Formal or casual?

Multiply that by 20+ tasks, and you've burned your best morning energy on administrative overhead.

Most people treat their task manager like a to-do list. They open it, feel overwhelmed, maybe knock off a few easy wins, and close it hoping tomorrow will be different.

I was stuck in this exact pattern for years.

---

## The Breakthrough: Task Manager as Data Source

The shift came when I stopped thinking of OmniFocus as a list and started thinking of it as a database.

My tasks weren't just reminders—they were structured data. Each one had:
- A priority tag (High, Medium, Low)
- A company or person associated with it
- A due date
- Context in the notes

What if I could feed all of that to an AI and let it do the cognitive heavy lifting?

That's when I built what I now call my **AI Chase List System**.

Fair warning: this took a weekend to set up properly. Getting OmniFocus structured with the right tags, projects, and notes took Saturday morning. Configuring Claude to connect to my task data (using something called MCP—Model Context Protocol) took another few hours. Tuning the prompts so the messages actually sounded like me? Another afternoon of iteration.

It wasn't plug-and-play. But it was a one-time investment that now pays dividends every single morning.

---

## The AI Chase List System: How It Works

Instead of manually scanning my task list every morning, I now run a single workflow that does four things:

### 1. Intelligent Prioritization

Claude connects directly to my OmniFocus data and surfaces what actually needs attention today. Not everything marked "high priority"—but the items where:
- The due date is approaching or passed
- The person/company hasn't responded in X days
- The task has been sitting without progress

It gives me a focused chase list, not an overwhelming dump.

### 2. Batch Decision-Making

I review the prioritized list in one session. For each item, I make a quick call:
- **Done** – Mark it complete
- **Chase** – Needs a follow-up message
- **Reassign** – Someone else should handle this
- **Defer** – Not actually urgent today

This takes 5 minutes. All decisions, one place, no context-switching.

### 3. Automated Message Generation

Here's where the magic happens. For every item I mark "Chase," the AI drafts two messages:
- A professional **email** version
- A shorter **WhatsApp** version

Both are context-aware. They reference the right project, the right person, the right history. They're professional but not robotic.

Here's a real example. The task in OmniFocus was:

> **Task:** Follow up on revised electrical quote
> **Project:** Arowana - Camps Bay
> **Tag:** waiting
> **Notes:** Spoke to Mike on 15th, he said new quote by end of week. Need updated pricing before we can finalize contractor selection.

The AI generated:

**Email version:**
> Hi Mike,
>
> Hope you're well. Following up on our conversation from the 15th regarding the revised electrical quote for the Camps Bay project. You mentioned you'd have updated pricing through by end of last week.
>
> Are you still on track to send that through? We're looking to finalize contractor selection shortly, so having your revised numbers would be helpful.
>
> Let me know if you need anything from our side.
>
> Best regards,
> Donovan

**WhatsApp version:**
> Hi Mike, just checking in on that revised electrical quote for Camps Bay. You mentioned end of last week—are we still on track? Need it for contractor selection. Thanks

Both took me about 3 seconds to scan, confirm the context was right, and send.

### 4. Single-Session Execution

The entire workflow happens in one place. I don't switch between OmniFocus, Gmail, WhatsApp, and back. I review, decide, and execute in a single session.

What used to take 45-60 minutes of scattered morning energy now takes 15-20 minutes of focused work.

---

## The Week I Tracked It

I was skeptical of my own claims, so I tracked it. For one week, I logged my morning chase routine—both the old way and the new way.

**Old method (Monday-Wednesday, before full adoption):**
- Monday: 47 minutes, 9 follow-ups sent
- Tuesday: 58 minutes, 11 follow-ups sent
- Wednesday: 41 minutes, 7 follow-ups sent

**New method (Thursday-Friday, with AI Chase List):**
- Thursday: 19 minutes, 12 follow-ups sent
- Friday: 16 minutes, 10 follow-ups sent

Average before: 49 minutes. Average after: 17.5 minutes. That's **31 minutes saved**—and more follow-ups actually sent.

The numbers surprised me. I'd assumed I was exaggerating the improvement. I wasn't.

Same tasks. Same responsibilities. Completely different energy.

---

## The Mistake That Almost Cost Me

Week two. I was flying through the chase list, feeling efficient. Copy, paste, send. Copy, paste, send.

Then my phone rang. It was a contractor I'd been chasing for revised pricing on a kitchen installation.

"Donovan, I already sent you the updated quote on Monday. You just sent me a message asking for it again."

I'd sent an AI-drafted follow-up without checking the context. The message referenced an old conversation, completely missing that he'd already responded. I looked careless at best, disorganised at worst.

**The lesson:** The AI handles the drafting. I handle the judgment. Now I spend 10 seconds scanning each message before sending—not editing the words, but verifying the context is right.

That extra 10 seconds per message adds maybe 3 minutes to my morning. Worth it to avoid looking like I'm not paying attention.

---

## "Aren't You Just Creating Dependency?"

I hear this objection a lot. "If AI writes all your messages, aren't you losing the skill?"

Here's my honest answer: maybe. But I'm making a deliberate trade-off.

The skill I'm "outsourcing" is message composition—the commodity work of turning a decision into words. I do this 20+ times a day. It's not where my value lies.

The skills I'm *keeping* are the ones that actually matter:
- **Deciding** what needs follow-up (judgment)
- **Reading** the relationship dynamics (context)
- **Knowing** when to pick up the phone instead of sending a message (wisdom)

The AI handles the drafting. I handle the thinking. That division of labor feels right to me.

If anything, I'm now *better* at the judgment calls because I'm not mentally exhausted from the drafting work.

---

## The Deeper Lesson

This isn't really about OmniFocus or Claude or saving 30 minutes.

It's about recognizing where friction steals your time—and building systems that eliminate it.

For me, the friction was in the space *between* seeing a task and acting on it. The context retrieval. The message composition. The channel decisions. All invisible work that drained my capacity before I touched anything strategic.

Your friction point might be different. Maybe it's email triage. Meeting prep. Status reports. The weekly update you dread writing.

The question isn't "what AI tool should I use?"

The question is: **Where does friction steal your time?**

---

## Your Next Step

Pick one daily task that drains more energy than it should. Not because it's hard—but because the friction around it is high.

Try this: Open your task manager right now. Find the task you've been avoiding because composing the follow-up feels tedious. That's your friction point.

Then ask: What if I could feed the inputs to AI and get the outputs I need?

That's the shift. From using AI for one-off tasks to building AI systems that remove friction permanently.

---

*I'm building more systems like this and documenting the exact setups. If you want the full implementation blueprint—including the MCP (Model Context Protocol) configuration that connects Claude to OmniFocus, the exact prompt templates I use, and the OmniFocus tag structure that makes it all work—that's coming in a future AI PM Lab post for paid subscribers.*

---

**What's your highest-friction daily task? Reply and let me know—I'm curious what's draining your mornings.**
