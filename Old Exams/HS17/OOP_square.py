# define Square here
from OOP_circle_rect import Rectangle
class Square(Rectangle):
    def __init__(self, width):
        self.__width = width
        self.__height = self.__width

    def area(self):
        super().area()
assert Square(5).description() == "Square with area 25"
assert Square(5).area() == 25