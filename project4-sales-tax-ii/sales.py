'''
./project4-sales-tax-ii/sales.py
<https://github.com/lduran2/cis106-python-projects/blob/master/project4-sales-tax-ii/sales.py>
A python module dealing with calculating sales taxes.
By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-05t18:16
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0
Changelog:
    1.0 - Implemented the library.
'''

# start

# Global Constants
STATE_TAX_RATE  = 0.05  # The tax rate for the state, 5%.
COUNTY_TAX_RATE = 0.025 # The tax rate for the county, 2.5%.


######################################################################
def calc_receipt(subtotal_price):
    '''
    Calculates the sales receipt including the state, count and total
    taxes and the total price.
    @params
        subtotal_price := the price before taxes
    @returns
        total_price    := the total price including taxes
        total_tax_abs  := the total tax itself
        state_tax_abs  := the absolute tax for the state
        county_tax_abs := the absolute tax for the county
    '''
    # Variables
    state_tax_abs  = 0.00   # Sales tax for the state in dollars.
    county_tax_abs = 0.00   # Sales tax for the county in dollars.
    total_tax_abs  = 0.00   # Sales tax total in dollars.
    total_price    = 0.00   # The total price including tax.

    # Calculate the total absolute tax.
    total_tax_abs, state_tax_abs, county_tax = calc_tax(subtotal_price)
    # Add total tax absolute to subtotal price giving total price.
    total_price = subtotal_price + total_tax_abs

    # Return the total price and all values used to calculate it.
    return total_price, total_tax_abs, state_tax_abs, county_tax_abs
# end def calc_receipt(subtotal_price)


######################################################################
def calc_tax(subtotal_price):
    '''
    Calculates the state, count and total taxes.
    @params
        subtotal_price := the price before taxes
    @returns
        total_tax_abs  := the total tax itself
        state_tax_abs  := the absolute tax for the state
        county_tax_abs := the absolute tax for the county
    '''
    # Variables
    state_tax_abs  = 0.00   # Sales tax for the state in dollars.
    county_tax_abs = 0.00   # Sales tax for the county in dollars.
    total_tax_abs  = 0.00   # Sales tax total in dollars.

    # Calculate the state tax.
    state_tax_abs = calc_state_tax(subtotal_price)
    
    # Calculate the county tax.
    county_tax_abs = calc_county_tax(subtotal_price)

    # Add county tax absolute to state tax absolute giving total tax
    # absolute.
    total_tax_abs = state_tax_abs + county_tax_abs

    # Return total absolute tax and all values used to calculate it.
    return total_tax_abs, state_tax_abs, county_tax_abs
# end def calc_tax(subtotal_price)


######################################################################
def calc_state_tax(subtotal_price):
    '''
    Calculates the state tax.
    @params
        subtotal_price := the price before taxes
    @returns
        the absolute tax for the state
    '''
    # Multiply subtotal price by STATE TAX RATE giving state tax
    # absolute.
    return (subtotal_price * STATE_TAX_RATE)
# end def calc_state_tax(subtotal_price)


######################################################################
def calc_county_tax(subtotal_price):
    '''
    Calculates the county tax.
    @params
        subtotal_price := the price before taxes
    @returns
        the absolute tax for the county
    '''
    # Multiply subtotal price by COUNTY TAX RATE giving county tax
    # absolute.
    return (subtotal_price * COUNTY_TAX_RATE)
# end def calc_state_tax(subtotal_price)

# finish
