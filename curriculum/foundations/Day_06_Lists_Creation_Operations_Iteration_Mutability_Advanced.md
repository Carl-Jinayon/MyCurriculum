# Day 6 Advanced — Lists, Mutability, and Exploring

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### The aliasing trap — deeper
```python
a = [1, 2, 3]
b = a          # same list
b[0] = 99
print(a)       # [99, 2, 3] — a changed!
```

This happens because `b = a` copies the *reference*, not the list. The fix — any of:
```python
b = a[:]       # slice copy
b = a.copy()   # method copy
b = list(a)    # constructor copy
b = copy.copy(a)  # from copy module
```

All create a **shallow copy** — new outer list, but inner objects still shared. For nested lists:
```python
a = [[1, 2], [3, 4]]
b = a[:]           # shallow
b[0][0] = 99
print(a)           # [[99, 2], [3, 4]] — inner changed!
```

For nested structures, need **deep copy**:
```python
import copy
b = copy.deepcopy(a)
```

### Default mutable arguments — the classic bug
```python
def add_item(item, shopping_list=[]):
    shopping_list.append(item)
    return shopping_list

print(add_item("apple"))   # ["apple"]
print(add_item("banana"))  # ["apple", "banana"] — BUG!
```

The default `[]` is created **once** at function definition time, not each call. The fix:
```python
def add_item(item, shopping_list=None):
    if shopping_list is None:
        shopping_list = []
    shopping_list.append(item)
    return shopping_list
```

This is one of the most infamous Python gotchas — you'll see it in code reviews forever.

### List multiplication trap
```python
rows = [[0] * 3] * 3
rows[0][0] = 1
print(rows)   # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] — all rows are the SAME list!
```

`[inner] * n` repeats the *same reference* n times. Fix:
```python
rows = [[0] * 3 for _ in range(3)]  # each row is a new list
```

### `sort()` vs `sorted()` — the return value trap
```python
a = [3, 1, 2]
b = a.sort()
print(b)      # None!
print(a)      # [1, 2, 3] — a was mutated
```
`sort()` mutates in place and returns `None`. The functional version:
```python
b = sorted(a)  # returns NEW list, a unchanged
```

### List comprehensions — the three patterns
```python
# map: transform each element
[x * 2 for x in range(5)]          # [0, 2, 4, 6, 8]

# filter: keep only some
[x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]

# map + filter
[x * 2 for x in range(10) if x % 2 == 0]  # [0, 4, 8, 12, 16]

# nested
[(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
```

### `enumerate` and `zip` — the iteration power tools
```python
for i, item in enumerate(items):          # (0, item0), (1, item1)...
for i, item in enumerate(items, 1):       # 1-based index

for x, y in zip(list1, list2):            # parallel iteration
for x, y, z in zip(a, b, c):              # three at a time
```
`zip` stops at the shortest list.

### `collections.deque` — when you need fast pops from both ends
```python
from collections import deque
d = deque([1, 2, 3])
d.appendleft(0)   # O(1)
d.popleft()       # O(1) — list.pop(0) is O(n)!
```
Use `deque` for queues, BFS, sliding windows.

### Unpacking with * — gather and scatter
```python
first, *rest = [1, 2, 3, 4]      # first=1, rest=[2,3,4]
*a, last = [1, 2, 3, 4]          # a=[1,2,3], last=4
print(*names, sep=", ")           # scatter list into separate arguments
combined = [*a, *b]               # merge lists without extend
```
The `*` flips between gathering (into list) and scattering (out of list).

### The memory model — what a list really is
A Python variable is a **name tag pointing at an object**. A list is an object holding a row of pointers:
```
a ──▶ [ ptr ]──▶ 1        b = a copies the ARROW, not the boxes
       [ ptr ]──▶ 2
       [ ptr ]──▶ 3
b = a[:] builds NEW boxes and copies the pointers one level deep.
copy.deepcopy() recursively rebuilds everything.
```
This one diagram explains: aliasing, shallow vs deep copy, why `[[0]*3]*3` shares rows, and why functions can mutate the lists you pass them. It is THE mental model for Days 6–8 and beyond.

### sorted() with keys — pointer ahead
`sorted(data, key=len)` sorts by any measurement (Day 7 Advanced uses `key=lambda kv: kv[1]` on dicts). Park the syntax; the idea is "sort by a computed value, not the item itself."

## 2. Explore-It-Yourself Guide

Predict, run, reflect:

1. `a = [1,2,3]; b = a; b.append(4); print(a)` — what happens? Why?
2. `a = [1,2,3]; b = a[:]; b.append(4); print(a)` — different? Why?
3. `def f(x=[]): x.append(1); return x; print(f()); print(f())` — observe the bug.
4. `rows = [[0]*2]*3; rows[0][0]=1; print(rows)` — explain the output.
5. `a = [3,1,2]; b = a.sort(); print(b)` — why is `b` None?
6. `a = [3,1,2]; b = sorted(a); print(b); print(a)` — difference?
7. Write a list comprehension: all squares of even numbers 0–20.
8. In REPL: `help(list)` — read the method list. Pick 3 you've never used and experiment.

## 3. Where This Leads Later
- Lists → Day 7: tuples, sets, dicts (other collections)
- Aliasing → Day 8: mutable vs immutable in function arguments
- Comprehensions → data processing pipelines, pandas, ML preprocessing
- Nested lists → matrices, images, grids (ML, graphics)
- `deque` → BFS, sliding windows, streaming (Stage 2+)
- Shallow vs deep copy → serialization, caching, immutability patterns

## Final Rule
Optional files never gate your progress. Master the main lesson, satisfy curiosity here, and move on.