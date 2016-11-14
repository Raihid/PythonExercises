#!/usr/bin/python

def add_sparse(sparse1, sparse2):       # sparse1 + sparse2
    out_sparse = dict(sparse1)
    for index, value in sparse2.items():
        if(out_sparse.has_key(index)):
            out_sparse[index] += value;
        else:
            out_sparse[index] = value;
    return out_sparse


def sub_sparse(sparse1, sparse2):
    negative_sparse = {key: -value for key, value in sparse2.items()}
    return add_sparse(sparse1, negative_sparse)
    
def mul_sparse(sparse1, sparse2):    
    out_sparse = dict()
    for (row1, col1) in sparse1:
        for (row2, col2) in sparse2:
            if col1 == row2:
                out_sparse[row1, col2] = out_sparse.get((row1, col2), 0) + sparse1[row1, col1] * sparse2[row2, col2]
    return out_sparse


def is_diagonal(sparse):
    return all(key[0] == key[1] or value == 0 for key, value in sparse.items())
def is_empty(sparse):
    return all(value == 0 for key, value in sparse.items())


import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.s1 = {}
        self.s2 = {(2, 2) : 3, (5, 3) : 9 }
        self.s3 = {(0, 0) : 5, (1, 1) : 1, (2,2) : 3, (3,3) : 4, (4,4): 8, (5,5): 9}
        self.s4 = {(0, 0) : 5, (1, 1) : 1, (2,2) : 6, (3,3) : 4, (4,4): 8, (5,3): 9, (5,5): 9}
        self.s5 = {(0, 0) : -5, (1, 1) : -1, (2,2) : 0, (3,3) : -4, (4,4) : -8, (5,3) : 9, (5,5) : -9}
        self.s6 = {(0,0) : 1, (0,1) : 2, (1,0) : 2, (1,1) : 1}
        self.s7 = {(0,1) : 5, (1,0) : 8}
        self.s8 = {(0,0) : 16, (0,1) : 5, (1,0) : 8, (1,1): 10}
        self.s9 = {(0,0) : 1, (0,1) : 7, (1,0) : 10, (1,1) : 1}

    def test_add_sparse(self):       # sparse1 + sparse2
        self.assertEqual(add_sparse(self.s2, self.s3), self.s4)
        self.assertEqual(add_sparse(self.s6, self.s7), self.s9)  

    def test_sub_sparse(self):
        self.assertEqual(sub_sparse(self.s2, self.s3), self.s5)
        self.assertEqual(sub_sparse(self.s4, self.s1), self.s4)
    
    def test_mul_sparse(self):
        self.assertEqual(mul_sparse(self.s6, self.s7), self.s8) 
        self.assertEqual(mul_sparse(self.s1, self.s2), self.s1)
        
    def test_is_diagonal(self):
        self.assertTrue(is_diagonal(self.s3))
        self.assertFalse(is_diagonal(self.s2))

    def test_is_empty(self):
        self.assertTrue(is_empty(self.s1))
        self.assertFalse(is_empty(self.s2))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy

