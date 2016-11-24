#!/usr/bin/python
import itertools

class Poly:
    def __init__(self, c=0, n=0):
        self.size = n +1
        self.a = self.size * [0]
        self.a[self.size-1] = c

    @staticmethod
    def from_list(L):
        tmp = Poly()
        tmp.a = L
        while len(tmp.a) > 1 and tmp.a[-1] == 0:
            tmp.a.pop()
        tmp.size = len(tmp.a)
        return tmp

    def add_list(self, L1, L2):        # L1(x) + L2(x)
        return [x+y for x,y in
                itertools.izip_longest(L1, L2, fillvalue=0)]

    def sub_list(self, L1, L2):        # L1(x) - L2(x)
        return [x-y for x,y in
                itertools.izip_longest(L1, L2, fillvalue=0)]

    def mul_list(self, L1, L2):        # L1(x) * L2(x)
        out_list = [0] * (len(L1)+len(L2))
        for i in range(0, len(L1)):
            for j in range(0, len(L2)):
                out_list[i+j] = out_list[i+j] + (L1[i] * L2[j])
        while len(out_list) > 1 and out_list[-1] == 0:
            out_list.pop()
        return out_list

    def cmp_list(self, L1, L2):        # bool, compare
        while len(L1) > 1 and L1[-1] == 0:
           L1.pop()
        while len(L2) > 1 and L2[-1] == 0:
           L2.pop()
        if(len(L1) != len(L2)):
            return False
        return all(x == y for x,y in zip(L1,L2))

    def eval_list(self, L, x0):           # L(x0), Horner
        result = L[-1]
        for i in reversed(range(0, len(L)-1)):
            result = result*x0 + L[i]
        return result

    def combine_list(self, L1, L2):    # L1(L2(x)), hard!
        out_list = [0] * len(L1) * len(L2)
        for i in range(0, len(L1)):
            temp = self.pow_list(L2, i)
            temp = self.mul_list([L1[i]], temp)
            out_list = self.add_list(out_list, temp)
        while len(out_list) > 1 and out_list[-1] == 0:
            out_list.pop()
        return out_list

    def pow_list(self, L, n):             # L(x) ** n
        result = [1]
        for i in range(0, n):
            result = self.mul_list(result, L)
        return result

    def diff_list(self, L):               # derivative of polynomial
        L[0] = 0
        for i in range(1, len(L)):
            L[i-1] = L[i]*i
            L[i] = 0
        while len(L) > 1 and L[-1] == 0:
            L.pop()
        return L

    def integrate_list(self, L):
        size = len(L)
        out_list = [0] * size+1
        for i in reversed(range(0,len(L))):
            out_list[i+1] = L[i]/(i+1)
        while len(out_list) > 1 and out_list[-1] == 0:
            out_list.pop()
        return out_list

    def __str__(self):
        return str(self.a)

    def __add__(self, other): # self + other
        return Poly.from_list(self.add_list(self.a, other.a))

    def __sub__(self, other):  # self - other
        return Poly.from_list(self.sub_list(self.a, other.a))

    def __mul__(self, other):  # self * other
        return Poly.from_list(self.mul_list(self.a, other.a))

    def __pos__(self):         # +poly1 = (+1)*poly1
        return self

    def __neg__(self):         # -poly1 = (-1)*poly1
        return Poly.from_list([-e for e in self.a])

    def __eq__(self, other):   # poly1 == poly2
        return self.cmp_list(self.a, other.a)

    def __ne__(self, other):        # poly1 != poly2
        return not self == other

    def eval(self, x):         # schemat Hornera
        return self.eval_list(self.a, x)

    def combine(self, other):       # poly1(poly2(x))
        return Poly.from_list(self.combine_list(self.a, other.a))

    def __pow__(self, n):      # poly(x)**n or pow(poly(x),n)
        return Poly.from_list(self.pow_list(self.a, n))

    def diff(self):            # differential
        return Poly.from_list(self.diff_list(self.a))

    def integrate(self):       # integral
        return Poly.from_list(self.integrate_list(self.a))

    def is_zero(self):         # bool, True for [0], [0, 0],...
        return all(k == 0 for k in self.a)

p1 = [2, 1]                   # W(x) = 2 + x
p2 = [-3, 0, 1]               # W(x) = -3 + x**2
p3 = [3]                      # W(x) = 3, wielomian zerowego stopnia
p4 = [0]                      # zero
p5 = [0, 0, 0]                # zero
p6 = [1,2,3]
p7 = [4,5,6]


import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = Poly.from_list([2, 1])                   # W(x) = 2 + x
        self.p2 = Poly.from_list([-3, 0, 1])               # W(x) = -3 + x**2
        self.p3 = Poly.from_list([3])                      # W(x) = 3, wielomian zerowego stopnia
        self.p4 = Poly.from_list([0])                      # zero
        self.p5 = Poly.from_list([0, 0, 0])                # zero (nie
        self.p6 = Poly.from_list([1,2,3])
        self.p7 = Poly.from_list([4,5,6])

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Poly.from_list([-1, 1, 1]))
        self.assertEqual(self.p3 + self.p4, Poly.from_list([3]))
        self.assertEqual(self.p6 + self.p7, Poly.from_list([5, 7, 9]))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Poly.from_list([5, 1, -1]))
        self.assertEqual(self.p3 - self.p4, Poly.from_list([3]))
        self.assertEqual(self.p6 - self.p7, Poly.from_list([-3, -3, -3]))

    def test_mul(self):
        self.assertEqual(self.p7 * self.p7, Poly.from_list([16, 40, 73, 60, 36]))
        self.assertEqual(self.p1 * self.p2, Poly.from_list([-6, -3, 2, 1]))
        self.assertEqual(self.p3 * self.p4, Poly.from_list([0]))

    def test_is_zero(self):
        self.assertTrue(self.p4.is_zero())
        self.assertTrue(self.p5.is_zero())
        self.assertFalse(self.p6.is_zero())

    def test_cmp(self):
        self.assertTrue(self.p4 == self.p4)
        self.assertTrue(self.p4 == self.p5)
        self.assertFalse(self.p2 == self.p7)

    def test_eval(self):
        self.assertEqual(Poly.eval(self.p4, 10), 0)
        self.assertEqual(Poly.eval(self.p7, 0), 4)
        self.assertEqual(Poly.eval(self.p2, 2), 1)

    def test_combine(self):
        self.assertEqual(Poly.combine(self.p6, self.p7), Poly.from_list([57, 130, 231, 180, 108]))
        self.assertEqual(Poly.combine(self.p7, self.p4), Poly.from_list([4]))

    def test_pow(self):
        self.assertEqual(self.p4 ** 2, Poly.from_list([0]))
        self.assertEqual(self.p7 ** 2, Poly.from_list([16, 40, 73, 60, 36]))

    def test_diff(self):
        self.assertEqual(Poly.diff(self.p7), Poly.from_list([5, 12]))
        self.assertEqual(Poly.diff(self.p1), Poly.from_list([1]))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

