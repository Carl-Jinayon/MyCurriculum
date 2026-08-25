# validator_oop.py — rewrite your Day 8 get_positive_int() using your 
# PositiveIntegerError(ValueError) properly, 
# with a docstring explaining the contract.

class PositiveIntegerError(ValueError):
    def __init__(self, number):
       self.number = number

def get_positive_int(prompt):
    """Returns number n if positive. Raises PositiveIntegerError otherwise."""
    while True:
        try: 
            number = int(input(prompt))
        except ValueError:
            print("Please enter a valid input.")
        else:
            try:
                if number <= 0:
                    raise PositiveIntegerError("Number must be greater than zero.")
            except PositiveIntegerError as e:
                print(e)
            else:
                return number

number = get_positive_int("Enter a positive integer: ")
print("Positive integer:", number)