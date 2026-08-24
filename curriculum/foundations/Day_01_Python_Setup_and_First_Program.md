# Day 1 — Python Setup, First Program, Variables, and the Terminal

## Objective
- Verify Python is installed and working
- Learn basic terminal navigation (pwd, ls, cd, mkdir)
- Write and run your first Python program
- Understand variables, print, and input
- Learn how errors appear and how to read them

## Prerequisites
- None. This is the starting point.

## Why This Matters
Every skill in this curriculum — DSA, web, databases, AI, ML — is exercised by writing and running code. If you cannot reliably create a file, run it, and read the output, nothing else works. This lesson establishes the loop you will use for the rest of your career:

```
Write code → Run it → See output → Find errors → Fix → Run again
```

## Mental Models

### The Program = Instructions
A Python program is a plain text file containing step-by-step instructions. Python reads the file from top to bottom and executes each line in order.

### The Computer is Literal
The computer does exactly what you write — nothing more, nothing less. If your program prints the wrong thing, it is not the computer's fault. The program is doing exactly what you told it to do. This is the most important mental model in debugging: **the computer is never wrong; your instructions are.**

### Terminal = Text Interface to the Computer
The terminal lets you control the computer by typing commands instead of clicking. It looks intimidating but is just: type a command, press Enter, read the output.

## Definitions
- **Program / script**: a text file with instructions for the computer
- **Run / execute**: making the computer follow the instructions
- **Output**: what the program displays after running
- **Error message**: the computer's way of telling you what went wrong
- **Variable**: a named box that holds a value
- **String**: text, written in quotes like `"hello"`
- **Integer**: a whole number like `42`

## The Terminal

### Your Location
The terminal always has a "current directory" (where you are). Key commands:

| Command | Meaning | Example |
|---|---|---|
| `pwd` | Print Working Directory — where am I? | `pwd` |
| `ls` | List files in current directory | `ls` |
| `cd dir` | Change Directory — move into a folder | `cd exercises` |
| `cd ..` | Move up one folder | `cd ..` |
| `mkdir name` | Make a new directory | `mkdir day_01` |
| `python3 file.py` | Run a Python file | `python3 hello.py` |

### Suggestion: Run Terminal Commands Yourself
In OpenCode I can run commands for you, but you must also practice typing them in your own terminal. Muscle memory matters.

### Comments (added later, when you started using them)
Lines starting with `#` are ignored by Python — they exist for humans:

```python
# This whole line is a comment
x = 5    # comments can also follow code
```

Use them for WHY, not what: `# skip 16-60 to avoid double-count` beats `# subtract`.

## First Program

Create the file `exercises/day_01/hello.py` with a text editor and type:

```python
print("Hello, world!")
```

Save it. In the terminal, from `exercises/day_01/`:

```bash
python3 hello.py
```

Expected output:

```
Hello, world!
```

### What Happened
1. Python opened `hello.py`
2. Read the line `print("Hello, world!")`
3. Executed the `print` function — it displays whatever is inside the parentheses
4. The text `"Hello, world!"` is a **string** (text value)

## Variables

A variable stores a value for later use. Think of a labeled box:

```python
name = "Maria"
age = 20
print(name)
print(age)
```

Output:

```
Maria
20
```

Rules:
- `=` means **assignment**: put the value on the right into the box named on the left
- The variable name is on the left, the value on the right
- Names are case-sensitive: `Age` and `age` are different boxes
- Good names matter: `student_age` is better than `x` when the meaning is "student's age"

## print() — The Output Function

`print()` displays values. You can print several things at once by separating with commas:

```python
name = "Maria"
age = 20
print("My name is", name, "and I am", age, "years old.")
```

Output:

```
My name is Maria and I am 20 years old.
```

Python inserts a space between comma-separated items.

### OPTIONAL PREVIEW (not required for Day 1)
`print()` has two useful extra parameters you will meet later when you need them:
- `sep="..."` — change the separator between items (default is a space)
- `end="..."` — change what is printed after all items (default is a newline)

```python
print("a", "b", "c", sep="-")   # a-b-c
print("a", end="")              # no newline after "a"
print("b")                      # ab  (same line as above)
```

These are preview material only — do not spend time on them today.

## input() — Reading From the User

`input()` pauses the program and waits for the user to type and press Enter. The typed text comes back as a **string**:

```python
name = input("What is your name? ")
print("Hello,", name)
```

Run it. Type your name when prompted. The program greets you.

Important: `input()` ALWAYS returns a string, even if the user types a number. `"20"` (text) is not the same as `20` (number). We will deal with this in a later lesson.

## Errors: Your New Best Friend

Errors are not failures. They are the computer telling you exactly what it does not understand. Read them.

### Example: Misspelled Function

```python
prnit("Hello")
```

```
Traceback (most recent call last):
  File "hello.py", line 1, in <module>
    prnit("Hello")
    ^^^^^
NameError: name 'prnit' is not defined
```

Read it like this:
- `File "hello.py", line 1` — where the problem is
- `NameError: name 'prnit' is not defined` — what the problem is: Python does not know what `prnit` means
- The `^^^^^` — the exact position

### The Debugging Loop (memorize this)
1. Read the error message
2. Find the file and line number it mentions
3. Look at that line
4. Form a hypothesis about what is wrong
5. Fix it
6. Run again
7. Repeat until the program does what you want

## Common Mistakes (Day 1)
- Forgetting quotes around text: `print(Hello)` → `NameError` (Python thinks `Hello` is a variable)
- Mismatched quotes: `print("hi')` → `SyntaxError`
- Printing a variable before it exists → `NameError`
- Typing `=` when you mean "is this equal?" (that is `==` — later lesson)

## Verification Checklist
- [ ] `python3 hello.py` produced `Hello, world!`
- [ ] You can explain what each line of your program does
- [ ] You can read an error message and identify file + line + error type
- [ ] You can predict what `print` will output before running

## Exercises (do these in exercises/day_01/)
1. `greet.py` — Ask for the user's name, then print a greeting with their name.
2. `profile.py` — Create variables for your name, age, and city. Print a sentence using all three.
3. `predict.py` — Before running, write down what you expect this to print, then run it:

   ```python
   x = 5
   y = 10
   print("x + y =", x + y)
   ```

4. **Break it deliberately**: Write `hello.py` with a typo (e.g. `pritn("hi")`). Run it. Read the error out loud: what type is it? What line? Then fix it. This teaches you that errors are diagnosable.

## HARD MODE — Stretch Exercises (STRICTLY OPTIONAL)
Attempt ONLY after the core exercises are verified. Solvable with only Day 1 knowledge
(print, input, variables, strings, errors). Failure is fine — struggle, debug, retry.

1. `receipt.py` — three items with prices stored in variables. Print a formatted receipt
   using ONLY `print` with `sep` and `end` (no f-strings yet): aligned columns, a total
   line, and a "change from 500 pesos" line. Exact spacing matters — measure your output.
2. `madlibs.py` — ask for a name, place, number, and verb; print a story where they fit
   grammatically in every slot. Run it 3 times with different inputs — every sentence must
   still read correctly.
3. `ascii_tag.py` — print your name inside a box drawn with `=`, `|`, and spaces. The box
   must look correct for a 10-letter name AND a 3-letter name (compute the padding, don't
   hardcode it).

## Build
There is no separate project today. The exercises ARE the build. From tomorrow, exercises become slightly bigger.

## AI Interaction — Level 1 Starts Today
The correct way to use OpenCode as a beginner:

**Good question:**
> "I ran python3 greet.py and got NameError on line 3. Here is my code: ... Why does Python not recognize `username`?"

**Bad question:**
> "Write me a program that greets the user."

The difference: the first question shows you attempted, shows your actual error, and asks for understanding. The second asks AI to do the thinking for you.

**Rule for this curriculum:**
1. Try it yourself first
2. If you are stuck, ask OpenCode for a *hint*, not the full answer
3. When you get an error, paste the error + your code and ask *why*
4. Never claim you understand code you did not write

## Mastery Check (answer from memory, no looking)
1. What does `print()` do? What does `input()` do?
2. What type of value does `input()` always return?
3. You run a program and see `NameError: name 'x' is not defined` on line 4. What does this mean in plain words?
4. Write, from memory, a program that asks for the user's name and prints "Hello, <name>!" — then run it and verify.

## Reflection
- What did you find confusing?
- Did you run every exercise, or only read them? (Running is the only way that counts.)
- Did any error surprise you? What did the error message teach you?

## Key Takeaways
- Programs are instructions; the computer follows them literally
- `print()` outputs, `input()` reads text, variables store values
- Errors tell you exactly where and what went wrong — read them
- Always verify by running: code you did not run is code that does not exist