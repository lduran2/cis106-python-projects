'''
./final-project/credit_card.py
Classes and methods for handling credit cards.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-12-20t0208
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.1

Changelog:
    v1.1 - 2020-12-20t0208
        Parsed second level of credit card configuration.
    v1.0 - 2020-12-20t0148
        Parsed top level of credit card configuration.
'''

def license(filename='credit-card-config'):
    '''
    Creates a license to create credit cards.
    @param
        filename -- the name of the configuration file,
                    or the file itself if it has a readline method,
                    or the list of lines from the file if it is a list
    '''
    # if `filename` is a list,
    if (isinstance(filename, list)):
        lines = filename    # it is the list of lines
        industries = []     # the major industry identifiers

        # the first two lines are the minimum and maximum lengths of
        # credit card numbers
        min = int(lines[0])
        max = int(lines[1])

        # for each of the remaining lines
        for line in lines[2:]:
            # if the line is first level,
            if (not(line.startswith('\t'))):
                # then it is the name of a major industry identifier
                # update the current industry, and append it to the list
                industry = { 'name' : line.strip(), 'companies' : [] }
                industries.append(industry)
            # end if (not(line.startswith('\t')))
            # if the line is second level,
            elif (not(line.startswith('\t' * 2))):
                # then it is a company
                # append to current industry's companies list
                industry['companies'].append(line.strip())
            # end elif (not(line.startswith('\t' * 2)))
        # end for line in lines[2:]

        # print the result and its length
        print(industries)
        print(len(industries))
    # end if (isinstance(filename, list))
    # if `filename` has a readlines method,
    elif (hasattr(filename, 'readlines')):
        infile = filename   # it is an input file
        # read the lines and make the license
        license(infile.readlines())
    # end elif (hasattr(filename, 'readlines'))
    # otherwise
    else:
        infile = open(filename, 'r')    # open the `filename` for reading
        try:
            # make the license from the input file
            license(infile)
        finally:
            # close the file
            infile.close()
        # end try license(infile) finally
    # end if (isinstance(filename, list)) elif (filename.readlines) else
# def license(lines)

# test run the license
license()
