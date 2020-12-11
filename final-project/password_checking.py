'''
./final-project/password_checking.py
An event-driven GUI program implementing password validator.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-11t18:34
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    v1.0 - 2020-12-11t18:34
        Implemented length, character classes.

Works cited:
    ^[1]: Built-in Functions: ord(c). (2020). Retrieved from Python
        <https://docs.python.org/3/library/functions.html?highlight=ord#ord>
'''

# The password must be at least 8 characters long.
MIN_LENGTH = 8

# The password must contain at least:
#   one alpha character [a-zA-Z];
#       `str.isalpha` accepts other character, so we don't use it.
#       We use ord so we can compare the integer values of each
#       characters^[1].
ALPHA = (tuple(range(ord('a'), (ord('z') + 1))) +
    tuple(range(ord('A'), (ord('Z') + 1))))
#   one numeric character [0-9];
NUMERIC = tuple(range(ord('0'), (ord('9') + 1)))
#   one character that is not alpha or numeric, such as
#   “! @ $ % ^ & * ( ) - _ = + [ ] ; : ' " , < . > / ?” this is an
#   example, all non-alpha or numeric characters should be included.
#       We can use `else` to perform this 
# The password must not: begin with an exclamation [!]
# or a question mark [?];
NONSTART = '!?'

# number of errors checked for
N_ERRORS = 6

def validate_password(s):
    '''
    Validates the password given by `s`.
    '''
    errors = []

    # check the length.
    if (len(s) < MIN_LENGTH):
        errors.append('✖ The password must be at least ' + str(MIN_LENGTH) +
            ' characters long.')
    # end if (len(s) < 8)

    # flags for the character classes
    has_alpha = False
    has_numeric = False
    has_nonalphanumeric = False
    has_space = False

    # populate the character class flags
    for c in s: # for each character in the string s
        if (ord(c) in ALPHA):
            has_alpha = True
        elif (ord(c) in NUMERIC):
            has_numeric = True
        elif (str.isspace(c)):
            has_space = True
        else:
            has_nonalphanumeric = True
        # end if (c in ALPHA) elif (c in NUMERIC)
        #     elif (str.isspace(c)) else
    # end for c in s

    # check each flag

    if (not(has_alpha)):
        errors.append('✖ The password must contain at least one alpha' +
            ' character.')
    # end if (not(has_alpha))

    if (not(has_numeric)):
        errors.append('✖ The password must contain at least one numeric' +
            ' character.')
    # end if (not(has_numeric))

    if (not(has_nonalphanumeric)):
        errors.append('✖ The password must contain at least one character' +
            ' that is not alpha or numeric.')
    # end if (not(has_nonalphanumeric))

    if (has_space):
        errors.append('✖ The password must not contain spaces.')
    # end if (has_space)

    # check the first character
    if (s[0] in NONSTART):
        errors.append('✖ The password must not begin with any of "' +
            NONSTART + '".')
    # end if (s[0] in NONSTART)

    # return the list of errors
    return tuple(errors)
# end def validate_password(s)
