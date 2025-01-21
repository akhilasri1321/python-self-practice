#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""
## Step 1: Create an variable 'balance' with initial value 0


balance =0
min_balance =1500
salary = 3300
online_purch =33.33
House_rent =1500
Gross_balance =(min_balance+salary)
expenses = (online_purch+House_rent)
balance =(Gross_balance-expenses)
print("Balance =",balance)
