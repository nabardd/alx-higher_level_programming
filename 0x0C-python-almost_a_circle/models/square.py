#!/usr/bin/python3

from rectangle import Rectangle

"""Object representation of rectangle"""
class Square(Rectangle):
    
    def __init__(self, size: int, x=0 , y=0, id=None):
        """
        Square Representation

        Args:
            size (int): size of the rectangle
            x (int): coordinates for x-axis
            y (int): coordinates for y-axis
            id (int): identifier for each class instance
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return (
            f"[Square] (<{self.id}>) <{self.x}>/<{self.y}> - <{self.width}>"
        )
    
    @property
    def size(self):
        """Get square size"""
        return self.size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if (value > 0):
                self.width = value
                self.height = value
            else:
                raise ValueError("value must be > 0")
        else:
            raise TypeError("value must be an integer")
        
    def update(self, *args, **kwargs):
        """update square that assigns attributes to args"""
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(
                                self.width, self.width, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                    self.height = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(
                                    self.width, self.width, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "size":
                        self.width = value
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

        def to_dictionary(self):
            """returns dictionary representation
            of a square"""
            return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}