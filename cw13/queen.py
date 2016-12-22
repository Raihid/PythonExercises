#!/usr/bin/python
# Exercise 13.2


class QueenProblem:

    def __init__(self, N):
        self.N = N
        self.x = N * [None]
        self.a = N * [True]
        self.b = (2*N-1) * [True]
        self.c = (2*N-1) * [True]
        self.solutions = []

    def __str__(self):
        str_board = ""
        for solution in self.solutions:
            for w in range(self.N):
                for k in range(self.N):
                    if solution[k] == w:
                        str_board += "H"
                    else:
                        str_board += "."
                    str_board += " "
                str_board += "\n"
            str_board += "--" * self.N + "\n"
        return str_board

    def is_valid(self, w, k):
        return self.a[w] and self.b[w+k] and self.c[w-k]

    def save(self, w, k):
        self.x[k] = w
        self.a[w] = False
        self.b[w+k] = False
        self.c[w-k] = False

    def erase(self, w, k):
        self.a[w] = True
        self.b[w+k] = True
        self.c[w-k] = True

    def try_solving(self, k):
        success = False
        w = 0                 # numbers from 0 to N-1
        while w < self.N:
            if self.is_valid(w, k):
                self.save(w, k)
                if k < (self.N-1):
                    success = self.try_solving(k+1)
                else:
                    success = True
                    self.solutions += [self.x]
                self.erase(w, k)

            w = w + 1
        return success


qp = QueenProblem(8)
qp.try_solving(0)
print(qp)
