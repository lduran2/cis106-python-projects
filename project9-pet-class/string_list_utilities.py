'''
./project6-total-sales/string_list_utilities.py
Different utility functions that use strings.

option_menu, option_menu_apply, create_label_from_strings
stringify_in, rstrip_n_in, max_len, ljust, false2

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-22t14:57
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 2.1

Changelog:
    v2.1 - 2020-11-22t14:57
        Implemented `stringify_in`, helpful for menu options.

    v2.0 - 2020-11-22t14:26
        Refactored a `option_menu` into `option_menu_apply`
            and `create_label_from_strings`.
        `option_menu_apply` uses a function to get the label which
            helps with OOP.
        `create_label_from_strings` gives the origin behavior of
            getting labels from an array of strings or stringables.

    v1.4 - 2020-11-09t20:57
        Abstracted ljust `from total-sales.py`.
        Added `false2`.

    v1.3 - 2020-10-16t23:45
        Abstracted from `total-sales.py`.

    v1.2 - 2020-10-16t22:03
        Implemented menu `option_menu`.

    v1.1 - 2020-10-16t21:27
        Read all constants.

    v1.0 - 2020-10-16t20:25
        Introduced the program.
'''

def option_menu(\
    length, legend, options, labels, prompt_message, callbacks, data, prompt, invalid_option):
    '''
    Allows the user to pick one of the `options`, using label string.
    @params
        length -- number of options
        legend -- prior to options list
        options -- the options the user can pick
        labels -- description of the options
        prompt_message -- instruction for the user
        callbacks : (data, i_choice) = callback functions
        data -- to manipulate
        prompt -- the prompt character for input
        invalid_option -- error message when the user gives bad input
    '''
    # prepare `labelfn` to just index the labels list
    labelfn = create_label_from_strings(labels)
    # call `option_menu_apply` using the giving parameters
    # and `labelfn`
    option_menu_apply(length, legend, options,\
        labelfn,\
        prompt_message, callbacks, data, prompt, invalid_option\
    )
# def def option_menu(\
#     length, legend, options, labels, prompt_message, callbacks, data)

def option_menu_apply(\
    length, legend, options, labelfn, prompt_message, callbacks, data,\
    prompt, invalid_option):
    '''
    Allows the user to pick one of the `options`, using label functions.
    @params
        length -- number of options
        legend -- prior to options list
        options -- the options the user can pick
        labelfn : (data, i_choice) = function for getting labels from the data
        prompt_message -- instruction for the user
        callbacks : (data, i_choice) = callback functions
        data -- to manipulate
        prompt -- the prompt character for input
        invalid_option -- error message when the user gives bad input
    '''
    choice = ''     # the option the user chose

    # poll user input
    while (True):
        i_choice = 0    # index of the user's choice

        # print the legend and options with labels
        print(legend, end='')
        for k in range(length):
            print('\t(', options[k], ')\t', labelfn(data, k), sep='')
        # end for k

        # accept the choice
        print(prompt_message, end='')
        choice = input(prompt)

        # if empty, stop the menu loop
        if (choice == ''):
            return
        # end if (choice == '')

        # while invalid choice, ask again
        while (choice not in options):
            print(invalid_option)
            choice = input(prompt)
            # again if the next choise is empty, stop the menu loop
            if (choice == ''):
                return
            # end if (choice == '')
        # end while (choice not in options)

        # perform the corresponding function
        i_choice = options.index(choice)
        # if the function returns false, end the menu
        if (not callbacks[i_choice](data, i_choice)):
            return
        # end if (not funcs[i_choice](data, i_choice))
    # end while (True)
# end option_menu_apply(\
#   length, legend, options, labelfn, prompt_message, callbacks, data,\
#   prompt, invalid_option)

def create_label_from_strings(labels):
    '''
    Create a label function that merely indexes the list `labels`.
    @params
        labels -- the label list from which to return
    @return a function of (data, index) that returns `labels[index]`.
    '''
    def label_from_strings(data, index):
        return labels[index]
    # end def
    return label_from_strings
# end def create_label_from_strings(labels)

def stringify_in(length, a_list):
    '''
    Transforms the elements of list `a_list` into strings in place.
    '''
    for k in range(length):
        a_list[k] = str(a_list[k])
# end def stringify(length, a_list)

def rstrip_n_in(length, a_list):
    '''
    Strips the newline from every string in list `a_list` of size
    `length`.
    '''
    for k in range(length):
        a_list[k] = a_list[k].rstrip('\n')
# end def trim_in(a_list)

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
    Returns False always, with 2 unused parameters.
    '''
    return False
# end def false2(unused0, unused1)
