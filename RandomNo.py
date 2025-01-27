print("Hello, Welcome to the Lucky Number Guessing Game!")
import random

while True:
    n = int(input("Select a number between 1 and 10:\n"))
    r = random.randint(1, 10)

    if n == r:
        print(f"Congratulations! You guessed it right. The lucky number is {r}.")
        break  # Exit the loop if the guess is correct
    else:
        print(f"Oops! The lucky number is {r}, but you selected {n}.")
        print("Try again! Select a number between 1 and 10.")
