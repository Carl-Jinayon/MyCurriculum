# Day 7 Cheat Sheet — Tuples, Sets, Dicts

## The Four Containers

| Type | Ordered | Mutable | Dupes? | Lookup by | Use for |
|---|---|---|---|---|---|
| `list` | ✓ | ✓ | ✓ | index | changing ordered data |
| `tuple` | ✓ | ✗ | ✓ | index | fixed records |
| `set` | ✗ | ✓ | ✗ | membership | uniqueness, fast `in` |
| `dict` | insertion* | ✓ | keys: ✗ | key | named lookups |

## Tuples
```python
p = (3, 5)
x, y = p          # unpacking
t = (5,)          # single-element NEEDS comma — (5) is just 5!
p[0] = 9          # TypeError: immutable
# tuples CAN be dict keys; lists CANNOT (unhashable)
```

## Sets
```python
s = {1, 2, 3}
empty = set()         # {} makes a DICT, not a set!
unique = set([1,2,2]) # {1,2} — instant dedupe
x in s                # fast membership
s.add(x); s.discard(x)   # discard: no error if missing
a | b   # union          a & b   # intersection
a - b   # difference     (no indexing!)
```

## Dicts
```python
d = {"name": "Carl", "age": 20}
d["name"]              # access (KeyError if missing)
d.get("gpa", 0.0)      # safe access with default
d["city"] = "Tanza"    # add/update
del d["age"]           # delete

for k in d: ...                    # keys
for v in d.values(): ...           # values
for k, v in d.items(): ...         # pairs — most common

"name" in d            # checks KEYS only

gradebook["Carl"]["math"]   # nested dicts
```

## Counting pattern (memorize)
```python
counts[word] = counts.get(word, 0) + 1
```

## Decision Questions
1. Lookup by name/key? → **dict**
2. Uniqueness / fast `in`? → **set**
3. Fixed record, never changes? → **tuple**
4. Otherwise → **list**

## Common Errors
- `(5)` not a tuple → use `(5,)`
- `{}` is empty dict → empty set is `set()`
- `set[0]` TypeError — no order
- missing key + `[ ]` → KeyError → use `.get()`
- list as dict key → unhashable TypeError

## Must-Know Checklist
- [ ] Four containers + their jobs
- [ ] Tuple unpacking + single-element comma
- [ ] Set dedupe + membership + ops
- [ ] Dict CRUD + .get() + .items() loop
- [ ] Counting pattern from memory
- [ ] All 6 exercises run and verified

## Active Recall
1. Which container for: unique visitors? student record? RGB color? shopping queue?
2. `(5)` vs `(5,)` — what's the difference?
3. `d[k]` vs `d.get(k)` vs `d.get(k, default)`?
4. Why can't a list be a dict key?
5. Write the word-counting pattern from memory.