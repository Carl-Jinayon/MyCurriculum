# counting_02.py — Password rules: 8 chars, uppercase + lowercase + digits (62 chars). 
# (a) Total possible? 
# (b) Must contain at least one digit? (use complement: total − no digits). 
# (c) Must contain at least one of each type? (inclusion-exclusion over 3 types).

# a - total possible I assume that there is a repetition
total_possible = 62 ** 8

# b - must contain at least one digit
contain_digit = (62 ** 8) - (52 ** 8)

# c - must contain at least one digit, one uppercase, one lowercase
# exclude following:
# no digit
no_digit = 52 ** 8
# no lowercase
no_loweracase = 36 ** 8
# no uppercase
no_uppercase = 36 ** 8
# no digit and lowercase
no_digit_lowercase = 26 ** 8
# no digit and uppercase
no_digit_uppercase = 26 ** 8
# no lowercase and uppercase
no_lowercase_uppercase = 10 ** 8

# For real I am having a tough time to answer this part. This is just a lucky guess haha.
valid = total_possible - (no_digit + no_loweracase + no_uppercase) + (no_digit_lowercase + no_digit_uppercase + no_lowercase_uppercase)

print("Total possible:", total_possible)
print(f"Total permutation with digit: {contain_digit}")
print(f"Number of permutation when contains at least each type: {valid}")


