# Expense Tracker v0.3 — Project Specification

> Version 0.3 adds robustness: custom exceptions, corrupt-file recovery, and a reusable input validation family. This is the hardening phase — making the tool production-ready.

---

## What's New in v0.3

| Feature | v0.2 | v0.3 |
|---------|------|------|
| Add/list/filter/summary | ✅ | ✅ |
| Modular structure | ✅ | ✅ |
| **Custom exceptions** | ❌ | ✅ NEW |
| **Corrupt file recovery** | Partial | ✅ HARDENED |
| **Reusable `get_*` input family** | ❌ | ✅ NEW |
| **Graceful missing file handling** | Partial | ✅ HARDENED |

---

## Feature: Custom Exceptions

### FR-1: `InvalidAmountError`
- Inherits from `ValueError`
- Raised when amount is not a valid positive number
- Message: `"Amount must be a positive number."`

### FR-2: `InvalidDateError`
- Inherits from `ValueError`
- Raised when date doesn't match `YYYY-MM-DD` format or is not a real date
- Message: `"Invalid date. Use YYYY-MM-DD."`

### FR-3: `InvalidCategoryError`
- Inherits from `ValueError`
- Raised when category is not in the fixed list
- Message: `"Invalid category. Choose: food, transport, rent, utilities, other"`

### FR-4: `InvalidMonthError`
- Inherits from `ValueError`
- Raised when month doesn't match `YYYY-MM` format
- Message: `"Invalid month. Use YYYY-MM."`

### File: `exceptions.py`
```python
class InvalidAmountError(ValueError):
    """Raised when amount is not a valid positive number."""
    pass

class InvalidDateError(ValueError):
    """Raised when date is invalid or wrong format."""
    pass

class InvalidCategoryError(ValueError):
    """Raised when category is not in the allowed list."""
    pass

class InvalidMonthError(ValueError):
    """Raised when month format is invalid."""
    pass
```

---

## Feature: Corrupt File Recovery

### FR-5: Graceful corrupt file handling
- If `expenses.json` exists but contains invalid JSON:
  - Print warning: `"expenses.json is corrupted. Starting with empty list. Your old file was renamed to expenses.json.bak"`
  - Rename corrupted file to `expenses.json.bak` (backup)
  - Create fresh `expenses.json` with `[]`
  - Continue normally

### FR-6: Graceful missing file handling
- If `expenses.json` doesn't exist:
  - Print: `"No data file found. Starting fresh."`
  - Create `expenses.json` with `[]`
  - Continue normally

### FR-7: Permission error handling
- If file can't be read/written due to permissions:
  - Print: `"Permission denied: cannot access expenses.json"`
  - Return empty list (for load) or print error (for save)
  - Don't crash

---

## Feature: Reusable `get_*` Input Family

### FR-8: `get_amount()` → `float`
- Prompt: `"Enter amount: "`
- Validate: must be a valid float AND > 0
- On invalid: print error, re-prompt
- Return: validated `float`

### FR-9: `get_category()` → `str`
- Prompt: `"Enter category (food, transport, rent, utilities, other): "`
- Validate: must be in `CATEGORY_LIST`
- On invalid: print error, re-prompt
- Return: validated `str`

### FR-10: `get_date()` → `str`
- Prompt: `"Enter date (YYYY-MM-DD): "`
- Validate: must match `YYYY-MM-DD` and be a real date
- On invalid: print error, re-prompt
- Return: validated `str`

### FR-11: `get_month()` → `str`
- Prompt: `"Enter month (YYYY-MM): "`
- Validate: must match `YYYY-MM`
- On invalid: print error, re-prompt
- Return: validated `str`

### FR-12: `get_note()` → `str`
- Prompt: `"Enter note (optional): "`
- Return: input string (empty string if nothing entered)

### FR-13: `get_menu_choice(options)` → `int`
- Display numbered menu from list of options
- Validate: must be a valid integer within range
- On invalid: print error, re-prompt
- Return: validated `int`

---

## File Structure

```
version0.3/
├── main.py          # Menu loop (slimmed down — uses get_* family)
├── models.py        # create_expense
├── storage.py       # load/save with corrupt recovery
├── reports.py       # list/filter/summary
├── exceptions.py    # Custom exception classes
├── input_handler.py # get_amount, get_category, get_date, get_month, get_note, get_menu_choice
└── expenses.json    # Data
```

### Import Rules:
```
main.py imports: storage, reports, models, input_handler
input_handler.py imports: exceptions, models (for CATEGORY_LIST)
models.py imports: storage (for save)
storage.py imports: json, os (for rename), exceptions
reports.py imports: (none — pure functions)
exceptions.py imports: (none — pure classes)
```

---

## Refactor: `main.py` After get_* Family

### Before (v0.2):
```python
# main.py had validation logic inline — 127 lines
while True:
    try:
        amount = float(input("Enter amount: "))
        try:
            models.validate_amount(amount)
        except ValueError as e:
            print(e)
        else:
            break
    except ValueError:
        print("Invalid amount. Enter a number.")
```

### After (v0.3):
```python
# main.py is now slim — validation delegated to input_handler
amount = input_handler.get_amount()
category = input_handler.get_category()
date = input_handler.get_date()
note = input_handler.get_note()
models.create_expense(data, amount, category, date, note)
```

---

## Validation Rules (same logic, new exceptions)

| Input | Exception | Error message |
|-------|-----------|---------------|
| Amount ≤ 0 | `InvalidAmountError` | "Amount must be a positive number." |
| Amount not a number | `InvalidAmountError` | "Amount must be a positive number." |
| Invalid category | `InvalidCategoryError` | "Invalid category. Choose: food, transport, rent, utilities, other" |
| Bad date format | `InvalidDateError` | "Invalid date. Use YYYY-MM-DD." |
| Impossible date | `InvalidDateError` | "Invalid date. Use YYYY-MM-DD." |
| Bad month format | `InvalidMonthError` | "Invalid month. Use YYYY-MM." |
| Menu out of range | `ValueError` | "Invalid choice." |

---

## Edge Cases to Test

| # | Case | Expected behavior |
|---|------|-------------------|
| 1 | All v0.1 + v0.2 edge cases pass | No regression |
| 2 | `expenses.json` is empty file `""` | Treated as `[]`, fresh start |
| 3 | `expenses.json` contains `"not json"` | Corrupt → rename to `.bak`, fresh start |
| 4 | `expenses.json` contains `{"broken":` | Corrupt → rename to `.bak`, fresh start |
| 5 | `expenses.json` doesn't exist | Create fresh, no crash |
| 6 | `expenses.json` is read-only | Print permission error, return `[]` |
| 7 | Enter string for amount | `InvalidAmountError`, re-prompt |
| 8 | Enter negative amount | `InvalidAmountError`, re-prompt |
| 9 | Enter invalid category | `InvalidCategoryError`, re-prompt |
| 10 | Enter bad date format | `InvalidDateError`, re-prompt |
| 11 | Enter impossible date | `InvalidDateError`, re-prompt |
| 12 | Enter bad month format | `InvalidMonthError`, re-prompt |
| 13 | Corrupt file backup exists | `expenses.json.bak` created |
| 14 | All custom exceptions inherit `ValueError` | `except ValueError` still catches them |
| 15 | `get_*` functions work independently | Can call from any module |

---

## Acceptance Criteria

- [ ] All v0.1 + v0.2 functionality still works (no regression)
- [ ] `exceptions.py` defines 4 custom exceptions (all inherit `ValueError`)
- [ ] Corrupt file → rename to `.bak` + fresh start + warning
- [ ] Missing file → create fresh + message
- [ ] Permission error → graceful fallback, no crash
- [ ] `input_handler.py` implements all 6 `get_*` functions
- [ ] `main.py` uses `get_*` family (validation logic removed from main)
- [ ] All 15 edge cases pass
- [ ] Clean commit with descriptive message

---

## How to Run

```bash
cd projects/project_01_expense_tracker/version0.3
python3 main.py
```

---

## Commit Strategy

```bash
git add version0.3/
git commit -m "feat: v0.3 — custom exceptions, corrupt recovery, get_* input family"
```

---

## Definition of Done (Project 1 Complete)

After v0.3 is verified, Project 1 is DONE. Remaining:
- README.md (problem statement, usage, structure, design decisions, limitations, AI disclosure)
- Clean commit history
- Domain journal entry #1

---

*Specification version: 0.3 | Created: 2026-08-30 | Project: Expense Tracker*
