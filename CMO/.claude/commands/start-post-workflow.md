---
allowed-tools: Read, Edit, Write, Glob, SlashCommand
description: Guide through the full idea-to-post workflow for newsletter content
argument-hint: [idea or draft filename]
model: sonnet
---

# Start Post Workflow

This prompt guides you through the complete workflow for taking a newsletter idea from concept to polished post. Follow the `Workflow` steps sequentially, using the specified slash commands at each stage.

## Variables

INPUT: $1

## Workflow

1. **Assess the input** - Determine if `INPUT` is:
   - A rough idea/concept (needs outline first)
   - An existing draft file (skip to analysis)
   - A topic description (needs outline first)

2. **If starting from idea/concept:**
   - Run `/free-post-outline` with the idea to create structure
   - Save the outline to `newsletter-drafts/[topic-name].md`
   - Run `/newsletter-post` to draft the full post from outline

3. **If starting from existing draft:**
   - Read the draft file to understand current state
   - Proceed directly to analysis step

4. **Critical Analysis:**
   - Run `/analyze-draft` on the draft
   - Present findings to user
   - Ask user which recommendations to implement
   - Apply the approved changes

5. **Angle Exploration:**
   - Run `/angle-generator` on the revised draft
   - Present the 5 strategic angles
   - Ask user if they want to pivot to a different angle
   - If yes, restructure the draft accordingly

6. **Hook Optimization:**
   - Run `/generate-hook-variants` on the draft
   - Present hook options for newsletter, LinkedIn, and Notes
   - Ask user to select preferred hook
   - Apply the selected hook to the draft

7. **Quick Edit Polish:**
   - Run `/quick-edit` on the draft
   - Review suggestions for: hook strength, framework clarity, transitions, conclusion, voice consistency
   - Ask user which edits to apply
   - Implement approved changes

8. **Final Review:**
   - Present the completed draft
   - Ask if user wants to proceed with repurposing

9. **Repurposing (Optional):**
   - Run `/newsletter-to-linkedin` for LinkedIn post
   - Run `/generate-notes` for Substack Notes

## Report

After each step, provide:
- A brief summary of what was done
- The key output or decision made
- Clear prompt for the next step: "Ready for [next step]? (yes/no/skip)"

At workflow completion, provide:
- Summary of the full journey (idea → final draft)
- List of all outputs created (draft, LinkedIn post, notes)
- File locations for all created content
- Suggested next actions (publish, schedule, further edits)
