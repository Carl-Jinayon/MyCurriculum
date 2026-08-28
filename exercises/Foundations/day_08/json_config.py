import json

content = {
    "theme": "dark",
    "volume": 5,
    "language": "en",
    "autosave": True,
    "window_size": [800, 600]
}

DEFAULT_CONFIG = {
    "value": "default"
}


dir_path = "data/config.json"

def dump_config(path, data):
    # This creates data inside the json file.
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except PermissionError:
        print("You do not have permission to write in this file.")

# Reads the json file.
def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("No config found - using defaults.")
        return DEFAULT_CONFIG
    except json.JSONDecodeError  as e:
        print(f"Corrupt config: {e} - using defaults.")
        return DEFAULT_CONFIG
    except PermissionError:
        print(f"Permission denied: {path}")
        raise
    else:
        return data

def corrupt_config(path, data):
    try:
        with open(path, "a", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except PermissionError:
        print("You do not have permission to write in this file.")

# Dumps the data into the file.
dump_config(dir_path, content)
# Reads the proper json.
json_content = load_config(dir_path)

for j, k in json_content.items():
    print(f"{j}: {k}")
# This corrupts the json file.
corrupt_config(dir_path, "fdsfasfd")
# Reads the corrupted json
print("\fAfter JSON corruption: ")
corrupt_json_content = load_config(dir_path)

for j, k in corrupt_json_content.items():
    print(f"{j}: {k}")

# Cleans back the json again
dump_config(dir_path, content)

