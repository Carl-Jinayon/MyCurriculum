# Day 8 — Errors, Exceptions, and File I/O: Building Robust Programs

## Objective
- Understand the exception hierarchy and common built-in exceptions
- Master try/except/else/finally for robust error handling
- Raise and create custom exceptions
- Read and write files safely with context managers
- Work with paths using pathlib
- Handle JSON and CSV data
- Build programs that fail gracefully and recover

## Prerequisites
- Day 7: tuples, sets, dicts
- Day 5: functions with return values
- Day 3: conditionals and boolean logic

## Why This Matters
Real programs run in messy environments: files go missing, networks fail, users give bad input, disks fill up. Code that assumes everything works will crash in production. Code that anticipates and handles failures is what separates prototypes from professional software. File I/O is also how programs persist data — the bridge between a running process and durable storage.

## Mental Models

### 1. Exceptions Are Objects, Not Errors
An exception is an object that represents something went wrong. When raised, it propagates up the call stack until caught or the program crashes. This is not an error in your code — it's a control flow mechanism.

### 2. The try/except/else/finally Flow
```
try:
    risky_code()
except SpecificError:
    handle_it()
except AnotherError as e:
    log_and_recover(e)
else:
    runs_if_no_exception()
finally:
    cleanup_always_runs()
```

Key rules:
- except catches the exception type and its subclasses
- Multiple except blocks: most specific first
- else runs only if NO exception occurred
- finally ALWAYS runs (even after return, break, continue)

### 3. Fail Fast, Fail Loud
Don't swallow exceptions silently. Catch what you can handle; let the rest bubble up. Silent failures are the worst bugs.

### 4. File I/O = External State
Files are outside your program's memory. They can disappear, change, be locked, or be too big for memory. Always use context managers (`with`) — they guarantee cleanup even on exceptions.

## Exception Hierarchy (Key Built-ins)

```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── AssertionError
      ├── AttributeError
      ├── EOFError
      ├── ImportError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── NameError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── IsADirectoryError
      ├── RuntimeError
      ├── StopIteration
      ├── SyntaxError
      ├── TypeError
      ├── ValueError
      └── UnicodeError
           ├── UnicodeDecodeError
           └── UnicodeEncodeError
```

## Try/Except/Else/Finally — The Full Syntax

```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Arguments must be numbers")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("Division attempted")  # runs ALWAYS

# Multiple except — specific first!
try:
    process(data)
except (ValueError, TypeError) as e:
    log_bad_data(e)
except Exception as e:          # catch-all last
    report_crash(e)
```

### The `as` Clause
```python
except ValueError as e:
    print(f"Bad value: {e}")     # e is the exception instance
```

### Else Block — Runs Only on Success
```python
try:
    result = risky()
except ValueError:
    handle_error()
else:
    save_result(result)    # only if no exception
finally:
    cleanup()              # always
```

### Raising Exceptions
```python
def withdraw(amount):
    if amount > balance:
        raise ValueError(f"Insufficient funds: need {amount}, have {balance}")
    return balance - amount
```

### Custom Exceptions
```python
class InsufficientFundsError(ValueError):
    """Raised when withdrawal exceeds balance."""
    def __init__(self, needed, available):
        self.needed = needed
        self.available = available
        super().__init__(f"Need {needed}, have {available}")

def withdraw(amount):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
```

## File I/O — The Right Way

### Context Managers (ALWAYS use `with`)
```python
# Reading
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Writing
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")

# Append
with open("log.txt", "a", encoding="utf-8") as f:
    f.write(f"{timestamp}: event\n")
```

### File Modes
| Mode | Meaning | Creates? | Truncates? | Position |
|---|---|---|---|---|
| `r` | read | no | no | start |
| `w` | write | yes | yes | start |
| `a` | append | yes | no | end |
| `r+` | read/write | no | no | start |
| `w+` | write/read | yes | yes | start |
| `a+` | append/read | yes | no | end |
| `rb`, `wb` | binary modes | | | |

### Encoding — Always Specify
```python
# GOOD
with open("file.txt", "r", encoding="utf-8") as f:

# BAD (system-dependent, breaks on non-ASCII)
with open("file.txt", "r") as f:
```

### Pathlib — Modern Path Handling
```python
from pathlib import Path

data_dir = Path("data")
file_path = data_dir / "input.txt"

# Path operations
file_path.exists()
file_path.is_file()
file_path.parent
file_path.name
file_path.suffix
file_path.stem

# Read/write with pathlib
content = file_path.read_text(encoding="utf-8")
file_path.write_text("content", encoding="utf-8")

# Iterate directory
for file in data_dir.glob("*.txt"):
    print(file.name)
```

### Reading Strategies
```python
# Entire file (small files)
with open("file.txt") as f:
    content = f.read()

# Line by line (memory efficient)
with open("file.txt") as f:
    for line in f:
        process(line.strip())

# All lines as list
with open("file.txt") as f:
    lines = f.readlines()

# Specific number of bytes
with open("file.txt") as f:
    chunk = f.read(1024)
```

### Writing Strategies
```python
# Write all at once
with open("out.txt", "w") as f:
    f.write(content)

# Write lines
with open("out.txt", "w") as f:
    for item in items:
        f.write(f"{item}\n")

# Using writelines (no automatic newlines)
with open("out.txt", "w") as f:
    f.writelines(f"{item}\n" for item in items)
```

## Structured Data — JSON and CSV

### JSON
```python
import json

# Write
data = {"name": "Carl", "age": 20, "skills": ["python", "sql"]}
with open("profile.json", "w") as f:
    json.dump(data, f, indent=2)

# Read
with open("profile.json") as f:
    data = json.load(f)
```

### CSV
```python
import csv

# Write
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "grade"])
    writer.writerow(["Carl", 20, "A"])
    writer.writerows([("Maria", 21, "B"), ("John", 19, "A")])

# Read
with open("students.csv") as f:
    reader = csv.DictReader(f)  # each row is a dict
    for row in reader:
        print(row["name"], row["grade"])
```

### newlines="" — Prevents Blank Lines on Windows
```python
# ALWAYS use newline="" with csv.writer
with open("file.csv", "w", newline="") as f:
```

## Error Handling in File Operations

```python
def read_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config not found: {path}")
        return DEFAULT_CONFIG
    except json.JSONDecodeError as e:
        print(f"Bad JSON in {path}: {e}")
        return DEFAULT_CONFIG
    except PermissionError:
        print(f"Permission denied: {path}")
        raise  # re-raise — can't recover
```

## Common Exception Patterns

### EAFP vs LBYL
```python
# EAFP (Easier to Ask Forgiveness than Permission) — Pythonic
try:
    result = data[key]
except KeyError:
    return default

# LBYL (Look Before You Leap) — sometimes necessary
if key in data:
    result = data[key]
```

### Exception Chaining
```python
try:
    process()
except ValueError as e:
    raise RuntimeError("Processing failed") from e  # preserves original traceback
```

### Bare Except — AVOID
```python
# BAD
except:
    pass

# GOOD
except Exception as e:
    logger.error(e)
    raise
```

## Verification Checklist
- [ ] I can list 5 built-in exceptions and when they occur
- [ ] I can write try/except/else/finally correctly
- [ ] I can raise and catch custom exceptions
- [ ] I always use `with` for file operations
- [ ] I can read/write JSON and CSV correctly
- [ ] I handle file-not-found and permission errors gracefully
- [ ] I understand exception propagation and `finally` guarantees

## Exercises (exercises/Foundations/day_08/)
1. `exceptions_01.py` — Write `safe_int(s)` that returns `int(s)` or `None` if conversion fails (catch ValueError). Test with "42", "3.14", "hello".
2. `exceptions_02.py` — Define `PositiveIntegerError(ValueError)`. Write `get_positive_int(prompt)` that loops until user enters positive int, raising your custom exception for negative/zero. Catch and retry in a loop.
3. `file_read.py` — Read `data/sample.txt` (create it first), print lines with line numbers. Handle FileNotFoundError gracefully.
4. `file_write.py` — Write a list of 5 dicts (name, score) to `scores.csv` with headers. Read back and print average score.
5. `json_config.py` — Write a config dict to `config.json`. Read it back. Add error handling for missing file and bad JSON.
6. `log_analyzer.py` — Build a log file analyzer: read `app.log` (create sample), parse lines with format `LEVEL: message`, count ERROR/WARNING/INFO, print summary. Handle missing file and malformed lines.

## Build
`log_analyzer.py` done well is today's build: a real tool that parses structured logs — the skill you'll use for debugging, monitoring, and observability.

## AI Interaction
Good prompts:
- "What exception does open() raise when file doesn't exist?"
- "Why does my JSON decode fail? Here's the error and file snippet."
- "How do I retry a file operation 3 times before giving up?"
- Do NOT ask "write a file reader" — write it first, ask for review.

## HARD MODE (optional)
1. `retry.py` — Write a decorator `@retry(max_attempts=3, exceptions=(IOError,))` that retries a function on specified exceptions with exponential backoff.
2. `atomic_write.py` — Implement atomic file write: write to temp file, then `os.replace()` (atomic on POSIX). Guarantees file is never partially written.
3. `config_class.py` — Build a `Config` class: loads from JSON, supports `config.key` attribute access, validates schema on load, saves back on change.

## Mastery Check (from memory)
1. What does `finally` guarantee?
2. What's the difference between `except Exception` and bare `except:`?
3. When does `finally` NOT run?
4. Write code to safely read a JSON file with proper error handling.
5. What's the difference between `FileNotFoundError` and `PermissionError`?
6. Write a context manager that times how long a block takes.

## Reflection
- When did an unhandled exception crash your program this week?
- When did catching an exception save your program?
- When did you catch too broadly and hide a bug?

## Key Takeaways
- Exceptions are objects — use the hierarchy, catch specifically
- `try/except/else/finally` gives full control flow
- `with` is non-negotiable for files — guarantees cleanup
- Always specify encoding; use `newline=""` for CSV
- Custom exceptions make error handling expressive
- JSON/CSV are your interchange formats — master them
- Fail fast, fail loud, fail with context