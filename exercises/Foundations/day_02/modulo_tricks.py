number = float(input("Enter number: "))

if number % 2 == 1:
    print("The number is odd.")
else:
    print("The number is even.")

last_digit = number % 10

print("Last digit:", int(last_digit))