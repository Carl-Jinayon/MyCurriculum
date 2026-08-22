number = input("Enter a whole number: ").lstrip("-")

if number.isdigit():
    number = int(number)
    is_divisible = number % 5 == 0
    if number % 2 == 0:
        if is_divisible:
            print("Number is even and is divisible by 5.")
        else:
            print("Number is even.")
    else:
        if is_divisible:
            print("Number is odd and divisible by5.")
        else:
            print("Number is odd.")
else:
    print("Please enter a valid input.")