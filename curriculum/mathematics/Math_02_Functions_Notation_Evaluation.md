# Math Day 2 — Functions: f(x), Evaluation, and the Input→Output Machine

## Objective
- Understand function notation: what f(x) actually means (and what it does NOT mean)
- Evaluate functions at given inputs, including negative numbers
- Work with multiple functions and build input→output tables
- Reverse the machine: given an output, find the input (solving f(x) = k)
- Connect math functions to Python functions — they are the same idea

## Prerequisites
- Math Day 1: variables, expressions, equations (balance rule)
- Day 5 Python: `def`, `return` — you have been writing math functions all along

## Why This Matters
The function is THE central concept of all later mathematics — linear algebra, calculus, probability, and ML are all built on functions transforming inputs into outputs. This lesson also closes a loop you opened on Math Day 1: `2x + 3` was just sitting there; now it becomes a *machine with a name*. And your Python `def f(x): return 2 * x + 3` from Day 5? That WAS this lesson, in code.

## Mental Models

### 1. A Function Is a Machine
```
        ┌─────────────┐
  x ──▶ │  rule: ×2 +3 │ ──▶ output
        └─────────────┘
```
Put a number in, the machine applies its rule, a number comes out. Same input → same output, every time.

### 2. f(x) Does NOT Mean "f times x"
`f(x)` reads "**f of x**" — f is the machine's NAME, x is what you feed it. The parentheses here mean "input to", not "multiply".

### 3. The Rule Is the Function
`f(x) = 2x + 3` means: "the machine named f takes an input x and outputs 2x + 3." The letter inside the parentheses is just a placeholder — like a Python parameter.

## Reading and Writing Functions

```python
f(x) = 2x + 3     # read: "f of x equals two-x plus three"
g(x) = x²         # read: "g of x equals x squared"
h(t) = 5t         # read: "h of t equals five-t" — input letter can be anything
```

Parts:
- **f** — the function's name
- **x** — the input variable (placeholder)
- **2x + 3** — the rule applied to the input

## Evaluating: Feeding the Machine

To evaluate `f(4)` when `f(x) = 2x + 3`: substitute 4 for EVERY x in the rule.

```
f(x)  = 2x + 3
f(4)  = 2(4) + 3 = 11      ← replace x with 4 everywhere
f(10) = 2(10) + 3 = 23
f(-2) = 2(-2) + 3 = -1
```

Predict-first pattern (your habit): write the expected output BEFORE computing.

### Different machines, same input:
```
f(x) = x + 5    →  f(3) = 8
g(x) = 2x       →  g(3) = 6
```
Same food, different machines, different outputs.

## Input→Output Tables

A table shows the machine's behavior over several inputs:

| x | f(x) = 2x + 3 |
|---|---|
| -2 | -1 |
| 0 | 3 |
| 1 | 5 |
| 4 | 11 |
| 10 | 23 |

Tables are how you *see* a machine's personality: this one grows steadily, always odd... patterns live in tables.

## Reversing the Machine: Solving f(x) = k

Given output, find input — this is Math Day 1's balance rule wearing a new outfit:

```
If f(x) = 2x + 3, find x when f(x) = 11:

2x + 3 = 11          ← translate the question into an equation
2x + 3 - 3 = 11 - 3   ← balance rule (subtract 3 both sides)
2x = 8
x = 4                 ← divide by 2

CHECK: f(4) = 2(4) + 3 = 11 ✓
```

You already knew this answer — from Math Day 1! Nothing new except notation.

## Domain and Range (informal)

- **Domain**: all inputs the machine accepts ("what can I feed it?")
- **Range**: all possible outputs ("what can come out?")

For `f(x) = 2x + 3`: domain is all numbers, range is all numbers.
For now, informal understanding is enough — formal definitions arrive later.

## The Python Bridge — Proof They Are the Same

```python
def f(x):
    return 2 * x + 3

print(f(4))    # 11
print(f(10))   # 23
print(f(-2))   # -1
```

| Math | Python |
|---|---|
| `f(x) = 2x + 3` | `def f(x): return 2 * x + 3` |
| `f(4)` | `f(4)` |
| evaluate | call |
| solve f(x) = 11 | loop/search for x where `f(x) == 11` |
| input variable x | parameter x |

Day 5's lesson was this lesson in disguise. Mathematics and programming share one concept: **transformation of inputs into outputs**.

## Common Mistakes
- Reading f(x) as "f times x" — it is "f OF x"
- Substituting only SOME of the x's: f(4) = 2·4 + 3 vs wrongly doing 2(4+3)
- Forgetting negatives: f(-2) = 2(-2) + 3 = -4 + 3 = -1 (not 7!)
- Confusing f(x) = 11 (an equation to solve) with f(11) (an evaluation)
- Thinking different letters change the machine: h(t) = 5t and h(x) = 5x are the same machine

## Verification Checklist
- [ ] I can explain why f(4) ≠ 4f without notes
- [ ] I evaluated functions at positive, zero, and negative inputs correctly
- [ ] I built a complete input→output table
- [ ] I reversed a machine (solved f(x) = k) and CHECKED by substitution
- [ ] My python_bridge matches my hand answers exactly

## Exercises (exercises/Math/math_02/) — predict first, then compute, then check
1. `exercise_01.txt` — Evaluate `f(x) = 3x - 1` for x = 0, x = 2, x = -3. Show substitution steps.
2. `exercise_02.txt` — Two machines: `f(x) = x + 5` and `g(x) = 2x`. Evaluate BOTH at x = 1, 2, 3, 10. Which machine grows faster? How do you see it in the numbers?
3. `exercise_03.txt` — Complete the table for `f(x) = x² - 4`: fill outputs for x = -3, -1, 0, 1, 3. What do you notice about symmetry?
4. `exercise_04.txt` — Reverse the machine: if `f(x) = 4x - 2` and `f(x) = 18`, find x. Balance rule + check. Then again: `g(x) = x/3 + 1` and `g(x) = 5`.
5. `python_bridge_02.py` — define `def f(x): return 3 * x - 1`; print f(0), f(2), f(-3); verify against exercise_01 answers. Then define g(x) = 4*x - 2 and find (by testing values in a loop) which input gives 18 — compare with your algebra answer.
6. `exercise_06.txt` — Word problem: a tricycle ride costs 40 pesos base plus 15 pesos per kilometer. Write the fare as a function F(k); evaluate F(1), F(3), F(8). Then: if a ride cost 130 pesos, how far was it? (Reverse!)

## HARD MODE (optional, after core)
1. Composition preview: if `f(x) = x + 1` and `g(x) = 2x`, compute `f(g(3))` and `g(f(3))` step by step. Are they equal? What does the order tell you about chaining machines?
2. Rule detective: a mystery machine produces 7, 9, 11, 13 for inputs 1, 2, 3, 4. Find the rule f(x) (hint: slope thinking — how much does output grow per input step?), then predict f(100).
3. Piecewise preview in Python: parking costs 50 pesos for the first hour and 30 pesos per additional hour (or fraction). Write `fee(t)` in Python using conditionals, then compute fee(0.5), fee(1), fee(2.5), fee(4). Describe the rule in words.

## Mastery Check (from memory, no notes)
1. In one sentence: what does f(x) mean, and what does it NOT mean?
2. If f(x) = 5x - 2, evaluate f(0), f(3), f(-1).
3. If f(x) = 5x - 2 and f(x) = 23, find x. Check your answer.
4. Write, from memory, the Python version of f(x) = 5x - 2 — then verify f(3) matches your hand answer from #2.

## Reflection
- Did function notation feel like new knowledge or a rename of things you knew?
- Where else have you seen input→output machines? (Think: input(), print(), your validator_fn)
- Which was harder: evaluating forward or reversing? Why?

## Key Takeaways
- f(x) = "f of x": name + input + rule — never multiplication
- Evaluate = substitute EVERYWHERE; watch negatives
- Reversing f(x) = k is just solving an equation — the balance rule again
- Tables reveal a machine's behavior; patterns hide in them
- Python def IS math's function — one concept, two languages