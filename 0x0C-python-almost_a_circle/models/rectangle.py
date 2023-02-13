#!/usr/bin/python3

from base import Base

"""Class representing a rectangle"""

class Rectangle(Base):
    
    def __init__(self, width, height, x=0, y=0, id=None):
        
        """
        Object representation of a square

        Args:

            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x coordinate
            y (int): y coordinate
        """
        super().__init__(self, id)

        if isinstance(width, int):
            if (width > 0):
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")
        
        if isinstance(height, int):
            if (height > 0):
                self.__height = height
            else:
                raise ValueError('height must be > 0')
        else:
            raise TypeError("height must be an integer")
        
        if isinstance(x, int):
            if (x >= 0):
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")
        
        if isinstance(y, int):
            if (y >= 0):
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    @property
    def x(self):
        """getter method for x"""
        return self.__x
    
    @x.setter
    def x(self, value: int):
        """Setter method for x"""
        if isinstance(value, int):
            if (value >= 0):
                self.__x = value
            else:
                raise ValueError("value must be >= 0")
        else:
            raise TypeError("value must be an integer")
    
    @property
    def y(self):
        """Getter method for y"""
        return self.__y
    
    @y.setter
    def y(self, value: int):
        """Setter method for y"""
        if isinstance(value, int):
            if (value >= 0):
                self.__y = value
            else:
                raise ValueError("value must be >= 0")
        else:
            raise TypeError("value must be an integer")

    @property
    def width(self):
        """Getter method for width"""
        return self.__width
    
    @width.setter
    def width(self, value: int):
        """Setter method for width"""
        if isinstance(value, int):
            if (value > 0):
                self.__width = value
            else:
                raise ValueError("value must be > 0")
        else:
            raise TypeError("value must be an integer")
        
    @property
    def height(self):
        """Getter method for height"""
        return self.__height
    
    @height.setter
    def height(self, value: int):
        """Setter method for height"""
        if isinstance(value, int):
            if (value > 0):
                self.__height = value
            else:
                raise ValueError("value must be > 0")
        else:
            raise TypeError("value must be an integer")
        
    def area(self):
        """Calculates the area of the rectangle"""

        return self.__height * self.__width
    
    def display(self):
        """Displays the rectangle using # to stdout"""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """String representation of rectangle info"""

        return f"[Rectangle] ({self.id}) <{self.__x}>/<{self.y}> - <{self.__width}>/<{self.__height}>"
    