'''
./project6-total-sales/total-sales.py
Asks for the sales for each day of the week and stores them in a list.
Then calculates the total and displays it.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-10-16t23:45
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.3

Changelog:
    v1.3 - 2020-10-16t23:45
        Finished implementation.

    v1.2 - 2020-10-16t22:03
        Implemented menu.

    v1.1 - 2020-10-16t21:27
        Read all constants.

    v1.0 - 2020-10-16t20:25
        Introduced the program.
'''

import string_list_utilities as slew

# Constants
CONFIG_FILENAME = './config'    # name of configuration file
N_ACTIONS = 3                   # the number of actions in main menu

# Constants read in from the configuration
INTRO = None                    # the introduction to this program
PROMPT = ''                     # prompt for user input
INVALID_OPTION = ''             # message for invalid option
WEEK_DAYS_LEGEND = ''           # the legend of the week day
N_WEEK_DAYS = 0                 # number of days of the week
WEEK_DAYS_OPTIONS = None        # the days of the week as options
WEEK_DAYS = None                # the days of the week
WEEK_DAYS_LEN = 0               # the length of the longest week day name
WEEK_DAYS_PROMPT = ''           # prompt for week day
WEEK_DAYS_FUNCS = None          # functions for days of week
ACTION_LEGEND = ''              # the legend of the action menu
ACTION_OPTIONS = None           # the actions as options in menu
ACTION_LABELS = None            # the action short descriptions
ACTION_PROMPT = ''              # prompt for action
SALES_PROMPT_BEFORE = ''        # part of sales prompt before day of week
SALES_PROMPT_AFTER = ''         # part of sales prompt after day of week
TOTAL_LABEL_BEFORE = ''         # the label for before total sales
TOTAL_LABEL_AFTER = ''          # the label for after total sales
DONE_STRING = ''                # the done string

def main():
    '''
    The main program.
    '''
    # Configure this program.
    config_total_sales()
    # Display the introduction.
    intro_total_sales()

    # Initialize list of sales.
    sales = [0.00] * N_WEEK_DAYS

    # Initialize functions of actions menu
    action_funcs = (print_sales, update_sales, calculate_totals)


    # Read an action
    slew.option_menu(N_ACTIONS, ACTION_LEGEND, \
                ACTION_OPTIONS, ACTION_LABELS, ACTION_PROMPT, \
                action_funcs, sales, PROMPT, INVALID_OPTION)

    # Program is done.
    print(DONE_STRING)
# end def main()

def print_sales(sales, unused):
    '''
    Displays all sales by their days of the week.
    @params
        sales -- to display
    @returns True to stay in menu
    '''
    print()
    # for each weekday
    for k in range(N_WEEK_DAYS):
        # print the week day name
        print(WEEK_DAYS[k], end='')
        # print remaining spaces
        print((' ' * (WEEK_DAYS_LEN - len(WEEK_DAYS[k]))), end='')
        # print the corresponding sales
        print('\t', format(sales[k], '10,.2f'))
    # end for k
    print()

    # stay in the menu
    return True
# end print_sales(sales)

def update_sales(sales, unused):
    '''
    Menu to choose which day to start updating.
    @params
        sales -- to update
    @returns True to stay in menu
    '''
    # Read an action
    slew.option_menu(N_WEEK_DAYS, WEEK_DAYS_LEGEND, \
                WEEK_DAYS_OPTIONS, WEEK_DAYS, WEEK_DAYS_PROMPT, \
                WEEK_DAYS_FUNCS, sales, PROMPT, INVALID_OPTION)

    # stay in the menu
    return True
#

def calculate_totals(sales, unused):
    '''
    Calculate the total and print it.
    @params
        sales -- to total
    @returns True to stay in menu
    '''
    total = 0   # total sales so far
    # add up all sales
    for sale in sales:
        total += sale
    # end for sale

    print()
    print(TOTAL_LABEL_BEFORE, format(total, '10,.2f'), TOTAL_LABEL_AFTER, sep='')
    print()

    # stay in the menu
    return True
# end def calculate_totals(sales)

def update_from(sales, i_choice):
    '''
    Updates the sales starting with a chosen week day.
    @params
        sales -- to update
        i_choice -- the day chosen
    @returns False to leave menu
    '''
    print()
    for k in range(i_choice, N_WEEK_DAYS):
        print(SALES_PROMPT_BEFORE, WEEK_DAYS[k], SALES_PROMPT_AFTER, sep='')
        unsafe_sales = float_input_sales()
        # stop if blank
        if (unsafe_sales == ''):
            return False
        # end if (unsafe_sales == '')
        # make sure sales is 
        while (sales[k] < 0):
            print(INVALID_INPUT)
            unsafe_safe = float_input_sales()
        # end while
        sales[k] = unsafe_sales
    # end for k
    print()

    # leave menu
    return False
# 

def float_input_sales():
    unsafe_sales = input(PROMPT)
    # empty string exits
    if (unsafe_sales == ''):
        return ''
    # end if (unsafe_sales == '')
    return float(unsafe_sales)
# def input_sales()

def intro_total_sales():
    '''
    Prints the introduction to this program.
    '''
    # Loop through the intro.
    for line in INTRO:
        # Print each line.
        print(line, end='')
    # end for line
# end def intro_total_sales()

def config_total_sales():
    '''
    Configures all constants for the program.
    '''
    # Global constants
    global INTRO
    global PROMPT
    global INVALID_OPTION
    global WEEK_DAYS_LEGEND
    global N_WEEK_DAYS
    global WEEK_DAYS_OPTIONS
    global WEEK_DAYS
    global WEEK_DAYS_LEN
    global WEEK_DAYS_PROMPT
    global WEEK_DAYS_FUNCS
    global ACTION_LEGEND
    global ACTION_OPTIONS
    global ACTION_LABELS
    global ACTION_PROMPT
    global SALES_PROMPT_BEFORE
    global SALES_PROMPT_AFTER
    global TOTAL_LABEL_BEFORE
    global TOTAL_LABEL_AFTER
    global DONE_STRING

    # Variables
    index = 0                       # index of the configuration lines
    config_file = None              # the configuration file object
    config_lines = None             # lines read from the configuration file
    n_intro_lines = 0               # number of lines in the introduction
    unsafe_intro_lines = None       # list of intro lines
    n_week_days = 0                 # number of days of the week
    unsafe_week_days = None         # list of days of week
    unsafe_action_options = None    # list of action options
    unsafe_action_labels = None     # list of action labels

    # Open the configuration file.
    config_file = open(CONFIG_FILENAME, 'r')
    # Read all of the lines in the configuration file.
    config_lines = config_file.readlines()
    # Close the configuration file
    config_file.close()

    # Find the number of lines in the introduction.
    n_intro_lines = int(config_lines[0])
    index += 1
    # Find the introduction.
    unsafe_intro_lines = config_lines[index:(index + n_intro_lines)]
    INTRO = tuple(unsafe_intro_lines)               # make a safe tuple copy
    index += n_intro_lines

    # Find the prompt string.
    PROMPT = config_lines[index].rstrip('\n')
    index += 1
    # Find the invalid option message.
    INVALID_OPTION = config_lines[index]
    index += 1

    # Find the legend of the day of the week.
    WEEK_DAYS_LEGEND = config_lines[index]
    index += 1
    # Find the number of days for the week.
    N_WEEK_DAYS = int(config_lines[index])
    index += 1
    # Find week day options.
    unsafe_WEEK_DAYS_options = config_lines[index:(index + N_WEEK_DAYS)]
    slew.rstrip_n_in(N_WEEK_DAYS, unsafe_WEEK_DAYS_options)   # strip newlines
    WEEK_DAYS_OPTIONS = tuple(\
            unsafe_WEEK_DAYS_options)                # make a safe tuple copy
    index += N_WEEK_DAYS
    # Find the days of the week.
    unsafe_week_days = config_lines[index:(index + N_WEEK_DAYS)]
    slew.rstrip_n_in(N_WEEK_DAYS, unsafe_week_days)      # strip newlines
    WEEK_DAYS = tuple(unsafe_week_days)             # make a safe tuple copy
    index += N_WEEK_DAYS
    # Find the length of the longest days of the week by name.
    WEEK_DAYS_LEN = slew.max_len(WEEK_DAYS)
    # Find day of the week prompt.
    WEEK_DAYS_PROMPT = config_lines[index]
    index += 1
    WEEK_DAYS_FUNCS = tuple([update_from] * N_WEEK_DAYS)

    # Find the legend of actions.
    ACTION_LEGEND = config_lines[index]
    index += 1
    # Find the number of actions.
    n_actions = int(config_lines[index])
    index += 1
    # Find action options.
    unsafe_action_options = config_lines[index:(index + n_actions)]
    slew.rstrip_n_in(n_actions, unsafe_action_options)   # strip newlines
    ACTION_OPTIONS = tuple(unsafe_action_options)   # make a safe tuple copy
    index += n_actions
    # Find action labels.
    unsafe_action_labels = config_lines[index:(index + n_actions)]
    slew.rstrip_n_in(n_actions, unsafe_action_labels)    # strip newlines
    ACTION_LABELS = tuple(unsafe_action_labels)     # make a safe tuple copy
    index += n_actions
    # Find action prompt.
    ACTION_PROMPT = config_lines[index]
    index += 1
    
    # Find prompt of the sales prompt before day of week.
    SALES_PROMPT_BEFORE = config_lines[index].rstrip('\n')
    index += 1
    # Find prompt of the sales prompt after day of week.
    SALES_PROMPT_AFTER  = config_lines[index].rstrip('\n')
    index += 1

    # Find label for before total sales.
    TOTAL_LABEL_BEFORE = config_lines[index].rstrip('\n')
    index += 1
    # Find label for after total sales.
    TOTAL_LABEL_AFTER = config_lines[index].rstrip('\n')
    index += 1

    # Find the done string.
    DONE_STRING = config_lines[index]
    index += 1
# end def config_total_sales()

main()
