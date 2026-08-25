# validator_oop.py — rewrite your Day 8 get_positive_int() using your 
# PositiveIntegerError(ValueError) properly, 
# with a docstring explaining the contract.

class PositiveIntegerError(ValueError):
    def __init__(self, number):
       self.number = number

def get_positive_int():
    