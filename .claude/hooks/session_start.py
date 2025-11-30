#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""
SessionStart Hook: Injects WORKING.md task state into Claude's context.
Runs automatically on startup, resume, clear, and compact.

Whatever prints to stdout gets injected into Claude's context.
"""

import json
import sys
import os
from datetime import datetime, timedelta
from pathlib import Path


def parse_working_file(filepath: Path) -> dict:
    """Parse a WORKING.md file and extract tasks by status."""
    if not filepath.exists():
        return {"in_progress": [], "blocked": [], "completed": []}

    content = filepath.read_text()
    result = {"in_progress": [], "blocked": [], "completed": [], "raw": content}

    current_section = None
    for line in content.split("\n"):
        line_stripped = line.strip()
        line_lower = line_stripped.lower()

        if "## in progress" in line_lower:
            current_section = "in_progress"
        elif "## blocked" in line_lower:
            current_section = "blocked"
        elif "## recently completed" in line_lower:
            current_section = "completed"
        elif "## active flywheel" in line_lower:
            current_section = "in_progress"
        elif "## strategic priorities" in line_lower:
            current_section = "priorities"
        elif line_stripped.startswith("- **") and current_section in ["in_progress", "blocked"]:
            result[current_section].append(line_stripped)
        elif line_stripped.startswith("- ~~") and current_section == "completed":
            result[current_section].append(line_stripped)

    return result


def check_stale_tasks(tasks: list, days_threshold: int = 3) -> list:
    """Identify tasks older than threshold."""
    stale = []
    today = datetime.now()

    for task in tasks:
        if "(started:" in task:
            try:
                date_str = task.split("(started:")[1].split(")")[0].strip()
                started = datetime.strptime(date_str, "%Y-%m-%d")
                age = (today - started).days
                if age >= days_threshold:
                    stale.append((task, age))
            except (IndexError, ValueError):
                pass

    return stale


def extract_task_name(task: str) -> str:
    """Extract clean task name from markdown format."""
    # Handle: - **Task Name** (started: 2025-01-01)
    if "**" in task:
        parts = task.split("**")
        if len(parts) >= 2:
            return parts[1]
    return task.replace("- ", "").strip()[:50]


def format_domain_summary(domain: str, data: dict) -> list:
    """Format a domain's task summary as lines."""
    lines = []

    if data.get("in_progress"):
        for task in data["in_progress"]:
            task_name = extract_task_name(task)
            lines.append(f"  - [In Progress] {task_name}")

    if data.get("blocked"):
        for task in data["blocked"]:
            task_name = extract_task_name(task)
            lines.append(f"  - [BLOCKED] {task_name}")

    return lines


def detect_domain(cwd: str) -> str:
    """Detect which domain we're running from."""
    cwd_lower = cwd.lower()
    if "/cmo" in cwd_lower:
        return "CMO"
    elif "/coo" in cwd_lower:
        return "COO"
    return "ROOT"


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        input_data = {}

    # Get working directory
    cwd = input_data.get("cwd", os.getcwd())
    source = input_data.get("source", "startup")
    current_domain = detect_domain(cwd)

    # Find project root (contains WORKING.md)
    project_dir = Path(cwd)

    # Walk up to find PROMAN_OS root if we're in a subdomain
    while project_dir.name not in ["PROMAN_OS", ""] and not (project_dir / "WORKING.md").exists():
        if project_dir.parent == project_dir:
            break
        project_dir = project_dir.parent

    # If we found PROMAN_OS, use it; otherwise use cwd
    if project_dir.name != "PROMAN_OS":
        project_dir = Path(cwd)
        # Try going up from CMO or COO
        if project_dir.name in ["CMO", "COO"]:
            project_dir = project_dir.parent

    output_lines = []
    all_stale = []
    has_tasks = False

    # Define domains to check based on current location
    if current_domain == "CMO":
        domains = {
            "CMO": project_dir / "CMO" / "WORKING.md",
            "Cross-Domain": project_dir / "WORKING.md",
        }
    elif current_domain == "COO":
        domains = {
            "COO": project_dir / "COO" / "WORKING.md",
            "Cross-Domain": project_dir / "WORKING.md",
        }
    else:
        # Root - show all
        domains = {
            "COO": project_dir / "COO" / "WORKING.md",
            "CMO": project_dir / "CMO" / "WORKING.md",
            "Cross-Domain": project_dir / "WORKING.md",
        }

    # Parse each WORKING.md
    for domain, filepath in domains.items():
        data = parse_working_file(filepath)

        domain_lines = format_domain_summary(domain, data)
        if domain_lines:
            has_tasks = True
            output_lines.append(f"[{domain}]")
            output_lines.extend(domain_lines)

            # Check for stale tasks
            stale = check_stale_tasks(data.get("in_progress", []))
            for task, age in stale:
                all_stale.append((domain, task, age))

    # Build output
    if has_tasks:
        print("=== ACTIVE TASKS ===")
        print("\n".join(output_lines))

        if all_stale:
            print("\n[!] STALE (3+ days):")
            for domain, task, age in all_stale:
                task_name = extract_task_name(task)
                print(f"  - [{domain}] {task_name} ({age}d)")

    # Check for learnings index
    learnings_index = project_dir / "docs" / "learnings" / "README.md"
    if learnings_index.exists():
        print(f"\n[Learnings available: docs/learnings/README.md]")

    sys.exit(0)


if __name__ == "__main__":
    main()
