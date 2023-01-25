#!/usr/bin/python3

class Square:
    """Object representation of a class"""

    def __init__(self, size=0):
        """
        initialization for square

        Args:
            size (int): size of square.
        """
        if size > 0:
            if isinstance(size, int):
                self.__size = size
            else:
                raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """get area of square."""
        return (int(self.__size) * int(self.__size))
