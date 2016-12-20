#!/usr/bin/python


board = {}
N = 6
BLOCK_WIDTH = 2
BLOCK_HEIGHT = 3

def empty(x, y):
    return board[x, y] == 0

def in_row(x, y, value):
    return any(board[x, i] == value for i in range(N))

def in_col(x, y, value):
    return any(board[i, y] == value for i in range(N))

def in_block(x, y, value):
    block_x = int(x/BLOCK_WIDTH)
    block_y = int(y/BLOCK_HEIGHT)
    for i in range(block_x, block_x + BLOCK_WIDTH):
        for j in range(block_y, block_y + BLOCK_HEIGHT):
            if board[i, j] == value:
                return True
    return False


def is_valid(x, y, val):
    return (empty(x, y) and not in_block(x, y, val) 
            and not in_row(x, y, val) and not in_col(x, y, val))
    

def print_board(board):
    board_str = ""
    for i in range(N):
        for j in range(N):
            board_str += str(board[i, j]) + " "
        board_str += "\n"
    board_str += "--" * N + "\n" 
    print(board_str)

solutions = []
def try_placing_number(step, num): # TODO: nic nie dziala
    placed = []

        good = False
        for i in range(N):
            for j in range(N):
                if is_valid(i, j, num):
                    placed += [(i, j)]
                    board[i, j] = num
                    good = True
        if good == False:
            for place in placed:
                board[place] = 0
            return False
    return placed

            

def try_solving(num):
    global solutions

    placed = try_placing_number(num)
    if placed is not False:
        if num == N:
            solutions += [board]
        else:
            try_solving(num + 1)
        for place in placed:
            board[place] = 0


for i in range(N):
    for j in range(N):
        board[i, j] = 0
try_solving(1)
print(solutions)
