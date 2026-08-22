def max_of_three(a, b, c):
    if b <= a >= c:
        return a
    elif a <= b >= c:
        return b
    elif a <= c >= b:
        return c

print(max_of_three(4,3,4))

# Function returns None type if there is no return statement.
# value of x is 10 because the x inside a function is just a local variable and can't be accessed outside.

def is_even(n):
    return n % 2 == 0

def main():
    for i in range(1, 11):
        print(f"Number {i}: ", end="")
        if is_even(i):
            print("Even.")
        else:
            print("Odd.")

if __name__ == "__main__":
    main()