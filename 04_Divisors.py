# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
number = int(input("Enter the number:\n"))
potential_divisors= range(2,number)  # Defining potential candidates for divisors
potential_divisors_list = []

# Forming the list of potential candidates after user input of number
for elem in potential_divisors:
    potential_divisors_list.append(elem)

divisors = [1,number]    #Final output list
# For finding the divisors as divisors will divide the given number evenly
for elem in potential_divisors_list:
    if number%elem==0:
        divisors.append(elem)

divisors.sort()
print(*divisors, sep = ",")
# sep function is used here to add commas between elements. Default value of sep is "space"

