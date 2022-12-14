# define Rectangle and Circle here
from OOP_Shape import Shape
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return self.__radius**2*3


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width*self.__height
assert Rectangle(2, 5).description() == "Rectangle with area 10"
assert Rectangle(2, 5).area() == 10
assert Circle(5).description() == "Circle with area 75" # Pi=3! assert Circle(5).area() == 75