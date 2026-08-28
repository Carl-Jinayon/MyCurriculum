try:
    with open("data/sample.txt", "r", encoding="utf-8") as f:
        content = f.readlines()
except FileNotFoundError:
    print("File does not exists.")
except PermissionError:
    print("You do not have permission to open this file.")
else:
    for i, line in enumerate(content, start=1):
        print(f"{i} - {line}", end="")
