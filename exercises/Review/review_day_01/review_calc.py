def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    """This function returns None if the divisor is Zero(0)."""
    if b == 0:
        return None
    else:
        return a / b

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter valid inputs.")
        else:
            return number

def main():
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")

    operation = input("Enter operation (+-*/): ")

    if operation in "+-*/":
        if operation == "+":
            print(f"Sum: {add(first_number, second_number)}")
        elif operation == "-":
            print(f"Difference: {sub(first_number, second_number)}")
        elif operation == "*":
            print(f"Product: {mul(first_number, second_number)}")
        elif operation == "/":
            print(f"Quotient: {div(first_number, second_number)}")
    else:
        print("Invalid operation.")

if __name__ == "__main__":
    main()