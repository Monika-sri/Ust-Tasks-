import random

while True:
    try:
        n = int(input("Select a number between 1 to 10:\n"))
        
        # Validate the input
        if n < 1 or n > 10:
            print("Invalid input! Please enter a number between 1 and 10.")
            continue
        
        r = random.randint(1, 10)
        
        if n == r:
            print("You guessed it right! The lucky number is", r)
            break
        else:
            print(f"Sorry, the lucky number is {r}, and your selected number is {n}.")
            print("Please try again!")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
