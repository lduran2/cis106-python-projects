'''
./project5-line-numbers/line-numbers.py
<https://github.com/lduran2/cis106-python-projects/blob/master/project5-line-numbers/line-numbers.py>
Numbers the lines in a given text file.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-10-19t21:18
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    1.0 - Implemented the line numbering.
'''

import filelines


######################################################################
def main():
    '''
    The program.
    '''

    # start

    # Variables
    infile = None       # the file to line number
    numbered_lines = '' # the file lines after numbering

    # Show the intro text.
    intro_line_number()
    # Get the file from the user.
    infile = input_file()
    # Number the lines of the file.
    try:
        numbered_lines = filelines.number(infile)
        # Print the result.
        print(numbered_lines)
    # Always close the file.
    finally:
        infile.close()
    # end finally
    print()
    # finish
    print('Done.')
# end main()


######################################################################
def intro_line_number():
    '''
    Introduces this program.
    '''
    print('This program numbers the lines in a file, by 1s starting')
    print('with 1 and separated by a colon character.')
    print()
# end def intro_sales_tax()
    

######################################################################
def input_file():
    '''
    Accepts and validates the name of the file.
    @returns
        a valid file.
    '''
    # Variables
    filename = ''   # name of the file to line number
    file = None     # the file itself

    # Accept the name of the file.
    print('Please enter the name of the file.')
    filename = input('> ')
    # While the file is not found:
    while (file == None):
        # Try opening the file
        try:
            file = open(filename, 'r')
        # If the file cannot open,
        except IOError:
            # Print an error message and try again.
            print('File not found. Please try again.')
            filename = input('> ')
        # end except IOError
    # end while (file == None)
    return file
# end def input_file()


######################################################################
# Execute the main program.
main()
