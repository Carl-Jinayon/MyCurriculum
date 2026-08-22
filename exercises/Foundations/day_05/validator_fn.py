def get_int(prompt, min, max):
    while True:
        number = input(prompt)

        if number.isdigit():
            number = int(number)
            if min < number <= max:
                return number

valid_number = get_int("Enter number: ", 0, 100)
print(f"Valid number: {valid_number}")