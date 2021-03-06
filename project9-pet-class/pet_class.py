'''
./project9-pet-class/pet-class.py
A program that demonstrates classes and objects by instantiating and
mutating an object, then accessing its properties.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-22t21:10
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.4

Changelog:
    v1.4 - 2020-11-22t21:10
        Made a little more user friendly.

    v1.3 - 2020-11-22t18:44
        Renamed to ./pet_class.py for use in ./notebook.ipynb

    v1.2 - 2020-11-22t18:18
        Finished ./pet-class.py and refactored `slew.option_menu`
            accordingly.

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
    pets = ([ None ] * N_PETS)                  # list of pets
    options = (list(range(1, N_PETS)) + [ 0 ])  # list of options
    callbacks = (( pet_menu, ) * N_PETS)        # list of callback
                                                #   functions of pets

    # stringify the options
    slew.stringify_in(N_PETS, options)
    options = tuple(options)

    # populate the list with pets
    for k in range(0, N_PETS):
        pets[k] = pet.Pet()
        # placeholder name before proper naming
        pets[k].set_name('Pet #' + str(k + 1))
    # end for k
    pets = tuple(pets)

    # main option menu
    slew.option_menu_apply(N_PETS, slew.create_legend('Pets:'), '',\
        options, get_pet_name, 'Choose a pet to manage. [default STOP]',\
        callbacks, pets, '\n> ', 'Invalid pet chosen.'\
    )

    # finish
    print('Done.')
# end main()

def pet_menu(pets, index):
    a_pet = pets[index]
    # menu parameters
    legend = (get_pet_name(pets, index) + ':\n')
    options = ( 'L', 'A', 'N', 'T', 'E' )
    labels = ( 'Display animal type.', 'Display age.',\
        'Change name.', 'Change animal type.', 'Change age.'\
    )
    callbacks = ( display_pet_type, display_pet_age,\
        change_pet_name, change_pet_type, change_pet_age\
    )
    n_options = len(options)    # count number of options

    # the index here represents the action number, not pet number
    slew.option_menu_apply(n_options, a_pet.get_name, ':\n',\
        options, slew.create_label_from_strings(labels),\
        'Choose an action. [default back to main]',\
        callbacks, a_pet, '\n> ', 'Invalid action.'\
    )

    # continue main menu
    return True
# end def pet_menu(pets, index)

def get_pet_name(pets, index):
    '''
    Returns the name of `pets[index]`
    @params
        pets -- list of pets
        index -- index of pet whose name to get
    '''
    return pets[index].get_name();
# end def get_pet_name(pets, index)

def display_pet_type(a_pet, i_action):
    '''
    Displays the name and type of the pet `a_pet`.
    @params
        a_pet -- the pet to manage
        i_action -- index of this action in the pet menu (unused)
    '''
    name = a_pet.get_name()                 # name of the pet
    animal_type = a_pet.get_animal_type()   # type of the pet
    # print the animal type considering unknown type
    if (animal_type == ''):
        print(name, 'is no known type of animal.')
    else:
        print(name, end='')
        if (animal_type[0] in 'AEIOU'):
            print(' is an ', end='')
        else:
            print(' is a ', end='')
        # end if (animal_type[0] in 'AEIOU')
        print(animal_type, '.', sep='')
    # end if (animal_type == '')
    print()
    # continue pet menu
    return True
# end def display_pet_type(a_pet, i_action)

def display_pet_age(a_pet, i_action):
    '''
    Displays the name and age of the pet `a_pet`.
    @params
        a_pet -- the pet to manage
        i_action -- index of this action in the pet menu (unused)
    '''
    name = a_pet.get_name() # name of the pet
    age = a_pet.get_age()   # age of the pet
    # print the age considering unknown type
    if (age == pet.Pet.UNKNOWN_AGE):
        print(name, ' is of an unknown age.')
    else:
        print(name, 'is', age, 'years old.')
    # end if (age == '')
    print()
    # continue pet menu
    return True
# end def display_pet_age(a_pet, i_action)

def change_pet_name(a_pet, i_action):
    '''
    Changes the name of the pet `a_pet`.
    @params
        a_pet -- the pet to manage
        i_action -- index of this action in the pet menu (unused)
    '''
    name = a_pet.get_name() # name of the pet
    # ask for the new name
    print('What is the new name of', (name + '?'))
    new_name = input('> ')
    # set the new name
    a_pet.set_name(new_name)
    print('Update:', name, 'renamed to', (a_pet.get_name() + '.'))
    print()
    # continue pet menu
    return True
# end def display_pet_type(a_pet, i_action)

def change_pet_type(a_pet, i_action):
    '''
    Changes the type of the pet `a_pet`.
    @params
        a_pet -- the pet to manage
        i_action -- index of this action in the pet menu (unused)
    '''
    name = a_pet.get_name() # name of the pet
    # ask for the new type of animal
    print('What type of animal is', (name + '?'))
    animal_type = input('> ')
    # set the new type of animal
    a_pet.set_animal_type(animal_type)
    print('Update: ', end='')
    display_pet_type(a_pet, i_action)
    # continue pet menu
    return True
# end def display_pet_type(a_pet, i_action)

def change_pet_age(a_pet, i_action):
    '''
    Changes the age of the pet `a_pet`.
    @params
        a_pet -- the pet to manage
        i_action -- index of this action in the pet menu (unused)
    '''
    name = a_pet.get_name() # name of the pet
    # ask for the new length of age
    print('How old is', (name + '?'))
    # handle non-integer ages
    try:
        age = int(input('> '))
        # set the new length of age
        if (not(a_pet.set_age(age))):
            # if no error, show the update
            print('Update: ', end='')
            display_pet_age(a_pet, i_action)
        else:
            print() # the error is already printed
        # end if (not(a_pet.set_age(age))) else
    except ValueError:
        print('Error: `age` is not an integer.')
        print()
    # end except ValueError
    # continue pet menu
    return True
# end def display_pet_age(a_pet, i_action)

# start
main()
