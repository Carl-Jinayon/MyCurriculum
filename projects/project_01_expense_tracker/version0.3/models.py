import storage

CATEGORY_LIST = ["food", "transport", "rent", "utilities", "other"]

def create_expense(expenses: list, amount: float, category: str, date: str, note: str) -> dict:
    data = {
        "amount": amount,
        "category": category, 
        "date": date,
        "note": note
    }

    expenses.append(data)

    storage.save_expenses(expenses)