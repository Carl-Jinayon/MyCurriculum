# Day 3 Cheat Sheet — Conditionals and Booleans

## Comparisons (all produce True/False)
```
==   equal          !=   not equal
<    less           >    greater
<=   less/equal     >=   greater/equal
```
`=` ASSIGNS. `==` ASKS. Never mix them.

## if / elif / else
```python
if condition:
    block          # 4-space indent REQUIRED
elif condition2:
    block
else:
    block
```
- Exactly ONE branch runs
- `elif` checked top-to-bottom, FIRST match wins → order matters
- `else` takes NO condition, optional
- Colon after every condition line

## Boolean operators
| Expression | True when |
|---|---|
| `a and b` | BOTH true |
| `a or b` | AT LEAST ONE true |
| `not a` | a is false |

## Truthiness
Falsy: `0`, `0.0`, `""`, `None`, empty collections. Everything else truthy.
```python
if name:        # runs when name is non-empty
```

## Input validation pattern (security)
```python
raw = input("Number: ")
if raw.isdigit():
    number = int(raw)
else:
    print("Not a valid positive integer.")
```
CHECK → CONVERT → USE. Never trust user input.

## Common Errors
- `if x = 5:` → SyntaxError (= vs ==)
- Missing colon → SyntaxError
- Bad indentation → IndentationError or silently wrong branch
- Specific condition AFTER general one → never runs (put most specific first)

## Must-Know Checklist
- [ ] I can predict the branch for any input
- [ ] I can write if/elif/else from memory
- [ ] I used and/or/not correctly
- [ ] I validated input before converting
- [ ] I tested edge cases (0, boundaries, negative)

## Active Recall Questions
1. `5 == "5"` — True or False? Why?
2. What happens if all conditions are False and there is no else?
3. `age >= 18 and age < 21` — in plain words?
4. Write FizzBuzz from memory (divisible by 3 and 5 → "FizzBuzz", 3 → "Fizz", 5 → "Buzz", else number)