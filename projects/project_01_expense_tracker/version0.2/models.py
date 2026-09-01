import storage
from datetime import datetime

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

def validate_amount(value) -> float:
    if value <= 0:
        raise ValueError("Amount must be greater than 0.")
    else:
        return value


def validate_category(value):
    if value not in CATEGORY_LIST:
        raise ValueError("Invalid category. Choose: food, transport, rent, utilities, other")
    else:
        return value

def validate_date(value):
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise ValueError
    else:
        return value

def validate_month(value):
    try:
        datetime.strptime(value, "%Y-%m")
    except ValueError:
        raise ValueError("Invalid format. Use YYYY-MM.")
    else:
        return value
