user_input = input("Enter number: ").lstrip("-")

if user_input.isdigit():
    user_input = int(user_input)

    if user_input % 5 == 0 and user_input % 3 == 0:
        print("FizzBuzz")
    elif user_input % 3 == 0:
        print("Fizz")
    elif user_input % 5 == 0:
        print("Buzz")
    else:
        print(f"Number: {user_input}")
else:
    print("Error: Not a valid input.")

# The difference between '=' and '==' 
# = is used when we assign value to something
# == we use this when we compare values. And it returns true or false.

# Which one is legal Python? Why?
# The first one is legal because it compares two values that has the same data type
# The second one it tries to create a variable name 5 which is not valid and assigns it to value 5 which will return an error.

# What does not (age >= 18) mean in plain words?
# it means that the boolean that the 'age >= 18' will return will be negated.
# for example, if the value of age is 17 inside the parenthesis, it will return false.
# but outside it, it is reversed. So the whole statement will return True.
