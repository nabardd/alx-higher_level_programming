class Square:

  def __init__(self, height="0", width="0"):
    self.height = height
    self.width = width

  @property
  def height(self):
    print("Retrieving the height")

    return self.__height
  
  @height.setter
  def height(self, value):
    if isinstance(value, int):
      self.__height = value
    else:
      print("Please only enter numbers for height")

  @property
  def width(self):
    print("Retrieving the width")

    return (self.__width)
  
  @width.setter
  def width(self, value):

    if isinstance(value, int):
      self.__width = value
    else:
      print("Please only enter numbers for height")

  def getArea(self):
    return int(self.__width) * int(self.__height)
  
def main():
  aSquare = Square()