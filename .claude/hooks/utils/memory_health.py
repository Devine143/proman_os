#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""
PROMAN_OS Health Check
======================

Validates the Working Memory system is correctly configured and healthy.

Usage:
    uv run .claude/hooks/utils/memory_health.py           # check only
    uv run .claude/hooks/utils/memory_health.py --fix     # auto-repair missing files

Or via slash command:
    /memory-health
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime


class HealthCheck:
    def __init__(self, project_path: Path, fix_mode: bool = False):
        self.project_path = project_path
        self.fix_mode = fix_mode
        self.passed = 0
        self.failed = 0
        self.warnings = 0

    def check(self, condition: bool, description: str, is_warning: bool = False) -> bool:
        if condition:
            print(f"  ✅ {description}")
            self.passed += 1
            return True
        elif is_warning:
            print(f"  ⚠️  {description}")
            self.warnings += 1
            return False
        else:
            print(f"  ❌ {description}")
            self.failed += 1
            return False

    def run_all(self):
        print(f"\n{'='*60}")
        print(f"  PROMAN_OS Health Check")
        print(f"  Path: {self.project_path}")
        if self.fix_mode:
            print(f"  Mode: --fix enabled")
        print('='*60)

        self.check_working_md_files()
        self.check_stale_tasks()
        self.check_hook_file()
        self.check_settings_json()
        self.check_learnings_structure()
        self.check_index_sync()
        self.check_hook_execution()
        self.check_claude_md()

        self.print_summary()

    def check_working_md_files(self):
        print("\n📋 WORKING.md Files:")

        required_sections = ["## in progress", "## blocked", "## recently completed"]

        working_files = {
            "Root": self.project_path / "WORKING.md",
            "COO": self.project_path / "COO" / "WORKING.md",
            "CMO": self.project_path / "CMO" / "WORKING.md",
        }

        for domain, filepath in working_files.items():
            if filepath.exists():
                self.check(True, f"{domain}/WORKING.md exists")

                # Check structure
                content = filepath.read_text().lower()
                missing = [s for s in required_sections if s not in content]
                if missing:
                    self.check(False, f"{domain}/WORKING.md has all sections", is_warning=True)
            else:
                result = self.check(False, f"{domain}/WORKING.md exists")
                if self.fix_mode:
                    self._create_working_md(filepath, domain)
                    print(f"       → Fixed: Created {domain}/WORKING.md")

    def _create_working_md(self, filepath: Path, domain: str):
        """Create a WORKING.md template."""
        filepath.parent.mkdir(parents=True, exist_ok=True)

        if domain == "Root":
            template = f"""# Cross-Domain Active Work
> Last updated: {datetime.now().strftime('%Y-%m-%d')}

## Active Flywheel Items
<!-- Work that spans COO <-> CMO -->

## Strategic Priorities This Week
1.
2.
3.

## In Progress
<!-- Cross-domain or system-level tasks -->

## Blocked
<!-- Format: - **Task Name** (started: YYYY-MM-DD) -->

## Recently Completed
<!-- Format: - ~~Task Name~~ (completed: YYYY-MM-DD) -->
"""
        else:
            template = f"""# {domain} Active Work
> Last updated: {datetime.now().strftime('%Y-%m-%d')}

## In Progress
<!-- Format: - **Task Name** (started: YYYY-MM-DD) -->

## Blocked
<!-- Format: - **Task Name** (started: YYYY-MM-DD) -->

## Recently Completed
<!-- Format: - ~~Task Name~~ (completed: YYYY-MM-DD) -->
"""
        filepath.write_text(template)

    def check_stale_tasks(self):
        print("\n⏰ Stale Tasks (3+ days):")

        stale_found = []
        today = datetime.now()
        days_threshold = 3

        working_files = [
            ("Root", self.project_path / "WORKING.md"),
            ("COO", self.project_path / "COO" / "WORKING.md"),
            ("CMO", self.project_path / "CMO" / "WORKING.md"),
        ]

        for domain, filepath in working_files:
            if not filepath.exists():
                continue

            content = filepath.read_text()
            in_progress = False

            for line in content.split("\n"):
                if "## in progress" in line.lower():
                    in_progress = True
                elif line.startswith("## "):
                    in_progress = False
                elif in_progress and "(started:" in line:
                    try:
                        date_str = line.split("(started:")[1].split(")")[0].strip()
                        started = datetime.strptime(date_str, "%Y-%m-%d")
                        age = (today - started).days
                        if age >= days_threshold:
                            task_name = line.split("**")[1] if "**" in line else line[:40]
                            stale_found.append((domain, task_name, age))
                    except (IndexError, ValueError):
                        pass

        if stale_found:
            for domain, task, age in stale_found:
                self.check(False, f"[{domain}] {task} ({age}d old)", is_warning=True)
        else:
            self.check(True, "No stale tasks found")

    def check_hook_file(self):
        print("\n🪝 SessionStart Hook:")

        hook_path = self.project_path / ".claude" / "hooks" / "session_start.py"

        if not self.check(hook_path.exists(), "session_start.py exists"):
            return

        content = hook_path.read_text(encoding="utf-8")

        # Check for shebang
        has_shebang = content.startswith("#!/")
        self.check(has_shebang, "Has shebang line")

        # Check for main function
        has_main = "def main" in content or 'if __name__' in content
        self.check(has_main, "Has main entry point")

    def check_settings_json(self):
        print("\n⚙️  Settings Configuration:")

        settings_files = [
            ("Root", self.project_path / ".claude" / "settings.json"),
            ("CMO", self.project_path / "CMO" / ".claude" / "settings.json"),
            ("COO", self.project_path / "COO" / ".claude" / "settings.json"),
        ]

        for domain, settings_path in settings_files:
            if not settings_path.exists():
                self.check(False, f"{domain} settings.json exists", is_warning=True)
                continue

            # Check valid JSON
            try:
                content = settings_path.read_text(encoding="utf-8")
                settings = json.loads(content)
            except json.JSONDecodeError as e:
                self.check(False, f"{domain} settings.json valid JSON - ERROR: {e}")
                continue

            # Check SessionStart hook configured
            has_session_start = (
                "hooks" in settings and
                "SessionStart" in settings.get("hooks", {})
            )
            self.check(has_session_start, f"{domain} has SessionStart hook")

            # Check for hardcoded paths
            content_lower = content.lower()
            has_hardcoded = "/users/" in content_lower or "/home/" in content_lower
            if has_hardcoded:
                self.check(False, f"{domain} no hardcoded paths", is_warning=True)

    def check_learnings_structure(self):
        print("\n📚 Learnings Structure:")

        learnings_dir = self.project_path / "docs" / "learnings"

        if not learnings_dir.exists():
            self.check(False, "docs/learnings/ directory exists")
            if self.fix_mode:
                learnings_dir.mkdir(parents=True, exist_ok=True)
                print("       → Fixed: Created docs/learnings/")
        else:
            self.check(True, "docs/learnings/ directory exists")

        # Check subdirectories
        subdirs = ["workflows", "decisions", "gotchas"]
        for subdir in subdirs:
            subdir_path = learnings_dir / subdir
            if subdir_path.exists():
                count = len(list(subdir_path.glob("*.md")))
                self.check(True, f"{subdir}/ exists ({count} files)")
            else:
                self.check(False, f"{subdir}/ exists", is_warning=True)
                if self.fix_mode:
                    subdir_path.mkdir(parents=True, exist_ok=True)
                    print(f"       → Fixed: Created {subdir}/")

        # Check README
        readme = learnings_dir / "README.md"
        if readme.exists():
            size = readme.stat().st_size
            self.check(size > 100, f"README.md has content ({size} bytes)")
        else:
            self.check(False, "README.md exists")

    def check_index_sync(self):
        print("\n🔗 Index Synchronization:")

        learnings_dir = self.project_path / "docs" / "learnings"
        readme = learnings_dir / "README.md"

        if not readme.exists():
            self.check(False, "Cannot check - README.md missing", is_warning=True)
            return

        index_content = readme.read_text().lower()
        unindexed = []

        # Check each .md file is referenced in index
        for md_file in learnings_dir.rglob("*.md"):
            if md_file.name == "README.md":
                continue
            relative = md_file.relative_to(learnings_dir)
            if str(relative).lower() not in index_content:
                unindexed.append(str(relative))

        if unindexed:
            for f in unindexed:
                self.check(False, f"{f} not in README.md", is_warning=True)
        else:
            self.check(True, "All files indexed in README.md")

    def check_hook_execution(self):
        print("\n🧪 Hook Execution Test:")

        hook_path = self.project_path / ".claude" / "hooks" / "session_start.py"

        if not hook_path.exists():
            self.check(False, "Cannot test - hook file missing")
            return

        try:
            # Set environment variable
            env = os.environ.copy()
            env["CLAUDE_PROJECT_DIR"] = str(self.project_path)

            # Run hook with test input
            result = subprocess.run(
                ["uv", "run", str(hook_path)],
                input='{"source": "startup", "session_id": "health-check", "cwd": "' + str(self.project_path) + '"}',
                capture_output=True,
                text=True,
                timeout=10,
                cwd=str(self.project_path),
                env=env
            )

            # Check exit code
            self.check(result.returncode == 0, f"Hook exits cleanly (code {result.returncode})")

            # Check for output
            has_output = len(result.stdout.strip()) > 0
            self.check(has_output, "Hook produces output", is_warning=not has_output)

            if has_output:
                lines = result.stdout.strip().split("\n")
                # Filter out uv metadata lines
                lines = [l for l in lines if not l.startswith("Reading inline")]
                print(f"     ℹ️  Output preview ({len(lines)} lines):")
                for line in lines[:3]:
                    print(f"        {line[:55]}{'...' if len(line) > 55 else ''}")
                if len(lines) > 3:
                    print(f"        ... and {len(lines) - 3} more lines")

        except subprocess.TimeoutExpired:
            self.check(False, "Hook completes within 10 seconds")
        except Exception as e:
            self.check(False, f"Hook execution - ERROR: {e}")

    def check_claude_md(self):
        print("\n📝 CLAUDE.md Integration:")

        claude_md = self.project_path / "CLAUDE.md"

        if not claude_md.exists():
            self.check(False, "CLAUDE.md exists", is_warning=True)
            return

        self.check(True, "CLAUDE.md exists")

        content = claude_md.read_text(encoding="utf-8").lower()

        # Check for memory system documentation
        has_working_ref = "working.md" in content
        has_learnings_ref = "learnings" in content

        self.check(has_working_ref, "References WORKING.md", is_warning=not has_working_ref)
        self.check(has_learnings_ref, "References learnings/", is_warning=not has_learnings_ref)

    def print_summary(self):
        print(f"\n{'='*60}")
        print("  SUMMARY")
        print('='*60)

        total = self.passed + self.failed + self.warnings

        print(f"\n  ✅ Passed:   {self.passed}/{total}")
        print(f"  ❌ Failed:   {self.failed}/{total}")
        print(f"  ⚠️  Warnings: {self.warnings}/{total}")

        if self.failed == 0:
            print("\n  🎉 System is healthy!")
            if self.warnings > 0:
                print("     (Some optional improvements suggested above)")
        else:
            print("\n  🔧 Some fixes needed - see failed checks above")
            if not self.fix_mode:
                print("     Run with --fix to auto-repair missing files")

        print()
        return self.failed == 0


def main():
    fix_mode = "--fix" in sys.argv

    # Get project path
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if args:
        project_path = Path(args[0]).resolve()
    else:
        project_path = Path.cwd()

    # Try to find PROMAN_OS root
    if not (project_path / ".claude").exists():
        if (project_path.parent / ".claude").exists():
            project_path = project_path.parent
        else:
            print(f"⚠️  Warning: No .claude directory found at {project_path}")
            print("   Make sure you're running this from your PROMAN_OS root directory")
            print()

    # Run health check
    checker = HealthCheck(project_path, fix_mode)
    checker.run_all()

    # Exit with appropriate code
    sys.exit(0 if checker.failed == 0 else 1)


if __name__ == "__main__":
    main()
