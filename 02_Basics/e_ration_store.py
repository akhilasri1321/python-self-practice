# you need to understand when you need to use jupitor notebook and python script
# jupitor is for  understanding some feautures or dwelling feature by feature but if you are solving some real problems we use script inly
# we need to create a small ration store--we will have predifined quantities and price of items - we are just supposed to go and make payment
#!/usr/bin/python3
"""
Purpose: Ration Store

    -----------------------------------------------
    item    cost        quantity        Amount
    -----------------------------------------------
    wheat   25/kg       30 kgs      25 * 30 = 750/-
    Rice    12/kg       50 kgs      12 * 50 = 600/-
                                -------------------
                                              1350/-
                                subsidy 20%   -270/-
                                --------------------
                                BillableAmount:1080/-

Algorithm
---------
Step 1:  Get the cost of items into variables
Step 2:  Get the quantity of items into variables
Step 3:  Compute the selling price to each item,
         and add them
Step 4:  Compute the subsidy amount and subtract
         from the selling price
Step 5:  Display the Billable Amount

"""

wheat_per_unit = 25
rice_per_unit = 12
quan_wheat =30
quan_rice =50

selling_price_per_unit = (wheat_per_unit*quan_wheat)+(rice_per_unit*quan_rice)
print("Selling_Price = ", selling_price_per_unit)
subsidy = selling_price_per_unit *20/100
print("subsidy = ",subsidy,
    "\nBillable Amount = ", selling_price_per_unit-subsidy)
