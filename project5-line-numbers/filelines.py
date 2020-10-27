'''
./project5-line-numbers/filelines.py
<https://github.com/lduran2/cis106-python-projects/blob/master/project5-line-numbers/filelines.py>
Functions which deal with lines in files.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-10-19t21:19
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    1.0 - Implemented the line numbering.
'''

import filelines


######################################################################
def number(infile, start=1, next=1, numformat='4d', linesep=': '):
    '''
    Numbers the lines in the specified file.
    @params
        infile    -- file whose lines to number
        start     -- the starting line number (default 1)
        next      -- the increment for each line (default 1)
        numformat -- format of the line numbers (default '4d')
        linesep   -- character separating number and statement
                     (default ': ')
    '''

    # start

    # Variables
    total = ''  # the string to return
    line = ''   # the current line read
    k = start   # the starting number

    # for each line
    for line in infile:
        # buffer the line number and statement
        total = total + format(k, numformat)
        total = total + linesep
        total = total + line
        # increase the line number
        k = k + 1
    # end for line

    # return the total string
    return total
# end main()
