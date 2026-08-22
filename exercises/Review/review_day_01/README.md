# Review Day 1 — Results

**Date:** 2026-08-22

## Exercises — Pass/Fail

| Exercise | File | First Run | Fix Needed? | Fix Description |
|---|---|---|---|---|
| 1. Basics + Types | `review_basics.py` | ✅ Pass | No | — |
| 2. Conditionals + Validation | `review_validator.py` | ✅ Pass | No | — |
| 3. Loops + Accumulator | `review_sum.py` | ✅ Pass | No | — |
| 4. Functions + Scope | `review_functions.py` | ❌ Fail | Yes | Fixed: checked factorial result instead of input number |
| 5. Nested Loops + Pattern | `review_pattern.py` | ✅ Pass | No | — |
| 6. Mini Calculator | `review_calc.py` | ✅ Pass | No | — |

## Fixes Applied

**Exercise 4 (review_functions.py):**
- **Bug:** Checked if input number was even/odd instead of the factorial result
- **Fix:** Changed `is_even(number)` to `is_even(factorial(number))` in `main()`
- **Verified:** Input `5` now correctly prints "Factorial is even." (5! = 120, even)

## Mistake Log Re-tests

- Mistake log is currently empty — no re-tests needed.

## Summary

All 6 exercises pass after fix. Review Day 1 complete.