from points import Point
import unittest


class Rectangle:
    """Class representing a rectangle on a plane
       Assumptions: pt1 < pt2 (x1 < x2 and y1 < y2)
       pt1 is bottom-left corner, pt2 is top-right corner 
    """

    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):         
        return "["  + str(self.pt1) + ", " +  str(self.pt2) +  "]"

    def __repr__(self):        
        return "Rectangle(" +  str(self.pt1.x) +  ", " +  str(self.pt1.y) + \
                ", " +  str(self.pt2.x) +  ", " +  str(self.pt2.y) +  ")"

    def __eq__(self, other):   
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):        
        return not self == other

    def center(self):          
        return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

    def area(self):            
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):      
        self.pt1 += Point(x, y)
        self.pt2 += Point(x, y)

class TestRectangle(unittest.TestCase): 

    def setUp(self):
        self.r1 = Rectangle(0, 0, 0, 0)
        self.r2 = Rectangle(0, 0, 2, 2)
        self.r3 = Rectangle(1, 1, 4.5, 4.5)
        self.r4 = Rectangle(-2, 0, 4, 4)
        self.r5 = Rectangle(-8, -4, 0, 0)
        self.r6 = Rectangle(-5, -5, 5, 5)
        self.r7 = Rectangle(2.25, 3.15, 8.5, 10.25)

    def test_str(self): 
        self.assertEqual(str(self.r1), "[(0, 0), (0, 0)]")
        self.assertEqual(str(self.r2), "[(0, 0), (2, 2)]")
        self.assertEqual(str(self.r3), "[(1, 1), (4.5, 4.5)]")
        self.assertEqual(str(self.r4), "[(-2, 0), (4, 4)]")

    def test_repr(self): 
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 0, 0)")
        self.assertEqual(repr(self.r2), "Rectangle(0, 0, 2, 2)")
        self.assertEqual(repr(self.r3), "Rectangle(1, 1, 4.5, 4.5)")
        self.assertEqual(repr(self.r4), "Rectangle(-2, 0, 4, 4)")

    def test_equals(self): 
        self.assertTrue(self.r1 == self.r1)
        self.assertTrue(self.r2 == self.r2)
        self.assertTrue(self.r3 == Rectangle(1, 1, 4.5, 4.5))
        self.assertFalse(self.r1 == self.r2)
        self.assertFalse(self.r5 == Rectangle(-5, -5, -4, -4))

    def test_not_equals(self): 
        self.assertFalse(self.r1 != self.r1)
        self.assertFalse(self.r2 != self.r2)
        self.assertFalse(self.r3 != Rectangle(1, 1, 4.5, 4.5))
        self.assertTrue(self.r1 != self.r2)
        self.assertTrue(self.r5 != Rectangle(-5, -5, -4, -4))

    def test_center(self): 
        self.assertEqual(self.r1.center(), Point(0, 0))
        self.assertEqual(self.r4.center(), Point(1, 2))
        self.assertEqual(self.r5.center(), Point(-4, -2))
        self.assertEqual(self.r6.center(), Point(0, 0))

    def test_area(self): 
        self.assertEqual(self.r1.area(), 0)
        self.assertEqual(self.r2.area(), 4)
        self.assertEqual(self.r4.area(), 24)
        self.assertEqual(self.r7.area(), 44.375)

    def test_move(self): 
        self.r1.move(3, 3)
        self.assertTrue(self.r1 == Rectangle(3, 3, 3, 3))
        self.r2.move(6, -1)
        self.assertTrue(self.r2 == Rectangle(6, -1, 8, 1))
        self.r7.move(8.5, 0)
        self.assertTrue(self.r7 == Rectangle(10.75, 3.15, 17, 10.25))
    
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()



