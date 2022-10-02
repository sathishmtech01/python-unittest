import unittest
import math

from shapes.circle import Circle
from shapes.shape import Shape


class TestCircle(unittest.TestCase):
    def test_circle_instance_of_shape(self):
        circle = Circle(10)
        self.assertIsInstance(circle, Shape)

    def test_create_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(-1)

    def test_area(self):
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.area(), math.pi * 2.5*2.5)

    # newly added for perimeter code coverage 100%
    def test_perimeter(self):
        circle = Circle(2.5)
        self.assertAlmostEqual(circle.perimeter(), math.pi * 2.5*2)