# Day 6 — Lists: Creation, Operations, Iteration, Mutability

## Objective
- Create lists and understand them as ordered, mutable sequences
- Master indexing, slicing, and negative indices
- Use core list methods (`append`, `extend`, `pop`, `remove`, `index`, `count`, `sort`, `reverse`)
- Iterate with `for` loops and understand mutability
- Work with nested lists (matrices, grids)
- Avoid common pitfalls (aliasing, mutating while iterating)

## Prerequisites
- Day 5: functions, loops, conditionals

## Why This Matters
Lists are the workhorse data structure in Python. Every real program — web apps, data pipelines, ML pipelines, games — uses lists to store collections of data. Understanding list mutability, aliasing, and iteration patterns is the difference between code that works and code that corrupts data silently. Lists are also the gateway to all other data structures (stacks, queues, sets, dictionaries).

## Mental Models

### 1. List = Ordered Sequence of Boxes
A list is a sequence of *references* to objects. Each position (index) holds a reference.
```python
scores = [85, 92, 78, 90]
# index:   0   1   2   3
```
The list itself is mutable — you can change what's in each box.

### 2. Indexing = Addressing Boxes
- Positive: `0` = first, `1` = second, ...
- Negative: `-1` = last, `-2` = second-to-last, ...
- Out of bounds → `IndexError`

### 3. Slicing = Extracting Sub-sequences
`list[start:stop:step]` — `start` inclusive, `stop` exclusive, `step` default 1.
```python
scores[1:3]    # [92, 78]  (indices 1, 2)
scores[:3]     # [85, 92, 78]  (from start to index 2)
scores[2:]     # [78, 90]  (index 2 to end)
scores[::2]    # [85, 78]  (every 2nd)
scores[::-1]   # [90, 78, 92, 85]  (reversed)
```

### 4. Mutability = Lists Change In Place
```python
a = [1, 2, 3]
b = a          # b REFERS to the SAME list
b[0] = 99
print(a)       # [99, 2, 3] — a changed too!
```
This is **aliasing** — two names, one list. The fix: `b = a[:]` (shallow copy) or `b = a.copy()`.

## List Methods

| Method | Effect | Returns |
|---|---|---|
| `append(x)` | add x to end | `None` |
| `extend(iterable)` | add all items from iterable | `None` |
| `insert(i, x)` | insert x at index i | `None` |
| `pop([i])` | remove and return item at i (default last) | item |
| `remove(x)` | remove first occurrence of x | `None` |
| `index(x)` | index of first x | int |
| `count(x)` | occurrences of x | int |
| `sort()` | sort in place | `None` |
| `reverse()` | reverse in place | `None` |
| `copy()` | shallow copy | new list |

**Key rule:** Methods that modify the list return `None`, not the list. This is a common trap:
```python
a = [3, 1, 2]
b = a.sort()      # b is None! a is now [1, 2, 3]
```
Correct:
```python
a.sort()
b = a[:]          # or b = sorted(a) which returns new list
```

## Iteration Patterns

```python
# Basic
for item in items:
    print(item)

# With index
for i, item in enumerate(items):
    print(i, item)

# With index starting at 1
for i, item in enumerate(items, start=1):
    print(f"{i}. {item}")

# Reverse iteration
for item in reversed(items):
    print(item)

# Multiple lists in parallel
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## Nested Lists = Grids / Matrices

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

grid[1][2]    # 6  (row 1, col 2)
grid[0][0]    # 1

for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()
```

## Common Pitfalls

1. **Mutating while iterating** — don't `remove`/`pop` inside a `for item in list` loop. Use list comprehension or build a new list.
2. **Aliasing** — `b = a` shares the list; use `b = a[:]` or `a.copy()` to copy.
3. **Default mutable arguments** — `def f(x=[])` is a bug; use `def f(x=None): x = [] if x is None else x`.
4. **`sort()` vs `sorted()`** — `sort()` mutates and returns `None`; `sorted()` returns new list.

## Verification Checklist
- [ ] I can create, index, slice, and iterate lists
- [ ] I can use all core methods and explain what they return
- [ ] I can explain aliasing and how to avoid it
- [ ] I can write nested loops for nested lists
- [ ] I ran all exercises and verified outputs

## Exercises (exercises/day_06/)
1. `list_basics.py` — create a list of 5 names; print first, last, middle (using negative index); slice first 3; print reversed.
2. `list_methods.py` — start with `[3, 1, 4, 1, 5]`; demonstrate: append 9, extend with [2, 6], pop last, remove first 1, count 1s, index of 4, sort, reverse. Print after each step.
3. `list_iteration.py` — list of 5 temperatures; print each with `enumerate` starting at 1; print max, min, average using a loop (no built-in `max`/`min`/`sum` — use accumulator).
4. `nested_lists.py` — create 3x3 multiplication table as nested list: `[[i*j for j in range(1,4)] for i in range(1,4)]`; print as grid; access center element.
5. `aliasing_demo.py` — demonstrate the aliasing bug: `a = [1,2,3]; b = a; b[0] = 99; print(a)` → then fix with `b = a[:]` and show `a` unchanged.
6. `filter_list.py` — given a list of numbers, create a new list containing only even numbers (use list comprehension and also a loop with accumulator).

## HARD MODE — Stretch Exercises (STRICTLY OPTIONAL)
Attempt ONLY after the core exercises are verified. These are deliberately harder —
they push your reasoning. Failure is fine: attempt, struggle, debug. Each must be solved
with only Day 1–6 knowledge (variables, conditionals, loops, functions, lists). No
future-topic tricks.

1. `rotate.py` — write `rotate_left(lst, k)` that returns a new list rotated left by k
   positions. Example: `rotate_left([1,2,3,4,5], 2)` → `[3,4,5,1,2]`. Handle k > len.
   Do not use `collections.deque` — use slicing.

2. `interleave.py` — write `interleave(a, b)` that merges two lists by alternating
   elements: `[1,2,3]` + `[4,5,6]` → `[1,4,2,5,3,6]`. If lengths differ, append the
   remainder of the longer list. Use `zip` and list comprehension.

3. `flatten.py` — write `flatten(nested)` that takes a list of lists (or deeper) and
   returns a single flat list. Example: `[[1,2],[3,[4,5]]]` → `[1,2,3,4,5]`. Use
   recursion (allowed since you know functions). Handle arbitrary nesting.

4. `group_consecutive.py` — given a sorted list of integers, group consecutive runs
   into sublists. Example: `[1,2,3,5,6,9]` → `[[1,2,3], [5,6], [9]]`. Use a single
   pass with accumulator pattern. This is a real-world pattern for run-length encoding.

The point of Hard Mode: these require decomposing problems into list operations you
already know — exactly the size of problem you'll decompose daily as an engineer.

## Build
`filter_list.py` done well is today's build: demonstrates list comprehension vs loop, filtering, and creating new lists without mutating original.

## AI Interaction
Good prompts:
- "My list gets modified unexpectedly when I pass it to a function — here's my code. Why?"
- "What's the difference between `a.sort()` and `sorted(a)`? Show me an example."
- "I'm removing items from a list while iterating and it skips elements. Show me the fix."
- Do NOT ask "write a list comprehension for X" — write it yourself first.

## Mastery Check (from memory)
1. What does `a = [1,2,3]; b = a; b[0] = 9` do to `a`? How do you fix it?
2. `a = [1,2,3,4,5]` — what is `a[1:4]`, `a[:3]`, `a[::-1]`?
3. What does `list.sort()` return? What about `sorted(list)`?
3. Write a loop that prints each item of `items` with its 1-based index.
4. Write a list comprehension that keeps only positive numbers from `[-2, -1, 0, 1, 2]`.

## Reflection
- Which list method was most surprising? Why?
- Did aliasing behavior surprise you? How will you remember to copy?
- When would you use list comprehension vs explicit loop?

## Key Takeaways
- Lists are ordered, mutable sequences of references
- Indexing: 0-based, negative = from end; slicing: `start:stop:step`
- Methods mutate in place and return `None` (except `pop`, `index`, `count`, `copy`)
- Aliasing: `b = a` shares the list; use `b = a[:]` or `a.copy()` to copy
- Don't mutate while iterating — build new lists instead
- List comprehensions = expressive, readable filtering/transformation