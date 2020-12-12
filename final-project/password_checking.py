'''
./final-project/password_checking.py
A password validator method.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-11t20:24
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.2

Changelog:
    v1.2 - 2020-12-11t21:04
        Modularized `validate_password`.

    v1.1 - 2020-12-11t20:24
        Implemented repeating characters.
        Refactored checks into a tuple.

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
N_ERRORS = 7

def validate_password(s):
    '''
    Validates the password given by `s`.
    @returns a list of all errors found in password `s`.
    '''
    # list of errors
    errors = []

    (has_alpha, has_numeric, has_nonalphanumeric,
        has_space, has_repeating) = check_password_characters(s)

    # place all checks in a tuple
    checks = check_tuple(s, has_alpha, has_numeric, has_nonalphanumeric,
        has_space, has_repeating)

    # reduce the checks into the list of errors
    reduce_checks_to_errors(checks, errors)

    # return the list of errors
    return tuple(errors)
# end def validate_password(s)

def check_password_characters(s):
    '''
    Performs the character checks.
    @returns each character class flag.
    '''

    # flags for the character classes
    has_alpha = False
    has_numeric = False
    has_nonalphanumeric = False
    has_space = False
    has_repeating = False   # special: whether any character repeat

    # populate the character class flags
    prev_c = '' # the previous character
    for c in s: # for each character in the string s
        # We make sure to check whether `ord(c)` is in the character
        # classes by comparing their integer values.
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

        # check if same as previous character
        if (c == prev_c):
            has_repeating = True
        # end if (c == prev_c)
        prev_c = c  # update prev_c
    # end for c in s

    return (has_alpha, has_numeric, has_nonalphanumeric,
        has_space, has_repeating)
# end def check_password_characters(s)

def check_tuple(s, has_alpha, has_numeric, has_nonalphanumeric,
        has_space, has_repeating):
    '''
    Create a tuple containing each check.
    '''

    # get the length
    length = len(s)

    return (
        # the length
        { 'test': (length < MIN_LENGTH), 'message':
            '✖ must be at least ' + str(MIN_LENGTH) + ' characters long.'},
        # the flags
        { 'test': not(has_alpha), 'message':
            '✖ must contain at least one alpha character.' },
        { 'test': not(has_numeric), 'message':
            '✖ must contain at least one numeric character.'},
        { 'test': not(has_nonalphanumeric), 'message':
            '✖ must contain at least one character that is not alpha' +
            ' or numeric.'
        },
        { 'test': has_space, 'message':
            '✖ must not contain spaces.'},
        # the first character, but make sure there is a first character
        { 'test': ((length != 0) and (s[0] in NONSTART)), 'message':
            '✖ must not begin with any of "' + NONSTART + '".' },
        # any repeating characters
        { 'test': (has_repeating), 'message':
            '✖ cannot contain repeating character strings of 2 or more' +
            ' identical characters.'
        }
    )
# end def check_tuple(has_alpha, has_numeric, has_nonalphanumeric,
#       has_space, has_repeating)

def reduce_checks_to_errors(checks, errors):
    '''
    Evaluates each check and if true, adds it to the error list.
    @params
        checks -- tuple of checks with the test and related error message
        errors -- the error messages that apply
    '''
    for check in checks:
        if (check['test']):
            errors.append(check['message'])
        # end if (check[test])
    # end for check in checks
# end def reduce_checks_to_errors(checks, errors)
