# Take a list and write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = len(a)
for i in range(n):
    if a[i]<5:
        print(a[i])

#Extras:
#Creating New list and printing the elements less than 5 via that
a1=[]
for i in range(n):
    if a[i]<5:
        a1.append(a[i])
print(*a1)

# ---------------------
# Writing in 1 line
print(*[x for x in a if x<5])
# ---------------------

# Ask the user for a number and return a list that contains only elements
# from the original list "a" that are smaller than that number given by the user.
new_list=[]
number = int(input("Enter a number:\n"))
for i in range(n):
    if a[i]<number:
        new_list.append(a[i])
print(*new_list)

