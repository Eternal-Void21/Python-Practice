# Write one line of Python that takes the list "a" and makes a new list that has only the even elements of this list in it.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_list = [elem for elem in a if elem%2==0] #To find even elements and add to new_list
print(f"Even elements: {even_list}")

#For odd elements
odd_list = [elem for elem in a if elem%2!=0]
print(f"Odd elements: {odd_list}")
