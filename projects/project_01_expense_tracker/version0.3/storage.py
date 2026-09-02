import json
import os

DEFAULT_PATH = "expenses.json"

def create_path(path=DEFAULT_PATH):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)
    except PermissionError:
        print(f"You do not have permission to write in '{path}'")
    else:
        print(f"'{path}' created successfully.")

def load_expenses(path=DEFAULT_PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = json.load(f)
    except FileNotFoundError:
        print("No data file found. Starting fresh.")
        create_path(path)
        return []
    except PermissionError:
        print("Permission denied: cannot access expenses.json. Returning empty list.")
        return []
    except json.JSONDecodeError:
        print("WARNING: expenses.json is corrupted. Starting with empty list. Your old file was renamed to expenses.json.bak")
        os.rename(DEFAULT_PATH, f"{DEFAULT_PATH}.bak")
        create_path(path)
        return []
    else:
        return content

def save_expenses(data, path=DEFAULT_PATH):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except FileNotFoundError:
        create_path(path)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except PermissionError:
        print("Permission denied: cannot write to expenses.json")
