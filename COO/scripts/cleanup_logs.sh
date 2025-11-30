#!/bin/bash
# cleanup_logs.sh - Delete log files older than 7 days
# Usage: ./scripts/cleanup_logs.sh [--dry-run]
#
# Run with --dry-run to see what would be deleted without actually deleting

set -e

# Get script directory and project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Check for dry-run mode
DRY_RUN=false
if [[ "$1" == "--dry-run" ]]; then
    DRY_RUN=true
    echo "=== DRY RUN MODE - No files will be deleted ==="
    echo ""
fi

# Define log directories to clean (relative to project root)
LOG_DIRS=(
    "logs"
    ".claude/skills/logs"
    ".claude/skills/docx/logs"
    "ai_docs/logs"
    "projects/_TEMPLATE_PMP_PROJECT/logs"
)

# Track counts
TOTAL_FILES=0
TOTAL_DIRS=0

echo "Cleaning logs older than 7 days..."
echo "Project root: $PROJECT_ROOT"
echo ""

for LOG_DIR in "${LOG_DIRS[@]}"; do
    FULL_PATH="$PROJECT_ROOT/$LOG_DIR"

    if [[ -d "$FULL_PATH" ]]; then
        echo "--- Checking: $LOG_DIR ---"

        # Find and delete files older than 7 days (excluding README.md and .gitignore)
        while IFS= read -r -d '' file; do
            # Skip README.md and .gitignore files
            filename=$(basename "$file")
            if [[ "$filename" == "README.md" || "$filename" == ".gitignore" || "$filename" == ".DS_Store" ]]; then
                continue
            fi

            ((TOTAL_FILES++))
            if [[ "$DRY_RUN" == true ]]; then
                echo "  Would delete: $file"
            else
                rm -f "$file"
                echo "  Deleted: $file"
            fi
        done < <(find "$FULL_PATH" -type f -mtime +7 -print0 2>/dev/null)

        # Find and delete empty directories (after files are removed)
        if [[ "$DRY_RUN" == false ]]; then
            while IFS= read -r -d '' dir; do
                if [[ -d "$dir" && "$dir" != "$FULL_PATH" ]]; then
                    rmdir "$dir" 2>/dev/null && {
                        ((TOTAL_DIRS++))
                        echo "  Removed empty dir: $dir"
                    } || true
                fi
            done < <(find "$FULL_PATH" -type d -empty -print0 2>/dev/null)
        fi
    else
        echo "--- Skipping (not found): $LOG_DIR ---"
    fi
    echo ""
done

echo "=== Summary ==="
if [[ "$DRY_RUN" == true ]]; then
    echo "Files that would be deleted: $TOTAL_FILES"
    echo ""
    echo "Run without --dry-run to actually delete files."
else
    echo "Files deleted: $TOTAL_FILES"
    echo "Empty directories removed: $TOTAL_DIRS"
fi
