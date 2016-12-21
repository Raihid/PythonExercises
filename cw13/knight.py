#!/usr/bin/python


class KnightProblem:
    KNIGHT_MOVES = 8
    def __init__(self, x0, y0, N):
        self.N = N
        if x0 >= N or y0 >= N:
           raise ValueError("Starting position outside of board") 
        self.x0 = x0
        self.y0 = y0
        self.delta_x = [2, 1, -1, -2, -2, -1, 1, 2]  # delta x
        self.delta_y = [1, 2, 2, 1, -1, -2, -2, -1]  # delta y
        self.board = {}
        for i in range(N):
            for j in range(N):
                self.board[i, j] = 0
        self.board[x0, y0] = 1

    def print_board(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.board[i, j])


    def is_valid(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.board[x, y] == 0


    def try_moving(self, step, x, y):
        # step - nr of the next step to make
        # x, y - knight starting position
        # Returns boolean
        success = False
        candidate = 0
        while (not success) and (candidate < self.KNIGHT_MOVES):
            u = x + self.delta_x[candidate]         # choosing a candidate
            v = y + self.delta_y[candidate]
            if self.is_valid(u, v):
                self.board[u, v] = step
                if step < self.N * self.N:         # recursion end condition
                    success = self.try_moving(step + 1, u, v)
                    if not success:
                       self.board[u, v] = 0
                else:
                    success = True
            candidate = candidate + 1
        return success



for N in range(3, 7):
    solution_existence = []
    for i in range(N):
        solution_in_row = []
        for j in range(N):
            kp = KnightProblem(i, j, N)
            solution_in_row += [ kp.try_moving(2, i, j) ]
        solution_existence += solution_in_row
        print(solution_in_row)
