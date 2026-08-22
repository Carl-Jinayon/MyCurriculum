def factorial(n):
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total

print("Factorial:", factorial(5))

def is_even(n):
    return n % 2 == 0

def main():
    number = input("Enter positive integer: ")

    if number.isdigit():
        number = int(number)
        if number > 0:
            if is_even(factorial(number)):
                print("Factorial is even.")
            else:
                print("Factorial is odd.")
        else:
            print("Number is not positive.")
    else:
        print("Invalid input.")

if __name__ == "__main__":
    main()