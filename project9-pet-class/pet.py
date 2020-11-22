'''
./project9-pet-class/pet.py
Module that manages pets.

By     : Leomar Duran <https://github.com/lduran2>
When   : 2020-11-16t23:51
Where  : Community College of Philadelphia
For    : CIS 106/Introduction to Programming
Version: 1.1

Changelog:
    v1.1 - 2020-11-16t23:51
        Fixed the last letter being cut from animal_type.

    v1.0 - 2020-11-16t22:13
        Implemented ./pet.py
'''
class Pet:
    '''
    Class for user's pets.
    '''

    UNKNOWN_AGE = -1    # pet's name is not known

    def __init__(self):
        '''
        Creates a default pet.
        @params
            self -- the pet to create
        '''
        self.__name = ''         # name of the pet
        self.__animal_type = ''  # type of animal, e.g., Dog, Cat, Bird
        self.__age = -1          # age of the pet (-1 is unknown)
    # end def __init__(self)

    def set_name(self, name):
        '''
        Renames this pet.
        @params
            self -- the pet to rename
            name : str = new name
        '''
        # name must be string
        if (isinstance(name, str)):
            self.__name = name
        else:
            print('Error: `name` is not a string.')
        # end if (isinstance(name, str))
    # end set_name(self, name)

    def set_animal_type(self, animal_type):
        '''
        Changes this pet's animal type.
        @params
            self -- the pet whose type to change
            animal_type : str = new type of animal
        '''
        # animal type must be string
        if (isinstance(animal_type, str)):
            # Get the first letter uppercase.
            self.__animal_type = animal_type[0].upper()
            # Get the rest letter lowercase.
            self.__animal_type += animal_type[1:].lower()
        else:
            print('Error: `animal_type` is not a string.')
        # end if (isinstance(animal_type, str))
    # end set_animal_type(self, animal_type)
        
    def set_age(self, age):
        '''
        Changes this pet's age.
        @params
            self -- the pet whos age to change
            age : int = new age
        '''
        # age must be a positive integer
        if (not(isinstance(age, int))):
            print('Error: `age` is not an integer.')
        elif (age < 0):
            print('Error: `age` is negative.')
        else:
            self.__age = age
        # end if (not(isinstance(age, int)))
    # end set_age(self, age)
        
    def get_name(self):
        '''
        @return this pet's name.
        '''
        return self.__name
    # end get_name(self)

    def get_animal_type(self):
        '''
        @return the type of this pet.
        '''
        return self.__animal_type
    # end get_animal_type(self)

    def get_age(self):
        '''
        @return the age of this pet.
        '''
        return self.__age
    # end get_age(self)

# end class Pet
