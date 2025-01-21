#!/usr/bin/python3
"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

Get all values in runtime
"""

p=int(input("Enter Initial Principal Balance : "))
r =float(input("Enter Annual Interest Rate : "))
t = int(input("Number Of Years : "))

A=p*(1+r*t)

print ("Final Amount : ",A)