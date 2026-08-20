number = input("Enter number: ").lstrip("-")

if number.isdigit():
    number = int(number)

    print(f"Square: {number * number}")
else:
    print("Warning: input is not a number.")