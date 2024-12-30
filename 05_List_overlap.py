# Take two lists and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.
import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 89]
c = []     #List for common elements
def list_sorting(a,b):
    for x in a:
        for y in b:
            if x==y:
                c.append(x)
    final1 = list(set(c))  # To remove duplicates
    print(*final1, sep=",")
list_sorting(a, b)

# Extras:
# Randomly generate two lists to test this
n = int(input("Enter number of elements in 1st list:\n"))
m = int(input("Enter number of elements in 2nd list:\n"))
# Function for random generation
rand_list_1 = random.sample(range(1,100),n)
rand_list_2 = random.sample(range(1,100), m)

list_sorting(rand_list_1, rand_list_2)

# Write this in one line of Python
#----------------------------------
# To be Done
#----------------------------------

