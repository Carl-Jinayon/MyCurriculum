import exceptions
import models

from datetime import datetime

def get_amount(prompt="Enter amount: ") -> float:
    """Asks the user for an amount. Returns amount with float value."""
    while True:
        try:
            amount = float(input(prompt))
            if amount <= 0:
                raise exceptions.InvalidAmountError
        except exceptions.InvalidAmountError as e:
            print(e)
        except ValueError:
            print("Amount must be a positive number.")
        else:
            return amount

def get_category(prompt="Enter category (food, transport, rent, utilities, other): ") -> str:
    """Asks the user for category (food, transport, rent, utilities, other). Returns a string with valid category."""
    while True:
        category = input(prompt)
        try:
            if category not in models.CATEGORY_LIST:
                raise exceptions.InvalidCategoryError
        except exceptions.InvalidCategoryError as e:
            print(e)
        else:
            return category

def get_date(prompt="Enter date (YYYY-MM-DD): ") -> str:
    while True:
        date = input(prompt)
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
        else:
            return date

def get_month(prompt="Enter month (YYYY-MM): "):
    while True:
        month = input(prompt)
        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            print("Invalid month. Use YYYY-MM.")
        else:
            return month

def get_note(prompt="Enter note (optional): "):
    note = input(prompt)
    return note

def get_menu_choice(options) -> int:
    while True:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        try:
            choice = int(input("Enter choice: "))

            if not (0 < choice <= len(options)):
                raise ValueError
        except ValueError:
            print("Invalid choice.")
        else:
            return choice