# Math Day 2 Advanced — Functions, Deeper

> STATUS: STRICTLY OPTIONAL. Read only if curious. Never gates progress.

## 1. Advanced Technical Content

### Composition — machines in a pipeline
If f and g are machines, `f(g(x))` means: g first, THEN feed its output into f.

```
f(x) = x + 1,  g(x) = 2x

f(g(3)):  g(3) = 6, then f(6) = 7
g(f(3)):  f(3) = 4, then g(4) = 8
```

Order matters! Machines chained left-to-right do NOT generally commute. This single idea is the seed of: function composition in Python (`f(g(x))` you already write), data pipelines, neural network layers (each layer is a machine feeding the next), and Unix pipes later.

### Function as mapping — arrows
A function maps each input to EXACTLY one output:
```
x: 1 → 5
x: 2 → 7     (rule: 2x + 3)
x: 3 → 9
```
One input can never have two outputs — that's the definition of a function. (Two inputs sharing one output is fine: f(1) = 5 and... not for this rule, but for f(x)=x² both -2 and 2 give 4.)

This "exactly one output" rule is what makes functions *predictable* — same reason pure Python functions (no randomness, no side effects) are easier to test.

### The vertical line intuition (preview)
When you eventually graph functions: if any vertical line crosses the graph twice, some input had two outputs — instant disqualification as a function. You don't need graphs yet; keep the idea parked.

### Why "domain" will matter more later
f(x) = x/3 has domain "all numbers" — but a future machine like √x refuses negative inputs, and 10/x refuses zero. Domain thinking = input validation. Your `get_int(prompt, min, max)` from Day 5 was domain enforcement in code!

### Linear functions — the pattern in tables (fulfilling the promise)
f(x) = mx + b machines:
- grow by the SAME amount per step of x (constant rate)
- m = growth per step ("slope"), b = starting value
- In your table for 2x+3: outputs went -1, 3, 5... differences: 4, 2? No wait — check with equal x-steps: inputs -2,0,1,4 aren't evenly spaced. Feed it 0,1,2,3: outputs 3,5,7,9 — always +2. That constant +2 IS the coefficient 2.

Detecting the rule from a table: divide "output change" by "input change." This is slope — the heart of linear functions, coming soon.

**Slope formally:** for two points (x₁, y₁) and (x₂, y₂):
m = (y₂ − y₁) / (x₂ − x₁)     — "rise over run"
b = the output when x = 0 (the y-intercept — where the machine starts)

**Worked example:** machine outputs 7 when x=2 and 19 when x=5.
- m = (19 − 7) / (5 − 2) = 12/3 = 4
- b: f(x) = 4x + b → 7 = 4(2) + b → b = −1
- Rule: **f(x) = 4x − 1**. Verify on both points. ✓

This is rule-detection from your Hard Mode, now with a general method. Every "constant rate" situation in reality (taxi fares, salaries per hour, distance over time) is a linear function waiting for m and b.

### Functions with multiple inputs (preview)
f(x, y) = x + y — machines can take several inputs. Python: `def f(x, y): return x + y`. ML loss functions live here later.

## 2. Explore-It-Yourself Guide

1. In Python: define f and g as above; print f(g(3)) and g(f(3)) — confirm they differ.
2. Table detective: fill outputs of h(x) = 3x - 1 for x = 0..5; verify each step grows by exactly 3.
3. Reverse-engineer: machine gives outputs 4, 10, 16, 22 for inputs 0, 1, 2, 3. Growth per step? Starting value? Write the rule; verify on input 10.
4. One-output rule: try to design a "function" where input 1 sometimes gives 2 and sometimes gives 5 (use random). Why does that violate the definition? What does this tell you about why `random.randint` isn't a math function?
5. REPL: define `def f(x): return 2 * x + 3` then call `f(f(f(1)))` — trace by hand FIRST: three chained machines. Predict, then run.

## 3. Where This Leads Later
- Composition → pipelines (data → model → output), Stage 4 agent chains
- Slope/linear functions → next math lessons; linear equations of lines
- Domain → input validation, security (never trust input)
- Multi-input functions → coordinate geometry, ML loss/error functions
- "Exactly one output" → deterministic testing, pure functions, reproducibility in ML

## Final Rule
Optional files never gate your progress. Master the main lesson, satisfy curiosity here, and move on.