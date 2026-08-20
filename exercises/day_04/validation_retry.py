number = int(input("Enter integer (1-100): "))

while not 0 < number <= 100:
    number = int(input("Invalid. Enter integer: "))
print("Valid number:", number)
