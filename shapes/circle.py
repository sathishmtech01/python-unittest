import math
from .shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            raise ValueError('The radius cannot be negative')

        self._radius = radius

    def area(self):
        return math.pi * math.pow(self._radius, 2)
    def perimeter(self):
        return 2 * math.pi * self._radius

# if __name__ == '__main__':
#     circle = Circle(2.5)
#     print(circle.perimeter())