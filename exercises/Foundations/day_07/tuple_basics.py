coordinate = (4, -3)

x, y = coordinate

print(f"x: {x}, y: {y}")

# Prediction: This will raise TypeError because tuples are immutable
# coordinate[0] = 99

# Actual error: TypeError: 'tuple' object does not support item assignment
# Explanation: This error occurs because the program attemps to create a value
# inside a tuple which will cause error becaues tuples values cannot be changed or immutable

