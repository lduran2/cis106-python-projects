'''
./project3-bug-collector/bug-collector.py
<https://github.com/lduran2/cis106-python-projects/blob/master/project3-bug-collector/bug-collector.py>
The Python program, calculates the running total of the bugs collected
during a 5 day period.
By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-10-05t23:22
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.2
Changelog:
    1.2 - Implemented the bug collector loops.
    1.0 - Created the pseudocode.
'''

# start

# Variables
iDay = 0                    # the current day
nBugs = 0                   # number of bugs caught on iDay
N_DAYS = 5                  # total number of days
days = range(1,N_DAYS+1)    # the five days [1, N_DAYS]


# Initialize total.
total = 0

# point P:
# Loop through the days.
for iDay in days:
    # Accept the # bugs for this day.
    print('Please enter the number of bugs for day ', iDay, '.', sep='')
    nBugs = int(input('> '))
    # point Q:
    # is the # bugs negative?
    while (nBugs < 0):
        # Display an error message.
        print('The number of bugs must be non-negative. Please try again.')
        # Accept the # bugs again.
        nBugs = int(input('> '))
    # end while (nBugs < 0)
    
    # Add # bugs to total.
    total += nBugs
# end for iDay in days

# Display the total.
print()
print('The total number of bugs for the', N_DAYS, 'days', end='')
print(' is ', total, '.', sep='')

# finish
print('Done.')
