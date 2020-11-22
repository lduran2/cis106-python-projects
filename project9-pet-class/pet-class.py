'''
./project9-pet-class/pet-class.py
A program that demonstrates classes and objects by instantiating and
mutating an object, then accessing its properties.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-22t15:02
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.1

Changelog:
    v1.1 - 2020-11-22t15:02
        Reimplementing as menu-driven.
        Used placeholder names and submenus.

    v1.0 - 2020-11-16t22:13
        Implemented ./pet-class.py
'''

# libraries
import pet                              # for the pet class
import string_list_utilities as slew    # for option_menu_apply

# number of pets to manage
N_PETS = 10

def main():
    '''
    The main program.
    '''

    # variables
    pets = [ None ] * N_PETS                    # list of pets
    options = list(range(1, N_PETS)) + [ 0 ]    # list of options
    callbacks = [ slew.false2 ] * N_PETS        # list of callback functions of pets

    # stringify the options
    slew.stringify_in(N_PETS, options)

    # populate the list with pets
    for k in range(0, N_PETS):
        pets[k] = pet.Pet()
        # placeholder names while testing
        pets[k].set_name(str(k))
    # end for k

    # main option menu
    slew.option_menu_apply(N_PETS, 'Pets:',\
        options, get_pet_name, 'Choose a pet to manage. [default STOP]',\
        callbacks, pets, '\n> ', 'Invalid pet chosen.'\
    )

    # finish
    print('Done.')
# end main()

def get_pet_name(pets, index):
    '''
    Returns the name of `pets[index]`
    @params
        pets -- list of pets
        index -- index of pet whose name to get
    '''
    return pets[index].get_name();
# end def get_pet_name()

# start
main()
