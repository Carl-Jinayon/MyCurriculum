number = input("Enter positive integer: ")
total = 0

if number.isdigit():
    number = int(number)
    for i in range(1, number + 1):
        total += i
    print("Total:", total)
else:
    print("Invalid input.")

# it prints numbers every two steps from 1 - 10 (10 is not included)
# this prints numbers from 10 to 2 in reverse because of -1.
# this prints (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)
# it only runs when the loop is not interrupted or ran properly.

# Reflection
# 1. The condition first, before the body. 
# because sometimes the body is dependent to the condition from the loop.
# 2. Nothing, I haven't encountered yet. But I have tried it (testing).
# 3. I used continue incase that the user input is invalid.