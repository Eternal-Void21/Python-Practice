# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
# Print out that many copies of the previous message on separate lines.

#Module to get system date and time
from datetime import date

name = input("What is your name?:\n")
age = int(input("What is your age?:\n"))
number = int(input("Enter any number from 1-100:\n")) #Simplicity purposes

#To get current year
current_date = date.today()
current_year = current_date.year

To_turn_100 = 100 - age
year = current_year + To_turn_100
print(f"{name}, you will be turning 100 in {year}")
print("Copies:")
print(f"{name}, you will be turning 100 in {year}\n" * number)


