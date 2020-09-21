'''
./project1-sales-tax/sales_tax.py
<https://github.com/lduran2/cis106-python-projects/blob/master/project1-sales-tax/salestax.py>
Calculates the total price including tax of a purchase.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-09-21t14:37
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    1.0 - Implemented the total price calculator.
'''

# start

# The tax rate for the state, 5%
STATE_TAX_RATE = 0.05

# The tax rate for the county, 2.5%
COUNTY_TAX_RATE = 0.025

# Variables
subtotal_price = 0  # The total price before including tax.
state_tax_abs = 0   # Sales tax for the state in dollars.
county_tax_abs = 0  # Sales tax for the county in dollars.
total_tax_abs = 0   # Sales tax total in dollars.
total_price = 0     # The total price including tax.

# Accept subtotal price.
print('Please enter the amount of the purchase.')
subtotal_price = float(input('> '))

# Multiply subtotal price by STATE TAX RATE giving state tax absolute.
state_tax_abs = (subtotal_price * STATE_TAX_RATE)
# Multiply subtotal price by COUNTY TAX RATE giving county tax
# absolute.
county_tax_abs = (subtotal_price * COUNTY_TAX_RATE)

# Add county tax absolute to state tax absolute giving total tax
# absolute.
total_tax_abs = state_tax_abs + county_tax_abs

# Add total tax absolute to subtotal price giving total price.
total_price = subtotal_price + total_tax_abs

# Display subtotal price, state tax absolue, county tax absolute, total
# tax absolute, total price.
print()
print('Purchase         :\t$', format(subtotal_price, '13,.2f'))
print('State  sales tax :\t$', format(state_tax_abs, '13,.2f'))
print('County sales tax :\t$', format(county_tax_abs, '13,.2f'))
print('Total  sales tax :\t$', format(total_tax_abs, '13,.2f'))
print('Total of the sale:\t$', format(total_price, '13,.2f'))
print()

# finish
print('Done.')
