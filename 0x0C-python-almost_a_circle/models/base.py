#!/usr/bin/python3
'''
This is the base module
It contains one class called Base
'''


class Base():
    '''Defines a new class called Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initializes a new instance of the Base class.

        Args:
            id (int): the id of each instance of the Base class.
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
