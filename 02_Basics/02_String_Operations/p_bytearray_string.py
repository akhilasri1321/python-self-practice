#!/usr/bin/python3
"""
Purpose: bytearray strings
"""

ordinary_string = "Tomorrow will be ours!!!"
#ordinary_string[9:17] = 'is '
# TypeError: 'str' object does not support item assignment

print(ordinary_string[:9] + "is " + ordinary_string[17:])
print()



# Ordinary string are immutable
# bytearray strings are mutable


b_string = bytearray("Tomorrow will be ours!!!", "ascii")
print("b_string      :", b_string)
print("type(b_string):", type(b_string))


print("b_string[9:17]", b_string[9:17])
print(b_string.find(b"will be"))

b_string[9:17] = b"is "
print("b_string", b_string)

#############################
print()
# indexing a bytearray string
print("ordinary_string[6]", ordinary_string[6])
print("b_string[6]       ", b_string[6])

print()
# ord() and chr()
# Ascii  : o -> 111
print("chr(111):", chr(111))
print("ord('o'):", ord("o"))



# Assignment
# -------------
# caesar cipher
# ------------------  + 3
# A B C D E F G H I J     Y Z
# 0 1 2 3 4 5 6 7
# D E F


# Ex: egg => hjj
#    bindu => elqg
#    yash  => bd..

# ASSUMPTION: Ignore case -sensitivity
# HINTS: ord(), chr(), %

text = input("Enter text: ")  # Get input from the user
result = "".join(chr(ord(c) + 3) if c.isalpha() else c for c in text)  # Shift each character by 3
print("Shifted text:", result)  # Print the result