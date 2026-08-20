# Day 4 Advanced — Loops, Iteration Patterns, and Exploring

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### The `else` clause on `try` and `for` — a family
```python
try:
    risky()
except SomeError:
    handle()
else:
    print("No error")      # runs if NO exception
finally:
    print("Always")        # cleanup
```

```python
for item in items:
    if found(item):
        break
else:
    print("Not found")     # runs if NO break
```

Both `else` clauses mean "the *normal* path completed without an early exit (exception or break)." This symmetry is intentional.

### `enumerate()` — index + value together
```python
for i, char in enumerate("hello"):
    print(i, char)    # 0 h, 1 e, 2 l, 3 l, 4 o
```

```python
for i, item in enumerate(items, start=1):   # 1-based
    print(f"{i}. {item}")
```

### `zip()` — iterate multiple sequences in parallel
```python
names = ["A", "B", "C"]
scores = [90, 85, 80]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

Stops at the shortest sequence.

### Infinite loops on purpose — servers, event loops
```python
while True:
    event = get_next_event()
    process(event)
```
Must have a `break` condition or signal handler to exit gracefully.

### Loop invariants — the formal way to reason about loops
An invariant is a statement that is true:
1. Before the first iteration
2. After each iteration (if it was true before, it's true after)
3. After the loop terminates

Example — sum of 1..n:
```python
total = 0
i = 1
while i <= n:
    total += i
    i += 1
# Invariant: total == sum(1..i-1)
# Loop ends when i == n+1 → total == sum(1..n)
```

This is how you prove algorithms correct. You'll meet it in algorithms (Stage 1).

### List comprehensions — loop as expression (preview)
```python
squares = [x * x for x in range(10)]     # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(10) if x % 2 == 0]
```
Syntactic sugar for a common accumulator pattern. You'll use these heavily.

### `itertools` — power tools for iteration (when you need them)
```python
import itertools

itertools.count(5)           # 5, 6, 7, 8... infinite
itertools.cycle([1,2,3])     # 1,2,3,1,2,3... infinite
itertools.repeat(7, 3)       # 7, 7, 7
itertools.islice(range(100), 5, 15)  # slice an iterator
```
Import only when you need them — don't pre-load.

## 2. Explore-It-Yourself Guide

Predict, run, reflect:

1. `for i in range(3): pass` then `print(i)` — what is `i` after the loop? (Leaks! Loop variable persists in Python.)
2. `for i in range(3): break` then `print(i)` — what is `i`?
3. `for _ in range(5): pass` — the `_` convention for "I don't need this variable." Run it.
4. Write a loop that prints all even numbers from 20 down to 2. Two ways: `range(20, 1, -2)` vs `range(20, 0, -1)` with `if i % 2 == 0: continue`. Compare.
5. `for x in []: print("hi")` then `print("done")` — what happens? Empty sequence = body never runs.
6. In the REPL, `help(range)` — read the signature. Then `dir(range)` — what methods does a range object have?

### Research loop
Hypothesis → experiment → evidence. The best way to internalize loop behavior is to make a guess, run a 3-line script, and check.

## 3. Where This Leads Later
- Loops → Day 5 functions (loops inside functions, functions called in loops)
- Loop invariants → algorithms, correctness proofs
- `enumerate`/`zip`/`comprehensions` → everyday Python, data processing
- `itertools` → large datasets, generators, pipelines (Stage 2+)
- Pattern: accumulate → map → filter → reduce → the functional core of data work (ML later)

## Final Rule
Optional files never gate your progress. Master the main lesson, satisfy curiosity here, and move on.