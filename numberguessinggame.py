import random

secret_number = random.randint(1, 100)

print("I am thinking of a number between 1 and 100.")
guess = int(input("Enter your guess: "))

if guess < secret_number:
    print(f"Too low! The secret number was {secret_number}.")
elif guess > secret_number:
    print(f"Too high! The secret number was {secret_number}.")
else:
    print("Congratulations! You guessed it right!")
