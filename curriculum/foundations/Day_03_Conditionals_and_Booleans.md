# Day 3 — Conditionals, Comparisons, and Boolean Logic

## Objective
- Master comparison operators and understand that they produce `bool` values
- Use `if` / `elif` / `else` to make programs branch
- Understand indentation as Python's block structure
- Combine conditions with `and`, `or`, `not`
- Validate user input before using it

## Prerequisites
- Day 2: types (especially `bool`), `%` operator

## Why This Matters
So far your programs run top-to-bottom with no decisions. Real programs make decisions constantly: "if the user is logged in...", "if the number is negative...", "if the request is invalid...". Conditionals are the first place your programs become *intelligent* rather than just *mechanical*. They are also the doorway to loops (Day 4), functions (Day 5), and every algorithm after.

## Mental Models

### A Condition Is a Question
A condition is an expression that evaluates to `True` or `False`. The `if` statement asks the question; the answer decides which block runs.

### Indentation IS the Structure
Python does not use `{ }` or `begin/end`. Indentation (4 spaces) groups statements into a block. Indentation errors are not style complaints — they are syntax errors. The block is part of the program's meaning.

### Only One Path Runs
`if/elif/else` executes exactly ONE branch — the first condition that is `True`. Order matters: `elif` branches are checked top to bottom, and the first match wins.

## Comparisons — the questions

| Operator | Meaning | True example |
|---|---|---|
| `==` | equal to | `5 == 5` |
| `!=` | not equal to | `5 != 3` |
| `<` | less than | `3 < 5` |
| `>` | greater than | `5 > 3` |
| `<=` | less than or equal | `3 <= 3` |
| `>=` | greater than or equal | `5 >= 4` |

Critical: `==` (comparison) and `=` (assignment) are DIFFERENT operators. `=` puts a value in a box; `==` asks a question.

Comparisons produce a `bool` — you can store the answer:

```python
age = 20
is_adult = age >= 18        # True
print(is_adult)             # True
print(type(is_adult))       # <class 'bool'>
```

## if / elif / else

```python
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

Walk through the rules:
- `if` — required, checked first
- `elif` — checked only if no previous condition was True. You can have many.
- `else` — runs when everything above was False. Optional. Takes NO condition.

Execution for `number = 0`: `0 > 0` is False → try `0 < 0` False → `else` runs → "Zero". Exactly one branch.

## Nested conditionals

```python
if age >= 18:
    if has_id:
        print("Entry allowed.")
    else:
        print("Need an ID.")
else:
    print("Too young.")
```

Nesting works, but prefer flat where possible. Deep nesting (3+ levels) is a smell — later you will learn `and`/`or` to flatten it.

## and / or / not — combining questions

```python
age = 20
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome in.")

if age < 18 or not has_ticket:
    print("Denied.")
```

| Operator | Result |
|---|---|
| `a and b` | True only if BOTH are True |
| `a or b` | True if AT LEAST ONE is True |
| `not a` | flips: True becomes False, False becomes True |

Read `and` as "both", `or` as "at least one", `not` as "the opposite of".

## Truthiness (preview)
Every value is truthy or falsy in a condition:
- Falsy: `0`, `0.0`, `""` (empty string), `None`, empty collections
- Everything else is truthy

```python
name = input("Name: ")
if name:              # True if name is not empty
    print(f"Hello, {name}!")
else:
    print("You gave no name.")
```

This is extremely common in real code. Use it for empty-input checks.

## Input Validation — your first security lesson
Never assume user input is valid. A program that trusts input is a program that crashes (or worse). Validate before using:

```python
raw = input("Enter a number: ")
if raw.isdigit():
    number = int(raw)
    print(f"Square: {number ** 2}")
else:
    print("That is not a positive whole number.")
```

- `isdigit()` — True if the string contains only digits
- The pattern: check → convert → use. Check BEFORE converting, or you get a crash instead of a message.

This is the beginning of the security thread: **never trust user input**. It will follow you through web, databases, AI agents, everything.

## Common Mistakes
- `if age = 18:` → `SyntaxError`. `=` is assignment; `==` is the question
- Forgetting the colon after the condition: `if x > 0` (no colon) → `SyntaxError`
- Wrong indentation → `IndentationError`, or worse: wrong block grouping (this runs, but does the wrong thing)
- Using `elif` with a condition after `else` — invalid
- Ordering: checking `age >= 18` before `age >= 65` means the elderly check never runs for those age 70 — because the first branch already matched. Put the most specific condition FIRST.

## Verification Checklist
- [ ] I ran every example and can explain the output
- [ ] I can predict which branch runs for any input
- [ ] I can explain why `elif` order matters
- [ ] I validated input before converting it
- [ ] I know the difference between `=` and `==`

## Exercises (exercises/day_03/)
1. `classifier.py` — number in; print Positive/Negative/Zero (from the lesson, then re-write from memory).
2. `even_odd_v2.py` — revisit: number in, print even/odd using a conditional (your Day 2 version is fine — now understand the conditional properly). Extend: also print "divisible by 5" if applicable.
3. `grade.py` — score (0-100) in; print letter grade: A >= 90, B >= 80, C >= 70, D >= 60, F below 60. Watch elif ordering.
4. `login_sim.py` — ask for username and password; if username == "admin" and password == "secret", print "Access granted.", else "Access denied." (Do NOT put real passwords in code — this is a simulation.)
5. `validator.py` — ask for input; if it is a digit, print its square; else print a warning. (From the lesson; then make it also handle negative numbers: e.g. strip a leading `-` before checking.)

## Build
`grade.py` done well is today's build: correct ordering, handles edge cases (0, 100, exactly 90). Tomorrow, loops will let you turn it into a program that grades until the user quits.

## AI Interaction
Good prompts for this lesson's learning style:
- "I get IndentationError on this code — what is wrong with my indentation?" (paste code) — the AI explains the structure rule, you fix it
- "My grade.py gives B for a score of 90, why?" — this is a real reasoning bug: paste code + output and ask WHY
- Do NOT ask "write a login system" — build it yourself first

## Mastery Check (from memory)
1. Write a program: number in; if divisible by 3 and 5 print "FizzBuzz", if by 3 print "Fizz", if by 5 print "Buzz", else the number. Run it with several values.
2. What is the difference between `=` and `==`?
3. `5 == 5` and `5 = 5` — which one is legal Python? Why?
4. What does `not (age >= 18)` mean in plain words?

## Reflection
- Did you think through branch ordering before writing?
- Did you test edge cases (0, negative, exactly a boundary)?
- What surprised you about boolean logic?

## Key Takeaways
- Conditions are questions that produce `True`/`False`
- `if/elif/else` runs exactly one branch; first match wins — order matters
- Indentation is Python's structure — treat it as part of the program
- `==` asks, `=` assigns — never mix them
- Validate input before converting: check → convert → use
- Never trust user input (security thread begins)