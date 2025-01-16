#!/usr/bin/python3
"""
Purpose: print() function syntax and usage
    Escapes Sequences
        - characters whose presence is felt, but they were not printed
        \t - tab space
        \n - new line
        \b - overwrites previous character

        r'' - raw string

"""

print('Hello world python')
print('Hello \tworld \tpython')
print('Hello \nworld \npython')

# in some scenarios we want escape sequences to be printed--- two things we can do: use \\ or use r before line for raw representation
print('Hello \tworld \\npython')
print(r'Hello \ttworld \npython')

# where we can use r
print("c:\my\newfolder")
print(r"c:\my\newfolder")

#print(data, sep=' ', end='\n')

print("hello") # defalut end ='\n'
print("world")

print("Hello", end='\n')
print("Hello", end='-')
print("Hello", end='\t')
print("Hello", "world","123", end='\t', sep="-")


# \b - overwrites previous character
print("He\bi")
print("12\b34")
print("first\bsecond")
print("\bsecond")  # if \b is at a start or end it will not have any effect)
print("second\b")
print("second\b1")
print()

# when you go to python and type :'he\bi' output: 'he\x08i' (x08i) is ascii character



# \r - overwrites complete existing line
print("He\ri")
print("12\r34")
print("first\rsecond")
print("abcdef\r1234")
print("1234567\rDOG")
print()



# Unicode characters \uXXX - unicode character
print("\u20B9")  # ₹
print("\u018e")  # Ǝ

print("\046")  # &

# \x... - hexadecimal number
print("\x24")
print("\xf1")
print()

print("#$%*&^(*;")

# ASCII & UTF encoding
# assignmen t -- get the unicode characters for telugu  range