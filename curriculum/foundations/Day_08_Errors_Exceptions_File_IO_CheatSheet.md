# Day 8 Cheat Sheet — Exceptions and File I/O

## Exception Hierarchy (Key Ones)
```
Exception
 ├── ValueError        # bad value for operation
 ├── TypeError         # wrong type for operation
 ├── KeyError          # missing dict key
 ├── IndexError        # bad list index
 ├── FileNotFoundError # missing file
 ├── PermissionError   # no access
 ├── ZeroDivisionError # / by zero
 ├── JSONDecodeError   # bad JSON
 └── Exception         # catch-all (use sparingly)
```

## Try/Except/Else/Finally
```python
try:
    risky()
except SpecificError as e:
    handle(e)
except AnotherError:
    handle()
else:
    runs_if_no_exception()
finally:
    always_runs()    # even after return/break
```

### Rules
- Specific exceptions first, generic last
- `as e` captures the exception object
- `else` runs ONLY if no exception
- `finally` ALWAYS runs (even return/break)

## Raising Exceptions
```python
raise ValueError("bad input")
raise MyError("msg") from e   # chaining
```

## Custom Exception
```python
class MyError(ValueError):
    def __init__(self, msg, code):
        self.code = code
        super().__init__(msg)
```

## File I/O — Always Use `with`
```python
# Read
with open("file.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Write
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("text")

# Append
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("line\n")

# Lines
with open("file.txt") as f:
    for line in f:
        process(line.strip())
```

## Modes
| Mode | Read | Write | Create | Truncate |
|---|---|---|---|---|
| r | ✓ | ✗ | ✗ | ✗ |
| w | ✗ | ✓ | ✓ | ✓ |
| a | ✗ | ✓ | ✓ | ✗ |
| r+ | ✓ | ✓ | ✗ | ✗ |

## Encoding & Pathlib
```python
# ALWAYS specify encoding
with open("f.txt", "r", encoding="utf-8") as f:

from pathlib import Path
p = Path("data/file.txt")
p.read_text(encoding="utf-8")
p.write_text("hello", encoding="utf-8")
p.exists()
p.parent / "other.txt"
```

## JSON
```python
import json
# Write
json.dump(obj, f, indent=2)
# Read
obj = json.load(f)
```

## CSV
```python
import csv
# Write
with open("f.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["a","b"])
    w.writerows(rows)
# Read
with open("f.csv") as f:
    for row in csv.DictReader(f):
        print(row["col"])
```

## Safe File Read Pattern
```python
def safe_read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None
    except PermissionError:
        raise
```

## JSON
```python
json.dump(obj, f, indent=2)
obj = json.load(f)
```

## CSV
```python
# Write
with open("f.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(headers)
    w.writerows(rows)

# Read
with open("f.csv") as f:
    for row in csv.DictReader(f):
        print(row["col"])
```

## Key Rules
- ALWAYS use `with` for files
- ALWAYS specify `encoding="utf-8"`
- Use `newline=""` for CSV
- Catch specific exceptions first
- Never bare `except:` — use `except Exception`
- `finally` runs even after return/break/exception

## Active Recall
1. What does `finally` guarantee?
2. Difference between `except Exception` and bare `except:`?
3. When does `finally` NOT run?
4. Write safe JSON read with error handling.
5. Difference between `FileNotFoundError` and `PermissionError`?