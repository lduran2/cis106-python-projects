'''
./project6-total-sales/string_list_utilities.py
Different utility functions that use strings.

option_menu, rstrip_n_in, max_len

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-10-16t23:45
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.4

Changelog:
    v1.4 - 2020-11-09t20:45
        Abstracted ljust from total-sales.py

    v1.3 - 2020-10-16t23:45
        Abstracted from total-sales.py

    v1.2 - 2020-10-16t22:03
        Implemented menu.

    v1.1 - 2020-10-16t21:27
        Read all constants.

    v1.0 - 2020-10-16t20:25
        Introduced the program.
'''

def option_menu(\
    length, legend, options, labels, prompt_message, funcs, data, PROMPT, INVALID_OPTION):
    '''
    Allows the user to pick one of the `options`.
    @params
        length -- number of options
        legend -- prior to options list
        options -- the options the user can pick
        labels -- description of the options
        prompt_message -- instruction for the user
        data -- to manipulate
    '''
    choice = ''     # the option the user chose

    # poll user input
    while (True):
        i_choice = 0    # index of the user's choice

        # print the legend and options
        print(legend, end='')
        for k in range(length):
            print('\t(', options[k], ')\t', labels[k], sep='')
        # end for k

        # accept the choice
        print(prompt_message, end='')
        choice = input(PROMPT)

        # if empty, stop the menu loop
        if (choice == ''):
            return
        # end if (choice == '')

        # while invalid choice, ask again
        while (choice not in options):
            print(INVALID_OPTION)
            choice = input(PROMPT)
        # end while (choice not in options)

        # perform the corresponding function
        i_choice = options.index(choice)
        # if the function returns false, end the menu
        if (not funcs[i_choice](data, i_choice)):
            return
        # end if (not funcs[i_choice](data, i_choice))
    # end while (True)
# def def option_menu(\
#     length, legend, options, labels, prompt_message, funcs, data)

def rstrip_n_in(length, a_list):
    '''
    Strips the newline from every string in list `a_list` of size
    `length`.
    '''
    for k in range(length):
        a_list[k] = a_list[k].rstrip('\n')
# def trim_in(a_list)

def max_len(a_tuple):
    cur_len = 0 # length of current string
    the_max = 0 # the maximum length so far

    # for each element in the tuple
    for el in a_tuple:
        # get the current length
        cur_len = len(el)
        # if the current length exceeds the maximum so far
        if (the_max < cur_len):
            # replace the maximum
            the_max = cur_len
        # end if (the_max < cur_len)
    # end for el

    # return the result.
    return the_max
# end def max_len(a_tuple)

def ljust(string, width):
    '''
    Right justifies the given string in the given column width.
    '''
    # return the string with enough spaces to make up the width
    return (string + (' ' * (width - len(string))))
# end def ljust(string, width)

def false2(unused0, unused1):
    '''
    Returns False always, with two parameters
    '''
    return False
# def def false2(unused0, unused1)
