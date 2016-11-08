import itertools

def add_poly(poly1, poly2):        # poly1(x) + poly2(x)
    return [x+y for x,y in 
            itertools.izip_longest(poly1, poly2, fillvalue=0)]

def sub_poly(poly1, poly2):        # poly1(x) - poly2(x)
    return [x-y for x,y in
            itertools.izip_longest(poly1, poly2, fillvalue=0)]

def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    out_poly = [0] * (len(poly1)+len(poly2))
    for i in range(0, len(poly1)):
        for j in range(0, len(poly2)):
            out_poly[i+j] = out_poly[i+j] + poly1[i] * poly2[j]
    while len(out_poly) > 1 and out_poly[-1] == 0:
        out_poly.pop()
    return out_poly;
        

def is_zero(poly):                 # bool, [0], [0,0], itp.
    return all(k == 0 for k in poly)

def cmp_poly(poly1, poly2):        # bool, porownywanie
    while len(poly1) > 1 and poly1[-1] == 0:
       poly1.pop() 
    while len(poly2) > 1 and poly2[-1] == 0:
       poly2.pop() 
    if(len(poly1) != len(poly2)):
        return false
    for i in range(0, len(poly1)):
        if poly1[i] != poly2[i]:
            return False
    return True

def eval_poly(poly, x0):           # poly(x0), algorytm Hornera
    result = poly[-1]
    for i in reversed(range(0, len(poly)-1)):
        result = result*x0 + poly[i]
    return result

def combine_poly(poly1, poly2):    # poly1(poly2(x)), trudne!
    out_poly = [0] * len(poly1) * len(poly2)
    for i in range(0, len(poly1)):
        temp = pow_poly(poly2, i)
        temp = mul_poly([poly1[i]], temp)
        out_poly = add_poly(out_poly, temp)
    while len(out_poly) > 1 and out_poly[-1] == 0:
        out_poly.pop()
    return out_poly

def pow_poly(poly, n):             # poly(x) ** n
    result = [1]
    for i in range(0, n):
        result = mul_poly(result, poly)
    return result

def diff_poly(poly):               # pochodna wielomianu
    poly[0] = 0
    for i in range(1, len(poly)):
        poly[i-1] = poly[i]*i
        poly[i] = 0 
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly

p1 = [2, 1]                   # W(x) = 2 + x
p2 = [-3, 0, 1]               # W(x) = -3 + x**2
p3 = [3]                      # W(x) = 3, wielomian zerowego stopnia
p4 = [0]                      # zero
p5 = [0, 0, 0]                # zero (nie
p6 = [1,2,3]
p7 = [4,5,6]


import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [2, 1]                   # W(x) = 2 + x
        self.p2 = [-3, 0, 1]               # W(x) = -3 + x**2
        self.p3 = [3]                      # W(x) = 3, wielomian zerowego stopnia
        self.p4 = [0]                      # zero
        self.p5 = [0, 0, 0]                # zero (nie
        self.p6 = [1,2,3]
        self.p7 = [4,5,6]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [-1, 1, 1])
        self.assertEqual(add_poly(self.p3, self.p4), [3])
        self.assertEqual(add_poly(self.p6, self.p7), [5, 7, 9])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [5, 1, -1])
        self.assertEqual(sub_poly(self.p3, self.p4), [3])
        self.assertEqual(sub_poly(self.p6, self.p7), [-3, -3, -3])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p7, self.p7), [16, 40, 73, 60, 36])
        self.assertEqual(mul_poly(self.p1, self.p2), [-6, -3, 2, 1])
        self.assertEqual(mul_poly(self.p3, self.p4), [0])

    def test_is_zero(self):
        self.assertTrue(is_zero(self.p4))
        self.assertTrue(is_zero(self.p5))
        self.assertFalse(is_zero(self.p6))

    def test_cmp_poly(self):
        self.assertTrue(cmp_poly(self.p4, self.p4))
        self.assertTrue(cmp_poly(self.p4, self.p5))
        self.assertFalse(cmp_poly(self.p2, self.p7))
        
    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p4, 10), 0)
        self.assertEqual(eval_poly(self.p7, 0), 4)
        self.assertEqual(eval_poly(self.p2, 2), 1)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p6, p7), [57, 130, 231, 180, 108])
        self.assertEqual(combine_poly(self.p7, p4), [4])

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p4, 2), [0])
        self.assertEqual(pow_poly(self.p7, 2), [16, 40, 73, 60, 36])

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p7), [5, 12])
        self.assertEqual(diff_poly(self.p1), [1])

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

