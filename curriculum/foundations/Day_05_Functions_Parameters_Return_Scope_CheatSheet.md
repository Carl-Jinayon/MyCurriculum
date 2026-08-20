# Day 5 Cheat Sheet — Functions

## Define and call
```python
def greet(name):
    return f"Hello, {name}!"

msg = greet("Maria")   # msg = "Hello, Maria!"
```

## return
```python
def square(x):
    return x * x       # value usable by caller

def bad(x):
    print(x * x)       # visible, but returns None
```
RULE: print = for humans, return = for programs.

## Defaults & keyword args
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

greet("A")                       # Hello, A
greet("A", greeting="Hi")        # Hi, A
```
Defaults must come AFTER non-default params.

## Scope
```python
x = 10                 # global

def f():
    x = 5              # LOCAL — global untouched
    print(x)           # 5

f()
print(x)               # 10
```
Assignment inside = new local. Avoid `global`.

## Math ↔ Python
f(x) = x²  ↔  `def f(x): return x * x`
Composition f(g(x)) ↔ `f(g(x))`

## Common errors
- Forgotten return → None
- print instead of return
- Call before def → NameError
- Global modified by local assignment → silently wrong

## Must-Know Checklist
- [ ] define + call + use return
- [ ] know why print ≠ return
- [ ] explain scope with example
- [ ] defaults + keyword args
- [ ] ran all 5 exercises

## Active Recall
1. What does a no-return function give back?
2. `def f(a=1, b)` — legal? Why not?
3. After `def f(): x = 1` with global `x=9` — what is `x` after `f()`?
4. Write `is_even(n)` from memory.