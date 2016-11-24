#!/usr/bin/python
from math import pi
from math import sqrt
from points import Point

class Circle:
    """A class representing a circle on a plane"""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle(" + str(self.pt.x) + ", " + str(self.pt.y) + ", " + str(self.radius) + ")"

    __str__ = __repr__

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return pi*self.radius*self.radius

    def move(self, x, y):     # przesuniecie o (x, y)
        self.pt += Point(x, y)

    def cover(self, other):   # todo: prawdopodobnie działa, ale testy
        c1, c2 = sorted([self, other], key = lambda item: item.radius)

        distance = sqrt((c1.pt.x - c2.pt.x) ** 2 + (c1.pt.y - c2.pt.y) ** 2)
        if(distance + c1.radius <= c2.radius):
            return c2
        final_radius = (distance + c1.radius + c2.radius)/2.0
        alpha = 1.0/2.0 + (c2.radius - c1.radius)/(2.0*distance)
        center = Point((1-alpha)*c1.pt.x + alpha*c2.pt.x,
                       (1-alpha)*c1.pt.y + alpha*c2.pt.y)
        return Circle(center.x, center.y, final_radius)



# Kod testujacy modul.

import unittest

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.c1 = Circle(0, 0, 5)
        self.c2 = Circle(2, 2, 3)
        self.c3 = Circle(0, 5, 3.5)
        self.c4 = Circle(1, 2, 1.5)
        self.c5 = Circle(3, 0.5, 6)
        self.c6 = Circle(-2.5, -1.25, 5)
        self.c7 = Circle(-3, 0, 2.2)
        self.c8 = Circle(-8, 2, 0)
        self.c9 = Circle(-2, -2, 0)
        self.c10 = Circle(10, 10, 5)

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(0, 0, 5)")
        self.assertEqual(repr(self.c2), "Circle(2, 2, 3)")
        self.assertEqual(repr(self.c3), "Circle(0, 5, 3.5)")
        self.assertEqual(repr(self.c4), "Circle(1, 2, 1.5)")

    def test_equals(self):
        self.assertTrue(self.c1 == self.c1)
        self.assertTrue(self.c2 == Circle(2.0, 2.0, 3.0))
        self.assertTrue(self.c6 == Circle(-2.5, -1.25, 5))
        self.assertFalse(self.c2 == self.c3)
        self.assertFalse(self.c5 == Circle(0, 0, 5))

    def test_not_equals(self):
        self.assertFalse(self.c1 != self.c1)
        self.assertFalse(self.c2 != Circle(2.0, 2.0, 3.0))
        self.assertFalse(self.c6 != Circle(-2.5, -1.25, 5))
        self.assertTrue(self.c2 != self.c3)
        self.assertTrue(self.c5 != Circle(0, 0, 5))

    def test_area(self):
        self.assertEqual(self.c1.area(), 5*5*pi)
        self.assertEqual(self.c8.area(), 0)
        self.assertEqual(self.c3.area(), 3.5*3.5*pi)

    def test_move(self):
        self.c1.move(3, 3)
        self.assertTrue(self.c1 == Circle(3, 3, 5))
        self.c2.move(6, -1)
        self.assertTrue(self.c2 == Circle(8, 1, 3))
        self.c7.move(8.5, 0)
        self.assertTrue(self.c7 == Circle(5.5, 0, 2.2))

    def test_cover(self):
        self.assertEqual(self.c1.cover(self.c9), self.c1)
        self.assertEqual(self.c1.cover(self.c3), Circle(0, 1.75, 6.75))
        self.assertEqual(self.c1.cover(self.c10), Circle(3, 0.5, 6))



    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()
