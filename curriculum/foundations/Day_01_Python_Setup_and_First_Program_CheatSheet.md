# Day 1 Cheat Sheet — Python Setup, First Program, Variables

## Key Commands
| Command | What it does |
|---|---|
| `pwd` | Where am I? |
| `ls` | List files here |
| `cd dir` / `cd ..` | Enter folder / go up |
| `mkdir name` | Make folder |
| `python3 file.py` | Run a Python file |

## Core Ideas
- **Program** = instructions in a file, executed top to bottom
- **Computer is literal** — it does exactly what you wrote
- **Variable** = labeled box holding a value: `name = "Maria"`
- **String** = text in quotes: `"hello"`
- **Integer** = whole number: `42`

## Syntax
```python
print("Hello")              # output
print("Age:", age)          # comma = space between items
name = input("Name? ")      # pauses, waits for user, ALWAYS returns string
```

## The Debugging Loop
1. Read error message → 2. Find file + line → 3. Look at the line → 4. Hypothesize → 5. Fix → 6. Run again

## Common Day-1 Errors
- `NameError: name 'X' is not defined` → X is not a variable, or you misspelled it (or forgot quotes)
- `SyntaxError` → Python can't parse the line (e.g. mismatched quotes)
- `File "x.py", line N` → the error is on line N of file x.py

## Must-Know Checklist
- [ ] I can create a .py file and run it with `python3`
- [ ] I can read an error: type, file, line
- [ ] I know `input()` always returns a string
- [ ] I ran all 4 exercises and verified outputs

## Active Recall Questions
1. What does `=` do in Python?
2. What happens if you `print` a variable that was never created?
3. `print("a", "b")` — how many spaces between a and b?
4. Why is `prnit("hi")` an error, and what type of error?

## AI Usage Rule
Try first → ask for hints, not full answers → paste error + code when stuck → never claim code you didn't write.