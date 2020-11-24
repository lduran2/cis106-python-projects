'''
./project10-employee-class-and-classes/employee_class_and_classes.py
A program that demonstrates inheritance by managing a list of several
employees.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-22t11:48
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    v1.0 - 2020-11-22t11:48
        Implemented ./employee_class_and_classes.py
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
        # 1 - production worker, 2 - shift supervisor ; for testing
        if (k == 1):
            employees[1] = employee.ProductionWorker()
        if (k == 2):
            employees[2] = employee.ShiftSupervisor()
        employees[k].set_name('#' + str(k + 1))
    # end for k in range(0, N_EMPLOYEES)
    employees = tuple(employees)

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
    options = [ 'E', 'N', 'P' ]
    labels = [ 'Display (E)mployee number.', 'Change (N)ame.', 'Change em(P)loyee number.' ]
    callbacks = [ display_employee_no, change_employee_name, change_employee_no ]

    # data is bound employees and index
    data = { 'employees' : employees, 'index' : index }

    # add the remaining options according to type
    if (isinstance(employees[index], employee.ProductionWorker)):
        options += [ 'K', 'T' ]
        labels += [ 'Production wor(K)er menu', 'Make a shif(T) supervisor.' ]
        callbacks += [ production_worker_menu, make_shift_supervisor ]
    elif (isinstance(employees[index], employee.ShiftSupervisor)):
        options += [ 'F', 'I' ]
        labels += [ 'Shi(F)t supervisor menu', 'Make a product(I)on worker.' ]
        callbacks += [ shift_supervisor_menu, make_production_worker ]
    else:
        options += [ 'I', 'T' ]
        labels += [ 'Make a product(I)on worker.', 'Make a shif(T) supervisor.' ]
        callbacks += [ make_production_worker, make_shift_supervisor ]
    # end if (isinstance(employees[index], employee.ProductionWorker))
    #   elif (isinstance(employees[index], employee.ShiftSupervisor)) else

    # finalize for menu
    options = tuple(options)
    labels = tuple(labels)
    callbacks = tuple(callbacks)
    n_options = len(options)

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
    options = ( 'S', 'P', 'G', 'N', 'E', 'T', 'L' )
    labels = ( 'Display (S)hift number.', 'Display (P)ay rate.',\
        'Calculate (G)ross pay.',\
        'Change shift (N)umber.', 'Change pay rat(E).',\
        'Make a shif(T) supervisor.', 'Make an emp(L)oyee' )
    callbacks = ( display_prodn_worker_shift_number,\
        display_prodn_worker_pay_rate,\
        calculate_prodn_worker_gross_pay,\
        change_prodn_worker_shift_number, change_prodn_worker_pay_rate,\
        make_shift_supervisor, make_employee
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
    options = ( 'S', 'N', 'P', 'R', 'G', 'I', 'L' )
    labels = ( 'Display (S)alary.', 'Display bo(N)us.',\
        'Display salary if (P)roduction goals are met.',\
        'Change sala(R)y.', 'Chan(G)e bonus.',\
        'Make a product(I)on worker.', 'Make an emp(L)oyee' )
    callbacks = ( display_shift_supvsr_salary, display_shift_supvsr_bonus,\
        display_shift_supvsr_salary_plus_bonus,\
        change_shift_supvsr_salary, change_shift_supvsr_bonus,\
        make_production_worker, make_employee
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
    pass

def make_production_worker(data, i_action):
    pass

def make_shift_supervisor(data, i_action):
    pass

def display_employee_no(data, i_action):
    pass

def change_employee_name(data, i_action):
    pass

def change_employee_no(data, i_action):
    pass

def display_prodn_worker_shift_number(data, i_action):
    pass

def display_prodn_worker_pay_rate(data, i_action):
    pass

def calculate_prodn_worker_gross_pay(data, i_action):
    pass

def change_prodn_worker_shift_number(data, i_action):
    pass

def change_prodn_worker_pay_rate(data, i_action):
    pass

def display_shift_supvsr_salary(data, i_action):
    pass

def display_shift_supvsr_bonus(data, i_action):
    pass

def display_shift_supvsr_salary_plus_bonus(data, i_action):
    pass

def change_shift_supvsr_salary(data, i_action):
    pass

def change_shift_supvsr_bonus(data, i_action):
    pass

# start
main()
