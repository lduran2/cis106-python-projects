'''
./project10-employee-class-and-classes/employee.py
Module that manages employees.

Employee, ProductionWorker, ShiftSupervisor

All classes follow the JavaBean model.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-22t23:14
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.1

Changelog:
    v1.1 - 2020-11-22t23:14
        Fixed `calc_gross_pay`, `get_salary_plus_bonus`, which were
            returning the pay rate, the bonus, instead of expected.
        Changes `this` to `self`.

    v1.0 - 2020-11-22t11:48
        Implemented ./employee.py
'''
class Employee:
    '''
    A base class representing an employee.
    '''
    def __init__(self):
        '''
        Creates a new employee.
        '''
        self.__name = ''
        self.__employee_no = ''
    # end def __init__(self)

    def get_name(self):
        '''
        @return the name of the employee.
        '''
        return self.__name
    # end def get_name(self)

    def get_employee_no(self):
        '''
        @return the employee number of the employee.
        '''
        return self.__employee_no
    # end def get_employee_no(self)

    def set_name(self, s):
        '''
        Sets the name of the employee.
        @param
            s -- string representing the new name
        @return True if `s` is not a string, False otherwise
        '''
        # validate s
        if (isinstance(s, str)):
            self.__name = s
            return False
        else:
            print('The new name is not a string.')
            return True
        # end if (isinstance(name, str)) else
    # end def set_name(self, s)

    def set_employee_no(self, s):
        '''
        Sets the employee number of the employee.
        @param
            s -- string representing the new employee number
        @return True if `s` is not a string, False otherwise
        '''
        # validate s
        if (isinstance(s, str)):
            self.__employee_no = s
            return False
        else:
            print('The new employee number is not a string.')
            return True
        # end if (isinstance(name, str)) else
    # end def set_employee_no(self, s)
# end class Employee

class ProductionWorker(Employee):
    '''
    A subclass representing a production worker, based on the employee
    class.
    '''

    # shifts including (0 -- undeclared)
    SHIFTS = ('undeclared', 'day', 'night')
    # number of shifts + undeclared
    N_SHIFTS = len(SHIFTS)
    # valid values for shift numbers
    VALID_SHIFT_NOS = tuple(range(1, N_SHIFTS))

    def __init__(self):
        '''
        Creates a new employee.
        '''
        Employee.__init__(self) # call super constructor
        self.__shift_no = 0
        self.__pay_rate = 0.00
    # end def __init__(self)

    def get_shift(self):
        '''
        @return the shift of the production worker.
        '''
        return ProductionWorker.SHIFTS[self.__shift_no]
    # end def get_shift_no(self)

    def get_pay_rate(self):
        '''
        @return the hourly pay rate of the production worker.
        '''
        return format(self.__pay_rate, '.2f')
    # end def get_pay_rate(self)

    def calc_gross_pay(self, hours):
        '''
        @return the gross pay of the production worker given time in
            hours, `hours`
        '''
        # variables
        effective_hours = hours # the number of hours used to
                                # calculate the gross pay
        gross_pay = 0.00        # the gross pay calculated
        # hours over 40 count twice
        if (hours > 40):
            effective_hours += (hours - 40)
        # end if (hours > 40)
        # calculate the gross pay
        gross_pay = (self.__pay_rate * effective_hours)
        # format to 2 decimal places
        return format(gross_pay, '.2f')
    # end def calc_gross_pay(self, hours)

    def set_shift_no(self, i):
        '''
        Sets the name of the employee.
        @param
            i -- integer representing the shift number
        @return
            0 -- valid new shift number
            1 -- new shift number out of range
            2 -- new shift number is not an integer
        '''
        # validate i
        if (not(i in ProductionWorker.VALID_SHIFT_NOS)):
            print('The new shift number is out of range(', end='')
            print(1, ', ', ProductionWorker.N_SHIFTS, ').', sep='')
            return 1
        elif (not(isinstance(i, int))):
            print('The new shift number is not an integer.')
            return 2
        else:
            self.__shift_no = i
            return 0
        # end if (i in ProductionWorker.VALID_SHIFT_NOS) else
    # end def set_shift_no(self, i)

    def set_pay_rate(self, f):
        '''
        Sets the hourly pay rate of the production worker.
        @param
            f -- float representing the new hourly pay rate
        @throws ValueError if `f` is not floatable
        '''
        self.__pay_rate = float(f)
    # end def set_pay_rate(self, f)
# end class ProductionWorker(Employee)

class ShiftSupervisor(Employee):
    '''
    A class representing a shift supervisor, based on the employee
    class.
    '''

    def __init__(self):
        '''
        Creates a new employee.
        '''
        Employee.__init__(self) # call super constructor
        self.__salary = 0.00
        self.__bonus = 0.00
    # end def __init__(self)

    def get_salary(self):
        '''
        @return the annual salary of the shift supervisor.
        '''
        return format(self.__salary, '.2f')
    # end def get_salary(self)

    def get_bonus(self):
        '''
        @return the annual production bonus of the shift supervisor.
        '''
        return format(self.__bonus, '.2f')
    # end def get_bonus(self)

    def get_salary_plus_bonus(self):
        '''
        @return the annual salary of the shift supervisor if production goals are met.
        '''
        sum = self.__salary + self.__bonus  # the total salary
        return format(sum, '.2f')
    # end def get_salary_plus_bonus(self)

    def set_salary(self, f):
        '''
        Sets the annual salary of the shift supervisor.
        @throws ValueError if `f` is not floatable
        '''
        self.__salary = float(f)
    # end def set_salary(self, f)

    def set_bonus(self, f):
        '''
        Sets the annual production bonus of the shift supervisor.
        @throws ValueError if `f` is not floatable
        '''
        self.__bonus = float(f)
    # end def set_salary(self, f)
# class ShiftSupervisor(Employee)
