def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return None

def main():
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    print("Sum:", add(first_number, second_number))
    print("Difference:", sub(first_number, second_number))
    print("Product:", multiply(first_number, second_number))
    print("Quotient:", divide(first_number, second_number))

if __name__ == "__main__":
    main()