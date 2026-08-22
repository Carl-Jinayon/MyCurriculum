# Day 2 — Data Types, Arithmetic, and Strings

## Objective
- Understand the four basic data types: int, float, str, bool
- Use `type()` to inspect values
- Master arithmetic operators including `//`, `%`, `**`
- Work with strings: concatenation, repetition, methods, length
- Convert between types with `int()`, `float()`, `str()`
- Handle the classic beginner error: mixing strings and numbers

## Prerequisites
- Day 1: variables, print, input

## Why This Matters
Almost every program you will ever write manipulates data: numbers, text, and truth values. If you do not know what *kind* of data you are holding, your program will do the wrong thing. Most beginner bugs come from type confusion — thinking `"5"` is `5`. This lesson kills that bug class permanently.

## Mental Models

### Data has a Type
Every value in Python has a type. The type decides what you can do with it:
- `5` (int) can be divided, multiplied, raised to powers
- `"5"` (str) cannot be divided — it is text

Think: the type is the *nature* of the thing, the value is its *content*. Two values can look identical on screen and be completely different things.

### Operators Act on Types
`+` means different things depending on type:
- `5 + 5` → `10` (addition)
- `"a" + "b"` → `"ab"` (concatenation)
- `"5" + 5` → `TypeError` (Python refuses: mixing text and number)

Python tells you which operators a type supports by *rejecting* invalid combinations. The error message is the contract.

## The Four Basic Types

| Type | Name | Examples | Notes |
|---|---|---|---|
| `int` | integer | `5`, `-3`, `0`, `1000000` | whole numbers |
| `float` | floating point | `3.14`, `-0.5`, `2.0` | numbers with decimals |
| `str` | string | `"hello"`, `'x'`, `""` | text; `""` is the empty string |
| `bool` | boolean | `True`, `False` | truth values (Day 3) |

### type()
`type(x)` tells you what type a value is:

```python
print(type(5))        # <class 'int'>
print(type(5.0))      # <class 'float'>
print(type("5"))      # <class 'str'>
```

Use `type()` whenever you are unsure what a value is. It is a debugging tool, not just a lesson concept.

## Arithmetic Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | addition | `7 + 3` | `10` |
| `-` | subtraction | `7 - 3` | `4` |
| `*` | multiplication | `7 * 3` | `21` |
| `/` | true division (always float) | `7 / 2` | `3.5` |
| `//` | floor division (integer) | `7 // 2` | `3` |
| `%` | modulo (remainder) | `7 % 2` | `1` |
| `**` | exponent | `2 ** 3` | `8` |

Key facts:
- `/` ALWAYS returns a float: `4 / 2` is `2.0`, not `2`
- `//` and `%` work together: `7 // 2 == 3` and `7 % 2 == 1`, and `(7 // 2) * 2 + 7 % 2 == 7`
- `%` is useful for: even/odd checks, wrapping around (Day 4 loops), extracting digits

### Order of Operations
Python follows the standard math order — parentheses first, then exponents, then multiplication/division/modulo, then addition/subtraction:

```python
print(2 + 3 * 4)     # 14, not 20
print((2 + 3) * 4)   # 20
print(2 ** 3 ** 2)   # 512 (right-to-left for **)
```

When unsure, use parentheses. Clarity beats cleverness.

## Strings

### Concatenation and Repetition
```python
first = "Carl"
last = "Jinayon"
full = first + " " + last      # "Carl Jinayon"
print("ha" * 3)                # "hahaha"
```

### Common String Methods
Methods are actions attached to a string value with a dot:

```python
name = "  Carl Jinayon  "
print(name.strip())            # remove surrounding spaces -> "Carl Jinayon"
print(name.lower())            # "  carl jinayon  "
print(name.upper())            # "  CARL JINAYON  "
print(len(name))               # 16 (includes spaces) — len() is a function, not a method
```

### Indexing (preview)
Characters are numbered from 0:
```python
word = "Python"
print(word[0])     # "P"
print(word[-1])    # "n" (negative counts from the end)
```

### f-strings (the good way to format)
Instead of messy concatenation, put variables directly inside the string:

```python
name = "Carl"
age = 20
print(f"My name is {name} and I am {age} years old.")
```

The `f` before the string means "format": `{name}` gets replaced with the variable's value. f-strings automatically convert numbers to text — no type error. Use these from now on.

## Type Conversion

| Function | Converts to | Example |
|---|---|---|
| `int(x)` | int | `int("5")` → `5`, `int(3.9)` → `3` (truncates, no rounding) |
| `float(x)` | float | `float("3.5")` → `3.5`, `float(2)` → `2.0` |
| `str(x)` | str | `str(5)` → `"5"` |

### Why input() Forces Conversions
`input()` always returns a string. To do math with user input, convert it:

```python
age_text = input("Your age: ")        # "20"  (string)
age = int(age_text)                   # 20    (integer)
print(f"Next year you will be {age + 1}")
```

### Conversion Errors
```python
int("abc")     # ValueError: invalid literal for int()
```
Converting text that is not a number raises a `ValueError`. The error message tells you exactly what was invalid.

## Common Mistakes
- `"5" + 5` → `TypeError`: mixing str and int. Fix: convert one side
- `10 / 2 == 5` → `False`! It is `5.0`. Comparing float to int with `==` usually works, but know that `/` yields floats
- `int(3.99)` → `3`, not `4`: `int()` truncates toward zero; it does not round
- `len(name)` counts characters including spaces
- Forgetting to convert `input()` before arithmetic

## Verification Checklist
- [ ] I ran every example in this lesson
- [ ] I can predict the result of `7 // 2`, `7 % 2`, `7 ** 2`, `2 + 3 * 4` correctly
- [ ] I can explain why `"5" + 5` fails and how to fix it
- [ ] I converted input() to a number and did arithmetic on it
- [ ] I used an f-string successfully

## Exercises (exercises/day_02/)
1. `basic_calc.py` — ask the user for two numbers (use `float()`), print sum, difference, product, and quotient.
2. `modulo_tricks.py` — a number, print whether it is even or odd using `%`, and print its last digit using `% 10`.
3. `string_tools.py` — ask for a name, print it with leading/trailing spaces stripped, uppercased, and its length.
4. `predict.py` — before running, write your predictions:

   ```python
   print(9 // 2)
   print(9 % 2)
   print(2 ** 5)
   print(10 / 4)
   print("ab" + "cd")
   print("ab" * 3)
   ```

5. `type_check.py` — print `type()` of: `42`, `4.2`, `"42"`, `True`, `"True"`. Before running, write what you expect for each.

## HARD MODE — Stretch Exercises (STRICTLY OPTIONAL)
Attempt ONLY after the core exercises are verified. Solvable with only Days 1–2 knowledge
(arithmetic, //, %, **, strings, conversions, f-strings). No conditionals yet — that is Day 3.

1. `time_split.py` — ask for a total number of seconds; convert to hours, minutes, seconds
   using ONLY `//` and `%` (no if-statements). Verify with 3671 → 1h 1m 11s.
2. `digits.py` — ask for a 4-digit number; extract and print each digit using ONLY `//`
   and `%` (no string conversion). Then print the digit sum.
3. `last_change.py` — a store gives change in coins of 10, 5, and 1 peso. Ask for an amount;
   compute the minimum coins needed using only integer division and modulo, printing each
   coin count. Verify: 48 → 4×10, 1×5, 3×1.

## Build
Today's build is `basic_calc.py` done well: clean f-string output, correct conversions, handles decimal numbers. Tomorrow's lesson (conditionals) will let you make this calculator handle division by zero gracefully.

## AI Interaction
Practice these patterns today:
- Instead of asking "how do I convert input to a number?", attempt it, run it, and if you get `TypeError`, paste the error + code and ask: "Why does Python say TypeError here?"
- Use the verification question: "Here is my code and its output. Is there anything wrong with my reasoning?" — get AI to *review your reasoning*, not write code.

## Mastery Check (from memory)
1. What are the four basic types and one example each?
2. `7 / 2`, `7 // 2`, `7 % 2` — results? Which are floats?
3. Why does `input()` always return a string?
4. Write from memory: a program that asks for a number and prints its square (use f-string). Run it.
5. `int(3.99)` — what does it return and why?

## Reflection
- Which operator was least intuitive? Why?
- Did you write predictions before running? That habit is the core of scientific debugging.
- Where did types bite you today?

## Key Takeaways
- Every value has a type; the type defines what operations are legal
- `/` always gives a float; `//` and `%` are the integer division pair
- `input()` returns strings — convert with `int()`/`float()` before math
- f-strings make formatting clean and safe
- `type()` and error messages are your type-debugging tools