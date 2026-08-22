user_input = input("Enter a number: ")

check = user_input

# Allow exactly one + or - at the beginning
if check.startswith(("+", "-")):
    check = check[1:]

if check.replace(".", "", 1).isdigit() and check.count(".") <= 1:
    number = float(user_input)

    if number == 0:
        print("The number is zero.")
    elif number > 0:
        print("The number is positive.")
    else:
        print("The number is negative.")
else:
    print("That is not a valid number.")