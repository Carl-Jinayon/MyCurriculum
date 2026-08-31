phone_book = {
    "Carl":  "0917-111-2222",
    "Ana":   "0917-333-4444",
    "Bo":    "0917-111-2222",   # duplicate of Carl
    "Maria": "0917-555-6666",
    "Bong":  "0917-333-4444"    # duplicate of Ana
}

inverted = {}

for name, number in phone_book.items():
    if number not in inverted.keys():
        inverted[number] = [name]
    else:
        inverted[number].append(name)

for number, name in inverted.items():
    print(f"{number}: ", end="")
    for n in name:
        print(f"{n}", end=" ")
    print()