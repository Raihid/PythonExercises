#!/usr/bin/python
from math import pi
from points import Point

class Circle:
    """A class representing circles on a plane"""

    def __init__(self, x=0, y=0, radius=1):
        if radius < 0:
            raise ValueError("promien ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle(" + str(self.x) + ", " + str(self.y) + ", " + str(radius) + ")"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):           # pole powierzchni
        return pi*radius*radius

    def move(self, x, y):     # przesuniecie o (x, y)
        self.x += x
        self.y += y
        
    def cover(self, other):   # todo: solid check
        left = min(self.x - radius, other.x - radius)
        bottom = min(self.y - radius,other.y - radius)
        right = max(self.x + radius, other.x + radius)
        top = max(self.y + radius, other.y + radius)
        center = Point((right - left)/2, (top - bottom)/2)
        radius = max(center - left, center - bottom)
        return Point(center.x, center.y, radius)
        


# Kod testujacy modul.

import unittest

class TestCircle(unittest.TestCase):

    def setUp: pass
    def test_repr: pass
    def test_str: pass
    def test_equals: pass
    def test_not_equals: pass
    def test_area: pass
    def test_move: pass
    def test_cover: pass
    def tearDown: pass
