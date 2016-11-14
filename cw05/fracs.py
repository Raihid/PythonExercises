#!/usr/bin/python
from fractions import gcd

def same_denom(frac1, frac2): 
    print(frac1, frac2)
    denom = abs(frac1[1]*frac2[1])/gcd(frac1[1], frac2[1])
    fracs = [frac1, frac2]
    for i,f in enumerate(fracs):
        multiplier = denom/f[1]
        fracs[i][0] *= multiplier
        fracs[i][1] = denom
    return fracs

def add_frac(frac1, frac2):         # frac1 + frac2
    fracs = same_denom(frac1, frac2)
    return simplify([fracs[0][0] + fracs[1][0], fracs[0][1]])

def sub_frac(frac1, frac2):         # frac1 - frac2
    fracs = same_denom(frac1, frac2)
    return simplify([fracs[0][0] - fracs[1][0], fracs[0][1]])

def mul_frac(frac1, frac2):         # frac1 * frac2
    return simplify([frac1[0] * frac2[0], frac1[1] * frac2[1]])

def div_frac(frac1, frac2):         # frac1 / frac2
    if(is_zero(frac2)):
        raise ZeroDivisionError
    return simplify([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_positive(frac):              # bool, czy dodatni
    return (frac[0]*frac[1]) > 0 

def is_zero(frac):                  # bool, typu [0, x]
    if(frac[1] == 0):
        raise ZeroDivisionError
    return (frac[0] == 0)

def simplify(frac):
    
    denom = gcd(frac[0], frac[1])
    frac[0] = frac[0] / denom
    frac[1] = frac[1] / denom
    return frac;

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    fracs = same_denom(frac1, frac2)
    return (fracs[0][0] > fracs[1][0]) - (fracs[0][0] < fracs[1][0])

def frac2float(frac):               # konwersja do float
    return float(frac[0])/float(frac[1])

f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznaczno)
f5 = [0, 2]                   # zero (niejednoznaczno)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        # self.assertEqual(add_frac([1, -2], [1, 3]), [-1, 6])
        self.assertEqual(add_frac([1, -2], [1,3]), [-1,6])
        self.assertEqual(add_frac([1, 9], [2, 9]), [1,3])
        self.assertEqual(add_frac([2, 3], [-4, 18]), [4,9])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([1, 2], [1,3]), [1,6])
        self.assertEqual(sub_frac([100, 1], [1, 2]), [199,2])
        self.assertEqual(sub_frac([5, 2], [-3, 4]), [13,4])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1,3]), [1,6])
        self.assertEqual(mul_frac([9, 10], [1,2]), [9,20])
        self.assertEqual(mul_frac([2, 5], [4, 10]), [4,25])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1,3]), [3,2])
        self.assertEqual(div_frac([9, 10], [1,2]), [9,5])
        self.assertEqual(div_frac([2, 5], [4, 10]), [1,1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertTrue(is_positive([1, 100]))
        self.assertFalse(is_positive(self.zero))
        self.assertFalse(is_positive([5, -2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 2]))
        self.assertTrue(is_zero([0, -100]))
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero([-2,1]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, 2], [1, 4]), 1)
        self.assertEqual(cmp_frac([-1, 3], [9, 5]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([19, 20]), 0.95)
    
    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
