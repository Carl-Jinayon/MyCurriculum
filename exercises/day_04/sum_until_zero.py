total = 0

# ask for user input
number = int(input("Enter number (zero to exit): "))

while number != 0:
    total += number

    number = int(input("Enter number (zero to exit): "))
else:
    print(f"Total: {total}")
