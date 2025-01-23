#!/usr/bin/python3
"""
Purpose: Demonstration of Palindrome check

    palindrome strings
        dad
        mom

Algorithms:
-----------
Step 1: Take the string in run-time and store in a variable


"""

# Taking input from the user
Palindrome_str = input("Enter a word to check if it's a palindrome: ")

# Checking if the string is equal to its reverse
if Palindrome_str == Palindrome_str[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
