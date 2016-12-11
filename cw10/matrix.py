#!/usr/bin/python


# Exercise 10.1
class Matrix:

    def __init__(self, rows=1, cols=1):
        self.rows = rows
        self.cols = cols
        self.data = [0] * rows * cols

    def __str__(self):
        out = "["
        for row in range(0, self.rows):
            out += str(self.data[row*self.cols:(row+1)*(self.cols)])
        out += "]"
        return out

    def __getitem__(self, pair):   # odczyt m[i,j]
        i, j = pair
        return self.data[i * self.cols + j]

    def __setitem__(self, pair, value):   # m[i,j] = value
        i, j = pair
        self.data[i * self.cols + j] = value

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Not a matrix!")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Number of rows and cols is not equal!")
        result_matrix = Matrix(self.rows, self.cols)
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                result_matrix[row, col] = self[row, col] + other[row, col]
        return result_matrix

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Not a matrix!")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Number of rows and cols is not equal!")
        result_matrix = Matrix(self.rows, self.cols)
        for row in range(0, self.rows):
            for col in range(0, self.cols):
                result_matrix[row, col] = self[row, col] - other[row, col]
        return result_matrix

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Not a matrix!")
        if self.cols != other.rows:
            raise ValueError("Wrong matrix dimensions!")
        result_matrix = Matrix(self.rows, other.cols)
        for row in range(0, self.rows):
            for col in range(0, other.cols):
                result_matrix[row, col] = sum(self[row, k] * other[k, col]
                                              for k in range(0, self.cols))
        return result_matrix

m = Matrix(3, 4)
m[0, 0] = 1
m[1, 1] = 2
m[2, 2] = 3

n = Matrix(4, 2)
n[0, 0] = 8
n[0, 1] = 5
n[1, 0] = 3

print(m*n)
