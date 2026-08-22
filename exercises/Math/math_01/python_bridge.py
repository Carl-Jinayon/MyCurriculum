# python_bridge.py — write Python that evaluates 2x + 3 for x = 4, 10, -2 and prints results. Verify they match your hand answers.

values = [4, 10, -2]

for value in values:
    print(f"\nx = {value}")
    print(f"2({value}) + 3")
    print(f"Result: {2 * value + 3}")