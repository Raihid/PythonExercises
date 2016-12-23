#!/usr/bin/python
"""
Exercises 13.4 and 13.5

This is a solution for finding all possible sudoku arrangements for boards
of any dimension. Unfortunately for bigger boards number of possible
arrangements is really big. There is no problem for 4x4 board, since there is
only 288 solutions for that size, but for board of size 6x6 (36 cells) there
are 28200960 solutions[1]. It would take a lot of time and space to name
them all. The sample containing 1000 6x6 solutions takes abount 90kb of space
which means that all  28200960 solutions would take about 200mb of space
([1] https://en.wikipedia.org/wiki/Mathematics_of_Sudoku#Enumeration_results)
"""


class SudokuFinder:
    def __init__(self, N, width, height):
        self.N = N
        self.block_width = width
        self.block_height = height
        self.board = {}
        self.solutions = []
        for i in range(self.N):
            for j in range(self.N):
                self.board[i, j] = 0

    def __str__(self):
        board_str = ""
        for solution in self.solutions:
            for i in range(self.N):
                board_str += " ".join(str(solution[i, j])
                                      for j in range(self.N))
                board_str += "\n"
            board_str += "-" * (2 * self.N - 1) + "\n"
        return board_str

    def empty(self, x, y):
        return self.board[x, y] == 0

    def in_row(self, x, y, value):
        return any(self.board[x, i] == value for i in range(self.N))

    def in_col(self, x, y, value):
        return any(self.board[i, y] == value for i in range(self.N))

    def in_block(self, x, y, value):
        block_x = self.block_height * int(x / self.block_height)
        block_y = self.block_width * int(y / self.block_width)
        for i in range(block_x, block_x + self.block_height):
            for j in range(block_y, block_y + self.block_width):
                if self.board[i, j] == value:
                    return True
        return False

    def is_valid(self, cell, val):
        x, y = cell[0], cell[1]
        return (self.empty(x, y) and not self.in_block(x, y, val)
                and not self.in_row(x, y, val) and not self.in_col(x, y, val))

    def try_solving(self, start_limit, steps):
        num = int(steps / self.N) + 1
        next_num = int((steps + 1) / self.N) + 1
        for index in range(start_limit, self.N * self.N):
            cell = (index / self.N, index % self.N)
            if self.is_valid(cell, num):
                self.board[cell] = num
                if steps == self.N * self.N - 1:
                    self.solutions += [{key: val for key, val in
                                       self.board.items()}]
                    size = len(self.solutions)
                    if size % 100 == 0:
                        print("We're at {} solutions".format(size))
                else:
                    new_limit = (index if next_num == num else 0)
                    self.try_solving(new_limit, steps + 1)
                self.board[cell] = 0


sf = SudokuFinder(6, 2, 3)
sf.try_solving(0, 0)
print(sf)
print("Found {} solutions".format(len(sf.solutions)))
