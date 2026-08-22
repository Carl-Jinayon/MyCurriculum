# Review Day 1 — Cumulative Review (Days 1–5)

> **Rules:** AI-free. No AI assistance. No notes. From memory only.
> Write each solution in `exercises/review_day/` and run to verify.

---

## Exercise 1: Basics + Types + F-strings
**File:** `review_basics.py`

**Requirements:**
- Ask for name (string), age (int), height in meters (float)
- Print one f-string: `"Name: {name}, Age: {age}, Height: {height}m"`
- Print the *types* of each variable using `type()`

---

## Exercise 2: Conditionals + Validation
**File:** `review_validator.py`

**Requirements:**
- Ask for a number between 1 and 100 (inclusive)
- Validate: must be digits only, and in range
- If invalid, loop until valid
- If valid, print whether it's:
  - Divisible by 3 only → "Fizz"
  - Divisible by 5 only → "Buzz"
  - Both 3 and 5 → "FizzBuzz"
  - Neither → the number itself

---

## Exercise 3: Loops + Accumulator
**File:** `review_sum.py`

**Requirements:**
- Ask for N (positive integer, validate)
- Use a `for` loop with `range` to compute sum of 1 to N
- Print the sum
- Also print the sum using the formula `N*(N+1)//2` — verify they match

---

## Exercise 4: Functions + Scope
**File:** `review_functions.py`

**Requirements:**
- Define `factorial(n)` that returns n! (use a loop, not recursion)
- Define `is_even(n)` returning `True`/`False`
- In a `main()` function:
  - Ask for a positive integer N (validate)
  - Print N!
  - Print whether N! is even or odd
- Call `main()` under `if __name__ == "__main__":`

---

## Exercise 5: Nested Loops + Pattern
**File:** `review_pattern.py`

**Requirements:**
- Ask for height H (positive integer, validate)
- Print a left-aligned triangle of height H using `*`
- Example H=4:
```
*
**
***
****
```

---

## Exercise 6: Integration — Mini Calculator (no `try/except`)
**File:** `review_calc.py`

**Requirements:**
- Functions: `add`, `sub`, `mul`, `div` (handle divide by zero → return `None`)
- `get_number(prompt)` — loops until valid float (use the `try/except` pattern — this is the integration test)
- `main()`:
  - Get two numbers
  - Ask for operation (+ - * /)
  - Call appropriate function
  - Print result or error message
- Call `main()` under `if __name__ == "__main__":`

---

## Mistake Log Re-tests

Re-test **every** entry in your `notes/mistakes/mistake_log.md` (if any). For each:
1. Write a tiny script that would have triggered the old mistake
2. Show the correct behavior now
3. Explain the correct mental model in one sentence

---

## Documentation

Create `README.md` with:
- Date
- Which exercises passed on first run
- Which needed fixes (and what the fix was)
- Any mistake-log entries that still trip you up

---

## Verification Checklist
- [ ] All 6 exercises run without errors
- [ ] All outputs match expectations
- [ ] Mistake log re-tests completed (if any entries exist)
- [ ] README.md filled out
- [ ] All files in `exercises/review_day/`