#!/usr/bin/python3

class Square:
    """Object representation of a square."""

    def __init__(self, size=0):
        """
        Initialization of a square.

        Args:
            size (int): size of the square.
        """

        if size > 0:
            if isinstance(size, int):
                self.__size = size
            else:
                raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Retrieving size of square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set size to value

        Args:
            value (int): new value for size.
        """
        if value > 0:
            if isinstance(value, int):
                self.__size = value
            else:
                raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """get area of square."""
        return (int(self.__size) * int(self.__size))
