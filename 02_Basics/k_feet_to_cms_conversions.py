#!/usr/bin/python3
"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""

Feet_value = float(input('Enter Any Value : '))
foot =12 #inches
inch = 2.54 #cms
foot_in_cms=(inch*foot)

print("feet in Cms = " ,(foot_in_cms*Feet_value))