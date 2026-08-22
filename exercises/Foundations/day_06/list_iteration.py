temps = [32,34,43,23,55]

# Print each with enumerate
for i, temp in enumerate(temps, start=1):
    print(f"Temp {i}: {temp}")

# Print max
maximum = temps[0]
minimum = temps[0]
total = 0
for temp in temps:
    total += temp

    if temp > maximum:
        maximum = temp

    if temp < minimum:
        minimum = temp

average = total / len(temps)
print("\nMax:", maximum)
print("Min:", minimum)
print("Average:", average)

    