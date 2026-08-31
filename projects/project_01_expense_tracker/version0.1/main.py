import json

from datetime import datetime

DEFAULT_VALUE = []

def default_file(file: str="expenses.json"):
    """Creates a file with default value."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(DEFAULT_VALUE, f, indent=2)


def load_file(file: str="expenses.json") -> list:
    """Returns the list of dicts from the file. If it fails it tries to create one if there is permission. """
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"File '{file}' does not exist. Creating one now.")
        default_file(file)
        return DEFAULT_VALUE
    except PermissionError:
        print("Reading failed. Permission denied.")
    except json.JSONDecodeError:
        print("Reading failed. File is corrupted. Creating one now.")
        default_file(file)
        return DEFAULT_VALUE
    else:
        return data

def save_file(data: list, file: str="expenses.json"):
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except FileNotFoundError:
        print(f"File '{file}' does not exist. Creating one now.")
    except PermissionError:
        print("Writing failed, permission error.")
    else:
        print("Data saved successfully without errors.")
    
def add_expense(data: list, amount: float, category: str, _date: str, note: str="", file: str="expenses.json"):
    expense = {
        "amount": amount,
        "category": category,
        "date": _date,
        "note": note
    }

    data.append(expense)

    save_file(data)

def list_expense(data: list, file: str="expenses.json"):
    if not data:
        print("No expenses recorded.")
        return
    for i, d in enumerate(data, 1):
        print(f"{i}. {d['amount']:.2f} | {d['category']} | {d['date']} | {d['note']}")

def monthly_summary(data: list, month: str):
    month_expense = [e for e in data if e['date'].startswith(month)]

    summary = {}
    for m in month_expense:
        summary[m['category']] = summary.get(m['category'], 0) + m['amount']

    if not summary:
        print(f"No expenses for '{month}'")
        return

    total = 0
    for s in summary.values():
        total += s

    print(f"\nSummary for {month}:")
    for k, v in summary.items():
        print(f"{k}: {v:<8.2f}")
    print("-"* 15)
    print(f"Total: {total:<8.2f}\n")

def main():
    data = load_file()

    print("Welcome to expense tracker!")

    while True:
        print("\nMENU:"
            "\n1. Add expense"
            "\n2. List expenses"
            "\n3. Monthly summary"
            "\n4. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                try:
                    while True:
                        try:
                            amount = float(input("Enter amount: "))

                            if amount <= 0:
                                print("Amount must be greater than 0.")
                                continue
                        except ValueError:
                            print("Invalid amount. Enter a number.")
                        else:
                            break
                    while True:
                        category = input("Enter category (food, transport, rent, utilities, other): ")

                        if category not in ["food", "transport", "rent", "utilities", "other"]:
                            print("Invalid category. Choose: food, transport, rent, utilities, other")
                            continue
                        else:
                            break
                    while True:
                        _date = input("Enter date (YYYY-MM-DD): ")
                        try:
                            datetime.strptime(_date, "%Y-%m-%d")
                        except ValueError:
                            print("Invalid date format. Use YYYY-MM-DD.")
                        else:
                            break
                    note = input("Enter note: ")
                except Exception as e:
                    print(f"Error: {e}")
                else:
                    add_expense(data, amount, category, _date, note)
            elif choice == 2:
                list_expense(data)
            elif choice == 3:
                while True:
                    month = input("Enter month (YYYY-MM): ")
                    try:
                        datetime.strptime(month, "%Y-%m")
                    except ValueError:
                        print("Invalid format. Use YYYY-MM.")
                    else:
                        monthly_summary(data, month)
                        break
            elif choice == 4:
                print("Expense tracker exited. Thank you for using!")
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Enter 1-4.")

if __name__ == "__main__":
    main()

