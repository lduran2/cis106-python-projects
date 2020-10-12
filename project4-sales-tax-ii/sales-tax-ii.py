'''
./project4-sales-tax-ii/sales-tax-ii.py
<https://github.com/lduran2/cis106-python-projects/blob/master/project4-sales-tax-ii/sales-tax-ii.py>
Calculates the total price including tax of a purchase.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-10-12t18:40
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    v1.2 - 2020-10-12 - Refactored for modularization.
    v1.0 - 2020-09-21 - Implemented the total price calculator.
'''

import sales


######################################################################
def main():
    '''
    The program.
    '''

    # start

    # Variables
    subtotal_price = 0.00   # The total price before including tax.
    state_tax_abs  = 0.00   # Sales tax for the state in dollars.
    county_tax_abs = 0.00   # Sales tax for the county in dollars.
    total_tax_abs  = 0.00   # Sales tax total in dollars.
    total_price    = 0.00   # The total price including tax.

    intro_sales_tax()
    subtotal_price = input_subtotal()
    total_price, total_tax_abs, state_tax_abs, county_tax_abs \
                 = sales.calc_receipt(subtotal_price)
    print_receipt(subtotal_price, state_tax_abs, county_tax_abs, \
                  total_tax_abs, total_price)

    # finish
    print('Done.')
# end main()


######################################################################
def intro_sales_tax():
    '''
    Introduces this program.
    '''
    print('This program calculates the state, local and total tax, and')
    print('total price given a subtotal price.')
    print('\tthe  state sales tax rate is', sales.STATE_TAX_RATE)
    print('\tthe county sales tax rate is', sales.COUNTY_TAX_RATE)
    print()
# end def intro_sales_tax()
    

######################################################################
def input_subtotal():
    '''
    Accepts and validates a subtotal price from the console.
    @returns
        a valid subtotal sales price.
    '''
    # Accept subtotal price.
    print('Please enter the amount of the purchase.')
    subtotal_price = float(input('> '))
    # While the price is negative
    while (subtotal_price < 0):
        print('The price must be positive. Please try again.')
        subtotal_price = float(input('> '))
    # end while (subtotal_price < 0)
    return subtotal_price
# end def input_subtotal()


######################################################################
def print_receipt(subtotal_price, state_tax_abs, county_tax_abs,\
                  total_tax_abs, total_price):
    '''
    Display subtotal price, state tax absolue, county tax absolute,
    total tax absolute, total price.
    @params
        state_tax_abs  := the absolute tax for the state
        county_tax_abs := the absolute tax for the county
        total_tax_abs  := the total tax itself
        total_price    := the total price including taxes
    '''
    print()
    print('Purchase         :\t$', format(subtotal_price, '13,.2f'))
    print('State  sales tax :\t$', format(state_tax_abs, '13,.2f'))
    print('County sales tax :\t$', format(county_tax_abs, '13,.2f'))
    print('Total  sales tax :\t$', format(total_tax_abs, '13,.2f'))
    print('Total of the sale:\t$', format(total_price, '13,.2f'))
    print()
# end def print_receipt(subtotal_price, state_tax_abs, county_tax_abs\
#                       total_tax_abs, total_price)


######################################################################
# Execute the main program.
main()
