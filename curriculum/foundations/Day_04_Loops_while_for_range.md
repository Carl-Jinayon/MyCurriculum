# Day 4 — Loops: while, for, range, and Iteration Patterns

## Objective
- Understand when and how to repeat code with `while` and `for` loops
- Master `range()` for counting, stepping, and reversing
- Use `break`, `continue`, and `else` clauses on loops
- Apply loops to common patterns: accumulation, searching, validation retries
- Avoid infinite loops and off-by-one errors

## Prerequisites
- Day 3: conditionals, comparisons, boolean logic, input validation

## Why This Matters
Without loops, every repetition requires copy-paste — unmaintainable and error-prone. Loops are the first construct that lets you write code whose *size* depends on *data*, not on how many lines you typed. They are the gateway to algorithms, data processing, and every program that handles "one of each" or "keep going until done."

## Mental Models

### A Loop Is a Question Repeated
A loop body runs, then the condition is checked again. The loop is the answer to: "Should I do this again?"

### Indentation Still Defines the Block
Everything indented under `while` or `for` is the loop body. Wrong indentation = wrong program.

### The Loop Variable Changes
In a working loop, something changes each iteration that eventually makes the condition false (for `while`) or exhausts the sequence (for `for`). If nothing changes, you have an infinite loop.

## while Loops

```python
count = 0
while count < 5:
    print(count)
    count += 1          # something MUST change
```

Three parts to check:
1. **Initialization** — `count = 0` before the loop
2. **Condition** — `count < 5` checked before each iteration
3. **Update** — `count += 1` inside the loop, moving toward false

### Common while Patterns

**Accumulator (sum, product, count):**
```python
total = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))
print(f"Sum: {total}")
```

**Retry until valid (input validation loop):**
```python
raw = input("Enter a positive integer: ")
while not raw.isdigit():
    print("Invalid. Try again.")
    raw = input("Enter a positive integer: ")
number = int(raw)
print(f"You entered {number}")
```

**Counting down:**
```python
n = 10
while n > 0:
    print(n)
    n -= 1
print("Liftoff!")
```

## for Loops and range()

`for` iterates over a sequence. `range()` produces integer sequences.

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step = 2)
    print(i)

for i in range(5, 0, -1):   # 5, 4, 3, 2, 1 (reverse)
    print(i)
```

`range(start, stop, step)` — `start` inclusive, `stop` exclusive. Default start=0, step=1.

### for over other sequences
```python
for char in "hello":        # iterate characters
    print(char)

items = ["apple", "banana", "cherry"]
for item in items:          # iterate list
    print(item)
```

## break, continue, and Loop else

```python
# break — exit the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)          # prints 0..4

# continue — skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)          # prints 0, 1, 3, 4

# else on loops — runs ONLY if loop completed WITHOUT break
for i in range(5):
    if i == 3:
        break
else:
    print("Loop finished normally")   # NOT printed (break happened)

for i in range(5):
    print(i)
else:
    print("Loop finished normally")   # printed (no break)
```

The `else` clause is rare but useful for search patterns:
```python
for item in items:
    if item == target:
        print("Found!")
        break
else:
    print("Not found")
```

## Nested Loops

```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

The inner loop runs to completion for each outer iteration.

## Common Mistakes
- **Infinite loop** — forgot to update the loop variable, or condition never becomes false
- **Off-by-one** — `range(5)` gives 0..4, not 1..5; `while i <= 5` vs `while i < 5`
- **Modifying the sequence you're iterating over** — don't `append`/`remove` from a list while looping over it
- **break only exits the innermost loop** — use flags or functions for multi-level exits
- **Using `while` when `for` is clearer** — `for i in range(n)` is usually better than manual counter

## Verification Checklist
- [ ] I can write a `while` loop that counts 1 to 10
- [ ] I can write a `for` loop with `range` that counts 10 down to 1
- [ ] I can write an input-validation retry loop
- [ ] I can explain what `break`, `continue`, and `else` on a loop do
- [ ] I can trace through a nested loop and predict the output

## Exercises (exercises/day_04/)
1. `countdown.py` — ask for a positive integer N, count down from N to 1, print "Liftoff!"
2. `sum_until_zero.py` — repeatedly ask for numbers, sum them, stop when user enters 0, print total
3. `multiplication_table.py` — ask for N, print N×1 through N×10 (use `for` + `range`)
4. `guess_game.py` — computer picks random 1-100 (use `random.randint`), user guesses; loop until correct; print "Too high" / "Too low" / "Correct! Attempts: X"
5. `pattern_printer.py` — nested loops: print a right triangle of asterisks, height N (ask for N)
6. `validation_retry.py` — ask for an integer between 1 and 100; loop until valid; print the valid number

## Build
`guess_game.py` done well is today's build: uses `random.randint`, clean retry loop, tracks attempt count, handles invalid input gracefully (non-integers). Tomorrow, functions will let you turn it into a reusable component.

## AI Interaction
Good prompts for loops:
- "My while loop runs forever — here's my code. What variable am I forgetting to update?"
- "I want to count down from N to 1 with a for loop. What range arguments do I need?"
- "How does the else clause on a for loop work? When does it run?"
- Do NOT ask "write a loop that does X" — build the skeleton yourself first

## Mastery Check (from memory)
1. Write a program: ask for a positive integer N, compute and print the sum of 1 + 2 + ... + N using a loop.
2. What does `range(1, 10, 2)` produce? What about `range(10, 1, -1)`?
3. Trace this by hand, then run to verify:
   ```python
   for i in range(3):
       for j in range(2):
           print(i, j)
   ```
4. When does a `for` loop's `else` block run?

## Reflection
- Did you write the loop condition first, then the body, or the body first? Both work — which felt safer?
- Did any infinite loop happen? What was missing?
- How did you handle invalid input in `guess_game.py`?

## Key Takeaways
- `while` = "repeat while condition is true" — you control the variable
- `for` + `range()` = "repeat for each value in this sequence" — Python handles the variable
- `break` exits, `continue` skips, `else` runs if no break
- Always trace the first, last, and one middle iteration before running
- Input validation loops are the first security pattern you'll use everywhere