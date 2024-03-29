#!/usr/bin/python3
"""Define a Square"""


class Square:
    """
    Object representation of a class
    """

    def __init__(self, size=0):
        """
        Initialization for square

        Args:
            size (int): size of square.
        """
        if size >= 0:
            if isinstance(size, int):
                self.__size = size
            else:
                raise TypeError("size must be an integer")
        else:
            raise ValueError("size must be >= 0")
