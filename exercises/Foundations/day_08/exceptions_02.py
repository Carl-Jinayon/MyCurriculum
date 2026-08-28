class PositiveIntegerError(ValueError):
    def __init__(self):
        super().__init__("Integer must be positive. Not negative neither zero.")

def get_positive_int(prompt="Enter a positive integer: "):
    while True:
        try:
            number = int(input(prompt))

            if number == 0 or number < 0:
                raise PositiveIntegerError
        except PositiveIntegerError as e:
            print(e)
        except ValueError:
            print("Please enter a valid integer.")
        else:
            return number

print(get_positive_int())