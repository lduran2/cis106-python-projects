'''
./project10-employee-class-and-classes/employee_class_and_classes.py
A program that demonstrates inheritance by managing a list of several
employees.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-23t22:16
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.2

Changelog:
    v1.2 - 2020-11-23t22:16
        Implemented accessor and mutator methods.
        Removed place holder subclass instances.
    v1.1 - 2020-11-23t21:52
        Implemented `make` actions.
        Moved all `make` actions to employee menu,
            since they are an employee function.
        Refactored main menu to be built using subclass booleans.

    v1.0 - 2020-11-23t21:12
        Stubbed menu options.
'''

import employee                         # for employee classes
import string_list_utilities as slew    # for option_menu_apply

# number of employees to manage
N_EMPLOYEES = 10

def main():
    '''
    The main program
    '''
    # variables
    employees = ([ None ] * N_EMPLOYEES)            # list of employees
    options = (list(range(1, N_EMPLOYEES)) + [ 0 ]) # list of options
    callbacks = (( employee_menu, ) * N_EMPLOYEES)  # list of callback
                                                    #   functions of employees
    #

    # stringify the options
    slew.stringify_in(N_EMPLOYEES, options)
    options = tuple(options)

    # populate the list with employees
    for k in range(0, N_EMPLOYEES):
        employees[k] = employee.Employee()
        employees[k].set_name('#' + str(k + 1))
    # end for k in range(0, N_EMPLOYEES)

    # employees is not finalized because it may change
    # if the title of the employee changes

    # main menu
    slew.option_menu_apply(N_EMPLOYEES,\
        slew.create_legend('Employees'), ':\n',\
        options, get_employee_titled_name,\
        'Choose an employee to manage. [default STOP]',\
        callbacks, employees, '\n> ', 'Invalid employee chosen.'
    )

    # finish
    print('Done.')
# end def main()

def employee_menu(employees, index):
    '''
    The menu for all employees.
    @return True to continue the main menu
    '''
    # menu options
    N_ADDITIONAL = 3
    additional = [ None ] * N_ADDITIONAL
    options = ([ 'E', 'N', 'P' ] + additional)
    labels = ([ 'Display (E)mployee number.',
        'Change (N)ame.', 'Change em(P)loyee number.',
    ] + additional)
    callbacks = [ display_employee_no, change_employee_name, change_employee_no,
        slew.false2, slew.false2, slew.false2 ]
    n_options = (len(options) - N_ADDITIONAL)

    # data is bound employees and index
    data = { 'employees' : employees, 'index' : index }

    # instance data
    is_production_worker = False
    is_shift_supervisor = False

    # initialize instance data
    if (isinstance(employees[index], employee.ProductionWorker)):
        is_production_worker = True
    elif (isinstance(employees[index], employee.ShiftSupervisor)):
        is_shift_supervisor = True
    # end if (isinstance(employees[index], employee.ProductionWorker))
    #   elif (isinstance(employees[index], employee.ShiftSupervisor))

    # add the remaining options according to type

    # submenus
    if (is_production_worker):
        options[n_options] = 'K'
        labels[n_options] = 'Production wor(K)er menu . . .'
        callbacks[n_options] = production_worker_menu
        n_options += 1
    elif (is_shift_supervisor):
        options[n_options] = 'F'
        labels[n_options] = 'Shi(F)t supervisor menu . . .'
        callbacks[n_options] = shift_supervisor_menu
        n_options += 1
    # end if (is_production_worker) elif (is_shift_supervisor)

    # if either subclass, add make employee
    if (is_production_worker or is_shift_supervisor):
        options[n_options] = 'L'
        labels[n_options] = 'Make an emp(L)oyee.'
        callbacks[n_options] = make_employee
        n_options += 1
    # end if (is_production_worker or is_shift_supervisor):

    # add make {subclass} if not {subclass}
    if (not(is_production_worker)):
        options[n_options] = 'I'
        labels[n_options] = 'Make a product(I)on worker.'
        callbacks[n_options] = make_production_worker
        n_options += 1
    # end if (not(is_production_worker))
    if (not(is_shift_supervisor)):
        options[n_options] = 'T'
        labels[n_options] = 'Make a shif(T) supervisor.'
        callbacks[n_options] = make_shift_supervisor
        n_options += 1
    # end if (not(is_shift_supervisor))

    # finalize for menu
    options = tuple(options)
    labels = tuple(labels)
    callbacks = tuple(callbacks)

    slew.option_menu_apply(n_options,\
        slew.create_callable_from_callback(get_employee_titled_name,\
            employees, index), ' (Employee menu):\n',\
        options, slew.create_label_from_strings(labels),\
        'Choose an action. [default to main]',\
        callbacks, data, '\n> ', 'Invalid action chosen.'
    )

    # continue main menu
    return True
# end def employee_menu(employees, index)

def production_worker_menu(data, i_action):
    '''
    The menu for all production workers.
    @return True to continue the employee menu
    '''
    options = ( 'S', 'P', 'G', 'N', 'E' )
    labels = ( 'Display (S)hift.', 'Display (P)ay rate.',\
        'Calculate (G)ross pay.',\
        'Change shift (N)umber.', 'Change pay rat(E).' )
    callbacks = ( display_prodn_worker_shift,\
        display_prodn_worker_pay_rate,\
        calculate_prodn_worker_gross_pay,\
        change_prodn_worker_shift_number, change_prodn_worker_pay_rate
    )
    # count the options
    n_options = len(options)

    slew.option_menu_apply(n_options,\
        slew.create_callable_from_callback(get_employee_titled_name,\
            data['employees'], data['index']),\
        ' (Production worker menu):\n',\
        options, slew.create_label_from_strings(labels),\
        'Choose an action. [default to main]',\
        callbacks, data, '\n> ', 'Invalid action chosen.'
    )

    # continue employee menu
    return True
# end def production_worker_menu(data, index)

def shift_supervisor_menu(data, index):
    '''
    The menu for all shift supervisor.
    @return True to continue the employee menu
    '''
    options = ( 'S', 'N', 'R', 'G' )
    labels = ( 'Display (S)alary.', 'Display bo(N)us.',\
        'Change sala(R)y.', 'Chan(G)e bonus.' )
    callbacks = ( display_shift_supvsr_salary, display_shift_supvsr_bonus,\
        change_shift_supvsr_salary, change_shift_supvsr_bonus
    )
    # count the options
    n_options = len(options)

    slew.option_menu_apply(n_options,\
        slew.create_callable_from_callback(get_employee_titled_name,\
            data['employees'], data['index']),\
        ' (Shift supervisor menu):\n',\
        options, slew.create_label_from_strings(labels),\
        'Choose an action. [default to main]',\
        callbacks, data, '\n> ', 'Invalid action chosen.'
    )

    # continue employee menu
    return True
# def shift_supervisor_menu(data, index)

def get_employee_titled_name(employees, index):
    '''
    @return the title and name of `employees[index]`
    '''
    # find the employee's title
    title = ''
    if (isinstance(employees[index], employee.ProductionWorker)):
        title = 'Production worker'
    elif (isinstance(employees[index], employee.ShiftSupervisor)):
        title = 'Shift supervisor'
    else:
        title = 'Employee'
    # end if (isinstance(employees[index], employee.ProductionWorker))
    #   elif (isinstance(employees[index], employee.ShiftSupervisor)) else

    # return the result
    return (title + ' ' + employees[index].get_name())
# end def get_employee_titled_name(employees, index)

# stubs of menu options
def make_employee(data, i_action):
    '''
    Create an employee out of the employee specified by data.
    @return False to fall back to the main menu
    '''
    employees = data['employees']
    index = data['index']
    old_employee = employees[index]
    employees[index] = employee.Employee()
    employees[index].set_name(old_employee.get_name())
    employees[index].set_employee_no(old_employee.get_employee_no())
    # tell the user
    print('Update:', get_employee_titled_name(employees, index), end='')
    print(' is now an employee.')
    print()
    return False
# end def make_employee(data, i_action)
    

def make_production_worker(data, i_action):
    '''
    Create a production worker out of the employee specified by data.
    @return False to fall back to the main menu
    '''
    employees = data['employees']
    index = data['index']
    old_employee = employees[index]
    employees[index] = employee.ProductionWorker()
    employees[index].set_name(old_employee.get_name())
    employees[index].set_employee_no(old_employee.get_employee_no())
    # tell the user
    print('Update:', get_employee_titled_name(employees, index), end='')
    print(' is now a production worker.')
    print()
    return False
# end def make_production_worker(data, i_action)

def make_shift_supervisor(data, i_action):
    '''
    Create a shift supervisor out of the employee specified by data.
    @return False to fall back to the main menu
    '''
    employees = data['employees']
    index = data['index']
    old_employee = employees[index]
    employees[index] = employee.ShiftSupervisor()
    employees[index].set_name(old_employee.get_name())
    employees[index].set_employee_no(old_employee.get_employee_no())
    # tell the user
    print('Update:', get_employee_titled_name(employees, index), end='')
    print(' is now a shift supervisor.')
    print()
    return False
# end def make_production_worker(data, i_action)

# employee functions

def display_employee_no(data, i_action):
    '''
    Displays the employee number of the employee specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    print(get_employee_titled_name(employees, index), "'s", sep='', end='')
    print(' employee number is ', end='')
    print(employees[index].get_employee_no(), '.', sep='')
    print()
    return True
# end def display_employee_no(data, i_action):

def change_employee_name(data, i_action):
    '''
    Changes the name of the employee specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    old_titled_name = get_employee_titled_name(employees, index)
    print('What is ', old_titled_name, "'s", ' new name?', sep='')
    name = input('> ')
    employees[index].set_name(name)
    # tell the user
    print('Update:', old_titled_name, 'renamed to ', end='')
    print(employees[index].get_name(), '.', sep='')
    print()
    return True
# end def change_employee_name(data, i_action):

def change_employee_no(data, i_action):
    '''
    Changes the employee number of the employee specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print('What is ', titled_name, "'s", ' new employee number?', sep='')
    employee_no = input('> ')
    employees[index].set_employee_no(employee_no)
    # tell the user
    print('Update: ', end='')
    return display_employee_no(data, i_action)
# end def change_employee_no(data, i_action):

# production worker functions

def display_prodn_worker_shift(data, i_action):
    '''
    Displays the shift number of the production worker specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print(titled_name, "'s", ' shift is at ',  sep='', end='')
    print(employees[index].get_shift(), 'time.')
    print()
    return True
# end def display_prodn_worker_shift(data, i_action):

def display_prodn_worker_pay_rate(data, i_action):
    '''
    Displays the pay rate of the production worker specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print(titled_name, "'s", ' pay rate is $', sep='', end='')
    print(employees[index].get_pay_rate(), '/hr.', sep='')
    print()
    return True
# end def display_prodn_worker_pay_rate(data, i_action):

def calculate_prodn_worker_gross_pay(data, i_action):
    '''
    Calculates and displays the gross pay of the production worker
    specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print('How many hours did', titled_name, 'work this week?')
    hours = int(input('> '))
    gross_pay = employees[index].calc_gross_pay(hours)
    print(titled_name, ' earned $', gross_pay, ' this week.', sep='')
    print()
    return True
# end def calculate_prodn_worker_gross_pay(data, i_action):

def change_prodn_worker_shift_number(data, i_action):
    '''
    Changes the shift number of the production worker specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print('What is ', titled_name, "'s", ' new shift?', sep='')
    for k in employee.ProductionWorker.VALID_SHIFT_NOS:
        print('\t(', k, ') ', employee.ProductionWorker.SHIFTS[k], sep='')
    # end for k
    try:
        shift_no = int(input('> '))
    except ValueError:
        print('Error: The shift number must be an integer.')
        return True
    # end except ValueError

    # stop on error
    if (employees[index].set_shift_no(shift_no)):
        print()
        return True
    # if (employees[index].set_shift_no(shift_no))
    # otherwise, tell the user
    print('Update: ', end='')
    return display_prodn_worker_shift(data, i_action)
# end def change_prodn_worker_shift_number(data, i_action):

def change_prodn_worker_pay_rate(data, i_action):
    '''
    Changes the pay rate of the production worker specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print('What is ', titled_name, "'s", ' new pay rate?', sep='')
    pay_rate = input('> ')

    # validate
    try:
        employees[index].set_pay_rate(pay_rate)
    except ValueError:
        print('Error: The pay rate must be a float.')
        return True
    # end except ValueError

    # tell the user
    print('Update: ', end='')
    return display_prodn_worker_pay_rate(data, i_action)
# end def change_prodn_worker_pay_rate(data, i_action):

# shift supervisor functions

def display_shift_supvsr_salary(data, i_action):
    '''
    Calculates and displays the salary of the shift supervisor
    specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)

    salary = ''
    print('Did ', titled_name, "'s", sep='', end='')
    print(' shift meet production goals?[YN]')
    choice = input('> ')
    if (choice == 'Y'):
        salary = employees[index].get_salary_plus_bonus()
    elif (choice == 'N'):
        salary = employees[index].get_salary()
    else:
        print('Error: Must choose Y or N.')
        return True

    print(titled_name, ' earned $', salary, ' this year.', sep='')
    print()
    return True
# end def display_shift_supvsr_salary(data, i_action):

def display_shift_supvsr_bonus(data, i_action):
    '''
    Displays the annual production bonus of the shift supervisor
    specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print(titled_name, 'may earn an annual production bonus of ', end='')
    print(employees[index].get_bonus(), 'this year.')
    print()
    return True
# end def display_shift_supvsr_bonus(data, i_action):

def change_shift_supvsr_salary(data, i_action):
    '''
    Changes the annual salary of the shift supervisor specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print('What is ', titled_name, "'s", ' new annual salary?', sep='')
    salary = input('> ')

    # validate
    try:
        employees[index].set_salary(salary)
    except ValueError:
        print('Error: The annual salary must be a float.')
        return True
    # end except ValueError

    # tell the user
    print('Update: ', end='')
    print(titled_name, "'s", ' new annual salary is $', salary, '.', sep='')
    print()
    return True
# end def change_shift_supvsr_salary(data, i_action):

def change_shift_supvsr_bonus(data, i_action):
    '''
    Changes the annual production bonus of the shift supervisor
    specified by `data`.
    @return True to continue in current menu
    '''
    employees = data['employees']
    index = data['index']
    titled_name = get_employee_titled_name(employees, index)
    print('What is ', titled_name, "'s", sep='', end='')
    print(' new annual production bonus?')
    salary = input('> ')

    # validate
    try:
        employees[index].set_bonus(salary)
    except ValueError:
        print('Error: The annual production bonus must be a float.')
        return True
    # end except ValueError

    # tell the user
    print('Update: ', end='')
    return display_shift_supvsr_bonus(data, i_action)
# end def change_prodn_worker_pay_rate(data, i_action):

# start
main()
