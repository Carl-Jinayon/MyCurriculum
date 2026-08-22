def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def absolute_value(n):
    if n < 0:
        return n * -1
    return n

total = add(3, 4)
product = multiply(3, 4)
absolute = absolute_value(-4)

print(f"Total: {total}")
print(f"Product: {product}")
print(f"Absolute value: {absolute}")