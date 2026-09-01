import json

DEFAULT_PATH = "expenses.json"

def create_path(path=DEFAULT_PATH):
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)
    except FileNotFoundError:
        print(f"'{path}' does not exists. Creating one now.")
    except PermissionError:
        print(f"You do not have permission to write in '{path}'")
    else:
        print(f"'{path}' created successfully.")

def load_expenses(path=DEFAULT_PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = json.load(f)
    except FileNotFoundError:
        create_path(path)
        return []
    except PermissionError:
        print(f"You do not have permission to read '{path}'")
        return []
    except json.JSONDecodeError:
        print(f"'{path}' is corrupted. Creating one now.")
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
    except PermissionError:
        print(f"You do not have permission to write in '{path}'")
    except json.JSONDecodeError:
        print(f"'{path}' is corrupted. Creating one now.")
        create_path(path)
    else:
        print("File saved without errors.")

