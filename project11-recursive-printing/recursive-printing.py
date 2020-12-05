'''
./project11-recursive-printing/recursive-printing.py
A program that demonstrates recursion by printing the numbers [1, n].

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-27t15:09
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.2

Changelog:
    v1.2 - 2020-11-27t15:09
        Cleaned up recursive call and comments.

    v1.1 - 2020-11-27t10:32
        Added parameter for printing function.

    v1.0 - 2020-11-27t10:10
        Initial implementation.
'''

def main():
    '''
    The main program.
    '''
    # Accept the end value
    print('What is the maximum limit to print to?')
    max_limit = int(input('> '))
    # print recursively up to `max_limit`
    print_recursively(max_limit)
    # finish
    print('Done.')
# end def main()

def print_recursively(n, index = 1, func=print):
    '''
    Counts recursively, and displays the result in standard output.
    @param
        n -- the maximum limit to count up through
        index -- the starting index to count from (default 1)
        func -- the printing function (default `print`)
    '''
    # base case, stop if the index is greater than the end value
    if (index > n):
        return
    # end if (index > n)

    # inductive step
    # print the index
    func(index)
    # repeat, increasing the index
    print_recursively(n, (index + 1), func)
# end def print_recursively(end, index = 1, func=print)

# start
main()