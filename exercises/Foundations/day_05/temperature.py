def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temp_fahren = celsius_to_fahrenheit(43)
temp_cel = fahrenheit_to_celsius(87)

print(f"Fahrenheit: {temp_fahren:.2f}")
print(f"Celsius: {temp_cel:.2f}")