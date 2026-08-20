# Math Day 1 — Algebra: Variables, Expressions, Equations

## Objective
- Understand what a variable is and why math uses them
- Read and evaluate algebraic expressions
- Simplify by combining like terms
- Solve one-step equations using the balance model
- Check solutions by substitution (verification-first — same rule as code)
- Translate English sentences into algebra

## Prerequisites
- Day 1 Python: you already KNOW variables — this lesson makes the connection formal

## Why This Matters
Algebra is the grammar of every later math subject (functions, linear algebra, calculus) — and it is the math of programming. A Python variable IS a math variable. An equation IS a constraint your code must satisfy. Learning this now makes every future stage faster, and it is the single most-used math in all of software engineering.

## Mental Models

### 1. A Variable Is a Named Box (you already know this)
In Python you wrote `x = 5`. In algebra, `x` is the same thing: a placeholder for a number we may not know yet. The only difference: Python *requires* a value; algebra *allows* the unknown.

### 2. Expression = Phrase, Equation = Sentence
- **Expression**: `2x + 3` — a phrase of numbers and variables. No "=" sign. It has a value once x has one.
- **Equation**: `2x + 3 = 11` — a sentence with "=", claiming two expressions are equal. It asks: *for which x is this true?*

### 3. The Balance Model
An equation is a balance scale: left pan = right pan. The rule that makes ALL of algebra work:

> Whatever you do to one side, do exactly the same to the other. The balance stays true.

That single rule is the entire method for solving equations.

## Variables and Coefficients

- `x`, `y`, `n` — letters standing for numbers
- In `2x`, the number `2` is the **coefficient** (how many x's you have), `x` is the variable
- In `2x + 3`, the `3` is a **constant** (a plain number)
- Implicit coefficient: `x` means `1x` — always 1 of them

## Evaluating an Expression (substitution)

To evaluate `2x + 3` for `x = 4`: replace x with 4, then compute.

```
2x + 3  →  2(4) + 3  →  8 + 3  =  11
```

Practice pattern — predict, then check (your debugging habit applies to math):
```
x = 4:  2x + 3 = 11
x = 10: 2x + 3 = 23
x = -2: 2x + 3 = -1
```

Python connection — this IS a Python expression:
```python
x = 4
print(2 * x + 3)   # 11
```

## Simplifying: Combining Like Terms

**Like terms** = same variable, same power. You can add/subtract them; you cannot combine different kinds.

| Expression | Simplified | Why |
|---|---|---|
| `3a + 2a` | `5a` | both are a's |
| `5x - 2x` | `3x` | both are x's |
| `2x + 3 + 4x + 1` | `6x + 4` | x's combine, constants combine |
| `2x + 3` | cannot simplify | x's and constants are different kinds |

Mental picture: 2 apples + 3 apples = 5 apples. 2 apples + 3 oranges = 2 apples + 3 oranges. The letters are the "kinds."

## Solving One-Step Equations

The balance rule in action. Goal: **isolate x** — get x alone on one side.

**Addition case:**
```
x + 5 = 12
x + 5 - 5 = 12 - 5     (subtract 5 from BOTH sides)
x = 7
```

**Subtraction case:**
```
x - 4 = 9
x - 4 + 4 = 9 + 4
x = 13
```

**Multiplication case:**
```
3x = 21
3x / 3 = 21 / 3        (divide BOTH sides by 3)
x = 7
```

**Division case:**
```
x / 5 = 6
x / 5 * 5 = 6 * 5
x = 30
```

## Checking Your Answer (verification-first)

You never trust a solution without checking — same rule as running code:

```
x = 7  for  x + 5 = 12
check: 7 + 5 = 12  ✓  correct
```

```
x = 5  for  3x = 21
check: 3(5) = 15 ≠ 21  ✗  wrong — redo
```

Checking is cheap. Guessing wrong and never checking is expensive.

## Word Problems: English → Algebra

This is the AI-era skill in math form: translating a vague problem into a precise statement.

> "I have some money. I spent 150 pesos. I have 350 left."

Let x = my money. Then:
```
x - 150 = 350
x = 500
```

Rules of translation:
- "some number / a number" → `x`
- "more than / sum / plus" → `+`
- "less than / spent / minus" → `-`
- "times / of / product" → `×`
- "is / equals / results in" → `=`

## Common Mistakes
- Combining unlike terms: `2x + 3 = 5x` — WRONG. Different kinds.
- Only changing one side of an equation — breaks the balance
- Forgetting to check the solution
- Confusing coefficient and exponent: `2x` means `x + x`, NOT `x · x` (that's `x²`)
- `x` alone means `1x` — `x + x = 2x`, not `x²`

## Verification Checklist
- [ ] I can evaluate `2x + 3` for any given x without mistakes
- [ ] I can simplify `2x + 3 + 4x + 1` correctly
- [ ] I can solve and CHECK all four equation types
- [ ] I can explain the balance rule in my own words
- [ ] I did every exercise with pen/paper FIRST, then checked

## Exercises (exercises/math_01/) — write solutions in a text file or on paper, check each
1. Evaluate `2x + 3` for x = 4, x = 10, x = -2. (Predict first, then compute.)
2. Evaluate `3y - 5` for y = 3, y = 0, y = 10.
3. Simplify: `3a + 2a`; `5x - 2x`; `2x + 3 + 4x + 1`; `7y - 3 + 2y - 5`.
4. Solve AND check: `x + 7 = 15`; `x - 4 = 9`; `3x = 21`; `x / 5 = 6`.
5. `python_bridge.py` — write Python that evaluates `2x + 3` for x = 4, 10, -2 and prints results. Verify they match your hand answers.
6. Word problems: (a) I spent 150 pesos and have 350 left — how much did I start with? (b) Three times my age is 60. How old am I? (c) Half of a number is 12. What is the number? Translate, solve, check.

## HARD MODE (optional, after core)
1. Solve and check two-step equations: `2x + 3 = 11`; `3x - 7 = 14` (undo the constant FIRST, then the coefficient).
2. "Three consecutive integers sum to 24." Let the first be x; the next two are x+1, x+2. Write the equation, solve, name the integers.
3. Translate this Python function into algebra notation, then solve for the input that makes output 27:
   ```python
   def mystery(x):
       return 2 * x + 5
   ```

## Mastery Check (from memory, no notes)
1. What is the difference between an expression and an equation?
2. Solve `x + 9 = 14` and check your answer.
3. Solve `4x = 28` and check.
4. Simplify `3x + 5 + 2x - 2`.
5. Explain the balance rule in your own words.

## Reflection
- Which equation type felt natural, which did you have to think about?
- Did you check every answer, or only the hard ones?
- How does this connect to your Python variables?

## Key Takeaways
- Variable = named box (same idea as Python)
- Expression = phrase, equation = sentence with a claim
- Balance rule: same operation on both sides — the entire method
- Like terms combine by kind; different kinds never combine
- Always check solutions by substitution — the math version of running your code
- Word problems are requirements analysis in disguise