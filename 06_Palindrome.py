# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

string_1 = str(input("Enter any string:\n")).upper()
print(" ".join(string_1))
reverse_string = string_1[::-1].upper()  #Reversing the string to check for palindrome
print(" ".join(reverse_string))

#Palindrome Checker
if string_1 == reverse_string:
    print("Yes, the given string is a palindrome.")
else:
    print("No, the given string is not a palindrome.")


