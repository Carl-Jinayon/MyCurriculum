#!/usr/bin/env bash
# SYNC CHECK — run at session start and after lesson completion.
# Flags stale/duplicate/inconsistent curriculum documentation.

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[0;33m'; NC='\033[0m'
pass() { echo -e "${GREEN}PASS${NC}: $1"; }
warn() { echo -e "${YELLOW}WARN${NC}: $1"; }
fail() { echo -e "${RED}FAIL${NC}: $1"; }

cd "$(dirname "$0")/.." || exit 1

echo "=== CURRICULUM SYNC CHECK ==="

# 1. State file updated recently (date line matches a recent edit)
state_date=$(grep -m1 "^Updated:" notes/curriculum_state.md | grep -oE "[0-9]{4}-[0-9]{2}-[0-9]{2}")
last_commit=$(git log -1 --format=%cs 2>/dev/null)
if [ -z "$last_commit" ] || [[ "$state_date" > "$last_commit" || "$state_date" == "$last_commit" ]]; then
    pass "curriculum_state.md date ($state_date) >= last commit ($last_commit)"
else
    warn "state date ($state_date) older than last commit ($last_commit) — state may be stale"
fi

# 2. No duplicate 'Current objective' lines in README
n=$(grep -c "Current objective" README.md)
if [ "$n" -le 1 ]; then pass "README has single Current objective line"; else fail "README has $n duplicate objective lines"; fi

# 3. Handoff 'Where we are NOW' exists and mentions the latest completed Day from state
latest_day=$(sed -n '/## Completed Objectives/,/^## /p' notes/curriculum_state.md | grep -oE "Day [0-9]+" | grep -oE "[0-9]+" | sort -n | tail -1)
if grep -q "Where we are NOW" notes/CONTEXT_HANDOFF.md; then
    if [ -n "$latest_day" ] && grep -q "Day ${latest_day}" notes/CONTEXT_HANDOFF.md; then
        pass "handoff references latest Day (${latest_day})"
    else
        warn "handoff does not mention Day ${latest_day} — 'Where we are NOW' may be stale"
    fi
else
    fail "handoff missing 'Where we are NOW' section"
fi

# 4. Every main lesson has HARD MODE
missing=0
for f in curriculum/foundations/Day_*.md curriculum/mathematics/Math_*.md; do
    case "$f" in *CheatSheet*|*Advanced*) continue ;; esac
    if ! grep -q "HARD MODE" "$f"; then echo "  missing HARD MODE: $f"; missing=$((missing+1)); fi
done
if [ "$missing" -eq 0 ]; then pass "all main lessons contain HARD MODE"; else fail "$missing lesson(s) missing HARD MODE"; fi

# 5. Lesson file triples complete (main implies CheatSheet + Advanced exist)
incomplete=0
for f in curriculum/foundations/Day_*.md curriculum/mathematics/Math_*.md; do
    case "$f" in *CheatSheet*|*Advanced*) continue ;; esac
    base="${f%.md}"
    [ -f "${base}_CheatSheet.md" ] || { echo "  missing: ${base}_CheatSheet.md"; incomplete=$((incomplete+1)); }
    [ -f "${base}_Advanced.md" ]   || { echo "  missing: ${base}_Advanced.md";   incomplete=$((incomplete+1)); }
done
if [ "$incomplete" -eq 0 ]; then pass "all lessons have CheatSheet + Advanced files"; else fail "$incomplete companion file(s) missing"; fi

# 6. Exercise directories have matching lesson files
orphan=0
for d in exercises/Foundations/day_* exercises/Math/math_*; do
    [ -d "$d" ] || continue
    # skip if directory is empty (nothing done yet)
    [ -n "$(ls -A "$d" 2>/dev/null)" ] || continue
    num=$(basename "$d" | grep -oE "[0-9]+")
    case "$d" in
        *Foundations*) pat="curriculum/foundations/Day_${num}_*.md" ;;
        *Math*)        pat="curriculum/mathematics/Math_${num}_*.md" ;;
    esac
    ls $pat >/dev/null 2>&1 || { echo "  orphan exercise dir (no lesson): $d"; orphan=$((orphan+1)); }
done
if [ "$orphan" -eq 0 ]; then pass "all non-empty exercise dirs have matching lessons"; else fail "$orphan orphan exercise dir(s)"; fi

# 7. Uncommitted changes reminder
if [ -n "$(git status --porcelain)" ]; then
    warn "uncommitted changes exist — commit after verification:"
    git status --short | head -8
else
    pass "working tree clean"
fi

echo "=== DONE ==="
