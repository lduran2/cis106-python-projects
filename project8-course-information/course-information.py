'''
./project8-course-information/course-information.py
Menu that accepts a course by course number and displays the
information about the course using various functions of a dictionary,
len(), keys(), keying.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-09t21:02
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.1

Changelog:
    v1.1 - 2020-11-09t21:02
        Abstracted out from ./tables.py

    v1.0 - 2020-11-09t17:04
        Implemented ./course-information.py
'''

import string_list_utilities as slew
import tables as tab

def main():
    '''
    The main program.
    '''

    # The course information dictionaries, Room Numbers, Instructors, Meeting Times.
    course_information = {\
        'Room Number' : {\
            'CS101' : '3004',\
            'CS102' : '4501',\
            'CS103' : '6755',\
            'NT110' : '1244',\
            'CM241' : '1411'\
        },\
        'Instructor' : {\
            'CS101' : 'Haynes',\
            'CS102' : 'Alvarado',\
            'CS103' : 'Rich',\
            'NT110' : 'Burke',\
            'CM241' : 'Lee'\
        },\
        'Meeting Time' : {\
            'CS101' : '8:00 a.m.',\
            'CS102' : '9:00 a.m.',\
            'CS103' : '10:00 a.m.',\
            'NT110' : '11:00 a.m.',\
            'CM241' : '1:00 p.m.'\
        }\
    }
    # Fetch the courses, the common keys of the course information.
    course_keys = list(course_information['Room Number'].keys())
    # Add the exit option.
    courses = tuple(course_keys + ['X'])
    # Get the number of courses.
    n_courses = len(course_keys)
    # Find the course column width.
    course_width = slew.max_len(courses)
    # Use blanks for course labels (the option is enough information).
    course_labels = tuple(([''] * n_courses) + ['Exit'])

    # create callback functions
    print_course_information = tab.create_row_printer(courses, course_width)
    funcs = tuple(([print_course_information] * n_courses)\
        + [slew.false2])

    slew.option_menu((n_courses + 1), 'Course number:\n',
        courses, course_labels,\
        'Please choose a course.\n',\
        funcs, course_information,\
        '> ', 'Invalid course number.'\
    )

    # finish
    print('Done.')
# end def main()

main()
