# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = int(input("Enter the number:\n"))
num = int(input("Enter another number:\n"))
check = int(input("Enter a number to divide to the previous one:\n"))
if number%4==0:
    print("Original number is a multiple of 4.")
elif number%2==0:
    print("Original number is even.")
else:
    print("Original number is odd.")

if num%check==0:
    print("The secondary number is evenly divided.")
else:
    print("The secondary number isn't even divided.")

