import unittest
from math import sqrt
class Point:
    """Klasa reprezentujaca punkty na plaszczyznie."""

    def __init__(self, x=0, y=0):  
        self.x = x
        self.y = y

    def __str__(self):         
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):        
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):   
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        
        return not self == other

    def __add__(self, other):  
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  
        return self.x*other.x + self.y*other.y

    def cross(self, other):         
        return self.x * other.y - self.y * other.x

    def length(self):          
        return sqrt(self.x*self.x + self.y*self.y)




class TestPoint(unittest.TestCase):
   
    def setUp(self):
        self.p1 = Point(0, 0) 
        self.p2 = Point(2, 0) 
        self.p3 = Point(4.75, 4) 
        self.p4 = Point(3.25, -2)
        self.p5 = Point(8, 2)
        self.p6 = Point(11.25, 0) 
        self.p7 = Point(-2, -2) 
        self.p8 = Point(-4, 3.15) 
        self.p9 = Point(-6, 1.15)
        self.p10 = Point(2.75, 4)
        self.p11 = Point(4.75, 4)
        self.p12 = Point(-2, -2)
        self.p13 = Point(3, 4)

    def test_print(self):
        self.assertEqual(str(self.p1), "(0, 0)")
        self.assertEqual(str(self.p2), "(2, 0)") 
        self.assertEqual(str(self.p3), "(4.75, 4)") 
        self.assertEqual(str(self.p4), "(3.25, -2)")

    def test_repr(self):   
        self.assertEqual(repr(self.p1), "Point(0, 0)")
        self.assertEqual(repr(self.p2), "Point(2, 0)") 
        self.assertEqual(repr(self.p3), "Point(4.75, 4)") 
        self.assertEqual(repr(self.p4), "Point(3.25, -2)")

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, self.p2)
        self.assertEqual(self.p3 + self.p4, self.p5)
        self.assertEqual(self.p4 + self.p5, self.p6)
        self.assertEqual(self.p7 + self.p8, self.p9)

    def test_sub(self):
        self.assertEqual(self.p2 - self.p1, self.p2)
        self.assertEqual(self.p3 - self.p2, self.p10)
        self.assertEqual(self.p5 - self.p4, self.p11)
        self.assertEqual(self.p9 - self.p8, self.p12)

    def test_equals(self): 
        self.assertTrue(self.p2 == self.p2)
        self.assertTrue(self.p1 == self.p1)
        self.assertTrue(self.p3 == Point(4.75, 4))
        self.assertTrue(self.p4 == Point(3.25, -2))
        self.assertFalse(self.p4 == self.p5)
        self.assertFalse(self.p6 == Point(11, 0))
        
    def test_not_equals(self): 
        self.assertFalse(self.p2 != self.p2)
        self.assertFalse(self.p1 != self.p1)
        self.assertFalse(self.p3 != Point(4.75, 4))
        self.assertFalse(self.p4 != Point(3.25, -2))
        self.assertTrue(self.p4 != self.p5)
        self.assertTrue(self.p6 != Point(11, 0))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 0)
        self.assertEqual(self.p3 * self.p4, 7.4375)
        self.assertEqual(self.p5 * self.p6, 90)

    def test_cross(self): 
        self.assertEqual(self.p1.cross(self.p2), 0)
        self.assertEqual(self.p3.cross(self.p4), -22.5)
        self.assertEqual(self.p5.cross(self.p6), -22.5)

    def test_length(self):
        self.assertEqual(self.p1.length(), 0) 
        self.assertEqual(self.p2.length(), 2) 
        self.assertEqual(self.p6.length(), 11.25) 
        self.assertEqual(self.p13.length(), 5) 
    
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
