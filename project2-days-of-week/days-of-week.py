'''
./project2-days-of-week/days-of-week.py
<https://github.com/lduran2/cis106-python-projects/blob/master/project2-days-of-week/days-of-week.py>
Finds the day of the week given a day number.
By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-09-28t23:51
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0
Changelog:
    1.0 - Implemented the day of week finder.
'''

# start

# Variables
dayNo = 0  # the day number

# Accept day number.
print('Please enter the day number.')
dayNo = int(input('> '))

# Find the day by the day number.
if (dayNo == 1):
    print("It's Monday.")
elif (dayNo == 2):
    print("It's Tuesday.")
elif (dayNo == 3):
    print("It's Wednesday.")
elif (dayNo == 4):
    print("It's Thusday.")
elif (dayNo == 5):
    print("It's Friday.")
elif (dayNo == 6):
    print("It's Saturday.")
elif (dayNo == 7):
    print("It's Sunday.")
else:
    print('The day number must be between 1 and 7. You entered', dayNo)
# end if (dayNo)

# finish
print('Done.')
