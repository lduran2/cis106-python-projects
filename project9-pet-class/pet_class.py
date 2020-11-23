'''
./project9-pet-class/pet-class.py
A program that demonstrates classes and objects by instantiating and
mutating an object, then accessing its properties.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-22t18:44
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.3

Changelog:
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
    pets = [ None ] * N_PETS                    # list of pets
    options = list(range(1, N_PETS)) + [ 0 ]    # list of options
    callbacks = [ pet_menu ] * N_PETS           # list of callback
                                                #   functions of pets

    # stringify the options
    slew.stringify_in(N_PETS, options)

    # populate the list with pets
    for k in range(0, N_PETS):
        pets[k] = pet.Pet()
        # placeholder name before proper naming
        pets[k].set_name('Pet #' + str(k + 1))
    # end for k

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
    options = [ 'L', 'A', 'N', 'T', 'E' ]
    labels = [ 'Display animal type.', 'Display age.',\
        'Change name.', 'Change animal type.', 'Change age.'\
    ]
    callbacks = [ display_pet_type, display_pet_age,\
        change_pet_name, change_pet_type, change_pet_age\
    ]
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
        print(name, 'is a', (animal_type + '.'))
    # end if (animal_type == '')
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
    print('Please enter the new name of', (name + '.'))
    new_name = input('> ')
    # set the new name
    a_pet.set_name(new_name)
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
    print('Please enter the new type of animal of', (name + '.'))
    animal_type = input('> ')
    # set the new type of animal
    a_pet.set_animal_type(animal_type)
    # continue pet menu
    return True
# end def display_pet_type(a_pet, i_action)

def change_pet_age(a_pet, index):
    '''
    Changes the age of the pet `a_pet`.
    @params
        a_pet -- the pet to manage
        i_action -- index of this action in the pet menu (unused)
    '''
    name = a_pet.get_name() # name of the pet
    # ask for the new length of age
    print('Please enter the new length of age of', (name + '.'))
    age = int(input('> '))
    # set the new length of age
    a_pet.set_age(age)
    # continue pet menu
    return True
# end def display_pet_age(a_pet, i_action)

# start
main()
