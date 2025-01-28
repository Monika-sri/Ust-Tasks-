'''
1.use the os and os.path modules to list the contents of your
downloads folder and indicate for each item whether it's a file or a folder
(hint : use os.path.join)'''

import os
downloads_folder = os.path.expanduser("~/Downloads")
contents = os.listdir(downloads_folder)
for item in contents:
    item_path = os.path.join(downloads_folder, item)
    if os.path.isfile(item_path):
        print(f"{item} - File")
    elif os.path.isdir(item_path):
        print(f"{item} - Folder")
    else:
        print(f"{item} - Unknown")



#2.import  string module and print out all  ASCII letters defined in this module

import string
print(string.ascii_letters)



'''
3.Import the sample() function from the random module and the ascii_letters
attribute of the string module. use these to randomly sample five letters and
assign these to a variable called five_letters'''

from random import sample
from string import ascii_letters
five_letters = ''.join(sample(ascii_letters, 5))
print(five_letters)



'''
4. Take a input from the user a date for eg: 25/02/2020
a.print output Date in format  Tuesday 25 February 2020
b.print the day of the week of a given input  date
c. Add 15 days and 23 hours to a given input date
d. calculate the date 6 months from the current date
'''
from datetime import datetime
from datetime import date, timedelta

date_input = input("Enter a date (DD/MM/YYYY): ")
date_obj = datetime.strptime(date_input, "%d/%m/%Y")

formatted_date = date_obj.strftime("%A %d %B %Y")
print("Formatted Date:", formatted_date)
day_of_week = date_obj.strftime("%A")
print("Day of the Week:", day_of_week)

new_date = date_obj + timedelta(days=15, hours=23)
print("New Date after adding 15 days and 23 hours:", new_date.strftime("%A %d %B %Y, %H:%M:%S"))

current_date = date.today()

def add_months(current_date, months):
    new_month = current_date.month + months
    new_year = current_date.year + (new_month - 1) // 12
    new_month = (new_month - 1) % 12 + 1

    day = min(current_date.day, [31, 29 if new_year % 4 == 0 and (new_year % 100 != 0 or new_year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][new_month - 1])
    return date(new_year, new_month, day)

current_date = date.today()

date_in_6_months = add_months(current_date, 6)
print("Date 6 months from today:", date_in_6_months.strftime("%A %d %B %Y"))




'''
5.Create a game of rock paper and scissors where user will input one option
while second option is chosen by the computer(i.e your python program).
Based on the options select declare the result
1. user wins
2. computer wins
3. draw
'''
import random
options = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

computer_choice = random.choice(options)

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
else:
    print("Computer wins!")


























