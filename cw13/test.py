# knightstour.py
#
# created by: M. Peele
# section: 01
#
# This program implements a brute-force solution for the Knight's tour problem
# using a recursive backtracking algorithm. The Knight's tour is a chessboard
# puzzle in which the objective is to find a sequence of moves by the knight in
# which it visits every square on the board exactly one. It uses a 6x6 array for
# the chessboard where each square is identified by a row and column index, the
# range of which both start at 0. Let the upper-left square of the board be the
# row 0 and column 0 square.
#
# Imports the necessary modules.
 
# Initializes the chessboard as a 6x6 array.
chessBoard = [[None for i in range(6)] for j in range(6)]
 
# Gets the input start position for the knight from the user.
row = int(input("Enter the row: "))
col = int(input("Enter the column: "))
 
# Main driver function which starts the recursion.
def main():
    knightsTour(row, col, 1)
 
# Recursive function that solves the Knight's Tour problem.    
def knightsTour(row, col, move):
    # Checks if the given index is in range of the array and is legal.
    if _inRange(row, col) and _isLegal(row, col):
        chessBoard[row][col] = move # Sets a knight-marker at the given index.
        # If the chessBoard is full, returns True and the solved board.
        if _isFull(chessBoard):
            return True, _draw(chessBoard)    
 
        # Checks to see if the knight can make another move. If so, makes that
        # move by calling the function again.
        possibleOffsets = ((-2, -1), (-2, 1), (-1, 2), (1, 2), \
                           (2, 1), (2, -1), (1, -2), (-1, -2))
        for offset in possibleOffsets:
            if knightsTour(row + offset[0], col + offset[1], move + 1):
                return True
        # If the loop terminates, no possible move can be made. Removes the
        # knight-marker at the given index.
        chessBoard[row][col] = None
        return False
    else:
        return False
 
# Determines if the given row, col index is a legal move.
def _isLegal(row, col):
    if _inRange(row, col) and chessBoard[row][col] == None:
        return True
    else:
        return False
 
# Determines if the given row, col index is in range.
def _inRange(row, col):
    return row >= 0 and row < len(chessBoard) and col >= 0 and col < len(chessBoard[0])
 
# A solution was found if the array is full, meaning that every element in the
# array is filled with a number saying the knight has visited there.
def _isFull(chessBoard):
    for row in chessBoard:
        for col in row:
            if col is None:
                return False
    return True
 
# Draws a pictoral representation of the array.
def _draw(chessBoard):
    for row in chessBoard:
        for col in row:
            print("%4s" % col, end = " ")
        print()
 
# Calls the main function.
main()
