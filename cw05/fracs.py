from fractions import gcd

def same_denom(frac1, frac2): # TODO znak
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
    return [fracs[0][0] + fracs[1][0], fracs[0][1]]

def sub_frac(frac1, frac2):         # frac1 - frac2
    
    fracs = same_denom(frac1, frac2)
    return [fracs[0][0] - fracs[1][0], fracs[0][1]]

def mul_frac(frac1, frac2):         # frac1 * frac2
    return [frac1[0] * frac2[0], frac1[1] * frac2[1]]

def div_frac(frac1, frac2):         # frac1 / frac2
    return [frac1[0] * frac2[1], frac1[1] * frac2[0]]

def is_positive(frac):              # bool, czy dodatni
    return (frac[0]*frac[1]) > 0 

def is_zero(frac):                  # bool, typu [0, x]
    if(frac[1] == 0):
        print("ojojoj")
        # booom
    return (frac[0] == 0)

def cmp_frac(frac1, frac2):         # -1 | 0 | +1
    fracs = same_denom(frac1, frac2)
    return (fracs[0][0] > fracs[1][0]) - (fracs[0][0] < fracs[1][0]) # (a > b) - (a < b)

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
        self.assertEqual(add_frac([1, -2], [1, 3]), [-1, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(f4, f5), f4)

    def test_mul_frac(self): pass

    def test_div_frac(self): pass

    def test_is_positive(self): pass

    def test_is_zero(self): pass

    def test_cmp_frac(self): pass

    def test_frac2float(self): pass

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
