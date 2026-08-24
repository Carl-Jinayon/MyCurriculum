# Day 2 Advanced — Types, Numbers, and Exploring on Your Own

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### Floats are approximate — a future debugging landmine
Floats are stored in binary, so some decimal numbers cannot be represented exactly:

```python
print(0.1 + 0.2)   # 0.30000000000000004  (!)
```

This is NOT a Python bug. It is how binary floating point works on every computer. You will meet this again in ML, finance, and system work. Never compare floats with `==` directly:

```python
print(0.1 + 0.2 == 0.3)   # False
```

Later solutions: `round()`, `math.isclose()`, or the `decimal` module.

### int vs float storage
- `int` can be arbitrarily large: `2 ** 100` works fine
- `float` has limited precision (about 15-17 significant digits)
- Division `//` on negatives: `-7 // 2` → `-4` (floor, not truncation). `int(-3.9)` → `-3` (truncation). These differ!

### Boolean is a subclass of int
```python
print(True + True)     # 2
print(int(True))       # 1
```
Do not write code depending on this — know it exists, ignore it in practice.

### More string methods worth knowing (they arrive soon)
```python
"hello world".split()          # ['hello', 'world']
"a,b,c".split(",")             # ['a', 'b', 'c']
"  x  ".strip()
"abc".replace("a", "z")
"hello".startswith("he")       # True
"hello".count("l")             # 2
"5".isdigit()                  # True — check text is a number before converting
```

### STRING METHODS — the complete reference (comprehensive)
Strings are immutable — every method returns a NEW string; the original never changes.

**Cutting & joining:**
```python
"Python is fun".split()          # ['Python', 'is', 'fun']   (splits on whitespace)
"a,b,c".split(",")               # ['a', 'b', 'c']           (any delimiter)
" ".join(["a", "b", "c"])        # "a b c"                   (glue list back together)
"-".join(["a", "b"])             # "a-b"
```
`split()` + `join()` are a matched pair: parse text in, rebuild text out. Day 7's word counter and Day 8's CSV handling both live on this pair.

**Searching & testing:**
```python
s = "hello world"
s.startswith("he")     # True          s.endswith("ld")    # True
s.find("world")        # 6  (index; -1 if absent)
s.index("world")       # 6  (like find, but ValueError if absent)
"world" in s           # True — membership, usually cleanest
s.count("l")           # 3
```

**Cleaning & casing:**
```python
"  x  ".strip()        # "x"      strip both ends
"  x  ".lstrip()       # "x  "    left only
"  x  ".rstrip()       # "  x"    right only
"abc".upper(); "ABC".lower()
"hello world".title()      # "Hello World"
"Hello".swapcase()         # "hELLO"
```

**Testing character classes (return booleans):**
```python
"123".isdigit()      # True      "abc".isalpha()    # True
"ab12".isalnum()     # True      "   ".isspace()    # True
"abc".islower()      # True      "ABC".isupper()    # True
```
The `is...` family is your validation toolkit — `isdigit()` guards int conversion (Day 3), `startswith` filters filenames, `isspace` detects blank input.

**Replacing:**
```python
"aaa".replace("a", "b")     # "bbb"
"2026-08-24".replace("-", "/")
```

**Immutability demonstrated:**
```python
s = "hello"
s.upper()        # "HELLO" — returned, s unchanged!
print(s)         # "hello"
s = s.upper()    # rebinding is how you "change" a string
```

**Escape sequences consolidated:**
| Sequence | Meaning |
|---|---|
| `\n` | newline |
| `\t` | tab |
| `\"` `\'` | quote inside same-type quotes |
| `\\` | literal backslash |

### Membership on strings/lists (the `in` operator everywhere)
`in` works on ANY sequence: `"ell" in "hello"` → True; `4 in [1,2,3]` → False. One operator, every container.

### Multiple assignment and swapping
```python
a, b = 1, 2
a, b = b, a                   # swap — no temp variable needed
```

### Preview: selecting without branching (list indexing)
`n % 2` produces 0 or 1 — that value can *select* an answer instead of driving an if-statement:

```python
label = ["even", "odd"][number % 2]   # 0 -> "even", 1 -> "odd"
```

This previews lists (Day 6) and a lasting pattern: arithmetic as selection. For now, the if-based version is the right tool; this is an insight to revisit later.

## 2. Explore-It-Yourself Guide

Predict first, then run each:

1. `0.1 + 0.2 == 0.3` — what do you expect? What do you get? Read the explanation above after.
2. `-7 // 2` and `int(-3.9)` — same or different? Why? (Hint: floor vs truncate)
3. `2 ** 100` — does Python handle it? What about `2 ** 1000`?
4. `"5" * 3` — works. Why is `"5" + 3` an error but `"5" * 3` is not? (Hint: what would `"5" * 3` even mean?)
5. In the REPL, run `help(str)` — scroll through the methods. Pick three you have never seen and figure out what they do by experimenting.

### Research loop reminder
Hypothesis → experiment → evidence. Every exploration above is that loop in miniature. This is exactly how you will learn new languages and libraries for the rest of your career.

## 3. Where This Leads Later
- Types → Day 3 conditionals (`bool`), Day 4 loops (modulo tricks), Day 5 functions (return types)
- Type conversion → parsing user input in every future app
- Float precision → Day on debugging, later statistics/ML (numerical stability)
- f-strings → every project, forever
- `isdigit()` → input validation (security thread: never trust user input)

## Final Rule
Optional files never gate your progress. Master the main lesson, satisfy curiosity here, and move on.