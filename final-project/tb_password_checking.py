'''
./final-project/tb_password_checking.py
Test bench for `./password_checking.py`

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-11t18:35
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    v1.0 - 2020-12-11t18:35
        Tested `./password_checking.py`.
'''

import password_checking as pwch

def main():
    passwords = ('abcdefg', 'abcdefgh', 'abcd1234', '1234!@#$', 'abcd!@#$',
        'abc 123!@#', 'abc123!@#', '!abc123@#', '?abc123@#', 'abc123!!@#', '!! ')
    #

    # test each password
    for word in passwords:
        print('Testing', word, '. . .')
        print('\n'.join(pwch.validate_password(word)))
        print()
    # end for word in passwords

    print('Done.')
# end def main()

main()
