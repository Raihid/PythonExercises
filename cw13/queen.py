#!/usr/bin/python


class QueenProblem:
    def __init__(self, N):
        self.N = N
        # x[i] to pozycja hetmana w kolumnie i
        self.x = N * [None]

        # a[j] == True to brak hetmana w wierszu j
        self.a = N * [True]

        # b[k] == True to brak hetmana na przekatnej k [/].
        # Suma wiersz+kolumna od 0 do (2N-2).
        self.b = (2*N-1) * [True]

        # c[k] == True to brak hetmana na przekatnej k [\].
        # Roznica wiersz-kolumna od (-N+1) do (N-1).
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



qp = QueenProblem(5)
qp.try_solving(0)
print(qp)
