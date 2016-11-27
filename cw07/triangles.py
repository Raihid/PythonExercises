#!/usr/bin/python
from math import sin
import unittest
from points import Point

class Triangle:
    """
        Class representing a triangle on a plane.
    """

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        if(self.area() == 0):
            return ValueError("Punkty wspolliniowe")

    def __hash__(self):
        return hash(self.pt1) ^ hash(self.pt2) ^ hash(self.pt3)

    @staticmethod
    def from_points(pt1, pt2, pt3):
        if (not isinstance(pt1, Point) or
           not isinstance(pt2, Point) or
           not isinstance(pt3, Point)):
            raise ValueError("These are not Points!")
        return Triangle(pt1.x, pt1.y, pt2.x, pt2.y, pt3.x, pt3.y)


    def __str__(self):
        return ("["  + str(self.pt1) + ", " +  str(self.pt2) + ", " +
                str(self.pt3) + "]")

    def __repr__(self):
        return ("Triangle(" +  str(self.pt1.x) +  ", " +  str(self.pt1.y) +
                ", " +  str(self.pt2.x) +  ", " +  str(self.pt2.y) + ", " +
                str(self.pt3.x) + ", " + str(self.pt3.y) + ")")

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("That's not a triangle!")
        return (set((self.pt1, self.pt2, self.pt3)) ==
               set((other.pt1, other.pt2, other.pt3)))

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

    def make4(self):
        points = [self.pt1, self.pt2, self.pt3]
        centers = []
        triangles = []

        for idx, point in enumerate(points):
            neighbor = points[(idx+1)%3]
            center = Point((point.x+neighbor.x)/2.0,
                           (point.y+neighbor.y)/2.0)
            centers += [center]


        for idx, point in enumerate(centers):
            neighbor = centers[(idx+1)%3]
            triangles += [Triangle.from_points(
                                   point, points[(idx+1)%3], neighbor)]
        triangles += [Triangle.from_points(*centers)]
        return triangles


class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.t1 = Triangle(0, 0, 1, 0, 0, 1)
        self.t2 = Triangle(0, 0, 2, 2, 4, 5)
        self.t3 = Triangle(0, 0, 5, 4, 3, 8)
        self.t4 = Triangle(-2, 0, 2, 0, 4, 4)
        self.t5 = Triangle(-8, -3, 0, 0, 5, 0)
        self.t6 = Triangle(-5, -5, 5, 5, 2.5, -2.5)
        self.t7 = Triangle(2.25, 3.15, 4.25, 10.25, -2.0, -12.5)
        self.t8 = Triangle(-2, 0, 0, 4, 2, 0)

    def test_str(self):
        self.assertEqual(str(self.t1), "[(0, 0), (1, 0), (0, 1)]")
        self.assertEqual(str(self.t2), "[(0, 0), (2, 2), (4, 5)]")
        self.assertEqual(str(self.t3), "[(0, 0), (5, 4), (3, 8)]")
        self.assertEqual(str(self.t4), "[(-2, 0), (2, 0), (4, 4)]")

    def test_repr(self):
        self.assertEqual(repr(self.t1), "Triangle(0, 0, 1, 0, 0, 1)")
        self.assertEqual(repr(self.t2), "Triangle(0, 0, 2, 2, 4, 5)")
        self.assertEqual(repr(self.t3), "Triangle(0, 0, 5, 4, 3, 8)")
        self.assertEqual(repr(self.t4), "Triangle(-2, 0, 2, 0, 4, 4)")

    def test_equals(self):
        self.assertTrue(self.t1 == self.t1)
        self.assertTrue(self.t2 == self.t2)
        self.assertTrue(self.t3 == Triangle(0, 0, 5, 4, 3, 8))
        self.assertTrue(self.t4 == Triangle(2, 0, -2, 0, 4, 4))
        self.assertFalse(self.t1 == self.t2)
        self.assertFalse(self.t5 == Triangle(-5, -5, -4, -4, 0, 1))
        with self.assertRaises(ValueError):
            self.t1 == "Rower"
        with self.assertRaises(ValueError):
            self.t5 == [1, 2]


    def test_not_equals(self):
        self.assertFalse(self.t1 != self.t1)
        self.assertFalse(self.t2 != self.t2)
        self.assertFalse(self.t3 != Triangle(0, 0, 5, 4, 3, 8))
        self.assertFalse(self.t4 != Triangle(2, 0, -2, 0, 4, 4))
        self.assertTrue(self.t1 != self.t2)
        self.assertTrue(self.t5 != Triangle(-5, -5, -4, -4, 0, 1))

    def test_center(self):
        self.assertEqual(self.t1.center(), Point(1.0/3.0, 1.0/3.0))
        self.assertEqual(self.t4.center(), Point(4.0/3.0, 4.0/3.0))
        self.assertEqual(self.t5.center(), Point(-1, -1))

    def test_area(self):
        self.assertEqual(self.t1.area(), 0.5)
        self.assertEqual(self.t3.area(), 14)
        self.assertEqual(self.t4.area(), 8)
        self.assertEqual(self.t6.area(), 25)

    def test_move(self):
        self.t1.move(3, 3)
        self.assertEqual(self.t1, Triangle(3, 3, 4, 3, 3, 4))
        self.t2.move(6, -1)
        self.assertEqual(self.t2, Triangle(6, -1, 8, 1, 10, 4))
        self.t7.move(8.5, 0)
        self.assertEqual(self.t7, Triangle(10.75, 3.15, 12.75, 10.25, 6.5, -12.5))
        with self.assertRaises(ValueError):
            self.t7.move("Rower", 2)
        with self.assertRaises(ValueError):
            self.t2.move([1, 2], (5, 8))

    def test_make4(self):
        s1 = set([Triangle(-1, 2, 0, 4, 1, 2),
                  Triangle(1, 2, 2, 0, 0, 0),
                  Triangle(0, 0, -2, 0, -1, 2),
                  Triangle(-1, 2, 1, 2, 0, 0)])
        s2 = set([Triangle(0, 0, 5, 5, 3.75, 1.25),
                  Triangle(-1.25, -3.75,  0, 0, -5, -5),
                  Triangle(-1.25, -3.75, 3.75, 1.25, 0, 0),
                  Triangle(2.5, -2.5, -1.25, -3.75, 3.75, 1.25)])
        self.assertEqual(set(self.t8.make4()), s1)
        self.assertEqual(set(self.t6.make4()), s2)




    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()



