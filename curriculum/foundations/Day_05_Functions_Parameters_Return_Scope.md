# Day 5 — Functions: Parameters, Return, Scope

## Objective
- Define functions with `def`
- Understand parameters, arguments, and `return`
- Understand local vs global scope
- Use default parameters and keyword arguments
- Build programs by composing small functions

## Prerequisites
- Day 4: loops, iteration patterns

## Why This Matters
So far, every program runs top-to-bottom as one block. Functions let you:
1. **Name** a piece of logic and reuse it anywhere — write once, call many times
2. **Abstract** — the caller does not need to know *how* the function works, only what it does
3. **Compose** — small tested pieces build bigger programs

Every real program — web apps, AI systems, ML pipelines — is built from functions. Functions are also where your math thread connects: a mathematical function `f(x)` and a Python function `f(x)` share the same core idea (input → output).

## Mental Models

### A Function Is a Recipe
A recipe takes ingredients (parameters), performs steps (body), and produces a dish (return value). You do not need to know the recipe to use it — you just call it.

### Input → Processing → Output
Every function can be thought of as:
```
parameters (inputs) → body (processing) → return value (output)
```

### Scope: The Box
Variables defined inside a function live inside that function's box. They do not exist outside it. Variables outside are visible inside (readable), but assignment inside creates a local variable. This is called **scope**.

## Defining and Calling

```python
def greet(name):
    print(f"Hello, {name}!")
    
greet("Maria")        # Hello, Maria!
greet("Carl")         # Hello, Carl!
```

- `def` — keyword that defines the function
- `greet` — function name (same naming rules as variables)
- `name` — parameter: a local variable holding the argument
- `"Maria"` — argument: the value passed in

## return — The Function's Output

`return` sends a value back to the caller. Without `return`, a function returns `None`.

```python
def square(x):
    return x * x

result = square(5)        # result = 25
print(result)

print(square(7))          # 49
```

KEY difference:
```python
def bad_square(x):
    print(x * x)          # prints, but returns None

r = bad_square(5)         # prints 25
print(r)                  # None — nothing was returned!
```

**Rule:** if you need the value, `return` it. `print` is for humans; `return` is for programs.

### return stops the function
```python
def classify(n):
    if n > 0:
        return "positive"
    if n < 0:
        return "negative"
    return "zero"         # reached only if both checks failed
```

Early returns are a clean way to handle cases one by one.

## Multiple Parameters

```python
def describe(name, age, city):
    return f"{name}, {age}, from {city}"

print(describe("Carl", 20, "Tanza"))
```

## Default Parameters and Keyword Arguments

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Maria")                  # Hello, Maria!
greet("Maria", "Good morning")  # Good morning, Maria!
greet(name="Maria", greeting="Hi")   # keyword arguments
```

- Defaults let callers omit optional inputs
- Keyword arguments make calls readable and order-independent
- Rule: parameters with defaults must come AFTER parameters without defaults

## Scope — the Box

```python
x = 10                      # global

def show():
    print(x)                # reads global — OK, prints 10

def set_x():
    x = 5                   # creates a LOCAL x — does NOT touch global
    print(x)                # 5

show()                      # 10
set_x()                     # 5
print(x)                    # 10 — global unchanged!
```

Assignment inside a function creates a new local variable, even if a global has the same name. To modify a global you'd need `global x` — **avoid this**; it makes code hard to reason about. Instead, pass values in and return values out.

## Functions and Loops — Together

```python
def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_to(10))     # 55
```

Your Day 4 mastery check is now a reusable function.

## The Math Connection

A Python function IS the programming mirror of a mathematical function:

| Math | Python |
|---|---|
| f(x) = x² | `def f(x): return x * x` |
| domain (allowed inputs) | parameters, validation |
| range (possible outputs) | return values |
| composition f(g(x)) | `f(g(x))` |

This is not a coincidence — the name comes from math. Your algebra thread starts this week; keep this table in mind.

## Common Mistakes
- Forgetting `return` — function returns `None` and the caller gets nothing
- `print` instead of `return` — output visible but unusable
- Calling a function before defining it — Python reads top to bottom; define before call
- Assuming a function can modify globals by assignment — it creates a local
- Confusing parameters (definition) with arguments (call)
- Typo in function name → `NameError`

## Verification Checklist
- [ ] I can define a function with parameters and return a value
- [ ] I can call a function and use its return value
- [ ] I can explain why `print` ≠ `return`
- [ ] I can explain what local scope means with an example
- [ ] I can use default parameters and keyword arguments

## Exercises (exercises/day_05/)
1. `my_functions.py` — define and test: `add(a, b)`, `multiply(a, b)`, `absolute_value(n)` (no built-in abs — write your own with conditionals)
2. `temperature.py` — `celsius_to_fahrenheit(c)` and `fahrenheit_to_celsius(f)`. Formulas: F = C × 9/5 + 32; C = (F − 32) × 5/9
3. `validator_fn.py` — turn your Day 4 validation-retry into `get_int(prompt, min, max)` that loops until valid and RETURNS the valid integer
4. `string_utils.py` — `reverse_string(s)` (loop-based, no slicing), `count_vowels(s)`, `is_palindrome(s)` (reuse reverse_string)
5. `calculator_fns.py` — refactor your Day 2 `basic_calc.py` into functions: `add`, `subtract`, `multiply`, `divide` + a `main()` that reads input and calls them

## Build
`calculator_fns.py` is today's build: clean function decomposition, a `main()` entry point, validation before conversion, division-by-zero handled in `divide()` (return a message or None — your choice, and say why).

## AI Interaction
Good prompts:
- "My function returns None. Here is my code — where did I forget return?"
- "Why doesn't my function change the global variable? Here's my code."
- "Is passing a value and returning it cleaner than using `global` here? Why?"
- After writing, ask: "Review my functions for scope and return correctness" — then verify each claim by running.

## Mastery Check (from memory)
1. Write `max_of_three(a, b, c)` returning the largest. Test it.
2. What does a function return if there is no `return` statement?
3. `x = 5` inside a function, `x = 10` outside. After calling the function, what is the global `x`? Why?
4. Write `is_even(n)` returning a boolean; use it in a loop that prints "even"/"odd" for 1..10.

## HARD MODE — Stretch Exercises (STRICTLY OPTIONAL)
Attempt ONLY after the core exercises are verified. These are deliberately harder than the lesson —
they push your reasoning. Failure is fine: attempt, struggle, debug. Each must be solved with only
Day 1–5 knowledge (variables, conditionals, loops, functions, return). No f-strings limits, no
built-in tricks beyond what you know.

1. `collatz.py` — write `collatz_steps(n)` that, for a positive integer n, repeatedly applies:
   if even, divide by 2; if odd, multiply by 3 and add 1. It should print each number in the
   sequence and RETURN the number of steps until reaching 1. Verify: `collatz_steps(6)` → 8 steps.
   (Every starting number eventually reaches 1 — unproven conjecture, but your loop must stop
   for any reasonable input. Why is a `while` loop the right choice here?)

2. `primes.py` — write `is_prime(n)` returning True/False, correctly handling 0, 1, negatives,
   and 2. Then write `primes_up_to(n)` that returns the count of primes ≤ n by calling
   `is_prime` (function composition). Verify: `primes_up_to(10)` → 4 (2,3,5,7).

3. `gcd_lcm.py` — write `gcd(a, b)` using the Euclidean algorithm (hint: repeatedly replace the
   larger number with `larger % smaller` until one is 0). Then `lcm(a, b)` = `a * b // gcd(a, b)`.
   Verify: `gcd(48, 18)` → 6, `lcm(4, 6)` → 12. This is real math: the function IS the algorithm.

4. `perfect_numbers.py` — a perfect number equals the sum of its proper divisors (divisors less
   than itself). Write `is_perfect(n)`, then find ALL perfect numbers below 10000 by looping.
   Expected: 6, 28, 496, 8128. Hint: you only need to check divisors up to `n // 2` — why?

The point of Hard Mode: these are exactly the size of problem you must decompose — and you now
have the tools (functions + return) to decompose them.

## Reflection
- Did you catch yourself printing when you should have returned?
- Was scope intuitive or surprising? What experiment would confirm your understanding?
- Which function was hardest to decompose? Why?

## Key Takeaways
- `def` defines, `return` produces output, parameters receive input
- `print` is for humans, `return` is for programs
- Assignment inside a function = local variable (scope)
- Defaults and keyword arguments make functions flexible and readable
- Small functions compose into large programs — and Python functions mirror math functions