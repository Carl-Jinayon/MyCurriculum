number = input("Enter positve number: ")
total = 0

if number.isdigit():
    number = int(number)

    if number > 0:
        for i in range(1, number + 1):
            total += i
        print(f"Sum from the loop: {total}")

        total = number * (number + 1) // 2

        print(f"Sum from the formula: {total}")
    else:
        print("Number is not positive.")
else:
    print("Input is not valid.")

        