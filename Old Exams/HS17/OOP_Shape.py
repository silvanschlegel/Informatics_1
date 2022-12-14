# define Shape here
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    def description(self):
        return f'{type(self).__name__} with area {self.area()}'

assert Shape().description() == "Shape with area 0"
assert Shape().area() == 0