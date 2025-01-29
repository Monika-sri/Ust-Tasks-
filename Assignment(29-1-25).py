#Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

import random
def generate_random_numbers():
    numbers = []
    while len(numbers) < 3:
        num = random.randint(100, 999)
        if num % 5 == 0:
            numbers.append(num)
    return numbers

print("Random numbers divisible by 5:", generate_random_numbers())




#Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random
def generate_lottery_tickets():
    tickets = set()  
    while len(tickets) < 100:
        ticket = random.randint(100000, 999999) 
        tickets.add(ticket)
    return list(tickets)

def pick_winners(tickets):
    return random.sample(tickets, 2)  

lottery_tickets = generate_lottery_tickets()

winners = pick_winners(lottery_tickets)

print("Generated Lottery Tickets:", lottery_tickets)
print("Winning Tickets:", winners)




#Exercise 3: Generate 6 digit random secure OTP

import secrets
otp = secrets.randbelow(900000) + 100000  # Ensures a 6-digit OTP (100000-999999)
print("Your Secure OTP:", otp)



#Exercise 4: Pick a random character from a given String

import random
text = "Good-Evening:Sir"
random_char = random.choice(text) 
print("Random Character:", random_char)



#Exercise 5: Generate random String of length 5

import random
import string
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
print("Random String:", random_string)



'''
Exercise 6: Generate a random Password which meets the following conditions Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.'''

import random
import string
Password = random.choices(string.ascii_uppercase, k=2)  
password += random.choice(string.digits)  
password += random.choice(string.punctuation)  
password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=7)
random.shuffle(password)
password = ''.join(password)
print("Random Password:", password)



#Exercise 7: Calculate multiplication of two random float numbers

import random
num1 = random.uniform(1.0, 10.0)  
num2 = random.uniform(1.0, 10.0)  
result = num1 * num2
print(f"Random Numbers: {num1}, {num2}")
print(f"Multiplication Result: {result}")



#Exercise 8: Generate random secure token of 64 bytes and random URL

import secrets
import random
import string
token = secrets.token_bytes(64)  
print("Random Secure Token:", token)
base_url = "https://www.example.com/"
path = ''.join(random.choices(string.ascii_letters + string.digits, k=10))  
random_url = base_url + path
print("Random URL:", random_url)



#Exercise 9: Roll dice in such a way that every time you get the same number

import random
fixed_roll = 4
def roll_dice():
    return fixed_roll

print("Rolling the dice:", roll_dice())



#Exercise 10: Generate a random date between given start and end dates

import random
from datetime import datetime, timedelta
def generate_random_date(start_date, end_date):
    delta = end_date - start_date  
    random_days = random.randint(0, delta.days) 
    random_date = start_date + timedelta(days=random_days) 
    return random_date

start_date = datetime(2020, 1, 1) 
end_date = datetime(2025, 1, 1)   

random_date = generate_random_date(start_date, end_date)
print("Random Date:", random_date.strftime('%Y-%m-%d')) 













































