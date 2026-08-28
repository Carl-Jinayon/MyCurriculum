import csv

data = [
    {"name": "Carl", "score": 96},
    {"name": "Mark", "score": 95},
    {"name": "Charles", "score": 94},
    {"name": "Charlene", "score": 93},
    {"name": "Cristhian", "score": 92}
]

fieldnames = ["name", "score"]

try:
    with open("data/scores.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
except PermissionError:
    print("You do not have permission to write in this file.")
else:

    try:
        with open("data/scores.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            reader = list(reader)  
    except PermissionError:
        print("You do not have permission to write in this file.")
    else:
        total = 0
        for r in reader:
            total += int(r["score"])

        print(f"{total/len(reader):.2f}")