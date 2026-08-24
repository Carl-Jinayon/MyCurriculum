#counting_01.py — 
# (a) How many ways to arrange 5 books on a shelf? 
# (b) How many ways to choose 3 books from 8 for a trip? 
# (c) A 4-digit PIN: digits 0-9, no repetition. 
# How many? (d) Same, with repetition allowed.

import math

# a - permutation
books_arrangement = math.factorial(5)

# b - combination
books_trip = math.factorial(8) / (math.factorial(3) * math.factorial(8 - 3))

# c - permutation
pin_no_repeat = math.factorial(10) / math.factorial(10 - 4)

# d - permutation
pin_with_repeat = 10 ** 4

print(f"Ways to arrange books: {books_arrangement}")
print(f"Ways to choose books for a trip: {books_trip}")
print(f"Four(4) digit pin no repetition: {pin_no_repeat}")
print(f"Four(4) digit pin with repetition: {pin_with_repeat}")
