itm = {
    "apples": 1,
    "mango": 5,
    "orange": 3,
    "cherry": 7, 
    "watermelon": 2
}

print("\nApples quantity before:", itm["apples"])
itm["apples"] = max(itm.get("apples") - 2, 0)
print("Apples quantity after:", itm["apples"])

print("\nWatermelon quantity before:", itm["watermelon"])
itm["watermelon"] += 5
print("Watermelon quantity after:", itm["watermelon"])

total = 0

for value in itm.values():
    print(f"total = {total} + {value}")
    total += value
print("\nTotal quantity of items =", total)

most_stacked_item = None
most_stacked_quantity = 0

for key, value in itm.items():
    if value > most_stacked_quantity:
        most_stacked_quantity = value
        most_stacked_item = key

print("\nMost stacked item:", most_stacked_item)
