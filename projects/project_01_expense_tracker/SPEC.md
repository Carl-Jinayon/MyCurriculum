# Project 1 — Expense Tracker (CLI)

> Stage 0 capstone project. First portfolio piece. Demonstrates integration of EVERYTHING in Stage 0.

## Why this project
Widest skill surface of the candidates: dict-based records (Day 7), JSON persistence (Day 8), exceptions + custom validation (Days 3+8+9), function decomposition (Day 5), aggregation loops (Day 4), CLI menus, Git discipline. Real domain ambiguity (categories, months, budgets) = real engineering judgment.

## Rules of engagement
- AI: hints only for debugging; NO generated features. This goes on your portfolio with an AI-usage disclosure.
- Git: one commit per working feature. Commit messages describe what + why.
- Verification: run after every feature; test edge cases manually; record them.

## Functional Requirements

### v0.1 — Core loop
- Menu: 1) Add expense  2) List expenses  3) Monthly summary  4) Exit
- Add: amount (validated float > 0), category (from fixed set), date (YYYY-MM-DD, validated), note (optional)
- Persistence: JSON file `expenses.json` — load on start, save after every change

### v0.2 — Analysis
- Monthly summary: total per category for a chosen month + grand total
- List supports filter by category and/or month

### v0.3 — Robustness
- Custom exceptions: `InvalidAmountError`, `InvalidDateError` (inherit ValueError)
- Corrupt/missing data file handled gracefully (start fresh + warn)
- All user input validated via a reusable `get_*` family of functions

### Data model (each expense = one record)
```json
{"amount": 250.0, "category": "food", "date": "2026-08-24", "note": "lunch"}
```

## Suggested structure
```
expense_tracker/
├── main.py            # menu loop only
├── models.py          # record helpers / validation functions
├── storage.py         # load/save JSON (all file I/O here)
├── reports.py         # summaries and filters
└── expenses.json      # data (gitignore this? decide + justify)
```

## Stretch goals (after v0.3 verified)
- Budget per category with warnings when exceeded
- Export monthly report to CSV
- Edit/delete existing records by index

## Definition of done
- [ ] All v0.1–v0.3 features work end-to-end
- [ ] README.md: problem statement, usage, structure, design decisions, limitations, AI-usage disclosure
- [ ] Clean commit history (feature-sized commits)
- [ ] Domain journal entry #1 completed
- [ ] Demoed end-to-end to yourself with edge cases (empty file, corrupt file, zero records month)
