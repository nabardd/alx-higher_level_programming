#!/usr/bin/python3
"""Define a Square"""

class Square:
    """Object representation of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialization of a square.

        Args:
            size (int): size of the square.
            position (tuple): position of the square
        """

        if size > 0:
            if isinstance(size, int):
                self.__size = size
            else:
                raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")

        if (
            not isinstance(position, tuple) or
            len(position) != 2 or
            not all(isinstance(x, int) for x in position) or
            not all(num >= 0 for num in position)
        ):
            raise TypeError("Position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Retrieving coordinates for square"""

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setting position to value

        Args:
            value (tuple): new position coordinates
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(x, int) for x in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("Position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """get area of square."""
        return (int(self.__size) * int(self.__size))

    def my_print(self):
        """Print square using # character"""
        if self.__size == 0:
            print()
        else:
            [print(" ") for y in self.__position[1]]
            for i in range(self.__size):
                [print(" ", end="") for k in range(self.__position[0])]
                [print("#", end="") for n in range(self.__size)]
                print("")
