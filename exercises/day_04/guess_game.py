import random

random_number = random.randint(1, 100)
attempts = 0

while True:
    attempts += 1
    user_guess = input("Enter guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Invalid input.")
        continue

    if user_guess == random_number:
        print("Correct! ", end="")
        break
    elif user_guess > random_number:
        print("Too high!")
    elif user_guess < random_number:
        print("Too low!")

print(f"Attempts: {attempts}")