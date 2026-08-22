while True:
    number = input("Enter number 1-100 (inclusive): ")

    if number.isdigit():
        number = int(number)

        if 0 < number <= 100:
            if number % 3 == 0 and number % 5 == 0:
                print("FizzBuzz")
            elif number % 3 == 0:
                print("Fizz")
            elif number % 5 == 0:
                print("Buzz")
            else:
                print(f"Number: {number}") 
            break
        else:
            print("Number is not in range.")
    else:
        print("Please enter valid input.")
    