'''
./project8-course-information/course-information.py
Menu that accepts a course by course number and displays the
information about the course using various functions of a dictionary,
len(), keys(), keying.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-09t17:04
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0
'''

import string_list_utilities as slew

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
    courses = tuple(course_information['Room Number'].keys())
    # Get the number of courses.
    n_courses = len(courses)
    # Use blanks for course labels (the option is enough information).
    course_labels = tuple([''] * n_courses)

    # create callback functions
    print_course_information = print_course_information_of(courses)
    funcs = tuple([print_course_information] * n_courses)

    slew.option_menu(n_courses, 'Course number:\n', courses, course_labels,\
        'Please choose a course (Ctrl+C to stop).\n',\
        funcs, course_information,\
        '> ', 'Invalid course number.'\
    )

    # finish
    print('Done.')
# end def main()

def print_course_information_of(course_numbers):
    '''
    Prints course information with the given course numbers sequence.

    @params
        course_numbers -- sequence of course number keys
    '''
    # We create a two-parameter function since slew.option_menu
    # expects this.
    def print_course_information(information, index):
        '''
        Prints the course information at the given index.
        @params
            data -- data from which to print
            index -- index of where from in the data to print
        @returns True to stay in the menu
        '''
        for property in information:
            print(property, ': ', information[property][course_numbers[index]], sep='')
        # end for property, values
        # empty line
        print()
        # stay in the menu
        return True
    # end def print_course_information(information, index)

    # create the two-parameter function
    return print_course_information
# end def print_course_information_of(course_numbers)

main()
