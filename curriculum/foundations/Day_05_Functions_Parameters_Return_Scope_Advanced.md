# Day 5 Advanced — Functions, Scope, and Exploring on Your Own

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### The call stack — what actually happens
When you call a function, Python pushes a frame onto the call stack: parameters and locals live there. When the function returns, the frame is popped. That is why locals vanish.

```python
def a():
    print("a starts")
    b()
    print("a ends")

def b():
    print("b starts")
    c()
    print("b ends")

def c():
    print("c")

a()
```

Output order: a starts → b starts → c → b ends → a ends (last in, first out). Deep recursion later uses exactly this stack — and overflowing it causes `RecursionError`.

### Mutable vs immutable arguments (BIG later topic)
Numbers and strings are immutable — passing them never changes the caller's variable. Lists are mutable — a function can CHANGE the list you passed:

```python
def add_item(items, item):
    items.append(item)      # mutates the CALLER's list

shopping = []
add_item(shopping, "milk")
print(shopping)             # ['milk'] — changed outside!
```

This is intentional and powerful — and a classic source of bugs. Full treatment in Day 6 (lists). Rule for now: if you don't want mutation, pass a copy.

### None — the value that means "nothing came back" (formal)
`None` is a real VALUE with its own type — Python's way of saying "absent":
```python
print(type(None))       # <class 'NoneType'>
result = print("hi")    # print RETURNS None!
print(result)           # None
```

**The rules:**
- Every function returns something; no `return` → returns `None` automatically
- `return` with no value also returns `None`
- Test for it with `is`, not `==`: `if result is None:` (identity, not equality — one-object guarantee makes `is` exact and idiomatic)
- Falsy in conditions: `if not result:` treats None like empty/zero

You already USED this contract: Day 8's `divide()` returning None on zero means "no valid answer exists" — callers must check before doing math with it.

### Docstrings — documentation that lives inside code
A docstring is the FIRST string literal inside a function/module/class:
```python
def get_int(prompt, lo, hi):
    """Keep asking until the user types an integer in [lo, hi].

    Returns the validated int. Re-prompts on anything else.
    """
    ...
```
- Triple quotes allow multi-line
- First line: one-sentence summary; blank line; details
- Conventions: describe the CONTRACT (what it returns, what it raises), not the mechanics
- Tooling reads them: `help(get_int)` displays your docstring; IDEs show it on hover; AI assistants parse it

Docstrings are the professional habit you asked about earlier — this IS where they live.

### Type hints — optional labels that scale (gentle intro)
```python
def square(x: int) -> int:
    return x * x

def greet(name: str, excited: bool = False) -> str:
    ...
```
- `parameter: type` and `-> type` are LABELS — Python ignores them at runtime
- Value: editors autocomplete correctly, bugs surface early (with type-checkers), readers understand contracts instantly
- Start using them on new functions now; they cost seconds and pay forever

### *args and **kwargs
```python
def total(*numbers):              # collects all positional args into a tuple
    return sum(numbers)

print(total(1, 2, 3, 4))          # 10

def show(**info):                 # collects keyword args into a dict
    print(info)

show(name="Carl", age=20)         # {'name': 'Carl', 'age': 20}
```
Useful for flexible APIs. Don't overuse.

### Higher-order functions (preview)
Functions can be passed as arguments:

```python
def apply_twice(f, x):
    return f(f(x))

def double(n):
    return n * 2

print(apply_twice(double, 3))     # 12
```

This is the doorway to map/filter/reduce — the functional style that dominates data and ML work.

### Recursion (preview — formal treatment in Stage 1)
A function calling itself:
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```
Every recursion needs: base case (stops) + recursive case (moves toward base).

### Docstrings
```python
def square(x):
    """Return the square of x."""
    return x * x

help(square)     # shows the docstring
```
Document WHAT functions do, not how.

## 2. Explore-It-Yourself Guide

Predict, run, reflect:

1. `def f(): pass` then `print(f())` — what value? Why?
2. Call a function before its definition in the file — what error?
3. `def f(x): return x + 1` then `f(f(f(0)))` — trace it by hand, then run. This is composition.
4. Write a function `counter()` that uses `global count` — then write the same behavior WITHOUT global by returning values. Compare. Which is easier to reason about?
5. In the REPL: `help(print)` — notice the `*objects` and defaults. Now you can read print's full signature as a docstring reader.
6. `def f(x=[]): x.append(1); return x` — call it 3 times. What happens? (This is the classic mutable-default trap. Ask an AI for "why" after you've observed it yourself.)

## 3. Where This Leads Later
- Functions → Day 6 lists (mutable arguments), Day 7 errors/exceptions
- Call stack → recursion, debugging stack traces
- *args/**kwargs → library APIs, web frameworks
- Higher-order functions → map/filter/reduce, pandas, ML preprocessing
- Docstrings → professional code, tools like pydoc, and AI-assisted development (AI reads your docs!)

## Final Rule
Optional files never gate your progress. Master the main lesson, satisfy curiosity here, and move on.