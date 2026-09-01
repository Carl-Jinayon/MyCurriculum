# Expense Tracker v0.2 — Project Specification

> Version 0.2 adds filtering and refactors the single-file v0.1 into a modular structure. This is the engineering lesson — taking working code and organizing it properly.

---

## What's New in v0.2

| Feature | v0.1 | v0.2 |
|---------|------|------|
| Add expense | ✅ | ✅ |
| List all expenses | ✅ | ✅ |
| Monthly summary | ✅ | ✅ |
| **Filter list by category** | ❌ | ✅ NEW |
| **Filter list by month** | ❌ | ✅ NEW |
| **Filter list by category + month** | ❌ | ✅ NEW |
| **Modular file structure** | ❌ (single file) | ✅ REFACTOR |

---

## Feature: Filtered List

### FR-1: List with Filter Options
- After selecting "List expenses", ask user how they want to view:
  ```
  1. List all
  2. Filter by category
  3. Filter by month
  4. Filter by category and month
  ```
- If no filter: show all expenses (same as v0.1)
- If filter by category: show only expenses matching that category
- If filter by month: show only expenses matching `YYYY-MM` prefix
- If both: show only expenses matching BOTH criteria
- If no expenses match filter: print "No expenses match that filter."

### FR-2: Filter by Category
- Prompt: "Enter category: "
- Validate against fixed category list
- Filter: `e["category"] == chosen_category`

### FR-3: Filter by Month
- Prompt: "Enter month (YYYY-MM): "
- Validate format with `datetime.strptime(month, "%Y-%m")`
- Filter: `e["date"].startswith(month)`

### FR-4: Filter by Both
- Ask for category first, then month
- Apply both filters: `category_match AND month_match`
- Order: category first, then month (doesn't matter, both are AND conditions)

---

## Refactor: Modular Structure

### Before (v0.1):
```
version0.1/
├── main.py          # Everything in one file (153 lines)
└── expenses.json    # Data
```

### After (v0.2):
```
version0.2/
├── main.py          # Menu loop + user interaction only
├── models.py        # Data structures and validation
├── storage.py       # JSON load/save (file I/O)
├── reports.py       # List filtering and monthly summary
├── expenses.json    # Data
└── __init__.py      # Empty (makes it a package)
```

### Module Responsibilities:

**`main.py`** — entry point and menu loop
- `main()` function: menu loop, user input, calls other modules
- No file I/O, no data logic — just orchestration

**`models.py`** — data structures and validation
- `CATEGORY_LIST` — constant for valid categories
- `create_expense(amount, category, date, note)` — builds and returns an expense dict
- `validate_amount(value)` — returns float if valid, raises ValueError
- `validate_category(value)` — returns str if valid, raises ValueError
- `validate_date(value)` — returns str if valid, raises ValueError
- `validate_month(value)` — returns str if valid, raises ValueError

**`storage.py`** — file I/O (JSON persistence)
- `load_expenses(path)` — load from JSON, handle missing/corrupt file
- `save_expenses(path, data)` — save to JSON
- `DEFAULT_PATH` constant — `"expenses.json"`

**`reports.py`** — filtering and summaries
- `list_expenses(data)` — print all expenses with index
- `filter_by_category(data, category)` — return filtered list
- `filter_by_month(data, month)` — return filtered list
- `monthly_summary(data, month)` — print summary with totals
- `get_filtered_list(data, category=None, month=None)` — apply filters and return

### Import Rules:
```
main.py imports: storage, reports, models
reports.py imports: models (for constants)
storage.py imports: json (stdlib only)
models.py imports: datetime (stdlib only)
```

No circular imports. Each module has a single responsibility.

---

## Validation Rules (unchanged from v0.1)

| Input | Rule | Error message | Retry |
|-------|------|---------------|-------|
| Amount | Must be a valid float | "Invalid amount. Enter a number." | Yes |
| Amount | Must be > 0 | "Amount must be greater than 0." | Yes |
| Category | Must be one of the fixed set | "Invalid category. Choose: food, transport, rent, utilities, other" | Yes |
| Date | Must match `YYYY-MM-DD` format | "Invalid date format. Use YYYY-MM-DD." | Yes |
| Date | Must be a real date | "Invalid date." | Yes |
| Menu choice | Must be valid option | "Invalid choice." | Yes |
| Month | Must match `YYYY-MM` format | "Invalid format. Use YYYY-MM." | Yes |

---

## Edge Cases to Test

| # | Case | Expected behavior |
|---|------|-------------------|
| 1 | All v0.1 edge cases still pass | No regression |
| 2 | Filter by category with matching expenses | Shows only those expenses |
| 3 | Filter by category with no matches | "No expenses match that filter." |
| 4 | Filter by month with matching expenses | Shows only those expenses |
| 5 | Filter by month with no matches | "No expenses match that filter." |
| 6 | Filter by both (category + month) | Shows only expenses matching both |
| 7 | Filter by both with no matches | "No expenses match that filter." |
| 8 | Filter with invalid category | Re-prompt |
| 9 | Filter with invalid month format | Re-prompt |
| 10 | Empty list + filter | "No expenses recorded." (not filter message) |
| 11 | All modules import correctly | No ImportError |
| 12 | Run from `main.py` entry point | Works end-to-end |

---

## Acceptance Criteria

All of these must be true before v0.2 is considered complete:

- [ ] All v0.1 functionality still works (no regression)
- [ ] List filter menu: all / category / month / both
- [ ] Filter by category works correctly
- [ ] Filter by month works correctly
- [ ] Filter by both works correctly
- [ ] Invalid filter input re-prompts
- [ ] Empty list handled before filter check
- [ ] Code split into 4 modules: main, models, storage, reports
- [ ] Each module has clear single responsibility
- [ ] No circular imports
- [ ] All 12 edge cases pass
- [ ] Clean commit with descriptive message

---

## How to Run

```bash
cd projects/project_01_expense_tracker/version0.2
python3 main.py
```

---

## Commit Strategy

After v0.2 is verified:
```bash
git add version0.2/
git commit -m "feat: v0.2 — list filters + modular refactor"
```

---

*Specification version: 0.2 | Created: 2026-08-30 | Project: Expense Tracker*
