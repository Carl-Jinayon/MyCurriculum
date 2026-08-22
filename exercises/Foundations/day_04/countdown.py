n = input("Enter positive integer: ")

if n.isdigit():
    n = int(n)

    print("Countdown: ", end="")
    for i in range(n, 0, -1):
        print(i, end=" ")
    else:
        print("\nLiftoff!")
else:
    print("Please enter a valid input.")