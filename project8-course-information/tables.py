'''
./project8-course-information/tables.py
Utility functions for tables.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-09t20:49
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.1

Changelog:
    v1.1 - 2020-11-09t20:49
        Abstracted from ./course-information.py

    v1.0 - 2020-11-09t17:04
        Implemented ./course-information.py
'''

import string_list_utilities as slew

def create_row_printer(rows, col_width):
    '''
    Creates a function to print using the specified sequence of rows.

    @params
        rows -- sequence of row keys for the table
        col_width -- maximum length of the column name
    '''
    # Constants
    COL_FMT = ('-' + str(col_width) + 's')   # the column format

    # We create a two-parameter function since slew.option_menu
    # expects this.
    def print_row(table, i_row):
        '''
        Prints the row from the given table at the given index.
        @params
            table -- data from which to print
            i_row -- index of the 
        @returns True to stay in the menu
        '''
        # for each column
        for col in table:
            # print the column header
            print(slew.ljust(col, col_width), ': ', sep='', end='')
            # print the data at this column and row
            print(table[col][rows[i_row]])
        # end for col
        # empty line
        print()
        # stay in the menu
        return True
    # end def print_row(table, i_row)

    # create the two-parameter function
    return print_row
# end def create_table_printer(course_numbers)
