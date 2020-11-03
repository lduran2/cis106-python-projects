'''
./project7-initals/initials.py
Accepts a name and returns the first, (middle), and last initials.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-02t19:27
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0
'''

# Constants
PROMPT = '> '
DEFAULT_MAX_INITIALS = 3    # by default find 3 initials
DEFAULT_INITIAL_SEPARATE = '. '

def main():
    '''
    The main program.
    '''
    # print the introductory text
    intro_initials()
    # accept a name string
    print('Please enter your name.')
    name = input(PROMPT)
    # find the initials
    initials = find_initials(name)
    # print the initials
    print('Your initials are', initials)
    # finish
    print('Done.')
# def end main()

def intro_initials():
    print('Project 7 Initials (More about strings)')
    print()
    print('Accepts a name and returns the first, (middle), and last initials.')
    print()
# def intro_initials()

def find_initials(string, \
                  max_initials=DEFAULT_MAX_INITIALS, \
                  sep=DEFAULT_INITIAL_SEPARATE):
    '''
    Finds the initials in a given string.
    @param
        string -- to search
        max_initials -- the number of initials to find (default 3)
        sep -- the separator character to use (default '. ')
    @return the initials in the string
    '''
    initials = ''           # the initials found so far
    n_initials_found = 0    # the number of initials found so far
    is_initial = True       # whether current character will be an initial

    # loop through the characters
    for ch in string:
        # if the current character is a space
        if (ch is ' '):
            # the next character is an initial
            is_initial = True
        # if the character is an initial
        elif (is_initial):
            # increment the number of initials found so far
            n_initials_found += 1
            # append the current character to the initials
            initials += ch + sep
            # if maximum initials found
            if (n_initials_found == max_initials):
                # end the loops
                break;
            # end if (n_initials_found == max_initials)
            # reset is_initial
            is_initial = False
        # end elif (is_initial)
    # end for ch in string

    # return the initials
    return initials
# end def find_initials(string, max_initials=DEFAULT_MAX_INITIALS)

# start the program
main()
