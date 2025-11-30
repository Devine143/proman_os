#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "python-dotenv",
# ]
# ///

import json
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional

# Configuration
MAX_PROMPT_LENGTH = 50  # Adjustable: Maximum characters to display for prompt
SHOW_GIT_INFO = False  # Set to True to show git branch and status


def log_status_line(input_data, status_line_output, error_message=None):
    """Log status line event to logs directory."""
    # Ensure logs directory exists
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "status_line.json"

    # Read existing log data or initialize empty list
    if log_file.exists():
        with open(log_file, "r") as f:
            try:
                log_data = json.load(f)
            except (json.JSONDecodeError, ValueError):
                log_data = []
    else:
        log_data = []

    # Create log entry with input data and generated output
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input_data": input_data,
        "status_line_output": status_line_output,
    }

    if error_message:
        log_entry["error"] = error_message

    # Append the log entry
    log_data.append(log_entry)

    # Write back to file with formatting
    with open(log_file, "w") as f:
        json.dump(log_data, f, indent=2)


def get_git_branch():
    """Get current git branch if in a git repository."""
    try:
        result = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None


def get_git_status():
    """Get git status indicators."""
    try:
        # Check if there are uncommitted changes
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            changes = result.stdout.strip()
            if changes:
                lines = changes.split('\n')
                return f"±{len(lines)}"
    except Exception:
        pass
    return ""


def get_session_data(session_id):
    """Get session data including agent name and prompts."""
    session_file = Path(f".claude/data/sessions/{session_id}.json")

    if not session_file.exists():
        return None, f"Session file {session_file} does not exist"

    try:
        with open(session_file, "r") as f:
            session_data = json.load(f)
            return session_data, None
    except Exception as e:
        return None, f"Error reading session file: {str(e)}"


def truncate_prompt(prompt, max_length=MAX_PROMPT_LENGTH):
    """Truncate prompt to specified length."""
    # Remove newlines and excessive whitespace
    prompt = " ".join(prompt.split())

    if len(prompt) > max_length:
        return prompt[:max_length - 3] + "..."
    return prompt


def get_project_context(input_data):
    """Extract active project from working directory."""
    workspace = input_data.get("workspace", {})
    cwd = workspace.get("current_dir", "")

    # Check if in a project folder
    if "/projects/" in cwd:
        # Extract project name from path
        project_name = cwd.split("/projects/")[1].split("/")[0]
        return f"📁 {project_name}"

    # Check if in AGENT root
    if cwd.endswith("/AGENT"):
        return "🏠 AGENT"

    return ""


def get_session_health(session_data, input_data):
    """Show session health and context indicators with detailed context window info."""
    indicators = []

    # Prompt count (context window health) - show actual number
    prompts = session_data.get("prompts", [])
    prompt_count = len(prompts)

    # Cost display (tokens not available in status line input)
    cost = input_data.get("cost", {})
    total_cost = cost.get("total_cost_usd", 0)

    # Format cost display
    if total_cost >= 1:
        cost_display = f"${total_cost:.2f}"
    elif total_cost > 0:
        # Show in cents for smaller amounts
        cost_display = f"{total_cost * 100:.0f}¢"
    else:
        cost_display = "$0"

    # Check if exceeding token budget
    exceeds_200k = input_data.get("exceeds_200k_tokens", False)

    # Build context window indicator with color coding
    if prompt_count > 50:
        context_indicator = f"🔥 {prompt_count}p/{cost_display}"
    elif prompt_count > 20:
        context_indicator = f"🌡️ {prompt_count}p/{cost_display}"
    else:
        context_indicator = f"💬 {prompt_count}p/{cost_display}"

    indicators.append(context_indicator)

    # High token usage warning
    if exceeds_200k:
        indicators.append("⚠️ LIMIT")

    return " ".join(indicators) if indicators else ""


def get_prompt_icon(prompt):
    """Get icon based on prompt type."""
    if prompt.startswith("/"):
        return "⚡"
    elif "?" in prompt:
        return "❓"
    elif any(
        word in prompt.lower()
        for word in ["create", "write", "add", "implement", "build"]
    ):
        return "💡"
    elif any(word in prompt.lower() for word in ["fix", "debug", "error", "issue"]):
        return "🐛"
    elif any(word in prompt.lower() for word in ["refactor", "improve", "optimize"]):
        return "♻️"
    else:
        return "💬"


def generate_status_line(input_data):
    """Generate the status line with agent name and most recent prompt."""
    # Extract session ID from input data
    session_id = input_data.get("session_id", "unknown")

    # Get model name
    model_info = input_data.get("model", {})
    model_name = model_info.get("display_name", "Claude")

    # Get session data
    session_data, error = get_session_data(session_id)

    if error:
        # Log the error but show a default message
        log_status_line(input_data, f"[{model_name}] 💭 No session data", error)
        return f"\033[36m[{model_name}]\033[0m \033[90m💭 No session data\033[0m"

    # Extract agent name and prompts
    agent_name = session_data.get("agent_name", "Agent")
    prompts = session_data.get("prompts", [])

    # Build status line components
    parts = []

    # Agent name - Red (distinguish between main and subagent)
    if agent_name == "Agent":
        # Main conversation - show as "Main"
        parts.append(f"\033[91m[Main]\033[0m")
    else:
        # Subagent - show actual agent name
        parts.append(f"\033[91m[{agent_name}]\033[0m")

    # Model name - Blue
    parts.append(f"\033[34m[{model_name}]\033[0m")

    # Session health indicators (Feature 4)
    health = get_session_health(session_data, input_data)
    if health:
        parts.append(health)

    # Git branch and status - green (optional)
    if SHOW_GIT_INFO:
        git_branch = get_git_branch()
        if git_branch:
            git_status = get_git_status()
            git_info = f"🌿 {git_branch}"
            if git_status:
                git_info += f" {git_status}"
            parts.append(f"\033[32m{git_info}\033[0m")

    # Project context display (Feature 3)
    project_context = get_project_context(input_data)
    if project_context:
        parts.append(f"\033[33m{project_context}\033[0m")  # Yellow for project

    # Most recent prompt only
    if prompts:
        current_prompt = prompts[-1]
        icon = get_prompt_icon(current_prompt)
        truncated = truncate_prompt(current_prompt, MAX_PROMPT_LENGTH)
        parts.append(f"{icon} \033[97m{truncated}\033[0m")
    else:
        parts.append("\033[90m💭 No prompts yet\033[0m")

    # Join with separator
    status_line = " | ".join(parts)

    return status_line


def main():
    try:
        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())

        # Generate status line
        status_line = generate_status_line(input_data)

        # Log the status line event (without error since it's successful)
        log_status_line(input_data, status_line)

        # Output the status line (first line of stdout becomes the status line)
        print(status_line)

        # Success
        sys.exit(0)

    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully - output basic status
        print("\033[31m[Agent] [Claude] 💭 JSON Error\033[0m")
        sys.exit(0)
    except Exception as e:
        # Handle any other errors gracefully - output basic status
        print(f"\033[31m[Agent] [Claude] 💭 Error: {str(e)}\033[0m")
        sys.exit(0)


if __name__ == "__main__":
    main()
