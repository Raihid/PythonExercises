#!/usr/bin/python
from math import sin
import unittest
from points import Point

class Triangle:
    """
        Class representing a triaangle on a plane.
    """

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        return "["  + str(self.pt1) + ", " +  str(self.pt2) + ", " + \
                str(self.pt3) + "]"

    def __repr__(self):
        return "Triangle(" +  str(self.pt1.x) +  ", " +  str(self.pt1.y) + \
                ", " +  str(self.pt2.x) +  ", " +  str(self.pt2.y) + ", " + \
                str(self.pt3.x) + ", " + str(self.pt3.y) + ")"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3.0,
                     (self.pt1.y + self.pt2.y + self.pt3.y) / 3.0)

    def area(self):
        return abs((self.pt1.x * (self.pt2.y - self.pt3.y) +
                self.pt2.x * (self.pt3.y - self.pt1.y) +
                self.pt3.x * (self.pt1.y - self.pt2.y)) / 2.0)

    def move(self, x, y):
        self.pt1 += Point(x, y)
        self.pt2 += Point(x, y)
        self.pt3 += Point(x, y)

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(0, 0, 1, 0, 0, 1)
        self.t2 = Triangle(0, 0, 2, 2, 4, 4)
        self.t3 = Triangle(0, 0, 0, 0, 0, 0)
        self.t4 = Triangle(-2, 0, 2, 0, 4, 4)
        self.t5 = Triangle(-8, -3, 0, 0, 5, 0)
        self.t6 = Triangle(-5, -5, 5, 5, 2.5, -2.5)
        self.t7 = Triangle(2.25, 3.15, 4.25, 10.25, -2.0, -12.5)

    def test_str(self):
        self.assertEqual(str(self.t1), "[(0, 0), (1, 0), (0, 1)]")
        self.assertEqual(str(self.t2), "[(0, 0), (2, 2), (4, 4)]")
        self.assertEqual(str(self.t3), "[(0, 0), (0, 0), (0, 0)]")
        self.assertEqual(str(self.t4), "[(-2, 0), (2, 0), (4, 4)]")

    def test_repr(self):
        self.assertEqual(repr(self.t1), "Triangle(0, 0, 1, 0, 0, 1)")
        self.assertEqual(repr(self.t2), "Triangle(0, 0, 2, 2, 4, 4)")
        self.assertEqual(repr(self.t3), "Triangle(0, 0, 0, 0, 0, 0)")
        self.assertEqual(repr(self.t4), "Triangle(-2, 0, 2, 0, 4, 4)")

    def test_equals(self):
        self.assertTrue(self.t1 == self.t1)
        self.assertTrue(self.t2 == self.t2)
        self.assertTrue(self.t3 == Triangle(0, 0, 0, 0, 0, 0))
        self.assertFalse(self.t1 == self.t2)
        self.assertFalse(self.t5 == Triangle(-5, -5, -4, -4, 0, 1))

    def test_not_equals(self):
        self.assertFalse(self.t1 != self.t1)
        self.assertFalse(self.t2 != self.t2)
        self.assertFalse(self.t3 != Triangle(0, 0, 0, 0, 0, 0))
        self.assertTrue(self.t1 != self.t2)
        self.assertTrue(self.t5 != Triangle(-5, -5, -4, -4, 0, 1))

    def test_center(self):
        self.assertEqual(self.t1.center(), Point(1.0/3.0, 1.0/3.0))
        self.assertEqual(self.t4.center(), Point(4.0/3.0, 4.0/3.0))
        self.assertEqual(self.t5.center(), Point(-1, -1))

    def test_area(self):
        self.assertEqual(self.t1.area(), 0.5)
        self.assertEqual(self.t2.area(), 0)
        self.assertEqual(self.t4.area(), 8)
        self.assertEqual(self.t6.area(), 25)

    def test_move(self):
        self.t1.move(3, 3)
        self.assertTrue(self.t1 == Triangle(3, 3, 4, 3, 3, 4))
        self.t2.move(6, -1)
        self.assertTrue(self.t2 == Triangle(6, -1, 8, 1, 10, 3))
        self.t7.move(8.5, 0)
        self.assertTrue(self.t7 == Triangle(10.75, 3.15, 12.75, 10.25, 6.5, -12.5))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()



