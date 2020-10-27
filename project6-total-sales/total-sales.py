'''
./project6-total-sales/total-sales.py
Asks for the sales for each day of the week and stores them in a list.
Then calculates the total and displays it.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-10-16t20:00
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    v1.0 - 2020-10-16t20:00
        Introduced the program.
'''

CONFIG_FILENAME = './config'
INTRO = None

def main():
    config_total_sales()    # Configure this program.
    intro_total_sales()     # Display the introduction.
# end def main()

def config_total_sales():
    '''
    Configures all constants for the program.
    '''
    # Allow to change intro.
    global INTRO

    # Open the configuration file.
    config_file = open(CONFIG_FILENAME, 'r')
    # Read all of the lines in the configuration file.
    config_lines = config_file.readlines()
    # Close the configuration file
    config_file.close()

    # Find the number of lines in the introduction.
    INTRO_LINES = int(config_lines[0])
    # Find the introduction.
    INTRO = config_lines[1:(1 + INTRO_LINES)]
# end def config_total_sales()

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

main()
