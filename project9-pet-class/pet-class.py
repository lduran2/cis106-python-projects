'''
./project9-pet-class/pet-class.py
A program that demonstrates classes and objects by instantiating and
mutating an object, then accessing its properties.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-16t22:13
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.0

Changelog:
    v1.0 - 2020-11-16t22:13
        Implemented ./pet-class.py
'''

# import the pet class
import pet

def main():
    '''
    The main program.
    '''

    # variables
    name = ''           # name of the pet
    animal_type = ''    # type of the pet
    age = 0             # age of the pet

    # Create the pet.
    my_pet = pet.Pet()

    # Accept the name from the user.
    print('Please enter the name of your pet.')
    name = input('> ')
    my_pet.set_name(name)

    # Accept the animal type from the user.
    print('Please enter the type of animal that your pet is.')
    animal_type = input('> ')
    my_pet.set_animal_type(animal_type)

    # Accept the age from the user.
    print('Please enter the age of your pet.')
    age = int(input('> '))
    my_pet.set_age(age)

    # Display the result
    print('Your pet\'s file:')
    print('Name       :\t', my_pet.get_name())
    print('Animal type:\t', my_pet.get_animal_type())
    print('Age        :\t', my_pet.get_age())

    # finish
    print('Done.')
# end main()

main()
