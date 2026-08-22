# Day 7 — Tuples, Sets, and Dictionaries: Choosing the Right Container

## Objective
- Understand tuples: immutable sequences, packing/unpacking, when to use them
- Understand sets: unordered unique members, fast membership, deduplication
- Understand dictionaries: key→value storage, access, iteration, nesting
- Choose the right container for a job (the decision skill)
- Avoid the classic pitfalls (single-element tuple, KeyError, unhashable keys, set indexing)

## Prerequisites
- Day 6: lists (indexing, methods, mutability, aliasing)

## Why This Matters
Lists are not the only container — they're just the first one you met. Real programs pick containers by *what job the data does*: fixed records (tuples), uniqueness and membership (sets), lookups by name (dicts). Choosing correctly makes code faster, safer, and clearer. This is also your first step toward data modeling — deciding what structure fits what reality — which is exactly what databases (Stage 2) and APIs will demand.

## Mental Models

### 1. Four Containers, Four Jobs

| Container | Ordered? | Mutable? | Duplicates? | Lookup by? | Job |
|---|---|---|---|---|---|
| list `[ ]` | yes | yes | yes | index | ordered collections that change |
| tuple `( )` | yes | **no** | yes | index | fixed records that shouldn't change |
| set `{ }` | **no** | yes | **no** | membership | uniqueness, fast "is it there?" |
| dict `{k: v}` | insertion order* | yes | keys: no | key | named lookups (phone book) |

*dicts preserve insertion order in modern Python; conceptually treat as "lookup by key."

### 2. Tuple = Sealed Box
Same indexing/slicing as lists, but sealed after creation. A tuple is a *record*: coordinates, RGB colors, (name, age) pairs. If you try to change it → `TypeError`.

### 3. Set = Bag of Unique Things
No order, no duplicates, one job: membership questions answered *fast*. Converting a list to a set instantly deduplicates it.

### 4. Dict = Labeled Drawers
A filing cabinet: each drawer has a label (key) and contents (value). You never ask "which drawer number?" — you ask "where are the keys to the car?" Lookups by name, not position.

## Tuples

```python
point = (3, 5)
color = (255, 128, 0)
person = ("Carl", 20)

print(point[0])        # 3 — indexing works like lists
print(color[-1])       # 0
a, b = point           # unpacking! a=3, b=5
```

### The single-element gotcha:
```python
t = (5)       # NOT a tuple — just the number 5!
t = (5,)      # comma makes it a tuple
```

### Why tuples exist:
- Safety: accidental modification impossible
- Meaning: signals "this is a record, don't touch its shape"
- Required: dict keys must be immutable → tuples can be keys, lists cannot

```python
coords_to_city = { (14.29, 120.90): "Tanza" }   # works
bad = { [1, 2]: "nope" }                        # TypeError: unhashable type
```

## Sets

```python
tags = {"python", "cs", "ai"}
numbers = {1, 2, 3, 3, 2}        # duplicates vanish: {1, 2, 3}

empty = set()                     # NOT {} — that's an empty DICT!

nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)                # {1, 2, 3} — instant dedupe
back_to_list = list(unique)
```

### Membership — the set's superpower:
```python
"python" in tags          # True — very fast even for huge sets
7 in numbers              # False
```

### Modifying:
```python
tags.add("math")
tags.discard("cs")        # no error if missing
tags.remove("cs")         # raises KeyError if missing — know both
```

### Set operations:
```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

a | b    # union:         {1, 2, 3, 4, 5}
a & b    # intersection:  {3, 4}
a - b    # difference:    {1, 2}
```

### No indexing:
```python
tags[0]    # TypeError — sets have NO order, so no positions
```

## Dictionaries

```python
student = {
    "name": "Carl",
    "age": 20,
    "city": "Tanza"
}

student["name"]              # "Carl"
student["age"] = 21          # update value
student["course"] = "BS CS"  # add new key
del student["city"]          # remove key
```

### Safe access — KeyError vs .get():
```python
student["gpa"]               # KeyError! crash
student.get("gpa")           # None
student.get("gpa", 0.0)      # 0.0 — default if missing
```

### Iteration:
```python
for key in student:                    # keys (default)
for value in student.values():         # values
for key, value in student.items():     # both — most common
    print(f"{key}: {value}")
```

### Checking membership:
```python
"name" in student             # True — checks KEYS only
"Carl" in student             # False! values need .values()
```

### Nested dicts — real-world structure:
```python
gradebook = {
    "Carl":    {"math": 92, "science": 88},
    "Maria":   {"math": 95, "science": 91}
}
gradebook["Carl"]["math"]     # 92
```

## Choosing the Right Container — the decision skill

Ask three questions:
1. **Do I look things up by name/key?** → dict
2. **Do I need uniqueness / fast membership tests?** → set
3. **Is this a fixed record that shouldn't change?** → tuple
4. Otherwise → list

Examples from your own work:
- Day 4 guess_game attempts counter → plain int was fine
- Student record (name/age/city) → dict (you did this in Day 1 profile!)
- Unique visitors → set
- Deck of cards order matters → list
- RGB color constant → tuple

## Common Pitfalls
- `(5)` is not a tuple — `(5,)` is
- `{}` creates an empty dict, not a set — use `set()`
- `tags[0]` crashes on sets — no order, no index
- `d[key]` crashes on missing keys — use `.get()` or check `in` first
- Lists can't be dict keys (unhashable); tuples can
- `for k, v in d:` without `.items()` → error; you must unpack via `.items()`

## Verification Checklist
- [ ] I can create and unpack tuples, and explain immutability's purpose
- [ ] I can deduplicate with a set and test membership
- [ ] I can build, update, iterate, and nest dicts
- [ ] I can state which container fits which job, with reasons
- [ ] All exercises run and outputs verified

## Exercises (exercises/Foundations/day_07/)
1. `tuple_basics.py` — create a coordinate tuple; print x and y via unpacking; attempt `point[0] = 99` inside a comment-predicted block, run, capture the TypeError message, explain it in a comment, then comment out the crash line.
2. `set_basics.py` — start with a list of 8 numbers containing duplicates; deduplicate via `set()`; add two items; discard one existing and one MISSING item (observe no error); test membership of two values with `in`.
3. `dict_basics.py` — build a `student` dict (4 keys); print one value; update age; add course; delete one key safely using `.get()` awareness; loop `.items()` printing `key: value`.
4. `inventory.py` — dict item→quantity (5 items): sell 2 of an item (subtract, floor at 0), restock another (+5), print total quantity across all items (accumulator over `.values()`), print the most-stocked item (loop compare).
5. `word_freq.py` — sentence string; count each word's occurrences into a dict (split + loop + dict.get(word, 0) + 1 pattern); print each word with count.
6. `contact_book.py` — dict name→phone (4 contacts): look up two names with safe `.get()`, add a contact, rename a key carefully (add new + del old), loop the final book.

## Build
`word_freq.py` done well is today's build: it combines strings (Day 2), loops (Day 4), dicts (today) — your first real data-analysis program. The `dict.get(key, 0) + 1` counting pattern appears in virtually every data pipeline you will ever write.

## AI Interaction
Good prompts:
- "Should this data be a list, tuple, set, or dict? Here is my use case: ..." (design question — good AI use)
- "Why does my dict raise KeyError but my friend's code with .get() doesn't?"
- "My set has no order but I expected insertion order — explain."
- Do NOT ask "write a word frequency counter" — build it first.

## HARD MODE — Stretch Exercises (STRICTLY OPTIONAL)
Attempt ONLY after core exercises are verified. Solvable with Days 1–7 knowledge only.

1. `gradebook_nested.py` — build the nested gradebook above (3 students × 3 subjects): compute each student's average (loop inner dict), the class average per subject (loop outer), and the single best student-by-average. No comprehensions required — accumulators are fine.
2. `club_overlap.py` — two sets of member names (club A: 5 names, club B: 5 names with partial overlap): print who is in BOTH (`&`), only A (`-`), and either (`|`). Then do it WITHOUT set operators — loops + `in` only — and confirm identical results.
3. `invert_dict.py` — given name→phone dict, produce phone→name inverted dict. What happens with duplicate values? Handle it: phone→list-of-names.
4. `grid_coords.py` — use TUPLES as dict keys to make a 3×3 treasure map: {(row, col): "gold"/"trap"/None}. Ask user for row and col, report what's there. This pattern (coordinate→data) underlies game boards and images.

The point of Hard Mode: nested structures + choosing containers deliberately — the exact thinking databases will formalize in Stage 2.

## Mastery Check (from memory)
1. Name the four containers and their one-word jobs.
2. Why does `(5)` fail to make a tuple, and what is the fix?
3. `d = {"a": 1}` — what does `d["b"]` do vs `d.get("b", 0)`?
4. Can a list be a dict key? Why not? Can a tuple?
5. From memory: write a loop that prints every key and value of a dict `scores`.

## Reflection
- Which container felt most natural? Which will you have to think twice about?
- Did the decision table (four jobs) change how you'd store your Day 1 profile data?
- Where did a KeyError surprise you today?

## Key Takeaways
- tuple = fixed record (immutable); `(5,)` needs the comma
- set = unique + fast membership; no indexing; `set()` for empty
- dict = key→value lookup; `.get()` for safe access; `.items()` to iterate pairs
- Choosing containers is a design decision — four jobs, four tools
- Keys must be immutable: tuples OK, lists forbidden