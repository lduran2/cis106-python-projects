'''
./project6-total-sales/total-sales.py
Asks for the sales for each day of the week and stores them in a list.
Then calculates the total and displays it.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-10-16t22:03
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.2

Changelog:
    v1.2 - 2020-10-16t22:03
        Implemented menu.

    v1.1 - 2020-10-16t21:27
        Read all constants.

    v1.0 - 2020-10-16t20:25
        Introduced the program.
'''

# Constants
CONFIG_FILENAME = './config'    # name of configuration file
INTRO = None                    # the introduction to this program
PROMPT = ''                     # prompt for user input
INVALID_OPTION = ''             # message for invalid option
N_WEEK_DAYS = 0                 # number of days of the week
WEEK_DAYS = None                # the days of the week
N_ACTIONS = 0                   # the number of actions in main menu
ACTION_LEGEND = ''              # the legend of the action menu
ACTION_OPTIONS = None           # the actions as options in menu
ACTION_LABELS = None            # the action short descriptions
ACTION_PROMPT = ''              # prompt for action
WEEK_DAY_LEGEND = ''            # the legend of the week day
WEEK_DAY_PROMPT = ''            # prompt for week day
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

    # Read an action
    option_menu(N_ACTIONS, ACTION_LEGEND, ACTION_OPTIONS, ACTION_LABELS, ACTION_PROMPT)

    # Program is done.
    print(DONE_STRING)
# end def main()

def option_menu(length, legend, options, labels, prompt_message):
    choice = ''     # the option the user chose

    # poll user input
    while (True):
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

        # if invalid choice, ask again
        while (choice not in options):
            print(INVALID_OPTION)
            choice = input(PROMPT)
        # end while (choice not in options)
    # end while (True)

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
    global N_WEEK_DAYS
    global WEEK_DAYS
    global N_ACTIONS
    global ACTION_LEGEND
    global ACTION_OPTIONS
    global ACTION_LABELS
    global ACTION_PROMPT
    global WEEK_DAY_LEGEND
    global WEEK_DAY_PROMPT
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
    INTRO = tuple(unsafe_intro_lines)   # make a safe tuple copy
    index += n_intro_lines

    # Find the prompt string.
    PROMPT = config_lines[index].rstrip('\n')
    index += 1
    # Find the invalid option message.
    INVALID_OPTION = config_lines[index]
    index += 1

    # Find the number of days for the week.
    N_WEEK_DAYS = int(config_lines[index])
    index += 1
    # Find the days of the week.
    unsafe_week_days = config_lines[index:(index + N_WEEK_DAYS)]
    WEEK_DAYS = tuple(unsafe_week_days) # make a safe tuple copy
    index += N_WEEK_DAYS

    # Find the legend of actions.
    ACTION_LEGEND = config_lines[index]
    index += 1
    # Find the number of actions.
    N_ACTIONS = int(config_lines[index])
    index += 1
    # Find action options.
    unsafe_action_options = config_lines[index:(index + N_ACTIONS)]
    rstrip_n_in(N_ACTIONS, unsafe_action_options)   # strip newlines
    ACTION_OPTIONS = tuple(unsafe_action_options)   # make a safe tuple copy
    index += N_ACTIONS
    # Find action labels.
    unsafe_action_labels = \
        config_lines[index:(index + N_ACTIONS)]     # make a safe tuple copy
    rstrip_n_in(N_ACTIONS, unsafe_action_labels)    # strip newlines
    ACTION_LABELS = tuple(unsafe_action_labels)
    index += N_ACTIONS
    # Find action prompt.
    ACTION_PROMPT = config_lines[index]
    index += 1
    
    # Find the legend of the day of the week.
    WEEK_DAY_LEGEND = config_lines[index]
    index += 1
    # Find day of the week prompt.
    WEEK_DAY_PROMPT = config_lines[index]
    index += 1

    # Find prompt of the sales prompt before day of week.
    SALES_PROMPT_BEFORE = config_lines[index]
    index += 1
    # Find prompt of the sales prompt after day of week.
    SALES_PROMPT_AFTER  = config_lines[index]
    index += 1

    # Find label for before total sales.
    SALES_PROMPT_BEFORE = config_lines[index]
    index += 1
    # Find label for after total sales.
    SALES_PROMPT_AFTER  = config_lines[index]
    index += 1

    # Find the done string.
    DONE_STRING = config_lines[index]
    index += 1
# end def config_total_sales()

def rstrip_n_in(length, a_list):
    for k in range(length):
        a_list[k] = a_list[k].rstrip('\n')
# def trim_in(a_list)

main()
