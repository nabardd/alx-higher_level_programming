#!/usr/bin/python3

from base import Base
import json

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

        for i in range(self.__y):
            print(" ")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Update the instance attributes

        Args:
        index 0 (int): id attribute
        index 1 (int): width attribute
        index 2 (int): height attribute
        index 3 (int): x attribute
        index 4 (int): y attribute
        """
        if args is not None:
            for i in range(len(args)):
                if i == 0:
                    if args[i] == None:
                        self.__init__(
                            self.height, self.width, self.x, self.y
                        )
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y == args[i]
        else:
            if kwargs or len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.height, self.x, self.y)
                        else:
                            self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def __str__(self):
        """String representation of rectangle info"""

        return f"[Rectangle] ({self.id}) <{self.__x}>/<{self.y}> - <{self.__width}>/<{self.__height}>"
    
    def to_dictionary(self):
        """returns dictionary representation
        of rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}