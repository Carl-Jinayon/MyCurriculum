# Day 7 Advanced — Tuples, Sets, Dicts, Deeper

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### Hash tables — WHY dict/set lookups are fast
Lists search one-by-one: checking `x in big_list` walks every element (slow at scale).
Dicts and sets use a **hash table**: the key is run through a function that computes its
"drawer number" directly — lookup time stays constant even with millions of keys.

That is also WHY keys must be immutable: a mutable key's hash would change, and its drawer
would no longer match. Lists can't be hashed; tuples/frozensets/strings/numbers can.
You will meet hash tables again as the theory behind Stage 1's hash-map data structure.

### frozenset — the immutable set
```python
fs = frozenset([1, 2, 3])     # like tuple : set :: frozenset : set
fs.add(4)                     # AttributeError — frozen
```
Use case: a set that must not change (e.g., allowed permissions), or a set used as a dict key.

### Tuple tricks you'll see in real code
```python
# swap without temp (you saw this in Day 2 Advanced)
a, b = b, a

# functions returning multiple values ARE tuples
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # unpack on arrival

# enumerate/zip hand you tuples
for i, item in enumerate(items):   # i, item IS a tuple being unpacked
```

### dict methods beyond .get()/.items()
```python
d.setdefault("visits", []).append(today)   # get-or-create pattern
d.pop("key")            # remove AND return value
d | {"new": 1}          # merge into NEW dict (3.9+)
d.update(other)         # merge other INTO d
```

The `setdefault` line is the pro version of your counting pattern:
```python
counts[word] = counts.get(word, 0) + 1        # yours — fine
counts.setdefault(word, 0); counts[word] += 1 # equivalent
from collections import Counter
counts = Counter(words_list)                  # built-in counter machine
```

`collections.Counter` does word frequency in ONE line — but write yours first; libraries
are rewards for understanding, not replacements for it.

### Sorting dicts and sets
```python
sorted(d.items())                       # by key
sorted(d.items(), key=lambda kv: kv[1], reverse=True)   # by value, descending
top3 = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:3]
```
`lambda kv: kv[1]` = "sort by the value part" — tiny anonymous function; full lambda
treatment comes later. Park the pattern.

### Set comprehension + dict comprehension (you know list ones)
```python
{s.lower() for s in words}              # set comprehension → unique lowered
{w: len(w) for w in words}              # dict comprehension → word→length
{n * n for n in range(5)}               # {0, 1, 4, 9, 16}
```

### Truthiness of containers
```python
bool([])      # False      bool({})    # False
bool((0,))    # True       bool({"a":1})  # True
```
Empty container = falsy. Powers the idiom: `if not results: print("none found")`.

## 2. Explore-It-Yourself Guide

Predict, run, reflect:

1. `t = (1, [2, 3]); t[1].append(4)` — wait, tuples are immutable... why did this WORK? (Immutability protects the reference, not the inner list. Deep idea.)
2. `d = {}; d[[1,2]] = "x"` vs `d[(1,2)] = "x"` — one crashes. Read the error word for word.
3. Time test: build a list AND a set of 100,000 numbers; time `99999 in list` vs `in set` using `time.perf_counter()` around each. Feel the hash table difference.
4. `Counter("mississippi")` — inspect the result. Then rebuild it yourself with YOUR counting loop and compare dictionaries.
5. `{True: "yes", 1: "one", 1.0: "uno"}` — how many keys? Why? (Hash surprise!)
6. Write dict comprehension mapping each letter of your name to its alphabet position.

## 3. Where This Leads Later
- Hash tables → Stage 1 data structures (hash maps), databases' indexes (Stage 2)
- Nested dicts → JSON — the language of web APIs and LLM tool calls (Stage 3–4)
- Sets → deduplicating training data, tag systems, permissions (AI security thread)
- Tuples as records → database rows, structured outputs from models
- Counter/sorting patterns → analytics, dashboards, ML data prep

## Final Rule
Optional files never gate your progress. Master the main lesson, satisfy curiosity here, and move on.