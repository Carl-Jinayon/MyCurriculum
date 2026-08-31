# Expense Tracker v0.1 — Project Specification

> A focused, version-0.1-only specification for the Expense Tracker project. This is the working document for the first sprint — everything listed here must be built, tested, and verified before moving to v0.2.

---

## Project Overview

A command-line expense tracker that lets users add expenses, list them, and view monthly summaries. Data persists to a JSON file between sessions. This is the Stage 0 capstone project — it demonstrates integration of every skill learned in Days 1–10.

---

## v0.1 Scope

### IN (must build)
- Interactive menu loop (add / list / monthly summary / exit)
- Add expense: amount, category, date, note
- Input validation for all fields
- List expenses with index numbers
- Monthly summary: total per category + grand total
- JSON file persistence (load on start, save after every change)
- Graceful handling of missing data file (first run)

### OUT (deferred to v0.2/v0.3)
- ~~Category/month filtering on list~~ (v0.2)
- ~~Custom exceptions~~ (v0.3)
- ~~Corrupt file recovery~~ (v0.3)
- ~~Reusable `get_*` input family~~ (v0.3)
- ~~Edit/delete records~~ (stretch goal)
- ~~Budget warnings~~ (stretch goal)
- ~~CSV export~~ (stretch goal)

---

## Data Model

Each expense is a single dictionary:

```json
{
  "amount": 250.0,
  "category": "food",
  "date": "2026-08-24",
  "note": "lunch"
}
```

| Field | Type | Constraints |
|-------|------|-------------|
| `amount` | `float` | Must be > 0 |
| `category` | `str` | Must be one of: `food`, `transport`, `rent`, `utilities`, `other` |
| `date` | `str` | Format: `YYYY-MM-DD` (validated with `datetime.strptime`) |
| `note` | `str` | Optional (can be empty string) |

The JSON file is a list of these dicts:
```json
[
  {"amount": 250.0, "category": "food", "date": "2026-08-24", "note": "lunch"},
  {"amount": 1500.0, "category": "rent", "date": "2026-08-01", "note": "august rent"}
]
```

---

## Functional Requirements

### FR-1: Menu Loop
- Display numbered menu on startup and after each action
- Options: `1) Add expense`, `2) List expenses`, `3) Monthly summary`, `4) Exit`
- Accept user input (1–4), re-prompt on invalid choice
- Loop until user selects Exit

### FR-2: Add Expense
- Prompt for amount, category, date, note (in that order)
- Validate each field before moving to the next
- On valid input: append expense dict to list, save to JSON immediately
- Print confirmation message after save

### FR-3: List Expenses
- Display all expenses with index number (1, 2, 3…)
- Format: `1. 250.0 | food | 2026-08-24 | lunch`
- If no expenses: print "No expenses recorded."

### FR-4: Monthly Summary
- Prompt for month in `YYYY-MM` format
- Validate format (must be exactly 7 characters, match `YYYY-MM`)
- Filter expenses by matching date prefix
- Print total per category (sorted by category name)
- Print grand total
- If no expenses for that month: print "No expenses for [month]."

### FR-5: Exit
- Print "Goodbye." and break the loop

### FR-6: JSON Persistence
- File path: `expenses.json` in the same directory as `main.py`
- Load on program start
- Save after every add operation
- If file doesn't exist (first run): start with empty list `[]`
- If file exists but is empty: treat as `[]`

---

## Validation Rules

| Input | Rule | Error message | Retry |
|-------|------|---------------|-------|
| Amount | Must be a valid float | "Invalid amount. Enter a number." | Yes |
| Amount | Must be > 0 | "Amount must be greater than 0." | Yes |
| Category | Must be one of the fixed set | "Invalid category. Choose: food, transport, rent, utilities, other" | Yes |
| Date | Must match `YYYY-MM-DD` format | "Invalid date format. Use YYYY-MM-DD." | Yes |
| Date | Must be a real date (not 2026-02-30) | "Invalid date." | Yes |
| Menu choice | Must be 1–4 | "Invalid choice. Enter 1–4." | Yes |
| Month (summary) | Must match `YYYY-MM` format | "Invalid format. Use YYYY-MM." | Yes |

---

## File Structure

```
projects/project_01_expense_tracker/
├── expense_tracker/
│   └── main.py          # All v0.1 code lives here (single file)
├── .gitignore           # Ignore __pycache__/, .env, expenses.json
└── README.md            # Project documentation (created after v0.1 verified)
```

`expenses.json` is created at runtime in `expense_tracker/` (gitignored — it's user data, not source code).

---

## Edge Cases to Test

| # | Case | Expected behavior |
|---|------|-------------------|
| 1 | First run (no `expenses.json`) | Program starts without crash, empty list |
| 2 | Add expense with valid input | Saved to file, confirmation printed |
| 3 | Add expense, close, reopen, list | Expense persists and appears |
| 4 | Enter string for amount ("abc") | Re-prompt with error message |
| 5 | Enter negative amount (-50) | Re-prompt with error message |
| 6 | Enter zero amount (0) | Re-prompt with error message |
| 7 | Enter invalid category ("movies") | Re-prompt with error message |
| 8 | Enter invalid date format ("24-08-2026") | Re-prompt with error message |
| 9 | Enter invalid date ("2026-02-30") | Re-prompt with error message |
| 10 | List when no expenses | "No expenses recorded." |
| 11 | Monthly summary with matching expenses | Correct totals per category + grand total |
| 12 | Monthly summary with no matching expenses | "No expenses for [month]." |
| 13 | Monthly summary with invalid format | Re-prompt with error message |
| 14 | Menu: enter "5" | "Invalid choice. Enter 1–4." |
| 15 | Menu: enter "abc" | "Invalid choice. Enter 1–4." |

---

## Acceptance Criteria

All of these must be true before v0.1 is considered complete:

- [ ] Program runs without crash on first run (missing JSON file)
- [ ] Menu displays correctly, loops until Exit
- [ ] Add expense validates all fields (amount > 0, valid category, valid date)
- [ ] Add expense saves to `expenses.json` immediately
- [ ] List expenses shows all records with index numbers
- [ ] Monthly summary filters correctly and calculates totals
- [ ] Invalid input re-prompts with error message (no crash)
- [ ] Data persists between sessions (close and reopen)
- [ ] All 15 edge cases pass
- [ ] Clean commit with descriptive message

---

## Tech Stack

| Component | Choice | Why |
|-----------|--------|-----|
| Language | Python 3.10+ | Language learned in Stage 0 |
| Standard library | `json`, `datetime` | No external dependencies |
| Persistence | JSON file | Simple, human-readable, Day 8 skill |
| Testing | Manual | v0.1 (automated tests in v0.2+) |

No `pip install` required. No third-party packages. Pure standard library.

---

## How to Run

```bash
cd projects/project_01_expense_tracker/expense_tracker
python3 main.py
```

---

*Specification version: 0.1 | Created: 2026-08-29 | Project: Expense Tracker*
