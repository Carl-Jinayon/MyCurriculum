# Day 6 Cheat Sheet — Lists

## Creation & Access
```python
a = [1, 2, 3]
a[0]        # 1 (first)
a[-1]       # 3 (last)
a[1:3]      # [2, 3]  (1 to 2)
a[:2]       # [1, 2]
a[1:]       # [2, 3]
a[::2]      # [1, 3]  (every 2nd)
a[::-1]     # [3, 2, 1] (reversed)
```

## Methods (mutate in place, return None unless noted)
| Method | Effect | Returns |
|---|---|---|
| `append(x)` | add x to end | None |
| `extend(iter)` | add all from iter | None |
| `insert(i, x)` | insert at i | None |
| `pop([i])` | remove & return at i (default last) | item |
| `remove(x)` | remove first x | None |
| `index(x)` | first index of x | int |
| `count(x)` | occurrences of x | int |
| `sort()` | sort in place | None |
| `reverse()` | reverse in place | None |
| `copy()` | shallow copy | new list |

## Sorting
```python
a.sort()          # mutates a, returns None
b = sorted(a)     # returns new sorted list, a unchanged
```

## Iteration
```python
for x in a: ...
for i, x in enumerate(a): ...
for i, x in enumerate(a, 1): ...
for x in reversed(a): ...
for x, y in zip(a, b): ...
```

## List Comprehension
```python
[x*2 for x in a]           # map
[x for x in a if x > 0]    # filter
[x*2 for x in a if x > 0]  # map + filter
```

## Nested Lists
```python
grid = [[1,2],[3,4]]
grid[0][1]   # 2
for row in grid:
    for cell in row: ...
```

## Aliasing vs Copying
```python
b = a          # alias — SAME list
b = a[:]       # copy
b = a.copy()   # copy
b = list(a)    # copy
```

## Common Pitfalls
- `a.sort()` returns None — don't write `b = a.sort()`
- Mutating while iterating skips items → build new list
- Default mutable arg: `def f(x=[])` → bug; use `x=None`
- `a = [1]*3` → `[1,1,1]` but `a = [[]]*3` → same inner list 3x

## Must-Know Checklist
- [ ] Index, slice, negative indices
- [ ] All core methods + what they return
- [ ] Aliasing vs copy
- [ ] List comprehension map/filter
- [ ] Nested list access
- [ ] Ran all 6 exercises

## Active Recall
1. `a = [1,2,3]; b = a; b[0]=9` — what is `a`?
2. `a = [1,2,3,4]` — `a[1:3]`? `a[::-1]`?
3. `list.sort()` vs `sorted(list)` — difference?
4. Write comprehension: even numbers from `[-2, 1, 4, -3, 6]`
5. How to copy a list safely?