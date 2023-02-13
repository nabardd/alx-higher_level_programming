#!/usr/bin/python3

"""Base class"""

class Base:
    
    """
    This class serves as the base for all classes
    in this project
    """
    
    def __init__(self, id=None):
        self.__nb_objects = 0

        if id is not None:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects